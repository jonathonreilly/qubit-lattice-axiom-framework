#!/usr/bin/env python3
"""Exact check of the hand construction in library/upper-chain-by-hand.md, section 3 (the nest objection, Text 23.5).

A kill test only. Nothing in the chain rests on this run; the proof is the written one. Exact rational arithmetic where it says so.

Setting: U = 1, normal-only field H = f e_1, as in checks/upper-chain_nest.py. Points m of the normal circle carry f(m); the bond at m joins
sites m - 1 and m; site x is the unit interval [x, x + 1]. W_sigma[f](c) := sum_(|k| < sigma) (1 - |k| / sigma) f(c + k) is Q^(l) on the normal
bond whose kernel is centred at c, sigma = L^l.

Criteria, written before the first run.
C1. For f affine on [c - sigma, c] and on [c, c + sigma], with values p, q, w: W_sigma[f](c) = sigma q + (sigma^2 - 1)/(6 sigma) (p + w - 2 q), and the half moment
    M_sigma = q (sigma - 1)/2 + (sigma^2 - 1)/(6 sigma) (w - q). Exact, on random rationals.
C2. W_(L sigma)[f](c) = sum_(|k| < L) (1 - |k|/L) W_sigma[f](c + k sigma). Exact, on random rationals.
C3. The exterior cubic g: g(0) = A, g(M) = 0, sum (1 - m/M) g(m) = -tau A, sum (m/M) g(m) = 0, and its energy equals
    a^2 M (M^2 - 1)/3 + b^2 M (M^2 - 1)(M^2 - 4)/5, equal to E(tau, M). Exact.
C4. Admissibility: on each configuration of the grid every constraint of the nest evaluates to exactly 0: top level on all bonds, level j on all bonds with both ends in
    layer j.
C5. Every inequality the written proof asserts, on each configuration: 0 < q <= 3/10; G >= 61 s_0 / 540; a <= 2 + 16/(5 L); 1 <= R_i <= 4; 0 < tau <= (s+1)(2s+1)/(6s);
    E <= 32 A^2 / M, and the total energy <= 64 A^2 / M; and the final bound, Rayleigh quotient <= 284 L^-k Gamma^2, with Gamma <= ((2 + 16/(5 L)) 4^(r-1))^(k-1).
C6. Controls: the test must be able to fail. (a) tau off by 1 in the exterior gives a non-zero top constraint at an edge. (b) The limit value kappa = 4 in place of kappa_s
    gives a non-zero fine constraint.
C7. Full operator, d = 2, by the code of checks/upper-chain_nest.py: L = 3, n = 2, depth 1; L = 3, n = 3, depth 2. The field lies in ker bC to 1e-11, curl 0 to 1e-11, and its
    Rayleigh quotient with P_N and the weight of that code equals the 1D value to 1e-9.
C8. Rayleigh: for L in {3, 5, 7, 9}, X = 2, depth 1, c_1D of checks/upper-chain_nest2.py is at most the quotient of this mode, to 1e-9.

FAIL of C4, C5 or C7 means the written construction is wrong.
"""
import math
import os
import random
import resource
import sys
import time
from fractions import Fraction as Fr

sys.dont_write_bytecode = True
RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def W(f, sigma, c):
    N = len(f)
    tot = f[c % N] + Fr(0)
    for k in range(1, sigma):
        wt = 1 - Fr(k, sigma)
        tot += wt * (f[(c + k) % N] + f[(c - k) % N])
    return tot


def half(sigma):
    return Fr(sigma * sigma - 1, 6 * sigma)


def kappa(s):
    return Fr(4 * s * s + 2, s * s - 1)


