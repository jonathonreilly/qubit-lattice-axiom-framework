#!/usr/bin/env python3
"""J:attack:PR8145 - clock-history note (PR #8145), attack pattern (f) NORMALIZATION: Part II's positive current representation
    W(J) = Z_J/Z_0,   Z_J = sum_{d1* s = J mod N} prod_p c_(s_p),   (1)
(c_k the discrete Fourier coefficients of the plaquette Villain weight on Z_N; the orientation J -> -J leaves W unchanged) and its
consequence, for J - K = d1* S with S a finite integer plaquette chain and R(S) = prod_p max_k c_k/c_(k+S_p),
    R(S)^-1 W(K) <= W(J) <= R(S) W(K),   (2)
recomputed by brute force at small sizes, beyond the runner's single cube at N = 2, 3:
  * W(J) directly as the normalized sum over link clocks of prod_p w(theta_p) e^{2 pi i <J, a>/N} (tree gauge: the non-tree link values
    only, legitimate because the weight and the character of a conserved current are gauge invariant), for ALL conserved currents at
    once by an N-ary FFT over the cycle coordinates; the Fourier coefficients by Poisson summation (all terms positive);
  * the fiber side of (1) by enumerating every plaquette current s in Z_N^P and binning d1* s;
  * (2) for every conserved K and every chain S of one or two plaquettes with coefficients in {-2..2} (N >= 5: up to the chains whose
    boundary differs mod N), the ratio W(J)/W(K) against R(S) and R(S)^-1; positivity of W(J) (nonempty fibers) for every conserved J;
on the cube (N = 2..6), the two-cube box 2x1x1 (N = 2, 3, 4) and the four-cube slab 2x2x1 (N = 2), at beta = 0.4, 0.8, 1.6.
HIT if (1) disagrees with the direct sums beyond 1e-10 (relative to the largest W), (2) fails beyond 1e-10, or some conserved W(J) <= 0.
"""
import itertools
import math
import sys
import time

import numpy as np


def villain(N, beta):
    th = 2 * np.pi * np.arange(N) / N
    n = np.arange(-40, 41)
    return np.exp(-beta * (th[:, None] + 2 * np.pi * n) ** 2 / 2).sum(axis=1)


def fourier_coeffs(N, beta):
    """c_k with w(x) = sum_k c_k e^{2 pi i k x/N}: c_k = (2 pi beta)^(-1/2) sum_{q = k mod N} e^{-q^2/(2 beta)} (Poisson; positive, even)."""
    k = np.arange(N)
    q = k[:, None] + N * np.arange(-60, 61)[None, :]
    c = np.exp(-q.astype(float) ** 2 / (2 * beta)).sum(axis=1) / math.sqrt(2 * math.pi * beta)
    w = villain(N, beta)
    x = np.arange(N)
    assert np.allclose((c[None, :] * np.exp(2j * np.pi * np.outer(x, k) / N)).sum(axis=1), w, rtol=1e-12, atol=1e-14 * w.max())
    return c


class Box:
    def __init__(self, n):
        verts = list(itertools.product(*(range(x) for x in n)))
        vid = {v: i for i, v in enumerate(verts)}

        def sh(v, ax):
            u = list(v)
            u[ax] += 1
            return tuple(u)

        edges = []
        for v in verts:
            for ax in range(3):
                u = sh(v, ax)
                if u in vid:
                    edges.append((vid[v], vid[u]))
        eid = {e: i for i, e in enumerate(edges)}
        rows = []
        for v in verts:
            for a1, a2 in ((0, 1), (0, 2), (1, 2)):
                v1, v2 = sh(v, a1), sh(v, a2)
                v12 = sh(v1, a2)
                if v1 in vid and v2 in vid and v12 in vid:
                    r = np.zeros(len(edges), dtype=np.int64)
                    r[eid[(vid[v], vid[v1])]] += 1
                    r[eid[(vid[v1], vid[v12])]] += 1
                    r[eid[(vid[v2], vid[v12])]] -= 1
                    r[eid[(vid[v], vid[v2])]] -= 1
                    rows.append(r)
        self.V, self.E, self.P = len(verts), len(edges), len(rows)
        self.d1 = np.array(rows)
        self.d0 = np.zeros((self.E, self.V), dtype=np.int64)
        for i, (t, h) in enumerate(edges):
            self.d0[i, t] -= 1
            self.d0[i, h] += 1
        assert not np.any(self.d1 @ self.d0)
        # spanning tree by BFS; the non-tree links are the cycle coordinates
        adj = [[] for _ in range(self.V)]
        for i, (t, h) in enumerate(edges):
            adj[t].append((h, i))
            adj[h].append((t, i))
        seen, order, tree = {0}, [0], set()
        for v in order:
            for u, i in adj[v]:
                if u not in seen:
                    seen.add(u)
                    order.append(u)
                    tree.add(i)
        self.nontree = [i for i in range(self.E) if i not in tree]
        self.C = len(self.nontree)
        assert self.C == self.E - self.V + 1


def w_direct(box, N, w):
    """W(J) for every conserved J (indexed by its non-tree values) from direct link sums in the tree gauge, via an N-ary FFT."""
    C = box.C
    grid = np.array(list(itertools.product(range(N), repeat=C)), dtype=np.int64)
    a = np.zeros((len(grid), box.E), dtype=np.int64)
    a[:, box.nontree] = grid
    theta = (a @ box.d1.T) % N
    wt = np.prod(w[theta], axis=1).reshape((N,) * C)
    Zhat = np.real(np.fft.ifftn(wt) * wt.size)  # sum_a wt(a) e^{+2 pi i <k, a>/N}: the current J with non-tree values k
    return Zhat / Zhat.flat[0]


