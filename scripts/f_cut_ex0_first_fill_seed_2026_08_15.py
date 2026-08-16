#!/usr/bin/env python3
"""Lex-first seed that F_cut remaining bits (0,0,1,1,0) fill.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_ex0 is the remaining-bit tuple (wt1, opp2, adj2, vertex3,
mixed3)=(0,0,1,1,0). f_L1 is the unbalanced-axis predicate (some n_mu != 0),
never Hamming |c|_1 mod 2. The lex-first filling seed is displayed, not
adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_EX0_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_EX0_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EMPTY: Config = (0, 0, 0, 0, 0, 0)
FULL: Config = (1, 1, 1, 1, 1, 1)
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
ORIGIN: Site = (0, 0, 0)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
EX0_REMAINING: tuple[int, ...] = (0, 0, 1, 1, 0)
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
DISPLAYED_SEED: tuple[Site, ...] = ((0, 0, 0), (1, 0, 1), (2, 1, 0))
DISPLAYED_HISTORY: tuple[tuple[Site, ...], ...] = (
    ((0, 0, 0), (1, 0, 1), (2, 1, 0)),
    ((0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (2, 1, 0)),
    ((0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0), (2, 1, 0)),
    (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
        (2, 0, 0),
        (2, 0, 1),
        (2, 1, 0),
    ),
    tuple(TWO_CUBE),
)


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Direction) -> Direction:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {direction: rotate_vector(rotation, direction) for direction in DIRECTIONS}
    inverse = {image: source for source, image in forward.items()}
    return tuple(occupancy[inverse[direction]] for direction in DIRECTIONS)  # type: ignore[return-value]


def axis_type(config: Config) -> OrbitType:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for axis in range(3):
        plus = config[2 * axis]
        minus = config[2 * axis + 1]
        if plus != minus:
            n_unbalanced += 1
        elif plus == 1:
            n_both += 1
        else:
            n_empty += 1
    return (n_unbalanced, n_both, n_empty)


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def f_ex0(config: Config) -> int:
    """F_cut remaining bits (0, 0, 1, 1, 0). Displayed, not adopted."""
    return remaining_value(config, EX0_REMAINING)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def neighborhood(site: Site, locked: set[Site]) -> Config:
    values = []
    for direction in DIRECTIONS:
        neighbor = (
            site[0] + direction[0],
            site[1] + direction[1],
            site[2] + direction[2],
        )
        values.append(1 if neighbor in locked else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def history(predicate, seed: frozenset[Site]) -> tuple[list[int], list[frozenset[Site]], set[Site]]:
    locked = set(seed)
    sizes = [len(locked)]
    snapshots = [frozenset(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return sizes, snapshots, locked
        locked = nxt
        sizes.append(len(locked))
        snapshots.append(frozenset(locked))
    return sizes, snapshots, locked


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    _sizes, _snapshots, locked = history(predicate, seed)
    return len(locked) == 12


def coverage(predicate, k: int) -> int:
    return sum(
        1
        for seed in combinations(TWO_CUBE, k)
        if fills_from_seed(predicate, frozenset(seed))
    )


def lex_first_fill(predicate, max_k: int = 6) -> tuple[int, tuple[Site, ...], list[int], list[frozenset[Site]]]:
    for k in range(1, max_k + 1):
        for seed in combinations(TWO_CUBE, k):
            s = frozenset(seed)
            if fills_from_seed(predicate, s):
                sizes, snapshots, _halt = history(predicate, s)
                return k, tuple(sorted(seed)), sizes, snapshots
    raise RuntimeError("no filling seed through the declared search bound")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    origin_sizes, origin_snaps, origin_halt = history(f_ex0, frozenset([ORIGIN]))
    p_ex0 = 0 if origin_sizes == [1] and len(origin_halt) == 1 else 1
    cov2 = coverage(f_ex0, 2)
    cov3 = coverage(f_ex0, 3)
    lex_k, lex_seed, lex_sizes, lex_snaps = lex_first_fill(f_ex0)
    lex_sites = tuple(sorted(lex_snaps[i]) for i in range(len(lex_snaps)))

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_two_cube={len(TWO_CUBE)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"f_ex0_remaining={EX0_REMAINING}")
    print(f"f_L1_remaining={L1_REMAINING}")
    print(f"origin_history_sizes={origin_sizes}")
    print(f"origin_halt={sorted(origin_halt)}")
    print(f"P={p_ex0}")
    print(f"cov2={cov2}")
    print(f"cov3={cov3}")
    print(f"lex_first_k={lex_k}")
    print(f"lex_first_seed={lex_seed}")
    print(f"lex_hist_sizes={lex_sizes}")
    for tick, snap in enumerate(lex_sites):
        print(f"  t{tick}={snap}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_EX0_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_EX0_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations-and-two-cube",
        "exactly 24 proper cube rotations and twelve two-cube vertices",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and ORIGIN in TWO_CUBE
        and TWO_CUBE == tuple(sorted(TWO_CUBE)),
    )
    checks.check(
        "thm1-f-ex0-remaining-bits",
        "f_ex0 is F_cut remaining bits (0,0,1,1,0) and not f_L1",
        EX0_REMAINING == (0, 0, 1, 1, 0)
        and EX0_REMAINING != L1_REMAINING
        and all(f_ex0(EMPTY) == 0 and f_ex0(FULL) == 0 for _ in (0,))
        and all(
            f_ex0(config) == f_ex0(tuple(1 - bit for bit in config))  # type: ignore[arg-type]
            for config in product((0, 1), repeat=6)
        )
        and remaining_value(EMPTY, EX0_REMAINING) == 0
        and remaining_value((1, 0, 0, 0, 0, 0), EX0_REMAINING) == 0
        and remaining_value((1, 0, 1, 0, 0, 0), EX0_REMAINING) == 1
        and remaining_value((1, 0, 1, 0, 1, 0), EX0_REMAINING) == 1
        and remaining_value((1, 0, 1, 1, 0, 0), EX0_REMAINING) == 0,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is unbalanced-axis n_mu != 0 and is not Hamming parity",
        L1_REMAINING == (1, 0, 1, 1, 1)
        and all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-P-zero-origin-history",
        "P=0: origin seed dies at history (1)",
        p_ex0 == 0
        and origin_sizes == [1]
        and origin_halt == {ORIGIN}
        and origin_snaps == [frozenset([ORIGIN])]
        and not fills_from_seed(f_ex0, frozenset([ORIGIN]))
        and coverage(f_ex0, 1) == 0
        and "P=0" in note
        and "dies at history (1)" in note,
    )
    checks.check(
        "thm1-cov2-and-cov3",
        "cov2(f_ex0)=0 and cov3(f_ex0)=24",
        cov2 == 0
        and cov3 == 24
        and "cov2 = 0" in note
        and "cov3 = 24" in note,
    )
    checks.check(
        "thm2-lex-first-size-and-sites",
        "lex-first filling seed has size 3 and sites ((0,0,0),(1,0,1),(2,1,0))",
        lex_k == 3
        and lex_seed == DISPLAYED_SEED
        and lex_seed == ((0, 0, 0), (1, 0, 1), (2, 1, 0))
        and fills_from_seed(f_ex0, frozenset(lex_seed))
        and "|S| = 3" in note
        and "(0, 0, 0), (1, 0, 1), (2, 1, 0)" in note,
    )
    checks.check(
        "thm2-no-smaller-fill",
        "no 1-site or 2-site seed fills, so the size-3 seed is first",
        coverage(f_ex0, 1) == 0
        and cov2 == 0
        and all(
            not fills_from_seed(f_ex0, frozenset(seed))
            for seed in combinations(TWO_CUBE, 3)
            if tuple(sorted(seed)) < lex_seed
        ),
    )
    checks.check(
        "thm3-displayed-history",
        "the displayed seed fills in four ticks along the reported history",
        lex_sizes == [3, 5, 7, 10, 12]
        and len(lex_snaps) == 5
        and tuple(tuple(sorted(snap)) for snap in lex_snaps) == DISPLAYED_HISTORY
        and len(lex_snaps[-1]) == 12
        and set(lex_snaps[-1]) == set(TWO_CUBE)
        and "history sizes (3, 5, 7, 10, 12)" in note,
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted seed, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "claim-scope-first-fill",
        "claim_scope states the lex-first seed that F_cut (0,0,1,1,0) fills",
        "On the two-cube with off-patch o=0, the" in note
        and "lex-first seed that F_cut (0,0,1,1,0) fills is reported" in note
        and "Displayed, not adopted" in note
        and "Do not write the seed or the remaining bits into Admissibility" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the seed or the remaining bits into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "new-first-fill-not-leftover-coverage",
        "the residual is the first fill of the newly named map, not leftover of the coverage counts",
        "New first fill of a newly named map" in note
        and "#6511" in note
        and "#6502" in note
        and "not leftover of the P=0 / cov3=24 counts" in note,
    )

    print("per_element: checked exactly — each neighbor 6-tuple is scored by the remaining-bit assignment of f_ex0")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — P, cov2, cov3, and the lex-first filling seed of this one F_cut map")
    print("per_block: checked exactly — the displayed size-3 seed fills and no smaller seed does")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
