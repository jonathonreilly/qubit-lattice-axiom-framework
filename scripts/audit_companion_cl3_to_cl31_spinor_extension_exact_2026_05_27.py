#!/usr/bin/env python3
"""Exact-symbolic companion for the Cl(3,0) one-generator extension note.

The runner proves the two sign branches constructively.  For the positive
branch it builds Hamilton's quaternions from their multiplication law, defines
the real-algebra map ``Phi: M_2(H) -> M_8(R)`` by left multiplication on
``H^2``, and proves that the 16 Clifford monomials span exactly ``Phi(M_2(H))``.
It independently solves the matrix commutant and proves that the result is the
quaternion division algebra supplied by diagonal right multiplication.

For the negative branch it constructs four real 4x4 generators and proves that
their 16 monomials span all of ``M_4(R)``.  Primitive-corner dimensions and a
duplicated-``M_4(R)`` decoy distinguish the two algebra types even when real
algebra rank and commutant dimension coincide.  No classification string or
literal Cartan-Bott table participates in a pass/fail check.

The sign normalization and the complete ``Cl(3,0)`` subalgebra multiplication
table are also checked exactly.  This remains a class-(A) finite-algebra
companion: it supplies no Wick-rotation, dynamics, or physical sign selector.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Matrix, eye, zeros
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"
CLAIM_ID = "cl3_to_cl31_spinor_extension_narrow_theorem_note_2026-05-27"


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Symbolic equality of two sympy matrices via simplify."""
    diff = sympy.simplify(A - B)
    return all(diff[i, j] == 0 for i in range(diff.rows) for j in range(diff.cols))


def mat_zero(A: Matrix) -> bool:
    return all(sympy.simplify(A[i, j]) == 0 for i in range(A.rows) for j in range(A.cols))


def kron(A: Matrix, B: Matrix) -> Matrix:
    """Kronecker (tensor) product of two sympy matrices."""
    rA, cA = A.shape
    rB, cB = B.shape
    out = zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            for k in range(rB):
                for l in range(cB):
                    out[i * rB + k, j * cB + l] = A[i, j] * B[k, l]
    return out


def flatten(M: Matrix) -> list:
    """Flatten a sympy matrix into a list of entries (row-major)."""
    out = []
    for i in range(M.rows):
        for j in range(M.cols):
            out.append(M[i, j])
    return out


def real_span_rank(matrices: list) -> int:
    """Rank of the R-linear span of a list of sympy matrices."""
    if not matrices:
        return 0
    cols = [flatten(M) for M in matrices]
    A = Matrix(cols).T  # rows = flattened entries, cols = matrices
    return A.rank()


def enumerate_monomial_indices(n: int) -> list:
    """Enumerate the 2^n standard Clifford monomial index tuples for n generators."""
    if n == 0:
        return [()]
    out = [()]
    # k = 1 .. n
    for k in range(1, n + 1):
        # Generate sorted k-tuples from {1, ..., n}
        def rec(start: int, depth: int, accum: tuple):
            if depth == 0:
                out.append(accum)
                return
            for i in range(start, n + 1):
                rec(i + 1, depth - 1, accum + (i,))
        rec(1, k, ())
    return out


def monomial(generators: list, indices: tuple, identity: Matrix) -> Matrix:
    """Compute the product G_{i_1} ... G_{i_k} for sorted 1-based indices."""
    if not indices:
        return identity
    M = generators[indices[0] - 1]
    for idx in indices[1:]:
        M = M * generators[idx - 1]
    return M


Quaternion = tuple
QuaternionMatrix2 = list[list[Quaternion]]

Q_ZERO: Quaternion = (0, 0, 0, 0)
Q_ONE: Quaternion = (1, 0, 0, 0)
Q_I: Quaternion = (0, 1, 0, 0)
Q_J: Quaternion = (0, 0, 1, 0)
Q_K: Quaternion = (0, 0, 0, 1)
Q_BASIS = [Q_ONE, Q_I, Q_J, Q_K]


def q_add(a: Quaternion, b: Quaternion) -> Quaternion:
    return tuple(x + y for x, y in zip(a, b))


def q_neg(a: Quaternion) -> Quaternion:
    return tuple(-x for x in a)


