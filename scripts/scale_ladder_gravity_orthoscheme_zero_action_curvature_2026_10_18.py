#!/usr/bin/env python3
"""Scale ladder, gravity rung: unseen curvature in orthoscheme Regge carriers, and a carrier without it.

Finite floating-point checks on supplied Regge second variations of translation-periodic triangulations
of Z^3 x Z_tau (index 3 = tick):
  G0 a generic Bloch Regge builder reproduces the landed Kuhn-complex module's edge form;
  G1 Kuhn complex, hypercubic lengths: the fifth null direction of the edge form is not a flat deformation
     (only the vertex displacements are flat), so it is curvature the quadratic action does not see;
  G2 the barycentric subdivision of the cubical complex (B4 x lattice symmetric, tick reflection included;
     all simplices orthoschemes) has 16 such directions per cell, with metric content;
  G3 Kuhn complex, hypercubic lengths: the P1 scalar is the nearest-neighbour Laplacian, with real energies;
  G4 the body-diagonal tilt b u u^T makes energies non-real at leading order;
  G5 a spatial trigonal skew c u_s u_s^T lifts the fifth direction, keeps the eliminated edge block stiff,
     and makes energies non-real only at relative order k^2;
  G6 at that skew the full edge form (non-metric edges eliminated) is -(1/4) sqrt(det g0) EH_g0;
  G7-G12 the D4 cone (D4 Delaunay 16-cells coned from their centres; B4-symmetric, no orthoschemes,
     hypercubic geometry): null directions are exactly the vertex displacements, the leading symbol is
     -(1/4) EH, the P1 scalar has real energies and no on-shell k^4 term, the graviton has two real
     shells split -+ c k^2 with one metric and one non-metric mode each, and the two non-metric
     massless modes overlap the all-vertex P1 stress only at relative order k;
  G13-G15 that all-vertex P1 stress sources the relative vertex-type displacements at O(1); matter read
     through a site-cell metric is consistent, and its static source then excites the graviton (h_tt k^2 = -2)
     plus one partner with conformal pattern 1 (-2/3), so the total h_xx/h_tt is -1/2.
Supplied models only; no physical identification.
Companion: docs/SCALE_LADDER_GRAVITY_ORTHOSCHEME_ZERO_ACTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py',)

import contextlib, io, itertools, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


U = np.ones(4)
US = np.array([1.0, 1.0, 1.0, 0.0])
HC = R4.HCOMPS
SYM = [(a, b) for a in range(4) for b in range(a, 4)]

# ------------------------------------------------------------------ groups (all four axes)
def signed_perms(perms, signs):
    out = []
    for p in perms:
        for s in signs:
            M = np.zeros((4, 4))
            for i in range(4): M[p[i], i] = s[i]
            out.append(M)
    return out

ALLP = list(itertools.permutations(range(4)))
SPATIAL = [p for p in ALLP if p[3] == 3]
SIGNS = list(itertools.product([1, -1], repeat=4))
GROUPS = {'B4': signed_perms(ALLP, SIGNS),
          'K48': signed_perms(ALLP, [(1,) * 4, (-1,) * 4]),
          'OhT': signed_perms(SPATIAL, SIGNS)}

# ------------------------------------------------------------------ polynomial forms F(h,k)
def monos(n, d): return list(itertools.combinations_with_replacement(range(n), d))

def basis(spin, n):
    return [(fm, km) for fm in monos({2: 10, 1: 4, 0: 1}[spin], 2) for km in monos(4, n)]

def fvec(h, spin):
    if spin == 2: return np.array([h[a, b] for a, b in SYM])
    return h if spin == 1 else np.array([h])

def evalF(B, hv, k):
    return np.array([np.prod(hv[list(fm)]) * np.prod(k[list(km)]) for fm, km in B])

def rfield(rng, spin):
    if spin == 2: a = rng.standard_normal((4, 4)); return a + a.T
    return rng.standard_normal(4) if spin == 1 else rng.standard_normal()

def act(g, h, spin):
    return g @ h @ g.T if spin == 2 else (g @ h if spin == 1 else h)

def null(rows, tol=1e-9):
    A = np.array(rows); A = A / np.maximum(np.linalg.norm(A, axis=1, keepdims=True), 1e-300)
    _, s, vt = np.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum())
    return vt[r:].T, (s[r - 1], s[r] if r < len(s) else 0.0)

def census(spin, n, G, seed=1):
    rng = np.random.default_rng(seed); B = basis(spin, n); rows = []
    for _ in range(3 * len(B) // len(G) + 2):
        h = rfield(rng, spin); k = rng.standard_normal(4); f0 = evalF(B, fvec(h, spin), k)
        rows += [evalF(B, fvec(act(g, h, spin), spin), g @ k) - f0 for g in G]
    V, gap1 = null(rows)
    if spin == 0: return B, V, V.shape[1], V.shape[1], gap1
    grows = []
    for _ in range(3 * V.shape[1] + 10):
        h = rfield(rng, spin); k = rng.standard_normal(4)
        hp = h + (np.outer(k, x := rng.standard_normal(4)) + np.outer(x, k) if spin == 2 else k * rng.standard_normal())
        grows.append((evalF(B, fvec(hp, spin), k) - evalF(B, fvec(h, spin), k)) @ V)
    W, gap2 = null(grows)
    return B, V @ W, V.shape[1], W.shape[1], (min(gap1[0], gap2[0]), max(gap1[1], gap2[1]))

def hfull(x):
    h = np.zeros((4, 4))
    for i, (a, b) in enumerate(HC): h[a, b] = h[b, a] = x[i]
    return h

def EH(h, k, g0):
    gi = np.linalg.inv(g0); k2 = k @ gi @ k; tr = np.trace(gi @ h)
    return (k2 * np.trace(gi @ h @ gi @ h) - 2 * (k @ gi @ h @ gi @ h @ gi @ k)
            + 2 * (k @ gi @ h @ gi @ k) * tr - k2 * tr ** 2)

def fit(Ffun, B, nsamp=650, seed=3):
    rng = np.random.default_rng(seed); A = []; y = []
    for _ in range(nsamp):
        x = rng.standard_normal(10); k = rng.standard_normal(4)
        A.append(evalF(B, fvec(hfull(x), 2), k)); y.append(Ffun(x, hfull(x), k))
    A = np.array(A); y = np.array(y); c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return c, np.linalg.norm(A @ c - y) / np.linalg.norm(y)

# ------------------------------------------------------------------ Regge form with lengths from g0
def regge(g0):
    L2 = lambda v: float(v @ g0 @ v); at_all, dt_all = [], []
    for tri in R4.TRI_CLASSES:
        vts = [np.array(x) for x in tri]; qv, ei = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j])); v = np.array(R4.DIRS15[cls], float)
            qv.append(L2(v)); ei.append((cls, anc, np.sqrt(L2(v))))
        ao = R4.AREA(*qv)
        at = [(c, np.array(a, float), 2 * l * float(ao[1 + n])) for n, (c, a, l) in enumerate(ei)]
        dt = []
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            miss = tuple(sorted(set(range(5)) - {loc[tri[0]], loc[tri[1]], loc[tri[2]]}))
            qv, ed = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j]); v = np.array(R4.DIRS15[cls], float)
                qv.append(L2(v)); ed.append((cls, anc, np.sqrt(L2(v))))
            out = R4.THETA[miss](*qv)
            dt += [(c, np.array(a, float), -2 * l * float(out[1 + n])) for n, (c, a, l) in enumerate(ed)]
        for src, dst in ((at, at_all), (dt, dt_all)):
            dst.append((np.array([t[0] for t in src]), np.array([t[1] for t in src]), np.array([t[2] for t in src])))

    def row(t, k):
        r = np.zeros(15, complex); np.add.at(r, t[0], t[2] * np.exp(1j * (t[1] @ k))); return r

    def Qe(k):
        k = np.asarray(k, complex); M = np.zeros((15, 15), complex)
        for a, d in zip(at_all, dt_all):
            M += 0.5 * (np.outer(row(a, -k), row(d, k)) + np.outer(row(d, -k), row(a, k)))
        return M

    def Mh(k):
        k = np.asarray(k, complex); M = np.zeros((15, 10), complex)
        for ci, v in enumerate(R4.DIRS15):
            vv = np.array(v, float); z = (k @ vv) / 2
            ph = 1.0 if abs(z) < 1e-13 else (np.exp(2j * z) - 1) / (2j * z)
            for j, (a, b) in enumerate(HC):
                M[ci, j] = ph * (vv[a] * vv[b] * (2 if a != b else 1)) / (2 * np.sqrt(L2(vv)))
        return M
    return Qe, Mh

# ------------------------------------------------------------------ P1 scalar on the Kuhn complex
SIMP = []
for s in ALLP:
    vs = [np.zeros(4, int)]
    for a in s: v = vs[-1].copy(); v[a] += 1; vs.append(v)
    SIMP.append(vs)
DIRS = [np.array(v) for v in itertools.product([0, 1], repeat=4) if any(v)]
DIDX = {tuple(v): i for i, v in enumerate(DIRS)}

def edge(p, q):
    d = q - p
    return (DIDX[tuple(d)], p, 1) if tuple(d) in DIDX else (DIDX[tuple(-d)], q, -1)

def geom(vs, g0):
    E = np.array([vs[i] - vs[0] for i in range(1, 5)], float)
    return E, np.sqrt(np.linalg.det(E @ g0 @ E.T)) / 24

def scalar(k, g0):
    gi = np.linalg.inv(g0); S = 0j
    for vs in SIMP:
        E, vol = geom(vs, g0)
        gp = np.linalg.solve(E, np.array([np.exp(1j * k @ v) for v in vs])[1:] - 1)
        gm = np.linalg.solve(E, np.array([np.exp(-1j * k @ v) for v in vs])[1:] - 1)
        S += vol * gm @ gi @ gp
    return S

def schur(Q, Mp, Mm, C):
    D = C.T @ Q @ C
    return Mm.T @ Q @ Mp - (Mm.T @ Q @ C) @ np.linalg.solve(D, C.T @ Q @ Mp)

def compl(M0):
    u, _, _ = np.linalg.svd(M0.real); return u[:, M0.shape[1]:]

def sv(M):
    s = np.sort(np.linalg.svd(M, compute_uv=False)); return s / s[-1]

def lattice_kt(ks):
    return 1j * 2 * np.arcsinh(np.sqrt(np.sum(4 * np.sin(ks / 2) ** 2)) / 2)

def newton(f, x):
    for _ in range(80):
        h = 1e-7 * max(abs(x), 1); st = f(x) / ((f(x + h) - f(x - h)) / (2 * h)); x -= st
        if abs(st) < 1e-15: break
    return x


# ------------------------------------------------------------------ generic Bloch Regge builder

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
        Einv = np.linalg.inv(E)                     # columns: grad lambda_i for i=1..4 (since E @ Einv = 1)
        gl = [-(Einv.sum(axis=1))] + [Einv[:, i] for i in range(4)]
        for i in range(5):
            for j in range(5):
                w = vol * gl[i] @ gi @ gl[j]
                ti, tj = tix[vs[i][1]], tix[vs[j][1]]
                S[ti, tj] += w * np.exp(1j * k @ (np.array(vs[j][0], float) - np.array(vs[i][0], float)))
    return S


def p1_stress(C, k1, phi1, k2, phi2):
    """edge-length response of the P1 action S[phibar(k1), phi(k2)]; delta l_c(T) = eps_c e^{iq.T}, q = k1 - k2."""
    tix = {t: i for i, t in enumerate(C.types)}; q = k1 - k2; J = np.zeros(C.E, complex)
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); E = P[1:] - P[0]; G = E @ E.T; Gi = np.linalg.inv(G)
        v2 = np.array([phi2[tix[v[1]]] * np.exp(1j * k2 @ np.array(v[0], float)) for v in vs])
        v1 = np.array([np.conj(phi1[tix[v[1]]]) * np.exp(-1j * k1 @ np.array(v[0], float)) for v in vs])
        d2 = v2[1:] - v2[0]; d1 = v1[1:] - v1[0]
        X = d1 @ Gi @ d2; Pm = np.outer(Gi @ d2, Gi @ d1); Pm = 0.5 * (Pm + Pm.T)
        Psi = np.sqrt(np.linalg.det(G)) / 24 * (0.5 * Gi * X - Pm)
        for i, j in itertools.combinations(range(5), 2):
            key, anc = _key_pair(vs[i], vs[j]); c = C.ekey[key]
            dl2 = 2 * np.linalg.norm(P[j] - P[i]) * np.exp(1j * q @ np.array(anc, float))
            dG = np.zeros((4, 4), complex)
            if i == 0:
                dG[j - 1, j - 1] += dl2
                for b in range(4):
                    if b != j - 1: dG[j - 1, b] += dl2 / 2; dG[b, j - 1] += dl2 / 2
            else:
                dG[i - 1, j - 1] -= dl2 / 2; dG[j - 1, i - 1] -= dl2 / 2
            J[c] += np.sum(Psi * dG)
    return J


def golden(f, lo, hi):
    gr = (5 ** .5 - 1) / 2; a, b = lo, hi; c, d = b - gr * (b - a), a + gr * (b - a); fc, fd = f(c), f(d)
    for _ in range(120):
        if fc < fd: b, d, fd = d, c, fc; c = b - gr * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + gr * (b - a); fd = f(d)
        if b - a < 1e-14: break
    return (a + b) / 2


def site_metric(C, k):
    """D4 cone: 10 site-cell metric components from edge lengths, using axis edges and both face diagonals,
    each face diagonal read through the deep hole it passes through (invariant under moving non-site vertices)."""
    pairs = list(itertools.combinations(range(4), 2)); E = np.eye(4, dtype=int); Z = (0, 0, 0, 0)
    k = np.asarray(k, complex); Lm = np.zeros((10, C.E), complex)
    def add(row, v1, v2, coef):
        key, anc = _key_pair(v1, v2); Lm[row, C.ekey[key]] += coef * np.exp(1j * k @ np.array(anc, float))
    for mu in range(4): add(HC.index((mu, mu)), (Z, 0), (tuple(E[mu]), 0), 2.0)
    for h, (m, n) in enumerate(pairs):
        row = HC.index((m, n)); hv = (Z, 2 + h); r2 = np.sqrt(2) / 2
        add(row, (Z, 0), hv, r2); add(row, hv, (tuple(E[m] + E[n]), 0), r2)
        add(row, (tuple(E[n]), 0), hv, -r2); add(row, hv, (tuple(E[m]), 0), -r2)
    return Lm


def drows(C, k, which):
    out = []
    for a, d in C.terms:
        t = d if which == 'd' else a
        r = np.zeros(C.E, complex); np.add.at(r, t[0], t[2] * np.exp(1j * (t[1] @ k))); out.append(r)
    return np.array(out)


def extras(C, k, ngauge):
    """null directions of the edge form beyond the vertex displacements, the singular-value gap, and D x."""
    Q = C.Q(k); _, s, vh = np.linalg.svd(Q); s = s / s[0]
    lg = np.log10(np.maximum(s[::-1], 1e-300)); n0 = int(np.argmax(np.diff(lg)[:200])) + 1
    N = vh[-n0:].conj().T; G = C.gauge(k)
    X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :n0 - ngauge]
    return n0, s[::-1][n0] / s[::-1][n0 - 1], X


def main():
    I4 = np.eye(4); rr = np.random.default_rng(3)
    # ---------------- G0 generic builder vs landed module
    OFF, S = kuhn(); K = Complex(OFF, S)
    Qe0, Mh0 = regge(I4); k = np.array([0.4, 0.1, -0.3, 0.2])
    a = np.sort(np.linalg.svd(K.Q(k), compute_uv=False)); b = np.sort(np.linalg.svd(Qe0(k), compute_uv=False))
    check("G0 generic Bloch Regge builder reproduces the landed Kuhn-complex edge form (singular values)",
          np.abs(a - b).max() < 1e-7 * b.max() and K.E == 15 and len(K.terms) == 50, f"max deviation {np.abs(a-b).max():.1e}; 15 edges, 50 hinge classes")

    # ---------------- G1 Kuhn: the fifth null direction is curvature, not a flat deformation
    worst_flat, minD, ranks = 0.0, 1.0, []
    for _ in range(3):
        k = 0.4 * rr.standard_normal(4)
        n0, gap, X = extras(K, k, 4); D = drows(K, k, 'd'); nD = np.linalg.norm(D, 2)
        ranks.append((n0, np.linalg.matrix_rank(D, tol=1e-8 * nD)))
        minD = min(minD, np.linalg.norm(D @ X, axis=0).min() / nD)
        worst_flat = max(worst_flat, np.linalg.norm(D @ K.gauge(k)) / nD / np.linalg.norm(K.gauge(k)))
    check("G1 Kuhn, hypercubic lengths: edge-form nullity 5 but deficit-map rank 15 - 4; the fifth direction has |D x| = O(1)",
          all(r == (5, 11) for r in ranks) and minD > 0.3 and worst_flat < 1e-8,
          f"(nullity, rank D) = {ranks}; |D x|/|D| >= {minD:.2f}; vertex displacements flat to {worst_flat:.0e}")

    # ---------------- G2 barycentric subdivision: 16 zero-action curvature directions per cell
    OFFb, Sb = barycentric(); Bc = Complex(OFFb, Sb); res = []
    for k in [0.4 * rr.standard_normal(4), np.array([0.7, 0, 0, 0.0])]:
        n0, gap, X = extras(Bc, k, 64); D = drows(Bc, k, 'd'); nD = np.linalg.norm(D, 2)
        M = Bc.line_map(k); G = Bc.gauge(k); Pg = np.eye(Bc.E) - G @ np.linalg.pinv(G, rcond=1e-9)
        Mm = Pg @ M; sh = np.linalg.svd(Mm @ np.linalg.pinv(Mm, rcond=1e-9) @ X, compute_uv=False)
        res.append((n0, gap, np.linalg.norm(D @ X, axis=0).min() / nD, int((sh > 0.2).sum())))
    check("G2 barycentric subdivision (384 orthoschemes, 240 edges, 16 vertex types per cell; B4 incl. tick reflection): nullity 64 + 16, extras curved and metric-carrying",
          all(r[0] == 80 and r[1] > 1e4 and r[2] > 0.1 and r[3] >= 4 for r in res),
          "; ".join(f"nullity {r[0]}, gap {r[1]:.0e}, min |Dx|/|D| {r[2]:.2f}, extras with metric share > 0.2: {r[3]}" for r in res))

    # ---------------- G3 Kuhn, hypercubic lengths: P1 scalar = NN Laplacian, real energies
    dev = 0.0
    for _ in range(6):
        p = 1.3 * rr.standard_normal(4) + 0.3j * rr.standard_normal(4)
        dev = max(dev, abs(scalar(p, I4) - np.sum(4 * np.sin(p / 2) ** 2)))
    n = np.array([0.48, 0.6, 0.64]); re0 = max(abs(newton(lambda t: scalar(np.array([*(km * n), t]), I4), 1j * km).real) for km in (0.2, 0.8, 1.5))
    check("G3 Kuhn, hypercubic lengths: P1 scalar = sum 4 sin^2(p/2) (complex momenta); on-shell tick momentum pure imaginary for real spatial momenta",
          dev < 1e-12 and re0 < 1e-12, f"deviation {dev:.1e}; max |Re k_t| {re0:.1e} (|k| = 0.2, 0.8, 1.5)")

    # ---------------- G4 body-diagonal tilt: non-real at leading order
    g0 = I4 + 0.3 * np.outer(U, U)
    rb = [abs(newton(lambda t: scalar(np.array([*(km * n), t]), g0), 1j * km).real) / km for km in (0.1, 0.05)]
    check("G4 tilt g0 = 1 + 0.3 u u^T: Re k_t / |k| tends to a nonzero constant (non-real energies at leading order)",
          abs(rb[0] / rb[1] - 1) < 0.02 and rb[1] > 0.1, f"Re k_t/|k| = {rb[0]:.4f}, {rb[1]:.4f} at |k| = 0.1, 0.05")

    # ---------------- G5 spatial trigonal skew
    out = []
    q = np.array([0.3, -0.2, 0.25, 0.15]); kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
    for c in (0.2, 0.05):
        g0 = I4 + c * np.outer(US, US); Qe, Mh = regge(g0); C = compl(Mh(np.zeros(4)))
        s5 = sv(Qe(q))[4]; stiff = np.min(np.abs(np.linalg.eigvals(C.T @ Qe(0.01 * kd) @ C)))
        r = [abs(newton(lambda t: scalar(np.array([*(km * n), t]), g0), 1j * km).real) / km for km in (0.1, 0.05)]
        out.append((c, s5, stiff, r[0] / r[1]))
    check("G5 skew g0 = 1 + c u_s u_s^T (c = 0.2, 0.05): fifth direction lifted, eliminated block stiff, Re k_t/|k| falls as |k|^2",
          all(o[1] > 1e-4 and o[2] > 1 and abs(o[3] - 4) < 0.1 for o in out),
          "; ".join(f"c={o[0]}: 5th sv {o[1]:.1e}, eliminated eigenvalue >= {o[2]:.1f}, halving ratio {o[3]:.2f}" for o in out))

    # ---------------- G6 full edge form at the skew = EH of the skewed metric
    g0 = I4 + 0.2 * np.outer(US, US); Qe, Mh = regge(g0); C = compl(Mh(np.zeros(4)))
    Bm, *_ = census(2, 2, GROUPS['K48'])
    def FS(x, h, k):
        a = [schur(Qe(e * k), Mh(e * k), Mh(-e * k), C) / e ** 2 for e in (2e-3, 1e-3)]; S2 = (4 * a[1] - a[0]) / 3
        return float(np.real(x @ (0.5 * (S2 + S2.T)) @ x))
    cS, _ = fit(FS, Bm, nsamp=700); cE, _ = fit(lambda x, h, k: EH(h, k, g0), Bm, nsamp=700)
    lam = (cS @ cE) / (cE @ cE); mis = np.linalg.norm(cS - lam * cE) / np.linalg.norm(cS); tgt = -0.25 * np.sqrt(np.linalg.det(g0))
    check("G6 skew c = 0.2: full edge form with non-metric edges eliminated = -(1/4) sqrt(det g0) EH_g0",
          mis < 1e-6 and abs(lam - tgt) < 1e-6, f"coefficient {lam:+.6f} vs {tgt:+.6f}; misfit {mis:.1e}")


    # ---------------- G7 the D4 cone: a B4-symmetric, non-orthoscheme triangulation on the hypercubic geometry
    OFFd, Sd = d4cone(); Dc = Complex(OFFd, Sd)
    vol = sum(np.sqrt(np.linalg.det((lambda E: E @ E.T)(np.array([Dc.pos(v) for v in sm])[1:] - Dc.pos(sm[0])))) / 24 for sm in Sd)
    def canon(sm):
        P = sorted(tuple(np.round(2 * Dc.pos(v)).astype(int)) for v in sm); P = np.array(P)
        sh = np.floor_divide(P.min(axis=0), 2) * 2; return tuple(map(tuple, P - sh))
    base = {canon(sm) for sm in Sd}; ok_sym = True
    for g in GROUPS['B4']:
        for sm in Sd:
            P = np.array([g @ Dc.pos(v) for v in sm]); P2 = sorted(tuple(np.round(2 * p).astype(int)) for p in P); P2 = np.array(P2)
            sh = np.floor_divide(P2.min(axis=0), 2) * 2
            if tuple(map(tuple, P2 - sh)) not in base: ok_sym = False; break
        if not ok_sym: break
    def is_ortho(sm):
        P = np.array([Dc.pos(v) for v in sm])
        for perm in itertools.permutations(range(5)):
            st = [P[perm[i + 1]] - P[perm[i]] for i in range(4)]
            if all(abs(st[i] @ st[j]) < 1e-12 for i in range(4) for j in range(i + 1, 4)): return True
        return False
    n_ortho = sum(is_ortho(sm) for sm in Sd)
    check("G7 D4 cone (D4 = Z^4 u (Z^4 + u/2), Delaunay 16-cells coned from their centres): tiles the cell, invariant under all 384 signed axis permutations, no orthoschemes",
          abs(vol - 1) < 1e-12 and ok_sym and n_ortho == 0 and Dc.E == 72 and len(Sd) == 96,
          f"{len(Sd)} simplices, volume {vol:.12f}, {Dc.E} edges, {len(Dc.types)} vertex types; orthoschemes {n_ortho}")

    # ---------------- G8 null directions = vertex displacements
    res = []
    for k in [0.4 * rr.standard_normal(4), np.array([0.7, 0, 0, 0.0]), np.array([1.2, -0.6, 0.3, 0.9])]:
        s_ = np.sort(np.linalg.svd(Dc.Q(k), compute_uv=False)); s_ = s_ / s_[-1]
        res.append((int((s_ < 1e-8).sum()), s_[32] / max(s_[31], 1e-300), np.linalg.matrix_rank(Dc.gauge(k), tol=1e-9)))
    check("G8 D4 cone: edge-form nullity = 32 = rank of the vertex displacements at three momenta (no unseen curvature)",
          all(r[0] == 32 and r[2] == 32 and r[1] > 1e5 for r in res), "; ".join(f"nullity {r[0]}, gauge rank {r[2]}, gap {r[1]:.0e}" for r in res))

    # ---------------- G9 leading symbol
    A0 = np.hstack([Dc.line_map(np.zeros(4)), Dc.gauge(np.zeros(4))]).real
    u_, s_, _ = np.linalg.svd(A0); Cd = u_[:, int((s_ > 1e-9 * s_[0]).sum()):]
    def sd(k):
        Q = Dc.Q(k); Mp, Mm = Dc.line_map(k), Dc.line_map(-k)
        return Mm.T @ Q @ Mp - (Mm.T @ Q @ Cd) @ np.linalg.solve(Cd.T @ Q @ Cd, Cd.T @ Q @ Mp)
    Bm4, *_ = census(2, 2, GROUPS['B4'])
    def F_full(x, h, k):
        a = [sd(e * k) / e ** 2 for e in (2e-2, 1e-2)]; S2 = (4 * a[1] - a[0]) / 3
        return float(np.real(x @ (0.5 * (S2 + S2.T)) @ x))
    cS, _ = fit(F_full, Bm4, nsamp=700); cE, _ = fit(lambda x, h, k: EH(h, k, I4), Bm4, nsamp=700)
    lam = (cS @ cE) / (cE @ cE); mis = np.linalg.norm(cS - lam * cE) / np.linalg.norm(cS)
    check("G9 D4 cone: full edge form (non-metric, non-gauge edges eliminated) has O(k^2) symbol -(1/4) EH",
          abs(lam + 0.25) < 1e-4 and mis < 1e-4, f"coefficient {lam:+.6f}; misfit {mis:.1e} (Richardson from |k| = 0.02, 0.01)")

    # ---------------- G10 P1 scalar on the D4 cone: real energies, no on-shell k^4 term
    def on_shell(ks, guess):
        f = lambda kt: np.linalg.det(p1_scalar(Dc, np.array([*ks, kt])))
        x = guess
        for _ in range(80):
            h = 1e-7; st = f(x) / ((f(x + h) - f(x - h)) / (2 * h)); x -= st
            if abs(st) < 1e-14: break
        k = np.array([*ks, x]); w, V = np.linalg.eig(p1_scalar(Dc, k)); i = np.argmin(abs(w)); return k, V[:, i]
    worst_re, worst_a = 0.0, 0.0
    for n in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n)
        for km in (0.2, 0.1):
            k, _ = on_shell(km * n, 1j * km); worst_re = max(worst_re, abs(k[3].real))
            worst_a = max(worst_a, abs((abs(k[3]) ** 2 / km ** 2 - 1) / km ** 2))
    check("G10 D4 cone: P1 scalar on-shell tick momentum pure imaginary (real energies) and no O(k^4) on-shell correction (4 directions)",
          worst_re < 1e-12 and worst_a < 1e-3, f"max |Re k_t| {worst_re:.0e}; max |alpha| {worst_a:.1e}")

    # ---------------- G11 graviton shells and their non-metric partners
    def svn(k):
        s_ = np.sort(np.linalg.svd(Dc.Q(k), compute_uv=False)); return s_ / s_[-1]
    rows = {}
    for name, n in {'axis': (1, 0, 0), 'face': (1, 1, 0), 'body': (1, 1, 1)}.items():
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05; ks = km * n
        oms = km * np.linspace(0.999, 1.001, 241); f = np.array([svn(np.array([*ks, 1j * o]))[32] for o in oms])
        mins = [golden(lambda o: svn(np.array([*ks, 1j * o]))[32], oms[i - 1], oms[i + 1]) for i in range(1, 240) if f[i] < f[i - 1] and f[i] < f[i + 1]]
        out = []
        for w in mins:
            k = np.array([*ks, 1j * w]); _, s_, vh = np.linalg.svd(Dc.Q(k)); s_ = s_[::-1] / s_[0]
            nul = int((s_ < 1e-9).sum()); N = vh[-nul:].conj().T; G = Dc.gauge(k)
            X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :nul - 32]
            A = np.hstack([Dc.line_map(k), G]); sh = np.linalg.svd(A @ np.linalg.pinv(A, rcond=1e-10) @ X, compute_uv=False)
            out.append(((w * w / km ** 2 - 1) / km ** 2, nul, sh))
        rows[name] = out
    ax, fa, bo = rows['axis'], rows['face'], rows['body']
    ok11 = (len(ax) == 2 and abs(ax[0][0] + 1 / 12) < 2e-3 and abs(ax[1][0] - 1 / 12) < 2e-3 and all(r[1] == 34 and r[2][0] > 0.999 and r[2][-1] < 0.02 for r in ax)
            and len(fa) == 2 and abs(fa[0][0] + 1 / 16) < 2e-3 and abs(fa[1][0] - 1 / 16) < 2e-3
            and len(bo) >= 1 and all(abs(r[0]) < 2e-3 and r[1] == 35 for r in bo))
    check("G11 D4 cone graviton: two real shells omega^2 = k^2 (1 -+ c k^2), each with one metric and one non-metric null direction; c = 1/12 (axis), 1/16 (face), 0 (body, nullity 35)",
          ok11, "; ".join(f"{nm}: " + ", ".join(f"alpha {r[0]:+.4f} nullity {r[1]}" for r in rows[nm]) for nm in rows))

    # ---------------- G12 the two non-metric massless modes couple to matter only at relative order k
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
    for s in (0.02, 0.01):
        Qh_ = Dc.Q(s * kd); w = np.linalg.eigvalsh(0.5 * (Qh_ + Qh_.conj().T)); ev.append(np.sort(np.abs(w)))
    n_soft = int(sum(abs(ev[0][i] / ev[1][i] - 4) < 0.05 for i in range(32, 60)))
    n1, n2 = rr.standard_normal(3), rr.standard_normal(3); fr = []
    for s in (0.1, 0.05):
        k1, p1 = on_shell(s * n1 / np.linalg.norm(n1), 1j * s); k2, p2 = on_shell(0.7 * s * n2 / np.linalg.norm(n2), 0.7j * s)
        J = p1_stress(Dc, k1, p1, k2, p2); q = k1 - k2
        w, V = np.linalg.eig(Dc.Q(q)); Vs = V[:, np.argsort(np.abs(w))[:40]]
        A = np.hstack([Dc.line_map(q), Dc.gauge(q)]); P = np.eye(Dc.E) - A @ np.linalg.pinv(A, rcond=1e-10)
        X = np.linalg.svd(P @ Vs)[0][:, :2]; fr.append(np.linalg.norm(X.conj().T @ J) / np.linalg.norm(J))
    check("G12 D4 cone: 8 massless non-gauge directions (6 metric + 2 non-metric); on-shell P1 stress overlap with the 2 non-metric ones falls linearly in k",
          n_soft == 8 and abs(fr[0] / fr[1] - 2) < 0.25, f"massless count {n_soft}; overlap {fr[0]:.2e} -> {fr[1]:.2e} on halving")


    # ---------------- G13 P1 matter on every D4-cone vertex sources the non-site vertex displacements
    n1, n2 = rr.standard_normal(3), rr.standard_normal(3); rows13 = []
    for s in (0.1, 0.05):
        k1, p1 = on_shell(s * n1 / np.linalg.norm(n1), 1j * s); k2, p2 = on_shell(0.7 * s * n2 / np.linalg.norm(n2), 0.7j * s)
        J = p1_stress(Dc, k1, p1, k2, p2); G = Dc.gauge(k1 - k2)
        Ga = sum(G[:, 4 * t:4 * t + 4] for t in range(len(Dc.types)))
        rows13.append((np.linalg.norm(G.T @ J) / np.linalg.norm(J), np.linalg.norm(Ga.T @ J) / np.linalg.norm(J)))
    check("G13 D4 cone, P1 matter on all vertices: on-shell stress has an O(1) component along vertex displacements (relative motions of the vertex types), the uniform part only O(k)",
          all(r[0] > 0.5 for r in rows13) and abs(rows13[0][1] / rows13[1][1] - 2) < 0.3,
          "; ".join(f"all {r[0]:.2f}, uniform {r[1]:.1e}" for r in rows13))

    # ---------------- G14 site-cell metric coupling
    kq = np.array([0.3, -0.2, 0.1, 0.25]); Lq = site_metric(Dc, kq); Gq = Dc.gauge(kq)
    blind = np.abs(Lq @ np.hstack([Gq[:, 4 * t:4 * t + 4] for t in range(1, 8)])).max()
    exact = np.abs(site_metric(Dc, np.zeros(4)) @ Dc.line_map(np.zeros(4)) - np.eye(10)).max()
    check("G14 site-cell metric (axis edges and both face diagonals through the holes): blind to every non-site vertex displacement, exact on constant metrics",
          blind < 1e-12 and exact < 1e-12, f"|L G_nonsite| {blind:.0e}; |L M(0) - 1| {exact:.0e}")

    # ---------------- G15 static response through the site metric: graviton + a conformal partner
    itt, ixx = HC.index((3, 3)), HC.index((0, 0)); out15 = []
    for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        Q = Dc.Q(kk); w, V = np.linalg.eigh(0.5 * (Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
        A = np.hstack([Dc.line_map(kk), Dc.gauge(kk)]); P = np.eye(Dc.E) - A @ np.linalg.pinv(A, rcond=1e-10)
        partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
        Lk = site_metric(Dc, kk); T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
        gov = np.linalg.norm(Dc.gauge(kk).conj().T @ J) / np.linalg.norm(J)
        x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x)
        hg, hp = Lk @ (x - xp), Lk @ xp; k2 = kk @ kk
        pat = (hp / hp[itt]).real; conf = np.abs(pat - np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])).max()
        out15.append((gov, hg[itt].real * k2, hg[ixx].real / hg[itt].real, hp[itt].real * k2, conf, ((hg + hp)[ixx] / (hg + hp)[itt]).real))
    check("G15 static T_tt through the site metric: no overlap with null directions; graviton h_tt k^2 = -2 with h_xx = -h_tt; partner adds -2/3 with conformal pattern 1; total h_xx/h_tt = -1/2",
          all(o[0] < 1e-12 and abs(o[1] + 2) < 2e-3 and abs(o[2] + 1) < 2e-3 and abs(o[3] + 2 / 3) < 2e-3 and o[4] < 1e-3 and abs(o[5] + 0.5) < 2e-3 for o in out15),
          "; ".join(f"overlap {o[0]:.0e}, graviton {o[1]:+.4f} (h_xx/h_tt {o[2]:+.4f}), partner {o[3]:+.4f} (pattern dev {o[4]:.0e}), total h_xx/h_tt {o[5]:+.4f}" for o in out15))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
