"""Tests for the authoring gates: graph-delta manifest, class-F headers,
and the directory-target link rule (front-door campaign, 2026-07-17)."""
from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import repo_invariants_check
from repo_invariants_check import (
    CLASS_F_REQUIRED_PHRASES,
    class_f_violations_from,
    collect_authority_links,
    graph_manifest_delta,
    _git_tracked_files,
)
from write_citation_graph_manifest import compute_manifest


def _graph(nodes):
    return {"nodes": {k: {"deps": v} for k, v in nodes.items()}}


class TopologyAcknowledgmentGateTest(unittest.TestCase):
    """A delta warns on ordinary runs and fails only when enforcement is asked for."""

    def _check(self, graph_check, **kwargs):
        snapshot = {
            "ledger": {"shard_parse_errors": [], "duplicate_claim_ids": [],
                       "shard_count": 1, "retained_grade_total": 0},
            "premises": {"tracked": True},
            "obligations": {"tracked": True},
            "docs": {"duplicate_basenames": []},
            "authority_links": {"violations": []},
        }
        output = io.StringIO()
        with mock.patch.object(repo_invariants_check, "build_snapshot", return_value=snapshot), \
                mock.patch.object(repo_invariants_check, "_git_tracked_files", return_value=[]), \
                mock.patch.object(repo_invariants_check, "collect_class_f_violations", return_value=[]), \
                mock.patch.object(repo_invariants_check, "collect_graph_manifest_check", return_value=graph_check), \
                mock.patch.object(repo_invariants_check, "_format_graph_delta", return_value="delta"), \
                contextlib.redirect_stdout(output):
            return repo_invariants_check.run_check(True, **kwargs), output.getvalue()

    def test_delta_warns_by_default(self):
        rc, output = self._check({"missing_from_index": False, "delta": {"added": ["n"]}})
        self.assertEqual(rc, 0)
        self.assertIn("WARN: citation-graph delta not acknowledged", output)

    def test_delta_fails_when_enforced(self):
        rc, output = self._check({"missing_from_index": False, "delta": {"added": ["n"]}},
                                 enforce_topology_ack=True)
        self.assertEqual(rc, 1)
        self.assertIn("FAIL: citation-graph delta not acknowledged", output)

    def test_missing_manifest_still_fails(self):
        rc, _ = self._check({"missing_from_index": True, "delta": None})
        self.assertEqual(rc, 1)


class ComputeManifestTest(unittest.TestCase):
    def test_shape_counts_and_determinism(self):
        g = _graph({"b": ["a"], "a": [], "c": ["a", "b"]})
        m1 = compute_manifest(g)
        self.assertEqual(m1["schema_version"], 1)
        self.assertEqual(m1["node_count"], 3)
        self.assertEqual(m1["edge_count"], 3)
        self.assertEqual(m1["nodes"]["c"]["out_degree"], 2)
        # Dep-order invariance: hashes are computed over sorted deps.
        g2 = _graph({"b": ["a"], "a": [], "c": ["b", "a"]})
        self.assertEqual(m1, compute_manifest(g2))

    def test_deps_hash_distinguishes_rewiring(self):
        m1 = compute_manifest(_graph({"c": ["a", "b"]}))
        m2 = compute_manifest(_graph({"c": ["a", "x"]}))
        self.assertEqual(
            m1["nodes"]["c"]["out_degree"], m2["nodes"]["c"]["out_degree"]
        )
        self.assertNotEqual(
            m1["nodes"]["c"]["deps_hash"], m2["nodes"]["c"]["deps_hash"]
        )


class GraphManifestDeltaTest(unittest.TestCase):
    def test_identical_is_none(self):
        m = compute_manifest(_graph({"a": [], "b": ["a"]}))
        self.assertIsNone(graph_manifest_delta(m, m))

    def test_added_removed_changed_named(self):
        old = compute_manifest(_graph({"a": [], "b": ["a"]}))
        new = compute_manifest(_graph({"a": [], "b": ["a", "c"], "c": []}))
        delta = graph_manifest_delta(new, old)
        self.assertEqual(delta["added"], ["c"])
        self.assertEqual(delta["removed"], [])
        self.assertEqual(delta["changed"], ["b"])


class ClassFHeaderTest(unittest.TestCase):
    REG = {"rows": [
        {"path": "docs/repo/GOOD.md", "class": "F"},
        {"path": "docs/repo/BAD.md", "class": "F"},
        {"path": "docs/repo/UNTRACKED.md", "class": "F"},
        {"path": "docs/repo/ANY.md", "class": "E"},
    ]}
    TEXTS = {
        "docs/repo/GOOD.md": " ".join(CLASS_F_REQUIRED_PHRASES),
        "docs/repo/BAD.md": CLASS_F_REQUIRED_PHRASES[0],
        "docs/repo/ANY.md": "",
    }

    def _run(self):
        tracked = {"docs/repo/GOOD.md", "docs/repo/BAD.md", "docs/repo/ANY.md"}
        return class_f_violations_from(self.REG, tracked, self.TEXTS.__getitem__)

    def test_good_doc_passes_bad_and_untracked_fail(self):
        violations = self._run()
        paths = sorted(v["path"] for v in violations)
        self.assertEqual(paths, ["docs/repo/BAD.md", "docs/repo/UNTRACKED.md"])
        bad = next(v for v in violations if v["path"] == "docs/repo/BAD.md")
        self.assertIn(CLASS_F_REQUIRED_PHRASES[1], bad["problem"])

    def test_non_class_f_rows_ignored(self):
        # docs/repo/ANY.md is class E with empty text and produces no violation.
        self.assertNotIn(
            "docs/repo/ANY.md", [v["path"] for v in self._run()]
        )


class ClassFRegistryUnreadableTest(unittest.TestCase):
    def test_invalid_utf8_registry_yields_structured_violation(self):
        # An invalid-UTF-8 registry must surface as the structured
        # "registry unreadable" violation, not a raw UnicodeDecodeError.
        import tempfile
        from unittest import mock

        import repo_invariants_check as ric

        with tempfile.TemporaryDirectory() as tmp:
            reg = Path(tmp) / ric.DOC_AUTHORITY_REGISTRY_REL
            reg.parent.mkdir(parents=True)
            reg.write_bytes(b'{"rows": [\xff\xfe]}')
            with mock.patch.object(ric, "REPO_ROOT", tmp):
                violations = ric.collect_class_f_violations([])
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0]["path"], ric.DOC_AUTHORITY_REGISTRY_REL)
        self.assertIn("registry unreadable", violations[0]["problem"])


class DirectoryTargetIntegrationTest(unittest.TestCase):
    def test_no_directory_targets_survive_on_authority_surfaces(self):
        # Integration: after the campaign's link fixes, no authority-surface
        # markdown link may resolve to a directory. Guards the rule itself
        # (reason must exist) and the repo state (no violators).
        result = collect_authority_links(_git_tracked_files())
        dir_violations = [
            v for v in result["violations"] if v["reason"] == "directory-target"
        ]
        self.assertEqual(dir_violations, [])


if __name__ == "__main__":
    unittest.main()
