"""K3: Bloch reduction of the composite-site network's flux-free (u = +1) Majorana problem and a certified node search."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import numpy as np

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
        # Lipschitz constant of every level in the sup-norm of the fractional momentum (Weyl's inequality, term by term)
        fac = np.where(self.a == self.b, 2.0, 1.0)
        self.lip = float(np.sum(fac * np.abs(self.t) * 2 * np.pi * np.abs(self.n).sum(axis=1)))

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


def certify(B, n0=40, levels=14, chunk=200000):
    """Adaptive cubes over the fractional zone [0,1)^3: a cube of half-width h at centre c is cleared when
    eps3(c) - eps2(c) > 2 lip h (the middle bands cannot meet inside). Returns the uncleared cubes at the finest level,
    the minimum cleared-gap ratio, and the number of evaluations."""
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    C = np.array(list(itertools.product(g, g, g)))
    counts = []
    for lev in range(levels):
        keep = []
        for s in range(0, len(C), chunk):
            ev = B.levels(C[s:s + chunk])
            gap = ev[:, 2] - ev[:, 1]
            keep.append(C[s:s + chunk][gap <= 2 * B.lip * h])
        C = np.concatenate(keep) if keep else np.zeros((0, 3))
        counts.append(len(C))
        if lev == levels - 1 or len(C) == 0:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        C = (C[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    return C, h, counts


def clusters(C, h):
    """Connected groups of uncleared cubes (touching or diagonal neighbours, periodic zone), by breadth-first search on the
    integer cube indices of the finest level."""
    n = int(round(0.5 / h))                          # cubes have full width 2h
    ids = np.floor(C / (2 * h)).astype(np.int64) % n
    where = {tuple(x): i for i, x in enumerate(ids)}
    seen = np.zeros(len(C), dtype=bool)
    out = []
    offs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
    for s0 in range(len(C)):
        if seen[s0]:
            continue
        seen[s0] = True
        grp = [s0]; q = [s0]
        while q:
            i = q.pop()
            x = ids[i]
            for d in offs:
                k = where.get(((x[0] + d[0]) % n, (x[1] + d[1]) % n, (x[2] + d[2]) % n))
                if k is not None and not seen[k]:
                    seen[k] = True; grp.append(k); q.append(k)
        out.append(np.array(grp))
    return out


def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    return np.angle(_link(V[:-1, :-1], V[1:, :-1]) * _link(V[1:, :-1], V[1:, 1:]) * _link(V[1:, 1:], V[:-1, 1:]) * _link(V[:-1, 1:], V[:-1, :-1]))


def sphere_chern(B, c, s, m=48, nocc=2):
    """Chern number of the lowest nocc bands on the sphere |f - c| = s (fractional coordinates, outward orientation), Fukui
    link method on a latitude-longitude grid with shared poles and a periodic seam. Also returns the smallest middle gap met."""
    th = np.linspace(0, np.pi, m + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :],
                  np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + c
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
    V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())


def slice_chern(B, f, m=60, nocc=2, axis=2):
    """Chern number of the lowest nocc bands on the slice (fractional coordinate `axis`) = f, oriented by the cyclic
    order of the two other coordinates; returns (Chern number, smallest middle gap on the slice)."""
    o = [(axis + 1) % 3, (axis + 2) % 3]
    u = np.arange(m + 1) / m
    P = np.zeros((m + 1, m + 1, 3)); P[:, :, o[0]] = u[:, None]; P[:, :, o[1]] = u[None, :]; P[:, :, axis] = f
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, m + 1, 4, nocc).copy()
    V[-1, :] = V[0, :]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())


def certify_zero(B, n0=40, levels=14, chunk=200000):
    """Adaptive cubes as in certify, clearing a cube when every level at its centre exceeds lip h in size (no level can reach
    zero inside). Returns the uncleared cubes at the finest level, the final half-width and per-level counts."""
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    C = np.array(list(itertools.product(g, g, g)))
    counts = []
    for lev in range(levels):
        keep = []
        for s in range(0, len(C), chunk):
            ev = B.levels(C[s:s + chunk])
            keep.append(C[s:s + chunk][np.abs(ev).min(axis=1) <= B.lip * h])
        C = np.concatenate(keep) if keep else np.zeros((0, 3))
        counts.append(len(C))
        if lev == levels - 1 or len(C) == 0:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        C = (C[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    return C, h, counts
