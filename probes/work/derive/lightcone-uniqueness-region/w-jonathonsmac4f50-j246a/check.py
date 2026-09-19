#!/usr/bin/env python3
"""lightcone-uniqueness-region, attempt 2 of 3 (worker w-jonathonsmac4f50-j246a, claude-opus-5).

Object (probes/lib/formation_levelplane.py, dim 3s, menu sphere): the record at (t+1, x) is drawn from mu_{beta S_x}, where
mu_V = vMF(V) has density exp(V.s)/Z(|V|) on S^2 and S_x is the sum of the 7 records at (t, x) and (t, x +- e_j), j = 1..3.
A(k) = coth k - 1/k.  Metric on S^2: the chordal distance |s - s'|.  'Lip' = 1-Lipschitz for it.
The W1 influence of the kernel at V in direction u: ||D_u(V)|| := sup_{f Lip} Cov_V(f, u.s) (the derivative of V -> E_V f).

E1  finite mirror identity: |V| = |V'| = k > 0  =>  sup_{f Lip} (E_V f - E_V' f) = (A(k)/k)|V - V'| (upper bound by the mirror
    across the bisector plane, attained by f = w.s); hence ||D_u(V)|| = A(k)/k for u perpendicular to V, and = 1/3 at V = 0.
E2  A(k)/k is strictly decreasing, < 1/3 for k > 0 (exact series sign).
E3  parallel direction: ||D_{V/k}(V)|| <= R(k) := A'(k) + I(k), I(k) = int_0^1 (1/sqrt(1-z^2) - 1) Delta(z) dz,
    Delta(z) = (coth k sinh kz - z cosh kz)/sinh k >= 0 (relaxed dual); I sinh^2 k = sum_j d_j k^{2j+1}, d_j >= 0 exact.
E4  rational interval sweep: sqrt(R(k)^2 + (A(k)/k)^2) < 10/21 for every k in [0, 21/10]  =>  the W1 Dobrushin coefficient
    c = 7 beta L(beta) < 1 for every beta <= 3/10 (unconditional).
E5  ceilings: any TV-Dobrushin coefficient >= 7 tanh(beta/2) (fails for beta >= ln(4/3) = 0.2877, and 3/10 > ln(4/3));
    block 27's TV sensitivity gives beta < sqrt3/7 = 0.2474; any sitewise W1 coefficient >= 7 beta/3 (so <= 3/7).
N1  (numerical, labelled) LP values of ||D_u(V)|| on grids: parallel (1D) and general directions (2D Fibonacci grid).
N2  (numerical, labelled) executed light-cone sphere runs parsed from logs/probes/X:*: late-level projection on e0.
"""
import glob
import os
import re
import sys
from fractions import Fraction as Fr
from math import factorial

import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def zero(e):
    return sp.simplify(sp.expand(sp.sympify(e).rewrite(sp.exp))) == 0


def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


