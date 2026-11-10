"""Tests for the landing-review depth: the script, its prose and their binding."""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import check_review_loop_skill_contract as contract  # noqa: E402

ROOT = contract.REPO_ROOT
SOURCE = ROOT / contract.REVIEW_DEPTH_REL
spec = importlib.util.spec_from_file_location("review_depth", SOURCE)
depth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(depth)

Change = depth.Change
LENSES = (ROOT / contract.SKILL_REL).parent / contract.REVIEW_DEPTH_LENSES_REL


def reasons(result):
    return {item["path"]: item["reason"] for item in result["full_read"]}


class ReviewDepthRuleTest(unittest.TestCase):
    """The rule itself, on path lists."""

    def test_a_unit_that_only_adds_working_material_gets_the_scope_read(self):
        result = depth.classify([
            Change("A", ".claude/science/physics-loops/gap/HANDOFF.md"),
            Change("M", ".claude/science/physics-loops/gap/STATE.md"),
            Change("D", ".claude/science/physics-loops/gap/old.log"),
            Change("A", "research/ym4d/parts/t0.md"),
            Change("M", "research/ym4d/FINISH.md"),
            Change("A", "docs/NEW_BOUNDED_THEOREM_NOTE_2026-11-10.md"),
            Change("A", "scripts/frontier_new_runner.py", "100755"),
            Change("A", "logs/runner-cache/frontier_new_runner.txt"),
        ])
        self.assertEqual(result["depth"], "scope")
        self.assertEqual(result["full_read"], [])
        self.assertEqual(result["working_material"], {
            ".claude/science/": 3, "research/": 2, "docs/<name>.md": 1,
            "scripts/<name>.py": 1, "logs/runner-cache/": 1,
        })

    def test_every_other_change_gets_the_full_read(self):
        outside_new = "new file outside the working-material paths"
        outside_changed = "changes a file outside the working-material paths"
        held = "changes or deletes a file that the base holds"
        cases = [
            (Change("M", "docs/EXISTING_NOTE.md"), held),
            (Change("D", "docs/EXISTING_NOTE.md", "000000"), held),
            (Change("T", "docs/EXISTING_NOTE.md"), held),
            (Change("M", "scripts/frontier_existing.py"), held),
            (Change("D", "logs/runner-cache/existing.txt", "000000"), held),
            (Change("R", "docs/RENAMED_NOTE.md"), held),
            (Change("M", "AGENTS.md"), outside_changed),
            (Change("M", "docs/ai_methodology/RULES.md"), outside_changed),
            (Change("D", "docs/audit/data/axiom_premise_nodes.json", "000000"), outside_changed),
            (Change("A", "docs/ai_methodology/procedures/new.md"), outside_new),
            (Change("A", "docs/audit/data/dispatch_sidecar.json"), outside_new),
            (Change("A", "docs/audit/scripts/tests/test_new.py"), outside_new),
            (Change("A", "docs/repo/NEW_POLICY.md"), outside_new),
            (Change("A", "docs/sub/NOTE.md"), outside_new),
            (Change("A", "docs/NOTE.txt"), outside_new),
            (Change("A", "scripts/review_support/tool.py"), outside_new),
            (Change("A", "scripts/install.sh"), outside_new),
            (Change("A", "tests/test_new.py"), outside_new),
            (Change("A", ".github/workflows/new.yml"), outside_new),
            (Change("A", ".claude/commands/new.md"), outside_new),
            (Change("A", ".claude/science.md"), outside_new),
            (Change("A", "researchx/a.md"), outside_new),
            (Change("A", "research.md"), outside_new),
            (Change("A", "README_NEW.md"), outside_new),
            (Change("A", "formalization/New.lean"), outside_new),
            (Change("A", "docs/LINK.md", "120000"), "not a regular file"),
            (Change("A", "research/ym4d/link", "120000"), "not a regular file"),
            (Change("M", ".claude/science/sub", "160000"), "not a regular file"),
            (Change("A", "docs/../AGENTS.md"), "not a plain repository path"),
            (Change("A", "/etc/passwd"), "not a plain repository path"),
        ]
        for change, reason in cases:
            with self.subTest(change=change):
                result = depth.classify([change])
                self.assertEqual(result["depth"], "full")
                self.assertEqual(reasons(result), {change.path: reason})

    def test_a_path_the_base_gained_since_the_branch_point_is_not_new(self):
        change = Change("A", "docs/NEW_NOTE.md")
        self.assertEqual(depth.classify([change])["depth"], "scope")
        result = depth.classify([change], frozenset({"docs/NEW_NOTE.md"}))
        self.assertEqual(reasons(result), {
            "docs/NEW_NOTE.md": "the base branch now holds this path"})

    def test_one_full_read_path_gives_the_whole_unit_the_full_read(self):
        changes = [Change("A", f"research/ym4d/part-{n}.md") for n in range(100)]
        changes.append(Change("M", "docs/KEY_SCIENCE.md"))
        result = depth.classify(changes)
        self.assertEqual(result["depth"], "full")
        self.assertEqual(result["paths"], 101)
        self.assertEqual(list(reasons(result)), ["docs/KEY_SCIENCE.md"])
        self.assertEqual(result["working_material"], {"research/": 100})

    def test_an_empty_delta_has_no_depth(self):
        with self.assertRaises(ValueError):
            depth.classify([])

    def test_long_full_read_lists_are_cut_only_in_the_text_output(self):
        changes = [Change("M", f"docs/NOTE_{n:03d}.md") for n in range(45)]
        result = depth.classify(changes)
        text = depth.render(result)
        self.assertIn("full-read paths: 45 of 45", text)
        self.assertIn("... 5 more; pass --all to list them", text)
        self.assertNotIn("more; pass", depth.render(result, list_all=True))
        self.assertEqual(len(result["full_read"]), 45)


