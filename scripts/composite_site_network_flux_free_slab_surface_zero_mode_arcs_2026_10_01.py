#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: surface (slab) zero contours, finite-slab floating-point diagnostic.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J = (1, 1, 1) and odd term kappa, four-site Bloch matrix H(f) = i M(f) with M(f)[a, b] += t e^{2 pi i f.n}, M[b, a] -= t e^{-2 pi i f.n}
for each real hopping term (a, b, n, t), n in units of the primitive translations a1 = (2,0,0), a2 = (0,2,0), a3 = (1,1,2).
Slab: open along a3 with N = 40 layers (layer L = the L-th a3 cell; "cell cut c": every site of cell R sits in layer R_3), good
momenta (f1, f2) = (u, v) along a1, a2; block (L, L + n_3) of M receives t e^{2 pi i (u n_1 + v n_2)}, hoppings leaving layers 0..N-1
are dropped, H_slab = i M_slab is a 4N x 4N Hermitian matrix.  Top surface = layers 0.., bottom = the last layers.
Zero contour of a surface: tt (bb) = weight of the negative-energy subspace of H_slab on the top (bottom) half of the slab; a surface
state crossing E = 0 moves its weight in or out of the negative subspace, so a grid edge of the 80 x 80 half-offset grid
(u, v) = ((i + 1/2)/80, (j + 1/2)/80) with |jump of tt (bb)| > 0.5 is a zero crossing on the top (bottom) surface; edges within 2.2 grid
units are joined into components; an open component is an "arc" (its ends = the two graph-diameter ends), a component wrapping the
torus is a "line".  The end distance of an arc is the distance from the projection of the node nearest to a graph-diameter end to the
nearest edge of the arc.
Checks (J = (1,1,1), kappa = 0.3 with two bulk touchings, kappa = 0.6 with six):
 (1a) the independently reconstructed H(f) equals Bloch.H at random f (< 1e-12); (1b) slabs along each of a1, a2, a3 are Hermitian;
      (1c) the slab with periodic closure reproduces the bulk (N = 1: H(f); N = 3: union of three bulk spectra), < 1e-12;
 (2)  Chern number C(f1) of the two lowest bands on f1 = const tori (Fukui links, 96 x 96 plaquettes, 80 slices) is constant between the
      f1 coordinates of the bulk touchings and jumps by -chi at each, chi = sign Im Tr(P d1H P d2H P d3H) computed here (P = projector on
      the two levels nearest zero) at the exact family positions of the landed note (formulas only);
 (3)  kappa = 0.3, a3 slab: the top contour has exactly one arc whose two ends lie within 0.02 of the surface projections (f1, f2) of
      the two touchings (one end at each), plus the straight line u = 1/2;
 (4)  kappa = 0.6: three arcs, ends within 0.02 of projections, each arc joins a (+) and a (-) touching, every touching used once,
      plus the line u = 1/2; the pairing is reported;
 (5)  net spectral flow of the zero contour along each of the 80 circles u = const, v = const (top and bottom surface) equals the slice
      Chern number in modulus on at least 70 of 80 circles, with a constant sign, and every exception lies within 0.015 of a node coordinate;
 (6)  termination dependence, reported not asserted: cell cut with the fourth site shifted by one layer (shift (0,0,0,1)) at kappa = 0.6:
      three arcs joining (+,-) touchings; whether the pairing differs from check (4) is reported (the pairing is not an intrinsic datum).
Everything is a floating-point finite-slab (N = 40, grid 0.0125) diagnostic: no interval arithmetic, no certification, no statement about
the half-infinite slab, other couplings or other terminations.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import time

import numpy as np

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label} :: {detail}", flush=True)


# ------------------------------------------------------------------------------------------------ network and Bloch terms (as landed)
AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])       # rows: primitive translations of the site and colour rules
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


class Bloch:
    def __init__(self, J, kappa):
        self.T = terms(J, kappa)
        self.a = np.array([x[0] for x in self.T]); self.b = np.array([x[1] for x in self.T])
        self.n = np.array([x[2] for x in self.T], dtype=float); self.t = np.array([x[3] for x in self.T])

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.T)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))


