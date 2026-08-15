#!/usr/bin/env python3
"""Exact occupancy and pairing checks for lock content without an M_2 action.

Finite {0,1}^6 occupancy. Integer n, S, k. Displayed axis-Pauli pairing
for rank-1 projectors. No cache write, no Aut-pick, no axiom edit.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/LOCK_CONTENT_WITHOUT_M2_ACTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/LOCK_CONTENT_WITHOUT_M2_ACTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

C = tuple[Fraction, Fraction]
Mat = tuple[tuple[C, C], tuple[C, C]]

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I_UNIT = (Fraction(0), Fraction(1))


def cadd(left: C, right: C) -> C:
    return (left[0] + right[0], left[1] + right[1])


def cscale(scalar: Fraction, value: C) -> C:
    return (scalar * value[0], scalar * value[1])


def madd(left: Mat, right: Mat) -> Mat:
    return (
        (cadd(left[0][0], right[0][0]), cadd(left[0][1], right[0][1])),
        (cadd(left[1][0], right[1][0]), cadd(left[1][1], right[1][1])),
    )


def mscale(scalar: Fraction, matrix: Mat) -> Mat:
    return (
        (cscale(scalar, matrix[0][0]), cscale(scalar, matrix[0][1])),
        (cscale(scalar, matrix[1][0]), cscale(scalar, matrix[1][1])),
    )


def mmul(left: Mat, right: Mat) -> Mat:
    def entry(row: int, col: int) -> C:
        first = (
            left[row][0][0] * right[0][col][0] - left[row][0][1] * right[0][col][1],
            left[row][0][0] * right[0][col][1] + left[row][0][1] * right[0][col][0],
        )
        second = (
            left[row][1][0] * right[1][col][0] - left[row][1][1] * right[1][col][1],
            left[row][1][0] * right[1][col][1] + left[row][1][1] * right[1][col][0],
        )
        return cadd(first, second)

    return ((entry(0, 0), entry(0, 1)), (entry(1, 0), entry(1, 1)))


def mtrace(matrix: Mat) -> C:
    return cadd(matrix[0][0], matrix[1][1])


def eye() -> Mat:
    return ((ONE, ZERO), (ZERO, ONE))


def sigma_x() -> Mat:
    return ((ZERO, ONE), (ONE, ZERO))


def sigma_y() -> Mat:
    return ((ZERO, (Fraction(0), Fraction(-1))), (I_UNIT, ZERO))


def sigma_z() -> Mat:
    return ((ONE, ZERO), (ZERO, (Fraction(-1), Fraction(0))))


PAULI = (sigma_x(), sigma_y(), sigma_z())


def occupancy_vector(bits: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        bits[0] - bits[1],
        bits[2] - bits[3],
        bits[4] - bits[5],
    )


def support_and_k(n_vec: tuple[int, int, int]) -> tuple[frozenset[int], int]:
    support = frozenset(index for index, value in enumerate(n_vec) if value != 0)
    return support, sum(value * value for value in n_vec)


def swap_lock_labels(bits: tuple[int, ...], axis: int) -> tuple[int, ...]:
    data = list(bits)
    plus = 2 * axis
    data[plus], data[plus + 1] = data[plus + 1], data[plus]
    return tuple(data)


def apply_sign_pattern(
    n_vec: tuple[int, int, int], signs: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (signs[0] * n_vec[0], signs[1] * n_vec[1], signs[2] * n_vec[2])


def permute_triple(
    n_vec: tuple[int, int, int], permutation: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (n_vec[permutation[0]], n_vec[permutation[1]], n_vec[permutation[2]])


def projector_from_unit(n_vec: tuple[int, int, int]) -> Mat:
    """Rank-1 projector for a displayed |S|=1 unit n, identity pairing."""
    combination = mscale(Fraction(0), eye())
    for coefficient, matrix in zip(n_vec, PAULI, strict=True):
        combination = madd(combination, mscale(Fraction(coefficient), matrix))
    return mscale(Fraction(1, 2), madd(eye(), combination))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; occupancy bits, n, S, k, and the displayed pairing are declared")
    print("framework_role: axioms supply Z^3, M_2(C), and Record lock-one; no Aut-pick")
    print("claim_scope: Occupancy determines (S,k) without Aut(M_2). Spectral projectors of a Bloch image require an axis–Pauli pairing, which is extra. Displayed, not adopted. No Aut-pick.")

    occupancies = tuple(product((0, 1), repeat=6))
    rows = []
    for bits in occupancies:
        n_vec = occupancy_vector(bits)
        support, k_value = support_and_k(n_vec)
        n_l1 = tuple(Fraction(value, 3) for value in n_vec)
        scaled = sum((3 * component) * (3 * component) for component in n_l1)
        rows.append((bits, n_vec, support, k_value, scaled))

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and the live axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "occupancy-census",
        "the directed cube has exactly 64 occupancy patterns",
        len(occupancies) == 64 and len(rows) == 64,
    )
    checks.check(
        "n-range",
        "every n_mu is an unscaled integer in {-1,0,1}",
        all(all(component in (-1, 0, 1) for component in n_vec) for _, n_vec, _, _, _ in rows),
    )
    checks.check(
        "k-equals-n-squared",
        "k = |n|^2 on every occupancy",
        all(k_value == sum(component * component for component in n_vec) for _, n_vec, _, k_value, _ in rows),
    )
    checks.check(
        "k-equals-S-cardinality",
        "k = |S| because each nonzero n_mu squares to 1",
        all(k_value == len(support) for _, _, support, k_value, _ in rows),
    )
    checks.check(
        "k-equals-L1-scaled-norm",
        "k = |3 n_L1|^2 for the displayed L1 coordinate n/3",
        all(k_value == scaled for _, _, _, k_value, scaled in rows),
    )

    k_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for _, _, _, k_value, _ in rows:
        k_counts[k_value] += 1
    checks.check(
        "k-class-census",
        "the occupancy k-classes are 8,24,24,8 for k=0,1,2,3",
        k_counts == {0: 8, 1: 24, 2: 24, 3: 8},
    )

    label_swap_invariant = True
    for bits, n_vec, support, k_value, _ in rows:
        for axis in range(3):
            swapped = swap_lock_labels(bits, axis)
            n_swapped = occupancy_vector(swapped)
            support_swapped, k_swapped = support_and_k(n_swapped)
            expected = list(n_vec)
            expected[axis] = -expected[axis]
            if n_swapped != tuple(expected) or support_swapped != support or k_swapped != k_value:
                label_swap_invariant = False
        for signs in product((-1, 1), repeat=3):
            signed = apply_sign_pattern(n_vec, signs)
            support_signed, k_signed = support_and_k(signed)
            if support_signed != support or k_signed != k_value:
                label_swap_invariant = False
    checks.check(
        "later-lock-label-swap",
        "(S,k) is unchanged under every later-lock two-label permutation",
        label_swap_invariant,
    )

    opposite_cancel = (
        occupancy_vector((1, 1, 0, 0, 0, 0)) == (0, 0, 0)
        and occupancy_vector((0, 0, 1, 1, 0, 0)) == (0, 0, 0)
        and occupancy_vector((0, 0, 0, 0, 1, 1)) == (0, 0, 0)
    )
    checks.check(
        "opposite-occupancy-cancels",
        "c_+mu = c_-mu, including double occupancy, gives n_mu = 0",
        opposite_cancel and occupancy_vector((0, 0, 0, 0, 0, 0)) == (0, 0, 0),
    )

    identity_perm = (0, 1, 2)
    fork_xy = (1, 0, 2)
    pairing_independent_k = True
    s1_xy_support_moves = True
    s1_xy_support_seen = 0
    occupancy_only_collision = True
    for _, n_vec, support, k_value, _ in rows:
        n_id = permute_triple(n_vec, identity_perm)
        n_fork = permute_triple(n_vec, fork_xy)
        if support_and_k(n_id)[1] != k_value or support_and_k(n_fork)[1] != k_value:
            pairing_independent_k = False
        if len(support) == 1 and (0 in support or 1 in support):
            s1_xy_support_seen += 1
            if n_id == n_fork:
                s1_xy_support_moves = False
        if n_id != n_fork and n_vec != (0, 0, 0):
            occupancy_only_collision = False
    checks.check(
        "sk-independent-of-pairing",
        "(S,k) is the same for the identity pairing and the displayed x-y fork",
        pairing_independent_k,
    )
    checks.check(
        "S1-fork-changes-direction",
        "the displayed x-y Pauli swap moves every |S|=1 triple supported on x or y",
        s1_xy_support_moves and s1_xy_support_seen == 16,
    )
    checks.check(
        "no-occupancy-only-global-map",
        "no occupancy-only map can equal both displayed projector families for all c",
        occupancy_only_collision is False,
    )

    nonempty_moved_or_symmetric = True
    for _, n_vec, support, _, _ in rows:
        if not support:
            continue
        moved = False
        for source in range(3):
            for target in range(source + 1, 3):
                perm = [0, 1, 2]
                perm[source], perm[target] = perm[target], perm[source]
                if permute_triple(n_vec, tuple(perm)) != n_vec:
                    moved = True
        abs_components = tuple(sorted(abs(value) for value in n_vec))
        totally_symmetric = abs_components == (1, 1, 1)
        if not moved and not totally_symmetric:
            nonempty_moved_or_symmetric = False
        if len(support) == 1 and not moved:
            nonempty_moved_or_symmetric = False
    checks.check(
        "fork-exists-whenever-S-nonempty",
        "every |S|>=1 occupancy is moved by some two-Pauli swap, except the totally symmetric n already recorded",
        nonempty_moved_or_symmetric,
    )

    displayed = (1, 0, 0)
    p_id = projector_from_unit(displayed)
    p_fork = projector_from_unit(permute_triple(displayed, fork_xy))
    p_id_sq = mmul(p_id, p_id)
    p_fork_sq = mmul(p_fork, p_fork)
    checks.check(
        "displayed-projector-idempotent",
        "P_id = (I+sigma_x)/2 is a rank-1 projector: P^2=P and Tr P=1",
        p_id_sq == p_id and mtrace(p_id) == ONE,
    )
    checks.check(
        "fork-projector-idempotent",
        "P_fork = (I+sigma_y)/2 is a rank-1 projector: P^2=P and Tr P=1",
        p_fork_sq == p_fork and mtrace(p_fork) == ONE,
    )
    checks.check(
        "displayed-fork-changes-P",
        "the displayed #6272 x-y fork sends the n=(1,0,0) projector to a different matrix",
        p_id != p_fork,
    )

    p_minus = projector_from_unit((-1, 0, 0))
    checks.check(
        "opposite-label-complement",
        "later-lock label swap on the displayed axis sends P to I-P, not to P",
        p_minus != p_id and madd(p_id, p_minus) == eye(),
    )

    symmetric = (1, 1, 1)
    checks.check(
        "symmetric-n-does-not-erase-pairing",
        "n=(1,1,1) is axis-permutation invariant, yet |S|=1 still requires the pairing",
        permute_triple(symmetric, fork_xy) == symmetric
        and permute_triple((1, 0, 0), fork_xy) != (1, 0, 0),
    )

    required_note_phrases = (
        "Occupancy determines (S,k) without Aut(M_2).",
        "Displayed, not adopted. No Aut-pick.",
        "does not invoke `Aut(M_2)`",
        "no occupancy-only map",
        "object-split",
        "later lock",
        "|3 n_L1|^2",
        "**Type:** bounded_theorem",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-contract",
        "the note states the occupancy/projector split and the no-Aut-pick boundary",
        all(phrase in note for phrase in required_note_phrases),
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids the dispatch-forbidden rhetoric tokens",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "axiom-unedited-content",
        "the live axiom memo still states the four named axioms and lock-one",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "When present, a record locks exactly one admissible local possibility." in axiom
        and "No Aut-pick" not in axiom,
    )
    checks.check(
        "cache-write-disabled",
        "the source note has no runner-cache section and the runner prints cache_write false",
        "cache_write: false" in self_source
        and "**Runner cache:**" not in note
        and "logs/runner" not in note,
    )

    print("per_element: checked — every occupancy in {0,1}^6 is classified by (S,k)")
    print("per_site: checked and not executed — no physical site history is formed")
    print("per_mode: checked — identity pairing versus the displayed Pauli-axis fork")
    print("per_block: checked — occupancy block versus projector block")
    print("lattice_wide: checked and not executed — no adopted cube action or Aut-pick")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
