"""Regression tests for the skill axiom-baseline generator and its guard.

Every case runs against a temp copy of the real sources and skill docs, so the
committed repo state is never mutated. The named boundary: generation is
extraction (never assertion), a source revision propagates into every target
before any digest is refreshed, roster coverage is semantic rather than nominal,
and the generator fails closed when a registered source loses the structure the
extraction addresses.

The mutation cases below are the ones that defeated the previous
literal-answer/anchor design (review iteration 1): a revised Admissibility
clause, an axiom-source edit no anchor guarded, a primitive boundary revision
that left the three selected anchors intact, and a roster id present only inside
an HTML comment.
"""

import io
import json
import re
import shutil
import sys
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

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


def block_text(root: Path, rel_path: str) -> str:
    """The generated block of a target file, markers excluded."""
    text = read(root, rel_path)
    begin = text.index(gen.BEGIN_MARKER) + len(gen.BEGIN_MARKER)
    end = text.index(gen.END_MARKER, begin)
    return text[begin:end]


def source_haystack(root: Path, rel_path: str) -> str:
    """The source doc as one normalized line, bullet markers removed."""
    raw = gen.delink(read(root, rel_path))
    lines = [re.sub(r"^\s*[-*]\s+", "", line) for line in raw.splitlines()]
    return gen.norm(gen.join_source_lines(lines))


class FixtureTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = make_fixture(Path(self._tmp.name))
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        self.axioms_rel = registry["nodes"][gen.AXIOM_NODE_ID]["current_path"]
        self.kinetic_rel = registry["nodes"]["kinetic_isotropy_primitive"][
            "current_path"
        ]

    def skill_targets(self) -> list[gen.Target]:
        return [t for t in gen.TARGETS if gen.SPAN_AXIOMS in t.spans]

    def assertInEveryTarget(self, needle: str, targets=None) -> None:
        for target in targets if targets is not None else gen.TARGETS:
            self.assertIn(
                gen.norm(needle),
                gen.norm(block_text(self.root, target.path)),
                f"{target.path} does not carry {needle!r}",
            )

    def assertInNoTarget(self, needle: str, targets=None) -> None:
        for target in targets if targets is not None else gen.TARGETS:
            self.assertNotIn(
                gen.norm(needle),
                gen.norm(block_text(self.root, target.path)),
                f"{target.path} still carries {needle!r}",
            )


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


class ExtractionFidelityTest(FixtureTestCase):
    """Generation must be extraction: no rendered sentence is authored here."""

    def all_extracts(self) -> list[gen.Extract]:
        src = gen.load_source(self.root)
        extracts = list(src.axiom_extracts)
        for prim in src.primitives:
            extracts.extend((prim.grant, prim.boundary))
        return extracts

    def test_every_rendered_chunk_is_verbatim_in_its_source(self):
        haystacks: dict[str, str] = {}
        for extract in self.all_extracts():
            haystack = haystacks.setdefault(
                extract.source, source_haystack(self.root, extract.source)
            )
            for chunk in extract.chunks:
                if chunk.kind == "code":
                    # A fenced formula is inlined as a code span; check its text.
                    self.assertIn(chunk.text.strip("`,.;: "), haystack)
                    continue
                self.assertIn(
                    chunk.text,
                    haystack,
                    f"{extract.source} / '{extract.heading}': rendered text is "
                    f"not verbatim in the source",
                )

    def test_blocks_carry_the_axiom_memo_text_not_a_paraphrase(self):
        for target in self.skill_targets():
            body = gen.norm(block_text(self.root, target.path))
            for sentence in (
                "Physical sites are the points of the cubic lattice `Z^3`",
                "There is one fixed nearest-neighbor admissibility rule, "
                "covariant under lattice translations and proper cubic rotations",
                "Records form.",
                "A site with no record cannot be read.",
            ):
                self.assertIn(sentence, body, target.path)

            for retired in (
                "scalar readout `I` is additive",
                "`I(empty)=0`",
            ):
                self.assertNotIn(retired, body, target.path)

    def test_retired_paraphrases_are_gone(self):
        """Wordings the old templates asserted but the sources never said."""
        for target in gen.TARGETS:
            body = gen.norm(block_text(self.root, target.path))
            for phrase in (
                "one fixed finite-neighborhood rule",
                "M_2(ℂ)",
                "only its specific values are downstream",
                "occupancy rule",
                "law-domain derivation",
            ):
                self.assertNotIn(phrase, body, f"{target.path}: {phrase!r}")


