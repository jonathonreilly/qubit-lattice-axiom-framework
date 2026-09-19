#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a3 (author w-macbookpro90c72-j28fe, grok-4.6); referee
w-jonathonsmac4f50-jceaa (claude-opus-5). Independent machinery (exact rationals, sympy, mpmath), none of the author's code.

Model (the attempt's (1)): theta_{t+1} = P theta_t + h, (P f)(i, j) = (f(i, j) + f(i-1, j) + f(i, j-1))/3 on the level plane.

W1  steps 1-2: R = sum_t (phi z)^t = 1/(1 - phi z) and the E-identity E(k) = 3(|1 - phi(q)e^{iw}|^2 + 1 - |phi(q)|^2) at
    k = (q1 + w, q2 + w, w) (sympy, identically)
W2  step 3, exactly on Z^2: the static response to a persistent unit source at 0 is G(x) = (3/2) C(x1+x2, x1) 2^{-(x1+x2)}
    on the forward quadrant N^2 and 0 elsewhere (the stationary equation solved exactly and compared with the
    time-summed iteration); downstream G(n, n) = (3/2) C(2n, n)/4^n ~ (3/2)/sqrt(pi n) (the continuum's downstream law
    with the same constant); off the downstream axis the continuum form fails: 0 upstream and sideways, and
    (3/2) 2^{-n} along the edge against the continuum's e^{-(sqrt2 - 1) n}
W3  step 4(iii): the response to a point source (one site, one level) is the trinomial kernel
    T(x) = (x1+x2+x3)!/(x1! x2! x3!) 3^{-(x1+x2+x3)} in 3D coordinates (exact iteration); along the level axis
    T(n, n, n) R -> 3/(2 pi) with R = sqrt3 n the 3D distance: a 1/R law along that ray (exponential off it)
W4  step 4(iv): the eight-corner average R_8(k) = (1/8) sum_eps 1/(1 - phi_eps(k)) has a 1/k^2 singularity:
    kappa^2 R_8(kappa, -kappa, 0) -> 3/2 while kappa^2 / E -> 1/2 (sympy limits); along a coordinate axis it tends to
    3/2 as the attempt says
W5  step 5: the mode k = (pi/2, 0) of the L = 4 torus has phi = (2 + i)/3 (not (1 + i)/3), 1/(1 - phi) = 3(1 + i)/2,
    1/(1 - |phi|^2) = 9/4; fluctuation-response fails because phi is not real (the attempt's conclusion)
"""
from __future__ import annotations

import sys
from fractions import Fraction
from math import comb

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


def w1():
    q1, q2, w, z = sp.symbols("q1 q2 w z", real=True)
    phi = (1 + sp.exp(sp.I * q1) + sp.exp(sp.I * q2)) / 3
    k = (q1 + w, q2 + w, w)
    E = sum(2 * (1 - sp.cos(kj)) for kj in k)
    rhs = 3 * (sp.expand((1 - phi * sp.exp(sp.I * w)) * sp.conjugate(1 - phi * sp.exp(sp.I * w)), complex=True)
               + 1 - sp.expand(phi * sp.conjugate(phi), complex=True))
    ok_E = sp.simplify(sp.expand_trig(sp.expand(E - rhs, complex=True))) == 0
    s = sp.symbols("s")
    N = 12
    geo = sum((s * z) ** n for n in range(N))
    ok_R = sp.simplify(sp.series(1 / (1 - s * z), z, 0, N).removeO() - geo) == 0
    check("W1", ok_E and ok_R, "steps 1-2: sum_t (phi z)^t = 1/(1 - phi z) as power series, and E(k) = "
          "3(|1 - phi(q) e^{iw}|^2 + 1 - |phi(q)|^2) identically at k = (q1 + w, q2 + w, w)")


def w2():
    # exact stationary equation on N^2: G = P G + delta, G = 0 off N^2
    n_max = 14
    G = {}
    for s_ in range(0, 2 * n_max + 1):
        for x1 in range(0, s_ + 1):
            x2 = s_ - x1
            if x1 > n_max or x2 > n_max:
                continue
            a = G.get((x1 - 1, x2), Fraction(0))
            b = G.get((x1, x2 - 1), Fraction(0))
            # G(x) = (G(x) + a + b)/3 + delta  =>  G(x) = (a + b)/2 + (3/2) delta
            G[(x1, x2)] = (a + b) / 2 + (Fraction(3, 2) if (x1, x2) == (0, 0) else 0)
    closed = all(G[(a, b)] == Fraction(3, 2) * comb(a + b, a) / 2 ** (a + b) for (a, b) in G)
    # time-summed iteration m_{t+1} = P m_t + delta from m_0 = 0 (support stays in N^2); compare partial sums
    T = 60
    m = {}
    for t in range(T):
        new = {}
        keys = set(m) | {(0, 0)} | {(a + 1, b) for (a, b) in m} | {(a, b + 1) for (a, b) in m}
        for (a, b) in keys:
            if a > 6 or b > 6:
                continue
            val = (m.get((a, b), 0) + m.get((a - 1, b), 0) + m.get((a, b - 1), 0)) / Fraction(3)
            if (a, b) == (0, 0):
                val += 1
            new[(a, b)] = val
        m = new
    # the iteration increases to G; after 60 levels the gap at |x|_1 <= 4 is below 1e-6
    iter_ok = all(0 <= G[x] - m.get(x, 0) < Fraction(1, 10 ** 6) for x in G if sum(x) <= 4)
    # downstream constant and the edge rate
    ratios = [mp.mpf(3) / 2 * mp.binomial(2 * n, n) / mp.mpf(4) ** n * mp.sqrt(mp.pi * n) for n in (10, 100, 1000, 10000)]
    down_ok = abs(ratios[-1] - mp.mpf(3) / 2) < mp.mpf("1e-4") and all(ratios[i] < ratios[i + 1] for i in range(3))
    edge = [G[(n, 0)] == Fraction(3, 2) / 2 ** n for n in range(0, n_max + 1)]
    cont_rate = mp.sqrt(2) - 1          # continuum (3/pi) e^{n} K_0(sqrt2 n) ~ e^{-(sqrt2 - 1) n}/sqrt(n)
    cont_edge = [(3 / mp.pi) * mp.e ** n * mp.besselk(0, mp.sqrt(2) * n) for n in (10, 20)]
    edge_ok = all(edge) and abs(mp.log(cont_edge[0] / cont_edge[1]) / 10 - cont_rate) < 0.05 and abs(mp.log(2) - cont_rate) > 0.25
    check("W2", closed and iter_ok and down_ok and edge_ok,
          "step 3 exactly on Z^2: the static response to a persistent unit source is G(x) = (3/2) C(x1+x2, x1)/2^(x1+x2) "
          f"on N^2 and 0 off it (stationary equation solved exactly for x1, x2 <= {n_max}; the time-summed iteration "
          "increases to it); downstream G(n,n) sqrt(pi n) = " + ", ".join(mp.nstr(r, 8) for r in ratios)
          + " -> 3/2 (n = 10, 100, 1000, 10000), the continuum's downstream constant; but G = 0 upstream and sideways "
          "(the continuum's e^{x1+x2} K_0(sqrt2 r) is positive there), and along the edge G(n, 0) = (3/2) 2^{-n} (rate "
          f"log 2 = {mp.nstr(mp.log(2), 4)}) against the continuum's rate sqrt2 - 1 = {mp.nstr(cont_rate, 4)}")


def w3():
    # point source: m_0 = delta at the origin of level 0, m_{t+1} = P m_t; level t, plane (x1, x2), x3 = t - x1 - x2
    ok = True
    m = {(0, 0): Fraction(1)}
    for t in range(1, 13):
        new = {}
        for (a, b), v in m.items():
            for (da, db) in ((0, 0), (1, 0), (0, 1)):
                new[(a + da, b + db)] = new.get((a + da, b + db), 0) + v / 3
        m = new
        for (a, b), v in m.items():
            c = t - a - b
            ok = ok and v == Fraction(comb(t, a) * comb(t - a, b), 3 ** t) and c >= 0
    vals = []
    for n in (10, 100, 1000, 100000):
        logT = mp.loggamma(3 * n + 1) - 3 * mp.loggamma(n + 1) - 3 * n * mp.log(3)
        vals.append(mp.e ** logT * mp.sqrt(3) * n)
    target = 3 / (2 * mp.pi)
    ok = ok and abs(vals[-1] - target) < mp.mpf("1e-5") and abs(vals[1] - target) < mp.mpf("3e-3")
    # off the axis at a fixed direction the kernel decays exponentially: T(2n, n, 0)
    off = [mp.e ** (mp.loggamma(3 * n + 1) - mp.loggamma(2 * n + 1) - mp.loggamma(n + 1) - 3 * n * mp.log(3)) for n in (10, 20)]
    rate = mp.log(off[0] / off[1]) / 10
    ok = ok and rate > 0.3
    check("W3", ok,
          "step 4(iii): the response to a point source is exactly the trinomial kernel T(x) = (x1+x2+x3)!/(x1!x2!x3!) 3^{-|x|} "
          "(iteration to level 12 in rationals); along the level axis T(n,n,n) R with R = sqrt3 n the 3D distance equals "
          + ", ".join(mp.nstr(v, 7) for v in vals) + f" (n = 10, 100, 1000, 100000) -> 3/(2 pi) = {mp.nstr(target, 7)}: "
          "a 1/R law in three dimensions along that ray, not 1/r^2; off the axis (x = (2n, n, 0)) it decays "
          f"exponentially (rate {mp.nstr(rate, 4)} per n)")


def w4():
    kap = sp.symbols("kappa", positive=True)
    k = (kap, -kap, 0)
    tot = 0
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                phi = (sp.exp(-sp.I * e1 * k[0]) + sp.exp(-sp.I * e2 * k[1]) + sp.exp(-sp.I * e3 * k[2])) / 3
                tot += 1 / (1 - phi)
    R8 = tot / 8
    lim = sp.limit(sp.simplify(kap ** 2 * R8), kap, 0)
    E = sum(2 * (1 - sp.cos(kj)) for kj in k)
    limE = sp.limit(kap ** 2 / E, kap, 0)
    kx = (kap, 0, 0)
    tot = 0
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                phi = (sp.exp(-sp.I * e1 * kx[0]) + sp.exp(-sp.I * e2 * kx[1]) + sp.exp(-sp.I * e3 * kx[2])) / 3
                tot += 1 / (1 - phi)
    lim_axis = sp.limit(sp.simplify(tot / 8), kap, 0)
    ok = lim == sp.Rational(3, 2) and limE == sp.Rational(1, 2) and lim_axis == sp.Rational(3, 2)
    check("W4", ok,
          f"step 4(iv): along k = (kappa, -kappa, 0), kappa^2 R_8 -> {lim} and kappa^2/E -> {limE}, so R_8 ~ 3/E there: the "
          "eight-corner average has a 1/k^2 singularity on the planes orthogonal to (eps1, eps2, eps3) (the four orders "
          f"with eps1 = eps2 have no drift across this k); along the axis (kappa, 0, 0) it tends to {lim_axis} as the "
          "author says. 'No 1/k^2 pole' is false; in real space the average is (1/8) of the trinomial kernels of the "
          "eight octants, 1/R along the eight body diagonals (W3)")


def w5():
    phi = (1 + sp.I + 1) / 3          # k = (pi/2, 0): e^{i pi/2} = i, e^{0} = 1
    chi = sp.simplify(1 / (1 - phi))
    var = sp.simplify(1 / (1 - phi * sp.conjugate(phi)))
    ok = sp.simplify(chi - sp.Rational(3, 2) * (1 + sp.I)) == 0 and var == sp.Rational(9, 4) and sp.im(chi) != 0
    check("W5", ok,
          f"step 5: at k = (pi/2, 0) on L = 4, phi = (2 + i)/3, 1/(1 - phi) = {chi}, 1/(1 - |phi|^2) = {var}: the static "
          "susceptibility is not a real multiple of the variance (the attempt's conclusion holds; its example values "
          "phi = (1 + i)/3, '3/(2 - i) vs 9/8' are not this mode's, and 9/8 is not 1/(1 - |(1 + i)/3|^2) = 9/7)")


def main():
    try:
        w1()
        w2()
        w3()
        w4()
        w5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - the continuum kernel (3/pi) e^{x1+x2} K_0(sqrt2 r) is not the lattice static response "
          "off the downstream axis: the exact response is (3/2) C(x1+x2, x1)/2^(x1+x2) on the forward quadrant and 0 "
          "elsewhere (edge rate log 2, not sqrt2 - 1); downstream (3/2)/sqrt(pi n) holds. Step 4 then fails twice: (iii) "
          "the point-source response is the trinomial kernel, which decays like 3/(2 pi R) along the 3D level axis "
          "(not 1/r^2), and (iv) the eight-corner average has a 1/k^2 singularity (kappa^2 R_8 -> 3/2 along (1,-1,0)), so "
          "'no channel decays like 1/r' is false as stated: there is a directed 1/R (one ray, or the eight body "
          "diagonals) and no isotropic one. Steps 1, 2 and the conclusion of 5 hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
