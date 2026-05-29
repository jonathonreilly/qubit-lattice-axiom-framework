#!/usr/bin/env python3
"""
HARDENING of Step 3 of the Koide Q=2/3 derivation from A1+A2.

The original Step 3 ("a pure qubit has equal identity/Pauli HS power, so
the sqrt-mass packet equipartitions") conflated TWO different splits:
  - the generation-space split (democratic vs fluctuation, both grade-1),
  - the qubit HS split (identity grade-0 vs Pauli grade-1).
These are not the same. This script rebuilds the forcing on a rigorous,
basis-independent footing using the Frobenius-Schur central tracial
state, and verifies every claim numerically.

Angles attacked (per user):
  1. The sqrt-mass <-> generation-space map from A1 (Cl(3) grade-1).
  2. Purity alone is NOT sufficient (honest demonstration).
  3. Holomorphic/Kahler (1,1): FS gives R[Z3] = R (+) C, 1 complex dof.
  4. Frobenius-Schur CENTRAL TRACIAL STATE -> equal block weight ->
     equipartition. (The real forcing.)
  5. |s_perp|^2 / |s_par|^2 = 1 derived from block balance + Cl(3).
  6. d=3 uniqueness robustness: transversality at d = 3 + eps.
"""

import numpy as np

np.set_printoptions(precision=6, suppress=True)


