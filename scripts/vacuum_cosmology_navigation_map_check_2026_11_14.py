#!/usr/bin/env python3
"""Checks the statements that the vacuum-cosmology navigation map makes.

docs/VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a
navigation map with no science of its own. What it does state is checkable:
that each "Carried notes" section quotes its carried note's current
claim_scope verbatim and names that note's own primary runner, that the map
covers each carried note once, that its carried sections and its logged table
together list 28 distinct source PRs (13 carried, 15 logged), and that every
repository link in the map resolves. This runner checks those statements.
Controls alter one quotation and one runner link and must be rejected.
Adapted on 2026-11-14 from the gauge-matter-registers map check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60

ROOT = Path(__file__).resolve().parents[1]
MAP = "docs/VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/AN_UNSPLIT_BLOCK_CANNOT_INFLATE_SO_THE_FOLD_PLATEAU_NEEDS_SPLITS_THAT_CARRY_ITS_ORDER_AND_DEPHASED_SPLIT_PHASES_TO_SEED_PERTURBATIONS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/BORN_SPLIT_TIMES_ARE_WHITE_INHERITED_OFFSETS_AND_THE_PASSING_LEAVES_NO_REMAINDER_SO_NO_LAW_SEEDS_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/CURVATURE_SQUARED_INFLATION_MISSES_THE_ACT_TILT_AND_NO_RULE_LIFTS_IT_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/FIRST_SLAB_FIXES_LAMBDA_ONLY_AT_THE_PLANCK_SCALE_AND_A_RECORD_COUNT_MULTIPLIER_GIVES_A_WRONG_SIGN_OR_A_DRIFTING_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/FLOQUET_SEA_VACUUM_SOURCE_IS_ZERO_PLANCKIAN_OR_MASS_DOMINATED_NOT_MEASURED_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/NO_STRUCTURE_OF_THE_UPDATE_PROTECTS_A_DARK_SPECIES_BECAUSE_THE_MIRROR_NUMBER_IS_SHARED_AT_EVERY_MOMENTUM_THE_BLOCK_PERIOD_BLOCKS_NO_COPY_DECAY_AND_THE_WINDOW_FLOOR_HOLDS_NO_ATOM_OR_REMNANT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/RECORDS_ON_CHANGE_ARE_FROZEN_IN_THE_HALF_FILLED_SEA_SO_A_RECORD_COUNT_LAMBDA_HAS_NO_POISSON_SOURCE_AND_EVERPRESENT_HISTORIES_FAIL_THE_EARLY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_GAPPED_MIRROR_KEEPS_ONLY_A_NUMBER_SHARED_WITH_LIGHT_MATTER_AND_ITS_LIGHTEST_STATE_IS_CHARGED_SO_IT_GIVES_NO_DARK_MATTER_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/THE_SPLIT_TIME_CASCADE_IS_SELF_SIMILAR_SO_ITS_DELTA_N_SPECTRUM_IS_FLAT_AND_THE_TRIGGER_READS_NO_LINEAR_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/TIME_REVERSAL_FREEZES_HALF_FILLED_SEA_RECORDS_AND_RECORD_COUNT_LAMBDA_NEEDS_POISSON_INPUT_BOUNDED_THEOREM_NOTE_2026-10-21.md",
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


def frontmatter_field(text: str, key: str) -> str | None:
    """A one-key YAML scalar from the front matter; a quoted scalar may continue on indented lines."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    lines = m.group(1).split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(key + ":")]
    if len(starts) != 1:
        return None
    i = starts[0]
    raw = lines[i][len(key) + 1:].strip()
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
    """Yield (heading, body) for each '### ' section of the 'Carried notes' part."""
    part = text.split("\n## Carried notes\n", 1)[1].split("\n## ", 1)[0]
    for chunk in re.split(r"^### ", part, flags=re.M)[1:]:
        head, _, body = chunk.partition("\n")
        yield head.strip(), body