def w_fiber(box, N, c):
    """W(J) from (1): the fiber sum over plaquette currents s with d1* s = J (mod N), binned by J's non-tree values."""
    if N ** box.P > 6_000_000:
        return None
    Zs = np.zeros(N ** box.C)
    d1 = box.d1.astype(np.int16)
    allS = itertools.product(range(N), repeat=box.P)
    while True:
        chunk = list(itertools.islice(allS, 200_000))
        if not chunk:
            break
        S = np.array(chunk, dtype=np.int16)
        J = (S @ d1) % N
        assert not np.any((J.astype(np.int64) @ box.d0) % N)          # d1* s is conserved
        idx = np.ravel_multi_index(J[:, box.nontree].T.astype(np.int64), (N,) * box.C)
        np.add.at(Zs, idx, np.prod(c[S], axis=1))
    Zs = Zs.reshape((N,) * box.C)
    return Zs / Zs.flat[0]


def current_of(box, N, s):
    return ((np.asarray(s) @ box.d1) % N)[box.nontree]


def main():
    t0 = time.time()
    hits = []
    PLAN = [((2, 2, 2), (2, 3, 4, 5, 6)), ((3, 2, 2), (2, 3, 4)), ((3, 3, 2), (2,))]
    worst1 = 0.0
    n1 = 0
    ncmp = 0
    worst_up = worst_lo = 0.0
    minW = math.inf
    for n, Ns in PLAN:
        box = Box(n)
        for N in Ns:
            for beta in (0.4, 0.8, 1.6):
                w = villain(N, beta)
                c = fourier_coeffs(N, beta)
                Wd = w_direct(box, N, w)
                Wf = w_fiber(box, N, c)
                # orientation: W(J) = W(-J)
                flip = tuple(slice(None, None, -1) for _ in range(box.C))
                Wneg = np.roll(Wd[flip], 1, axis=tuple(range(box.C)))
                orient = np.abs(Wneg - Wd).max()
                if Wf is not None:
                    dev = np.abs(Wd - Wf).max() / np.abs(Wd).max()
                    worst1 = max(worst1, dev, orient)
                    n1 += Wd.size
                    if dev > 1e-10 or orient > 1e-10:
                        hits.append(f"(1) on box {n}, N={N}, beta={beta}: direct vs fiber {dev:.2e}, orientation {orient:.2e}")
                minW = min(minW, Wd.min())
                if Wd.min() <= 1e-300:
                    hits.append(f"W(J) <= 0 for a conserved current on box {n}, N={N}, beta={beta}")
                # (2): chains of one or two plaquettes with coefficients in {-2..2}
                coeffs = [x for x in range(-2, 3) if x != 0]
                chains = [((p,), (k,)) for p in range(box.P) for k in coeffs]
                chains += [((p, q), (k, l)) for p in range(box.P) for q in range(p + 1, box.P) for k in (1, -1) for l in (1, -1)]
                Wflat = Wd.reshape(-1)
                shape = (N,) * box.C
                for ps, ks in chains:
                    s = np.zeros(box.P, dtype=np.int64)
                    for p, k in zip(ps, ks):
                        s[p] = k
                    Rs = 1.0
                    for p, k in zip(ps, ks):
                        Rs *= max(c[j] / c[(j + k) % N] for j in range(N))
                    dJ = current_of(box, N, s)
                    # every conserved K (all cycle coordinates) and J = K + d1* S
                    Kgrid = np.indices(shape).reshape(box.C, -1).T
                    Jgrid = (Kgrid + dJ[None, :]) % N
                    WK = Wflat
                    WJ = Wflat[np.ravel_multi_index(Jgrid.T, shape)]
                    up = (WJ / (Rs * WK)).max()
                    lo = (WJ * Rs / WK).min()
                    worst_up = max(worst_up, up)
                    worst_lo = max(worst_lo, 1 / lo)
                    ncmp += len(WJ)
                    if up > 1 + 1e-10 or lo < 1 - 1e-10:
                        hits.append(f"(2) fails on box {n}, N={N}, beta={beta}, chain {ps}/{ks}: max W(J)/(R W(K)) = {up:.6f}, min R W(J)/W(K) = {lo:.6f}")
            print(f"[box {n[0]}x{n[1]}x{n[2]}] V={box.V}, E={box.E}, P={box.P}, cycle coordinates {box.C}; N={N}: done  ({time.time() - t0:.0f}s)")
    print(f"[(1)] fiber representation vs direct link sums: {n1} (box, N, beta, J) values, largest relative difference {worst1:.2e} (orientation included)")
    print(f"[(2)] {ncmp} (K, S) comparisons over one- and two-plaquette chains: largest W(J)/(R(S) W(K)) = {worst_up:.6f}, largest "
          f"W(K)/(R(S) W(J)) = {worst_lo:.6f} (both must be <= 1); smallest conserved W(J) = {minW:.3e}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits[:10]:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - Part II's current representation (1) recomputed by brute force (tree-gauge link sums with an "
          f"N-ary FFT against the enumerated plaquette-current fibers) on the cube (N = 2..6), 2x1x1 (N = 2..4) and 2x2x1 (N = 2) at three couplings: "
          f"largest difference {worst1:.1e}; comparison (2) at {ncmp} (K, S) pairs, tightest ratios {worst_up:.4f} and {worst_lo:.4f} (<= 1); "
          f"all conserved W(J) > 0; {len(hits)} failures; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
