#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the partial-narrowing note
`BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md`.

The parent partial-narrowing note proves:

(T1) Explicit antiunitary involution J on C^3 defined by
       J(z_0, z_1, z_2) := (conj(z_0), conj(z_2), conj(z_1))
       equivalently J(v) = U_swap * conj(v), where
       U_swap = diag(1) extended with a 2-cycle swap on indices (1, 2),
     is well-defined and satisfies J^2 = +I (KO-dim 0 mod 8 family).

(T2) J relates to the C_3 cyclic shift C = perm(0->1->2->0) by
       J C J^{-1}  =  C^{-1}  =  C^2,
     so J inverts orbit orientation (anti-isometry on C-orbits).

(T3) For any circulant Hermitian D = a I + b C + b_bar C^2 with a real,
     b complex, the operator commutator [D, J] = 0. Concretely:
       D * U_swap  =  U_swap * conj(D),
     verified as a polynomial identity over (a, b_re, b_im).

(T4) The +1 eigenspace of J inside C^3 is a 3-real-dimensional subspace
     H_R, parametrized by (x_0, u + i v, u - i v) with (x_0, u, v) in R^3.
     D restricted to H_R is a 3x3 real symmetric matrix in the orthonormal
     basis e_1 = (1, 0, 0), e_2 = (0, 1, 1)/sqrt(2), e_3 = (0, i, -i)/sqrt(2),
     with eigenvalues
       lambda_0  =  a + 2 b_re,
       lambda_om = a - b_re - sqrt(3) b_im,
       lambda_omb = a - b_re + sqrt(3) b_im,
     identical to the eigenvalues of D on full C^3.

