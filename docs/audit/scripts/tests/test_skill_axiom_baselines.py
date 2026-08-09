"""Regression tests for the skill axiom-baseline generator and its guard.

Every case runs against a temp copy of the real sources and skill docs, so the
committed repo state is never mutated. The named boundary: in-sync passes, a
hand-edit of a generated block fails, an axiom-source edit fails until
regeneration, regeneration is byte-stable, and sourced values actually reach the
rendered blocks.
"""

import io
import json
import shutil
import sys
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from tempfile import TemporaryDirectory

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import generate_skill_axiom_baselines as gen  # noqa: E402

REAL_REPO_ROOT = gen.REPO_ROOT


def _copy_into(root: Path, rel_path: str) -> Path:
    dest = root / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REAL_REPO_ROOT / rel_path, dest)
    return dest


def make_fixture(root: Path) -> Path:
    """Copy every file the generator reads or writes into a temp repo root."""
    _copy_into(root, gen.REGISTRY_REL)
    registry = json.loads((root / gen.REGISTRY_REL).read_text(encoding="utf-8"))
    for entry in registry["nodes"].values():
        _copy_into(root, entry["current_path"])
    for target in gen.TARGETS:
        _copy_into(root, target.path)
    _copy_into(root, gen.MANIFEST_REL)
    return root


def run_generator(root: Path, check: bool) -> tuple[int, str]:
    argv = ["--repo-root", str(root)]
    if check:
        argv.append("--check")
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = gen.main(argv)
    return code, out.getvalue() + err.getvalue()


def read(root: Path, rel_path: str) -> str:
    return (root / rel_path).read_text(encoding="utf-8")


def write(root: Path, rel_path: str, text: str) -> None:
    (root / rel_path).write_text(text, encoding="utf-8")


class FixtureTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = make_fixture(Path(self._tmp.name))
        self.axioms_rel = json.loads(
            read(self.root, gen.REGISTRY_REL)
        )["nodes"][gen.AXIOM_NODE_ID]["current_path"]


class InSyncTest(FixtureTestCase):
    def test_committed_state_passes_check(self):
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 0, output)
        self.assertIn("axiom-baseline block in sync", output)
        self.assertIn("source acknowledgment current", output)

    def test_committed_repo_itself_passes_check(self):
        """The real tree, not just the fixture, must be in sync."""
        code, output = run_generator(REAL_REPO_ROOT, check=True)
        self.assertEqual(code, 0, output)

    def test_every_target_carries_both_markers(self):
        for target in gen.TARGETS:
            text = read(self.root, target.path)
            self.assertEqual(
                text.count(gen.BEGIN_MARKER), 1, f"{target.path} BEGIN marker"
            )
            self.assertEqual(
                text.count(gen.END_MARKER), 1, f"{target.path} END marker"
            )


class SkillBlockEditTest(FixtureTestCase):
    def test_hand_edit_inside_block_fails_with_diff(self):
        target = gen.TARGETS[0]
        text = read(self.root, target.path)
        edited = text.replace(
            "The approved axiom baseline",
            "The approved axiom baseline, more or less,",
            1,
        )
        self.assertNotEqual(text, edited, "test edit did not apply")
        write(self.root, target.path, edited)

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("generated block is stale", output)
        self.assertIn("more or less", output)
        self.assertIn("--- " + target.path, output)

    def test_deleted_marker_fails(self):
        target = gen.TARGETS[1]
        text = read(self.root, target.path)
        write(self.root, target.path, text.replace(gen.END_MARKER, "", 1))
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("expected exactly one BEGIN and one END marker", output)

    def test_write_repairs_a_hand_edited_block(self):
        target = gen.TARGETS[2]
        original = read(self.root, target.path)
        write(
            self.root,
            target.path,
            original.replace("availability is its support", "anything goes", 1),
        )
        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertEqual(read(self.root, target.path), original)
        self.assertEqual(run_generator(self.root, check=True)[0], 0)


