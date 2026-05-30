#!/usr/bin/env python3
"""
Bridge-gap attack, move 3: the OS-measure crux. The value gate reduced (move 2)
to a 3-way fork -- which inner product / measure does the matter sector place on
the S3-invariant operator space span{I, J-I}?  HS/block-count -> Q=2/3,
dimension/Plancherel -> Q=1, fermion dynamics -> Q=1/3. The campaign's long-
standing verdict was 'rep theory ranks NEITHER block-count nor dimension'. This
move finds a NATIVE tie-breaker.

KEY RESULT (analytic + Monte Carlo, both below): the STANDARD COVARIANT matrix-
field action S = Tr(M^2) -- the unique unitarily-invariant quadratic, native to
A1's operator algebra (Cl(3)=M2(C) has a UNIQUE tracial state = the trace) --
realizes the BLOCK-COUNT measure, NOT the dimension measure. Under
e^{-Tr(M^2)/2} on M = aI + b(J-I):
    <singlet isotype weight>  = <lambda0^2>   = 1
    <doublet isotype weight>  = <2 lambda1^2> = 1     (EQUAL)
-> equal expected C3-isotype weights = the block-count condition = r=1/2 = Q=2/3.

WHY (the dimension factor cancels): the doublet has dim 2 (TWO states), but the
doublet operator (J-I)'s HS-stiffness is 2x the singlet's (Tr((J-I)^2)/Tr(I^2)=
6/3=2), so each doublet state fluctuates at HALF variance (1/2); 2 x 1/2 = 1 =
the singlet's weight. The covariant matrix-field measure thus weights the two
C3 isotypes EQUALLY -- it is the block-count measure, giving Q=2/3, while the
non-covariant flat-in-coefficients measure gives the dimension answer Q=1.

SO: the framework's MATRIX-FIELD structure breaks the campaign's 'rep theory
ranks neither' tie -- toward Q=2/3 -- because the natural covariant action on a
matrix-valued mass field is the block-count measure.

HONEST CAVEATS (this is a LEAN, not a forcing):
 1. EXPECTATION, not per-operator: <W_singlet>=<W_doublet> means the measure's
    EXPECTED weights satisfy the Q=2/3 (block-count) condition; a specific
    operator's weights fluctuate, so its Q != 2/3 exactly. The covariant measure
    realizes block-count ON AVERAGE.
 2. BARE, not dynamical: this is the free Tr(M^2) measure. The fermion DYNAMICS
    (this session, 3 computations) modifies it and drives b->0 (Q=1/3). The lean
    is kinematic; whether the dynamics preserves or overrides it is open.
 3. A nonzero diagonal MEAN (background mass a) is not modeled by the zero-mean
    Gaussian; with a strong background, r=b^2/a^2 is small (toward Q=1/3).

NET: the first NATIVE argument that ranks the two canonical measures -- the
covariant matrix-field action selects block-count (Q=2/3) over dimension (Q=1).
A genuine lean toward the observed value, import-free; not a forcing. The open
piece is whether the g_bare=1 matter dynamics preserves this kinematic block-
count measure or collapses it (the move-2 tension, now sharpened to: does the
covariant Tr(M^2) measure survive the fermion loop?).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("ANALYTIC: e^{-Tr(M^2)/2} on M=aI+b(J-I) -> equal expected isotype weights")
    print("  Tr(M^2)=3a^2+6b^2 -> <a^2>=1/3, <b^2>=1/6, <ab>=0.")
    print("  eigenvalues lambda0=a+2b (singlet x1), lambda1=a-b (doublet x2).")
    print(f"  <singlet weight>=<lambda0^2>    = <a^2>+4<b^2> = {1/3+4/6:.4f}")
    print(f"  <doublet weight>=<2 lambda1^2>  = 2(<a^2>+<b^2>) = {2*(1/3+1/6):.4f}")
    print("  EQUAL -> block-count measure -> r=1/2 -> Q=2/3 (NOT dimension's 2:1 -> Q=1).")

    sep("MONTE CARLO confirmation (N=4e5)")
    rng = np.random.RandomState(7)
    N = 400000
    a = rng.randn(N) / np.sqrt(3); b = rng.randn(N) / np.sqrt(6)
    l0 = a + 2 * b; l1 = a - b
    ws, wd = (l0 ** 2).mean(), (2 * l1 ** 2).mean()
    print(f"  <singlet weight>={ws:.4f}  <doublet weight>={wd:.4f}  ratio={wd/ws:.4f}")
    print("  ratio ~ 1 -> block-count (Q=2/3); the dimension measure would give 2 (Q=1).")

    sep("WHY: the dimension factor cancels")
    print("  dim(doublet)=2 states, but Tr((J-I)^2)/Tr(I^2)=6/3=2 -> doublet stiffer ->")
    print("  variance 1/2 per state -> 2 x 1/2 = 1 = singlet weight. Net equal = block-count.")

    sep("VERDICT (native lean toward Q=2/3 -- NOT a forcing)")
    print("  The covariant matrix-field action Tr(M^2), native to A1's operator algebra")
    print("  (unique tracial state), realizes the BLOCK-COUNT measure -> Q=2/3, ranking the")
    print("  two canonical measures the campaign called 'rep theory ranks neither'. Caveats:")
    print("  (1) expectation not per-operator; (2) BARE measure -- fermion dynamics drives")
    print("  b->0 (Q=1/3); (3) background mean unmodeled. Open: does the g_bare=1 matter loop")
    print("  preserve the covariant block-count measure or collapse it? (the move-2 tension).")


if __name__ == "__main__":
    main()
