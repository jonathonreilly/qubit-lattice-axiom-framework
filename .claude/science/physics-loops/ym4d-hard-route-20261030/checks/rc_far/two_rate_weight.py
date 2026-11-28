#!/usr/bin/env python3
"""Kill test of the two-rate weight (Lemma W) on the real chart matrix. Item rc-far.

Written before running. Abelian, trivial background, d = 2, torus N = L nc, odd L, chart of
checks/hard-core--mapped_chart_rate.py: M_1 := T^T K T on free variables, the Hessian whose inverse has the fast rate
(Theorem F). This script reads that file's Setup and designated() and changes neither.

Lemma W claims: let M_2 agree with M_1 on Q_n(0) up to a tail, be arbitrary outside, and let M_t := (1 - t) M_1 + t M_2.
M_t may have only a slow Combes-Thomas rate on the far region, yet the weight
    f(i) := rho min(d(i), R) + rho_c (d(i) - R)_+,    R := n + 1 = dist(box 0, complement of Q_n),
has ||e^f A_t e^-f|| <= C(L), uniformly in n, for rho below the fast rate. Also the far effect on the local inverse decays at
a rate free of L.

Far part. X_0 := graph Laplacian on the free variables (unit weights, adjacency: bonds sharing a site), so it hops the low modes
of M_1 between boxes. S := diag(s_i), s_i := exp(-0.5 r(i)), r(i) := box distance to the complement of Q_n, 0 outside. M_2 :=
M_1 + S X_0 S. So E := M_2 - M_1 is a tail of rate about 1 per box in Q_n, and order one outside.

Registered parameters: rho = 0.5, rho_c = 0.02, t = 1/2, n = 1, 2, 3, 4, nc = 10, L = 3, 5, 7.
PRE-STATED criteria.
 T1. For each L: N_2(4) / N_2(1) <= 4, where N_2(n) := ||e^f A_t e^-f||_(2 -> 2).
 T2. For each L, n: for j in box 0, all i: |A_t(i, j) - A_1(i, j)| <= (1 / gap(M_t)) ||E A_1 e_j||_2 (1 + 1e-9). (The resolvent step.)
 T3. a(n) := max over i, j in box 0 of |A_t(i, j) - A_1(i, j)|, rate := least-squares slope of -log a(n) on n = 1..4.
     rate >= 0.5 at each L, and rate(7) >= 0.5 rate(3).
 C1. Control, reported, no criterion: N_s(n) := the same norm for the single-rate weight rho d(i). If N_s grows with n much faster than
     N_2, the truncation is doing real work; if not, this far part did not produce a slow region and T1 tested less than intended.
FAIL if T1, T2 or T3 fails. Limits: abelian, trivial background, d = 2, one level, one family of far parts. A pass supports
an elementary inequality and says nothing on the non-Gaussian law. RSS guard 2 GB.
"""
import importlib.util
import pathlib
import resource
import sys

import numpy as np
import scipy.sparse as sp

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("chart_rate", HERE.parent / "hard-core--mapped_chart_rate.py")
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2.0:
        raise SystemExit("RSS above 2 GB")


def chart(s):
    D = s.curl()
    K = (D.T @ D).toarray()
    used, Q = cr.designated(s)
    Qd = Q.toarray()
    tree = set(s.tree_bonds().tolist())
    des = np.array([used[r] for r in range(Qd.shape[0])])
    dset = set(des.tolist())
    free = np.array([b for b in range(s.nb) if b not in tree and b not in dset])
    Tdes = -np.linalg.solve(Qd[:, des], Qd[:, free])
    T = np.zeros((s.nb, len(free)))
    T[free, np.arange(len(free))] = 1.0
    T[des, :] = Tdes
    M = T.T @ K @ T
    return 0.5 * (M + M.T), free


def adjacency(s, free):
    """Graph Laplacian on free variables: bonds sharing a site."""
    nsites = s.nsites
    d = s.d
    pos = -np.ones(s.nb, dtype=int)
    pos[free] = np.arange(len(free))
    rows, cols = [], []
    ends = {}
    for mu in range(d):
        e = np.eye(d, dtype=int)[mu]
        coords = np.array(np.unravel_index(np.arange(nsites), s.shape)).T
        for k in range(nsites):
            b = k + mu * nsites
            if pos[b] < 0:
                continue
            a0 = k
            a1 = s.site(coords[k] + e)
            ends.setdefault(a0, []).append(pos[b])
            ends.setdefault(a1, []).append(pos[b])
    for lst in ends.values():
        for x in lst:
            for y in lst:
                if x != y:
                    rows.append(x)
                    cols.append(y)
    A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(free), len(free)))
    A.data[:] = 1.0
    return (sp.diags(np.asarray(A.sum(axis=1)).ravel()) - A).toarray()


