#!/usr/bin/env python3
"""J:falsifier:PR8145 - clock-history-field note (PR #8145), Part III, a stated theorem's finite check: for the finite-clock Villain
transfer operator on a free spatial box, every nonzero external charge profile rho obeys
    (2)  |C_rho(a,b)| <= r^|A| C_0(a,b)  pointwise,                    r = 1 - (m/M)^6,  m = min w, M = max w,
    (3)  ||T_rho|| <= r^|A| lambda0,       (4)  H|rho >= |A| [-log(1 - (m/M)^6)],
for every set A of charged vertices with no adjacent pair, with lambda0 = ||T_0|| the full Perron eigenvalue; the proof's own step
uses r_v = 1 - (m/M)^(d_v) at a vertex of degree d_v (the exponent 6 is the cubic maximum).  The runner executes the 4-vertex square
(one plaquette, degree 2) for N = 2, 3, 4.  Here, with machinery disjoint from the runner's (it builds the full link-basis matrix and
its Fourier blocks):
  [spectral] the charge-rho sector of T = V^(1/2) C_rho V^(1/2) is built directly in the ELECTRIC basis: states E in Z_N^edges with
     div E = rho, parametrized by cycle coordinates n in Z_N^(cycles) of a spanning tree (Gauss law solved on the tree); the temporal
     kernel is diagonal there, kappa(E) = prod_e w^(E_e) (w^ the Z_N transform of w), and the magnetic factor V = prod_p w(curl a) is
     the convolution by V^(F) = N^-P sum_{s: d1^T s = F} prod_p w^(s_p) over plaquette-current fibers, so the sector matrix is
     diag(kappa^1/2) Conv(V^) diag(kappa^1/2) on Z_N^(cycles) (dense for small dimension, else Lanczos with an FFT convolution);
     E_rho = -log(lambda_rho/lambda0) is compared with the stated floor (4) and with the proof's degree-wise floor, on the boxes
     3x2x1, 3x3x1, 4x3x1, 2x2x2, 4x4x1, 3x2x2, 3x3x2 (vertex degrees up to 5), N up to 12, beta in {1/4, 1/2, 1, 2, 4}, for dipoles
     (adjacent, far, centre-corner), charge-2 pairs, quadrupoles and three-charge profiles; the neutral top is compared with the top
     of the full link-basis T (FFT Lanczos) where the link space is small enough;
  [extended] at beta >= 1 the floors fall below what double precision resolves in E_rho (q = m/M is about 5e-9 at beta = 4, so the
     stated floor is about 1e-50): the sectors of dimension <= 243 (boxes 3x2x1 N <= 12, 3x3x1 N <= 3, 2x2x2 N <= 3, 4x3x1 N = 2) are
     recomputed at 90 digits (mpmath: Poisson-summed coefficients, fiber sums, eigsy), where every floor is resolved;
  [kernel]   (2) itself at random spatial differences c = a - b by exhaustive gauge sums (and a layer transfer for the 3x3x3 box at
     N = 2, whose centre has degree 6), with A the best independent set of charged vertices.
Resolution rule: in double precision a floor is tested only where it is at least 1e-11 (the absolute accuracy of E_rho), and a violation
must exceed 1e-11; unresolved sectors are counted, and the small ones are the extended-precision set.  HIT if a resolved E_rho is below the
stated floor (4) or the degree-wise floor, if (2) fails beyond 1e-12 relative, or if the neutral top differs from the full top beyond 1e-9
relative (also if the electric-basis construction disagrees with an explicit link-basis gauge projection on the 3x2x1 box).
Deterministic (seeded).
"""
import itertools
import math
import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

rng = np.random.default_rng(8145)


def villain(N, beta):
    th = 2 * np.pi * np.arange(N) / N
    n = np.arange(-30, 31)
    return np.exp(-beta * (th[:, None] + 2 * np.pi * n) ** 2 / 2).sum(axis=1)


def dft(w):
    N = len(w)
    k = np.arange(N)
    return np.real(np.exp(-2j * np.pi * np.outer(k, k) / N) @ w)


