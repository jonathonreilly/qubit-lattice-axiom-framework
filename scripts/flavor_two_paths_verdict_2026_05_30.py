#!/usr/bin/env python3
"""
Two-paths press (workflow wf_33a8ac1e): is native Q=2/3 forced via (1) A1's trace
forcing the block-count weighting, or (2) a native variational saddle at
b/a=1/sqrt2? Verdict: NEITHER -- and Track 1 INVERTS, correcting this session's
'native lean toward 2/3'.

TRACK 1 -- INVERTED. A1's matrix-algebra trace does NOT force block-count(->2/3);
it forces DIMENSION (->Q=1). The C3-symmetric Hermitian mass operator is
M = a I + b C + conj(b) C^2 with b COMPLEX (a real). The doublet isotype =
(Re b, Im b) = TWO real dof; the singlet = a = ONE dof. Tr(M^2)=3a^2+6|b|^2; the
canonical trace-induced (HS-isotropic) Gaussian e^{-Tr(M^2)/2} gives, by Schur,
E[||proj onto k-dim block||^2] = k -> doublet:singlet = 2:1 = DIMENSION -> Q=1
(verified: isotype HS-weight ratio = 2.00; median Q = 1.34). Block-count (1:1 ->
Q=2/3) is recovered ONLY by setting Im b = 0 (collapsing the doublet to ONE real
coordinate) -- a real-structure IMPORT beyond the trace.

==> CORRECTION to this session's moves 3 / 'B' / exactness-closure: those computed
the covariant measure with REAL b (Im b=0) IMPLICITLY and got median Q=2/3. With
the FULL complex-b operator (the physical case -- theta=arg(b)!=0 is exactly what
splits e,mu,tau into 3 distinct masses), the SAME covariant trace measure gives
median Q=1.34 (dimension). So 'the native covariant measure ranks toward 2/3' was
an artifact of the real-b restriction. A1's canonical full-operator measure ranks
toward Q=1.

TRACK 2 -- a concentrating saddle at b/a=1/sqrt2 EXISTS but is CONDITIONAL. The
2-sector Shannon entropy of {3a^2, 6b^2} stationarizes at b/a=sqrt2/2 with S''<0
(genuine per-operator maximum, not a median). But its location rides on the SAME
block weighting: the general weighted-log saddle is r*=nu/(2mu); r=1/2 iff nu=mu =
equal BLOCK weight = the Track-1 open choice. Every block-saddle functional has a
dimension-reading twin landing at r=1 (Q=1). The only UNCONSTRAINED native saddle
is b=0 (uniform condensate, Q=1/3). Placing a minimum AT r=1/2 unconditionally
requires F=(r-1/2)^2 -- reverse-engineered/circular.

NET (corrected value-question state):
 - A1 canonical full-operator covariant measure -> median Q ~ 1.34 (DIMENSION/Q=1).
 - unconstrained native dynamics (condensate saddle) -> Q = 1/3 (uniform b=0).
 - block-count -> Q=2/3 requires the Im b=0 / doublet-phase-not-a-dof restriction
   (an import), in TENSION with the physical theta!=0 (3 distinct masses).
 - EXACT 2/3 = the chiral constraint {M,Gamma_chi}=0 (retained theorem; Gamma_chi
   non-native, retained_bounded no-go).
 - data needs Q=2/3 (0.91 sigma) -- which is NEITHER the A1-native (1) NOR the
   dynamics (1/3); it needs an IMPORT.
Both tracks reduce to the SAME single d.o.f.: does the doublet's 2nd real
coordinate (Im b = the phase theta) count as a measure dof? A1's full operator
says YES -> (1,2) -> Q=1; block-count needs NO -> (1,1) -> Q=2/3. Neither makes
(1,1) forced; A1 actually votes (1,2).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    rng = np.random.RandomState(11)
    N = 2_000_000
    a = rng.randn(N) / np.sqrt(3)
    reb = rng.randn(N) / np.sqrt(6)
    imb = rng.randn(N) / np.sqrt(6)

    sep("TRACK 1: full complex-b covariant measure -> DIMENSION (Q=1), not block-count")
    for name, b2 in [("COMPLEX b (2 dof, FULL operator)", reb ** 2 + imb ** 2),
                     ("REAL b   (Im b=0, 1 dof)", reb ** 2)]:
        Q = 1 / 3 + 2 / 3 * b2 / a ** 2
        print(f"  {name:34s}: median Q={np.median(Q):.3f}")
    print(f"  isotype HS-weight ratio doublet/singlet: complex={np.mean(6*(reb**2+imb**2))/np.mean(3*a**2):.2f} (DIM)"
          f"  real={np.mean(6*reb**2)/np.mean(3*a**2):.2f} (block)")
    print("  => A1 trace forces DIMENSION (2:1, Q=1). 2/3 needs Im b=0 import. Corrects moves 3/B/closure.")

    sep("TRACK 2: entropy saddle at b/a=1/sqrt2 exists but is block-weight-conditional")
    print("  2-sector entropy of {3a^2,6b^2} stationary at b/a=sqrt2/2, S''<0 (genuine max).")
    print("  but weighted-log saddle r*=nu/(2mu); r=1/2 iff nu=mu = equal BLOCK weight (Track-1 choice).")
    print("  unconstrained native saddle = b=0 (Q=1/3). Minimum AT r=1/2 unconditionally = F=(r-1/2)^2 (circular).")

    sep("NET (corrected)")
    print("  A1 canonical measure -> Q=1 (dim);  dynamics -> Q=1/3 (b=0);  data -> Q=2/3 needs an IMPORT.")
    print("  Block-count/2/3 = the Im b=0 (doublet-phase-not-a-dof) restriction, in tension w/ theta!=0")
    print("  (the 3-distinct spectrum). Exact 2/3 = chiral {M,Gamma_chi}=0 import. The session's 'native")
    print("  lean toward 2/3' is RETRACTED: it used real b; A1's full-operator measure votes Q=1.")


if __name__ == "__main__":
    main()
