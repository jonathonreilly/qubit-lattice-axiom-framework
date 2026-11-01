#!/usr/bin/env python3
"""Does the inf-sup of the nested constraint system lose with depth? (kill criterion C)

Registered before the first run (2026-11-01, mac-mini-worker, item joint-induction).

Why. flat2d.py Part A passed A1, but lam fell .381, .308, .238 with no sign of saturating, and
there the period along the wall was tied to the depth. A pass with an unexplained trend is not
evidence. This run separates depth from the period.

Model. d = 2 tents as in flat2d.py. One sheet at x = 0. Levels l0, ..., l0 + m - 1 carry layers
Sigma_l = [-3 s_(l+1), 3 s_(l+1)) (whole level-(l+1) blocks; clearance 2 level-(l+2) blocks);
level l0 + m is the top and its rows run over all x in a window. A level-l row is kept only if it
has a free child, the constraint set of Theorem F-D: rows with both x-blocks inside Sigma_(l-1)
are dropped, so G is non-singular. Rows are unit vectors. G = C C^T is assembled from exact 1D
tent overlaps and block-diagonalised in Bloch momentum along the wall, of period P = s_(l0+m).

lam(m) := smallest eigenvalue over the scanned Bloch momenta. lam^(1/2) is the inf-sup constant in
the norm with unit rows, the analogue of Lam in Theorem F-D.

Criteria, fixed now:
 G1 PASS if lam(m + 1) >= 0.85 lam(m) for m = 2, 3, 4 at l0 = 2 (depth saturates).
 G2 PASS if lam(m) >= 0.1 at every m, l0 scanned.
 G3 PASS if lam at fixed m moves by at most 15 percent from l0 = 2 to l0 = 3 (scale invariance).
 Control: with the clearance removed, Sigma_l = [-3 s_l, 3 s_l) for every l, so that the layers
 chain: report lam, no pass criterion, to see that the test can respond to the geometry.
G1 FAILING is a depth-growing coercivity loss in this model, and it would be reported as such.
Stops itself above 2 GB RSS. A run can refute; it discharges nothing.
"""
import resource
import sys
import time

import numpy as np

RSS_LIMIT = 2 * 1024 ** 3
L = 3


def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT:
        sys.exit("RSS guard: above 2 GB, stopping")


def tent(s):
    a = np.arange(2 * s - 1)
    return (s - np.abs(a - (s - 1))) / s


class Overlap:
    """c(l, m, delta) := sum_i t_l(i) t_m(i - delta), for l, m in the level set."""

    def __init__(self, levels):
        self.t = {l: tent(L ** l) for l in levels}
        self.n = {l: float(self.t[l] @ self.t[l]) for l in levels}
        self.tab = {}
        for l in levels:
            for m in levels:
                c = np.correlate(self.t[l], self.t[m], mode="full")
                # index k of c corresponds to delta = k - (len(t_m) - 1)
                self.tab[(l, m)] = (c, self.t[m].size - 1)

    def get(self, l, m, delta):
        c, off = self.tab[(l, m)]
        k = np.asarray(delta) + off
        out = np.zeros(np.shape(k))
        ok = (k >= 0) & (k < c.size)
        out[ok] = c[k[ok]]
        return out


def rows_for(l0, m, chain=False):
    top = l0 + m
    st = L ** top
    win = 12 * st
    rows = []  # (level, x position of the tent's left end)
    def sig(l):
        if chain:
            return -3 * L ** l, 3 * L ** l
        return -3 * L ** (l + 1), 3 * L ** (l + 1)
    for l in range(l0, top):
        s = L ** l
        lo, hi = sig(l)
        lo = int(np.floor(lo / s)) * s
        hi = int(np.ceil(hi / s)) * s
        for X in range(lo // s, hi // s - 1):
            if l > l0:
                flo, fhi = sig(l - 1)
                if X * s >= flo and (X + 2) * s <= fhi:
                    continue
            rows.append((l, X * s))
    lo, hi = sig(top - 1)
    for X in range(-win // st, win // st):
        if X * st >= lo and (X + 2) * st <= hi:
            continue
        rows.append((top, X * st))
    return rows


def gram(l0, m, kappa, chain=False):
    top = l0 + m
    P = L ** top
    levels = list(range(l0, top + 1))
    ov = Overlap(levels)
    rows = rows_for(l0, m, chain)
    # expand with y offsets a in range(P / s_l)
    lev = []
    xs = []
    ys = []
    for l, x in rows:
        s = L ** l
        n = P // s
        lev.extend([l] * n)
        xs.extend([x] * n)
        ys.extend(list(s * np.arange(n)))
    lev = np.array(lev)
    xs = np.array(xs)
    ys = np.array(ys)
    N = lev.size
    G = np.zeros((N, N), dtype=complex)
    nz = 2  # images in y; tents reach at most 2 P
    for l in levels:
        I = np.where(lev == l)[0]
        for m2 in levels:
            J = np.where(lev == m2)[0]
            if I.size == 0 or J.size == 0:
                continue
            dx = xs[I][:, None] - xs[J][None, :]
            cx = ov.get(l, m2, -dx)
            if not np.any(cx):
                continue
            dy0 = ys[I][:, None] - ys[J][None, :]
            cy = np.zeros(dy0.shape, dtype=complex)
            for z in range(-nz, nz + 1):
                cy += np.exp(1j * kappa * z) * ov.get(l, m2, -(dy0 - z * P))
            G[np.ix_(I, J)] = cx * cy / (ov.n[l] * ov.n[m2])
    return G


def lam(l0, m, chain=False, kappas=(0.0, np.pi / 3, 2 * np.pi / 3, np.pi)):
    best = np.inf
    size = 0
    for k in kappas:
        G = gram(l0, m, k, chain)
        size = G.shape[0]
        G = 0.5 * (G + G.conj().T)
        ev = np.linalg.eigvalsh(G)
        best = min(best, ev[0])
        guard()
    return best, size


def main():
    table = {}
    for l0 in (1, 2, 3):
        for m in (1, 2, 3, 4):
            if (L ** (l0 + m)) // (L ** l0) > 81:
                continue
            t0 = time.time()
            v, size = lam(l0, m)
            table[(l0, m)] = v
            print(f"l0={l0} m={m}: rows per period {size}, lam {v:.5f}, t={time.time() - t0:.0f}s", flush=True)
    for m in (2, 3):
        v, size = lam(2, m, chain=True)
        print(f"control, no clearance: l0=2 m={m}: rows {size}, lam {v:.5f}", flush=True)
    G1 = all(table[(2, m + 1)] >= 0.85 * table[(2, m)] for m in (2, 3) if (2, m + 1) in table)
    G2 = all(v >= 0.1 for v in table.values())
    G3 = all(abs(table[(3, m)] - table[(2, m)]) <= 0.15 * table[(2, m)]
             for m in (1, 2, 3, 4) if (3, m) in table and (2, m) in table)
    print("G1", "PASS" if G1 else "FAIL", "G2", "PASS" if G2 else "FAIL", "G3", "PASS" if G3 else "FAIL", flush=True)
    print("peak RSS bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == "__main__":
    main()
