#!/usr/bin/env python3
"""Checks the statements that the families-flavour navigation map makes.

docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a
navigation map with no science of its own. What it does state is checkable:
that each "Carried results" section quotes its carried note's current
claim_scope verbatim, that the map covers each carried note once, and that
every repository link in the map resolves. This runner checks those
statements. A control alters one quotation and must be rejected.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60

ROOT = Path(__file__).resolve().parents[1]
MAP = "docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/ASYMMETRY_AS_MISALIGNMENT_OCTONION_ROUTE_FAILS_CELL_CODE_GROUP_IS_AGAMMAL_1_8_AND_SECTOR_RESIDUAL_ANTIUNITARIES_GIVE_TREE_THETA_ZERO_BUT_FAIL_CROSS_TALK_BOUNDED_THEOREM_NOTE_2026-10-26.md",
    "docs/A_TURN_KEPT_BY_THE_UPDATE_AND_BROKEN_BY_THE_VACUUM_GIVES_CP_AND_THETA_BAR_TOGETHER_UNLESS_A_NELSON_BARR_BLOCK_IS_SUPPLIED_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/NO_VACUUM_OF_FAMILY_BLIND_RULES_TESTED_GIVES_THREE_HIERARCHICAL_FAMILIES_WITH_A_T_ODD_PHASE_ADJOINT_VACUA_CANNOT_ENTER_MASSES_AND_QUARTIC_ALIGNMENT_IS_T_EVEN_BOUNDED_THEOREM_NOTE_2026-10-24.md",
    "docs/THE_CUBE_CELL_SLAB_WALL_HOLDS_AT_MOST_TWO_OPPOSITE_HANDED_COPIES_SO_FAMILIES_ARE_NOT_WALL_NODES_WHILE_THE_SUPPLIED_WILSON_KERNEL_GIVES_A_TURN_TRIPLET_ONLY_IN_AN_UNFORCED_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_CUBE_TASTES_ARE_TWO_DOUBLETS_AND_NO_SYMMETRY_PROTECTS_A_FAMILY_TRIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_FAMILY_CLASS_TICK_KEEPS_A_TIME_REVERSING_ANTIUNITARY_THAT_FIXES_EVERY_FAMILY_SO_IT_SUPPLIES_NO_QUARK_CP_PHASE_AND_KEEPS_THETA_BAR_AT_ZERO_OR_PI_BOUNDED_THEOREM_NOTE_2026-10-24.md",
    "docs/THE_FAMILY_COPY_FORM_FIXES_KOIDE_Q_IN_EVERY_SECTOR_AND_CAPS_THE_MASS_TOWER_AT_ONE_STEP_SO_THE_QUARKS_EXCLUDE_IT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_FAMILY_IMAGE_OF_THE_TWO_TILINGS_IS_S3_AND_INVERSION_CLOSED_ZOOM_CHARGES_HAVE_AT_MOST_TWO_SPURION_DISTANCES_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_LATTICE_THETA_DENSITY_IS_ODD_UNDER_THE_KEPT_ANTIUNITARY_AND_ZOOM_THREE_CHARACTERS_GIVE_THETA_BAR_ZERO_AT_RENORMALISABLE_ORDER_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_LIGHT_COPY_CARRIES_A_NONZERO_TURN_CHARGE_SO_A_SYMMETRICALLY_GAPPED_MIRROR_NEEDS_FAMILY_COUNT_ZERO_MOD_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_MINIMAL_TURN_NEUTRAL_FAR_WALL_TERM_FOR_THREE_FAMILIES_HAS_A_FREE_FAMILY_MATRIX_WHOSE_ONLY_RULE_BLIND_CHOICE_KEEPS_U3_SO_NO_FAMILY_LABEL_BOUNDED_THEOREM_NOTE_2026-10-24.md",
    "docs/THE_TWO_TILING_TICK_HAS_NO_CELL_LOCAL_FAMILY_SYMMETRY_AND_A_TURN_TRIPLET_FORCES_TURN_INVARIANT_MIXING_TO_BE_CP_BLIND_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/TRANSLATION_INVARIANT_TERMS_GIVE_FAMILY_DIAGONAL_MIXING_AND_A_KEPT_FAMILY_THREE_CYCLE_IS_EXCLUDED_BOUNDED_THEOREM_NOTE_2026-10-22.md",
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: object = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail != "" else ""))
    return ok


def frontmatter_scope(text: str) -> str | None:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = re.findall(r"^claim_scope:[ \t]*(.*)$", m.group(1), re.M)
    if len(fields) != 1:
        return None
    raw = fields[0].strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1].replace('\\"', '"')
    return " ".join(raw.split())


def sections(text: str):
    """Yield (heading, body) for each '### #' section of the 'Carried results' part."""
    part = text.split("\n## Carried results\n", 1)[1].split("\n## ", 1)[0]
    chunks = re.split(r"^### ", part, flags=re.M)[1:]
    for chunk in chunks:
        head, _, body = chunk.partition("\n")
        yield head.strip(), body


def quoted_scope(body: str) -> str | None:
    lines = [l[2:] if l.startswith("> ") else l[1:] for l in body.splitlines() if l.startswith(">")]
    return " ".join(" ".join(lines).split()) if lines else None


def carried_note(body: str) -> str | None:
    m = re.search(r"\*\*Note:\*\* \[`?[^\]]+?`?\]\(([^)]+\.md)\)", body)
    return m.group(1) if m else None


def compare(map_text: str):
    results = []
    for head, body in sections(map_text):
        rel = carried_note(body)
        quote = quoted_scope(body)
        note = ROOT / "docs" / rel if rel else None
        scope = frontmatter_scope(note.read_text(encoding="utf-8")) if note and note.is_file() else None
        results.append((head, rel, quote is not None and scope is not None and quote == scope))
    return results


def main() -> int:
    text = (ROOT / MAP).read_text(encoding="utf-8")
    print("=" * 78)
    print("Navigation map check: families-flavour carried results")
    print("=" * 78)

    results = compare(text)
    notes = [r[1] for r in results]
    check("the map has 13 'Carried results' sections, each naming one carried note",
          len(results) == 13 and all(notes), len(results))
    check("no carried note appears in two sections", len(set(notes)) == len(notes))
    bad = [h for h, _, ok in results if not ok]
    check("each section quotes its carried note's current claim_scope verbatim", not bad,
          f"{len(results) - len(bad)} of {len(results)} match" + (f"; mismatched: {bad[:3]}" if bad else ""))

    links = re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text)
    local = [l for l in links if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", l)]
    missing = sorted({l for l in local if not (ROOT / "docs" / l).resolve().exists()})
    check("every repository link in the map resolves", not missing and len(local) > 0,
          f"{len(local)} links" + (f"; missing: {missing[:3]}" if missing else ""))

    first = next(sections(text))[1]
    quote = quoted_scope(first)
    words = quote.split() if quote else []
    altered = text.replace(" ".join(words[-3:]), " ".join(words[-3:-1]), 1) if len(words) > 3 else text
    mutant_ok = all(ok for _, _, ok in compare(altered))
    check("control rejects mutant: a quotation with its last word dropped still matches", not mutant_ok)

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Scope: the map's quotations, coverage and links. The carried notes' science is checked by their own runners.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
