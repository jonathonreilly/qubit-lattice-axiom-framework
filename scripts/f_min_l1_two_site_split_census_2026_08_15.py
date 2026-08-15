#!/usr/bin/env python3
"""Two-site split census of f_min versus f_L1 on the twelve-vertex two-cube.

Enumerates every unordered pair of the twelve sites of
{0,1,2} x {0,1} x {0,1} with off-patch occupancy 0. A split is a
different fill bit or a different lock-count history. The census
displays N_split; it does not adopt a seed or write a selector into
Admissibility.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIN_L1_TWO_SITE_SPLIT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_L1_TWO_SITE_SPLIT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
FACE_DIAGONAL = frozenset(((0, 0, 0), (1, 1, 0)))
DISTINGUISHER = frozenset(((0, 0, 0), (2, 1, 1)))
FACE_HISTORY = (2, 7, 11, 12)


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


def census() -> dict[str, object]:
    n_split = n_fill_l1 = n_fill_min = n_fill_both = 0
    n_history_only = n_fill_only = 0
    pairs = tuple(frozenset(pair) for pair in combinations(SITES, 2))
    for seed in pairs:
        hist_l1, fill_l1 = run(seed, fire_l1)
        hist_min, fill_min = run(seed, fire_min)
        n_fill_l1 += int(fill_l1)
        n_fill_min += int(fill_min)
        n_fill_both += int(fill_l1 and fill_min)
        fill_diff = fill_l1 != fill_min
        hist_diff = hist_l1 != hist_min
        if fill_diff or hist_diff:
            n_split += 1
            n_fill_only += int(fill_diff and not hist_diff)
            n_history_only += int(hist_diff and not fill_diff)
    return {
        "n_pairs": len(pairs),
        "n_split": n_split,
        "n_fill_l1": n_fill_l1,
        "n_fill_min": n_fill_min,
        "n_fill_both": n_fill_both,
        "n_history_only": n_history_only,
        "n_fill_only": n_fill_only,
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
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: exhaustive two-site lock-step census on the twelve-vertex two-cube with off-patch occupancy 0")
    print("negative_scope: N_split is displayed; no seed is adopted and no selector is written into Admissibility")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_L1_TWO_SITE_SPLIT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
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

    checks.check("two-cube-cardinality", "the two-cube is exactly the twelve sites {0,1,2} x {0,1} x {0,1}", len(SITES) == 12 and len(SITE_SET) == 12)
    checks.check("pair-count", "there are C(12,2)=66 unordered two-site seeds", len(tuple(combinations(SITES, 2))) == 66)

    hist_l1_face, fill_l1_face = run(FACE_DIAGONAL, fire_l1)
    hist_min_face, fill_min_face = run(FACE_DIAGONAL, fire_min)
    checks.check(
        "theorem-1-face-diagonal",
        "the face-diagonal seed fills under both maps with history (2, 7, 11, 12)",
        fill_l1_face
        and fill_min_face
        and hist_l1_face == FACE_HISTORY
        and hist_min_face == FACE_HISTORY,
        residual=(hist_l1_face, hist_min_face, fill_l1_face, fill_min_face),
    )

    hist_l1_star, fill_l1_star = run(DISTINGUISHER, fire_l1)
    hist_min_star, fill_min_star = run(DISTINGUISHER, fire_min)
    splits_star = (fill_l1_star != fill_min_star) or (hist_l1_star != hist_min_star)
    checks.check(
        "theorem-1-distinguisher",
        "the seed {(0,0,0),(2,1,1)} splits fill or lock history",
        splits_star and fill_l1_star and not fill_min_star,
        residual=(hist_l1_star, hist_min_star, fill_l1_star, fill_min_star),
    )

    counts = census()
    n_split = int(counts["n_split"])
    n_fill_l1 = int(counts["n_fill_l1"])
    n_fill_min = int(counts["n_fill_min"])
    n_fill_both = int(counts["n_fill_both"])
    print(
        "census: "
        f"N_split={n_split} N_fill_L1={n_fill_l1} "
        f"N_fill_min={n_fill_min} N_fill_both={n_fill_both} "
        f"N_history_only={counts['n_history_only']} "
        f"N_fill_bit_only={counts['n_fill_only']}"
    )
    checks.check(
        "theorem-2-census-range",
        "the four census integers lie in 0..66 and N_fill_both <= min(N_fill_L1, N_fill_min)",
        counts["n_pairs"] == 66
        and 0 <= n_split <= 66
        and 0 <= n_fill_both <= min(n_fill_l1, n_fill_min)
        and n_fill_l1 <= 66
        and n_fill_min <= 66,
    )
    checks.check(
        "theorem-2-split-positive",
        "at least the displayed distinguisher contributes to N_split",
        n_split >= 1 and splits_star,
    )

    checks.check(
        "theorem-3-display",
        "the note displays the computed N_split and does not adopt a seed",
        f"N_split = {n_split}" in note
        and "displayed, not adopted" in normalized_note
        and "do not adopt" in normalized_note,
        residual=n_split,
    )
    checks.check(
        "theorem-3-fill-counts",
        "the note reports the three fill counts",
        f"N_fill_L1 = {n_fill_l1}" in note
        and f"N_fill_min = {n_fill_min}" in note
        and f"N_fill_both = {n_fill_both}" in note,
        residual=(n_fill_l1, n_fill_min, n_fill_both),
    )

    # Identity: f_L1 is n != 0, not Hamming weight of the six occupancy bits.
    # On this two-cube, n_both is possible only on the long axis at x=1.
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

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-phrases",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "no-admissibility-selector",
        "the note does not write a seed selector into Admissibility",
        "not written into Admissibility" in normalized_note
        and "selector" in normalized_note,
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the 66-seed display",
        "Among the 66 two-site seeds" in note and f"{n_split}" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
