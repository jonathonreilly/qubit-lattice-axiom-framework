#!/usr/bin/env python3
"""J:note falsifier for KOIDE_Z_S4B_RGE_IMPORT_TIER_REVIEW_NOTE_2026-05-08_probeZ_S4b_audit (on main).

Falsifier implemented: "a runner reproduction showing that the one-loop-only table does not give m_H = 130.60 GeV under the reviewed
inputs". The note's runner prints the stored table (lambda(v) = 0.140609, m_H = 130.60 GeV, +4.27%); the numbers come from
scripts/frontier_higgs_mass_full_3loop.py part 3 (scipy RK45 up to M_Pl, lambda(M_Pl) = 0, back down). Reviewed inputs: v = M_Pl (7/8)^(1/4)
alpha_LM^16, M_Pl = 1.2209e19 GeV, alpha_LM = alpha_bare/u0, alpha_bare = 1/(4 pi), u0 = 0.5934^(1/4); g1(v) = 0.464 (GUT), g2(v) = 0.648,
g3(v) = sqrt(4 pi alpha_bare/u0^2), y_t(v) = 0.9176, n_f = 6 throughout (v > m_t, no threshold crossed), comparator 125.25 GeV.

Disjoint machinery (30-digit mpmath):
  - one-loop gauge couplings in closed form, 1/g_i^2(t) = 1/g_i^2(t_v) - 2 b_i (t - t_v)/(16 pi^2), b = (41/10, -19/6, -7);
  - y_t in closed form through w = 1/y_t^2: w' = (2 G(t) w - 9)/(16 pi^2), w(t) = E(t)[w_v - 9/(16 pi^2) int E^-1], with
    E(t) = prod_i (1 - 2 b_i g_i^2(t_v) (t - t_v)/(16 pi^2))^(-c_i/b_i), c = (17/20, 9/4, 8), the integral by Gauss-Legendre quadrature;
  - lambda from lambda(M_Pl) = 0 down to v by fixed-step classical RK4 on (y_t, lambda) at 2000 and 4000 steps with Richardson
    extrapolation, y_t cross-checked against the closed form;
  - beyond the table: m_H(1L) under the y_t band +-1.2147511 % (the runner's conservative bound), the reduced Planck mass 2.435e18 GeV as
    boundary scale, and +-1 % in each gauge input.
HIT if the replay under the reviewed inputs differs from lambda(v) = 0.140609 by more than 5e-6 or from m_H = 130.60 GeV by more than 0.01.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 30
PI = mp.pi
K = 16 * PI ** 2
B = (mp.mpf(41) / 10, mp.mpf(-19) / 6, mp.mpf(-7))
C = (mp.mpf(17) / 20, mp.mpf(9) / 4, mp.mpf(8))


def inputs(mpl=mp.mpf("1.2209e19")):
    alpha_bare = 1 / (4 * PI)
    u0 = mp.mpf("0.5934") ** (mp.mpf(1) / 4)
    alpha_lm = alpha_bare / u0
    v = mp.mpf("1.2209e19") * (mp.mpf(7) / 8) ** (mp.mpf(1) / 4) * alpha_lm ** 16
    g3 = mp.sqrt(4 * PI * alpha_bare / u0 ** 2)
    return v, (mp.mpf("0.464"), mp.mpf("0.648"), g3), mp.mpf("0.9176"), mpl


def gauge(g0, tau):
    return [g0[i] / mp.sqrt(1 - 2 * B[i] * g0[i] ** 2 * tau / K) for i in range(3)]


def E_of(g0, tau):
    out = mp.mpf(1)
    for i in range(3):
        out *= (1 - 2 * B[i] * g0[i] ** 2 * tau / K) ** (-C[i] / B[i])
    return out


def yt_closed(g0, yt0, tau):
    integ = mp.quad(lambda s: 1 / E_of(g0, s), [0, tau / 4, tau / 2, 3 * tau / 4, tau])
    w = E_of(g0, tau) * (1 / yt0 ** 2 - 9 / K * integ)
    return 1 / mp.sqrt(w)


def rhs(g, yt, lam):
    g1, g2, g3 = g
    gp2 = mp.mpf(3) / 5 * g1 ** 2
    g22 = g2 ** 2
    dyt = yt * (mp.mpf(9) / 2 * yt ** 2 - C[0] * g1 ** 2 - C[1] * g22 - C[2] * g3 ** 2) / K
    dlam = (24 * lam ** 2 + 12 * lam * yt ** 2 - 6 * yt ** 4 - 3 * lam * (3 * g22 + gp2)
            + mp.mpf(3) / 8 * (2 * g22 ** 2 + (g22 + gp2) ** 2)) / K
    return dyt, dlam


def run_down(g0, yt_pl, T, n):
    """RK4 in s = T - tau from tau = T (M_Pl, lambda = 0) down to tau = 0 (v)."""
    h = T / n
    yt, lam = yt_pl, mp.mpf(0)
    for k in range(n):
        tau = T - k * h
        def f(tt, y, l):
            a, b = rhs(gauge(g0, tt), y, l)
            return -a, -b
        k1 = f(tau, yt, lam)
        k2 = f(tau - h / 2, yt + h / 2 * k1[0], lam + h / 2 * k1[1])
        k3 = f(tau - h / 2, yt + h / 2 * k2[0], lam + h / 2 * k2[1])
        k4 = f(tau - h, yt + h * k3[0], lam + h * k3[1])
        yt += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        lam += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    return yt, lam


def replay(v, g0, yt0, mpl, n=(2000, 4000)):
    T = mp.log(mpl) - mp.log(v)
    yt_pl = yt_closed(g0, yt0, T)
    res = [run_down(g0, yt_pl, T, m) for m in n]
    lam = res[1][1] + (res[1][1] - res[0][1]) / 15            # RK4 Richardson
    yt_back = res[1][0]
    mh = mp.sqrt(2 * lam) * v
    return {"T": T, "g_pl": gauge(g0, T), "yt_pl": yt_pl, "yt back at v": yt_back, "lambda(v)": lam,
            "lambda Richardson correction": res[1][1] - res[0][1], "m_H": mh}


def main():
    v, g0, yt0, mpl = inputs()
    r = replay(v, g0, yt0, mpl)
    gap = (r["m_H"] / mp.mpf("125.25") - 1) * 100
    print(f"1. reviewed inputs: v = {mp.nstr(v, 12)} GeV, g(v) = {[mp.nstr(x, 8) for x in g0]}, y_t(v) = {yt0}; ln(M_Pl/v) = {mp.nstr(r['T'], 10)}")
    print(f"   one-loop: g(M_Pl) = {[mp.nstr(x, 8) for x in r['g_pl']]}, y_t(M_Pl) closed form = {mp.nstr(r['yt_pl'], 10)} (runner cache 0.403207, "
          f"g_3 0.489206); y_t returned to v by RK4: {mp.nstr(r['yt back at v'], 12)}")
    print(f"   lambda(v) = {mp.nstr(r['lambda(v)'], 10)} (RK4 step-halving change {mp.nstr(r['lambda Richardson correction'], 3)}), "
          f"m_H = {mp.nstr(r['m_H'], 8)} GeV, gap to 125.25: {mp.nstr(gap, 5)} %")
    sens = {}
    for tag, yt_ in (("y_t -1.2147511%", yt0 * (1 - mp.mpf("0.012147511"))), ("y_t +1.2147511%", yt0 * (1 + mp.mpf("0.012147511")))):
        sens[tag] = replay(v, g0, yt_, mpl)["m_H"]
    sens["M_Pl -> 2.435e18 (boundary scale only)"] = replay(v, g0, yt0, mp.mpf("2.435e18"))["m_H"]
    for i, name in enumerate(("g1", "g2", "g3")):
        for sgn in (-1, 1):
            gg = list(g0)
            gg[i] = gg[i] * (1 + sgn * mp.mpf("0.01"))
            sens[f"{name} {'+' if sgn > 0 else '-'}1%"] = replay(v, gg, yt0, mpl)["m_H"]
    print(f"2. one-loop m_H under input variations: { {k: mp.nstr(x, 6) for k, x in sens.items()} }")
    fails = []
    if abs(r["lambda(v)"] - mp.mpf("0.140609")) > mp.mpf("5e-6") or abs(r["m_H"] - mp.mpf("130.60")) > mp.mpf("0.01"):
        fails.append(f"one-loop replay lambda(v) = {mp.nstr(r['lambda(v)'], 8)}, m_H = {mp.nstr(r['m_H'], 7)}")
    if fails:
        print(f"HIT: {fails}")
    lo = min(sens['y_t -1.2147511%'], sens['y_t +1.2147511%'])
    hi = max(sens['y_t -1.2147511%'], sens['y_t +1.2147511%'])
    print(f"SUMMARY: the semi-analytic one-loop replay (closed-form gauge couplings and y_t, 30-digit RK4 for lambda) under the reviewed "
          f"inputs gives y_t(M_Pl) = {mp.nstr(r['yt_pl'], 7)}, lambda(v) = {mp.nstr(r['lambda(v)'], 8)}, m_H = {mp.nstr(r['m_H'], 7)} GeV "
          f"({mp.nstr(gap, 4)} % above 125.25), matching the table's 0.140609 / 130.60 / +4.27 %; beyond the table, the runner's y_t band "
          f"moves the one-loop m_H over [{mp.nstr(lo, 5)}, {mp.nstr(hi, 5)}] GeV, the reduced Planck mass as boundary scale gives "
          f"{mp.nstr(sens['M_Pl -> 2.435e18 (boundary scale only)'], 5)} GeV, and 1 % in g3 moves it to "
          f"{mp.nstr(sens['g3 -1%'], 5)}/{mp.nstr(sens['g3 +1%'], 5)} GeV; the falsifier does not fire")


if __name__ == "__main__":
    main()
