"""C7_check: independent corner-graph geometry, oriented faces, Bloch Hamiltonians and GF(2) gauge solver.

Written from the definitions (not from c6_corner_graph.py / c7_common.py / C6_check chk_geometry.py).

Corner = frozenset {a, b} of two perpendicular unit vectors.  Edge TYPES of the one-site cell:
  on-site  {a,b} -- {a,f}  (shared a; f perpendicular to a and b),   R = 0
  link     {a,b}@0 -- {-a,b}@a                                       R = a
A supercell of L^3 sites carries edges (I, J, wind) with Bloch phase exp(i K . wind), K the supercell momentum.
Amplitude convention (mine): an edge with complex amplitude a contributes a c^dag_J c_I + h.c.,
i.e. H[J, I] += a e^{iK.wind}.  Standard flux of an oriented closed walk: arg prod (-amp along the walk).
"""
import itertools
import numpy as np

UNIT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def neg(a): return tuple(-x for x in a)
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def det3(a, b, c): return dot(a, cross(b, c))


CORNERS = sorted({frozenset((a, b)) for a in UNIT for b in UNIT if dot(a, b) == 0},
                 key=lambda c: sorted(c))
assert len(CORNERS) == 12
CI = {c: i for i, c in enumerate(CORNERS)}


def _types():
    T = []; seen = set()
    def put(c1, c2, R, kind):
        if (c1, c2, R) in seen or (c2, c1, neg(R)) in seen:
            return
        seen.add((c1, c2, R)); T.append((c1, c2, R, kind))
    for c in CORNERS:
        for a in c:
            b = next(iter(c - {a}))
            for f in UNIT:
                if dot(f, a) == 0 and dot(f, b) == 0:
                    put(c, frozenset((a, f)), (0, 0, 0), 'onsite')
            put(c, frozenset((neg(a), b)), a, 'link')
    return T


TYPES = _types()
NT = len(TYPES)
assert NT == 36 and sum(t[3] == 'onsite' for t in TYPES) == 24
TKEY = {}
for _t, (_c1, _c2, _R, _k) in enumerate(TYPES):
    TKEY[(_c1, _c2, _R)] = (_t, +1)
    TKEY[(_c2, _c1, neg(_R))] = (_t, -1)


def cell_faces():
    """faces of one site as unwrapped vertex walks [(pos, corner)], oriented: squares and triangles outward
    from the cuboctahedron; plaquettes and tubes with a fixed orientation."""
    o = (0, 0, 0)
    F = []
    for d in UNIT:                                   # 6 squares, outward (r_i x r_{i+1} = d)
        r0 = next(r for r in UNIT if dot(r, d) == 0)
        r1 = cross(d, r0)
        ring = [r0, r1, neg(r0), neg(r1)]
        assert all(cross(ring[i], ring[(i + 1) % 4]) == d for i in range(4))
        F.append(('square', [(o, frozenset((d, r))) for r in ring], d))
    for s in itertools.product((1, -1), repeat=3):   # 8 triangles, outward
        x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        if det3(x, y, z) < 0:
            x, y = y, x                               # swap -> det(x,y,z) = +1
        assert det3(x, y, z) == 1
        F.append(('triangle', [(o, frozenset((x, y))), (o, frozenset((y, z))), (o, frozenset((z, x)))], s))
    for d, e in ((E3[0], E3[1]), (E3[1], E3[2]), (E3[2], E3[0])):   # 3 plaquettes
        F.append(('plaquette', [(o, frozenset((d, e))), (d, frozenset((neg(d), e))),
                                (add(d, e), frozenset((neg(d), neg(e)))), (e, frozenset((d, neg(e))))], (d, e)))
    for d in E3:                                     # 12 tubes
        r0 = next(r for r in UNIT if dot(r, d) == 0); r1 = cross(d, r0)
        ring = [r0, r1, neg(r0), neg(r1)]
        for i in range(4):
            p, q = ring[i], ring[(i + 1) % 4]
            F.append(('tube', [(o, frozenset((d, p))), (o, frozenset((d, q))),
                               (d, frozenset((neg(d), q))), (d, frozenset((neg(d), p)))], (d, p, q)))
    return F


CELL_FACES = cell_faces()
FTYPES = ('square', 'triangle', 'plaquette', 'tube')