# ------------------------------------------------------------------------------------------------ independent bulk, slab, nodes
def H_bulk_loop(T, f):
    """Plain loop reconstruction of H(f) = i M(f) from the term list (independent of Bloch.H)."""
    M = np.zeros((4, 4), dtype=complex)
    for (a, b, n, t) in T:
        ph = np.exp(2j * np.pi * (f[0] * n[0] + f[1] * n[1] + f[2] * n[2]))
        M[a, b] += t * ph
        M[b, a] -= t * np.conj(ph)
    return 1j * M


def dH_bulk(T, f, axis):
    D = np.zeros((4, 4), dtype=complex)
    for (a, b, n, t) in T:
        ph = np.exp(2j * np.pi * (f[0] * n[0] + f[1] * n[1] + f[2] * n[2]))
        d = 2j * np.pi * n[axis] * ph
        D[a, b] += t * d
        D[b, a] -= t * np.conj(d)
    return 1j * D


def slab_hamiltonian(T, d, fperp, N, shift=(0, 0, 0, 0), periodic=None):
    """Slab of N layers along the primitive translation a_{d+1} (d = 0, 1, 2), good momenta fperp along the other two.
    Basis index 4 L + a.  Site a of cell R sits in layer R_d + shift[a]; the term (a, b, n, t) joins (a, L) to (b, L + n_d + shift[b] - shift[a]).
    Hoppings leaving layers 0..N-1 are dropped, or wrapped modulo N with phase e^{2 pi i periodic wrap} if `periodic` is given (tests)."""
    perp = [i for i in range(3) if i != d]
    M = np.zeros((4 * N, 4 * N), dtype=complex)
    for (a, b, n, t) in T:
        ph = np.exp(2j * np.pi * (fperp[0] * n[perp[0]] + fperp[1] * n[perp[1]]))
        dl = n[d] + shift[b] - shift[a]
        L = np.arange(N); L2 = L + dl
        if periodic is None:
            keep = (L2 >= 0) & (L2 < N)
            L, L2 = L[keep], L2[keep]
            w = 1.0
        else:
            wrap, L2 = np.divmod(L2, N)
            w = np.exp(2j * np.pi * periodic * wrap)
        r, c = 4 * L + a, 4 * L2 + b
        M[r, c] += t * ph * w
        M[c, r] -= t * np.conj(ph * w)
    return 1j * M


def node_families(J, kappa):
    """Zero-energy touchings from the three exact families of the landed note (formulas only), J = (1, 1, Jz):
    (i) (x, 1-x, 0), (1-x, x, 0), 4k^2 c^2 - 2c + J^2 - 4k^2 - 2 = 0, c = cos 2 pi x;
    (ii) (x, 1-x, f3) and images, cos 2 pi x = 1 - J/(4k^2), cos 2 pi f3 = (J+2)/(4k^2) - (4+J-J^2)/J, kappa_c < k <= kappa_h;
    (iii) (f3+g, f3-g, f3), cos 2 pi f3 = [J+2 - sqrt(5J^2+8J+J(J+2)/k^2)]/2, cos 2 pi g = -J - cos 2 pi f3, k >= kappa_h."""
    Jz = J[2]
    assert abs(J[0] - 1) < 1e-14 and abs(J[1] - 1) < 1e-14
    k = kappa
    out = []
    for c in np.roots([4 * k * k, -2.0, Jz * Jz - 4 * k * k - 2.0]):
        if abs(c.imag) < 1e-13 and -1 <= c.real <= 1:
            x = np.arccos(c.real) / (2 * np.pi)
            for xx in sorted({x, 1 - x}):
                out.append(("i", np.array([xx, (1 - xx) % 1.0, 0.0])))
    kc2 = Jz * (Jz + 2) / (4 * (4 + 2 * Jz - Jz ** 2))
    kh2 = Jz / (4 * (2 - Jz)) if Jz < 2 else np.inf
    if kc2 < k * k <= kh2 + 1e-15:
        cx = 1 - Jz / (4 * k * k); c3 = (Jz + 2) / (4 * k * k) - (4 + Jz - Jz ** 2) / Jz
        if abs(cx) <= 1 and abs(c3) <= 1:
            x = np.arccos(cx) / (2 * np.pi); f3 = np.arccos(c3) / (2 * np.pi)
            for xx in sorted({x, 1 - x}):
                for ff in sorted({f3, 1 - f3}):
                    out.append(("ii", np.array([xx, (1 - xx) % 1.0, ff])))
    if k * k >= kh2 - 1e-15:
        s = np.sqrt(5 * Jz ** 2 + 8 * Jz + Jz * (Jz + 2) / (k * k))
        c3 = (Jz + 2 - s) / 2; cg = -Jz - c3
        if abs(c3) <= 1 and abs(cg) <= 1:
            f3 = np.arccos(c3) / (2 * np.pi); g = np.arccos(cg) / (2 * np.pi)
            for ff in sorted({f3, 1 - f3}):
                for gg in sorted({g, 1 - g}):
                    out.append(("iii", np.array([(ff + gg) % 1.0, (ff - gg) % 1.0, ff])))
    return out


