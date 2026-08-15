#!/usr/bin/env python3
"""Display one cube-covariant formation member inequivalent to L1.

The paired note is
docs/TWO_AXIS_UNBALANCED_FORMATION_MEMBER_BOUNDED_THEOREM_NOTE_2026-08-15.md.

Objects: occupancy 6-tuples on the six directed nearest-neighbor slots,
the 24 proper cube rotations, and the displayed twelve-vertex two-cube
with seed (0,0,0) and off-patch occupancy 0. The two-axis predicate is
displayed, not adopted. No axiom sentence is written. No cache is written.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_UNBALANCED_FORMATION_MEMBER_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_UNBALANCED_FORMATION_MEMBER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED = (0, 0, 0)
OFF_PATCH = 0


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
    return tuple(sorted(set(mats)))


def matvec(
    matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def slot_permutation(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(SLOT_INDEX[matvec(matrix, slot)] for slot in SLOTS)


def apply_perm(cell: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for source, dest in enumerate(perm):
        out[dest] = cell[source]
    return tuple(out)


def all_cells() -> tuple[tuple[int, ...], ...]:
    return tuple(product((0, 1), repeat=6))


def unbalanced_axis_count(cell: tuple[int, ...]) -> int:
    return sum(cell[plus] != cell[minus] for plus, minus in AXIS_PAIRS)


def imbalance(cell: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(cell[plus] - cell[minus] for plus, minus in AXIS_PAIRS)


def f_l1(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 1)


def f_two(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 2)


def is_covariant(func, perms: tuple[tuple[int, ...], ...]) -> bool:
    for cell in all_cells():
        value = func(cell)
        for perm in perms:
            if func(apply_perm(cell, perm)) != value:
                return False
    return True


def gf2_add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % 2 for a, b in zip(left, right, strict=True))


def two_cube_patch() -> frozenset[tuple[int, int, int]]:
    cube_a = product((0, 1), (0, 1), (0, 1))
    cube_b = product((1, 2), (0, 1), (0, 1))
    return frozenset(cube_a) | frozenset(cube_b)


def occupancy(
    site: tuple[int, int, int],
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> int:
    if site in locked:
        return 1
    if site not in patch:
        return OFF_PATCH
    return 0


def neighbor_cell(
    site: tuple[int, int, int],
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> tuple[int, ...]:
    return tuple(
        occupancy(
            (site[0] + slot[0], site[1] + slot[1], site[2] + slot[2]),
            locked,
            patch,
        )
        for slot in SLOTS
    )


def first_wave(
    func,
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> frozenset[tuple[int, int, int]]:
    return frozenset(
        site
        for site in patch
        if site not in locked and func(neighbor_cell(site, locked, patch)) == 1
    )


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

    print("Two-axis unbalanced formation member versus L1")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: displayed f_two on 64 cells and the two-cube first wave; not adopted")

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
    checks.check(
        "cells-are-binary-6-tuples",
        all(len(cell) == 6 and set(cell) <= {0, 1} for cell in cells),
    )

    rotations = proper_rotation_matrices()
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    inversion = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    rotation_set = set(rotations)
    checks.check("rotation-count-24", len(rotations) == 24)
    checks.check("rotations-include-identity", identity in rotation_set)
    checks.check("rotations-exclude-inversion", inversion not in rotation_set)
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
    checks.check(
        "slot-permutations-are-bijections",
        all(sorted(perm) == list(range(6)) for perm in perms),
    )

    u_values = tuple(unbalanced_axis_count(cell) for cell in cells)
    checks.check("u-range-is-0-to-3", set(u_values) == {0, 1, 2, 3})
    checks.check(
        "u-invariant-under-rotations",
        all(
            unbalanced_axis_count(apply_perm(cell, perm)) == unbalanced_axis_count(cell)
            for cell in cells
            for perm in perms
        ),
    )
    checks.check("f_two-cube-covariant", is_covariant(f_two, perms))
    checks.check("f_L1-cube-covariant", is_covariant(f_l1, perms))
    checks.check(
        "f_L1-is-n-nonzero",
        all(f_l1(cell) == int(any(component != 0 for component in imbalance(cell))) for cell in cells),
    )
    checks.check(
        "f_two-is-not-n-nonzero",
        any(f_two(cell) != int(any(component != 0 for component in imbalance(cell))) for cell in cells),
    )

    disagree_cells = tuple(cell for cell in cells if f_l1(cell) != f_two(cell))
    one_unbalanced = tuple(cell for cell in cells if unbalanced_axis_count(cell) == 1)
    combo_count = 3 * 2 * 2 * 2
    print(f"disagree_count={len(disagree_cells)}")
    print(f"one_unbalanced_count={len(one_unbalanced)}")
    print(f"combo_count={combo_count}")
    checks.check(
        "disagreement-is-exactly-one-unbalanced-axis",
        set(disagree_cells) == set(one_unbalanced),
        f"disagree={len(disagree_cells)}",
    )
    checks.check(
        "disagreement-count-matches-axis-combo",
        len(disagree_cells) == combo_count == len(one_unbalanced),
        f"count={len(disagree_cells)}",
    )
    checks.check("disagreement-at-least-one", len(disagree_cells) >= 1)
    checks.check(
        "split-cells-are-L1-form-and-f_two-absent",
        all(f_l1(cell) == 1 and f_two(cell) == 0 for cell in one_unbalanced),
    )

    axis_unit = []
    for plus, _minus in AXIS_PAIRS:
        unit = [0] * 6
        unit[plus] = 1
        axis_unit.append(tuple(unit))
    gf2_additivity_fails = any(
        f_two(left) == 0
        and f_two(right) == 0
        and f_two(gf2_add(left, right)) == 1
        for left, right in zip(axis_unit, axis_unit[1:], strict=False)
    )
    checks.check("f_two-not-linear-over-GF2", gf2_additivity_fails)

    patch = two_cube_patch()
    locked = frozenset({SEED})
    axis_sites = frozenset(
        (SEED[0] + slot[0], SEED[1] + slot[1], SEED[2] + slot[2])
        for slot in SLOTS
        if (SEED[0] + slot[0], SEED[1] + slot[1], SEED[2] + slot[2]) in patch
    )
    l1_wave = first_wave(f_l1, locked, patch)
    two_wave = first_wave(f_two, locked, patch)
    axis_u = {site: unbalanced_axis_count(neighbor_cell(site, locked, patch)) for site in axis_sites}
    print(f"two_cube_sites={len(patch)}")
    print(f"L1_first_wave={sorted(l1_wave)}")
    print(f"f_two_first_wave={sorted(two_wave)}")
    print(f"axis_u={axis_u}")

    checks.check("two-cube-has-twelve-sites", len(patch) == 12)
    checks.check("seed-is-on-patch", SEED in patch)
    checks.check("L1-first-wave-is-three-axis-sites", l1_wave == axis_sites and len(axis_sites) == 3)
    checks.check("axis-sites-have-u-one", set(axis_u.values()) == {1})
    checks.check("f_two-first-wave-empty", two_wave == frozenset())
    checks.check("members-inequivalent-as-occupancy-lock-steps", l1_wave != two_wave)

    checks.check(
        "note-reports-disagreement-count",
        f"disagree on exactly {len(disagree_cells)} cells" in note,
    )
    checks.check(
        "note-reports-combo-identity",
        f"3 × 2 × 2 × 2 = {combo_count}" in note,
    )
    checks.check(
        "note-claim-scope-displayed-not-adopted",
        "inequivalent to L1" in normalized_note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "note-does-not-adopt-the-member",
        "does not adopt" in normalized_note and "not adopted" in normalized_note,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "new axiom")
    checks.check(
        "forbidden-phrase-hygiene",
        all(phrase not in note for phrase in forbidden),
        ",".join(phrase for phrase in forbidden if phrase in note),
    )
    checks.check(
        "no-runner-cache-or-citation-manifest",
        "runner-cache" not in note
        and "citation_manifest" not in note
        and "CITATION_MANIFEST" not in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
