#!/usr/bin/env python3
"""
Bridge-gap attack, move 2 (6-angle workflow wf_10741a2a + independent verify):
does the g_bare=1 action FORCE or BOUND the corner-coupling ratio b/a, the
import-free Koide value gate (Q=2/3 <=> b/a=1/sqrt2)?

VERDICT: b/a is NOT forced by any native principle; it is a FREE coefficient of
the open staggered-Dirac matter action (= the kinetic-to-mass amplitude ratio on
the (Z2)^3 corner cube, b/a=tanh^2(t)). But it is BOUNDED by reflection
positivity and CHARACTERIZED cleanly by Hilbert-Schmidt equipartition. The crux
is a 3-way MEASURE fork.

(1) NOT FORCED -- every native candidate gives the wrong value:
    naive heat-kernel t=g_bare^2=1 -> b/a=tanh^2(1)=0.5800 (Q=0.558)
    bare-action t->0             -> b/a=0          (Q=1/3)
    nearest Casimir t=C2(1,0)=4/3 -> b/a=0.7570    (Q=0.715, closest, 7% high)
    target t*=atanh(2^-1/4)=1.2242 is transcendental -- no Casimir/Laplacian/
    counting origin.

(2) REFLECTION-POSITIVITY BOUND (native, import-free): Y=aI+b(J-I) PSD requires
    a+2b>=0 (singlet) and a-b>=0 (doublet) => b/a in [-1/2, 1]. 1/sqrt2=0.7071 is
    INTERIOR, 0.2929 below the upper edge b/a=1 (=Q=1, massless doublet). Contains
    1/sqrt2; does not pin it.

(3) HILBERT-SCHMIDT EQUIPARTITION (the strongest lead, clean characterization):
    1/sqrt2 is the UNIQUE point where the off-diagonal operator b(J-I) carries the
    same canonical-trace (HS) norm as the diagonal aI:
       Tr((aI)^2)=3a^2,  Tr((b(J-I))^2)=6b^2  =>  equal <=> b/a=sqrt(3/6)=1/sqrt2.
    The factor 2 = Tr((J-I)^2)/Tr(I^2) = 6/3 = dim(doublet)/dim(singlet). Under the
    canonical HS measure e^{-Tr(M^2)/2}, the ensemble variance ratio
       r = <b^2>/<a^2> = 1/2  ->  Q = 2/3   (exactly).

(4) THE 3-WAY MEASURE FORK (the crux, now concrete not philosophical):
    HS / trace measure        -> r=1/2 -> Q=2/3   (the equipartition point above)
    dimension / Plancherel     -> r=1   -> Q=1     (weights doublet by dim, not HS)
    fermion DYNAMICS (this session, 3 computations: gap eqn / competing orders /
      effective potential)      -> b->0 -> Q=1/3   (uniform condensate wins)
    The observed Q=2/3 matches the HS measure; the framework's fermion vacuum
    selects NEITHER HS nor dimension -- it gives Q=1/3. So 1/sqrt2 is the HS-max-
    entropy value, which the dynamics does NOT realize. NOT forced; a genuine
    tension (native dynamics -> Q=1/3, observed -> Q=2/3 = HS-equipartition).

IMPORT CAUGHT: b/a = Brannen's fitted circulant amplitude eta (eta^2=1/2 fit to
observed lepton masses). Citing eta to 'fix' b/a imports the answer
(wrong-escape-via-citation). The tanh^2(t) FORM is native; its evaluation point
is not.

HONEST STATUS: the value gate Q=2/3 is (a) not forced, (b) RP-bounded to
b/a in [-1/2,1] containing 1/sqrt2, (c) the HS-equipartition / max-entropy point.
The single decidable next question: does the matter-sector OS-reconstruction
measure on span{I, J-I} use the HS/trace inner product (-> 1/sqrt2, Q=2/3) or
dimension/Plancherel (-> Q=1) -- or does the fermion dynamics (-> Q=1/3) win?
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q_of_r(r):
    return 1 / 3 + 2 / 3 * r


def main():
    J = np.ones((3, 3)); I = np.eye(3); B = J - I

    sep("(1) NOT forced: native-candidate t all miss b/a=0.7071")
    for label, t in [("naive t=g^2=1", 1.0), ("Casimir 4/3", 4 / 3), ("Casimir 3/4", 0.75),
                     ("t=1/2", 0.5), ("t*=atanh(2^-1/4)", np.arctanh(2 ** -0.25))]:
        ba = np.tanh(t) ** 2
        print(f"   {label:18s}: b/a={ba:.4f}  Q={Q_of_r(ba**2):.4f}  |Δ to 0.7071|={abs(ba-2**-0.5):.4f}")

    sep("(2) reflection-positivity bound: b/a in [-1/2, 1], 1/sqrt2 interior")
    print(f"   eigenvalues a+2b (singlet), a-b (doublet) >=0  =>  b/a in [-0.5, 1.0]")
    print(f"   1/sqrt2={2**-0.5:.4f} interior; {1-2**-0.5:.4f} below upper edge (b/a=1 -> Q=1).")

    sep("(3) Hilbert-Schmidt equipartition -> r=1/2 (the clean characterization)")
    print(f"   Tr(I^2)={np.trace(I@I):.0f}, Tr((J-I)^2)={np.trace(B@B):.0f}; equal HS weight 3a^2=6b^2")
    print(f"   <=> b/a=sqrt(3/6)={np.sqrt(0.5):.4f}=1/sqrt2; factor 2 = 6/3 = dim(doublet)/dim(singlet).")
    print(f"   HS measure e^-Tr(M^2)/2: <b^2>/<a^2> = (1/6)/(1/3) = {(1/6)/(1/3):.3f} -> Q={Q_of_r(0.5):.4f}")

    sep("(4) the 3-way measure fork (the crux)")
    print(f"   HS/trace      -> r=1/2 -> Q={Q_of_r(0.5):.4f}   (equipartition)")
    print(f"   dimension     -> r=1   -> Q={Q_of_r(1.0):.4f}   (Plancherel)")
    print(f"   fermion dyn.  -> r=0   -> Q={Q_of_r(0.0):.4f}   (uniform condensate wins, 3 computations)")
    print("   observed Q=2/3 = HS-equipartition; the framework's vacuum selects Q=1/3. NOT forced.")

    sep("VERDICT")
    print("  b/a=1/sqrt2 NOT forced; RP-bounded to [-1/2,1] (contains it); = HS-equipartition /")
    print("  max-entropy point. The fermion dynamics gives Q=1/3 (tension with observed 2/3).")
    print("  Decidable next: which inner product does the matter-sector OS measure use on")
    print("  span{I, J-I} -- HS/trace (->2/3), dimension (->1), or does dynamics (->1/3) win?")


if __name__ == "__main__":
    main()