def chirality_trace(T, f):
    """Im Tr(P d1H P d2H P d3H), P = projector on the two levels nearest zero (its sign = landed det V sign)."""
    w, V = np.linalg.eigh(H_bulk_loop(T, f))
    idx = np.argsort(np.abs(w))[:2]
    P = V[:, idx] @ V[:, idx].conj().T
    D = [dH_bulk(T, f, a) for a in range(3)]
    return np.trace(P @ D[0] @ P @ D[1] @ P @ D[2]).imag, float(np.abs(w).min())


# ------------------------------------------------------------------------------------------------ slice Chern number (Fukui links)
def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    return np.angle(_link(V[:-1, :-1], V[1:, :-1]) * _link(V[1:, :-1], V[1:, 1:]) * _link(V[1:, 1:], V[:-1, 1:]) * _link(V[:-1, 1:], V[:-1, :-1]))


def slice_chern(B, f, m=96, nocc=2, axis=0):
    """Chern number of the lowest nocc bands on the torus f_axis = f, oriented by the cyclic order of the other two coordinates."""
    o = [(axis + 1) % 3, (axis + 2) % 3]
    u = np.arange(m + 1) / m
    P = np.zeros((m + 1, m + 1, 3)); P[:, :, o[0]] = u[:, None]; P[:, :, o[1]] = u[None, :]; P[:, :, axis] = f
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, m + 1, 4, nocc).copy()
    V[-1, :] = V[0, :]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi)


