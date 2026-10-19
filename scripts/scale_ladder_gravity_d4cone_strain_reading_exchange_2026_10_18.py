#!/usr/bin/env python3
"""Scale ladder, gravity rung: exchange through the strain-fitted reading of the D4-cone Regge carrier.

Finite floating-point checks on a supplied model: the Regge second variation of the D4 cone (D4 Delaunay
16-cells of Z^4 u (Z^4 + u/2) coned from their centres; index 3 = tick), with matter coupled through a
least-squares metric fitted to the relative strains of the 24 site-site segments of a cell.
  H1 static T_tt source, null-fluid test source vs static dust test source: ratio 2 (the value 1 + gamma takes
     in linearised GR), error falling with |k|;
  H2 exchange between lattice-conserved sources at generic Euclidean momenta (tick component included):
     -4 (T1.T2 - 1/2 trT1 trT2)/k^2, the linearised-EH form, with the non-metric partners' share O(k^2);
  H3 near the light cone (k_t = i omega) the strain reading of the non-metric null directions is O(k);
  H4 a site-only scalar (nearest-neighbour differences, metric read through the strain fit): the lattice
     vertex-displacement Ward identity fails at relative O(k), for corner and cell-averaged gradients;
  H5 the O(k) comes from the reading: its gradient symbol has entries outside the continuum gradient's support
     at relative O(k), with per-component registration points that differ from component to component;
  H6 for the exchange of two on-shell scalar pairs the gauge-fixing dependence is O(k^2);
  H7 class-weighted relative-strain readings (axis, face, body weights): the partner shifts the trace
     coefficient by (2/3) rho^2, rho = 4(w_a - w_b)/(4 w_a + 12 w_f + 8 w_b), so the exchange is the
     linearised-EH form iff w_a = w_b, for every face weight;
  H8 w_a = w_b is exactly the condition that the weighted segment directions have an isotropic fourth moment;
     the reading is not the Euclidean pseudo-inverse of the line map;
  H9 segment-midpoint coupling (each segment's share of the stress evaluated at the segment midpoint by local
     averaging over the cells around it): the Ward violation drops to relative O(k^2);
  H10 with that coupling the on-shell scalar-scalar exchange matches the linearised-EH form to O(k^2), and
     its gauge-fixing dependence is O(k^4).
Supplied model only; no physical identification.
Companion: docs/SCALE_LADDER_GRAVITY_D4CONE_STRAIN_READING_EXCHANGE_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600

import itertools, sys
import numpy as np

PASS = FAIL = 0
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ------------------------------------------------------------------ generic Bloch Regge builder (as in the orthoscheme runner)
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



# ------------------------------------------------------------------ readings, sources, propagator
CLS = np.array([0] * 4 + [1] * 12 + [2] * 8)


def segment_readings(C, k):
    """delta(l^2) of the 24 site-site segments through one cell (4 axes, 12 face diagonals through the deep holes,
    8 body diagonals through the centre) over edge variables, the design matrix in the 10 metric components, lengths."""
    pairs = list(itertools.combinations(range(4), 2)); E = np.eye(4, dtype=int); Z = (0, 0, 0, 0)
    k = np.asarray(k, complex); R, D, ls = [], [], []
    def seg(parts, l):
        r = np.zeros(C.E, complex)
        for (p, q) in parts:
            key, anc = _key_pair(p, q); r[C.ekey[key]] += 2 * l * np.exp(1j * k @ np.array(anc, float))
        return r
    def drow(v): return [v[a] * v[b] * (2 if a != b else 1) for a, b in HC]
    for mu in range(4):
        R.append(seg([((Z, 0), (tuple(E[mu]), 0))], 1.0)); D.append(drow(E[mu].astype(float))); ls.append(1.0)
    for h, (m, n) in enumerate(pairs):
        hv = (Z, 2 + h)
        R.append(seg([((Z, 0), hv), (hv, (tuple(E[m] + E[n]), 0))], np.sqrt(2))); D.append(drow((E[m] + E[n]).astype(float))); ls.append(np.sqrt(2))
        R.append(seg([((tuple(E[n]), 0), hv), (hv, (tuple(E[m]), 0))], np.sqrt(2))); D.append(drow((E[m] - E[n]).astype(float))); ls.append(np.sqrt(2))
    for sg in itertools.product([1, -1], repeat=3):
        s_ = np.array([1, *sg]); v0 = tuple(int(x) for x in (1 - s_) // 2); v1 = tuple(int(x) for x in (1 - s_) // 2 + s_)
        R.append(seg([((v0, 0), (Z, 1)), ((Z, 1), (v1, 0))], 2.0)); D.append(drow(s_.astype(float))); ls.append(2.0)
    return np.array(R), np.array(D, float), np.array(ls)


def reading(C, k, w=(1.0, 1.0, 1.0)):
    """least-squares metric fitted to relative strains delta(l^2)/l^2, class weights w = (axis, face, body);
    w = (1, 1, 1) is the strain metric (uniform weights on relative strain, i.e. 1/l^4 on delta(l^2))."""
    R, D, ls = segment_readings(C, k); W = np.diag(np.sqrt(np.array(w, float)[CLS]) / ls ** 2)
    return np.linalg.pinv(W @ D) @ (W @ R)


def cvec(T): return np.array([T[a, b] * (1 if a == b else 2) for a, b in HC])


def T_of_c(c):
    T = np.zeros((4, 4), complex)
    for i, (a, b) in enumerate(HC): T[a, b] = T[b, a] = c[i] / (1 if a == b else 2)
    return T


def Qinv(C, k):
    """inverse of the edge form on the orthogonal complement of the exact vertex-displacement range (two of those
    eigenvalues sit near 1e-9 from the finite-difference build, so a plain pseudo-inverse cutoff does not remove them)."""
    Q = C.Q(k); G = C.gauge(k); U_ = np.linalg.svd(G)[0]; r = np.linalg.matrix_rank(G, tol=1e-9); B = U_[:, r:]
    return B @ np.linalg.inv(B.conj().T @ Q @ B) @ B.conj().T


def partners(C, k):
    Q = C.Q(k); w, V = np.linalg.eigh(0.5 * (Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    A = np.hstack([C.line_map(k), C.gauge(k)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    return np.linalg.svd(P @ V[:, 32:40])[0][:, :2]


def conserved_basis(C, k, L):
    """6 coupling vectors c with c . (L G_site) = 0 exactly (lattice-conserved for this reading)."""
    W = L @ C.gauge(k)[:, :4]; Cb = np.linalg.svd(W.T)[2][4:]
    if np.abs(Cb @ W).max() > 1e-10: Cb = Cb.conj()
    return Cb, np.abs(Cb @ W).max()


def exchange_fit(C, k, L, Qi, P2=None):
    """fit k^2 c2* K c1 on the conserved basis to alpha T1*.T2 + beta trT1* trT2; also the partners' share."""
    K = L @ Qi @ L.conj().T; Cb, _ = conserved_basis(C, k, L); Ts = [T_of_c(c) for c in Cb]; k2 = (k @ k).real
    M = (Cb.conj() @ K @ Cb.T) * k2
    X = np.array([[np.sum(Ti.conj() * Tj), np.conj(np.trace(Ti)) * np.trace(Tj)] for Ti in Ts for Tj in Ts])
    coef = np.linalg.lstsq(X, M.ravel(), rcond=None)[0]; res = np.linalg.norm(X @ coef - M.ravel()) / np.linalg.norm(M.ravel())
    share = None
    if P2 is not None:
        Pp = P2 @ P2.conj().T; share = np.abs((Cb.conj() @ (L @ Pp @ Qi @ Pp @ L.conj().T) @ Cb.T) * k2).max() / np.abs(M).max()
    return coef.real, res, share


