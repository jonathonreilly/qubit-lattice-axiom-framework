#!/usr/bin/env python3
"""Corrected Delta_R as an HONEST BOUND (memory-safe: single process, N<=48,
list-of-4-arrays, del+gc between allocations; peak RAM < ~700 MB).

Assembles Delta_R = (alpha_LM/4pi)[C_F*Delta_1 + C_A*Delta_2 + T_F n_f*Delta_3]
with the three channels treated per the verified findings:

  Delta_1 (C_F, scalar):  corrected scalar I_S WITHOUT the /N_TASTE double-count
                          (-> I_S~32.4, Delta_1 = 2*I_S - 6).  This is the
                          single-link 1-loop value, which the spot-check found
                          NON-PERTURBATIVE/uncontrolled -- a bound, not a result.
  Delta_2 (C_A, gluonic): CLEAN (D_g^2 vanishes only at origin); unchanged.
  Delta_3 (T_F n_f):      production single-corner subtraction is regulator-
                          dependent (BROKEN). Use FULL 16-doubler subtraction +
                          m^2->0 extrapolation to recover a finite constant C_f,
                          then show the channel for BOTH candidate taste powers
                          (/16, /256). It is subdominant either way.

Output: the corrected channel breakdown and Delta_R, vs the runner's -3.27%.
"""
from __future__ import annotations
import math, gc
import numpy as np

PI = math.pi
TWO_PI = 2.0 * PI
S16 = 16.0 * PI * PI

# canonical-surface constants
try:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from canonical_plaquette_surface import (CANONICAL_U0, CANONICAL_ALPHA_LM)
    U0 = float(CANONICAL_U0)
    ALPHA_LM = float(CANONICAL_ALPHA_LM)
except Exception:
    U0 = 0.5934 ** 0.25
    ALPHA_LM = 0.09067
ALPHA_LM_4PI = ALPHA_LM / (4.0 * PI)

C_F = 4.0 / 3.0
C_A = 3.0
T_F = 0.5
N_F = 6
N_TASTE = 16.0
GAMMA_S = -6.0
REPORTED_DELTA_R = -0.0327


def comps(N):
    d = TWO_PI / N
    g = -PI + (np.arange(N, dtype=np.float64) + 0.5) * d
    K = list(np.meshgrid(g, g, g, g, indexing="ij"))
    return K, (d / TWO_PI) ** 4


def Dpsi(K): return sum(np.sin(k) ** 2 for k in K)
def Dg(K): return 4.0 * sum(np.sin(k / 2.0) ** 2 for k in K)
def Fg(K): return sum(np.cos(k / 2.0) ** 2 for k in K)
def ksq(K): return sum(k * k for k in K)
def wrap(x): return (x + PI) % TWO_PI - PI


def scalar_I_S(N, m2=0.01):
    """Corrected scalar matching coeff: NO /N_TASTE, + continuum offset 2."""
    K, dk = comps(N)
    Df = Dpsi(K) + m2
    Db = Dg(K) + m2
    lat = S16 * (Fg(K) / (Df * Db)).sum() * dk
    k2 = ksq(K) + m2
    cont = S16 * (4.0 / (k2 * k2)).sum() * dk
    del K, Df, Db, k2; gc.collect()
    return (lat - cont) / (U0 ** 2) + 2.0


def gluonic_I_SE(N, m2=0.01):
    """Clean C_A channel (unchanged)."""
    K, dk = comps(N)
    Db = Dg(K) + m2
    lat = S16 * (Fg(K) / (Db * Db)).sum() * dk
    k2 = ksq(K) + m2
    cont = S16 * (4.0 / (k2 * k2)).sum() * dk
    del K, Db, k2; gc.collect()
    return (lat - cont) / (U0 ** 2)


def fermion_full_const(N, m2):
    """Full 16-doubler-subtracted fermion (lat - full_cont), before taste/u0."""
    K, dk = comps(N)
    Df = Dpsi(K) + m2
    lat = S16 * (Fg(K) / (Df * Df)).sum() * dk
    ref = np.zeros_like(Df)
    for mask in range(16):
        c = [PI if (mask >> i) & 1 else 0.0 for i in range(4)]
        w = sum(1.0 for x in c if x == 0.0)
        ksh2 = sum(wrap(K[i] - c[i]) ** 2 for i in range(4))
        ref += w / ((ksh2 + m2) ** 2)
        del ksh2; gc.collect()
    cont = S16 * ref.sum() * dk
    del K, Df, ref; gc.collect()
    return lat - cont


