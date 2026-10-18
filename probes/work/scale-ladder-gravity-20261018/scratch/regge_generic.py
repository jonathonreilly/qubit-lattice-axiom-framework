"""Generic Bloch Regge second variation for a translation-periodic 4D simplicial complex.

Vertices are (b, t): b in Z^4 (cell), t a vertex type with offset OFF[t]; position = b + OFF[t].
The complex is a list of base 4-simplices (5 vertices each); all translates by Z^4 are included.
Edge variables are edge lengths, one per edge class (pair of types + relative cell).
Q(k) = sum_hinges 1/2 [a(-k)^T d(k) + d(-k)^T a(k)], with a = dA/dl and d = d(deficit)/dl.
"""
import itertools, numpy as np

def _key_pair(v1, v2):
    (b1, t1), (b2, t2) = v1, v2
    if (t1, b1) > (t2, b2): (b1, t1), (b2, t2) = (b2, t2), (b1, t1)
    rel = tuple(np.subtract(b2, b1))
    return (t1, t2, rel), tuple(b1)

def _key_tri(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0]))
    b0 = vs[0][0]
    return tuple((t, tuple(np.subtract(b, b0))) for b, t in vs), tuple(b0)

def coords_from_lengths(L2):
    """L2: 5x5 squared lengths -> 5x4 coordinates (vertex 0 at origin)."""
    G = np.array([[0.5 * (L2[0, a] + L2[0, b] - L2[a, b]) for b in range(1, 5)] for a in range(1, 5)])
    C = np.linalg.cholesky(G)
    return np.vstack([np.zeros(4), C])

def dihedral(P, h, m, n):
    """interior dihedral angle at triangle h (3 indices) between facets opposite m and opposite n."""
    def outward(opp):
        face = [i for i in range(5) if i != opp]
        A = np.array([P[i] - P[face[0]] for i in face[1:]])
        _, _, vt = np.linalg.svd(A); nv = vt[-1]
        if (P[opp] - P[face[0]]) @ nv > 0: nv = -nv
        return nv
    c = np.clip(outward(m) @ outward(n), -1, 1)
    return np.pi - np.arccos(c)

def tri_area(L2):
    a, b, c = L2
    G = np.array([[a, 0.5 * (a + b - c)], [0.5 * (a + b - c), b]])
    return 0.5 * np.sqrt(np.linalg.det(G))

class Complex:
    def __init__(self, OFF, base_simplices, g0=None, fd=1e-6):
        self.OFF = [np.array(o, float) for o in OFF]
        self.g0 = np.eye(4) if g0 is None else np.asarray(g0, float)
        self.simp = [list(s) for s in base_simplices]
        # edge classes
        self.ekey = {}
        for s in self.simp:
            for i, j in itertools.combinations(range(5), 2):
                k, _ = _key_pair(s[i], s[j])
                if k not in self.ekey: self.ekey[k] = len(self.ekey)
        self.E = len(self.ekey)
        self.evec = [None] * self.E
        for (t1, t2, rel), c in self.ekey.items():
            self.evec[c] = np.array(rel, float) + self.OFF[t2] - self.OFF[t1]
        self.types = sorted({t for s in self.simp for _, t in s})
        self._build(fd)

    def pos(self, v): return np.array(v[0], float) + self.OFF[v[1]]
    def L(self, v1, v2):
        d = self.pos(v2) - self.pos(v1); return np.sqrt(d @ self.g0 @ d)

    def _build(self, fd):
        # hinge classes and their stars (simplex, translation) with hinge at anchor 0
        stars, hverts = {}, {}
        for si, s in enumerate(self.simp):
            for tri in itertools.combinations(range(5), 3):
                key, anc = _key_tri([s[i] for i in tri])
                T = -np.array(anc)
                stars.setdefault(key, []).append((si, T, tri))
                hverts.setdefault(key, [(tuple(np.add(s[i][0], T)), s[i][1]) for i in tri])
        self.terms = []
        for key, st in stars.items():
            hv = hverts[key]
            # area gradient
            a_terms = []
            pairs = [(0, 1), (0, 2), (1, 2)]
            L2 = [self.L(hv[i], hv[j]) ** 2 for i, j in pairs]
            for n, (i, j) in enumerate(pairs):
                l = np.sqrt(L2[n]); up = list(L2); dn = list(L2)
                up[n] = (l + fd) ** 2; dn[n] = (l - fd) ** 2
                dA = (tri_area(up) - tri_area(dn)) / (2 * fd)
                c, anc = _key_pair(hv[i], hv[j]); a_terms.append((self.ekey[c], np.array(anc, float), dA))
            d_terms = []
            for si, T, tri in st:
                vs = [(tuple(np.add(v[0], T)), v[1]) for v in self.simp[si]]
                L2m = np.array([[self.L(vs[i], vs[j]) ** 2 for j in range(5)] for i in range(5)])
                m, n = [i for i in range(5) if i not in tri]
                for i, j in itertools.combinations(range(5), 2):
                    l = np.sqrt(L2m[i, j]); th = []
                    for sgn in (1, -1):
                        M = L2m.copy(); M[i, j] = M[j, i] = (l + sgn * fd) ** 2
                        th.append(dihedral(coords_from_lengths(M), tri, m, n))
                    dth = (th[0] - th[1]) / (2 * fd)
                    c, anc = _key_pair(vs[i], vs[j])
                    d_terms.append((self.ekey[c], np.array(anc, float), -dth))
            pack = lambda tl: (np.array([t[0] for t in tl]), np.array([t[1] for t in tl]), np.array([t[2] for t in tl]))
            self.terms.append((pack(a_terms), pack(d_terms)))

    def Q(self, k):
        k = np.asarray(k, complex); Q = np.zeros((self.E, self.E), complex)
        def row(t, kk):
            r = np.zeros(self.E, complex); np.add.at(r, t[0], t[2] * np.exp(1j * (t[1] @ kk))); return r
        for a, d in self.terms:
            Q += 0.5 * (np.outer(row(a, -k), row(d, k)) + np.outer(row(d, -k), row(a, k)))
        return Q

    def gauge(self, k):
        """vertex displacements xi_t e^{ik.b}: delta l = (xi_2 e^{ik.b2} - xi_1 e^{ik.b1}) . v/|v| per Bloch edge variable."""
        k = np.asarray(k, complex); nt = len(self.types); tix = {t: i for i, t in enumerate(self.types)}
        G = np.zeros((self.E, 4 * nt), complex)
        for (t1, t2, rel), c in self.ekey.items():
            v = self.evec[c]; u = self.g0 @ v / np.sqrt(v @ self.g0 @ v)
            G[c, 4 * tix[t2]:4 * tix[t2] + 4] += u * np.exp(1j * k @ np.array(rel, float))
            G[c, 4 * tix[t1]:4 * tix[t1] + 4] -= u
        return G

    def line_map(self, k):
        k = np.asarray(k, complex); HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        M = np.zeros((self.E, 10), complex)
        for (t1, t2, rel), c in self.ekey.items():
            v = self.evec[c]; l = np.sqrt(v @ self.g0 @ v); z = k @ v
            ph = np.exp(1j * k @ self.OFF[t1]) * (1.0 if abs(z) < 1e-14 else (np.exp(1j * z) - 1) / (1j * z))
            for j, (a, b) in enumerate(HC):
                M[c, j] = ph * v[a] * v[b] * (2 if a != b else 1) / (2 * l)
        return M

