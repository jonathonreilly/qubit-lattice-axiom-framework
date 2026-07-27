"""Tests for the runner-pin gate.

A verdict is bound to the runner it cites only through
`audit_state_snapshot.runner_hash` and `.helper_runner_hashes` — the two
fields `invalidate_stale_audits.detect_invalidation` compares. Covers: the
writer refuses a terminal verdict that leaves a named runner unbound; a
missing runner is a legitimate non-clean state and an illegitimate clean one;
non-terminal writes stay unconstrained; the lint classifier separates a live
writer regression from recorded pre-pin debt, and separates unchanged debt
from source that has moved under an unpinned verdict; the baseline drains when
a row is re-pinned; and the shipped baseline is internally well-formed.
"""

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import runner_pin_gate as gate  # noqa: E402

RUNNER_PATH = "scripts/fixture_runner.py"
HELPER_PATH = "scripts/fixture_helper.py"
OTHER_HELPER_PATH = "scripts/fixture_other_helper.py"
RUNNER_BODY = "print('PASS=1')\n"
HELPER_BODY = "VALUE = 'helper'\n"

RUNNER_SHA = hashlib.sha256(RUNNER_BODY.encode()).hexdigest()
HELPER_SHA = hashlib.sha256(HELPER_BODY.encode()).hexdigest()
OTHER_SHA = hashlib.sha256(b"other\n").hexdigest()


def _row(**overrides):
    row = {
        "claim_id": "fixture_row",
        "audit_status": "audited_clean",
        "effective_status": "retained",
        "runner_path": RUNNER_PATH,
        "helper_runner_paths": [],
    }
    row.update(overrides)
    return row


def _snapshot(**overrides):
    snap = {"runner_hash": RUNNER_SHA, "helper_runner_hashes": {}}
    snap.update(overrides)
    return snap


class RepoFixture:
    """Temp repo root so presence/hash checks read fixture files."""

    def __init__(self, tmp: Path, write_runner=True, write_helpers=()):
        self.tmp = tmp
        (tmp / "scripts").mkdir(parents=True)
        if write_runner:
            (tmp / RUNNER_PATH).write_text(RUNNER_BODY, encoding="utf-8")
        for helper in write_helpers:
            (tmp / helper).write_text(HELPER_BODY, encoding="utf-8")

    def patches(self):
        return [
            mock.patch.object(gate, "REPO_ROOT", self.tmp),
            mock.patch.object(gate.rc, "REPO_ROOT", self.tmp),
        ]


