#!/usr/bin/env python3
"""J:attack-a:PR9359 -- WITNESS REALIZABILITY: the stated parameters, limits and the arms of the microscopic-transmon note exist in the declared setting.

Checks, exactly where the note is exact: (1) alpha = (Ja - Jb)/(Ja + Jb) with Ja/Jb = (256*257)/(178*143) equals 0.442079652807 (exact rational, reduced); Bb = 0.8*256/178 T; the field ratios B/Ba = 0.1875 and B/Bb = 0.1304 are below one, so the sinc arguments m B/Bnode stay in the main lobe for m <= 5 and the first zero of sinc(m B/Bnode) is at m = Bnode/B (5.33 and 7.67), so the envelope changes sign at m = 6 (arm a) and m = 8 (arm b), inside the harmonics kept by the model (m <= 14): the 'signed' envelopes are realised;
(2) the short-channel potential r_tau(phi) = 4 s/[1 + sqrt(1 - tau s)] is real and finite for every 0 <= tau < 1 and phi (the radicand 1 - tau s >= 1 - tau > 0), reduces to 1 - cos(phi) at tau = 0 (Fourier coefficients a_m = 0 for m >= 2 to 1e-15), and its first cosine coefficient a_1 is nonzero and negative for all tau tested in [0, 0.99], so 'minus twice the first coefficient' is a well-defined positive normalisation;
(3) at tau -> 1 the coefficients stay finite (r_1 = 4 s/(1 + cos(phi/2)) is bounded), so the calibrated tau values (about 0.08 - 0.15, see the falsifier of this PR) lie well inside the domain.
Prints SUMMARY:; HIT only if a stated parameter or limit is not realisable.
"""
import sys
from fractions import Fraction as Fr
import numpy as np
ok = True
ALPHA = Fr(256 * 257 - 178 * 143, 256 * 257 + 178 * 143)
print(f"   alpha = {ALPHA} = {float(ALPHA):.12f}; Bb = 0.8*256/178 = {0.8 * 256 / 178:.6f} T")
c1 = abs(float(ALPHA) - 0.442079652807) < 5e-13
print(f"[{'PASS' if c1 else 'FAIL'}] alpha = 0.442079652807 to 5e-13 (exact fraction above)"); ok &= c1
B, BA, BB = 0.15, 0.8, 0.8 * 256 / 178
z0a, z0b = BA / B, BB / B
c2 = B / BA < 1 and B / BB < 1 and int(np.floor(z0a)) == 5 and int(np.floor(z0b)) == 7
print(f"[{'PASS' if c2 else 'FAIL'}] B/Ba = {B / BA:.4f}, B/Bb = {B / BB:.4f} < 1; the first sinc zeros are at m = {z0a:.3f} and {z0b:.3f}: the envelopes change sign at m = 6 (arm a) and m = 8 (arm b)"); ok &= c2
def local(ph, tau):
    s = np.sin(ph / 2) ** 2
    return 4 * s / (1 + np.sqrt(1 - tau * s))
def cosc(tau, M=8192, mmax=14):
    ph = (np.arange(M) + 0.5) * 2 * np.pi / M
    r = local(ph, tau)
    return np.array([(2.0 / M) * np.sum(r * np.cos(m * ph)) for m in range(mmax + 1)])
a0 = cosc(0.0)
c3 = np.max(np.abs(a0[2:])) < 1e-14 and abs(a0[1] + 1) < 1e-14
print(f"[{'PASS' if c3 else 'FAIL'}] tau = 0: r = 1 - cos(phi): a_1 = {a0[1]:+.15f}, max |a_m| for m >= 2 = {np.max(np.abs(a0[2:])):.1e}"); ok &= c3
taus = np.linspace(0, 0.99, 100)
a1s = np.array([cosc(t)[1] for t in taus])
c4 = np.all(a1s < 0) and np.all(np.isfinite(a1s)) and np.all(np.abs(a1s) > 0.5)
print(f"[{'PASS' if c4 else 'FAIL'}] a_1(tau) is finite, negative and bounded away from zero for 100 values of tau in [0, 0.99]: range [{a1s.min():.4f}, {a1s.max():.4f}]"); ok &= c4
a99 = cosc(0.999999)
c5 = np.all(np.isfinite(a99)) and abs(a99[1]) > 0.5
print(f"[{'PASS' if c5 else 'FAIL'}] tau -> 1: coefficients stay finite (tau = 0.999999: a_1 = {a99[1]:+.4f}, a_2 = {a99[2]:+.4f})"); ok &= c5
if ok:
    print("SUMMARY: no purchase: the note's parameters and limits are realisable: alpha reduces to 0.442079652807 exactly from the stated ratio, the sinc envelopes are below their first zeros for the fundamental and change sign at m = 6 and 8 as 'signed' implies, the short-channel potential is real and finite on 0 <= tau < 1 and reduces to a cosine at tau = 0, and its first coefficient never vanishes")
else:
    print("SUMMARY: a stated parameter or limit is not realisable"); print("HIT: see failed check")
sys.exit(0)
