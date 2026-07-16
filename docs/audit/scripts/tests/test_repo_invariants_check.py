"""Regression tests for the repo-invariants harness.

Encodes the concrete probe cases from the PR #5399 sol-max review rounds
(markdown masking and link grammar, ledger-shard schema safety, tracked-set
discipline for every measured family, destination classification, snapshot
diff sensitivity, and the alias-safe snapshot-output refusal). It is a
regression boundary for those named cases, not a full CommonMark or JSON
conformance suite.
"""

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import repo_invariants_check as ric  # noqa: E402


class ScanMarkdownLinkTargetsTest(unittest.TestCase):
    def test_extracts_plain_link_with_relative_path(self):
        self.assertEqual(
            ric.scan_markdown_link_targets("see [x](../audit/data/ledger/)"),
            ["../audit/data/ledger/"],
        )

    def test_ignores_links_inside_inline_code(self):
        text = "every markdown link `[..](OTHER.md)` is treated as an edge"
        self.assertEqual(ric.scan_markdown_link_targets(text), [])

    def test_ignores_links_inside_fenced_code(self):
        text = "```\n[real looking](DEAD.md)\n```\nafter"
        self.assertEqual(ric.scan_markdown_link_targets(text), [])

    def test_math_artifact_scans_raw_but_classifies_skip(self):
        text = "the Hessian candidate S[h] = 1/2 D^2 W[g_*](h,h) in the cell"
        targets = ric.scan_markdown_link_targets(text)
        self.assertEqual(targets, ["h,h"])
        self.assertEqual(ric.classify_target(targets[0]), "skip")

    def test_handles_title_and_angle_bracket_destination(self):
        text = '[a](X.md "The X note") and [b](<sub dir/Y.md>)'
        self.assertEqual(
            ric.scan_markdown_link_targets(text), ["X.md", "sub dir/Y.md"]
        )

    def test_external_and_mailto_classify_skip(self):
        text = "[w](https://example.org/x.md) [m](mailto:a@b.c) [k](K.md)"
        kinds = [ric.classify_target(x) for x in ric.scan_markdown_link_targets(text)]
        self.assertEqual(kinds, ["skip", "skip", "relative"])


class CollectLedgerSchemaTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._old_root = ric.REPO_ROOT
        ric.REPO_ROOT = self._tmp.name
        self.addCleanup(self._restore)
        shard_dir = Path(self._tmp.name) / ric.LEDGER_PREFIX / "aa"
        shard_dir.mkdir(parents=True)
        (shard_dir / "good_note.json").write_text(json.dumps(
            {"claim_id": "good_note", "effective_status": "unaudited",
             "note_path": "docs/GOOD_NOTE.md"}))
        (shard_dir / "list_shard.json").write_text("[]")
        (shard_dir / "null_claim.json").write_text(json.dumps(
            {"claim_id": None, "effective_status": "retained"}))

    def _restore(self):
        ric.REPO_ROOT = self._old_root
        self._tmp.cleanup()

    def test_schema_invalid_shards_recorded_not_crashed(self):
        tracked = [
            ric.LEDGER_PREFIX + "aa/good_note.json",
            ric.LEDGER_PREFIX + "aa/list_shard.json",
            ric.LEDGER_PREFIX + "aa/null_claim.json",
            "docs/GOOD_NOTE.md",
        ]
        result = ric.collect_ledger(tracked)
        self.assertEqual(result["shard_count"], 3)
        self.assertEqual(len(result["shard_parse_errors"]), 2)
        self.assertEqual(result["rows_with_missing_note_path"], 0)
        self.assertEqual(
            result["effective_status_histogram"], {"retained": 1, "unaudited": 1}
        )

    def test_untracked_files_do_not_perturb_measurement(self):
        # An extra shard exists on disk but is not in the tracked list.
        extra = Path(self._tmp.name) / ric.LEDGER_PREFIX / "aa" / "scratch.json"
        extra.write_text(json.dumps({"claim_id": "scratch"}))
        tracked = [ric.LEDGER_PREFIX + "aa/good_note.json", "docs/GOOD_NOTE.md"]
        result = ric.collect_ledger(tracked)
        self.assertEqual(result["shard_count"], 1)
        self.assertNotIn("scratch", json.dumps(result))


class AuthorityLinksTrackedSetTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        self._old_root = ric.REPO_ROOT
        ric.REPO_ROOT = str(root)
        self.addCleanup(self._restore)
        (root / "docs" / "repo").mkdir(parents=True)
        (root / "README.md").write_text(
            "[tracked](docs/TRACKED.md) [untracked](docs/PRESENT_UNTRACKED.md) "
            "[gone](docs/MISSING.md) [dir](docs/repo/)"
        )
        (root / "docs" / "TRACKED.md").write_text("x")
        (root / "docs" / "PRESENT_UNTRACKED.md").write_text("x")
        (root / "docs" / "repo" / "KEEP.md").write_text("x")

    def _restore(self):
        ric.REPO_ROOT = self._old_root
        self._tmp.cleanup()

    def test_untracked_and_missing_targets_are_violations(self):
        tracked = ["README.md", "docs/TRACKED.md", "docs/repo/KEEP.md"]
        result = ric.collect_authority_links(tracked)
        reasons = {v["target"]: v["reason"] for v in result["violations"]}
        self.assertEqual(
            reasons,
            {
                "docs/PRESENT_UNTRACKED.md": "not-tracked",
                "docs/MISSING.md": "not-tracked",
            },
        )

    def test_reason_is_stable_under_untracked_scratch_files(self):
        # BUG-16: an untracked file appearing on disk must not change the
        # serialized violation reason between two worktrees at one commit.
        tracked = ["README.md", "docs/TRACKED.md", "docs/repo/KEEP.md"]
        before = ric.collect_authority_links(tracked)["violations"]
        (Path(ric.REPO_ROOT) / "docs" / "MISSING.md").write_text("late")
        after = ric.collect_authority_links(tracked)["violations"]
        self.assertEqual(before, after)

    def test_outside_repository_link_is_reported(self):
        (Path(ric.REPO_ROOT) / "README.md").write_text("[out](../OUTSIDE.md)")
        result = ric.collect_authority_links(["README.md"])
        self.assertEqual(
            [(v["target"], v["reason"]) for v in result["violations"]],
            [("../OUTSIDE.md", "outside-repository")],
        )


class DiffSensitivityTest(unittest.TestCase):
    def _diff(self, a: dict, b: dict, allow=""):
        with tempfile.TemporaryDirectory() as tmp:
            pa, pb = Path(tmp) / "a.json", Path(tmp) / "b.json"
            pa.write_text(json.dumps(a))
            pb.write_text(json.dumps(b))
            out = io.StringIO()
            with redirect_stdout(out):
                code = ric.run_diff(
                    str(pa), str(pb),
                    {k for k in allow.split(",") if k},
                )
            return code, out.getvalue()

    def test_missing_vs_null_is_a_difference(self):
        code, out = self._diff({"a": {}}, {"a": {"k": None}})
        self.assertEqual(code, 1)
        self.assertIn("CHANGED", out)

    def test_empty_object_appearance_is_a_difference(self):
        code, out = self._diff({"a": {"k": 1}}, {"a": {"k": 1}, "b": {}})
        self.assertEqual(code, 1)

    def test_allow_is_dot_segment_bounded(self):
        code, _ = self._diff({"a": {"b": 1, "bb": 1}}, {"a": {"b": 2, "bb": 2}},
                             allow="a.b")
        self.assertEqual(code, 1)  # a.bb change is NOT covered by allow=a.b

    def test_identical_snapshots_pass(self):
        code, out = self._diff({"a": {"k": 1}}, {"a": {"k": 1}})
        self.assertEqual(code, 0)
        self.assertIn("IDENTICAL", out)




class MaskCodeRoundTwoProbes(unittest.TestCase):
    def test_tilde_and_long_fences(self):
        for text in (
            "~~~~\n[a](TILDE4.md)\n~~~~",
            "```\n[a](CLOSE_LONGER.md)\n````",
            "   ~~~\n[a](INDENTED.md)\n   ~~~",
            "````\n```\n[a](FENCE4.md)\n```\n````",
        ):
            self.assertEqual(ric.scan_markdown_link_targets(text), [], text)

    def test_unclosed_fence_masks_to_end(self):
        self.assertEqual(
            ric.scan_markdown_link_targets("```\n[a](UNCLOSED.md)\ntail"), []
        )

    def test_double_backtick_span_containing_single_backtick(self):
        text = "`` [a](NESTED.md) ` `` and [b](REAL.md)"
        self.assertEqual(ric.scan_markdown_link_targets(text), ["REAL.md"])