def chain(T, kap):
    """Solve f_(i+1) + kap f_i + f_(i-1) = 0, i = 1 .. T - 1, f_0 = f_T = 1."""
    if T == 1:
        return [Fr(1), Fr(1)]
    n = T - 1
    c = [Fr(0)] * n
    d = [Fr(0)] * n
    # rows i = 1 .. T - 1: f_(i-1) + kap f_i + f_(i+1) = rhs
    for idx in range(n):
        rhs = Fr(0)
        if idx == 0:
            rhs -= 1
        if idx == n - 1:
            rhs -= 1
        if idx == 0:
            denom = kap
            c[idx] = Fr(1) / denom
            d[idx] = rhs / denom
        else:
            denom = kap - c[idx - 1]
            c[idx] = Fr(1) / denom
            d[idx] = (rhs - d[idx - 1]) / denom
    x = [Fr(0)] * n
    x[-1] = d[-1]
    for idx in range(n - 2, -1, -1):
        x[idx] = d[idx] - c[idx] * x[idx + 1]
    return [Fr(1)] + x + [Fr(1)]


def cubic(A, tau, M):
    a = -6 * A * (tau + Fr(M - 1, 2)) / (M * (M * M - 1))
    b = 30 * A * (tau * M + Fr((M - 1) * (M - 2), 6)) / (M * (M * M - 1) * (M * M - 4))
    g = [A * (1 - Fr(m, M)) + a * m * (M - m) + b * m * (M - m) * (2 * m - M) for m in range(M + 1)]
    E = a * a * M * (M * M - 1) / 3 + b * b * M * (M * M - 1) * (M * M - 4) / 5
    return g, a, b, E


def affine_fill(f, N, start, step, vals, sign=1):
    """Fill f on start + sign * [0, step * (len(vals) - 1)], affine between nodes."""
    for i in range(len(vals) - 1):
        for p in range(step + 1):
            f[(start + sign * (i * step + p)) % N] = vals[i] + Fr(p, step) * (vals[i + 1] - vals[i])


def build(L, n, k, r, t, X, tau_shift=0, kap0=None):
    M = L**n
    s = [L ** (n - k + j) for j in range(k + 1)]
    assert s[k] == M and s[0] >= L
    Lx = X * M
    lo = [0] * k
    hi = [0] * k
    lo[k - 1], hi[k - 1] = 0, t * M
    for j in range(k - 1, 0, -1):
        lo[j - 1], hi[j - 1] = lo[j] + r * s[j], hi[j] - r * s[j]
        assert hi[j - 1] > lo[j - 1]
    f = [Fr(0)] * Lx
    T0 = (hi[0] - lo[0]) // s[0]
    assert (hi[0] - lo[0]) % s[0] == 0 and T0 >= L
    fine = chain(T0, kappa(s[0]) if kap0 is None else kap0)
    affine_fill(f, Lx, lo[0], s[0], fine)
    q = -fine[1] / fine[0]
    sl = s[0]
    tau = Fr(sl + 1, 2) + half(sl) * (fine[1] / fine[0] - 1)
    A = [Fr(1)]
    taus = [tau]
    ratios = []
    avals = []
    for j in range(1, k):
        sj = s[j]
        kj = kappa(sj)
        F = [A[-1], A[-1] * (1 - Fr(6 * sj, sj * sj - 1) * (tau + Fr(sj - 1, 2)))]
        avals.append(-F[1] / F[0])
        for i in range(1, r):
            F.append(-kj * F[i] - F[i - 1])
        ratios.extend([-F[i + 1] / F[i] for i in range(r)])
        affine_fill(f, Lx, hi[j - 1], sj, F, 1)
        affine_fill(f, Lx, lo[j - 1], sj, F, -1)
        A.append(F[r])
        tau = Fr(sj + 1, 2) + half(sj) * (F[r - 1] / F[r] - 1)
        taus.append(tau)
    g, a, b, E = cubic(A[-1], tau + tau_shift, M)
    assert g[0] == A[-1] or tau_shift != 0
    for m in range(1, M):
        f[(hi[k - 1] + m) % Lx] += g[m]
        f[(lo[k - 1] - m) % Lx] += g[m]
    return dict(L=L, n=n, k=k, r=r, t=t, X=X, M=M, s=s, Lx=Lx, lo=lo, hi=hi, f=f, q=q, A=A, taus=taus, ratios=ratios, avals=avals, a=a, b=b, E=E, T0=T0)