def kuhn():
    sims = []
    for s in itertools.permutations(range(4)):
        vs = [np.zeros(4, int)]
        for a in s: v = vs[-1].copy(); v[a] += 1; vs.append(v)
        sims.append([(tuple(v), 0) for v in vs])
    return [np.zeros(4)], sims

def barycentric():
    subsets = [frozenset(c) for r in range(5) for c in itertools.combinations(range(4), r)]
    tid = {S: i for i, S in enumerate(subsets)}
    OFF = [0.5 * np.array([1.0 if i in S else 0.0 for i in range(4)]) for S in subsets]
    sims = []
    for sig in itertools.permutations(range(4)):
        for a in itertools.product([0, 1], repeat=4):
            vs = []
            for k in range(5):
                S = frozenset(sig[:k])
                b = tuple(0 if i in S else a[i] for i in range(4))
                vs.append((b, tid[S]))
            sims.append(vs)
    return OFF, sims

def d4cone():
    """D4 = Z^4 u (Z^4 + u/2) with each Delaunay 16-cell (centred at the deep holes (e_mu+e_nu)/2) coned from its centre."""
    pairs = list(itertools.combinations(range(4), 2))
    OFF = [np.zeros(4), 0.5 * np.ones(4)] + [0.5 * (np.eye(4)[m] + np.eye(4)[n]) for m, n in pairs]
    def as_vertex(p):
        p = np.asarray(p, float)
        if np.allclose(p, np.round(p)): return (tuple(int(x) for x in np.round(p)), 0)
        q = p - 0.5
        assert np.allclose(q, np.round(q)); return (tuple(int(x) for x in np.round(q)), 1)
    sims = []
    for h, (m, n) in enumerate(pairs):
        r, s = [i for i in range(4) if i not in (m, n)]
        c = OFF[2 + h]; E = np.eye(4)
        axes = [0.5 * (E[m] + E[n]), 0.5 * (E[m] - E[n]), 0.5 * (E[r] + E[s]), 0.5 * (E[r] - E[s])]
        for signs in itertools.product([1, -1], repeat=4):
            vs = [((0, 0, 0, 0), 2 + h)] + [as_vertex(c + sg * ax) for sg, ax in zip(signs, axes)]
            sims.append(vs)
    return OFF, sims

def p1_scalar(C, k):
    """P1 stiffness on a generic complex: (ntypes x ntypes) Bloch matrix of sum vol |grad phi|^2."""
    k = np.asarray(k, complex); nt = len(C.types); tix = {t: i for i, t in enumerate(C.types)}
    S = np.zeros((nt, nt), complex); gi = np.linalg.inv(C.g0)
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); E = P[1:] - P[0]
        vol = np.sqrt(abs(np.linalg.det(E @ C.g0 @ E.T))) / 24
        # gradient of barycentric functions: grad lambda_i (i=1..4) = rows of inv(E)^T ; lambda_0 = 1 - sum
        Gr = np.linalg.inv(E).T; grads = np.vstack([-Gr.sum(axis=0), Gr]) if False else np.vstack([-(np.linalg.inv(E) @ np.ones(4)), np.linalg.inv(E).T])
        grads = np.vstack([-np.linalg.inv(E).sum(axis=1), np.linalg.inv(E).T]) if False else None
        Einv = np.linalg.inv(E)                     # columns: grad lambda_i for i=1..4 (since E @ Einv = 1)
        gl = [-(Einv.sum(axis=1))] + [Einv[:, i] for i in range(4)]
        for i in range(5):
            for j in range(5):
                w = vol * gl[i] @ gi @ gl[j]
                ti, tj = tix[vs[i][1]], tix[vs[j][1]]
                S[ti, tj] += w * np.exp(1j * k @ (np.array(vs[j][0], float) - np.array(vs[i][0], float)))
    return S
