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
    # validates a synthetic temp ledger against the REAL repo's
    # tier_a_admissions.json / audit_dispatch_queue.json and emits spurious
    # errors (rows the test never created).
    if hasattr(module, "TIER_A_ADMISSIONS_PATH"):
        module.TIER_A_ADMISSIONS_PATH = module.DATA_DIR / "tier_a_admissions.json"
    if hasattr(module, "AUDIT_DISPATCH_QUEUE_PATH"):
        module.AUDIT_DISPATCH_QUEUE_PATH = module.DATA_DIR / "audit_dispatch_queue.json"
    if hasattr(module, "SUMMARY_PATH"):
        # Either compute_effective_status (effective_status_summary) or
        # compute_load_bearing (load_bearing_summary). Set both files under
        # tmp data dir; only the relevant one is written.
        module.SUMMARY_PATH = module.DATA_DIR / "effective_status_summary.json"
    if hasattr(module, "OUTPUT_PATH"):
        module.OUTPUT_PATH = module.DATA_DIR / "auditor_reliability.json"


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
            "audit_state_snapshot": {"criticality": "high", "deps": []},
            "previous_audits": [],
        }
        new_row = m.archive_prior_audit(dict(row_with_snapshot))
        # Snapshot should be in EMPTY_AUDIT (now None), not preserved
        self.assertIsNone(new_row.get("audit_state_snapshot"))
        # Prior values archived
        self.assertEqual(len(new_row["previous_audits"]), 1)

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
                        "previous_audits": [{"verdict": "old"}],
                        "audit_status": "unaudited",
                        "auditor": "stale-auditor",
                        "auditor_family": "codex-gpt-5",
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
        self.assertIsNone(row["independence"])
        self.assertIsNone(row["load_bearing_step"])
        self.assertIsNone(row["chain_closes"])
        self.assertIsNone(row["audit_state_snapshot"])
        self.assertIsNone(row["cross_confirmation"])
        self.assertEqual(row["claim_type"], "no_go")
        self.assertEqual(row["claim_type_provenance"], "migration_hint")
        self.assertIsNone(row["claim_scope"])
        self.assertEqual(row["previous_audits"], [{"verdict": "old"}])

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

    def test_axiom_and_primitive_premises_do_not_bound_positive_theorem(self):
        """Axioms and explicitly approved framework primitives satisfy chain
        closure without forcing retained_bounded. Tier-A derivation targets are
        the only accepted premises that bound an otherwise clean positive
        theorem."""
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
            "uses_tier_a_admission": {
                "claim_id": "uses_tier_a_admission",
                "deps": ["observable_principle_from_axiom_note"],
                "audit_status": "audited_clean",
                "claim_type": "positive_theorem",
            },
        }
        with mock.patch.object(
            m.premise_nodes,
            "is_axiom_premise",
            side_effect=lambda dep_id: dep_id
            in {"minimal_axioms", "scale_reference_primitive"},
        ), mock.patch.object(
            m.premise_nodes,
            "is_admitted_derivation_target",
            side_effect=lambda dep_id: dep_id
            == "observable_principle_from_axiom_note",
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
            new_rows["uses_tier_a_admission"]["effective_status"],
            "retained_bounded",
        )
        self.assertEqual(
            new_rows["uses_tier_a_admission"]["effective_status_reason"],
            "bounded_by_tier_a_admitted_derivation_target",
        )

    def test_metadata_dependencies_satisfy_clean_chain_without_bounding(self):
        """Metadata rows are stable audit-governance inputs. They satisfy a
        clean theorem's dependency chain without turning the theorem into
        retained_pending_chain and without imposing Tier-A boundedness."""
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

    def test_is_ready_accepts_premise_deps(self):
        """Queue readiness mirrors compute_effective_status's accepted-premise
        policy: a row whose only non-retained deps are an axiom/primitive
        premise node or a Tier-A admitted derivation target is auditable now
        (a clean verdict resolves it to retained / retained_bounded), so the
        queue must mark it ready instead of holding it behind the admission's
        own unaudited row."""
        m = _import("compute_audit_queue")
        rows = {
            "tier_a_gate": {
                "claim_id": "tier_a_gate",
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
                "deps": ["minimal_axioms", "tier_a_gate", "retained_dep"],
                "effective_status": "unaudited",
            },
            "blocked_note": {
                "claim_id": "blocked_note",
                "deps": ["tier_a_gate", "unaudited_dep"],
                "effective_status": "unaudited",
            },
        }
        with mock.patch.object(
            m.premise_nodes,
            "is_accepted_premise_dep",
            side_effect=lambda dep_id: dep_id in {"minimal_axioms", "tier_a_gate"},
        ):
            self.assertTrue(m.is_ready(rows["discharge_note"], rows))
            self.assertFalse(m.is_ready(rows["blocked_note"], rows))


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
