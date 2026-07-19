"""Tests for v1 blocker-fingerprint snapshot stamping (dispatch-retarget
design note, 2026-07-16, section 3b): the audit-verdict writer stamps a
complete blocker_fingerprint_v1 snapshot on every NEW conditional/failed
verdict write, so the shadow would-park comparator sees v1-complete rows
instead of fail-open legacy ones. Covers: stamped rows are v1-complete and
park under unchanged current state; every required-key omission fails
loudly in the comparator; stamp-then-mutate-one-channel un-parks with the
named reason; the writer itself fails loudly (and transactionally) on an
incomplete stamp; terminal/clean verdicts stay legacy-shaped (no backfill,
no scope creep); and byte-identical determinism across identical passes."""

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import apply_audit  # noqa: E402
import compute_audit_queue as caq  # noqa: E402
import invalidate_stale_audits as isa  # noqa: E402

NOTE_BODY = "# Fixture theorem note\n\nA small fixture claim.\n"
DEP_NOTE_BODY = "# Fixture dep note\n\nAn open upstream authority.\n"
RUNNER_BODY = "import sympy\nassert sympy.simplify(0) == 0\nprint('PASS=1')\n"
HELPER_BODY = "VALUE = 'helper'\n"
PROMPT_TEMPLATE_BODY = "# Audit agent prompt template (fixture)\n"
CLAIM_ID = "fixture_conditional_row"
NOTE_PATH = "docs/FIXTURE_CONDITIONAL_ROW.md"
RUNNER_PATH = "scripts/fixture_runner.py"
HELPER_PATH = "scripts/fixture_helper.py"
AXIOM_DEP = "fixture_axiom_dep"
OPEN_DEP = "fixture_open_dep"
AXIOM_HASH = hashlib.sha256(b"fixture axiom note").hexdigest()


def _audit_blob(verdict="audited_conditional", **overrides):
    blob = {
        "claim_id": CLAIM_ID,
        "verdict": verdict,
        "claim_type": "positive_theorem",
        "claim_scope": "fixture scope",
        "auditor": "fixture-auditor",
        "auditor_family": "codex-gpt-5.6",
        "auditor_model": "gpt-5.6-sol",
        "auditor_reasoning_effort": "xhigh",
        "independence": "cross_family",
        "load_bearing_step_class": "C",
        "load_bearing_step": "fixture step",
        "chain_closes": False,
        "chain_closure_explanation": "upstream dep not retained yet",
        "verdict_rationale": "conditional on the open upstream dep",
        "notes_for_re_audit_if_any": "await fixture_open_dep",
        "audit_date": "2026-07-16T00:00:00+00:00",
        "negative_assertion_classes": [],
    }
    blob.update(overrides)
    return blob


