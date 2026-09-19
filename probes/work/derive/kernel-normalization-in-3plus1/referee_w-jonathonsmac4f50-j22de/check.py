#!/usr/bin/env python3
"""Referee check for J:derive:kernel-normalization-in-3plus1:a3 (author w-macbookpro90c72-j2171, grok-4.6).

Independent code; nothing is taken from the author's script. n = 4 predecessors {0, e1, e2, e3},
phi(k) = (1 + sum_j e^{-i k_j})/4, sigma^2 = A(n beta)/(n beta), A(kappa) = coth kappa - 1/kappa.

V1  step 1: vMF moments (sympy): Z = 4 pi sinh k/k, E[s.u] = A, E[(s.u)^2] = 1 - 2A/k, transverse variance A/k,
    A = 1 - 1/k + 2/(e^{2k} - 1).
V2  step 2: 1 - |phi|^2 = 3/4 - (1/8)[sum cos k_j + sum_{i<j} cos(k_i - k_j)].
V3  step 3: G_4 = 1913/1344 (exact enumeration).
V4  step 4: all 3x3 matrices with entries in {-1,0,1}, |det| = 1, mapping the signed root set onto itself: count 48;
    those with M e1 = e1 - e2: 4; f(M^T k) = f(k) on the L = 4 and L = 5 grids for all 48.
V5  step 5: on L = 4 (sigma^2 = 1, zero mode removed) C(x) at the six root vectors all equal 149/1344, C_v = 295/672,
    Gamma = (C(0) + 3 C_1)/4 = C_v, and H(k) = C_v phi(k) on all 64 modes, exactly (Gaussian rationals);
    H(k)/phi(k) constant on L = 5, 6 (floating point).
V6  step 6: the cubic jet of A(beta|S|) S_perp/|S| with A = 1 - 1/kappa for four predecessors with random rational
    transverse components (sympy series in a scale eps): order eps = [1 - 1/(n beta)] P theta; the beta-free order
    eps^3 = (Q/(2n)) P theta - (1/2)|P theta|^2 P theta.
V7  step 7 by Gaussian integration by parts (Stein: the Gaussian-closed linear map is E[grad F]), exact on L = 4
    with symbolic beta and sigma^2: g = 1 - 1/(n beta) + C(0) - C_v = 1 - 1/(n beta) + sigma^2 (1 - 1/V).
V8  beyond the attempt: the EXACT vMF mean map (A untruncated, all orders in theta) under the same Gaussian closure
    (infinite-volume C(0) = sigma^2 G_3, C_1 = sigma^2 (G_3 - 4/3)): exchangeability of the four predecessors gives
    K = g_full phi exactly; g_full by Monte Carlo of E[dF/dtheta] at beta = 6, 12, 24, 48 -- beta (1 - g_full) -> 0
    (no O(1/beta) term), while beta^2 (1 - g_full) is the full O(1/beta^2) coefficient, not the truncation's 1/16.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

N_PRED = 4
DELTAS = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


# --------------------------------------------------------------------------------------------- V1
def v1():
    k, u, ph = sp.symbols("kappa u phi", positive=True)
    Z = sp.integrate(sp.integrate(sp.exp(k * u), (u, -1, 1)), (ph, 0, 2 * sp.pi))
    A = sp.simplify(sp.diff(sp.log(Z), k))
    E2 = sp.simplify(sp.diff(Z, k, 2) / Z)
    ok = (sp.simplify((Z - 4 * sp.pi * sp.sinh(k) / k).rewrite(sp.exp)) == 0
          and sp.simplify((A - (sp.coth(k) - 1 / k)).rewrite(sp.exp)) == 0
          and sp.simplify((E2 - (1 - 2 * A / k)).rewrite(sp.exp)) == 0
          and sp.simplify(((1 - E2) / 2 - A / k).rewrite(sp.exp)) == 0
          and sp.simplify(((sp.coth(k) - 1 / k) - (1 - 1 / k + 2 / (sp.exp(2 * k) - 1))).rewrite(sp.exp)) == 0)
    return ok


# --------------------------------------------------------------------------------------------- V2
def v2():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2) + sp.exp(-sp.I * k3)) / 4
    lhs = sp.expand(1 - sp.expand_complex(phi * sp.conjugate(phi)))
    rhs = sp.Rational(3, 4) - (sp.cos(k1) + sp.cos(k2) + sp.cos(k3) + sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3)) / 8
    return sp.simplify(sp.expand_trig(lhs - rhs)) == 0


# --------------------------------------------------------------------------------------------- L = 4 exact machinery
COS4 = [Fr(1), Fr(0), Fr(-1), Fr(0)]
SIN4 = [Fr(0), Fr(1), Fr(0), Fr(-1)]


def f4(n):
    """1 - |phi|^2 at k = (pi/2) n, exact."""
    tot = Fr(0)
    for a, b in ((0, None), (1, None), (2, None), (0, 1), (0, 2), (1, 2)):
        m = n[a] if b is None else (n[a] - n[b])
        tot += COS4[m % 4]
    return Fr(3, 4) - tot / 8


def phi4(n):
    """phi at k = (pi/2) n as (re, im) Fractions; e^{-i k_j} = cos - i sin."""
    re = Fr(1) + sum(COS4[m % 4] for m in n)
    im = -sum(SIN4[m % 4] for m in n)
    return (re / 4, im / 4)


def v3():
    G = Fr(0)
    for n in itertools.product(range(4), repeat=3):
        if n == (0, 0, 0):
            continue
        G += 1 / f4(n)
    return G / 64


# --------------------------------------------------------------------------------------------- V4
ROOTS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]
SIGNED = set(ROOTS) | {tuple(-c for c in r) for r in ROOTS}


def v4():
    group = []
    for entries in itertools.product((-1, 0, 1), repeat=9):
        M = np.array(entries).reshape(3, 3)
        if abs(round(np.linalg.det(M))) != 1:
            continue
        if all(tuple(M @ np.array(r)) in SIGNED for r in ROOTS):
            group.append(M)
    to_root = [M for M in group if tuple(M @ np.array([1, 0, 0])) == (1, -1, 0)]

    def f(k):
        return 0.75 - (np.cos(k[0]) + np.cos(k[1]) + np.cos(k[2]) + np.cos(k[0] - k[1]) + np.cos(k[0] - k[2]) + np.cos(k[1] - k[2])) / 8

    inv_ok = True
    for L in (4, 5):
        ks = [2 * np.pi * np.array(n) / L for n in itertools.product(range(L), repeat=3)]
        for M in group:
            inv_ok &= all(abs(f(M.T @ k) - f(k)) < 1e-12 for k in ks)
    Mex = np.array([[1, 0, 0], [-1, -1, -1], [0, 0, 1]])
    ex_in = any((Mex == M).all() for M in group) and tuple(Mex @ np.array([1, 0, 0])) == (1, -1, 0)
    return len(group), len(to_root), inv_ok, ex_in


# --------------------------------------------------------------------------------------------- V5
def v5():
    modes = [n for n in itertools.product(range(4), repeat=3)]
    S = {n: (Fr(0) if n == (0, 0, 0) else 1 / f4(n)) for n in modes}

    def C(x):
        return sum(S[n] * COS4[sum(a * b for a, b in zip(n, x)) % 4] for n in modes) / 64

    root_vals = {r: C(r) for r in ROOTS}
    C0 = C((0, 0, 0))
    Cv = sum(S[n] * (phi4(n)[0] ** 2 + phi4(n)[1] ** 2) for n in modes) / 64
    C1 = root_vals[(1, 0, 0)]
    Gamma = (C0 + 3 * C1) / 4
    # H(k) = V^-1 sum_p phi(-p) phi(p + k) S(p), phi(-p) = conj phi(p)
    H_ok = True
    for kn in modes:
        hr, hi = Fr(0), Fr(0)
        for p in modes:
            if S[p] == 0:
                continue
            a_r, a_i = phi4(p)
            a_i = -a_i  # conj
            q = tuple((pi + ki) % 4 for pi, ki in zip(p, kn))
            b_r, b_i = phi4(q)
            hr += (a_r * b_r - a_i * b_i) * S[p]
            hi += (a_r * b_i + a_i * b_r) * S[p]
        hr, hi = hr / 64, hi / 64
        pr, pim = phi4(kn)
        H_ok &= hr == Cv * pr and hi == Cv * pim
    flt = []
    for L in (5, 6):
        ks = [2 * np.pi * np.array(n) / L for n in itertools.product(range(L), repeat=3)]
        ph = np.array([(1 + np.exp(-1j * k).sum()) / 4 for k in ks])
        Sv = np.array([0.0 if i == 0 else 1 / (1 - abs(p) ** 2) for i, p in enumerate(ph)])
        idx = {tuple(n): i for i, n in enumerate(itertools.product(range(L), repeat=3))}
        nlist = list(itertools.product(range(L), repeat=3))
        ratios = []
        for kn in nlist:
            h = 0
            for i, p in enumerate(nlist):
                q = tuple((a + b) % L for a, b in zip(p, kn))
                h += np.conj(ph[i]) * ph[idx[q]] * Sv[i]
            h /= L ** 3
            if abs(ph[idx[kn]]) > 1e-9:
                ratios.append(h / ph[idx[kn]])
        cv = (np.abs(ph) ** 2 * Sv).sum() / L ** 3
        flt.append((L, max(abs(r - cv) for r in ratios)))
    return root_vals, C0, Cv, Gamma, H_ok, flt


# --------------------------------------------------------------------------------------------- V6
def v6(seed=3):
    rng = np.random.default_rng(seed)
    eps, beta = sp.symbols("epsilon beta", positive=True)
    th = [[sp.Rational(int(rng.integers(-5, 6)), int(rng.integers(1, 7))) for _ in range(2)] for _ in range(N_PRED)]
    n = N_PRED
    Sx = sum(eps * t[0] for t in th)
    Sy = sum(eps * t[1] for t in th)
    Sz = sum(sp.sqrt(1 - eps ** 2 * (t[0] ** 2 + t[1] ** 2)) for t in th)
    normS = sp.sqrt(Sx ** 2 + Sy ** 2 + Sz ** 2)
    Fx = (1 - 1 / (beta * normS)) * Sx / normS
    ser = sp.series(Fx, eps, 0, 4).removeO()
    Px = sum(t[0] for t in th) / n
    Py = sum(t[1] for t in th) / n
    Q = sum(t[0] ** 2 + t[1] ** 2 for t in th)
    lin = sp.simplify(ser.coeff(eps, 1) - (1 - 1 / (n * beta)) * Px)
    cub = sp.expand(ser.coeff(eps, 3))
    cub_beta0 = sp.limit(cub, beta, sp.oo)
    claimed = Q / (2 * n) * Px - sp.Rational(1, 2) * (Px ** 2 + Py ** 2) * Px
    even = sp.simplify(ser.coeff(eps, 2)) == 0 and sp.simplify(ser.coeff(eps, 0)) == 0
    cub_beta1 = sp.simplify(sp.expand(cub - cub_beta0) * beta)  # the O(theta^3 / beta) part, times beta
    return lin == 0, sp.simplify(cub_beta0 - claimed) == 0, even, sp.simplify(cub_beta1) != 0


# --------------------------------------------------------------------------------------------- V7
def v7():
    beta, s2 = sp.symbols("beta sigma2", positive=True)
    n = N_PRED
    # covariance on L = 4: C(x) = s2 * C4(x), C4 from V5 (sigma^2 = 1)
    modes = [m for m in itertools.product(range(4), repeat=3)]
    S = {m: (Fr(0) if m == (0, 0, 0) else 1 / f4(m)) for m in modes}

    def C4(x):
        return sum(S[m] * COS4[sum(a * b for a, b in zip(m, x)) % 4] for m in modes) / 64

    Cmat = [[s2 * sp.Rational(*(lambda v: (v.numerator, v.denominator))(C4(tuple(a - b for a, b in zip(DELTAS[i], DELTAS[j])))))
             for j in range(n)] for i in range(n)]
    # Stein: E[dF^1(x)/d theta^1(x - delta_a)] for F = c1 P theta + (Q/(2n)) P theta - (1/2)|P theta|^2 P theta
    # dF^1/dtheta^1_a = c1/n + (1/(2n))[2 theta^1_a (P theta)^1 + Q/n] - (1/2)[2 (P theta)^1 (P theta)^1 / n + |P theta|^2 / n]
    c1 = 1 - 1 / (n * beta)
    E_theta_a_Ptheta = sum(Cmat[0][b] for b in range(n)) / n                 # E[theta^1_a (P theta)^1], a = 0
    E_Q = 2 * sum(Cmat[b][b] for b in range(n))                               # two components
    E_Ptheta_sq = sum(Cmat[a][b] for a in range(n) for b in range(n)) / n ** 2  # E[((P theta)^1)^2] = C_v
    dF = c1 / n + (2 * E_theta_a_Ptheta + E_Q / n) / (2 * n) - (2 * E_Ptheta_sq / n + 2 * E_Ptheta_sq / n) / 2
    g = sp.simplify(n * dF)
    target = sp.simplify(1 - 1 / (n * beta) + s2 * (1 - sp.Rational(1, 64)))
    return sp.simplify(g - target) == 0, g


# --------------------------------------------------------------------------------------------- V8
def g3_extrapolated():
    vals = []
    for L in (64, 128):
        k = 2 * np.pi * np.arange(L) / L
        g1, g2, g3 = np.meshgrid(k, k, k, indexing="ij")
        ph = (1 + np.exp(-1j * g1) + np.exp(-1j * g2) + np.exp(-1j * g3)) / 4
        f = 1 - np.abs(ph) ** 2
        m = f > 1e-14
        vals.append((1 / f[m]).sum() / L ** 3)
    return 2 * vals[1] - vals[0]  # finite-size error ~ c/L


def A_exact(kap):
    return 1 / np.tanh(kap) - 1 / kap


def v8(G3, betas=(6, 12, 24, 48), samples=2_000_000, seed=22):
    rng = np.random.default_rng(seed)
    n = N_PRED
    out = []
    for beta in betas:
        s2 = A_exact(n * beta) / (n * beta)
        C0 = s2 * G3
        C1 = s2 * (G3 - 4 / 3)
        Sig = C1 * np.ones((n, n)) + (C0 - C1) * np.eye(n)
        Lc = np.linalg.cholesky(Sig)
        tot_full, tot_poly, kept = 0.0, 0.0, 0
        h = 1e-5
        for _ in range(samples // 250_000):
            X = rng.standard_normal((250_000, n)) @ Lc.T  # component 1 of the four predecessors
            Y = rng.standard_normal((250_000, n)) @ Lc.T  # component 2
            good = (X ** 2 + Y ** 2 < 1 - 1e-3).all(axis=1)  # margin for the finite difference
            X, Y = X[good], Y[good]
            kept += len(X)

            def F_full(Xm):
                Sz = np.sqrt(1 - Xm ** 2 - Y ** 2).sum(axis=1)
                Sx, Sy = Xm.sum(axis=1), Y.sum(axis=1)
                nS = np.sqrt(Sx ** 2 + Sy ** 2 + Sz ** 2)
                return A_exact(beta * nS) * Sx / nS

            def F_poly(Xm):
                Px, Py = Xm.mean(axis=1), Y.mean(axis=1)
                Q = (Xm ** 2 + Y ** 2).sum(axis=1)
                return (1 - 1 / (n * beta)) * Px + Q / (2 * n) * Px - 0.5 * (Px ** 2 + Py ** 2) * Px

            Xp, Xm_ = X.copy(), X.copy()
            Xp[:, 0] += h
            Xm_[:, 0] -= h
            tot_full += ((F_full(Xp) - F_full(Xm_)) / (2 * h)).sum()
            tot_poly += ((F_poly(Xp) - F_poly(Xm_)) / (2 * h)).sum()
        g_full = n * tot_full / kept
        g_poly = n * tot_poly / kept
        g_trunc = 1 - 1 / (n * beta) + s2  # infinite-volume truncation value (= 1 - 1/(16 beta^2) + exp. small)
        out.append((beta, g_full, g_poly, g_trunc, kept))
    return out


def main():
    ok1 = v1()
    print(f"V1 vMF moments (Z, A, E[(s.u)^2] = 1 - 2A/k, transverse variance A/k, A = 1 - 1/k + 2/(e^(2k)-1)): {ok1}")
    ok2 = v2()
    print(f"V2 1 - |phi|^2 = 3/4 - (1/8)(sum of the six A3 cosines): {ok2}")
    G4 = v3()
    print(f"V3 G_4 = {G4}")
    ng, nto, inv_ok, ex_in = v4()
    print(f"V4 root-set automorphisms with entries in {{-1,0,1}}: {ng}; sending e1 to e1-e2: {nto}; f invariant on L=4,5 grids: {inv_ok}; "
          f"the attempt's M among them: {ex_in}")
    root_vals, C0, Cv, Gamma, H_ok, flt = v5()
    print(f"V5 L=4, sigma^2=1: C at the six roots {sorted(set(root_vals.values()))}; C(0) = {C0}; C_v = {Cv}; Gamma = {Gamma}; "
          f"H(k) = C_v phi(k) on all 64 modes: {H_ok}; float max |H/phi - C_v|: {', '.join(f'L={L}: {d:.1e}' for L, d in flt)}")
    lin_ok, cub_ok, even_ok, has_b = v6()
    print(f"V6 cubic jet (4 predecessors, random rational theta): order eps = [1 - 1/(n beta)] P theta: {lin_ok}; beta-free order eps^3 = "
          f"(Q/2n) P theta - |P theta|^2 P theta/2: {cub_ok}; even orders vanish: {even_ok}; an O(theta^3/beta) part present (dropped): {has_b}")
    ok7, g7 = v7()
    print(f"V7 Stein on L=4, symbolic beta, sigma^2: g = {g7}; equals 1 - 1/(n beta) + sigma^2 (1 - 1/V): {ok7}")
    G3 = g3_extrapolated()
    print(f"V8 G_3 (torus 64/128, extrapolated) = {G3:.5f}")
    rows = v8(G3)
    for beta, gf, gp, gt, kept in rows:
        print(f"   beta={beta}: g_full (exact vMF map, Gaussian closure) = {gf:.6f}; g_poly (cubic map, MC) = {gp:.6f}; truncation "
              f"formula = {gt:.6f}; beta(1-g_full) = {beta * (1 - gf):.4f}; beta^2(1-g_full) = {beta ** 2 * (1 - gf):.3f}; "
              f"naive gain loss beta(1/(4 beta)) = 0.25; samples {kept}")

    b_scaled = [beta * (1 - gf) for beta, gf, gp, gt, kept in rows]
    no_first_order = abs(b_scaled[-1]) < 0.01 and abs(b_scaled[-1]) < abs(b_scaled[0]) / 10
    poly_consistent = all(abs(gp - gt) < 2e-3 for beta, gf, gp, gt, kept in rows)
    all_ok = (ok1 and ok2 and G4 == Fr(1913, 1344) and ng == 48 and nto == 4 and inv_ok and ex_in
              and len(set(root_vals.values())) == 1 and root_vals[(1, 0, 0)] == Fr(149, 1344) and Cv == Fr(295, 672)
              and Gamma == Cv and H_ok and all(d < 1e-10 for L, d in flt) and lin_ok and cub_ok and even_ok and ok7
              and no_first_order and poly_consistent)
    if all_ok:
        print("HIT: confirmed - cubic-Gaussian mean map K = g phi with g = 1 - 1/(n beta) + sigma^2 (1 - 1/V) re-derived by Gaussian "
              "integration by parts (exact on L=4), the A3 automorphism group (48, four maps e1 -> e1-e2), equal root-vector "
              "covariances 149/1344, C_v = 295/672, H = C_v phi on every mode, G_4 = 1913/1344, the vMF moments and the cubic jet; "
              "beyond the truncation, the exact vMF mean map under the same Gaussian closure also gives K = g_full phi with "
              f"beta(1 - g_full) = {', '.join(f'{b:.4f}' for b in b_scaled)} at beta = 6, 12, 24, 48: no O(1/beta) term")
        print("SUMMARY: confirmed - the mean-map statement survives (K proportional to phi by A3 exchangeability, O(1/beta) cancels, "
              "G_3 drops out); the displayed 1 - g = 1/(16 beta^2) is the truncation's value only: the exact map's O(1/beta^2) "
              f"coefficient beta^2(1-g_full) = {', '.join(f'{beta ** 2 * (1 - gf):.2f}' for beta, gf, gp, gt, kept in rows)} "
              "-- opposite in sign to the truncation's +1/16, so the finite-beta 'Goldstone mass' 1 - g^2 of step 8 is a truncation "
              "artefact (the attempt's (3) says the dropped terms are O(1/beta^2)); the noise factor and the task's full a are not derived")
    else:
        print(f"SUMMARY: fails - V1 {ok1}, V2 {ok2}, G4 {G4}, group {ng}/{nto}/{inv_ok}/{ex_in}, V5 {root_vals}/{Cv}/{Gamma}/{H_ok}, "
              f"V6 {lin_ok}/{cub_ok}/{even_ok}, V7 {ok7}, V8 {b_scaled}/{poly_consistent}")


if __name__ == "__main__":
    main()
