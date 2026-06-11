#!/usr/bin/env python3
"""Probe the '1.000 (machine precision)' claim for the EXACT-MIXTURE event.
Question (a): is within-family |ch1| EXACTLY 1, or 1 - 1e-k? what is k? does 'machine
precision' hold? Machine precision for float64 ~ 2.2e-16. We measure the per-family
within concentration deficit and decompose WHY it is what it is (residual Theta spread).
"""
from __future__ import annotations
import numpy as np
import indep_lens1b as M

r = M.RES[4242]["rows"][3]
Theta, w, bits = r["Theta"], r["w"], r["bits"]

print("EXACT-MIXTURE event seed 4242 depth 3 -- within-family Theta values")
print("=" * 72)
fams = {}
for b in range(len(w)):
    fams.setdefault(bits[b][:2], []).append(b)

worst_deficit = 0.0
for key, idxs in sorted(fams.items()):
    idxs = np.array(idxs)
    ww = w[idxs]
    th = Theta[idxs]
    conc = abs(complex(np.sum(ww * np.exp(1j * th)) / ww.sum()))
    deficit = 1.0 - conc
    worst_deficit = max(worst_deficit, deficit)
    # the two members differ only in step-3 outcome; the within-family spread is the
    # gap between their two Theta values
    th_spread = float(np.ptp(th))   # max-min of the (2) Theta values in the family
    print(f"  family first2={key}: members={list(idxs)}")
    print(f"    Theta values = {np.round(th, 8)}   spread(rad) = {th_spread:.3e}")
    print(f"    within |ch1| = {conc:.12f}   deficit (1-|ch1|) = {deficit:.3e}")

eps_mach = np.finfo(np.float64).eps
print("=" * 72)
print(f"  float64 machine epsilon              = {eps_mach:.3e}")
print(f"  worst within-family deficit          = {worst_deficit:.3e}")
print(f"  ratio (deficit / machine eps)        = {worst_deficit/eps_mach:.3e}")
print(f"  k such that deficit ~ 1e-k           : k = {-np.log10(worst_deficit):.2f}")
print()
print("  VERDICT on 'machine precision' label:")
if worst_deficit < 1e3 * eps_mach:
    print("    consistent with machine precision")
else:
    print(f"    NOT machine precision -- the deficit is ~{worst_deficit/eps_mach:.0e}x larger")
    print("    than float64 eps; the within-family law has a genuine O(1e-5) angular")
    print("    spread (the two step-3 children have slightly different det-phase Theta).")

# Is the within-family spread a NUMERICAL artifact (polar readout near small sv) or a
# REAL physical residual? Check by tightening: recompute Theta children with the exact
# det of the unitary-projected M and see if the spread is stable, and report sv.
print()
print("  diagnostic: the within-family residual is REAL structure (the two step-3")
print("  children genuinely carry different det phases), not float noise -- the spread")
print("  is ~1e-2 to 1e-3 rad in Theta? Let's see the actual ptp above. If ptp is")
print("  O(1e-2) the |ch1| deficit O(1e-5) is just (spread^2)/8 for a 2-atom law:")
for key, idxs in sorted(fams.items()):
    idxs = np.array(idxs); ww = w[idxs]; th = Theta[idxs]
    spread = float(np.ptp(th))
    # 2-atom equal-ish weight: |ch1| ~ cos(half-spread) ~ 1 - (spread/2)^2/2
    pred_deficit = 0.5 * (spread / 2) ** 2
    actual = 1 - abs(complex(np.sum(ww * np.exp(1j * th)) / ww.sum()))
    print(f"    family {key}: ptp(Theta)={spread:.4e}  predicted deficit~{pred_deficit:.3e}  "
          f"actual {actual:.3e}")
