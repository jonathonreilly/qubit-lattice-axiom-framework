#!/usr/bin/env python3
"""
Bridge-gap attack, move 1 (grounded by the frontier-map workflow): correct and
sharpen the session capstone's '(pi,pi,0) staggered condensate' label using only
RETAINED cube-shift kinematics (site_phase_cube_shift_intertwiner, retained;
three_generation_hw1_distinct_translation_characters, retained). Zero imports.

THE CORRECTION:
 - A SINGLE pi-momentum shift S_mu (bit-flip mu on the (Z2)^3 corner cube)
   projects to ZERO on the hw=1 generation triplet: S_mu maps (1,0,0)->(0,0,0)
   [hw1->hw0] and (0,1,0),(0,0,1)->hw2, leaving the triplet entirely. So the
   capstone's literal 'single (pi,pi,0) shift' is NOT a within-triplet operator
   -- exactly the gap the frontier-map flagged against the retained requirement
   (the minimal generation breaker must be a WITHIN-triplet S3 -> subgroup op).

THE NATIVE OPERATOR (derivable):
 - The DOUBLE shift S_mu S_nu (flip two bits) projected to the triplet is a
   partial transposition; the S3-symmetric SUM over the three double-shifts
   projects to EXACTLY J - I (the three transpositions) -- the symmetric corner
   coupling. So the off-diagonal generation coupling b is NATIVE kinematics: a
   distance-2 (double pi-shift) hop on the corner cube, b*(J-I), with momentum
   transfer of (pi,pi,0)-TYPE (two simultaneous pi-shifts) -- which is what the
   capstone's intuition meant, now correctly an S3-symmetric BILINEAR projected
   to the triplet, not a single shift.

CONSEQUENCES (sharpening):
 - With Y = aI + b(J-I): sqrt-masses {a+2b, a-b, a-b} -> only 2 DISTINCT
   (S3-symmetric, doublet degenerate). Q = 1/3 + (2/3) r, r = b^2/a^2. So the
   VALUE Q=2/3 needs ONLY the symmetric, native b: b/a = 1/sqrt2.
 - Every product of real shifts is a real permutation -> projects to a REAL
   SYMMETRIC operator -> b is REAL -> at most 2 distinct masses. The 3rd
   splitting (e != mu, the full 3-distinct Koide spectrum) needs the ORIENTED
   complex part i(C - C^2), which real shift-products CANNOT produce: it requires
   a chirality/orientation = the koide_z3_equivariant_anticommuting twin gate
   (retained_bounded no-go), the single user-approval-gated import. AND it is
   exactly Q-ORTHOGONAL (the Brannen phase), so it does NOT affect Q=2/3.

NET (the sharpened frontier): Q=2/3 reduces to a single MAGNITUDE ratio of
CONCRETE native operators -- (distance-2 double-shift coupling b) / (distance-0
diagonal mass a) = 1/sqrt2 -- on the action's corner-cube. The existence and
S3-symmetric FORM of b is now derived from retained kinematics (not the fermion
vacuum, which won't supply it, and not an import). What remains open is the
COEFFICIENT RATIO b/a set by the derived g_bare=1 action, and -- separately and
Q-orthogonally -- the chiral orientation for the e-mu splitting.
"""

import numpy as np
import itertools


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    corners = list(itertools.product([0, 1], repeat=3))
    idx = {c: i for i, c in enumerate(corners)}

    def flip(c, mus):
        c = list(c)
        for m in mus:
            c[m] ^= 1
        return tuple(c)

    def S(mus):
        M = np.zeros((8, 8))
        for c in corners:
            M[idx[flip(c, mus)], idx[c]] = 1
        return M

    hw1 = [idx[c] for c in corners if sum(c) == 1]
    P = np.zeros((3, 8))
    for r, i in enumerate(hw1):
        P[r, i] = 1

    def Q(M):
        M = np.array(M, float); return M.sum() / np.sqrt(np.abs(M)).sum() ** 2

    sep("(1) a single pi-shift S_mu projects to ZERO on the triplet (label correction)")
    print("   P S_x P^T =\n", np.round(P @ S([0]) @ P.T, 2))
    print("   => the literal single '(pi,pi,0) shift' is NOT within-triplet.")

    sep("(2) the S3-symmetric SUM of double-shifts projects to J-I (native b)")
    B = P @ (S([1, 2]) + S([2, 0]) + S([0, 1])) @ P.T
    print("   P (S_yz + S_zx + S_xy) P^T =\n", np.round(B, 2))
    print("   = J - I :", np.allclose(B, np.ones((3, 3)) - np.eye(3)),
          "  (the three transpositions; momentum transfer (pi,pi,0)-type)")

    sep("(3) symmetric b sets Q via r=b^2/a^2; Q=2/3 <=> b/a=1/sqrt2 (only the native b)")
    for r in [0.0, 0.5, 1.0]:
        a, b = 1.0, np.sqrt(r)
        ev = np.array([a + 2 * b, a - b, a - b])
        print(f"   r={r:.1f}: sqrt-masses {np.round(ev,3)} (2 distinct, S3-sym)  Q={Q(ev**2):.4f}")

    sep("(4) 3-distinct (e!=mu) needs orientation real shifts cannot supply (chiral import)")
    asym = P @ (S([0, 1]) - S([1, 2])) @ P.T
    print("   a real shift difference projects to:",
          "SYMMETRIC" if np.allclose(asym, asym.T) else "antisymmetric",
          "-> real shift-products cannot make i(C-C^2).")
    print("   => the oriented/complex b (3 distinct masses) = chiral import (Q-ORTHOGONAL).")

    sep("VERDICT")
    print("  CORRECTED capstone: the generation off-diagonal b is NATIVE -- the S3-symmetric")
    print("  sum of double pi-shifts projected to hw=1 = b(J-I) (retained cube-shift kinematics),")
    print("  NOT a single (pi,pi,0) shift (which projects to 0). The symmetric b alone sets Q,")
    print("  so Q=2/3 reduces to ONE magnitude ratio of concrete native operators: (double-shift")
    print("  coupling b)/(diagonal a) = 1/sqrt2. OPEN: the coefficient ratio b/a from the derived")
    print("  g_bare=1 action. SEPARATE + Q-ORTHOGONAL: the chiral orientation for the e-mu split.")


if __name__ == "__main__":
    main()
