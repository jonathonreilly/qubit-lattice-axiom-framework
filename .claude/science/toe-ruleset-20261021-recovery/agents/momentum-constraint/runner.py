#!/usr/bin/env python3
"""momentum-constraint: lattice momentum constraints (vertex displacements) on CL-1's six-edge triangulation.

Spatial triangulation: Z^3 torus, every unit cube five tetrahedra alternating between neighbours (axis edges + the
face diagonals joining even-sum corners; 6 edges per site).  The momentum constraint of a vertex is the generator of
its displacement, C_v = sum_e (dl_e/dX_v) p_e.  Checks: exactness on the flat sector, breaking off it (spatial hinge
sum), a matter proxy, the linear scalar sector with a breaking term, register quantisation, and the projector fix.
Tags: [T] exact theorem/identity checked numerically, [D] finite diagnostic, [E] estimate vs measurement.
numpy / scipy / sympy only.
"""
import itertools, time, signal
import numpy as np
import sympy as sp
from scipy.linalg import expm, polar

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(AUDIT_TIMEOUT_SEC)
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(7)


def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


# ---------------- triangulation ----------------
def torus(P):
    """five-tetrahedra torus of side P (P even). Returns edges (a,b), wrap vectors, tet->edge, tet vertices, offsets."""
    idx = lambda v: (v[0] % P) * P * P + (v[1] % P) * P + (v[2] % P)
    pos = np.array(list(itertools.product(range(P), repeat=3)), float)
    edges, tet_e, tv, off = {}, [], [], []
    for o in itertools.product(range(P), repeat=3):
        o = np.array(o); C = [o + np.array(c) for c in itertools.product((0, 1), repeat=3)]
        ev = [c for c in C if c.sum() % 2 == 0]; od = [c for c in C if c.sum() % 2 == 1]
        for T in [ev] + [[q] + [c for c in ev if np.abs(c - q).sum() == 1] for q in od]:
            row = []
            for i, j in itertools.combinations(range(4), 2):
                ia, ib, w = idx(T[i]), idx(T[j]), T[j] - T[i]
                key = (ia, ib, tuple(w)) if ia < ib else (ib, ia, tuple(-w))
                edges.setdefault(key, len(edges)); row.append(edges[key])
            tet_e.append(row); tv.append([idx(c) for c in T]); off.append(np.array(T, float))
    E = np.array([[k[0], k[1]] for k in edges]); W = np.array([k[2] for k in edges], float)
    W = W - (pos[E[:, 1]] - pos[E[:, 0]])
    return E, W, np.array(tet_e), np.array(tv), np.array(off), pos


PAIR = list(itertools.combinations(range(4), 2))
def dihedrals(L):
    l2 = L ** 2; d = {p: l2[:, k] for k, p in enumerate(PAIR)}
    d2 = lambda a, b: d[(min(a, b), max(a, b))]
    G = np.zeros((L.shape[0], 3, 3))
    for a in range(1, 4):
        for b in range(1, 4):
            G[:, a - 1, b - 1] = 0.5 * (d2(0, a) + d2(0, b) - (d2(a, b) if a != b else 0))
    Di = np.linalg.inv(np.linalg.cholesky(G))
    gr = [-Di.sum(axis=2)] + [Di[:, :, a] for a in range(3)]
    out = np.zeros_like(L)
    for k, (i, j) in enumerate(PAIR):
        a, b = [m for m in range(4) if m not in (i, j)]
        c = -(gr[a] * gr[b]).sum(1) / np.linalg.norm(gr[a], axis=1) / np.linalg.norm(gr[b], axis=1)
        out[:, k] = np.arccos(np.clip(c, -1, 1))
    return out, np.sqrt(np.linalg.det(G)) / 6


def deficits(l, TE):
    th, vol = dihedrals(l[TE]); s = np.zeros(len(l)); np.add.at(s, TE.ravel(), th.ravel())
    return 2 * np.pi - s, vol.sum()