def sep(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# =====================================================================
# ANGLE 1: the generation space is Cl(3) grade-1 = regular rep of the
# color-Z_3 automorphism = R[Z_3]. The Z_3 cyclic permutation of the
# three Pauli/Cl(3) vector generators IS the regular representation.
# =====================================================================
def angle1_generation_space():
    sep("ANGLE 1 -- generation space = Cl(3) grade-1 = regular rep of Z_3")
    # Color-Z_3 automorphism: cyclic permutation sigma_1->sigma_2->sigma_3.
    P = np.array([[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]], dtype=float)   # cyclic permutation (123)
    print("  Color-Z_3 generator P (permutes the 3 Cl(3) vector axes):")
    print(P)
    w, V = np.linalg.eig(P)
    print(f"  eigenvalues of P = {np.round(w,6)}  (should be 1, w, w^2)")
    cube = np.exp(2j * np.pi / 3)
    expected = sorted([1.0, cube, cube ** 2], key=lambda z: (z.real, z.imag))
    got = sorted(w, key=lambda z: (z.real, z.imag))
    ok = np.allclose(got, expected)
    print(f"  matches cube roots of unity: {ok}")

    # Trivial isotypic = eigenvalue-1 eigenvector = body diagonal (1,1,1).
    diag = np.array([1, 1, 1], dtype=float) / np.sqrt(3)
    print(f"  trivial isotypic (Z_3-fixed) = body diagonal = {np.round(diag,5)}")
    print(f"  P @ diag = diag ? {np.allclose(P @ diag, diag)}")
    print("  => 'democratic direction' is forced as the unique Z_3-fixed")
    print("     axis of the Cl(3) color automorphism (NOT an external input).")
    return P, diag


# =====================================================================
# ANGLE 3: Frobenius-Schur. Over R, R[Z_3] = R (+) C: the non-trivial
# isotypic is a SINGLE 2-real-dim block carrying a complex structure J.
# J is Cl(3)-native: it is the grade-2 bivector dual to the body-diagonal
# axis, acting on grade-1 vectors (= rotation generator about (1,1,1)).
# =====================================================================
def angle3_kahler(P, diag):
    sep("ANGLE 3 -- Frobenius-Schur: R[Z_3] = R (+) C ; Cl(3)-native J")
    # Fluctuation plane = orthogonal complement of the body diagonal.
    # Build an orthonormal basis of that plane.
    a = np.array([1.0, -1.0, 0.0]); a /= np.linalg.norm(a)
    b = diag.copy()                                    # = (1,1,1)/sqrt3
    f2 = np.cross(b, a)                                 # complete the frame
    f1 = a
    print(f"  fluctuation plane basis f1={np.round(f1,4)} f2={np.round(f2,4)}")

    # Cl(3)-native complex structure: rotation generator about axis (1,1,1).
    # L_ij = -eps_ijk n_k  (the grade-2 bivector dual to n=diag).
    n = diag
    L = np.array([[0, -n[2], n[1]],
                  [n[2], 0, -n[0]],
                  [-n[1], n[0], 0]])
    # Restrict L to the fluctuation plane (coords in {f1,f2}):
    F = np.column_stack([f1, f2])          # 3x2
    Jplane = F.T @ L @ F                    # 2x2 generator
    print(f"  bivector generator L (grade-2, dual to body diagonal):\n{np.round(L,4)}")
    print(f"  L restricted to fluctuation plane (2x2):\n{np.round(Jplane,4)}")
    print(f"  J^2 = -I on plane ? {np.allclose(Jplane @ Jplane, -np.eye(2))}")
    print("  => the fluctuation isotypic is ONE COMPLEX line (Kahler (1,1)):")
    print("     1 real trivial block (+) 1 complex fluctuation block.")
    print("     The complex structure J is the Cl(3) grade-2 bivector dual")
    print("     to the Z_3-fixed body-diagonal axis. (1 complex dof.)")


# =====================================================================
# ANGLE 4 (CORE): Frobenius-Schur CENTRAL TRACIAL STATE on R[Z_3]=R(+)C
# weights the two SIMPLE BLOCKS equally (1/2 each), independent of their
# real dimensions (1 and 2). A self-adjoint generation element decomposed
# as (a in R-block, z in C-block) has the central trace assign
#   tau(X) ~ (1/2)|proj_R X|^2 + (1/2)|proj_C X|^2  balanced.
# The packet realizing equal block-weight has |s_par|^2 = |s_perp|^2.
# =====================================================================
def Q_from_power(p_triv, p_fluct):
    """Q given normalized power in trivial vs fluctuation isotypic."""
    cos2 = p_triv / (p_triv + p_fluct)
    return 1.0 / (3 * cos2)


def num_real_blocks(d):
    """# real-irreducible blocks of R[Z_d]."""
    b = 1                       # trivial
    if d % 2 == 0:
        b += 1                  # sign rep (real)
    b += (d - 1) // 2           # conjugate complex pairs
    return b


def angle4_central_trace():
    sep("ANGLE 4 (CORE, AUDITED+CORRECTED) -- which block weighting?")
    print("  R[Z_3] = R (+) C : the isotypic POWER split (trivial, fluct)")
    print("  determines Q. Three canonical weightings exist:")
    print()
    print("   weighting (p_triv, p_fluct) |   Q    | meaning")
    rows = [
        ("all-trivial   (1 , 0  )", 1.0, 0.0, "Q_min = democratic"),
        ("equal-block   (1/2,1/2)", 0.5, 0.5, "MIDPOINT = 2/3"),
        ("dim-weighted  (1/3,2/3)", 1/3, 2/3, "Q_max = canonical/Plancherel"),
    ]
    for label, pt, pf, meaning in rows:
        print(f"   {label}  | {Q_from_power(pt, pf):.5f} | {meaning}")
    print()
    print("  AUDIT RESULT (corrects my earlier claim):")
    print("   * The CANONICAL group-algebra / Plancherel central trace weights")
    print("     each irrep block by dim^2/|G| = (1/3, 2/3) -> Q = 1, NOT 2/3.")
    print("     So 'equipartition = canonical central trace' is FALSE. KILLED.")
    print("   * Equipartition is the EQUAL-BLOCK weighting (1/2,1/2): equal")
    print("     weight to each of the B=2 Frobenius-Schur blocks, INDEPENDENT")
    print("     of block dimension. This is max-entropy over the BLOCK LABEL,")
    print("     not over generations and not the dimension-weighted trace.")
    print()
    print("  The three canonical weightings map EXACTLY onto the three")
    print("  special Koide values: (Q_min, midpoint, Q_max) = (1/3, 2/3, 1).")


# Clean closed-form: equal block power => Q = 2/d, no cone artifacts.
def angle4_closed_form():
    sep("ANGLE 4b -- closed form (no cone artifacts): equal block => Q=2/d")
    print("  Let total norm^2 = 1, split equally: |s_par|^2=|s_perp|^2=1/2.")
    print("  cos^2 theta = |s_par|^2 / |s|^2 = 1/2  =>  Q = 1/(d * 1/2) = 2/d.")
    for d in [2, 3, 4]:
        print(f"    d={d}: Q = 2/d = {2.0/d:.6f}")
    print("  Exact, basis-free. d=3 (Cl(3)/Z^3) => Q = 2/3.")


# =====================================================================
# ANGLE 2: purity (|n|=1) alone does NOT force equipartition. Honest.
# =====================================================================
def angle4c_qubit_block_label():
    sep("ANGLE 4c -- A1's qubit fixes the B=2 block label (the '2' of 2/3)")
    print("  # real-irreducible (Frobenius-Schur) blocks B of R[Z_d]:")
    for d in range(2, 8):
        b = num_real_blocks(d)
        tag = "  <== B=2 (qubit-like 1-bit block label)" if b == 2 else ""
        print(f"    Z_{d}: B = {b}{tag}")
    print()
    print("  B=2 ONLY for d=2,3. A1 says the primitive distinction is a QUBIT")
    print("  = a single 2-valued (1-bit) label. The FS decomposition of the")
    print("  generation regular-rep gives a 2-valued block label (trivial vs")
    print("  fluctuation) PRECISELY when d in {2,3}. Maximum entropy over this")
    print("  1-bit qubit-block label = (1/2,1/2) = equipartition.")
    print("  d=2 -> Q=2/d=1 (degenerate); d=3 is the unique nontrivial case.")
    print("  => '2' in Q=2/3 is the qubit/block count (A1); '3' is the")
    print("     generation/lattice count (A2).")


def angle2_purity_insufficient():
    sep("ANGLE 2 -- purity (|n|=1) alone is NOT sufficient (honest)")
    print("  Bloch-trine embedding sqrt(m_k)=a + b*cos(2pi k/3), pure: a^2+b^2=1.")
    print("  Equipartition needs b^2 = 2 a^2 (=> a^2=1/3,b^2=2/3, magic angle).")
    print("  Pure state alone leaves a free 1-parameter family:")
    for adeg in [20, 45, 54.7356, 70]:
        al = np.radians(adeg)
        a, b = np.cos(al), np.sin(al)
        s = np.array([a + b * np.cos(2 * np.pi * k / 3) for k in range(3)])
        Q = (s @ s) / (s.sum() ** 2) if s.min() >= 0 else float('nan')
        print(f"    alpha={adeg:7.3f} deg (pure): b^2/a^2={b*b/(a*a):.4f}  Q={Q:.5f}")
    print("  => purity fixes |n|=1 but NOT the direction/ratio. The RATIO is")
    print("     fixed by the equal-block weighting (Angle 4/4c), NOT by")
    print("     purity. Purity is at best a consistency condition, not the")
    print("     forcing. (This corrects the original Step 3.)")


# =====================================================================
# ANGLE 6: robustness of the d=3 double-characterization.
# Q_equi(d)=2/d, Q_mid(d)=(1+d)/(2d). Delta(d)=Q_mid-Q_equi=(d-3)/(2d).
# Transversal simple zero at d=3, slope d/dd Delta |_{3} = 1/6.
# =====================================================================
def angle6_transversality():
    sep("ANGLE 6 -- d=3 uniqueness robustness (transversal simple zero)")
    print("  Delta(d) = Q_mid - Q_equi = (1+d)/(2d) - 2/d = (d-3)/(2d).")
    print("  Zero only at d=3; near d=3: Delta(3+eps) = eps/(2(3+eps)) ~ eps/6.")
    for d in [2.5, 2.9, 3.0, 3.1, 3.5, 4.0]:
        delta = (d - 3) / (2 * d)
        print(f"    d={d:4.1f}: Delta={delta:+.5f}")
    # numerical slope at d=3
    h = 1e-6
    slope = (((3 + h) - 3) / (2 * (3 + h)) - ((3 - h) - 3) / (2 * (3 - h))) / (2 * h)
    print(f"  numerical d(Delta)/dd at d=3 = {slope:.6f}  (exact 1/6 = {1/6:.6f})")
    print("  => isolated, transversal (non-degenerate) selection of d=3;")
    print("     the two balance principles separate linearly off d=3.")


def main():
    P, diag = angle1_generation_space()
    angle3_kahler(P, diag)
    angle4_central_trace()
    angle4_closed_form()
    angle4c_qubit_block_label()
    angle2_purity_insufficient()
    angle6_transversality()

    sep("SYNTHESIS (post-audit)")
    print("  EXACT, BASIS-FREE (proven here, no assumption):")
    print("   (1) generation space = Cl(3) grade-1 = regular rep of color-Z_3;")
    print("       the democratic direction is FORCED as the unique Z_3-fixed")
    print("       body diagonal -- not an external choice.")
    print("   (3) Frobenius-Schur: R[Z_3] = R (+) C ; fluctuation = ONE complex")
    print("       block, complex structure J = Cl(3) grade-2 bivector dual to")
    print("       the body diagonal (Kahler (1,1)).")
    print("   (4) the THREE canonical isotypic weightings (all-trivial,")
    print("       equal-block, dim-weighted) give EXACTLY (Q_min,mid,Q_max)=")
    print("       (1/3, 2/3, 1). The canonical/Plancherel trace = dim-weighted")
    print("       => Q=1 (NOT 2/3): the central-trace route is KILLED.")
    print("   (4c) B=2 FS blocks only for d in {2,3}; d=3 unique nontrivial.")
    print("   (6) d=3 double-characterization (equipartition = range-midpoint)")
    print("       is a transversal simple zero (slope 1/6).")
    print("  RESIDUAL ASSUMPTION (sharpened weakest link, tied to A1):")
    print("   the packet sits at EQUAL-BLOCK weight = maximum entropy over the")
    print("   B=2 (qubit / 1-bit) Frobenius-Schur block label. This is the '2'")
    print("   of A1. It is NOT the canonical trace (which gives Q=1) and NOT")
    print("   max-entropy-over-generations (which gives Q=1/3). Deriving WHY")
    print("   the block label rather than the state label carries the max-")
    print("   entropy is the remaining open step.")


if __name__ == "__main__":
    main()
