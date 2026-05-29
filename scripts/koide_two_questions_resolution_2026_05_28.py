#!/usr/bin/env python3
"""
Resolving "how can the framework give BOTH Q=1 and Q=2/3?"

It cannot, physically. Pure representation theory is agnostic between two
canonical measures, but they answer DIFFERENT physical questions; only one
is the right question for a charged-lepton MASS SPECTRUM.

  QUESTION A (thermal / dynamical): if the C_3 generation doublet is a
    FLUCTUATING field, what spread does equilibrium / a condensate give?
    -> weight by thermal dof = real dimension (1,2) = the TRACE measure
    -> r = 1, Q = 1.  (every dynamical probe landed here, or on an
       irrational tuned root -- never the clean 2/3.)

  QUESTION B (structural / representation): weight the Z_3-IRREDUCIBLE
    BLOCKS of the FIXED mass operator equally (counting measure on the two
    minimal central idempotents of R[Z_3]=R(+)C).
    -> weight by irreducible block (1,1) = the BLOCK measure
    -> r = 1/2, Q = 2/3  EXACTLY (a clean rational).

The observed Q = 2/3 (to 1e-5, a clean rational) answers QUESTION B. So
the charged-lepton masses are a REPRESENTATION-STRUCTURAL spectrum (counted
by Z_3 block), NOT a thermal/dynamical condensate (which gives Q=1 or an
irrational value). The Q=1 'measure' is the answer to a question the
charged-lepton masses are not asking.
"""

import math


def Q(r):
    return 1/3 + 2/3 * r


def r_gap_root():
    # NJL/gap-equation self-consistent doublet:singlet root s/d = 4 - 3 sqrt(2)
    # giving sqrt-mass slots (s, d, d) with the doublet degenerate; r = |b|^2/a^2
    # via a = (s+2d)/3-type combination. Illustrative: a generic dynamical root
    # is NOT the clean rational 1/2.
    s_over_d = 4 - 3 * math.sqrt(2)     # ~ -0.2426 (irrational)
    return s_over_d


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("QUESTION A -- thermal/dynamical (fluctuating doublet field) -> Q=1")
    print("  weight the doublet by its thermal dof = 2 real dims (the TRACE):")
    print(f"    equipartition / condensate:  r = 1.0   Q = {Q(1.0):.4f}  (F3)")
    print("  campaign dynamical probes (free, interacting, condensate, RG, gap)")
    print("  ALL gave Q=1 or an IRRATIONAL tuned root -- never the clean 2/3.")
    print(f"    (gap-eqn root s/d = 4-3*sqrt2 = {r_gap_root():.4f}: irrational, not 1/2)")

    sep("QUESTION B -- structural/representation (fixed mass operator) -> Q=2/3")
    print("  weight the Z_3-IRREDUCIBLE BLOCKS equally (counting measure on the")
    print("  2 minimal central idempotents of R[Z_3]=R(+)C):")
    print(f"    block (1,1):  r = 0.5   Q = {Q(0.5):.4f}  (F1) -- a CLEAN RATIONAL")

    sep("WHICH QUESTION are the charged-lepton masses asking?")
    Q_obs = 0.6666605
    print(f"  observed Q (PDG)  = {Q_obs:.7f}  -- a clean rational 2/3 to 1e-5")
    print(f"  |Q_obs - 2/3|/(2/3) = {abs(Q_obs-2/3)/(2/3)*100:.4f}%")
    print(f"  |Q_obs - 1|         = {abs(Q_obs-1):.4f}  (thermal answer is far off)")
    print("  => the masses answer QUESTION B (structural/block), NOT A (thermal).")
    print("  The SHARP RATIONAL 2/3 is a representation-theoretic signature:")
    print("  a thermal/dynamical mechanism gives Q=1 or an irrational value;")
    print("  only the block/representation structure gives the clean 2/3.")

    sep("RESOLUTION")
    print("  There are not two answers to one question -- there are two")
    print("  questions. Pure rep theory is agnostic (both measures canonical),")
    print("  but PHYSICS picks the question: the charged leptons are a FIXED,")
    print("  sharp, non-mixing mass SPECTRUM organized by Z_3 representation,")
    print("  so the representation/block weighting is the physical one -> Q=2/3.")
    print("  The Q=1 'prediction' answers 'what if the masses were a thermal")
    print("  condensate' -- which they are not (it gives the wrong, non-rational")
    print("  region). DERIVED from A1+A2: the Z_3 block structure + the algebraic")
    print("  equivalence Q=2/3 <=> equal-block. IDENTIFICATION (data-confirmed,")
    print("  not yet first-principles-derived): that charged-lepton mass-")
    print("  generation is structural (block) not thermal (trace). The sharp")
    print("  rational 2/3 is the evidence -- and the framework makes the")
    print("  thermal-vs-structural dichotomy precise and falsifiable.")


if __name__ == "__main__":
    main()