def what(N, beta):
    """Z_N transform of the Villain weight by Poisson summation (all terms positive, no cancellation):
    w^(k) = sum_x w(2 pi x/N) e^{-2 pi i k x/N} = N (2 pi beta)^(-1/2) sum_{q = k mod N} e^{-q^2/(2 beta)}."""
    k = np.arange(N)
    q = k[:, None] + N * np.arange(-40, 41)[None, :]
    wh = N / np.sqrt(2 * np.pi * beta) * np.exp(-q.astype(float) ** 2 / (2 * beta)).sum(axis=1)
    assert np.max(np.abs(wh - dft(villain(N, beta)))) < 1e-12 * wh.max()
    return wh


class Box:
    def __init__(self, n):
        self.n = n
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
        plaq = []
        for v in verts:
            for a1, a2 in ((0, 1), (0, 2), (1, 2)):
                v1, v2 = sh(v, a1), sh(v, a2)
                v12 = sh(v1, a2)
                if v1 in vid and v2 in vid and v12 in vid:
                    plaq.append([(eid[(vid[v], vid[v1])], 1), (eid[(vid[v1], vid[v12])], 1), (eid[(vid[v2], vid[v12])], -1),
                                 (eid[(vid[v], vid[v2])], -1)])
        self.verts, self.vid, self.edges = verts, vid, edges
        self.V, self.E, self.P = len(verts), len(edges), len(plaq)
        self.d0 = np.zeros((self.E, self.V), dtype=np.int64)
        for i, (t, h) in enumerate(edges):
            self.d0[i, t] -= 1
            self.d0[i, h] += 1
        self.d1 = np.zeros((self.P, self.E), dtype=np.int64)
        for p, bd in enumerate(plaq):
            for e, s in bd:
                self.d1[p, e] += s
        assert not np.any(self.d1 @ self.d0)
        self.deg = np.abs(self.d0).sum(axis=0)
        # spanning tree (BFS) and cycle coordinates
        adj = [[] for _ in range(self.V)]
        for i, (t, h) in enumerate(edges):
            adj[t].append((h, i))
            adj[h].append((t, i))
        parent_edge = [-1] * self.V
        seen = [False] * self.V
        order = [0]
        seen[0] = True
        k = 0
        while k < len(order):
            v = order[k]
            k += 1
            for u, i in adj[v]:
                if not seen[u]:
                    seen[u] = True
                    parent_edge[u] = i
                    order.append(u)
        assert len(order) == self.V
        self.order, self.parent_edge = order, parent_edge
        tree = set(i for i in parent_edge if i >= 0)
        self.nontree = [i for i in range(self.E) if i not in tree]
        self.C = len(self.nontree)
        assert self.C == self.E - self.V + 1

    def solve(self, Enon, rho, N):
        """Rows of Enon carry the non-tree values; fill the tree edges from Gauss's law div E = rho (mod N)."""
        E = Enon.copy()
        for v in reversed(self.order[1:]):
            p = self.parent_edge[v]
            s = np.zeros(len(E), dtype=np.int64)
            for i in np.flatnonzero(self.d0[:, v]):
                if i != p:
                    s += self.d0[i, v] * E[:, i]
            E[:, p] = (rho[v] - s) * self.d0[p, v]          # d0[p, v] = +-1
        E %= N
        assert not np.any((E @ self.d0 - rho) % N)
        return E


def sector_setup(box, N, wh):
    grid = np.array(list(itertools.product(range(N), repeat=box.C)), dtype=np.int64).reshape(-1, box.C)
    # V^ on the cycle group: enumerate plaquette currents s, F = d1^T s, coordinate = F on the non-tree edges
    S = np.array(list(itertools.product(range(N), repeat=box.P)), dtype=np.int32).reshape(-1, box.P)
    F = (S @ box.d1.astype(np.int32)) % N
    assert not np.any((F @ box.d0) % N)
    idx = np.ravel_multi_index(F[:, box.nontree].T, (N,) * box.C) if box.C else np.zeros(len(S), dtype=np.int64)
    wts = np.prod(wh[S], axis=1) * float(N) ** (-box.P)
    Vhat = np.zeros(N ** box.C)
    np.add.at(Vhat, idx, wts)
    assert Vhat.min() > 0
    return grid, Vhat


