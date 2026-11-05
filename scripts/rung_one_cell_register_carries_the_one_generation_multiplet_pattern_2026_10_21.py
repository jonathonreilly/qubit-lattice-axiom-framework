#!/usr/bin/env python3
"""Site content for one generation: a coarse cell of one-mode sites versus a 5-mode Spin(10) register.
Supplied models, finite exact diagnostics; no physical identification.

Z. Zoom (Qubit axiom unchanged): the CL-3 tick run at rung 1, with each 2^3 cell of one-mode sites as a super-site
   whose 8 modes are carried in parallel (W x 1_8). Rotation content of cells, covariance, band, exact internal
   symmetry, covariant masses, the cell factorisation C^2 (x) C^4 and its forced traceless generators.
C. Charges for the vector-like and the chiral (even cells L, odd cells R) assignments.
R. 5 modes per site (Qubit axiom changed): W x 1_5, which internal symmetry survives, Spin(10) on Lambda(C^5),
   content and exchange statistics of the register states.
S. Symmetric-mass-generation algebra for one Weyl 16 at a site.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/RUNG_ONE_CELL_REGISTER_CARRIES_THE_ONE_GENERATION_MULTIPLET_PATTERN_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------------------------------------------------------- common geometry
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
ODD = [TAB['A2'][cname(R)] == -1 for R in ROTS]          # C4 and C2': they exchange the two corner tetrahedra
def decompose(chis):
    return {k: int(round(sum(t[cname(R)] * ch for R, ch in zip(ROTS, chis)).real / 24)) for k, t in TAB.items()}
def perm_char(P):
    P = np.array(P, float)
    return [sum(np.allclose((R @ P[i]), P[i]) for i in range(len(P))) for R in ROTS]
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
def coherent(j):
    J = Jm(j); out = []
    for i in range(8):
        n = (2 * C[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J[k] for k in range(3))); out.append(v[:, -1])
    return out
def img(R, i): return int(np.argmin(np.sum(abs(c - R @ c[i]), 1)))
def corner_rep(j, R):
    xi = coherent(j); D = Dj(j, *axang(R)); L = np.zeros((8, 8), complex)
    for i in range(8):
        k = img(R, i); L[k, i] = xi[k].conj() @ D @ xi[i]
    return L
XI = coherent(1.5)
GM = np.array([[XI[a].conj() @ XI[b] for b in range(8)] for a in range(8)])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: W[a, b] = -GM[a, b] / abs(GM[a, b]) / np.sqrt(3)
PCELL = [np.real(corner_rep(0, R)) for R in ROTS]                 # plain corner permutations
PR = {k: sum(TAB[k][cname(R)] * P for R, P in zip(ROTS, PCELL)) * TAB[k]['E'] / 24 for k in ('A1', 'A2', 'T1', 'T2')}

def comm_dim(reps):
    d = reps[0].shape[0]; Mm = np.zeros((d * d, d * d), complex)
    for g in reps:
        A = np.kron(g, np.eye(d)) - np.kron(np.eye(d), g.T); Mm += A.conj().T @ A
    return int(np.sum(np.linalg.eigvalsh(Mm) < 1e-9))

def gauge_phases(U):
    """site phases lam with U_yx = e^{i lam_y} conj(U_yx) e^{-i lam_x} (BFS over every component); residual."""
    U = np.asarray(U); nzr, nzc = np.nonzero(np.abs(U) > 1e-12); lam = np.full(U.shape[0], np.nan); adj = {}
    for r_, c_ in zip(nzr, nzc): adj.setdefault(c_, []).append(r_); adj.setdefault(r_, []).append(c_)
    for root in range(U.shape[0]):
        if not np.isnan(lam[root]): continue
        lam[root] = 0.0; stack = [root]
        while stack:
            x = stack.pop()
            for y in adj.get(x, []):
                if np.isnan(lam[y]):
                    lam[y] = lam[x] + 2 * np.angle(U[y, x]) if abs(U[y, x]) > 1e-12 else lam[x] - 2 * np.angle(U[x, y])
                    stack.append(y)
    resd = np.abs(np.angle(np.exp(1j * (lam[nzr] - lam[nzc] - 2 * np.angle(U[nzr, nzc])))))
    return lam, (resd.max() if len(resd) else 0.0)
def pairing_dim(U, lam, nint, cell_of, off_of):
    """dim of {K antisymmetric nint x nint : U Phi_K U^T = Phi_K}, Phi_K[x,y] = e^{i lam_x} K[off x, off y] (same cell);
    tested on a generic random projection (keeps the rank)."""
    U = sp.csr_matrix(U); n_ = U.shape[0]; V = np.random.default_rng(13).normal(size=(n_, 24)); UtV = U.T @ V
    groups = {}
    for i in range(n_): groups.setdefault(cell_of[i], []).append(i)
    cols = []
    for a_ in range(nint):
        for b_ in range(a_ + 1, nint):
            K = np.zeros((nint, nint)); K[a_, b_], K[b_, a_] = 1, -1; rr, cc_, vv = [], [], []
            for mem in groups.values():
                for x in mem:
                    for y in mem:
                        if K[off_of[x], off_of[y]] != 0: rr.append(x); cc_.append(y); vv.append(np.exp(1j * lam[x]) * K[off_of[x], off_of[y]])
            Phi = sp.csr_matrix((vv, (rr, cc_)), shape=(n_, n_)); cols.append(U @ (Phi @ UtV) - Phi @ V)
    P = np.array([c_.ravel() for c_ in cols]).T; ew = np.linalg.eigvalsh(P.conj().T @ P)
    return int(np.sum(ew < 1e-10 * max(1.0, ew.max())))
# ================================================================ Z. zoom
print('== Z. rung 1: a 2^3 cell of one-mode sites as the internal register of a super-site')
cells = {'octahedron (6, site-centred)': [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 1],
         '2^3 (8)': list(c), '4^3 (64)': [np.array(x) - 1.5 for x in itertools.product(range(4), repeat=3)]}
dec = {k: decompose(perm_char(v)) for k, v in cells.items()}
j1 = decompose([np.trace(corner_rep(1, R)) for R in ROTS])
fmt = lambda d: '+'.join(f'{v}{k}' if v > 1 else k for k, v in d.items() if v)
print('   plain content: ' + '; '.join(f'{k}: {fmt(v)}' for k, v in dec.items()) + f'; 2^3 with j=1 phases: {fmt(j1)}')
mult_tw = int(round(np.mean([abs(np.trace(corner_rep(1.5, R))) ** 2 for R in ROTS])))
check('Z1 the plain 2^3 cell = A1+A2+T1+T2, so T+(A1+A2) is a rotation-invariant C^3+C^2 (a 5-mode register) '
      'inside one cell; the spin-3/2-twisted cell (mean|chi|^2 = 4 forces 2 x G3/2) has invariant subspaces of dim 0, 4, 8 only',
      dec['2^3 (8)'] == dict(A1=1, A2=1, E=0, T1=1, T2=1) and mult_tw == 4 and j1 == dict(A1=0, A2=0, E=1, T1=1, T2=1),
      'octahedron gives T1+E (3+2) but is not a Margolus cell; 4^3 multiplicities ' +
      str([dec['4^3 (64)'][k] for k in ('A1', 'A2', 'E', 'T1', 'T2')]))
two_pi_coarse = Dj(1.5, np.array([0, 0, 1.0]), 2 * np.pi); two_pi_int = np.eye(8)
check('Z2 spin-statistics fixes the internal action: with the spin-3/2 coarse twist, a 2pi turn is -1 only if the '
      'cell index carries a non-spinorial action (plain j=0: A1+A2+T1+T2, or j=1: E+T1+T2)',
      np.allclose(two_pi_coarse, -np.eye(4)) and np.allclose(np.kron(two_pi_coarse, two_pi_int), -np.eye(32)))
# ---- the rung-1 lattice tick on an 8^3 fine torus (4^3 cells)
N = 8; NC = 4
SITES = np.array(list(itertools.product(range(N), repeat=3))); IDX = {tuple(s): i for i, s in enumerate(SITES)}
OFF = np.array([int((x % 2) @ [4, 2, 1]) for x in SITES]); CELL = SITES // 2
CPAR = CELL.sum(1) % 2
def coins(M, b):
    w, V = np.linalg.eigh(M); out = []
    for sgn in (+1, -1):
        A = w / 2 + sgn * b
        out.append(np.kron(W, V @ np.diag(np.cos(A)) @ V.conj().T) + 1j * np.kron(np.eye(8), V @ np.diag(np.sin(A)) @ V.conj().T))
    return out                                             # index (coarse corner label, cell offset)
def half(Wc, off):
    rr, cc_, vv = [], [], []
    for b in itertools.product(range(0, NC, 2), repeat=3):
        cl = [(np.array(b) + off + s) % NC for s in C]
        ids = np.array([[IDX[tuple(2 * q + C[r])] for r in range(8)] for q in cl]); labs = [int((q % 2) @ [4, 2, 1]) for q in cl]
        for ia in range(8):
            for ie in range(8):
                blk = Wc[labs[ia] * 8:(labs[ia] + 1) * 8, labs[ie] * 8:(labs[ie] + 1) * 8]
                nz = np.nonzero(blk)
                rr += list(ids[ia][nz[0]]); cc_ += list(ids[ie][nz[1]]); vv += list(blk[nz])
    return sp.csr_matrix((vv, (rr, cc_)), shape=(N ** 3, N ** 3))
def tick(M, b):
    We, Wo = coins(M, b); return (half(Wo, np.ones(3, int)) @ half(We, np.zeros(3, int))).tocsr()
lab_c = lambda x: int(((np.asarray(x) // 2) % 2) @ [4, 2, 1])
def glob(R, cen):
    S = Dj(1.5, *axang(R)); rr, vv = [], []
    for x in SITES:
        y = np.rint(R @ (x - cen) + cen).astype(int) % N
        rr.append(IDX[tuple(y)]); vv.append(XI[lab_c(y)].conj() @ S @ XI[lab_c(x)])
    return sp.csr_matrix((vv, (rr, np.arange(N ** 3))), shape=(N ** 3, N ** 3))
GS = [glob(R, cn) for R in ROTS for cn in (np.full(3, 1.5), np.full(3, 3.5))]
LOOK = {(tuple(CELL[i]), OFF[i]): i for i in range(N ** 3)}
def lift(X, par=None):
    """internal operator X on the offsets of every cell (or only cells of parity par)."""
    rr, cc_, vv = [], [], []
    for i in range(N ** 3):
        if par is not None and CPAR[i] != par: continue
        for a in range(8):
            if X[a, OFF[i]] != 0: rr.append(LOOK[(tuple(CELL[i]), a)]); cc_.append(i); vv.append(X[a, OFF[i]])
    return sp.csr_matrix((vv, (rr, cc_)), shape=(N ** 3, N ** 3))
PROJ = np.random.default_rng(11).normal(size=(N ** 3, 24)) + 1j * np.random.default_rng(12).normal(size=(N ** 3, 24))
def null_count(cols):
    P = np.array([c_.ravel() for c_ in cols]).T; ew = np.linalg.eigvalsh(P.conj().T @ P); tol = 1e-10 * max(1.0, ew.max())
    return int(np.sum(ew < tol)), (ew[ew >= tol].min() if np.any(ew >= tol) else 0.0)
def commutant_dim(U):
    """dim of {X : [U, 1 (x) X] = 0}, from the randomly projected commutators [U, L_X] V (generic V keeps the rank)."""
    UV = U @ PROJ; cols = []
    for a in range(8):
        for e in range(8):
            E = np.zeros((8, 8)); E[a, e] = 1; L = lift(E); cols.append(U @ (L @ PROJ) - L @ UV)
    return null_count(cols)
MCOV = 0.1 * PR['A1'] + 0.25 * PR['A2'] + 0.4 * PR['T1'] + 0.7 * PR['T2']
res = {}
for name, M, b in (('massless', np.zeros((8, 8)), 0.0), ('equal mass 0.3, b 0.2', 0.3 * np.eye(8), 0.2),
                   ('covariant masses, b 0.2', MCOV, 0.2)):
    U = tick(M, b); Ud = U.toarray()
    uni = np.abs(Ud.conj().T @ Ud - np.eye(N ** 3)).max()
    cov = max(abs((G @ U - U @ G)).max() for G in GS)
    w_ = np.abs(-np.angle(np.linalg.eigvals(Ud))); res[name] = (U, w_, uni, cov, commutant_dim(U))
U0, w0, u0, c0, cd0 = res['massless']
Kset = [np.pi * np.array(k) for k in C]
pred = np.sort(np.concatenate([np.full(64, np.arccos(np.clip(np.mean(np.cos(K)), -1, 1))) for K in Kset]))
check('Z3 rung-1 tick (W x 1_8 on 8^3 sites, three mass settings): unitary, commutes with all 24 rotations about both '
      'coarse block centres, and the massless band is cos w = (cos Kx + cos Ky + cos Kz)/3 with each level 8x the CL-3 one',
      max(r[2] for r in res.values()) < 1e-12 and max(r[3] for r in res.values()) < 1e-12 and np.allclose(np.sort(w0), pred, atol=1e-9),
      f"unitarity {max(r[2] for r in res.values()):.0e}, covariance {max(r[3] for r in res.values()):.0e}")
U3, w3, _, _, (cd3, gap3) = res['covariant masses, b 0.2']
kz = np.round(np.sort(w3)[:64], 6); mlt = Counter(kz)
check('Z4 exact internal symmetry: operators 1 (x) X commute with the tick for all X (commutant dim 64 = U(8)); '
      'rotation-covariant masses m(A1),m(A2),m(T1),m(T2) leave dim 20 = U(1)xU(1)xU(3)xU(3), lowest levels 1:1:3:3',
      res['massless'][4][0] == 64 and res['equal mass 0.3, b 0.2'][4][0] == 64 and cd3 == 20
      and [mlt[round(m, 6)] for m in (0.1, 0.25, 0.4, 0.7)] == [8, 8, 24, 24],
      f"K=0 level multiplicities {[mlt[round(m, 6)] for m in (0.1, 0.25, 0.4, 0.7)]}, commutant gap {gap3:.2f}")
# factorisation corner = (tetrahedron parity, body diagonal)
DIAG = {}; dl = []
for i in range(8):
    key = tuple(sorted([i, 7 - i]))
    if key not in dl: dl.append(key)
    DIAG[i] = dl.index(key)
PAR8 = np.array([int(s.sum()) % 2 for s in C])
order = [int(np.where((PAR8 == e) & (np.array([DIAG[i] for i in range(8)]) == d))[0][0]) for e in (0, 1) for d in range(4)]
BF = np.eye(8)[:, order]; X2 = np.array([[0., 1.], [1., 0.]])
fac = True
for R, P, odd in zip(ROTS, PCELL, ODD):
    Pd = np.zeros((4, 4))
    for d in range(4): Pd[DIAG[img(R, dl[d][0])], d] = 1
    fac &= np.allclose(BF.T @ P @ BF, np.kron(X2 if odd else np.eye(2), Pd))
kin = {}
for k in C:
    v = np.array([(-1) ** int(k @ r) for r in C]); kin[''.join(map(str, k))] = [nm for nm, p in PR.items() if np.allclose(p @ v, v)][0]
check('Z5 the cell factorises canonically as C^2 (tetrahedron parity) x C^4 (body diagonal): R acts as X^[R odd] x P_diag(R). '
      'In internal momentum k in {0,pi}^3: A1 = 0, A2 = pi(1,1,1), T1 = axes, T2 = face diagonals', fac,
      ', '.join(f'{k}:{v}' for k, v in kin.items()))
PD = []
for R in ROTS:
    Pd = np.zeros((4, 4))
    for d in range(4): Pd[DIAG[img(R, dl[d][0])], d] = 1
    PD.append(Pd)
ENDR = [X2 if o else np.eye(2) for o in ODD]
J4 = np.ones((4, 4)) / 4
T3 = np.kron(X2 / 2, np.eye(4)); BL = np.kron(np.eye(2), (np.eye(4) - 4 * J4) / 3)
cov_gen = all(np.allclose(P @ (BF @ G @ BF.T), (BF @ G @ BF.T) @ P) for P in PCELL for G in (T3, BL))
check('Z6 the traceless rotation-invariant generators acting on one factor are unique up to scale: T3 = X/2 on C^2 '
      '(+-1/2) and B-L = (1 - 4P_A1)/3 on C^4 (1/3 x3, -1)', cov_gen and comm_dim(ENDR) == 2 and comm_dim(PD) == 2
      and np.allclose(np.linalg.eigvalsh(BL), sorted([-1.0] * 2 + [1 / 3] * 6)))
rng = np.random.default_rng(5)
def rand_u(k):
    h = rng.normal(size=(k, k)) + 1j * rng.normal(size=(k, k)); return expm(1j * (h + h.conj().T))
ge, go = rand_u(8), rand_u(8); Gx = lift(ge, 0) + lift(go, 1)
U03 = res['equal mass 0.3, b 0.2'][0]
Ub = tick(np.zeros((8, 8)), 0.2)
cx0 = abs(U0 @ Gx - Gx @ U0).max(); cx3 = abs(U03 @ Gx - Gx @ U03).max(); cxb = abs(Ub @ Gx - Gx @ Ub).max()
par_swap = all((int(sum(np.rint(R @ (q - 0.5) + 0.5))) % 2 != int(sum(q)) % 2) == o for R, o in zip(ROTS, ODD) for q in C)
check('Z7 massless: independent internal unitaries on even and odd cells commute with the tick (exact U(8)_e x U(8)_o); '
      'mu and b each break it to the diagonal U(8); the 12 odd rotations exchange even and odd cells',
      cx0 < 1e-12 and cx3 > 1e-2 and cxb > 1e-2 and par_swap, f'massless {cx0:.0e}, mu 0.3: {cx3:.2f}, b 0.2: {cxb:.2f}')

coset0 = np.where(OFF == 0)[0]
lam_c, res_c = gauge_phases(U03.toarray()[np.ix_(coset0, coset0)])
lam_cell = {tuple(CELL[coset0[i]]): lam_c[i] for i in range(len(coset0))}
LAMF = np.array([lam_cell[tuple(CELL[i])] for i in range(N ** 3)]); CELLID = [tuple(q) for q in CELL]
MREG = 0.4 * (PR['A1'] + PR['A2'] + PR['T1']) + 0.7 * PR['T2']
pd = [pairing_dim(tick(M, 0.2), LAMF, 8, CELLID, OFF) for M in (0.3 * np.eye(8), MCOV, MREG)]
check('Z8 the rung-1 tick is real in a cell-phase gauge, so staggered pairings sum_c lam_c a_cr a_cr\' are conserved too: '
      'internal symmetry SO(16) (equal masses; 28 pairings), SO(2)^2 x SO(6)^2 (covariant masses; 6), and with equal '
      'masses on T1+A1+A2 an exact SO(10) on that 5-mode register times SO(6) (13)', res_c < 1e-9 and pd == [28, 6, 13],
      f'pairings {pd}')

# ================================================================ C. charges
print('== C. charges from the forced generators (exact fractions)')
states = {'nu': (Fr(1, 2), Fr(-1)), 'e': (Fr(-1, 2), Fr(-1)), 'u': (Fr(1, 2), Fr(1, 3)), 'd': (Fr(-1, 2), Fr(1, 3))}
def charges(a, bb, cc_):
    return {k: a * t3 + bb * bl / 2 + cc_ for k, (t3, bl) in states.items()}
ok = True
for a, bb, cc_ in [(Fr(1), Fr(1), Fr(0)), (Fr(1), Fr(3, 7), Fr(0)), (Fr(2), Fr(-1), Fr(1, 5)), (Fr(1), Fr(1), Fr(1, 3))]:
    q = charges(a, bb, cc_); qp = 2 * q['u'] + q['d']; qn = q['u'] + 2 * q['d']
    ok &= (q['e'] + qp == 4 * cc_) and (qn + q['nu'] == 4 * cc_)
q = charges(Fr(1), Fr(1), Fr(0))
check('C1 vector-like Q = a T3 + b (B-L)/2 + c F: q_e + q_p = 4c and q_n + q_nu = 4c identically; c = 0 (no fermion-number '
      'admixture) and b = a give (u, d, e, nu) = (2/3, -1/3, -1, 0)', ok and [q[k] for k in ('u', 'd', 'e', 'nu')] == [Fr(2, 3), Fr(-1, 3), Fr(-1), Fr(0)],
      'measured |q_e + q_p|, |q_n| < ~1e-21 e')
# chiral assignment: even cells carry L (SU(2)_L on the end index), odd cells carry R
YL = {'Q': (Fr(1, 3)) / 2, 'L': Fr(-1) / 2}
YR = {k: t3 + bl / 2 for k, (t3, bl) in states.items()}
weyl = []                                                    # left-handed Weyl list: (SU3 dim, SU2 dim, Y, count)
weyl += [(3, 2, YL['Q']), (1, 2, YL['L'])]
weyl += [(3, 1, -YR['u']), (3, 1, -YR['d']), (1, 1, -YR['e']), (1, 1, -YR['nu'])]
TT = {1: Fr(0), 2: Fr(1, 2), 3: Fr(1, 2)}
an = dict(SU3sqY=sum(d2 * TT[d3] * y for d3, d2, y in weyl if d3 == 3), SU2sqY=sum(d3 * TT[d2] * y for d3, d2, y in weyl if d2 == 2),
          Y3=sum(d3 * d2 * y ** 3 for d3, d2, y in weyl), grav=sum(d3 * d2 * y for d3, d2, y in weyl))
Ys = [YL['Q'], -YR['u'], -YR['d'], YL['L'], -YR['e']]
qL = {'u': Fr(1, 2) + YL['Q'], 'd': Fr(-1, 2) + YL['Q'], 'nu': Fr(1, 2) + YL['L'], 'e': Fr(-1, 2) + YL['L']}
same = all(qL[k] == YR[k] for k in qL)
check('C2 chiral assignment (L on even cells with SU(2)_L on C^2, R on odd cells): Y = (B-L)/2 on L and T3 + (B-L)/2 on R '
      'gives the left-handed 16 with Y ratios 1:-4:2:-3:6, every anomaly zero, and Q = T3_L + Y equal on L and R',
      all(v == 0 for v in an.values()) and [y / Ys[0] for y in Ys] == [1, -4, 2, -3, 6] and same and -YR['nu'] == 0,
      f"q(u,d,e,nu,p,n) = {[str(x) for x in (qL['u'], qL['d'], qL['e'], qL['nu'], 2 * qL['u'] + qL['d'], qL['u'] + 2 * qL['d'])]}")

# ================================================================ R. 5 modes per site
print('== R. five modes per site (Qubit axiom changed)')
def apply_c(k, s, dag):
    occ = (s >> k) & 1
    if dag == bool(occ): return None, 0
    return s ^ (1 << k), (-1) ** bin(s & ((1 << k) - 1)).count('1')
def opmat(word, bfrom, bto=None):
    bto = bfrom if bto is None else bto
    ix = {s: i for i, s in enumerate(bto)}; M = np.zeros((len(bto), len(bfrom)), complex)
    for j, s in enumerate(bfrom):
        t, sg = s, 1
        for k, dag in reversed(word):
            t, g_ = apply_c(k, t, dag)
            if t is None: break
            sg *= g_
        if t is not None and t in ix: M[ix[t], j] += sg
    return M
FULL = list(range(32)); EV = [s for s in FULL if bin(s).count('1') % 2 == 0]; OD = [s for s in FULL if bin(s).count('1') % 2]
GAM = []
for i in range(5):
    cd_, c_ = opmat([(i, True)], FULL), opmat([(i, False)], FULL); GAM += [c_ + cd_, -1j * (c_ - cd_)]
SIG = [0.25j * (GAM[p] @ GAM[q] - GAM[q] @ GAM[p]) for p in range(10) for q in range(p + 1, 10)]
T16 = [g[np.ix_(EV, EV)] for g in SIG]; T16b = [g[np.ix_(OD, OD)] for g in SIG]
def hom_dim(Ta, Tb):                                          # dim Hom(a -> b) intertwiners
    da, db = Ta[0].shape[0], Tb[0].shape[0]; Mm = np.zeros((da * db, da * db), complex)
    for ta, tb in zip(Ta, Tb):
        A = np.kron(tb, np.eye(da)) - np.kron(np.eye(db), ta.T); Mm += A.conj().T @ A
    return int(np.sum(np.linalg.eigvalsh(Mm) < 1e-9))
leak = max(np.abs(g[np.ix_(EV, OD)]).max() for g in SIG)
check('R1 Spin(10) on one register Lambda(C^5): 16 (even) and 16bar (odd) irreducible and inequivalent, so its commutant is '
      'span{1, (-1)^N}: an invariant site term can only shift 16 against 16bar, and no register state is a singlet',
      leak == 0 and comm_dim(T16) == 1 and comm_dim(T16b) == 1 and hom_dim(T16, T16b) == 0)
occ = lambda s: [(s >> k) & 1 for k in range(5)]
Yof = lambda s: Fr(sum(occ(s)[3:]), 2) - Fr(sum(occ(s)[:3]), 3)
cont_e = sorted(Counter((sum(occ(s)), Yof(s)) for s in EV).items()); cont_o = sorted(Counter((sum(occ(s)), -Yof(s)) for s in OD).items())
gen = sorted([(Fr(1, 6), 6), (Fr(-2, 3), 3), (Fr(1, 3), 3), (Fr(-1, 2), 2), (Fr(1), 1), (Fr(0), 1)])
check('R2 Y = N2/2 - N3/3: the even sector is one generation; so is the odd sector conjugated, in which only L and d^c '
      'are single modes (Q, u^c, e^c three-mode, nu^c five-mode)',
      sorted((y, n_) for (k, y), n_ in cont_e) == gen and sorted((y, n_) for (k, y), n_ in cont_o) == gen
      and sorted(set((k, y) for (k, y), _ in cont_o)) == [(1, Fr(-1, 2)), (1, Fr(1, 3)), (3, Fr(-2, 3)), (3, Fr(1, 6)), (3, Fr(1)), (5, Fr(0))])
# exchange statistics of register states at two sites (10 modes, bit-level)
def create_word(S, site): return [(5 * site + k, True) for k in S]
def apply_word(word, s):
    sg = 1
    for k, dag in reversed(word):
        s, g_ = apply_c(k, s, dag)
        if s is None: return None, 0
        sg *= g_
    return s, sg
sgns = set(); okx = True
for S in [(), (0,), (0, 3), (0, 1, 2), (1, 3, 4), (0, 1, 3, 4)]:
    for S2 in [(1,), (2, 4), (0, 1, 2), (0, 1, 2, 3)]:
        sa, ga = apply_word(create_word(S, 0) + create_word(S2, 1), 0); sb, gb = apply_word(create_word(S2, 1) + create_word(S, 0), 0)
        okx &= (sa == sb) and (ga * gb == (-1) ** (len(S) * len(S2)))
yneutral = [s_ for s_ in FULL if Yof(s_) == 0]
check('R3 exchange: register operators at two sites commute up to (-1)^(|S||S\'|). The only Y-neutral register states are '
      'empty and full: over the empty one the 16 are bosons; over the full one they are fermions but only the 5bar (L, d^c) '
      'is a single mode (Q, u^c, e^c are three-hole states). Either way no whole generation is elementary', okx and sorted(bin(x).count('1') for x in yneutral) == [0, 5],
      'measured: quarks and leptons are elementary fermions at all tested scales')
# W x 1_5 on a 4^3 fine torus: band, U(5), and whether the pairing (Spin(10)) generators survive
Nf = 4; SF = np.array(list(itertools.product(range(Nf), repeat=3))); IF = {tuple(s): i for i, s in enumerate(SF)}
def fine_half(Wc, off):
    M = np.zeros((Nf ** 3, Nf ** 3), complex)
    for b in itertools.product(range(0, Nf, 2), repeat=3):
        xs = [(np.array(b) + off + s) % Nf for s in C]; ids = [IF[tuple(x)] for x in xs]; rs = [int((x % 2) @ [4, 2, 1]) for x in xs]
        for a_ in range(8):
            for e_ in range(8): M[ids[a_], ids[e_]] = Wc[rs[a_], rs[e_]]
    return M
def fine_tick(mu, b):
    We = np.cos(mu / 2 + b) * W + 1j * np.sin(mu / 2 + b) * np.eye(8); Wo = np.cos(mu / 2 - b) * W + 1j * np.sin(mu / 2 - b) * np.eye(8)
    return fine_half(Wo, np.ones(3, int)) @ fine_half(We, np.zeros(3, int))
U1 = fine_tick(0.3, 0.2); U5 = np.kron(U1, np.eye(5))
hX = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)); comm5 = np.abs(U5 @ np.kron(np.eye(Nf ** 3), hX) - np.kron(np.eye(Nf ** 3), hX) @ U5).max()
lamf, resf = gauge_phases(U1)
pd5 = pairing_dim(np.kron(U1, np.eye(5)), np.repeat(lamf, 5), 5, list(np.repeat(np.arange(Nf ** 3), 5)), list(np.tile(np.arange(5), Nf ** 3)))
check('R4 W x 1_5 (mu 0.3, b 0.2): unitarity, covariance and the band (x5) hold by the Kronecker structure; U(5) is exact, '
      'and because the CL-3 tick is real in a site gauge for every mu, b (plaquettes -1, nearest-neighbour terms imaginary), '
      'the staggered pairings are conserved too: the full Spin(10) of the register is exact', comm5 < 1e-12 and resf < 1e-9 and pd5 == 10,
      f'real-gauge residual {resf:.0e}, conserved pairings {pd5}/10')

# ================================================================ S. SMG algebra
print('== S. one Weyl 16 at a site: what a Spin(10)-invariant mirror-gapping term needs')
def inv_forms(Ta, Tb):
    da, db = Ta[0].shape[0], Tb[0].shape[0]; Mm = np.zeros((da * db, da * db), complex)
    for ta, tb in zip(Ta, Tb):
        A = np.kron(ta.T, np.eye(db)) + np.kron(np.eye(da), tb.T); Mm += A.conj().T @ A
    return int(np.sum(np.linalg.eigvalsh(Mm) < 1e-9))
WT = np.array([[((s >> k) & 1) - 0.5 for k in range(5)] for s in EV])
SIMPLE16 = [opmat([(k, True), (k + 1, False)], EV).real for k in range(4)] + [opmat([(3, True), (4, True)], EV).real]
def singlets(N_, nmodes, weights, simple):
    subs = list(itertools.combinations(range(nmodes), N_)); ix = {S: i for i, S in enumerate(subs)}
    zw = [S for S in subs if np.allclose(weights[list(S)].sum(0), 0)] if N_ else [()]
    if not zw: return 0
    blocks = []
    for E in simple:
        rr, cc_, vv = [], [], []; nzA, nzB = np.nonzero(E)
        for j, S in enumerate(zw):
            Ss = set(S)
            for A_, B_ in zip(nzA, nzB):
                if B_ not in Ss or (A_ != B_ and A_ in Ss): continue
                rem = [x for x in S if x != B_]; sg = (-1) ** S.index(B_); new = sorted(rem + [A_]); sg *= (-1) ** new.index(A_)
                rr.append(ix[tuple(new)]); cc_.append(j); vv.append(sg * E[A_, B_])
        blocks.append(sp.csr_matrix((vv, (rr, cc_)), shape=(len(subs), len(zw))))
    Mx = sp.vstack(blocks).tocsr(); ew = np.linalg.eigvalsh((Mx.T @ Mx).toarray())
    return int(np.sum(ew < 1e-9))
s16 = [singlets(N_, 16, WT, SIMPLE16) for N_ in range(1, 9)]
WT32 = np.array([np.concatenate([WT[A], [0.5 - s_]]) for A in range(16) for s_ in (0, 1)])
SIMPLE32 = [np.kron(E, np.eye(2)) for E in SIMPLE16] + [np.kron(np.eye(16), np.array([[0., 1.], [0., 0.]]))]
s32 = [singlets(N_, 32, WT32, SIMPLE32) for N_ in (2, 4)]
check('S1 no Spin(10)-invariant bilinear pairs 16 with 16 (a mirror 16bar needs interactions; a 16-16bar Dirac mass would '
      'gap both); a spinless 16 (16 modes) has no singlet in Lambda^N for N = 1..8, so no invariant quartic at all',
      inv_forms(T16, T16) == 0 and inv_forms(T16, T16b) == 1 and s16 == [0] * 8, f'Lambda^1..8(16) singlets {s16}')
B1 = GAM[0] @ GAM[2] @ GAM[4] @ GAM[6] @ GAM[8]
SP = [(B1 @ GAM[p])[np.ix_(EV, EV)] for p in range(10)]
eps = np.array([[0, 1], [-1, 0]]); MP = [np.kron(x, eps) for x in SP]
def ad_pair(Mm, dag):
    A = np.zeros((64, 64), complex)
    if dag: A[32:, :32] = 2 * Mm.conj().T
    else: A[:32, 32:] = 2 * Mm
    return A
gens = [ad_pair(m, False) for m in MP] + [ad_pair(m, True) for m in MP]
basis = []
def add(X):
    v = X.ravel().copy()
    for bb_ in basis: v -= np.vdot(bb_, v) * bb_
    nv = np.linalg.norm(v)
    if nv > 1e-8: basis.append(v / nv); return True
    return False
for g in gens: add(g)
front = list(gens)
while front:
    new = []
    for Xm in front:
        for Ym in gens:
            Z = Xm @ Ym - Ym @ Xm
            if add(Z): new.append(Z)
    front = new
def pair_square_norm():
    """norm of sum_p Phi^p^dag Phi^p^dag |0> on 32 modes (Phi^p^dag = sum conj(M_IJ) c_J^dag c_I^dag), bit-level."""
    st = {}
    for Mm in MP:
        nz = [(I, J, np.conj(Mm[I, J])) for I, J in zip(*np.nonzero(Mm))]
        for I, J, v1 in nz:
            for K, L, v2 in nz:
                s_, g_ = 0, v1 * v2
                for k_ in (I, J, K, L):            # rightmost operator of c_L^dag c_K^dag c_J^dag c_I^dag acts first
                    s_, sg = apply_c(k_, s_, True)
                    if s_ is None: break
                    g_ *= sg
                if s_ is not None: st[s_] = st.get(s_, 0) + g_
    return np.sqrt(sum(abs(v) ** 2 for v in st.values()))
nps = pair_square_norm()
check('S2 with the two spin components (32 modes per site): no invariant mass (Lambda^2 singlets 0), the invariant '
      'quartic is unique (Lambda^4 singlets 1, and (Phi^dag.Phi^dag)|0> is nonzero, so it is the 10-channel pair square), and '
      'the pairs Phi^p and their adjoints generate a 66-dim algebra (so(12) = so(10)+so(2)+10+10)',
      s32 == [0, 1] and nps > 1 and all(np.allclose(x, x.T) for x in SP) and len(basis) == 66,
      f'Lambda^2, Lambda^4 singlets {s32}, |(Phi.Phi)^dag|0>| = {nps:.1f}, algebra dim {len(basis)}')
print('   not run: the 2^32-state site (beyond the size cap), so no SMG gap, uniqueness or phase is claimed here')

print('== measured reality used')
print('   N_nu = 2.984 +- 0.008 (LEP Z width): the two Margolus tastes per internal state cannot both stay light')
print('   |q_n| < 1.5e-21 e, |q_e + q_p| ~< 1e-21 e (neutrality); LEP C_A = 2.89 +- 0.21, C_F = 1.30 +- 0.09 (SU(3) triplets)')
print('   parity violation (sin^2 theta_eff = 0.2315 at LEP): weak couplings are chiral')
print('supplied: the rung-1 rule (CL-3 at rung 1, cell modes carried in parallel), the plain internal action, the mass '
      'matrix, the chiral assignment, the 5-mode register; cited: none of the anomaly-free SMG literature is rederived.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