def main():
    k, z, t = sp.symbols("kappa z t", positive=True)
    q = lambda x: k * sp.exp(k * x) / (2 * sp.sinh(k))       # density of the height z = s.V/|V| under mu_V
    A = sp.coth(k) - 1 / k
    Ap = sp.diff(A, k)

    # ---------------- E1
    Ez = sp.integrate(z * q(z), (z, -1, 1))
    Ez2 = sp.integrate(z ** 2 * q(z), (z, -1, 1))
    ok = zero(Ez - A) and zero((1 - Ez2) / 2 - A / k) and zero(Ez2 - Ez ** 2 - Ap)
    v = sp.symbols("v1:4", real=True)
    vp = sp.symbols("w1:4", real=True)
    dot = lambda a, b: sum(ai * bi for ai, bi in zip(a, b))
    d = [v[i] - vp[i] for i in range(3)]
    # V.(V - V') - |V - V'|^2/2 = (|V|^2 - |V'|^2)/2, so with |V| = |V'| the reflection rho_w, w = (V - V')/|V - V'|, maps V to V'
    ok &= sp.expand(dot(v, d) - dot(d, d) / 2 - (dot(v, v) - dot(vp, vp)) / 2) == 0
    check("E1", ok, "E_V[s] = A(k) V/k and E_V[s_perp^2] = A(k)/k, Var_V(s.V/k) = A'(k) (symbolic); V.(V - V') - |V - V'|^2/2 = (|V|^2 - |V'|^2)/2, so for "
          "|V| = |V'| = k the reflection rho_w across w-perp, w = (V - V')/|V - V'|, swaps V and V' and maps {w.s > 0} onto {w.s < 0}, where mu_V - mu_V' "
          "is positive exactly on {w.s > 0} (density ratio exp((V - V').s), same normaliser); for Lip f: E_V f - E_V' f = int_{w.s>0} (f(s) - f(rho_w s)) "
          "(p_V - p_V')(s) ds <= int_{w.s>0} 2 (w.s)(p_V - p_V') = E_V[w.s] - E_V'[w.s] = A(k)(V - V').w/k = (A(k)/k)|V - V'|, with equality for f = w.s: "
          "the finite mirror identity; as V' -> V along u perpendicular to V: ||D_u(V)|| = A(k)/k; at V = 0 (uniform law) every direction gives "
          "E_0[(u.s)^2] = 1/3 by the same mirror across u-perp")

    # ---------------- E2
    x, m = sp.symbols("x m", positive=True, integer=True)
    g = sp.cosh(x) - 1 - x ** 2 / 4 - x * sp.sinh(x) / 4
    ser = sp.series(g, x, 0, 16).removeO()
    coef_ok = all(sp.nsimplify(ser.coeff(x, 2 * mm) - sp.Rational(2 - mm, 2 * factorial(2 * mm))) == 0 for mm in range(2, 8))
    gen_ok = sp.simplify(1 / sp.factorial(2 * m) - 1 / (4 * sp.factorial(2 * m - 1)) - (2 - m) / (2 * sp.factorial(2 * m))) == 0
    kk = sp.symbols("kk", positive=True)
    Akk = sp.coth(kk) - 1 / kk
    ident = zero(kk * sp.diff(Akk, kk) - Akk - g.subs(x, 2 * kk) / (kk * sp.sinh(kk) ** 2))
    lim = sp.series(Akk / kk, kk, 0, 3).removeO().subs(kk, 0) == sp.Rational(1, 3)     # constant term of the Laurent-free series
    check("E2", coef_ok and gen_ok and ident and lim,
          "k A'(k) - A(k) = g(2k)/(k sinh^2 k), g(x) = cosh x - 1 - x^2/4 - (x/4) sinh x = sum_{m>=3} (2 - m) x^{2m}/(2 (2m)!) < 0 for x > 0 "
          "(coefficient 1/(2m)! - 1/(4 (2m-1)!) = (2 - m)/(2 (2m)!) symbolic in m, series to x^15), so (A/k)' = (k A' - A)/k^2 < 0: A(k)/k strictly "
          "decreasing from its limit 1/3; the perpendicular constant A(k)/k < 1/3 for k > 0")

    # ---------------- E3
    Wz = sp.integrate((t - A) * q(t), (t, -1, z))
    ok = zero(Wz.subs(z, 1)) and zero(sp.integrate(Wz, (z, -1, 1)) + Ap)
    Delta = (sp.coth(k) * sp.sinh(k * z) - z * sp.cosh(k * z)) / sp.sinh(k)
    ok &= zero(-Wz + Wz.subs(z, -z) - Delta)
    ok &= zero(sp.diff(-Wz.subs(z, -z), z) + (z + A) * q(-z))
    cb = [sp.integrate((1 / sp.sqrt(1 - z ** 2) - 1) * z ** (2 * b + 1), (z, 0, 1)) for b in range(7)]
    ok &= all(sp.nsimplify(cb[b] - (sp.Rational(dfact(2 * b), dfact(2 * b + 1)) - sp.Rational(1, 2 * b + 2))) == 0 for b in range(7))
    num = sp.cosh(k) * sp.sinh(k * z) - z * sp.sinh(k) * sp.cosh(k * z)
    sk = sp.expand(sp.series(num, k, 0, 16).removeO())
    dbl = sum(sp.Rational(2 * (a - b), factorial(2 * a + 1) * factorial(2 * b + 1)) * k ** (2 * (a + b) + 1) * z ** (2 * b + 1)
              for a in range(8) for b in range(8) if 2 * (a + b) + 1 < 16)
    ok &= sp.expand(sk - dbl) == 0
    c = [Fr(dfact(2 * b), dfact(2 * b + 1)) - Fr(1, 2 * b + 2) for b in range(40)]
    J = 30
    dj = [sum(Fr(2 * (j - 2 * b), factorial(2 * (j - b) + 1) * factorial(2 * b + 1)) * c[b] for b in range(j + 1)) for j in range(J + 1)]
    ok &= dj[0] == 0 and dj[1] == Fr(1, 36) and dj[2] == Fr(1, 225) and all(dj[j] > 0 for j in range(1, J + 1))
    check("E3", ok, "for V = k e3 and Lip f, averaging f over rotations about e3 gives F(z) with |F(z) - F(z')| <= the same-azimuth chord; "
          "Cov_V(f, z) = int F w = int F'|W|, W(z) = int_{-1}^z (t - A) q(t) dt <= 0, W(+-1) = 0, int |W| = A'(k) (symbolic); keeping only |F'| <= "
          "1/sqrt(1-z^2) and the vertical chords F(z) - F(-z) <= 2z gives Cov_V(f, z) <= A'(k) + I(k) with |W(z)| - |W(-z)| = Delta(z) = "
          "(coth k sinh kz - z cosh kz)/sinh k (symbolic; >= 0 by concavity of tanh), |W(-z)| non-increasing on [0,1] (d/dz = -(z + A) q(-z)); "
          "c_b = int_0^1 (1/sqrt(1-z^2) - 1) z^{2b+1} = (2b)!!/(2b+1)!! - 1/(2b+2) (b <= 6 symbolic, Wallis recursion), "
          "cosh k sinh kz - z sinh k cosh kz = sum_{a,b} 2(a - b) k^{2(a+b)+1} z^{2b+1}/((2a+1)!(2b+1)!) (series to k^15), so I(k) sinh^2 k = "
          "sum_j d_j k^{2j+1} with d_1 = 1/36, d_2 = 1/225, all d_j > 0 for 1 <= j <= 30 (exact); |d_j| <= 2j 2^{2j+1}/(2j+2)! for the tail")

    # ---------------- E4: exact rational sweep over k in [0, 21/10]
    KT = 26

    def sinh_lo(a):                      # partial sum of positive terms: a lower bound
        s = Fr(0)
        for i in range(KT):
            s += a ** (2 * i + 1) / factorial(2 * i + 1)
        return s

    def P1_up(b):                        # A/k = (k/sinh k) P1(k), P1 = sum_{i>=1} 2i k^{2i-2}/(2i+1)!
        s = sum(Fr(2 * i, factorial(2 * i + 1)) * b ** (2 * i - 2) for i in range(1, KT + 1))
        T = b ** (2 * KT) / factorial(2 * KT + 2)
        r = b * b / ((2 * KT + 3) * (2 * KT + 4))
        return s + T / (1 - r)

    def P2_up(b):                        # A' = (k/sinh k)^2 P2(k), P2 = sum_{i>=2} 2^{2i-1} k^{2i-4}/(2i)!
        s = sum(Fr(2 ** (2 * i - 1), factorial(2 * i)) * b ** (2 * i - 4) for i in range(2, KT + 1))
        T = Fr(2 ** (2 * KT + 1), factorial(2 * KT + 2)) * b ** (2 * KT - 2)
        r = 4 * b * b / ((2 * KT + 3) * (2 * KT + 4))
        return s + T / (1 - r)

    def Q_up(b):                         # I = k (k/sinh k)^2 Q(k), Q = sum_{j>=1} d_j k^{2j-2}
        s = sum(dj[j] * b ** (2 * j - 2) for j in range(1, J + 1))
        e = Fr(2 * (J + 1) * 2 ** (2 * J + 3), factorial(2 * J + 4)) * b ** (2 * J)
        r = 8 * b * b / ((2 * J + 5) * (2 * J + 6))
        return s + e / (1 - r)

    target = Fr(100, 441)
    stack = [(Fr(0), Fr(21, 10))]
    nint, worst, worst_at = 0, Fr(0), None
    while stack:
        a, b = stack.pop()
        f = Fr(1) if a == 0 else a / sinh_lo(a)
        R = f * f * P2_up(b) + b * f * f * Q_up(b)
        Ak = f * P1_up(b)
        val = R * R + Ak * Ak
        if val < target:
            nint += 1
            if val > worst:
                worst, worst_at = val, (a, b)
        elif b - a < Fr(1, 10 ** 5):
            nint = -1
            break
        else:
            mid = (a + b) / 2
            stack += [(a, mid), (mid, b)]
    import math
    Lup = math.sqrt(worst.numerator / worst.denominator) if nint > 0 else float("nan")
    check("E4", nint > 0, f"exact rational bounds on {nint} subintervals of [0, 21/10] (k/sinh k <= a/sinh_lo(a), P1, P2, Q increasing with "
          f"explicit geometric tails): sup sqrt(R^2 + (A/k)^2) <= {Lup:.5f} < 10/21 = {10/21:.5f} (largest bound on [{float(worst_at[0]):.4f}, "
          f"{float(worst_at[1]):.4f}]); so for |V| <= 21/10 and every direction u = cos(al) V/k + sin(al) u_perp: ||D_u(V)|| <= |cos al| R + |sin al| A/k "
          f"< 10/21, and the W1 Dobrushin coefficient 7 beta L(beta) < 7 (3/10)(10/21) = 1 for every beta <= 3/10")

    # ---------------- E5: ceilings and the TV side
    b_ = sp.symbols("beta", positive=True)
    qb = lambda x: b_ * sp.exp(b_ * x) / (2 * sp.sinh(b_))
    tv = sp.integrate(qb(z) - qb(-z), (z, 0, 1))
    ok = zero(tv - sp.tanh(b_ / 2))
    ok &= sp.simplify(sp.exp((2 * sp.atanh(sp.Rational(1, 7))).rewrite(sp.log)) - sp.Rational(4, 3)) == 0     # 2 artanh(1/7) = ln(4/3)
    e03_lo = sum(Fr(3, 10) ** i / factorial(i) for i in range(8))
    ok &= e03_lo > Fr(4, 3)                                  # e^{3/10} > 4/3, i.e. ln(4/3) < 3/10
    ln43_lo = sum(Fr(1, (2 * i + 1) * 7 ** (2 * i + 1)) for i in range(6)) * 2   # 2 artanh(1/7) > partial sum
    ok &= Fr(3, 49) < ln43_lo ** 2                           # sqrt3/7 < ln(4/3)
    s3 = sp.sqrt(3)
    sig = sp.Matrix([0, 0, 1])
    tri = [sp.Matrix([1, 0, 0]), sp.Matrix([-sp.Rational(1, 2), s3 / 2, 0]), sp.Matrix([-sp.Rational(1, 2), -s3 / 2, 0])]
    R_minus = [-sig, sig, -sig] + tri                          # six unit vectors summing to -sigma
    ok &= all(sp.simplify(u.dot(u)) == 1 for u in R_minus) and sp.simplify(sum(R_minus, sp.zeros(3, 1)) + sig) == sp.zeros(3, 1)
    R_zero = [sig, -sig, tri[0], -tri[0], sp.Matrix([0, 1, 0]), sp.Matrix([0, -1, 0])]
    ok &= sp.simplify(sum(R_zero, sp.zeros(3, 1))) == sp.zeros(3, 1)
    check("E5", ok, "TV(mu_{beta e}, mu_{-beta e}) = tanh(beta/2) (symbolic); with the other six predecessors summing to 0 (explicit) a flip of one "
          "predecessor to its antipode costs TV tanh(beta/2), so every TV-Dobrushin coefficient is >= 7 tanh(beta/2) and fails for beta >= "
          "2 artanh(1/7) = ln(4/3) (symbolic) < 3/10 (e^{3/10} > 4/3 exact); block 27's sensitivity |V - V'|/(2 sqrt3) gives 7 beta/sqrt3 < 1, "
          "beta < sqrt3/7 < ln(4/3) (exact); with the other six summing to -sigma (explicit) the kernel sits at V = 0 and a small turn of "
          "sigma has W1 cost beta/3 per unit, so every sitewise W1 coefficient is >= 7 beta/3: the W1 route cannot pass 3/7, and reaches 3/7 "
          "exactly if ||D_u(V)|| <= 1/3 for all |V| <= 3 (the directional lemma, ASSUMED; E1 proves it for u perpendicular to V)")

    # ---------------- N1 (numerical, labelled): LP values of the W1 influence
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix

    def Af(x):
        return 1 / np.tanh(x) - 1 / x

    def Apf(x):
        return 1 / x ** 2 - 1 / np.sinh(x) ** 2

    def transport(P, w):
        src = np.where(w > 0)[0]
        snk = np.where(w < 0)[0]
        ns, nk = len(src), len(snk)
        Dm = np.sqrt(((P[src][:, None, :] - P[snk][None, :, :]) ** 2).sum(-1))
        rows = np.concatenate([np.repeat(np.arange(ns), nk), ns + np.tile(np.arange(nk), ns)])
        cols = np.concatenate([np.arange(ns * nk), np.arange(ns * nk)])
        Aeq = coo_matrix((np.ones(2 * ns * nk), (rows, cols)), shape=(ns + nk, ns * nk)).tocsr()
        res = linprog(Dm.ravel(), A_eq=Aeq, b_eq=np.concatenate([w[src], -w[snk]]), bounds=(0, None), method="highs")
        return res.fun

    def lp_par(kap, N=240):
        a = (np.arange(N) + 0.5) / N * np.pi - np.pi / 2
        zz, rr = np.sin(a), np.cos(a)
        w = (zz - Af(kap)) * kap * np.exp(kap * zz) / (2 * np.sinh(kap)) * np.cos(a) * np.pi / N
        w -= w.mean()
        return transport(np.stack([rr, zz], 1), w)

    def I_num(kap):
        from scipy.integrate import quad
        Dl = lambda u: (np.sinh(kap * u) / np.tanh(kap) - u * np.cosh(kap * u)) / np.sinh(kap)
        return quad(lambda u: (1 / np.sqrt(1 - u * u) - 1) * Dl(u), 0, 1, limit=400)[0]

    rows, okn = [], True
    for kap in (0.25, 1.0, 2.0):
        lpv = lp_par(kap)
        Rk = Apf(kap) + I_num(kap)
        rows.append(f"k={kap}: parallel LP {lpv:.4f}, relaxed bound R(k) {Rk:.4f}, A/k {Af(kap)/kap:.4f}, A' {Apf(kap):.4f}")
        okn &= lpv <= Rk + 2e-3
    Nf = 500
    i = np.arange(Nf) + 0.5
    zf = 1 - 2 * i / Nf
    ph = np.pi * (1 + 5 ** 0.5) * i
    Sf = np.stack([np.sqrt(1 - zf * zf) * np.cos(ph), np.sqrt(1 - zf * zf) * np.sin(ph), zf], 1)
    for kap in (1.0, 2.0):
        p = np.exp(kap * Sf[:, 2])
        p /= p.sum()
        vals = []
        for al in (0, 45, 90):
            u = np.array([np.sin(np.radians(al)), 0, np.cos(np.radians(al))])
            xx = Sf @ u
            vals.append(transport(Sf, p * (xx - (p * xx).sum())))
        rows.append(f"k={kap}: sphere-grid LP (N=500) at 0/45/90 degrees from V: " + "/".join(f"{v_:.4f}" for v_ in vals) + f", A/k = {Af(kap)/kap:.4f}")
        okn &= max(vals) <= Af(kap) / kap + 5e-3 and vals[0] < vals[1] < vals[2]
    check("N1", okn, "(numerical, labelled; linear programs on grids, not a proof) " + "; ".join(rows) + "; the largest influence is the perpendicular one, "
          "consistent with the directional lemma ||D_u(V)|| <= A(|V|)/|V|")

    # ---------------- N2 (numerical, labelled): executed runs
    here = os.getcwd()
    runs = []
    for f in sorted(glob.glob(os.path.join(here, "logs/probes/X:*/*.txt"))):
        txt = open(f).read()
        hm = re.search(r"menu=sphere beta=([\d.]+) L=(\d+) T=(\d+) T0=\d+ seed=\d+; predecessors n=7", txt)
        if not hm:
            continue
        tab = re.findall(r"^\s+(\d+)\s+([\d.]+)\s+([+-][\d.]+)\s*$", txt, re.M)
        if not tab:
            continue
        lvl, mag, proj = tab[-1]
        runs.append((float(hm.group(1)), int(hm.group(2)), int(lvl), float(proj)))
    runs.sort()
    check("N2", len(runs) >= 2, "(numerical, labelled; parsed from logs/probes/X:*, light-cone sphere runs) " +
          "; ".join(f"beta={b_v:g} L={L_v}: m.e0 = {p_v:+.4f} at level {l_v}" for b_v, L_v, l_v, p_v in runs) +
          "; the proved region beta <= 3/10 (and 3/7 under the directional lemma) lies below every run that keeps its initial direction")

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("for the light-cone sphere formation law (7 predecessors, kernel vMF(beta S)) the chordal W1 influence of the kernel satisfies the exact "
            "finite mirror identity W1(mu_V, mu_V') = (A(k)/k)|V - V'| for |V| = |V'| = k (so 1/3 at V = 0 in every direction and A(k)/k perpendicular to V), "
            "and ||D_u(V)|| <= |cos al|(A'(k) + I(k)) + |sin al| A(k)/k < 10/21 for |V| <= 21/10 (exact rational sweep); hence the level chain forgets "
            "its initial records, m_t <= c^t with c = 7 beta L < 1, and has one invariant law for every beta <= 3/10, beyond ln(4/3) = 0.2877, "
            "the ceiling of every TV-Dobrushin argument (block 27's constant gives sqrt3/7 = 0.2474); the W1 route's ceiling is 3/7, reached "
            "exactly if the directional lemma ||D_u(V)|| <= A(|V|)/|V| holds (proved perpendicular and at V = 0; LP numerics N1)")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