def sector_top(box, N, wh, grid, Vhat, rho):
    Enon = np.zeros((len(grid), box.E), dtype=np.int64)
    Enon[:, box.nontree] = grid
    E = box.solve(Enon, rho, N)
    sk = np.sqrt(np.prod(wh[E], axis=1))
    dim = len(grid)
    shape = (N,) * box.C
    if dim <= 1600:
        diff = (grid[:, None, :] - grid[None, :, :]) % N
        conv = Vhat[np.ravel_multi_index(np.moveaxis(diff, -1, 0), shape)]
        M = sk[:, None] * conv * sk[None, :]
        return float(np.linalg.eigvalsh(M)[-1]), "dense"
    Vf = np.fft.fftn(Vhat.reshape(shape))

    def mv(x):
        y = np.fft.ifftn(Vf * np.fft.fftn((sk * x).reshape(shape)))
        return sk * np.real(y).ravel()

    op = LinearOperator((dim, dim), matvec=mv, dtype=np.float64)
    val = eigsh(op, k=1, which="LA", tol=1e-13, v0=np.ones(dim))[0][0]
    return float(val), "lanczos"


def full_top(box, N, w, wh):
    """Top eigenvalue of T = V^1/2 C V^1/2 on the whole link space Z_N^E (no charge projection), FFT Lanczos."""
    shape = (N,) * box.E
    a = np.array(list(itertools.product(range(N), repeat=box.E)), dtype=np.int64)
    Va = np.prod(w[(a @ box.d1.T) % N], axis=1) if box.P else np.ones(len(a))
    sv = np.sqrt(Va)
    Kf = np.prod(wh[np.array(list(itertools.product(range(N), repeat=box.E)))], axis=1).reshape(shape)
    # the convolution by prod_e w(a_e) has multiplier prod_e w^(k_e) at frequency k (with numpy's fft sign convention: w even)
    dim = N ** box.E

    def mv(x):
        return sv * np.real(np.fft.ifftn(Kf * np.fft.fftn((sv * x).reshape(shape)))).ravel()

    op = LinearOperator((dim, dim), matvec=mv, dtype=np.float64)
    return float(eigsh(op, k=1, which="LA", tol=1e-13, v0=np.ones(dim))[0][0])


def best_independent(box, charged, weight):
    """Maximum total weight over independent subsets of the charged vertices (brute force)."""
    best, bestA = 0.0, []
    adjset = set()
    for t, h in box.edges:
        adjset.add((t, h))
        adjset.add((h, t))
    ch = list(charged)
    for r in range(1, len(ch) + 1):
        for A in itertools.combinations(ch, r):
            if any((u, v) in adjset for u, v in itertools.combinations(A, 2)):
                continue
            s = sum(weight(v) for v in A)
            if s > best:
                best, bestA = s, list(A)
    return best, bestA


def profiles(box, N):
    V = box.V
    vid = box.vid
    n = box.n
    corner0 = vid[(0, 0, 0)]
    far = vid[tuple(x - 1 for x in n)]
    centre = int(np.argmax(box.deg))
    t, h = box.edges[0]
    out = []

    def prof(d):
        rho = np.zeros(V, dtype=np.int64)
        for v, q in d.items():
            rho[v] = (rho[v] + q) % N
        return rho

    out.append(("adjacent dipole", prof({t: 1, h: -1})))
    out.append(("far dipole", prof({corner0: 1, far: -1})))
    if centre != corner0:
        out.append(("centre-corner dipole", prof({centre: 1, corner0: -1})))
    if N >= 3:
        out.append(("far charge-2 pair", prof({corner0: 2, far: -2})))
        if centre not in (corner0, far):
            out.append(("three charges 1, 1, -2", prof({corner0: 1, far: 1, centre: -2})))
    cs = [vid[c] for c in itertools.product(*[(0, x - 1) for x in n[:2]], [0])]
    if len(set(cs)) == 4:
        out.append(("quadrupole", prof({cs[0]: 1, cs[1]: -1, cs[3]: 1, cs[2]: -1})))
    return out


_GAUGE = {}


def kernel_values(box, N, w, c, rhos):
    """F_rho(c) = N^-V sum_eta e^{-2 pi i <rho, eta>/N} prod_e w(c_e + (d0 eta)_e) for all rho in rhos (exhaustive eta)."""
    key = (box.n, N)
    if key not in _GAUGE:
        etas = np.array(list(itertools.product(range(N), repeat=box.V)), dtype=np.int64)
        _GAUGE[key] = (etas, (etas @ box.d0.T) % N, {})
    etas, G, phases = _GAUGE[key]
    wt = np.prod(w[(c[None, :] + G) % N], axis=1)
    out = []
    for rho in rhos:
        k = tuple(rho % N)
        if k not in phases:
            phases[k] = np.exp(-2j * np.pi * (etas @ rho) / N)
        out.append(np.sum(wt * phases[k]) / len(etas))
    return out