def lengths(X, E, W, f=None):
    D = X[E[:, 1]] + W - X[E[:, 0]]; s2 = (D ** 2).sum(1)
    if f is not None: s2 = s2 + (f[E[:, 1]] - f[E[:, 0]]) ** 2
    return np.sqrt(s2)


# ---------------- A. flat sector ----------------
print('== A. flat sector (P = 4 torus, 64 sites, 384 edge registers)')
P = 4; E, W, TE, TV, OFF, X0 = torus(P); ne, nv = len(E), P ** 3
l0 = lengths(X0, E, W); e0, V0 = deficits(l0, TE)
dmax, dvol = 0, 0
for r in range(3):
    X1 = X0 + 0.05 * rng.normal(size=X0.shape); e1, V1 = deficits(lengths(X1, E, W), TE)
    dmax = max(dmax, np.abs(e1).max()); dvol = max(dvol, abs(V1 - V0))
check('A1 [T] finite flat displacements keep every deficit 0 and the volume fixed: the flat sector is an exact (abelian) orbit; hinge sum and constant per volume exactly invariant',
      dmax < 1e-12 and dvol < 1e-12, f'max |deficit| {dmax:.0e}, |dVol| {dvol:.0e} (amplitude 0.05 l, 3 draws)')
h = 1e-5; H = np.zeros((ne, ne))
for e in range(ne):
    lp = l0.copy(); lp[e] += h; lm = l0.copy(); lm[e] -= h
    H[:, e] = (deficits(lp, TE)[0] - deficits(lm, TE)[0]) / (2 * h)
H = 0.5 * (H + H.T); evH = np.linalg.eigvalsh(H)
u = (X0[E[:, 1]] + W - X0[E[:, 0]]) / l0[:, None]; J = np.zeros((ne, 3 * nv))
for k, (a, b) in enumerate(E): J[k, 3 * b:3 * b + 3] += u[k]; J[k, 3 * a:3 * a + 3] -= u[k]
nz = int(np.sum(np.abs(evH) < 1e-6 * np.abs(evH).max())); rJ = np.linalg.matrix_rank(J)
check('A2 [T] linear order: Hessian kernel = displacements + flat moduli, HJ = 0 at EVERY lattice k; C = J^T p commutes with exp(-i(T(p)+V2)tau) for any step and any T(p): first class, exact',
      nz == rJ + 6 and rJ == 3 * nv - 3 and np.abs(H @ J).max() < 1e-8,
      f'kernel {nz} = {rJ} displacements (3x64-3) + 6 moduli; |HJ| {np.abs(H @ J).max():.0e}; lightest massive {np.sort(np.abs(evH))[nz]:.3f}')

# ---------------- B. off the flat sector ----------------
print('== B. curved slices: smooth 3-geometry x4 = f(x) in R^4, chord lengths (exact secant triangulation)')
q = 2 * np.pi
def fgraph(X, kap):
    x, y, z = X[:, 0], X[:, 1], X[:, 2]
    f = (kap / q) * (np.sin(q * x + .3) * np.sin(q * y + .7) + .5 * np.cos(q * z + 1.1) + .4 * np.sin(q * (x + z) + .2))
    gx = kap * np.cos(q * x + .3) * np.sin(q * y + .7) + .4 * kap * np.cos(q * (x + z) + .2)
    gy = kap * np.sin(q * x + .3) * np.cos(q * y + .7)
    gz = -.5 * kap * np.sin(q * z + 1.1) + .4 * kap * np.cos(q * (x + z) + .2)
    return f, np.stack([gx, gy, gz], 1)