# site scalar: gradient symbols for a mode e^{i k.x}
def grad_corner(k): return np.exp(1j * k) - 1
def grad_cell(k):
    return np.array([(np.exp(1j * k[m]) - 1) * np.prod([(1 + np.exp(1j * k[n])) / 2 for n in range(4) if n != m]) for m in range(4)])
def shell_f(k, grad): return grad(k) @ grad(-k)
def shell_kt(ks, grad):
    x = 1j * np.linalg.norm(ks); f = lambda kt: shell_f(np.array([*ks, kt]), grad)
    for _ in range(100):
        h = 1e-7; st = f(x) / ((f(x + h) - f(x - h)) / (2 * h)); x -= st
        if abs(st) < 1e-15: break
    return np.array([*ks, x], complex)
def stress_c(a, b):
    return cvec(0.5 * (np.outer(a, b) + np.outer(b, a)) - 0.5 * np.eye(4) * (a @ b))
def pair_at(q, s, grad, d, e):
    """on-shell k3 = (s d + t e, k3_t) with k3 - q also on shell (Newton in complex t, several starts)."""
    for t0 in (0.1, 0.5, -0.5, 1.0, -1.0, 0.3j, -0.3j):
        t = t0 * s
        for _ in range(60):
            f0 = shell_f(shell_kt(s * d + t * e, grad) - q, grad); h = 1e-7
            df = (shell_f(shell_kt(s * d + (t + h) * e, grad) - q, grad) - shell_f(shell_kt(s * d + (t - h) * e, grad) - q, grad)) / (2 * h)
            st = f0 / df; t -= st
            if abs(st) < 1e-15: break
        k3 = shell_kt(s * d + t * e, grad)
        if abs(shell_f(k3 - q, grad)) < 1e-12: return k3, k3 - q
    raise RuntimeError("no on-shell pair")


