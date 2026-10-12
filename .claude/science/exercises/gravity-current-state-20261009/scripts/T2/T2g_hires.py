#!/usr/bin/env python3
"""T2g (high resolution): physical-cell perfect action, slice-by-slice (L up to 96), BLAS contractions.
kappa_raw  = -1/2 < S''/S - (S'/S)^2 >  on the grid;
kappa_corr = kappa_raw + <S''>_grid/(2 s^2)   (removes the grid error of the term whose exact value is 0, EXACT unfolding).
"""
import sys
import numpy as np
from t2_core import midgrid, fit_power
from T2g_physical_blocking import U_tables

SQ2 = np.sqrt(2.0)
S2LIST = np.array([1.0, 2.0, 4.0, 9.0, 16.0, 25.0, 36.0])


def run(L, smin=-18.0, ds=0.04):
    q = midgrid(L)
    smax = np.log(45 * L * L / (4 * np.pi ** 2)) + 1.0
    sg = np.arange(smin, smax + ds / 2, ds)
    w = ds * np.exp(sg); w[0] *= 0.5; w[-1] *= 0.5
    keys = [(j, a) for j in range(3) for a in range(3)]
    U = {key: np.zeros((len(sg), L)) for key in keys}
    for i, s in enumerate(sg):
        Ut = U_tables(q, np.exp(s))
        for key in keys:
            U[key][i] = Ut[key]

    def tri(c, A, B, C):
        Ap = (c[:, None] * A).T                     # (L, nt)
        M = (B[:, :, None] * C[:, None, :]).reshape(len(c), -1)
        return (Ap @ M).reshape(L, L, L)

    U00, U11, U10, U01, U22, U20, U02 = U[(0, 0)], U[(1, 1)], U[(1, 0)], U[(0, 1)], U[(2, 2)], U[(2, 0)], U[(0, 2)]
    acc = {ch: np.zeros(len(S2LIST)) for ch in ("E_g", "T_2g")}
    Spp = {ch: 0.0 for ch in acc}
    for i0 in range(L):
        c = w * U00[:, i0]
        S0 = tri(c, U00, U00, U00)
        d1E = (-tri(c, U11, U00, U00) + tri(c, U00, U11, U00)) / (2 * SQ2)
        d1T = -(tri(c, U10, U01, U00) + tri(c, U01, U10, U00)) / (2 * SQ2)
        common = tri(c, U11, U00, U00) + tri(c, U00, U11, U00)
        d2E = (tri(c, U22, U00, U00) - 2 * tri(c, U11, U11, U00) + tri(c, U00, U22, U00) + common) / 8
        d2T = (tri(c, U20, U02, U00) + 2 * tri(c, U11, U11, U00) + tri(c, U02, U20, U00) + common) / 8
        for ch, d1, d2 in (("E_g", d1E, d2E), ("T_2g", d1T, d2T)):
            Spp[ch] += d2.sum()
            for j, s2 in enumerate(S2LIST):
                S = S0 + s2
                acc[ch][j] += np.sum(d2 / S - (d1 / S) ** 2)
    N = L ** 4
    out = {}
    for ch in acc:
        kraw = -0.5 * acc[ch] / N
        mSpp = Spp[ch] / N
        out[ch] = (kraw, kraw + mSpp / (2 * S2LIST), mSpp)
    return out


if __name__ == "__main__":
    Ls = [int(x) for x in sys.argv[1:]] or [32, 64, 96]
    res = {}
    for L in Ls:
        res[L] = run(L)
        print(f"L={L}: <S''>_grid E/T = {res[L]['E_g'][2]:+.2e} {res[L]['T_2g'][2]:+.2e}", flush=True)
        print("   s^2   sigma_N   kE_raw       kE_corr      kT_raw       kT_corr      kE_corr*s^4  kT_corr*s^4", flush=True)
        for j, s2 in enumerate(S2LIST):
            sN = np.sqrt(4 * s2 - 1 / 3)
            e = res[L]["E_g"]; t = res[L]["T_2g"]
            print(f"  {s2:5.1f}  {sN:6.3f}  {e[0][j]:+.4e}  {e[1][j]:+.4e}  {t[0][j]:+.4e}  {t[1][j]:+.4e}  {e[1][j]*s2*s2:+.4e}  {t[1][j]*s2*s2:+.4e}", flush=True)
    L = Ls[-1]
    sN = np.sqrt(4 * S2LIST - 1 / 3)
    sel = (S2LIST >= 4) & (S2LIST <= 25)
    for ch in ("E_g", "T_2g"):
        p, c = fit_power(sN[sel], res[L][ch][1][sel])
        print(f" L={L} fit 4<=s^2<=25 ({ch}, corrected): |kappa| ~ {c:.4f} sigma_N^-{p:.3f}")
