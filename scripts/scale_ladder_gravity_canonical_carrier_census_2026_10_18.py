#!/usr/bin/env python3
"""Finite supplied-model geometry and numerical diagnostics.
The companion note defines the precise fixtures and deferred claims.
No continuum limit, universal spectral census, OS reconstruction, or physical identification is certified.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_CANONICAL_CARRIER_CENSUS_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/work_history/repo/review_feedback/GRAVITY_REVIEW_SCOPE_AND_RECOVERY_2026-10-18.md', 'archive/gravity_review_2026_10_18/MANIFEST.json', 'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md')

import itertools, math, sys
import numpy as np
import scipy.linalg as sl
from scipy.spatial import Delaunay, ConvexHull

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


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


# ------------------------------------------------------------------ Whitney forms of every degree


def canon(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0]))
    b0 = np.array(vs[0][0])
    key = tuple((t, tuple(np.subtract(b, b0))) for b, t in vs)
    return key, tuple(b0), vs

class Forms:
    def __init__(self, C):
        self.C = C
        self.cls = [dict() for _ in range(5)]      # degree k -> {key: index}
        for s in C.simp:
            for k in range(5):
                for sub in itertools.combinations(s, k + 1):
                    key, _, _ = canon(list(sub))
                    if key not in self.cls[k]: self.cls[k][key] = len(self.cls[k])
        self.n = [len(c) for c in self.cls]
        # coboundary terms: for each (k+1)-class tau (at anchor 0), faces = drop one vertex
        self.dterms = []
        for k in range(4):
            terms = []
            for key, ti in self.cls[k + 1].items():
                verts = [(b, t) for t, b in key]
                for j in range(len(verts)):
                    face = verts[:j] + verts[j + 1:]
                    fkey, fanc, fsorted = canon(face)
                    # sign: orientation of face as it appears in tau (order induced) vs canonical order
                    perm = [fsorted.index(v) for v in face]
                    sign = (-1) ** j * self._perm_sign(perm)
                    terms.append((ti, self.cls[k][fkey], np.array(fanc, float), sign))
            self.dterms.append(terms)
        # mass-matrix terms per 4-simplex
        self.mterms = [[] for _ in range(5)]
        for s in C.simp:
            P = np.array([C.pos(v) for v in s]); E = P[1:] - P[0]
            vol = abs(np.linalg.det(E)) / 24
            Einv = np.linalg.inv(E)
            grads = [-(Einv.sum(axis=1))] + [Einv[:, i] for i in range(4)]
            Gg = np.array([[gi @ gj for gj in grads] for gi in grads])
            Ill = vol * (np.ones((5, 5)) + np.eye(5)) / 30.0           # int lambda_a lambda_b
            for k in range(5):
                subs = list(itertools.combinations(range(5), k + 1))
                info = []
                for sub in subs:
                    vs = [s[i] for i in sub]; key, anc, srt = canon(vs)
                    perm = [srt.index(v) for v in vs]; sg = self._perm_sign(perm)
                    info.append((self.cls[k][key], np.array(anc, float), sg, sub))
                for (ca, aa, sa, A) in info:
                    for (cb, ab, sb, Bs) in info:
                        val = 0.0
                        for j, ia in enumerate(A):
                            Ar = [x for x in A if x != ia]
                            for l, ib in enumerate(Bs):
                                Br = [x for x in Bs if x != ib]
                                det = np.linalg.det(Gg[np.ix_(Ar, Br)]) if k > 0 else 1.0
                                val += (-1) ** (j + l) * Ill[ia, ib] * det
                        val *= math.factorial(k) ** 2 * sa * sb
                        if abs(val) > 1e-15: self.mterms[k].append((ca, cb, aa, ab, val))

    @staticmethod
    def _perm_sign(p):
        p = list(p); s = 1
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
        return s

    def d(self, k, q):
        q = np.asarray(q, complex); D = np.zeros((self.n[k + 1], self.n[k]), complex)
        for ti, fi, fanc, sg in self.dterms[k]: D[ti, fi] += sg * np.exp(1j * q @ fanc)
        return D

    def M(self, k, q):
        q = np.asarray(q, complex); Mm = np.zeros((self.n[k], self.n[k]), complex)
        for ca, cb, aa, ab, v in self.mterms[k]:
            Mm[ca, cb] += v * np.exp(1j * q @ (ab - aa))
        return Mm

    def hodge(self, k, q):
        """stiffness K_k = d_k^dag M_{k+1} d_k + M_k d_{k-1} M_{k-1}^{-1} d_{k-1}^dag M_k (holomorphic: dag -> (-q)^T)."""
        q = np.asarray(q, complex); Mk = self.M(k, q); K = np.zeros_like(Mk)
        if k < 4:
            K += self.d(k, -q).T @ self.M(k + 1, q) @ self.d(k, q)
        if k > 0:
            Dm = self.d(k - 1, q); Dmm = self.d(k - 1, -q)
            K += Mk @ Dm @ np.linalg.solve(self.M(k - 1, q), Dmm.T @ Mk)
        return K, Mk


# ------------------------------------------------------------------ canonical symmetric triangulations


TOL = 1e-8
E4 = np.eye(4)

def orbit_offsets(which):
    """which: subset of {1,2,3,4}: half-integer orbits with that many 1/2 coordinates."""
    offs = [np.zeros(4)]
    for r in sorted(which):
        for S in itertools.combinations(range(4), r):
            v = np.zeros(4); v[list(S)] = 0.5; offs.append(v)
    return offs

def patch(offs, lo=-2, hi=3):
    pts = []
    for b in itertools.product(range(lo, hi), repeat=4):
        for o in offs: pts.append(np.array(b, float) + o)
    return np.array(pts)

def circumcenter(P):
    """centre of the sphere through the points P (m x 4), within their affine hull."""
    p0 = P[0]; A = P[1:] - p0
    # x = p0 + A^T y ; |x - p_i|^2 equal  ->  2 A A^T y = |A_i|^2
    G = A @ A.T; b = 0.5 * np.einsum('ij,ij->i', A, A)
    y = np.linalg.lstsq(G, b, rcond=None)[0]
    return p0 + A.T @ y

def local_frame(P):
    c = P.mean(axis=0); u, s, vt = np.linalg.svd(P - c)
    d = int((s > TOL).sum()); return c, vt[:d]

def facets(P):
    """facets of the convex polytope with vertex set P (points spanning their affine hull)."""
    c, B = local_frame(P); X = (P - c) @ B.T; d = B.shape[0]
    if d == 1:
        i, j = np.argmin(X[:, 0]), np.argmax(X[:, 0]); return [P[[i]], P[[j]]]
    hull = ConvexHull(X)
    groups = {}
    for eq in hull.equations:
        key = tuple(np.round(eq / np.linalg.norm(eq[:-1]), 7))
        groups[key] = eq
    out = []
    for eq in groups.values():
        on = np.abs(X @ eq[:-1] + eq[-1]) < 1e-7
        out.append(P[on])
    return out

def subdivide(P):
    """symmetric triangulation of the polytope conv(P) (P cospherical vertex set) -> list of point arrays."""
    c, B = local_frame(P); d = B.shape[0]
    if len(P) == d + 1: return [P]
    cc = circumcenter(P)
    out = []
    for F in facets(P):
        for s in subdivide(F):
            t = np.vstack([s, cc])
            if np.linalg.matrix_rank(t[1:] - t[0], tol=1e-9) == len(t) - 1: out.append(t)   # drop flat cones
    return out

def delaunay_cells(offs):
    pts = patch(offs)
    tri = Delaunay(pts, qhull_options='Qbb Qc Qz Q12 Qt')
    cells = {}
    for simp in tri.simplices:
        P = pts[simp]
        if abs(np.linalg.det(P[1:] - P[0])) < 1e-9: continue           # flat sliver from Qt
        cc = circumcenter(P); r = np.linalg.norm(P[0] - cc)
        if np.any(cc < -0.01) or np.any(cc > 1.01): continue      # keep cells whose centre is near the base cell
        key = tuple(np.round(cc, 6))
        if key in cells: continue
        # all patch points on that sphere = the Delaunay cell
        on = np.abs(np.linalg.norm(pts - cc, axis=1) - r) < 1e-6
        cells[key] = (cc, pts[on])
    # one representative per translation class: circumcentre in [0,1)^4
    reps = {}
    for key, (cc, P) in cells.items():
        f = np.mod(np.round(cc, 6), 1.0); f[np.abs(f - 1) < 1e-9] = 0
        k2 = tuple(np.round(f, 6))
        if k2 not in reps: reps[k2] = (cc, P - (cc - f))
    return list(reps.values())

def build(which):
    offs = orbit_offsets(which)
    cells = delaunay_cells(offs)
    simps = []
    for cc, P in cells:
        simps += subdivide(P)
    # vertex types by fractional position
    types = {}
    def vid(x):
        f = np.mod(np.round(x * 840) / 840, 1.0); key = tuple(np.round(f, 6))
        if key not in types: types[key] = len(types)
        b = tuple(int(v) for v in np.round(x - np.array(key)))
        return (b, types[key])
    base = [[vid(x) for x in s] for s in simps]
    OFF = [np.array(k) for k, _ in sorted(types.items(), key=lambda kv: kv[1])]
    vol = sum(abs(np.linalg.det(s[1:] - s[0])) / 24 for s in simps)
    return OFF, base, vol, len(cells), [len(P) for _, P in cells]


# ------------------------------------------------------------------ helpers for the census
B4 = []
for _p in itertools.permutations(range(4)):
    for _s in itertools.product([1, -1], repeat=4):
        _M = np.zeros((4, 4))
        for _i in range(4): _M[_p[_i], _i] = _s[_i]
        B4.append(_M)


def b4_symmetric(C):
    def canon_pts(P):
        P2 = np.array(sorted(tuple(np.round(840 * p).astype(int)) for p in P)); sh = np.floor_divide(P2.min(axis=0), 840) * 840
        return tuple(map(tuple, P2 - sh))
    base = {canon_pts([C.pos(v) for v in s]) for s in C.simp}
    return all(canon_pts([g @ C.pos(v) for v in s]) in base for g in B4 for s in C.simp)


def profile(C, ngauge=None):
    """(nullity, gauge rank, massless non-gauge count) of the Regge edge form."""
    q = np.array([0.31, -0.22, 0.17, 0.4]); s = np.sort(np.linalg.svd(C.Q(q), compute_uv=False)); s = s / s[-1]
    nul = int((s < 1e-8).sum()); grk = np.linalg.matrix_rank(C.gauge(q), tol=1e-9)
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
    for x in (0.02, 0.01):
        Q = C.Q(x * kd); w = np.linalg.eigvalsh(0.5 * (Q + Q.conj().T)); ev.append(np.sort(np.abs(w)))
    soft = int(sum(1 for i in range(nul, min(nul + 40, C.E)) if abs(ev[0][i] / ev[1][i] - 4) < 0.1 and ev[1][i] < 1e-2))
    return nul, grk, soft


def k4_form_residue(C):
    """max over degrees and two directions of |lambda(omega = k)|/k^4 for the C(4,k) lowest Hodge eigenvalues at |k| = 0.025."""
    F = Forms(C); worst = 0.0
    for n in [(1, 0, 0), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.025
        for j in range(5):
            K, M = F.hodge(j, np.array([*(km * n), 1j * km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            worst = max(worst, w[math.comb(4, j) - 1] / km ** 4)
    return worst


def comp_inv(Q, G, J):
    Pq, _ = np.linalg.qr(G); n = Q.shape[0]
    Pc = np.linalg.svd(np.eye(n) - Pq @ Pq.conj().T)[0][:, :n - G.shape[1]]
    return Pc @ np.linalg.solve(Pc.conj().T @ Q @ Pc, Pc.conj().T @ J)


def rp_vertex(Qfun, offs_t, ks, Nt, t0):
    kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    half = [(bt, tau, bt + ot) for bt in range(-1, Nt // 2 + 1) for tau, ot in enumerate(offs_t)
            if t0 - 1e-9 <= bt + ot <= t0 + Nt / 2 + 1e-9]
    R = np.zeros((len(half),) * 2, complex)
    for a, (bt1, ta, _) in enumerate(half):
        for b, (bt2, tb, t2) in enumerate(half):
            R[a, b] = G(bt1 - int(round(2 * t0 - t2 - offs_t[tb])))[ta, tb]
    return R


def main():
    built = {}
    def get(which):
        if which not in built:
            OFF, base, vol, ncell, sizes = build(which); built[which] = (Complex(OFF, base), vol, len(base))
        return built[which]
    # K1 finite fixture; see companion inventory.
    C4, vol4, n4 = get((4,))
    check("K1 finite supplied-model control; fixture and predicate specified in source",
          n4 == 96 and len(C4.types) == 8 and abs(vol4 - 1) < 1e-9 and C4.E == 72, f"{n4} simplices, {len(C4.types)} vertex types, {C4.E} edges, volume {vol4:.6f}")
    # K2 finite fixture; see companion inventory.
    expect = {(): (1, 0), (1,): (0, 0), (2,): (0, 2), (3,): (0, 0), (4,): (0, 2)}
    rows, ok2 = [], True
    for which, (eh, ep) in expect.items():
        C, vol, n = get(which); nul, grk, soft = profile(C); sym = b4_symmetric(C)
        hid, par = nul - grk, soft - 6; ok2 &= (hid == eh and par == ep and sym and abs(vol - 1) < 1e-9)
        rows.append(f"{set(which) or '{}'}: hidden {hid}, partners {par}, B4 {sym}")
    check("K2 finite supplied-model control; fixture and predicate specified in source",
          ok2, "; ".join(rows))
    # K3 finite fixture; see companion inventory.
    res = {w: k4_form_residue(get(w)[0]) for w in [(4,), (2,), (1,), (3,)]}
    check("K3 finite supplied-model control; fixture and predicate specified in source",
          res[(4,)] < 1e-4 and res[(2,)] < 1e-4 and res[(1,)] > 1e-3 and res[(3,)] > 1e-3, "; ".join(f"{set(w)}: {v:.1e}" for w, v in res.items()))
    # K4 finite fixture; see companion inventory.
    C1 = get((1,))[0]; site = [i for i, o in enumerate(C1.OFF) if np.allclose(o, 0)][0]
    def Gns(k):
        G = C1.gauge(k); return np.hstack([G[:, 4 * t:4 * t + 4] for t in range(len(C1.types)) if t != site])
    def reading(k, W):
        A = np.hstack([C1.line_map(k), Gns(k)]); return np.linalg.solve(A.conj().T @ W @ A, A.conj().T @ W)[:10]
    rng = np.random.default_rng(0); Ws = [np.eye(C1.E), np.diag(rng.uniform(0.2, 5, C1.E))]
    itt, ixx = 3, 0; out = []
    for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        for W in Ws:
            L = reading(kk, W); T = np.zeros(10); T[itt] = 1.0
            h = L @ comp_inv(C1.Q(kk), C1.gauge(kk), L.conj().T @ T); out.append((h[itt].real * (kk @ kk), (h[ixx] / h[itt]).real))
    check("K4 finite supplied-model control; fixture and predicate specified in source",
          all(abs(a + 2) < 1e-3 and abs(b + 1) < 1e-3 for a, b in out), "; ".join(f"{a:+.4f}/{b:+.4f}" for a, b in out))
    # K5 finite fixture; see companion inventory.
    tix = {t: i for i, t in enumerate(C1.types)}; wv = np.zeros(len(C1.types))
    for vs in C1.simp:
        P = np.array([C1.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for v in vs: wv[tix[v[1]]] += vol / 5
    offs_t = [float(o[3]) for o in C1.OFF]; mn = 1.0
    for ks in [np.zeros(3), np.array([0.7, -0.3, 0.2])]:
        for t0 in (0.0, 0.5):
            R = rp_vertex(lambda k: p1_scalar(C1, k) + 0.3 * np.diag(wv), offs_t, ks, 6, t0)
            w = np.linalg.eigvalsh(0.5 * (R + R.conj().T)); mn = min(mn, w.min() / abs(w).max())
    check("K5 finite supplied-model control; fixture and predicate specified in source", mn > -1e-12, f"min/max eigenvalue {mn:+.1e}")
    # K6 finite fixture; see companion inventory.
    from fractions import Fraction
    def zoom(C):
        den = 1
        for o in C.OFF:
            for x in o: den = int(np.lcm(den, Fraction(float(x)).limit_denominator(840).denominator))
        return den, len({tuple(int(round(v * den)) % den for v in o) for o in C.OFF})
    z1, z4 = zoom(C1), zoom(C4)
    residues1 = {tuple(int(round(2*x)) % 2 for x in o) for o in C1.OFF}
    residues4 = {tuple(int(round(2*x)) % 2 for x in o) for o in C4.OFF}
    binary = set(itertools.product((0, 1), repeat=4))
    parity_ok = residues1 == binary and residues4 == {v for v in binary if sum(v) % 2 == 0}
    check("K6 finite supplied-model control; fixture and predicate specified in source",
          z1 == (2, 16) and z4 == (2, 8) and parity_ok, f"link-midpoint carrier: zoom {z1[0]}, {z1[1]} of 16 residues; D4 cone: zoom {z4[0]}, {z4[1]} of 16")
    # K7 finite fixture; see companion inventory.
    tix1 = {t: i for i, t in enumerate(C1.types)}
    def on_shell(ks, guess):
        f = lambda kt: np.linalg.det(p1_scalar(C1, np.array([*ks, kt])))
        x = guess
        for _ in range(80):
            hh = 1e-7; st = f(x) / ((f(x + hh) - f(x - hh)) / (2 * hh)); x -= st
            if abs(st) < 1e-14: break
        k = np.array([*ks, x]); w, V = np.linalg.eig(p1_scalar(C1, k)); return k, V[:, np.argmin(abs(w))]
    def stress(k1, f1, k2, f2):
        qv = k1 - k2; J = np.zeros(C1.E, complex)
        for vs in C1.simp:
            P = np.array([C1.pos(v) for v in vs]); E_ = P[1:] - P[0]; Gm = E_ @ E_.T; Gi = np.linalg.inv(Gm)
            v2 = np.array([f2[tix1[v[1]]] * np.exp(1j * k2 @ np.array(v[0], float)) for v in vs])
            v1 = np.array([f1[tix1[v[1]]] * np.exp(-1j * k1 @ np.array(v[0], float)) for v in vs])
            d2 = v2[1:] - v2[0]; d1 = v1[1:] - v1[0]; X = d1 @ Gi @ d2
            Pm = np.outer(Gi @ d2, Gi @ d1); Pm = 0.5 * (Pm + Pm.T); Psi = np.sqrt(np.linalg.det(Gm)) / 24 * (0.5 * Gi * X - Pm)
            for i, j in itertools.combinations(range(5), 2):
                key, anc = _key_pair(vs[i], vs[j]); c = C1.ekey[key]
                dl2 = 2 * np.linalg.norm(P[j] - P[i]) * np.exp(1j * qv @ np.array(anc, float)); dG = np.zeros((4, 4), complex)
                if i == 0:
                    dG[j - 1, j - 1] += dl2
                    for b in range(4):
                        if b != j - 1: dG[j - 1, b] += dl2 / 2; dG[b, j - 1] += dl2 / 2
                else:
                    dG[i - 1, j - 1] -= dl2 / 2; dG[j - 1, i - 1] -= dl2 / 2
                J[c] += np.sum(Psi * dG)
        return J
    rng = np.random.default_rng(9); n1, n2 = rng.standard_normal(3), rng.standard_normal(3); fr = []; residuals = []
    for s in (0.1, 0.05, 0.025):
        k1, f1 = on_shell(s * n1 / np.linalg.norm(n1), 1j * s); k2, f2 = on_shell(0.7 * s * n2 / np.linalg.norm(n2), 0.7j * s)
        wleft, Vleft = np.linalg.eig(p1_scalar(C1, -k1)); left = Vleft[:, np.argmin(abs(wleft))]
        left /= np.linalg.norm(left); left *= np.exp(-1j * np.angle(left[np.argmax(abs(left))]))
        residuals.append((np.linalg.norm(left @ p1_scalar(C1, k1)), np.linalg.norm(p1_scalar(C1, k2) @ f2)))
        J = stress(k1, left, k2, f2); Gq = C1.gauge(k1 - k2); Ga = sum(Gq[:, 4 * t:4 * t + 4] for t in range(len(C1.types)))
        fr.append((np.linalg.norm(Gq.T @ J) / np.linalg.norm(J), np.linalg.norm(Ga.T @ J) / np.linalg.norm(J)))
    check("K7 finite supplied-model control; fixture and predicate specified in source",
          max(max(r) for r in residuals) < 1e-10 and all(0 < x < 3e-5 for r in fr for x in r) and all(7.5 < fr[i][j] / fr[i+1][j] < 8.5 for i in range(2) for j in range(2)), "left/right residuals " + repr(residuals) + "; (all, uniform) " + repr(fr))
    print("per_element: explicit simplex geometry and local matrix entries are computed on the supplied finite carrier; no microscopic interaction supplier is derived")
    print("per_site: listed vertex types and periodic-cell incidences are included; arbitrary lattice defects and unspecified site models are untested")
    print("per_mode: only the literal momentum fixtures, thresholds and finite scans above are tested; no complete zero-set or spectrum census is certified")
    print("per_block: the displayed cell operators and source or covariance contractions are evaluated; numerical pass labels do not supply an interacting physical theory")
    print("lattice_wide: finite periodic-symbol diagnostics and explicitly stated constructive identities only; thermodynamic limits, all-volume OS positivity and physical reconstruction remain deferred")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