def anomaly(P, kap):
    E, W, TE, _, _, X0 = torus(P); X0 = X0 / P; W = W / P
    f, gf = fgraph(X0, kap); D = X0[E[:, 1]] + W - X0[E[:, 0]]; df = f[E[:, 1]] - f[E[:, 0]]
    l = np.sqrt((D ** 2).sum(1) + df ** 2); eps = deficits(l, TE)[0]
    gb = (D + df[:, None] * gf[E[:, 1]]) / l[:, None]; ga = -(D + df[:, None] * gf[E[:, 0]]) / l[:, None]
    A = np.zeros((len(X0), 3)); Fn = np.zeros(len(X0))
    np.add.at(A, E[:, 1], eps[:, None] * gb); np.add.at(A, E[:, 0], eps[:, None] * ga)
    np.add.at(Fn, E[:, 1], np.abs(eps) * np.linalg.norm(gb, axis=1)); np.add.at(Fn, E[:, 0], np.abs(eps) * np.linalg.norm(ga, axis=1))
    Sof = lambda Y: (lambda ll: (ll * deficits(ll, TE)[0]).sum())(lengths(Y, E, W, fgraph(Y, kap)[0]))
    return np.sqrt((A ** 2).sum(1).mean()), np.sqrt((Fn ** 2).mean()), np.abs(eps).max(), A, Sof, X0
a4, fn4, em4, A4, Sof, Xs = anomaly(4, 0.3); g = np.zeros(3)
for c in range(3):
    Xp = Xs.copy(); Xp[5, c] += 1e-6; Xm = Xs.copy(); Xm[5, c] -= 1e-6; g[c] = (Sof(Xp) - Sof(Xm)) / 2e-6
check('B1 [T] Schlafli: moving a vertex along the fixed smooth geometry changes the hinge sum by A_v = sum deficit dl/dX (the anomaly; 0 in the continuum)', np.abs(g - A4[5]).max() < 1e-8 * max(1, np.abs(g).max()) + 1e-9,
      f'FD {np.array2string(g, precision=7)} vs formula {np.array2string(A4[5], precision=7)}')
r1 = anomaly(8, 0.1); r2 = anomaly(8, 0.2)
ratio = r2[0] / r1[0]
check('B2 [T] first order cancels (J0^T H = 0, lattice Bianchi): A ~ eta^2 (eta = metric perturbation ~ kappa^2)',
      abs(ratio - 16) < 0.6, f'A(kappa=0.2)/A(kappa=0.1) = {ratio:.2f} (eta^2 -> 16); max deficit {r1[2]:.2e}')
rows, prev = [], None
for Pn in (8, 12, 16, 24):
    a, fn, em, *_ = anomaly(Pn, 0.1); rr = a / fn
    pA = None if prev is None else np.log(prev[0] / a) / np.log(Pn / prev[2])
    pr = None if prev is None else np.log(prev[1] / rr) / np.log(Pn / prev[2])
    rows.append((Pn, a, rr, em, pA, pr)); prev = (a, rr, Pn)
cr = rows[-1][2] / (rows[-1][3] * (q / rows[-1][0]))
check('B3 [D] refining at fixed geometry: A_v -> l^5, relative violation r -> l^3 = c (R l^2)(q l); at cell-scale curvature r ~ R l^2',
      4.6 < rows[-1][4] < 5.2 and 2.7 < rows[-1][5] < 3.2,
      'P, A, r, max deficit, local exponents of A and r: ' + '; '.join(
          f'{p}: {a:.2e}, {r:.2e}, {e:.1e}' + ('' if x is None else f', {x:.2f}, {y:.2f}') for p, a, r, e, x, y in rows) +
      f'; c = r/(eps_max q l) = {cr:.3f}')