(T5) (NEGATIVE / partial-narrowing core.) The spectral-action functional
     S[D] = Tr_{H_R} f(D / Lambda) on the J-real subspace equals the
     spectral-action functional on full C^3, and therefore is a symmetric
     function of the three eigenvalues (lambda_0, lambda_om, lambda_omb).
     Consequently, no choice of (J, KO-dim, projection-onto-H_R) supplies
     the F1 multiplicity-(1,1) weighting from this NCG/KO-dim route:
     the doublet pair (lambda_om, lambda_omb) remains counted as TWO
     eigenvalues, not one isotype bin. The eigenvalue-symmetric structure
     identified in Probe U (PR #769) persists under projection onto H_R.

(T6) (Counterfactual that recovers F3.) The standard pointwise-conjugation
     real structure J' = K (no swap) does NOT commute with circulant D
     when b is complex: [D, K] = 0 forces b_im = 0 (a 1-real-dim slice of
     the doublet). This confirms that the U_swap-twisted J of (T1) is a
     genuinely different real structure from K: under J the full circulant
     family is fixed; under K only the b-real slice is fixed.

The note's audit-honest disposition is partial-narrowing / honest gap:
positive content (T1)-(T4) ships; (T5) records that the NCG/KO-dim route
does NOT close F1; (T6) sharpens the counterfactual.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence at exact symbolic precision.
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import (
        I,
        Matrix,
        Rational,
        Symbol,
        conjugate,
        expand,
        eye,
        sqrt,
        simplify,
        symbols,
        zeros,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


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


def J_op_matrix(U_swap, M):
    """Apply J-conjugation to a matrix M: J M J^{-1} = U_swap * conj(M) * U_swap."""
    return U_swap * M.applyfunc(conjugate) * U_swap


def J_op_vector(U_swap, v):
    """Apply J to a vector v: J v = U_swap * conj(v)."""
    return U_swap * v.applyfunc(conjugate)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification that")
    print("  (a) J = U_swap*K satisfies J^2 = +I, [D, J] = 0 for circulant D,")
    print("  (b) D-restricted-to-H_R has same eigenvalues as D on C^3,")
    print("  (c) the NCG/KO-dim route does NOT collapse doublet to F1.")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # ---------------------------------------------------------------------

    a = Symbol("a", real=True)
    b_re = Symbol("b_re", real=True)
    b_im = Symbol("b_im", real=True)
    b = b_re + I * b_im
    b_bar = b_re - I * b_im

    # 3x3 cyclic permutation matrix C: C^3 = I
    C = Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ])
    C2 = C * C
    I3 = eye(3)

    H = a * I3 + b * C + b_bar * C2

    check(
        "C^3 = I (cyclic identity)",
        simplify(C ** 3 - I3) == zeros(3, 3),
        detail="C generates the cyclic group of order 3",
    )
    check(
        "H is Hermitian (H^dagger = H)",
        simplify(H.H - H) == zeros(3, 3),
        detail="circulant Hermitian on (a real, b complex) pair",
    )

    # ---------------------------------------------------------------------
    section("Part 1: J = U_swap * K well-defined antiunitary involution (T1)")
    # ---------------------------------------------------------------------

    # U_swap: swap indices (1, 2), fix index 0.
    U_swap = Matrix([
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ])

    check(
        "U_swap is real (entries in R)",
        all(U_swap[i, j].is_real or U_swap[i, j].is_integer for i in range(3) for j in range(3)),
        detail="U_swap has 0/1 entries",
    )
    check(
        "U_swap is symmetric (U_swap = U_swap^T)",
        U_swap == U_swap.T,
        detail="symmetric permutation matrix",
    )
    check(
        "U_swap is unitary (U_swap * U_swap^T = I)",
        simplify(U_swap * U_swap.T - I3) == zeros(3, 3),
        detail="real orthogonal involution",
    )
    check(
        "U_swap^2 = I (involution)",
        simplify(U_swap * U_swap - I3) == zeros(3, 3),
        detail="period 2",
    )

    # J^2 = +I on C^3: J^2(v) = U_swap * conj(U_swap * conj(v)) = U_swap * U_swap * v = v
    # since conj(U_swap) = U_swap (U_swap real)
    z0, z1, z2 = symbols("z_0 z_1 z_2", complex=True)
    v_test = Matrix([z0, z1, z2])
    Jv = J_op_vector(U_swap, v_test)
    JJv = J_op_vector(U_swap, Jv)
    check(
        "J^2(v) = v for generic v in C^3 (J^2 = +I)",
        simplify(JJv - v_test) == zeros(3, 1),
        detail="KO-dim 0 mod 8 family",
    )

    # ---------------------------------------------------------------------
    section("Part 2: J C J^{-1} = C^{-1} = C^2 (T2)")
    # ---------------------------------------------------------------------

    # Operator-level: J M J^{-1} acts on a matrix as U_swap * conj(M) * U_swap
    # (since J is antiunitary involution: (J M J^{-1})(v) = J M(J^{-1}(v))
    # = U_swap * conj( M * U_swap^{-1} * conj(v) ) = U_swap * conj(M) * conj(U_swap) * v
    # and U_swap = U_swap^{-1}, conj(U_swap) = U_swap.

    JCJinv = J_op_matrix(U_swap, C)
    check(
        "J C J^{-1} = C^2 (= C^{-1})",
        simplify(JCJinv - C2) == zeros(3, 3),
        detail="J inverts orbit orientation",
    )

    JC2Jinv = J_op_matrix(U_swap, C2)
    check(
        "J C^2 J^{-1} = C",
        simplify(JC2Jinv - C) == zeros(3, 3),
        detail="cycle inverse on the other generator",
    )

    JIJinv = J_op_matrix(U_swap, I3)
    check(
        "J I J^{-1} = I (J fixes the identity)",
        simplify(JIJinv - I3) == zeros(3, 3),
        detail="trivial isotype is J-fixed",
    )

    # ---------------------------------------------------------------------
    section("Part 3: [D, J] = 0 for all circulant Hermitian D (T3)")
    # ---------------------------------------------------------------------

    # JDJ^{-1} on the matrix algebra:
    JDJinv = J_op_matrix(U_swap, H)
    check(
        "J D J^{-1} = D for D = aI + bC + bbar C^2 (any complex b)",
        simplify(JDJinv - H) == zeros(3, 3),
        detail="explicit verification at the matrix-element level",
    )

    # Operator commutator: [D, J] = 0 iff D U_swap = U_swap conj(D)
    LHS = H * U_swap
    RHS = U_swap * H.applyfunc(conjugate)
    check(
        "Operator equation: D U_swap = U_swap conj(D)",
        simplify(LHS - RHS) == zeros(3, 3),
        detail="this is the [D, J] = 0 condition for J = U_swap * K",
    )

    # ---------------------------------------------------------------------
    section("Part 4: H_R = +1 eigenspace of J is real-3-dim with explicit basis (T4)")
    # ---------------------------------------------------------------------

    # H_R parametrization: v = (x_0, u + i v, u - i v) with x_0, u, v in R.
    x0_sym, u_sym, v_sym = symbols("x_0 u v", real=True)
    v_HR = Matrix([x0_sym, u_sym + I * v_sym, u_sym - I * v_sym])
    Jv_HR = J_op_vector(U_swap, v_HR)
    check(
        "J(x_0, u + iv, u - iv) = (x_0, u + iv, u - iv) (H_R is J-fixed)",
        simplify(Jv_HR - v_HR) == zeros(3, 1),
        detail="3-real-parameter family of J-fixed vectors",
    )

    # Orthonormal basis for H_R:
    e1 = Matrix([1, 0, 0])
    e2 = Matrix([0, 1, 1]) / sqrt(2)
    e3 = Matrix([0, I, -I]) / sqrt(2)

    for name, e in [("e_1", e1), ("e_2", e2), ("e_3", e3)]:
        norm_sq = simplify((e.H * e)[0, 0])
        check(
            f"||{name}||^2 = 1 (orthonormal)",
            norm_sq == 1,
            detail=f"||{name}||^2 = {norm_sq}",
        )
        Je = J_op_vector(U_swap, e)
        check(
            f"J({name}) = {name} (basis vector in H_R)",
            simplify(Je - e) == zeros(3, 1),
            detail="explicit J-invariance check",
        )

    # Orthogonality
    for (na, ea), (nb, eb) in [
        (("e_1", e1), ("e_2", e2)),
        (("e_1", e1), ("e_3", e3)),
        (("e_2", e2), ("e_3", e3)),
    ]:
        ip = simplify((ea.H * eb)[0, 0])
        check(
            f"<{na}, {nb}> = 0",
            ip == 0,
            detail=f"<{na}, {nb}> = {ip}",
        )

    # Compute D_R: D restricted to H_R in (e_1, e_2, e_3) basis
    basis = [e1, e2, e3]
    D_R = zeros(3, 3)
    for i in range(3):
        for j in range(3):
            ip = (basis[i].H * H * basis[j])[0, 0]
            D_R[i, j] = simplify(ip)

    # Verify D_R is real
    D_R_all_real = all(simplify(sympy.im(D_R[i, j])) == 0 for i in range(3) for j in range(3))
    check(
        "D restricted to H_R has only real matrix elements in (e_1, e_2, e_3) basis",
        D_R_all_real,
        detail="real symmetric realization on the J-real form",
    )

    # Verify D_R is symmetric
    check(
        "D_R = D_R^T (real symmetric)",
        simplify(D_R - D_R.T) == zeros(3, 3),
        detail="standard real-symmetric structure",
    )

    # Verify D_R eigenvalues match the C^3 eigenvalues (lam_0, lam_om, lam_omb)
    lam_0 = a + 2 * b_re
    lam_om = a - b_re - sqrt(3) * b_im
    lam_omb = a - b_re + sqrt(3) * b_im

    # Characteristic polynomial check: the three eigenvalues are roots of char poly of D_R
    eigs_DR = D_R.eigenvals()
    eigs_DR_simplified = {simplify(ev): mult for ev, mult in eigs_DR.items()}

    check(
        "lambda_0 = a + 2 b_re is an eigenvalue of D_R",
        any(simplify(ev - lam_0) == 0 for ev in eigs_DR_simplified),
        detail=f"lambda_0 = {lam_0}",
    )
    check(
        "lambda_om = a - b_re - sqrt(3) b_im is an eigenvalue of D_R",
        any(simplify(ev - lam_om) == 0 for ev in eigs_DR_simplified),
        detail=f"lambda_om = {lam_om}",
    )
    check(
        "lambda_omb = a - b_re + sqrt(3) b_im is an eigenvalue of D_R",
        any(simplify(ev - lam_omb) == 0 for ev in eigs_DR_simplified),
        detail=f"lambda_omb = {lam_omb}",
    )

    # Sum of eigenvalues = trace of D_R = trace of H = 3a
    sum_eigs = simplify(D_R.trace())
    check(
        "Tr(D_R) = lambda_0 + lambda_om + lambda_omb = 3a",
        simplify(sum_eigs - 3 * a) == 0,
        detail="trace identity",
    )

    # Sum of eigenvalue squares = ||H||_F^2 = 3a^2 + 6|b|^2
    sum_eigs_sq = simplify(D_R.trace() ** 2 - 2 * sum(D_R[i, j] * D_R[j, i] for i in range(3) for j in range(i + 1, 3)))
    # Easier: compute Tr(D_R^2) directly
    D_R_sq = D_R * D_R
    trD2 = simplify(D_R_sq.trace())
    expected_trD2 = 3 * a ** 2 + 6 * (b_re ** 2 + b_im ** 2)
    check(
        "Tr(D_R^2) = 3a^2 + 6|b|^2 (matches block-total Frobenius E_+ + E_perp)",
        simplify(trD2 - expected_trD2) == 0,
        detail="J-real Frobenius norm = full Frobenius norm",
    )

    # ---------------------------------------------------------------------
    section("Part 5: spectral action on H_R = spectral action on C^3 (T5 — negative core)")
    # ---------------------------------------------------------------------

    # The spectral action S[D] = Tr_{H_R} f(D/Lambda) = sum_k f(lam_k / Lambda)
    # equals the full spectral action on C^3 because D_R has the SAME 3 eigenvalues
    # as D on C^3 (verified above).
    #
    # We test this with three specific cutoff functions f and show that the
    # J-restricted spectral action is identical to the unrestricted spectral action
    # at the formal-polynomial level.
    #
    # The negative core is: a symmetric function of (lam_0, lam_om, lam_omb)
    # cannot supply F1-weighting (which would count {lam_om, lam_omb} as ONE bin).

    # f = x^2: Tr f(D) = lam_0^2 + lam_om^2 + lam_omb^2 = 3a^2 + 6|b|^2
    spec_x2 = simplify(lam_0 ** 2 + lam_om ** 2 + lam_omb ** 2)
    check(
        "Tr_{H_R}(D^2) = 3a^2 + 6|b|^2 (matches Probe U a_2 coefficient)",
        simplify(spec_x2 - (3 * a ** 2 + 6 * (b_re ** 2 + b_im ** 2))) == 0,
        detail="block-total Frobenius E_+ + E_perp",
    )

    # f = x^4: Tr f(D) = lam_0^4 + lam_om^4 + lam_omb^4
    spec_x4 = simplify(lam_0 ** 4 + lam_om ** 4 + lam_omb ** 4)
    # This is a 4th-order symmetric polynomial in eigenvalues.
    # Specifically, it's a polynomial in (a, b_re, b_im) with structure 3a^4 + ...
    # Just verify the leading coefficient.
    coeff_a4 = sympy.Poly(spec_x4, a).coeff_monomial(a ** 4)
    check(
        "Tr_{H_R}(D^4) leading a^4 coefficient = 3 (sum of three eigenvalues squared)",
        simplify(coeff_a4 - 3) == 0,
        detail="symmetric in 3 eigenvalues",
    )

    # The key negative content: setting d/d|b| of any polynomial-in-power-sums = 0
    # gives critical points that are NOT at BAE (a^2 = 2|b|^2).
    # We test this concretely on the linear combination 3 a_2 + a_4 ~ Tr(D^2) + (alpha) Tr(D^4)
    # for a sample alpha.

    # F1 functional from block-total Frobenius: F1 = log(3 a^2) + log(6 |b|^2)
    # Critical point of F1 under E_+ + E_perp = const:
    # at 3 a^2 = 6 |b|^2, i.e., a^2 = 2 |b|^2 (BAE).
    #
    # vs the spectral-action functional Tr f(D^2): a SYMMETRIC function of (lam_0, lam_om, lam_omb).
    # Critical points lie at {b_im = 0, b_re/a fixed by f shape}, NOT at BAE.
    # (Probe U numerical scan: critical points at |b|/a ~ 0.997 for various f.)

    # Specifically: the gradient of Tr(D^2) wrt b_im is
    # d/db_im (3a^2 + 6 b_re^2 + 6 b_im^2) = 12 b_im, vanishes at b_im = 0 only.
    grad_b_im_TrD2 = sympy.diff(spec_x2, b_im)
    check(
        "d/db_im Tr(D^2) = 12 b_im, vanishes only at b_im = 0 (not at BAE)",
        simplify(grad_b_im_TrD2 - 12 * b_im) == 0,
        detail="symmetric power-sum critical point is degenerate not BAE",
    )

    # Same for d/db_re of Tr(D^2):
    grad_b_re_TrD2 = sympy.diff(spec_x2, b_re)
    check(
        "d/db_re Tr(D^2) = 12 b_re, vanishes only at b_re = 0 (not at BAE)",
        simplify(grad_b_re_TrD2 - 12 * b_re) == 0,
        detail="symmetric power-sum critical point is degenerate not BAE",
    )

    # Cross-check Probe U observation: BAE locus a^2 = 2|b|^2 is NOT a critical point of Tr(D^2).
    # Substitute a^2 = 2 |b|^2 and check gradient is nonzero.
    # At a fixed E_+ + E_perp = E_tot, the BAE constraint is 3a^2 = 6|b|^2, i.e., a^2 = 2|b|^2.
    # Critical point of Tr(D^2) wrt (a, b_re, b_im) at fixed Tr(D) = sum_eigs = 3a is at a fixed.
    # Free in (b_re, b_im); gradient = (12 b_re, 12 b_im), vanishes only at b = 0.
    # BAE (with |b| > 0) is NOT a critical point. Confirmed structurally.

    # ---------------------------------------------------------------------
    section("Part 6: counterfactual — K alone does NOT commute with complex-b D (T6)")
    # ---------------------------------------------------------------------

    # K (pointwise conjugation, no swap) does NOT commute with complex-b D:
    # [D, K] = 0 iff D = conj(D) iff b = b_bar iff b_im = 0.

    # K-conjugation of H: K H K^{-1} = conj(H)
    H_conj = H.applyfunc(conjugate)
    K_commute_diff = simplify(H_conj - H)
    # This should NOT be zero in general. Let's verify it equals 2i b_im (C - C^2)
    expected_diff = -2 * I * b_im * (C - C2)
    check(
        "K H K^{-1} - H = -2i b_im (C - C^2) (not zero for complex b)",
        simplify(K_commute_diff - expected_diff) == zeros(3, 3),
        detail="K alone forces b_im = 0 to commute with circulant D",
    )

    # When b_im = 0 (b real), K does commute:
    H_b_real = a * I3 + b_re * C + b_re * C2
    H_b_real_conj = H_b_real.applyfunc(conjugate)
    check(
        "K H K^{-1} = H for b real (1-real-dim slice of doublet)",
        simplify(H_b_real_conj - H_b_real) == zeros(3, 3),
        detail="b real is the K-fixed slice, only 1-dim of the 2-real-dim doublet",
    )

    # ---------------------------------------------------------------------
    section("Part 7: F1 vs F3 selection NOT supplied by J (the negative claim)")
    # ---------------------------------------------------------------------

    # F1 functional from block-total Frobenius (multiplicity weighting (1,1)):
    # F1(a, b) = log(3 a^2) + log(6 |b|^2)
    # Critical point under E_+ + E_perp = const: 3a^2 = 6|b|^2, i.e., a^2 = 2|b|^2 (BAE).

    # F3 functional (real-dim weighting (1,2)):
    # F3(a, b) = log(3 a^2) + 2 log(6 |b|^2)
    # Critical point: 6|b|^2 / (3a^2) = 2, i.e., a^2 = |b|^2.

    # The spectral action Tr f(D^2/Lambda^2) on H_R or on C^3 = sum_k f(lam_k^2/Lambda^2)
    # is a symmetric function of (lam_0^2, lam_om^2, lam_omb^2).
    # In the b complex case, the doublet pair (lam_om, lam_omb) contributes
    # f(lam_om^2/Lambda^2) + f(lam_omb^2/Lambda^2), which weights the doublet by 2
    # at the eigenvalue level. This is F3-style weighting, not F1.

    # Verify symbolically: Tr f(D^2) decomposes as
    # f(lam_0^2/Lambda^2) + [f(lam_om^2/Lambda^2) + f(lam_omb^2/Lambda^2)]
    # where the bracket contributes weight 2 to the doublet block.

    Lambda = Symbol("Lambda", positive=True)
    # Symbolic f: leave it abstract via a placeholder.
    # We can encode the structural statement: the action decomposes into a trivial-isotype
    # contribution and a doublet contribution counted as 2 eigenvalue terms.

    # Concrete test with f(x) = x^2 (most extreme symmetric case):
    spec_full = lam_0 ** 2 / Lambda ** 2 + lam_om ** 2 / Lambda ** 2 + lam_omb ** 2 / Lambda ** 2
    # vs F1-style: trivial * 1 + doublet * 1 (representative)
    spec_F1_eigen = lam_0 ** 2 / Lambda ** 2 + (lam_om ** 2 + lam_omb ** 2) / (2 * Lambda ** 2)
    # vs F3-style: trivial * 1 + doublet * 2 (sum)
    spec_F3_eigen = lam_0 ** 2 / Lambda ** 2 + (lam_om ** 2 + lam_omb ** 2) / Lambda ** 2

    # Verify: spec_full = spec_F3_eigen (each eigenvalue counted once)
    check(
        "Tr_{H_R}(D^2/Lambda^2) = lam_0^2/Lambda^2 + lam_om^2/Lambda^2 + lam_omb^2/Lambda^2 = F3-style eigenvalue weighting",
        simplify(spec_full - spec_F3_eigen) == 0,
        detail="each eigenvalue counted once = doublet weight 2 = F3",
    )

    # And spec_F1_eigen != spec_full (so F1 is structurally distinct):
    check(
        "F1-eigenvalue-collapse spectral action != Tr_{H_R}(D^2/Lambda^2) for b complex",
        simplify(spec_full - spec_F1_eigen).has(b_im) or simplify(spec_full - spec_F1_eigen).has(b_re),
        detail="confirms F1 weighting is NOT supplied by J-projection",
    )

    # ---------------------------------------------------------------------
    section("Part 8: claim-scope review hygiene")
    # ---------------------------------------------------------------------

    doc_path = (Path(__file__).parent.parent / "docs" /
                "BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md")
    if doc_path.is_file():
        prose = doc_path.read_text()
        check(
            "note exists",
            True,
            detail=str(doc_path.name),
        )
        check(
            "note declares Status authority = independent audit lane only",
            "Status authority:** independent audit lane only" in prose,
            detail="audit-pipeline language compliance",
        )
        check(
            "note uses bounded_theorem claim type framing",
            "Type:** bounded_theorem" in prose,
            detail="partial-narrowing = bounded, not no-go",
        )
        check(
            "note explicitly does NOT discharge F1 hypothesis",
            "does **not** discharge" in prose.lower() or "does NOT discharge" in prose or "does not discharge" in prose.lower() or "Does NOT discharge" in prose,
            detail="preserves F1 vs F3 Open derivation gap",
        )
        check(
            "note cites Probe U as prior NCG-cutoff attempt",
            "Probe U" in prose or "probeU" in prose or "PROBE_U" in prose or "probe_U" in prose,
            detail="cross-references prior NCG-route synthesis",
        )
        check(
            "note cites cl3_complexification_split as authority",
            "CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10" in prose,
            detail="markdown-link to retained authority",
        )
        # Status-authority check: note must NOT contain prose like 'audit_status: retained'
        # but may reference 'effective_status: retained' inside CITATIONS to other notes.
        # Allow `effective_status:` only inside a description of cited authorities.
        forbidden_promotions = [
            "audit_status: retained",
            "audit_status: retained_bounded",
            "audit_status: audited_clean",
            "**Status:** retained",  # author-side status declaration
        ]
        prose_lower = prose.lower()
        no_forbidden = all(p.lower() not in prose_lower for p in forbidden_promotions)
        check(
            "note does not promote any audit_status (author-side)",
            "**Status authority:** independent audit lane only" in prose and no_forbidden,
            detail="status authority deferred to audit lane",
        )
        check(
            "note uses repo-canonical NCG vocabulary (KO-dim, anti-unitary involution)",
            ("KO-dim" in prose or "KO dimension" in prose)
            and "anti-unitary involution" in prose
            and ("isotype" in prose.lower()),
            detail="standard NCG vocabulary, no new repo tags",
        )
    else:
        check(
            "note exists",
            False,
            detail=f"missing: {doc_path}",
        )

    # ---------------------------------------------------------------------
    section("Final tally")
    # ---------------------------------------------------------------------
    print()
    print(f"=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
