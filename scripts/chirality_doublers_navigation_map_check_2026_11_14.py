#!/usr/bin/env python3
"""Checks the statements that the chirality-doublers navigation map makes.

docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a
navigation map with no science of its own. What it does state is checkable:
that each "Carried notes" section quotes its carried note's current
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
MAP = "docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/A_DOMAIN_WALL_TICK_WITH_THE_LAYER_DIRECTION_AS_SPACE_PUTS_ONE_WEYL_CONE_ON_EACH_WALL_BUT_THE_CIRCUIT_FORCES_THE_MIRROR_ONTO_THE_FAR_WALL_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/GRABOWSKA_KAPLAN_FAR_LAYERS_PASS_THE_NIELSEN_NINOMIYA_COUNT_BUT_INDUCE_A_GAUGE_INVARIANT_CUTOFF_SCALE_PHOTON_MASS_ABOVE_THE_SMOOTHING_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/OCTREE_LADDER_OF_CUBE_TICKS_GIVES_ONE_FINE_CHIRALITY_ONLY_BY_A_SWINDLE_WITH_UNBOUNDED_RANGE_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_COMPOSITE_TWIST_WALK_IS_A_FIVE_LAYER_CUBE_LOCAL_CIRCUIT_AND_FREEZING_ONE_COPY_LEAVES_ONE_L_AND_ONE_R_PER_NODE_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_COMPOSITE_TWO_CELL_LIGHT_LABEL_MAKES_THE_CORNER_STABILIZERS_REDUCIBLE_BUT_THE_LIGHT_FLOQUET_WINDING_FORCES_THE_MIRROR_TO_CARRY_THE_OPPOSITE_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_FAMILY_CLASS_TICKS_FORCED_PI_SECTOR_IS_A_LIGHT_CHARGED_INVERTED_COPY_WHOSE_DOUBLER_MAP_CANCELS_ALL_VACUUM_POLARIZATION_SO_IT_NEEDS_REPAIR_WHILE_ITS_ANOMALIES_STAY_SAFE_BOUNDED_THEOREM_NOTE_2026-10-24.md",
    "docs/THE_FAMILY_CLASS_WINDING_FORCES_BULK_PI_STATES_BUT_A_SLAB_CAN_PUT_ALL_ITS_PI_FLOW_ON_THE_FAR_WALL_WHILE_NO_TICK_ALTERNATING_TERM_SEPARATES_PI_PI_FROM_ZERO_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md",
    "docs/THE_FORCED_FAR_WALL_TERM_HAS_A_UNIQUE_GAPPED_THREE_SITE_CELL_STATE_BUT_A_STRONG_COUPLING_CELL_ONLY_MOVES_THE_MIRROR_AND_THE_ONE_ORBITAL_SIXTEEN_SITE_HAS_ONLY_TWO_SPIN10_SINGLETS_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_ONE_FAMILY_U1_ANOMALY_FOUR_FIELD_COEFFICIENT_IN_ADMISSIBLE_BACKGROUNDS_AT_WILSON_MASS_ONE_DOES_NOT_VANISH_LIKE_P_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-25.md",
    "docs/THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU3_X_SU2_X_U1_BACKGROUNDS_CANCELS_THE_ONE_GENERATION_GAUGE_ANOMALY_LOCALLY_AND_IN_EVERY_MEASURED_INDEX_INCLUDING_A_Z6_TWISTED_FLUX_BUT_ANOMALOUS_SUBSETS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_OVERLAP_OF_THE_CUBE_WALK_EUCLIDEAN_KERNEL_GIVES_EXACT_GINSPARG_WILSON_CHIRALITY_WITHOUT_DOUBLERS_BUT_ITS_CHIRAL_PROJECTOR_IS_NOT_A_WALK_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_ZOOMED_FILTERED_MIRROR_TERM_KEEPS_THE_CHIRAL_Z4_AND_THE_16_WEYL_TOY_IS_ANOMALY_FREE_WITH_AN_UNSETTLED_K_GAP_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md",
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
    """Yield (heading, body) for each '### #' section of the 'Carried notes' part."""
    part = text.split("\n## Carried notes\n", 1)[1].split("\n## ", 1)[0]
    chunks = re.split(r"^### ", part, flags=re.M)[1:]
    for chunk in chunks:
        head, _, body = chunk.partition("\n")
        yield head.strip(), body


def quoted_scope(body: str) -> str | None:
    lines = [l[2:] if l.startswith("> ") else l[1:] for l in body.splitlines() if l.startswith(">")]
    return " ".join(" ".join(lines).split()) if lines else None


def carried_note(body: str) -> str | None:
    m = re.search(r"\*\*Carried note\.\*\* \[[^\]]+\]\(([^)]+\.md)\)", body)
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
    print("Navigation map check: chirality-doublers carried notes")
    print("=" * 78)

    results = compare(text)
    notes = [r[1] for r in results]
    check("the map has 21 'Carried notes' sections, each naming one carried note",
          len(results) == 21 and all(notes), len(results))
    check("no carried note appears in two sections", len(set(notes)) == len(notes))
    bad = [h for h, _, ok in results if not ok]
    check("each section quotes its carried note's current claim_scope verbatim", not bad,
          f"{21 - len(bad)} of {len(results)} match" + (f"; mismatched: {bad[:3]}" if bad else ""))

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
