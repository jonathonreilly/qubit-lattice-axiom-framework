#!/usr/bin/env python3
"""
Self-correction runner: the F1/F3 (Q=2/3 vs Q=1) selection is UNDETERMINED
between TWO canonical measures on R[Z_3] = R (+) C, NOT a prediction of Q=1.

Retracts the "framework predicts Q=1" overreach. Both measures below are
canonical and internally consistent; pure representation theory ranks
neither above the other.

  Q = 1/3 + (2/3) r,  r = |b|^2/a^2.  E_+ = 3a^2 (trivial), E_perp = 6|b|^2 (doublet).
  Balance per weight: 3a^2/w_+ = 6|b|^2/w_perp  =>  r = 3 w_perp / (6 w_+).
"""

import numpy as np


def Q(r):
    return 1/3 + 2/3 * r


def r_balance(w_plus, w_perp):
    return 3 * w_perp / (6 * w_plus)


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("(1) TWO canonical measures on R[Z_3] = R (+) C")
    print("  R[Z_3] real Wedderburn decomposition: R (+) C")
    print("    -> 2 minimal central idempotents (real-irreducible blocks):")
    print("       P_+ (trivial, real irrep, FS +1) and P_perp (doublet, complex type).")
    print()
    schemes = [
        ("DIMENSION / trace (Plancherel)  weight by real dim", 1, 2),
        ("BLOCK / central-idempotent count weight each block 1", 1, 1),
    ]
    for name, wp, wpp in schemes:
        r = r_balance(wp, wpp)
        print(f"  {name}")
        print(f"      (w_+, w_perp)=({wp},{wpp})  ->  r={r:.3f}  Q={Q(r):.4f}"
              f"  ({'F3 = Q=1' if abs(r-1)<1e-9 else 'F1 = Q=2/3'})")
    print()
    print("  => DIMENSION measure -> Q=1 ;  BLOCK measure -> Q=2/3.")
    print("     Both canonical & consistent. Rep theory ranks NEITHER.")
    print("     'framework predicts Q=1' is RETRACTED -> UNDETERMINED.")

    sep("(2) number of minimal central idempotents of R[Z_d] (= # blocks)")
    def n_real_blocks(d):
        b = 1                     # trivial
        if d % 2 == 0: b += 1     # sign rep (real)
        b += (d - 1) // 2         # complex conjugate-pair blocks
        return b
    for d in [2, 3, 4, 5, 6]:
        print(f"    Z_{d}: {n_real_blocks(d)} real-irreducible blocks"
              f"{'   <- d=3: 2 blocks (1 real + 1 complex)' if d == 3 else ''}")
    print("  For Z_3 the block-count measure is uniform on 2 blocks = (1,1) = F1.")

    sep("(3) what the campaign DID establish (still valid, narrower scope)")
    print("  trace/dimension-type mechanisms all realize the DIMENSION measure -> F3:")
    for m in ["canonical/Plancherel trace", "Tomita-Takesaki modular flow",
              "Euclidean-Jordan trace", "Gaussian functional determinant",
              "Kahler/Bargmann measure", "reflection-positivity saturation",
              "perturbative + nonperturbative dynamics"]:
        print(f"    - {m}  -> F3 (Q=1)")
    print("  ALL are trace/dimension-type. NONE is the block-count measure")
    print("  (counting measure on central idempotents, not a trace) -> F1 (Q=2/3)")
    print("  remains canonical and UNTOUCHED by these. So: 'IF trace-type, Q=1';")
    print("  trace-type is NOT forced.")

    sep("VERDICT (corrected): UNDETERMINED between two canonical measures")
    print("  A1+A2+retained admit BOTH Q=1 (dimension/trace) and Q=2/3")
    print("  (block/sector-count); neither is forced. = main's open_gate status.")
    print("  OPEN PHYSICS QUESTION: does charged-lepton mass-generation weight")
    print("  the C_3 isotypes by the TRACE (dimension -> Q=1; thermal/spectral)")
    print("  or by the BLOCK/SECTOR count (-> Q=2/3; democratic over distinct")
    print("  superselection sectors)? Observed Q=2/3 favors the sector reading")
    print("  -- a falsifiable hint, not a framework refutation, and not settled.")


if __name__ == "__main__":
    main()
