#!/usr/bin/env python3
"""Scale ladder, gravity rung: what fixes the supplied Kuhn-complex Regge graviton's form and cone.

Finite floating-point checks on the supplied 4D path (Kuhn) complex on Z^3 x Z_tau
(24 path 4-simplices per cell, 15 edge classes; index 3 = tick), with flat edge lengths
l_v^2 = v^T g0 v and g0 = 1 + b u u^T, u = (1,1,1,1):
  C1 census: gauge-invariant two-derivative quadratic forms under B4, K48 = S4 x {+-1}
     (the complex's isometries) and spatial O_h x tick reversal; K48 + tick reflection = B4.
  C2 the two K48 gauge-invariant spin-2 forms are the linearised EH forms of K48-invariant flat metrics.
  C3 the line-map pullback of the Regge form has O(k^2) symbol -(1/4) sqrt(det g0) EH_g0; C3b the same holds
     for the full edge form with non-metric edges eliminated at b != 0, while at b = 0 that elimination goes soft.
  C4 P1 scalar and Whitney-1-form Maxwell on the same complex: leading symbols are sqrt(g) x continuum in g0.
  C5 b != 0 gives complex on-shell tick momenta for real spatial momenta; b = 0 gives real energies.
  C6 O(k^4) on-shell fingerprints at b = 0: Regge TT = P1 scalar = -(1 + sum n^4)/12; Whitney Maxwell differs.
  C7 at b = 0 the Regge TT pair lies exactly on the P1 scalar's lattice shell sum 4 sin^2(p/2) = 0.
  C8 the fifth exact zero mode of the Regge form occurs at b = 0 and not at b != 0.
  C8b the fifth null direction exists on diagonal backgrounds, lifts linearly in b, and has metric part u u^T - 2*1.
  C9 the P1 scalar's stress obeys the vertex-displacement Ward identity to leading order only.
  C10 the on-shell P1 stress sources the fifth null direction at leading order.
  C11 the pullback's static response to T_tt is -2/k^2 isotropically, and exactly -2/(4 sin^2(k/2)) on the axis.
Supplied models only; no physical identification.
Companion: docs/SCALE_LADDER_GRAVITY_REGGE_METRIC_UNIVERSALITY_COMMON_CONE_BOUNDED_THEOREM_NOTE_2026-10-18.md
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
HC = R4.HCOMPS                                   # (0,0),(1,1),(2,2),(3,3),(0,1),...
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

# ------------------------------------------------------------------ P1 scalar and Whitney Maxwell on the same complex
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

def maxwell(k, g0):
    gi = np.linalg.inv(g0); Q = np.zeros((15, 15), complex)
    def F(kk, vs, Ei):
        Fe = np.zeros((4, 4, 15), complex)
        for i in range(1, 5):
            for j in range(i + 1, 5):
                r = np.zeros(15, complex)
                for (p, q) in [(0, i), (i, j), (j, 0)]:
                    c, anc, sg = edge(vs[p], vs[q]); r[c] += sg * np.exp(1j * kk @ anc)
                Fe[i - 1, j - 1] = 2 * r; Fe[j - 1, i - 1] = -2 * r
        return np.einsum('ma,abc,nb->mnc', Ei, Fe, Ei)
    for vs in SIMP:
        E, vol = geom(vs, g0); Ei = np.linalg.inv(E)
        Q += 0.5 * vol * np.einsum('mnc,rsd,mr,ns->cd', F(-k, vs, Ei), F(k, vs, Ei), gi, gi)
    return Q

def lmap(k):
    M = np.zeros((15, 4), complex)
    for c, v in enumerate(DIRS):
        z = k @ v; M[c] = (1.0 if abs(z) < 1e-14 else (np.exp(1j * z) - 1) / (1j * z)) * v
    return M

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


def main():
    I4 = np.eye(4)
    # ---------------- C1 census
    expect = {(0, 2): {'B4': 1, 'K48': 2, 'OhT': 2}, (1, 2): {'B4': 1, 'K48': 2, 'OhT': 2},
              (2, 2): {'B4': 1, 'K48': 2, 'OhT': 2}, (2, 0): {'B4': 0, 'K48': 0, 'OhT': 0}}
    got, gaps, K48SP2 = {}, [], None
    for (spin, n), ex in expect.items():
        for gname in ex:
            B, W, ninv, ng, gap = census(spin, n, GROUPS[gname]); got[(spin, n, gname)] = (ninv, ng); gaps.append(gap)
            if (spin, n, gname) == (2, 2, 'K48'): K48SP2 = (B, W)
    ok = all(got[(sp, n, g)][1] == v for (sp, n), e in expect.items() for g, v in e.items())
    sep = min(g[0] for g in gaps) / max(max(g[1] for g in gaps), 1e-300)
    check("C1 gauge-invariant forms: scalar/spin-1/spin-2 at k^2 = 1,1,1 (B4), 2,2,2 (K48), 2,2,2 (OhT); spin-2 mass 0",
          ok, f"invariant spin-2 forms B4/K48/OhT = {got[(2,2,'B4')][0]}/{got[(2,2,'K48')][0]}/{got[(2,2,'OhT')][0]}; rank gap >= {sep:.0e}")
    theta = np.diag([1, 1, 1, -1.0]); gen = [np.round(g).astype(int) for g in GROUPS['K48']] + [theta.astype(int)]
    closure = {tuple(g.flatten()) for g in gen}; frontier = list(closure)
    while frontier:
        new = []
        for a in frontier:
            for b in gen:
                c = tuple((np.array(a).reshape(4, 4) @ b).flatten())
                if c not in closure: closure.add(c); new.append(c)
        frontier = new
    check("C1 K48 together with tick reflection generates the full hyperoctahedral group", len(closure) == 384, f"order {len(closure)}")

    # ---------------- C2 K48 span = linearised EH of K48-invariant flat metrics
    B, W = K48SP2; W, _ = np.linalg.qr(W)
    cE0, r0 = fit(lambda x, h, k: EH(h, k, I4), B)
    g03 = I4 + 0.3 * np.outer(U, U); cE3, r3 = fit(lambda x, h, k: EH(h, k, g03), B)
    out = [np.linalg.norm(c - W @ (W.T @ c)) / np.linalg.norm(c) for c in (cE0, cE3)]
    indep = np.linalg.svd(np.array([W.T @ cE0 / np.linalg.norm(cE0), W.T @ cE3 / np.linalg.norm(cE3)]), compute_uv=False)
    check("C2 EH of g0 = 1 and g0 = 1 + 0.3 u u^T both lie in the K48 gauge-invariant pair and span it",
          max(out) < 1e-10 and indep[-1] > 0.1, f"outside {max(out):.1e}; second singular value {indep[-1]:.3f}")

    # ---------------- C3 metric universality of the Regge leading symbol
    worst, coefs = 0.0, []
    for b in (0.0, 0.3, -0.15):
        g0 = I4 + b * np.outer(U, U); Qe, Mh = regge(g0)
        def Qh(k): return Mh(-k).T @ Qe(k) @ Mh(k)
        def FR(x, h, k):
            a = [Qh(e * k) / e ** 2 for e in (2e-3, 1e-3)]; Q2 = (4 * a[1] - a[0]) / 3
            return float(np.real(x @ (0.5 * (Q2 + Q2.T)) @ x))
        cR, _ = fit(FR, B, nsamp=700); cE, _ = fit(lambda x, h, k: EH(h, k, g0), B, nsamp=700)
        lam = (cR @ cE) / (cE @ cE); mis = np.linalg.norm(cR - lam * cE) / np.linalg.norm(cR)
        target = -0.25 * np.sqrt(np.linalg.det(g0)); worst = max(worst, mis, abs(lam - target))
        coefs.append(f"{lam:+.6f}")
    check("C3 line-map pullback Q_h = M^T Q M: O(k^2) symbol = -(1/4) sqrt(det g0) EH_g0 at b = 0, 0.3, -0.15",
          worst < 1e-5, f"coefficients {', '.join(coefs)} vs {-0.25:+.6f}, {-0.25*np.sqrt(2.2):+.6f}, {-0.25*np.sqrt(0.4):+.6f}; worst {worst:.1e}")

    # ---------------- C3b full edge form with the five non-metric edge directions eliminated
    worst, soft = 0.0, {}
    for b in (0.3, 0.05):
        g0 = I4 + b * np.outer(U, U); Qe, Mh = regge(g0); Cb = compl(Mh(np.zeros(4)))
        def FS(x, h, k):
            a = [schur(Qe(e * k), Mh(e * k), Mh(-e * k), Cb) / e ** 2 for e in (2e-3, 1e-3)]; S2 = (4 * a[1] - a[0]) / 3
            return float(np.real(x @ (0.5 * (S2 + S2.T)) @ x))
        cS, _ = fit(FS, B, nsamp=700); cE, _ = fit(lambda x, h, k: EH(h, k, g0), B, nsamp=700)
        lam = (cS @ cE) / (cE @ cE)
        worst = max(worst, np.linalg.norm(cS - lam * cE) / np.linalg.norm(cS), abs(lam + 0.25 * np.sqrt(np.linalg.det(g0))))
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
    for b in (0.3, 0.0):
        Qe, Mh = regge(I4 + b * np.outer(U, U)); Cb = compl(Mh(np.zeros(4)))
        soft[b] = [np.min(np.abs(np.linalg.eigvals(Cb.T @ Qe(s * kd) @ Cb))) for s in (0.02, 0.01)]
    check("C3b eliminating the non-metric edges: symbol = -(1/4) sqrt(det g0) EH_g0 at b = 0.3, 0.05; at b = 0 the eliminated block goes soft as k^2",
          worst < 1e-5 and soft[0.3][1] > 1 and abs(soft[0.0][0] / soft[0.0][1] - 4) < 0.05,
          f"worst {worst:.1e}; smallest eliminated eigenvalue b=0.3: {soft[0.3][1]:.1f}; b=0: {soft[0.0][0]:.2e} -> {soft[0.0][1]:.2e} on halving k")

    # ---------------- C4 P1 scalar and Whitney Maxwell leading symbols
    rng = np.random.default_rng(7); dev = 0.0
    for b in (0.0, 0.3):
        g0 = I4 + b * np.outer(U, U); gi = np.linalg.inv(g0); sq = np.sqrt(np.linalg.det(g0))
        for _ in range(4):
            kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); A = rng.standard_normal(4)
            rs = [scalar(s * kd, g0).real / s ** 2 for s in (2e-3, 1e-3)]
            dev = max(dev, abs((4 * rs[1] - rs[0]) / 3 / (sq * kd @ gi @ kd) - 1))
            rm = []
            for s in (2e-3, 1e-3):
                k = s * kd; Fc = 1j * (np.outer(k, A) - np.outer(A, k))
                cont = 0.5 * np.real(np.einsum('mn,rs,mr,ns->', np.conj(Fc), Fc, gi, gi))
                rm.append(np.real(np.conj(lmap(k) @ A) @ maxwell(k, g0) @ (lmap(k) @ A)) / cont)
            dev = max(dev, abs((4 * rm[1] - rm[0]) / 3 / sq - 1))
    check("C4 P1 scalar and Whitney Maxwell on the same complex: leading symbol = sqrt(g) x continuum form in g0 (b = 0, 0.3)",
          dev < 1e-6, f"max relative deviation {dev:.1e}")

    # ---------------- C5 real energies only at b = 0
    res = {}
    for b in (0.0, 0.3):
        g0 = I4 + b * np.outer(U, U); ks = 0.6 * np.array([0.48, 0.6, 0.64])
        kt = newton(lambda t: scalar(np.array([*ks, t]), g0), 0.6j); res[b] = kt
    check("C5 real spatial momentum: tick momentum on the scalar shell is pure imaginary (real energy) at b = 0, complex at b = 0.3",
          abs(res[0.0].real) < 1e-12 and abs(res[0.3].real) > 1e-3, f"k_t = {res[0.0]:.6f} (b=0), {res[0.3]:.6f} (b=0.3)")

    # ---------------- C6 O(k^4) on-shell fingerprints at b = 0
    Qe0, Mh0 = regge(I4); Cr = compl(Mh0(np.zeros(4))); Cm = compl(lmap(np.zeros(4)))
    def alphas(n, k):
        p = np.array([*(k * n), 1j * k])
        a = np.cross(n, [0.3, 0.5, 0.7]); a /= np.linalg.norm(a); bb = np.cross(n, a)
        e1, e2 = np.array([*a, 0]), np.array([*bb, 0])
        Sm = schur(maxwell(p, I4), lmap(p), lmap(-p), Cm); Em = np.array([e1, e2]).T
        vec = lambda h: np.array([h[x, y] for (x, y) in HC])
        Et = np.array([vec(np.outer(e1, e1) - np.outer(e2, e2)), vec(np.outer(e1, e2) + np.outer(e2, e1))]).T
        Sr = schur(Qe0(p), Mh0(p), Mh0(-p), Cr)
        return (np.array([scalar(p, I4).real / k ** 4]),
                np.sort(np.linalg.eigvals(Em.T @ Sm @ Em).real) / k ** 4,
                np.sort(np.linalg.eigvals(Et.T @ Sr @ Et).real) / (-0.5 * k ** 4))
    rows, worst_law, split = {}, 0.0, {}
    for name, n in {'axis': (1, 0, 0), 'face': (1, 1, 0), 'face-': (1, -1, 0), 'body': (1, 1, 1), 'gen': (3, 1, 2)}.items():
        n = np.array(n, float); n /= np.linalg.norm(n); law = -(1 + (n ** 4).sum()) / 12
        a1, a2 = alphas(n, 0.02), alphas(n, 0.01); r = [(4 * y - x) / 3 for x, y in zip(a1, a2)]
        worst_law = max(worst_law, abs(r[0][0] - law), *np.abs(r[2] - law)); rows[name] = r; split[name] = r[1]
    check("C6 O(k^4): Regge TT pair and P1 scalar both obey omega^2 = k^2[1 - k^2 (1 + sum n^4)/12] (5 directions)",
          worst_law < 1e-5, f"worst deviation {worst_law:.1e}; axis/face/body = -1/6, -1/8, -1/9")
    check("C6 Whitney Maxwell differs at O(k^4): birefringent on the axis and face+ != face- (S4-only harmonic)",
          abs(split['axis'][1] - split['axis'][0]) > 1e-3 and abs(split['face'][0] - split['face-'][0]) > 1e-3,
          f"axis {split['axis'][0]:+.4f}/{split['axis'][1]:+.4f}; face+ {split['face'][0]:+.4f}, face- {split['face-'][0]:+.4f}")

    # ---------------- C7 exact lattice shell at b = 0
    on_max, off_min, mx_min = 0.0, 1.0, 1.0
    for n in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2), (3, -1, 2), (1, -2, 0.5)]:
        n = np.array(n, float); n /= np.linalg.norm(n)
        for km in (0.3, 0.9, 1.5, 2.5):
            ks = km * n; p = np.array([*ks, lattice_kt(ks)])
            s_on = sv(Qe0(p)); s_off = sv(Qe0(np.array([*ks, 1.01 * lattice_kt(ks)])))
            on_max = max(on_max, s_on[6], abs(scalar(p, I4)) / max(km ** 2, 1)); off_min = min(off_min, s_off[5])
            mx_min = min(mx_min, sv(maxwell(p, I4))[1])
    check("C7 b = 0: on sum_mu 4 sin^2(p_mu/2) = 0 the Regge edge form has 7 null directions (5 off shell); the P1 scalar vanishes there",
          on_max < 1e-13 and off_min > 1e-7, f"7th singular value on shell <= {on_max:.1e}; 6th off shell >= {off_min:.1e} (k up to 2.5, 6 directions)")
    check("C7 Whitney Maxwell is not on that shell at finite k", mx_min > 1e-7, f"its 2nd singular value there >= {mx_min:.1e}")

    # ---------------- C8 fifth zero mode only at b = 0
    counts = {}
    for b in (0.0, 0.3, -0.15):
        Qe, _ = regge(I4 + b * np.outer(U, U)); rr = np.random.default_rng(5); c = []
        for _ in range(3): c.append(int((sv(Qe(0.5 * rr.standard_normal(4))) < 1e-12).sum()))
        counts[b] = c
    check("C8 null directions at real momenta: 5 at b = 0, 4 (the vertex displacements) at b = 0.3, -0.15",
          counts[0.0] == [5] * 3 and counts[0.3] == [4] * 3 and counts[-0.15] == [4] * 3, f"{counts}")

    # ---------------- C8b the fifth null direction: diagonal backgrounds, linear lift, metric content
    def gauge_e(k):
        G = np.zeros((15, 4), complex)
        for c, v in enumerate(R4.DIRS15):
            vv = np.array(v, float); G[c] = (np.exp(1j * k @ vv) - 1) * vv / np.linalg.norm(vv)
        return G
    def fifth(Qe, k):
        _, _, vh = np.linalg.svd(Qe(k)); N = vh[-5:].conj().T; G = gauge_e(k)
        r = N - G @ np.linalg.pinv(G) @ N; return np.linalg.svd(r)[0][:, 0]
    q = np.array([0.3, -0.2, 0.25, 0.0])
    gst = I4.copy(); gst[3, 3] = 1.3
    n_diag = int((sv(regge(gst)[0](q)) < 1e-12).sum())
    lift = [np.sort(np.linalg.svd(regge(I4 + b * np.outer(U, U))[0](q), compute_uv=False))[4] / b for b in (1e-6, 1e-4)]
    vecc = lambda H: np.array([H[x, y] for (x, y) in HC], complex)
    Wt = np.diag([1, 1, 1, 1, 2, 2, 2, 2, 2, 2.0]); cosmin = 1.0; rr = np.random.default_rng(1)
    for _ in range(3):
        qq = 0.02 * rr.standard_normal(4); f = fifth(Qe0, qq); a, *_ = np.linalg.lstsq(Mh0(qq), f, rcond=None)
        Gm = np.array([vecc(np.outer(qq, e) + np.outer(e, qq)) for e in I4]).T; P = np.eye(10) - Gm @ np.linalg.pinv(Gm)
        x, y = P @ a, P @ vecc(np.outer(U, U) - 2 * I4)
        cosmin = min(cosmin, abs(np.conj(x) @ Wt @ y) / np.sqrt(abs(np.conj(x) @ Wt @ x) * abs(np.conj(y) @ Wt @ y)))
    check("C8b fifth null direction: present on the diagonal background diag(1,1,1,1.3), lifted linearly in b, metric part = u u^T - 2*1 mod gauge",
          n_diag == 5 and abs(lift[0] / lift[1] - 1) < 0.05 and cosmin > 1 - 1e-6,
          f"nullity {n_diag}; sv5/b = {lift[0]:.2f}, {lift[1]:.2f}; min cosine {cosmin:.8f}")

    # ---------------- C9 Ward identity of the P1 scalar's stress
    def W(k1, k2, xi):
        q = k1 - k2; tot = 0j
        for vs in SIMP:
            E = np.array([vs[i] - vs[0] for i in range(1, 5)], float); G = E @ E.T; Gi = np.linalg.inv(G)
            d2 = np.array([np.exp(1j * k2 @ v) for v in vs])[1:] - 1; d1 = np.array([np.exp(-1j * k1 @ v) for v in vs])[1:] - 1
            X = d1 @ Gi @ d2; P = np.outer(Gi @ d2, Gi @ d1); P = 0.5 * (P + P.T)
            Psi = np.sqrt(np.linalg.det(G)) / 24 * (0.5 * Gi * X - P)
            dE = np.array([xi * np.exp(1j * q @ v) for v in vs]); dE = dE[1:] - dE[0]
            tot += np.sum(Psi * (E @ dE.T + dE @ E.T))
        return tot
    rr = np.random.default_rng(2); ron, roff = [], []
    for _ in range(3):
        n1, n2, xi = rr.standard_normal(3), rr.standard_normal(3), rr.standard_normal(4)
        vals_on, vals_off = [], []
        for s in (0.1, 0.05):
            k1s, k2s = s * n1 / np.linalg.norm(n1), 0.7 * s * n2 / np.linalg.norm(n2)
            k1 = np.array([*k1s, lattice_kt(k1s)])
            vals_on.append(abs(W(k1, np.array([*k2s, lattice_kt(k2s)]), xi)))
            vals_off.append(abs(W(k1, np.array([*k2s, 1.2 * lattice_kt(k2s)]), xi)))
        ron.append(vals_on[0] / vals_on[1]); roff.append(vals_off[0] / vals_off[1])
    check("C9 P1 scalar stress: on-shell Ward violation falls as s^5 (relative (a/w)^2), off-shell response as s^3",
          all(abs(r - 32) < 1.0 for r in ron) and all(abs(r - 8) < 0.5 for r in roff),
          f"halving ratios on shell {', '.join(f'{r:.2f}' for r in ron)}; off shell {', '.join(f'{r:.2f}' for r in roff)}")

    # ---------------- C10 the P1 stress sources the fifth direction at leading order
    def J_edge(k1, k2):
        qv = k1 - k2; J = np.zeros(15, complex)
        for vs in SIMP:
            E = np.array([vs[i] - vs[0] for i in range(1, 5)], float); G = E @ E.T; Gi = np.linalg.inv(G)
            d2 = np.array([np.exp(1j * k2 @ v) for v in vs])[1:] - 1; d1 = np.array([np.exp(-1j * k1 @ v) for v in vs])[1:] - 1
            X = d1 @ Gi @ d2; P = np.outer(Gi @ d2, Gi @ d1); P = 0.5 * (P + P.T)
            Psi = np.sqrt(np.linalg.det(G)) / 24 * (0.5 * Gi * X - P)
            for i in range(5):
                for j in range(i + 1, 5):
                    c, anc, _ = edge(vs[i], vs[j]); dl2 = 2 * np.linalg.norm(vs[j] - vs[i]) * np.exp(1j * qv @ anc)
                    dG = np.zeros((4, 4), complex)
                    if i == 0:
                        dG[j - 1, j - 1] += dl2
                        for bb in range(4):
                            if bb != j - 1: dG[j - 1, bb] += dl2 / 2; dG[bb, j - 1] += dl2 / 2
                    else:
                        dG[i - 1, j - 1] -= dl2 / 2; dG[j - 1, i - 1] -= dl2 / 2
                    J[c] += np.sum(Psi * dG)
        return J
    rr = np.random.default_rng(9); fr = []
    for _ in range(2):
        n1, n2 = rr.standard_normal(3), rr.standard_normal(3); row = []
        for s in (0.1, 0.05):
            k1s, k2s = s * n1 / np.linalg.norm(n1), 0.7 * s * n2 / np.linalg.norm(n2)
            k1, k2 = np.array([*k1s, lattice_kt(k1s)]), np.array([*k2s, lattice_kt(k2s)])
            J = J_edge(k1, k2); row.append(abs(np.vdot(fifth(Qe0, k1 - k2), J)) / np.linalg.norm(J))
        fr.append(row)
    check("C10 on-shell P1 stress has a scale-independent component along the fifth null direction (sourced at leading order)",
          all(r[1] > 0.05 and abs(r[0] / r[1] - 1) < 0.1 for r in fr), "fractions " + "; ".join(f"{r[0]:.3f} -> {r[1]:.3f}" for r in fr))

    # ---------------- C11 Newtonian rung of the pullback: static T_tt response
    itt = HC.index((3, 3)); hk2, hax = [], []
    for n in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); k = np.array([*(0.01 * n), 0.0])
        T = np.zeros(10); T[itt] = 1.0; h = np.linalg.pinv(Mh0(-k).T @ Qe0(k) @ Mh0(k), rcond=1e-9) @ T; hk2.append(h[itt].real * 1e-4)
    for km in (0.5, 1.5):
        k = np.array([km, 0, 0, 0.0]); T = np.zeros(10); T[itt] = 1.0
        h = np.linalg.pinv(Mh0(-k).T @ Qe0(k) @ Mh0(k), rcond=1e-9) @ T; hax.append(h[itt].real * 4 * np.sin(km / 2) ** 2)
    check("C11 pullback static response to T_tt: h_tt k^2 -> -2 in 4 directions (continuum -EH/4); on the axis h_tt = -2 / (4 sin^2(k/2)) exactly",
          max(abs(x + 2) for x in hk2) < 1e-3 and max(abs(x + 2) for x in hax) < 1e-9,
          f"k = 0.01: {', '.join(f'{x:+.5f}' for x in hk2)}; axis k = 0.5, 1.5: {', '.join(f'{x:+.9f}' for x in hax)}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
