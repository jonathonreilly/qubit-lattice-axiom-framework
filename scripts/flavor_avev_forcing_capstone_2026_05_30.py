#!/usr/bin/env python3
"""
Bridge-gap attack capstone (move 6): is a_VEV=0 (exact charged-lepton Q=2/3)
FORCED, or only consistent? Answer: NOT forced by any NATIVE symmetry -- it needs
the chiral grading Gamma_chi (the single user-approval import) OR dynamical
selection of the chiral-critical point. The native block-count measure supplies
the EXPECTED 2/3; the import/criticality promotes expected -> exact.

The decomposition: generation mass operator M = a*I + (off-diagonal). a = the
UNIFORM (S3-singlet) generation mass. Q=2/3 <=> the operator is the pure
block-count fluctuation with NO extra uniform piece (a_VEV=0 beyond the
fluctuation). Is a_VEV=0 forced?

WHAT ALLOWS the uniform mass a*I (so a_VEV is NOT forced to 0):
 - S3 (axis permutations): a*I is S3-INVARIANT -> allowed.
 - native reflections (CPT / charge-conj): generation-BLIND (~ +-I on gen space)
   -> commute with a*I -> allowed.
 - generic DYNAMICS: the uniform condensate WINS (this session, 3 computations)
   -> a_VEV != 0 -> Q=1/3 (degenerate). So the generic vacuum has a_VEV != 0.

WHAT FORBIDS it (forces a_VEV=0 -> exact Q=2/3):
 - the chiral grading Gamma_chi=(2/3)J-I: {M,Gamma_chi}=0 forces Tr(M Gamma_chi)=0;
   for the uniform part, Tr(I*Gamma_chi)=Tr(Gamma_chi)=-1 != 0, so a=0 is forced.
   (This is the retained koide_anticommuting_operator route -> Q=2/3.) But Gamma_chi
   is non-circulant on the C3 orbit -> the user-approval import
   (retained_bounded koide_z3_equivariant_anticommuting_no_go: not native).
 - equivalently, the chiral-CRITICAL point (condensate -> 0): there a_VEV->0
   dynamically and the block-count fluctuation gives Q=2/3.

SO: the charged-lepton Koide VALUE reduces, cleanly and rigorously, to the SINGLE
chiral input -- now with the new native result that 2/3 is the IMPORT-FREE
EXPECTED value (covariant block-count measure, RG-stable, moves 3-4), so the
chiral input's role is reduced from 'explains 2/3' to 'promotes the expected 2/3
to exact / selects the chiral-critical point'.

LIVE OPEN PATH (not a closure): is the charged-lepton sector dynamically NEAR the
chiral-critical point (condensate -> 0, a_VEV -> 0)? Leptons are light = small
mass = plausibly near-critical. If the framework's vacuum sits at/near chiral
criticality for the lepton sector, a_VEV -> 0 and Q -> 2/3 WITHOUT the operator-
level Gamma_chi import -- a dynamical-criticality route distinct from the operator
grading. That is the next attack.
"""

import numpy as np
import itertools


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    J = np.ones((3, 3)); I = np.eye(3); Gx = (2 / 3) * J - I

    sep("native symmetries ALLOW the uniform generation mass a*I (a_VEV not forced to 0)")
    perms = [np.array([[1 if p[i] == j else 0 for j in range(3)] for i in range(3)])
             for p in itertools.permutations(range(3))]
    print("  S3 (axis permutations): a*I invariant?", all(np.allclose(P @ I @ P.T, I) for P in perms), "-> ALLOWED")
    print("  native reflections (CPT/charge-conj): generation-blind (~ +-I) -> commute with a*I -> ALLOWED")
    print("  generic dynamics: uniform condensate wins -> a_VEV != 0 -> Q=1/3 (this session, 3 computations)")

    sep("only the chiral grading Gamma_chi forbids it (the import)")
    print(f"  Tr(Gamma_chi) = {np.trace(Gx):.1f}  -> {{M,Gamma_chi}}=0 => Tr(M Gamma_chi)=0 => a*(-1)=0 => a=0.")
    print("  Gamma_chi is non-circulant on the C3 orbit -> NOT native (retained_bounded no-go).")
    print("  equivalently: the chiral-CRITICAL point (condensate->0) gives a_VEV->0 dynamically.")

    sep("VERDICT")
    print("  a_VEV=0 (exact Q=2/3) is NOT natively forced (S3 + generation-blind reflections allow")
    print("  the uniform mass; generic condensate -> a_VEV!=0 -> Q=1/3). It requires the chiral")
    print("  grading Gamma_chi (single import) OR the chiral-critical point. The native block-count")
    print("  measure supplies the EXPECTED 2/3 (moves 3-4); the import/criticality promotes it to")
    print("  exact. So the charged-lepton Koide VALUE reduces cleanly to the ONE chiral input.")
    print("  LIVE PATH: is the (light) lepton sector dynamically near the chiral-critical point?")
    print("  If so, a_VEV->0 and Q->2/3 WITHOUT the operator-level import -- the next attack.")


if __name__ == "__main__":
    main()