def quoted_scope(body: str) -> str | None:
    lines = [l[2:] if l.startswith("> ") else l[1:] for l in body.splitlines() if l.startswith(">")]
    return " ".join(" ".join(lines).split()) if lines else None


def carried_note(body: str) -> str | None:
    m = re.search(r"^- Note: \[[^\]]+\]\(([^)]+\.md)\)", body, re.M)
    return m.group(1) if m else None


def carried_runner(body: str) -> str | None:
    m = re.search(r"Runner: \[`[^`]+`\]\(\.\./(scripts/[^)]+\.py)\)", body)
    return m.group(1) if m else None


def compare(map_text: str):
    results = []
    for head, body in sections(map_text):
        rel = carried_note(body)
        note = ROOT / "docs" / rel if rel else None
        text = note.read_text(encoding="utf-8") if note and note.is_file() else ""
        scope, runner = frontmatter_field(text, "claim_scope"), frontmatter_field(text, "runner")
        quote, link = quoted_scope(body), carried_runner(body)
        results.append((head, rel, quote is not None and scope is not None and quote == scope,
                        link is not None and runner is not None and link == runner and (ROOT / link).is_file()))
    return results


def source_prs(map_text: str):
    carried = [re.match(r"#(\d+):", h).group(1) if re.match(r"#(\d+):", h) else None for h, _ in sections(map_text)]
    part = map_text.split("\n## Logged notes", 1)[1].split("\n## ", 1)[0]
    logged = re.findall(r"^\| #(\d+) \|", part, flags=re.M)
    return carried, logged


def main() -> int:
    text = (ROOT / MAP).read_text(encoding="utf-8")
    print("=" * 78)
    print("Navigation map check: vacuum-cosmology carried and logged notes")
    print("=" * 78)

    results = compare(text)
    notes = [r[1] for r in results]
    check("the map has 13 'Carried notes' sections, each naming one carried note",
          len(results) == 13 and all(notes), len(results))
    check("no carried note appears in two sections", len(set(notes)) == len(notes))
    bad = [h for h, _, ok, _ in results if not ok]
    check("each section quotes its carried note's current claim_scope verbatim", not bad,
          f"{len(results) - len(bad)} of {len(results)} match" + (f"; mismatched: {bad[:3]}" if bad else ""))
    badr = [h for h, _, _, ok in results if not ok]
    check("each section's runner link is its carried note's own frontmatter runner, and the file exists", not badr,
          f"{len(results) - len(badr)} of {len(results)} match" + (f"; mismatched: {badr[:3]}" if badr else ""))

    carried, logged = source_prs(text)
    allpr = carried + logged
    check("13 carried and 15 logged source PRs, 28 distinct, none both carried and logged",
          len(carried) == 13 and None not in carried and len(logged) == 15 and len(set(allpr)) == 28,
          f"carried {len(carried)}, logged {len(logged)}, distinct {len(set(allpr))}")

    links = re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text)
    local = [l for l in links if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", l)]
    missing = sorted({l for l in local if not (ROOT / "docs" / l).resolve().exists()})
    check("every repository link in the map resolves", not missing and len(local) > 0,
          f"{len(local)} links" + (f"; missing: {missing[:3]}" if missing else ""))

    first = next(sections(text))[1]
    quote = quoted_scope(first)
    words = quote.split() if quote else []
    altered = text.replace(" ".join(words[-3:]), " ".join(words[-3:-1]), 1) if len(words) > 3 else text
    check("control rejects mutant: a quotation with its last word dropped still matches",
          not all(ok for _, _, ok, _ in compare(altered)))
    secs = list(sections(text))
    r0, r1 = carried_runner(secs[0][1]), carried_runner(secs[1][1])
    swapped = text.replace(f"(../{r0})", f"(../{r1})", 1) if r0 and r1 else text
    check("control rejects mutant: the first section's runner link pointed at the second note's runner",
          not all(ok for _, _, _, ok in compare(swapped)))

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Scope: the map's quotations, runner links, coverage, PR counts and links. The carried notes' science is checked by their own runners.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
