#!/usr/bin/env python3
"""T2c: family C = free fixed-point ('perfect') action blocked from the continuum (Bietenholz-Wiese form).

Continuum massless scalar with constant metric G = diag(1, g); block variables Phi_n = average of phi over the LABEL
unit hypercube around n (a physical parallelepiped A[-1/2,1/2]^4); Gaussian blocking with parameter alpha.
Lattice propagator (BW):  S_G(q) = sum_l Pi(q+2 pi l) / ((q+2 pi l)^T G^-1 (q+2 pi l)) + s^2,  s^2 = 1/alpha,
  Pi(k) = prod_mu sinc^2(k_mu/2).   D_G = 1/S_G.   (Blocking a continuum rational kernel p^2/(1+c^2 p^2) gives the
  same form with s^2 -> 1/alpha + c^2, because sum_l Pi(q+2 pi l) = 1: so s^2 is the family's width parameter.)
The metric enters only through the continuum proper distance (the continuum propagator), identically on all axes.
RP: link-RP for every g (EXACT: blocks with n0 >= 1 depend only on phi at x0 >= 1/2; continuum OS positivity).
Site-RP / positive transfer (Lemma N class): needs s^2 >= 1/6 at zero spatial momentum (EXACT 1D formula
  S(q0, 0) = (2 + cos q0)/(12 sin^2(q0/2)) + s^2), checked over all spatial momenta in T2e.
Width (Lemma N): sigma_N^2 = 4 s^2 - 1/3.
Evaluation: Schwinger proper time; all 1D image sums in closed form (Poisson for small t, direct for large t).
Prediction (large s): kappa ~ -<S0''>/(2 s^2), <S0''> = d^2/deps^2 of the Coulomb (1/r^2) self-energy of the
  sheared unit cell (BZ average unfolds the image sum to an integral over R^4).
"""
import numpy as np
from scipy.special import erfc
from t2_core import midgrid, fit_power

SQ2 = np.sqrt(2.0)


def B_tables(q, t):
    """B_j(q,t) = sum_l k^j exp(-t k^2), k = q + 2 pi l, for j = -2..2; q: (L,), t: scalar. Returns dict."""
    out = {}
    if t < 0.05:
        nmax = int(np.ceil(np.sqrt(160 * t))) + 3
        n = np.arange(1, nmax + 1)[:, None]
        e = np.exp(-n ** 2 / (4 * t))
        c = np.cos(q[None, :] * n); s = np.sin(q[None, :] * n)
        pref = 1 / np.sqrt(4 * np.pi * t)
        out[0] = pref * (1 + 2 * (e * c).sum(0))
        out[1] = (1 / (2 * t)) * pref * 2 * (n * s * e).sum(0)
        out[2] = pref * (1 / (2 * t) + 2 * (c * e * (1 / (2 * t) - n ** 2 / (4 * t * t))).sum(0))
        ef = erfc(n / (2 * np.sqrt(t)))
        out[-1] = 0.5 / np.tan(q / 2) - (s * ef).sum(0)
        out[-2] = 1 / (4 * np.sin(q / 2) ** 2) - np.sqrt(t / np.pi) - 2 * (
            c * (np.sqrt(t) * e - np.sqrt(np.pi) * n / 2 * ef)).sum(0) / np.sqrt(np.pi)
    else:
        lmax = int(np.ceil(np.sqrt(45 / t) / (2 * np.pi))) + 2
        l = np.arange(-lmax, lmax + 1)[:, None]
        k = q[None, :] + 2 * np.pi * l
        e = np.exp(-t * k * k)
        for j in (-2, -1, 0, 1, 2):
            out[j] = (k ** j * e).sum(0)
    return out


def T_tables(q, t):
    B = B_tables(q, t)
    s2 = 4 * np.sin(q / 2) ** 2
    return [s2 * B[a - 2] for a in range(5)]  # T_a = sum_l sinc^2(k/2) k^a e^{-t k^2}