def midpoint_coupling(C):
    """segment-strain weights Lt (10 x 24, h = Lt delta(l^2)) and the segment midpoints (cell corner at the origin)."""
    R0, D, ls = segment_readings(C, np.zeros(4)); Wt = np.diag(1 / ls ** 2); Lt = np.linalg.pinv(Wt @ D) @ Wt
    E = np.eye(4); pairs = list(itertools.combinations(range(4), 2))
    mids = [0.5 * E[m] for m in range(4)] + [0.5 * (E[m] + E[n]) for (m, n) in pairs for _ in (0, 1)] + [0.5 * np.ones(4)] * 8
    return Lt, mids


def place(q, mid):
    """local average of a cell-centred density (cell centre u/2) over the cells whose centres surround the midpoint."""
    fr = [nu for nu in range(4) if abs(mid[nu] - round(mid[nu])) < 1e-9]; tot = 0
    for sg in itertools.product([-0.5, 0.5], repeat=len(fr)):
        c = np.array(mid, float)
        for nu, s_ in zip(fr, sg): c[nu] += s_
        tot += np.exp(1j * q @ (c - 0.5))
    return tot / 2 ** len(fr)


def golden(f, lo, hi):
    gr = (5 ** .5 - 1) / 2; a, b = lo, hi; c, d = b - gr * (b - a), a + gr * (b - a); fc, fd = f(c), f(d)
    for _ in range(120):
        if fc < fd: b, d, fd = d, c, fc; c = b - gr * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + gr * (b - a); fd = f(d)
        if b - a < 1e-14: break
    return (a + b) / 2