class ReviewDepthGitTest(unittest.TestCase):
    """The script against a real repository."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.write("AGENTS.md", "rules\n")
        self.write("docs/OLD_NOTE.md", "# Old note\n")
        self.write("scripts/old_runner.py", "print('old')\n")
        self.write("research/target/STATE.md", "state one\n")
        self.commit("base")
        self.git("checkout", "-q", "-b", "unit")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], text=True, stderr=subprocess.STDOUT
        ).strip()

    def write(self, relative, text):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def run_script(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = depth.main(["--repo", str(self.repo), "--base", "main", *args])
        return code, out.getvalue(), err.getvalue()

    def add_working_material(self):
        self.write("docs/NEW_NOTE.md", "# New note\n")
        self.write("scripts/new_runner.py", "print('new')\n")
        self.write("logs/runner-cache/new_runner.txt", "new\n")
        self.write("research/target/STATE.md", "state two\n")
        self.write(".claude/science/physics-loops/gap/HANDOFF.md", "handoff\n")
        self.commit("working material")

    def test_new_working_material_prints_scope(self):
        self.add_working_material()
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        lines = out.splitlines()
        self.assertEqual(lines[0], "DEPTH scope")
        self.assertIn(
            "working material: .claude/science/ 1, research/ 1, docs/<name>.md 1, "
            "scripts/<name>.py 1, logs/runner-cache/ 1", lines)
        self.assertNotIn("full-read paths", out)

    def test_a_changed_note_prints_full(self):
        self.add_working_material()
        self.write("docs/OLD_NOTE.md", "# Old note, corrected\n")
        self.commit("correct a note")
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH full")
        self.assertIn("full-read paths: 1 of 6", out)
        self.assertIn(
            "  M docs/OLD_NOTE.md: changes or deletes a file that the base holds", out)

    def test_a_renamed_note_is_a_deletion_and_prints_full(self):
        self.git("mv", "docs/OLD_NOTE.md", "docs/OLD_NOTE_RENAMED.md")
        self.commit("rename")
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH full")
        self.assertIn("  D docs/OLD_NOTE.md: changes or deletes a file that the base holds", out)
        self.assertNotIn("OLD_NOTE_RENAMED.md:", out)

    def test_a_changed_rule_or_tool_prints_full(self):
        self.write("AGENTS.md", "other rules\n")
        self.write("scripts/old_runner.py", "print('changed')\n")
        self.write("tests/test_new.py", "pass\n")
        self.commit("rules and tools")
        code, out, _ = self.run_script("--json", "unit")
        self.assertEqual(code, 0)
        result = json.loads(out)
        self.assertEqual(result["depth"], "full")
        self.assertEqual(reasons(result), {
            "AGENTS.md": "changes a file outside the working-material paths",
            "scripts/old_runner.py": "changes or deletes a file that the base holds",
            "tests/test_new.py": "new file outside the working-material paths",
        })

    def test_a_new_symlink_prints_full(self):
        os.symlink("../AGENTS.md", self.repo / "docs" / "LINK.md")
        self.commit("symlink")
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH full")
        self.assertIn("  A docs/LINK.md: not a regular file", out)

    def test_unrelated_movement_of_the_base_keeps_the_depth(self):
        self.add_working_material()
        self.git("checkout", "-q", "main")
        self.write("docs/OTHER_NOTE.md", "# Other\n")
        self.write("AGENTS.md", "rules, changed on main\n")
        self.commit("main moves")
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH scope")

    def test_a_path_the_base_added_meanwhile_prints_full(self):
        self.add_working_material()
        self.git("checkout", "-q", "main")
        self.write("docs/NEW_NOTE.md", "# The same path, from another PR\n")
        self.commit("main gains the path")
        code, out, _ = self.run_script("unit")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH full")
        self.assertIn("  A docs/NEW_NOTE.md: the base branch now holds this path", out)

    def test_a_unit_of_two_heads_takes_the_deeper_read(self):
        self.add_working_material()
        self.git("checkout", "-q", "-b", "second", "main")
        self.write("docs/OLD_NOTE.md", "# Old note, corrected\n")
        self.commit("second constituent")
        self.assertEqual(self.run_script("unit")[1].splitlines()[0], "DEPTH scope")
        code, out, _ = self.run_script("unit", "second")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0], "DEPTH full")
        self.assertIn("full-read paths: 1 of 6", out)

    def test_a_failure_prints_no_depth_line(self):
        self.add_working_material()
        for args in (("no-such-ref",), ("--", "--upload-pack=x"), ("main",)):
            with self.subTest(args=args):
                code, out, err = self.run_script(*args)
                self.assertEqual(code, 2)
                self.assertEqual(out, "")
                self.assertIn("review_depth:", err)


class ReviewDepthContractTest(unittest.TestCase):
    """Prose and script state one rule, and the contract check holds both."""

    @classmethod
    def setUpClass(cls):
        cls.lenses = LENSES.read_text(encoding="utf-8")
        cls.script = SOURCE.read_text(encoding="utf-8")
        cls.skill, routing_failures = contract.load_skill_contract(ROOT)
        assert not routing_failures, routing_failures
        cls.generator = (ROOT / contract.GENERATOR_REL).read_text(encoding="utf-8")
        cls.pipeline = (ROOT / contract.PIPELINE_REL).read_text(encoding="utf-8")
        cls.command = (ROOT / contract.COMMAND_REL).read_text(encoding="utf-8")

    def copy_skill(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        entry = Path(temp.name) / contract.SKILL_REL
        source = ROOT / contract.SKILL_REL
        entry.parent.mkdir(parents=True)
        shutil.copyfile(source, entry)
        for relative in contract.REFERENCE_TRIGGER_RULES:
            destination = entry.parent / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source.parent / relative, destination)
        return Path(temp.name), entry

    def replace(self, text, old, new):
        self.assertIn(old, text, f"mutation needle absent: {old}")
        return text.replace(old, new)

    def test_the_live_repository_passes(self):
        self.assertEqual(contract.validate_repo(ROOT), [])

    def test_the_table_is_the_scripts_list(self):
        self.assertEqual(contract.review_depth_table(self.lenses), depth.WORKING_MATERIAL)
        self.assertEqual(
            contract.review_depth_script_paths(self.script), depth.WORKING_MATERIAL)
        self.assertTrue(contract.review_depth_paths_ok(self.lenses, self.script))

    def test_a_changed_table_no_longer_matches_the_script(self):
        row = "| `docs/<name>.md` | added |"
        heading = "## Review depth"
        mutations = {
            "wider change": (row, "| `docs/<name>.md` | any |"),
            "wider path": (row, "| `docs/` | added |"),
            "row removed": (row + "\n", ""),
            "row added": (row, row + "\n| `tests/` | added |"),
            "row hidden in a comment": (row, "<!-- " + row + " -->"),
            "row shown as code": (row, "    " + row),
            "two sections": (heading, heading + "\n\n| `docs/` | any |\n\n" + heading),
            "no section": (heading, "## Depth"),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                mutated = self.replace(self.lenses, old, new)
                self.assertFalse(contract.review_depth_paths_ok(mutated, self.script))

    def test_a_changed_script_no_longer_matches_the_table(self):
        entry = '    ("docs/<name>.md", "added"),\n'
        mutations = {
            "wider change": (entry, '    ("docs/<name>.md", "any"),\n'),
            "wider path": (entry, '    ("docs/", "any"),\n'),
            "entry added": (entry, entry + '    ("tests/", "added"),\n'),
            "entry removed": (entry, ""),
            "computed list": ("WORKING_MATERIAL = (", "WORKING_MATERIAL = tuple(EXTRA) + ("),
            "list renamed": ("WORKING_MATERIAL = (", "WORKING = ("),
            "second assignment": (
                "REGULAR_MODES =", "WORKING_MATERIAL = ()\nREGULAR_MODES ="),
            "syntax error": ("WORKING_MATERIAL = (", "WORKING_MATERIAL = (("),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                mutated = self.replace(self.script, old, new)
                self.assertFalse(contract.review_depth_paths_ok(self.lenses, mutated))

    def test_a_missing_script_fails_the_repository_check(self):
        root, _entry = self.copy_skill()
        for relative in (contract.GENERATOR_REL, contract.PIPELINE_REL,
                         contract.COMMAND_REL, *contract.PLACEMENT_REFERENCES.values()):
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)
        self.assertEqual(contract.validate_repo(root), ["review_depth_paths"])
        script = root / contract.REVIEW_DEPTH_REL
        script.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE, script)
        self.assertEqual(contract.validate_repo(root), [])

    def test_the_depth_rule_cannot_be_weakened_in_the_lens_reference(self):
        section_start = "## Review depth\n"
        section_end = "## Reviewer Fanout\n"
        mutations = {
            "most paths": ("only when every changed path is working material",
                           "when most changed paths are working material"),
            "scope by default": ("Every other change gets the full read and prints",
                                 "Every other change gets a scope read and prints"),
            "split units": ("One such path gives the whole unit the full read.",
                            "One such path gets the full read and the rest a scope read."),
            "scope on failure": ("`DEPTH` line, the unit gets the full read.",
                                 "`DEPTH` line, the unit gets a scope read."),
            "lowering allowed": ("Nobody lowers a depth.", "The lander may lower a depth."),
            "raise without a record": ("and records the\nreason.", "at will."),
            "lenses become optional": ("list, it describes the full read.",
                                       "list, a scope read may leave it out."),
            "scope read as a check": (
                "A scope read files no check record and moves no standing.",
                "A scope read counts as a check of what it read."),
            "rule kept only as a sample": (
                "Nobody lowers a depth. Raise it when",
                "Nobody lowers a depth.\n\n```text\nRaise it when"),
            "rule kept only as indented code": (
                "A scope read files no check record",
                "    A scope read files no check record"),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                root, entry = self.copy_skill()
                path = entry.parent / contract.REVIEW_DEPTH_LENSES_REL
                text = self.replace(path.read_text(encoding="utf-8"), old, new)
                path.write_text(text, encoding="utf-8")
                self.assertIn("routed_review_depth", contract.load_skill_contract(root)[1])
        with self.subTest(name="section hidden in a comment"):
            root, entry = self.copy_skill()
            path = entry.parent / contract.REVIEW_DEPTH_LENSES_REL
            text = path.read_text(encoding="utf-8")
            text = self.replace(text, section_start, "<!--\n" + section_start)
            text = self.replace(text, section_end, "-->\n\n" + section_end)
            path.write_text(text, encoding="utf-8")
            self.assertIn("routed_review_depth", contract.load_skill_contract(root)[1])

    def test_the_depth_rule_cannot_be_weakened_in_the_entry_point(self):
        mutations = {
            "lowering allowed": ("with a recorded reason and is never lowered",
                                 "or lowered with a recorded reason"),
            "scope by default": ("and the full read for every other\nchange.",
                                 "and a scope read for every other\nchange."),
            "depth chosen by hand": ("reads the depth from the unit's delta",
                                     "suggests a depth for the unit"),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                root, entry = self.copy_skill()
                entry.write_text(
                    self.replace(entry.read_text(encoding="utf-8"), old, new),
                    encoding="utf-8")
                self.assertIn("routed_review_depth", contract.load_skill_contract(root)[1])
                mutated = self.replace(self.skill, old, new)
                self.assertIn("review_depth", contract.validate_texts(
                    mutated, self.generator, self.pipeline, self.command))

    def test_the_depth_rule_cannot_be_weakened_in_the_command(self):
        mutations = {
            "lowering allowed": ("never lower one.", "lower one when a unit is large."),
            "scope by default": ("the full read for\n   every other change.",
                                 "a scope read for\n   every other change."),
            "script not named": ("`scripts/review_depth.py`", "the lander's judgment"),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                mutated = self.replace(self.command, old, new)
                self.assertIn("command_review_depth", contract.validate_texts(
                    self.skill, self.generator, self.pipeline, mutated))
        self.assertEqual(contract.validate_texts(
            self.skill, self.generator, self.pipeline, self.command), [])

    def test_the_full_read_keeps_its_lenses_and_gates(self):
        for family in ("reviewer_lenses", "independent_math_and_mutations",
                       "proof_import_governance", "no_go_discipline"):
            self.assertIn(family, contract.SKILL_RULES)
        self.assertTrue(contract._reviewer_structure_ok(
            contract._markdown_scan(self.lenses).prose))

    def test_the_procedure_and_the_setting_state_the_same_rule(self):
        land = (ROOT / "docs/ai_methodology/procedures/land.md").read_text(encoding="utf-8")
        step = land.split("4. **Independent read.**", 1)[1].split("\n5. **", 1)[0]
        step = " ".join(step.split())
        self.assertIn("`review_depth.py` sets the depth; raise it with a reason, "
                      "never lower it.", step)
        self.assertIn("A unit that only adds working material gets a scope read", step)
        self.assertIn("Any other unit gets the full read", step)
        settings = (ROOT / "docs/ai_methodology/SETTINGS.md").read_text(encoding="utf-8")
        row = next(line for line in settings.splitlines()
                   if line.startswith("| Landing review |"))
        self.assertIn("`skills/review-loop/scripts/review_depth.py`", row)
        self.assertIn("the full read for every other change", row)
        self.assertIn("is never lowered", row)
        self.assertIn("2026-11-10", row)


if __name__ == "__main__":
    unittest.main()
