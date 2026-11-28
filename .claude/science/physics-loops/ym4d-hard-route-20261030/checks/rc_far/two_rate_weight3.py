#!/usr/bin/env python3
"""Third registration, item rc-far. Written before running. two_rate_weight.py and two_rate_weight2.py read FAIL and stay on record.

Run 2, Part A settled T3: the slope of a(n) is 0.99, 0.97, 0.93 at L = 3, 5, 7 on n = 5, 6, 7, the rate 1 of the registered tail of E, so the first run's T3
was saturation at the gap scale. Run 2, Part B failed its vacuity control: the far part did not slow M_t, so B1 proved little. Adding anything positive to the
far block of M_1 keeps M_1's large energy on smooth fields, so no convex combination with weight on M_1 can be slow. This run uses t = 1, allowed by
Lemma W, and builds a far block that is slow by construction.

In blocks (inner, far), inner := free coordinates of boxes in Q_n(0), M_1 = [[a, b], [b^T, c]]. Put B := gamma_0 + X_0 on the far coordinates, X_0 the graph
Laplacian of the earlier runs restricted to far coordinates, gamma_0 := 0.02, and c' := b^T a^-1 b + B. M_2 := [[a, b], [b^T, c']], SPD by Schur, equal to
M_1 on the inner block and on the coupling. The far block of M_2^-1 is B^-1, whose rate is about sqrt(gamma_0) L per box at L = 3 ... ; so M_2 is genuinely slow outside
Q_n, far more slowly than the fast rate. M_t := M_2 (t = 1). rho = 0.8, rho_c = 0.05, R = n + 1. L = 3, 5 at nc = 10, n = 1..4; L = 7 at nc = 8, n = 1..3.

PRE-STATED criteria.
 C1. N_2(nmax) / N_2(1) <= 4 at each L, N_2 as before.
 C2. Control: at L = 5 and at L = 7, N_s(1) / N_2(1) >= 5, N_s the single-rate weight. So the two-rate weight is doing real work where it is tested.
 C3. a(n) := max over i, j in box 0 of |A_2(i, j) - A_1(i, j)|, slope of -log a(n) over all n used: slope >= 0.5 at each L, and slope at L = 7 >= 0.5 slope at L = 3.
FAIL if C1, C2 or C3 fails. Limits: abelian, trivial background, d = 2, one level, Gaussian, an artificial far block. This checks an elementary inequality only. RSS guard 2 GB.
"""
import importlib.util
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("w2", HERE / "two_rate_weight2.py")
w2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w2)


def run(L, nc, ns, rho, rho_c, gamma_0):
    s = w2.cr.Setup(2, L, nc)
    M1s, free = w2.chart_sparse(s)
    X0 = w2.graph_laplacian(s, free)
    M1 = M1s.toarray()
    del M1s
    w2.guard()
    d0 = w2.box_distance(s, free)
    A1 = np.linalg.inv(M1)
    A1 = 0.5 * (A1 + A1.T)
    box0 = np.nonzero(d0 == 0)[0]
    rows = {}
    for n in ns:
        inner = np.nonzero(d0 <= n)[0]
        far = np.nonzero(d0 > n)[0]
        a = M1[np.ix_(inner, inner)]
        b = M1[np.ix_(inner, far)]
        B = X0[far][:, far].toarray() + gamma_0 * np.eye(len(far))
        cprime = b.T @ np.linalg.solve(a, b) + B
        M2 = M1.copy()
        M2[np.ix_(far, far)] = cprime
        M2 = 0.5 * (M2 + M2.T)
        gap = float(np.linalg.eigvalsh(M2)[0])
        A2 = np.linalg.inv(M2)
        A2 = 0.5 * (A2 + A2.T)
        w2.guard()
        R = n + 1
        f = rho * np.minimum(d0, R) + rho_c * np.maximum(d0 - R, 0.0)
        g = rho * d0
        N2 = w2.opnorm((np.exp(f)[:, None] * A2) * np.exp(-f)[None, :])
        Ns = w2.opnorm((np.exp(g)[:, None] * A2) * np.exp(-g)[None, :])
        an = float(np.abs((A2 - A1)[np.ix_(box0, box0)]).max())
        rows[n] = dict(N2=N2, Ns=Ns, a=an, gap=gap)
        print(f"L={L} nc={nc} n={n}: gap(M_2)={gap:.4e} N_2={N2:.3f} N_s={Ns:.3f} a(n)={an:.3e} rss={w2.rss_gb():.2f}GB", flush=True)
    return rows


def main():
    ok = True
    slopes = {}
    for L, nc, ns in ((3, 10, (1, 2, 3, 4)), (5, 10, (1, 2, 3, 4)), (7, 8, (1, 2, 3))):
        rows = run(L, nc, ns, 0.8, 0.05, 0.02)
        nmax = ns[-1]
        r2 = rows[nmax]["N2"] / rows[1]["N2"]
        good1 = r2 <= 4
        ctrl = rows[1]["Ns"] / rows[1]["N2"]
        good2 = ctrl >= 5 if L in (5, 7) else True
        sl = float(np.polyfit(np.array(ns, dtype=float), -np.log([rows[n]["a"] for n in ns]), 1)[0])
        slopes[L] = sl
        good3 = sl >= 0.5
        ok = ok and good1 and good2 and good3
        print(f"L={L}: C1 N_2 ratio {r2:.3f}: {good1}; C2 N_s(1)/N_2(1) {ctrl:.3f}: {good2}; C3 slope {sl:.3f}: {good3}", flush=True)
    good = slopes[7] >= 0.5 * slopes[3]
    ok = ok and good
    print(f"C3b slope(7)/slope(3) = {slopes[7] / slopes[3]:.3f}: {good}", flush=True)
    print("PASS" if ok else "FAIL", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