def q_mul(a: Quaternion, b: Quaternion) -> Quaternion:
    """Hamilton product in the ordered basis (1, i, j, k)."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    )


def quaternion_regular_matrix(q: Quaternion, side: str) -> Matrix:
    """Real 4x4 matrix for left or right multiplication by q on H."""
    if side not in {"left", "right"}:
        raise ValueError(f"unknown quaternion action side: {side}")
    columns = []
    for basis_element in Q_BASIS:
        product = (
            q_mul(q, basis_element)
            if side == "left"
            else q_mul(basis_element, q)
        )
        columns.append(Matrix(product))
    return Matrix.hstack(*columns)


def h2_zero() -> QuaternionMatrix2:
    return [[Q_ZERO, Q_ZERO], [Q_ZERO, Q_ZERO]]


def h2_unit(row: int, col: int, q: Quaternion) -> QuaternionMatrix2:
    result = h2_zero()
    result[row][col] = q
    return result


def h2_add(A: QuaternionMatrix2, B: QuaternionMatrix2) -> QuaternionMatrix2:
    return [[q_add(A[r][c], B[r][c]) for c in range(2)] for r in range(2)]


def h2_mul(A: QuaternionMatrix2, B: QuaternionMatrix2) -> QuaternionMatrix2:
    return [
        [
            q_add(q_mul(A[r][0], B[0][c]), q_mul(A[r][1], B[1][c]))
            for c in range(2)
        ]
        for r in range(2)
    ]


def phi_m2h(A: QuaternionMatrix2) -> Matrix:
    """Explicit real-algebra map M_2(H) -> M_8(R) by left action on H^2."""
    blocks = [
        [quaternion_regular_matrix(A[r][c], "left") for c in range(2)]
        for r in range(2)
    ]
    top = blocks[0][0].row_join(blocks[0][1])
    bottom = blocks[1][0].row_join(blocks[1][1])
    return top.col_join(bottom)


def matrix_units(n: int) -> list[Matrix]:
    result = []
    for row in range(n):
        for col in range(n):
            unit = zeros(n)
            unit[row, col] = 1
            result.append(unit)
    return result


def basis_coordinates(M: Matrix, basis: list[Matrix]) -> list | None:
    """Exact coordinates of M in basis, or None when M is outside its span."""
    coefficient_matrix = Matrix.hstack(*[Matrix(flatten(B)) for B in basis])
    try:
        solution = coefficient_matrix.solve(Matrix(flatten(M)))
    except Exception:
        return None
    return [sympy.simplify(solution[i, 0]) for i in range(len(basis))]


def commutant_basis(generators: list[Matrix]) -> list[Matrix]:
    """Solve XG=GX exactly for every supplied generator G."""
    if not generators:
        return []
    n = generators[0].rows
    ambient_units = matrix_units(n)
    columns = []
    for unit in ambient_units:
        constraints = [Matrix(flatten(unit * G - G * unit)) for G in generators]
        columns.append(Matrix.vstack(*constraints))
    system = Matrix.hstack(*columns)
    return [Matrix(n, n, list(vector)) for vector in system.nullspace()]


def block_diagonal_twice(M: Matrix) -> Matrix:
    """diag(M, M)."""
    zero = zeros(M.rows, M.cols)
    return M.row_join(zero).col_join(zero.row_join(M))


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27")
    print("Goal: construct both Cl(3, 0) one-generator sign extensions")
    print("      and distinguish M_2(H) from M_4(R) by explicit algebra maps,")
    print("      solved commutants, and primitive-corner invariants.")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (S1) Sign-`epsilon` rescaling exhausts the sign branch")
    # =========================================================================
    # Every nonzero real epsilon is either +r^2 or -r^2 for a unique r>0.
    # These two symbolic identities therefore cover the entire nondegenerate
    # branch, rather than a finite sample of epsilon values.
    r = sympy.symbols("r", positive=True, real=True)
    check(
        "(S1) positive square +r^2 rescales to +1 for every r > 0",
        sympy.simplify((r ** 2) / (r ** 2)) == 1,
        detail="epsilon = +r^2",
    )
    check(
        "(S1) negative square -r^2 rescales to -1 for every r > 0",
        sympy.simplify(-(r ** 2) / (r ** 2)) == -1,
        detail="epsilon = -r^2",
    )
    print("  [BOUNDARY] epsilon = 0 is excluded by the nondegenerate-extension hypothesis")

    # =========================================================================
    section("Part 2: (S2) Cl(4, 0) realization with all Gammas squaring to +I_8")
    # =========================================================================
    # Build the plus branch inside M_2(H) first, then apply the explicit
    # left-action map Phi: M_2(H) -> M_8(R).  This makes the target algebra
    # part of the construction rather than a name inferred from dimension.
    I2 = eye(2)
    I4 = eye(4)
    I8 = eye(8)
    sigma_x = Matrix([[0, 1], [1, 0]])
    sigma_z = Matrix([[1, 0], [0, -1]])
    eps_mat = Matrix([[0, -1], [1, 0]])  # iσ_y as a real matrix

    # Verify small-matrix algebra (used by both realizations)
    check("(S2) σ_x^2 = I_2", mat_eq(sigma_x * sigma_x, I2))
    check("(S2) σ_z^2 = I_2", mat_eq(sigma_z * sigma_z, I2))
    check("(S2) ε^2 = -I_2", mat_eq(eps_mat * eps_mat, -I2))
    check(
        "(S2) {σ_x, σ_z} = 0",
        mat_zero(sigma_x * sigma_z + sigma_z * sigma_x),
    )
    check(
        "(S2) {σ_x, ε} = 0",
        mat_zero(sigma_x * eps_mat + eps_mat * sigma_x),
    )
    check(
        "(S2) {σ_z, ε} = 0",
        mat_zero(sigma_z * eps_mat + eps_mat * sigma_z),
    )

    # Generators for the minus branch are defined now because Part 3 reuses
    # the same exact 2x2 building blocks.
    Gamma_1 = kron(sigma_x, I2)             # squares to +I_4
    Gamma_2 = kron(sigma_z, sigma_x)        # squares to +I_4
    Gamma_3 = kron(sigma_z, sigma_z)        # squares to +I_4

    # In M_2(H), let
    #   g_1 = [[0,1],[1,0]],
    #   g_u = [[0,u],[-u,0]] for u in {i,j,k}.
    # Since u^2=-1 and distinct imaginary units anticommute, all four g's
    # square to +1 and anticommute pairwise.
    gamma_h_1 = h2_add(h2_unit(0, 1, Q_ONE), h2_unit(1, 0, Q_ONE))

    def gamma_h_imaginary(q: Quaternion) -> QuaternionMatrix2:
        return h2_add(h2_unit(0, 1, q), h2_unit(1, 0, q_neg(q)))

    Gammas_40_h = [
        gamma_h_1,
        gamma_h_imaginary(Q_I),
        gamma_h_imaginary(Q_J),
        gamma_h_imaginary(Q_K),
    ]
    Gammas_40 = [phi_m2h(G) for G in Gammas_40_h]
    Gamma_4_8_plus = Gammas_40[3]

    # The standard 16-element real basis of M_2(H), mapped explicitly into
    # M_8(R).  Its rank proves Phi injective.
    m2h_basis = [h2_unit(row, col, q) for row in range(2) for col in range(2)
                 for q in Q_BASIS]
    phi_basis = [phi_m2h(A) for A in m2h_basis]
    phi_rank = real_span_rank(phi_basis)
    check(
        "(S2) explicit Phi: M_2(H) -> M_8(R) is injective on its 16-element basis",
        phi_rank == 16,
        detail=f"computed image-basis rank = {phi_rank}",
    )
    phi_multiplicative = all(
        mat_eq(phi_m2h(h2_mul(A, B)), phi_m2h(A) * phi_m2h(B))
        for A in m2h_basis
        for B in m2h_basis
    )
    check(
        "(S2) Phi preserves all 256 products of standard M_2(H) basis elements",
        phi_multiplicative,
        detail="explicit real-algebra homomorphism",
    )

    # Verify the plus-branch Clifford relations after applying Phi.
    for i in range(4):
        check(
            f"(S2) Γ_{i+1}^2 = +I_8 (Cl(4, 0) signature)",
            mat_eq(Gammas_40[i] * Gammas_40[i], I8),
            detail=f"Cl(4, 0) generator {i+1}",
        )
    for i in range(4):
        for j in range(i + 1, 4):
            anti = Gammas_40[i] * Gammas_40[j] + Gammas_40[j] * Gammas_40[i]
            check(
                f"(S2) {{Γ_{i+1}, Γ_{j+1}}} = 0 (Cl(4, 0) off-diagonal)",
                mat_zero(anti),
                detail="anticommute",
            )

    # Compute the Clifford image and prove it is exactly image(Phi), not just
    # another real algebra of the same dimension.
    monomial_indices = enumerate_monomial_indices(4)
    check(
        "(S2) 16 monomial indices enumerated for n = 4",
        len(monomial_indices) == 16,
        detail=f"count = {len(monomial_indices)}",
    )

    monomials_40 = [monomial(Gammas_40, idx, I8) for idx in monomial_indices]
    rank_40 = real_span_rank(monomials_40)
    check(
        "(S2) Cl(4, 0): 16 monomials have R-linear rank 16 in M_8(R)",
        rank_40 == 16,
        detail=f"computed rank = {rank_40}; dim_R Cl(4, 0) = 16",
    )
    joint_rank_40_m2h = real_span_rank(monomials_40 + phi_basis)
    check(
        "(S2) Clifford-monomial image equals explicit Phi(M_2(H))",
        rank_40 == phi_rank == joint_rank_40_m2h == 16,
        detail=f"rank(Cl image + Phi basis) = {joint_rank_40_m2h}",
    )
    transition_40_to_m2h = [basis_coordinates(M, phi_basis) for M in monomials_40]
    transition_matrix = Matrix.hstack(
        *[Matrix(coefficients) for coefficients in transition_40_to_m2h
          if coefficients is not None]
    )
    check(
        "(S2) explicit Clifford-to-M_2(H) change-of-basis matrix is invertible",
        len(transition_40_to_m2h) == 16
        and all(coefficients is not None for coefficients in transition_40_to_m2h)
        and transition_matrix.det() != 0,
        detail=f"determinant = {transition_matrix.det()}",
    )

    # Compute the full commutant from X Gamma_a = Gamma_a X.  Independent
    # right multiplication on H^2 supplies the expected quaternion basis.
    commutant_40 = commutant_basis(Gammas_40)
    right_actions = [
        block_diagonal_twice(quaternion_regular_matrix(q, "right"))
        for q in Q_BASIS
    ]
    # Right multiplication is an anti-representation.  Negating the three
    # imaginary actions gives the usual Hamilton multiplication order.
    comm_h = [right_actions[0], -right_actions[1], -right_actions[2], -right_actions[3]]
    commutant_joint_rank = real_span_rank(commutant_40 + comm_h)
    check(
        "(S2) solved commutant has dimension 4 and equals diagonal right-H action",
        len(commutant_40) == 4
        and real_span_rank(comm_h) == 4
        and commutant_joint_rank == 4,
        detail=f"computed dim = {len(commutant_40)}; joint rank = {commutant_joint_rank}",
    )
    check(
        "(S2) commutant units satisfy i^2=j^2=k^2=-1 and ij=k=-ji",
        mat_eq(comm_h[1] * comm_h[1], -I8)
        and mat_eq(comm_h[2] * comm_h[2], -I8)
        and mat_eq(comm_h[3] * comm_h[3], -I8)
        and mat_eq(comm_h[1] * comm_h[2], comm_h[3])
        and mat_eq(comm_h[2] * comm_h[1], -comm_h[3]),
    )
    a, b, c, d = sympy.symbols("a b c d", real=True)
    comm_q = a * comm_h[0] + b * comm_h[1] + c * comm_h[2] + d * comm_h[3]
    comm_q_conjugate = a * comm_h[0] - b * comm_h[1] - c * comm_h[2] - d * comm_h[3]
    norm_sq = a ** 2 + b ** 2 + c ** 2 + d ** 2
    check(
        "(S2) symbolic quaternion norm makes every nonzero commutant element invertible",
        mat_eq(comm_q * comm_q_conjugate, norm_sq * I8)
        and mat_eq(comm_q_conjugate * comm_q, norm_sq * I8),
        detail="q q_bar = q_bar q = (a^2+b^2+c^2+d^2) I_8",
    )

    # =========================================================================
    section("Part 3: (S3) Cl(3, 1) realization with η = diag(+1, +1, +1, -1)")
    # =========================================================================
    # The 4x4 real Cl(3, 1) realization uses the three R^4 matrices defined
    # above (each squaring to +I_4), plus Gamma_4 squaring to -I_4.

    Gamma_4 = kron(sigma_z, eps_mat)  # squares to -I_4, anticommutes with Γ_1, Γ_2, Γ_3

    Gammas_31 = [Gamma_1, Gamma_2, Gamma_3, Gamma_4]
    eta = [1, 1, 1, -1]

    for i in range(4):
        check(
            f"(S3) Γ_{i+1}^2 = {eta[i]} · I_4 (Cl(3, 1) signature)",
            mat_eq(Gammas_31[i] * Gammas_31[i], eta[i] * I4),
            detail=f"η_{{{i+1}{i+1}}} = {eta[i]}",
        )
    for i in range(4):
        for j in range(i + 1, 4):
            anti = Gammas_31[i] * Gammas_31[j] + Gammas_31[j] * Gammas_31[i]
            check(
                f"(S3) {{Γ_{i+1}, Γ_{j+1}}} = 0 (Cl(3, 1) off-diagonal)",
                mat_zero(anti),
                detail="anticommute",
            )

    # 16 Cl(3, 1) monomials on R^4
    monomials_31 = [monomial(Gammas_31, idx, I4) for idx in monomial_indices]
    rank_31 = real_span_rank(monomials_31)
    check(
        "(S3) Cl(3, 1): 16 monomials have R-linear rank 16 in M_4(R)",
        rank_31 == 16,
        detail=f"computed rank = {rank_31}; dim_R M_4(R) = 16",
    )
    check(
        "(S3) span(16 Cl(3, 1) monomials) = M_4(R) (rank = 16 = dim_R M_4(R))",
        rank_31 == 16,
        detail="surjective onto M_4(R)",
    )
    m4r_basis = matrix_units(4)
    m4r_joint_rank = real_span_rank(monomials_31 + m4r_basis)
    check(
        "(S3) Clifford-monomial image equals the standard M_4(R) matrix-unit span",
        real_span_rank(m4r_basis) == 16 and m4r_joint_rank == 16,
        detail=f"rank(Cl image + matrix units) = {m4r_joint_rank}",
    )
    commutant_31 = commutant_basis(Gammas_31)
    check(
        "(S3) solved commutant is exactly the scalar real algebra R I_4",
        len(commutant_31) == 1
        and real_span_rank(commutant_31 + [I4]) == 1,
        detail=f"computed commutant dimension = {len(commutant_31)}",
    )

    # =========================================================================
    section("Part 4: (S2)-(S3) Side-by-side: only sign of Γ_4^2 differs")
    # =========================================================================
    # The first three generators of Cl(3, 1) and the first three generators
    # of the abstract Cl(4, 0) (in any realization) satisfy the same
    # Cl(3, 0) relations. The only difference between (S2) and (S3) is the
    # sign of Γ_4^2.
    #
    # We verify this on the abstract level: in the realization above,
    # Cl(3, 1) Γ_4^2 = -I_4 (with Γ_4 = σ_z ⊗ ε on R^4), while in the
    # 8x8 Cl(4, 0) realization, Γ_4^2 = +I_8. The signs differ; the
    # anticommutation with Γ_1, Γ_2, Γ_3 holds in both cases.

    check(
        "(S4-side) Cl(3, 1): Γ_4^2 = -I (sign ε = -1)",
        mat_eq(Gamma_4 * Gamma_4, -I4),
        detail="Cl(3, 1) timelike generator",
    )
    check(
        "(S4-side) Cl(4, 0): Γ_4^2 = +I (sign ε = +1)",
        mat_eq(Gamma_4_8_plus * Gamma_4_8_plus, I8),
        detail="Cl(4, 0) spacelike-extended generator",
    )
    # Extract the scalar-square coefficients from the displayed matrices.  The
    # branch definition changes only this coefficient; equality of the first
    # three generators' abstract multiplication tables is checked in Part 8.
    sign_31 = sympy.trace(Gamma_4 * Gamma_4) / I4.rows
    sign_40 = sympy.trace(Gamma_4_8_plus * Gamma_4_8_plus) / I8.rows
    check(
        "(S4-side) computed fourth-generator square coefficients are opposite unit signs",
        sympy.simplify(sign_31 * sign_40) == -1
        and sympy.simplify(sign_31 ** 2) == 1
        and sympy.simplify(sign_40 ** 2) == 1,
        detail=f"epsilon_minus = {sign_31}; epsilon_plus = {sign_40}",
    )

    # =========================================================================
    section("Part 5: (S4) Constructive real-vs-quaternionic discrimination")
    # =========================================================================
    # A primitive idempotent gives an algebra-isomorphism invariant: the real
    # dimension and division type of its corner eAe.  For M_2(H), e=E_11 has
    # corner H (dimension four and division).  For M_4(R), a primitive matrix
    # unit has corner R (dimension one).  This rules out an accidental
    # identification of the two 16-dimensional real algebras.
    primitive_h = phi_m2h(h2_unit(0, 0, Q_ONE))
    corner_h = [primitive_h * B * primitive_h for B in phi_basis]
    corner_h_basis = [phi_m2h(h2_unit(0, 0, q)) for q in Q_BASIS]
    corner_h_rank = real_span_rank(corner_h)
    check(
        "(S4) plus-branch E_11 is idempotent and its corner has real dimension 4",
        mat_eq(primitive_h * primitive_h, primitive_h)
        and corner_h_rank == 4
        and real_span_rank(corner_h + corner_h_basis) == 4,
        detail=f"dim_R(E_11 A_plus E_11) = {corner_h_rank}",
    )
    corner_q = (
        a * corner_h_basis[0]
        + b * corner_h_basis[1]
        + c * corner_h_basis[2]
        + d * corner_h_basis[3]
    )
    corner_q_conjugate = (
        a * corner_h_basis[0]
        - b * corner_h_basis[1]
        - c * corner_h_basis[2]
        - d * corner_h_basis[3]
    )
    check(
        "(S4) plus-branch primitive corner is quaternionic division algebra H",
        mat_eq(corner_q * corner_q_conjugate, norm_sq * primitive_h)
        and mat_eq(corner_q_conjugate * corner_q, norm_sq * primitive_h),
        detail="nonzero corner elements invert by quaternion conjugation",
    )

    primitive_r = m4r_basis[0]
    corner_r = [primitive_r * B * primitive_r for B in m4r_basis]
    corner_r_rank = real_span_rank(corner_r)
    check(
        "(S4) minus-branch primitive matrix-unit corner has real dimension 1",
        mat_eq(primitive_r * primitive_r, primitive_r) and corner_r_rank == 1,
        detail=f"dim_R(E_11 M_4(R) E_11) = {corner_r_rank}",
    )

    real_matrix_sizes = [size for size in range(1, 17) if size * size == rank_40]
    check(
        "(S4) a single real matrix algebra of real dimension 16 would have size 4",
        real_matrix_sizes == [4],
        detail=f"integer solutions of k^2 = {rank_40}: {real_matrix_sizes}",
    )
    check(
        "(S4) primitive-corner invariant separates Phi(M_2(H)) from M_4(R)",
        corner_h_rank != corner_r_rank,
        detail=f"quaternionic corner dim {corner_h_rank} vs real corner dim {corner_r_rank}",
    )

    # Mutation/decoy control.  Let M_4(R) act twice on R^8.  Its image also
    # has algebra rank 16 and commutant dimension four, so either number by
    # itself could falsely mimic the plus branch.  The decoy commutant is
    # M_2(R), however, and contains nonzero zero divisors; the quaternion norm
    # gate above rejects it.
    duplicated_m4r_basis = [kron(B, I2) for B in m4r_basis]
    duplicated_commutant = commutant_basis(duplicated_m4r_basis)
    expected_duplicated_commutant = [kron(I4, B) for B in matrix_units(2)]
    check(
        "(S4 mutation control) duplicated M_4(R) also has rank 16 and commutant dimension 4",
        real_span_rank(duplicated_m4r_basis) == 16
        and len(duplicated_commutant) == 4
        and real_span_rank(duplicated_commutant + expected_duplicated_commutant) == 4,
        detail="dimension-only classifier is deliberately non-decisive",
    )
    decoy_idempotent = kron(I4, Matrix([[1, 0], [0, 0]]))
    decoy_complement = I8 - decoy_idempotent
    check(
        "(S4 mutation control) duplicated-M_4(R) commutant has nonzero zero divisors",
        not mat_zero(decoy_idempotent)
        and not mat_zero(decoy_complement)
        and mat_zero(decoy_idempotent * decoy_complement)
        and all(
            mat_zero(decoy_idempotent * B - B * decoy_idempotent)
            for B in duplicated_m4r_basis
        ),
        detail="M_2(R) commutant fails the quaternion division-norm gate",
    )

    # =========================================================================
    section("Part 6: (S4) Restriction to Cl(3, 0)-extensions at n = 4")
    # =========================================================================
    # Cl(3, 0) has three positive-square generators. A single-generator
    # extension with ε = +1 adds a fourth positive-square generator → Cl(4, 0).
    # A single-generator extension with ε = -1 adds a fourth negative-square
    # generator → Cl(3, 1).
    # Derive the signatures arithmetically from the computed square signs.
    def extension_signature(square_sign: int) -> tuple[int, int]:
        return (3 + int(square_sign > 0), int(square_sign < 0))

    reachable = {
        extension_signature(int(sign_40)),
        extension_signature(int(sign_31)),
    }
    check(
        "(S4) Cl(3, 0)-extensions at n = 4: exactly {(4, 0), (3, 1)} reachable",
        reachable == {(4, 0), (3, 1)},
        detail=f"derived from square signs: {sorted(reachable)}",
    )
    check(
        "(S4) (2, 2) NOT reachable from Cl(3, 0) by single-generator extension",
        (2, 2) not in reachable,
        detail="every derived signature retains the three positive-square generators",
    )
    check(
        "(S4) Among Cl(3, 0)-extensions at n = 4, only (3, 1) is single-M_k(R)",
        rank_31 == 16
        and m4r_joint_rank == 16
        and joint_rank_40_m2h == 16
        and corner_h_rank != corner_r_rank,
        detail="minus image is M_4(R); plus image is M_2(H) with quaternionic primitive corner",
    )

    # =========================================================================
    section("Part 7: (S5) Cl(3, 0) subalgebra preservation in both extensions")
    # =========================================================================
    # In both the Cl(4, 0) (on R^8) and the Cl(3, 1) (on R^4) realizations,
    # the subalgebra generated by Γ_1, Γ_2, Γ_3 alone is Cl(3, 0), of
    # real dimension 8.
    #
    # 8 standard monomials for Cl(3, 0):
    #   {1, Γ_1, Γ_2, Γ_3, Γ_1 Γ_2, Γ_1 Γ_3, Γ_2 Γ_3, Γ_1 Γ_2 Γ_3}

    cl3_indices = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    check(
        "(S5) 8 Cl(3, 0) monomial indices enumerated",
        len(cl3_indices) == 8,
        detail=f"count = {len(cl3_indices)} = 2^3",
    )

    # In the Cl(3, 1) realization on R^4
    cl3_monomials_31 = [monomial(Gammas_31, idx, I4) for idx in cl3_indices]
    rank_cl3_in_31 = real_span_rank(cl3_monomials_31)
    check(
        "(S5) Cl(3, 0) in Cl(3, 1): 8 monomials span 8-dim real subalgebra of M_4(R)",
        rank_cl3_in_31 == 8,
        detail=f"computed rank = {rank_cl3_in_31}; dim_R Cl(3, 0) = 8",
    )

    # In the Cl(4, 0) realization on R^8 (using first three generators only)
    cl3_monomials_40 = [monomial(Gammas_40, idx, I8) for idx in cl3_indices]
    rank_cl3_in_40 = real_span_rank(cl3_monomials_40)
    check(
        "(S5) Cl(3, 0) in Cl(4, 0): 8 monomials span 8-dim real subalgebra of M_8(R)",
        rank_cl3_in_40 == 8,
        detail=f"computed rank = {rank_cl3_in_40}; dim_R Cl(3, 0) = 8",
    )

    # =========================================================================
    section("Part 8: (S5) Structure constants of Cl(3, 0) subalgebra match")
    # =========================================================================
    # Multiplication table of the 8 Cl(3, 0) monomials is identical between
    # the two realizations (up to the embedding-dimension difference; the
    # structure constants over the 8-dim subspace are the same).
    #
    # We verify: for each pair (idx_a, idx_b), the product monomial
    # m_a * m_b expressed in the 8-monomial basis has the same
    # coefficients in both realizations (Cl(3, 1) on R^4 and Cl(4, 0) on R^8).
    #
    # Check every product, not a representative subset.  This comparison is
    # independent of the different ambient module dimensions.
    structure_constants_31 = [
        basis_coordinates(A * B, cl3_monomials_31)
        for A in cl3_monomials_31
        for B in cl3_monomials_31
    ]
    structure_constants_40 = [
        basis_coordinates(A * B, cl3_monomials_40)
        for A in cl3_monomials_40
        for B in cl3_monomials_40
    ]
    check(
        "(S5) all 64 Cl(3, 0) basis products have identical structure constants",
        all(coefficients is not None for coefficients in structure_constants_31)
        and all(coefficients is not None for coefficients in structure_constants_40)
        and structure_constants_31 == structure_constants_40,
        detail="complete 8 x 8 multiplication table compared",
    )

    # Product Γ_1 Γ_2 Γ_3 (the volume element of Cl(3, 0)).  For three
    # anticommuting +1-square generators, omega^2 = -I:
    # ω^2 = Γ_1 Γ_2 Γ_3 Γ_1 Γ_2 Γ_3
    #     = Γ_1 Γ_2 (-Γ_1) Γ_3 Γ_2 Γ_3   (Γ_3 Γ_1 = -Γ_1 Γ_3)
    #     = -Γ_1 (-Γ_1) Γ_2 Γ_3 Γ_2 Γ_3  (Γ_2 Γ_1 = -Γ_1 Γ_2)
    #     = +I * Γ_2 (-Γ_2) Γ_3 Γ_3        (Γ_3 Γ_2 = -Γ_2 Γ_3, Γ_1^2 = +I)
    #     = -I * I                          (Γ_2^2 = I, Γ_3^2 = I)
    #     = -I
    # So ω^2 = -I in Cl(3, 0).
    omega_31 = Gammas_31[0] * Gammas_31[1] * Gammas_31[2]
    check(
        "(S5) Cl(3, 0) volume element ω = Γ_1 Γ_2 Γ_3 satisfies ω^2 = -I (Cl(3, 1) realization)",
        mat_eq(omega_31 * omega_31, -I4),
        detail="standard Cl(3, 0) pseudoscalar relation",
    )

    omega_40 = Gammas_40[0] * Gammas_40[1] * Gammas_40[2]
    check(
        "(S5) Cl(3, 0) volume element ω = Γ_1 Γ_2 Γ_3 satisfies ω^2 = -I (Cl(4, 0) realization)",
        mat_eq(omega_40 * omega_40, -I8),
        detail="same Cl(3, 0) pseudoscalar relation",
    )

    # =========================================================================
    section("Part 9: Final sign-extension classification summary")
    # =========================================================================
    print("  Summary of the narrow theorem identities:")
    print("    (S1) sign-ε branch:        ε ∈ {+1, -1} exhausts the rescaling")
    print("    (S2) ε = +1 → Cl(4, 0):    M_2(H), real-dim 16, faithful on R^8")
    print("    (S3) ε = -1 → Cl(3, 1):    M_4(R), real-dim 16, faithful on R^4")
    print("    (S4) single-M_k(R) cell:   (3, 1) is the unique Cl(3, 0)-extension")
    print("                                landing on a single M_k(R) at n = 4")
    print("    (S5) Cl(3, 0) ⊂ A':        preserved in both extensions, dim 8")

    # =========================================================================
    section("Final result")
    # =========================================================================
    print(f"  Note path: {NOTE_PATH}")
    print(f"  Claim id:  {CLAIM_ID}")
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()
    if FAIL == 0:
        print("  RESULT: PASS (no failures detected)")
        return 0
    else:
        print("  RESULT: FAIL (one or more checks failed)")
        return 1


if __name__ == "__main__":
    sys.exit(main())