def main():
    OFF, S = d4cone(); Dc = Complex(OFF, S); itt = HC.index((3, 3))
    print(f"D4 cone: {len(S)} simplices, {Dc.E} edge classes, {len(Dc.types)} vertex types")
    L0 = reading(Dc, np.zeros(4)); kq = np.array([0.3, -0.2, 0.1, 0.25]); Gq = Dc.gauge(kq)
    blind = np.abs(reading(Dc, kq) @ np.hstack([Gq[:, 4 * t:4 * t + 4] for t in range(1, 8)])).max()
    exact = np.abs(L0 @ Dc.line_map(np.zeros(4)) - np.eye(10)).max()
    print(f"strain reading: exact on constant metrics ({exact:.0e}), blind to non-site vertex displacements ({blind:.0e})")

    # ---------------- H1 light bending ratio
    rows = []
    for kk in [np.array([0, 0.04, 0, 0.]), np.array([0, 0.02, 0, 0.]), np.array([0, 0.012, 0.009, 0.])]:
        L = reading(Dc, kk); T1 = np.zeros((4, 4)); T1[3, 3] = 1; h = L @ Qinv(Dc, kk) @ (L.conj().T @ cvec(T1)); k2 = kk @ kk
        kh = kk[:3] / np.linalg.norm(kk[:3]); e = np.cross(kh, [0, 0, 1.]); e /= np.linalg.norm(e)
        nE = np.array([*e, 1j]); Tn = np.outer(nE, nE); Td = np.zeros((4, 4), complex); Td[3, 3] = -1
        An, Al = cvec(Td) @ h, cvec(Tn) @ h; rows.append((np.sqrt(k2), An.real * k2, (Al / An).real))
    check("H1 static T_tt source: null-fluid / static-dust test amplitude = 2 (Euclidean, n = (e_perp, i)); Newton amplitude k^2 A = 2",
          all(abs(r[2] - 2) < 3e-4 and abs(r[1] - 2) < 1e-3 for r in rows) and abs(rows[1][2] - 2) < abs(rows[0][2] - 2),
          "; ".join(f"|k| {r[0]:.3f}: k^2 A_N {r[1]:+.5f}, ratio {r[2]:.6f}" for r in rows))

    # ---------------- H2 non-static Euclidean exchange
    dirs = {'axis': [0, 1, 0, 0], 'tick': [0, 0, 0, 1], 'tick-space face': [0, 1, 0, 1], 'body': [1, 1, 1, 1], 'generic': [0.3, -0.5, 0.6, 0.55], 'generic2': [0.7, 0.2, -0.4, -0.45]}
    out = {}
    for nm, d in dirs.items():
        d = np.array(d, float) / np.linalg.norm(d); out[nm] = []
        for s in (0.02, 0.01):
            k = s * d; out[nm].append(exchange_fit(Dc, k, reading(Dc, k), Qinv(Dc, k), partners(Dc, k)))
    ok = all(abs(o[1][0][0] + 4) < 2e-4 and abs(o[1][0][1] - 2) < 2e-4 and o[1][1] < 5e-3 and o[1][1] <= o[0][1] * 0.75 + 1e-5
             and o[1][2] < 1e-6 and 3 < o[0][2] / o[1][2] < 5 for o in out.values())
    check("H2 conserved sources, |k| = 0.02 -> 0.01, six directions incl. tick: alpha -> -4, beta -> +2 (linearised-EH ratio -1/2); fit residual falls; partner share O(k^2)",
          ok, "; ".join(f"{n}: a {o[1][0][0]:+.5f} b {o[1][0][1]:+.5f} res {o[0][1]:.0e}->{o[1][1]:.0e} share {o[1][2]:.0e}" for n, o in out.items()))

    # ---------------- H3 Lorentzian shells: strain reading of the non-metric null directions
    def svn(k): s_ = np.sort(np.linalg.svd(Dc.Q(k), compute_uv=False)); return s_ / s_[-1]
    res3 = {}
    for nm, n in {'axis': (1, 0, 0), 'face': (1, 1, 0), 'generic': (3, 1, 2)}.items():
        n = np.array(n, float) / np.linalg.norm(n); res3[nm] = []
        for km in (0.08, 0.04):
            ks = km * n; oms = km * np.linspace(0.996, 1.004, 121); f = [svn(np.array([*ks, 1j * o]))[32] for o in oms]
            mins = [golden(lambda o: svn(np.array([*ks, 1j * o]))[32], oms[i - 1], oms[i + 1]) for i in range(1, 120) if f[i] < f[i - 1] and f[i] < f[i + 1]]
            worst, nuls = 0.0, []
            for w in mins:
                k = np.array([*ks, 1j * w]); _, s_, vh = np.linalg.svd(Dc.Q(k)); s_ = s_[::-1] / s_[0]
                nul = int((s_ < 1e-8).sum()); nuls.append(nul); N = vh[-nul:].conj().T; G = Dc.gauge(k)
                X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :nul - 32]
                A = np.hstack([Dc.line_map(k), G]); _, sh, vv = np.linalg.svd(A @ np.linalg.pinv(A, rcond=1e-10) @ X); Y = X @ vv.conj().T
                hr = np.linalg.norm(reading(Dc, k) @ Y, axis=0); met = sh > 0.5   # metric vs non-metric null directions
                worst = max(worst, hr[~met].max() / hr[met].max())
            res3[nm].append((len(mins), nuls, worst / km))
    check("H3 near the light cone (k_t = i omega): on each shell max strain reading of the non-metric null directions / of the metric ones in [0.2, 0.35] x |k| (|k| = 0.08, 0.04)",
          all(len(r) == 2 and all(x[0] == 2 and min(x[1]) >= 33 for x in r) and 0.2 < r[0][2] < 0.35 and 0.2 < r[1][2] < 0.35 for r in res3.values()),
          "; ".join(f"{n}: " + ", ".join(f"nullities {x[1]} ratio/|k| {x[2]:.3f}" for x in r) for n, r in res3.items()))

    # ---------------- H4 site scalar Ward identity
    rng = np.random.default_rng(7); n1, n2 = rng.standard_normal(3), rng.standard_normal(3); n1 /= np.linalg.norm(n1); n2 /= np.linalg.norm(n2)
    ward = {}
    for nm, grad in (('corner', grad_corner), ('cell-averaged', grad_cell)):
        ward[nm] = []
        for s in (0.1, 0.05, 0.025):
            k1 = shell_kt(s * n1, grad); k2 = shell_kt(0.7 * s * n2, grad); q = k2 - k1; a, b = grad(-k1), grad(k2); c = stress_c(a, b)
            W = reading(Dc, -q) @ Dc.gauge(-q)[:, :4]; T = T_of_c(c)
            ward[nm].append((np.linalg.norm(c @ W) / (np.linalg.norm(c) * np.linalg.norm(W)), np.linalg.norm(T @ q) / (np.linalg.norm(T) * np.linalg.norm(q))))
    wc, wa = ward['corner'], ward['cell-averaged']
    check("H4 site scalar on Z^4 (NN differences, metric read by the strain fit): on-shell Ward ratio |c.LG|/(|c||LG|) is O(k) for both gradients; the cell-averaged stress is continuum-conserved to O(k^2)",
          all(1.9 < wc[i][0] / wc[i + 1][0] < 2.1 and 1.9 < wa[i][0] / wa[i + 1][0] < 2.1 for i in range(2)) and 3.8 < wa[1][1] / wa[2][1] < 4.2,
          "corner " + ", ".join(f"{x[0]:.2e}" for x in wc) + "; cell " + ", ".join(f"{x[0]:.2e}" for x in wa) + " (s = 0.1, 0.05, 0.025); cell q.T/(|T||q|) " + ", ".join(f"{x[1]:.1e}" for x in wa))

    # ---------------- H5 where the O(k) comes from: the reading's gradient symbol
    def Wcont(q):
        W = np.zeros((10, 4), complex)
        for i, (a, b) in enumerate(HC):
            for r in range(4): W[i, r] = 1j * (q[a] * (b == r) + q[b] * (a == r))
        return W
    PR = np.array([[.5 if m == a else .125 for m in range(4)] if a == b else [.5 if m in (a, b) else .25 for m in range(4)] for a, b in HC])
    base = np.array([0.013, 0.007, -0.011, 0.005]); eps = 1e-4; maxdev = 0.0
    for i, (a, b) in enumerate(HC):
        for col in sorted({a, b}):
            ph = lambda q: np.angle((reading(Dc, q) @ Dc.gauge(q)[:, :4])[i, col] / Wcont(q)[i, col])
            p = [(ph(base + eps * np.eye(4)[m]) - ph(base - eps * np.eye(4)[m])) / (2 * eps) for m in range(4)]
            maxdev = max(maxdev, np.abs(np.array(p) - PR[i]).max())
    d = np.array([0.3, -0.5, 0.6, 0.55]) / np.linalg.norm([0.3, -0.5, 0.6, 0.55]); offs = []
    for s in (0.1, 0.05):
        q = s * d; W = reading(Dc, q) @ Dc.gauge(q)[:, :4]; Wm = np.exp(1j * PR @ q)[:, None] * Wcont(q); mask = np.abs(Wcont(q)) > 0
        offs.append((np.linalg.norm((W - Wm)[~mask]) / np.linalg.norm(W), np.linalg.norm((W - Wm)[mask]) / np.linalg.norm(W)))
    check("H5 reading's gradient symbol = e^{i q.p_row} x continuum on its support (p: h_mumu at 1/2 along mu, 1/8 across; h_munu at 1/2 along mu, nu, 1/4 across), plus off-support entries at relative O(k)",
          maxdev < 2e-3 and 1.9 < offs[0][0] / offs[1][0] < 2.1 and 3.5 < offs[0][1] / offs[1][1] < 4.5,
          f"max |p - table| {maxdev:.0e}; off-support {offs[0][0]:.1e} -> {offs[1][0]:.1e}; on-support remainder {offs[0][1]:.1e} -> {offs[1][1]:.1e}")

    # ---------------- H6 gauge-fixing dependence of an on-shell scalar-scalar exchange
    rng = np.random.default_rng(11); ds = [rng.standard_normal(3) for _ in range(4)]; ds = [x / np.linalg.norm(x) for x in ds]
    def amp(q, c1, c2, lam):
        G, Gm = Dc.gauge(q), Dc.gauge(-q)
        return c2 @ reading(Dc, q) @ np.linalg.solve(Dc.Q(q) + lam * G @ Gm.T, reading(Dc, -q).T @ c1)
    g6 = {}
    for nm, grad in (('corner', grad_corner), ('cell-averaged', grad_cell)):
        g6[nm] = []
        for s in (0.1, 0.05):
            k1 = shell_kt(s * ds[0], grad); k2 = shell_kt(0.8 * s * ds[1], grad); q = k2 - k1; k3, k4 = pair_at(q, 0.9 * s, grad, ds[2], ds[3])
            c1 = stress_c(grad(-k1), grad(k2)); c2 = stress_c(grad(-k3), grad(k4)); A = [amp(q, c1, c2, l) for l in (1.0, 10.0)]
            T1, T2 = T_of_c(c1), T_of_c(c2); gr = -4 * (np.sum(T1 * T2) - 0.5 * np.trace(T1) * np.trace(T2)) / (q @ q)
            g6[nm].append((abs(A[1] - A[0]) / abs(A[0]), abs(A[0] - gr) / abs(gr)))
    check("H6 two on-shell scalar pairs at momenta q, -q: gauge-fixing dependence (lambda 1 -> 10) falls ~4x on halving (O(k^2)); distance from -4(T.T - trT trT/2)/q^2 is O(k)",
          all(3.5 < r[0][0] / r[1][0] < 10 and 1.6 < r[0][1] / r[1][1] < 2.6 for r in g6.values()),
          "; ".join(f"{n}: gauge {r[0][0]:.1e} -> {r[1][0]:.1e}, from EH form {r[0][1]:.1e} -> {r[1][1]:.1e}" for n, r in g6.items()))

    # ---------------- H7 the weighting family
    kk = {'axis': np.array([0, 0.01, 0, 0]), 'generic': 0.01 * d}; Qis = {n: Qinv(Dc, k) for n, k in kk.items()}; rows7 = []
    for w in [(1, 1, 1), (1, 0.25, 1), (1, 4, 1), (1, 0, 1), (1, 1, 0.5), (1, 1, 2), (1, 4, 16), (1, 1, 0)]:
        rho = 4 * (w[0] - w[2]) / (4 * w[0] + 12 * w[1] + 8 * w[2])
        fits = [exchange_fit(Dc, k, reading(Dc, k, w), Qis[n])[0] for n, k in kk.items()]
        rows7.append((w, rho, max(abs(f[0] + 4) for f in fits), max(abs(f[1] - (2 - 2 / 3 * rho ** 2)) for f in fits), fits[1][0] / (fits[1][0] + fits[1][1])))
    check("H7 class weights (axis, face, body) on relative strain: alpha = -4 and beta = 2 - (2/3) rho^2, rho = 4(w_a - w_b)/(4 w_a + 12 w_f + 8 w_b); EH form iff w_a = w_b, any face weight (8 weightings, 2 directions)",
          all(r[2] < 3e-4 and r[3] < 3e-4 for r in rows7),
          "; ".join(f"{r[0]}: rho {r[1]:+.3f}, ratio {r[4]:.4f}" for r in rows7) + f"; max dev {max(max(r[2], r[3]) for r in rows7):.0e}")

    # ---------------- H8 the condition is isotropy of the weighted fourth moment; not the Euclidean pseudo-inverse
    dirs24 = [np.eye(4)[m] for m in range(4)] + [v for (m, n) in itertools.combinations(range(4), 2) for v in (np.eye(4)[m] + np.eye(4)[n], np.eye(4)[m] - np.eye(4)[n])] + [np.array([1, *sg], float) for sg in itertools.product([1, -1], repeat=3)]
    def aniso(w):
        F = sum(w[CLS[i]] * np.einsum('a,b,c,e->abce', *(4 * [v / np.linalg.norm(v)])) for i, v in enumerate(dirs24))
        I = np.eye(4); iso = (np.einsum('ab,ce->abce', I, I) + np.einsum('ac,be->abce', I, I) + np.einsum('ae,bc->abce', I, I))
        lam = np.sum(F * iso) / np.sum(iso * iso); return np.linalg.norm(F - lam * iso) / np.linalg.norm(F)
    an = [(w, aniso(w)) for w in [(1, 1, 1), (1, 0.25, 1), (1, 4, 1), (1, 0, 1), (1, 1, 0.5), (1, 4, 16)]]
    M0 = Dc.line_map(np.zeros(4)).real; Ls = L0.real; used = np.where(np.abs(Ls).sum(0) > 1e-12)[0]; Lu = np.zeros_like(Ls); Lu[:, used] = np.linalg.pinv(M0[used])
    mis = (np.linalg.norm(Ls - np.linalg.pinv(M0)) / np.linalg.norm(Ls), np.linalg.norm(Ls - Lu) / np.linalg.norm(Ls))
    check("H8 weighted 24-direction fourth moment is isotropic iff w_a = w_b; the strain reading is not the Euclidean pseudo-inverse of the line map (all 72 or the 44 used edges)",
          all((a < 1e-12) == (w[0] == w[2]) for w, a in an) and min(mis) > 0.1,
          "; ".join(f"{w}: {a:.1e}" for w, a in an) + f"; pinv misfit {mis[0]:.2f} / {mis[1]:.2f}")

    # ---------------- H9 segment-midpoint coupling: Ward order
    Lt, mids = midpoint_coupling(Dc)
    assert np.abs(Lt @ segment_readings(Dc, np.zeros(4))[0] - L0).max() < 1e-12
    w9 = {'cell-centred': [], 'midpoint': []}
    for s in (0.1, 0.05, 0.025):
        k1 = shell_kt(s * n1, grad_cell); k2 = shell_kt(0.7 * s * n2, grad_cell); q = k2 - k1
        b = stress_c(grad_cell(-k1), grad_cell(k2)) @ Lt; WG = segment_readings(Dc, -q)[0] @ Dc.gauge(-q)[:, :4]
        for nm, bb in (('cell-centred', b), ('midpoint', b * np.array([place(q, m) for m in mids]))):
            w9[nm].append(np.linalg.norm(bb @ WG) / (np.linalg.norm(bb) * np.linalg.norm(WG)))
    f9 = {nm: [v[i] / v[i + 1] for i in range(2)] for nm, v in w9.items()}
    check("H9 cell-averaged scalar, each segment's share of the stress evaluated at the segment midpoint (local cell average): Ward ratio over segment strains falls 4x on halving (O(k^2)); cell-centred falls 2x",
          all(3.8 < f < 4.3 for f in f9['midpoint']) and all(1.9 < f < 2.1 for f in f9['cell-centred']),
          "; ".join(f"{nm} " + ", ".join(f"{x:.2e}" for x in v) for nm, v in w9.items()) + " (s = 0.1, 0.05, 0.025)")

    # ---------------- H10 midpoint coupling: exchange of two on-shell scalar pairs
    def amp_seg(q, b1, b2, lam):
        G, Gm = Dc.gauge(q), Dc.gauge(-q)
        return b2 @ segment_readings(Dc, q)[0] @ np.linalg.solve(Dc.Q(q) + lam * G @ Gm.T, segment_readings(Dc, -q)[0].T @ b1)
    o10 = []
    for s in (0.1, 0.05, 0.025):
        k1 = shell_kt(s * ds[0], grad_cell); k2 = shell_kt(0.8 * s * ds[1], grad_cell); q = k2 - k1; k3, k4 = pair_at(q, 0.9 * s, grad_cell, ds[2], ds[3])
        c1 = stress_c(grad_cell(-k1), grad_cell(k2)); c2 = stress_c(grad_cell(-k3), grad_cell(k4))
        b1 = (c1 @ Lt) * np.array([place(q, m) for m in mids]); b2 = (c2 @ Lt) * np.array([place(-q, m) for m in mids])
        A = [amp_seg(q, b1, b2, l) for l in (1.0, 10.0)]
        T1, T2 = T_of_c(c1), T_of_c(c2); gr = -4 * (np.sum(T1 * T2) - 0.5 * np.trace(T1) * np.trace(T2)) / (q @ q)
        o10.append((abs(A[1] - A[0]) / abs(A[0]), abs(A[0] - gr) / abs(gr)))
    check("H10 midpoint coupling, two on-shell scalar pairs at q, -q: distance from -4(T.T - trT trT/2)/q^2 falls ~4x on halving (O(k^2)); gauge-fixing dependence (lambda 1 -> 10) falls ~16x (O(k^4))",
          all(3.0 < o10[i][1] / o10[i + 1][1] < 4.5 and o10[i][0] / o10[i + 1][0] > 12 for i in range(2)),
          "from EH form " + ", ".join(f"{o[1]:.1e}" for o in o10) + "; gauge " + ", ".join(f"{o[0]:.1e}" for o in o10) + " (s = 0.1, 0.05, 0.025)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