# ---------------- C. matter proxy ----------------
print('== C. matter proxy on a flat displaced lattice (P1 Laplacian read from the tetrahedra, lumped mass)')
def fem(P, s):
    E, W, TE, TV, OFF, X0 = torus(P); X0 = X0 / P; OFF = OFF / P
    dX = (s / q) * np.stack([np.sin(q * X0[:, 1] + .4), np.sin(q * X0[:, 2] + .1), np.sin(q * X0[:, 0] + .9)], 1)
    C = OFF + dX[TV]; M = C[:, 1:] - C[:, :1]; V = np.abs(np.linalg.det(M)) / 6; Gi = np.linalg.inv(M)
    gr = np.concatenate([-Gi.sum(2)[:, None, :], np.transpose(Gi, (0, 2, 1))], 1)
    loc = V[:, None, None] * np.einsum('tai,tbi->tab', gr, gr); n = P ** 3; K = np.zeros((n, n)); Ml = np.zeros(n)
    for a in range(4):
        np.add.at(Ml, TV[:, a], V / 4)
        for b in range(4): np.add.at(K, (TV[:, a], TV[:, b]), loc[:, a, b])
    Mi = 1 / np.sqrt(Ml); w = np.linalg.eigvalsh(Mi[:, None] * K * Mi[None, :])
    return w[1:7].mean() / (4 * np.pi ** 2), V.sum()
mres = {}
for Pn in (6, 12):
    w0, _ = fem(Pn, 0)
    for s_ in (0.05, 0.1):
        w1, vol = fem(Pn, s_); mres[(Pn, s_)] = (w1 - w0) / w0
cm = mres[(12, 0.05)] / (0.05 ** 2 * (q / 12) ** 2)
check('C1 [D] matter proxy (P1 Laplacian from the tetrahedra) sees vertex positions at c s^2 (kl)^2 (strain s, geometry flat)',
      3.6 < mres[(6, .1)] / mres[(6, .05)] < 4.4 and 3.3 < mres[(6, .05)] / mres[(12, .05)] < 4.7,
      f'shift: P6 {mres[(6, .05)]:.2e}/{mres[(6, .1)]:.2e}, P12 {mres[(12, .05)]:.2e}/{mres[(12, .1)]:.2e} (s = .05/.1); c = {cm:.3f}')

# ---------------- D. linear scalar sector with a breaking term ----------------
print('== D. case A (fixed lapse, shift stationary; inhomog-volume B2 model) plus a breaking term delta Q')
t, w, dl, mu = sp.symbols('t omega delta mu'); K, KR = sp.symbols('K K_R', positive=True)
z, Ef, Bf = [sp.Function(nm)(t) for nm in ('zeta', 'E', 'B')]
def lagA(Q, Bv=Bf):
    return -6 * z.diff(t) ** 2 + 4 * K * z.diff(t) * (Ef.diff(t) - Bv) + 2 * KR * z ** 2 + 4 * KR * (z - K * Ef / 3) * z + dl * Q
def eomM(L, qs):
    am = sp.symbols('c0:%d' % len(qs)); sb = {x: c * sp.exp(-sp.I * w * t) for x, c in zip(qs, am)}
    eqs = [sp.euler_equations(L, [x], t)[0].lhs for x in qs]
    return sp.Matrix([[sp.expand(sp.simplify(eq.subs(sb).doit() * sp.exp(sp.I * w * t))).coeff(c) for c in am] for eq in eqs])
detB = sp.factor(eomM(lagA(0, 0), [z, Ef]).det())                       # case B (shift not varied)
dets = {nm: sp.factor(eomM(lagA(Q), [z, Ef, Bf]).det()) for nm, Q in
        (('shift mass K B^2', K * Bf ** 2), ('shift rate K B_t^2', K * Bf.diff(t) ** 2),
         ('displacement pair K^2(E_t^2 - mu^2 E^2)', K ** 2 * (Ef.diff(t) ** 2 - mu ** 2 * Ef ** 2)))}