class LinkGrammarRoundTwoProbes(unittest.TestCase):
    def test_single_quote_and_paren_titles(self):
        text = "[x](X.md 'title') [y](Y.md (title))"
        self.assertEqual(ric.scan_markdown_link_targets(text), ["X.md", "Y.md"])

    def test_balanced_parens_in_bare_destination(self):
        self.assertEqual(
            ric.scan_markdown_link_targets("[x](dir/foo(bar).md)"),
            ["dir/foo(bar).md"],
        )

    def test_escaped_opener_is_not_a_link(self):
        self.assertEqual(ric.scan_markdown_link_targets("\\[not-link](FAKE.md)"), [])

    def test_fragment_and_query_are_preserved_raw_then_strippable(self):
        targets = ric.scan_markdown_link_targets("[a](docs/T.md#part) [b](docs/T.md?raw=1)")
        self.assertEqual(
            [ric.strip_fragment_query(x) for x in targets],
            ["docs/T.md", "docs/T.md"],
        )


class ClassifyTargetTest(unittest.TestCase):
    def test_classification_table(self):
        cases = {
            "file:///tmp/LOCAL.md": "absolute",
            "//example.com/X.md": "skip",
            "C:/Users/me/X.md": "absolute",
            "/Users/me/X.md": "absolute",
            "https://example.org/a.md": "skip",
            "mailto:a@b.c": "skip",
            "h,h": "skip",
            "../X.md": "relative",
            "data/ledger/": "relative",
        }
        for dest, want in cases.items():
            self.assertEqual(ric.classify_target(dest), want, dest)


class RegistryTrackedSetTest(unittest.TestCase):
    def test_untracked_registry_is_flagged_not_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = ric.REPO_ROOT
            ric.REPO_ROOT = tmp
            try:
                p = Path(tmp) / ric.PREMISE_NODES
                p.parent.mkdir(parents=True)
                p.write_text(json.dumps({"nodes": {"UNTRACKED_PREMISE": {}}}))
                out = ric._load_ids(ric.PREMISE_NODES, ("nodes",), set())
                self.assertEqual(out, {"ids": [], "file_sha256": None, "tracked": False})
                out2 = ric._load_ids(ric.PREMISE_NODES, ("nodes",), {ric.PREMISE_NODES})
                self.assertEqual(out2["ids"], ["UNTRACKED_PREMISE"])
                self.assertTrue(out2["tracked"])
            finally:
                ric.REPO_ROOT = old