class WriterGateTest(unittest.TestCase):
    def _problems(self, row, snapshot, **fixture_kwargs):
        with tempfile.TemporaryDirectory() as raw:
            fixture = RepoFixture(Path(raw), **fixture_kwargs)
            with mock.patch.object(gate, "REPO_ROOT", fixture.tmp), \
                    mock.patch.object(gate.rc, "REPO_ROOT", fixture.tmp):
                return gate.verdict_pin_problems(row, snapshot)

    def test_complete_snapshot_has_no_problems(self):
        self.assertEqual(self._problems(_row(), _snapshot()), [])

    def test_missing_runner_hash_key_is_refused(self):
        snap = _snapshot()
        del snap["runner_hash"]
        self.assertIn("runner_hash:missing_key", self._problems(_row(), snap))

    def test_null_runner_hash_with_present_runner_is_refused(self):
        problems = self._problems(_row(), _snapshot(runner_hash=None))
        self.assertTrue(
            any(p.startswith("runner_hash:required_sha256_for_present_runner") for p in problems),
            problems,
        )

    def test_absent_runner_blocks_clean_but_not_conditional(self):
        clean = self._problems(
            _row(), _snapshot(runner_hash=None), write_runner=False
        )
        self.assertTrue(
            any(
                p.startswith(
                    "runner_hash:audited_clean_names_absent_runner_without_presence_pin"
                )
                for p in clean
            ),
            clean,
        )
        conditional = self._problems(
            _row(audit_status="audited_conditional"),
            _snapshot(runner_hash=None),
            write_runner=False,
        )
        self.assertEqual(conditional, [])

    def test_absent_runner_blocks_every_verdict_without_a_presence_pin(self):
        """Only the v1-stamped verdicts pin `runner_present`, so only they can
        legitimately record a null hash for a runner that is missing on disk.
        `detect_invalidation` never fires on a null legacy hash, so an
        absent->present move under any other terminal verdict is invisible
        forever."""
        for status in sorted(gate.TERMINAL_VERDICTS - gate.PRESENCE_PINNED_VERDICTS):
            problems = self._problems(
                _row(audit_status=status), _snapshot(runner_hash=None), write_runner=False
            )
            self.assertTrue(
                any(
                    p.startswith(f"runner_hash:{status}_names_absent_runner")
                    for p in problems
                ),
                (status, problems),
            )
        for status in sorted(gate.PRESENCE_PINNED_VERDICTS):
            self.assertEqual(
                self._problems(
                    _row(audit_status=status),
                    _snapshot(runner_hash=None),
                    write_runner=False,
                ),
                [],
                status,
            )

    def test_presence_pinned_set_matches_the_writer_stamp_set(self):
        """If `apply_audit.FINGERPRINT_STAMP_VERDICTS` grows or shrinks, the
        absent-runner exemption above must move with it or the gate starts
        exempting verdicts that carry no presence pin."""
        import apply_audit

        self.assertEqual(
            gate.PRESENCE_PINNED_VERDICTS, apply_audit.FINGERPRINT_STAMP_VERDICTS
        )

    def test_row_without_runner_is_unconstrained(self):
        self.assertEqual(
            self._problems(_row(runner_path=None), _snapshot(runner_hash=None)), []
        )

    def test_non_terminal_verdict_is_unconstrained(self):
        for status in ("unaudited", "audit_in_progress"):
            self.assertEqual(
                self._problems(_row(audit_status=status), {"runner_hash": None}),
                [],
                status,
            )

    def test_helper_map_must_cover_declared_helpers_exactly(self):
        row = _row(helper_runner_paths=[HELPER_PATH])
        missing = self._problems(row, _snapshot(), write_helpers=[HELPER_PATH])
        self.assertTrue(any(p.startswith("helper_runner_hashes:missing") for p in missing), missing)

        extra = self._problems(
            _row(),
            _snapshot(helper_runner_hashes={HELPER_PATH: HELPER_SHA}),
            write_helpers=[HELPER_PATH],
        )
        self.assertTrue(any(p.startswith("helper_runner_hashes:unexpected") for p in extra), extra)

        absent_map = self._problems(row, {"runner_hash": RUNNER_SHA})
        self.assertIn("helper_runner_hashes:missing_map", absent_map)

        complete = self._problems(
            row,
            _snapshot(helper_runner_hashes={HELPER_PATH: HELPER_SHA}),
            write_helpers=[HELPER_PATH],
        )
        self.assertEqual(complete, [])

    def test_null_helper_hash_for_present_helper_is_refused(self):
        problems = self._problems(
            _row(helper_runner_paths=[HELPER_PATH]),
            _snapshot(helper_runner_hashes={HELPER_PATH: None}),
            write_helpers=[HELPER_PATH],
        )
        self.assertTrue(
            any(
                p.startswith("helper_runner_hashes:required_sha256_for_present_runner")
                for p in problems
            ),
            problems,
        )


class WriterRefusesUnpinnedVerdictTest(unittest.TestCase):
    """The gate is wired into the real snapshot writer, not just available."""

    def test_snapshot_audit_state_raises_on_unpinnable_clean_verdict(self):
        import apply_audit

        row = {
            "claim_id": "fixture_row",
            "note_path": "docs/FIXTURE.md",
            "audit_status": "audited_clean",
            "runner_path": "scripts/does_not_exist_fixture_runner.py",
            "helper_runner_paths": [],
            "deps": [],
        }
        with self.assertRaises(gate.RunnerPinIncomplete):
            apply_audit.snapshot_audit_state(row, {})


