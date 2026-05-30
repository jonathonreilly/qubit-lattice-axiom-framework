#!/usr/bin/env python3
"""
Session capstone reframing: the charged-lepton Koide PROBLEM is a spontaneous
TRANSLATION-symmetry-breaking problem. This is the crispest, most native
statement the whole investigation converges on.

Generations = the three hw=1 momentum (BZ) corners (retained taste=momentum
identification). The generation mass operator on this triplet is
  Y = a I + b C + bbar C^2   (C = 3-cycle),  r = |b|^2/a^2,  Q = 1/3 + (2/3) r.

KEY NATIVE FACTS:
 - a = the DIAGONAL corner mass (same corner); b = the OFF-DIAGONAL corner<->corner
   coupling. Two corners differ by momentum Q* = corner_i - corner_j = (pi,pi,0).
 - TRANSLATION INVARIANCE (axiom A2) => any translation-invariant mass/vacuum is
   DIAGONAL in the momentum basis => b = 0 EXACTLY (momentum conservation).
 - The Koide RELATION Q=1/3+(2/3)r is a structural prediction OF the circulant
   (b!=0) form: 2 parameters (a,b) generate the constrained 3-mass spectrum. With
   b=0 you have 3 INDEPENDENT diagonal masses -- Q can numerically hit 2/3 but only
   as a tuned coincidence, NOT as the Koide relation.

THEREFORE: the predictive Koide relation (Q=2/3 to 1e-5, a *relation* not a
coincidence) requires b != 0, which requires the vacuum to carry a condensate at
Q* = (pi,pi,0) -- i.e. SPONTANEOUS TRANSLATION-SYMMETRY BREAKING by exactly the
corner-connecting (staggered) momentum, at strength b/a = 1/sqrt(2).

The fermion vacuum does NOT do this (this session, 3 independent computations:
gap equation, competing-orders, effective potential -- the uniform condensate
wins, b->0, Q=1/3). So:

  THE KOIDE VALUE PROBLEM  ==  a spontaneous translation-breaking problem,
  unsupplied by the native fermion-vacuum dynamics.

This unifies the whole session: 'flat direction' (retracted) -> nonperturbative
vacuum output -> Jahn-Teller -> r=1/2 = off-diag/diag ratio -> multicritical
coexistence -> fermion vacuum won't select it -> heat-kernel frame (diagonal in
the physical basis) -> all of it is the single statement that b!=0 needs
translation breaking at (pi,pi,0) that the dynamics does not spontaneously
produce. NOT a wall: it names exactly what must happen (a staggered condensate at
(pi,pi,0), b/a=1/sqrt2) and where it must come from (outside the fermion
determinant: the derived bridge-gap action or a non-fermionic sector).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q(M):
    M = np.array(M, float)
    return M.sum() / np.sqrt(np.abs(M)).sum() ** 2


def main():
    sep("(1) translation invariance (A2) => mass operator diagonal in momentum => b=0")
    L = 8
    rng = np.random.RandomState(0)
    fx = rng.randn(L, L, L)
    fx = (fx + fx[::-1, ::-1, ::-1]) / 2          # generic symmetric translation-invariant kernel
    mk = np.fft.fftn(fx).real                     # diagonal in momentum
    corners = {'x': (L // 2, 0, 0), 'y': (0, L // 2, 0), 'z': (0, 0, L // 2)}
    print("  hw=1 corner masses for a generic translation-invariant vacuum (diagonal):")
    for nm, c in corners.items():
        print(f"    corner {nm}: m={mk[c]:+.4f}")
    print("  off-diagonal corner-corner coupling b = 0 EXACTLY (momentum conservation).")
    print(f"  corner_x - corner_y = (pi,pi,0): b!=0 would need a condensate at this momentum.")

    sep("(2) the Koide RELATION needs the circulant b!=0; b=0 gives only a coincidence")
    print("  circulant (b!=0): Q = 1/3 + (2/3) r is a RELATION from 2 params (a,b):")
    for r in [0.0, 0.5, 1.0]:
        a, b = 1.0, np.sqrt(r)
        ev = np.array([a + 2 * b, a - b, a - b])
        print(f"    r={r:.1f}: sqrt-masses {np.round(ev,3)} -> Q={Q(ev**2):.4f}")
    print("  diagonal (b=0): 3 INDEPENDENT masses; Q=2/3 only by tuning 3 free numbers")
    print("    (e.g. (2.914,0.043,0.043) -> Q=0.667) -- a coincidence, NOT the Koide relation.")

    sep("(3) so b!=0 <=> spontaneous translation breaking at (pi,pi,0), b/a=1/sqrt2")
    print("  fermion vacuum does NOT break translation (this session, 3 computations:")
    print("  gap equation / competing-orders / effective potential -> uniform wins, b->0).")

    sep("CAPSTONE")
    print("  THE KOIDE VALUE PROBLEM == a spontaneous translation-symmetry-breaking problem:")
    print("  the predictive relation Q=2/3 requires the vacuum to carry a staggered condensate")
    print("  at the corner-connecting momentum (pi,pi,0) with strength b/a=1/sqrt2. Native")
    print("  translation invariance (A2) forbids it in any translation-invariant vacuum; the")
    print("  fermion-vacuum dynamics does not spontaneously supply it. NOT a wall -- it names")
    print("  exactly what must happen and where it must come from (the derived bridge-gap")
    print("  action or a non-fermionic sector). The cleanest statement of the open gate.")


if __name__ == "__main__":
    main()
