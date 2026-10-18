#!/usr/bin/env python3
"""Scale ladder, gravity rung: one cone for spins 0, 1 and 2 on the D4-cone carrier, and a control on the Kuhn complex.

Finite floating-point checks on supplied models (index 3 = tick):
  H1 Kuhn complex, hypercubic lengths: a relative-strain least-squares metric over its 15 edge classes (all
     site-site) reads the fifth zero-action direction at O(1), so that coupling does not decouple it;
  H2 Whitney 1-form Maxwell on the D4 cone: null directions = vertex gauge; leading symbol = continuum Maxwell;
  H3 three massless non-gauge directions, as in the continuum (no partner modes);
  H4 both photon polarisations on one shell with no on-shell O(k^4) correction (4 directions);
  H5 P1 scalar and photon: first on-shell correction at O(k^6), photon coefficient = -1/4 of the scalar's,
     both zero on the axis.
Supplied models only; no physical identification.
Companion: docs/SCALE_LADDER_GRAVITY_D4_CONE_COMMON_CONE_SPINS_ZERO_ONE_TWO_BOUNDED_THEOREM_NOTE_2026-10-18.md
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


HC = R4.HCOMPS
I4 = np.eye(4)


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


def sv(M):
    s = np.sort(np.linalg.svd(M, compute_uv=False)); return s / s[-1]


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



def golden(f, lo, hi):
    gr = (5 ** .5 - 1) / 2; a, b = lo, hi; c, d = b - gr * (b - a), a + gr * (b - a); fc, fd = f(c), f(d)
    for _ in range(120):
        if fc < fd: b, d, fd = d, c, fc; c = b - gr * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + gr * (b - a); fd = f(d)
        if b - a < 1e-14: break
    return (a + b) / 2




# ------------------------------------------------------------------ Whitney 1-form Maxwell on a generic complex
class Whitney:
    def __init__(self, C):
        self.C = C; self.tix = {t: i for i, t in enumerate(C.types)}; self.pre = []
        def ref(v1, v2):
            key, anc = _key_pair(v1, v2); t1, t2, rel = key
            start = (tuple(anc), t1)
            sgn = 1 if (tuple(v1[0]), v1[1]) == start else -1
            return C.ekey[key], np.array(anc, float), sgn
        for vs in C.simp:
            P = np.array([C.pos(v) for v in vs]); E = P[1:] - P[0]; vol = np.sqrt(np.linalg.det(E @ E.T)) / 24
            tris = [(i - 1, j - 1, [ref(vs[p], vs[q]) for (p, q) in [(0, i), (i, j), (j, 0)]])
                    for i in range(1, 5) for j in range(i + 1, 5)]
            self.pre.append((np.linalg.inv(E), vol, tris))

    def Q(self, k):
        k = np.asarray(k, complex); E_ = self.C.E; Q = np.zeros((E_, E_), complex)
        def F(kk, Ei, tris):
            Fe = np.zeros((4, 4, E_), complex)
            for a, b, es in tris:
                r = np.zeros(E_, complex)
                for c, anc, sg in es: r[c] += sg * np.exp(1j * kk @ anc)
                Fe[a, b] = 2 * r; Fe[b, a] = -2 * r
            return np.einsum('ma,abc,nb->mnc', Ei, Fe, Ei)
        for Ei, vol, tris in self.pre:
            Q += 0.5 * vol * np.einsum('mnc,mnd->cd', F(-k, Ei, tris), F(k, Ei, tris))
        return Q

    def gauge(self, k):
        G = np.zeros((self.C.E, len(self.C.types)), complex)
        for (t1, t2, rel), c in self.C.ekey.items():
            G[c, self.tix[t2]] += np.exp(1j * np.asarray(k, complex) @ np.array(rel, float)); G[c, self.tix[t1]] -= 1
        return G

    def line_map(self, k):
        M = np.zeros((self.C.E, 4), complex)
        for (t1, t2, rel), c in self.C.ekey.items():
            v = self.C.evec[c]; z = k @ v
            M[c] = np.exp(1j * k @ self.C.OFF[t1]) * (1.0 if abs(z) < 1e-14 else (np.exp(1j * z) - 1) / (1j * z)) * v
        return M


def main():
    rr = np.random.default_rng(1)
    # ---------------- H1 Kuhn control
    Qe, _ = regge(I4); D15 = [np.array(v, float) for v in R4.DIRS15]
    l = np.array([np.linalg.norm(v) for v in D15])
    Dm = np.array([[v[a] * v[b] * (2 if a != b else 1) for a, b in HC] for v in D15])
    W = np.diag(1 / l ** 2); Ls = np.linalg.pinv(W @ Dm) @ (W @ np.diag(2 * l))
    exact = np.abs(Ls @ (np.diag(1 / (2 * l)) @ Dm) - np.eye(10)).max()
    def gk(k):
        G = np.zeros((15, 4), complex)
        for c, v in enumerate(D15): G[c] = (np.exp(1j * k @ v) - 1) * v / np.linalg.norm(v)
        return G
    seen = []
    for q in [np.array([0.02, 0.01, -0.015, 0.012]), np.array([0.02, 0, 0, 0.0]), np.array([0.3, -0.2, 0.25, 0.1])]:
        _, _, vh = np.linalg.svd(Qe(q)); N = vh[-5:].conj().T; G = gk(q)
        f = np.linalg.svd(N - G @ np.linalg.pinv(G) @ N)[0][:, 0]; seen.append(np.linalg.norm(Ls @ f))
    check("H1 Kuhn, hypercubic lengths: the relative-strain least-squares metric (exact on constant metrics) reads the fifth zero-action direction at O(1)",
          exact < 1e-12 and min(seen) > 0.5, f"exactness {exact:.0e}; |L f| = {', '.join(f'{x:.2f}' for x in seen)}")

    # ---------------- H2-H3 Whitney Maxwell on the D4 cone
    OFF, S = d4cone(); Dc = Complex(OFF, S); Mx = Whitney(Dc)
    k = 0.4 * rr.standard_normal(4); Q = Mx.Q(k); s_ = sv(Q)
    nul, grk, qg = int((s_ < 1e-10).sum()), np.linalg.matrix_rank(Mx.gauge(k)), np.abs(Q @ Mx.gauge(k)).max()
    dev = 0.0
    for _ in range(4):
        kd = rr.standard_normal(4); kd /= np.linalg.norm(kd); A = rr.standard_normal(4); r = []
        for e in (2e-3, 1e-3):
            kk = e * kd; Fc = 1j * (np.outer(kk, A) - np.outer(A, kk)); cont = 0.5 * np.real(np.sum(np.conj(Fc) * Fc))
            r.append(np.real(np.conj(Mx.line_map(kk) @ A) @ Mx.Q(kk) @ (Mx.line_map(kk) @ A)) / cont)
        dev = max(dev, abs((4 * r[1] - r[0]) / 3 - 1))
    check("H2 Whitney Maxwell on the D4 cone: null directions = the 8 vertex gauge directions; leading symbol = continuum F^2/2",
          nul == 8 and grk == 8 and qg < 1e-12 and dev < 1e-6, f"nullity {nul}, gauge rank {grk}, |QG| {qg:.0e}; leading deviation {dev:.1e}")
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
    for s in (0.02, 0.01):
        Qh = Mx.Q(s * kd); ev.append(np.sort(np.abs(np.linalg.eigvalsh(0.5 * (Qh + Qh.conj().T)))))
    nsoft = int(sum(abs(ev[0][i] / ev[1][i] - 4) < 0.05 for i in range(8, 30)))
    check("H3 Whitney Maxwell on the D4 cone: 3 massless non-gauge directions (the continuum count; no partner modes); next eigenvalue O(1)",
          nsoft == 3 and ev[1][11] > 1, f"massless count {nsoft}; first massive {ev[1][11]:.3f}")

    # ---------------- H4-H5 on-shell: photon and scalar
    def svn(k): return sv(Mx.Q(k))
    def scalar_shell(ks, km):
        f = lambda kt: np.linalg.det(p1_scalar(Dc, np.array([*ks, kt])))
        x = 1j * km
        for _ in range(80):
            h = 1e-7; st = f(x) / ((f(x + h) - f(x - h)) / (2 * h)); x -= st
            if abs(st) < 1e-14: break
        return x
    def photon_shell(ks, km, lo, hi, npt):
        oms = km * np.linspace(lo, hi, npt); fv = [svn(np.array([*ks, 1j * o]))[8] for o in oms]; i = int(np.argmin(fv))
        w = golden(lambda o: svn(np.array([*ks, 1j * o]))[8], oms[max(i - 1, 0)], oms[min(i + 1, npt - 1)])
        return w, int((svn(np.array([*ks, 1j * w])) < 1e-9).sum())
    a4, nuls = [], []
    for n in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05
        w, nu = photon_shell(km * n, km, 0.998, 1.002, 161); a4.append((w * w / km ** 2 - 1) / km ** 2); nuls.append(nu)
    check("H4 photon on the D4 cone: both polarisations on one shell (nullity 8 -> 10) with no on-shell O(k^4) term (4 directions)",
          all(nu == 10 for nu in nuls) and max(abs(a) for a in a4) < 2e-3, f"nullities {nuls}; alpha {', '.join(f'{a:+.1e}' for a in a4)}")
    rows = []
    for n in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.3; ks = km * n
        bs = (abs(scalar_shell(ks, km)) ** 2 / km ** 2 - 1) / km ** 4
        w, _ = photon_shell(ks, km, 0.97, 1.03, 241); bp = (w * w / km ** 2 - 1) / km ** 4
        rows.append((bs, bp))
    ok5 = abs(rows[0][0]) < 2e-5 and abs(rows[0][1]) < 2e-5 and all(abs(b[1] / b[0] + 0.25) < 0.03 and abs(b[0]) > 1e-4 for b in rows[1:])
    check("H5 first on-shell correction at O(k^6): photon coefficient = -1/4 of the P1 scalar's (face, body, generic); both zero on the axis",
          ok5, "; ".join(f"scalar {b[0]:+.5f} photon {b[1]:+.5f}" for b in rows))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