def box_distance(s, free):
    bb = s.box_of_bond()[free]
    db = np.minimum(bb, s.nc - bb)
    return db.max(axis=1).astype(float)


def opnorm(B, iters=300):
    rng = np.random.default_rng(0)
    v = rng.standard_normal(B.shape[1])
    v /= np.linalg.norm(v)
    last = 0.0
    for _ in range(iters):
        w = B @ v
        u = B.T @ w
        nu = np.linalg.norm(u)
        v = u / nu
        val = np.sqrt(nu)
        if abs(val - last) < 1e-7 * val:
            break
        last = val
    return float(val)


def run(L, nc, rho, rho_c, t, ns):
    s = cr.Setup(2, L, nc)
    M1, free = chart(s)
    guard()
    d0 = box_distance(s, free)
    X0 = adjacency(s, free)
    guard()
    A1 = np.linalg.inv(M1)
    A1 = 0.5 * (A1 + A1.T)
    in_box0 = np.nonzero(d0 == 0)[0]
    gap1 = float(np.linalg.eigvalsh(M1)[0])
    rows = {}
    for n in ns:
        r = np.maximum(n + 1 - d0, 0.0)
        sv = np.exp(-0.5 * r)
        E2 = (sv[:, None] * X0) * sv[None, :]
        E = t * E2
        Mt = M1 + E
        Mt = 0.5 * (Mt + Mt.T)
        gap_t = float(np.linalg.eigvalsh(Mt)[0])
        At = np.linalg.inv(Mt)
        At = 0.5 * (At + At.T)
        guard()
        R = n + 1
        f = rho * np.minimum(d0, R) + rho_c * np.maximum(d0 - R, 0.0)
        g = rho * d0
        N2 = opnorm((np.exp(f)[:, None] * At) * np.exp(-f)[None, :])
        Ns = opnorm((np.exp(g)[:, None] * At) * np.exp(-g)[None, :])
        N1 = opnorm((np.exp(g)[:, None] * A1) * np.exp(-g)[None, :])
        diff = At - A1
        ok2 = True
        worst = 0.0
        EA = E @ A1[:, in_box0]
        for col, j in enumerate(in_box0):
            bound = np.linalg.norm(EA[:, col]) / gap_t
            lhs = np.abs(diff[:, j]).max()
            worst = max(worst, lhs / bound if bound > 0 else 0.0)
            ok2 = ok2 and lhs <= bound * (1 + 1e-9)
        a = float(np.abs(diff[np.ix_(in_box0, in_box0)]).max())
        rows[n] = dict(N2=N2, Ns=Ns, N1=N1, a=a, ok2=ok2, worst=worst, gap_t=gap_t)
        print(f"L={L} n={n}: gap(M_1)={gap1:.4e} gap(M_t)={gap_t:.4e} N_2={N2:.3f} N_s={Ns:.3f} N_1={N1:.3f} a(n)={a:.3e} T2 ratio={worst:.3f} rss={rss_gb():.2f}GB", flush=True)
    return rows


def main():
    rho, rho_c, t, ns, nc = 0.5, 0.02, 0.5, (1, 2, 3, 4), 10
    ok = True
    rates = {}
    for L in (3, 5, 7):
        rows = run(L, nc, rho, rho_c, t, ns)
        ratio = rows[4]["N2"] / rows[1]["N2"]
        good1 = ratio <= 4
        good2 = all(rows[n]["ok2"] for n in ns)
        x = np.array(ns, dtype=float)
        y = -np.log([rows[n]["a"] for n in ns])
        rate = float(np.polyfit(x, y, 1)[0])
        rates[L] = rate
        good3 = rate >= 0.5
        ok = ok and good1 and good2 and good3
        ctrl = rows[4]["Ns"] / rows[1]["Ns"]
        print(f"L={L}: T1 N_2(4)/N_2(1)={ratio:.3f}: {good1}; T2: {good2}; T3 rate={rate:.3f}: {good3}; C1 N_s(4)/N_s(1)={ctrl:.3f}", flush=True)
    good = rates[7] >= 0.5 * rates[3]
    ok = ok and good
    print(f"T3b rate(7)/rate(3) = {rates[7] / rates[3]:.3f}: {good}", flush=True)
    print("PASS" if ok else "FAIL", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
