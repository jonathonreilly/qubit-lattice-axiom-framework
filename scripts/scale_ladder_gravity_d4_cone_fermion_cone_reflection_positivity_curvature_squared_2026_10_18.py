#!/usr/bin/env python3
"""Finite supplied-model geometry and numerical diagnostics.
The companion note defines the precise fixtures and deferred claims.
No continuum limit, universal spectral census, OS reconstruction, or physical identification is certified.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_D4_CONE_FERMION_CONE_REFLECTION_POSITIVITY_CURVATURE_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/work_history/repo/review_feedback/GRAVITY_REVIEW_SCOPE_AND_RECOVERY_2026-10-18.md', 'archive/gravity_review_2026_10_18/MANIFEST.json', 'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md')

import itertools, math, sys
import numpy as np
import scipy.linalg as sl

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

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


# ------------------------------------------------------------------ curvature-squared term, masses, readings
def R2(C, k):
    """sum over hinge classes of delta_h(-k) delta_h(k): the quadratic form of sum_h delta_h^2."""
    k = np.asarray(k, complex); M = np.zeros((C.E, C.E), complex)
    for a, d in C.terms:
        rp = np.zeros(C.E, complex); np.add.at(rp, d[0], d[2] * np.exp(1j * (d[1] @ k)))
        rm = np.zeros(C.E, complex); np.add.at(rm, d[0], d[2] * np.exp(-1j * (d[1] @ k)))
        M += np.outer(rm, rp)
    return M


def lumped_mass(C):
    tix = {t: i for i, t in enumerate(C.types)}; w = np.zeros(len(C.types))
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for v in vs: w[tix[v[1]]] += vol / 5
    return np.diag(w)


def consistent_mass(C, k):
    k = np.asarray(k, complex); tix = {t: i for i, t in enumerate(C.types)}; M = np.zeros((len(C.types),) * 2, complex)
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for i in range(5):
            for j in range(5):
                M[tix[vs[i][1]], tix[vs[j][1]]] += vol * (2 if i == j else 1) / 30 * np.exp(1j * k @ (np.array(vs[j][0], float) - np.array(vs[i][0], float)))
    return M


def comp_inv(Q, G, J):
    """solve Q x = J on the orthogonal complement of the exact null directions G."""
    Pq, _ = np.linalg.qr(G); n = Q.shape[0]
    Pc = np.linalg.svd(np.eye(n) - Pq @ Pq.conj().T)[0][:, :n - G.shape[1]]
    return Pc @ np.linalg.solve(Pc.conj().T @ Q @ Pc, Pc.conj().T @ J)


def face_metric(C, k):
    """D4 cone: site-cell metric from axis edges and both face diagonals, each read through the deep hole it crosses."""
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


def kuhn_reading(K, k, relative=True):
    """Kuhn complex: least-squares metric from the 15 edge classes (relative or plain strains)."""
    l = np.array([np.linalg.norm(K.evec[c]) for c in range(K.E)]); M = K.line_map(k)
    W = np.diag(1 / l ** 2) if relative else np.eye(K.E)
    return np.linalg.pinv(W @ M) @ W


# ------------------------------------------------------------------ OS reflection positivity of Gaussian fields
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


def rp_forms(F, k, Qfun, ks, Nt, t0):
    C = F.C; kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    reps = sorted((ci, [(np.array(b, float), t) for t, b in key]) for key, ci in F.cls[k].items())
    half = []
    for bt in range(-2, Nt // 2 + 2):
        for ci, verts in reps:
            ts = [bt + v[0][3] + C.OFF[v[1]][3] for v in verts]
            if min(ts) >= t0 - 1e-9 and max(ts) <= t0 + Nt / 2 + 1e-9:
                half.append((bt, ci, [(tuple(int(x) for x in v[0] + np.array([0, 0, 0, bt])), v[1]) for v in verts]))
    img = []
    for bt, ci, verts in half:
        rv = []
        for b, t in verts:
            p = np.array(b, float) + C.OFF[t]; p[3] = 2 * t0 - p[3]; rv.append((tuple(int(x) for x in np.round(p - C.OFF[t])), t))
        key, anc, srt = canon(rv)
        img.append((F.cls[k][key], anc, Forms._perm_sign([srt.index(v) for v in rv])))
    R = np.zeros((len(half),) * 2, complex)
    for a, (bt1, c1, _) in enumerate(half):
        for b, (c2, anc2, sg2) in enumerate(img):
            R[a, b] = sg2 * G(bt1 - anc2[3])[c1, c2] * np.exp(-1j * np.array(ks) @ np.array(anc2[:3], float))
    return R


def rel_min_eig(R):
    w = np.linalg.eigvalsh(0.5 * (R + R.conj().T)); return w.min() / abs(w).max()


def main():
    OFF, S = d4cone(); D = Complex(OFF, S); F = Forms(D)
    # J1 finite fixture; see companion inventory.
    q = np.array([0.31, -0.22, 0.17, 0.4])
    d2 = max(np.abs(F.d(k + 1, q) @ F.d(k, q)).max() for k in range(3))
    minm = min(np.linalg.eigvalsh(0.5 * (F.M(k, q) + F.M(k, q).conj().T)).min() for k in range(5))
    check("J1 finite supplied-model control; fixture and predicate specified in source",
          F.n == [8, 72, 208, 240, 96] and d2 < 1e-12 and sum((-1) ** k * F.n[k] for k in range(5)) == 0 and minm > 0,
          f"counts {F.n}; |d d| {d2:.0e}; min mass eigenvalue {minm:.2e}")
    # J2 finite fixture; see companion inventory.
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); rows = []
    for k in range(5):
        K, M = F.hodge(k, 0.01 * kd); w = np.sort(np.real(sl.eigvals(K, M)))
        ns = int((np.abs(w) < 1e-2).sum()); rows.append((ns, np.abs(w[:ns] / 1e-4 - 1).max() if ns else 1, w[ns]))
    check("J2 finite supplied-model control; fixture and predicate specified in source",
          [r[0] for r in rows] == [math.comb(4, k) for k in range(5)] and max(r[1] for r in rows) < 1e-3 and min(r[2] for r in rows) > 20,
          f"counts {[r[0] for r in rows]}; max |lambda/k^2 - 1| {max(r[1] for r in rows):.0e}; gap {min(r[2] for r in rows):.1f}")
    # J3 finite fixture; see companion inventory.
    worst = 0.0; nxt = np.inf
    for n in [(1, 0, 0), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05
        for k in range(5):
            K, M = F.hodge(k, np.array([*(km * n), 1j * km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            worst = max(worst, w[math.comb(4, k) - 1] / km ** 2); nxt = min(nxt, w[math.comb(4, k)] / km ** 2)
    check("J3 finite supplied-model control; fixture and predicate specified in source",
          worst < 1e-7 and nxt > 1e3, f"max |lambda|/k^2 {worst:.1e}; next {nxt:.1e}")
    # J4 finite fixture; see companion inventory.
    m2 = 0.3; Nt = 6; ksl = [np.array([0.0, 0.0, 0.0]), np.array([0.7, -0.3, 0.2])]
    nn = lambda k: np.array([[np.sum(4 * np.sin(np.asarray(k) / 2) ** 2) + m2]], complex)
    hd = lambda k: np.array([[(lambda L: L + 0.5 * L * L + m2)(np.sum(4 * np.sin(np.asarray(k) / 2) ** 2))]], complex)
    offs_t = [float(o[3]) for o in D.OFF]; ML = lumped_mass(D)
    c_nn = min(rel_min_eig(rp_vertex(nn, [0.0], ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    c_hd = max(rel_min_eig(rp_vertex(hd, [0.0], ks, Nt, 0.0)) for ks in ksl)
    c_cm = max(rel_min_eig(rp_vertex(lambda k: p1_scalar(D, k) + m2 * consistent_mass(D, k), offs_t, ks, Nt, 0.0)) for ks in ksl)
    check("J4 finite supplied-model control; fixture and predicate specified in source",
          c_nn > -1e-12 and c_hd < -1e-3 and c_cm < -1e-5, f"NN min/max {c_nn:+.0e}; higher-derivative {c_hd:+.1e}; consistent-mass P1 {c_cm:+.1e}")
    # J5 finite fixture; see companion inventory.
    s5 = min(rel_min_eig(rp_vertex(lambda k: p1_scalar(D, k) + m2 * ML, offs_t, ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    check("J5 finite supplied-model control; fixture and predicate specified in source",
          s5 > -1e-12, f"min/max eigenvalue over 2 momenta x 2 planes {s5:+.1e}")
    # J6 finite fixture; see companion inventory.
    Mdiag = np.diag(np.real(np.diag(F.M(1, np.zeros(4)))))
    proca = lambda q: F.d(1, -np.asarray(q, complex)).T @ F.M(2, q) @ F.d(1, q) + 0.5 * Mdiag
    procac = lambda q: F.d(1, -np.asarray(q, complex)).T @ F.M(2, q) @ F.d(1, q) + 0.5 * F.M(1, q)
    s6 = min(rel_min_eig(rp_forms(F, 1, proca, ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    c6 = rel_min_eig(rp_forms(F, 1, procac, ksl[1], Nt, 0.0))
    check("J6 finite supplied-model control; fixture and predicate specified in source",
          s6 > -1e-12 and c6 < -1e-5, f"min/max {s6:+.1e}; control {c6:+.1e}")
    # J7 finite fixture; see companion inventory.
    lam = -0.1; OFFk, Sk = kuhn(); K = Complex(OFFk, Sk); qg = np.array([0.3, -0.2, 0.25, 0.15])
    nk0 = int((np.sort(np.linalg.svd(K.Q(qg), compute_uv=False)) / np.abs(K.Q(qg)).max() < 1e-9).sum())
    sk = np.sort(np.linalg.svd(K.Q(qg) + lam * R2(K, qg), compute_uv=False)); nk = int((sk / sk[-1] < 1e-9).sum())
    Qd = D.Q(0.01 * kd) + lam * R2(D, 0.01 * kd); wd = np.linalg.eigvalsh(0.5 * (Qd + Qd.conj().T)); wd = wd[np.argsort(np.abs(wd))]
    Qd0 = D.Q(0.01 * kd); wd0 = np.linalg.eigvalsh(0.5 * (Qd0 + Qd0.conj().T)); wd0 = wd0[np.argsort(np.abs(wd0))]
    soft = int((np.abs(wd[32:]) < 1e-2).sum()); soft0 = int((np.abs(wd0[32:]) < 1e-2).sum())
    check("J7 finite supplied-model control; fixture and predicate specified in source",
          nk0 == 5 and nk == 4 and soft0 == 8 and soft == 6, f"Kuhn {nk0} -> {nk}; D4 {soft0} -> {soft}; D4 next eigenvalue {abs(wd[32 + soft]):.2f}")
    # J8 finite fixture; see companion inventory.
    def roots(C, ng, axis):
        vals = np.linspace(0.005, 3.0, 400); out = []
        def s_at(v):
            kk = np.array([0.05, 0.0, 0.0, (1j * v if axis == 'E' else v)])
            s_ = np.sort(np.linalg.svd(C.Q(kk) + lam * R2(C, kk), compute_uv=False)); return s_[ng] / s_[-1]
        f = np.array([s_at(v) for v in vals])
        return [vals[i] for i in range(1, len(vals) - 1) if f[i] < f[i - 1] and f[i] < f[i + 1] and f[i] < 1e-4]
    rk_t, rd_t = roots(K, 4, 'T'), roots(D, 32, 'T'); rk_e, rd_e = roots(K, 4, 'E'), roots(D, 32, 'E')
    check("J8 finite supplied-model control; fixture and predicate specified in source",
          not rk_t and not rd_t and min(abs(np.array(rk_e) - 0.05)) < 0.01 and min(abs(np.array(rd_e) - 0.05)) < 0.01,
          f"Kuhn real-energy roots {np.round(rk_e, 3).tolist()}; D4 {np.round(rd_e, 3).tolist()}")
    # J9 finite fixture; see companion inventory.
    itt, ixx = HC.index((3, 3)), HC.index((0, 0)); res = []
    for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        T = np.zeros(10); T[itt] = 1.0; k2 = kk @ kk
        for lab, Cx, Lk in (('D4 face', D, face_metric(D, kk)), ('Kuhn rel', K, kuhn_reading(K, kk, True)), ('Kuhn plain', K, kuhn_reading(K, kk, False))):
            x = comp_inv(Cx.Q(kk) + lam * R2(Cx, kk), Cx.gauge(kk), Lk.conj().T @ T); h = Lk @ x
            res.append((lab, h[itt].real * k2, (h[ixx] / h[itt]).real))
    check("J9 finite supplied-model control; fixture and predicate specified in source",
          all(abs(r[1] + 2) < 2e-3 and abs(r[2] + 1) < 2e-3 for r in res), "; ".join(f"{r[0]} {r[1]:+.4f}/{r[2]:+.4f}" for r in res))
    # J10 finite fixture; see companion inventory.
    kk = np.array([1.0, 0, 0, 0.0]); T = np.zeros(10); T[itt] = 1.0; Lk = face_metric(D, kk)
    h = (Lk @ comp_inv(D.Q(kk) + lam * R2(D, kk), D.gauge(kk), Lk.conj().T @ T))[itt].real
    nnv = 4 * np.sin(0.5) ** 2
    check("J10 finite supplied-model control; fixture and predicate specified in source",
          abs(h * 1.0 + 2) > 0.02 and abs(h * nnv + 2) > 0.02, f"h_tt k^2 {h:+.4f}; h_tt * 4 sin^2(1/2) {h * nnv:+.4f}")
    print("per_element: explicit simplex geometry and local matrix entries are computed on the supplied finite carrier; no microscopic interaction supplier is derived")
    print("per_site: listed vertex types and periodic-cell incidences are included; arbitrary lattice defects and unspecified site models are untested")
    print("per_mode: only the literal momentum fixtures, thresholds and finite scans above are tested; no complete zero-set or spectrum census is certified")
    print("per_block: the displayed cell operators and source or covariance contractions are evaluated; numerical pass labels do not supply an interacting physical theory")
    print("lattice_wide: finite periodic-symbol diagnostics and explicitly stated constructive identities only; thermodynamic limits, all-volume OS positivity and physical reconstruction remain deferred")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