d1, d2, d3 = dets.values()
Bsol = sp.solve(sp.diff(lagA(K * sp.Symbol('b') ** 2, sp.Symbol('b')), sp.Symbol('b')), sp.Symbol('b'))[0]
Leff = sp.expand(lagA(K * Bsol ** 2, Bsol)); kz = Leff.coeff(z.diff(t), 2)
Tm = sp.Matrix([[2 * kz, 4 * K], [4 * K, 0]])
okD = sp.simplify(d1 - 2 * K * dl * detB) == 0 and sp.simplify(d2 - 2 * K * dl * w ** 2 * detB) == 0 and \
      sp.simplify(d3 - 32 * K ** 4 * dl * w ** 2 * (mu ** 2 - w ** 2)) == 0 and sp.simplify(Tm.det() + 16 * K ** 2) == 0
check('D1 [T] breaking touching the shift (mass or rate, any delta != 0) restores EXACTLY the case-B spectrum, det = 2K delta det_B: the w^2 = K_R/3 ghost-normal Jordan pair returns at every k (zeta weight ~1/delta, signature (+,-)); breaking in E alone gives one mode at mu; the constraint on the odds removes all scalars', okD,
      f'det_B = {detB}; ' + '; '.join(f'{n}: {d}' for n, d in dets.items()) + f'; zeta kinetic after B eliminated {sp.simplify(kz)}')

# ---------------- E. register quantisation and the hop on an expanding background ----------------
print('== E. edge registers (CL-1: length = flat length x (1 + n/2S)) and the edge hop')
Js = J / l0[:, None]                                          # dl_e in steps (|flat Delta_e| l/2S) per l/2S of xi
ent = np.unique(np.round(np.abs(Js[np.abs(Js) > 1e-12]), 12))
xi2 = 2 * rng.integers(-3, 4, size=3 * nv); ok2 = np.abs(Js @ xi2 - np.round(Js @ xi2)).max() < 1e-9
xi1 = np.zeros(3 * nv); xi1[0] = 1; fail1 = np.abs(Js @ xi1 - np.round(Js @ xi1)).max() > 1e-9
# anisotropic slice: axis lengths a_i; a diagonal (i,j) of either sign changes by (a_i N_i +- a_j N_j)/sqrt(2(a_i^2+a_j^2))
# steps, N_i = a_i xi_i the axis-step changes; an irrational denominator forces a_i N_i = -+ a_j N_j for both signs -> N = 0
def shifts_exist(avals):
    irr = [not sp.sqrt(2 * (avals[i] ** 2 + avals[j] ** 2)).is_rational for i, j in ((0, 1), (1, 2), (0, 2))]
    return not any(irr)
iso_ok, ani_ok = shifts_exist([sp.Rational(6, 5)] * 3), shifts_exist([1, sp.Rational(11, 10), 1])
check('E1 [T] steps proportional to flat length: even shifts (2 steps/axis) map register values to register values, commute with S+ + S- (bulk) and V2; isotropic expansion keeps them; an anisotropic slice has none (irrational diagonals)',
      set(ent.tolist()) == {0.5, 1.0} and ok2 and fail1 and iso_ok and not ani_ok,
      f'|J| entries in step units {ent.tolist()}; random even shift exact {ok2}; unit shift exact {not fail1}; '
      f'isotropic a = 6/5 shifts exist {iso_ok}; anisotropic (1, 11/10, 1) shifts exist {ani_ok}')
Xd = X0 + 0.05 * rng.normal(size=X0.shape); ld = lengths(Xd, E, W)
dT = ((ld ** 2).sum() - (l0 ** 2).sum()) / (l0 ** 2).sum(); dV = abs(deficits(ld, TE)[1] - V0)
check('E2 [T] ultralocal hop on uniform expansion: H^2 sum w l_e^2 changes at 2nd order under a flat displacement (volume does not): pseudo-gauge mass ~ (H l)^2',
      abs(dT) > 1e-4 and dV < 1e-12, f'd(sum l^2)/sum l^2 = {dT:.2e} at displacement 0.05 l; dVol {dV:.0e}')

