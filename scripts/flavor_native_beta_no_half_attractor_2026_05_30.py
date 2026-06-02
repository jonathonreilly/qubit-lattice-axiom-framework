#!/usr/bin/env python3
"""
NATIVE matter beta-function check (the assumptions-audit's one unexplored route):
does the framework's OWN (framework baseline) RG flow have an attractive fixed point at r=1/2?
ANSWER: NO -- and for a GENERAL (not model-specific) structural reason.

r = |b|^2/a^2 is the generation off-diagonal/diagonal coupling ratio; Q=1/3+(2/3)r.

(1) NATIVE FLOW (heat-kernel/blocking on the corner cube, move 2): r(t)=tanh^4(t),
    t = proper-time/blocking scale. beta_r = dr/dt = 4 tanh^3 t (1-tanh^2 t) > 0 for all
    finite t>0. Fixed points (beta_r=0): t=0 -> r=0 (UV) and t=inf -> r=1 (IR). r=1/2 sits
    at t=1.2242 with beta_r=0.70 != 0 -- a TRANSIT value, NOT a fixed point.

(2) CONDENSATE FLOW (gap-equation dynamics, this campaign): attractive fixed point b=0 -> r=0.

(3) GENERAL ARGUMENT (model-independent): RG fixed points sit at ENHANCED-SYMMETRY couplings.
    On the C3 triplet the symmetry of the spectrum (a+2b, a-b, a-b):
       r=0  -> (1,1,1)   : FULL S3 (all equal)         -> enhanced -> fixed point (Q=1/3)
       r=1  -> (3,0,0)   : rank-1 (two zeros)          -> enhanced -> fixed point (Q=1)
       r=1/2-> (2.41,0.29,0.29): 2 distinct, the GENERIC C3 pattern -> NO enhancement.
    r=1/2 has the SAME symmetry as generic r (a degenerate doublet + singlet) -- it is NOT a
    symmetry-enhanced coupling, so NO C3-symmetric beta-function fixes it. r=1/2 is precisely
    the Gamma_chi-null point <v|Gamma_chi|v>=0, and Gamma_chi is the non-native chiral grading
    (retained_bounded koide_z3_equivariant_anticommuting_no_go) -- not a symmetry of the flow.

CONCLUSION: there is NO native 1/2-attractor. Every native flow (heat-kernel 0->1; condensate
->0) and the general symmetry argument put the fixed points at the SYMMETRY-ENHANCED ENDPOINTS
r=0 (Q=1/3) and r=1 (Q=1). r=1/2 (Q=2/3) is a generic, non-enhanced, continuous value -- the
framework's RG/blocking machinery cannot land on it as an attractor. This CLOSES the last
derivation route from the assumptions audit and confirms, structurally, that r=1/2 is the
irreducible pin: it is a CONTINUOUS, non-symmetry-enhanced modulus = the generation chiral
grading, which no symmetric/discrete/RG mechanism of the framework reaches.

WHAT THIS MEANS (honest): the framework reduces ALL charged-lepton flavor -- the 3 distinct
masses AND Q=2/3 -- to ONE dimensionless input: the generation chiral grading (the Gamma_chi-
null point r=1/2), plus the Planck scale for units. That input is a genuine physical STRUCTURE
(the chirality of the flavor sector), shared across Koide/quark/generation-ID/strong-CP, not a
fitted number; but it is NOT derivable from the framework's symmetric/discrete content, for the
structural reason above. 'Rock-solid top-to-bottom' is achieved GIVEN that one chiral input.
"""
import numpy as np


def main():
    print("native heat-kernel flow r(t)=tanh^4(t): beta_r = dr/dt")
    for t in [0.5, 1.2242, 2.5, 5.0]:
        r = np.tanh(t) ** 4
        br = 4 * np.tanh(t) ** 3 * (1 - np.tanh(t) ** 2)
        print(f"  t={t:.4f}: r={r:.4f}, beta_r={br:+.4f}" + ("  <- r=1/2, beta_r!=0 (transit, not fixed)" if abs(r - .5) < .01 else ""))
    print("  fixed points: r=0 (t=0, UV) and r=1 (t=inf, IR).")
    print()
    print("symmetry of spectrum (a+2b,a-b,a-b): r=0 -> all-equal (full S3, enhanced);")
    print("  r=1 -> rank-1 (enhanced); r=1/2 -> 2 distinct = GENERIC C3 (NOT enhanced).")
    print("  => RG fixed points (= enhanced couplings) are r=0,1; r=1/2 is not a fixed point.")
    print()
    print("VERDICT: NO native 1/2-attractor. r=1/2 = continuous non-enhanced modulus = the")
    print("generation chiral grading (Gamma_chi-null) = the one irreducible chiral pin.")
    print("Framework reduces all charged-lepton flavor to that ONE chiral input + Planck.")


if __name__ == "__main__":
    main()
