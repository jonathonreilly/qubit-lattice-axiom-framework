#!/usr/bin/env python3
"""List the four two-site seeds that split f_min from f_L1.

Recomputes every unordered pair of the twelve two-cube sites with
off-patch occupancy 0. A split is a different fill bit or a different
lock-count history. The four seeds are listed in lexicographic order;
they are displayed, not adopted, and are not written into Admissibility.
f_L1 is the some-axis-unbalanced (n != 0) map, not Hamming weight.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIN_L1_FOUR_SPLIT_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_L1_FOUR_SPLIT_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
NAMED_SPLITTER = frozenset(((0, 0, 0), (2, 1, 1)))
L1_SPLIT_HISTORY = (2, 8, 12)
MIN_SPLIT_HISTORY = (2, 8, 10)


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


def fire_min(counts: tuple[int, int, int]) -> bool:
    """f_min: nonempty and n_both = 0."""
    n_unbalanced, n_both, _n_empty = counts
    return n_both == 0 and n_unbalanced != 0


def run(seed: frozenset[Point], fire) -> tuple[tuple[int, ...], bool]:
    locked = frozenset(seed)
    history = [len(locked)]
    for _tick in range(len(SITES)):
        ready = [
            site
            for site in SITES
            if site not in locked and fire(axis_type(site, locked))
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
    n_split = n_fill_l1 = n_fill_min = 0
    splits: list[frozenset[Point]] = []
    histories: dict[tuple[Point, ...], tuple[tuple[int, ...], bool, tuple[int, ...], bool]] = {}
    pairs = tuple(frozenset(pair) for pair in combinations(SITES, 2))
    for seed in pairs:
        hist_l1, fill_l1 = run(seed, fire_l1)
        hist_min, fill_min = run(seed, fire_min)
        n_fill_l1 += int(fill_l1)
        n_fill_min += int(fill_min)
        if (fill_l1 != fill_min) or (hist_l1 != hist_min):
            n_split += 1
            splits.append(seed)
            histories[seed_key(seed)] = (hist_l1, fill_l1, hist_min, fill_min)
    splits_lex = tuple(sorted(splits, key=seed_key))
    return {
        "n_pairs": len(pairs),
        "n_split": n_split,
        "n_fill_l1": n_fill_l1,
        "n_fill_min": n_fill_min,
        "splits_lex": splits_lex,
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
    print("construction: exhaustive two-site lock-step census; the four split seeds are listed in lex order")
    print("negative_scope: the four seeds are displayed; no selector is adopted or written into Admissibility")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_L1_FOUR_SPLIT_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_MIN_L1_FOUR_SPLIT_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
    n_split = int(counts["n_split"])
    n_fill_l1 = int(counts["n_fill_l1"])
    n_fill_min = int(counts["n_fill_min"])
    splits_lex = counts["splits_lex"]
    histories = counts["histories"]
    assert isinstance(splits_lex, tuple)
    assert isinstance(histories, dict)
    displays = [seed_display(seed) for seed in splits_lex]
    print(
        "census: "
        f"N_split={n_split} N_fill_L1={n_fill_l1} N_fill_min={n_fill_min}"
    )
    print("four_split_seeds_lex: " + ", ".join(displays))
    for seed in splits_lex:
        hist_l1, fill_l1, hist_min, fill_min = histories[seed_key(seed)]
        print(
            f"  {seed_display(seed)} "
            f"hist_L1={hist_l1} fill_L1={fill_l1} "
            f"hist_min={hist_min} fill_min={fill_min}"
        )

    checks.check(
        "theorem-1-census",
        "N_split=4, N_fill_L1=62, and N_fill_min=58 on the 66 two-site seeds",
        counts["n_pairs"] == 66 and n_split == 4 and n_fill_l1 == 62 and n_fill_min == 58,
        residual=(n_split, n_fill_l1, n_fill_min),
    )

    hist_l1_star, fill_l1_star = run(NAMED_SPLITTER, fire_l1)
    hist_min_star, fill_min_star = run(NAMED_SPLITTER, fire_min)
    splits_star = (fill_l1_star != fill_min_star) or (hist_l1_star != hist_min_star)
    checks.check(
        "theorem-1-named-splitter",
        "the seed {(0,0,0),(2,1,1)} is one split",
        splits_star
        and fill_l1_star
        and not fill_min_star
        and hist_l1_star == L1_SPLIT_HISTORY
        and hist_min_star == MIN_SPLIT_HISTORY
        and NAMED_SPLITTER in splits_lex,
        residual=(hist_l1_star, hist_min_star, fill_l1_star, fill_min_star),
    )

    keys = [seed_key(seed) for seed in splits_lex]
    checks.check(
        "theorem-2-lex-list",
        "the four seeds are listed in lexicographic site-pair order",
        len(splits_lex) == 4
        and keys == sorted(keys)
        and all(len(key) == 2 and key == tuple(sorted(key)) for key in keys),
        residual=keys,
    )

    history_ok = all(
        histories[seed_key(seed)] == (L1_SPLIT_HISTORY, True, MIN_SPLIT_HISTORY, False)
        for seed in splits_lex
    )
    checks.check(
        "theorem-2-histories",
        "each listed seed has f_L1 history (2, 8, 12) and f_min unfilled (2, 8, 10)",
        history_ok and len(splits_lex) == 4,
        residual=[(seed_display(seed), histories[seed_key(seed)]) for seed in splits_lex],
    )

    note_has_each = all(display in note.replace(" ", "") for display in displays)
    order_ok = True
    cursor = 0
    compact_note = note.replace(" ", "")
    for display in displays:
        found = compact_note.find(display, cursor)
        if found < 0:
            order_ok = False
            break
        cursor = found + len(display)
    checks.check(
        "theorem-3-display",
        "the note displays the four computed seeds in lex order and does not adopt a selector",
        note_has_each
        and order_ok
        and "displayed, not adopted" in normalized_note.lower()
        and "do not adopt" in normalized_note.lower()
        and f"N_split = {n_split}" in note
        and f"N_fill_L1 = {n_fill_l1}" in note
        and f"N_fill_min = {n_fill_min}" in note,
        residual=displays,
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
        opp2 == (0, 1, 2) and hamming_opp == 2 and not fire_l1(opp2) and not fire_min(opp2),
    )
    locked_mixed = frozenset(((0, 0, 0), (2, 0, 0), (1, 1, 0)))
    mixed3 = axis_type((1, 0, 0), locked_mixed)
    locked_wt1 = frozenset(((0, 0, 0),))
    wt1 = axis_type((1, 0, 0), locked_wt1)
    checks.check(
        "identity-min-nboth-zero",
        "f_min fires on nonempty n_both=0 and refuses mixed3",
        wt1 == (1, 0, 2)
        and mixed3 == (1, 1, 1)
        and fire_min(wt1)
        and fire_l1(wt1)
        and not fire_min(mixed3)
        and fire_l1(mixed3),
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
        and "selector" in normalized_note
        and "Do not write" in note,
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the four-seed display",
        "The four two-site seeds on the two-cube that distinguish f_min from f_L1 are listed." in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "not-leftover-count",
        "the claim is the four-seed set, not leftover character of the count-only census",
        "Not leftover-character of #6422" in note and "that only counted" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
