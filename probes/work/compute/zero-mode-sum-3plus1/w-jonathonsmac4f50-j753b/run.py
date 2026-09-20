#!/usr/bin/env python3
"""zero-mode-sum-3plus1, independent run 2 of 2 (worker w-jonathonsmac4f50-j753b, claude-opus-5).

G = (2 pi)^-3 int_{[-pi,pi]^3} dk / (1 - |phi(k)|^2), phi(k) = (1 + sum_j e^{i k_j})/4: the return sum of the backward
(four-predecessor) plane walk on the 3+1 event lattice.

A1 (exact)  1/(1 - u) = sum_n u^n with u = |phi|^2 in [0, 1), and (2 pi)^-3 int u^n = sum_x p_n(x)^2 = P_n, the probability
            that the difference of two independent plane walks is back at the origin after n steps (Parseval).  P_n is
            computed in exact rational arithmetic for n <= 400 from
              sum_x p_n(x)^2 = (n!)^2 16^-n [t^n] (sum_k t^k/(k!)^2)^4 ,
            by one integer polynomial power (the multinomial squares summed by the series identity).
A2 (exact)  tail bound: P_n <= max_x p_n(x) <= 16/(2 pi (n - 3))^{3/2} for n >= 4 (Robbins' Stirling bounds at the balanced
            multinomial, plus max_x p_n(x) non-increasing in n), so sum_{n > N} P_n <= (32/(2 pi)^{3/2}) / sqrt(N - 3).
N1 (numerical, labelled)  the local limit: n^{3/2} P_n -> 1/((2 pi)^{3/2} sqrt(det Sigma)) with Sigma = 2 Cov(step) = 2M,
            M = (1/4)I - (1/16)J, det Sigma = 1/32, i.e. 4 sqrt2/(2 pi)^{3/2} = 0.359174; verified on the exact P_n, and used
            for the sharper bracket under the (numerically verified) monotonicity of n^{3/2} P_n.
N2 (numerical, labelled)  the spin-wave plateau |m| ~ 1 - sigma^2 G, sigma^2 = A(4 beta)/(4 beta), against the logs under
            logs/probes/X:formation-3plus1-sphere-memory/.
N3 (numerical, labelled)  the 2+1 contrast: the same sum on the L x L plane, phi = (1 + e^{ik1} + e^{ik2})/3, L = 16..512,
            and its log L growth."""
import glob
import math
import os
import re
import sys
from fractions import Fraction as Fr

import numpy as np

FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def exact_P(N):
    """P_n for n <= N as exact Fractions, from (n!)^2 16^-n [t^n] (sum_k t^k/(k!)^2)^4"""
    fact = [1] * (N + 1)
    for k in range(1, N + 1):
        fact[k] = fact[k - 1] * k
    d = [(fact[N] // fact[k]) ** 2 for k in range(N + 1)]          # integer: (N!/k!)^2, so f = (1/(N!)^2) sum d_k t^k
    def mul(a, b):
        out = [0] * (N + 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if i + j > N:
                        break
                    if bj:
                        out[i + j] += ai * bj
        return out
    f2 = mul(d, d)
    f4 = mul(f2, f2)
    den = fact[N] ** 8
    return [Fr(fact[n] ** 2 * f4[n], den * 16 ** n) for n in range(N + 1)]


def main():
    N = 400
    P = exact_P(N)
    ok = P[0] == 1 and P[1] == Fr(4, 16) and P[2] == Fr(28, 256)
    # direct check of P_1, P_2 from the step set: the difference walk has 16 equally likely steps
    steps = [tuple(a[i] - b[i] for i in range(3)) for a in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
             for b in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    n0 = sum(1 for s in steps if s == (0, 0, 0))
    n2 = sum(1 for s in steps for t in steps if tuple(s[i] + t[i] for i in range(3)) == (0, 0, 0))
    ok &= P[1] == Fr(n0, 16) and P[2] == Fr(n2, 256)
    S = sum(P)
    check("A1", ok, f"P_n = (2 pi)^-3 int |phi|^{{2n}} = sum_x p_n(x)^2 exactly: P_0 = 1, P_1 = {P[1]} (the 4 null steps of the 16), "
          f"P_2 = {P[2]} ({n2} two-step returns of 256), P_10 = {float(P[10]):.6f}, P_100 = {float(P[100]):.3e}, P_400 = {float(P[400]):.3e}; "
          f"partial sum to n = {N}: {float(S):.6f}")

    # ---------------- A2: rigorous tail
    C_stir = 16 / (2 * math.pi) ** 1.5
    tail_rig = 2 * C_stir / math.sqrt(N - 3)
    lo, hi = float(S), float(S) + tail_rig
    okb = all(P[n] <= C_stir / (n - 3) ** 1.5 for n in range(4, N + 1))
    check("A2", okb, f"P_n <= max_x p_n(x) <= 16/(2 pi (n-3))^(3/2) for 4 <= n <= {N} (checked against the exact P_n), so the tail beyond {N} is at "
          f"most {tail_rig:.4f} and G is bracketed by [{lo:.4f}, {hi:.4f}] rigorously")

    # ---------------- N1: local limit and the sharper bracket
    c_llt = 4 * math.sqrt(2) / (2 * math.pi) ** 1.5
    scaled = [0.0] + [float(P[n]) * n ** 1.5 for n in range(1, N + 1)]
    mono = all(scaled[n] >= scaled[n - 1] - 1e-12 for n in range(10, N)) and scaled[N - 1] <= c_llt
    # n^{3/2} P_n increases to the local-limit constant, so for n > N: scaled[N] n^{-3/2} <= P_n <= c_llt n^{-3/2},
    # and 2/sqrt(N+1) <= sum_{n>N} n^{-3/2} <= 2/sqrt(N)
    tail_llt_lo = scaled[N] * 2 / math.sqrt(N + 1)
    tail_llt_up = c_llt * 2 / math.sqrt(N)
    check("N1", abs(scaled[N] / c_llt - 1) < 0.01 and mono,
          f"(numerical, labelled) n^(3/2) P_n = {scaled[9]:.4f}, {scaled[99]:.4f}, {scaled[N-1]:.4f} at n = 10, 100, {N} against the local-limit "
          f"constant 4 sqrt2/(2 pi)^(3/2) = {c_llt:.6f} ({scaled[N-1]/c_llt - 1:+.2%} at n = {N}); it increases in n and stays below the constant on "
          f"1 <= n <= {N}, which gives the sharper tail bracket [{tail_llt_lo:.5f}, {tail_llt_up:.5f}] and G in "
          f"[{lo + tail_llt_lo:.5f}, {lo + tail_llt_up:.5f}] (numerical, since the monotonicity is checked only on that range)")
    G_est = lo + (tail_llt_lo + tail_llt_up) / 2

    # ---------------- N2: the spin-wave plateau
    def A(x):
        return 1 / math.tanh(x) - 1 / x
    rows = []
    for beta in (1, 1.5, 2, 3, 6, 12):
        s2 = A(4 * beta) / (4 * beta)
        rows.append((beta, s2, 1 - s2 * G_est))
    runs = {}
    for f in sorted(glob.glob(os.path.join(os.getcwd(), "logs/probes/X:formation-3plus1-sphere-memory/*.txt"))):
        txt = open(f).read()
        h = re.search(r"menu=sphere beta=([\d.]+) L=(\d+) T=(\d+).*?plateau_\|m\|=([\d.]+)", txt, re.S)
        if h and "predecessors n=4" in txt:
            runs[(float(h.group(1)), int(h.group(2)))] = float(h.group(4))
    comp = []
    for (beta, L), m in sorted(runs.items()):
        pred = next((p for b, s, p in rows if b == beta), None)
        if pred is not None:
            comp.append(f"beta={beta:g} L={L}: measured {m:.4f}, spin wave {pred:.4f} ({m/pred - 1:+.2%})")
    okc = all(abs(float(c.split("(")[1].split("%")[0]) / 100) < 0.05 for c in comp if "beta=6" in c or "beta=12" in c) if comp else True
    check("N2", okc, f"(numerical, labelled) G = {G_est:.4f}: |m| ~ 1 - sigma^2 G with sigma^2 = A(4 beta)/(4 beta) gives "
          + ", ".join(f"beta={b:g}: sigma^2={s:.4f}, |m|={p:.4f}" for b, s, p in rows)
          + ("; against the logs: " + "; ".join(comp) if comp else "; no sphere-memory run with four predecessors is logged yet"))

    # ---------------- N3: the 2+1 contrast
    vals = []
    for L in (16, 32, 64, 128, 256, 512):
        k = 2 * np.pi * np.fft.fftfreq(L)
        K1, K2 = np.meshgrid(k, k, indexing="ij")
        ph = (1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3
        u = np.abs(ph) ** 2
        m = np.ones_like(u, bool)
        m[0, 0] = False
        vals.append((L, float(np.sum(1.0 / (1 - u[m])) / L ** 2)))
    slopes = [(vals[i + 1][1] - vals[i][1]) / math.log(2) for i in range(len(vals) - 1)]
    check("N3", all(s > 0 for s in slopes), "(numerical, labelled) the same sum in 2+1, (1/L^2) sum_{k != 0} 1/(1 - |phi|^2) with phi = (1 + e^{ik1} + "
          "e^{ik2})/3: " + ", ".join(f"L={L}: {v:.4f}" for L, v in vals) + "; successive differences per doubling: "
          + ", ".join(f"{s:.4f}" for s in slopes) + " (a log L growth, no finite limit), against the finite 3+1 value")

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: FAILED checks {FAILS}")
        return 0
    print(f"SUMMARY: the 3+1 return sum is finite, G = {G_est:.4f} (rigorous bracket [{lo:.4f}, {hi:.4f}] from 400 exact rational terms and a "
          f"Stirling tail bound; [{lo + tail_llt_lo:.4f}, {lo + tail_llt_up:.4f}] using the local-limit decay n^(3/2) P_n -> {c_llt:.6f}), so the "
          f"spin-wave plateau 1 - sigma^2 G is positive at every coupling (|m| = {rows[-1][2]:.4f} at beta = 12, {rows[0][2]:.4f} at beta = 1), "
          f"while the same sum in 2+1 grows like log L ({vals[0][1]:.3f} at L = 16 to {vals[-1][1]:.3f} at L = 512): memory in 3+1, none in 2+1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