def perfect_arrays(L, smin=-18.0, smax=None, ds=0.04):
    q = midgrid(L)
    if smax is None:
        smax = np.log(45 * L * L / (4 * np.pi ** 2)) + 1.0
    sgrid = np.arange(smin, smax + ds / 2, ds)
    S0 = np.zeros((L,) * 4)
    d1 = {"E_g": np.zeros((L,) * 4), "T_2g": np.zeros((L,) * 4)}
    d2 = {"E_g": np.zeros((L,) * 4), "T_2g": np.zeros((L,) * 4)}
    for i, s in enumerate(sgrid):
        t = np.exp(s)
        w = ds * t * (0.5 if i in (0, len(sgrid) - 1) else 1.0)
        T = T_tables(q, t)
        A03 = np.multiply.outer(T[0], T[0])                     # (q0, q3)
        P00 = np.multiply.outer(T[0], T[0])                     # (q1, q2)
        P20 = np.multiply.outer(T[2], T[0]); P02 = P20.T
        P11 = np.multiply.outer(T[1], T[1])
        P22 = np.multiply.outer(T[2], T[2])
        P40 = np.multiply.outer(T[4], T[0]); P04 = P40.T
        def put(arr, plane, c):
            arr += c * A03[:, None, None, :] * plane[None, :, :, None]
        put(S0, P00, w)
        put(d1["E_g"], (P20 - P02) / SQ2, w * t)
        put(d1["T_2g"], SQ2 * P11, w * t)
        put(d2["E_g"], t * t * (P40 - 2 * P22 + P04) / 2 - t * (P20 + P02) / 2, w)
        put(d2["T_2g"], t * t * 2 * P22 - t * (P20 + P02) / 2, w)
    return S0, d1, d2


def kappa_perfect(S0, d1, d2, s2):
    S = S0 + s2
    return {ch: -0.5 * np.mean(d2[ch] / S - (d1[ch] / S) ** 2) for ch in d1}


if __name__ == "__main__":
    print("== T2c: Bietenholz-Wiese perfect action, S = S0_G + s^2 (s^2 = 1/alpha [+ c^2]); m = 0 ==")
    # sanity: 1D closed form at q_spatial -> 0 is exact for the T0 tables; check S0 against direct sum at one point
    for L in (24, 32, 48):
        S0, d1, d2 = perfect_arrays(L)
        q = midgrid(L)
        # direct check of S0 at one grid point via brute image sum
        i = (L // 2, L // 3, L // 4, 1)
        qq = np.array([q[j] for j in i])
        r = np.arange(-60, 61)
        acc = 0.0
        for l0 in r:
            k0 = qq[0] + 2 * np.pi * l0
            l = np.array(np.meshgrid(r[40:81] if False else np.arange(-12, 13), np.arange(-12, 13), np.arange(-12, 13), indexing="ij")).reshape(3, -1).T
            k = qq[1:] + 2 * np.pi * l
            Pi = np.sinc(k0 / (2 * np.pi)) ** 2 * np.prod(np.sinc(k / (2 * np.pi)) ** 2, axis=1)
            acc += (Pi / (k0 ** 2 + (k ** 2).sum(1))).sum()
        print(f"L={L}: S0 check at grid point {i}: Schwinger {S0[i]:.8f}  direct image sum (|l|<=12, l0<=60) {acc:.8f}")
        print(f"  <S0''>: E_g {np.mean(d2['E_g']):+.6f}   T_2g {np.mean(d2['T_2g']):+.6f}   (<S0'> E/T {np.mean(d1['E_g']):+.1e} {np.mean(d1['T_2g']):+.1e})")
        print("   s^2     sigma_N   kappa_E        kappa_T        pred_E=-<S''>/(2s^2)  pred_T")
        rows = []
        for s2 in (0.0, 1 / 12, 1 / 6, 0.25, 1 / 3, 0.5, 1.0, 2.0, 4.0, 9.0, 16.0, 25.0):
            k = kappa_perfect(S0, d1, d2, s2)
            sN = np.sqrt(max(4 * s2 - 1 / 3, 0))
            pe = -np.mean(d2["E_g"]) / (2 * s2) if s2 > 0 else np.nan
            pt = -np.mean(d2["T_2g"]) / (2 * s2) if s2 > 0 else np.nan
            print(f"  {s2:6.3f}  {sN:6.3f}   {k['E_g']:+.4e}  {k['T_2g']:+.4e}   {pe:+.4e}   {pt:+.4e}")
            rows.append((sN, k["E_g"], k["T_2g"]))
        rows = np.array(rows); sel = rows[:, 0] >= 3
        for j, name in ((1, "E_g"), (2, "T_2g")):
            p, c = fit_power(rows[sel, 0], rows[sel, j])
            print(f"  fit sigma_N >= 3, {name}: |kappa| ~ {c:.4f} sigma_N^-{p:.3f}")
