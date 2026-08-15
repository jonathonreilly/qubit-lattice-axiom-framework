#!/usr/bin/env python3
"""List the four two-site seeds from which f_L1 does not fill.

Recomputes every unordered pair of the twelve two-cube sites with
off-patch occupancy 0. Coverage is the number of those seeds from
which f_L1 fills. The four misses are listed in lexicographic order
with halt lock-count and lock-history; they are displayed, not
adopted, and are not written into Admissibility. The four
opposite-corner seeds of the f_min/f_L1 split are fills, not misses.
f_L1 is the some-axis-unbalanced (n != 0) map, not Hamming weight.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_L1_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_L1_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
OPP_CORNER_SEEDS: tuple[frozenset[Point], ...] = (
    frozenset(((0, 0, 0), (2, 1, 1))),
    frozenset(((0, 0, 1), (2, 1, 0))),
    frozenset(((0, 1, 0), (2, 0, 1))),
    frozenset(((0, 1, 1), (2, 0, 0))),
)
L1_OPP_HISTORY = (2, 8, 12)
L1_MISS_HISTORY = (2, 6, 8)
L1_MISS_HALT = 8


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Point, locked: frozenset[Point]) -> int:
    """On-patch occupancy is the lock bit; off-patch occupancy is 0."""
    if site not in SITE_SET:
        return 0
    return 1 if site in locked else 0


def axis_type(site: Point, locked: frozenset[Point]) -> tuple[int, int, int]:
    """Return (n_unbalanced, n_both, n_empty) for the three cubic axes."""
    n_unbalanced = n_both = n_empty = 0
    for axis in AXES:
        plus = occupancy(add(site, axis), locked)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), locked)
        if plus == minus == 0:
            n_empty += 1
        elif plus == minus == 1:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def fire_l1(counts: tuple[int, int, int]) -> bool:
    """f_L1: some axis is unbalanced (n != 0). Not Hamming weight."""
    n_unbalanced, _n_both, _n_empty = counts
    return n_unbalanced != 0


def run(seed: frozenset[Point]) -> tuple[tuple[int, ...], bool]:
    locked = frozenset(seed)
    history = [len(locked)]
    for _tick in range(len(SITES)):
        ready = [
            site
            for site in SITES
            if site not in locked and fire_l1(axis_type(site, locked))
        ]
        if not ready:
            break
        locked = locked.union(ready)
        history.append(len(locked))
    return (tuple(history), len(locked) == len(SITES))


def seed_key(seed: frozenset[Point]) -> tuple[Point, ...]:
    return tuple(sorted(seed))


def seed_display(seed: frozenset[Point]) -> str:
    left, right = seed_key(seed)
    return f"{{({left[0]},{left[1]},{left[2]}),({right[0]},{right[1]},{right[2]})}}"


def census() -> dict[str, object]:
    n_fill = 0
    misses: list[frozenset[Point]] = []
    histories: dict[tuple[Point, ...], tuple[tuple[int, ...], int, bool]] = {}
    pairs = tuple(frozenset(pair) for pair in combinations(SITES, 2))
    for seed in pairs:
        hist, fill = run(seed)
        histories[seed_key(seed)] = (hist, hist[-1], fill)
        if fill:
            n_fill += 1
        else:
            misses.append(seed)
    misses_lex = tuple(sorted(misses, key=seed_key))
    return {
        "n_pairs": len(pairs),
        "n_fill": n_fill,
        "n_miss": len(misses),
        "misses_lex": misses_lex,
        "histories": histories,
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: exhaustive two-site lock-step census under f_L1; the four miss seeds are listed in lex order")
    print("negative_scope: the four miss seeds are displayed; no seed is adopted or written into Admissibility")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_L1_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_L1_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalized_axiom and admissibility_sentence in note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    checks.check(
        "two-cube-cardinality",
        "the two-cube is exactly the twelve sites {0,1,2} x {0,1} x {0,1}",
        len(SITES) == 12 and len(SITE_SET) == 12 and SITES[0] == (0, 0, 0) and SITES[-1] == (2, 1, 1),
    )
    checks.check("pair-count", "there are C(12,2)=66 unordered two-site seeds", len(tuple(combinations(SITES, 2))) == 66)

    counts = census()
    n_fill = int(counts["n_fill"])
    n_miss = int(counts["n_miss"])
    misses_lex = counts["misses_lex"]
    histories = counts["histories"]
    assert isinstance(misses_lex, tuple)
    assert isinstance(histories, dict)
    miss_displays = [seed_display(seed) for seed in misses_lex]
    opp_displays = [seed_display(seed) for seed in OPP_CORNER_SEEDS]
    print(f"census: cov(f_L1)={n_fill} n_miss={n_miss} n_pairs={counts['n_pairs']}")
    print("four_miss_seeds_lex: " + ", ".join(miss_displays))
    for seed in misses_lex:
        hist, halt, fill = histories[seed_key(seed)]
        print(f"  {seed_display(seed)} hist_L1={hist} halt={halt} fill={fill}")
    print("opp_corner_seeds_are_fills:")
    for seed in OPP_CORNER_SEEDS:
        hist, halt, fill = histories[seed_key(seed)]
        print(f"  {seed_display(seed)} hist_L1={hist} halt={halt} fill={fill}")

    checks.check(
        "theorem-1-cov-sixty-two",
        "cov(f_L1)=62 among the 66 two-site seeds",
        counts["n_pairs"] == 66 and n_fill == 62 and n_miss == 4 and n_fill + n_miss == 66,
        residual=(n_fill, n_miss),
    )

    opp_ok = all(
        histories[seed_key(seed)] == (L1_OPP_HISTORY, 12, True)
        for seed in OPP_CORNER_SEEDS
    )
    disjoint = all(seed not in misses_lex for seed in OPP_CORNER_SEEDS)
    checks.check(
        "theorem-1-opp-corner-fills",
        "the four opposite-corner seeds of #6423 fill under f_L1 and are not misses",
        len(OPP_CORNER_SEEDS) == 4
        and opp_ok
        and disjoint
        and all(display in note.replace(" ", "") for display in opp_displays),
        residual=[(seed_display(seed), histories[seed_key(seed)]) for seed in OPP_CORNER_SEEDS],
    )

    keys = [seed_key(seed) for seed in misses_lex]
    checks.check(
        "theorem-2-lex-list",
        "the four miss seeds are listed in lexicographic site-pair order",
        len(misses_lex) == 4
        and keys == sorted(keys)
        and all(len(key) == 2 and key == tuple(sorted(key)) for key in keys),
        residual=keys,
    )

    history_ok = all(
        histories[seed_key(seed)] == (L1_MISS_HISTORY, L1_MISS_HALT, False)
        for seed in misses_lex
    )
    checks.check(
        "theorem-2-histories",
        "each miss seed has halt lock-count 8 and history (2, 6, 8)",
        history_ok and len(misses_lex) == 4,
        residual=[(seed_display(seed), histories[seed_key(seed)]) for seed in misses_lex],
    )

    note_has_each = all(display in note.replace(" ", "") for display in miss_displays)
    order_ok = True
    cursor = 0
    compact_note = note.replace(" ", "")
    for display in miss_displays:
        found = compact_note.find(display, cursor)
        if found < 0:
            order_ok = False
            break
        cursor = found + len(display)
    checks.check(
        "theorem-3-display",
        "the note displays the four computed miss seeds in lex order and does not adopt a seed",
        note_has_each
        and order_ok
        and "displayed, not adopted" in normalized_note.lower()
        and "do not adopt" in normalized_note.lower()
        and f"cov(f_L1) = {n_fill}" in note
        and "(2, 6, 8)" in note
        and "halt lock-count 8" in note,
        residual=miss_displays,
    )

    locked_opp = frozenset(((0, 0, 0), (2, 0, 0)))
    opp2 = axis_type((1, 0, 0), locked_opp)
    hamming_opp = sum(
        occupancy(add((1, 0, 0), shift), locked_opp)
        for shift in AXES + tuple((-a, -b, -c) for a, b, c in AXES)
    )
    checks.check(
        "identity-l1-not-hamming",
        "opp2 has Hamming weight 2 but n_unbalanced=0, so f_L1 does not fire",
        opp2 == (0, 1, 2) and hamming_opp == 2 and not fire_l1(opp2),
    )

    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases",
        "the note and runner avoid the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "no-admissibility-selector",
        "the note does not write a seed selector into Admissibility",
        "not written into Admissibility" in normalized_note
        and "Do not write" in note
        and "Do not adopt a seed" in note,
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the four miss-seed display",
        "The four two-site seeds on the two-cube from which f_L1 does not fill are listed." in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "not-leftover-6422",
        "the four misses are a new object, not leftover character of the opposite-corner split four",
        "Not leftover-character of #6422" in note
        and "opposite-corner" in note
        and "L1 fills" in note
        and "f_min does not" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "some axis is unbalanced" in normalized_note
        and "n_unbalanced" in note
        and "not Hamming" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
