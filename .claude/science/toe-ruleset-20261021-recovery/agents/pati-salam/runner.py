#!/usr/bin/env python3
"""A Pati-Salam reading of the rung-1 cell register: what is exact, what is not.
Supplied models (the CL-2 tick at rung 1 with the cell's 8 modes carried in parallel), finite exact diagnostics;
no physical identification.

A. The cell: unique corner product structure C^2 x C^4, forced generators, one (4,2), another split.
B. Exact internal symmetry of the rung-1 tick for every rotation-covariant mass pattern.
C. Spin: G = G_c x P_int, the content of the twist P_int, the rotation-blind symmetry G' = G_c x 1,
   the emergent Dirac algebra read from the tick, and a covariant spin-orbit hop that breaks G'.
D. Left/right: the sublattice sign against the emergent chirality at every step; copy locking at step pi/2.
E. Anomalies and the CL-5 link rule.  F. Generations: multiplicities of 2^n cells.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
from scipy.linalg import expm, logm

T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
nrm = lambda A: np.linalg.norm(A, 2)

# ------------------------------------------------------------------ geometry, spin-3/2 corner states, W
C = np.array(list(itertools.product((0, 1), repeat=3))); c = C - 0.5
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): ROTS.append(R)
def cname(R):
    t = round(np.trace(R))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    return 'C2f' if np.allclose(R, np.diag(np.diag(R))) else "C2'"
TAB = {'A1': dict(E=1, C3=1, C2f=1, C4=1, **{"C2'": 1}), 'A2': dict(E=1, C3=1, C2f=1, C4=-1, **{"C2'": -1}),
       'E': dict(E=2, C3=-1, C2f=2, C4=0, **{"C2'": 0}), 'T1': dict(E=3, C3=0, C2f=-1, C4=1, **{"C2'": -1}),
       'T2': dict(E=3, C3=0, C2f=-1, C4=-1, **{"C2'": 1})}
ODD = [TAB['A2'][cname(R)] == -1 for R in ROTS]
def decompose(chis):
    return {k: int(round(sum(t[cname(R)] * ch for R, ch in zip(ROTS, chis)).real / 24)) for k, t in TAB.items()}
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def Dj(j, n, a): J = Jm(j); return expm(-1j * a * sum(n[k] * J[k] for k in range(3)))
J32 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J32[k] for k in range(3))); XI.append(v_[:, -1])
def img(R, i): return int(np.argmin(np.sum(abs(c - R @ c[i]), 1)))
def corner_rep(R, twisted=True):
    D = Dj(1.5, *axang(R)); L = np.zeros((8, 8), complex)
    for i in range(8):
        k = img(R, i); L[k, i] = (XI[k].conj() @ D @ XI[i]) if twisted else 1.0
    return L
GM = np.array([[XI[a].conj() @ XI[b] for b in range(8)] for a in range(8)])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: W[a, b] = -GM[a, b] / abs(GM[a, b]) / np.sqrt(3)
SUB = np.diag([(-1.0) ** int(s.sum()) for s in C])                          # sublattice sign (-1)^(x+y+z)
PINT = [corner_rep(R, False).real for R in ROTS]                           # plain action on the cell index
GC0 = [corner_rep(R) for R in ROTS]                                        # spin-3/2 action on coarse corners
PR = {k: sum(TAB[k][cname(R)] * P for R, P in zip(ROTS, PINT)) * TAB[k]['E'] / 24 for k in TAB}
def comm_dim(gens, d, tol=1e-9):
    M = np.vstack([np.kron(g, np.eye(d)) - np.kron(np.eye(d), g.T) for g in gens])
    return int(np.sum(np.linalg.svd(M, compute_uv=False) < tol))
def Ublock(K, eps, mu):                                                      # coarse (rung-0 form) Bloch tick
    D = np.diag(np.exp(1j * (C @ K)))
    return D @ expm(1j * (eps + mu / 2) * W) @ D.conj().T @ expm(-1j * (eps - mu / 2) * W)

# ================================================================== A. the cell
print('== A. the cell of 2^3 one-mode sites')
def invariant(blocks):
    bs = [frozenset(b) for b in blocks]
    return all(frozenset(img(R, i) for i in b) in bs for b in bs for R in ROTS)
halves = [(set(h), set(range(8)) - set(h)) for h in itertools.combinations(range(8), 4) if 0 in h]
def pairings(s):
    s = sorted(s)
    if not s: yield []; return
    for b in s[1:]:
        for rest in pairings([x for x in s if x not in (s[0], b)]): yield [(s[0], b)] + rest
ih = [h for h in halves if invariant(h)]; ip = [p for p in pairings(range(8)) if invariant(p)]
nprod = sum(all(len(set(q) & h[0]) == 1 for q in p) for h in ih for p in ip)
PAR8 = np.array([int(s.sum()) % 2 for s in C]); dl = []; DIAG = {}
for i in range(8):
    key = tuple(sorted([i, 7 - i])); dl += [key] if key not in dl else []; DIAG[i] = dl.index(key)
order = [int(np.where((PAR8 == e) & (np.array([DIAG[i] for i in range(8)]) == d))[0][0]) for e in (0, 1) for d in range(4)]
BF = np.eye(8)[:, order]; X2 = np.array([[0., 1.], [1., 0.]]); PD = []
fac = True
for R, P, o in zip(ROTS, PINT, ODD):
    Pd = np.zeros((4, 4))
    for d in range(4): Pd[DIAG[img(R, dl[d][0])], d] = 1
    PD.append(Pd); fac &= np.allclose(BF.T @ P @ BF, np.kron(X2 if o else np.eye(2), Pd))
d8 = decompose([np.trace(P) for P in PINT]); d2 = decompose([0 if o else 2 for o in ODD]); d4 = decompose([np.trace(p) for p in PD])
check('A1 plain cell = A1+A2+T1+T2; one invariant halving (tetrahedra) and one invariant pairing (body diagonals) give the '
      'only product structure C^8 = C^2 x C^4, R = X^[R odd] x P_diag(R), C^2 = A1+A2, C^4 = A1+T2', d8 == dict(A1=1, A2=1, E=0, T1=1, T2=1) and len(ih) == 1 and len(ip) == 1 and nprod == 1 and fac
      and d2 == dict(A1=1, A2=1, E=0, T1=0, T2=0) and d4 == dict(A1=1, A2=0, E=0, T1=0, T2=1), f'halvings {len(ih)}, pairings {len(ip)}')
inv8 = comm_dim(PINT, 8); inv2 = comm_dim([X2 if o else np.eye(2) for o in ODD], 2); inv4 = comm_dim(PD, 4)
J4 = np.ones((4, 4)) / 4; BLm = (np.eye(4) - 4 * J4) / 3
check('A2 invariant cell operators = span{1,X} x span{1,J4}; the traceless invariant of each factor is unique: T3 = X/2, '
      'B-L = (1 - 4 J4)/3 (1/3 x3, -1; scale a convention)',
      inv8 == 4 and inv2 == 2 and inv4 == 2 and np.allclose(sorted(np.linalg.eigvalsh(BLm)), [-1, 1 / 3, 1 / 3, 1 / 3]))
H2 = np.array([[1, 1], [1, -1]]) / np.sqrt(2); Q4 = np.linalg.qr(np.column_stack([np.ones(4) / 2, np.eye(4)[:, :3]]))[0]
Q4[:, 0] *= np.sign(Q4[0, 0]); BASIS = BF @ np.kron(H2.T, Q4)                # columns: (+,lep,q1,q2,q3, -,lep,q1..q3)
pa = [X2.astype(complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]
def sun(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E)
            E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; out.append(E)
    for k in range(1, n):
        dd = np.zeros(n); dd[:k] = 1; dd[k] = -k; out.append(np.diag(dd).astype(complex))
    return out
G2 = [BASIS @ np.kron(p, np.eye(4)) @ BASIS.T for p in pa]; G4 = [BASIS @ np.kron(np.eye(2), g) @ BASIS.T for g in sun(4)]
def rot_content(gens):
    Qb = np.linalg.qr(np.array([g.ravel() for g in gens]).T)[0]
    return decompose([np.trace(Qb.conj().T @ np.array([(P @ Qb[:, i].reshape(8, 8) @ P.T).ravel() for i in range(Qb.shape[1])]).T) for P in PINT])
T3 = BASIS @ np.kron(np.diag([.5, -.5]), np.eye(4)) @ BASIS.T; BL = BASIS @ np.kron(np.eye(2), np.diag([-1, 1 / 3, 1 / 3, 1 / 3])) @ BASIS.T
br = Counter((round(t, 6), round(b, 6)) for t, b in zip(np.diag(BASIS.T @ T3 @ BASIS), np.diag(BASIS.T @ BL @ BASIS)))
c4, c2 = rot_content(G4), rot_content(G2)
forced = abs(T3 - BF @ np.kron(X2 / 2, np.eye(4)) @ BF.T).max() + abs(BL - BF @ np.kron(np.eye(2), BLm) @ BF.T).max()
check('A3 su(4)+su(2) is irreducible on the cell: one (4,2) = (3, 1/3, +-1/2) + (1, -1, +-1/2) in (colour, B-L, T3); rotations '
      'carry su(4) = A1+E+T1+3T2, su(2) = A1+2A2, so only B-L and T3 are rotation-blind', forced < 1e-12 and comm_dim(G2 + G4, 8) == 1
      and br == Counter({(0.5, 0.333333): 3, (-0.5, 0.333333): 3, (0.5, -1.0): 1, (-0.5, -1.0): 1})
      and c4 == dict(A1=1, A2=0, E=1, T1=1, T2=3) and c2 == dict(A1=1, A2=2, E=0, T1=0, T2=0))
chi_ok = all(np.isclose((2 * np.cos(axang(R)[1] / 2)) ** 2 * (1 + TAB['A2'][cname(R)]), np.trace(P)) for R, P in zip(ROTS, PINT))
check('A4 E1/2 x (E1/2+E5/2) also has the corner character: the SU(2) x SU(4) split is fixed by corner geometry, not by '
      'rotations alone', chi_ok)

# ================================================================== B. exact internal symmetry
print('== B. exact internal symmetry of the rung-1 tick (cell index carried in parallel)')
def U1(K, eps, ms): return sum(np.kron(Ublock(K, eps, ms[k]), PR[k]) for k in ('A1', 'A2', 'T1', 'T2'))
def int_comm(eps, ms, seed=0):
    rng = np.random.default_rng(seed); blocks = []
    for _ in range(3):
        U = U1(rng.normal(size=3) * 1.3, eps, ms); M = []
        for a in range(8):
            for b in range(8):
                E = np.zeros((8, 8)); E[a, b] = 1; L = np.kron(np.eye(8), E); M.append((U @ L - L @ U).ravel())
        blocks.append(np.array(M).T)
    s = np.linalg.svd(np.vstack(blocks), compute_uv=False); return int(np.sum(s < 1e-9))
PATS = {'distinct': dict(A1=.1, A2=.25, T1=.4, T2=.7), 'nu=u,e=d': dict(A1=.1, A2=.25, T1=.25, T2=.1),
        'nu=e,u=d': dict(A1=.1, A2=.1, T1=.4, T2=.4), 'equal': dict(A1=.3, A2=.3, T1=.3, T2=.3)}
dims = {e: [int_comm(e, m) for m in PATS.values()] for e in (0.04, 0.3, np.pi / 2)}
check('B1 internal commutant of the rung-1 tick (steps .04, .3, pi/2): 20 = U(1)_nu U(1)_e U(3)_u U(3)_d for distinct masses; '
      '32 = U(4)^2 if nu=u, e=d; 40 = U(2) U(6) if nu=e, u=d; 64 if equal',
      all(v == [20, 32, 40, 64] for v in dims.values()), f'{list(dims.values())[0]}')
Kt = np.array([0.7, -0.4, 1.3]); cs = {}
for nm, ms in PATS.items():
    U = U1(Kt, 0.3, ms)
    cs[nm] = [max(nrm(U @ np.kron(np.eye(8), g) - np.kron(np.eye(8), g) @ U) for g in G) for G in (G4, G2)]
check('B2 su(4) commutes only if m_nu = m_u, m_e = m_d; su(2) only if m_nu = m_e, m_u = m_d; (4,2) is irreducible, so no mass '
      'pattern keeps exactly SU(4) x SU(2)', cs['nu=u,e=d'][0] < 1e-12 and cs['nu=e,u=d'][1] < 1e-12
      and min(cs['distinct']) > .1 and cs['nu=u,e=d'][1] > .1 and cs['nu=e,u=d'][0] > .1,
      '(su4,su2) ' + ', '.join(f'{k} {v[0]:.2f},{v[1]:.2f}' for k, v in cs.items() if k != 'equal'))

# ================================================================== C. spin
print('== C. spin: the twist and the rotation-blind symmetry')
NC = 4; CELLS = list(itertools.product(range(NC), repeat=3)); CI = {q: i for i, q in enumerate(CELLS)}
LAB = {tuple(s): i for i, s in enumerate(C)}
lab = lambda q: LAB[tuple(np.array(q) % 2)]
def coarse_tick(eps, mu):
    def half(A, off):
        M = np.zeros((NC ** 3, NC ** 3), complex)
        for b in itertools.product(range(0, NC, 2), repeat=3):
            qs = [tuple((np.array(b) + off + s) % NC) for s in C]; ids = [CI[q] for q in qs]; ls = [lab(q) for q in qs]
            for a_ in range(8):
                for e_ in range(8): M[ids[a_], ids[e_]] += A[ls[a_], ls[e_]]
        return M
    return half(expm(1j * (eps + mu / 2) * W), np.ones(3, int)) @ half(expm(-1j * (eps - mu / 2) * W), np.zeros(3, int))
def Gc(R, cc):
    S = Dj(1.5, *axang(R)); M = np.zeros((NC ** 3, NC ** 3), complex)
    for q in CELLS:
        q2 = tuple(np.rint(R @ (np.array(q) - cc) + cc).astype(int) % NC); M[CI[q2], CI[q]] = XI[lab(q2)].conj() @ S @ XI[lab(q)]
    return M
def Gfine(R, cen):
    S = Dj(1.5, *axang(R)); M = np.zeros((8 * NC ** 3,) * 2, complex)
    for x in itertools.product(range(2 * NC), repeat=3):
        x = np.array(x); y = np.rint(R @ (x - cen) + cen).astype(int) % (2 * NC)
        M[CI[tuple(y // 2)] * 8 + lab(y % 2), CI[tuple(x // 2)] * 8 + lab(x % 2)] = XI[lab(y // 2)].conj() @ S @ XI[lab(x // 2)]
    return M
RR, GCS, fac = [], [], 0
for R, P in zip(ROTS, PINT):
    for cen in (np.full(3, 1.5), np.full(3, 3.5)):
        g = Gc(R, (cen - .5) / 2); RR.append(P); GCS.append(g); fac = max(fac, abs(Gfine(R, cen) - np.kron(g, P)).max())
R4 = [i for i, R in enumerate(ROTS) if cname(R) == 'C4'][0]
q2 = {q: tuple(np.rint(ROTS[R4] @ (np.array(q) - .5) + .5).astype(int) % NC) for q in CELLS}
moved = lambda x: 2 * np.array(q2[tuple(x // 2)]) + x % 2
broken = sum(np.abs(((moved(np.array(x)) - moved((np.array(x) + e) % 8) + 4) % 8) - 4).sum() != 1
             for x in itertools.product(range(8), repeat=3) for e in np.eye(3, dtype=int))
check('C1 8^3 fine sites: all 48 rotations factorise, G = G_c x P_int (the cell index turns with space); G\' = G_c x 1 moves '
      'cells rigidly and is not a fine-lattice isometry', fac == 0 and broken > 0, f'residual {fac:.0e}; a C4 of G\' breaks {broken}/1536 bonds')
tw = 0
for R, P, o in zip(ROTS, PINT, ODD):
    Xm = expm(1j * np.pi * o * np.diag(np.diag(BASIS.T @ (T3 + 0.75 * BL + 0.25 * np.eye(8)) @ BASIS))) @ (BASIS.T @ P @ BASIS)
    Ou, Od = Xm[1:4, 1:4], Xm[5:, 5:]
    tw = max(tw, abs(Xm - np.diag([1, 0, 0, 0, 1, 0, 0, 0]) - np.kron(np.eye(2), np.pad(Ou, ((1, 0), (1, 0))))).max(),
             abs(Ou - Od).max(), abs(np.linalg.det(Ou) - 1), abs(Ou @ Ou.T - np.eye(3)).max(), abs(np.trace(Ou) - np.trace(R)))
check('C2 twist = colour x sign: P_int(R) = O(R)_colour exp(-i pi [R odd](T3 + 3(B-L)/4 + N/4)), O(R) in SO(3), the same on '
      'up and down, conjugate to R', tw < 1e-12, f'residual {tw:.0e}')
MS = PATS['distinct']; cG = cGp = 0
for eps in (0.04, 0.3):
    U = sum(np.kron(coarse_tick(eps, MS[k]), PR[k]) for k in ('A1', 'A2', 'T1', 'T2'))
    for g, P in zip(GCS, RR):
        G = np.kron(g, P); Gp = np.kron(g, np.eye(8)); cG = max(cG, abs(G @ U - U @ G).max()); cGp = max(cGp, abs(Gp @ U - U @ Gp).max())
g4 = np.kron(GCS[2 * R4], np.eye(8))
check('C3 distinct masses, steps .04 and .3: the tick commutes with G and with G\' (48 rotations), G\'(C4)^4 = -1: the cell '
      'index can be made rotation-blind',
      cG < 1e-12 and cGp < 1e-12 and np.allclose(np.linalg.matrix_power(g4, 4), -np.eye(512)), f'{cG:.0e}, {cGp:.0e}')
G6 = lambda a: -1j * np.sqrt(3) * (np.diag(C[:, a]) @ W - W @ np.diag(C[:, a]))       # Gamma_(a+3)
def alphas(eps): return [G6(a) @ expm(-1j * eps * W) for a in range(3)]
c4r = []; taus_ok = True; chi_tau = {}
for eps in (0.04, 0.3, np.pi / 2):
    al = alphas(eps); v = np.sin(eps) / np.sqrt(3); h = 1e-5
    num = max(abs(1j * (logm(Ublock(h * e, eps, 0)) - logm(Ublock(-h * e, eps, 0))) / (2 * h * v) - al[a]).max() for a, e in enumerate(np.eye(3)))
    cl = max(abs(al[a] @ al[b] + al[b] @ al[a] - 2 * (a == b) * np.eye(8)).max() for a in range(3) for b in range(3))
    bt = max(abs(W @ x + x @ W).max() for x in al)
    S = [-.25j * (al[(k + 1) % 3] @ al[(k + 2) % 3] - al[(k + 2) % 3] @ al[(k + 1) % 3]) for k in range(3)]
    for R, G in zip(ROTS, GC0):
        n_, th = axang(R); tau = expm(1j * th * sum(n_[k] * S[k] for k in range(3))) @ G
        taus_ok &= max(abs(tau @ x - x @ tau).max() for x in al + [W]) < 1e-10
        if eps == 0.3: chi_tau.setdefault(cname(R), set()).add(int(round(np.trace(tau).real / 4)))
    c4r.append(max(num, cl, bt, abs(sum(s @ s for s in S) - .75 * np.eye(8)).max()))
check('C4 the tick\'s long-wavelength algebra (steps .04, .3, pi/2): alpha_a = Gamma_(a+3) e^(-i eps W), beta = W are Dirac; '
      'each rotation = e^(-i theta n.S) x a copy matrix in the E irrep. Every cell state is a spin-1/2 Dirac fermion', max(c4r) < 1e-6 and taus_ok
      and chi_tau == {'E': {2}, 'C3': {-1}, 'C2f': {2}, 'C4': {0}, "C2'": {0}}, f'max residual {max(c4r):.0e}')
V = np.column_stack([(C[:, i] - .5) / np.sqrt(2) for i in range(3)])
LEV = np.array([[[np.linalg.det(np.eye(3)[[k, i, j]]) for j in range(3)] for i in range(3)] for k in range(3)])
J3 = [-1j * LEV[k] for k in range(3)]; J8 = [V @ j @ V.T for j in J3]
def Wlam(lam, sgn):
    M = np.zeros((64, 64), complex)
    for a in range(8):
        for b in range(8):
            if W[a, b] != 0: M[a * 8:a * 8 + 8, b * 8:b * 8 + 8] = W[a, b] * expm(1j * lam * sgn * sum((C[a] - C[b])[k] * J8[k] for k in range(3)))
    return M
MINT = sum(MS[k] * PR[k] for k in ('A1', 'A2', 'T1', 'T2'))
def Uso(K, eps, lam):
    D = np.kron(np.diag(np.exp(1j * (C @ K))), np.eye(8)); Mi = np.kron(np.eye(8), MINT)
    return D @ expm(1j * Wlam(lam, -1) @ (eps * np.eye(64) + Mi / 2)) @ D.conj().T @ expm(-1j * Wlam(lam, 1) @ (eps * np.eye(64) - Mi / 2))
rng = np.random.default_rng(3); eG = eGp = 0
for K in rng.normal(size=(2, 3)):
    for R, P, g in zip(ROTS, PINT, GC0):
        for G, isp in ((np.kron(g, P), 0), (np.kron(g, np.eye(8)), 1)):
            e_ = abs(G @ Uso(K, .3, .15) @ G.conj().T - Uso(R @ K, .3, .15)).max()
            eG, eGp = (max(eG, e_), eGp) if not isp else (eG, max(eGp, e_))
al = alphas(.3); S = [-.25j * (al[(k + 1) % 3] @ al[(k + 2) % 3] - al[(k + 2) % 3] @ al[(k + 1) % 3]) for k in range(3)]
Jt = [np.kron(S[k], np.eye(3)) + np.kron(np.eye(8), J3[k]) for k in range(3)]; J2 = sum(j @ j for j in Jt)
Pt = np.kron(np.eye(8), V); w_, vec = np.linalg.eig(Pt.conj().T @ Uso(np.zeros(3), .3, .15) @ Pt)
ang = np.angle(w_); srt = np.argsort(ang); cuts = [0] + [i + 1 for i in range(23) if ang[srt[i + 1]] - ang[srt[i]] > 1e-6] + [24]
nj = Counter(); dev = 0; nlev = len(cuts) - 1
for a_, b_ in zip(cuts[:-1], cuts[1:]):
    idx = srt[a_:b_]; Qv = np.linalg.qr(vec[:, idx])[0]; jj = float(np.real(np.trace(Qv.conj().T @ J2 @ Qv))) / len(idx)
    j_ = 0.5 if jj < 2.25 else 1.5; nj[j_] += len(idx); dev = max(dev, abs(jj - j_ * (j_ + 1)))
gap = min(abs(ang[srt[i + 1]] - ang[srt[i]]) for i in range(23) if ang[srt[i + 1]] - ang[srt[i]] > 1e-6)
check('C5 converse: a hop turning the cell index with its direction (e^(i lam d.J) on T1) commutes with G, not G\'; the 24 '
      'down-type K=0 states split into 8 with j = 1/2 and 16 with j = 3/2: colour degeneracy and spin 1/2 lost',
      eG < 1e-12 and eGp > 1e-3 and nj == Counter({0.5: 8, 1.5: 16}) and dev < .02 and nlev > 2,
      f"G {eG:.0e}, G' {eGp:.1e}; {nlev} levels, j(j+1) off by < {dev:.3f}")

# ================================================================== D. left / right
print('== D. even/odd cells and copies against chirality')
idres = max(nrm(Ublock(K, e, 0) - SUB @ Ublock(K, e, 0) @ SUB - 1j * np.sin(2 * e) * (np.diag(np.exp(1j * C @ K)) @ W @ np.diag(np.exp(-1j * C @ K)) - W))
            for e in (0.04, 0.3, 1.2) for K in rng.normal(size=(3, 3)))
cm = {(e, m): nrm(Ublock(Kt, e, m) @ SUB - SUB @ Ublock(Kt, e, m)) for e, m in ((0.04, 0), (0.3, 0), (np.pi / 2, 0), (np.pi / 2, .2))}
check('D1 zero mass: U - sUs = i sin(2 eps)(W_odd(K) - W) exactly (s = sublattice sign): separate even/odd cell unitaries '
      'commute with the tick only at step pi/2 and zero mass',
      idres < 1e-12 and cm[(np.pi / 2, 0)] < 1e-12 and min(cm[(0.04, 0)], cm[(0.3, 0)], cm[(np.pi / 2, .2)]) > 1e-2,
      '||[U,s]|| ' + ', '.join(f'{e:.2f}/{m}: {v:.3f}' for (e, m), v in cm.items()))
g50 = -1j * G6(0) @ G6(1) @ G6(2); g5p = -G6(0) @ G6(1) @ G6(2) @ W; d2 = 0; trs = 0; nn = []
for e in (0.04, 0.3, 0.8, np.pi / 2):
    al = alphas(e); g5 = -1j * al[0] @ al[1] @ al[2]
    d2 = max(d2, abs(g5 - np.cos(e) * g50 - np.sin(e) * g5p).max()); trs = max(trs, abs(np.trace((np.eye(8) + SUB) / 2 @ g5)))
    nn.append((nrm(SUB @ g5 + g5 @ SUB) - 2 * np.sin(e), nrm(SUB @ g5 - g5 @ SUB) - 2 * np.cos(e)))
check('D2 the tick\'s chirality g5(eps) = cos(eps) g5_0 + sin(eps) g5_pi/2, {s,g5_0} = 0 = [s,g5_pi/2]; ||{s,g5}|| = 2 sin eps, '
      '||[s,g5]|| = 2 cos eps, tr(P_even g5) = 0: even cells never carry net chirality', d2 < 1e-12 and trs < 1e-12 and np.abs(nn).max() < 1e-10
      and abs(SUB @ g50 + g50 @ SUB).max() < 1e-12 and abs(SUB @ g5p - g5p @ SUB).max() < 1e-12)
al = alphas(np.pi / 2); g5 = -1j * al[0] @ al[1] @ al[2]; s3 = SUB @ g5
cont = {(se, ch, cp): int(round(np.trace((np.eye(8) + se * SUB) @ (np.eye(8) + ch * g5) @ (np.eye(8) + cp * s3) / 8).real))
        for se in (1, -1) for ch in (1, -1) for cp in (1, -1)}
flip = all(np.allclose(G @ s3 @ G.conj().T, -s3 if o else s3) and np.allclose(G @ SUB @ G.conj().T, -SUB if o else SUB)
           for G, o in zip(GC0, ODD))
check('D3 step pi/2: s = g5 sigma3, sigma3 in the copy algebra; even cells = (L,+)+(R,-), odd = (R,+)+(L,-), 2 states each; odd '
      'rotations flip s and sigma3: copy + is a family (4,2,1)+(4b,1,2) of SU(4) x SU(2)_even x SU(2)_odd, copy - its mirror',
      max(abs(s3 @ x - x @ s3).max() for x in al + [W]) < 1e-12 and abs(s3 @ s3 - np.eye(8)).max() < 1e-12 and flip
      and {k: v for k, v in cont.items() if v} == {(1, 1, 1): 2, (1, -1, -1): 2, (-1, 1, -1): 2, (-1, -1, 1): 2})

comp = [LAB[tuple(1 - s_)] for s_ in C]; inv_ok = True; nsol = []
for e, m in ((0.04, 0), (0.3, .2), (np.pi / 2, .3)):
    Ks = rng.normal(size=(4, 3)); cols = []
    for i in range(8):
        E_ = np.zeros((8, 8)); E_[comp[i], i] = 1
        cols.append(np.concatenate([(E_ @ Ublock(K, e, m) - Ublock(-K, e, m) @ E_).ravel() for K in Ks]))
    sv, Vh = np.linalg.svd(np.array(cols).T)[1:]; nsol.append(int(np.sum(sv < 1e-9)))
    x = Vh[-1].conj(); Pv = np.zeros((8, 8), complex)
    for i in range(8): Pv[comp[i], i] = x[i] / abs(x[0])
    al = alphas(e); g5e = -1j * al[0] @ al[1] @ al[2]
    inv_ok &= (abs(Pv.conj().T @ Pv - np.eye(8)).max() < 1e-10 and abs(Pv @ g5e @ Pv.conj().T + g5e).max() < 1e-10
               and abs(Pv @ SUB @ Pv.conj().T + SUB).max() < 1e-10 and abs(Pv @ W @ Pv.conj().T - W).max() < 1e-10)
check('D4 a block-local inversion (corner complement with phases, unique) maps U(K) to U(-K) at every step and mass, flips g5 '
      'and s, keeps beta: the tick is parity-even, so no rule breaks parity', inv_ok and nsol == [1, 1, 1])

# ================================================================== E. anomalies, CL-5
print('== E. anomalies and the CL-5 link rule')
fam = [(4, 2, 1, 1), (-4, 1, 2, 1)]                     # left-handed (SU4 rep: 4 or 4bar=-4, SU2_L dim, SU2_R dim)
su4cubed = sum((1 if r > 0 else -1) * dl_ * dr for r, dl_, dr, _ in fam)
witL = sum(4 * dr for r, dl_, dr, _ in fam if dl_ == 2); witR = sum(4 * dl_ for r, dl_, dr, _ in fam if dr == 2)
lh = [('Q', 3, 2, Fr(1, 6), Fr(1, 3)), ('u', 3, 1, Fr(-2, 3), Fr(-1, 3)), ('d', 3, 1, Fr(1, 3), Fr(-1, 3)),
      ('L', 1, 2, Fr(-1, 2), Fr(-1)), ('e', 1, 1, Fr(1), Fr(1)), ('n', 1, 1, Fr(0), Fr(1))]   # (name, SU3, SU2, Y, B-L) left-handed
TT = {1: 0, 2: Fr(1, 2), 3: Fr(1, 2)}
an = []
for f in (lambda y, x: y, lambda y, x: x):
    an += [sum(n2 * TT[n3] * f(y, x) for nm, n3, n2, y, x in lh if n3 == 3), sum(n3 * TT[n2] * f(y, x) for nm, n3, n2, y, x in lh if n2 == 2),
           sum(n3 * n2 * f(y, x) ** 3 for nm, n3, n2, y, x in lh), sum(n3 * n2 * f(y, x) for nm, n3, n2, y, x in lh)]
an += [sum(n3 * n2 * y * y * x for nm, n3, n2, y, x in lh), sum(n3 * n2 * y * x * x for nm, n3, n2, y, x in lh)]
check('E1 the Pati-Salam family is anomaly-free: SU(4)^3 = 0, 4 doublets per SU(2), all 10 anomalies of Y = T3R + (B-L)/2 and '
      'B-L vanish; the lattice content is vector-like, so its anomalies vanish identically and select nothing',
      su4cubed == 0 and witL % 2 == 0 and witR % 2 == 0 and all(a == 0 for a in an), f'doublets {witL}, {witR}')
lam8 = []
for i in range(3):
    for j in range(i + 1, 3):
        E = np.zeros((3, 3), complex); E[i, j] = E[j, i] = 1; lam8.append(E); E = np.zeros((3, 3), complex); E[i, j] = -1j; E[j, i] = 1j; lam8.append(E)
lam8 += [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
I3 = np.eye(3); k3 = lambda a, b, d: np.kron(np.kron(a, b), d)
def singlets(gens):
    M = np.vstack(gens); return int(np.sum(np.linalg.svd(M, compute_uv=False) < 1e-9))
s_diag = singlets([k3(t, I3, I3) + k3(I3, t, I3) + k3(I3, I3, t) for t in lam8])
s_sep = singlets([k3(t, I3, I3) + k3(I3, t, I3) for t in lam8] + [k3(I3, I3, t) for t in lam8])
check('E2 CL-5 with distinct masses allows at most the 20-dim group of B1 < 21 = dim su(4)+2 su(2): no Pati-Salam links; uud '
      'colour singlets: 0 under separate up/down SU(3), 1 under a shared one (the proton), allowed but not forced',
      dims[0.3][0] == 20 and 15 + 3 + 3 == 21 and s_sep == 0 and s_diag == 1, f'singlets {s_sep}, {s_diag}')

# ================================================================== F. generations
print('== F. generations: what rotations allow inside 2^n cells')
def cell_mult(n):
    L_ = 2 ** n; pts = 2 * np.array(list(itertools.product(range(L_), repeat=3))) - (L_ - 1)      # doubled, integer
    Ri = [np.rint(R).astype(int) for R in ROTS]
    return decompose([int(np.sum(np.all(pts @ R.T == pts, axis=1))) for R in Ri])
formula = lambda n: dict(A1=(8 ** n + 8 * 2 ** n) // 24, A2=(8 ** n + 8 * 2 ** n) // 24, E=(2 * 8 ** n - 8 * 2 ** n) // 24, T1=8 ** (n - 1), T2=8 ** (n - 1))
direct = [cell_mult(n) for n in (1, 2, 3)]
check('F1 2^n cells: (A1,A2,E,T1,T2) multiplicities ((8^n+8 2^n)/24 x2, (2 8^n-8 2^n)/24, 8^(n-1) x2), direct for n = 1..3; '
      'triplets come 8^(n-1) times, never a multiple of 3: no rung has three rotation-blind families', direct == [formula(n) for n in (1, 2, 3)] and all(8 ** (n - 1) % 3 for n in range(1, 13)),
      f'{[tuple(d.values()) for d in direct]}')
pts = 2 * np.array(list(itertools.product(range(4), repeat=3))) - 3; PI64 = {tuple(p): i for i, p in enumerate(pts)}
P64 = []
for R in ROTS:
    P = np.zeros((64, 64)); Ri = np.rint(R).astype(int)
    for i, p in enumerate(pts): P[PI64[tuple(Ri @ p)], i] = 1
    P64.append(P)
Xr = rng.normal(size=(64, 64)); Xr = Xr + Xr.T; Hc = sum(P @ Xr @ P.T for P in P64) / 24
ev = np.round(np.linalg.eigvalsh(Hc), 8); mult = Counter(Counter(ev).values())
check('F2 a random covariant one-body term on the 4^3 cell has 16 threefold, 4 twofold, 8 single levels: every triplet stays '
      'degenerate, so a rotation triplet can be colour, not a family', mult == Counter({3: 16, 2: 4, 1: 8}))

print('== measured (comparisons only): quark spin 1/2 (Callan-Gross); exact colour; proton = uud; m_mu/m_e = 206.77; '
      'N_nu = 2.984 +- 0.008; W_R > ~5 TeV vs W_L 80.4 GeV')
print('supplied: the rung-1 rule (cell modes carried in parallel), step and four masses, labels (lepton = A1 of C^4, T3 sign, '
      'B-L scale), the C5 hop (counterexample only); cited: none')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
