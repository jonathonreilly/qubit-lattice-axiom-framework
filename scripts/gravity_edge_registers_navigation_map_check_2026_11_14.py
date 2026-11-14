#!/usr/bin/env python3
"""Checks the statements that the gravity-edge-registers navigation map makes.

docs/GRAVITY_EDGE_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a
navigation map with no science of its own. What it does state is checkable:
that each "Carried notes" section quotes its carried note's current
claim_scope verbatim, that the map covers each carried note exactly once, and
that every repository link in the map resolves. This runner checks those
statements. Controls alter one quotation, duplicate one section and break one
link; each must be rejected.

Adapted from the gauge-matter-registers map check (2026-11-14).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60

ROOT = Path(__file__).resolve().parents[1]
MAP = "docs/GRAVITY_EDGE_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/GRAVITY_EDGE_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_COVARIANT_MOMENTUM_TERM_KEEPS_THE_VOLUME_RATE_SHIFT_HYPERBOLIC_THROUGH_COLLAPSE_AND_STATIC_STARS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_CUBE_TICK_THAT_READS_ITS_OWN_LAPSE_AND_EDGES_IS_WEYL_BLIND_SO_ITS_VACUUM_ENTROPY_COUNTS_CUT_BONDS_NOT_PROPER_AREA_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_GLUED_SPLIT_OF_EDGE_REGISTERS_IS_UNITARY_AND_LOCAL_WHILE_ONE_SHOT_TRIGGERED_AND_SCHEDULED_SPLITS_FAIL_IN_A_ONE_DIMENSIONAL_TOY_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_NORMAL_FRAME_WAVE_SHIFT_FED_BY_THE_PER_TICK_VOLUME_RATE_GIVES_BLACK_HOLE_EXTERIORS_AN_ATTRACTING_HORIZON_REGULAR_SLICING_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_SITE_TICK_COUNT_AND_A_SITE_DENSITY_ANSWER_THE_HINGE_SUM_THROUGH_ONE_OPERATOR_SO_LIGHT_BENDS_TWICE_THE_NEWTONIAN_AMOUNT_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/EDGES_READING_THE_ACTUAL_CONFIGURATION_RADIATE_ON_EVERY_HOP_AND_EDGE_REGISTERS_KEEP_BORN_TRANSPORT_NO_SIGNALLING_AND_THE_VACUUM_STANDARD_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/GLUED_SPLIT_BESIDE_UNSPLIT_CUBES_NEEDS_A_ONE_SIDED_COLLAR_AND_FORCES_TWO_TO_ONE_BALANCE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/ISOTROPIC_COLLAPSE_ON_THE_CUBIC_FRUSTUM_CARRIER_HAS_A_STATIONARY_POINT_AT_EVERY_TICK_AND_NO_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/READ_LAPSE_MOMENTUM_CONSTRAINT_AND_MINIMAL_STRAIN_ARE_LINEARISED_GR_WITH_CAUSAL_CURVATURE_AND_AN_INSTANTANEOUS_SHIFT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/STATIC_REDSHIFT_ON_FIXED_STEP_EDGES_NEEDS_A_WIDER_EDGE_WINDOW_WHILE_SPLIT_HISTORY_CANNOT_HELP_AND_SKIPPED_HALF_TICKS_HEAT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_TICK_FRACTION_AND_PAIR_OFFSETS_ANSWERING_THE_HINGE_SUM_ARE_CONSTRAINTS_AND_LEAVE_EXACTLY_TWO_TENSOR_WAVES_ON_THE_EDGE_CONE_WITH_THE_QUADRUPOLE_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-10-23.md",
    "docs/THE_TIED_LAPSE_LEAVES_THE_SHIFT_FREE_A_GEOMETRY_ONLY_MOMENTUM_CONSTRAINT_EXCLUDES_MOVING_SOURCES_AND_MINIMAL_STRAIN_FIXES_THE_SHIFT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/WAVE_LAW_SHIFT_SOURCED_BY_THE_MOMENTUM_CONSTRAINT_KEEPS_NO_SLICE_BEND_MEMORY_AND_STAYS_CAUSAL_BOUNDED_THEOREM_NOTE_2026-10-22.md",
)
CARRIED = AUDIT_INPUT_PATHS[1:]
N_LOGGED = 26

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
    """The claim_scope value of a note's YAML front matter, whitespace-normalised.

    A quoted scalar may continue on indented lines until its closing quote; YAML folds
    those lines with single spaces, which the normalisation reproduces.
    """
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    lines = m.group(1).split("\n")
    starts = [i for i, line in enumerate(lines) if line.startswith("claim_scope:")]
    if len(starts) != 1:
        return None
    i = starts[0]
    raw = lines[i][len("claim_scope:"):].strip()
    if raw[:1] in "\"'" and not (len(raw) >= 2 and raw.endswith(raw[0]) and not raw.endswith("\\" + raw[0])):
        q = raw[0]
        for cont in lines[i + 1:]:
            raw += " " + cont.strip()
            if cont.rstrip().endswith(q) and not cont.rstrip().endswith("\\" + q):
                break
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1].replace('\\"', '"') if raw[0] == '"' else raw[1:-1].replace("''", "'")
    return " ".join(raw.split())


def frontmatter_type(text: str) -> str | None:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    t = re.search(r"^claim_type:\s*(\S+)\s*$", m.group(1), re.M)
    return t.group(1) if t else None


def sections(text: str):
    """Yield (heading, body) for each '### ' section of the 'Carried notes' part."""
    part = text.split("\n## Carried notes\n", 1)[1].split("\n## ", 1)[0]
    chunks = re.split(r"^### ", part, flags=re.M)[1:]
    for chunk in chunks:
        head, _, body = chunk.partition("\n")
        yield head.strip(), body


def quoted_scope(body: str) -> str | None:
    lines = [line[2:] if line.startswith("> ") else line[1:] for line in body.splitlines() if line.startswith(">")]
    return " ".join(" ".join(lines).split()) if lines else None


def carried_note(body: str) -> str | None:
    m = re.search(r"^- Note: \[[^\]]+\]\(([^)]+\.md)\)", body, re.M)
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


def coverage(results):
    notes = [r[1] for r in results]
    expected = sorted(Path(p).name for p in CARRIED)
    return notes, sorted(n for n in notes if n) == expected and len(set(notes)) == len(notes)


def links(text: str):
    found = re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text)
    local = [x for x in found if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", x)]
    missing = sorted({x for x in local if not (ROOT / "docs" / x).resolve().exists()})
    return local, missing


def logged_rows(text: str) -> int:
    part = text.split("\n## Logged notes", 1)[1].split("\n## ", 1)[0]
    return len([line for line in part.splitlines() if re.match(r"^\| #\d+ \|", line)])


def main() -> int:
    text = (ROOT / MAP).read_text(encoding="utf-8")
    print("=" * 78)
    print("Navigation map check: gravity-edge-registers carried notes")
    print("=" * 78)

    check("the map is typed meta (a navigation map, no science of its own)", frontmatter_type(text) == "meta", frontmatter_type(text))
    results = compare(text)
    notes, covered = coverage(results)
    check(f"the map has {len(CARRIED)} 'Carried notes' sections, each naming one carried note",
          len(results) == len(CARRIED) and all(notes), len(results))
    check("each carried note appears exactly once and no other note is named", covered)
    bad = [h for h, _, ok in results if not ok]
    check("each section quotes its carried note's current claim_scope verbatim", not bad,
          f"{len(results) - len(bad)} of {len(results)} match" + (f"; mismatched: {bad[:3]}" if bad else ""))

    local, missing = links(text)
    check("every repository link in the map resolves", not missing and len(local) > 0,
          f"{len(local)} links" + (f"; missing: {missing[:3]}" if missing else ""))
    check(f"the logged-notes table lists {N_LOGGED} source notes", logged_rows(text) == N_LOGGED, logged_rows(text))

    # controls: each perturbed map must be rejected by the same tests
    first = next(sections(text))[1]
    quote = quoted_scope(first)
    words = quote.split() if quote else []
    altered = text.replace(" ".join(words[-3:]), " ".join(words[-3:-1]), 1) if len(words) > 3 else text
    check("control rejects mutant: a quotation with its last word dropped", not all(ok for _, _, ok in compare(altered)))
    head0, body0 = next(sections(text))
    dup = text.replace("\n## Carried notes\n", "\n## Carried notes\n\n### " + head0 + "\n" + body0, 1)
    check("control rejects mutant: one carried section duplicated", not coverage(compare(dup))[1])
    first_link = local[0] if local else ""
    broken = text.replace("](" + first_link, "](MISSING_" + first_link, 1)
    check("control rejects mutant: one repository link broken", bool(links(broken)[1]))

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Scope: the map's type, quotations, coverage, links and logged-table size. The carried notes' science is checked by their own runners.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