# ------------------------------------------------------------------------------------------------ slab scan, contours, components
def scan_halves(T, N, M, shift):
    """tt, bb: weight of the negative-energy subspace of the slab on the top / bottom half of the layers, on the M x M half-offset grid."""
    tt = np.zeros((M, M)); bb = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            w, V = np.linalg.eigh(slab_hamiltonian(T, 2, ((i + 0.5) / M, (j + 0.5) / M), N, shift))
            pw = (np.abs(V[:, w < 0]) ** 2).sum(axis=1).reshape(N, 4).sum(axis=1)
            tt[i, j] = pw[:N // 2].sum(); bb[i, j] = pw[N // 2:].sum()
    return tt, bb


def contour_edges(A, M, thr=0.5):
    """Grid edges with |jump of A| > thr.  Returns arrays U, V (edge midpoints), FL (+1 if the crossing state goes - to + along the
    increasing coordinate, i.e. the negative weight drops), DIR (0: edge along v at fixed u_i, 1: edge along u at fixed v_j), I, J."""
    rec = []
    for i in range(M):
        for j in range(M):
            for (di, dj, code) in ((0, 1, 0), (1, 0, 1)):
                dl = A[(i + di) % M, (j + dj) % M] - A[i, j]
                if abs(dl) > thr:
                    rec.append((((i + 0.5) / M + (0.5 / M if di else 0.0)) % 1.0, ((j + 0.5) / M + (0.5 / M if dj else 0.0)) % 1.0,
                                -int(np.sign(dl)), code, i, j))
    R = np.array(rec) if rec else np.zeros((0, 6))
    return R[:, 0], R[:, 1], R[:, 2].astype(int), R[:, 3].astype(int), R[:, 4].astype(int), R[:, 5].astype(int)


def circ(a, b):
    d = np.abs(a - b) % 1.0
    return np.minimum(d, 1 - d)


def circ_extent(x):
    xs = np.sort(x); gaps = np.diff(np.concatenate([xs, [xs[0] + 1]]))
    k0 = int(np.argmax(gaps))
    return 1 - gaps[k0]


def components(U, V, M, reach=2.2, min_edges=4):
    """Connected components of edge midpoints (torus distance <= reach grid units in both coordinates); returns a list of dicts."""
    n = len(U)
    adj = (circ(U[:, None], U[None, :]) <= reach / M) & (circ(V[:, None], V[None, :]) <= reach / M)
    seen = np.zeros(n, bool); comps = []
    for s in range(n):
        if seen[s]:
            continue
        idx = [s]; seen[s] = True; q = [s]
        while q:
            x = q.pop()
            for y in np.where(adj[x] & ~seen)[0]:
                seen[y] = True; idx.append(y); q.append(y)
        idx = np.array(idx)
        if len(idx) < min_edges:
            continue
        sub = adj[np.ix_(idx, idx)]

        def bfs(s0):
            dist = np.full(len(idx), -1); dist[s0] = 0; qq = [s0]
            while qq:
                x = qq.pop(0)
                for y in np.where(sub[x] & (dist < 0))[0]:
                    dist[y] = dist[x] + 1; qq.append(y)
            return dist
        ia = int(np.argmax(bfs(0))); ib = int(np.argmax(bfs(ia)))
        comps.append(dict(idx=idx, n=len(idx), wrap_u=circ_extent(U[idx]) > 1 - 3.0 / M, wrap_v=circ_extent(V[idx]) > 1 - 3.0 / M,
                          ends=[(U[idx[ia]], V[idx[ia]]), (U[idx[ib]], V[idx[ib]])]))
    return comps


def nearest_node(proj, u, v):
    d = np.hypot(circ(u, proj[:, 0]), circ(v, proj[:, 1]))
    k = int(np.argmin(d))
    return k, float(d[k])


def classify(A, M, proj, chi):
    """Top-surface (or bottom) contour of A: open arcs with the nodes at their ends, wrapping lines, edge count."""
    U, V, FL, DIR, I_, J_ = contour_edges(A, M)
    comps = components(U, V, M)
    arcs, lines = [], []
    for c in comps:
        if c["wrap_u"] or c["wrap_v"]:
            lines.append(dict(n=c["n"], wrap_v=c["wrap_v"], wrap_u=c["wrap_u"], du=float(np.abs(U[c["idx"]] - 0.5).max()), dv=float(np.abs(V[c["idx"]] - 0.5).max())))
        elif c["n"] >= 10:
            e = [nearest_node(proj, u, v) for (u, v) in c["ends"]]
            # end distance = distance from the assigned node's projection to the nearest edge of the arc (robust against the
            # staircase shape of the end; the node is the one nearest to the graph-diameter end)
            dist = [float(np.hypot(circ(U[c["idx"]], proj[k, 0]), circ(V[c["idx"]], proj[k, 1])).min()) for k in (e[0][0], e[1][0])]
            arcs.append(dict(n=c["n"], k=(e[0][0], e[1][0]), d=(dist[0], dist[1]), chi=(chi[e[0][0]], chi[e[1][0]])))
    return dict(nedges=len(U), arcs=arcs, lines=lines, U=U, V=V, FL=FL, DIR=DIR, I=I_, J=J_)


def pairing(arcs):
    return sorted(tuple(sorted(a["k"])) for a in arcs)


# ================================================================================================ checks
J = (1.0, 1.0, 1.0)
rng = np.random.default_rng(20261001)
KAPS = (0.3, 0.6)
TT = {k: terms(J, k) for k in KAPS}
BB = {k: Bloch(J, k) for k in KAPS}

# (1) construction
err = {k: max(np.abs(H_bulk_loop(TT[k], f) - BB[k].H(f)[0]).max() for f in rng.random((200, 3))) for k in KAPS}
check("(1a) reconstructed H(f) = Bloch.H at 200 random f, kappa 0.3 / 0.6", max(err.values()) < 1e-12,
      f"max abs diff {err[0.3]:.2e} / {err[0.6]:.2e}")
herm = max(np.abs(Hs - Hs.conj().T).max() for k in KAPS for d in range(3) for Hs in [slab_hamiltonian(TT[k], d, rng.random(2), 12)])
check("(1b) open slabs (N = 12) along a1, a2, a3 are Hermitian, both couplings", herm < 1e-12, f"max |H - H^dagger| = {herm:.2e}")
e1 = e3 = 0.0
for k in KAPS:
    for d in range(3):
        perp = [i for i in range(3) if i != d]
        for _ in range(5):
            f = rng.random(3)
            e1 = max(e1, np.abs(slab_hamiltonian(TT[k], d, f[perp], 1, periodic=f[d]) - BB[k].H(f)[0]).max())
            ev = np.sort(np.linalg.eigvalsh(slab_hamiltonian(TT[k], d, f[perp], 3, periodic=f[d])))
            ref = []
            for j in range(3):
                g = f.copy(); g[d] = (f[d] + j) / 3; ref.extend(np.linalg.eigvalsh(BB[k].H(g)[0]))
            e3 = max(e3, np.abs(ev - np.sort(ref)).max())
check("(1c) periodic closure reproduces the bulk (all three directions, both couplings)", max(e1, e3) < 1e-12,
      f"N=1 vs H(f): {e1:.2e}; N=3 spectrum vs union of 3 bulk spectra: {e3:.2e}")

# nodes (landed families) and their chirality, computed here
NODES = {}
for k in KAPS:
    fam = node_families(J, k)
    tr = [chirality_trace(TT[k], f) for _, f in fam]
    NODES[k] = dict(f=np.array([f for _, f in fam]), chi=np.array([int(np.sign(t[0])) for t in tr]), res=max(t[1] for t in tr),
                    proj=np.array([[f[0], f[1]] for _, f in fam]))

# (2) slice Chern numbers C(f1), C(f2) on the 80 grid values; check C(f1)
MG = 80
GRID = (np.arange(MG) + 0.5) / MG
CH = {}
for k in KAPS:
    CH[k] = (np.array([slice_chern(BB[k], g, axis=0) for g in GRID]), np.array([slice_chern(BB[k], g, axis=1) for g in GRID]))
    nd = NODES[k]
    x1 = nd["f"][:, 0]; order = np.argsort(x1); xs = x1[order]; ch = nd["chi"][order]
    n = len(xs)
    cu = CH[k][0]
    margin = 0.012
    ok = len(set(np.round(xs, 3))) == n and np.diff(xs).min() > 2 * margin
    nearest = np.min(circ(GRID[:, None], xs[None, :]), axis=1)
    use = nearest > margin
    ci = np.round(cu).astype(int)
    iid = np.array([int(np.sum(xs <= g)) % n for g in GRID])
    vals = {}
    for q in range(n):
        sel = use & (iid == q)
        ok &= sel.sum() >= 1 and np.all(ci[sel] == ci[sel][0]) and np.abs(cu[sel] - ci[sel]).max() < 0.1
        vals[q] = int(ci[sel][0]) if sel.any() else None
    jumps = []
    for j in range(n):
        before, after = vals[j % n], vals[(j + 1) % n]
        jumps.append((None if before is None or after is None else after - before, -int(ch[j])))
        ok &= jumps[-1][0] is not None and jumps[-1][0] == jumps[-1][1]
    check(f"(2) kappa {k}: sampled numerical C(f1) agrees within intervals; observed changes equal -chi",
          ok and nd["res"] < 1e-12,
          "node f1:chi " + ",".join(f"{x:.3f}:{int(c):+d}" for x, c in zip(xs, ch)) + f"; C per interval {[vals[q] for q in range(n)]}; "
          f"jumps (seen,-chi) {jumps}; max |C-round C| {np.abs(cu[use] - ci[use]).max():.1e}; node min|E| {nd['res']:.1e}")

# scans: kappa 0.3 and 0.6 (cell cut c), and the shifted cut at kappa 0.6
N_SLAB = 40
SCAN = {}
for key, kap, sh in (("c0.3", 0.3, (0, 0, 0, 0)), ("c0.6", 0.6, (0, 0, 0, 0)), ("s0.6", 0.6, (0, 0, 0, 1))):
    SCAN[key] = scan_halves(TT[kap], N_SLAB, MG, sh)
CLS = {}
for key, kap in (("c0.3", 0.3), ("c0.6", 0.6), ("s0.6", 0.6)):
    nd = NODES[kap]
    CLS[key] = (classify(SCAN[key][0], MG, nd["proj"], nd["chi"]), classify(SCAN[key][1], MG, nd["proj"], nd["chi"]))


def arcs_text(arcs):
    return "; ".join(f"#{a['k'][0]}({a['chi'][0]:+d})-#{a['k'][1]}({a['chi'][1]:+d}) {a['n']} edges, ends {a['d'][0]:.3f}/{a['d'][1]:.3f}" for a in arcs)


def has_u_line(c):
    return any(l["wrap_v"] and l["du"] <= 0.6 / MG for l in c["lines"])


# (3) kappa 0.3
c3 = CLS["c0.3"][0]
a3 = c3["arcs"]
ok3 = (len(a3) == 1 and sorted(a3[0]["k"]) == [0, 1] and max(a3[0]["d"]) < 0.02 and has_u_line(c3))
check("(3) kappa 0.3, a3 slab N=40: top contour = one arc joining the two projected touchings + line u = 1/2", ok3,
      f"edges {c3['nedges']}; arcs: {arcs_text(a3)}; line u=1/2: {has_u_line(c3)}")

# (4) kappa 0.6
c4 = CLS["c0.6"][0]
a4 = c4["arcs"]
used = sorted(k for a in a4 for k in a["k"])
ok4 = (len(a4) == 3 and used == list(range(6)) and all(a["chi"][0] * a["chi"][1] == -1 for a in a4) and max(max(a["d"]) for a in a4) < 0.02
       and has_u_line(c4))
PAIR_C = pairing(a4)
check("(4) kappa 0.6, a3 slab N=40: top contour = three arcs, each joining a (+) and a (-) touching, + line u = 1/2", ok4,
      f"edges {c4['nedges']}; pairing {PAIR_C}; arcs: {arcs_text(a4)}; line u=1/2: {has_u_line(c4)}")

# (5) flow = slice Chern
for kap, key in ((0.3, "c0.3"), (0.6, "c0.6")):
    nd = NODES[kap]
    msg = []; ok5 = True
    for surf, cl in zip(("top", "bot"), CLS[key]):
        FL, DIR, I_, J_ = cl["FL"], cl["DIR"], cl["I"], cl["J"]
        flow_u = np.zeros(MG, int); flow_v = np.zeros(MG, int)
        for f, dr, i, j in zip(FL, DIR, I_, J_):
            if dr == 0:
                flow_u[i] += f
            else:
                flow_v[j] += f
        for lab, flow, cvec, coord in (("u", flow_u, CH[kap][0], nd["f"][:, 0]), ("v", flow_v, CH[kap][1], nd["f"][:, 1])):
            R = np.round(cvec).astype(int)
            match = np.abs(flow) == np.abs(R)
            exc = np.where(~match)[0]
            dist = [float(np.min(circ(GRID[i], coord))) for i in exc]
            signs = set(np.sign(flow[match & (R != 0)] * R[match & (R != 0)]).tolist())
            good = match.sum() >= 70 and all(d_ < 0.015 for d_ in dist) and len(signs) == 1
            ok5 &= good
            msg.append(f"{surf}/{lab}-circles {int(match.sum())}/80 sign(flow*C) {sorted(signs)} exceptions at {[round(float(GRID[i]), 4) for i in exc]} (node distance {[round(d_, 4) for d_ in dist]})")
    check(f"(5) kappa {kap}: net flow of the zero contour = slice Chern number on >= 70/80 circles per surface and coordinate", ok5, "; ".join(msg))

# (6) termination dependence (reported, not asserted)
cs = CLS["s0.6"][0]
as_ = cs["arcs"]
PAIR_S = pairing(as_)
ok6 = (len(as_) == 3 and sorted(k for a in as_ for k in a["k"]) == list(range(6)) and all(a["chi"][0] * a["chi"][1] == -1 for a in as_)
       and max(max(a["d"]) for a in as_) < 0.02)
check("(6) kappa 0.6, a3, shifted cut (0,0,0,1): three arcs, each joining a (+) and a (-) touching (pairing reported, not asserted)", ok6,
      f"edges {cs['nedges']}; pairing {PAIR_S}; pairing differs from cell cut c: {PAIR_S != PAIR_C}; line u=1/2 present: {has_u_line(cs)}; arcs: {arcs_text(as_)}")

print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")

# A failed decisive check must fail the bounded execution.
if __name__ == "__main__":
    raise SystemExit(int(not all(RESULTS)))
