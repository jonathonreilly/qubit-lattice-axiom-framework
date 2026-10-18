"""C6 shared geometry: the corner graph of Z^3 on an L-torus, written independently of the
repo runners (same definitions as the corner-code note: vertices = the 12 perpendicular
direction pairs {d,e} at each site; on-site edges = cuboctahedron edges; link edges
{a,b}@v -- {-a,b}@v+a; faces = squares (about the C4 axes at a site), triangles (octants),
plaquettes, edge tubes).

Every edge stores its unwrapped displacement so that a torus of side L can be used as a
Bloch supercell (edge winding = (unwrapped - wrapped)/L).
"""
import itertools
import numpy as np

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def neg(d):
    return tuple(-x for x in d)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def perp(d, e):
    return dot(d, e) == 0 and d != e


CORNERS = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
assert len(CORNERS) == 12


class CornerGraph:
    def __init__(self, L):
        self.L = L
        self.sites = list(itertools.product(range(L), repeat=3))
        self.verts = [(v, c) for v in self.sites for c in CORNERS]
        self.vid = {q: i for i, q in enumerate(self.verts)}
        self.nV = len(self.verts)
        self.edges = []          # (i, j, kind, winding) with j reached from i by the stored displacement
        self.edesc = []          # (v, c, disp, c2): edge from corner c at site v to corner c2 at site v+disp
        self.ekey = {}           # (i, j, winding) -> edge index (both orientations)
        for v in self.sites:
            for c in CORNERS:
                d, e = tuple(c)
                for a, b in ((d, e), (e, d)):
                    for f in DIRS:
                        if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                            self._add((v, c), (v, frozenset((a, f))), (0, 0, 0), 'onsite')
                    self._add((v, c), (v, frozenset((neg(a), b))), a, 'link')
        self.nE = len(self.edges)
        deg = np.zeros(self.nV, int)
        for i, j, _, _ in self.edges:
            deg[i] += 1; deg[j] += 1
        assert set(deg.tolist()) == {6}, set(deg.tolist())
        self._faces()

    def _wrap(self, v, disp):
        raw = tuple(x + y for x, y in zip(v, disp))
        wrapped = tuple(x % self.L for x in raw)
        wind = tuple((r - w) // self.L for r, w in zip(raw, wrapped))
        return wrapped, wind

    def _add(self, q, r_local, disp, kind):
        (v, c), (_, c2) = q, r_local
        w, wind = self._wrap(v, disp)
        i, j = self.vid[q], self.vid[(w, c2)]
        if (i, j, wind) in self.ekey:
            return
        k = len(self.edges)
        self.edges.append((i, j, kind, wind))
        self.edesc.append((v, c, tuple(disp), c2))
        self.ekey[(i, j, wind)] = k
        self.ekey[(j, i, tuple(-x for x in wind))] = k

    def edge_between(self, q, disp, r_corner):
        """edge from vertex q=(v,c) to corner r_corner at site v+disp (unwrapped)."""
        v, c = q
        w, wind = self._wrap(v, disp)
        return self.ekey[(self.vid[q], self.vid[(w, r_corner)], wind)]

    def _cycle(self, seq):
        """seq: list of (site_unwrapped, corner); returns ordered list of (edge, i, j) traversals."""
        out = []
        for (p1, c1), (p2, c2) in zip(seq, seq[1:] + seq[:1]):
            v1 = tuple(x % self.L for x in p1)
            disp = tuple(y - x for x, y in zip(p1, p2))
            e = self.edge_between((v1, c1), disp, c2)
            out.append(e)
        return out

    def _faces(self):
        L = self.L
        self.faces = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
        self.face_seq = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
        Z0 = (0, 0, 0)
        for v in self.sites:
            for d in DIRS:
                a = [f for f in DIRS if perp(f, d) and f != neg(d)]
                a0 = a[0]
                b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
                ring = [a0, b0, neg(a0), neg(b0)]
                seq = [(v, frozenset((d, r))) for r in ring]
                self.faces['square'].append(self._cycle(seq)); self.face_seq['square'].append(seq)
                for i in range(4):
                    p, q = ring[i], ring[(i + 1) % 4]
                    w = tuple(x + y for x, y in zip(v, d))
                    seq = [(v, frozenset((d, p))), (w, frozenset((neg(d), p))),
                           (w, frozenset((neg(d), q))), (v, frozenset((d, q)))]
                    self.faces['tube'].append(self._cycle(seq)); self.face_seq['tube'].append(seq)
            for s in itertools.product((1, -1), repeat=3):
                x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                seq = [(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]
                self.faces['triangle'].append(self._cycle(seq)); self.face_seq['triangle'].append(seq)
            for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
                vd = tuple(x + y for x, y in zip(v, d)); ve = tuple(x + y for x, y in zip(v, e))
                vde = tuple(x + y for x, y in zip(vd, e))
                seq = [(v, frozenset((d, e))), (vd, frozenset((neg(d), e))),
                       (vde, frozenset((neg(d), neg(e)))), (ve, frozenset((d, neg(e))))]
                self.faces['plaquette'].append(self._cycle(seq)); self.face_seq['plaquette'].append(seq)
        # tubes are listed once per (site, direction d) including both d and -d: each edge tube
        # face is then generated twice (from v along d and from v+d along -d); deduplicate.
        for k in self.faces:
            seen = {}; fl = []; sl = []
            for f, s in zip(self.faces[k], self.face_seq[k]):
                key = frozenset(f)
                if key in seen:
                    continue
                seen[key] = 1; fl.append(f); sl.append(s)
            self.faces[k] = fl; self.face_seq[k] = sl

    def face_list(self):
        out = []
        for k in ('square', 'triangle', 'plaquette', 'tube'):
            for f in self.faces[k]:
                out.append((k, f))
        return out


# ---------------------------------------------------------------- GF(2) linear algebra
def gf2_rank_and_basis(rows, n):
    """rows: list of python-int bitsets (n bits). Returns pivot dict (reduced echelon)."""
    piv = {}
    for x in rows:
        while x:
            c = x.bit_length() - 1
            if c in piv:
                x ^= piv[c]
            else:
                piv[c] = x
                break
    return piv


def gf2_solve(rows, rhs, n):
    """Solve sum_{j in row} x_j = rhs over GF(2). rows: list of index lists. None if inconsistent."""
    piv = {}
    for r, b in zip(rows, rhs):
        x = 0
        for j in r:
            x ^= (1 << j)
        if b:
            x ^= (1 << n)
        while True:
            low = x & ((1 << n) - 1)
            if low == 0:
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
            sol |= (1 << c)
    return np.array([(sol >> j) & 1 for j in range(n)], dtype=np.uint8)


def bits(idx):
    x = 0
    for j in idx:
        x ^= (1 << j)
    return x
