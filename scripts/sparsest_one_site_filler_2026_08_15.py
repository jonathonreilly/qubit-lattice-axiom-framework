#!/usr/bin/env python3
"""Support-minimizer census among cube-covariant 1-site two-cube fillers.

Enumerates the 24 proper cube rotations, the 10 orbits on {0,1}^6, and the
512 cube-covariant maps with f(empty)=0. Fills the twelve-vertex two-cube
from a 1-site seed with off-patch occupancy 0. Among the 96 fillers, reports
the minimal support and whether f_L1 (some axis unbalanced; never Hamming
parity) is the unique minimizer.

No axiom edit, no cache write, no citation-manifest write.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/SPARSEST_ONE_SITE_FILLER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

DIRS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}

PATCH: tuple[tuple[int, int, int], ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
SEED = (0, 0, 0)
EMPTY = (0, 0, 0, 0, 0, 0)
FULL = (1, 1, 1, 1, 1, 1)
Cell = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def matrix_det(matrix: Rotation) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_rotations() -> tuple[Rotation, ...]:
    rotations: list[Rotation] = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for row in range(3):
                matrix[row][perm[row]] = signs[row]
            rotation = tuple(tuple(row) for row in matrix)
            if matrix_det(rotation) == 1:
                rotations.append(rotation)  # type: ignore[arg-type]
    return tuple(rotations)


def apply_rotation(cell: Cell, rotation: Rotation) -> Cell:
    image = [0] * 6
    for index, direction in enumerate(DIRS):
        mapped = (
            rotation[0][0] * direction[0]
            + rotation[0][1] * direction[1]
            + rotation[0][2] * direction[2],
            rotation[1][0] * direction[0]
            + rotation[1][1] * direction[1]
            + rotation[1][2] * direction[2],
            rotation[2][0] * direction[0]
            + rotation[2][1] * direction[1]
            + rotation[2][2] * direction[2],
        )
        image[DIR_INDEX[mapped]] = cell[index]
    return (image[0], image[1], image[2], image[3], image[4], image[5])


def orbit_catalog(
    rotations: tuple[Rotation, ...],
) -> tuple[frozenset[Cell], ...]:
    remaining = set(product((0, 1), repeat=6))
    orbits: list[frozenset[Cell]] = []
    while remaining:
        seed = min(remaining)
        bucket: set[Cell] = set()
        stack = [seed]
        while stack:
            cell = stack.pop()
            if cell in bucket:
                continue
            bucket.add(cell)
            for rotation in rotations:
                stack.append(apply_rotation(cell, rotation))
        remaining -= bucket
        orbits.append(frozenset(bucket))
    return tuple(sorted(orbits, key=lambda orbit: (min(orbit), len(orbit))))


def f_L1(cell: Cell) -> bool:
    """True iff some axis is unbalanced: n ≠ 0. Never Hamming |c|_1 mod 2."""
    return cell[0] != cell[1] or cell[2] != cell[3] or cell[4] != cell[5]


def f_min(cell: Cell) -> bool:
    """Nonempty axis-transversal: at most one occupied sign per axis."""
    if cell == EMPTY:
        return False
    return (
        cell[0] + cell[1] <= 1
        and cell[2] + cell[3] <= 1
        and cell[4] + cell[5] <= 1
    )


def f_hamming(cell: Cell) -> bool:
    return sum(cell) % 2 == 1


def occupancy_cell(
    vertex: tuple[int, int, int],
    locked: set[tuple[int, int, int]],
) -> Cell:
    bits = []
    for direction in DIRS:
        neighbor = (
            vertex[0] + direction[0],
            vertex[1] + direction[1],
            vertex[2] + direction[2],
        )
        bits.append(1 if neighbor in locked else 0)
    return (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])


def run_fill(predicate) -> tuple[int, tuple[int, ...]]:
    locked = {SEED}
    history = [1]
    for _ in range(12):
        newcomers = {
            vertex
            for vertex in PATCH
            if vertex not in locked and predicate(occupancy_cell(vertex, locked))
        }
        if not newcomers:
            break
        locked |= newcomers
        history.append(len(locked))
    return len(locked), tuple(history)


def mask_from_predicate(
    predicate,
    orbits: tuple[frozenset[Cell], ...],
) -> int:
    mask = 0
    for index, orbit in enumerate(orbits):
        values = {bool(predicate(cell)) for cell in orbit}
        if len(values) != 1:
            raise ValueError("predicate is not constant on a cube orbit")
        if True in values:
            mask |= 1 << index
    return mask


def predicate_from_mask(mask: int, cell_to_orbit: dict[Cell, int]):
    def predicate(cell: Cell, _mask: int = mask) -> bool:
        return bool(_mask & (1 << cell_to_orbit[cell]))

    return predicate


def support_of_mask(mask: int, orbits: tuple[frozenset[Cell], ...]) -> int:
    return sum(len(orbit) for index, orbit in enumerate(orbits) if mask & (1 << index))


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; two-cube patch, seed, and off-patch o=0 are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact finite census on 64 cells and 12 vertices; no physical selector")
    print("negative_scope: sparsity among 1-site fillers does not select f_L1")

    rotations = proper_rotations()
    checks.check(
        "rotations-24",
        "exactly 24 distinct proper cube rotations",
        len(rotations) == 24 and len(set(rotations)) == 24,
    )
    checks.check(
        "rotations-det-plus",
        "every listed rotation has determinant +1",
        all(matrix_det(rotation) == 1 for rotation in rotations),
    )

    orbits = orbit_catalog(rotations)
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    checks.check(
        "orbits-10",
        "exactly 10 orbits on the 64 cells",
        len(orbits) == 10 and sum(orbit_sizes) == 64,
    )
    checks.check(
        "empty-full-orbits",
        "empty and full are singleton orbits",
        EMPTY in orbits[0]
        and len(orbits[0]) == 1
        and FULL in orbits[-1]
        and len(orbits[-1]) == 1,
    )
    checks.check(
        "patch-12",
        "the two-cube patch has twelve vertices",
        len(PATCH) == 12 and len(set(PATCH)) == 12 and SEED in PATCH,
    )

    l1_ok = all(
        f_L1(apply_rotation(cell, rotation)) == f_L1(cell)
        for cell in product((0, 1), repeat=6)
        for rotation in rotations
    )
    min_ok = all(
        f_min(apply_rotation(cell, rotation)) == f_min(cell)
        for cell in product((0, 1), repeat=6)
        for rotation in rotations
    )
    checks.check("l1-covariant", "f_L1 is constant on every proper-cube orbit", l1_ok)
    checks.check("min-covariant", "the displayed minimizer is cube-covariant", min_ok)
    checks.check("l1-empty-zero", "f_L1(empty)=0", not f_L1(EMPTY))
    checks.check(
        "l1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        any(f_L1(cell) != f_hamming(cell) for cell in product((0, 1), repeat=6)),
    )

    cell_to_orbit = {
        cell: index for index, orbit in enumerate(orbits) for cell in orbit
    }
    l1_mask = mask_from_predicate(f_L1, orbits)
    min_mask = mask_from_predicate(f_min, orbits)
    ham_mask = mask_from_predicate(f_hamming, orbits)
    l1_support = support_of_mask(l1_mask, orbits)
    min_support = support_of_mask(min_mask, orbits)
    checks.check(
        "l1-support-56",
        "supp(f_L1)=56, equivalently 64 minus the 8 fully balanced cells",
        l1_support == 56
        and sum(1 for cell in product((0, 1), repeat=6) if f_L1(cell)) == 56,
    )
    checks.check(
        "min-support-26",
        "the displayed minimizer has support 3^3-1=26",
        min_support == 26
        and sum(1 for cell in product((0, 1), repeat=6) if f_min(cell)) == 26,
    )
    checks.check(
        "min-strict-subset-l1",
        "the displayed minimizer is a strict subset of f_L1",
        min_mask != l1_mask
        and min_mask & ~l1_mask == 0
        and all((not f_min(cell)) or f_L1(cell) for cell in product((0, 1), repeat=6)),
    )

    free = [index for index in range(10) if index != 0]
    checks.check("maps-512", "f(empty)=0 leaves 2^9=512 cube-covariant maps", len(free) == 9)

    fillers: list[tuple[int, int]] = []
    for bits in range(1 << 9):
        mask = 0
        for slot, index in enumerate(free):
            if bits & (1 << slot):
                mask |= 1 << index
        locks, _history = run_fill(predicate_from_mask(mask, cell_to_orbit))
        if locks == 12:
            fillers.append((mask, support_of_mask(mask, orbits)))

    n_fill = len(fillers)
    supports = [support for _mask, support in fillers]
    minimum = min(supports)
    n_min = sum(1 for support in supports if support == minimum)
    min_masks = [mask for mask, support in fillers if support == minimum]
    l1_locks, l1_history = run_fill(f_L1)
    min_locks, min_history = run_fill(f_min)
    ham_locks, _ham_history = run_fill(f_hamming)

    checks.check("thm1-n-fill-96", "N_fill=96 among the 512 maps", n_fill == 96)
    checks.check(
        "thm1-l1-fills",
        "f_L1 fills the twelve-vertex two-cube from the 1-site seed",
        l1_locks == 12 and l1_mask in {mask for mask, _support in fillers},
    )
    checks.check(
        "thm2-minimum-26",
        "m = min supp(f) over fillers equals 26",
        minimum == 26,
    )
    checks.check(
        "thm2-n-min-1",
        "exactly one filler attains the minimum support",
        n_min == 1 and len(min_masks) == 1,
    )
    checks.check(
        "thm3-unique-is-not-l1",
        "the unique support-minimizer is not f_L1",
        n_min == 1 and min_masks[0] == min_mask and min_masks[0] != l1_mask,
    )
    checks.check(
        "thm3-min-fills",
        "the displayed unique minimizer fills, with the same lock counts as f_L1",
        min_locks == 12 and min_history == l1_history == (1, 4, 8, 11, 12),
    )
    checks.check(
        "mutation-hamming-nine-locks",
        "Hamming parity is covariant but does not fill (9 locks)",
        ham_locks == 9 and ham_mask != l1_mask and ham_mask != min_mask,
    )
    checks.check(
        "mutation-weight-one-only",
        "the weight-1 orbit alone is not a filler",
        run_fill(predicate_from_mask(1 << 1, cell_to_orbit))[0] != 12,
    )
    hist = Counter(supports)
    checks.check(
        "support-histogram-unique-tail",
        "the support histogram has a unique minimum bin at 26",
        hist[26] == 1 and all(key >= 26 for key in hist),
    )

    banned = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases-absent",
        "note avoids the forbidden phrase list",
        all(phrase not in note for phrase in banned),
    )
    checks.check(
        "l1-definition-unbalanced-axis",
        "the note defines f_L1 by an unbalanced axis / n≠0, not Hamming parity",
        "unbalanced" in note
        and "Hamming" in note
        and "never Hamming" in note
        and "n ≠ 0" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the minimizer and f_L1 are displayed, not adopted",
        "Displayed, not adopted" in note
        and "hypothetical_axiom_status: \"not proposed; no axiom or approved primitive is added\""
        in note,
    )
    checks.check(
        "axiom-quotes",
        "Lattice nearest-neighbor / proper-cubic and Record lock sentences are quoted live",
        "proper cubic rotations about each site" in axiom
        and "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "proper cubic rotations about each site" in note
        and "one fixed nearest-neighbor admissibility rule" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SPARSEST_ONE_SITE_FILLER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )
    checks.check(
        "claim-scope-minimum",
        "claim_scope reports m=26, N_min=1, and that f_L1 is not the unique minimizer",
        "minimal support size is 26" in note
        and "N_min = 1" in note
        and "f_L1 is not the unique minimizer" in note,
    )
    cache_probe = ROOT / "logs" / ("runner" + "-cache") / (
        "sparsest_one_site_filler_2026_08_15.txt"
    )
    checks.check(
        "no-cache-write",
        "this run did not emit a runner cache file",
        not cache_probe.is_file(),
    )

    print("per_element: checked exactly — each of the 64 cells is assigned by orbit and counted in supp(f)")
    print("per_site: checked exactly — each of the 12 two-cube vertices is a lock site under o=0")
    print("per_mode: checked exactly — the 512 empty-vanishing cube-covariant maps and the 96 fillers")
    print("per_block: checked exactly — unique support minimum 26 is attained by the axis-transversal filler, not f_L1")
    print("lattice_wide: checked and not executed — no infinite-lattice fill or adopted occupancy axiom is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