# ---------------- F. the constraint as a projector each half-tick ----------------
print('== F. constraint imposed on the odds each half-tick (finite model)')
n0, nb = 12, 36; Cv = np.r_[np.zeros(n0), rng.integers(1, 4, nb)]
H0 = np.zeros((n0 + nb, n0 + nb), complex)
for c in np.unique(Cv):
    ix = np.where(Cv == c)[0]; Ab = rng.normal(size=(len(ix),) * 2) + 1j * rng.normal(size=(len(ix),) * 2); H0[np.ix_(ix, ix)] = (Ab + Ab.conj().T) / 4
Vb = rng.normal(size=H0.shape) + 1j * rng.normal(size=H0.shape); Vb = (Vb + Vb.conj().T) / 4
Pp = np.diag((Cv == 0).astype(float)); res = []
for d in (1e-2, 1e-3):
    U = expm(-1j * (H0 + d * Vb)); leak = np.linalg.norm((np.eye(len(Cv)) - Pp) @ U @ Pp, 2) ** 2
    PUP = (U[:n0, :n0]); Wu, _ = polar(PUP); unit = np.abs(Wu.conj().T @ Wu - np.eye(n0)).max()
    Z = expm(-1j * (H0 + d * Vb)[:n0, :n0]); res.append((leak, unit, np.linalg.norm(Wu - Z, 2), np.linalg.norm(Wu - U[:n0, :n0], 2)))
check('F1 [T] constraint as projector each half-tick: leak delta^2/tick (not unitary); polar part W of PUP is unitary on the subspace, keeps the constraint exactly, = exp(-iPHP) to O(delta^2); closed since displacement generators commute',
      1.8 < np.log10(res[0][0] / res[1][0]) < 2.2 and res[0][1] < 1e-12 and res[1][2] < res[0][2] / 30,
      f'leak/tick {res[0][0]:.1e} -> {res[1][0]:.1e} (delta 1e-2 -> 1e-3); unitarity {res[0][1]:.0e}; '
      f'|W - exp(-iPHP)| {res[0][2]:.1e} -> {res[1][2]:.1e}; |W - PUP| {res[0][3]:.1e} -> {res[1][3]:.1e}')

# ---------------- G. estimates ----------------
print('== G. estimates against measurement')
lP = 1.616e-35; lr = np.sqrt(32 * np.pi) * lP          # l_rung^2 = 4 x 8 pi G hbar (unit map)
env = {'cosmic today (R ~ 4 Lambda)': 4 * 1.1e-52, 'Earth surface (GM/c^2 r^3)': 4.4e-3 / 6.37e6 ** 3,
       'neutron-star surface': 2.07e3 / 1.2e4 ** 3, 'nucleon interior (G rho/c^2)': 7.4e-28 * 4e17}
dlt = {k: v * lr ** 2 for k, v in env.items()}
Mp = 1.22e19; Lam = Mp / 10; bound = 3e-3
excess = (Lam / bound) ** 8; Ls = np.sqrt(dlt['cosmic today (R ~ 4 Lambda)']) * Mp
check('G1 [E] delta ~ R l^2 in real environments (constraints and dark-constant uniformity exact to this)',
      max(dlt.values()) < 1e-70, '; '.join(f'{k}: {v:.0e}' for k, v in dlt.items()))
check('G2 [E] shift only stationary: restored ghost pair couples gravitationally after normalisation, CJM Gamma ~ Lambda^8/M_P^4 independent of delta (excluded by ~1e165) but strongly coupled above sqrt(delta) M_P (undecided); constraint on the odds closes the channel',
      excess > 1e160 and Ls < 1e-30, f'(Lambda/3 MeV)^8 = {excess:.0e}; strong-coupling scale today sqrt(delta) M_P = {Ls:.0e} GeV')
print('supplied: secant triangulation of a smooth 3-geometry (B), P1 Laplacian as matter proxy (C), continuum ADM scalar '
      'model with generic breaking Q (D), random finite model (F). not built: 4D slab with mixed hinges off flat, CL-1 '
      'cube tick under displacement, the lattice-derived Q and its sign.')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
