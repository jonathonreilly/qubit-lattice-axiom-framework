#!/usr/bin/env python3
"""Referee of J:derive:two-source-interaction:a1 (author w-macbookpro90c72-jf686, grok-4.6); referee w-jonathonsmac4f50-j714a
(claude-opus-5). Independent code (exact rationals; Fourier sums on the L = 4 torus with cosines in {1, 0, -1}); nothing from the
author's check.py. Disclosure: this referee's model family refereed attempts a2 and a5 of this problem (grok), which share these values.

Linear light-cone law theta_{t+1} = P theta_t + xi, P the symmetric 7-point average, phi = 1 - E/7, sigma^2 = 1; chi = 7/E, C = 1/(1 - phi^2).

U1  (a) chi = 7/E, C = 7/(2E(1 - E/14)), chi/C = 1 + phi on all 63 nonzero modes of L = 4 (exact)
U2  (a)'s 'the law is not reversible w.r.t. the Gaussian pi' is false: P is symmetric, so the lag-one covariance P C (Fourier symbol phi C,
    real) is symmetric and the stationary Gaussian chain is reversible; checked as a real-space matrix identity on L = 4
U3  (c) G(0) = 18179/15360, G(e1) = 539/15360, G(0) - G(e1) = 147/128, unlike-pin energy a^2/(G(0) - G(e1)) = 128 a^2/147
U4  step 4 does not follow: with the zero mode kept through a mass m (C_m = 1/(1 - (1-m)^2 phi^2) on every mode), G(0) - G(e1) -> 147/128
    (the zero mode cancels) while G(0) + G(e1) grows like 1/m, so the like-pin energy a^2/(G(0) + G(e1)) tends to 0 - it vanishes, it does
    not diverge; on the mean-zero torus it is finite, 7680 a^2/9359
U5  (d)'s superposition of pinned means fails for unlike pins too: at the pinned site the summed one-pin means give a(1 - G(e1)/G(0)) =
    (360/371) a, not a
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


L = 4
COS = [1, 0, -1, 0]            # cos(pi m/2)
MODES = list(itertools.product(range(L), repeat=3))


def E(m):
    return sum(2 * (1 - COS[j]) for j in m)


def G(x, Ck, include_zero=False):
    tot = F(0)
    for m in MODES:
        if m == (0, 0, 0) and not include_zero:
            continue
        tot += Ck(m) * COS[sum(a * b for a, b in zip(m, x)) % 4]
    return tot / L ** 3


def main():
    ok = True
    for m in MODES:
        if m == (0, 0, 0):
            continue
        e = E(m)
        phi = 1 - F(e, 7)
        chi, C = 1 / (1 - phi), 1 / (1 - phi * phi)
        ok &= chi == F(7, e) and C == F(7, 2 * e) / (1 - F(e, 14)) and chi / C == 1 + phi
    check("U1", ok, "chi = 7/E, C = 7/(2E(1 - E/14)), chi/C = 1 + phi on the 63 nonzero modes")

    # real-space P and C on mean-zero functions; check P C symmetric
    sites = MODES
    idx = {x: i for i, x in enumerate(sites)}
    Cfun = lambda m: 1 / (1 - (1 - F(E(m), 7)) ** 2)
    Cx = {x: G(x, Cfun) for x in sites}
    nb = lambda x: [x] + [tuple((x[t] + (s if t == j else 0)) % L for t in range(3)) for j in range(3) for s in (1, -1)]
    PC = {}
    for x in sites:
        for y in sites:
            PC[(x, y)] = sum(Cx[tuple((z[t] - y[t]) % L for t in range(3))] for z in nb(x)) / 7
    sym = all(PC[(x, y)] == PC[(y, x)] for x in sites for y in sites)
    check("U2", sym, "the lag-one covariance P C is a symmetric matrix on L = 4 (mean-zero stationary law): the Gaussian chain is reversible")

    G0, G1 = Cx[(0, 0, 0)], Cx[(1, 0, 0)]
    check("U3", G0 == F(18179, 15360) and G1 == F(539, 15360) and G0 - G1 == F(147, 128) and 1 / (G0 - G1) == F(128, 147),
          f"G(0) = {G0}, G(e1) = {G1}, G(0) - G(e1) = {G0 - G1}, unlike energy {1 / (G0 - G1)} a^2")

    rows, ok, prev_like = [], True, None
    for mm in (F(1, 10), F(1, 100), F(1, 1000), F(1, 10000)):
        Cm = lambda m, mm=mm: 1 / (1 - (1 - mm) ** 2 * (1 - F(E(m), 7)) ** 2)
        g0, g1 = G((0, 0, 0), Cm, True), G((1, 0, 0), Cm, True)
        like, unlike = 1 / (g0 + g1), 1 / (g0 - g1)
        rows.append(f"m = {mm}: like {float(like):.6f} a^2, unlike {float(unlike):.6f} a^2")
        if prev_like is not None:
            ok &= like < prev_like
        prev_like = like
    ok &= like < F(1, 100) and abs(float(unlike) - 128 / 147) < 1e-3 and 1 / (G0 + G1) == F(7680, 9359)
    check("U4", ok, "; ".join(rows) + f" -> like-pin energy tends to 0 as m -> 0 (unlike -> 128/147 = {128 / 147:.6f}); mean-zero torus: like "
          f"{1 / (G0 + G1)} a^2")

    two_pin_at0 = F(1)
    sup = 1 - G1 / G0
    check("U5", sup != two_pin_at0 and sup == F(17640, 18179), f"unlike pins +a at 0, -a at e1: summed one-pin means at 0 = {sup} a, not a")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 4 - chi = 7/E, C, chi/C = 1 + phi and the unlike-pin energy 128 a^2/147 (G(0) = 18179/15360, G(e1) = "
          "539/15360) hold, but 'like pins are IR-divergent on the massless torus' is backwards: keeping the zero mode through a mass, the "
          "like-pin energy a^2/(G(0)+G(e1)) tends to 0 while the unlike one tends to 128/147 (mean-zero torus: 7680 a^2/9359, finite). Also "
          "false: (a) 'not reversible w.r.t. the Gaussian pi' (P C is symmetric; the chain is reversible and chi != C is a conjugate-"
          "observable effect) and (d) 'superposition of means holds' for pins (the summed one-pin means give 360 a/371 at the pin)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
