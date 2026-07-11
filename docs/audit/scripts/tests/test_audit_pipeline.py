#!/usr/bin/env python3
"""Smoke + behavior tests for the audit pipeline scripts.

These are deliberately small, self-contained, and run without touching
the live ledger. Each test patches the relevant module's REPO_ROOT to a
temporary directory so the script reads/writes only the test fixture.

Run via:
  python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline
or:
  python3 docs/audit/scripts/tests/test_audit_pipeline.py
"""
from __future__ import annotations

import importlib
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = REPO_ROOT / "audit" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))


def _no_go_packet(
    *,
    status: str = "PASS",
    route_count: int = 5,
    evidence_path: str = "docs/TEST_NO_GO.md",
    evidence_locator: str = "No-go obstruction",
    claim_scope: str = "the scoped obstruction",
    prior_claim_scope: str = "the unrestricted obstruction",
    claim_id: str = "test_no_go",
    cross_cycle_candidates: tuple[str, ...] = (),
) -> dict:
    failures = [] if status == "PASS" else ["N1: fewer than five routes close"]
    route_classes = [
        "algebraic_rearrangement",
        "symmetry_or_representation",
        "alternate_carrier_or_sector",
        "boundary_or_initial_condition",
        "normalization_or_units",
        "dynamical_or_effective_action",
    ]
    mechanisms = [
        "symbolic cancellation",
        "representation change",
        "alternate carrier sector",
        "boundary data selection",
        "normalization transport",
        "effective action deformation",
    ]
    attempts = [
        "expand and cancel the defining algebra",
        "decompose every supplied representation",
        "test the alternate carrier against the source",
        "vary the allowed boundary data",
        "transport every supplied normalization",
        "insert the effective action candidate",
    ]
    cross_cycle_path = f"audit-packet://cross-cycle-index/{claim_id}"
    partial_closure_path = f"audit-packet://partial-closure-index/{claim_id}"
    packet = {
        "required": True,
        "status": status,
        "N1_alternative_routes": [
            {
                "route_id": f"route-{index}",
                "route_class": route_classes[index],
                "mechanism": mechanisms[index],
                "attempt": attempts[index],
                "outcome": "closed by the restricted packet",
                "honesty_marker": "ATTEMPTED",
                "disposition": "CLOSED",
                "evidence_path": evidence_path,
                "evidence_locator": evidence_locator,
            }
            for index in range(route_count)
        ],
        "N2_wall_independence": {
            "walls": ["selector wall", "dynamics wall"],
            "pairwise_checks": [{
                "left": "selector wall",
                "right": "dynamics wall",
                "left_closes_right": False,
                "right_closes_left": False,
                "independent": True,
            }],
            "collapsed_wall_set": ["selector wall", "dynamics wall"],
            "unresolved": [],
            "evidence_path": evidence_path,
            "evidence_locator": evidence_locator,
        },
        "N3_hidden_wall_scan": {
            "scan_scope": "all wall and admission phrases in the restricted packet",
            "hits": [],
            "none_found_reason": "the scan found no hidden wall phrases",
            "unresolved": [],
            "evidence_path": evidence_path,
            "evidence_locator": evidence_locator,
        },
        "N4_residual_matching": {
            "scan_scope": "all witness and residual statements in the restricted packet",
            "witnesses": [],
            "none_found_reason": "no route was ruled out by a prior witness",
            "unresolved": [],
            "evidence_path": evidence_path,
            "evidence_locator": evidence_locator,
        },
        "N5_rhetoric_audit": {
            "scan_scope": "all negative resolution phrases in the restricted packet",
            "statements": [],
            "none_found_reason": "the source has no additional rhetoric phrases",
            "unresolved": [],
            "evidence_path": evidence_path,
            "evidence_locator": evidence_locator,
        },
        "N6_partial_closure_scan": {
            "scan_scope": "all registered premise classes and definition reframes",
            "premise_classes_checked": [
                "axiom_or_approved_primitive",
                "open_derivation_obligation",
                "convention_not_accepted",
                "definition_or_scope_reframe",
            ],
            "candidates": [],
            "none_found_reason": "no registered partial-closure candidate applies",
            "unresolved": [],
            "evidence_path": partial_closure_path,
            "evidence_locator": "no_go_partial_closure_index_v1",
        },
        "N7_steelman": {
            "route_id": "route-0",
            "argument": "the strongest counter-route",
            "resolution": "the restricted packet answers it",
            "resolved": True,
            "evidence_path": evidence_path,
            "evidence_locator": evidence_locator,
        },
        "N8_cross_cycle_echo": {
            "packet_complete": True,
            "echoes": [
                {
                    "candidate_id": candidate_id,
                    "mechanism": "the indexed prior retirement mechanism",
                    "retired": True,
                    "applicable": False,
                    "addressed": True,
                    "evidence_path": cross_cycle_path,
                    "evidence_locator": candidate_id,
                }
                for candidate_id in cross_cycle_candidates
            ],
            "none_found_reason": "the orchestrator index contains zero candidates",
            "unresolved": [],
            "evidence_path": cross_cycle_path,
            "evidence_locator": "no_go_cross_cycle_index_v1",
        },
        "failures": failures,
    }
    if status == "FAIL":
        packet["N1_alternative_routes"][-1]["disposition"] = "UNTESTED"
        packet.update({
            "demotion": "partial-attempt-with-named-untested-routes",
            "prior_claim_scope": prior_claim_scope,
            "narrowed_claim_scope": claim_scope,
            "corrected_wall_set": ["selector wall", "dynamics wall"],
            "next_route": {
                "route_id": packet["N1_alternative_routes"][-1]["route_id"],
                "reason_untested": "this is the cheapest remaining route",
            },
        })
    return packet


def _import(module_name: str):
    """Force a fresh import each test."""
    if module_name in sys.modules:
        del sys.modules[module_name]
    return importlib.import_module(module_name)


