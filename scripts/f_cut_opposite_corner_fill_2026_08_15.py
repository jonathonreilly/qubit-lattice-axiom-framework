#!/usr/bin/env python3
"""Opposite-corner F_cut fill census on the twelve-vertex two-cube.

Displayed occupancy-lock dynamics only. No Admissibility rewrite, no
axiom edit, no cache write, and no physical selector.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_OPPOSITE_CORNER_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_OPPOSITE_CORNER_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

PATCH: tuple[tuple[int, int, int], ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SEED_OPP: tuple[tuple[int, int, int], ...] = ((0, 0, 0), (2, 1, 1))
SEED_ONE: tuple[tuple[int, int, int], ...] = ((0, 0, 0),)
SEED_FACE: tuple[tuple[int, int, int], ...] = ((0, 0, 0), (1, 1, 0))

# Six nearest-neighbor slots: +x, -x, +y, -y, +z, -z.
SLOT_DIRS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_PAIRS: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
BIT_ORBITS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
ORBIT_OF_TYPE: dict[tuple[int, int, int], str] = {
    (0, 0, 3): "empty",
    (0, 3, 0): "full",
    (1, 0, 2): "wt1",
    (1, 2, 0): "wt5",
    (0, 1, 2): "opp2",
    (0, 2, 1): "opp2c",
    (2, 0, 1): "adj2",
    (2, 1, 0): "adj2c",
    (3, 0, 0): "vertex3",
    (1, 1, 1): "mixed3",
}
COMPLEMENT_TO_FREE: dict[str, str] = {
    "wt5": "wt1",
    "opp2c": "opp2",
    "adj2c": "adj2",
}

# f_L1 is n != 0: at least one unbalanced axis. Not Hamming weight or parity.
F_L1: tuple[int, int, int, int, int] = (1, 0, 1, 1, 1)
HAMMING_PARITY: tuple[int, int, int, int, int] = (1, 0, 0, 1, 1)
DISPLAYED_OTHER: tuple[int, int, int, int, int] = (1, 0, 1, 1, 0)


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


def add(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def axis_type(cell: tuple[int, ...]) -> tuple[int, int, int]:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for left, right in AXIS_PAIRS:
        total = cell[left] + cell[right]
        if total == 0:
            n_empty += 1
        elif total == 2:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def orbit_name(cell: tuple[int, ...]) -> str:
    return ORBIT_OF_TYPE[axis_type(cell)]


def occupancy_cell(
    vertex: tuple[int, int, int], occupied: set[tuple[int, int, int]]
) -> tuple[int, ...]:
    bits: list[int] = []
    for direction in SLOT_DIRS:
        neighbor = add(vertex, direction)
        bits.append(1 if neighbor in occupied else 0)
    return tuple(bits)


def f_cut_value(cell: tuple[int, ...], bits: tuple[int, ...]) -> int:
    name = orbit_name(cell)
    if name in ("empty", "full"):
        return 0
    if name in COMPLEMENT_TO_FREE:
        name = COMPLEMENT_TO_FREE[name]
    return bits[BIT_ORBITS.index(name)]


def n_unbalanced(cell: tuple[int, ...]) -> int:
    return axis_type(cell)[0]


def run_locks(
    bits: tuple[int, ...], seed: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, ...], frozenset[tuple[int, int, int]]]:
    locks: set[tuple[int, int, int]] = set(seed)
    history = [len(locks)]
    for _ in range(len(PATCH)):
        occupied = set(locks)
        newborn: set[tuple[int, int, int]] = set()
        for vertex in PATCH:
            if vertex in locks:
                continue
            if f_cut_value(occupancy_cell(vertex, occupied), bits) == 1:
                newborn.add(vertex)
        if not newborn:
            break
        locks |= newborn
        history.append(len(locks))
    return tuple(history), frozenset(locks)


def proper_cube_rotations() -> list[tuple[int, ...]]:
    """24 proper rotations as permutations of the six directed-axis slots."""
    rotations: list[tuple[int, ...]] = []
    for perm in permutations(range(3)):
        invert = 0
        seen = list(perm)
        for i in range(3):
            while seen[i] != i:
                j = seen[i]
                seen[i], seen[j] = seen[j], seen[i]
                invert += 1
        for signs in product((-1, 1), repeat=3):
            det = (1 if invert % 2 == 0 else -1) * signs[0] * signs[1] * signs[2]
            if det != 1:
                continue
            image: list[int] = [0] * 6
            for axis in range(3):
                for sign_index, sign in enumerate((1, -1)):
                    src = 2 * axis + sign_index
                    new_axis = perm[axis]
                    new_sign = sign * signs[axis]
                    dst = 2 * new_axis + (0 if new_sign == 1 else 1)
                    image[src] = dst
            rotations.append(tuple(image))
    return rotations


def apply_perm(cell: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for src, dst in enumerate(perm):
        out[dst] = cell[src]
    return tuple(out)


def f_min_value(cell: tuple[int, ...]) -> int:
    n_unb, n_both, _n_empty = axis_type(cell)
    return int(n_both == 0 and n_unb > 0)


def run_predicate(
    pred, seed: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, ...], frozenset[tuple[int, int, int]]]:
    locks: set[tuple[int, int, int]] = set(seed)
    history = [len(locks)]
    for _ in range(len(PATCH)):
        occupied = set(locks)
        newborn: set[tuple[int, int, int]] = set()
        for vertex in PATCH:
            if vertex in locks:
                continue
            if pred(occupancy_cell(vertex, occupied)) == 1:
                newborn.add(vertex)
        if not newborn:
            break
        locks |= newborn
        history.append(len(locks))
    return tuple(history), frozenset(locks)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; S-star, F_cut, and o=0 are displayed")
    print("package_local_integrity_reads: runner source, proposed source note, live axiom memo")
    print("measure_boundary: exact finite occupancy locks on twelve sites")
    print("negative_scope: no Admissibility rewrite and no unique-filler claim")

    rotations = proper_cube_rotations()
    orbit_sizes: dict[str, int] = {}
    for cell in product((0, 1), repeat=6):
        name = orbit_name(cell)
        orbit_sizes[name] = orbit_sizes.get(name, 0) + 1
        for perm in rotations:
            moved = apply_perm(cell, perm)
            if orbit_name(moved) != name:
                raise AssertionError("orbit name is not rotation-invariant")

    all_maps = tuple(bits for bits in product((0, 1), repeat=5))
    fillers: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for bits in all_maps:
        history, locks = run_locks(bits, SEED_OPP)
        if len(locks) == 12:
            fillers.append((bits, history))
    n_cutopp = len(fillers)
    other_tuples = [bits for bits, _history in fillers if bits != F_L1]

    one_site_fillers = [
        bits for bits in all_maps if run_locks(bits, SEED_ONE)[1].__len__() == 12
    ]
    face_fillers = [
        bits for bits in all_maps if run_locks(bits, SEED_FACE)[1].__len__() == 12
    ]
    l1_history, l1_locks = run_locks(F_L1, SEED_OPP)
    other_history, other_locks = run_locks(DISPLAYED_OTHER, SEED_OPP)
    ham_history, ham_locks = run_locks(HAMMING_PARITY, SEED_ONE)
    fmin_history, fmin_locks = run_predicate(f_min_value, SEED_OPP)

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_OPPOSITE_CORNER_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "two-cube-and-seed",
        "twelve-site two-cube and opposite-corner seed S-star",
        len(PATCH) == 12
        and len(set(PATCH)) == 12
        and set(SEED_OPP).issubset(set(PATCH))
        and SEED_OPP == ((0, 0, 0), (2, 1, 1)),
    )
    checks.check(
        "orbit-census-10",
        "ten directed-axis orbits partition the 64 cells",
        len(orbit_sizes) == 10
        and sum(orbit_sizes.values()) == 64
        and orbit_sizes["empty"] == 1
        and orbit_sizes["full"] == 1
        and orbit_sizes["wt1"] == 6
        and orbit_sizes["opp2"] == 3
        and orbit_sizes["adj2"] == 12
        and orbit_sizes["vertex3"] == 8
        and orbit_sizes["mixed3"] == 12
        and len(rotations) == 24,
    )
    checks.check(
        "f-cut-cardinality-32",
        "F_cut has 32 complement-even empty-full-silent maps",
        len(all_maps) == 32,
    )
    checks.check(
        "thm1-fl1-in-fcut",
        "f_L1 is the F_cut bit-tuple (1, 0, 1, 1, 1)",
        F_L1 in all_maps and F_L1 == (1, 0, 1, 1, 1),
    )
    checks.check(
        "thm1-fl1-is-n-neq-0",
        "f_L1 fires exactly on cells with at least one unbalanced axis",
        all(
            (f_cut_value(cell, F_L1) == 1) == (n_unbalanced(cell) != 0)
            for cell in product((0, 1), repeat=6)
        ),
    )
    checks.check(
        "thm1-fl1-not-hamming",
        "f_L1 is n != 0 and is not Hamming parity",
        F_L1 != HAMMING_PARITY
        and f_cut_value((1, 1, 0, 0, 0, 0), F_L1) == 0
        and f_cut_value((1, 1, 0, 0, 0, 0), HAMMING_PARITY) == 0
        and f_cut_value((1, 0, 1, 0, 0, 0), F_L1) == 1
        and f_cut_value((1, 0, 1, 0, 0, 0), HAMMING_PARITY) == 0,
    )
    checks.check(
        "thm1-history-2-8-12",
        "f_L1 fills from S-star with lock history (2, 8, 12)",
        l1_history == (2, 8, 12) and len(l1_locks) == 12,
    )
    checks.check(
        "thm2-n-cutopp",
        "N_cutopp equals 4",
        n_cutopp == 4 and len(all_maps) == 32,
    )
    checks.check(
        "thm3-not-unique",
        "f_L1 is not the unique S-star filler in F_cut",
        n_cutopp > 1 and F_L1 in [bits for bits, _history in fillers],
    )
    checks.check(
        "thm3-display-other-tuple",
        "another filler is the remaining-bit tuple (1, 0, 1, 1, 0)",
        DISPLAYED_OTHER in other_tuples
        and other_history == (2, 8, 12)
        and len(other_locks) == 12
        and set(bits for bits, _history in fillers)
        == {
            (1, 0, 1, 1, 0),
            (1, 0, 1, 1, 1),
            (1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1),
        },
    )
    checks.check(
        "seed-contrast-one-and-face",
        "same 32 maps give eight 1-site fillers and four face-diagonal fillers",
        len(one_site_fillers) == 8 and len(face_fillers) == 4,
    )
    checks.check(
        "fmin-does-not-fill-sstar",
        "the support-26 n_both=0 rival does not fill from S-star",
        len(fmin_locks) != 12 and fmin_history[-1] == 10,
    )
    checks.check(
        "hamming-one-site-nine",
        "Hamming parity is in F_cut and reaches nine locks from 1-site",
        HAMMING_PARITY in all_maps and ham_history[-1] == 9 and len(ham_locks) == 9,
    )
    checks.check(
        "mutation-unique-fails",
        "predicate N_cutopp == 1 fails",
        n_cutopp != 1,
    )
    checks.check(
        "displayed-not-adopted",
        "note displays the census and refuses adoption",
        "Displayed, not adopted" in note
        and "Do not write the four maps into Admissibility" in note
        and "no axiom or approved primitive is added" in note,
    )
    checks.check(
        "axiom-boundary-quotes",
        "Lattice covariance and Record lock sentences are quoted, not rewritten",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "machine-status-contract",
        "note carries the bounded-support status and no hypothetical axiom adoption",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "actual_current_surface_status: bounded-support" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases-absent",
        "note omits the five forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )

    print("per_element: checked exactly — each of the 32 F_cut maps is run from S-star")
    print("per_site: checked exactly — lock counts are on the twelve two-cube sites")
    print("per_mode: checked exactly — one occupancy predicate class and one opposite-corner seed")
    print("per_block: checked exactly — N_cutopp=4 and f_L1 is not unique among those four")
    print("lattice_wide: checked and not executed — no Z^3-wide law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
