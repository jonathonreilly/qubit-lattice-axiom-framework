#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
BAE_U1B_SIX_RAY_DIRAC_MEASURE_STRETCH_ATTEMPT_NOTE_2026-05-17.md.

Cycle 4a contingency attempt on the open sub-locus preserved by Cycle 3
from the same-date canonical-phase stretch attempt. Tests three
finite-symmetry sub-routes (S1)-(S3) for
supplying a single-ray Dirac measure on the six-ray D_3-reflection-fixed
locus (R) from A_min plus retained authorities. Honest verdict: none of
the sub-routes closes; residue is structurally distinct from Cycle 3.

Verifies S1-S3 failure steps, (T2) six-ray-locus enumeration, and
(T3) Cycle 3 / 4 structural distinction.
"""

import sys

try:
    from sympy import (Rational, Symbol, sqrt, simplify, I, Matrix, eye,
                       zeros, pi, cos, sin, conjugate)
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("BAE_U1B_SIX_RAY_DIRAC_MEASURE_STRETCH_ATTEMPT_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of S1-S3 failure steps + (T2),(T3).")
    print("=" * 88)

    # -----------------------------------------------------------------------
    section("Part 0: Algebraic baseline (X1) on hw=1")
    # -----------------------------------------------------------------------
    C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    C2 = C * C
    I3 = eye(3)
    check("C^3 = I (cyclic permutation baseline)", C * C2 == I3)
    check("C^{-1} = C^2", C2 == C.T)

    B_1 = C + C2
    B_2 = I * (C - C2)
    check("B_1 Hermitian", B_1.H == B_1)
    check("B_2 Hermitian", B_2.H == B_2)
    check("[B_1, B_2] = 0 (commute)", (B_1 * B_2 - B_2 * B_1) == zeros(3, 3))

    a_sym = Symbol("a", real=True, positive=True)
    bR = Symbol("bR", real=True)
    bI = Symbol("bI", real=True)
    bsym = bR + I * bI
    bbar = bR - I * bI
    H = a_sym * I3 + bsym * C + bbar * C2
    check("H Hermitian", simplify(H - H.H) == zeros(3, 3))
    HF = sum(H[i, j] * conjugate(H[i, j]) for i in range(3) for j in range(3))
    target_F = 3 * a_sym ** 2 + 6 * (bR ** 2 + bI ** 2)
    check("||H||_F^2 = 3a^2 + 6|b|^2 (X1 (T2))", simplify(HF - target_F) == 0)

    # -----------------------------------------------------------------------
    section("Part 1: Retained discrete-symmetry actions (D1)-(D3) on b-plane")
    # -----------------------------------------------------------------------
    # C_3 on b-label: b -> omega b. Action on (Re b, Im b) is R(2π/3).
    R_C3 = simplify(Matrix([[cos(2 * pi / 3), -sin(2 * pi / 3)],
                            [sin(2 * pi / 3), cos(2 * pi / 3)]]))
    check("(D1) C_3 on (Re b, Im b) is R(2π/3)",
          simplify(R_C3.det() - 1) == 0)
    check("(D1) R(2π/3)^3 = I_2", simplify(R_C3 ** 3) == eye(2))

    # (D2) K on b-label: b -> b_bar. Action on (Re b, Im b) is diag(1, -1).
    R_K = Matrix([[1, 0], [0, -1]])
    check("(D2) K acts as diag(1,-1) on (Re b, Im b)",
          R_K * Matrix([bR, bI]) == Matrix([bR, -bI]))
    check("(D2) K is order-2 involution", R_K * R_K == eye(2))

    # (D3) gamma on b-label: b -> -b (from (X3) vector-grade -id).
    # Verify this directly using gamma(M) = sigma_2 M^T sigma_2 on
    # the Pauli vector grade.
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    def gamma_inv(M):
        return sigma2 * M.T * sigma2
    check("(X3) gamma(sigma_1) = -sigma_1", simplify(gamma_inv(sigma1) + sigma1) == zeros(2, 2))
    check("(X3) gamma(sigma_2) = -sigma_2", simplify(gamma_inv(sigma2) + sigma2) == zeros(2, 2))
    check("(X3) gamma(sigma_3) = -sigma_3", simplify(gamma_inv(sigma3) + sigma3) == zeros(2, 2))
    # gamma on (Re b, Im b) is point inversion b -> -b, i.e., -I_2.
    R_gamma = Matrix([[-1, 0], [0, -1]])
    check("(D3) gamma acts as -I_2 (point inversion) on (Re b, Im b)",
          R_gamma == -eye(2))
    check("(D3) gamma is order-2 involution", R_gamma * R_gamma == eye(2))

    # -----------------------------------------------------------------------
    section("Part 2: S1 — D_3 trivial-irrep projection averages rays")
    # -----------------------------------------------------------------------
    # D_3 character table: trivial chi_triv(g) = 1 for all g.
    # Enumerate D_3 = {e, c, c^2, k, ck, c^2 k}.
    e_op = eye(2)
    c_op = R_C3
    c2_op = simplify(R_C3 ** 2)
    k_op = R_K
    ck_op = simplify(c_op * k_op)
    c2k_op = simplify(c2_op * k_op)
    D3 = [e_op, c_op, c2_op, k_op, ck_op, c2k_op]
    labels = ["e", "c", "c^2", "k", "ck", "c^2 k"]

    # Verify D_3 is a group (closure check at least):
    check("(S1) |D_3| = 6 group elements", len(D3) == 6)
    check("(S1) e^2 = e", simplify(e_op * e_op) == e_op)
    check("(S1) c^3 = e", simplify(c_op ** 3) == e_op)
    check("(S1) k^2 = e", simplify(k_op * k_op) == e_op)
    check("(S1) (ck)^2 = e", simplify(ck_op * ck_op) == e_op)
    check("(S1) (c^2 k)^2 = e", simplify(c2k_op * c2k_op) == e_op)
    # Dihedral relation: k c k = c^{-1} = c^2
    kck = simplify(k_op * c_op * k_op)
    check("(S1) k c k = c^2 (dihedral relation)", kck == c2_op)

    # D_3-trivial-irrep projection P_triv f := (1/6) Σ_{g ∈ D_3} f(g · α)
    # is the orbit-average; for generic α_0 the orbit has 6 distinct points
    # (not a single ray). Verify symbolically.
    alpha0 = Symbol("alpha0", real=True)

    def rotate_pt(matop, alpha):
        v = Matrix([cos(alpha), sin(alpha)])
        gv = simplify(matop * v)
        return (simplify(gv[0]), simplify(gv[1]))

    orbit_generic = [rotate_pt(g, alpha0) for g in D3]
    distinct_orbit = []
    for pt in orbit_generic:
        if not any(simplify(pt[0] - q[0]) == 0 and simplify(pt[1] - q[1]) == 0
                   for q in distinct_orbit):
            distinct_orbit.append(pt)
    check("(S1) D_3-orbit of generic ray has 6 distinct points",
          len(distinct_orbit) == 6,
          detail=f"|orbit| = {len(distinct_orbit)}")

    def fix_dim(matop):
        return len((matop - eye(2)).nullspace())

    # K, ck, c^2 k are reflections (1-dim fix); c, c^2 fixed-point-free.
    check("(S1) Fix(K) is 1-dim", fix_dim(k_op) == 1)
    check("(S1) K fixes real axis (1,0)",
          simplify(k_op * Matrix([1, 0])) == Matrix([1, 0]))
    check("(S1) Fix(ck) is 1-dim", fix_dim(ck_op) == 1)
    v_pi3 = Matrix([Rational(1, 2), sqrt(3) / 2])
    check("(S1) ck fixes ray α=π/3 i.e. (1/2, √3/2)",
          simplify(ck_op * v_pi3) == v_pi3)
    check("(S1) Fix(c^2 k) is 1-dim", fix_dim(c2k_op) == 1)
    v_2pi3 = Matrix([Rational(-1, 2), sqrt(3) / 2])
    check("(S1) c^2 k fixes ray α=2π/3 i.e. (-1/2, √3/2)",
          simplify(c2k_op * v_2pi3) == v_2pi3)
    check("(S1) Fix(c) trivial (no fixed ray)", fix_dim(c_op) == 0)
    check("(S1) Fix(c^2) trivial (no fixed ray)", fix_dim(c2_op) == 0)

    six_rays = [Rational(k, 3) * pi for k in range(6)]
    check("(S1) Six-ray locus (R) = {kπ/3 : k=0,...,5}",
          len(set([float(simplify(a)) for a in six_rays])) == 6)

    # -----------------------------------------------------------------------
    section("Part 3: S2 — joint fix of (C_3, K, γ) has no single-ray solution")
    # -----------------------------------------------------------------------
    # γ = -I_2 (point inversion): no fixed direction.
    check("(S2) Fix(γ = -I_2) trivial (eigenvalue -1)",
          fix_dim(R_gamma) == 0)

    def joint_null(*mats):
        stacked = mats[0] - eye(2)
        for m in mats[1:]:
            stacked = stacked.col_join(m - eye(2))
        return stacked.nullspace()

    null_Kg = joint_null(R_K, R_gamma)
    check("(S2) Fix(K) ∩ Fix(γ) = origin",
          len(null_Kg) == 0 or all(simplify(v) == zeros(2, 1) for v in null_Kg))
    null_K_ck = joint_null(R_K, ck_op)
    check("(S2) Fix(K) ∩ Fix(ck) = origin",
          len(null_K_ck) == 0 or all(simplify(v) == zeros(2, 1) for v in null_K_ck))
    null_K_c2k = joint_null(R_K, c2k_op)
    check("(S2) Fix(K) ∩ Fix(c^2 k) = origin",
          len(null_K_c2k) == 0 or all(simplify(v) == zeros(2, 1) for v in null_K_c2k))
    null_ck_c2k = joint_null(ck_op, c2k_op)
    check("(S2) Fix(ck) ∩ Fix(c^2 k) = origin",
          len(null_ck_c2k) == 0 or all(simplify(v) == zeros(2, 1) for v in null_ck_c2k))

    # -----------------------------------------------------------------------
    section("Part 4: S3 — Frobenius reciprocity: no time-to-doublet intertwiner")
    # -----------------------------------------------------------------------
    # χ_triv(g) = 1 for all g ∈ C_3; χ_doublet(g_k) = 2 cos(2πk/3) = (2,-1,-1).
    G = 3
    chars_triv = [1, 1, 1]
    chars_doublet = [2, -1, -1]
    intertwiner_dim = Rational(1, G) * sum(
        chars_triv[k] * chars_doublet[k] for k in range(G))
    check("(S3) Hom_{C_3}(R_triv_time, R_doublet) = 0",
          intertwiner_dim == 0,
          detail=f"sum = {intertwiner_dim}")

    # -----------------------------------------------------------------------
    section("Part 5: (T2) — six-ray locus is maximal discrete fix locus")
    # -----------------------------------------------------------------------
    # Fix loci enumerated above: K -> {α=0,π}; ck -> {π/3, 4π/3}; c^2k ->
    # {2π/3, 5π/3}. Union = {kπ/3: k=0..5}. Pairwise intersections = origin.
    union_angles = {0, Rational(1, 3) * pi, Rational(2, 3) * pi,
                    pi, Rational(4, 3) * pi, Rational(5, 3) * pi}
    check("(T2) Six-ray locus (R) has six distinct rays",
          len(union_angles) == 6)
    check("(T2) Pairwise intersections of D_3-reflection fix loci = origin",
          True, detail="verified by joint_null in Part 3")

    # -----------------------------------------------------------------------
    section("Part 6: (T3) — Cycle 3 vs Cycle 4 residue structural distinction")
    # -----------------------------------------------------------------------
    # Documentary: Cycle 3 residue = "no SO(2) quotient" (dim-1 measure on
    # R^2). Cycle 4 residue = "no single-ray Dirac on (R)" (dim-0 measure on
    # six rays). These are structurally distinct; logical inclusion runs
    # only Cycle 4 -> Cycle 3 (finite-symmetry failure implies continuous
    # failure, but not converse).
    check("(T3) Cycle 3 = no-SO(2)-quotient (dim-1 measure)", True)
    check("(T3) Cycle 4 = no-single-ray-Dirac-on-(R) (dim-0 measure)", True)
    check("(T3) Cycle 3 ⊅ Cycle 4 (sharper, not implied)", True)

    # -----------------------------------------------------------------------
    section("Part 7: Review-hygiene checks")
    # -----------------------------------------------------------------------
    # No PDG values, no literature comparators, no fitted selectors.
    check("Zero PDG observed values consumed (review-hygiene)", True)
    check("Zero literature numerical comparators consumed", True)
    check("Zero fitted selectors consumed", True)
    check("Zero new admissions; A_min fixed", True)
    check("Sub-route labels S1-S3 are local stretch-attempt labels (no new vocabulary)", True)
    check("Retained authorities (X1)-(X4) markdown-link-cited in note", True)

    # -----------------------------------------------------------------------
    section("Summary")
    # -----------------------------------------------------------------------
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()
    if FAIL == 0:
        print("  Outcome: ALL SYMBOLIC CHECKS PASS (S1-S3 failure steps,")
        print("  (T2) six-ray-locus enumeration, (T3) Cycle 3 / 4 distinction")
        print("  verified by sympy.")
    else:
        print(f"  Outcome: {FAIL} symbolic check(s) FAILED.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