class SkillBlockEditTest(FixtureTestCase):
    def test_hand_edit_inside_block_fails_with_diff(self):
        target = gen.TARGETS[0]
        text = read(self.root, target.path)
        edited = text.replace(
            "Physical sites are the points",
            "Physical sites are, more or less, the points",
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
            original.replace("Records form.", "Records never form.", 1),
        )
        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertEqual(read(self.root, target.path), original)
        self.assertEqual(run_generator(self.root, check=True)[0], 0)


class AxiomSourceEditTest(FixtureTestCase):
    def test_nested_axiom_subsection_propagates(self):
        text = read(self.root, self.axioms_rel)
        anchor = (
            "the probability distribution over the possibilities is\n"
            "determined by, and varies with, the nearest-neighbor conditions."
        )
        nested = (
            anchor
            + "\n\n#### Nested Admissibility Clarification\n\n"
            + "This nested axiom sentence must reach every applicable block."
        )
        revised = text.replace(anchor, nested, 1)
        self.assertNotEqual(text, revised, "test edit did not apply")
        write(self.root, self.axioms_rel, revised)

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertInEveryTarget(
            "This nested axiom sentence must reach every applicable block",
            self.skill_targets(),
        )
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_duplicate_addressed_axiom_heading_fails_closed(self):
        text = read(self.root, self.axioms_rel)
        duplicate = "\n\n### Record / Fixed Reality\n\nAmbiguous duplicate.\n"
        write(self.root, self.axioms_rel, text + duplicate)

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("duplicate ATX section heading", output)
        self.assertIn("Record / Fixed Reality", output)

    def test_edit_outside_every_extracted_span_still_fails_until_regenerated(self):
        text = read(self.root, self.axioms_rel)
        write(self.root, self.axioms_rel, text + "\nA later clarification.\n")

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1, output)
        self.assertIn("source acknowledgment is stale", output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 0, output)

    def test_revised_admissibility_clause_reaches_every_applicable_block(self):
        """Review finding F1, mutation 1: the clause must PROPAGATE, not stop."""
        before = {t.path: block_text(self.root, t.path) for t in gen.TARGETS}
        text = read(self.root, self.axioms_rel)
        revised = text.replace(
            "the probability distribution over the possibilities is\n"
            "determined by, and varies with, the nearest-neighbor conditions.",
            "the probability distribution over the possibilities is\n"
            "determined by the nearest-neighbor conditions and by nothing else.",
            1,
        )
        self.assertNotEqual(text, revised, "test edit did not apply")
        write(self.root, self.axioms_rel, revised)

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1, output)
        self.assertIn("generated block is stale", output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        skills = self.skill_targets()
        self.assertInEveryTarget(
            "determined by the nearest-neighbor conditions and by nothing else",
            skills,
        )
        for target in skills:
            self.assertNotEqual(
                before[target.path],
                block_text(self.root, target.path),
                f"{target.path} block did not visibly change",
            )
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_axiom_edit_no_anchor_guarded_propagates(self):
        """Review finding F1, mutation 2: a non-anchored source edit must land.

        Nothing in the retired ATOMS/ANCHORS tables touched the memo's open-gate
        list or its reading notes, so edits there changed no block.
        """
        before = {t.path: block_text(self.root, t.path) for t in gen.TARGETS}
        text = read(self.root, self.axioms_rel)
        revised = text.replace(
            "- `g_bare = 1` convention handling;",
            "- `g_bare = 1` convention handling and every coupling convention;",
            1,
        ).replace(
            "it does not supply the formation site, probability,\nor rate.",
            "it does not supply the formation site, probability,\nrate, or ordering.",
            1,
        )
        self.assertNotEqual(text, revised, "test edit did not apply")
        write(self.root, self.axioms_rel, revised)

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)

        skills = self.skill_targets()
        self.assertInEveryTarget("and every coupling convention", skills)
        self.assertInEveryTarget("rate, or ordering", skills)
        for target in skills:
            self.assertNotEqual(before[target.path], block_text(self.root, target.path))
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_renamed_axiom_is_a_governance_failure(self):
        text = read(self.root, self.axioms_rel)
        write(
            self.root,
            self.axioms_rel,
            text.replace("4. **Record**", "4. **Registration**", 1),
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("governance event", output)

    def test_renamed_axiom_section_fails_closed(self):
        text = read(self.root, self.axioms_rel)
        write(
            self.root,
            self.axioms_rel,
            text.replace("### Record / Fixed Reality", "### Records", 1),
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("Record", output)

    def test_missing_qualification_section_fails_closed(self):
        text = read(self.root, self.axioms_rel)
        write(
            self.root,
            self.axioms_rel,
            text.replace(f"## {gen.QUALIFICATION_SECTION}", "## Notes", 1),
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn(gen.QUALIFICATION_SECTION, output)

    def test_emptied_extracted_section_fails_closed(self):
        text = read(self.root, self.axioms_rel)
        start = text.index(f"## {gen.OPEN_GATES_SECTION}")
        end = text.index("## Historical Context", start)
        write(
            self.root,
            self.axioms_rel,
            text[:start] + f"## {gen.OPEN_GATES_SECTION}\n\n" + text[end:],
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("would render nothing", output)


class PrimitiveSourceEditTest(FixtureTestCase):
    def assert_fenced_heading_is_not_structural(self, fence: str) -> None:
        text = read(self.root, self.kinetic_rel)
        next_heading = "## Why It Is A Primitive"
        inserted = (
            f"{fence}text\n"
            "## Fenced Example Heading\n"
            "FENCED_CODE_SENTINEL\n"
            f"{fence}\n\n"
            "VISIBLE_AFTER_FENCE_SENTINEL\n\n"
            + next_heading
        )
        revised = text.replace(next_heading, inserted, 1)
        self.assertNotEqual(text, revised, "test edit did not apply")
        write(self.root, self.kinetic_rel, revised)

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertInEveryTarget("FENCED_CODE_SENTINEL")
        self.assertInEveryTarget("VISIBLE_AFTER_FENCE_SENTINEL")
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_backtick_fenced_heading_is_not_structural(self):
        self.assert_fenced_heading_is_not_structural("```")

    def test_tilde_fenced_heading_is_not_structural(self):
        self.assert_fenced_heading_is_not_structural("~~~")

    def test_nested_primitive_grant_and_boundary_propagate(self):
        text = read(self.root, self.kinetic_rel)
        grant_anchor = f"## {gen.PRIMITIVE_GRANT_SECTION}"
        boundary_anchor = f"## {gen.PRIMITIVE_BOUNDARY_SECTION}"
        grant_end = "## Why It Is A Primitive"
        boundary_end = "## Audit-Pipeline Treatment"
        revised = text.replace(
            grant_end,
            "### Nested Grant Clarification\n\n"
            "This nested grant sentence must propagate.\n\n"
            + grant_end,
            1,
        )
        revised = revised.replace(
            boundary_end,
            "### Nested Boundary Clarification\n\n"
            "This nested boundary sentence must propagate.\n\n"
            + boundary_end,
            1,
        )
        self.assertIn(grant_anchor, revised)
        self.assertIn(boundary_anchor, revised)
        self.assertNotEqual(text, revised, "test edit did not apply")
        write(self.root, self.kinetic_rel, revised)

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertInEveryTarget("This nested grant sentence must propagate")
        self.assertInEveryTarget("This nested boundary sentence must propagate")
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_changed_primitive_boundary_reaches_every_skill(self):
        """Review finding F2/F1: the mutation that the three anchors survived.

        The retired design kept `c_t = c_s`, the graining sentence, and "It does
        not supply the absolute scale" as anchors, so this revision regenerated
        nothing and left three skill surfaces asserting the superseded boundary.
        """
        before = {t.path: block_text(self.root, t.path) for t in gen.TARGETS}
        text = read(self.root, self.kinetic_rel)
        revised = text.replace(
            "spacing ratio (derived from the no-diagonal clause); it supplies "
            "only the\n  kinetic-form isotropy.",
            "spacing ratio (derived from the no-diagonal clause); it supplies "
            "the\n  kinetic-form isotropy and one supplied mass ratio.",
            1,
        )
        self.assertNotEqual(text, revised, "test edit did not apply")
        for anchor in (
            "c_t = c_s",
            "grained on the same footing as the spatial lattice edge",
            "It does not supply the absolute scale",
        ):
            self.assertIn(anchor, revised, "retired anchors must still survive")
        write(self.root, self.kinetic_rel, revised)

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1, output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertInEveryTarget("kinetic-form isotropy and one supplied mass ratio")
        self.assertInNoTarget("it supplies only the kinetic-form isotropy")
        for target in gen.TARGETS:
            self.assertNotEqual(
                before[target.path],
                block_text(self.root, target.path),
                f"{target.path} block did not visibly change",
            )
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_primitive_note_without_a_boundary_section_fails_closed(self):
        text = read(self.root, self.kinetic_rel)
        write(
            self.root,
            self.kinetic_rel,
            text.replace(
                f"## {gen.PRIMITIVE_BOUNDARY_SECTION}", "## Caveats", 1
            ),
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn(gen.PRIMITIVE_BOUNDARY_SECTION, output)
        self.assertIn("kinetic_isotropy_primitive", output)

    def test_unreadable_primitive_note_fails_closed(self):
        (self.root / self.kinetic_rel).unlink()
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("missing on disk", output)

    def test_primitive_without_current_path_fails_closed(self):
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        registry["nodes"]["realized_state_primitive"]["current_path"] = ""
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("no current_path", output)


class RegistryEditTest(FixtureTestCase):
    def test_repathed_primitive_note_propagates_into_the_roster(self):
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        node = registry["nodes"]["realized_state_primitive"]
        old_path = node["current_path"]
        new_path = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2099-01-01.md"
        (self.root / new_path).write_text(
            read(self.root, old_path), encoding="utf-8"
        )
        node["current_path"] = new_path
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")

        self.assertEqual(run_generator(self.root, check=True)[0], 1)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)

        rendered = read(self.root, gen.TARGETS[-1].path)
        self.assertIn(new_path, rendered)
        self.assertNotIn(old_path, rendered)

    def test_newly_registered_primitive_reaches_every_target(self):
        note_rel = "docs/HYPOTHETICAL_PRIMITIVE_NOTE.md"
        write(
            self.root,
            note_rel,
            "# Hypothetical Primitive\n\n"
            f"## {gen.PRIMITIVE_GRANT_SECTION}\n\n"
            "The framework takes one hypothetical reference, for this test only.\n\n"
            f"## {gen.PRIMITIVE_BOUNDARY_SECTION}\n\n"
            "- It does not supply any dimensionless quantity whatsoever.\n",
        )
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        registry["canonical_ids"].append("brand_new_primitive")
        registry["nodes"]["brand_new_primitive"] = {
            "current_path": note_rel,
            "aliased_paths": [],
            "legacy_claim_ids": [],
            "note": "hypothetical",
        }
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("brand_new_primitive", output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertInEveryTarget(
            "It does not supply any dimensionless quantity whatsoever"
        )
        self.assertInEveryTarget(
            "The framework takes one hypothetical reference, for this test only"
        )
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_newly_registered_primitive_without_the_sections_fails_closed(self):
        note_rel = "docs/STRUCTURELESS_PRIMITIVE_NOTE.md"
        write(self.root, note_rel, "# Structureless\n\nJust prose.\n")
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        registry["canonical_ids"].append("structureless_primitive")
        registry["nodes"]["structureless_primitive"] = {"current_path": note_rel}
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("structureless_primitive", output)
        self.assertEqual(run_generator(self.root, check=False)[0], 1)


class RosterCoverageTest(FixtureTestCase):
    """Review finding F2: coverage is the boundary text, not the node id."""

    def _replace_last_boundary(self, target: gen.Target, replacement: str) -> None:
        text = read(self.root, target.path)
        start = text.rindex(f"*{gen.PRIMITIVE_BOUNDARY_SECTION}*")
        end = text.index(gen.END_MARKER, start)
        write(self.root, target.path, text[:start] + replacement + text[end:])

    def test_boundary_text_inside_an_html_comment_is_not_coverage(self):
        target = gen.TARGETS[1]
        text = read(self.root, target.path)
        start = text.rindex(f"*{gen.PRIMITIVE_BOUNDARY_SECTION}*")
        end = text.index(gen.END_MARKER, start)
        commented = "<!--\n" + text[start:end] + "-->\n"
        write(self.root, target.path, text[:start] + commented + text[end:])

        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("realized_state_primitive", output)
        self.assertIn("as visible prose", output)
        self.assertIn(gen.PRIMITIVE_BOUNDARY_SECTION, output)

        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertNotIn("<!--\n*What This Does Not Do*", read(self.root, target.path))
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_bare_node_id_is_not_coverage(self):
        target = gen.TARGETS[2]
        self._replace_last_boundary(
            target, "  See `realized_state_primitive` in the registry.\n"
        )
        code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("realized_state_primitive", output)
        self.assertIn("as visible prose", output)

    def test_target_that_stops_rendering_the_roster_is_refused(self):
        crippled = tuple(
            gen.Target(
                key=t.key,
                path=t.path,
                marker_indent=t.marker_indent,
                spans=(gen.SPAN_AXIOMS,) if t.key == "review-loop" else t.spans,
            )
            for t in gen.TARGETS
        )
        with patch.object(gen, "TARGETS", crippled):
            code, output = run_generator(self.root, check=True)
        self.assertEqual(code, 1)
        self.assertIn("SOURCE DRIFT", output)
        self.assertIn("do not state", output)
        self.assertIn("review-loop", output)


class DigestPropagationInvariantTest(FixtureTestCase):
    """A digest refresh can never stand in for propagation."""

    def test_digest_is_not_refreshed_when_a_target_cannot_be_written(self):
        manifest_before = read(self.root, gen.MANIFEST_REL)
        broken = gen.TARGETS[1]
        intact = gen.TARGETS[0]
        intact_block_before = block_text(self.root, intact.path)

        text = read(self.root, self.kinetic_rel)
        write(
            self.root,
            self.kinetic_rel,
            text.replace(
                "It does not change any audit verdict.",
                "It does not change any audit verdict, ever.",
            ),
        )
        (self.root / broken.path).unlink()

        code, output = run_generator(self.root, check=False)
        self.assertEqual(code, 1, output)
        self.assertIn("refusing to refresh", output)
        self.assertIn("file missing on disk", output)
        self.assertEqual(
            read(self.root, gen.MANIFEST_REL),
            manifest_before,
            "the source digest was refreshed without full propagation",
        )
        # The source edit did reach the targets that could be written, and the
        # stale manifest keeps the next check red.
        self.assertNotEqual(intact_block_before, block_text(self.root, intact.path))
        self.assertEqual(run_generator(self.root, check=True)[0], 1)

        _copy_into(self.root, broken.path)
        self.assertEqual(run_generator(self.root, check=False)[0], 0)
        self.assertNotEqual(read(self.root, gen.MANIFEST_REL), manifest_before)
        self.assertEqual(run_generator(self.root, check=True)[0], 0)

    def test_digest_is_not_refreshed_when_a_written_block_is_uncovered(self):
        manifest_before = read(self.root, gen.MANIFEST_REL)
        registry = json.loads(read(self.root, gen.REGISTRY_REL))
        registry["nodes"][gen.AXIOM_NODE_ID]["note"] = "touched for this test"
        write(self.root, gen.REGISTRY_REL, json.dumps(registry, indent=1) + "\n")

        with patch.object(
            gen, "missing_roster_coverage",
            lambda src, text: [
                (src.primitives[0].node_id, src.primitives[0].boundary)
            ] if gen.BEGIN_MARKER in text else [],
        ):
            code, output = run_generator(self.root, check=False)
        self.assertEqual(code, 1, output)
        self.assertIn("refusing to refresh", output)
        self.assertEqual(read(self.root, gen.MANIFEST_REL), manifest_before)


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
    def test_every_target_renders_the_primitive_roster(self):
        for target in gen.TARGETS:
            self.assertIn(gen.SPAN_PRIMITIVES, target.spans, target.path)

    def test_blocks_wrap_within_the_declared_width(self):
        src = gen.load_source(self.root)
        for key, lines in gen.render_all(src).items():
            for line in lines:
                if len(line) <= gen.WRAP_WIDTH:
                    continue
                # Only an unbreakable single token (a long registered path) may
                # overflow; extraction never re-breaks a source token.
                self.assertEqual(len(line.split()), 1, f"{key}: {line!r}")

    def test_no_generated_line_has_trailing_whitespace(self):
        src = gen.load_source(self.root)
        for key, lines in gen.render_all(src).items():
            for line in lines:
                self.assertEqual(line, line.rstrip(), f"{key}: {line!r}")

    def test_extracted_relative_links_are_flattened(self):
        """A source link target would be a broken link in the consuming file."""
        for target in gen.TARGETS:
            body = block_text(self.root, target.path)
            self.assertNotIn("](", body, target.path)

    def test_manifest_records_every_source_target_and_extracted_section(self):
        src = gen.load_source(self.root)
        manifest = gen.build_manifest(src, gen.render_all(src))
        self.assertEqual(set(manifest["targets"]), {t.path for t in gen.TARGETS})
        self.assertIn(self.axioms_rel, manifest["sources"])
        self.assertIn(gen.REGISTRY_REL, manifest["sources"])
        self.assertIn(
            gen.QUALIFICATION_SECTION, manifest["extracted_sections"][self.axioms_rel]
        )
        for prim in src.primitives:
            self.assertIn(prim.path, manifest["sources"])
            self.assertEqual(
                sorted(manifest["extracted_sections"][prim.path]),
                sorted([gen.PRIMITIVE_GRANT_SECTION, gen.PRIMITIVE_BOUNDARY_SECTION]),
            )


class TextMechanicsTest(unittest.TestCase):
    def test_hand_wrapped_compound_words_are_rejoined(self):
        self.assertEqual(
            gen.join_source_lines(["explicit approved-", "primitive registration"]),
            "explicit approved-primitive registration",
        )
        self.assertEqual(
            gen.join_source_lines(["denotes its support --", "on finite menus"]),
            "denotes its support -- on finite menus",
        )
        self.assertEqual(
            gen.join_source_lines(["a rule", "Covariant under"]),
            "a rule Covariant under",
        )

    def test_html_comments_are_not_visible_text(self):
        self.assertEqual(
            gen.visible_text("alpha <!-- beta\ngamma --> delta"), "alpha delta"
        )

    def test_links_are_flattened_without_touching_code_spans(self):
        self.assertEqual(
            gen.delink("the [four named axioms](MINIMAL_AXIOMS_2026-06-29.md): x"),
            "the four named axioms: x",
        )
        self.assertEqual(gen.delink("`I(empty)=0`"), "`I(empty)=0`")


if __name__ == "__main__":
    unittest.main()
