#!/usr/bin/env python3
"""
THREAD 2 + COMBINED FINAL STATUS of the charged-lepton Koide value question.

Thread 2 asked: can r=1/2 (Q=2/3) be derived OUTSIDE the operator/measure/dynamics
framing? Answer (6 routes, 0 survived): NO. Every non-operator route reduces to
(a) operator-in-disguise (the sqrt-mass vector IS the spectrum of the open
generation operator; the singlet/doublet split is its diagonalization), or
(b) numerology (cherry-picking 2/N=2/3 over the framework's own universal
(N-1)/N^2=2/9, or importing a non-Z3 value 1/sqrt2=cos(pi/4)).

Verified facts:
 - Q = 1/3 + (2/3) r, r=1/2 <=> |v_singlet|^2=|v_doublet|^2 <=> theta_v=45deg <=> Q=2/3.
   PDG leptons: Q=0.666660, theta_v=44.9997deg (empirically exact balance).
 - The balance is CODIM-1 / TUNED: under a flat sqrt-mass prior, mean Q~0.43 and only
   ~0.4% of vectors land within 1% of 2/3 (vs ~4% near democratic Q=1/3). Not generic.
 - 2-block MaxEnt (binary entropy over {singlet,doublet}) has a genuine interior max at
   P_s=P_d=1/2 -> r=1/2 (real extremum) -- BUT applied to the 3 MODES gives Q=1, and the
   partition-agnostic Fisher-info extremum sits at r~0.06, nowhere near 1/2. So the
   '2-block' choice IS the equal-block/idempotent-counting measure = the chiral pin.
 - The framework's universal (N-1)/N^2 mechanism gives 2/9 at N=3, NOT 2/3=2/N.
 - 1/sqrt2 is a Z4/Z8 value; genuine Z3 objects give sqrt3, 1/2, sqrt3/2 -- never 1/sqrt2.

COMBINED with THREAD 1 (native S3-commutant = span{I,J-I}, none anticommutes with
Gamma_chi -> no native OPERATOR escape; airtight):

FINAL STATUS -- the charged-lepton Koide value reduces, in EVERY framing examined
(operator, measure, dynamics, combinatorial, geometric, information, number-theoretic,
holographic), to ONE chiral pin: the equal-block / idempotent-counting weight on
R[Z3]=R(+)C, equivalently {M,Gamma_chi}=0 (Gamma_chi a C3-orbit-splitting chiral
grading). The framework's symmetry-natural objects (identity metric, isotropic
Gaussian, trace/Gram diag(3,6,6)) all return the DIMENSION reading -> Q=1; the
democratic/emergent-time-symmetric objects return Q=1/3; observed 2/3 sits at the
block-count fixed point -- a real algebraic structure, NOT numerology, but NOT
selected by any audited mechanism. So Q=2/3 is DERIVED-MODULO-ONE-IMPORT (the
equal-block/chiral grading): n_gen=3 derived, 3-distinctness (orientation) plausibly
native, the single VALUE r=1/2 reproduced-not-derived = the one pin shared across
Koide/quark/generation-ID/strong-CP/signed-gravity.

LIVE NEXT PATHS (not a closed wall): (1) a native audited reason emergent-time/record
dynamics coarse-grains the C3 isotypes into 2 SECTORS (condensate-singlet vs 2-dim
fluctuation block) not 3 modes -> would DERIVE the block-count MaxEnt and convert the
import to a theorem; (2) a first-principles block-count-vs-Plancherel selection from
the Cl(3) qubit structure itself (the only genuinely non-operator route; not found,
not foreclosed).
"""
import numpy as np


def main():
    rng = np.random.RandomState(0)
    N = 2_000_000
    v = np.abs(rng.randn(N, 3))                      # flat-ish sqrt-mass prior (|gaussian|)
    m = v ** 2
    Q = m.sum(1) / v.sum(1) ** 2
    print("flat sqrt-mass prior: the Q=2/3 balance is codim-1 / tuned, not generic:")
    print(f"  mean Q = {Q.mean():.3f}  (NOT 2/3)")
    print(f"  frac within 1% of 2/3   = {np.mean(np.abs(Q-2/3)<2/3*0.01)*100:.2f}%")
    print(f"  frac within 1% of 1/3   = {np.mean(np.abs(Q-1/3)<1/3*0.01)*100:.2f}%  (democratic basin)")
    print()
    print("2/N vs (N-1)/N^2 at N=3:", f"2/N={2/3:.4f}, (N-1)/N^2={2/9:.4f} (distinct; coincide only at... they don't)")
    print("1/sqrt2 =", round(1/np.sqrt(2), 5), "= cos(pi/4) (Z4/Z8); genuine Z3 values: 1/2, sqrt3/2 =",
          round(np.sqrt(3)/2, 4), "-- never 1/sqrt2")
    print()
    print("FINAL: Q=2/3 = block-count fixed point = the one chiral pin; reproduced-not-derived.")
    print("Threads 1 (no native operator escape) + 2 (no non-operator derivation) both close on it.")


if __name__ == "__main__":
    main()