class StampFixture:
    """Minimal on-disk repo + in-memory ledger that drives the REAL verdict
    writer (apply_audit.apply_one) end to end, with all module paths
    redirected into a temp root (mirrors test_audit_pipeline conventions)."""

    def __init__(self, tmp: Path):
        self.tmp = tmp
        (tmp / "docs" / "audit" / "data").mkdir(parents=True)
        (tmp / "scripts").mkdir()
        self._write(NOTE_PATH, NOTE_BODY)
        self._write("docs/FIXTURE_OPEN_DEP.md", DEP_NOTE_BODY)
        self._write(RUNNER_PATH, RUNNER_BODY)
        self._write(HELPER_PATH, HELPER_BODY)
        self._write("docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md", PROMPT_TEMPLATE_BODY)
        self._write(
            "docs/audit/data/axiom_premise_nodes.json",
            json.dumps(
                {"schema_version": 1, "canonical_ids": [AXIOM_DEP]},
                indent=2, sort_keys=True,
            ) + "\n",
        )
        self.ledger = {
            "schema_version": 1,
            "rows": {
                CLAIM_ID: {
                    "claim_id": CLAIM_ID,
                    "note_path": NOTE_PATH,
                    "note_hash": hashlib.sha256(NOTE_BODY.encode()).hexdigest(),
                    "deps": [OPEN_DEP, AXIOM_DEP],
                    "audit_status": "unaudited",
                    "effective_status": "unaudited",
                    "claim_type": None,
                    "criticality": "leaf",
                    "previous_audits": [],
                    "runner_path": RUNNER_PATH,
                    "helper_runner_paths": [HELPER_PATH],
                },
                OPEN_DEP: {
                    "claim_id": OPEN_DEP,
                    "note_path": "docs/FIXTURE_OPEN_DEP.md",
                    "note_hash": hashlib.sha256(DEP_NOTE_BODY.encode()).hexdigest(),
                    "deps": [],
                    "audit_status": "unaudited",
                    "effective_status": "unaudited",
                    "claim_type": "open_gate",
                    "claim_scope": "dep scope",
                    "criticality": "leaf",
                    "previous_audits": [],
                },
                AXIOM_DEP: {
                    "claim_id": AXIOM_DEP,
                    "note_path": "docs/MINIMAL_AXIOMS_FIXTURE.md",
                    "note_hash": AXIOM_HASH,
                    "deps": [],
                    "audit_status": "unaudited",
                    "effective_status": "meta",
                    "claim_type": "meta",
                    "claim_scope": "axiom scope",
                    "criticality": "leaf",
                    "previous_audits": [],
                },
            },
        }

    def _write(self, rel: str, body: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    def write_runner_caches(self) -> None:
        """Canonical SHA-pinned caches for runner + helper (fixed inputs, so
        the produced cache bytes are identical across identical fixtures)."""
        result = {
            "stdout": "PASS=1", "stderr": "", "timeout_sec": 120,
            "exit_code": 0, "elapsed_sec": 0.0, "status": "ok",
        }
        for path in (RUNNER_PATH, HELPER_PATH):
            apply_audit.runner_cache.write_cache(path, dict(result))

    def patches(self):
        return (
            mock.patch.multiple(
                apply_audit,
                REPO_ROOT=self.tmp,
                LEDGER_PATH=self.tmp / "docs" / "audit" / "data" / "audit_ledger.json",
                AXIOM_PREMISE_NODES_PATH=(
                    self.tmp / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
                ),
                _AXIOM_PREMISE_IDS=None,
            ),
            mock.patch.multiple(
                apply_audit.runner_cache,
                REPO_ROOT=self.tmp,
                CACHE_DIR=self.tmp / "logs" / "runner-cache",
                LIVE_LOG_DIR=self.tmp / "logs" / "runner-cache" / ".in-progress",
            ),
            mock.patch.multiple(
                caq,
                REPO_ROOT=self.tmp,
                DATA_DIR=self.tmp / "docs" / "audit" / "data",
            ),
        )


class FingerprintV1StampingTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.fx = StampFixture(Path(self._tmp.name))
        p1, p2, p3 = self.fx.patches()
        p1.start(); self.addCleanup(p1.stop)
        p2.start(); self.addCleanup(p2.stop)
        p3.start(); self.addCleanup(p3.stop)
        self.fx.write_runner_caches()

    def _apply(self, verdict="audited_conditional", **overrides):
        ok, msg = apply_audit.apply_one(self.fx.ledger, _audit_blob(verdict, **overrides))
        self.assertTrue(ok, msg)
        return self.fx.ledger["rows"][CLAIM_ID]

    def _prepare_judicial(self, verdict="audited_conditional"):
        row = self.fx.ledger["rows"][CLAIM_ID]
        row["audit_status"] = "audit_in_progress"
        row["claim_type"] = "positive_theorem"
        row["claim_scope"] = "fixture scope"
        row["criticality"] = "critical"
        seat = {
            "auditor": "first-auditor",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "fresh_context",
            "verdict": verdict,
            "claim_type": "positive_theorem",
            "claim_scope": "fixture scope",
            "load_bearing_step_class": "C",
            "negative_assertion_classes": [],
        }
        row["cross_confirmation"] = {
            "status": "disagreement",
            "first_audit": seat,
            "second_audit": {**seat, "auditor": "second-auditor"},
        }
        return {
            "claim_id": CLAIM_ID,
            "third_auditor": "judicial-panel",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "judicial_review",
            "sided_with": "hybrid",
            "negative_assertion_classes": [],
            "ratified_verdict": verdict,
            "ratified_claim_type": "positive_theorem",
            "ratified_claim_scope": "fixture scope",
            "ratified_load_bearing_step_class": "C",
            "ratified_load_bearing_step": "fixture step",
            "judgment_rationale": "fixture judicial disposition",
            "first_auditor_error": "scope incomplete",
            "second_auditor_error": "scope incomplete",
            "hybrid_resolution_note": "bounded fixture resolution",
        }

    # -- v1 completeness and parking under unchanged current state --------

    def test_conditional_stamp_is_v1_complete_and_parks(self):
        row = self._apply("audited_conditional")
        snap = row["audit_state_snapshot"]
        self.assertEqual(snap.get("schema"), caq.BLOCKER_FINGERPRINT_V1)
        for key, typ in caq.FINGERPRINT_V1_REQUIRED_KEYS.items():
            self.assertIn(key, snap)
            self.assertIsInstance(snap[key], typ, key)
        # membership data recorded for deps AND helpers
        self.assertEqual(sorted(snap["dep_effective_status"]), [AXIOM_DEP, OPEN_DEP])
        self.assertEqual(sorted(snap["helper_runner_hashes"]), [HELPER_PATH])
        # unchanged current state -> parks: not fail-open, no unpark reason
        parked, reason = caq._live_conditional_would_park(row, self.fx.ledger["rows"])
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")
        self.assertFalse(reason.startswith("fail_open"))

    def test_failed_stamp_is_v1_complete_and_parks(self):
        row = self._apply("audited_failed")
        snap = row["audit_state_snapshot"]
        self.assertEqual(snap.get("schema"), caq.BLOCKER_FINGERPRINT_V1)
        parked, reason = caq._live_conditional_would_park(row, self.fx.ledger["rows"])
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")

    def test_stamp_records_this_pass_channel_values(self):
        row = self._apply("audited_conditional")
        snap = row["audit_state_snapshot"]
        registry_bytes = (
            self.fx.tmp / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
        ).read_bytes()
        self.assertEqual(
            snap["premise_registry_epoch"],
            hashlib.sha256(registry_bytes).hexdigest(),
        )
        self.assertEqual(
            snap["policy_versions"]["audit_tuple_agreement_schema"],
            apply_audit.AUDIT_TUPLE_AGREEMENT_SCHEMA,
        )
        self.assertEqual(
            snap["policy_versions"]["audit_prompt_template_sha256"],
            hashlib.sha256(PROMPT_TEMPLATE_BODY.encode()).hexdigest(),
        )
        self.assertEqual(
            snap["policy_versions"]["n8_source_corpus_version"],
            apply_audit.no_go_discipline_gate.N8_SOURCE_CORPUS_VERSION,
        )
        self.assertEqual(
            snap["policy_versions"]["no_go_discipline_gate_sha256"],
            hashlib.sha256(
                Path(apply_audit.no_go_discipline_gate.__file__).read_bytes()
            ).hexdigest(),
        )
        runner_sha = hashlib.sha256(RUNNER_BODY.encode()).hexdigest()
        helper_sha = hashlib.sha256(HELPER_BODY.encode()).hexdigest()
        self.assertEqual(snap["runner_path"], RUNNER_PATH)
        self.assertIs(snap["runner_present"], True)
        self.assertEqual(snap["runner_hash"], runner_sha)
        self.assertEqual(snap["helper_runner_hashes"], {HELPER_PATH: helper_sha})
        self.assertEqual(
            snap["runner_cache_state"][RUNNER_PATH],
            {"cache_freshness": "fresh", "cache_runner_sha256": runner_sha,
             "cache_status": "ok", "cache_exit_code": "0"},
        )
        self.assertEqual(
            snap["runner_cache_state"][HELPER_PATH],
            {"cache_freshness": "fresh", "cache_runner_sha256": helper_sha,
             "cache_status": "ok", "cache_exit_code": "0"},
        )
        self.assertEqual(
            snap["artifact_classifier_state"],
            {
                "runner_path": RUNNER_PATH,
                "exists": True,
                "counts": {"A": 2, "B": 0, "C": 0, "D": 0},
                "assert_count": 2,
                "dominant_class": "A",
                "decoration_candidate": True,
            },
        )

    # -- validation matrix: omissions fail loudly in the comparator -------

    def test_each_required_key_omission_raises_loudly(self):
        row = self._apply("audited_conditional")
        for key in caq.FINGERPRINT_V1_REQUIRED_KEYS:
            mutated = copy.deepcopy(row)
            del mutated["audit_state_snapshot"][key]
            with self.assertRaises(caq.FingerprintV1Invalid, msg=key):
                caq._live_conditional_would_park(mutated, self.fx.ledger["rows"])

    def test_each_required_key_ill_typing_raises_loudly(self):
        row = self._apply("audited_conditional")
        for key in caq.FINGERPRINT_V1_REQUIRED_KEYS:
            mutated = copy.deepcopy(row)
            mutated["audit_state_snapshot"][key] = None
            with self.assertRaises(caq.FingerprintV1Invalid, msg=key):
                caq._live_conditional_would_park(mutated, self.fx.ledger["rows"])

    def test_boolean_epoch_and_malformed_nested_objects_fail_loudly(self):
        row = self._apply("audited_conditional")
        mutations = (
            ("premise_registry_epoch", True),
            ("policy_versions", {}),
            ("runner_cache_state", {}),
            ("artifact_classifier_state", {}),
            ("helper_runner_hashes", {HELPER_PATH: "not-a-sha"}),
        )
        for key, value in mutations:
            mutated = copy.deepcopy(row)
            mutated["audit_state_snapshot"][key] = value
            self.assertTrue(caq.fingerprint_v1_problems(
                mutated["audit_state_snapshot"]
            ), key)
            with self.assertRaises(caq.FingerprintV1Invalid, msg=key):
                caq._live_conditional_would_park(
                    mutated, self.fx.ledger["rows"]
                )

    # -- stamp-then-mutate-one-channel un-parks with the named reason ------

    def test_dep_effective_status_movement_unparks(self):
        row = self._apply("audited_conditional")
        rows = copy.deepcopy(self.fx.ledger["rows"])
        rows[OPEN_DEP]["effective_status"] = "retained"
        parked, reason = caq._live_conditional_would_park(row, rows)
        self.assertFalse(parked)
        self.assertEqual(reason, f"dep_effective_status_changed:{OPEN_DEP}")

    def test_dep_claim_type_and_scope_movement_unpark(self):
        row = self._apply("audited_conditional")
        for field, snap_field in (
            ("claim_type", "dep_claim_type"),
            ("claim_scope", "dep_claim_scope"),
        ):
            rows = copy.deepcopy(self.fx.ledger["rows"])
            rows[OPEN_DEP][field] = "moved_value"
            parked, reason = caq._live_conditional_would_park(row, rows)
            self.assertFalse(parked, field)
            self.assertEqual(reason, f"{snap_field}_changed:{OPEN_DEP}")

    def test_axiom_premise_note_hash_movement_unparks(self):
        row = self._apply("audited_conditional")
        self.assertEqual(
            row["audit_state_snapshot"]["dep_axiom_premise_note_hash"],
            {AXIOM_DEP: AXIOM_HASH},
        )
        rows = copy.deepcopy(self.fx.ledger["rows"])
        rows[AXIOM_DEP]["note_hash"] = hashlib.sha256(b"moved axiom").hexdigest()
        parked, reason = caq._live_conditional_would_park(row, rows)
        self.assertFalse(parked)
        self.assertEqual(reason, f"dep_axiom_premise_note_hash_changed:{AXIOM_DEP}")

    def test_dep_membership_movement_unparks(self):
        row = copy.deepcopy(self._apply("audited_conditional"))
        row["deps"] = row["deps"] + ["fixture_new_dep"]
        parked, reason = caq._live_conditional_would_park(row, self.fx.ledger["rows"])
        self.assertFalse(parked)
        self.assertEqual(reason, "dep_membership_changed")

    def test_helper_membership_movement_unparks(self):
        row = copy.deepcopy(self._apply("audited_conditional"))
        row["helper_runner_paths"] = []
        parked, reason = caq._live_conditional_would_park(row, self.fx.ledger["rows"])
        self.assertFalse(parked)
        self.assertEqual(reason, "helper_runner_membership_changed")

    def test_helper_hash_movement_unparks(self):
        row = copy.deepcopy(self._apply("audited_conditional"))
        self.fx._write(HELPER_PATH, HELPER_BODY + "MOVED = True\n")
        parked, reason = caq._live_conditional_would_park(row, self.fx.ledger["rows"])
        self.assertFalse(parked)
        self.assertEqual(reason, f"helper_runner_hash_changed:{HELPER_PATH}")

    def test_live_cache_policy_and_registry_movement_unpark(self):
        stamped = copy.deepcopy(self._apply("audited_conditional"))

        apply_audit.runner_cache.cache_path_for(RUNNER_PATH).unlink()
        parked, reason = caq._live_conditional_would_park(
            stamped, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "runner_cache_state_changed")
        self.fx.write_runner_caches()

        self.fx._write(
            "docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md",
            PROMPT_TEMPLATE_BODY + "\nchanged\n",
        )
        parked, reason = caq._live_conditional_would_park(
            stamped, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "policy_versions_changed")
        self.fx._write("docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md", PROMPT_TEMPLATE_BODY)

        self.fx._write(
            "docs/audit/data/axiom_premise_nodes.json",
            json.dumps(
                {"schema_version": 2, "canonical_ids": [AXIOM_DEP]},
                indent=2,
                sort_keys=True,
            ) + "\n",
        )
        parked, reason = caq._live_conditional_would_park(
            stamped, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "premise_registry_epoch_changed")

    def test_classifier_current_channel_is_recomputed_from_live_source(self):
        row = self._apply("audited_conditional")
        before = caq.fingerprint_v1_current_channels(row)[
            "artifact_classifier_state"
        ]
        self.fx._write(RUNNER_PATH, "print('PASS=1')\n")
        after = caq.fingerprint_v1_current_channels(row)[
            "artifact_classifier_state"
        ]
        self.assertNotEqual(before, after)
        self.assertEqual(after["counts"], {"A": 0, "B": 0, "C": 0, "D": 0})

    def test_primary_present_to_missing_unparks_and_invalidates(self):
        row = copy.deepcopy(self._apply("audited_conditional"))
        (self.fx.tmp / RUNNER_PATH).unlink()
        parked, reason = caq._live_conditional_would_park(
            row, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "runner_presence_changed")
        self.assertIn("runner_presence_changed", isa.detect_invalidation(
            row, self.fx.ledger["rows"]
        ))

    def test_primary_missing_to_present_unparks_and_invalidates(self):
        (self.fx.tmp / RUNNER_PATH).unlink()
        row = copy.deepcopy(self._apply("audited_conditional"))
        self.assertIs(row["audit_state_snapshot"]["runner_present"], False)
        self.fx._write(RUNNER_PATH, RUNNER_BODY)
        parked, reason = caq._live_conditional_would_park(
            row, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "runner_presence_changed")
        self.assertIn("runner_presence_changed", isa.detect_invalidation(
            row, self.fx.ledger["rows"]
        ))

    def test_primary_byte_identical_path_change_unparks_and_invalidates(self):
        row = copy.deepcopy(self._apply("audited_conditional"))
        moved_path = "scripts/fixture_runner_moved.py"
        self.fx._write(moved_path, RUNNER_BODY)
        row["runner_path"] = moved_path
        parked, reason = caq._live_conditional_would_park(
            row, self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "runner_path_changed")
        self.assertEqual(
            isa.detect_invalidation(row, self.fx.ledger["rows"]),
            "runner_path_changed",
        )

    # -- writer-side fail-loud and transactionality ------------------------

    def test_writer_refuses_incomplete_stamp_loudly_and_transactionally(self):
        before = copy.deepcopy(self.fx.ledger)
        with mock.patch.object(
            apply_audit, "_fingerprint_policy_versions", return_value=None
        ):
            with self.assertRaises(caq.FingerprintV1Invalid):
                apply_audit.apply_one(self.fx.ledger, _audit_blob())
        self.assertEqual(self.fx.ledger, before)

    def test_writer_rejects_boolean_epoch_before_full_ledger_commit(self):
        before = copy.deepcopy(self.fx.ledger)
        with mock.patch.object(
            apply_audit, "_fingerprint_premise_registry_epoch", return_value=True
        ):
            with self.assertRaises(caq.FingerprintV1Invalid):
                apply_audit.apply_one(self.fx.ledger, _audit_blob())
        self.assertEqual(self.fx.ledger, before)

    def test_required_policy_read_failure_is_loud_and_transactional(self):
        before = copy.deepcopy(self.fx.ledger)
        (self.fx.tmp / "docs" / "audit" / "AUDIT_AGENT_PROMPT_TEMPLATE.md").unlink()
        with self.assertRaises(OSError):
            apply_audit.apply_one(self.fx.ledger, _audit_blob())
        self.assertEqual(self.fx.ledger, before)

    def test_judicial_conditional_stamps_complete_v1_snapshot(self):
        judgment = self._prepare_judicial("audited_conditional")
        ok, msg = apply_audit.apply_one(self.fx.ledger, judgment)
        self.assertTrue(ok, msg)
        snapshot = self.fx.ledger["rows"][CLAIM_ID]["audit_state_snapshot"]
        self.assertEqual(snapshot["schema"], caq.BLOCKER_FINGERPRINT_V1)
        self.assertEqual(caq.fingerprint_v1_problems(snapshot), [])

    def test_judicial_failed_stamps_complete_v1_snapshot(self):
        judgment = self._prepare_judicial("audited_failed")
        ok, msg = apply_audit.apply_one(self.fx.ledger, judgment)
        self.assertTrue(ok, msg)
        snapshot = self.fx.ledger["rows"][CLAIM_ID]["audit_state_snapshot"]
        self.assertEqual(snapshot["schema"], caq.BLOCKER_FINGERPRINT_V1)
        self.assertEqual(caq.fingerprint_v1_problems(snapshot), [])

    def test_judicial_late_snapshot_failure_rolls_back_full_ledger(self):
        judgment = self._prepare_judicial("audited_conditional")
        before = copy.deepcopy(self.fx.ledger)
        with mock.patch.object(
            apply_audit, "_fingerprint_policy_versions", return_value={}
        ):
            with self.assertRaises(caq.FingerprintV1Invalid):
                apply_audit.apply_one(self.fx.ledger, judgment)
        self.assertEqual(self.fx.ledger, before)

    # -- scope: new conditional/failed writes only -------------------------

    def test_clean_verdict_snapshot_stays_legacy_shaped(self):
        row = self._apply(
            "audited_clean",
            chain_closes=True,
            chain_closure_explanation="closes on fixture inputs",
            verdict_rationale="clean fixture",
        )
        snap = row["audit_state_snapshot"]
        self.assertNotIn("schema", snap)
        for key in ("runner_cache_state", "artifact_classifier_state",
                    "policy_versions", "premise_registry_epoch"):
            self.assertNotIn(key, snap)
        # legacy baselines are still written exactly as before
        self.assertIn("dep_effective_status", snap)
        self.assertIn("helper_runner_hashes", snap)

    def test_preexisting_legacy_rows_are_not_rewritten(self):
        legacy_snapshot = {"dep_effective_status": {OPEN_DEP: "unaudited"}}
        self.fx.ledger["rows"][CLAIM_ID]["audit_status"] = "audited_conditional"
        self.fx.ledger["rows"][CLAIM_ID]["audit_state_snapshot"] = copy.deepcopy(
            legacy_snapshot
        )
        # No verdict write happens; the legacy row must stay fail-open in the
        # comparator (the version matrix's honest legacy branch), untouched.
        parked, reason = caq._live_conditional_would_park(
            self.fx.ledger["rows"][CLAIM_ID], self.fx.ledger["rows"]
        )
        self.assertFalse(parked)
        self.assertEqual(reason, "fail_open_legacy_unversioned")
        self.assertEqual(
            self.fx.ledger["rows"][CLAIM_ID]["audit_state_snapshot"],
            legacy_snapshot,
        )

    # -- determinism --------------------------------------------------------

    def test_stamp_is_byte_identical_across_identical_passes(self):
        first = json.dumps(
            self._apply("audited_conditional")["audit_state_snapshot"],
            sort_keys=True,
        )
        with tempfile.TemporaryDirectory() as tmp2:
            fx2 = StampFixture(Path(tmp2))
            p1, p2, p3 = fx2.patches()
            with p1, p2, p3:
                fx2.write_runner_caches()
                ok, msg = apply_audit.apply_one(fx2.ledger, _audit_blob())
                self.assertTrue(ok, msg)
                second = json.dumps(
                    fx2.ledger["rows"][CLAIM_ID]["audit_state_snapshot"],
                    sort_keys=True,
                )
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
