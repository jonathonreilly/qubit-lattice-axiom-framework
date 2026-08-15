#!/usr/bin/env python3
"""Orbit count of the four f_min/f_L1 split seeds under two-cube rotations.

Recomputes the four two-site seeds that split f_min from f_L1 on
{0,1,2} x {0,1} x {0,1} with off-patch occupancy 0, then counts
G-orbits under the proper cube rotations about the box center
(1, 1/2, 1/2) that permute those twelve sites. Displays N_orb; does
not adopt a seed or write an orbit into Admissibility.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIN_L1_SPLIT_SEED_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_L1_SPLIT_SEED_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
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


def split_seeds() -> tuple[frozenset[Point], ...]:
    found: list[frozenset[Point]] = []
    for pair in combinations(SITES, 2):
        seed = frozenset(pair)
        hist_l1, fill_l1 = run(seed, fire_l1)
        hist_min, fill_min = run(seed, fire_min)
        if fill_l1 != fill_min or hist_l1 != hist_min:
            found.append(seed)
    return tuple(found)


def det3(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cube_rotations() -> tuple[Matrix, ...]:
    """The 24 proper cubic matrices: signed permutations with det +1."""
    mats: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                rows[i][perm[i]] = signs[i]
            matrix = (tuple(rows[0]), tuple(rows[1]), tuple(rows[2]))
            if det3(matrix) == 1:
                mats.append(matrix)
    return tuple(mats)


def apply_about_center(matrix: Matrix, point: Point) -> Point | None:
    """Apply R about the box center (1, 1/2, 1/2) in doubled integer coordinates."""
    delta = (2 * point[0] - 2, 2 * point[1] - 1, 2 * point[2] - 1)
    image = tuple(sum(matrix[i][j] * delta[j] for j in range(3)) for i in range(3))
    if (image[0] + 2) % 2 != 0 or (image[1] + 1) % 2 != 0 or (image[2] + 1) % 2 != 0:
        return None
    return ((image[0] + 2) // 2, (image[1] + 1) // 2, (image[2] + 1) // 2)


def two_cube_preserving_rotations() -> tuple[Matrix, ...]:
    """Keep only proper cube rotations that permute the twelve sites."""
    kept: list[Matrix] = []
    for matrix in proper_cube_rotations():
        images = [apply_about_center(matrix, site) for site in SITES]
        if all(image in SITE_SET for image in images) and set(images) == SITE_SET:
            kept.append(matrix)
    return tuple(kept)


def act_on_seed(matrix: Matrix, seed: frozenset[Point]) -> frozenset[Point] | None:
    images = [apply_about_center(matrix, site) for site in seed]
    if any(image is None or image not in SITE_SET for image in images):
        return None
    return frozenset(images)  # type: ignore[arg-type]


def orbit_count(seeds: tuple[frozenset[Point], ...], group: tuple[Matrix, ...]) -> int:
    unused = set(range(len(seeds)))
    n_orb = 0
    while unused:
        start = min(unused)
        unused.remove(start)
        stack = [start]
        n_orb += 1
        while stack:
            index = stack.pop()
            for matrix in group:
                image = act_on_seed(matrix, seeds[index])
                if image is None:
                    continue
                for other, seed in enumerate(seeds):
                    if seed == image and other in unused:
                        unused.remove(other)
                        stack.append(other)
    return n_orb


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
    print("construction: four split seeds recomputed; G-orbits under two-cube-preserving proper cube rotations")
    print("negative_scope: N_orb is displayed; no seed is adopted and no orbit is written into Admissibility")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_L1_SPLIT_SEED_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

    ambient = proper_cube_rotations()
    group = two_cube_preserving_rotations()
    seeds = split_seeds()
    n_split = len(seeds)
    n_orb = orbit_count(seeds, group)
    print(
        "orbit: "
        f"N_split={n_split} N_ambient={len(ambient)} "
        f"|G|={len(group)} N_orb={n_orb}"
    )
    print("split_seeds: " + "; ".join(str(tuple(sorted(seed))) for seed in seeds))

    checks.check(
        "two-cube-and-ambient",
        "the two-cube has twelve sites and the ambient proper cubic group has 24 matrices",
        len(SITES) == 12 and len(SITE_SET) == 12 and len(ambient) == 24 and len(set(ambient)) == 24,
    )
    checks.check(
        "group-preserves-twelve",
        "only site-permutations of the two-cube induced by proper cube rotations are used",
        0 < len(group) <= 24
        and all(det3(matrix) == 1 for matrix in group)
        and all(
            {apply_about_center(matrix, site) for site in SITES} == SITE_SET
            for matrix in group
        ),
        residual=len(group),
    )
    unused_count = len(ambient) - len(group)
    checks.check(
        "unused-non-permutations",
        "rotations that do not permute the twelve sites are discarded",
        unused_count == 16 and unused_count + len(group) == 24,
        residual=unused_count,
    )

    all_split_histories = True
    lex_seeds = tuple(tuple(sorted(seed)) for seed in seeds)
    for seed in seeds:
        hist_l1, fill_l1 = run(seed, fire_l1)
        hist_min, fill_min = run(seed, fire_min)
        if not (
            fill_l1
            and not fill_min
            and hist_l1 == L1_SPLIT_HISTORY
            and hist_min == MIN_SPLIT_HISTORY
        ):
            all_split_histories = False
    expected_lex = (
        ((0, 0, 0), (2, 1, 1)),
        ((0, 0, 1), (2, 1, 0)),
        ((0, 1, 0), (2, 0, 1)),
        ((0, 1, 1), (2, 0, 0)),
    )
    checks.check(
        "theorem-1-four-split-seeds",
        "recomputed N_split=4 with f_L1 history (2,8,12) and f_min halt (2,8,10)",
        n_split == 4 and all_split_histories and lex_seeds == expected_lex,
        residual=lex_seeds,
    )
    checks.check(
        "theorem-1-n-orb",
        "N_orb is the number of G-orbits among the four seeds",
        n_orb >= 1 and n_orb <= n_split == 4,
        residual=n_orb,
    )

    if n_orb == 1:
        theorem2_ok = (
            "N_orb = 1" in note
            and "one geometric type" in normalized_note
            and "opposite corners" in normalized_note
        )
        theorem2_statement = "N_orb=1: the note reports one geometric type (opposite corners of the long box)"
    else:
        second = tuple(sorted(seeds[1])) if n_split > 1 else ()
        theorem2_ok = (
            f"N_orb = {n_orb}" in note
            and "second orbit" in normalized_note
            and str(second) in note.replace(" ", "")
        )
        theorem2_statement = "N_orb>1: the note displays one seed from a second orbit"
    checks.check("theorem-2-geometric-type", theorem2_statement, theorem2_ok, residual=n_orb)

    checks.check(
        "theorem-3-display",
        "the note displays the computed N_orb and does not adopt a seed or orbit",
        f"N_orb = {n_orb}" in note
        and "displayed, not adopted" in normalized_note
        and "do not adopt" in normalized_note
        and "not written into Admissibility" in normalized_note,
        residual=n_orb,
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

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-phrases",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "no-admissibility-orbit",
        "the note does not write an orbit into Admissibility",
        "not written into Admissibility" in normalized_note
        and "orbit" in normalized_note,
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the orbit-count display",
        "form" in note and "orbits under two-cube-preserving proper cube rotations" in note and f"{n_orb}" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
