#!/usr/bin/env python3
"""
Bridge-gap / native-action angle on r=|b|^2/a^2: the fermion vacuum will not
generate the corner coupling b (3 computations). Does the CASIMIR-NATIVE action
structure supply it? The canonical Casimir-native object on the framework's
(Z2)^3 corner cube is the heat kernel K_t = exp(-t*Laplacian) on the cube graph
Q3 -- no import (it IS the Casimir propagator; the bare Laplacian is the t->0
action, the heat kernel its resolvent).

Cube graph Q3: Laplacian eigenvalue for character S is 2|S|, so
  K_t(d) = ((1+u)/2)^(3-d) ((1-u)/2)^d ,  u=exp(-2t),  d=Hamming distance.
Generation triplet = hw=1 corners. diagonal a=K_t(0)=((1+u)/2)^3; off-diagonal
(all pairs are d=2) b=K_t(2)=((1+u)/2)((1-u)/2)^2. The induced generation Yukawa
Y = a I + b(J-I) (C3-symmetric) has sqrt-masses {a+2b, a-b, a-b}, giving
  Q = 1/3 + (2/3) r ,  r = (b/a)^2 ,  b/a = ((1-u)/(1+u))^2 = tanh(t)^2.
So  r = tanh(t)^4  and  Q = 1/3 + (2/3) tanh(t)^4.

FINDINGS:
 - This is the FIRST native, import-free structure where r spans (0,1) as a
   single clean function of one parameter, and r=1/2 (Q=2/3) appears as a
   specific INTERIOR point: tanh(t) = 2^(-1/4), i.e. b/a = 2^(-1/4) = 0.8409,
   t = atanh(2^(-1/4)) = 1.2242. (Contrast the fermion vacuum, which drives
   r->0.)
 - BUT the heat-kernel time t is a free modulus. r=1/2 is NOT forced; it just
   re-expresses the unforced ratio b/a as an unforced t. The naive t=1 gives
   Q=0.558 (not 2/3); no special/derived t lands on 1.224 here.

HONEST STATUS: a clean native characterization (r=tanh^4 t), NOT a derivation.
It relocates the single modulus from b/a to the Casimir time t, and gives a
concrete next question: does the framework fix t (the Casimir proper time / the
generation self-energy scale)? CAVEAT: the identification of the generation mass
matrix with the cube heat kernel is a CANDIDATE (position-cube object vs the
momentum-corner generations), not established -- so this is a lead on the
bridge-gap action, not a result about the leptons.
"""

import numpy as np
from scipy.optimize import brentq


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def ba(t):
    return np.tanh(t) ** 2          # b/a = ((1-u)/(1+u))^2 = tanh(t)^2


def r_of(t):
    return ba(t) ** 2               # r = tanh(t)^4


def Q_of(t):
    return 1 / 3 + 2 / 3 * r_of(t)


def main():
    sep("Casimir heat kernel on the corner cube Q3 -> generation r = tanh(t)^4")
    print("   t       b/a       r        Q")
    for t in [0.3, 0.5, 0.8, 1.0, 1.2242, 1.5, 2.0, 3.0]:
        tag = "  <-- Q=2/3" if abs(Q_of(t) - 2 / 3) < 5e-4 else ""
        print(f"  {t:.4f}   {ba(t):.4f}   {r_of(t):.4f}   {Q_of(t):.4f}{tag}")

    sep("r=1/2 point and the natural-t check")
    tstar = brentq(lambda t: r_of(t) - 0.5, 0.5, 3.0)
    print(f"  r=1/2 (Q=2/3) at t={tstar:.4f}: tanh(t)=2^(-1/4)={2**-0.25:.4f}, b/a=2^(-1/4)={ba(tstar):.4f}")
    print(f"  naive t=1 (if Casimir time ~ g_bare=1): Q={Q_of(1):.4f}  (NOT 2/3)")
    print("  => r=1/2 re-expressed as an unforced heat-kernel time t; no derived t lands here.")

    sep("VERDICT")
    print("  First native (import-free) structure giving the full r in (0,1) as r=tanh^4(t),")
    print("  with r=1/2 a clean interior point (b/a=2^-1/4). NOT a derivation: the modulus")
    print("  moves from b/a to the Casimir time t (naive t=1 -> Q=0.558, not 2/3). Open")
    print("  question for the bridge-gap action: what fixes t (the Casimir proper time)?")
    print("  CAVEAT: cube-heat-kernel <-> generation mass-matrix identification is a")
    print("  candidate, not established. A lead on the action, not a lepton result.")


if __name__ == "__main__":
    main()