def _import_codex_audit_runner():
    """Import the repo-root codex audit runner without changing sys.path."""
    module_name = "codex_audit_runner_under_test"
    if module_name in sys.modules:
        del sys.modules[module_name]
    spec = importlib.util.spec_from_file_location(
        module_name, PROJECT_ROOT / "scripts" / "codex_audit_runner.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _import_repo_script(filename: str):
    """Import one repo-root runner under a fresh, test-specific name."""
    module_name = f"repo_script_under_test_{Path(filename).stem}"
    if module_name in sys.modules:
        del sys.modules[module_name]
    scripts_dir = PROJECT_ROOT / "scripts"
    spec = importlib.util.spec_from_file_location(module_name, scripts_dir / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[module_name] = module
    sys.path.insert(0, str(scripts_dir))
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    finally:
        sys.path.remove(str(scripts_dir))
    return module


class CleanLedgerFixture:
    """Build a minimal but valid audit_ledger.json + citation_graph.json
    on a temporary REPO_ROOT for unit-style testing."""

    def __init__(self, tmpdir: Path):
        self.tmpdir = tmpdir
        self.audit_dir = tmpdir / "docs" / "audit"
        self.data_dir = self.audit_dir / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.tmpdir / "docs").mkdir(parents=True, exist_ok=True)

    def write_note(self, rel_path: str, body: str) -> Path:
        path = self.tmpdir / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return path

    def write_runner(self, rel_path: str, body: str) -> Path:
        path = self.tmpdir / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return path

    def write_ledger(self, ledger: dict) -> None:
        (self.data_dir / "audit_ledger.json").write_text(
            json.dumps(ledger, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def write_graph(self, graph: dict) -> None:
        (self.data_dir / "citation_graph.json").write_text(
            json.dumps(graph, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def read_ledger(self) -> dict:
        return json.loads((self.data_dir / "audit_ledger.json").read_text(encoding="utf-8"))


def _patch_repo_root(module, tmp_root: Path) -> None:
    """Override the module-level REPO_ROOT-derived paths."""
    module.REPO_ROOT = tmp_root
    module.DATA_DIR = tmp_root / "docs" / "audit" / "data"
    module.LEDGER_PATH = module.DATA_DIR / "audit_ledger.json"
    if hasattr(module, "GRAPH_PATH"):
        module.GRAPH_PATH = module.DATA_DIR / "citation_graph.json"
    # audit_lint reads these at main() time; without redirecting them the lint
    # validates a synthetic temp ledger against the REAL repo's premise and
    # queue registries and emits spurious errors (rows the test never created).
    if hasattr(module, "RETIRED_ADMISSIONS_PATH"):
        module.RETIRED_ADMISSIONS_PATH = module.DATA_DIR / "tier_a_admissions.json"
    if hasattr(module, "DERIVATION_OBLIGATIONS_PATH"):
        module.DERIVATION_OBLIGATIONS_PATH = (
            module.DATA_DIR / "derivation_obligations.json"
        )
    if hasattr(module, "AUDIT_DISPATCH_QUEUE_PATH"):
        module.AUDIT_DISPATCH_QUEUE_PATH = module.DATA_DIR / "audit_dispatch_queue.json"
    if hasattr(module, "SUMMARY_PATH"):
        # Either compute_effective_status (effective_status_summary) or
        # compute_load_bearing (load_bearing_summary). Set both files under
        # tmp data dir; only the relevant one is written.
        module.SUMMARY_PATH = module.DATA_DIR / "effective_status_summary.json"
    if hasattr(module, "OUTPUT_PATH"):
        module.OUTPUT_PATH = module.DATA_DIR / "auditor_reliability.json"


class ChangedRunnerFailureGateTest(unittest.TestCase):
    def test_record_census_returns_nonzero_when_constituent_check_fails(self):
        import contextlib
        import io

        m = _import_repo_script(
            "record_saturation_availability_census_2026_07_08.py"
        )
        with mock.patch.object(
            m, "load_text_authorities", return_value=(False, True)
        ), contextlib.redirect_stdout(io.StringIO()) as output:
            rc = m.run()
        self.assertEqual(rc, 1)
        self.assertIn("TOTAL: MACHINERY-FAIL", output.getvalue())

    def test_schwinger_rotor_coupling_check_is_decisive(self):
        import contextlib
        import io

        m = _import_repo_script(
            "gauged_schwinger_staggered_ed_engine_2026_07_08.py"
        )
        with (
            mock.patch.object(m, "check_exact_rotor_g0_couples_w", return_value=False),
            mock.patch.object(m, "check_01", return_value=(True, "ok")),
            mock.patch.object(m, "check_02", return_value=(True, "ok", {})),
            mock.patch.object(m, "check_03", return_value=(True, "ok")),
            mock.patch.object(m, "check_06", return_value=(True, "ok")),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            rc = m.main()
        self.assertEqual(rc, 1)
        self.assertIn("CHECK-04=FAIL", output.getvalue())

    def test_wep_comparator_rejects_bad_curvature_fit(self):
        import contextlib
        import io

        m = _import_repo_script(
            "wep_source_reduction_scaling_window_2026_07_08.py"
        )
        m.PASS_COUNT = 0
        m.FAIL_COUNT = 0
        with (
            mock.patch.object(
                m,
                "tune_to_energy",
                side_effect=lambda length, mass, target: (1.0, target),
            ),
            mock.patch.object(
                m,
                "fitted_curvature_mass",
                side_effect=[(1.0, 999.0), (2.0, 999.0)],
            ),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            m.check_finite_same_energy_comparator()
        self.assertEqual(m.FAIL_COUNT, 1)
        self.assertIn("fit_residual_tolerance=1.0e-06", output.getvalue())

    def test_wep_fit_residual_is_overdetermined(self):
        m = _import_repo_script(
            "wep_source_reduction_scaling_window_2026_07_08.py"
        )

        def adversarial_energy(length, mass_a, mass_b, coupling, index):
            momentum = m.signed_momentum_value(index, length)
            return 1.0 + momentum**2 + 1.0e8 * momentum**8

        with mock.patch.object(
            m, "lowest_pblock_energy", side_effect=adversarial_energy
        ):
            _, residual = m.fitted_curvature_mass(64, 0.5, 1.0)
        self.assertGreater(residual, m.FIT_RESID_TOL)

    def test_wep_comparator_rejects_nan_fit_residual(self):
        import contextlib
        import io

        m = _import_repo_script(
            "wep_source_reduction_scaling_window_2026_07_08.py"
        )
        m.PASS_COUNT = 0
        m.FAIL_COUNT = 0
        with (
            mock.patch.object(
                m,
                "tune_to_energy",
                side_effect=lambda length, mass, target: (1.0, target),
            ),
            mock.patch.object(
                m,
                "fitted_curvature_mass",
                side_effect=[(1.0, float("nan")), (2.0, float("nan"))],
            ),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            m.check_finite_same_energy_comparator()
        self.assertEqual(m.FAIL_COUNT, 1)
        self.assertIn("max_fit_residual=inf", output.getvalue())


class ApplyAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _seed_one_row(self, cid: str, *, audit_status="unaudited",
                      claim_type=None, deps=None,
                      criticality="leaf", note_body="# test\n"):
        path = f"docs/{cid.upper()}.md"
        self.fx.write_note(path, note_body)
        import hashlib
        note_hash = hashlib.sha256(note_body.encode("utf-8")).hexdigest()
        ledger = {
            "schema_version": 1,
            "rows": {
                cid: {
                    "claim_id": cid,
                    "note_path": path,
                    "note_hash": note_hash,
                    "deps": list(deps or []),
                    "audit_status": audit_status,
                    "claim_type": claim_type,
                    "criticality": criticality,
                    "previous_audits": [],
                }
            },
        }
        self.fx.write_ledger(ledger)
        return path, note_hash

    def test_apply_clean_verdict_writes_snapshot_with_runner_hash(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)

        runner_path = "scripts/test_runner.py"
        runner_body = "print('PASS=1 FAIL=0')\n"
        self.fx.write_runner(runner_path, runner_body)

        path, note_hash = self._seed_one_row("test_clean_row", criticality="leaf")
        # Add runner_path to ledger row
        led = self.fx.read_ledger()
        led["rows"]["test_clean_row"]["runner_path"] = runner_path
        self.fx.write_ledger(led)

        audit = {
            "claim_id": "test_clean_row",
            "verdict": "audited_clean",
            "claim_type": "positive_theorem",
            "claim_scope": "test scope",
            "auditor": "test-auditor",
            "auditor_family": "codex-gpt-5.5",
            "auditor_model": "gpt-5.5",
            "auditor_reasoning_effort": "xhigh",
            "independence": "cross_family",
            "load_bearing_step_class": "C",
            "load_bearing_step": "test step",
            "chain_closes": True,
            "chain_closure_explanation": "ok",
            "verdict_rationale": "ok",
        }
        ok, msg = m.apply_one(led, audit)
        self.assertTrue(ok, msg)
        snap = led["rows"]["test_clean_row"].get("audit_state_snapshot")
        self.assertIsNotNone(snap)
        self.assertIn("runner_hash", snap)
        # Runner hash matches actual file hash
        import hashlib
        expected = hashlib.sha256(runner_body.encode("utf-8")).hexdigest()
        self.assertEqual(snap["runner_hash"], expected)

    def test_weak_independence_blocks_audited_clean(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)
        path, _ = self._seed_one_row("test_weak", criticality="medium")
        led = self.fx.read_ledger()
        audit = {
            "claim_id": "test_weak",
            "verdict": "audited_clean",
            "claim_type": "positive_theorem",
            "claim_scope": "test",
            "auditor": "weak-auditor",
            "auditor_family": "claude-opus",
            "auditor_model": "claude-opus-4.1",
            "auditor_reasoning_effort": "xhigh",
            "independence": "weak",
            "load_bearing_step_class": "C",
        }
        ok, msg = m.apply_one(led, audit)
        self.assertFalse(ok)
        self.assertIn("weak", msg)

    def test_no_go_requires_and_preserves_discipline_packet(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)
        self._seed_one_row(
            "test_no_go",
            claim_type="no_go",
            note_body="# No-go obstruction\n",
        )
        led = self.fx.read_ledger()
        base = {
            "claim_id": "test_no_go",
            "verdict": "audited_clean",
            "claim_type": "no_go",
            "claim_scope": "the scoped obstruction",
            "chain_closes": True,
            "auditor": "fresh-no-go-auditor",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "cross_family",
            "load_bearing_step_class": "A",
        }

        ok, msg = m.apply_one(led, dict(base))
        self.assertFalse(ok)
        self.assertIn("N1-N8 packet is required", msg)

        audit = {**base, "no_go_discipline": _no_go_packet()}
        ok, msg = m.apply_one(led, audit)
        self.assertTrue(ok, msg)
        row = led["rows"]["test_no_go"]
        self.assertEqual(row["no_go_discipline"]["status"], "PASS")
        self.assertEqual(
            m.audit_summary_from_blob(audit)["no_go_discipline"]["status"],
            "PASS",
        )

    def test_hybrid_judicial_review_records_applyable_third_tuple(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)
        self._seed_one_row(
            "test_hybrid",
            audit_status="audit_in_progress",
            claim_type="positive_theorem",
            criticality="critical",
        )
        led = self.fx.read_ledger()
        led["rows"]["test_hybrid"]["cross_confirmation"] = {
            "status": "disagreement",
            "first_audit": {
                "auditor": "first-auditor",
                "auditor_family": "codex-gpt-5",
                "verdict": "audited_clean",
                "claim_type": "positive_theorem",
                "load_bearing_step_class": "C",
            },
            "second_audit": {
                "auditor": "second-auditor",
                "auditor_family": "codex-gpt-5.5",
                "verdict": "audited_clean",
                "claim_type": "bounded_theorem",
                "load_bearing_step_class": "A",
            },
        }
        audit = {
            "claim_id": "test_hybrid",
            "third_auditor": "second-stage-panel",
            "auditor_family": "codex-gpt-5.5",
            "auditor_model": "gpt-5.5",
            "auditor_reasoning_effort": "xhigh",
            "independence": "judicial_review",
            "sided_with": "hybrid",
            "ratified_verdict": "audited_clean",
            "ratified_claim_type": "bounded_theorem",
            "ratified_load_bearing_step_class": "C",
            "ratified_claim_scope": "bounded clean scope",
            "ratified_load_bearing_step": "bounded clean step",
            "judgment_rationale": "human-authorized panel selected a third applyable tuple",
            "first_auditor_error": "overstated claim type",
            "second_auditor_error": "understated load-bearing class",
            "hybrid_resolution_note": "human-authorized second-stage panel",
        }
        ok, msg = m.apply_one(led, audit)
        self.assertTrue(ok, msg)
        row = led["rows"]["test_hybrid"]
        self.assertEqual(row["cross_confirmation"]["status"], "third_confirmed_hybrid")
        self.assertEqual(row["cross_confirmation"]["third_audit"]["sided_with"], "hybrid")
        self.assertEqual(row["audit_status"], "audited_clean")
        self.assertEqual(row["claim_type"], "bounded_theorem")
        self.assertEqual(row["load_bearing_step_class"], "C")
        self.assertIsNone(row["blocker"])

    def test_judicial_no_go_requires_discipline_packet(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)
        self._seed_one_row(
            "test_judicial_no_go",
            audit_status="audit_in_progress",
            claim_type="no_go",
            note_body="# No-go obstruction\n",
        )
        led = self.fx.read_ledger()
        led["rows"]["test_judicial_no_go"]["cross_confirmation"] = {
            "status": "disagreement",
            "first_audit": {
                "auditor": "first-auditor",
                "auditor_family": "codex-gpt-5.6",
                "verdict": "audited_clean",
                "claim_type": "no_go",
                "claim_scope": "the obstruction",
                "load_bearing_step_class": "A",
            },
            "second_audit": {
                "auditor": "second-auditor",
                "auditor_family": "codex-gpt-5.6",
                "verdict": "audited_conditional",
                "claim_type": "no_go",
                "claim_scope": "the obstruction",
                "load_bearing_step_class": "A",
            },
        }
        judgment = {
            "claim_id": "test_judicial_no_go",
            "third_auditor": "panel-majority",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "judicial_review",
            "sided_with": "first",
            "ratified_verdict": "audited_clean",
            "ratified_claim_type": "no_go",
            "ratified_load_bearing_step_class": "A",
            "judgment_rationale": "the scoped obstruction closes",
            "first_auditor_error": "none on the scoped result",
            "second_auditor_error": "treated a supplied authority as absent",
        }

        before_rejected = json.dumps(led, sort_keys=True)
        ok, msg = m.apply_one(led, dict(judgment))
        self.assertFalse(ok)
        self.assertIn("N1-N8 packet is required", msg)
        self.assertEqual(json.dumps(led, sort_keys=True), before_rejected)

        judgment["no_go_discipline"] = _no_go_packet(
            evidence_path="docs/TEST_JUDICIAL_NO_GO.md",
            claim_id="test_judicial_no_go",
        )
        ok, msg = m.apply_one(led, judgment)
        self.assertTrue(ok, msg)
        self.assertEqual(
            led["rows"]["test_judicial_no_go"]["no_go_discipline"]["status"],
            "PASS",
        )

    def test_judicial_neither_validates_before_recording_blocker(self):
        m = _import("apply_audit")
        _patch_repo_root(m, self.tmp_root)
        self._seed_one_row(
            "test_judicial_neither_no_go",
            audit_status="audit_in_progress",
            claim_type="no_go",
            note_body="# No-go obstruction\n",
        )
        led = self.fx.read_ledger()
        led["rows"]["test_judicial_neither_no_go"]["cross_confirmation"] = {
            "status": "disagreement",
            "first_audit": {
                "auditor": "first-auditor",
                "auditor_family": "codex-gpt-5.6",
                "verdict": "audited_clean",
                "claim_type": "no_go",
                "claim_scope": "the scoped obstruction",
                "load_bearing_step_class": "A",
            },
            "second_audit": {
                "auditor": "second-auditor",
                "auditor_family": "codex-gpt-5.6",
                "verdict": "audited_conditional",
                "claim_type": "no_go",
                "claim_scope": "the scoped obstruction",
                "load_bearing_step_class": "A",
            },
        }
        judgment = {
            "claim_id": "test_judicial_neither_no_go",
            "third_auditor": "panel-neither",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "judicial_review",
            "sided_with": "neither",
            "ratified_verdict": "audited_conditional",
            "ratified_claim_type": "no_go",
            "ratified_claim_scope": "the scoped obstruction",
            "ratified_load_bearing_step_class": "A",
            "judgment_rationale": "both readings overstate the packet",
            "first_auditor_error": "overclosed",
            "second_auditor_error": "miscounted the walls",
        }
        before = json.dumps(led, sort_keys=True)
        ok, msg = m.apply_one(led, judgment)
        self.assertFalse(ok)
        self.assertIn("N1-N8 packet is required", msg)
        self.assertEqual(json.dumps(led, sort_keys=True), before)


class BuildCitationGraphParserTest(unittest.TestCase):
    """Parser behavior tests for _parse_script_imports — must detect bare
    PYTHONPATH-style imports (`from X import ...`, `import X`) when
    scripts/X.py exists, in addition to `from scripts.X import` and
    relative-form imports."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.scripts_dir = self.tmp_root / "scripts"
        self.scripts_dir.mkdir(parents=True, exist_ok=True)

    def _write(self, name: str, body: str) -> Path:
        p = self.scripts_dir / f"{name}.py"
        p.write_text(body, encoding="utf-8")
        return p

    def test_bare_from_import_is_detected_when_scripts_file_exists(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("helper_one", "x = 1\n")
            self._write("helper_two", "y = 2\n")
            primary = self._write(
                "primary",
                "from helper_one import x\n"
                "from helper_two import y\n"
                "import numpy as np\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"helper_one", "helper_two"})

    def test_bare_import_X_is_detected_when_scripts_file_exists(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("aliased_helper", "z = 3\n")
            primary = self._write(
                "primary",
                "import aliased_helper as alias\n"
                "import json\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"aliased_helper"})

    def test_third_party_imports_excluded(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            primary = self._write(
                "primary",
                "import numpy\n"
                "import scipy.linalg\n"
                "from math import sqrt\n"
                "from pathlib import Path\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, set())

    def test_existing_scripts_dot_prefix_form_still_works(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("prefixed_helper", "w = 4\n")
            primary = self._write(
                "primary",
                "from scripts.prefixed_helper import w\n"
                "import scripts.prefixed_helper\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"prefixed_helper"})

    def test_from_scripts_import_name_form_is_detected(self):
        # `from scripts import X [as Y]` must resolve to the imported module
        # X (the real name), not the package `scripts` nor the local alias Y.
        # This is the form the gate_b primary runners use
        # (`from scripts import gate_b_connectivity_tolerance as gate_b`).
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("gate_b_connectivity_tolerance", "K = 1\n")
            self._write("plain_helper", "v = 5\n")
            primary = self._write(
                "primary",
                "from scripts import gate_b_connectivity_tolerance as gate_b\n"
                "from scripts import plain_helper\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"gate_b_connectivity_tolerance", "plain_helper"})

    def test_static_dynamic_loader_paths_are_detected(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("dynamic_helper", "VALUE = 1\n")
            primary = self._write(
                "primary",
                "import importlib.util\n"
                "from pathlib import Path\n"
                "ROOT = Path(__file__).resolve().parents[1]\n"
                "HELPER = ROOT / 'scripts' / 'dynamic_helper.py'\n"
                "spec = importlib.util.spec_from_file_location('dynamic_helper', HELPER)\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"dynamic_helper"})

    def test_local_dynamic_loader_wrapper_paths_are_detected(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("wrapped_helper", "VALUE = 2\n")
            primary = self._write(
                "primary",
                "import importlib.util\n"
                "from pathlib import Path\n"
                "ROOT = Path(__file__).resolve().parents[1]\n"
                "WRAPPED = ROOT / 'scripts/wrapped_helper.py'\n"
                "def load_module(name, path):\n"
                "    return importlib.util.spec_from_file_location(name, path)\n"
                "load_module('wrapped_helper', WRAPPED)\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"wrapped_helper"})

    def test_load_frontier_filename_keyword_is_detected(self):
        m = _import("build_citation_graph")
        original = m.REPO_ROOT
        m.REPO_ROOT = self.tmp_root
        try:
            self._write("keyword_helper", "VALUE = 3\n")
            primary = self._write(
                "primary",
                "from _frontier_loader import load_frontier\n"
                "load_frontier('keyword_helper', filename='keyword_helper.py')\n",
            )
            helpers = m._parse_script_imports(primary)
        finally:
            m.REPO_ROOT = original
        self.assertEqual(helpers, {"keyword_helper"})


class SeedLedgerTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def test_archive_prior_audit_clears_audit_state_snapshot(self):
        # Regression test for issue #3 in the audit-framework review:
        # archive_prior_audit must clear audit_state_snapshot, not leave it
        # in place where it would confuse invalidate_stale_audits + lint.
        m = _import("seed_audit_ledger")
        row_with_snapshot = {
            "claim_id": "test",
            "audit_status": "audited_clean",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "audit_state_snapshot": {"criticality": "high", "deps": []},
            "previous_audits": [],
        }
        new_row = m.archive_prior_audit(dict(row_with_snapshot))
        # Snapshot should be in EMPTY_AUDIT (now None), not preserved
        self.assertIsNone(new_row.get("audit_state_snapshot"))
        # Prior values archived
        self.assertEqual(len(new_row["previous_audits"]), 1)
        self.assertEqual(
            new_row["previous_audits"][0]["auditor_model"], "gpt-5.6-sol"
        )
        self.assertEqual(
            new_row["previous_audits"][0]["auditor_reasoning_effort"], "xhigh"
        )
        self.assertIsNone(new_row["auditor_model"])
        self.assertIsNone(new_row["auditor_reasoning_effort"])

    def test_existing_unaudited_row_clears_stale_audit_residue(self):
        m = _import("seed_audit_ledger")
        _patch_repo_root(m, self.tmp_root)
        body = "# test\nClaim type: no_go\n"
        self.fx.write_note("docs/test.md", body)
        import hashlib
        note_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
        self.fx.write_graph(
            {
                "nodes": {
                    "test": {
                        "path": "docs/test.md",
                        "title": "test",
                        "runner_path": None,
                        "deps": [],
                        "note_hash": note_hash,
                        "claim_type_seed_hint": "no_go",
                        "claim_type_author_hint": None,
                        "claim_type_author_hint_raw": None,
                    }
                }
            }
        )
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "test": {
                        "claim_id": "test",
                        "note_path": "docs/test.md",
                        "title": "test",
                        "runner_path": None,
                        "deps": [],
                        "note_hash": note_hash,
                        "previous_audits": [
                            {
                                "verdict": "old",
                                "auditor": "stale-auditor",
                                "auditor_family": "codex-gpt-5",
                            }
                        ],
                        "audit_status": "unaudited",
                        "auditor": "stale-auditor",
                        "auditor_family": "codex-gpt-5",
                        "auditor_model": "gpt-5",
                        "auditor_reasoning_effort": "high",
                        "independence": "fresh_context",
                        "load_bearing_step": "stale step",
                        "chain_closes": True,
                        "audit_state_snapshot": {"criticality": "medium"},
                        "cross_confirmation": {"status": "confirmed"},
                        "claim_type": "positive_theorem",
                        "claim_type_provenance": "audited",
                        "claim_scope": "stale scope",
                    }
                },
            }
        )

        seeded = m.seed()
        row = seeded["rows"]["test"]

        self.assertEqual(row["audit_status"], "unaudited")
        self.assertIsNone(row["auditor"])
        self.assertIsNone(row["auditor_family"])
        self.assertIsNone(row["auditor_model"])
        self.assertIsNone(row["auditor_reasoning_effort"])
        self.assertIsNone(row["independence"])
        self.assertIsNone(row["load_bearing_step"])
        self.assertIsNone(row["chain_closes"])
        self.assertIsNone(row["audit_state_snapshot"])
        self.assertIsNone(row["cross_confirmation"])
        self.assertEqual(row["claim_type"], "no_go")
        self.assertEqual(row["claim_type_provenance"], "migration_hint")
        self.assertIsNone(row["claim_scope"])
        self.assertEqual(
            row["previous_audits"],
            [
                {
                    "verdict": "old",
                    "auditor": "stale-auditor",
                    "auditor_family": "codex-gpt-5",
                    "auditor_model": "gpt-5",
                    "auditor_reasoning_effort": "high",
                }
            ],
        )

    def test_unaudited_sole_history_recovers_exact_provenance_without_live_identity(self):
        m = _import("seed_audit_ledger")
        row = {
            "audit_status": "unaudited",
            "auditor": None,
            "auditor_family": None,
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "previous_audits": [
                {
                    "audit_status": "audited_clean",
                    "auditor": "archived-auditor",
                    "auditor_family": "codex-gpt-5.6",
                }
            ],
        }

        m.reset_unaudited_audit_fields(row)

        archived = row["previous_audits"][0]
        self.assertEqual(archived["auditor_model"], "gpt-5.6-sol")
        self.assertEqual(archived["auditor_reasoning_effort"], "xhigh")
        self.assertIsNone(row["auditor_model"])
        self.assertIsNone(row["auditor_reasoning_effort"])

    def test_unaudited_ambiguous_history_retains_unattributed_exact_provenance(self):
        m = _import("seed_audit_ledger")
        row = {
            "audit_status": "unaudited",
            "auditor": None,
            "auditor_family": None,
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "previous_audits": [
                {"audit_status": "audited_clean", "auditor": "first"},
                {"audit_status": "audited_conditional", "auditor": "second"},
            ],
        }

        m.reset_unaudited_audit_fields(row)

        self.assertNotIn("auditor_model", row["previous_audits"][0])
        self.assertNotIn("auditor_model", row["previous_audits"][1])
        self.assertEqual(
            row["unattributed_audit_provenance"],
            [
                {
                    "auditor_model": "gpt-5.6-sol",
                    "auditor_reasoning_effort": "xhigh",
                    "reason": "legacy_unaudited_exact_provenance_without_unique_history_match",
                }
            ],
        )
        self.assertIsNone(row["auditor_model"])
        self.assertIsNone(row["auditor_reasoning_effort"])

    def test_archived_failed_row_refreshes_note_hash(self):
        m = _import("seed_audit_ledger")
        _patch_repo_root(m, self.tmp_root)
        body = "# archived failed note\n\nRETRACTED.\n"
        note_path = "archive_unlanded/stale/NOTE.md"
        self.fx.write_note(note_path, body)
        import hashlib
        current_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
        self.fx.write_graph({"nodes": {}})
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "archived_failed": {
                        "claim_id": "archived_failed",
                        "note_path": note_path,
                        "title": "archived failed note",
                        "runner_path": None,
                        "deps": [],
                        "note_hash": "stalehash",
                        "previous_audits": [],
                        "audit_status": "audited_failed",
                        "claim_type": "no_go",
                        "claim_type_provenance": "audited",
                        "claim_scope": "archived failed scope",
                    }
                },
            }
        )

        seeded = m.seed()
        row = seeded["rows"]["archived_failed"]

        self.assertEqual(row["audit_status"], "audited_failed")
        self.assertEqual(row["note_hash"], current_hash)
        self.assertEqual(seeded["stats"]["preserved_archived_failed"], 1)

    def test_infra_path_prefixes_default_to_meta_when_hintless(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "META_SOURCE_PATTERNS", ()):
            for path in (
                "docs/ai_methodology/README.md",
                "docs/ai_methodology/raw/repo_audit.md",
                "docs/repo/anything.md",
                "docs/work_history/x/y.md",
                "docs/lanes/open_science/lane.md",
                "docs/publication/ci3_z3/table.md",
            ):
                claim_type, provenance = m.default_claim_type_for({"path": path})
                self.assertEqual(
                    (claim_type, provenance), ("meta", "backfilled_from_path"), path
                )

    def test_author_hint_beats_infra_path_prefix(self):
        # Lane docs and other hinted notes under infra directories keep
        # their declared types; the prefix tier only catches hint-less notes.
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "META_SOURCE_PATTERNS", ()):
            claim_type, provenance = m.default_claim_type_for(
                {
                    "path": "docs/lanes/open_science/lane.md",
                    "claim_type_author_hint": "open_gate",
                }
            )
            self.assertEqual((claim_type, provenance), ("open_gate", "author_hint"))
            claim_type, provenance = m.default_claim_type_for(
                {
                    "path": "docs/lanes/open_science/lane.md",
                    "claim_type_seed_hint": "open_gate",
                }
            )
            self.assertEqual((claim_type, provenance), ("open_gate", "migration_hint"))

    def test_meta_source_pattern_registry_beats_hint(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(
            m, "META_SOURCE_PATTERNS", ("docs/CANONICAL_HARNESS_INDEX.md",)
        ):
            claim_type, provenance = m.default_claim_type_for(
                {
                    "path": "docs/CANONICAL_HARNESS_INDEX.md",
                    "claim_type_author_hint": "positive_theorem",
                }
            )
            self.assertEqual((claim_type, provenance), ("meta", "backfilled_from_path"))

    def test_untyped_docs_root_note_still_defaults_to_positive_theorem(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "META_SOURCE_PATTERNS", ()):
            claim_type, provenance = m.default_claim_type_for(
                {"path": "docs/SOME_THEOREM_NOTE.md"}
            )
            self.assertEqual(
                (claim_type, provenance),
                ("positive_theorem", "default_positive_theorem"),
            )

    def test_gate_drops_unaudited_unknown_under_excluded_pattern(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "EXCLUDED_SOURCE_PATTERNS", ("docs/lanes/**",)), \
             mock.patch.object(m, "NEVER_GATE_SOURCE_PATHS", frozenset()):
            node = {"path": "docs/lanes/legacy_lane.md"}
            # Brand-new node: gated.
            self.assertTrue(m.should_gate_node(node, None))
            # Prior row that is an unaudited unknown: gated (history-free).
            prior = {"audit_status": "unaudited", "previous_audits": [],
                     "effective_status": "meta"}
            self.assertTrue(m.should_gate_node(node, prior))

    def test_gate_keeps_rows_with_audit_history(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "EXCLUDED_SOURCE_PATTERNS", ("docs/lanes/**",)), \
             mock.patch.object(m, "NEVER_GATE_SOURCE_PATHS", frozenset()):
            node = {"path": "docs/lanes/legacy_lane.md"}
            # Terminal or in-flight audit_status: kept.
            self.assertFalse(
                m.should_gate_node(node, {"audit_status": "audited_renaming"})
            )
            self.assertFalse(
                m.should_gate_node(node, {"audit_status": "audit_in_progress"})
            )
            # Archived previous_audits on an unaudited row: kept.
            self.assertFalse(
                m.should_gate_node(
                    node,
                    {"audit_status": "unaudited",
                     "previous_audits": [{"audit_status": "audited_clean"}]},
                )
            )

    def test_gate_respects_never_gate_pins_and_non_excluded_paths(self):
        m = _import("seed_audit_ledger")
        with mock.patch.object(m, "EXCLUDED_SOURCE_PATTERNS", ("docs/lanes/**",)), \
             mock.patch.object(
                 m, "NEVER_GATE_SOURCE_PATHS", frozenset({"docs/lanes/pinned.md"})
             ):
            self.assertFalse(m.should_gate_node({"path": "docs/lanes/pinned.md"}, None))
            self.assertFalse(m.should_gate_node({"path": "docs/REAL_NOTE.md"}, None))


class ComputeEffectiveStatusTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def test_clean_positive_with_clean_dep_is_retained(self):
        m = _import("compute_effective_status")
        rows = {
            "parent": {
                "claim_id": "parent",
                "deps": [],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "child": {
                "claim_id": "child",
                "deps": ["parent"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        new_rows, _cycles = m.compute_effective(rows)
        self.assertEqual(new_rows["parent"]["effective_status"], "retained")
        self.assertEqual(new_rows["child"]["effective_status"], "retained")

    def test_clean_with_unaudited_dep_is_pending_chain(self):
        m = _import("compute_effective_status")
        rows = {
            "parent": {
                "claim_id": "parent",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "positive_theorem",
            },
            "child": {
                "claim_id": "child",
                "deps": ["parent"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        new_rows, _cycles = m.compute_effective(rows)
        self.assertEqual(new_rows["child"]["effective_status"], "retained_pending_chain")

    def test_clean_with_metadata_dep_is_retained(self):
        """Metadata links are non-claim infrastructure and should not strand
        audited-clean theorem rows in retained_pending_chain."""
        m = _import("compute_effective_status")
        rows = {
            "glossary": {
                "claim_id": "glossary",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "meta",
            },
            "child": {
                "claim_id": "child",
                "deps": ["glossary"],
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
            },
        }
        new_rows, _cycles = m.compute_effective(rows)
        self.assertEqual(new_rows["glossary"]["effective_status"], "meta")
        self.assertEqual(new_rows["child"]["effective_status"], "retained_bounded")

    def test_only_axioms_and_primitives_satisfy_positive_theorem_chain(self):
        """Governance records and historical admissions remain blockers."""
        m = _import("compute_effective_status")
        rows = {
            "uses_minimal_axioms": {
                "claim_id": "uses_minimal_axioms",
                "deps": ["minimal_axioms"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "uses_scale_reference_primitive": {
                "claim_id": "uses_scale_reference_primitive",
                "deps": ["scale_reference_primitive"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "uses_open_obligation": {
                "claim_id": "uses_open_obligation",
                "deps": ["ac_orbit_obligation"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "uses_historical_admission": {
                "claim_id": "uses_historical_admission",
                "deps": ["historical_admission"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "ac_orbit_obligation": {
                "claim_id": "ac_orbit_obligation",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "open_gate",
            },
            "historical_admission": {
                "claim_id": "historical_admission",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "bounded_theorem",
            },
        }
        with mock.patch.object(
            m.premise_nodes,
            "is_axiom_premise",
            side_effect=lambda dep_id: dep_id
            in {"minimal_axioms", "scale_reference_primitive"},
        ):
            new_rows, _cycles = m.compute_effective(rows)
        self.assertEqual(
            new_rows["uses_minimal_axioms"]["effective_status"], "retained"
        )
        self.assertEqual(
            new_rows["uses_scale_reference_primitive"]["effective_status"],
            "retained",
        )
        self.assertEqual(
            new_rows["uses_open_obligation"]["effective_status"],
            "retained_pending_chain",
        )
        self.assertEqual(
            new_rows["uses_historical_admission"]["effective_status"],
            "retained_pending_chain",
        )
        self.assertEqual(
            new_rows["uses_open_obligation"]["effective_status_reason"],
            "chain_waiting_on:ac_orbit_obligation",
        )

    def test_metadata_dependencies_satisfy_clean_chain_without_bounding(self):
        """Metadata rows are stable audit-governance inputs. They satisfy a
        clean theorem's dependency chain without turning the theorem into
        retained_pending_chain without creating any admission-class exception."""
        m = _import("compute_effective_status")
        rows = {
            "key_terminology": {
                "claim_id": "key_terminology",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "meta",
            },
            "bounded_child": {
                "claim_id": "bounded_child",
                "deps": ["key_terminology"],
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
            },
            "positive_child": {
                "claim_id": "positive_child",
                "deps": ["key_terminology"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        new_rows, _cycles = m.compute_effective(rows)
        self.assertEqual(new_rows["key_terminology"]["effective_status"], "meta")
        self.assertEqual(
            new_rows["bounded_child"]["effective_status"], "retained_bounded"
        )
        self.assertEqual(
            new_rows["positive_child"]["effective_status"], "retained"
        )

    def test_criticality_bump_soft_reset_propagates_as_retained(self):
        """A row in the criticality-bump soft-reset state (audit_in_progress
        + awaiting_cross_confirmation + first_audit on file) keeps its
        effective_status at retained. Downstream rows depending on it stay
        retained — the criticality bump does not force them to re-audit."""
        m = _import("compute_effective_status")
        soft_reset_row = {
            "claim_id": "soft_reset_dep",
            "deps": [],
            "audit_status": "audit_in_progress",
            "blocker": "awaiting_cross_confirmation",
            "claim_type": "positive_theorem",
            "claim_type_provenance": "audited_pending_cross_confirmation_after_criticality_bump",
            "cross_confirmation": {
                "first_audit": {
                    "auditor": "auditor-1",
                    "auditor_family": "codex-gpt-5.5",
                    "independence": "cross_family",
                    "verdict": "audited_clean",
                    "claim_type": "positive_theorem",
                    "claim_scope": "test scope",
                    "load_bearing_step_class": "A",
                },
                "second_audit": None,
                "status": "awaiting_second",
            },
        }
        rows = {
            "soft_reset_dep": soft_reset_row,
            "child": {
                "claim_id": "child",
                "deps": ["soft_reset_dep"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(new_rows["soft_reset_dep"]["effective_status"], "retained")
        self.assertTrue(
            new_rows["soft_reset_dep"]["effective_status_reason"].startswith(
                "awaiting_cross_confirmation_after_criticality_bump:"
            )
        )
        # Child's chain still closes against the first-pass clean evidence.
        self.assertEqual(new_rows["child"]["effective_status"], "retained")

    def test_criticality_bump_soft_reset_with_disagreement_drops(self):
        """Once cross-confirmation disagrees, the soft-reset state ends and
        the row drops to audit_in_progress. Downstream rows then properly
        see the chain break and are flagged for re-audit."""
        m = _import("compute_effective_status")
        rows = {
            "disagreed_dep": {
                "claim_id": "disagreed_dep",
                "deps": [],
                "audit_status": "audit_in_progress",
                "blocker": "cross_confirmation_disagreement",  # not awaiting_cross_confirmation
                "claim_type": "positive_theorem",
                "claim_type_provenance": "audited_pending_cross_confirmation_after_criticality_bump",
                "cross_confirmation": {
                    "first_audit": {"verdict": "audited_clean"},
                    "second_audit": {"verdict": "audited_conditional"},
                    "status": "disagreement",
                },
            },
            "child": {
                "claim_id": "child",
                "deps": ["disagreed_dep"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(new_rows["disagreed_dep"]["effective_status"], "audit_in_progress")
        self.assertEqual(new_rows["child"]["effective_status"], "retained_pending_chain")

    def test_born_critical_first_pass_does_not_trigger_soft_reset_path(self):
        """A born-critical claim in first-pass audit_in_progress (NOT from a
        criticality bump) keeps the standard audit_in_progress effective_status.
        The soft-reset path requires the specific provenance flag set by
        invalidate_stale_audits.py — apply_audit.py uses a different
        provenance for first-pass rows."""
        m = _import("compute_effective_status")
        rows = {
            "born_critical": {
                "claim_id": "born_critical",
                "deps": [],
                "audit_status": "audit_in_progress",
                "blocker": "awaiting_cross_confirmation",
                "claim_type": "positive_theorem",
                "claim_type_provenance": "audited_pending_cross_confirmation",  # NOT the bump suffix
                "cross_confirmation": {
                    "first_audit": {"verdict": "audited_clean"},
                    "second_audit": None,
                    "status": "awaiting_second",
                },
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(new_rows["born_critical"]["effective_status"], "audit_in_progress")

    def test_decoration_under_retained_counts_as_retained_grade(self):
        """A clean theorem whose only dep is a decoration_under_<retained_parent>
        must promote to retained-grade. The decoration's effective_status is
        only assigned when the parent is itself retained-grade, so it inherits
        retention and is_retained_grade() must honor that for chain closure."""
        m = _import("compute_effective_status")
        rows = {
            "root": {
                "claim_id": "root",
                "deps": [],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "decoration_child": {
                "claim_id": "decoration_child",
                "deps": ["root"],
                "audit_status": "audited_decoration",
                "claim_type": "decoration",
                "decoration_parent_claim_id": "root",
            },
            "downstream_theorem": {
                "claim_id": "downstream_theorem",
                "deps": ["decoration_child"],
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(new_rows["root"]["effective_status"], "retained")
        self.assertEqual(
            new_rows["decoration_child"]["effective_status"],
            "decoration_under_root",
        )
        self.assertEqual(
            new_rows["downstream_theorem"]["effective_status"],
            "retained_bounded",
        )

    def test_chained_decoration_under_retained_resolves(self):
        """A decoration whose parent is itself a decoration_under_<retained_root>
        must resolve to decoration_under_<parent>, not retained_pending_chain.
        Chained decorations preserve retention down the chain."""
        m = _import("compute_effective_status")
        rows = {
            "root": {
                "claim_id": "root",
                "deps": [],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
            "decoration_mid": {
                "claim_id": "decoration_mid",
                "deps": ["root"],
                "audit_status": "audited_decoration",
                "claim_type": "decoration",
                "decoration_parent_claim_id": "root",
            },
            "decoration_leaf": {
                "claim_id": "decoration_leaf",
                "deps": ["decoration_mid"],
                "audit_status": "audited_decoration",
                "claim_type": "decoration",
                "decoration_parent_claim_id": "decoration_mid",
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(
            new_rows["decoration_mid"]["effective_status"],
            "decoration_under_root",
        )
        self.assertEqual(
            new_rows["decoration_leaf"]["effective_status"],
            "decoration_under_decoration_mid",
        )

    def test_decoration_under_non_retained_does_not_promote(self):
        """If the decoration's parent is NOT retained-grade (e.g. unaudited),
        the decoration row stays retained_pending_chain. The relaxation only
        applies to decoration_under_<X> where X is itself retained-grade."""
        m = _import("compute_effective_status")
        rows = {
            "unaudited_root": {
                "claim_id": "unaudited_root",
                "deps": [],
                "audit_status": "unaudited",
                "claim_type": "positive_theorem",
            },
            "decoration_child": {
                "claim_id": "decoration_child",
                "deps": ["unaudited_root"],
                "audit_status": "audited_decoration",
                "claim_type": "decoration",
                "decoration_parent_claim_id": "unaudited_root",
            },
            "downstream_theorem": {
                "claim_id": "downstream_theorem",
                "deps": ["decoration_child"],
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
            },
        }
        new_rows, _ = m.compute_effective(rows)
        self.assertEqual(
            new_rows["decoration_child"]["effective_status"],
            "retained_pending_chain",
        )
        self.assertEqual(
            new_rows["downstream_theorem"]["effective_status"],
            "retained_pending_chain",
        )

    def test_main_drops_stale_top_level_timestamp_keys(self):
        m = _import("compute_effective_status")
        _patch_repo_root(m, self.tmp_root)
        ledger = {
            "schema_version": 1,
            "generated_at": "2026-01-01T00:00:00+00:00",
            "effective_status_computed_at": "2026-01-01T00:00:00+00:00",
            "load_bearing_computed_at": "2026-01-01T00:00:00+00:00",
            "invalidation_run_at": "2026-01-01T00:00:00+00:00",
            "rows": {},
        }
        self.fx.write_ledger(ledger)
        m.main()
        post = self.fx.read_ledger()
        for stale in ("generated_at", "effective_status_computed_at",
                      "load_bearing_computed_at", "invalidation_run_at"):
            self.assertNotIn(stale, post)


class SanitizeLegacyAuditArtifactsTest(unittest.TestCase):
    def test_bare_uppercase_decoration_parent_stem_canonicalizes(self):
        m = _import("sanitize_legacy_audit_artifacts")
        ledger = {
            "rows": {
                "cl3_complexification_split_narrow_theorem_note_2026-05-10": {
                    "claim_id": "cl3_complexification_split_narrow_theorem_note_2026-05-10",
                    "note_path": "docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md",
                },
                "decoration_child": {
                    "claim_id": "decoration_child",
                    "note_path": "docs/DECORATION_CHILD.md",
                    "decoration_parent_claim_id": "CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10",
                },
            }
        }
        m.canonicalize_decoration_parent_ids(ledger)
        self.assertEqual(
            ledger["rows"]["decoration_child"]["decoration_parent_claim_id"],
            "cl3_complexification_split_narrow_theorem_note_2026-05-10",
        )


class ComputeAuditorReliabilityTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def test_cross_confirmation_counts_actual_participants(self):
        m = _import("compute_auditor_reliability")
        _patch_repo_root(m, self.tmp_root)
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "confirmed_cross_family": {
                        "claim_id": "confirmed_cross_family",
                        "audit_status": "audited_clean",
                        "auditor_family": "codex-gpt-5",
                        "criticality": "leaf",
                        "cross_confirmation": {
                            "status": "confirmed",
                            "first_audit": {
                                "auditor_family": "codex-gpt-5.5",
                                "verdict": "audited_clean",
                            },
                            "second_audit": {
                                "auditor_family": "codex-gpt-5",
                                "verdict": "audited_clean",
                            },
                        },
                    },
                    "third_pass_cross_family": {
                        "claim_id": "third_pass_cross_family",
                        "audit_status": "audited_conditional",
                        "auditor_family": "codex-gpt-5",
                        "criticality": "leaf",
                        "cross_confirmation": {
                            "status": "third_confirmed_second",
                            "first_audit": {
                                "auditor_family": "codex-gpt-5.5",
                                "verdict": "audited_clean",
                            },
                            "second_audit": {
                                "auditor_family": "codex-gpt-5",
                                "verdict": "audited_conditional",
                            },
                            "third_audit": {
                                "auditor_family": "codex-gpt-5",
                                "verdict": "audited_conditional",
                            },
                        },
                    },
                },
            }
        )

        self.assertEqual(m.main(), 0)
        out = json.loads(
            (self.fx.data_dir / "auditor_reliability.json").read_text(encoding="utf-8")
        )
        gpt5 = out["auditor_family_summary"]["codex-gpt-5"]
        gpt55 = out["auditor_family_summary"]["codex-gpt-5.5"]

        self.assertEqual(gpt5["cross_confirmation_pairs_seen"], 2)
        self.assertEqual(gpt55["cross_confirmation_pairs_seen"], 2)
        self.assertEqual(gpt5["cross_confirmation_pairs_agreed_first_try"], 1)
        self.assertEqual(gpt55["cross_confirmation_pairs_agreed_first_try"], 1)
        self.assertEqual(gpt55["bias_direction_breakdown"]["more_lenient"], 1)
        self.assertEqual(out["totals"]["total_cross_confirmation_pairs"], 2)
        self.assertEqual(out["totals"]["total_cross_confirmation_family_participations"], 4)
        self.assertEqual(out["totals"]["overall_agreement_rate"], 0.5)


class AuditLintTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _write_minimal_ledger(self, rows: dict) -> None:
        # Provide a synthetic citation_graph.json so the cycle scan does
        # not blow up.
        graph_nodes = {
            cid: {"deps": list(row.get("deps") or [])}
            for cid, row in rows.items()
        }
        self.fx.write_graph({"nodes": graph_nodes, "edges": []})
        # Each row needs note_path that exists on disk + matching note_hash
        import hashlib
        for cid, row in rows.items():
            np = row.get("note_path") or f"docs/{cid}.md"
            row["note_path"] = np
            body = row.get("_body", f"# {cid}\n")
            row.pop("_body", None)
            (self.tmp_root / np).parent.mkdir(parents=True, exist_ok=True)
            (self.tmp_root / np).write_text(body, encoding="utf-8")
            row["note_hash"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
            row.setdefault("deps", [])
        self.fx.write_ledger({"schema_version": 1, "rows": rows})

    def test_front_door_current_markdown_link_passes(self):
        m = _import("audit_lint")
        errors = m.front_door_axiom_pointer_errors(
            "docs/START_HERE.md",
            "See [the current axioms](MINIMAL_AXIOMS_2026-06-29.md#scope).\n",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            ["docs/MINIMAL_AXIOMS_2026-06-05.md"],
        )
        self.assertEqual(errors, [])

    def test_owner_governed_class_counts_match_nodes_and_atoms(self):
        m = _import("audit_lint")
        registry = {
            "owner_governed_premise_node_count": 1,
            "owner_governed_residual_atom_count": 2,
            "nodes": {
                "ac": {
                    "adopted_residual_candidates": ["ac_i", "ac_ii"],
                }
            },
        }
        self.assertEqual(m.owner_governed_count_errors(registry), [])

        registry["owner_governed_premise_node_count"] = 0
        self.assertEqual(
            m.owner_governed_count_errors(registry),
            [
                "owner_governed_premise_nodes.json "
                "owner_governed_premise_node_count must equal nodes"
            ],
        )

        registry["owner_governed_premise_node_count"] = 1
        registry["owner_governed_residual_atom_count"] = 0
        self.assertEqual(
            m.owner_governed_count_errors(registry),
            [
                "owner_governed_premise_nodes.json "
                "owner_governed_residual_atom_count must equal "
                "adopted_residual_candidates across nodes"
            ],
        )

    def test_lint_validates_live_and_cross_confirmation_no_go_packets(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        live_path = "docs/linted_no_go.md"
        rows = {
            "linted_no_go": {
                "claim_id": "linted_no_go",
                "note_path": live_path,
                "_body": "# No-go obstruction\n",
                "audit_status": "audited_clean",
                "claim_type": "no_go",
                "claim_scope": "the scoped obstruction",
                "chain_closes": True,
                "effective_status": "retained_no_go",
                "auditor": "lint-auditor",
                "auditor_family": "codex-gpt-5.6",
                "auditor_model": "gpt-5.6-sol",
                "auditor_reasoning_effort": "xhigh",
                "independence": "cross_family",
                "criticality": "leaf",
                "load_bearing_step_class": "A",
                "no_go_discipline": _no_go_packet(
                    evidence_path=live_path, claim_id="linted_no_go"
                ),
            }
        }
        self._write_minimal_ledger(rows)
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 0, buf.getvalue())

        bad = _no_go_packet(evidence_path=live_path, claim_id="linted_no_go")
        bad["N7_steelman"]["resolved"] = False
        ledger = self.fx.read_ledger()
        ledger["rows"]["linted_no_go"]["cross_confirmation"] = {
            "status": "awaiting_second",
            "first_audit": {
                "auditor": "first-auditor",
                "auditor_family": "codex-gpt-5.6",
                "verdict": "audited_clean",
                "claim_type": "no_go",
                "claim_scope": "the scoped obstruction",
                "load_bearing_step_class": "A",
                "no_go_discipline": bad,
            },
            "second_audit": None,
        }
        self.fx.write_ledger(ledger)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 1)
        self.assertIn("cross_confirmation.first_audit invalid", buf.getvalue())

    def test_lint_allows_schema_old_no_go_packet_in_non_authoritative_history(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        packet = _no_go_packet()
        del packet["N3_hidden_wall_scan"]["scan_scope"]
        rows = {
            "migrated_history": {
                "claim_id": "migrated_history",
                "_body": "# Historical packet holder\n",
                "audit_status": "unaudited",
                "effective_status": "unaudited",
                "claim_type": "positive_theorem",
                "criticality": "leaf",
                "previous_audits": [{
                    "audit_status": "audited_clean",
                    "claim_type": "no_go",
                    "claim_scope": "legacy negative scope",
                    "no_go_discipline": packet,
                    "invalidation_reason": "dep_weakened:authority:retained->unaudited",
                }],
            }
        }
        self._write_minimal_ledger(rows)
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn("archived_invalid_no_go_packet", buf.getvalue())

    def test_front_door_prose_or_code_path_does_not_count(self):
        m = _import("audit_lint")
        errors = m.front_door_axiom_pointer_errors(
            "README.md",
            "Current memo: `docs/MINIMAL_AXIOMS_2026-06-29.md`.\n",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            ["docs/MINIMAL_AXIOMS_2026-06-05.md"],
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("does not cite the current axiom memo", errors[0])

    def test_front_door_nonrendered_markdown_links_do_not_count(self):
        m = _import("audit_lint")
        current = "docs/MINIMAL_AXIOMS_2026-06-29.md"
        examples = (
            "`[example](docs/MINIMAL_AXIOMS_2026-06-29.md)`\n",
            "```md\n[example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n```\n",
            "<!-- [example](docs/MINIMAL_AXIOMS_2026-06-29.md) -->\n",
            "\\[example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "> ~~~md\n> [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n> ~~~\n",
            "> ```md\n> [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n> ````\n",
            "    [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            ">\n>     [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "- item\n\n        [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "- item\n\n>     [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "-     [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "1.     [example](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
        )
        for text in examples:
            with self.subTest(text=text):
                errors = m.front_door_axiom_pointer_errors(
                    "README.md", text, current, []
                )
                self.assertEqual(len(errors), 1)
                self.assertIn("does not cite the current axiom memo", errors[0])

    def test_front_door_rendered_links_in_continuations_count(self):
        m = _import("audit_lint")
        current = "docs/MINIMAL_AXIOMS_2026-06-29.md"
        examples = (
            "\\`[current](docs/MINIMAL_AXIOMS_2026-06-29.md)\\`\n",
            "Paragraph\n    [current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "- item\n    [current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "- item\n\n    [current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "-    [current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
            "1.    [current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n",
        )
        for text in examples:
            with self.subTest(text=text):
                self.assertEqual(
                    m.front_door_axiom_pointer_errors(
                        "README.md", text, current, []
                    ),
                    [],
                )

    def test_front_door_superseded_link_after_blank_list_paragraph_fails(self):
        m = _import("audit_lint")
        errors = m.front_door_axiom_pointer_errors(
            "README.md",
            "[current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n\n"
            "- item\n\n"
            "    [old](docs/MINIMAL_AXIOMS_2026-06-05.md)\n",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            ["docs/MINIMAL_AXIOMS_2026-06-05.md"],
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("cites superseded axiom memo", errors[0])

    def test_front_door_backslash_does_not_escape_code_span_closer(self):
        m = _import("audit_lint")
        errors = m.front_door_axiom_pointer_errors(
            "README.md",
            "[current](docs/MINIMAL_AXIOMS_2026-06-29.md)\n\n"
            "`code\\` [old](docs/MINIMAL_AXIOMS_2026-06-05.md) `\n",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            ["docs/MINIMAL_AXIOMS_2026-06-05.md"],
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("cites superseded axiom memo", errors[0])

    def test_front_door_superseded_markdown_link_fails(self):
        m = _import("audit_lint")
        errors = m.front_door_axiom_pointer_errors(
            "README.md",
            "[current](docs/MINIMAL_AXIOMS_2026-06-29.md) and "
            "[old](docs/MINIMAL_AXIOMS_2026-06-05.md)\n",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            ["docs/MINIMAL_AXIOMS_2026-06-05.md"],
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("cites superseded axiom memo", errors[0])

    def test_conditional_without_repair_class_warns(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "test_cond": {
                "claim_id": "test_cond",
                "audit_status": "audited_conditional",
                "claim_type": "positive_theorem",
                "claim_scope": "real scope here",
                "effective_status": "audited_conditional",
                "notes_for_re_audit_if_any": "re-audit when X is closed",
                "auditor_family": "codex-gpt-5.5",
                "criticality": "leaf",
            },
        }
        self._write_minimal_ledger(rows)
        # Capture stdout
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        out = buf.getvalue()
        # Should pass (warnings only) but include a warning about repair-class
        self.assertEqual(rc, 0)
        self.assertIn("audited_conditional notes_for_re_audit_if_any", out)

    def test_backfill_scope_reports_notice_not_warning(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "legacy_scope": {
                "claim_id": "legacy_scope",
                "audit_status": "audited_conditional",
                "claim_type": "positive_theorem",
                "claim_scope": f"{m.BACKFILL_SCOPE_PREFIX}; placeholder",
                "effective_status": "audited_conditional",
                "notes_for_re_audit_if_any": "missing_bridge_theorem: repair",
                "auditor_family": "codex-gpt-5.5",
                "criticality": "leaf",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        out = buf.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("legacy_backfill_scope", out)
        self.assertIn("notices", out)
        self.assertNotIn("warnings:", out)

    def test_legacy_auditor_family_warns(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "legacy": {
                "claim_id": "legacy",
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
                "claim_scope": "real scope",
                "effective_status": "retained",
                "auditor_family": "codex-current",  # legacy
                "auditor": "x",
                "criticality": "leaf",
                "load_bearing_step_class": "C",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            m.main()
        self.assertIn("legacy", buf.getvalue())
        self.assertIn("codex-current", buf.getvalue())

    def test_lint_allows_retained_row_with_metadata_dep(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "glossary": {
                "claim_id": "glossary",
                "audit_status": "unaudited",
                "claim_type": "meta",
                "effective_status": "meta",
                "criticality": "leaf",
            },
            "bounded_child": {
                "claim_id": "bounded_child",
                "deps": ["glossary"],
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
                "claim_scope": "bounded theorem with glossary link",
                "effective_status": "retained_bounded",
                "auditor": "synthetic-auditor",
                "auditor_family": "codex-gpt-5.5",
                "criticality": "leaf",
                "load_bearing_step_class": "A",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 0)
        self.assertNotIn("bounded_child: effective_status", buf.getvalue())

    def test_stale_top_level_timestamp_errors(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        # Build empty rows ledger but with stale timestamp key
        self.fx.write_graph({"nodes": {}, "edges": []})
        ledger = {
            "schema_version": 1,
            "generated_at": "2026-01-01T00:00:00+00:00",
            "rows": {},
        }
        self.fx.write_ledger(ledger)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 1)
        self.assertIn("stale timestamp key", buf.getvalue())

    def test_retained_grade_row_may_depend_on_metadata(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "key_terminology": {
                "claim_id": "key_terminology",
                "audit_status": "unaudited",
                "claim_type": "meta",
                "effective_status": "meta",
            },
            "clean_bounded": {
                "claim_id": "clean_bounded",
                "audit_status": "audited_clean",
                "claim_type": "bounded_theorem",
                "claim_scope": "bounded theorem whose only dep is metadata",
                "effective_status": "retained_bounded",
                "deps": ["key_terminology"],
                "auditor": "unit-test-auditor",
                "auditor_family": "codex-gpt-5.5",
                "criticality": "leaf",
                "load_bearing_step_class": "A",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        self.assertEqual(rc, 0, buf.getvalue())

    def test_defaulted_claim_type_warns_but_passes(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "untyped_catalog": {
                "claim_id": "untyped_catalog",
                "audit_status": "unaudited",
                "claim_type": "positive_theorem",
                "claim_type_provenance": "default_positive_theorem",
                "effective_status": "unaudited",
                "criticality": "leaf",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        out = buf.getvalue()
        self.assertEqual(rc, 0, out)
        self.assertIn("claim_type_defaulted", out)
        self.assertIn("'Type:' header", out)

    def test_typed_rows_do_not_trigger_defaulted_warning(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        rows = {
            "typed_note": {
                "claim_id": "typed_note",
                "audit_status": "unaudited",
                "claim_type": "bounded_theorem",
                "claim_type_provenance": "author_hint",
                "effective_status": "unaudited",
                "criticality": "leaf",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        out = buf.getvalue()
        self.assertEqual(rc, 0, out)
        self.assertNotIn("claim_type_defaulted", out)

    def test_grandfathered_excluded_path_row_notices(self):
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        (self.tmp_root / "docs" / "audit" / "data" / "excluded_source_patterns.txt").write_text(
            "# infra families\ndocs/lanes/**\n", encoding="utf-8"
        )
        rows = {
            # History-free unaudited unknown: drops at the next seeding run.
            "lanes.legacy_lane": {
                "claim_id": "lanes.legacy_lane",
                "note_path": "docs/lanes/legacy_lane.md",
                "audit_status": "unaudited",
                "claim_type": "open_gate",
                "claim_type_provenance": "migration_hint",
                "effective_status": "unaudited",
                "criticality": "leaf",
            },
            # Archived audit history: kept by history-preserving exclusion.
            "lanes.audited_lane": {
                "claim_id": "lanes.audited_lane",
                "note_path": "docs/lanes/audited_lane.md",
                "audit_status": "unaudited",
                "previous_audits": [{"audit_status": "audited_clean"}],
                "claim_type": "open_gate",
                "claim_type_provenance": "migration_hint",
                "effective_status": "unaudited",
                "criticality": "leaf",
            },
        }
        self._write_minimal_ledger(rows)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.main()
        out = buf.getvalue()
        self.assertEqual(rc, 0, out)
        self.assertIn("excluded_path_row_pending_drop", out)
        self.assertIn("lanes.legacy_lane", out)
        self.assertIn("excluded_path_row_grandfathered", out)
        self.assertIn("lanes.audited_lane", out)
        self.assertNotIn("warnings:", out)


class CheckStagedClaimTypingTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _run(self, m, staged: str) -> tuple[int, str]:
        import io, contextlib
        buf = io.StringIO()
        with mock.patch.object(sys, "stdin", io.StringIO(staged)):
            with contextlib.redirect_stdout(buf):
                rc = m.main()
        return rc, buf.getvalue()

    def _patch_paths(self, m) -> None:
        m.REPO_ROOT = self.tmp_root
        m.LEDGER_PATH = self.tmp_root / "docs" / "audit" / "data" / "audit_ledger.json"

    def test_staged_defaulted_note_blocks(self):
        m = _import("check_staged_claim_typing")
        self._patch_paths(m)
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "untyped": {
                        "claim_id": "untyped",
                        "note_path": "docs/UNTYPED_NOTE.md",
                        "claim_type": "positive_theorem",
                        "claim_type_provenance": "default_positive_theorem",
                    },
                },
            }
        )
        rc, out = self._run(m, "docs/UNTYPED_NOTE.md\nscripts/foo.py\n")
        self.assertEqual(rc, 1)
        self.assertIn("docs/UNTYPED_NOTE.md", out)
        self.assertIn("'Type:' header", out)

    def test_typed_and_unledgered_notes_pass(self):
        m = _import("check_staged_claim_typing")
        self._patch_paths(m)
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "typed": {
                        "claim_id": "typed",
                        "note_path": "docs/TYPED_NOTE.md",
                        "claim_type": "bounded_theorem",
                        "claim_type_provenance": "author_hint",
                    },
                },
            }
        )
        rc, _ = self._run(m, "docs/TYPED_NOTE.md\ndocs/publication/gated_infra.md\n")
        self.assertEqual(rc, 0)

    def test_no_staged_docs_short_circuits(self):
        m = _import("check_staged_claim_typing")
        self._patch_paths(m)
        # No ledger written at all: the gate must not fail on non-doc commits.
        rc, _ = self._run(m, "scripts/foo.py\nlogs/runner-cache/x.json\n")
        self.assertEqual(rc, 0)


class InvalidateStaleAuditsCriticalityBumpTest(unittest.TestCase):
    """Per FRESH_LOOK_REQUIREMENTS.md §4, criticality bumps fall into three
    cases:

    - 'noop': the existing audit already qualifies, OR the verdict is
      terminal-non-clean (cross-confirmation doesn't apply).
    - 'soft_reset': audited_clean + non-weak independence + bump to
      critical without cross-confirmation. Mirrors apply_audit's
      first-pass flow: audit_in_progress + awaiting_cross_confirmation,
      first-audit evidence preserved as cross_confirmation.first_audit.
    - 'invalidate': audit fundamentally fails the new tier
      (e.g. weak independence bumping to high/critical).
    """

    def _categorize(self, *, audit_status="audited_clean", indep, cc_status, target):
        m = _import("invalidate_stale_audits")
        row = {"audit_status": audit_status, "independence": indep}
        if cc_status is not None:
            row["cross_confirmation"] = {"status": cc_status}
        return m._categorize_criticality_bump(row, target)

    def test_hard_invalidation_archives_and_clears_exact_model_provenance(self):
        m = _import("invalidate_stale_audits")
        row = {
            "claim_id": "test",
            "audit_status": "audited_clean",
            "auditor": "unique-auditor",
            "auditor_family": "codex-gpt-5.6",
            "auditor_model": "gpt-5.6-sol",
            "auditor_reasoning_effort": "xhigh",
            "independence": "cross_family",
            "claim_type": "bounded_theorem",
            "claim_type_author_hint": "bounded_theorem",
            "previous_audits": [],
        }
        reset = m.archive_and_reset(row, "note_hash_changed:old->new")
        archived = reset["previous_audits"][-1]
        self.assertEqual(archived["auditor_model"], "gpt-5.6-sol")
        self.assertEqual(archived["auditor_reasoning_effort"], "xhigh")
        self.assertIsNone(reset["auditor_model"])
        self.assertIsNone(reset["auditor_reasoning_effort"])

    def test_bump_to_medium_is_always_noop(self):
        # No special requirement at medium. Even weak audits stay live.
        self.assertEqual(self._categorize(indep="weak", cc_status=None, target="medium"), "noop")
        self.assertEqual(self._categorize(indep=None, cc_status=None, target="medium"), "noop")
        self.assertEqual(
            self._categorize(audit_status="audited_conditional", indep="cross_family",
                             cc_status=None, target="medium"),
            "noop",
        )

    def test_bump_to_high_with_non_weak_indep_is_noop(self):
        for indep in ("cross_family", "fresh_context", "strong"):
            self.assertEqual(self._categorize(indep=indep, cc_status=None, target="high"), "noop")

    def test_bump_to_high_with_weak_indep_invalidates(self):
        self.assertEqual(self._categorize(indep="weak", cc_status=None, target="high"), "invalidate")
        self.assertEqual(self._categorize(indep=None, cc_status=None, target="high"), "invalidate")

    def test_bump_to_critical_with_cross_confirmation_is_noop(self):
        for cc in ("confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"):
            self.assertEqual(
                self._categorize(indep="cross_family", cc_status=cc, target="critical"),
                "noop",
            )

    def test_bump_to_critical_with_weak_indep_invalidates(self):
        # Independence floor cannot be salvaged by cross-confirmation.
        self.assertEqual(
            self._categorize(indep="weak", cc_status="confirmed", target="critical"),
            "invalidate",
        )
        self.assertEqual(
            self._categorize(indep=None, cc_status=None, target="critical"),
            "invalidate",
        )

    def test_bump_to_critical_clean_no_cc_is_soft_reset(self):
        # The user's case: audited_clean + non-weak indep + bump to critical
        # without cross-confirmation -> soft reset, not full invalidate.
        self.assertEqual(
            self._categorize(indep="cross_family", cc_status=None, target="critical"),
            "soft_reset",
        )
        self.assertEqual(
            self._categorize(indep="fresh_context", cc_status=None, target="critical"),
            "soft_reset",
        )
        self.assertEqual(
            self._categorize(indep="cross_family", cc_status="awaiting_second", target="critical"),
            "soft_reset",
        )

    def test_terminal_non_clean_verdict_bumps_are_noops(self):
        # Cross-confirmation doesn't apply to non-clean verdicts; criticality
        # bump leaves them in their final state.
        for status in ("audited_conditional", "audited_numerical_match",
                       "audited_renaming", "audited_decoration", "audited_failed"):
            self.assertEqual(
                self._categorize(audit_status=status, indep="cross_family",
                                 cc_status=None, target="critical"),
                "noop",
                f"terminal verdict {status} should be noop",
            )

    def test_detect_invalidation_emits_distinct_reason_prefixes(self):
        m = _import("invalidate_stale_audits")
        with mock.patch.object(m.rc, "runner_sha256", return_value=None):
            base_snap = {
                "criticality": "high",
                "deps": [],
                "dep_effective_status": {},
                "runner_hash": None,
            }
            # Soft reset path: audited_clean + cross_family + bump to critical, no cc.
            row_soft = {
                "audit_status": "audited_clean",
                "deps": [],
                "criticality": "critical",
                "independence": "cross_family",
                "cross_confirmation": None,
                "audit_state_snapshot": base_snap,
            }
            reason = m.detect_invalidation(row_soft, {})
            self.assertIsNotNone(reason)
            self.assertTrue(reason.startswith("criticality_soft_reset:high->critical"))

            # Hard invalidate path: weak indep at high.
            row_hard = {
                "audit_status": "audited_clean",
                "deps": [],
                "criticality": "high",
                "independence": "weak",
                "cross_confirmation": None,
                "audit_state_snapshot": {**base_snap, "criticality": "leaf"},
            }
            reason = m.detect_invalidation(row_hard, {})
            self.assertIsNotNone(reason)
            self.assertTrue(reason.startswith("criticality_increased:leaf->high"))

            # Noop path: audited_clean + cross_family + bump to high.
            row_noop = {
                "audit_status": "audited_clean",
                "deps": [],
                "criticality": "high",
                "independence": "cross_family",
                "cross_confirmation": None,
                "audit_state_snapshot": {**base_snap, "criticality": "leaf"},
            }
            self.assertIsNone(m.detect_invalidation(row_noop, {}))

    def test_soft_reset_preserves_audit_evidence_as_first_audit(self):
        """A soft reset must mirror apply_audit's first-pass flow: clean
        evidence stays live as cross_confirmation.first_audit, audit_status
        flips to audit_in_progress + awaiting_cross_confirmation."""
        m = _import("invalidate_stale_audits")
        row = {
            "audit_status": "audited_clean",
            "auditor": "test-auditor-1",
            "auditor_family": "codex-gpt-5.5",
            "auditor_model": "gpt-5.5",
            "auditor_reasoning_effort": "xhigh",
            "independence": "cross_family",
            "audit_date": "2026-05-09T10:00:00+00:00",
            "claim_type": "positive_theorem",
            "claim_scope": "test scope",
            "load_bearing_step_class": "A",
            "cross_confirmation": None,
            "previous_audits": [],
        }
        out = m.soft_reset_to_cross_confirmation_pending(
            row, "criticality_soft_reset:high->critical"
        )
        self.assertEqual(out["audit_status"], "audit_in_progress")
        self.assertEqual(out["blocker"], "awaiting_cross_confirmation")
        self.assertEqual(out["claim_type_provenance"], "audited_pending_cross_confirmation_after_criticality_bump")
        cc = out["cross_confirmation"]
        self.assertEqual(cc["status"], "awaiting_second")
        self.assertIsNone(cc["second_audit"])
        first = cc["first_audit"]
        self.assertEqual(first["auditor"], "test-auditor-1")
        self.assertEqual(first["auditor_family"], "codex-gpt-5.5")
        self.assertEqual(first["independence"], "cross_family")
        self.assertEqual(first["claim_type"], "positive_theorem")
        self.assertEqual(first["claim_scope"], "test scope")
        self.assertEqual(first["load_bearing_step_class"], "A")
        self.assertEqual(first["verdict"], "audited_clean")
        # The clean evidence must NOT be archived to previous_audits — it
        # is still live as the first audit. apply_audit's first-pass flow
        # also doesn't archive on first-pass.
        self.assertEqual(out["previous_audits"], [])
        # The auditor + claim_type fields must remain on the live row
        # (the cross-confirmation second pass needs them for comparison).
        self.assertEqual(out["auditor"], "test-auditor-1")
        self.assertEqual(out["claim_type"], "positive_theorem")
        self.assertEqual(out["claim_scope"], "test scope")


class ComputeAuditQueueTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)

    def test_cycle_break_instruction_names_manual_source_graph_repair(self):
        m = _import("compute_audit_queue")
        m.CYCLE_INVENTORY_PATH = self.tmp_root / "cycle_inventory.json"
        m.CYCLE_INVENTORY_PATH.write_text(
            json.dumps(
                {
                    "cycles": [
                        {
                            "cycle_id": "cycle-1",
                            "length": 2,
                            "max_transitive_descendants": 7,
                            "nodes": [
                                {"claim_id": "z_node"},
                                {"claim_id": "a_node"},
                            ],
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        rows = {
            "a_node": {"transitive_descendants": 7, "audit_status": "unaudited"},
            "z_node": {"transitive_descendants": 7, "audit_status": "unaudited"},
        }

        targets = m.cycle_break_targets(rows)

        self.assertEqual(targets[0]["primary_break_target"], "a_node")
        self.assertNotIn("runner_pipeline", targets[0]["instruction"])
        self.assertIn("source-graph repair", targets[0]["instruction"])

    def test_is_ready_accepts_only_foundational_premise_deps(self):
        """Open obligations remain queue blockers."""
        m = _import("compute_audit_queue")
        rows = {
            "open_obligation": {
                "claim_id": "open_obligation",
                "deps": [],
                "effective_status": "unaudited",
            },
            "retained_dep": {
                "claim_id": "retained_dep",
                "deps": [],
                "effective_status": "retained_bounded",
            },
            "unaudited_dep": {
                "claim_id": "unaudited_dep",
                "deps": [],
                "effective_status": "unaudited",
            },
            "discharge_note": {
                "claim_id": "discharge_note",
                "deps": ["minimal_axioms", "retained_dep"],
                "effective_status": "unaudited",
            },
            "obligation_discharge_note": {
                "claim_id": "obligation_discharge_note",
                "deps": ["open_obligation", "retained_dep"],
                "effective_status": "unaudited",
            },
            "blocked_note": {
                "claim_id": "blocked_note",
                "deps": ["open_obligation", "unaudited_dep"],
                "effective_status": "unaudited",
            },
        }
        with mock.patch.object(
            m.premise_nodes,
            "is_accepted_premise_dep",
            side_effect=lambda dep_id: dep_id == "minimal_axioms",
        ):
            self.assertTrue(m.is_ready(rows["discharge_note"], rows))
            self.assertFalse(m.is_ready(rows["obligation_discharge_note"], rows))
            self.assertFalse(m.is_ready(rows["blocked_note"], rows))


class NoGoDisciplineGateTest(unittest.TestCase):
    @staticmethod
    def _manifest() -> dict:
        return {
            "docs/TEST_NO_GO.md": {
                "path": "docs/TEST_NO_GO.md",
                "roles": ["source"],
                "text": "No-go obstruction with a selector wall and dynamics wall.",
                "effective_status": None,
                "accepted_premise_type": None,
            },
            "audit-packet://cross-cycle-index/test_no_go": {
                "path": "audit-packet://cross-cycle-index/test_no_go",
                "roles": ["cross_cycle_index"],
                "text": json.dumps({
                    "schema": "no_go_cross_cycle_index_v1",
                    "claim_id": "test_no_go",
                    "candidates": [],
                }),
                "effective_status": None,
                "accepted_premise_type": None,
            },
            "audit-packet://partial-closure-index/test_no_go": {
                "path": "audit-packet://partial-closure-index/test_no_go",
                "roles": ["partial_closure_index"],
                "text": json.dumps({
                    "schema": "no_go_partial_closure_index_v1",
                    "claim_id": "test_no_go",
                    "candidates": [],
                }),
                "effective_status": None,
                "accepted_premise_type": None,
            },
        }

    def test_source_and_output_triggers_are_conservative(self):
        m = _import("no_go_discipline_gate")
        self.assertTrue(
            m.source_requires_no_go_discipline(
                "docs/BOUNDARY.md",
                "This result is bounded with named walls.",
                "bounded_theorem",
            )
        )
        self.assertFalse(
            m.output_requires_no_go_discipline(
                {
                    "claim_type": "bounded_theorem",
                    "notes_for_re_audit_if_any": "missing_bridge_theorem: derive the carrier",
                }
            )
        )
        self.assertTrue(
            m.output_requires_no_go_discipline(
                {
                    "claim_type": "bounded_theorem",
                    "claim_scope": "The candidate construction does not lift to the full sector.",
                }
            )
        )
        self.assertFalse(
            m.source_requires_no_go_discipline(
                "docs/POSITIVE.md", "An exact positive identity.", "positive_theorem"
            )
        )
        for body in (
            "The theorem leaves two residual walls.",
            "The attempted route does not close on the supplied carrier.",
            "A scoped obstruction rules out the alternate carrier.",
            "A selector wall prevents closure.",
            "A scalar U(1) action cannot select the reading.",
            "No single tensor-factorization exists.",
            "Bounded negative theorem: checked channels do not derive the Lorentzian sign.",
            "An obstruction remains.",
            "The theorem does not close the remaining obstruction.",
            "No route closes.",
            "No four-action distinct shell closes the observed boundary.",
            "The carrier is blocked by a selector wall.",
            "There remains an obstruction.",
            "The attempted construction fails to close.",
            "The construction does not supply an admission.",
            "No route closes the remaining obstruction.",
            "No argument closes the wall.",
            "Nothing closes the remaining obstruction.",
            "Neither route closes the remaining obstruction.",
            "Zero candidates close the wall.",
            "No available route can close the wall.",
            "No route is able to close the obstruction.",
            "None of the tested routes closes the obstruction.",
            "The retained inputs are unable to determine the selector.",
            "The theorem does not yet fully close the remaining obstruction.",
            "The construction cannot ever completely remove the scoped obstruction.",
            "The attempt fails completely to resolve the remaining obstruction.",
            "No route succeeds in closing the obstruction.",
            "The wall cannot be closed.",
            "The obstruction cannot be resolved.",
            "The admission cannot be discharged.",
            "The obstruction is not resolved.",
            "The obstruction has not been resolved.",
            "No derivation closes the remaining boundary.",
            "No anomaly mechanism within these scopes can close the obstruction.",
            "No finite truncation can close the boundary.",
            "No compute frontier closes the structural gap.",
            "No published path supplies the missing selector.",
            "No retained operator determines the readout.",
            "No local observable exists to threshold on.",
            "No `kappa_EW` selector exists.",
            "No `Z`-valued additive label exists.",
            "No retained theorem or method closes the boundary.",
            "No local or global route closes the obstruction.",
            "None of (S1)-(S3) supplies the missing direction.",
            "No solutions exist.",
            "No viable routes exist.",
            "No carriers exist.",
            "No tensor factorizations exist.",
            "No methods exist.",
            "No operators exist.",
            "No theorems exist.",
        ):
            with self.subTest(body=body):
                self.assertTrue(
                    m.source_requires_no_go_discipline(
                        "docs/BOUNDARY.md", body, "bounded_theorem"
                    )
                )
                self.assertTrue(
                    m.output_requires_no_go_discipline({
                        "claim_type": "bounded_theorem",
                        "verdict_rationale": body,
                    })
                )
        self.assertTrue(
            m.output_requires_no_go_discipline({
                "claim_type": "bounded_theorem",
                "verdict_rationale": "A scoped obstruction rules out the carrier.",
            })
        )
        self.assertFalse(
            m.output_requires_no_go_discipline({
                "claim_type": "positive_theorem",
                "verdict_rationale": "This is not an admission; the identity closes.",
            })
        )
        for rationale in (
            "These are scope boundaries, not live admissions; the positive identity closes.",
            "The explicit admission that beta=6 is supplied remains open, but does not block the theorem.",
            "This is not a bounded wall claim; the exact construction closes.",
            "The arithmetic follows from one admitted input and makes no negative claim.",
            "The theorem closes the remaining obstruction.",
            "The construction removes the scoped obstruction.",
            "All residual walls are discharged by the exact identity.",
            "The remaining admission is explicitly supplied, so the theorem closes.",
            "No obstruction remains after the exact construction.",
            "This does not require a new axiom.",
            "The construction does not introduce an admission.",
            "The identity cannot produce an obstruction.",
            "This cannot require a new axiom.",
            "This doesn't require a new axiom.",
            "No obstruction remains because the theorem closes the wall.",
            "No new axiom is required because this theorem closes the remaining obstruction.",
            "No admission is introduced because the exact identity resolves the wall.",
            "No alternate route is needed because the construction removes the scoped obstruction.",
            "Neither admission is needed once the theorem resolves the obstruction.",
            "Nothing further is required because the theorem closes the remaining boundary.",
            "No obstruction exists after the exact construction.",
            "No wall exists because the identity closes it.",
            "No admission affects the proof as the theorem closes the wall.",
        ):
            with self.subTest(rationale=rationale):
                self.assertFalse(
                    m.source_requires_no_go_discipline(
                        "docs/POSITIVE.md", rationale, "positive_theorem"
                    )
                )
                self.assertFalse(
                    m.output_requires_no_go_discipline({
                        "claim_type": "positive_theorem",
                        "verdict_rationale": rationale,
                    })
                )
        for assertion in (
            "The theorem does not fully close the remaining obstruction.",
            "The attempt fails to resolve the remaining obstruction.",
            "The construction cannot completely remove the scoped obstruction.",
        ):
            with self.subTest(assertion=assertion):
                self.assertTrue(
                    m.source_requires_no_go_discipline(
                        "docs/POLARITY.md", assertion, "bounded_theorem"
                    )
                )
                self.assertTrue(
                    m.output_requires_no_go_discipline({
                        "claim_type": "bounded_theorem",
                        "verdict_rationale": assertion,
                    })
                )
        for closure in (
            "The theorem has closed the remaining obstruction.",
            "The remaining obstruction was closed by the theorem.",
            "The residual walls have been discharged.",
        ):
            with self.subTest(closure=closure):
                self.assertFalse(
                    m.source_requires_no_go_discipline(
                        "docs/POSITIVE.md", closure, "positive_theorem"
                    )
                )
                self.assertFalse(
                    m.output_requires_no_go_discipline({
                        "claim_type": "positive_theorem",
                        "verdict_rationale": closure,
                    })
                )
        self.assertTrue(
            m.source_requires_no_go_discipline(
                "docs/spatial_anisotropy_no_go_note.md",
                "A scoped negative boundary.",
                "bounded_theorem",
            )
        )
        self.assertFalse(
            m.source_requires_no_go_discipline(
                "docs/POSITIVE.md",
                "This is not an admission; it is an exact identity.",
                "positive_theorem",
            )
        )

    def test_cross_cycle_index_walks_every_physics_loop_no_go_ledger(self):
        m = _import("no_go_discipline_gate")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = (
                root
                / ".claude/science/physics-loops/first-cycle/NO_GO_LEDGER.md"
            )
            second = (
                root
                / ".claude/science/physics-loops/second-cycle/NO_GO_LEDGER.md"
            )
            first.parent.mkdir(parents=True, exist_ok=True)
            second.parent.mkdir(parents=True, exist_ok=True)
            first.write_text("# No-Go Ledger\nselector obstruction retired\n", encoding="utf-8")
            second.write_text("# No-Go Ledger\ndynamics wall remains\n", encoding="utf-8")
            tail_marker = "tail mechanism: alternate carrier remains blocked"
            first.write_text(
                "# No-Go Ledger\nselector obstruction retired\n"
                + ("x" * 4500)
                + "\n"
                + tail_marker
                + "\n",
                encoding="utf-8",
            )

            rendered = json.loads(
                m.build_cross_cycle_index(
                    {
                        "claim_id": "target",
                        "claim_scope": "selector obstruction",
                        "deps": [],
                    },
                    {},
                    root,
                )
            )

        scope = rendered["search_scope"]["physics_loop_no_go_ledgers"]
        expected_paths = [
            ".claude/science/physics-loops/first-cycle/NO_GO_LEDGER.md",
            ".claude/science/physics-loops/second-cycle/NO_GO_LEDGER.md",
        ]
        self.assertEqual(scope["glob"], ".claude/science/physics-loops/**/NO_GO_LEDGER.md")
        self.assertEqual(scope["scanned_count"], 2)
        self.assertEqual(scope["scanned_paths"], expected_paths)
        loop_candidates = [
            candidate
            for candidate in rendered["candidates"]
            if candidate["kind"] == "physics_loop_no_go_ledger"
        ]
        self.assertEqual(
            [candidate["note_path"] for candidate in loop_candidates],
            expected_paths,
        )
        self.assertTrue(
            all(candidate["content_sha256"] for candidate in loop_candidates)
        )
        first_candidate = next(
            candidate
            for candidate in loop_candidates
            if candidate["note_path"] == expected_paths[0]
        )
        self.assertIn(tail_marker, first_candidate["content"])
        self.assertFalse(first_candidate["content_truncated"])

    def test_partial_closure_index_scans_vocab_meta_and_in_flight_surfaces(self):
        m = _import("no_go_discipline_gate")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path, payload in (
                (m.AXIOM_REGISTRY, {"canonical_ids": [], "nodes": {}}),
                (m.OBLIGATION_REGISTRY, {"canonical_ids": [], "nodes": {}}),
            ):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(payload), encoding="utf-8")
            vocab = root / m.CONTROLLED_VOCABULARY
            vocab.parent.mkdir(parents=True, exist_ok=True)
            vocab.write_text(
                "selector_obstruction: {definition: selector convention reframe}\n",
                encoding="utf-8",
            )
            meta = root / "docs/SELECTOR_META.md"
            meta.write_text(
                "Selector obstruction can be retired by a labeling convention reframe.\n",
                encoding="utf-8",
            )
            queue = root / m.ACTIVE_REVIEW_QUEUE
            queue.write_text(
                "Selector obstruction convention reframe is in flight.\n",
                encoding="utf-8",
            )
            row = {
                "claim_id": "selector_obstruction",
                "claim_scope": "selector obstruction boundary",
                "note_path": "docs/TARGET.md",
            }
            rendered = json.loads(
                m.build_partial_closure_index(
                    row,
                    {
                        "meta": {
                            "claim_type": "meta",
                            "note_path": "docs/SELECTOR_META.md",
                        }
                    },
                    root,
                )
            )

        candidate_ids = {candidate["candidate_id"] for candidate in rendered["candidates"]}
        self.assertTrue(any(cid.startswith("controlled_vocabulary:") for cid in candidate_ids))
        self.assertIn("meta_reframe:docs/SELECTOR_META.md", candidate_ids)
        self.assertIn("in_flight_reframe:docs/repo/ACTIVE_REVIEW_QUEUE.md", candidate_ids)
        self.assertEqual(rendered["search_scope"]["meta_notes"]["scanned_count"], 1)

    def test_pass_requires_five_distinct_routes(self):
        m = _import("no_go_discipline_gate")
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": _no_go_packet(route_count=4),
        }
        self.assertIn(
            "at least 5 distinct route_class values",
            m.validate_no_go_discipline(audit) or "",
        )

        audit["no_go_discipline"] = _no_go_packet(route_count=5)
        self.assertIsNone(m.validate_no_go_discipline(audit))

    def test_pass_rejects_duplicate_route_classes_and_open_routes(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet()
        for route in packet["N1_alternative_routes"]:
            route["route_class"] = "algebraic_rearrangement"
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "distinct route_class",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

        packet = _no_go_packet()
        packet["N1_alternative_routes"][0]["disposition"] = "OPEN"
        audit["no_go_discipline"] = packet
        self.assertIn(
            "disposition=OPEN",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

    def test_pass_rejects_numbered_paraphrases_and_requires_closed_chain(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet()
        for index, route in enumerate(packet["N1_alternative_routes"]):
            route["mechanism"] = f"same mechanism {index}"
            route["attempt"] = f"same test {index}"
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "numbered paraphrases",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

        audit["no_go_discipline"] = _no_go_packet()
        audit["chain_closes"] = False
        self.assertIn(
            "requires chain_closes=true",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

    def test_prior_routes_require_matching_n4_witnesses(self):
        m = _import("no_go_discipline_gate")
        manifest = self._manifest()
        manifest["docs/AUTH.md"] = {
            "path": "docs/AUTH.md",
            "roles": ["authority"],
            "text": "Retained authority closes the route residual exactly.",
            "effective_status": "retained",
            "accepted_premise_type": None,
        }
        packet = _no_go_packet()
        route = packet["N1_alternative_routes"][0]
        route.update({
            "honesty_marker": "RULED OUT BY PRIOR",
            "prior_witness_id": "witness-0",
            "evidence_path": "docs/AUTH.md",
            "evidence_locator": "Retained authority closes the route residual exactly",
        })
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "does not name an N4 witness",
            m.validate_no_go_discipline(audit, evidence_manifest=manifest) or "",
        )
        packet["N4_residual_matching"]["witnesses"] = [{
            "witness_id": "witness-0",
            "route_id": "route-0",
            "witness_residual": "the route residual",
            "claim_residual": "the route residual",
            "match": True,
            "evidence_path": "docs/AUTH.md",
            "evidence_locator": "Retained authority closes the route residual exactly",
        }]
        self.assertIsNone(
            m.validate_no_go_discipline(audit, evidence_manifest=manifest)
        )

    def test_n3_and_n6_cannot_launder_convention_as_authority(self):
        m = _import("no_go_discipline_gate")
        manifest = self._manifest()
        manifest["docs/CONVENTION.md"] = {
            "path": "docs/CONVENTION.md",
            "roles": ["authority"],
            "text": "Convention metadata does not supply theorem authority.",
            "effective_status": "unaudited",
            "accepted_premise_type": "convention_not_accepted",
        }
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": _no_go_packet(),
        }
        audit["no_go_discipline"]["N3_hidden_wall_scan"]["hits"] = [{
            "phrase": "convention authority",
            "classification": "retained_authority",
            "evidence_path": "docs/CONVENTION.md",
            "evidence_locator": "Convention metadata does not supply theorem authority",
        }]
        self.assertIn(
            "not retained or accepted",
            m.validate_no_go_discipline(audit, evidence_manifest=manifest) or "",
        )
        audit["no_go_discipline"] = _no_go_packet()
        partial_index_path = "audit-packet://partial-closure-index/test_no_go"
        manifest[partial_index_path]["text"] = json.dumps({
            "schema": "no_go_partial_closure_index_v1",
            "claim_id": "test_no_go",
            "candidates": [{
                "candidate_id": "approved_primitive:convention",
                "kind": "approved_primitive",
            }],
        })
        audit["no_go_discipline"]["N6_partial_closure_scan"]["candidates"] = [{
            "candidate_id": "approved_primitive:convention",
            "kind": "approved_primitive",
            "could_close_wall": False,
            "addressed": True,
            "disposition": "does not close the wall",
            "evidence_path": "docs/CONVENTION.md",
            "evidence_locator": "Convention metadata does not supply theorem authority",
        }]
        self.assertIn(
            "does not match manifest premise type",
            m.validate_no_go_discipline(audit, evidence_manifest=manifest) or "",
        )

    def test_n6_requires_orchestrator_index_and_complete_disposition(self):
        m = _import("no_go_discipline_gate")
        manifest = self._manifest()
        index_path = "audit-packet://partial-closure-index/test_no_go"
        candidate_id = "convention_reframe:selector_label"
        manifest[index_path]["text"] = json.dumps({
            "schema": "no_go_partial_closure_index_v1",
            "claim_id": "test_no_go",
            "candidates": [{
                "candidate_id": candidate_id,
                "kind": "convention_reframe",
                "content": "selector_label convention reframe candidate",
            }],
        })
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": _no_go_packet(),
        }
        self.assertIn(
            "must disposition every partial-closure candidate",
            m.validate_no_go_discipline(audit, evidence_manifest=manifest) or "",
        )
        audit["no_go_discipline"]["N6_partial_closure_scan"]["candidates"] = [{
            "candidate_id": candidate_id,
            "kind": "convention_reframe",
            "could_close_wall": False,
            "addressed": True,
            "disposition": "the indexed convention does not close this wall",
            "evidence_path": index_path,
            "evidence_locator": "selector_label convention reframe candidate",
        }]
        self.assertIsNone(
            m.validate_no_go_discipline(audit, evidence_manifest=manifest)
        )

    def test_n8_missing_evidence_path_returns_gate_error(self):
        m = _import("no_go_discipline_gate")
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": _no_go_packet(),
        }
        del audit["no_go_discipline"]["N8_cross_cycle_echo"]["evidence_path"]
        error = m.validate_no_go_discipline(
            audit, evidence_manifest=self._manifest()
        )
        self.assertIn("requires non-empty evidence_path", error or "")

    def test_n8_requires_orchestrator_index(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet()
        packet["N8_cross_cycle_echo"].update({
            "evidence_path": "docs/TEST_NO_GO.md",
            "evidence_locator": "No-go obstruction",
        })
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "orchestrator-owned cross_cycle_index",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

    def test_pass_rejects_packet_gaps_and_unresolved_sections(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet()
        packet["N1_alternative_routes"][0]["evidence_locator"] = (
            "language that is absent from the packet"
        )
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_clean",
            "chain_closes": True,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "is not present",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

        packet = _no_go_packet()
        packet["N2_wall_independence"]["unresolved"] = ["pair remains open"]
        audit["no_go_discipline"] = packet
        self.assertIn(
            "N2.unresolved",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

    def test_failed_gate_requires_applied_narrowing(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet(status="FAIL", route_count=3)
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_conditional",
            "claim_scope": "a different applied scope",
            "chain_closes": False,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "must equal the applied claim_scope",
            m.validate_no_go_discipline(
                audit, evidence_manifest=self._manifest()
            ) or "",
        )

    def test_failed_gate_binds_prior_scope_walls_and_next_route(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet(status="FAIL", route_count=3)
        audit = {
            "claim_type": "no_go",
            "verdict": "audited_conditional",
            "claim_scope": "the scoped obstruction",
            "chain_closes": False,
            "no_go_discipline": packet,
        }
        self.assertIn(
            "pre-audit ledger scope",
            m.validate_no_go_discipline(
                audit,
                evidence_manifest=self._manifest(),
                prior_claim_scope="a different old scope",
            ) or "",
        )
        packet["prior_claim_scope"] = "a different old scope"
        packet["corrected_wall_set"] = ["invented wall"]
        self.assertIn(
            "must equal N2.collapsed_wall_set",
            m.validate_no_go_discipline(
                audit,
                evidence_manifest=self._manifest(),
                prior_claim_scope="a different old scope",
            ) or "",
        )
        packet["corrected_wall_set"] = ["selector wall", "dynamics wall"]
        packet["next_route"]["route_id"] = "route-0"
        self.assertIn(
            "OPEN or UNTESTED",
            m.validate_no_go_discipline(
                audit,
                evidence_manifest=self._manifest(),
                prior_claim_scope="a different old scope",
            ) or "",
        )

    def test_failed_gate_allows_non_clean_but_never_clean(self):
        m = _import("no_go_discipline_gate")
        packet = _no_go_packet(status="FAIL", route_count=3)
        non_clean = {
            "claim_type": "no_go",
            "verdict": "audited_conditional",
            "claim_scope": "the scoped obstruction",
            "chain_closes": False,
            "no_go_discipline": packet,
        }
        self.assertIsNone(m.validate_no_go_discipline(non_clean))

        clean = {**non_clean, "verdict": "audited_clean"}
        self.assertIn(
            "audited_clean is forbidden",
            m.validate_no_go_discipline(clean) or "",
        )

    def test_runner_validation_enforces_source_trigger(self):
        m = _import_codex_audit_runner()
        positive = {
            "claim_id": "positive",
            "load_bearing_step": "an exact identity",
            "load_bearing_step_class": "A",
            "claim_type": "positive_theorem",
            "claim_scope": "the exact identity",
            "chain_closes": True,
            "chain_closure_explanation": "the identity closes",
            "verdict": "audited_clean",
            "verdict_rationale": "the algebra closes",
            "no_go_discipline": None,
        }
        self.assertIsNone(m.validate_verdict(positive, "positive"))
        self.assertIn(
            "N1-N8 packet is required",
            m.validate_verdict(
                positive, "positive", source_requires_no_go=True
            )
            or "",
        )

    def test_validation_repair_prompt_reuses_packet_and_preserves_strict_gate(self):
        m = _import_codex_audit_runner()
        original_prompt = "restricted packet with EXACT EVIDENCE LOCATOR"
        rejected = {
            "claim_id": "target",
            "verdict": "audited_conditional",
            "claim_scope": "bounded target scope",
            "no_go_discipline": {
                "required": True,
                "status": "FAIL",
            },
        }
        error = (
            "N1 route 2 evidence_locator is not present in "
            "'docs/TARGET.md'"
        )

        prompt = m.render_validation_repair_prompt(
            original_prompt, rejected, error, 1
        )
        flat_prompt = " ".join(prompt.split())

        self.assertIn(original_prompt, prompt)
        self.assertIn(error, prompt)
        self.assertIn('"claim_id": "target"', prompt)
        self.assertIn(
            "ordinary validator and apply gate remain unchanged", flat_prompt
        )
        self.assertIn("12+ character verbatim substring", flat_prompt)
        self.assertIn("Do not invent evidence", flat_prompt)
        self.assertIn("or change the verdict itself", flat_prompt)
        self.assertIn("untrusted correction target, not evidence", flat_prompt)
        self.assertIn("may not add a top-level field", flat_prompt)
        self.assertNotIn("accept despite", prompt.casefold())

    def test_validation_repair_cannot_change_scientific_judgment(self):
        m = _import_codex_audit_runner()
        rejected = {
            "claim_id": "target",
            "load_bearing_step": "the exact obstruction",
            "load_bearing_step_class": "A",
            "claim_type": "no_go",
            "claim_scope": "bounded obstruction",
            "chain_closes": False,
            "chain_closure_explanation": "one route remains open",
            "verdict": "audited_conditional",
            "verdict_rationale": "the packet is incomplete",
            "no_go_discipline": {
                "required": True,
                "status": "FAIL",
                "N1_alternative_routes": [{
                    "route_id": "route-1",
                    "disposition": "UNTESTED",
                    "evidence_path": "docs/WRONG.md",
                    "evidence_locator": "wrong locator text",
                }],
            },
        }
        locator_repair = json.loads(json.dumps(rejected))
        locator_repair["no_go_discipline"]["N1_alternative_routes"][0].update({
            "evidence_path": "docs/TARGET.md",
            "evidence_locator": "exact packet locator",
        })
        changed_verdict = {**locator_repair, "verdict": "audited_clean"}

        self.assertIsNone(
            m.validation_repair_preservation_error(rejected, locator_repair)
        )
        self.assertIn(
            "changed preserved scientific field 'verdict'",
            m.validation_repair_preservation_error(rejected, changed_verdict)
            or "",
        )

        changed_notes = {
            **locator_repair,
            "notes_for_re_audit_if_any": "a new scientific instruction",
        }
        self.assertIn(
            "changed the top-level field set",
            m.validation_repair_preservation_error(rejected, changed_notes)
            or "",
        )

        rejected_with_optional_fields = {
            **rejected,
            "notes_for_re_audit_if_any": "original repair instruction",
            "auditor_confidence": "medium",
            "runner_check_breakdown": {
                "A": 1,
                "B": 0,
                "C": 0,
                "D": 0,
                "total_pass": 1,
            },
        }
        changed_confidence = {
            **rejected_with_optional_fields,
            "auditor_confidence": "high",
        }
        self.assertIn(
            "changed preserved scientific field 'auditor_confidence'",
            m.validation_repair_preservation_error(
                rejected_with_optional_fields, changed_confidence
            )
            or "",
        )

        injected_apply_control = {
            **rejected,
            "cross_confirmation_role": "second_seat",
        }
        self.assertIn(
            "changed the top-level field set",
            m.validation_repair_preservation_error(
                rejected, injected_apply_control
            )
            or "",
        )

        changed_route_disposition = json.loads(json.dumps(locator_repair))
        changed_route_disposition["no_go_discipline"][
            "N1_alternative_routes"
        ][0]["disposition"] = "CLOSED"
        self.assertIn(
            "changed preserved no-go judgment content",
            m.validation_repair_preservation_error(
                rejected, changed_route_disposition
            )
            or "",
        )

        changed_packet_status = json.loads(json.dumps(locator_repair))
        changed_packet_status["no_go_discipline"]["status"] = "PASS"
        self.assertIn(
            "changed preserved no-go judgment content",
            m.validation_repair_preservation_error(
                rejected, changed_packet_status
            )
            or "",
        )

        self.assertTrue(
            m.validation_repair_eligible(
                rejected,
                "target",
                "N1 route 1 evidence_locator is not present in docs/TARGET.md",
            )
        )
        self.assertFalse(
            m.validation_repair_eligible(
                rejected,
                "target",
                "N2.unresolved must be a list of non-empty strings",
            )
        )
        missing_judgment = dict(rejected)
        del missing_judgment["verdict_rationale"]
        self.assertFalse(
            m.validation_repair_eligible(
                missing_judgment,
                "target",
                "N1 route 1 evidence_locator is not present in docs/TARGET.md",
            )
        )

    def test_prompt_preserves_raw_placeholders_and_types_every_premise(self):
        m = _import_codex_audit_runner()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m.REPO_ROOT = root
            notes = {
                "target": (
                    "literal {{CLAIM_ID}} and {{RUNNER_SOURCE}} inside source evidence"
                ),
                "axiom": "axiom authority",
                "owner": "owner authority",
                "tier": "tier authority",
                "convention": (
                    "literal {{RUNNER_PATH}} and {{NOTE_BODY}} inside authority"
                ),
            }
            for name, body in notes.items():
                path = root / "docs" / f"{name}.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body, encoding="utf-8")
            rows = {
                name: {
                    "claim_id": name,
                    "note_path": f"docs/{name}.md",
                    "effective_status": "unaudited",
                    "claim_type": "bounded_theorem",
                    "deps": [],
                }
                for name in notes
            }
            rows["target"]["deps"] = ["axiom", "owner", "tier", "convention"]
            template = (
                "control={{CLAIM_ID}}\n"
                "{{FOREACH cited_authority IN CITED_AUTHORITIES}}ignored"
                "{{ENDFOREACH}}\n"
                "note={{NOTE_BODY}}\n"
                "manifest={{NO_GO_EVIDENCE_MANIFEST}}\n"
                "premises={{FRAMEWORK_PREMISE_CONTEXT}}\n"
                "partial={{NO_GO_PARTIAL_CLOSURE_INDEX}}\n"
                "gate={{NO_GO_DISCIPLINE_REQUIRED}}\n"
                "stdout={{RUNNER_STDOUT}}\nsource={{RUNNER_SOURCE}}\n"
                "helpers={{HELPER_RUNNER_SOURCES}}"
            )
            with (
                mock.patch.object(m.premise_nodes, "is_axiom_premise", side_effect=lambda x: x == "axiom"),
            ):
                prompt = m.render_prompt(
                    rows["target"], rows, template, 1, skip_runner_stdout=True
                )
            self.assertIn("control=target", prompt)
            self.assertIn("literal {{CLAIM_ID}} and", prompt)
            self.assertIn("{{RUNNER_SOURCE}} inside source evidence", prompt)
            self.assertIn("literal {{RUNNER_PATH}} and", prompt)
            self.assertIn("{{NOTE_BODY}} inside authority", prompt)
            self.assertIn("accepted_premise_type: axiom_or_approved_primitive", prompt)
            self.assertNotIn("accepted_premise_type: owner_governed_residual", prompt)
            self.assertNotIn("accepted_premise_type: tier_a_derivation_target", prompt)
            self.assertIn("bounds_downstream: false", prompt)
            self.assertIn("no_go_partial_closure_index_v1", prompt)

    def test_exact_manifest_matches_truncated_source_and_visible_stdout(self):
        m = _import_codex_audit_runner()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m.REPO_ROOT = root
            m.RUNNER_SOURCE_CHAR_LIMIT = 120
            note_path = root / "docs" / "target.md"
            runner_path = root / "scripts" / "large_runner.py"
            note_path.parent.mkdir(parents=True, exist_ok=True)
            runner_path.parent.mkdir(parents=True, exist_ok=True)
            note_path.write_text("# No-go obstruction\n", encoding="utf-8")
            hidden = "HIDDEN_MIDDLE_LOCATOR_NOT_RENDERED"
            runner_path.write_text(
                "VISIBLE_RUNNER_HEAD_LOCATOR\n"
                + ("x" * 180)
                + hidden
                + ("y" * 180)
                + "\nVISIBLE_RUNNER_TAIL_LOCATOR",
                encoding="utf-8",
            )
            row = {
                "claim_id": "target",
                "note_path": "docs/target.md",
                "runner_path": "scripts/large_runner.py",
                "claim_type": "no_go",
                "deps": [],
            }
            rows = {"target": row}
            template = (
                "{{NOTE_BODY}}\n{{RUNNER_STDOUT}}\n{{RUNNER_SOURCE}}\n"
                "{{HELPER_RUNNER_SOURCES}}\n{{FRAMEWORK_PREMISE_CONTEXT}}\n"
                "{{NO_GO_PARTIAL_CLOSURE_INDEX}}\n"
                "{{NO_GO_CROSS_CYCLE_INDEX}}\n{{NO_GO_EVIDENCE_MANIFEST}}"
            )
            manifest: dict[str, dict] = {}
            with mock.patch.object(
                m, "get_runner_stdout", return_value="VISIBLE_STDOUT_ONLY_LOCATOR"
            ):
                m.render_prompt(
                    row,
                    rows,
                    template,
                    1,
                    use_cache=False,
                    evidence_manifest_out=manifest,
                )
            self.assertNotIn(hidden, manifest["scripts/large_runner.py"]["text"])
            stdout_path = "audit-packet://runner-stdout/target"
            self.assertIn("VISIBLE_STDOUT_ONLY_LOCATOR", manifest[stdout_path]["text"])

            audit = {
                "claim_type": "no_go",
                "verdict": "audited_clean",
                "claim_scope": "the scoped obstruction",
                "chain_closes": True,
                "no_go_discipline": _no_go_packet(
                    evidence_path="scripts/large_runner.py",
                    evidence_locator=hidden,
                    claim_id="target",
                ),
            }
            self.assertIn(
                "is not present",
                m.no_go_discipline_gate.validate_no_go_discipline(
                    audit, evidence_manifest=manifest
                ) or "",
            )
            audit["no_go_discipline"] = _no_go_packet(
                evidence_path=stdout_path,
                evidence_locator="VISIBLE_STDOUT_ONLY_LOCATOR",
                claim_id="target",
            )
            self.assertIsNone(
                m.no_go_discipline_gate.validate_no_go_discipline(
                    audit, evidence_manifest=manifest
                )
            )

    def test_invalidation_archives_and_clears_packet(self):
        m = _import("invalidate_stale_audits")
        packet = _no_go_packet()
        row = {
            "audit_status": "audited_clean",
            "claim_type": "no_go",
            "claim_type_author_hint": "no_go",
            "no_go_discipline": packet,
            "previous_audits": [],
        }
        reset = m.archive_and_reset(row, "test invalidation")
        self.assertEqual(reset["previous_audits"][0]["no_go_discipline"], packet)
        self.assertNotIn("no_go_discipline", reset)

    def test_packetless_clean_no_go_is_invalidated(self):
        m = _import("invalidate_stale_audits")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m.REPO_ROOT = root
            path = root / "docs" / "LEGACY_NO_GO.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# No-go obstruction\n", encoding="utf-8")
            row = {
                "claim_id": "legacy_no_go",
                "note_path": "docs/LEGACY_NO_GO.md",
                "audit_status": "audited_clean",
                "claim_type": "no_go",
                "claim_scope": "legacy obstruction",
                "chain_closes": True,
            }
            self.assertEqual(
                m.detect_invalidation(row, {"legacy_no_go": row}),
                "no_go_discipline_packet_missing",
            )


class CodexAuditRunnerModelPolicyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)

    def _model(self, slug: str, *, priority: int = 0, xhigh: bool = True) -> dict:
        levels = [{"effort": "high"}]
        if xhigh:
            levels.append({"effort": "xhigh"})
        return {
            "slug": slug,
            "priority": priority,
            "supported_reasoning_levels": levels,
        }

    def test_best_cached_model_uses_highest_full_gpt_version_not_cache_order(self):
        m = _import_codex_audit_runner()
        (self.tmp_root / "models_cache.json").write_text(
            json.dumps(
                {
                    "models": [
                        self._model("gpt-5.4"),
                        self._model("gpt-5.3-codex"),
                        self._model("gpt-5.5"),
                        self._model("gpt-5.6-mini"),
                        self._model("gpt-6", xhigh=False),
                    ]
                }
            ),
            encoding="utf-8",
        )

        with mock.patch.dict(os.environ, {"CODEX_HOME": str(self.tmp_root)}):
            model, source = m.best_cached_codex_model()

        self.assertEqual(model, "gpt-5.5")
        self.assertIn("models_cache.json", source)


class CodexAuditRunnerReauditCandidatesTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)

    def test_reaudit_role_records_independence_against_prior_auditor(self):
        m = _import_codex_audit_runner()

        same_family = {
            "audit_status": "audited_conditional",
            "auditor_family": "codex-gpt-5.5",
        }
        role, independence = m.determine_audit_role(
            same_family,
            "codex-gpt-5.5",
            is_reaudit_candidate=True,
        )
        self.assertEqual((role, independence), ("reaudit", "fresh_context"))

        cross_family = {
            "audit_status": "audited_failed",
            "auditor_family": "claude-sonnet",
        }
        role, independence = m.determine_audit_role(
            cross_family,
            "codex-gpt-5.5",
            is_reaudit_candidate=True,
        )
        self.assertEqual((role, independence), ("reaudit", "cross_family"))

    def test_reaudit_role_still_skips_judicial_blockers(self):
        m = _import_codex_audit_runner()

        role, reason = m.determine_audit_role(
            {
                "audit_status": "audited_conditional",
                "blocker": "cross_confirmation_disagreement",
            },
            "codex-gpt-5.5",
            is_reaudit_candidate=True,
        )

        self.assertEqual(role, "skip")
        self.assertIn("judicial review needed", reason)

    def test_load_reaudit_candidates_normalizes_sorts_and_filters_streams(self):
        m = _import_codex_audit_runner()
        path = self.tmp_root / "reaudit_candidates.json"
        path.write_text(
            json.dumps(
                {
                    "candidates": [
                        {
                            "claim_id": "medium_dep",
                            "criticality": "medium",
                            "criticality_rank": 1,
                            "transitive_descendants": 10,
                            "load_bearing_score": 2.0,
                        }
                    ],
                    "runner_drift_candidates": [
                        {
                            "claim_id": "critical_runner",
                            "criticality": "critical",
                            "criticality_rank": 3,
                            "transitive_descendants": 1,
                            "load_bearing_score": 1.0,
                            "queue_reason": "custom_runner_reason",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        m.REAUDIT_CANDIDATES_PATH = path

        rows = m.load_reaudit_candidates()

        self.assertEqual([r["claim_id"] for r in rows], ["critical_runner", "medium_dep"])
        self.assertTrue(all(r["ready"] for r in rows))
        self.assertEqual(rows[0]["queue_reason"], "custom_runner_reason")
        self.assertEqual(rows[1]["queue_reason"], "reaudit_candidate")
        self.assertEqual(rows[1]["audit_status"], "unaudited")

        dep_only = m.load_reaudit_candidates(include_runner_drift=False)
        self.assertEqual([r["claim_id"] for r in dep_only], ["medium_dep"])


class CodexAuditRunnerTargetSelectionTest(unittest.TestCase):
    def test_select_named_targets_preserves_requested_order(self):
        m = _import_codex_audit_runner()
        queue = [
            {"claim_id": "first", "score": 100},
            {"claim_id": "second", "score": 10},
        ]

        selected = m.select_named_targets(queue, ["second", "first"])

        self.assertEqual([row["claim_id"] for row in selected], ["second", "first"])

    def test_select_named_targets_rejects_missing_and_duplicate_ids(self):
        m = _import_codex_audit_runner()
        queue = [{"claim_id": "first"}]

        with self.assertRaisesRegex(ValueError, "absent from the selected queue"):
            m.select_named_targets(queue, ["missing"])
        with self.assertRaisesRegex(ValueError, "duplicate --claim-id"):
            m.select_named_targets(queue, ["first", "first"])


class RelabelUnverifiedCodexAuditsTest(unittest.TestCase):
    def test_relabels_below_floor_row_and_matching_cross_confirmation(self):
        m = _import("relabel_unverified_codex_audits")
        row = {
            "audit_status": "audited_conditional",
            "auditor": "codex-audit-loop",
            "auditor_family": "codex-gpt-5",
            "cross_confirmation": {
                "first_audit": {
                    "auditor": "codex-audit-loop",
                    "auditor_family": "codex-gpt-5",
                },
                "second_audit": {
                    "auditor": "independent-human",
                    "auditor_family": "codex-gpt-5",
                },
            },
        }

        relabeled, cc_count = m.relabel_row(row)

        self.assertTrue(relabeled)
        self.assertEqual(cc_count, 1)
        self.assertEqual(row["auditor_family"], "codex-gpt-5.5")
        self.assertEqual(row["previous_auditor_family"], "codex-gpt-5")
        self.assertEqual(
            row["cross_confirmation"]["first_audit"]["auditor_family"],
            "codex-gpt-5.5",
        )
        self.assertEqual(
            row["cross_confirmation"]["second_audit"]["auditor_family"],
            "codex-gpt-5",
        )
        self.assertEqual(
            row["relabel_reason"],
            "operator_pre_floor_policy_relabel_2026-05-06",
        )

    def test_skips_pending_or_already_marked_rows(self):
        m = _import("relabel_unverified_codex_audits")
        self.assertFalse(
            m.is_unverified_codex_label(
                {"audit_status": "unaudited", "auditor_family": "codex-gpt-5"}
            )
        )
        self.assertFalse(
            m.is_unverified_codex_label(
                {
                    "audit_status": "audited_clean",
                    "auditor_family": "codex-gpt-5",
                    "previous_auditor_family": "codex-current",
                }
            )
        )
        self.assertFalse(
            m.is_unverified_codex_label(
                {"audit_status": "audited_clean", "auditor_family": "claude-opus"}
            )
        )

    def test_audit_lint_model_floor_helper(self):
        m = _import("audit_lint")
        self.assertFalse(m.codex_family_meets_minimum("codex-gpt-5"))
        self.assertTrue(m.codex_family_meets_minimum("codex-gpt-5.5"))
        self.assertTrue(m.codex_family_meets_minimum("codex-gpt-6"))
        self.assertTrue(m.codex_family_meets_minimum("claude-opus"))


class RestoreOveraggressivelyInvalidatedAuditsTest(unittest.TestCase):
    """One-shot restoration of audits over-aggressively invalidated before
    PR #907's policy refinement."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _archived_audit(self, *, audit_status="audited_clean",
                        independence="cross_family", cc_status=None,
                        invalidation_reason="criticality_increased:medium->critical",
                        claim_type="positive_theorem",
                        auditor_family="codex-gpt-5.5",
                        notes_for_re_audit_if_any=None):
        archived = {
            "audit_status": audit_status,
            "independence": independence,
            "auditor": "codex-test",
            "auditor_family": auditor_family,
            "claim_type": claim_type,
            "claim_scope": "test scope",
            "load_bearing_step_class": "A",
            "audit_state_snapshot": {"criticality": "leaf", "deps": []},
            "audit_date": "2026-05-09T11:00:00+00:00",
            "archived_at": "2026-05-09T15:00:00+00:00",
            "invalidation_reason": invalidation_reason,
        }
        if notes_for_re_audit_if_any is not None:
            archived["notes_for_re_audit_if_any"] = notes_for_re_audit_if_any
        if cc_status is not None:
            archived["cross_confirmation"] = {
                "first_audit": {"verdict": "audited_clean"},
                "second_audit": None,
                "status": cc_status,
            }
        return archived

    def _seed_with_archived(self, cid: str, archived: dict, *,
                            current_status="unaudited") -> dict:
        return {
            "claim_id": cid,
            "note_path": f"docs/{cid.upper()}.md",
            "note_hash": "deadbeef",
            "deps": [],
            "audit_status": current_status,
            "previous_audits": [archived],
        }

    def _import_and_patch(self):
        m = _import("restore_overaggressively_invalidated_audits")
        m.REPO_ROOT = self.tmp_root
        m.DATA_DIR = self.tmp_root / "docs" / "audit" / "data"
        m.LEDGER_PATH = m.DATA_DIR / "audit_ledger.json"
        return m

    def test_categorize_archived_mirrors_invalidate_policy(self):
        m = self._import_and_patch()
        # leaf/medium: any audit qualifies
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(audit_status="audited_conditional"), "medium"),
            "noop",
        )
        # high requires non-weak
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(independence="weak"), "high"),
            "invalidate",
        )
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(independence="cross_family"), "high"),
            "noop",
        )
        # critical: cc-confirmed -> noop, weak -> invalidate, otherwise soft_reset
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(cc_status="confirmed"), "critical"),
            "noop",
        )
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(independence="weak"), "critical"),
            "invalidate",
        )
        self.assertEqual(
            m.categorize_criticality_bump_for_archived(
                self._archived_audit(independence="cross_family"), "critical"),
            "soft_reset",
        )

    def test_restore_round_trips_and_validates_no_go_packet(self):
        m = self._import_and_patch()
        cid = "restore_no_go"
        note_path = "docs/RESTORE_NO_GO.md"
        self.fx.write_note(note_path, "# No-go obstruction\n")
        archived = self._archived_audit(
            claim_type="no_go",
            invalidation_reason="criticality_increased:leaf->medium",
        )
        archived["claim_scope"] = "the scoped obstruction"
        archived["chain_closes"] = True
        archived["no_go_discipline"] = _no_go_packet(
            evidence_path=note_path,
            claim_id=cid,
        )
        row = self._seed_with_archived(cid, archived)
        row["note_path"] = note_path
        rows = {cid: row}

        restored = m.restore_audit_from_previous(row, rows)
        self.assertIsNotNone(restored)
        self.assertEqual(
            restored["no_go_discipline"], archived["no_go_discipline"]
        )

        archived_bad = dict(archived)
        archived_bad["no_go_discipline"] = dict(archived["no_go_discipline"])
        archived_bad["no_go_discipline"]["status"] = "BROKEN"
        bad_row = self._seed_with_archived(cid, archived_bad)
        bad_row["note_path"] = note_path
        self.assertIsNone(
            m.restore_audit_from_previous(bad_row, {cid: bad_row})
        )

    def test_restore_refuses_packetless_clean_no_go_authority(self):
        m = self._import_and_patch()
        cid = "packetless_no_go"
        note_path = "docs/PACKETLESS_NO_GO.md"
        self.fx.write_note(note_path, "# No-go obstruction\n")
        archived = self._archived_audit(
            claim_type="no_go",
            invalidation_reason="criticality_increased:leaf->medium",
        )
        archived["chain_closes"] = True
        row = self._seed_with_archived(cid, archived)
        row["note_path"] = note_path
        self.assertIsNone(
            m.restore_audit_from_previous(row, {cid: row})
        )

    def test_restore_refuses_packetless_clean_output_negative_authority(self):
        m = self._import_and_patch()
        cid = "packetless_output_negative"
        note_path = "docs/POSITIVE_SOURCE.md"
        self.fx.write_note(note_path, "# Positive source theorem\n")
        archived = self._archived_audit(
            claim_type="positive_theorem",
            invalidation_reason="criticality_increased:leaf->medium",
        )
        archived["claim_scope"] = "A scoped obstruction rules out the carrier."
        archived["chain_closes"] = True
        row = self._seed_with_archived(cid, archived)
        row["note_path"] = note_path

        self.assertFalse(
            m.no_go_discipline_gate.source_requires_no_go_discipline(
                note_path,
                "# Positive source theorem\n",
                archived["claim_type"],
            )
        )
        self.assertTrue(
            m.no_go_discipline_gate.output_requires_no_go_discipline(
                {**archived, "verdict": archived["audit_status"]}
            )
        )
        self.assertIsNone(
            m.restore_audit_from_previous(row, {cid: row})
        )

    def test_select_restore_candidates_picks_criticality_increased(self):
        m = self._import_and_patch()
        rows = {
            "ok_to_restore": self._seed_with_archived(
                "ok_to_restore",
                self._archived_audit(invalidation_reason="criticality_increased:leaf->medium"),
            ),
            "soft_reset_target": self._seed_with_archived(
                "soft_reset_target",
                self._archived_audit(
                    invalidation_reason="criticality_increased:high->critical",
                    independence="cross_family", cc_status=None,
                ),
            ),
            "weak_at_critical_skip": self._seed_with_archived(
                "weak_at_critical_skip",
                self._archived_audit(
                    invalidation_reason="criticality_increased:leaf->critical",
                    independence="weak",
                ),
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertIn("ok_to_restore", crit)
        self.assertIn("soft_reset_target", crit)
        self.assertNotIn("weak_at_critical_skip", crit)
        self.assertEqual(dep_weak, [])

    def test_select_restore_candidates_picks_dep_weakened_only_from_crit_set(self):
        m = self._import_and_patch()
        # downstream_in_set's dep is in crit_set; downstream_orphan's dep is not.
        rows = {
            "soft_reset_dep": self._seed_with_archived(
                "soft_reset_dep",
                self._archived_audit(
                    invalidation_reason="criticality_increased:medium->critical",
                ),
            ),
            "downstream_in_set": self._seed_with_archived(
                "downstream_in_set",
                self._archived_audit(
                    invalidation_reason="dep_weakened:soft_reset_dep:retained_bounded->audit_in_progress",
                    claim_type="positive_theorem",
                ),
            ),
            "downstream_orphan": self._seed_with_archived(
                "downstream_orphan",
                self._archived_audit(
                    invalidation_reason="dep_weakened:unrelated_dep:retained->unaudited",
                    claim_type="positive_theorem",
                ),
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertIn("soft_reset_dep", crit)
        dep_weak_cids = {cid for cid, _, _ in dep_weak}
        self.assertEqual(dep_weak_cids, {"downstream_in_set"})

    def test_dep_weakened_not_restored_when_dep_remains_weaker(self):
        m = self._import_and_patch()
        rows = {
            "conditional_dep": self._seed_with_archived(
                "conditional_dep",
                self._archived_audit(
                    audit_status="audited_conditional",
                    invalidation_reason="criticality_increased:high->critical",
                    notes_for_re_audit_if_any="other: terminal conditional remains conditional",
                ),
            ),
            "downstream_still_weakened": self._seed_with_archived(
                "downstream_still_weakened",
                self._archived_audit(
                    audit_status="audited_numerical_match",
                    invalidation_reason=(
                        "dep_weakened:conditional_dep:"
                        "audited_numerical_match->audited_conditional"
                    ),
                ),
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertIn("conditional_dep", crit)
        self.assertEqual(dep_weak, [])

    def test_lint_incompatible_archived_audits_stay_invalidated(self):
        m = self._import_and_patch()
        missing_scope = self._archived_audit(
            invalidation_reason="criticality_increased:leaf->medium",
        )
        missing_scope.pop("claim_scope")
        rows = {
            "missing_scope": self._seed_with_archived("missing_scope", missing_scope),
            "low_model_floor": self._seed_with_archived(
                "low_model_floor",
                self._archived_audit(
                    invalidation_reason="criticality_increased:leaf->medium",
                    auditor_family="codex-gpt-5",
                ),
            ),
            "conditional_missing_repair_class": self._seed_with_archived(
                "conditional_missing_repair_class",
                self._archived_audit(
                    audit_status="audited_conditional",
                    invalidation_reason="criticality_increased:leaf->medium",
                ),
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertEqual(crit, {})
        self.assertEqual(dep_weak, [])

    def test_noncritical_blocker_keeps_candidate_invalidated(self):
        m = self._import_and_patch()
        archived = self._archived_audit(
            invalidation_reason="criticality_increased:medium->critical",
        )
        archived["audit_state_snapshot"] = {
            "criticality": "medium",
            "deps": ["weak_dep"],
            "dep_effective_status": {"weak_dep": "retained_bounded"},
        }
        rows = {
            "candidate": self._seed_with_archived("candidate", archived),
            "weak_dep": {
                "claim_id": "weak_dep",
                "audit_status": "audited_conditional",
                "effective_status": "audited_conditional",
                "note_path": "docs/WEAK_DEP.md",
                "deps": [],
            },
        }
        rows["candidate"]["deps"] = ["weak_dep"]

        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertEqual(crit, {})
        self.assertEqual(dep_weak, [])

    def test_other_invalidation_reasons_are_not_touched(self):
        m = self._import_and_patch()
        rows = {
            "hash_drift": self._seed_with_archived(
                "hash_drift",
                self._archived_audit(invalidation_reason="runner_hash_changed:abc->def"),
            ),
            "deps_changed": self._seed_with_archived(
                "deps_changed",
                self._archived_audit(
                    invalidation_reason="deps_changed:dep_added:new_dep_xyz",
                ),
            ),
            "claim_scope_drift": self._seed_with_archived(
                "claim_scope_drift",
                self._archived_audit(
                    invalidation_reason="dep_claim_scope_changed:some_dep",
                ),
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertEqual(crit, {})
        self.assertEqual(dep_weak, [])

    def test_restore_audit_from_previous_copies_archived_fields_back(self):
        m = self._import_and_patch()
        archived = self._archived_audit(
            audit_status="audited_clean",
            independence="fresh_context",
            invalidation_reason="criticality_increased:leaf->critical",
            cc_status=None,
        )
        row = {
            "claim_id": "test_row",
            "note_path": "docs/TEST.md",
            "note_hash": "abc",
            "deps": [],
            "audit_status": "unaudited",  # over-aggressively invalidated
            "claim_type": None,
            "claim_type_provenance": "needs_reaudit_after_invalidation",
            "auditor": None,
            "previous_audits": [archived],
        }
        new_row = m.restore_audit_from_previous(row)
        self.assertEqual(new_row["audit_status"], "audited_clean")
        self.assertEqual(new_row["independence"], "fresh_context")
        self.assertEqual(new_row["claim_type"], "positive_theorem")
        self.assertEqual(new_row["claim_scope"], "test scope")
        self.assertEqual(new_row["auditor"], "codex-test")
        # The archive entry is removed from previous_audits.
        self.assertEqual(new_row["previous_audits"], [])

    def test_idempotent_on_already_audited_rows(self):
        """A row that's currently audited (not unaudited) is not a candidate."""
        m = self._import_and_patch()
        rows = {
            "live_audited": dict(
                self._seed_with_archived(
                    "live_audited",
                    self._archived_audit(invalidation_reason="criticality_increased:leaf->medium"),
                    current_status="audited_clean",
                )
            ),
        }
        crit, dep_weak = m.select_restore_candidates(rows)
        self.assertEqual(crit, {})
        self.assertEqual(dep_weak, [])

    def test_main_writes_restored_ledger(self):
        m = self._import_and_patch()
        m.DATA_DIR.mkdir(parents=True, exist_ok=True)
        archived_clean = self._archived_audit(
            invalidation_reason="criticality_increased:leaf->medium",
        )
        archived_dep_weak = self._archived_audit(
            invalidation_reason="dep_weakened:soft_reset_dep:retained->unaudited",
        )
        ledger = {
            "schema_version": 1,
            "rows": {
                "soft_reset_dep": self._seed_with_archived("soft_reset_dep", archived_clean),
                "downstream": self._seed_with_archived("downstream", archived_dep_weak),
            },
        }
        m.LEDGER_PATH.write_text(json.dumps(ledger, indent=2, sort_keys=True))

        with mock.patch.object(sys, "argv", ["restore", ""]):
            sys.argv = ["restore"]
            rc = m.main()
        self.assertEqual(rc, 0)

        out = json.loads(m.LEDGER_PATH.read_text(encoding="utf-8"))
        soft = out["rows"]["soft_reset_dep"]
        down = out["rows"]["downstream"]
        self.assertEqual(soft["audit_status"], "audited_clean")
        self.assertEqual(soft["claim_type"], "positive_theorem")
        self.assertEqual(soft["previous_audits"], [])
        self.assertEqual(down["audit_status"], "audited_clean")
        self.assertEqual(down["previous_audits"], [])


class ComputeAuditDispatchQueueTest(unittest.TestCase):
    """Behavior tests for compute_audit_dispatch_queue.py — the new
    resolution semantics (post-manifest fresh-context re-audit retires a
    dispatch target even when its status tuple is unchanged) and the
    dependency-blocker detail on `ready_blocker`."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _patch_dispatch_module(self, module) -> None:
        _patch_repo_root(module, self.tmp_root)
        module.AUDIT_DIR = self.tmp_root / "docs" / "audit"
        module.OUT_JSON = module.DATA_DIR / "audit_dispatch_queue.json"
        module.OUT_MD = module.AUDIT_DIR / "AUDIT_DISPATCH_QUEUE.md"

    def _write_sidecar(self, name: str, manifest: dict) -> Path:
        path = self.fx.data_dir / name
        path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _basic_manifest(self, *, generated_date: str, group_id: str,
                        targets: list[dict], retired_targets: list[dict] | None = None,
                        blocked_by_group_ids: list[str] | None = None) -> dict:
        manifest = {
            "schema": "promotion_reaudit_queue.v1",
            "generated_date": generated_date,
            "allowed_context_paths": [],
            "forbidden_context": [],
            "groups": [
                {
                    "group_id": group_id,
                    "order": 1,
                    "blocked_by_group_ids": blocked_by_group_ids or [],
                    "targets": targets,
                }
            ],
        }
        if retired_targets is not None:
            manifest["retired_targets"] = retired_targets
        return manifest

    def _row(self, cid: str, *, audit_status: str, claim_type: str,
             effective_status: str, audit_date: str | None = None,
             independence: str | None = None, deps: list[str] | None = None,
             auditor: str | None = None, auditor_family: str | None = None) -> dict:
        return {
            "claim_id": cid,
            "audit_status": audit_status,
            "claim_type": claim_type,
            "effective_status": effective_status,
            "audit_date": audit_date,
            "independence": independence,
            "deps": list(deps or []),
            "auditor": auditor,
            "auditor_family": auditor_family,
        }

    def _read_output(self) -> dict:
        return json.loads(
            (self.fx.data_dir / "audit_dispatch_queue.json").read_text(encoding="utf-8")
        )

    def test_same_status_fresh_context_reaudit_resolves_to_resolved_targets(self):
        """A row whose audit_date is on/after the manifest's generated_date
        AND whose independence is no longer 'weak' resolves out of the live
        queue, even when its {claim_type, audit_status, effective_status}
        tuple is unchanged from the manifest guard.

        The resolved entry must record the resolution reason and the
        post-manifest audit's date + independence + auditor for provenance.
        """
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "no_go_row": self._row(
                "no_go_row",
                audit_status="audited_failed",
                claim_type="no_go",
                effective_status="retained_no_go",
                audit_date="2026-05-23T18:12:00+00:00",
                independence="fresh_context",
                auditor="codex-test-fresh",
                auditor_family="codex-gpt-5.5",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "provenance_reaudit_queue_2026-05-22.json",
            self._basic_manifest(
                generated_date="2026-05-22",
                group_id="legacy_weak_independence_terminal_no_go_rows",
                targets=[
                    {
                        "claim_id": "no_go_row",
                        "note_path": "docs/NO_GO_ROW.md",
                        "audit_question": "Re-audit weak no-go boundary.",
                        "current_audit_status": "audited_failed",
                        "current_claim_type": "no_go",
                        "current_effective_status": "retained_no_go",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 0)
        live_ids = [e["claim_id"] for e in out["live"]]
        self.assertNotIn("no_go_row", live_ids)
        resolved_ids = [e["claim_id"] for e in out["resolved_targets"]]
        self.assertEqual(resolved_ids, ["no_go_row"])

        resolved = out["resolved_targets"][0]
        self.assertEqual(
            resolved["resolution_reason"],
            m.RESOLUTION_REASON_FRESH_CONTEXT,
        )
        evidence = resolved["resolution_evidence"]
        self.assertEqual(evidence["audit_date"], "2026-05-23T18:12:00+00:00")
        self.assertEqual(evidence["independence"], "fresh_context")
        self.assertEqual(evidence["auditor"], "codex-test-fresh")
        self.assertEqual(evidence["auditor_family"], "codex-gpt-5.5")
        self.assertEqual(resolved["resolution_manifest_date"], "2026-05-22")

    def test_bounded_terminal_resolution_for_promotion_reaudit(self):
        """A bounded-to-retained promotion dispatch whose post-manifest
        re-audit confirms the row is still bounded_theorem records the
        resolution reason as `bounded_terminal_after_reaudit`, distinct from
        the generic fresh-context resolution. This signals the operator may
        elevate the entry to `retired_targets` if bounded should be treated
        as terminal until the source note changes."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "bounded_row": self._row(
                "bounded_row",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
                audit_date="2026-05-24T10:00:00+00:00",
                independence="fresh_context",
                auditor="codex-bounded",
                auditor_family="codex-gpt-5.5",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "bounded_to_retained_reaudit_queue_2026-05-23.json",
            self._basic_manifest(
                generated_date="2026-05-23",
                group_id="bounded_to_retained_chain",
                targets=[
                    {
                        "claim_id": "bounded_row",
                        "note_path": "docs/BOUNDED_ROW.md",
                        "audit_question": "Can this row promote from bounded to positive?",
                        "current_audit_status": "audited_clean",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "retained_bounded",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 0)
        self.assertEqual(len(out["resolved_targets"]), 1)
        resolved = out["resolved_targets"][0]
        self.assertEqual(resolved["claim_id"], "bounded_row")
        self.assertEqual(
            resolved["resolution_reason"],
            m.RESOLUTION_REASON_BOUNDED_TERMINAL,
        )

    def test_weak_independence_row_stays_live_after_resolution_check(self):
        """A row whose post-manifest re-audit kept independence=weak must
        NOT resolve — weak independence cannot retire a dispatch that
        explicitly asked for stronger independence."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "weak_row": self._row(
                "weak_row",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
                audit_date="2026-05-23T18:00:00+00:00",
                independence="weak",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "provenance_reaudit_queue_2026-05-22.json",
            self._basic_manifest(
                generated_date="2026-05-22",
                group_id="legacy_weak_independence_clean_rows",
                targets=[
                    {
                        "claim_id": "weak_row",
                        "note_path": "docs/WEAK_ROW.md",
                        "audit_question": "Re-audit with stronger independence.",
                        "current_audit_status": "audited_clean",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "retained_bounded",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 1)
        self.assertEqual(out["live"][0]["claim_id"], "weak_row")
        self.assertEqual(out["resolved_targets"], [])

    def test_audit_date_before_manifest_stays_live(self):
        """A row whose audit_date is BEFORE the manifest's generated_date
        is not yet considered resolved — the dispatch asked for a NEW
        re-audit after the manifest was generated."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "old_audit": self._row(
                "old_audit",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
                audit_date="2026-05-01T10:00:00+00:00",
                independence="fresh_context",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "provenance_reaudit_queue_2026-05-22.json",
            self._basic_manifest(
                generated_date="2026-05-22",
                group_id="legacy_weak_independence_clean_rows",
                targets=[
                    {
                        "claim_id": "old_audit",
                        "note_path": "docs/OLD_AUDIT.md",
                        "audit_question": "Re-audit pre-manifest verdict.",
                        "current_audit_status": "audited_clean",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "retained_bounded",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 1)
        self.assertEqual(out["resolved_targets"], [])

    def test_ready_blocker_reports_specific_dependency_when_blocked(self):
        """A live dispatch row whose dependency is non-retained-grade must
        report the specific dep claim_id + dep status in `ready_blocker`,
        not a blank field. This was the born_rule bug: deps blocked the
        row but the blocker was opaque."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "child_row": self._row(
                "child_row",
                audit_status="unaudited",
                claim_type="bounded_theorem",
                effective_status="unaudited",
                deps=["bad_dep_one", "ok_dep"],
            ),
            "bad_dep_one": self._row(
                "bad_dep_one",
                audit_status="audited_failed",
                claim_type="no_go",
                effective_status="audited_failed",
            ),
            "ok_dep": self._row(
                "ok_dep",
                audit_status="audited_clean",
                claim_type="positive_theorem",
                effective_status="retained",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "promotion_reaudit_queue_2026-05-22.json",
            self._basic_manifest(
                generated_date="2026-05-22",
                group_id="downstream_chain",
                targets=[
                    {
                        "claim_id": "child_row",
                        "note_path": "docs/CHILD_ROW.md",
                        "audit_question": "Audit child row.",
                        "current_audit_status": "unaudited",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "unaudited",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 1)
        live = out["live"][0]
        self.assertEqual(live["claim_id"], "child_row")
        self.assertFalse(live["ready"])
        blocker = live["ready_blocker"]
        self.assertIsNotNone(blocker)
        self.assertTrue(blocker.startswith("blocked_by_dependency:"))
        self.assertIn("bad_dep_one:audited_failed", blocker)
        # Healthy dep should not appear in blocker.
        self.assertNotIn("ok_dep", blocker)

    def test_ready_blocker_reports_multiple_dep_blockers(self):
        """Multiple non-retained-grade deps are reported comma-separated."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "child": self._row(
                "child",
                audit_status="unaudited",
                claim_type="bounded_theorem",
                effective_status="unaudited",
                deps=["dep_a", "dep_b"],
            ),
            "dep_a": self._row(
                "dep_a",
                audit_status="audited_conditional",
                claim_type="bounded_theorem",
                effective_status="audited_conditional",
            ),
            "dep_b": self._row(
                "dep_b",
                audit_status="audited_failed",
                claim_type="no_go",
                effective_status="audited_failed",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        self._write_sidecar(
            "promotion_reaudit_queue_2026-05-22.json",
            self._basic_manifest(
                generated_date="2026-05-22",
                group_id="downstream_chain",
                targets=[
                    {
                        "claim_id": "child",
                        "note_path": "docs/CHILD.md",
                        "audit_question": "Audit child.",
                        "current_audit_status": "unaudited",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "unaudited",
                    }
                ],
            ),
        )

        m.main()
        out = self._read_output()

        live = out["live"][0]
        blocker = live["ready_blocker"]
        self.assertIn("dep_a:audited_conditional", blocker)
        self.assertIn("dep_b:audited_failed", blocker)

    def test_group_blocker_still_uses_existing_format(self):
        """When a group is blocked by another live group, the ready_blocker
        uses the existing `blocked_by_live_group:` prefix (not the new
        dep format). Existing behavior must not regress."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "blocking_row": self._row(
                "blocking_row",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
                audit_date="2026-04-01T00:00:00+00:00",
                independence="weak",
            ),
            "blocked_row": self._row(
                "blocked_row",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
                audit_date="2026-04-01T00:00:00+00:00",
                independence="weak",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        manifest = {
            "schema": "promotion_reaudit_queue.v1",
            "generated_date": "2026-05-22",
            "allowed_context_paths": [],
            "forbidden_context": ["this manifest as evidence"],
            "groups": [
                {
                    "group_id": "first_group",
                    "order": 1,
                    "blocked_by_group_ids": [],
                    "targets": [{
                        "claim_id": "blocking_row",
                        "note_path": "docs/BLOCKING_ROW.md",
                        "audit_question": "Audit blocker.",
                        "current_audit_status": "audited_clean",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "retained_bounded",
                    }],
                },
                {
                    "group_id": "second_group",
                    "order": 2,
                    "blocked_by_group_ids": ["first_group"],
                    "targets": [{
                        "claim_id": "blocked_row",
                        "note_path": "docs/BLOCKED_ROW.md",
                        "audit_question": "Audit blocked.",
                        "current_audit_status": "audited_clean",
                        "current_claim_type": "bounded_theorem",
                        "current_effective_status": "retained_bounded",
                    }],
                },
            ],
        }
        self._write_sidecar("promotion_reaudit_queue_2026-05-22.json", manifest)

        m.main()
        out = self._read_output()

        blocked_entries = [e for e in out["live"] if e["claim_id"] == "blocked_row"]
        self.assertEqual(len(blocked_entries), 1)
        blocker = blocked_entries[0]["ready_blocker"]
        self.assertEqual(blocker, "blocked_by_live_group:first_group")

    def test_retired_targets_path_still_works(self):
        """Manual retired_targets sidecar entries continue to land in the
        retired bucket (not resolved_targets). The new resolution mechanism
        is additive."""
        m = _import("compute_audit_dispatch_queue")
        self._patch_dispatch_module(m)

        rows = {
            "retired_row": self._row(
                "retired_row",
                audit_status="audited_clean",
                claim_type="bounded_theorem",
                effective_status="retained_bounded",
            ),
        }
        self.fx.write_ledger({"schema_version": 1, "rows": rows})
        manifest = self._basic_manifest(
            generated_date="2026-05-22",
            group_id="legacy_group",
            targets=[],
            retired_targets=[{
                "claim_id": "retired_row",
                "note_path": "docs/RETIRED_ROW.md",
                "audit_question": "Originally targeted, now retired.",
                "retired_reason": "operator_marked_bounded_terminal",
                "current_audit_status": "audited_clean",
                "current_claim_type": "bounded_theorem",
                "current_effective_status": "retained_bounded",
            }],
        )
        self._write_sidecar("promotion_reaudit_queue_2026-05-22.json", manifest)

        m.main()
        out = self._read_output()

        self.assertEqual(out["live_count"], 0)
        self.assertEqual(out["resolved_targets"], [])
        self.assertEqual(len(out["retired"]), 1)
        retired = out["retired"][0]
        self.assertEqual(retired["claim_id"], "retired_row")
        self.assertEqual(retired["retired_reason"], "operator_marked_bounded_terminal")


class AuditLintDispatchQueueTest(unittest.TestCase):
    """Sidecar-lint regression coverage: audit_lint.py must still flag
    live dispatch targets missing from audit_dispatch_queue.json, AND it
    must accept resolved_targets / retired / resolved_or_invalid as
    'known to the dispatch queue' so the new resolution mechanism does
    not trigger spurious stale-target warnings."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    def _write_minimal_ledger(self, rows: dict) -> None:
        graph_nodes = {
            cid: {"deps": list(row.get("deps") or [])}
            for cid, row in rows.items()
        }
        self.fx.write_graph({"nodes": graph_nodes, "edges": []})
        import hashlib
        for cid, row in rows.items():
            np = row.get("note_path") or f"docs/{cid}.md"
            row["note_path"] = np
            body = row.get("_body", f"# {cid}\n")
            row.pop("_body", None)
            (self.tmp_root / np).parent.mkdir(parents=True, exist_ok=True)
            (self.tmp_root / np).write_text(body, encoding="utf-8")
            row["note_hash"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
            row.setdefault("deps", [])
        self.fx.write_ledger({"schema_version": 1, "rows": rows})

    def _write_sidecar_and_queue(self, *, target_cid: str, in_queue_bucket: str | None):
        sidecar = {
            "schema": "promotion_reaudit_queue.v1",
            "generated_date": "2026-05-22",
            "allowed_context_paths": [],
            "forbidden_context": [],
            "groups": [{
                "group_id": "g",
                "order": 1,
                "blocked_by_group_ids": [],
                "targets": [{
                    "claim_id": target_cid,
                    "note_path": f"docs/{target_cid}.md",
                    "audit_question": "test",
                    "current_audit_status": "audited_clean",
                    "current_claim_type": "bounded_theorem",
                    "current_effective_status": "retained_bounded",
                }],
            }],
        }
        (self.fx.data_dir / "promotion_reaudit_queue_2026-05-22.json").write_text(
            json.dumps(sidecar) + "\n", encoding="utf-8"
        )

        # Build dispatch queue with the target placed in the chosen bucket
        # (or omitted entirely when in_queue_bucket is None).
        queue: dict = {
            "schema": "audit_dispatch_queue.v1",
            "live": [],
            "resolved_targets": [],
            "retired": [],
            "resolved_or_invalid": [],
            "live_count": 0,
            "ready_count": 0,
        }
        if in_queue_bucket is not None:
            queue[in_queue_bucket].append({"claim_id": target_cid})
        if in_queue_bucket == "live":
            queue["live_count"] = 1
        (self.fx.data_dir / "audit_dispatch_queue.json").write_text(
            json.dumps(queue) + "\n", encoding="utf-8"
        )

    def _run_lint(self, rows: dict, target_cid: str, *, in_queue_bucket: str | None) -> str:
        self._write_minimal_ledger(rows)
        self._write_sidecar_and_queue(target_cid=target_cid, in_queue_bucket=in_queue_bucket)
        m = _import("audit_lint")
        _patch_repo_root(m, self.tmp_root)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            m.main()
        return buf.getvalue()

    def _live_row(self, cid: str) -> dict:
        return {
            "claim_id": cid,
            "audit_status": "audited_clean",
            "claim_type": "bounded_theorem",
            "effective_status": "retained_bounded",
            "auditor": "x",
            "auditor_family": "codex-gpt-5.5",
            "criticality": "leaf",
            "claim_scope": "real scope",
            "load_bearing_step_class": "C",
        }

    def test_live_target_missing_from_queue_warns(self):
        rows = {"my_live_target": self._live_row("my_live_target")}
        out = self._run_lint(rows, "my_live_target", in_queue_bucket=None)
        self.assertIn("audit_dispatch_queue_stale", out)
        self.assertIn("my_live_target", out)

    def test_live_target_in_live_bucket_passes(self):
        rows = {"in_live": self._live_row("in_live")}
        out = self._run_lint(rows, "in_live", in_queue_bucket="live")
        self.assertNotIn("audit_dispatch_queue_stale", out)

    def test_live_target_in_resolved_targets_passes(self):
        """A target in resolved_targets is 'known to the dispatch queue'
        and must not trigger the stale-target warning. This is the
        regression coverage for the new resolution mechanism."""
        rows = {"in_resolved": self._live_row("in_resolved")}
        out = self._run_lint(rows, "in_resolved", in_queue_bucket="resolved_targets")
        self.assertNotIn("audit_dispatch_queue_stale", out)

    def test_live_target_in_retired_bucket_passes(self):
        rows = {"in_retired": self._live_row("in_retired")}
        out = self._run_lint(rows, "in_retired", in_queue_bucket="retired")
        self.assertNotIn("audit_dispatch_queue_stale", out)


class RepairMissingDependencyEdgesTest(unittest.TestCase):
    """Guards on the nightly dependency-edge repair.

    The bot must not convert a deliberately-backticked sideways pointer into a
    live citation edge, and must not auto-wire any edge that would close a
    cycle in the citation graph. Either move re-creates a length-2 cycle that
    a human broke on purpose, and the next nightly run would re-add it.
    """

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp_root = Path(self._tmp.name)
        self.fx = CleanLedgerFixture(self.tmp_root)

    # --- pure-logic unit tests (no fixture needed) ---------------------------

    def test_edge_would_close_cycle_detects_back_paths(self):
        m = _import("repair_missing_dependency_edges")
        # b already points at a; wiring a -> b closes a length-2 cycle.
        self.assertTrue(m.edge_would_close_cycle({"a": [], "b": ["a"]}, "a", "b"))
        # No path from b back to a: the edge is cycle-free.
        self.assertFalse(m.edge_would_close_cycle({"a": [], "b": []}, "a", "b"))
        # Longer cycle: a -> b -> c, and c -> a closes it.
        chain = {"a": ["b"], "b": ["c"], "c": []}
        self.assertTrue(m.edge_would_close_cycle(chain, "c", "a"))
        # A forward shortcut a -> c does not close any cycle.
        self.assertFalse(m.edge_would_close_cycle(chain, "a", "c"))
        # Re-adding an existing edge introduces no new cycle.
        self.assertFalse(m.edge_would_close_cycle({"a": ["b"], "b": ["a"]}, "b", "a"))
        # A node unknown to the graph cannot lie on an existing path.
        self.assertFalse(m.edge_would_close_cycle({"a": []}, "a", "z"))

    def test_has_backticked_reference_matches_filename_not_links(self):
        m = _import("repair_missing_dependency_edges")
        tgt = Path("docs/FOO_BOUNDED_NOTE_2026-05-08.md")
        self.assertTrue(
            m.has_backticked_reference("see `FOO_BOUNDED_NOTE_2026-05-08.md` here", tgt)
        )
        # Backticked repo-relative path still matches on basename.
        self.assertTrue(
            m.has_backticked_reference("`docs/sub/FOO_BOUNDED_NOTE_2026-05-08.md`", tgt)
        )
        # A live markdown link is NOT a backtick reference (the existing dedup
        # owns that case; this guard must not fire on it).
        self.assertFalse(
            m.has_backticked_reference("[foo](FOO_BOUNDED_NOTE_2026-05-08.md)", tgt)
        )
        # A bare prose mention without backticks is not a backtick reference.
        self.assertFalse(
            m.has_backticked_reference("plain FOO_BOUNDED_NOTE_2026-05-08.md text", tgt)
        )

    # --- integration tests over a fixture ledger + graph ---------------------

    def _seed_pair(self, *, source_body: str, target_deps):
        """Seed source NOTE_A (audited_conditional, names NOTE_B in
        open_dependency_paths) and target NOTE_B (with the given graph deps).
        Returns the imported, repo-root-patched module."""
        self.fx.write_note("docs/NOTE_A.md", source_body)
        self.fx.write_note("docs/NOTE_B.md", "# Note B\n")
        self.fx.write_graph(
            {
                "nodes": {
                    "note_a": {"deps": []},
                    "note_b": {"deps": list(target_deps)},
                }
            }
        )
        self.fx.write_ledger(
            {
                "schema_version": 1,
                "rows": {
                    "note_a": {
                        "claim_id": "note_a",
                        "note_path": "docs/NOTE_A.md",
                        "deps": [],
                        "audit_status": "audited_conditional",
                        "open_dependency_paths": ["docs/NOTE_B.md"],
                    },
                    "note_b": {
                        "claim_id": "note_b",
                        "note_path": "docs/NOTE_B.md",
                        "deps": list(target_deps),
                        "audit_status": "audited_clean",
                    },
                },
            }
        )
        m = _import("repair_missing_dependency_edges")
        _patch_repo_root(m, self.tmp_root)
        return m

    def _apply(self, m):
        rows = m.load_rows()
        repairs = m.candidate_repairs(rows)
        stats = m.apply_repairs(rows, repairs, apply=True)
        note_a = (self.tmp_root / "docs" / "NOTE_A.md").read_text(encoding="utf-8")
        return stats, note_a

    def test_skips_edge_that_would_close_cycle(self):
        # NOTE_B already cites NOTE_A (graph edge note_b -> note_a), so wiring
        # note_a -> note_b would close a length-2 cycle.
        m = self._seed_pair(source_body="# Note A\n", target_deps=["note_a"])
        stats, note_a = self._apply(m)
        self.assertEqual(stats["skipped_cycle"], 1)
        self.assertEqual(stats["dependency_edges"], 0)
        self.assertEqual(stats["changed_files"], 0)
        self.assertNotIn("](NOTE_B.md)", note_a)
        self.assertNotIn(m.MARKER, note_a)

    def test_skips_target_already_backticked(self):
        # NOTE_A backticks NOTE_B's filename as a deliberate sideways pointer.
        body = (
            "# Note A\n\n"
            "See `NOTE_B.md` (backticked to break the audit-graph cycle: "
            "downstream consumer, not a load-bearing edge).\n"
        )
        m = self._seed_pair(source_body=body, target_deps=[])
        stats, note_a = self._apply(m)
        self.assertEqual(stats["skipped_backticked"], 1)
        self.assertEqual(stats["dependency_edges"], 0)
        self.assertNotIn("](NOTE_B.md)", note_a)

    def test_adds_legitimate_non_cycle_non_backticked_edge(self):
        # No back edge and no backtick: the missing edge is wired normally.
        m = self._seed_pair(source_body="# Note A\n", target_deps=[])
        stats, note_a = self._apply(m)
        self.assertEqual(stats["dependency_edges"], 1)
        self.assertEqual(stats["changed_files"], 1)
        self.assertEqual(stats["skipped_backticked"], 0)
        self.assertEqual(stats["skipped_cycle"], 0)
        self.assertIn("- [note_b](NOTE_B.md)", note_a)
        self.assertIn(m.MARKER, note_a)

    def test_existing_live_link_is_not_duplicated(self):
        body = (
            "# Note A\n\n"
            "## Audit dependency repair links\n\n"
            "- [note_b](NOTE_B.md)\n"
        )
        m = self._seed_pair(source_body=body, target_deps=[])
        stats, note_a = self._apply(m)
        self.assertEqual(stats["dependency_edges"], 0)
        self.assertEqual(note_a.count("](NOTE_B.md)"), 1)


class SanitizeLegacyAuditArtifactsTest(unittest.TestCase):
    def test_canonicalizes_decoration_parent_filename_stem(self):
        m = _import("sanitize_legacy_audit_artifacts")
        ledger = {
            "rows": {
                "cl3_complexification_split_narrow_theorem_note_2026-05-10": {
                    "claim_id": "cl3_complexification_split_narrow_theorem_note_2026-05-10",
                    "note_path": "docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md",
                },
                "staggered_jw_decoration": {
                    "claim_id": "staggered_jw_decoration",
                    "decoration_parent_claim_id": "CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10",
                },
            }
        }

        m.canonicalize_decoration_parent_ids(ledger)

        self.assertEqual(
            ledger["rows"]["staggered_jw_decoration"]["decoration_parent_claim_id"],
            "cl3_complexification_split_narrow_theorem_note_2026-05-10",
        )


if __name__ == "__main__":
    unittest.main()
