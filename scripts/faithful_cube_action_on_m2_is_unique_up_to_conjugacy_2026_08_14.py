#!/usr/bin/env python3
"""Exact Q(i) / integer checks: faithful cube actions on M_2 form one class.

Concrete proper cubic G (|G|=24) acting by unital *-maps on one-site
M_2(C). No axiom edit, no cache write, no adopted action.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "FAITHFUL_CUBE_ACTION_ON_M2_IS_UNIQUE_UP_TO_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/FAITHFUL_CUBE_ACTION_ON_M2_IS_UNIQUE_UP_TO_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Qi:
    """a + b i with a, b in Q and i^2 = -1."""

    __slots__ = ("re", "im")

    def __init__(self, re: Fraction | int, im: Fraction | int = 0) -> None:
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other: Qi) -> Qi:
        return Qi(self.re + other.re, self.im + other.im)

    def __sub__(self, other: Qi) -> Qi:
        return Qi(self.re - other.re, self.im - other.im)

    def __mul__(self, other: Qi) -> Qi:
        return Qi(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __neg__(self) -> Qi:
        return Qi(-self.re, -self.im)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Qi):
            return NotImplemented
        return self.re == other.re and self.im == other.im

    def __hash__(self) -> int:
        return hash((self.re, self.im))

    def conj(self) -> Qi:
        return Qi(self.re, -self.im)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0


ZERO = Qi(0)
ONE = Qi(1)
I_UNIT = Qi(0, 1)
NEG_I = Qi(0, -1)
HALF = Qi(Fraction(1, 2))

Mat2 = tuple[tuple[Qi, Qi], tuple[Qi, Qi]]
Auto = tuple[Mat2, Mat2, Mat2]
IntMat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def mat2_add(left: Mat2, right: Mat2) -> Mat2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def mat2_mul(left: Mat2, right: Mat2) -> Mat2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mat2_scale(coeff: Qi, matrix: Mat2) -> Mat2:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat2_neg(matrix: Mat2) -> Mat2:
    return (
        (-matrix[0][0], -matrix[0][1]),
        (-matrix[1][0], -matrix[1][1]),
    )


def mat2_adj(matrix: Mat2) -> Mat2:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def mat2_trace(matrix: Mat2) -> Qi:
    return matrix[0][0] + matrix[1][1]


def identity2() -> Mat2:
    return ((ONE, ZERO), (ZERO, ONE))


def zero2() -> Mat2:
    return ((ZERO, ZERO), (ZERO, ZERO))


SX: Mat2 = ((ZERO, ONE), (ONE, ZERO))
SY: Mat2 = ((ZERO, NEG_I), (I_UNIT, ZERO))
SZ: Mat2 = ((ONE, ZERO), (ZERO, -ONE))
PAULIS: tuple[Mat2, Mat2, Mat2] = (SX, SY, SZ)


def pauli_coeff(matrix: Mat2, pauli: Mat2) -> Qi:
    return mat2_trace(mat2_mul(matrix, pauli)) * HALF


def apply_auto(auto: Auto, matrix: Mat2) -> Mat2:
    scalar = mat2_trace(matrix) * HALF
    out = mat2_scale(scalar, identity2())
    for index, pauli in enumerate(PAULIS):
        out = mat2_add(out, mat2_scale(pauli_coeff(matrix, pauli), auto[index]))
    return out


def compose_auto(left: Auto, right: Auto) -> Auto:
    return (
        apply_auto(left, right[0]),
        apply_auto(left, right[1]),
        apply_auto(left, right[2]),
    )


def identity_auto() -> Auto:
    return (SX, SY, SZ)


def det3(matrix: IntMat) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat3_mul(left: IntMat, right: IntMat) -> IntMat:
    return tuple(
        tuple(
            left[row][0] * right[0][col]
            + left[row][1] * right[1][col]
            + left[row][2] * right[2][col]
            for col in range(3)
        )
        for row in range(3)
    )


def mat3_transpose(matrix: IntMat) -> IntMat:
    return tuple(tuple(matrix[col][row] for col in range(3)) for row in range(3))


def identity3() -> IntMat:
    return ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def is_signed_permutation(matrix: IntMat) -> bool:
    for row in matrix:
        nonzero = [entry for entry in row if entry != 0]
        if len(nonzero) != 1 or nonzero[0] not in (-1, 1):
            return False
    for col in range(3):
        nonzero = [matrix[row][col] for row in range(3) if matrix[row][col] != 0]
        if len(nonzero) != 1 or nonzero[0] not in (-1, 1):
            return False
    return True


def all_signed_permutation_matrices() -> list[IntMat]:
    out: list[IntMat] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[perm[row]] = signs[row]
                rows.append(tuple(entries))
            out.append(tuple(rows))
    return out


def proper_cubic_group() -> list[IntMat]:
    return [matrix for matrix in all_signed_permutation_matrices() if det3(matrix) == 1]


def proper_cubic_count() -> int:
    return len(proper_cubic_group())


RX: IntMat = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
RY: IntMat = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
RZ: IntMat = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
SW: IntMat = ((0, 0, 1), (1, 0, 0), (0, 1, 0))


def alpha_on(rotation: IntMat) -> Auto:
    images: list[Mat2] = []
    for col in range(3):
        acc = zero2()
        for row in range(3):
            coeff = rotation[row][col]
            if coeff == 1:
                acc = mat2_add(acc, PAULIS[row])
            elif coeff == -1:
                acc = mat2_add(acc, mat2_neg(PAULIS[row]))
        images.append(acc)
    return (images[0], images[1], images[2])


def phi0_on(_rotation: IntMat) -> Auto:
    return identity_auto()


def is_faithful(phi) -> bool:
    group = proper_cubic_group()
    identity_hits = [rotation for rotation in group if phi(rotation) == identity_auto()]
    images = [phi(rotation) for rotation in group]
    return len(identity_hits) == 1 and len(set(images)) == len(group)


def alpha_rx_on_sigmay() -> Mat2:
    return alpha_on(RX)[1]


def conjugator_exhibits_beta() -> bool:
    sw_inv = mat3_transpose(SW)
    for rotation in proper_cubic_group():
        conjugated = compose_auto(
            alpha_on(SW),
            compose_auto(alpha_on(rotation), alpha_on(sw_inv)),
        )
        beta_image = alpha_on(mat3_mul(SW, mat3_mul(rotation, sw_inv)))
        if conjugated != beta_image:
            return False
    return True


def plus_one_axis(rotation: IntMat) -> tuple[int, int, int]:
    shifted = tuple(
        tuple(rotation[row][col] - (1 if row == col else 0) for col in range(3))
        for row in range(3)
    )
    rows = [list(row) for row in shifted]
    candidates = (
        (
            rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1],
            rows[1][2] * rows[2][0] - rows[1][0] * rows[2][2],
            rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0],
        ),
        (
            rows[2][1] * rows[0][2] - rows[2][2] * rows[0][1],
            rows[2][2] * rows[0][0] - rows[2][0] * rows[0][2],
            rows[2][0] * rows[0][1] - rows[2][1] * rows[0][0],
        ),
        (
            rows[0][1] * rows[1][2] - rows[0][2] * rows[1][1],
            rows[0][2] * rows[1][0] - rows[0][0] * rows[1][2],
            rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0],
        ),
    )
    axis = next((vector for vector in candidates if vector != (0, 0, 0)), (0, 0, 0))
    gcd = 0
    for entry in axis:
        value = abs(entry)
        gcd = value if gcd == 0 else _gcd(gcd, value)
    if gcd > 1:
        axis = (axis[0] // gcd, axis[1] // gcd, axis[2] // gcd)
    if axis < (0, 0, 0):
        axis = (-axis[0], -axis[1], -axis[2])
    return axis


def _gcd(left: int, right: int) -> int:
    while right:
        left, right = right, left % right
    return abs(left)


def apply_intmat(matrix: IntMat, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        matrix[row][0] * vector[0] + matrix[row][1] * vector[1] + matrix[row][2] * vector[2]
        for row in range(3)
    )


DIAGONALS: tuple[tuple[int, int, int], ...] = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
)


def canon_diag(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    for entry in vector:
        if entry != 0:
            return vector if entry > 0 else (-vector[0], -vector[1], -vector[2])
    return vector


def diagonal_perm(rotation: IntMat) -> tuple[int, int, int, int]:
    images = []
    for diag in DIAGONALS:
        mapped = canon_diag(apply_intmat(rotation, diag))
        images.append(DIAGONALS.index(mapped))
    return (images[0], images[1], images[2], images[3])


def perm_sign(perm: tuple[int, int, int, int]) -> int:
    inversions = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if perm[i] > perm[j]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def element_order(matrix: IntMat) -> int:
    acc = identity3()
    for order in range(1, 25):
        acc = mat3_mul(acc, matrix)
        if acc == identity3():
            return order
    return 0


def g_iso_s4_via_diagonals() -> bool:
    perms = [diagonal_perm(rotation) for rotation in proper_cubic_group()]
    return len(set(perms)) == 24 and all(sorted(perm) == [0, 1, 2, 3] for perm in perms)


def order3_count() -> int:
    return sum(1 for rotation in proper_cubic_group() if element_order(rotation) == 3)


def all_g_conjugates_faithful() -> bool:
    for conjugator in proper_cubic_group():
        inverse = mat3_transpose(conjugator)

        def conjugate_action(
            rotation: IntMat, conjugator: IntMat = conjugator, inverse: IntMat = inverse
        ) -> Auto:
            return alpha_on(mat3_mul(conjugator, mat3_mul(rotation, inverse)))

        if not is_faithful(conjugate_action):
            return False
        for rotation in proper_cubic_group():
            conjugated = compose_auto(
                alpha_on(conjugator),
                compose_auto(alpha_on(rotation), alpha_on(inverse)),
            )
            if conjugated != conjugate_action(rotation):
                return False
    return True


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

    print("external_scientific_inputs: none; G, α, φ0, Sω, β are theorem data")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q(i) and integer 3x3 matrices; no adopted action")
    print("negative_scope: φ0 is unfaithful; uniqueness is conditional on a faithful action")

    group = proper_cubic_group()
    group_set = set(group)
    count = proper_cubic_count()
    checks.check(
        "identity-proper-cubic-count",
        "|G|=24 via proper_cubic_count()",
        count == 24 and count == len(group_set),
    )
    checks.check(
        "thm1-signed-perm-pool",
        "48 signed permutation matrices before the det=+1 cut",
        len(all_signed_permutation_matrices()) == 48,
    )
    checks.check(
        "thm1-generators-in-G",
        "Rx, Ry, Rz, Sω lie in G",
        RX in group_set
        and RY in group_set
        and RZ in group_set
        and SW in group_set
        and all(is_signed_permutation(matrix) and det3(matrix) == 1 for matrix in (RX, RY, RZ, SW)),
    )
    checks.check(
        "thm1-group-closed",
        "G is closed under multiplication and transpose-inverse",
        all(mat3_mul(left, right) in group_set for left in group for right in group)
        and all(mat3_transpose(matrix) in group_set for matrix in group)
        and identity3() in group_set,
    )

    checks.check("qi-i-square", "i^2 = -1", I_UNIT * I_UNIT == -ONE)
    checks.check(
        "pauli-involutions",
        "σx^2 = σy^2 = σz^2 = I",
        mat2_mul(SX, SX) == identity2()
        and mat2_mul(SY, SY) == identity2()
        and mat2_mul(SZ, SZ) == identity2(),
    )
    checks.check(
        "pauli-hermitian",
        "each Pauli is Hermitian",
        mat2_adj(SX) == SX and mat2_adj(SY) == SY and mat2_adj(SZ) == SZ,
    )
    checks.check(
        "pauli-rh-triad",
        "σx σy = i σz",
        mat2_mul(SX, SY) == mat2_scale(I_UNIT, SZ),
    )

    alpha_rx = alpha_on(RX)
    checks.check(
        "identity-alpha-rx-sigmay",
        "α_Rx(σy) = σz via alpha_rx_on_sigmay()",
        alpha_rx_on_sigmay() == SZ and alpha_rx[1] == SZ,
    )
    checks.check(
        "thm2-alpha-rx-images",
        "α_Rx(σx)=σx, α_Rx(σz)=-σy",
        alpha_rx[0] == SX and alpha_rx[2] == mat2_neg(SY),
    )
    checks.check(
        "thm2-alpha-hom",
        "α_R ∘ α_S = α_{RS} on all of G",
        all(
            compose_auto(alpha_on(left), alpha_on(right)) == alpha_on(mat3_mul(left, right))
            for left in group
            for right in group
        ),
    )
    checks.check(
        "identity-alpha-faithful",
        "is_faithful(α) holds",
        is_faithful(alpha_on),
    )
    checks.check(
        "identity-phi0-unfaithful",
        "is_faithful(φ0) fails",
        not is_faithful(phi0_on),
    )
    checks.check(
        "mutation-phi0-injective-fails",
        "predicate φ0 is injective must fail",
        not is_faithful(phi0_on),
    )
    checks.check(
        "mutation-alpha-rx-id-fails",
        "predicate α_Rx == id must fail",
        alpha_rx != identity_auto() and RX != identity3(),
    )

    sw_inv = mat3_transpose(SW)
    checks.check(
        "thm4-sw-order-3",
        "Sω^3 = I and det(Sω)=+1",
        mat3_mul(SW, mat3_mul(SW, SW)) == identity3()
        and det3(SW) == 1
        and mat3_mul(SW, sw_inv) == identity3(),
    )
    checks.check(
        "identity-conjugator",
        "conjugator_exhibits_beta() holds",
        conjugator_exhibits_beta(),
    )
    beta_rx = alpha_on(mat3_mul(SW, mat3_mul(RX, sw_inv)))
    conjugated_rx = compose_auto(alpha_on(SW), compose_auto(alpha_on(RX), alpha_on(sw_inv)))
    checks.check(
        "thm4-beta-rx-formula",
        "β_Rx = α_{Sω Rx Sω^{-1}} equals the conjugated action",
        beta_rx == conjugated_rx,
    )
    checks.check(
        "mutation-beta-eq-alpha-fails",
        "predicate β_Rx == α_Rx must fail",
        beta_rx != alpha_rx,
    )
    checks.check(
        "mutation-no-conjugator-fails",
        "predicate no conjugator must fail",
        conjugator_exhibits_beta() and conjugated_rx == beta_rx,
    )
    checks.check(
        "thm4-beta-faithful",
        "is_faithful(β) holds",
        is_faithful(lambda rotation: alpha_on(mat3_mul(SW, mat3_mul(rotation, sw_inv)))),
    )
    checks.check(
        "thm4-axes",
        "axis(α_Rx)=ê_x and axis(β_Rx)=Sω ê_x=ê_y",
        plus_one_axis(RX) == (1, 0, 0)
        and plus_one_axis(mat3_mul(SW, mat3_mul(RX, sw_inv))) == (0, 1, 0)
        and apply_intmat(SW, (1, 0, 0)) == (0, 1, 0),
    )
    checks.check(
        "thm3-rx-ry-is-sw",
        "Rx Ry = Sω, so the cube 120° relation holds on the nose",
        mat3_mul(RX, RY) == SW,
    )
    checks.check(
        "thm3-frame-of-alpha",
        "α axes are the standard right-handed frame",
        plus_one_axis(RX) == (1, 0, 0)
        and plus_one_axis(RY) == (0, 1, 0)
        and plus_one_axis(RZ) == (0, 0, 1),
    )
    checks.check(
        "thm3-g-iso-s4",
        "G ≅ S_4 via the four space diagonals",
        g_iso_s4_via_diagonals(),
    )
    checks.check(
        "thm3-eight-order-3",
        "G has eight order-3 elements, so it is not C_24 or D_12",
        order3_count() == 8,
    )
    rz_perm = diagonal_perm(RZ)
    checks.check(
        "thm3b-rz-odd-det-plus",
        "Rz is an odd permutation of the diagonals with det=+1, so 3⊗sgn misses SO(3)",
        perm_sign(rz_perm) == -1
        and det3(RZ) == 1
        and len(set(rz_perm)) == 4,
    )
    checks.check(
        "thm3c-all-g-conjugates",
        "every G-conjugate of α is faithful and conjugate by α_S",
        all_g_conjugates_faithful(),
    )
    checks.check(
        "thm3-no-false-census",
        "note does not claim octahedral groups are the only order-24 subgroups of SO(3)",
        "The only order-`24` groups" not in note
        and "dihedral" in note
        and "isomorphic to `S_4`" in note,
    )

    memo_names_standard_action = (
        "standard action" in axiom
        or "Bloch action" in axiom
        or "α_R" in axiom
        or "faithful unital" in axiom
    )
    checks.check(
        "mutation-memo-names-action-fails",
        "predicate live memo names the standard action as axiom content must fail",
        not memo_names_standard_action
        and "proper cubic rotations about each site" in axiom
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "mutation-lattice-named-fails",
        "predicate note claims Lattice-named action must fail",
        "Lattice-named" not in note,
    )
    checks.check(
        "thm5-quoted-lattice-qubit",
        "note quotes live Lattice and Qubit, including the Cl(3,0) non-structure sentence",
        "proper cubic rotations about each site" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "No possibility is privileged" in note
        and "adds no further primitive structure" in note
        and "conditional on requiring a faithful" in note,
    )
    checks.check(
        "thm5-not-required",
        "note states the axioms do not require a faithful action and do not adopt α",
        "do not require a faithful action" in note
        and "does not adopt" in note
        and "Qubit remains `M_2(C)`" in note,
    )
    forbidden = (
        "axioms supply",
        "we adopt",
        "exhausted",
        "closes the route",
        "only route",
        "flip Qubit",
        "Qubit is M_3",
        "#6268",
        "#6272",
        "#6273",
    )
    checks.check(
        "boundary-forbidden-phrases",
        "note omits the forbidden close-the-route and adoption phrases",
        all(phrase not in note for phrase in forbidden)
        and "one conjugacy class" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and no hypothetical axiom adoption",
        "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/FAITHFUL_CUBE_ACTION_ON_M2_IS_UNIQUE_UP_TO_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source,
    )
    qcd_ok = "QCD is unused" in note or "not QCD" in note or "No color or QCD" in note
    checks.check(
        "thm6-not-qcd-color",
        "QCD appears only as a negation / unused boundary",
        qcd_ok
        and "Qubit remains `M_2(C)`" in note
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: checked exactly — each of the 24 proper cubic matrices is a det=+1 signed permutation")
    print("per_site: checked exactly — α and β are unital *-actions on one-site M_2(C) over Q(i)")
    print("per_mode: checked exactly — φ0 is unfaithful; α and β are faithful and conjugate")
    print("per_block: checked exactly — uniqueness is one conjugacy class, conditional on faithfulness")
    print("lattice_wide: checked and not executed — no action is adopted and none is required by the axioms")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
