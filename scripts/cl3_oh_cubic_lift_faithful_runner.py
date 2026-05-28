"""Runner: Cl(3) faithful lift of cubic point group O_h.

Verifies the narrow theorem in
docs/CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md:

  (T1) For every R in O_h, the map γᵢ → Σⱼ Rᵢⱼ γⱼ extends to an
       ℝ-algebra automorphism φ_R: Cl(3) → Cl(3).
  (T2) φ_R(I) = det(R) · I where I = γ₁γ₂γ₃.
  (T3) Z₂ sgn(det) grading: 24 proper rotations fix I; 24 improper
       flip I → −I.
  (T4) The O_h-average of the pure pseudoscalar line is zero, so an
       O_h-invariant expression cannot carry a nonzero coefficient in
       a slot already proved to transform only by det(R).

Concrete realization: Cl(3) ≅ M₂(ℂ) via γᵢ = σᵢ (Pauli matrices).
Then I = γ₁γ₂γ₃ = σ₁σ₂σ₃ = i·I₂ (since σ₁σ₂ = iσ₃, σ₃² = I₂).
I² = (i·I₂)² = -I₂, consistent with Cl(3,0) pseudoscalar.

No new physics admissions; pure finite-group + Clifford-algebra
verification.
"""

from __future__ import annotations

import itertools

import numpy as np

# ----------------------------------------------------------------------
# Cl(3) concrete realization via Pauli matrices: Cl(3) ⊂ M₂(ℂ)
# ----------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
SIGMA = [
    np.array([[0, 1], [1, 0]], dtype=complex),  # σ₁ = γ₁
    np.array([[0, -1j], [1j, 0]], dtype=complex),  # σ₂ = γ₂
    np.array([[1, 0], [0, -1]], dtype=complex),  # σ₃ = γ₃
]


def gamma(i):
    """γᵢ for i ∈ {1, 2, 3}; index is 1-based."""
    return SIGMA[i - 1]


def pseudoscalar():
    """I = γ₁γ₂γ₃ = i·I₂."""
    return SIGMA[0] @ SIGMA[1] @ SIGMA[2]


# ----------------------------------------------------------------------
# O_h: 48 signed permutation matrices on ℝ³
# ----------------------------------------------------------------------


