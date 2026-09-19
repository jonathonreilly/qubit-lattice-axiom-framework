#!/usr/bin/env python3
"""Referee check for J:derive:formation-in-3plus1:a4 (author w-macbookpro90c72-j5855, grok-4.6).

Independent code; nothing is taken from the author's script.

V1  M_d from the step law: phi_d is the characteristic function of Z uniform on {0, e_1..e_d}, so
    1 - |phi_d|^2 = k^T Cov(Z) k + O(k^4); Cov(Z) = ((d+1)I - J)/(d+1)^2, eigenvalues 1/(d+1)^2 (ones) and
    1/(d+1) (perp); checked against an exact multivariate Taylor expansion for d = 1..5; the ATTEMPT's
    step-2 display (d/(2(d+1)^2))|k|^2 - (1/(d+1)^2) sum_{i<j} k_i k_j is half of it, and its form
    (d/2) sum k^2 - sum_{i<j} has eigenvalue 1/2 along (1..1), not the text's '(d+2)/2'.
V2  step 1: u = 1 only at k = 0, exactly on the grids (2 pi/4) Z^d (Gaussian rationals), d = 1..4, and in
    floating point on (2 pi/n) Z^d, n = 5..9, d = 1..3.
V3  the dichotomy on finite tori: G_L = L^-d sum_{k != 0} 1/(1 - u) for L = 8..128 grows ~L (d = 1),
    ~log L (d = 2, increment per doubling -> log 2/(2 pi sqrt(det M_2)) = 3 sqrt 3 log 2/(2 pi)), and settles (d = 3).
V4  the lattice kernel at d = 3 against the continuum 4/(pi sqrt(x^T M^-1 x)): torus FFT, L = 256, the
    constant zero-mode offset removed by differences, (G(x) - G(2x)) * 2 sqrt(x^T M^-1 x) -> 4/pi along
    the cone axis (1,1,1) and across it (1,-1,0), (1,0,0).
V5  drift (1,1,1)/4 (exact derivative) and the forward-cone count: paths of 4n unit steps in Z^4 ending at
    (n,n,n,n) by dynamic programming, n = 1..6, against (4n)!/(n!)^4.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp


# --------------------------------------------------------------------------------------------- V1
def v1():
    out = {}
    ok = True
    for d in range(1, 6):
        ks = sp.symbols(f"k1:{d + 1}", real=True)
        t = sp.Symbol("t", real=True)
        re = (1 + sum(sp.cos(t * k) for k in ks)) / (d + 1)
        im = sum(sp.sin(t * k) for k in ks) / (d + 1)
        one_minus_u = sp.expand(sp.series(1 - (re ** 2 + im ** 2), t, 0, 4).removeO())
        quad = sp.expand(one_minus_u.coeff(t, 2))
        odd3 = sp.expand(one_minus_u.coeff(t, 3))
        # covariance of Z uniform on {0, e_1..e_d}
        pts = [tuple(0 for _ in range(d))] + [tuple(1 if j == i else 0 for j in range(d)) for i in range(d)]
        mean = [sp.Rational(sum(p[i] for p in pts), d + 1) for i in range(d)]
        cov = sp.Matrix(d, d, lambda i, j: sp.Rational(sum(p[i] * p[j] for p in pts), d + 1) - mean[i] * mean[j])
        kv = sp.Matrix(ks)
        ok &= sp.expand((kv.T * cov * kv)[0] - quad) == 0 and odd3 == 0
        Md = ((d + 1) * sp.eye(d) - sp.ones(d, d)) / (d + 1) ** 2
        ok &= cov == Md
        ev = Md.eigenvals()
        ok &= ev.get(sp.Rational(1, (d + 1) ** 2), 0) >= 1 and (d == 1 or ev.get(sp.Rational(1, d + 1), 0) == d - 1)
        # the ATTEMPT's step-2 display
        disp = sp.Rational(d, 2 * (d + 1) ** 2) * sum(k ** 2 for k in ks) - sp.Rational(1, (d + 1) ** 2) * sum(
            ks[i] * ks[j] for i in range(d) for j in range(i + 1, d))
        ratio = sp.simplify(quad / disp) if d >= 1 else None
        form = sp.Rational(d, 2) * sp.eye(d) - (sp.ones(d, d) - sp.eye(d)) / 2  # (d/2) sum k^2 - sum_{i<j} k_i k_j
        ones = sp.ones(d, 1)
        ev_ones = sp.simplify((ones.T * form * ones)[0] / d)
        out[d] = (ratio, ev_ones)
    M3 = ((4) * sp.eye(3) - sp.ones(3, 3)) / 16
    return ok, out, M3.det(), sorted(M3.eigenvals().items())


# --------------------------------------------------------------------------------------------- V2
def v2():
    I_POW = [1, sp.I, -1, -sp.I]
    ok_exact = True
    for d in range(1, 5):
        for n in itertools.product(range(4), repeat=d):
            phi = (1 + sum(I_POW[m] for m in n)) / sp.Integer(d + 1)
            u = sp.expand(phi * sp.conjugate(phi))
            if (u == 1) != all(m == 0 for m in n):
                ok_exact = False
    worst = 0.0
    for d in range(1, 4):
        for nn in range(5, 10):
            g = np.array(list(itertools.product(range(nn), repeat=d))) * 2 * np.pi / nn
            phi = (1 + np.exp(1j * g).sum(axis=1)) / (d + 1)
            u = np.abs(phi) ** 2
            nz = np.any(g != 0, axis=1)
            worst = max(worst, u[nz].max())
    return ok_exact, worst


# --------------------------------------------------------------------------------------------- V3
def torus_u(d, L):
    k = 2 * np.pi * np.arange(L) / L
    grids = np.meshgrid(*([k] * d), indexing="ij")
    phi = (1 + sum(np.exp(1j * g) for g in grids)) / (d + 1)
    return np.abs(phi) ** 2


def v3():
    res = {}
    for d, Ls in ((1, (8, 16, 32, 64, 128)), (2, (8, 16, 32, 64, 128)), (3, (8, 16, 32, 64, 128))):
        vals = []
        for L in Ls:
            u = torus_u(d, L)
            inv = np.zeros_like(u)
            mask = u < 1 - 1e-14
            inv[mask] = 1.0 / (1.0 - u[mask])
            vals.append(inv.sum() / L ** d)
        res[d] = (Ls, vals)
    return res


# --------------------------------------------------------------------------------------------- V4
def v4(L=256):
    # half spectrum along the last axis; f is real and even, so G = inverse FFT is real
    k = 2 * np.pi * np.arange(L) / L
    kh = 2 * np.pi * np.arange(L // 2 + 1) / L
    g1, g2, g3 = np.meshgrid(k, k, kh, indexing="ij")
    phi = (1 + np.exp(1j * g1) + np.exp(1j * g2) + np.exp(1j * g3)) / 4
    u = np.abs(phi) ** 2
    del phi, g1, g2, g3
    f = np.zeros_like(u)
    mask = u < 1 - 1e-14
    f[mask] = 1.0 / (1.0 - u[mask])
    del u, mask
    G = np.fft.irfftn(f, s=(L, L, L))  # G[x] = L^-3 sum_k f(k) e^{i k.x}

    def g(x):
        return G[tuple(c % L for c in x)]

    Minv = 4 * (np.eye(3) + np.ones((3, 3)))
    rows = []
    for name, dvec in (("(1,1,1)", (1, 1, 1)), ("(1,-1,0)", (1, -1, 0)), ("(1,0,0)", (1, 0, 0))):
        for m in (3, 5, 8):
            x = tuple(m * c for c in dvec)
            x2 = tuple(2 * c for c in x)
            q = math.sqrt(np.array(x) @ Minv @ np.array(x))
            rows.append((name, m, (g(x) - g(x2)) * 2 * q))
    return rows


# --------------------------------------------------------------------------------------------- V5
def v5():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4
    grad = [sp.simplify(sp.diff(phi, k).subs({k1: 0, k2: 0, k3: 0})) for k in (k1, k2, k3)]
    ok = True
    counts = []
    for n in range(1, 7):
        # DP over compositions: number of step sequences reaching (a,b,c,e) with a+b+c+e = steps
        dp = {(0, 0, 0, 0): 1}
        for _ in range(4 * n):
            nd = {}
            for s, c in dp.items():
                for i in range(4):
                    if s[i] < n:
                        t = list(s)
                        t[i] += 1
                        t = tuple(t)
                        nd[t] = nd.get(t, 0) + c
            dp = nd
        cnt = dp[(n, n, n, n)]
        counts.append(cnt)
        ok &= cnt == math.factorial(4 * n) // math.factorial(n) ** 4
    return grad, ok, counts


D2_PRED = 3 * math.sqrt(3) * math.log(2) / (2 * math.pi)


def main():
    ok1, disp, det3, ev3 = v1()
    print(f"V1 1 - |phi_d|^2 = k^T Cov(Z) k + O(k^4) with Cov(Z) = ((d+1)I - J)/(d+1)^2, eigenvalues 1/(d+1)^2 and 1/(d+1), d = 1..5: {ok1}; "
          f"d = 3: det {det3}, eigenvalues {ev3}")
    print(f"   ATTEMPT step-2 display: true quadratic form / displayed form = {[disp[d][0] for d in range(1, 6)]} for d = 1..5; "
          f"eigenvalue of (d/2)sum k^2 - sum_(i<j) k_i k_j along (1..1) = {[disp[d][1] for d in range(1, 6)]} (text: (d+2)/2)")
    ok2, worst2 = v2()
    print(f"V2 u = 1 only at k = 0: exact on (2pi/4)Z^d, d = 1..4: {ok2}; float max u off 0 on (2pi/n)Z^d, n = 5..9, d = 1..3: {worst2:.6f}")
    r3 = v3()
    for d in (1, 2, 3):
        Ls, vals = r3[d]
        incr = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        print(f"V3 d={d}: G_L for L={list(Ls)}: {[round(v, 4) for v in vals]}; increments per doubling {[round(v, 4) for v in incr]}")
    print(f"   d=2 predicted increment log 2 / (2 pi sqrt(det M_2)), det M_2 = 1/27: 3 sqrt(3) log 2/(2 pi) = {D2_PRED:.4f}")
    rows = v4()
    for name, m, val in rows:
        print(f"V4 d=3 lattice (G(x) - G(2x)) * 2 sqrt(x^T M^-1 x) along {name}, x = {m}*dir: {val:.4f} (4/pi = {4 / math.pi:.4f})")
    grad, ok5, counts = v5()
    print(f"V5 grad phi at 0 = {grad}; (n,n,n,n) path counts by DP n = 1..6: {counts}; equal (4n)!/(n!)^4: {ok5}")

    d1_grow = r3[1][1][-1] > 1.8 * r3[1][1][-2]
    d2_incr = [r3[2][1][i + 1] - r3[2][1][i] for i in range(len(r3[2][1]) - 1)]
    d2_log = abs(d2_incr[-1] - D2_PRED) < 0.005
    d3_incr = [r3[3][1][i + 1] - r3[3][1][i] for i in range(len(r3[3][1]) - 1)]
    d3_settles = abs(d3_incr[-1]) < 0.6 * abs(d3_incr[-2]) and abs(d3_incr[-1]) < 0.02
    far = [val for name, m, val in rows if m == 8]
    green_ok = all(abs(v - 4 / math.pi) < 0.03 * 4 / math.pi for v in far)
    display_half = all(disp[d][0] == 2 for d in range(1, 6))
    all_ok = ok1 and ok2 and worst2 < 1 and d1_grow and d2_log and d3_settles and green_ok and ok5 and grad == [sp.I / 4] * 3
    if all_ok:
        print("HIT: confirmed - 1 - u = k^T M_d k + O(k^4) with M_d = Cov of the step law = ((d+1)I-J)/(d+1)^2 (exact, d = 1..5); u = 1 "
              "only at k = 0; equal-level sums on tori grow ~L (d=1), ~(3 sqrt 3 log 2/(2 pi)) per doubling (d=2), settle (d=3); at d = 3 "
              "det M = 1/256 and the lattice kernel's differences match the continuum 4/(pi sqrt(x^T M^-1 x)) within 3% at x = 8*dir (L = 256) "
              "along and across the cone axis; drift (1,1,1)/4; (n,n,n,n) counts (4n)!/(n!)^4 by DP")
        print("SUMMARY: confirmed - the linear partial survives (dichotomy d > 2, M_d, det 1/256, prefactor 4/pi on the lattice, drift, "
              f"multinomial cone); correction: ATTEMPT step 2's general-d display is half the true form (ratio 2 for d = 1..5: "
              f"{display_half}) and its '(d+2)/2 along (1..1)' should be 1/2 for that form (1/(d+1)^2 for M_d); the HIT's M_d is right; "
              "sphere LRO and nonlinear S(k) bounds are not claimed")
    else:
        print(f"SUMMARY: fails - V1 {ok1}, V2 {ok2}, d1 {d1_grow}, d2 {d2_log}, d3 {d3_settles}, green {green_ok}, V5 {ok5}")


if __name__ == "__main__":
    main()