def main():
    print("=" * 70)
    print("CORRECTED Delta_R (honest bound) -- memory-safe, single process")
    print("=" * 70)
    print(f"  u0={U0:.5f}  alpha_LM/4pi={ALPHA_LM_4PI:.5f}")

    # ---- Delta_1: corrected scalar ----
    I_S = scalar_I_S(48)
    d1 = 2.0 * I_S + GAMMA_S          # I_v_gauge = 0 (Ward)
    cf_ch = ALPHA_LM_4PI * C_F * d1
    print("\n[Delta_1 / C_F scalar channel]  (NON-PERTURBATIVE single-link bound)")
    print(f"  corrected I_S (no /N_TASTE) = {I_S:.3f}   "
          f"(buggy /16 value was 3.90)")
    print(f"  Delta_1 = 2*I_S - 6 = {d1:+.3f}   C_F*Delta_1 channel = {cf_ch*100:+.2f}%")

    # ---- Delta_2: clean gluonic ----
    I_SE_g = gluonic_I_SE(48)
    d2 = 0.0 - (5.0 / 3.0) * I_SE_g
    ca_ch = ALPHA_LM_4PI * C_A * d2
    print("\n[Delta_2 / C_A gluonic channel]  (CLEAN, unchanged)")
    print(f"  I_SE_gluonic = {I_SE_g:.3f}   Delta_2 = -(5/3)I_SE = {d2:+.3f}   "
          f"C_A*Delta_2 channel = {ca_ch*100:+.2f}%")

    # ---- Delta_3: full-doubler-subtracted + m^2->0 extrapolation ----
    print("\n[Delta_3 / T_F n_f fermion channel]  (was BROKEN; full-doubler fixed)")
    pts = [0.12, 0.06, 0.03]   # all resolved at N=48 (sqrt(m2) > spacing 0.131)
    vals = [(m2, fermion_full_const(48, m2)) for m2 in pts]
    for m2, v in vals:
        print(f"    m^2={m2:<6}: full-doubler const = {v:+.3f}")
    # extrapolate ~ C - a*sqrt(m2): linear fit of v vs sqrt(m2), intercept = C
    xs = np.array([math.sqrt(m2) for m2, _ in vals])
    ys = np.array([v for _, v in vals])
    A = np.vstack([xs, np.ones_like(xs)]).T
    a, C_f = np.linalg.lstsq(A, ys, rcond=None)[0]
    print(f"  m^2->0 extrapolation (linear in sqrt(m^2)): C_f ~ {C_f:.2f} "
          f"(slope a={a:.2f})")
    for div, name in [(N_TASTE, "/16"), (N_TASTE ** 2, "/256")]:
        I_SE_f = C_f / div / (U0 ** 2)
        d3 = (4.0 / 3.0) * I_SE_f
        tf_ch = ALPHA_LM_4PI * T_F * N_F * d3
        print(f"    taste power {name:<5}: I_SE_fermion={I_SE_f:+.3f}  "
              f"Delta_3={d3:+.3f}  T_F n_f channel={tf_ch*100:+.2f}%")

    # ---- assemble Delta_R as a bound (use /16 as the structural default) ----
    I_SE_f16 = C_f / N_TASTE / (U0 ** 2)
    d3_16 = (4.0 / 3.0) * I_SE_f16
    tf_ch16 = ALPHA_LM_4PI * T_F * N_F * d3_16
    I_SE_f256 = C_f / (N_TASTE ** 2) / (U0 ** 2)
    tf_ch256 = ALPHA_LM_4PI * T_F * N_F * (4.0 / 3.0) * I_SE_f256

    print("\n" + "=" * 70)
    print("CORRECTED Delta_R (bound):")
    for tname, tch in [("/16", tf_ch16), ("/256", tf_ch256)]:
        dR = cf_ch + ca_ch + tch
        print(f"  taste {tname:<5}:  C_F {cf_ch*100:+.2f}%  +  C_A {ca_ch*100:+.2f}%"
              f"  +  T_Fn_f {tch*100:+.2f}%   =  Delta_R = {dR*100:+.2f}%")
    print(f"\n  Runner's REPORTED Delta_R = {REPORTED_DELTA_R*100:+.2f}%")
    print("  => dominated by the scalar C_F channel (~+56%), which is the")
    print("     UNCONTROLLED non-perturbative single-link value. Delta_R is an")
    print("     O(50%) uncontrolled quantity, NOT the small -3.27% reported;")
    print("     the fermion channel is subdominant (taste power barely matters).")
    print("=" * 70)


if __name__ == "__main__":
    main()