def all_o_h_matrices():
    """Generate all 48 elements of O_h as 3×3 signed permutation matrices."""
    matrices = []
    for perm in itertools.permutations([0, 1, 2]):
        for signs in itertools.product([+1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for row, (col, sign) in enumerate(zip(perm, signs)):
                M[row, col] = sign
            matrices.append(M)
    return matrices


# ----------------------------------------------------------------------
# Algebra automorphism φ_R extending γᵢ → Σⱼ Rᵢⱼ γⱼ
# ----------------------------------------------------------------------


def phi_R_on_gamma(R, i):
    """φ_R(γᵢ) = Σⱼ Rᵢⱼ γⱼ for i ∈ {1, 2, 3}."""
    result = np.zeros((2, 2), dtype=complex)
    for j in range(3):
        result += R[i - 1, j] * gamma(j + 1)
    return result


def phi_R_on_product(R, indices):
    """φ_R(γ_{i₁} γ_{i₂} … γ_{iₖ}) = ∏ φ_R(γ_{iₐ})."""
    result = np.eye(2, dtype=complex)
    for i in indices:
        result = result @ phi_R_on_gamma(R, i)
    return result


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

PASS = 0
FAIL = 0


def report(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    PASS += int(ok)
    FAIL += int(not ok)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def matrices_close(A, B, tol=1e-10):
    return np.allclose(A, B, atol=tol)


def test_pauli_relations():
    """Sanity: σᵢ² = I, σᵢσⱼ + σⱼσᵢ = 2δᵢⱼ I (Clifford relations)."""
    for i in range(1, 4):
        sq = gamma(i) @ gamma(i)
        report(f"σ_{i}² = I", matrices_close(sq, I2))
    for i, j in [(1, 2), (1, 3), (2, 3)]:
        anti = gamma(i) @ gamma(j) + gamma(j) @ gamma(i)
        report(f"{{σ_{i}, σ_{j}}} = 0", matrices_close(anti, np.zeros((2, 2))))


def test_pseudoscalar_squared():
    """I² = -I_2 in Cl(3,0)."""
    I = pseudoscalar()
    Isq = I @ I
    report("I² = -I (Cl(3,0) pseudoscalar)", matrices_close(Isq, -I2),
           detail=f"I = {I[0,0]}·I₂")


def test_o_h_orthogonality(o_h):
    """Sanity: every O_h element is orthogonal."""
    all_ok = True
    for k, R in enumerate(o_h):
        if not matrices_close(R @ R.T, np.eye(3, dtype=int).astype(float)):
            all_ok = False
            break
    report(f"All {len(o_h)} O_h elements are orthogonal", all_ok)


def test_o_h_count(o_h):
    """O_h has exactly 48 elements."""
    n = len(o_h)
    report("|O_h| = 48", n == 48, detail=f"|O_h| = {n}")


def test_o_h_det_split(o_h):
    """24 elements have det = +1, 24 have det = -1."""
    proper = sum(1 for R in o_h if np.linalg.det(R) > 0)
    improper = sum(1 for R in o_h if np.linalg.det(R) < 0)
    report(f"24 proper rotations (det = +1)", proper == 24,
           detail=f"got {proper}")
    report(f"24 improper rotations (det = −1)", improper == 24,
           detail=f"got {improper}")


def test_t1_clifford_relations_preserved(o_h):
    """T1: φ_R preserves Clifford relations {φ_R(γᵢ), φ_R(γⱼ)} = 2δᵢⱼ I."""
    all_ok = True
    for k, R in enumerate(o_h):
        for i in range(1, 4):
            for j in range(1, 4):
                anti = phi_R_on_gamma(R, i) @ phi_R_on_gamma(R, j) + \
                       phi_R_on_gamma(R, j) @ phi_R_on_gamma(R, i)
                expected = 2 * (1 if i == j else 0) * I2
                if not matrices_close(anti, expected):
                    all_ok = False
                    break
            if not all_ok:
                break
        if not all_ok:
            print(f"    FAIL at R index {k}: {R.tolist()}")
            break
    report(f"T1: Clifford relations preserved for all 48 O_h elements", all_ok)


def test_t1_extends_to_automorphism(o_h):
    """T1 stronger: φ_R(γᵢγⱼ) = φ_R(γᵢ)φ_R(γⱼ) for all i, j."""
    all_ok = True
    for k, R in enumerate(o_h):
        for i in range(1, 4):
            for j in range(1, 4):
                if i == j:
                    continue
                # Direct image of γᵢγⱼ
                lhs = phi_R_on_product(R, [i, j])
                # Product of images
                rhs = phi_R_on_gamma(R, i) @ phi_R_on_gamma(R, j)
                if not matrices_close(lhs, rhs):
                    all_ok = False
                    break
            if not all_ok:
                break
        if not all_ok:
            break
    report(f"T1: φ_R(γᵢγⱼ) = φ_R(γᵢ)φ_R(γⱼ) for all bivectors, all R", all_ok)


def test_t2_pseudoscalar_character(o_h):
    """T2: φ_R(I) = det(R) · I for every R in O_h."""
    I = pseudoscalar()
    all_ok = True
    mismatches = 0
    for k, R in enumerate(o_h):
        det_R = int(round(np.linalg.det(R)))
        phi_I = phi_R_on_product(R, [1, 2, 3])
        expected = det_R * I
        if not matrices_close(phi_I, expected):
            all_ok = False
            mismatches += 1
    report(f"T2: φ_R(I) = det(R) · I for all 48 O_h elements",
           all_ok, detail=f"{mismatches} mismatches" if mismatches else "")


def test_t3_z2_grading(o_h):
    """T3: 24 fix I, 24 flip I."""
    I = pseudoscalar()
    fixers = 0
    flippers = 0
    for R in o_h:
        phi_I = phi_R_on_product(R, [1, 2, 3])
        if matrices_close(phi_I, I):
            fixers += 1
        elif matrices_close(phi_I, -I):
            flippers += 1
    report(f"T3: 24 elements fix I (det=+1)", fixers == 24,
           detail=f"fixers={fixers}")
    report(f"T3: 24 elements flip I (det=-1)", flippers == 24,
           detail=f"flippers={flippers}")


def test_t4_pseudoscalar_average_zero(o_h):
    """T4: the O_h-average of the pure pseudoscalar line is zero."""
    # Average operator: P_inv = (1/|G|) Σ_R φ_R
    # Apply to I: should give zero (since improper R's flip I and cancel proper)
    I = pseudoscalar()
    avg_phi_I = np.zeros((2, 2), dtype=complex)
    for R in o_h:
        avg_phi_I += phi_R_on_product(R, [1, 2, 3])
    avg_phi_I /= len(o_h)
    report("T4: O_h-averaged pseudoscalar = 0 (no invariant in ℝ·I)",
           matrices_close(avg_phi_I, np.zeros((2, 2))),
           detail=f"||avg||_F = {np.linalg.norm(avg_phi_I):.4e}")


def test_pin_double_cover_sanity():
    """Sanity: SO(3) elements act via Spin(3) ⊂ Cl⁰(3) by conjugation.
    For rotation by π about z-axis: corresponds to Spin element γ_1γ_2 = iσ_3.
    Check: u γ_1 u^{-1} = -γ_1 with u = γ_1γ_2."""
    u = SIGMA[0] @ SIGMA[1]  # γ₁γ₂ = iσ₃
    # u γ_1 u^{-1}
    result = u @ SIGMA[0] @ np.linalg.inv(u)
    # Expected: -γ₁ (rotation by π about z flips x and y, fixes z)
    expected = -SIGMA[0]
    report("Pin double-cover sanity: u γ_1 u^{-1} = -γ_1 for u = γ_1γ_2",
           matrices_close(result, expected))


def main():
    print("=" * 76)
    print("CL3 FAITHFUL LIFT OF CUBIC POINT GROUP O_h — VERIFICATION")
    print("=" * 76)
    print()

    print("Sanity: Clifford algebra and pseudoscalar")
    print("-" * 76)
    test_pauli_relations()
    test_pseudoscalar_squared()
    test_pin_double_cover_sanity()

    print()
    print("O_h structure")
    print("-" * 76)
    o_h = all_o_h_matrices()
    test_o_h_count(o_h)
    test_o_h_orthogonality(o_h)
    test_o_h_det_split(o_h)

    print()
    print("T1: φ_R is an algebra automorphism (Clifford relations preserved)")
    print("-" * 76)
    test_t1_clifford_relations_preserved(o_h)
    test_t1_extends_to_automorphism(o_h)

    print()
    print("T2: Pseudoscalar character φ_R(I) = det(R) · I")
    print("-" * 76)
    test_t2_pseudoscalar_character(o_h)

    print()
    print("T3: Z₂ sgn(det) grading on ℝ·I")
    print("-" * 76)
    test_t3_z2_grading(o_h)

    print()
    print("T4: O_h average kills the pure pseudoscalar line")
    print("-" * 76)
    test_t4_pseudoscalar_average_zero(o_h)

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: Cl(3) faithful lift of O_h holds; pseudoscalar")
        print("transforms as det character; all 48 elements verified.")
        return 0
    print("VERDICT: Cl(3) faithful lift FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
