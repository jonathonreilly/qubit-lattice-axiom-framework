#!/usr/bin/env python3
"""Enumerate the cube-covariant boolean formation predicates on {0,1}^6.

The paired note is
docs/CUBE_COVARIANT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md.

The objects are occupancy 6-tuples on the six directed nearest-neighbor slots
and the 24 proper cube rotations acting by slot permutation. No formation
member is selected. No axiom sentence is written. No cache is written.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/CUBE_COVARIANT_FORMATION_PREDICATE_CLASS_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CUBE_COVARIANT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

SLOTS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_INDEX = {slot: i for i, slot in enumerate(SLOTS)}
AXIS_PAIRS = ((0, 1), (2, 3), (4, 5))


def normalize(text: str) -> str:
    return " ".join(text.split())


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_rotation_matrices() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    mats: list[tuple[tuple[int, int, int], ...]] = []
    for perm in permutations(range(3)):
        axis_sign = permutation_sign(perm)
        for signs in product((-1, 1), repeat=3):
            det = axis_sign * signs[0] * signs[1] * signs[2]
            if det != 1:
                continue
            rows = [[0, 0, 0] for _ in range(3)]
            for col, row in enumerate(perm):
                rows[row][col] = signs[col]
            mats.append(tuple(tuple(row) for row in rows))
    unique = tuple(sorted(set(mats)))
    return unique


def matvec(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def matmul(
    left: tuple[tuple[int, int, int], ...],
    right: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose(matrix: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def slot_permutation(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(SLOT_INDEX[matvec(matrix, slot)] for slot in SLOTS)


def apply_perm(cell: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for source, dest in enumerate(perm):
        out[dest] = cell[source]
    return tuple(out)


def all_cells() -> tuple[tuple[int, ...], ...]:
    return tuple(product((0, 1), repeat=6))


def cycle_count(perm: tuple[int, ...]) -> int:
    seen = [False] * len(perm)
    cycles = 0
    for start in range(len(perm)):
        if seen[start]:
            continue
        cycles += 1
        here = start
        while not seen[here]:
            seen[here] = True
            here = perm[here]
    return cycles


def orbit_partition(perms: tuple[tuple[int, ...], ...]) -> tuple[frozenset[tuple[int, ...]], ...]:
    remaining = set(all_cells())
    orbits: list[frozenset[tuple[int, ...]]] = []
    while remaining:
        seed = remaining.pop()
        orbit = {seed}
        stack = [seed]
        while stack:
            cell = stack.pop()
            for perm in perms:
                image = apply_perm(cell, perm)
                if image not in orbit:
                    orbit.add(image)
                    stack.append(image)
        remaining -= orbit
        orbits.append(frozenset(orbit))
    return tuple(sorted(orbits, key=lambda orbit: (len(orbit), min(orbit))))


def unbalanced_axis_count(cell: tuple[int, ...]) -> int:
    return sum(cell[plus] != cell[minus] for plus, minus in AXIS_PAIRS)


def f_l1(cell: tuple[int, ...]) -> int:
    return 0 if all(cell[plus] == cell[minus] for plus, minus in AXIS_PAIRS) else 1


def f_empty(cell: tuple[int, ...]) -> int:
    return int(cell == (0, 0, 0, 0, 0, 0))


def f_any(cell: tuple[int, ...]) -> int:
    return int(sum(cell) >= 1)


def f_full(cell: tuple[int, ...]) -> int:
    return int(cell == (1, 1, 1, 1, 1, 1))


def f_two(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 2)


def table_of(func) -> tuple[int, ...]:
    return tuple(func(cell) for cell in all_cells())


def is_covariant(func, perms: tuple[tuple[int, ...], ...]) -> bool:
    for cell in all_cells():
        value = func(cell)
        for perm in perms:
            if func(apply_perm(cell, perm)) != value:
                return False
    return True


def constant_on_orbits(func, orbits: tuple[frozenset[tuple[int, ...]], ...]) -> bool:
    for orbit in orbits:
        values = {func(cell) for cell in orbit}
        if len(values) != 1:
            return False
    return True


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("Cube-covariant formation predicate class on occupancy 6-tuples")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: boolean maps on the 64 occupancy 6-tuples; no member adopted")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-unique-normalized",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    covariant_rule_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice "
        "translations and proper cubic rotations."
    )
    formation_boundary = "it does not supply the formation site, probability, or rate"
    records_form = "Records form."

    checks.check(
        "source-lattice-current",
        lattice_sentence in normalized_axiom and lattice_sentence in normalized_note,
    )
    checks.check(
        "source-one-fixed-covariant-rule-current",
        covariant_rule_sentence in normalized_axiom
        and covariant_rule_sentence in normalized_note,
    )
    checks.check(
        "source-formation-open-current",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-records-form-current",
        records_form in axiom and records_form in note,
    )
    checks.check(
        "note-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        or 'hypothetical_axiom_status: "no edit"' in note,
    )

    cells = all_cells()
    checks.check("cell-count-64", len(cells) == 64 and len(set(cells)) == 64)
    checks.check("cells-are-binary-6-tuples", all(len(cell) == 6 and set(cell) <= {0, 1} for cell in cells))

    rotations = proper_rotation_matrices()
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    inversion = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    rotation_set = set(rotations)
    checks.check("rotation-count-24", len(rotations) == 24)
    checks.check("rotations-include-identity", identity in rotation_set)
    checks.check("rotations-exclude-inversion", inversion not in rotation_set)
    checks.check(
        "rotation-group-closed",
        all(matmul(left, right) in rotation_set for left in rotations for right in rotations),
    )
    checks.check(
        "rotation-inverses-present",
        all(transpose(matrix) in rotation_set and matmul(matrix, transpose(matrix)) == identity for matrix in rotations),
    )
    checks.check(
        "rotation-determinants-plus-one",
        all(
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            == 1
            for matrix in rotations
        ),
    )

    perms = tuple(slot_permutation(matrix) for matrix in rotations)
    checks.check("slot-permutations-24-distinct", len(set(perms)) == 24)
    checks.check("slot-permutations-are-bijections", all(sorted(perm) == list(range(6)) for perm in perms))

    orbits = orbit_partition(perms)
    n_orb = len(orbits)
    covered = set().union(*orbits)
    class_size = 1 << n_orb
    burnside_fixed = sum(1 << cycle_count(perm) for perm in perms)
    burnside_orbits, burnside_rem = divmod(burnside_fixed, 24)

    print(f"N_orb={n_orb}")
    print(f"|F_G|={class_size}")
    print(f"orbit_sizes={sorted(len(orbit) for orbit in orbits)}")
    print(f"burnside_orbits={burnside_orbits}")

    checks.check("orbits-partition-C", covered == set(cells) and sum(len(orbit) for orbit in orbits) == 64)
    checks.check("orbit-count-is-positive-int", isinstance(n_orb, int) and n_orb > 0)
    checks.check(
        "burnside-agrees-exact-int",
        burnside_rem == 0 and burnside_orbits == n_orb and isinstance(burnside_fixed, int),
        f"sum={burnside_fixed}",
    )
    checks.check("class-size-is-two-to-N_orb", class_size == 2**n_orb)
    checks.check(
        "covariant-maps-are-orbit-constant",
        all(constant_on_orbits(lambda cell, orbit=orbit: int(cell in orbit), orbits) for orbit in orbits)
        and is_covariant(lambda cell: int(cell in next(iter(orbits))), perms),
    )

    named = {
        "f_L1": f_l1,
        "f_empty": f_empty,
        "f_any": f_any,
        "f_full": f_full,
        "f_two": f_two,
    }
    tables = {name: table_of(func) for name, func in named.items()}
    for name, func in named.items():
        checks.check(
            f"{name}-cube-covariant",
            is_covariant(func, perms) and constant_on_orbits(func, orbits),
        )

    checks.check(
        "f_L1-is-n-nonzero",
        all(f_l1(cell) == int(unbalanced_axis_count(cell) != 0) for cell in cells),
    )
    checks.check(
        "named-predicates-distinct-from-f_L1",
        all(tables[name] != tables["f_L1"] for name in ("f_empty", "f_any", "f_full", "f_two")),
    )
    checks.check(
        "named-predicates-pairwise-distinct",
        len({tables[name] for name in named}) == len(named),
    )

    disagree = sum(f_l1(cell) != f_two(cell) for cell in cells)
    one_unbalanced = sum(unbalanced_axis_count(cell) == 1 for cell in cells)
    print(f"f_L1_f_two_disagree={disagree}")
    checks.check(
        "class-split-is-exactly-one-unbalanced-axis",
        disagree == one_unbalanced and disagree > 0,
        f"disagree={disagree}",
    )
    checks.check(
        "split-cells-are-L1-form-and-f_two-absent",
        all(
            (f_l1(cell) == 1 and f_two(cell) == 0) if unbalanced_axis_count(cell) == 1 else True
            for cell in cells
        ),
    )

    checks.check("note-reports-N_orb", f"N_orb = {n_orb}" in note)
    checks.check("note-reports-class-size", f"|F_G| = {class_size}" in note)
    checks.check("note-reports-disagreement", f"disagree on exactly {disagree} cells" in note)
    checks.check(
        "note-claim-scope-class-not-law",
        "cube-covariant boolean formation predicates form a set of size" in normalized_note
        and "No physical law is adopted" in note,
    )
    checks.check(
        "note-does-not-adopt-a-member",
        "does not adopt" in normalized_note and "one element" in normalized_note,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "new axiom")
    checks.check(
        "forbidden-phrase-hygiene",
        all(phrase not in note for phrase in forbidden),
        ",".join(phrase for phrase in forbidden if phrase in note),
    )
    checks.check(
        "no-runner-cache-or-citation-manifest",
        "runner-cache" not in note and "citation_manifest" not in note and "CITATION_MANIFEST" not in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