def all_constraints(c):
    """Every constraint of ker bC, as (name, value)."""
    f, M, Lx, s, lo, hi, X = c["f"], c["M"], c["Lx"], c["s"], c["lo"], c["hi"], c["X"]
    out = []
    for J in range(X):
        out.append((f"top {J}", W(f, M, J * M)))
    for j in range(c["k"]):
        for node in range(lo[j] + s[j], hi[j], s[j]):
            out.append((f"level {j} node {node}", W(f, s[j], node)))
    return out


def energies(c):
    f, Lx, s, lo, hi, k, M = c["f"], c["Lx"], c["s"], c["lo"], c["hi"], c["k"], c["M"]
    atoms = {}
    weight_s = {}
    for x in range(Lx):
        key = None
        for j in range(k):
            if lo[j] <= x < hi[j]:
                key = (j, x // s[j])
                weight_s[x] = s[j]
                break
        if key is None:
            key = (k, x // M)
            weight_s[x] = M
        atoms.setdefault(key, []).append(x)
    en = Fr(0)
    for xs in atoms.values():
        d = [f[(x + 1) % Lx] - f[x] for x in xs]
        mean = sum(d, Fr(0)) / len(d)
        en += sum(((v - mean) ** 2 for v in d), Fr(0))
    norm_code = sum((f[(x + 1) % Lx] ** 2 / Fr(weight_s[x]) ** 2 for x in range(Lx)), Fr(0))
    s0 = s[0]
    inner = sum((f[m] ** 2 for m in list(range(lo[0] + 1, lo[0] + s0)) + list(range(hi[0] - s0 + 1, hi[0]))), Fr(0)) / Fr(s0) ** 2
    return en, norm_code, inner


def check_c5(c):
    L, k, r, s, M, q, A = c["L"], c["k"], c["r"], c["s"], c["M"], c["q"], c["A"]
    ok = True
    msgs = []

    def req(cond, text):
        nonlocal ok
        if not cond:
            ok = False
            msgs.append(text)

    s0 = s[0]
    G = (s0 - 1) * ((1 + q) ** 2 * Fr(2 * s0 - 1, 6 * s0) - q)
    req(0 < q <= Fr(3, 10), f"q = {float(q)}")
    req(G >= Fr(61 * s0, 540), "G")
    for j, tau in enumerate(c["taus"]):
        sj = s[j]
        req(0 < tau <= Fr((sj + 1) * (2 * sj + 1), 6 * sj), f"tau {j}")
    for a in c["avals"]:
        req(a <= 2 + Fr(16, 5 * L), f"a = {float(a)}")
    for R in c["ratios"]:
        req(1 <= R <= 4, f"R = {float(R)}")
    AA = A[-1]
    req(c["E"] <= 32 * AA * AA / M, "E")
    en, norm_code, inner = energies(c)
    req(en <= 64 * AA * AA / M, "total energy")
    req(inner == 2 * G * A[0] ** 2 / Fr(s0) ** 2, "first block sum formula")
    Gamma = abs(AA / A[0])
    req(Gamma <= ((2 + Fr(16, 5 * L)) * 4 ** (r - 1)) ** (k - 1), "Gamma")
    req(en / inner <= 284 * Gamma**2 / Fr(L) ** k, "final bound")
    req(norm_code >= inner, "norm")
    return ok, msgs, en, norm_code, inner, Gamma


def main():
    t0 = time.time()
    rnd = random.Random(20261101)
    verdict = {}

    # C1
    ok = True
    for sigma in (2, 3, 4, 5, 9, 16):
        for _ in range(5):
            p, qv, w = [Fr(rnd.randint(-99, 99), rnd.randint(1, 40)) for _ in range(3)]
            N = 4 * sigma
            f = [Fr(0)] * N
            for i in range(sigma + 1):
                f[(sigma + i) % N] = qv + Fr(i, sigma) * (w - qv)
                f[(sigma - i) % N] = qv + Fr(i, sigma) * (p - qv)
            ok = ok and W(f, sigma, sigma) == sigma * qv + half(sigma) * (p + w - 2 * qv)
            mom = sum(((1 - Fr(i, sigma)) * f[sigma + i] for i in range(1, sigma)), Fr(0))
            ok = ok and mom == qv * Fr(sigma - 1, 2) + half(sigma) * (w - qv)
    verdict["C1"] = ok

    # C2
    ok = True
    for LL, sigma in ((3, 3), (3, 9), (5, 3), (4, 5), (2, 7)):
        N = 3 * LL * sigma
        f = [Fr(rnd.randint(-50, 50), rnd.randint(1, 30)) for _ in range(N)]
        for c in (0, 7, N // 2):
            lhs = W(f, LL * sigma, c)
            rhs = sum(((1 - Fr(abs(k), LL)) * W(f, sigma, c + k * sigma) for k in range(-LL + 1, LL)), Fr(0))
            ok = ok and lhs == rhs
    verdict["C2"] = ok

    # C3
    ok = True
    for M in (9, 15, 25, 27, 81):
        for _ in range(3):
            A = Fr(rnd.randint(1, 50), rnd.randint(1, 20)) * rnd.choice((1, -1))
            tau = Fr(rnd.randint(0, 200), rnd.randint(1, 20))
            g, a, b, E = cubic(A, tau, M)
            ok = ok and g[0] == A and g[M] == 0
            ok = ok and sum(((1 - Fr(m, M)) * g[m] for m in range(1, M)), Fr(0)) == -tau * A
            ok = ok and sum((Fr(m, M) * g[m] for m in range(1, M)), Fr(0)) == 0
            d = [g[m + 1] - g[m] for m in range(M)]
            mean = sum(d, Fr(0)) / M
            en = sum(((v - mean) ** 2 for v in d), Fr(0))
            ok = ok and en == E
            E2 = 12 * A * A * (tau + Fr(M - 1, 2)) ** 2 / (M * (M * M - 1)) + 180 * A * A * (tau * M + Fr((M - 1) * (M - 2), 6)) ** 2 / (M * (M * M - 1) * (M * M - 4))
            ok = ok and E == E2
    verdict["C3"] = ok
    print("C1, C2, C3:", verdict, f"elapsed {time.time() - t0:.1f} s", flush=True)

    grid = [
        (3, 2, 1, 1, 1, 2), (3, 2, 1, 1, 1, 3), (3, 2, 1, 1, 1, 4), (3, 2, 1, 1, 2, 5), (3, 2, 1, 1, 2, 3),
        (5, 2, 1, 1, 1, 2), (5, 2, 1, 1, 1, 4), (7, 2, 1, 1, 1, 2), (9, 2, 1, 1, 1, 3),
        (3, 3, 1, 1, 1, 2), (3, 3, 1, 1, 1, 4),
        (3, 3, 2, 1, 1, 2), (3, 3, 2, 1, 2, 3), (3, 3, 2, 2, 2, 3), (5, 3, 2, 1, 1, 2), (5, 3, 2, 2, 1, 2), (7, 3, 2, 1, 1, 2), (7, 3, 2, 3, 1, 2),
        (3, 4, 3, 1, 1, 2), (5, 4, 3, 1, 1, 2),
    ]
    ok4 = ok5 = True
    print("config (L, n, k, r, t, X): quotient Q, Q L^k, Gamma, Q / (284 L^-k Gamma^2), ", flush=True)
    for cfg in grid:
        c = build(*cfg)
        bad = [(nm, v) for nm, v in all_constraints(c) if v != 0]
        if bad:
            ok4 = False
            print("  C4 FAIL", cfg, bad[:3])
        good, msgs, en, norm_code, inner, Gamma = check_c5(c)
        if not good:
            ok5 = False
            print("  C5 FAIL", cfg, msgs)
        Q = en / norm_code
        LK = c["L"] ** c["k"]
        print(f"  {cfg}: Q = {float(Q):.5f}, Q L^k = {float(Q) * LK:.3f}, Gamma = {float(Gamma):.3f}, ratio to bound {float(en / inner / (284 * Gamma ** 2 / Fr(LK))):.3f}; elapsed {time.time() - t0:.1f} s", flush=True)
        rss_guard()
    verdict["C4"] = ok4
    verdict["C5"] = ok5

    # C6 controls
    c = build(3, 2, 1, 1, 1, 3, tau_shift=1)
    v = dict(all_constraints(c))
    bad_a = any(val != 0 for nm, val in v.items() if nm.startswith("top"))
    c = build(3, 2, 1, 1, 1, 3, kap0=Fr(4))
    bad_b = any(val != 0 for nm, val in all_constraints(c) if nm.startswith("level 0"))
    verdict["C6"] = bad_a and bad_b

    # C7 full operator
    import importlib.util

    import numpy as np
    import scipy.linalg as sl

    here = os.path.dirname(os.path.abspath(__file__))
    checks = os.path.dirname(here)
    spec = importlib.util.spec_from_file_location("nest1", os.path.join(checks, "upper-chain_nest.py"))
    nest1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nest1)
    ok7 = True
    for L, n, k, r, t, X, layers in ((3, 2, 1, 1, 1, 4, {1: (0, 3)}), (3, 3, 2, 1, 1, 2, {2: (0, 3), 1: (3, 6)})):
        c = build(L, n, k, r, t, X)
        lat = nest1.Lat(2, L, n, X, (0.0,))
        co = lat.coords()
        ff = np.array([float(v) for v in c["f"]])
        H = np.zeros(lat.nb)
        H[0::2] = ff[(co[:, 0] + 1) % lat.shape[0]]
        bC, rN = nest1.constraints(lat, layers)
        qmax = float(np.abs(bC.real @ H).max())
        curl = float(np.abs(lat.curl().real @ H).max())
        phi = lat.D().real.T @ H
        U = sl.orth(rN.real.T.toarray(), rcond=1e-10)
        Y = phi - U @ (U.T @ phi)
        w = nest1.weights(lat, layers)
        q_full = float(Y @ Y) / float(np.sum(w * H * H))
        en, norm_code, inner = energies(c)
        q_1d = float(en / norm_code)
        print(f"C7 L={L} n={n} depth {k}: max constraint {qmax:.2e}, max curl {curl:.2e}, quotient {q_full:.10f}, 1D {q_1d:.10f}", flush=True)
        ok7 = ok7 and qmax <= 1e-11 and curl <= 1e-11 and abs(q_full - q_1d) <= 1e-9
        rss_guard()
    verdict["C7"] = ok7

    # C8
    spec = importlib.util.spec_from_file_location("nest2", os.path.join(checks, "upper-chain_nest2.py"))
    nest2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nest2)
    ok8 = True
    for L in (3, 5, 7, 9):
        layers = nest2.nested_layers(L, 2, 1, 2)
        cmin, _ = nest2.one_d(L, 2, 2, layers)
        c = build(L, 2, 1, 1, 1, 2)
        en, norm_code, inner = energies(c)
        Q = float(en / norm_code)
        print(f"C8 L={L}: c_1D = {cmin:.5f}, quotient of the mode = {Q:.5f}, ratio {Q / cmin:.3f}", flush=True)
        ok8 = ok8 and cmin <= Q * (1 + 1e-9)
        rss_guard()
    verdict["C8"] = ok8

    for key in sorted(verdict):
        print(key, "PASS" if verdict[key] else "FAIL")
    print(f"elapsed {time.time() - t0:.1f} s; max RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9:.3f} GB")


if __name__ == "__main__":
    main()