class ClassifierTest(unittest.TestCase):
    BASELINE = {
        "fixture_row": {
            "audit_status": "audited_clean",
            "runner_path": RUNNER_PATH,
            "runner_sha256_at_baseline": RUNNER_SHA,
        }
    }

    def _classify(self, row, baseline=None, sha_map=None, present=None):
        sha_map = sha_map or {RUNNER_PATH: RUNNER_SHA, HELPER_PATH: HELPER_SHA}
        present = {RUNNER_PATH, HELPER_PATH, OTHER_HELPER_PATH} if present is None else present
        with mock.patch.object(gate, "current_sha256", lambda p: sha_map.get(p)), \
                mock.patch.object(gate, "runner_exists", lambda p: p in present):
            return gate.classify_row(row, self.BASELINE if baseline is None else baseline)

    def test_pinned_row_is_not_classified(self):
        row = _row(audit_state_snapshot=_snapshot())
        self.assertIsNone(self._classify(row))

    def test_unaudited_row_is_not_classified(self):
        row = _row(audit_status="unaudited", audit_state_snapshot={})
        self.assertIsNone(self._classify(row))

    def test_absent_runner_is_not_a_pin_finding(self):
        """No pin can be demanded for source nobody can hash; the clean-verdict
        write path refuses that row instead."""
        row = _row(audit_state_snapshot={"deps": []})
        self.assertIsNone(self._classify(row, present=set()))

    def test_pin_capable_snapshot_with_empty_field_is_a_writer_regression(self):
        row = _row(audit_state_snapshot=_snapshot(runner_hash=None))
        label, _ = self._classify(row)
        self.assertEqual(label, gate.PIN_WRITER_REGRESSION)

    def test_pre_pin_snapshot_outside_the_baseline_is_a_hard_miss(self):
        row = _row(claim_id="not_in_baseline", audit_state_snapshot={"deps": []})
        label, _ = self._classify(row, baseline={})
        self.assertEqual(label, gate.PIN_BASELINE_MISSING)

    def test_recorded_unchanged_debt_is_grandfathered(self):
        row = _row(audit_state_snapshot={"deps": []})
        label, _ = self._classify(row)
        self.assertEqual(label, gate.PIN_GRANDFATHERED)

    def test_recorded_prior_drift_is_reported_separately(self):
        baseline = {
            "fixture_row": {
                **self.BASELINE["fixture_row"],
                "source_drifted_since_verdict": True,
                "drift_evidence": ["abc1234 2026-07-12 scripts/fixture_runner.py"],
            }
        }
        row = _row(audit_state_snapshot={"deps": []})
        label, detail = self._classify(row, baseline=baseline)
        self.assertEqual(label, gate.PIN_BASELINE_SOURCE_DRIFTED)
        self.assertIn("re-audit candidate", detail)
        # The finding must not claim the row has been queued: nothing in this
        # module or in audit_lint writes a dispatcher sidecar.
        self.assertIn("nothing here queues it", detail)

    def test_source_moving_after_the_baseline_is_new_drift(self):
        row = _row(audit_state_snapshot={"deps": []})
        label, detail = self._classify(row, sha_map={RUNNER_PATH: OTHER_SHA})
        self.assertEqual(label, gate.PIN_BASELINE_NEW_DRIFT)
        self.assertIn(RUNNER_PATH, detail)

    def test_helper_channel_alone_triggers_classification(self):
        baseline = {
            "fixture_row": {
                "audit_status": "audited_clean",
                "helper_runner_sha256_at_baseline": {HELPER_PATH: HELPER_SHA},
            }
        }
        row = _row(
            runner_path=None,
            helper_runner_paths=[HELPER_PATH],
            audit_state_snapshot={"runner_hash": None},
        )
        label, _ = self._classify(row, baseline=baseline)
        self.assertEqual(label, gate.PIN_GRANDFATHERED)

        moved = self._classify(row, baseline=baseline, sha_map={HELPER_PATH: OTHER_SHA})
        self.assertEqual(moved[0], gate.PIN_BASELINE_NEW_DRIFT)

    def test_helper_entering_an_unpinned_closure_is_new_drift(self):
        """The recorded shas cover only the helpers that existed at baseline
        time. On an unpinned helper channel nothing watches membership, so a
        helper that enters the closure later is source the verdict has never
        been compared against — it must not report as `source unchanged`."""
        baseline = {
            "fixture_row": {
                "audit_status": "audited_clean",
                "helper_runner_sha256_at_baseline": {HELPER_PATH: HELPER_SHA},
            }
        }
        row = _row(
            runner_path=None,
            helper_runner_paths=[HELPER_PATH, OTHER_HELPER_PATH],
            audit_state_snapshot={"runner_hash": None},
        )
        label, detail = self._classify(row, baseline=baseline)
        self.assertEqual(label, gate.PIN_BASELINE_NEW_DRIFT)
        self.assertIn(OTHER_HELPER_PATH, detail)
        self.assertEqual(
            gate.helpers_unpinned(row, row["audit_state_snapshot"]), True
        )

    def test_recorded_prior_drift_does_not_mask_a_later_move(self):
        """A row already flagged `source_drifted_since_verdict` is the worst-off
        entry in the file. Short-circuiting on the flag would make every further
        move on exactly those rows report as the softer recorded-drift warning
        forever, so the rows with known drift would be the only ones the ratchet
        never protects."""
        baseline = {
            "fixture_row": {
                **self.BASELINE["fixture_row"],
                "source_drifted_since_verdict": True,
                "drift_evidence": ["abc1234 2026-07-12 scripts/fixture_runner.py"],
            }
        }
        row = _row(audit_state_snapshot={"deps": []})
        label, detail = self._classify(
            row, baseline=baseline, sha_map={RUNNER_PATH: OTHER_SHA}
        )
        self.assertEqual(label, gate.PIN_BASELINE_NEW_DRIFT)
        self.assertIn(RUNNER_PATH, detail)

    def test_recorded_helper_map_with_a_changed_key_set_is_not_a_pin_finding(self):
        """`detect_invalidation` returns `helper_runner_paths_changed` on any
        key-set difference, so a recorded map binds the channel even when the
        closure has moved. Reporting it here would turn an ordinary import edit
        into a retained-grade hard error with no drain path."""
        row = _row(
            helper_runner_paths=[HELPER_PATH, OTHER_HELPER_PATH],
            audit_state_snapshot=_snapshot(
                helper_runner_hashes={HELPER_PATH: HELPER_SHA}
            ),
        )
        self.assertFalse(gate.helpers_unpinned(row, row["audit_state_snapshot"]))
        self.assertIsNone(self._classify(row))
        empty_map = _row(
            helper_runner_paths=[HELPER_PATH],
            audit_state_snapshot=_snapshot(helper_runner_hashes={}),
        )
        self.assertFalse(gate.helpers_unpinned(empty_map, empty_map["audit_state_snapshot"]))


