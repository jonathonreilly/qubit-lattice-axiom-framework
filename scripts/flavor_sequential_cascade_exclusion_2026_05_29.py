#!/usr/bin/env python3
"""
Test of the sequential / open-chain (emergent-time cascade) breaking method
for charged-lepton Koide Q=2/3. Does breaking the cyclic C_3 to a LINEAR
order (open chain) land natively at r=1/2 (Q=2/3)?

RESULT: NO -- and the failure is informative.
- The open-chain operator DOES reach the Gamma_chi-odd sector (unlike every
  C_3-symmetric method), BUT its physical (positive-sqrt-mass) SPECTRUM caps
  at Q = 5/9 < 2/3. A uniform sequential cascade CANNOT reach 2/3.
- Non-uniform chains reach 2/3 only on a tuned measure-zero surface.
- KEY: Q_obs = 2/3 > 5/9 (open-chain max). The leptons are MORE balanced
  than any uniform temporal cascade -> the data DISFAVORS the sequential
  cascade and FAVORS the cyclic (circulant/Brannen) balanced structure,
  where r=1/2 is the free amplitude modulus.

NEW BOUNDED RESULT: the framework forbids the charged-lepton spectrum from
arising as a uniform sequential (open-chain) cascade (cap Q<=5/9).
"""

import numpy as np


def Q(s):
    s = np.abs(np.array(s, float))
    return (s * s).sum() / s.sum() ** 2


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    hop = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0.]])  # open 3-chain, open BC

    sep("(1) uniform open chain caps at Q=5/9 (cannot reach 2/3 physically)")
    print("  sqrt-mass = eigenvalues of d*I + t*hop_open; positivity needs t/d < 1/sqrt2")
    qmax = 0
    for td in np.linspace(0, 1/np.sqrt(2), 8):
        s = 1 + td * np.array([np.sqrt(2), 0, -np.sqrt(2)])
        if s.min() >= -1e-12:
            qmax = max(qmax, Q(s))
            print(f"    t/d={td:.3f}: sqrt-masses={np.round(np.sort(s),3)}  Q={Q(s):.4f}")
    print(f"  => Q caps at 5/9 = {5/9:.4f} (at t/d=1/sqrt2); 2/3 = {2/3:.4f} is UNREACHABLE.")

    sep("(2) non-uniform chains hit 2/3 only on a tuned measure-zero surface")
    rng = np.random.default_rng(0); reached = 0; hits = 0
    for _ in range(20000):
        d = rng.uniform(0.5, 2, 3); t = rng.uniform(0, 1)
        H = np.diag(d) + t * hop
        s = np.linalg.eigvalsh(H)
        if s.min() >= 0:
            reached += 1
            if abs(Q(s) - 2/3) < 0.01:
                hits += 1
    print(f"  positive-spectrum chains: {reached}/20000; within 0.01 of 2/3: {hits}"
          f" ({hits/max(reached,1)*100:.2f}% -> measure-zero / tuned)")

    sep("(3) the data DISFAVORS the cascade, FAVORS the cyclic-balanced structure")
    sm = np.sqrt([0.51099895, 105.6583755, 1776.86])
    print(f"  observed charged-lepton Q = {Q(sm):.5f} = 2/3")
    print(f"  open-chain (uniform cascade) maximum Q = 5/9 = {5/9:.4f}")
    print(f"  2/3 ({2/3:.4f}) > 5/9 ({5/9:.4f}): the leptons are MORE balanced than")
    print("  any uniform temporal cascade can produce. So the generations do NOT")
    print("  break into a linear/sequential order; they retain the CYCLIC balance")
    print("  (circulant/Brannen form), where r=|b|^2/a^2=1/2 is the free amplitude.")

    sep("VERDICT: sequential/open-chain breaking ruled out; flat direction confirmed")
    print("  The open-chain operator reaches the Gamma_chi-odd sector (good), but its")
    print("  physical spectrum caps at 5/9 < 2/3 (uniform) or needs tuning (non-uniform).")
    print("  No native sequential-generation mechanism exists. So even the last")
    print("  distinct NATIVE breaking candidate does not force r=1/2 -- confirming the")
    print("  flat-direction conclusion from the sequential/temporal-order direction.")
    print("  NEW BOUNDED RESULT (falsifiable): the framework forbids the charged-lepton")
    print("  spectrum from arising as a uniform sequential (open-chain) cascade: Q<=5/9.")
    print("  The data places the leptons at the cyclic-balanced point (2/3>5/9), i.e.")
    print("  the circulant structure with the amplitude r=1/2 a contingent flat direction.")


if __name__ == "__main__":
    main()