def link_basis_sector_top(box, N, w, rho):
    """Validation only (a runner-like route): P_rho T P_rho built in the link basis by explicit gauge averaging."""
    a = np.array(list(itertools.product(range(N), repeat=box.E)), dtype=np.int64)
    size = len(a)
    code = N ** np.arange(box.E)[::-1]
    Va = np.prod(w[(a @ box.d1.T) % N], axis=1) if box.P else np.ones(size)
    diff = (a[:, None, :] - a[None, :, :]) % N
    T = np.sqrt(Va)[:, None] * np.prod(w[diff], axis=2) * np.sqrt(Va)[None, :]
    P = np.zeros((size, size), dtype=complex)
    for eta in itertools.product(range(N), repeat=box.V):
        eta = np.array(eta, dtype=np.int64)
        tgt = ((a + box.d0 @ eta) % N) @ code
        P[np.arange(size), tgt] += np.exp(-2j * np.pi * (rho @ eta) / N)
    P /= N ** box.V
    return float(np.linalg.eigvalsh(P @ T @ P.conj().T)[-1])


def kernel_values_layers(box, w, c, rhos):
    """Same sum for N = 2 by a transfer over z-layers (used for the 3x3x3 box)."""
    N = 2
    n1, n2, n3 = box.n
    layer = [[box.vid[(x, y, z)] for x in range(n1) for y in range(n2)] for z in range(n3)]
    states = np.array(list(itertools.product(range(N), repeat=n1 * n2)), dtype=np.int64)
    out = []
    for rho in rhos:
        vec = None
        for z in range(n3):
            ids = layer[z]
            loc = {v: i for i, v in enumerate(ids)}
            L = np.exp(-2j * np.pi * (states @ rho[ids]) / N)
            for e, (t, h) in enumerate(box.edges):
                if t in loc and h in loc:
                    L = L * w[(c[e] + states[:, loc[h]] - states[:, loc[t]]) % N]
            if vec is None:
                vec = L
            else:
                prev = layer[z - 1]
                B = np.ones((len(states), len(states)))
                for i, (vp, vn) in enumerate(zip(prev, ids)):
                    e = box.edges.index((vp, vn))
                    B = B * w[(c[e] + states[None, :, i] - states[:, None, i]) % N]
                vec = (vec @ B) * L
        out.append(np.sum(vec) / N ** box.V)
    return out


def mp_sector_energies(box, N, beta, profs, dps=90):
    """Extended precision (mpmath, dps digits) sector tops for small sector dimensions: returns (q, {name: E_rho}, ...)."""
    import mpmath as mp
    mp.mp.dps = dps
    b = mp.mpf(beta)
    wv = [mp.fsum(mp.exp(-b * (2 * mp.pi * x / N + 2 * mp.pi * n) ** 2 / 2) for n in range(-30, 31)) for x in range(N)]
    q = min(wv) / max(wv)
    wh = [N / mp.sqrt(2 * mp.pi * b) * mp.fsum(mp.exp(-mp.mpf(k + N * j) ** 2 / (2 * b)) for j in range(-40, 41)) for k in range(N)]
    grid = np.array(list(itertools.product(range(N), repeat=box.C)), dtype=np.int64).reshape(-1, box.C)
    S = np.array(list(itertools.product(range(N), repeat=box.P)), dtype=np.int64).reshape(-1, box.P)
    F = (S @ box.d1) % N
    idx = np.ravel_multi_index(F[:, box.nontree].T, (N,) * box.C)
    Vhat = [mp.mpf(0)] * (N ** box.C)
    scale = mp.mpf(N) ** (-box.P)
    for srow, i in zip(S, idx):
        Vhat[int(i)] += mp.fprod(wh[int(x)] for x in srow) * scale
    shape = (N,) * box.C
    diff = (grid[:, None, :] - grid[None, :, :]) % N
    didx = np.ravel_multi_index(np.moveaxis(diff, -1, 0), shape)

    def top(rho):
        Enon = np.zeros((len(grid), box.E), dtype=np.int64)
        Enon[:, box.nontree] = grid
        E = box.solve(Enon, rho, N)
        sk = [mp.sqrt(mp.fprod(wh[int(x)] for x in row)) for row in E]
        dim = len(grid)
        M = mp.matrix(dim, dim)
        for i in range(dim):
            for j in range(i, dim):
                M[i, j] = M[j, i] = sk[i] * sk[j] * Vhat[int(didx[i, j])]
        return max(mp.eigsy(M, eigvals_only=True))

    lam0 = top(np.zeros(box.V, dtype=np.int64))
    out = {}
    for name, rho in profs:
        out[name] = -mp.log(top(rho) / lam0)
    return q, out