class BaselineDrainTest(unittest.TestCase):
    def test_repinned_row_drains_from_the_baseline(self):
        baseline = {"fixture_row": {"audit_status": "audited_clean"}}
        rows = {"fixture_row": _row(audit_state_snapshot=_snapshot())}
        self.assertEqual(
            gate.stale_baseline_entries(rows, baseline),
            {"drained": ["fixture_row"], "absent": []},
        )

    def test_still_unpinned_row_does_not_drain(self):
        baseline = {"fixture_row": {"audit_status": "audited_clean"}}
        rows = {"fixture_row": _row(audit_state_snapshot={"deps": []})}
        self.assertEqual(
            gate.stale_baseline_entries(rows, baseline),
            {"drained": [], "absent": []},
        )

    def test_reset_row_drains_and_absent_row_is_reported_apart(self):
        baseline = {"gone": {}, "reset": {}}
        rows = {"reset": _row(audit_status="unaudited", audit_state_snapshot={})}
        self.assertEqual(
            gate.stale_baseline_entries(rows, baseline),
            {"drained": ["reset"], "absent": ["gone"]},
        )


class ShippedBaselineTest(unittest.TestCase):
    def test_baseline_is_well_formed(self):
        data = json.loads(gate.BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], gate.BASELINE_SCHEMA)
        self.assertTrue(data["entries"])
        for cid, entry in data["entries"].items():
            self.assertIn(entry["audit_status"], gate.TERMINAL_VERDICTS, cid)
            self.assertTrue(
                "runner_path" in entry or "helper_runner_sha256_at_baseline" in entry,
                f"{cid}: baseline entry records no unpinned channel",
            )
            if "runner_path" in entry:
                self.assertIn("runner_sha256_at_baseline", entry, cid)

    def test_baseline_loads_through_the_gate(self):
        entries = gate.load_baseline()
        self.assertTrue(entries)
        self.assertIsInstance(next(iter(entries.values())), dict)

    def test_wrong_schema_is_refused(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "baseline.json"
            path.write_text(json.dumps({"schema": "nope", "entries": {}}), encoding="utf-8")
            with self.assertRaises(ValueError):
                gate.load_baseline(path)


if __name__ == "__main__":
    unittest.main()