class AxiomSourceEditTest(FixtureTestCase):
    def test_benign_axiom_edit_fails_until_regenerated(self):
        text = read(self.root, self.axioms_rel)
        write(self.root, self.axioms_rel, text + "\nA later clarification.\n")

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1, output)
        self.assertIn("source acknowledgment is stale", output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 0, output)

    def test_primitive_note_edit_fails_until_regenerated(self):
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        note_rel = registry["nodes"]["kinetic_isotropy_primitive"]["current_path"]
        write(self.root, note_rel, read(self.root, note_rel) + "\nAddendum.\n")

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_changed_admissibility_clause_is_source_drift(self):
        """The clause the templates interpolate cannot change silently."""
        atom = next(a for a in gen.ATOMS if a.key == "distribution_clause")
        text = read(self.root, self.axioms_rel)
        self.assertIn(atom.text, text.replace("\n", " "))
        write(
            self.root,
            self.axioms_rel,
            text.replace(
                "the probability distribution over the possibilities is\ndetermined by, and varies with, the nearest-neighbor conditions",
                "the possibilities available at a site are fixed by the\nnearest-neighbor conditions",
            ),
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("distribution_clause", output)

    def test_renamed_axiom_is_a_governance_failure(self):
        text = read(self.root, self.axioms_rel)
        write(self.root, self.axioms_rel, text.replace("4. **Record**", "4. **Registration**", 1))
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("governance event", output)

    def test_lost_anchor_is_source_drift(self):
        text = read(self.root, self.axioms_rel)
        write(self.root, self.axioms_rel, text.replace("Records form.", "", 1))
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)


class RegistryEditTest(FixtureTestCase):
    def test_repathed_primitive_note_propagates_into_the_roster(self):
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        node = registry["nodes"]["realized_state_primitive"]
        old_path, new_path = node["current_path"], "docs/REALIZED_STATE_PRIMITIVE_NOTE_2099-01-01.md"
        (self.root / new_path).write_text(read(self.root, old_path), encoding="utf-8")
        node["current_path"] = new_path
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)

        rendered = read(self.root, "docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md")
        self.assertIn(new_path, rendered)
        self.assertNotIn(old_path, rendered)

    def test_newly_registered_primitive_fails_closed(self):
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        registry["canonical_ids"].append("brand_new_primitive")
        registry["nodes"]["brand_new_primitive"] = {
            "current_path": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
            "aliased_paths": [],
            "legacy_claim_ids": [],
            "note": "hypothetical",
        }
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("brand_new_primitive", output)
        self.assertIn("PRIMITIVE_ANCHORS", output)

    def test_unmentioned_primitive_fails_roster_coverage(self):
        """A primitive outside a file's roster_scope must still be named there."""
        target = next(t for t in gen.TARGETS if t.key == "review-loop")
        text = read(self.root, target.path)
        stripped = text.replace("realized_state_primitive", "REDACTED")
        self.assertNotEqual(text, stripped)
        write(self.root, target.path, stripped)
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("realized_state_primitive", output)
        self.assertIn("neither rendered in the generated block", output)


class IdempotenceTest(FixtureTestCase):
    def test_write_is_byte_stable_across_runs(self):
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        first = {
            rel: read(self.root, rel)
            for rel in [t.path for t in gen.TARGETS] + [gen.MANIFEST_REL]
        }
        for _ in range(3):
            self.assertEqual(run_generator(self.root, check=False)[0], 0)
        second = {rel: read(self.root, rel) for rel in first}
        self.assertEqual(first, second)

    def test_write_leaves_committed_state_untouched(self):
        before = {
            rel: read(self.root, rel)
            for rel in [t.path for t in gen.TARGETS] + [gen.MANIFEST_REL]
        }
        code, output = run_generator(self.root, check=False)
        self.assertEqual(code, 0, output)
        after = {rel: read(self.root, rel) for rel in before}
        self.assertEqual(before, after)
        self.assertIn("unchanged", output)


class RenderingTest(FixtureTestCase):
    def test_every_declared_exclusion_is_used_by_some_target(self):
        used = set(gen.PHYSICS_LOOP_EXCLUSIONS)
        used |= set(gen.REVIEW_LOOP_EXCLUSIONS)
        used |= set(gen.AUDIT_LOOP_EXCLUSIONS)
        self.assertEqual(set(gen.EXCLUSIONS) - used, set())

    def test_blocks_wrap_within_the_declared_width(self):
        src = gen.load_source(self.root)
        for key, lines in gen.render_all(src).items():
            for line in lines:
                self.assertLessEqual(len(line), gen.WRAP_WIDTH, f"{key}: {line!r}")

    def test_manifest_records_every_source_and_target(self):
        src = gen.load_source(self.root)
        manifest = gen.build_manifest(src, gen.render_all(src))
        self.assertEqual(
            set(manifest["targets"]), {t.path for t in gen.TARGETS}
        )
        self.assertIn(self.axioms_rel, manifest["sources"])
        self.assertIn(gen.REGISTRY_REL, manifest["sources"])
        for prim in src.primitives:
            self.assertIn(prim.path, manifest["sources"])


if __name__ == "__main__":
    unittest.main()
