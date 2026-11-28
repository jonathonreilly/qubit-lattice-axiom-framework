#!/usr/bin/env python3
"""Lower bound on the rank of the contracted vertex on an open box, against engineered gauges.

Setting: b = b0 + d X on the links of a box of side L in Z^4, with b0 generic. B[b](a, a') = VV(a, a', b), VV := sum_p phi_p ^ m_p ^ n_p.
For a plane pi = (mu, nu), a sign s, the grading tau = e_mu + s e_nu on link midpoints has top part C_+ := the entries of B of shift exactly 1 (with s = +1, also the mirrored with s = -1).
Hand derivation (Text 3.13): rank B >= rank C_+, and C_+ is a direct sum of 2 x 2 blocks on the links of directions mu, nu, one per plaquette of pi, and of hopping matrices on the other two directions.
So rank C_+ >= LB := sum_(p in pi) (2 - [c_a(p) = 0] - [c_b(p) = 0]) + #{p in (h_1, rho_1) : mean of h_1 links != 0} + #{p in (h_2, rho_2) : mean of h_2 links != 0},
with (c_a, c_b) = two opposite corner sums, the pair (2, 4) for s = +1, (1, 3) for s = -1, rho_1, rho_2 the other two directions, h_1, h_2 in {mu, nu}.
Also: with the six pair functionals on each plaquette (four corner sums, two parallel differences), Ob := #zero corner sums + 2 #zero parallel differences <= 9 R, R the rank on link fields of the zero set, when no plaquette flux vanishes.

PRE-REGISTERED CRITERIA (written before the first run).
 B1: rank B >= rank C_+ >= LB for all 48 choices, in every engineered gauge. Any failure means the derivation is wrong; stop and find out.
 B2: Ob <= 9 R, and R <= V - 1, in every gauge with non-vanishing flux.
 B3: average of the loss over the 48 choices equals Ob / 12 up to boundary count; report the smallest and largest loss.
 B4: rank B itself, reported against 2 (V - 1).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import resource
import sys
import time

import numpy as np


def check_rss(limit_gb=2.0):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3
    if r > limit_gb:
        raise MemoryError(f"rss {r:.2f} GB")
    return r


class Box:
    def __init__(self, L, d=4):
        self.L, self.d = L, d
        self.sites = list(itertools.product(range(L), repeat=d))
        self.sidx = {x: i for i, x in enumerate(self.sites)}
        self.links = []
        for x in self.sites:
            for mu in range(d):
                y = list(x)
                y[mu] += 1
                if y[mu] < L:
                    self.links.append((x, mu))
        self.lidx = {l: i for i, l in enumerate(self.links)}
        self.W = len(self.links)
        self.V = len(self.sites)
        self.plaq = []  # (x, mu, nu, A, Bb, C, E)
        for x in self.sites:
            for mu in range(d):
                for nu in range(mu + 1, d):
                    if x[mu] + 1 < L and x[nu] + 1 < L:
                        xm = list(x)
                        xm[mu] += 1
                        xn = list(x)
                        xn[nu] += 1
                        self.plaq.append((x, mu, nu, self.lidx[(x, mu)], self.lidx[(tuple(xm), nu)], self.lidx[(tuple(xn), mu)], self.lidx[(x, nu)]))
        self.P = np.array([[p[3], p[4], p[5], p[6]] for p in self.plaq], dtype=int)
        self.pmu = np.array([p[1] for p in self.plaq])
        self.pnu = np.array([p[2] for p in self.plaq])
        self.mid = np.zeros((self.W, d))
        for i, (x, mu) in enumerate(self.links):
            self.mid[i] = np.array(x, dtype=float)
            self.mid[i, mu] += 0.5
        self.D0 = np.zeros((self.W, self.V))
        for i, (x, mu) in enumerate(self.links):
            y = list(x)
            y[mu] += 1
            self.D0[i, self.sidx[x]] = -1.0
            self.D0[i, self.sidx[tuple(y)]] = 1.0

    def steps(self, b):
        P = self.P
        return b[P[:, 0]], b[P[:, 1]], -b[P[:, 2]], -b[P[:, 3]]

    def pair_values(self, b):
        s1, s2, s3, s4 = self.steps(b)
        return dict(c1=s1 + s2, c2=s2 + s3, c3=s3 + s4, c4=s4 + s1, m=s1 - s3, n=s2 - s4, f=s1 + s2 + s3 + s4)

    def Bmat(self, b):
        P = self.P
        M = np.zeros((self.W, self.W))
        s1, s2, s3, s4 = self.steps(b)
        f = s1 + s2 + s3 + s4
        bm = 0.5 * (s1 - s3)
        bn = 0.5 * (s2 - s4)
        ph = np.array([1.0, 1.0, -1.0, -1.0])
        me = np.array([0.5, 0.0, 0.5, 0.0])
        ne = np.array([0.0, 0.5, 0.0, 0.5])
        W1 = np.outer(me, ne) - np.outer(ne, me)
        W2 = np.outer(ne, ph) - np.outer(ph, ne)
        W3 = np.outer(ph, me) - np.outer(me, ph)
        for i in range(P.shape[0]):
            M[np.ix_(P[i], P[i])] += f[i] * W1 + bm[i] * W2 + bn[i] * W3
        return M

    def functional_rows(self, which):
        """Rows on link space for a list of (plaquette index, name)."""
        R = np.zeros((len(which), self.W))
        for r, (i, name) in enumerate(which):
            a, b, c, e = self.P[i]
            st = {1: (a, 1.0), 2: (b, 1.0), 3: (c, -1.0), 4: (e, -1.0)}
            pairs = {"c1": (1, 2, 1), "c2": (2, 3, 1), "c3": (3, 4, 1), "c4": (4, 1, 1), "m": (1, 3, -1), "n": (2, 4, -1)}
            u, v, sg = pairs[name]
            R[r, st[u][0]] += st[u][1]
            R[r, st[v][0]] += sg * st[v][1]
        return R


def rank(M, tol=1e-9):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(s[0], 1e-300)))


def analyse(box, b, label, tol=1e-9):
    t0 = time.time()
    pv = box.pair_values(b)
    scale = np.abs(b).max()
    zero = {k: np.abs(pv[k]) < tol * scale for k in ("c1", "c2", "c3", "c4", "m", "n")}
    zf = int(np.sum(np.abs(pv["f"]) < tol * scale))
    # zero set rank
    which = [(i, k) for k in zero for i in np.nonzero(zero[k])[0]]
    R = rank(box.functional_rows(which)) if which else 0
    nZ = sum(int(np.sum(zero[k])) for k in ("c1", "c2", "c3", "c4"))
    nA = int(np.sum(zero["m"])) + int(np.sum(zero["n"]))
    Ob = nZ + 2 * nA
    B = box.Bmat(b)
    rB = rank(B)
    best = (-1, None)
    ok = True
    losses = []
    n_pl = {}
    d = box.d
    for mu, nu in itertools.combinations(range(d), 2):
        others = [r for r in range(d) if r not in (mu, nu)]
        inpl = (box.pmu == mu) & (box.pnu == nu)
        for s in (1, -1):
            a, bb = ("c2", "c4") if s == 1 else ("c1", "c3")
            base = int(np.sum(2 - zero[a][inpl].astype(int) - zero[bb][inpl].astype(int)))
            tau = np.zeros(d)
            tau[mu] = 1
            tau[nu] = s
            h = box.mid @ tau
            mask = np.abs(np.subtract.outer(h, h).T - 1.0) < 1e-9  # column minus row = 1
            Cp = np.where(mask, B, 0.0)
            rC = rank(Cp)
            # hopping lower bound along h in {mu, nu}
            for h1, h2 in itertools.product((mu, nu), repeat=2):
                cnt = 0
                loss = int(np.sum(zero[a][inpl])) + int(np.sum(zero[bb][inpl]))
                for rho, hh in zip(others, (h1, h2)):
                    lo, hi = min(hh, rho), max(hh, rho)
                    sel = (box.pmu == lo) & (box.pnu == hi)
                    name = "m" if hh == lo else "n"
                    cnt += int(np.sum(~zero[name][sel]))
                    loss += int(np.sum(zero[name][sel]))
                LB = base + cnt
                losses.append(loss)
                if not (rB >= rC >= LB):
                    ok = False
                    print(f"   FAIL at plane {mu,nu} s={s} h={h1,h2}: rB={rB} rC={rC} LB={LB}")
                if LB > best[0]:
                    best = (LB, (mu, nu, s, h1, h2, rC))
    print(f"{label}: V={box.V} W={box.W} bound 2(V-1)={2*(box.V-1)} | zero flux {zf} | R={R} |Z|={nZ} |A|={nA} Ob={Ob} (9R={9*R}) | loss min/mean/max {min(losses)}/{np.mean(losses):.1f}/{max(losses)} Ob/12={Ob/12:.1f} | best LB={best[0]} rankC+={best[1][5]} rank B={rB} | B1 {'PASS' if ok else 'FAIL'} B2 {'PASS' if (Ob<=9*R and R<=box.V-1) else 'FAIL'} t={time.time()-t0:.1f}s rss={check_rss():.2f}GB", flush=True)
    return ok


def solve_gauge(box, b0, which):
    """X with the functionals in `which` vanishing on b0 + d X, in least squares; returns b and the residual."""
    R = box.functional_rows(which)
    A = R @ box.D0
    rhs = -R @ b0
    X, *_ = np.linalg.lstsq(A, rhs, rcond=None)
    b = b0 + box.D0 @ X
    res = np.abs(R @ b).max() if len(which) else 0.0
    return b, res


def consistent_subset(box, b0, cand, rng):
    """Greedy: add functionals from cand while the system on X stays consistent for this generic b0. With generic b0 this keeps span intersect Z = 0."""
    keep = []
    R_list = []
    # work with rows on W: consistency means rank [R D0 , R b0] = rank [R D0]
    rows = box.functional_rows(cand)
    A = rows @ box.D0
    y = rows @ b0
    # incremental orthogonal basis of the augmented rows
    Q = []
    Q2 = []
    for i in range(len(cand)):
        v = A[i].copy()
        w = y[i]
        for q, qy in zip(Q, Q2):
            c = q @ v
            v = v - c * q
            w = w - c * qy
        n = np.linalg.norm(v)
        if n > 1e-9:
            Q.append(v / n)
            Q2.append(w / n)
            keep.append(cand[i])
        elif abs(w) < 1e-9:
            keep.append(cand[i])  # dependent and consistent
        # else inconsistent, drop
    return keep


def main():
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    rng = np.random.default_rng(11)
    box = Box(L)
    b0 = rng.normal(size=box.W)
    allok = True
    allok &= analyse(box, b0, "generic b")
    # axial in direction 0: all direction 0 links vanish
    cand = [(i, "m") for i in range(len(box.plaq)) if box.pmu[i] == 0] + [(i, "n") for i in range(len(box.plaq)) if box.pnu[i] == 0]
    keep = consistent_subset(box, b0, cand, rng)
    b, res = solve_gauge(box, b0, keep)
    allok &= analyse(box, b, f"zero means of direction 0, {len(keep)} kept of {len(cand)}, residual {res:.0e}")
    # light cone in plane (0, 1): corner c4 = 0 on all its plaquettes
    cand = [(i, "c4") for i in range(len(box.plaq)) if box.pmu[i] == 0 and box.pnu[i] == 1]
    keep = consistent_subset(box, b0, cand, rng)
    b, res = solve_gauge(box, b0, keep)
    allok &= analyse(box, b, f"corner c4 in plane (0, 1), {len(keep)} kept of {len(cand)}, residual {res:.0e}")
    # piecewise: each of four regions zero means of its own direction
    cand = []
    for i, p in enumerate(box.plaq):
        x = p[0]
        reg = (x[0] * 2 // L) * 2 + (x[1] * 2 // L)
        if box.pmu[i] == reg:
            cand.append((i, "m"))
        if box.pnu[i] == reg:
            cand.append((i, "n"))
    keep = consistent_subset(box, b0, cand, rng)
    b, res = solve_gauge(box, b0, keep)
    allok &= analyse(box, b, f"piecewise zero means, {len(keep)} kept of {len(cand)}, residual {res:.0e}")
    # random pair functionals, kept while consistent: this is the greedy maximal zero set
    names = ["c1", "c2", "c3", "c4", "m", "n"]
    for trial in range(2):
        cand = [(i, k) for i in range(len(box.plaq)) for k in names]
        rng.shuffle(cand)
        cand = [(int(i), str(k)) for i, k in cand]
        keep = consistent_subset(box, b0, cand, rng)
        b, res = solve_gauge(box, b0, keep)
        allok &= analyse(box, b, f"greedy random zero set, {len(keep)} kept, residual {res:.0e}")
    # greedy favouring means, then corners
    cand = [(i, k) for k in ("m", "n") for i in rng.permutation(len(box.plaq))] + [(i, k) for k in ("c1", "c2", "c3", "c4") for i in rng.permutation(len(box.plaq))]
    cand = [(int(i), str(k)) for i, k in cand]
    keep = consistent_subset(box, b0, cand, rng)
    b, res = solve_gauge(box, b0, keep)
    allok &= analyse(box, b, f"greedy means first, {len(keep)} kept, residual {res:.0e}")
    print("ALL PASS" if allok else "SOME FAIL")


if __name__ == "__main__":
    main()