class Lat:
    def __init__(self, L):
        self.L = L
        self.sites = list(itertools.product(range(L), repeat=3))
        self.N = len(self.sites)
        self.sidx = {v: i for i, v in enumerate(self.sites)}
        self.n = 12 * self.N
        self.nE = NT * self.N
        I = []; J = []; W = []; kind = []; typ = []; site = []
        for v in self.sites:
            for t, (c1, c2, R, k) in enumerate(TYPES):
                w = add(v, R)
                wr = tuple(x % L for x in w)
                I.append(self.vid(v, c1)); J.append(self.vid(wr, c2))
                W.append(tuple((x - y) // L for x, y in zip(w, wr))); kind.append(k); typ.append(t); site.append(v)
        self.I = np.array(I); self.J = np.array(J); self.W = np.array(W, float)
        self.onsite = np.array([k == 'onsite' for k in kind]); self.typ = np.array(typ); self.esite = site
        deg = np.bincount(np.concatenate([self.I, self.J]), minlength=self.n)
        assert (deg == 6).all()
        # faces: (kind, [(edge, +-1)], label)
        self.faces = []
        for v in self.sites:
            for k, walk, lab in CELL_FACES:
                walk2 = [(add(v, p), c) for p, c in walk]
                self.faces.append((k, self.walk_edges(walk2), (v, lab)))
        self.fkind = np.array([FTYPES.index(f[0]) for f in self.faces])

    def vid(self, v, c):
        return 12 * self.sidx[tuple(x % self.L for x in v)] + CI[c]

    def edge(self, p1, c1, p2, c2):
        t, s = TKEY[(c1, c2, sub(p2, p1))]
        base = p1 if s == 1 else p2
        return self.sidx[tuple(x % self.L for x in base)] * NT + t, s

    def walk_edges(self, walk):
        out = []
        for (p1, c1), (p2, c2) in zip(walk, walk[1:] + walk[:1]):
            out.append(self.edge(p1, c1, p2, c2))
        tot = np.zeros(3)
        for e, s in out:
            tot += s * self.W[e]
        assert np.allclose(tot, 0)          # contractible faces: no net winding
        return out

    # ------------------------------------------------------------------
    def flux(self, amp, walk):
        p = 1.0 + 0j
        for e, s in walk:
            p *= -(amp[e] if s == 1 else np.conj(amp[e]))
        return np.angle(p)

    def fluxes(self, amp):
        return np.array([self.flux(amp, w) for _, w, _ in self.faces])

    def bloch(self, amp, Ks):
        Ks = np.atleast_2d(Ks)
        H = np.zeros((len(Ks), self.n, self.n), complex)
        ph = np.exp(1j * Ks @ self.W.T) * amp[None, :]
        for e in range(self.nE):
            H[:, self.J[e], self.I[e]] += ph[:, e]
            H[:, self.I[e], self.J[e]] += np.conj(ph[:, e])
        return H

    def realspace(self, amp):
        H = np.zeros((self.n, self.n), complex)
        for e in range(self.nE):
            H[self.J[e], self.I[e]] += amp[e]; H[self.I[e], self.J[e]] += np.conj(amp[e])
        return H


def kgrid(nk, shift=(0.0, 0.0, 0.0)):
    g = [2 * np.pi * (np.arange(nk) + s) / nk for s in shift]
    return np.array(list(itertools.product(*g)))


def eigs(lat, amp, Ks, chunk=512):
    out = []
    for i in range(0, len(Ks), chunk):
        out.append(np.linalg.eigvalsh(lat.bloch(amp, Ks[i:i + chunk])))
    return np.concatenate(out)


def gf2(rows, rhs, n):
    """solve sum_{j in row} x_j = rhs (mod 2); rows = lists of column ids (multiplicity mod 2). None if inconsistent."""
    piv = {}
    for r, b in zip(rows, rhs):
        x = 0
        for j in r:
            x ^= 1 << int(j)
        x |= (int(b) & 1) << n
        while True:
            low = x & ((1 << n) - 1)
            if not low:
                if x:
                    return None
                break
            c = low.bit_length() - 1
            if c in piv:
                x ^= piv[c]
            else:
                piv[c] = x
                break
    sol = 0
    for c in sorted(piv):
        x = piv[c]
        rest = x & ((1 << c) - 1)
        if ((x >> n) & 1) ^ (bin(rest & sol).count('1') & 1):
            sol |= 1 << c
    return np.array([(sol >> j) & 1 for j in range(n)], np.uint8)


def solve_gauge(lat, base, target, faces_mask=None):
    """bits x with fluxes(base * (-1)^x) = target (mod 2 pi) on all faces; None if impossible."""
    ph0 = lat.fluxes(base)
    d = np.mod(np.asarray(target) - ph0 + 1e-7, 2 * np.pi) - 1e-7
    b = np.round(d / np.pi).astype(int)
    if np.max(np.abs(d - np.pi * b)) > 1e-6:
        return None
    rows = [[e for e, _ in w] for _, w, _ in lat.faces]
    return gf2(rows, list(b % 2), lat.nE)


def maj_targets(lat, sq, tri, pl, tu):
    """tri in 'c+','c-','s+','s-': outward triangle flux +-pi/2, chiral (all equal) or staggered by octant parity."""
    tg = np.zeros(len(lat.faces))
    for f, (k, _, (v, lab)) in enumerate(lat.faces):
        if k == 'square': tg[f] = np.pi * sq
        elif k == 'plaquette': tg[f] = np.pi * pl
        elif k == 'tube': tg[f] = np.pi * tu
        else:
            sg = 1 if tri[1] == '+' else -1
            par = lab[0] * lab[1] * lab[2]
            tg[f] = sg * np.pi / 2 * (1 if tri[0] == 'c' else par)
    return tg


def maj_amp(lat, x, t1, t2):
    return 1j * np.where(lat.onsite, t1, t2) * (-1.0) ** x


def e_half(ev):
    """Majorana / half-filled ground energy per fine site: sum of negative eigenvalues / number of sites."""
    nsites = ev.size / 12.0
    return float(ev[ev < 0].sum() / nsites)
