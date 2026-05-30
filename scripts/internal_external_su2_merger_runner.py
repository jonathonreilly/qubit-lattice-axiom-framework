"""Runner for the Internal-External SU(2) Merger from Universal Property of Cl(3,0).

Verifies the claims in
docs/INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md:

  (M1) Internal su(2) on H_x = C^2: bivector generators
       B_i := (1/2) * gamma_j * gamma_k for (i,j,k) cyclic in (1,2,3)
       acting on H_x via the retained Pauli irrep satisfy
       [B_i, B_j] = -epsilon_{ijk} B_k, equivalently with S_i = -i * B_i
       we get [S_i, S_j] = i epsilon_{ijk} S_k. Standard bivector-spin
       identification.
  (M2) Spatial-rotation action of SO(3) on the bivector subspace
       Lambda^2(R^3) under universal-property automorphism phi_R: for
       every R in SO(3), phi_R restricted to the bivector subspace
       Lambda^2 is exactly the SO(3) action on Lambda^2 R^3
       (equivalently, R itself in 3D via Hodge duality).
  (M3) Infinitesimal generator coincidence: differentiating phi_R at R=I
       along the i-th rotation axis yields, on H_x, the operator S_i
       = sigma_i/2. The internal-su(2) generators and the spatial-Spin(3)
       generators are the SAME operators, not merely isomorphic.
  (M4) Cubic O_h subgroup: of the 48 elements of O_h, the 24 proper
       rotations lift to 24 SU(2) actions on H_x = C^2; the 24 improper
       rotations are checked as signed real-Clifford generator actions,
       not as ordinary complex-linear unitary conjugations on H_x.
  (M5) Pauli-element equivariance: for all 24 proper R in O_h, there
       exists U(R) in SU(2) such that U(R) sigma_i U(R)^* = sum_j R_ij
       sigma_j. The map R -> U(R) is the standard SO(3) -> SU(2)
       double cover restricted to the cubic point group; it is exactly
       the same data as the internal-su(2) representation on H_x.

Exact sympy + integer/rational symbolic checks. No floating-point
approximations are used for the load-bearing identities. No new
admissions; pure finite-group + Clifford-algebra + Lie-algebra
verification.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp


# ----------------------------------------------------------------------
# Cl(3,0) concrete realization via Pauli matrices: Cl(3) inside M_2(C)
# ----------------------------------------------------------------------

I2 = sp.eye(2)
SIGMA = [
    sp.Matrix([[0, 1], [1, 0]]),                # sigma_1 = gamma_1
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),         # sigma_2 = gamma_2
    sp.Matrix([[1, 0], [0, -1]]),               # sigma_3 = gamma_3
]


def gamma(i: int):
    """gamma_i for i in {1,2,3}; 1-based index. Realized as Pauli sigma_i."""
    return SIGMA[i - 1]


def pseudoscalar():
    """omega = gamma_1 gamma_2 gamma_3 = i * I_2 in M_2(C)."""
    return SIGMA[0] * SIGMA[1] * SIGMA[2]


def matrices_close_exact(A, B) -> bool:
    """Exact equality test on sympy matrices."""
    return sp.simplify(A - B) == sp.zeros(*A.shape)


def commutator(A, B):
    return A * B - B * A


def anticommutator(A, B):
    return A * B + B * A


# ----------------------------------------------------------------------
# Bivector / spin generators on H_x = C^2
# ----------------------------------------------------------------------


def bivector_B(i: int):
    """Bivector B_i = (1/2) gamma_j gamma_k for (i,j,k) cyclic.
    Note: (1,2,3) -> B_1 = (1/2) gamma_2 gamma_3, etc.
    """
    cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
    j, k = cyc[i]
    return sp.Rational(1, 2) * gamma(j) * gamma(k)


def spin_S(i: int):
    """Spin generator S_i = sigma_i / 2. Equivalently = -sp.I * B_i for
    the (positive-chirality) Pauli realization.
    """
    return sp.Rational(1, 2) * gamma(i)


# ----------------------------------------------------------------------
# O(3) elements via signed permutations (O_h, full 48 elements)
# ----------------------------------------------------------------------


def all_o_h_matrices():
    """All 48 elements of O_h as 3x3 sympy signed permutation matrices."""
    matrices = []
    for perm in itertools.permutations([0, 1, 2]):
        for signs in itertools.product([+1, -1], repeat=3):
            M = sp.zeros(3, 3)
            for row, (col, sign) in enumerate(zip(perm, signs)):
                M[row, col] = sign
            matrices.append(M)
    return matrices


def is_proper(R) -> bool:
    """det(R) = +1 (proper rotation)."""
    return sp.simplify(R.det()) == 1


# ----------------------------------------------------------------------
# Universal-property automorphism phi_R on Cl(3) generators
# ----------------------------------------------------------------------


def phi_R_on_gamma(R, i: int):
    """phi_R(gamma_i) = sum_j R_ij gamma_j (universal-property lift)."""
    result = sp.zeros(2, 2)
    for j in range(3):
        result += R[i - 1, j] * gamma(j + 1)
    return result


def phi_R_on_product(R, indices):
    """phi_R(gamma_{i_1} ... gamma_{i_k}) = prod_a phi_R(gamma_{i_a})."""
    result = I2
    for i in indices:
        result = result * phi_R_on_gamma(R, i)
    return result


def phi_R_on_bivector(R, i: int):
    """phi_R(B_i) where B_i = (1/2) gamma_j gamma_k for (i,j,k) cyclic."""
    cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
    j, k = cyc[i]
    return sp.Rational(1, 2) * phi_R_on_product(R, [j, k])


# ----------------------------------------------------------------------
# Spin double-cover: find U(R) such that U sigma_i U^* = sum_j R_ij sigma_j
# ----------------------------------------------------------------------


def cofactor_3x3(R):
    """Cofactor matrix (matrix of (i,j)-cofactors) of a 3x3 matrix."""
    M = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            minor = R.minor(i, j)
            M[i, j] = (-1)**(i + j) * minor
    return M


def find_double_cover_U(R):
    """Given proper R in SO(3), construct an SU(2) double-cover element U
    using a direct exponential-of-generator formula.

    Strategy: extract axis-angle (n, theta) of R, then build
      U = cos(theta/2) * I_2  - i * sin(theta/2) * (n.sigma)

    For O_h elements, theta in {0, pi/2, pi, 2pi/3, ...} and n has rational
    components; we handle the theta = pi case (skew part vanishes) and
    theta = 0 case (identity) separately.

    The returned U is one of the two double-cover pre-images; the other is
    -U. Either gives the same conjugation action sigma_i -> U sigma_i U^*.
    """
    if not is_proper(R):
        return None

    # Identity matrix special case
    if matrices_close_exact(R, sp.eye(3)):
        return I2

    cos_t = sp.simplify(sp.Rational(1, 2) * (R.trace() - 1))

    # Compute skew part to extract sin(theta) * n
    skew = (R - R.T) / 2
    sv1 = skew[2, 1]
    sv2 = skew[0, 2]
    sv3 = skew[1, 0]
    s_squared = sp.simplify(sv1**2 + sv2**2 + sv3**2)

    if sp.simplify(s_squared) == 0:
        # theta = 0 (handled above) or theta = pi
        # theta = pi: axis from (R + I)/2 = n n^T
        proj = sp.simplify((R + sp.eye(3)) / 2)
        # Find a column with maximum diagonal entry to extract axis
        best_col = -1
        best_val = sp.Integer(0)
        for col in range(3):
            v = sp.simplify(proj[col, col])
            if v != 0 and (best_col < 0 or v > best_val):
                best_col = col
                best_val = v
        if best_col < 0:
            return None
        # Extract axis from this column
        n = sp.Matrix([proj[i, best_col] for i in range(3)])
        # Normalize: n . n should be best_val (the diagonal entry, since
        # proj = n n^T, so proj[k, k] = n_k^2 and proj[i, k] = n_i * n_k).
        # So n = (proj[0,k], proj[1,k], proj[2,k]) / sqrt(proj[k,k])
        denom = sp.sqrt(best_val)
        n = sp.simplify(n / denom)
        # Verify n has unit length
        norm_sq = sp.simplify(n[0]**2 + n[1]**2 + n[2]**2)
        if sp.simplify(norm_sq - 1) != 0:
            return None
        # For theta = pi: U = -i (n . sigma)  (cos(pi/2) = 0, sin(pi/2) = 1)
        ndotS = n[0] * SIGMA[0] + n[1] * SIGMA[1] + n[2] * SIGMA[2]
        U = sp.simplify(-sp.I * ndotS)
        return U

    # General case: theta in (0, pi) or theta in (pi, 2pi).
    # The sign of skew[2,1] etc. distinguishes the rotation direction.
    # Use half-angle formulas:
    #   cos(theta/2) = sqrt((1 + cos(theta))/2)   (positive choice)
    #   sin(theta/2) = sqrt((1 - cos(theta))/2)   (positive choice)
    half_cos_sq = sp.simplify(sp.Rational(1, 2) * (1 + cos_t))
    half_sin_sq = sp.simplify(sp.Rational(1, 2) * (1 - cos_t))
    half_cos = sp.sqrt(half_cos_sq)
    half_sin = sp.sqrt(half_sin_sq)

    # n_i = sv_i / sin(theta); but sin(theta) = 2 sin(theta/2) cos(theta/2),
    # so n_i = sv_i / (2 * half_sin * half_cos), and the product
    # half_sin * n_i = sv_i / (2 * half_cos).
    # This avoids any sqrt issues when reconstructing the U matrix.
    n1_times_halfsin = sp.simplify(sv1 / (2 * half_cos))
    n2_times_halfsin = sp.simplify(sv2 / (2 * half_cos))
    n3_times_halfsin = sp.simplify(sv3 / (2 * half_cos))
    ndotS_halfsin = (n1_times_halfsin * SIGMA[0]
                     + n2_times_halfsin * SIGMA[1]
                     + n3_times_halfsin * SIGMA[2])
    U = half_cos * I2 - sp.I * ndotS_halfsin
    return sp.simplify(U)


def double_cover_check(R):
    """For proper R in SO(3), verify the PR-2046 convention double-cover
    relation U(R) sigma_i U(R)^* = sum_j R_{ij} sigma_j = phi_R(sigma_i).

    We use the row-vector universal-property convention:
      phi_R(gamma_i) := sum_j R_ij gamma_j
    The spinorial lift U(R) realizes this conjugation on H_x = C^2:
      U(R) sigma_i U(R)^* = phi_R(sigma_i) = sum_j R_ij sigma_j

    Implementation: find_double_cover_U is calibrated to "rotation R acts
    on basis vectors via R*e_i = sum_j R_{ji} e_j" (column convention), which
    yields U sigma_i U^* = sum_j R_{ji} sigma_j. To recover the
    row-vector convention
    convention we apply find_double_cover_U to R.T and verify against R.

    Returns True if the equation holds, False otherwise.
    """
    if not is_proper(R):
        return None  # not in domain
    # Use R.T in the half-angle construction so the conjugation matches
    # row-vector universal-property convention phi_R.
    U = find_double_cover_U(R.T)
    if U is None:
        return False
    U_dag = U.H
    # Sanity: U is unitary (U U^* = I).
    if not matrices_close_exact(sp.simplify(U * U_dag), I2):
        return False
    for i in range(3):
        lhs = sp.simplify(U * SIGMA[i] * U_dag)
        rhs = sp.zeros(2, 2)
        for j in range(3):
            rhs += R[i, j] * SIGMA[j]
        if not matrices_close_exact(lhs, rhs):
            return False
    return True


# ----------------------------------------------------------------------
# Test sections
# ----------------------------------------------------------------------


def run_section_1_pauli_sanity():
    """Section 1: Sanity checks on Pauli realization of Cl(3,0)."""
    name = "Section 1: Pauli realization of Cl(3,0)"
    pass_count = 0
    fail_count = 0
    failures = []

    # Pauli relations: {sigma_i, sigma_j} = 2 delta_{ij} I
    for i in range(1, 4):
        for j in range(1, 4):
            anti = anticommutator(gamma(i), gamma(j))
            expected = 2 * (1 if i == j else 0) * I2
            if matrices_close_exact(anti, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(f"  FAIL: {{sigma_{i}, sigma_{j}}} != 2 delta_{{{i}{j}}} I")

    # Pseudoscalar omega = sigma_1 sigma_2 sigma_3 = i * I
    omega = pseudoscalar()
    expected_omega = sp.I * I2
    if matrices_close_exact(omega, expected_omega):
        pass_count += 1
    else:
        fail_count += 1
        failures.append(f"  FAIL: omega != i * I_2; got {omega}")

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_2_internal_su2():
    """Section 2: (M1) Bivectors implement internal su(2) on H_x.

    For (i,j,k) cyclic, B_i = (1/2) gamma_j gamma_k.
    Check [B_i, B_j] = -epsilon_{ijk} B_k (bivector commutator yields su(2)).
    Equivalently with S_i = -i B_i: [S_i, S_j] = i epsilon_{ijk} S_k.

    Also S_i = sigma_i / 2 in the Pauli realization (consistency).
    """
    name = "Section 2: (M1) Internal su(2) from bivectors on H_x"
    pass_count = 0
    fail_count = 0
    failures = []

    # epsilon symbol
    def eps(i, j, k):
        if (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
            return 1
        if (i, j, k) in [(1, 3, 2), (2, 1, 3), (3, 2, 1)]:
            return -1
        return 0

    # B_i = (1/2) sigma_j sigma_k for (i,j,k) cyclic; verify B_i = (i/2) sigma_i (since sigma_j sigma_k = i sigma_i for cyclic)
    for i in range(1, 4):
        cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
        j, k = cyc[i]
        # B_i = (1/2) sigma_j sigma_k. For (i,j,k) cyclic in {1,2,3}, sigma_j sigma_k = i sigma_i.
        Bi = bivector_B(i)
        expected = sp.Rational(1, 2) * sp.I * gamma(i)
        if matrices_close_exact(Bi, expected):
            pass_count += 1
        else:
            fail_count += 1
            failures.append(f"  FAIL: B_{i} != (i/2) sigma_{i}")

    # [B_i, B_j] = -epsilon_{ijk} B_k bivector commutator
    for i in range(1, 4):
        for j in range(1, 4):
            comm = commutator(bivector_B(i), bivector_B(j))
            expected = sp.zeros(2, 2)
            for k in range(1, 4):
                expected += -eps(i, j, k) * bivector_B(k)
            if matrices_close_exact(comm, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(f"  FAIL: [B_{i}, B_{j}] != -epsilon_{{{i}{j}k}} B_k")

    # S_i = -i B_i = sigma_i / 2 (linking internal su(2) to spin generators)
    for i in range(1, 4):
        Si = spin_S(i)
        Bi = bivector_B(i)
        # S_i = -i * B_i
        from_bivector = -sp.I * Bi
        if matrices_close_exact(Si, from_bivector):
            pass_count += 1
        else:
            fail_count += 1
            failures.append(f"  FAIL: S_{i} != -i B_{i}")

    # [S_i, S_j] = i epsilon_{ijk} S_k (canonical su(2) commutator)
    for i in range(1, 4):
        for j in range(1, 4):
            comm = commutator(spin_S(i), spin_S(j))
            expected = sp.zeros(2, 2)
            for k in range(1, 4):
                expected += sp.I * eps(i, j, k) * spin_S(k)
            if matrices_close_exact(comm, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(f"  FAIL: [S_{i}, S_{j}] != i epsilon_{{{i}{j}k}} S_k")

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_3_so3_acts_on_bivectors_as_vectors():
    """Section 3: (M2) Under universal-property action phi_R for R in SO(3),
    the bivector subspace transforms as the SO(3) vector representation.

    Concretely: phi_R(B_i) = sum_j R_ij B_j for all proper R in O_h.
    """
    name = "Section 3: (M2) SO(3) acts on bivectors as vector rep"
    pass_count = 0
    fail_count = 0
    failures = []

    o_h = all_o_h_matrices()
    proper = [R for R in o_h if is_proper(R)]
    if len(proper) != 24:
        fail_count += 1
        failures.append(f"  FAIL: expected 24 proper O_h elements, got {len(proper)}")
    else:
        pass_count += 1

    # For each proper R, verify phi_R(B_i) = sum_j R_ij B_j on H_x.
    for R in proper:
        for i in range(1, 4):
            phi_Bi = phi_R_on_bivector(R, i)
            expected = sp.zeros(2, 2)
            for j in range(1, 4):
                expected += R[i - 1, j - 1] * bivector_B(j)
            if matrices_close_exact(phi_Bi, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(f"  FAIL: phi_R(B_{i}) != (R . B)_{i} for proper R = {R.tolist()}")

    # And on improper R (det = -1): phi_R(B_i) = +sum_j R_ij B_j as well,
    # because bivectors are even-degree elements (orientation-preserving).
    # Strictly: phi_R(gamma_a gamma_b) = phi_R(gamma_a) phi_R(gamma_b) = R_ac gamma_c R_bd gamma_d.
    # The induced action on the bivector basis is via R (acting as a vector rep on Lambda^2).
    # In 3D, Lambda^2(R^3) ~= R^3 via Hodge star with character sgn(det) absorbed
    # in the parity assignment of the pseudoscalar; on bivectors B_i (canonical basis)
    # the action is the adjugate cof(R) = det(R) R^{-T}; for signed-permutation R,
    # cof(R) is also a signed permutation (verified below).
    improper = [R for R in o_h if not is_proper(R)]
    if len(improper) != 24:
        fail_count += 1
        failures.append(f"  FAIL: expected 24 improper O_h elements, got {len(improper)}")
    else:
        pass_count += 1

    for R in improper:
        cof_R = cofactor_3x3(R)
        # cof(R) = det(R) * R^{-T} = -R^{-T} for improper rotations
        for i in range(1, 4):
            phi_Bi = phi_R_on_bivector(R, i)
            expected = sp.zeros(2, 2)
            for j in range(1, 4):
                expected += cof_R[i - 1, j - 1] * bivector_B(j)
            if matrices_close_exact(phi_Bi, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(
                    f"  FAIL: phi_R(B_{i}) != (cof(R) . B)_{i} for improper R"
                )

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_4_so3_to_su2_double_cover():
    """Section 4: (M3, M5) For each proper R in O_h, U(R) sigma_i U(R)^* = R . sigma.

    This verifies that the spinor lift of SO(3) on H_x = C^2 acts via the same
    generators sigma_i/2 = S_i that build the internal su(2). I.e., the
    "internal SU(2)" generators are literally the infinitesimal generators
    of the spatial Spin(3) action on H_x.
    """
    name = "Section 4: (M3, M5) SO(3) -> SU(2) double cover via U sigma_i U^*"
    pass_count = 0
    fail_count = 0
    failures = []

    o_h = all_o_h_matrices()
    proper = [R for R in o_h if is_proper(R)]

    for R in proper:
        # Construct U(R) using axis-angle / half-angle
        check = double_cover_check(R)
        if check is True:
            pass_count += 1
        else:
            fail_count += 1
            failures.append(f"  FAIL: U(R) sigma_i U(R)^* != R.sigma for R = {R.tolist()}")

    # Identity check: U(I) = +/- I_2; verify the +I_2 branch is consistent
    U_id = find_double_cover_U(sp.eye(3))
    if matrices_close_exact(U_id, I2):
        pass_count += 1
    else:
        fail_count += 1
        failures.append(f"  FAIL: U(I) != I_2; got {U_id}")

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_5_infinitesimal_coincidence():
    """Section 5: (M3) Infinitesimal generators of phi_R on H_x equal S_i.

    For R(t) = I + t * J_i + O(t^2) with [J_i]_{jk} = -epsilon_{ijk} (skew
    rotation generator about axis i), we have phi_{R(t)} = exp(t * X_i) on
    H_x for some X_i. Compute X_i and verify X_i = -i S_i (i.e., the
    infinitesimal generator of the rotation Spin(3) action on H_x = C^2
    is exactly the spin operator from the internal su(2)).

    Equivalently in the unitary convention U(R(t)) = exp(-i t S_i) + O(t^2),
    we have U(R(t)) sigma_a U(R(t))^* = (R(t) sigma)_a, and matching
    coefficients of t gives [-i S_i, sigma_a] = -epsilon_{iab} sigma_b,
    i.e., [S_i, sigma_a] = i epsilon_{iab} sigma_b. We verify this exactly.
    """
    name = "Section 5: (M3) Infinitesimal generator coincidence"
    pass_count = 0
    fail_count = 0
    failures = []

    def eps(i, j, k):
        if (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
            return 1
        if (i, j, k) in [(1, 3, 2), (2, 1, 3), (3, 2, 1)]:
            return -1
        return 0

    # [S_i, sigma_a] = i epsilon_{iab} sigma_b
    for i in range(1, 4):
        for a in range(1, 4):
            comm = commutator(spin_S(i), gamma(a))
            expected = sp.zeros(2, 2)
            for b in range(1, 4):
                expected += sp.I * eps(i, a, b) * gamma(b)
            if matrices_close_exact(comm, expected):
                pass_count += 1
            else:
                fail_count += 1
                failures.append(f"  FAIL: [S_{i}, sigma_{a}] != i epsilon_{{{i}{a}b}} sigma_b")

    # Verify that the bivector generators B_i (which build the internal su(2))
    # are EXACTLY (1/2) i sigma_i = i S_i, so the bivector lift Spin(3) -> SO(3)
    # is realized by the same generators as the internal su(2) on H_x.
    for i in range(1, 4):
        Bi = bivector_B(i)
        Si = spin_S(i)
        # B_i = (i/2) sigma_i = i * S_i
        if matrices_close_exact(Bi, sp.I * Si):
            pass_count += 1
        else:
            fail_count += 1
            failures.append(f"  FAIL: B_{i} != i * S_{i}")

    # The map  bivector B_i  <->  spin generator -i B_i = S_i
    # makes the algebraic identification operator-level (M3):
    # internal su(2) generators = spatial Spin(3) infinitesimal action on H_x.
    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_6_oh_signed_action():
    """Section 6: cubic O_h action on the Pauli generators.

    24 proper rotations are checked by ordinary SU(2) conjugation on H_x.
    24 improper rotations are checked as the signed Clifford-generator action
    phi_R(sigma_i) = sum_j R_ij sigma_j, implemented as parity sign times the
    proper SU(2) action for R' = -R. The improper checks are not ordinary
    complex-linear unitary conjugations on C^2; they are the real-Clifford
    universal-property action on the odd generators.
    """
    name = "Section 6: (M4) O_h proper lifts and improper signed actions"
    pass_count = 0
    fail_count = 0
    failures = []

    o_h = all_o_h_matrices()
    proper = [R for R in o_h if is_proper(R)]
    improper = [R for R in o_h if not is_proper(R)]

    # For each proper R, find U(R) using the row-vector convention; record matrices.
    proper_Us = []
    for R in proper:
        U = find_double_cover_U(R.T)
        proper_Us.append(U)

    # For each improper R, write R = (-I_3) R' with R' = -R proper.
    # The real-Clifford universal-property action on odd generators is
    # phi_R(sigma_i) = - phi_{R'}(sigma_i). This sign is not ordinary
    # complex-linear unitary conjugation by a 2x2 matrix on H_x. The runner
    # checks the signed generator action itself and keeps the ordinary
    # H_x lift claim restricted to proper rotations.

    # Verify proper-case explicitly (the substantive M4 content):
    for R, U in zip(proper, proper_Us):
        U_dag = U.H
        all_ok = True
        for i in range(3):
            lhs = sp.simplify(U * SIGMA[i] * U_dag)
            rhs = sp.zeros(2, 2)
            for j in range(3):
                rhs += R[i, j] * SIGMA[j]
            if not matrices_close_exact(lhs, rhs):
                all_ok = False
                break
        if all_ok:
            pass_count += 1
        else:
            fail_count += 1
            failures.append(
                f"  FAIL: U(R) sigma_i U^{{-1}} != phi_R(sigma_i) for proper R = {R.tolist()}"
            )

    # For improper R = parity * R_proper, verify the signed generator action:
    # phi_R(sigma_i) = -U(R_proper) sigma_i U(R_proper)^*.
    for R in improper:
        R_proper = -R  # det(-R) = (-1)^3 * (-1) = +1
        U_prime = find_double_cover_U(R_proper.T)
        all_ok = True
        for i in range(3):
            # phi_R(sigma_i) = - phi_{R'}(sigma_i) = -U' sigma_i U'^*
            lhs = sp.simplify(-U_prime * SIGMA[i] * U_prime.H)
            rhs = sp.zeros(2, 2)
            for j in range(3):
                rhs += R[i, j] * SIGMA[j]
            if not matrices_close_exact(lhs, rhs):
                all_ok = False
                break
        if all_ok:
            pass_count += 1
        else:
            fail_count += 1
            failures.append(
                f"  FAIL: -U(-R) sigma_i U(-R)^* != phi_R(sigma_i) for improper R = {R.tolist()}"
            )

    # Verify total count: 24 proper ordinary lifts plus 24 improper signed
    # generator-action checks.
    if len(proper_Us) == 24:
        pass_count += 1
    else:
        fail_count += 1
        failures.append(f"  FAIL: expected 24 proper lifts, got {len(proper_Us)}")

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_7_generator_frame_consistency():
    """Section 7: generator-frame consistency.

    Under the universal property + (M2) + (M3) + (M4) above, the gamma_i
    generators of the local Cl(3) carry the same Lie-algebra generator data
    as the spin-1/2 representation of Spin(3) on H_x. This section checks
    that the spatial-axis rotation generated by U(R) on H_x is the same
    operator data as the bivector-flow in the corresponding plane, since
    S_i = -i B_i.
    """
    name = "Section 7: generator-frame consistency"
    pass_count = 0
    fail_count = 0
    failures = []

    # Verify: for each i, the SO(3) generator about axis i, exponentiated
    # at angle t, conjugates sigma_a on H_x to (R . sigma)_a -- where
    # R . sigma uses the row-vector universal-property convention.
    #
    # The infinitesimal spatial generator on R^3 about axis i is the
    # antisymmetric matrix J_i with [J_i]_{jk} = -epsilon_{ijk}.
    # The lift to H_x is generated by S_i = sigma_i / 2 = -i B_i.
    # Concretely U(R(t)) = exp(-i t S_i) realizes the spatial rotation
    # on H_x = C^2 via conjugation.
    t = sp.pi / 2
    # Row-vector convention: phi_R(gamma_i) = sum_j R_ij gamma_j.
    # +pi/2 rotation about +x sending gamma_2 -> gamma_3 and gamma_3 -> -gamma_2
    # corresponds to R[1,:] = (0,0,1), R[2,:] = (0,-1,0). So
    # R = [[1,0,0], [0,0,1], [0,-1,0]] in row-convention.
    R1 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])

    # Internal/bivector lift to H_x: U_internal = exp(-i t S_1) = exp(-i t sigma_1 / 2)
    # Use applyfunc + expand_complex so sympy reduces exp(i pi / N) to closed form.
    U_internal_raw = (-sp.I * t * spin_S(1)).exp()
    U_internal = U_internal_raw.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))

    # Test: U_internal sigma_a U_internal^* = phi_R(sigma_a) = sum_b R[a,b] sigma_b
    for a in range(3):
        lhs = sp.simplify(U_internal * SIGMA[a] * U_internal.H)
        rhs = sp.zeros(2, 2)
        for b in range(3):
            rhs += R1[a, b] * SIGMA[b]
        if matrices_close_exact(lhs, rhs):
            pass_count += 1
        else:
            fail_count += 1
            failures.append(
                f"  FAIL: U_internal sigma_{a} U_internal^* != phi_R(sigma_{a}); "
                f"lhs={lhs}, rhs={rhs}"
            )

    # Cross-check: the bivector-flow exp(t B_1) on H_x acts as the INVERSE
    # rotation phi_{R^{-1}}(sigma_a) (since B_i = i S_i implies the flow
    # parameter direction is opposite). This is the same Lie group SU(2)
    # with two natural parametrizations that differ by sign of the flow
    # parameter.
    U_bivector_raw = (t * bivector_B(1)).exp()
    U_bivector = U_bivector_raw.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
    R1_inv = R1.inv()
    for a in range(3):
        lhs_bivector = sp.simplify(U_bivector * SIGMA[a] * U_bivector.inv())
        rhs_inv = sp.zeros(2, 2)
        for b in range(3):
            rhs_inv += R1_inv[a, b] * SIGMA[b]
        if matrices_close_exact(lhs_bivector, rhs_inv):
            pass_count += 1
        else:
            fail_count += 1
            failures.append(
                f"  FAIL: bivector-flow conjugation != phi_{{R^{{-1}}}}(sigma_{a})"
            )

    # Final coincidence: B_i = i S_i means the bivector subalgebra spanned
    # by {B_1, B_2, B_3} and the spin Lie algebra span_{S_1, S_2, S_3} are
    # the SAME real Lie algebra (with one differing by an overall factor
    # of i, both isomorphic to su(2)). Confirm the operator-level identity
    # at a single representative point.
    if matrices_close_exact(spin_S(1), -sp.I * bivector_B(1)):
        pass_count += 1
    else:
        fail_count += 1
        failures.append("  FAIL: S_1 != -i * B_1")

    print(f"{name}: PASS={pass_count} FAIL={fail_count}")
    for f in failures:
        print(f)
    return pass_count, fail_count


def run_section_8_summary():
    """Section 8: Print operator-level conclusion summary."""
    name = "Section 8: Summary (operator-level identification)"
    print(name)
    print("  The internal su(2) generators on H_x = C^2 are S_i = sigma_i / 2.")
    print("  The infinitesimal spatial Spin(3) action on H_x via the universal")
    print("  property of Cl(3,0) is also generated by S_i = sigma_i / 2.")
    print("  These are the SAME OPERATORS, not merely isomorphic.")
    print("  Identification 'internal SU(2) = spatial Spin(3)' is a corollary")
    print("  of the one-qubit Cl(3,0) algebraic data, not an additional axiom.")
    return 0, 0


def main():
    total_pass = 0
    total_fail = 0

    sections = [
        run_section_1_pauli_sanity,
        run_section_2_internal_su2,
        run_section_3_so3_acts_on_bivectors_as_vectors,
        run_section_4_so3_to_su2_double_cover,
        run_section_5_infinitesimal_coincidence,
        run_section_6_oh_signed_action,
        run_section_7_generator_frame_consistency,
        run_section_8_summary,
    ]
    for sec in sections:
        p, f = sec()
        total_pass += p
        total_fail += f
        print()

    print(f"TOTAL: PASS={total_pass} FAIL={total_fail}")
    sys.exit(0 if total_fail == 0 else 1)


if __name__ == "__main__":
    main()
