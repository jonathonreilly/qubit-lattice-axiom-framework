#!/usr/bin/env python3
"""Checks the statements that the gauge-matter-registers navigation map makes.

docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a
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
MAP = "docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/A_SITE_QUBIT_ICE_PHOTON_MAKES_MARGOLUS_FERMIONS_NEUTRAL_DIPOLES_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/BLOCK_COVARIANCE_GIVES_ABELIAN_OR_COPY_U2_AND_NO_REGISTER_SELECTS_THE_GAUGE_GROUP_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/DEFINITE_STATIONARY_LINKS_GIVE_CLASSICAL_COULOMB_COLOUR_FLAT_VACUUM_ONE_BODY_MATTER_AND_UNDECAYING_LEVELS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/FACE_REGISTER_LOOPS_AROUND_BLOCK_EDGES_ARE_GAUGE_INVARIANT_COMPLETE_AND_REACH_MAXWELL_AND_YANG_MILLS_AT_LIGHT_SPEED_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/FIVE_MODE_CONES_CARRY_THE_SPIN10_VECTOR_AND_SEPARATED_SIXTEEN_CONES_EVADE_THE_COMPOSITE_PARTNER_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/LINK_REGISTERS_BUILT_FROM_RISHON_FERMION_MODE_SITES_CARRY_EXACT_U1_AND_SU3_GAUSS_LAWS_AND_SIT_COVARIANTLY_FROM_ZOOM_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/LINK_REGISTER_SPLIT_TRANSPORT_AND_RESPONSE_GIVE_A_COVARIANT_LEVEL_MATCHED_ZOOM_MAP_BORN_EXPONENTIAL_DECAY_AND_THE_MAXWELL_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/QUBIT_CELL_COMPLEX_EMERGENT_GAUGE_FIELDS_SELECT_NO_MATTER_MULTIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/RUNG_ONE_CELL_REGISTER_CARRIES_THE_ONE_GENERATION_MULTIPLET_PATTERN_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md",
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
    lines = m.group(1).split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("claim_scope:")]
    if len(starts) != 1:
        return None
    i = starts[0]
    raw = lines[i][len("claim_scope:"):].strip()
    # a quoted scalar may continue on indented lines until its closing quote (YAML folds them with spaces)
    if raw[:1] in "\"'" and not (len(raw) >= 2 and raw.endswith(raw[0]) and not raw.endswith("\\" + raw[0])):
        q = raw[0]
        for cont in lines[i + 1:]:
            raw += " " + cont.strip()
            if cont.rstrip().endswith(q) and not cont.rstrip().endswith("\\" + q):
                break
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1].replace('\\"', '"') if raw[0] == '"' else raw[1:-1].replace("''", "'")
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


def main() -> int:
    text = (ROOT / MAP).read_text(encoding="utf-8")
    print("=" * 78)
    print("Navigation map check: gauge-matter-registers carried notes")
    print("=" * 78)

    results = compare(text)
    notes = [r[1] for r in results]
    check("the map has 12 'Carried notes' sections, each naming one carried note",
          len(results) == 12 and all(notes), len(results))
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