def main():
    t0 = time.time()
    hits = []
    RES = 1e-11                   # double precision resolves E_rho only to about this absolute accuracy
    BETAS = (0.25, 0.5, 1.0, 2.0, 4.0)
    PLAN = [((3, 2, 1), (2, 3, 5, 8, 12)), ((3, 3, 1), (2, 3, 5, 8)), ((4, 3, 1), (2, 3, 4)), ((2, 2, 2), (2, 3, 4, 5, 6)),
            ((4, 4, 1), (2, 3)), ((3, 2, 2), (2, 3)), ((3, 3, 2), (2,))]
    worst6 = (math.inf, None)
    worstd = (math.inf, None)
    n_cases = n_res6 = n_resd = 0
    maxdev_full = 0.0
    n_full = 0
    for n, Ns in PLAN:
        box = Box(n)
        for N in Ns:
            for beta in BETAS:
                w = villain(N, beta)
                wh = what(N, beta)
                assert wh.min() > 0
                q = w.min() / w.max()
                grid, Vhat = sector_setup(box, N, wh)
                lam0, how0 = sector_top(box, N, wh, grid, Vhat, np.zeros(box.V, dtype=np.int64))
                if N ** box.E <= 300000:
                    lf = full_top(box, N, w, wh)
                    dev = abs(lf - lam0) / lf
                    maxdev_full = max(maxdev_full, dev)
                    n_full += 1
                    if dev > 1e-9:
                        hits.append(f"neutral sector top {lam0:.12e} differs from the full Perron eigenvalue {lf:.12e} on {n}, N={N}, beta={beta}")
                for name, rho in profiles(box, N):
                    charged = [v for v in range(box.V) if rho[v] % N]
                    if not charged or rho.sum() % N:
                        continue
                    lam, how = sector_top(box, N, wh, grid, Vhat, rho)
                    Erho = -math.log(lam / lam0)
                    f6, A6 = best_independent(box, charged, lambda v: -math.log1p(-q ** 6))
                    fd, Ad = best_independent(box, charged, lambda v: -math.log1p(-q ** int(box.deg[v])))
                    n_cases += 1
                    tag = (n, N, beta, name, Erho, f6, fd, len(A6), how)
                    if f6 >= RES:                       # the stated floor is resolvable in double precision
                        n_res6 += 1
                        if Erho / f6 < worst6[0]:
                            worst6 = (Erho / f6, tag)
                        if Erho < f6 - RES:
                            hits.append(f"stated floor (4) fails on {n}, N={N}, beta={beta}, {name}: E_rho = {Erho:.6e} < {f6:.6e}")
                    if fd >= RES:
                        n_resd += 1
                        if Erho / fd < worstd[0]:
                            worstd = (Erho / fd, tag)
                        if Erho < fd - RES:
                            hits.append(f"degree-wise floor fails on {n}, N={N}, beta={beta}, {name}: E_rho = {Erho:.6e} < {fd:.6e}")
            print(f"[spectral] box {n[0]}x{n[1]}x{n[2]} (V={box.V}, E={box.E}, P={box.P}, cycles={box.C}, max degree {box.deg.max()}), N={N}: "
                  f"sector dimension {N ** box.C}  ({time.time() - t0:.0f}s)")
    print(f"[spectral] {n_cases} (box, N, beta, profile) sectors in double precision; the stated floor |A|(-log(1-(m/M)^6)) is at least {RES:g} "
          f"(resolvable) in {n_res6} of them: smallest E_rho / floor = {worst6[0]:.4g} at box {worst6[1][0]}, N={worst6[1][1]}, beta={worst6[1][2]}, "
          f"{worst6[1][3]} (E_rho = {worst6[1][4]:.4e}, floor {worst6[1][5]:.4e})")
    print(f"[spectral] the degree-wise floor sum_A -log(1-(m/M)^d_v) is resolvable in {n_resd}: smallest E_rho / floor = {worstd[0]:.4g} at box "
          f"{worstd[1][0]}, N={worstd[1][1]}, beta={worstd[1][2]}, {worstd[1][3]} (E_rho = {worstd[1][4]:.4e}, floor {worstd[1][6]:.4e})")
    print(f"[spectral] neutral sector top vs full link-space Perron eigenvalue: {n_full} comparisons, largest relative difference {maxdev_full:.2e}")
    # validation of the electric-basis construction against an explicit link-basis gauge projection (small box only)
    vdev = 0.0
    box = Box((3, 2, 1))
    for N in (2, 3):
        w = villain(N, 0.5)
        wh = what(N, 0.5)
        grid, Vhat = sector_setup(box, N, wh)
        for name, rho in profiles(box, N):
            if rho.sum() % N:
                continue
            e_top, _ = sector_top(box, N, wh, grid, Vhat, rho)
            l_top = link_basis_sector_top(box, N, w, rho)
            vdev = max(vdev, abs(e_top - l_top) / l_top)
    print(f"[validation] box 3x2x1, N = 2, 3, beta = 1/2: electric-basis sector tops vs explicit link-basis gauge projection, largest relative "
          f"difference {vdev:.2e}")
    if vdev > 1e-9:
        hits.append(f"internal: the electric-basis construction disagrees with the link-basis projection ({vdev:.2e}); results unreliable")
    # extended precision where double precision cannot resolve the floors (beta >= 1)
    xworst6 = (None, None)
    xworstd = (None, None)
    n_x = 0
    XPLAN = [((3, 2, 1), (2, 3, 5, 8, 12)), ((3, 3, 1), (2, 3)), ((2, 2, 2), (2, 3)), ((4, 3, 1), (2,))]
    import mpmath as mp
    for n, Ns in XPLAN:
        box = Box(n)
        for N in Ns:
            for beta in (1.0, 2.0, 4.0):
                profs = [(name, rho) for name, rho in profiles(box, N) if rho.sum() % N == 0 and np.any(rho % N)]
                q, Es = mp_sector_energies(box, N, beta, profs)
                for name, rho in profs:
                    charged = [v for v in range(box.V) if rho[v] % N]
                    A6 = best_independent(box, charged, lambda v: 1.0)[1]                 # a largest independent set
                    x6 = len(A6) * (-mp.log1p(-q ** 6))
                    qf = float(q)
                    Ad = best_independent(box, charged, lambda v: -math.log1p(-qf ** int(box.deg[v])))[1]
                    xd = mp.fsum(-mp.log1p(-q ** int(box.deg[v])) for v in Ad)
                    Er = Es[name]
                    n_x += 1
                    r6, rd = Er / x6, Er / xd
                    if xworst6[0] is None or r6 < xworst6[0]:
                        xworst6 = (r6, (n, N, beta, name, Er, x6))
                    if xworstd[0] is None or rd < xworstd[0]:
                        xworstd = (rd, (n, N, beta, name, Er, xd))
                    if Er < x6 * (1 - mp.mpf(10) ** -40) or Er < xd * (1 - mp.mpf(10) ** -40):
                        hits.append(f"extended precision: floor fails on {n}, N={N}, beta={beta}, {name}: E_rho = {mp.nstr(Er, 12)}, stated floor "
                                    f"{mp.nstr(x6, 12)}, degree-wise floor {mp.nstr(xd, 12)}")
            print(f"[extended] box {n[0]}x{n[1]}x{n[2]}, N={N}: beta = 1, 2, 4 at 90 digits  ({time.time() - t0:.0f}s)")
    print(f"[extended] {n_x} sectors at 90 digits (beta = 1, 2, 4): smallest E_rho / stated floor = {mp.nstr(xworst6[0], 6)} at box {xworst6[1][0]}, "
          f"N={xworst6[1][1]}, beta={xworst6[1][2]}, {xworst6[1][3]} (E_rho = {mp.nstr(xworst6[1][4], 6)}, floor {mp.nstr(xworst6[1][5], 6)}); "
          f"smallest E_rho / degree-wise floor = {mp.nstr(xworstd[0], 6)} at box {xworstd[1][0]}, N={xworstd[1][1]}, beta={xworstd[1][2]}, "
          f"{xworstd[1][3]} (E_rho = {mp.nstr(xworstd[1][4], 6)}, floor {mp.nstr(xworstd[1][5], 6)})")
    # kernel inequality (2) at random differences c
    kchecks = 0
    kworst = 0.0
    kworst_res = 0.0
    klayer_mark = None
    KPLAN = [((2, 2, 2), (2, 3, 4, 5), 40), ((3, 3, 1), (2, 3, 4), 40), ((3, 2, 2), (2,), 40), ((3, 3, 2), (2,), 24), ((3, 3, 3), (2,), 24)]
    for n, Ns, reps in KPLAN:
        box = Box(n)
        if n == (3, 3, 2):
            klayer_mark = kchecks
        for N in Ns:
            for beta in (0.25, 1.0, 4.0):
                w = villain(N, beta)
                q = w.min() / w.max()
                profs = profiles(box, N)
                rhos = [np.zeros(box.V, dtype=np.int64)] + [r for _, r in profs if r.sum() % N == 0 and np.any(r % N)]
                for _ in range(reps):
                    c = rng.integers(0, N, size=box.E)
                    vals = kernel_values_layers(box, w, c, rhos) if box.V > 20 else kernel_values(box, N, w, c, rhos)
                    if box.n == (3, 3, 2) and kchecks == klayer_mark:
                        alt = kernel_values_layers(box, w, c, rhos)
                        layer_dev = max(abs(x - y) / abs(vals[0]) for x, y in zip(vals, alt))
                        if layer_dev > 1e-12:
                            hits.append(f"internal: layer transfer disagrees with the exhaustive gauge sum ({layer_dev:.2e})")
                        print(f"[kernel] layer transfer vs exhaustive gauge sum on 3x3x2 (N=2): largest difference {layer_dev:.1e} (relative to C_0)")
                        klayer_mark = -1
                    F0 = vals[0].real
                    assert F0 > 0 and abs(vals[0].imag) < 1e-12 * F0
                    for rho, val in zip(rhos[1:], vals[1:]):
                        charged = [v for v in range(box.V) if rho[v] % N]
                        _, A = best_independent(box, charged, lambda v: -math.log1p(-q ** int(box.deg[v])))
                        bd = math.prod(1 - q ** int(box.deg[v]) for v in A)
                        b6 = (1 - q ** 6) ** len(A)
                        kchecks += 1
                        kworst = max(kworst, abs(val) / (bd * F0))
                        if bd < 1 - 1e-6:
                            kworst_res = max(kworst_res, abs(val) / (bd * F0))
                        if abs(val) > bd * F0 * (1 + 1e-12) or abs(val) > b6 * F0 * (1 + 1e-12):
                            hits.append(f"kernel bound (2) fails on {n}, N={N}, beta={beta}: |C_rho| = {abs(val):.6e} > {bd * F0:.6e}")
            print(f"[kernel] box {n[0]}x{n[1]}x{n[2]} (max degree {box.deg.max()}), N={N}: {reps} random c per beta checked  ({time.time() - t0:.0f}s)")
    print(f"[kernel] {kchecks} (c, rho) checks of |C_rho(c)| <= prod_A (1 - (m/M)^d_v) C_0(c) (hence <= r^|A| C_0): largest ratio {kworst:.12f} "
          f"(ratios within 1e-12 of 1 occur where the bound itself is within 1e-12 of 1, i.e. unresolved in double precision); largest ratio among "
          f"checks whose bound is below 1 - 1e-6: {kworst_res:.6f}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits[:10]:
        print("HIT: " + h)
    print(f"SUMMARY: electric-basis exact charge sectors on 7 free boxes (up to 3x3x2, degree <= 5; N up to 12; beta 1/4..4): {n_cases} sectors; "
          f"where double precision resolves the floor, min E_rho / stated floor = {worst6[0]:.3g} ({n_res6} sectors) and min E_rho / degree-wise "
          f"floor = {worstd[0]:.3g} ({n_resd}); at 90 digits (beta 1, 2, 4; {n_x} sectors) min ratios {mp.nstr(xworst6[0], 3)} and "
          f"{mp.nstr(xworstd[0], 3)}; neutral top = full Perron eigenvalue ({n_full} checks, max rel. diff {maxdev_full:.1e}); kernel bound (2) at "
          f"{kchecks} random (c, rho) incl. the 3x3x3 box's degree-6 centre, largest |C_rho|/bound = {kworst:.6f}; falsifier {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
