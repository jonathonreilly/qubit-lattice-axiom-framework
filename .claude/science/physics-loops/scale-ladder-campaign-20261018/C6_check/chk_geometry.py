"""C6_check: independent corner-graph geometry (written from the note text, not from c6_corner_graph.py).

Directions are integers 0..5 -> +x,-x,+y,-y,+z,-z.  A corner is a sorted pair (d,e) of perpendicular
directions.  Vertex id = site_index*12 + corner_index.  Every edge records the unwrapped site displacement
so it can be used for Bloch twists.  Faces are vertex cycles given by unwrapped (site, corner) lists.
"""
import itertools
import numpy as np

VEC = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])


def opp(d):
    return d ^ 1


def axis(d):
    return d // 2


def perp(d, e):
    return axis(d) != axis(e)


CORN = sorted({tuple(sorted((d, e))) for d in range(6) for e in range(6) if perp(d, e)})
assert len(CORN) == 12
CIDX = {c: i for i, c in enumerate(CORN)}


def cid(d, e):
    return CIDX[tuple(sorted((d, e)))]


def dir_of(v):
    v = tuple(int(x) for x in v)
    for i, w in enumerate(VEC):
        if tuple(w) == v:
            return i
    raise ValueError(v)


class Corner:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3
        self.V = 12 * self.N
        self.edges = []      # (i, j, disp(np int3), kind)
        self.emap = {}       # (i, j, disp tuple) -> edge index (and reverse)
        for s in range(self.N):
            v = self.site(s)
            for (d, e) in CORN:
                # on-site: share exactly one direction, others perpendicular
                for (d2, e2) in CORN:
                    sh = set((d, e)) & set((d2, e2))
                    if len(sh) != 1:
                        continue
                    a = (set((d, e)) - sh).pop(); b = (set((d2, e2)) - sh).pop()
                    if perp(a, b):
                        self.add(v, (d, e), v, (d2, e2), 'onsite')
                # link {a,b}@v -- {-a,b}@v+a for a in {d,e}
                for a, b in ((d, e), (e, d)):
                    self.add(v, (a, b), v + VEC[a], (opp(a), b), 'link')
        self.E = len(self.edges)
        deg = np.bincount([x for (i, j, _, _) in self.edges for x in (i, j)], minlength=self.V)
        assert (deg == 6).all()
        self.build_faces()

    def site(self, s):
        L = self.L
        return np.array([s // (L * L), (s // L) % L, s % L])

    def sidx(self, v):
        L = self.L
        v = np.asarray(v) % L
        return int(v[0] * L * L + v[1] * L + v[2])

    def vid(self, v, c):
        return self.sidx(v) * 12 + cid(*c)

    def add(self, v, c, w, c2, kind):
        i, j = self.vid(v, c), self.vid(w, c2)
        disp = tuple(int(x) for x in (np.asarray(w) - np.asarray(v)))
        wrapped = tuple(int(x) for x in ((np.asarray(w) % self.L) - (np.asarray(v) % self.L)))
        key = (i, j, disp)
        # store the winding: number of supercell boundaries crossed
        if key in self.emap:
            return
        k = len(self.edges)
        wind = tuple((a - b) // self.L for a, b in zip(disp, wrapped))
        self.edges.append((i, j, np.array(wind), kind))
        self.emap[key] = k
        self.emap[(j, i, tuple(-x for x in disp))] = k

    def edge(self, v, c, w, c2):
        i, j = self.vid(v, c), self.vid(w, c2)
        disp = tuple(int(x) for x in (np.asarray(w) - np.asarray(v)))
        return self.emap[(i, j, disp)]

    def cycle_edges(self, seq):
        out = []
        for (v, c), (w, c2) in zip(seq, seq[1:] + seq[:1]):
            out.append(self.edge(np.asarray(v), c, np.asarray(w), c2))
        return out

    def build_faces(self):
        self.faces = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
        self.fseq = {k: [] for k in self.faces}
        pos = [0, 2, 4]
        for s in range(self.N):
            v = self.site(s)
            # squares about each of the 6 directions d
            for d in range(6):
                others = [x for x in range(6) if perp(x, d)]
                a0 = others[0]; b0 = [x for x in others if perp(x, a0)][0]
                ring = [a0, b0, opp(a0), opp(b0)]
                seq = [(v, (d, r)) for r in ring]
                self._addface('square', seq)
            # triangles: octants
            for sx, sy, sz in itertools.product((0, 1), repeat=3):
                x, y, z = 0 + sx, 2 + sy, 4 + sz
                self._addface('triangle', [(v, (x, y)), (v, (y, z)), (v, (z, x))])
            # plaquettes in the three positive planes
            for d, e in ((0, 2), (2, 4), (4, 0)):
                vd, ve = v + VEC[d], v + VEC[e]
                self._addface('plaquette', [(v, (d, e)), (vd, (opp(d), e)), (vd + VEC[e], (opp(d), opp(e))), (ve, (d, opp(e)))])
            # tubes: for each positive direction d, each adjacent pair (p,q) around d
            for d in pos:
                others = [x for x in range(6) if perp(x, d)]
                a0 = others[0]; b0 = [x for x in others if perp(x, a0)][0]
                ring = [a0, b0, opp(a0), opp(b0)]
                w = v + VEC[d]
                for t in range(4):
                    p, q = ring[t], ring[(t + 1) % 4]
                    self._addface('tube', [(v, (d, p)), (v, (d, q)), (w, (opp(d), q)), (w, (opp(d), p))])

    def _addface(self, k, seq):
        self.faces[k].append(self.cycle_edges(seq)); self.fseq[k].append(seq)

    def face_list(self):
        return [(k, f) for k in ('square', 'triangle', 'plaquette', 'tube') for f in self.faces[k]]
