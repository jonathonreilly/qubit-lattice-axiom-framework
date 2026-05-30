#!/usr/bin/env python3
"""
DERIVE-THE-BLOCK-COUNT-PIN press (wf_1887d84a, 2 tracks, 7 angles, 0 survived) +
verification. Neither emergent-time/records (T1) nor the Cl(3) qubit (T2) converts
the block-count weight into a theorem. But the pin is sharpened to its sharpest
form and a genuine new positive is derived.

(A) THE PIN, sharpest form: the C3-symmetric generation algebra is R[Z3]=R(+)C with
    TWO minimal central idempotents (singlet R, doublet C). The value is the WEIGHT:
      - center trace Z(R[Z3])=R(+)R, 2 equal idempotents: (1,1) -> r=1/2 -> Q=2/3 (observed)
      - full-algebra trace / Plancherel / retained Gram diag(3,6,6)=3(1,2,2): (1,2) ->
        r=1 -> Q=1.
    EVERY canonical native object (identity metric, isotropic Gaussian, regular/Plancherel/
    Haar trace, einselected Born weight on the retained tracial reference rho=I/3) votes
    DIMENSION -> Q=1. Democratic/3-mode -> Q=1/3. Block-count (2/3) is ONLY the center trace
    (or the Im b=0 real slice) -- selected by NO audited mechanism.

(B) NEW POSITIVE (Track 1): the 2-SECTOR PARTITION is natively derived. A real circulant
    H=aI+b(C+C^2) energy-DEGENERATES the two C3 doublet phases (+-2pi/3) -> a single clock /
    einselection cannot resolve them -> EXACTLY 2 energy sectors (singlet vs doublet block) =
    1 objective record bit. Cleaner than the prior democratic Schur framing. BUT it is the
    PARTITION (count 2 sectors), not the WEIGHT.

(C) The redundancy-objectivity lead (quantum-Darwinism R_delta is probability-INDEPENDENT, so
    "1 objective sector = 1 equal vote" would give the center-trace (1,1) weight) DERIVES THE
    PARTITION but CANNOT reweight Q. The observed leptons are 3 DISTINCT masses (the doublet IS
    2 physical generations mu,tau, counted SEPARATELY); Q is a fixed function of the 3 spectral
    masses. Counting the doublet ONCE (2-sector) gives Q=0.807 != 2/3 -- it contradicts the
    3-distinct spectrum. So objectivity gives the partition, not the value: same wall as Track 1.

HONEST STATUS: Q=2/3 = derived-modulo-the-block-count pin. The pin is now ONE sharply-posed
question -- center trace (idempotent-count -> 2/3) vs full-algebra trace (Plancherel/dimension
-> 1) on R[Z3]=R(+)C -- with every canonical native object voting full-trace/dimension and the
2-sector partition (but not the weight) natively derived. The observed operator sits at the
block-count fixed point r=1/2, a specific non-generic point no native selector reaches.
"""
import numpy as np


def main():
    print("(A) weights: full-trace/Plancherel/Gram(3,6,6) -> (1,2) -> Q=1;  center trace -> (1,1) -> Q=2/3")
    a, b = 1.0, 0.4
    ev = np.array([a + 2 * b, a - b, a - b])
    print(f"(B) partition: real circulant eigenvalues {np.round(ev,3)} -> 2 energy sectors (doublet degenerate). DERIVED.")
    Q = lambda e: (e ** 2).sum() / np.sqrt(np.abs(e ** 2)).sum() ** 2
    s, d = 2.414, 0.293
    print(f"(C) 3-mode (doublet x2, physical): Q={Q(np.array([s,d,d])):.4f}=2/3 (observed);  "
          f"2-sector (doublet x1): Q={Q(np.array([s,d])):.4f} != 2/3")
    print("    -> objectivity derives PARTITION not WEIGHT (mu,tau are 2 physical generations).")
    print("VERDICT: no survivor; pin = center-trace vs full-trace; partition derived, weight not.")


if __name__ == "__main__":
    main()
