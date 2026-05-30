#!/usr/bin/env python3
"""
Verification of the 7-angle panel verdict on 'what fixes the Casimir time t /
why b/a (r=1/2, Q=2/3)' for the heat-kernel route. Three machine-precision
claims, all reproduced here.

PANEL OUTCOME: 0 of 5 reporting angles produced an import-free, non-circular
forcing of t=1.2242 / r=1/2. The route is a real native CHARACTERIZATION but not
a derivation; the modulus persists as t. Key verified facts:

 (a) BASIS CAVEAT (decisive). The cube heat kernel K_t is EXACTLY DIAGONAL in the
     character/momentum (Hadamard) basis (off-diagonal ~1e-16). The retained
     carrier (CL3_TASTE_GENERATION_THEOREM / SITE_PHASE_CUBE_SHIFT_INTERTWINER)
     identifies the hw=1 generation labels as momentum/BZ-corner (taste) indices
     = exactly that Hadamard basis. So in the PHYSICAL basis b=0 -> r=0 -> Q=1/3,
     matching the fermion-vacuum capstone. The off-diagonal b!=0 (hence
     r=tanh^4 t spanning (0,1)) lives only in the DUAL position-cube basis; it is
     a taste-breaking amplitude of free strength, generic to any 2-parameter
     C3-symmetric ansatz, not special to the cube.

 (b) LABEL FIX. b/a = tanh^2(t) = 1/sqrt2 = 0.7071 at r=1/2 (NOT 2^{-1/4};
     2^{-1/4}=0.8409 = tanh(t)). Matches the consolidation note's '1/sqrt2 x
     diagonal'. The heat-kernel note's earlier '2^{-1/4}' label was wrong; Q=2/3
     unaffected. (2^{-1/4} carries no independent content: it is (1/2)^{1/4}.)

 (c) EQUIPARTITION = SAME UNFORCED t. The C3 isotype equipartition
     |c0|^2(singlet) = |c1|^2+|c2|^2(doublet) is EXACTLY r=1/2, and for the heat
     kernel it needs a/b = K_t(0)/K_t(2) = sqrt2, which holds ONLY at t=1.2242.
     The ratio varies continuously with t; no cube symmetry forces it. So the
     'isotype-equipartition' reframing does not force r=1/2 either.

GENUINE POSITIVE (angle 5, survived, non-circular): the heat-kernel Yukawa
Y=aI+bC+bbar C^2 COMMUTES with Gamma_chi ([Y,Gamma_chi]=0), so it reaches r=1/2
by Fourier-weight balance (a^2=2|b|^2), NOT by the anticommutation {H,Gamma_chi}=0
that the retained no-go forbids. The route is therefore genuinely INDEPENDENT of
the chiral-grading import -- it lives in the case the no-go leaves open.

LIT CATCH (wrong-escape-via-citation): Brannen's circulant amplitude sqrt2 <=>
b/a=1/sqrt2 <=> r=1/2 is numerically identical to the target, but Brannen's sqrt2
is IMPOSED to match observed Koide, not derived -- adopting it to 'fix t' would
import the answer. Caught. The tanh^4(t) form itself appears genuinely native.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    n, N = 3, 8
    corners = [tuple((i >> b) & 1 for b in range(n)) for i in range(N)]
    ham = lambda x, y: sum(p != q for p, q in zip(x, y))

    def Kpos(t):
        u = np.exp(-2 * t)
        return np.array([[((1 + u) / 2) ** (n - ham(x, y)) * ((1 - u) / 2) ** ham(x, y)
                          for y in corners] for x in corners])

    H = np.array([[(-1) ** sum(x[b] * sx[b] for b in range(n)) for sx in corners]
                  for x in corners], float) / np.sqrt(N)
    t = 1.2242
    Kp = Kpos(t)
    Kchar = H.T @ Kp @ H
    hw1 = [i for i, c in enumerate(corners) if sum(c) == 1]
    a, b = Kp[hw1[0], hw1[0]], Kp[hw1[0], hw1[1]]

    sep("(a) heat kernel is DIAGONAL in the physical (taste=momentum) basis")
    print(f"   off-diagonal max in character basis = {np.abs(Kchar - np.diag(np.diag(Kchar))).max():.2e}")
    print("   => physical basis b=0 -> r=0 -> Q=1/3 (matches fermion-vacuum capstone).")
    print("   b!=0 only in the DUAL position-cube basis (a free-strength taste-breaking).")

    sep("(b) b/a label fix")
    print(f"   b/a = {b/a:.4f} = tanh^2(t) = 1/sqrt2 = {1/np.sqrt(2):.4f}")
    print(f"   tanh(t) = {np.tanh(t):.4f} = 2^(-1/4) = {2**-0.25:.4f}  (this is what was mislabeled as b/a)")

    sep("(c) isotype equipartition = r=1/2 = same unforced t")
    v = np.array([a + 2 * b, a - b, a - b])
    c0 = v.sum() ** 2 / 3
    print(f"   singlet |c0|^2 = {c0:.4f}   doublet = {v@v - c0:.4f}   r=(b/a)^2 = {(b/a)**2:.4f}")
    print("   equipartition <=> a/b = K(0)/K(2) = sqrt2, holds only at one t:")
    for tt in [0.8, 1.0, 1.2242, 1.5]:
        K2 = Kpos(tt)
        print(f"     t={tt}: K(0)/K(2) = {K2[hw1[0],hw1[0]]/K2[hw1[0],hw1[1]]:.4f}  (target sqrt2={np.sqrt(2):.4f})")
    print("   => no cube symmetry forces a/b=sqrt2; equipartition is not forced either.")

    sep("VERDICT")
    print("  Panel: 0/5 angles natively forced t/r=1/2. Heat-kernel route = real native")
    print("  CHARACTERIZATION (r=tanh^4 t), genuinely chirality-INDEPENDENT (commutes with")
    print("  Gamma_chi, the case the no-go leaves open), but in the PHYSICAL taste basis it")
    print("  is diagonal (b=0, Q=1/3). The modulus persists as t. Lit-search caught the")
    print("  Brannen-sqrt2 import trap. No forcing yet; not a wall -- the open question is")
    print("  whether a native cube normalization (not Koide input) sets t / equalizes the")
    print("  C3 isotype weights without working in the dual position basis.")


if __name__ == "__main__":
    main()