class ShardSchemaRoundTwoProbes(unittest.TestCase):
    def test_nonstring_status_and_invalid_utf8_recorded(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = ric.REPO_ROOT
            ric.REPO_ROOT = tmp
            try:
                d = Path(tmp) / ric.LEDGER_PREFIX / "aa"
                d.mkdir(parents=True)
                (d / "liststatus.json").write_text(
                    json.dumps({"claim_id": "liststatus", "effective_status": ["retained"]})
                )
                (d / "badbytes.json").write_bytes(b'\xff\xfe{"claim_id"')
                tracked = [
                    ric.LEDGER_PREFIX + "aa/liststatus.json",
                    ric.LEDGER_PREFIX + "aa/badbytes.json",
                ]
                result = ric.collect_ledger(tracked)
                self.assertEqual(len(result["shard_parse_errors"]), 2)
                self.assertEqual(result["effective_status_histogram"].get("SCHEMA_INVALID"), 1)
                self.assertEqual(result["retained_grade_total"], 0)
            finally:
                ric.REPO_ROOT = old


class DiffRoundTwoProbes(unittest.TestCase):
    def _diff(self, a, b, allow=""):
        with tempfile.TemporaryDirectory() as tmp:
            pa, pb = Path(tmp) / "a.json", Path(tmp) / "b.json"
            pa.write_text(json.dumps(a))
            pb.write_text(json.dumps(b))
            out = io.StringIO()
            with redirect_stdout(out):
                code = ric.run_diff(str(pa), str(pb), {k for k in allow.split(",") if k})
            return code, out.getvalue()

    def test_marker_key_cannot_spoof_empty_object(self):
        code, _ = self._diff({"a": {}}, {"a": {"<empty-object>": True}})
        self.assertEqual(code, 1)

    def test_allow_covers_empty_to_populated_transition(self):
        code, _ = self._diff({"a": {}}, {"a": {"k": 1}}, allow="a.k")
        self.assertEqual(code, 0)

    def test_dotted_key_does_not_collide_with_nesting(self):
        code, _ = self._diff({"a.b": 1}, {"a": {"b": 1}})
        self.assertEqual(code, 1)

    def test_bool_is_not_number(self):
        code, _ = self._diff({"a": True}, {"a": 1})
        self.assertEqual(code, 1)


class SnapshotOutputAliasGuardTest(unittest.TestCase):
    """Any destination inside the repository is refused (symlinks, case
    folds, unicode normalization, and ..-prefixed basenames are all inside
    after realpath); multi-linked existing files are refused anywhere."""

    def _run_snapshot(self, root: Path, req: str) -> int:
        old, argv = ric.REPO_ROOT, sys.argv
        ric.REPO_ROOT = str(root)
        sys.argv = ["ric", "--snapshot", req]
        try:
            out = io.StringIO()
            with redirect_stdout(out):
                return ric.main()
        finally:
            ric.REPO_ROOT, sys.argv = old, argv

    def test_all_in_repo_destinations_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(os.path.realpath(tmp))
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            victim = root / "Tracked.JSON"
            victim.write_text("precious")
            dotdot = root / "..victim.json"
            dotdot.write_text("precious2")
            subprocess.run(
                ["git", "-C", str(root), "add", "Tracked.JSON", "..victim.json"],
                check=True,
            )
            link = root / "alias.json"
            link.symlink_to(victim)
            for req in (
                str(link),
                str(root / "tracked.json"),
                str(root / "..victim.json"),
                str(root / "brand_new.json"),
            ):
                self.assertEqual(self._run_snapshot(root, req), 2, req)
            self.assertEqual(victim.read_text(), "precious")
            self.assertEqual(dotdot.read_text(), "precious2")

    def test_hard_link_alias_outside_repo_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(os.path.realpath(tmp)) / "repo"
            outside = Path(os.path.realpath(tmp)) / "outside"
            root.mkdir(); outside.mkdir()
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            victim = root / "tracked.json"
            victim.write_text("precious")
            subprocess.run(["git", "-C", str(root), "add", "tracked.json"], check=True)
            hard = outside / "hard.json"
            os.link(victim, hard)
            self.assertEqual(self._run_snapshot(root, str(hard)), 2)
            self.assertEqual(victim.read_text(), "precious")

    def test_outside_scratch_destination_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(os.path.realpath(tmp)) / "repo"
            root.mkdir()
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            dest = Path(os.path.realpath(tmp)) / "snap.json"
            code = self._run_snapshot(root, str(dest))
            self.assertEqual(code, 0)
            self.assertTrue(dest.exists())




class RoundThreeScannerProbes(unittest.TestCase):
    def test_escaped_backticks_do_not_open_code_spans(self):
        text = "\\` [bad](MISSING.md) \\`"
        self.assertEqual(ric.scan_markdown_link_targets(text), ["MISSING.md"])

    def test_windows_path_preserved_and_absolute(self):
        targets = ric.scan_markdown_link_targets("[x](C:\\Users\\me\\X.md)")
        self.assertEqual(targets, ["C:\\Users\\me\\X.md"])
        self.assertEqual(ric.classify_target(targets[0]), "absolute")

    def test_uri_schemes_and_extensionless(self):
        self.assertEqual(ric.classify_target("doi:10.1000/xyz"), "skip")
        self.assertEqual(ric.classify_target("LICENSE"), "relative")
        self.assertEqual(ric.classify_target("file:///tmp/L.md"), "absolute")


class RoundThreeLedgerProbes(unittest.TestCase):
    def test_claim_id_filename_identity_and_status_enum(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = ric.REPO_ROOT
            ric.REPO_ROOT = tmp
            try:
                d = Path(tmp) / ric.LEDGER_PREFIX / "aa"
                d.mkdir(parents=True)
                (d / "alpha.json").write_text(json.dumps(
                    {"claim_id": "beta", "effective_status": "unaudited"}))
                (d / "typo.json").write_text(json.dumps(
                    {"claim_id": "typo", "effective_status": "retianed"}))
                result = ric.collect_ledger([
                    ric.LEDGER_PREFIX + "aa/alpha.json",
                    ric.LEDGER_PREFIX + "aa/typo.json",
                ])
                errors = " ".join(result["shard_parse_errors"])
                self.assertIn("!= filename stem", errors)
                self.assertIn("not in controlled set", errors)
                self.assertEqual(
                    result["effective_status_histogram"].get("SCHEMA_INVALID"), 1
                )
                self.assertEqual(result["retained_grade_total"], 0)
            finally:
                ric.REPO_ROOT = old


class RoundThreeDiffProbes(DiffSensitivityTest):
    def test_bool_vs_one_inside_array(self):
        code, _ = self._diff({"a": [True]}, {"a": [1]})
        self.assertEqual(code, 1)

    def test_nested_dict_inside_array(self):
        code, _ = self._diff({"a": [{"b": True}]}, {"a": [{"b": 1}]})
        self.assertEqual(code, 1)

    def test_array_leaf_path_is_allowable(self):
        code, _ = self._diff({"a": [{}]}, {"a": [{"b": 1}]}, allow="a.0.b")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
