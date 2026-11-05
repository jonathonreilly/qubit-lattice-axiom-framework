#!/usr/bin/env python3
"""Does the structure of a site or block register select a gauge group?  Supplied models, finite exact
diagnostics; no physical identification.

A. One-body covariance on a 2x2x2 block (one mode per corner) under the 24 rotations about its centre:
   plain corner permutations, and the spin-3/2-twisted action under which the CL-3 (v3) edge coin is covariant.
B. Whether the forced block symmetry survives the two-partition tick on a 4^3 torus.
C. Link registers: covariant link-operator spaces (rederived), state counts, and what a register size selects.
D. Fock registers Lambda(C^p + C^q): the U(1) that is vacuum-neutral and anomaly-free, for every split p+q <= 6.
E. Many-body (Fock) commutants of the block rotations.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 60

import os, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm, null_space

T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(7)
C = np.array(list(itertools.product((0, 1), repeat=3)))            # corner a <-> index 4x+2y+z
IDX = {tuple(c): i for i, c in enumerate(C)}
HAM = np.array([[int(np.sum(abs(C[a] - C[b]))) for b in range(8)] for a in range(8)])

def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J32 = Jm(1.5)
def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    w, v = np.linalg.eigh(sum(n[k] * J32[k] for k in range(3))); return v[:, -1]
XI = [coh(2 * C[a] - 1.0) for a in range(8)]
GM = np.array([[XI[a].conj() @ XI[b] for b in range(8)] for a in range(8)])
W0 = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if HAM[a, b] == 1:
            W0[a, b] = -(1 / np.sqrt(3)) * GM[a, b] / abs(GM[a, b])

ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): ROTS.append(R)

def su2_lift(R, J):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if th < 1e-9: return np.eye(len(J[0]), dtype=complex)
    if abs(th - np.pi) < 1e-9:
        w, v = np.linalg.eig(R); n = np.real(v[:, np.argmin(abs(w - 1))])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    return expm(-1j * th * sum(n[k] * J[k] for k in range(3)))

def corner_map(R):
    return [IDX[tuple(((R @ (2 * C[a] - 1) + 1) // 2).astype(int))] for a in range(8)]

PERM, TWIST, PHMAX = [], [], 0.0
for R in ROTS:
    mp = corner_map(R); D = su2_lift(R, J32)
    P = np.zeros((8, 8)); V = np.zeros((8, 8), complex)
    for a in range(8):
        ph = XI[mp[a]].conj() @ (D @ XI[a]); PHMAX = max(PHMAX, abs(abs(ph) - 1))
        P[mp[a], a] = 1; V[mp[a], a] = ph
    PERM.append(P); TWIST.append(V)

def commutant(reps, d):
    """Basis of {X : V X = X V for all V in reps} via the group average (exact projector)."""
    cols = []
    for a in range(d):
        for b in range(d):
            E = np.zeros((d, d), complex); E[a, b] = 1
            cols.append(sum(V @ E @ V.conj().T for V in reps).ravel() / len(reps))
    M = np.array(cols).T
    u, s, vh = np.linalg.svd(M); r = int(np.sum(s > 1e-9))
    return [u[:, k].reshape(d, d) for k in range(r)]

def comm_norm(A, B): return np.linalg.norm(A @ B - B @ A)

# ===================== A. block covariance =====================
print('== A. one-body covariance on the 8-corner block (24 rotations about its centre)')
chi_p = [int(round(np.trace(P))) for P in PERM]
cp = commutant(PERM, 8)
ab_p = max(comm_norm(x, y) for x in cp for y in cp)
Hp = sum(rng.normal() * (x + x.conj().T) for x in cp)
wp = np.round(np.linalg.eigvalsh(Hp), 8); dims_p = sorted(list(wp).count(v) for v in set(wp))
check('A1 plain corner permutations: multiplicity-free summands of dims 1,1,3,3 (A1+A2+T1+T2); commutant dim 4 '
      'and abelian -> U(1)^4', len(cp) == 4 and ab_p < 1e-10 and round(sum(c * c for c in chi_p) / 24) == 4
      and dims_p == [1, 1, 3, 3], f'summand dims {dims_p}, max [X,Y] = {ab_p:.0e}')
cov = max(np.linalg.norm(V @ W0 @ V.conj().T - W0) for V in TWIST)
uni = max(np.linalg.norm(V.conj().T @ V - np.eye(8)) for V in TWIST)
check('A2 spin-3/2 twist: each rotation sends xi_a to a unit phase times xi_Ra; the CL-3 coin W0 is covariant',
      PHMAX < 1e-12 and cov < 1e-12 and uni < 1e-12, f'phase-modulus err {PHMAX:.0e}, ||V W0 V^+ - W0|| <= {cov:.0e}')
chi_t = np.array([np.trace(V) for V in TWIST])
nz = sorted(set(np.round(abs(chi_t), 6)))
ct = commutant(TWIST, 8)
ab_t = max(comm_norm(x, y) for x in ct for y in ct)
cent = []
for coeffs in np.eye(len(ct)):
    X = sum(c * b for c, b in zip(coeffs, ct)); cent.append(np.concatenate([(X @ y - y @ X).ravel() for y in ct]))
zdim = len(ct) - np.linalg.matrix_rank(np.array(cent).T, tol=1e-9)
Emap = np.array(XI).T                                                 # C^8 -> C^4, e_a -> xi_a
inter = max(np.linalg.norm(su2_lift(R, J32) @ Emap - Emap @ V) for R, V in zip(ROTS, TWIST))
check('A3 twisted: |chi| = 8 at identity, 2 on the 8 body-diagonal turns, 0 elsewhere -> 8 = 2 x (spin 3/2); '
      'commutant = M_2(C) (dim 4, non-commutative, 1-dim centre): a forced copy U(2)',
      len(ct) == 4 and ab_t > 0.5 and zdim == 1 and nz == [0.0, 2.0, 8.0] and inter < 1e-12
      and np.linalg.matrix_rank(Emap) == 4,
      f'|chi| values {[float(x) for x in nz]}, max [X,Y] = {ab_t:.2f}, centre dim {zdim}, D E = E V err {inter:.0e}')
per_class = {}
for h in range(4):
    reps = []
    for a in range(8):
        for b in range(8):
            if HAM[a, b] == h:
                E = np.zeros((8, 8), complex); E[a, b] = 1
                reps.append(sum(V @ E @ V.conj().T for V in TWIST).ravel())
    per_class[h] = np.linalg.matrix_rank(np.array(reps), tol=1e-9)
inC = np.linalg.norm(W0 - sum(np.vdot(b, W0) * b for b in ct))
ev = np.round(np.linalg.eigvalsh(W0), 9)
check('A4 one covariant operator per corner distance 0,1,2,3 (identity, edge hop, face diagonal, body diagonal); '
      'W0 lies in the copy algebra with eigenvalues +-1 x 4 (W0 = n.sigma x 1_4)',
      [per_class[h] for h in range(4)] == [1, 1, 1, 1] and inC < 1e-12 and list(ev).count(1.0) == 4 and list(ev).count(-1.0) == 4,
      f'dims by distance {[int(per_class[h]) for h in range(4)]}')
diag_dim = np.linalg.matrix_rank(np.array([np.diag(np.diag(b)).ravel() for b in ct]), tol=1e-9)
check('A5 covariant site-diagonal block operators = scalars only: per-site phase registers can compensate only the '
      'U(1) block phase, never the copy SU(2)', diag_dim == 1, f'rank of diagonal parts = {diag_dim}')
cw = len(ct) - np.linalg.matrix_rank(np.array([(W0 @ x - x @ W0).ravel() for x in ct]).T, tol=1e-9)
check('A6 commutant of {rotations, coin} = span{1, W0}: the coin breaks the copy U(2) to U(1) x U(1)', cw == 2,
      f'dim {cw}')
# repo colour embedding: su(3) on the b1<->b2-symmetric base (x) b3 fiber
s3 = np.array([[1, 0, 0, 0], [0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0], [0, 0, 0, 1], [0, 1 / np.sqrt(2), -1 / np.sqrt(2), 0]])
lam = [np.array(m, complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / np.sqrt(3))]
Tcol = []
for l in lam:
    B = np.zeros((4, 4), complex); B[:3, :3] = l / 2
    Tcol.append(np.kron(s3.T @ B @ s3, np.eye(2)))                    # (b1 b2) base (x) b3 fiber = index 4b1+2b2+b3
brk_p = max(comm_norm(V, T) for V in PERM for T in Tcol)
brk_t = max(comm_norm(V, T) for V in TWIST for T in Tcol)
check('A7 the repo symmetric-base su(3) is not rotation covariant (plain or twisted); no su(3) fits in u(1)^4 or u(2) '
      '(8 > 4 dims), so no covariant one-body SU(3) acts on a block', brk_p > 0.3 and brk_t > 0.3,
      f'max ||[V_R, T^a]|| plain {brk_p:.2f}, twisted {brk_t:.2f}')

# ===================== B. torus tick =====================
print('== B. the copy algebra on the two-partition tick (4^3 torus, 64 modes)')
N = 4; sites = list(itertools.product(range(N), repeat=3)); sid = {s: i for i, s in enumerate(sites)}
ev_b, od_b = [], []
for o in itertools.product(range(0, N, 2), repeat=3):
    o = np.array(o)
    ev_b.append([sid[tuple((o + C[r]) % N)] for r in range(8)])
    od_b.append([sid[tuple((o + 1 + (1 - C[r])) % N)] for r in range(8)])
def lift(M, blocks):
    out = np.zeros((64, 64), complex)
    for ss in blocks: out[np.ix_(ss, ss)] += M
    return out
He, Ho = lift(W0, ev_b), lift(W0, od_b)
herm = []
for b in ct:
    for h in (b + b.conj().T, 1j * (b - b.conj().T)):
        if np.linalg.norm(h) > 1e-9: herm.append(h)
gens = []
for h in herm:
    h = h - np.trace(h) / 8 * np.eye(8)
    if np.linalg.norm(h) > 1e-9 and all(abs(np.vdot(g, h)) / np.linalg.norm(g) / np.linalg.norm(h) < 1 - 1e-9 for g in gens):
        gens.append(h)
G = np.array([g.ravel() for g in gens]); r_g = np.linalg.matrix_rank(G, tol=1e-9)
U = Ho @ He
# best combination of even-block copy generators that commutes with the tick
Ms = [lift(g, ev_b) for g in gens]
A = np.array([(U @ M - M @ U).ravel() for M in Ms]).T
sv = np.linalg.svd(A, compute_uv=False)
Xn = null_space(A); Bx = sum(c * g for c, g in zip(Xn[:, 0], gens)); Bx = Bx / np.linalg.norm(Bx)
w3 = float(np.linalg.norm(Bx[HAM == 3]) ** 2); Be = lift(Bx, ev_b)
anti = max(np.linalg.norm(Be @ He + He @ Be), np.linalg.norm(Be @ Ho + Ho @ Be))
al = 0.3; Um = (np.cos(al) * Ho + 1j * np.sin(al) * np.eye(64)) @ (np.cos(al) * He + 1j * np.sin(al) * np.eye(64))
brk = np.linalg.norm(Um @ Be - Be @ Um)
check('B1 of the three copy generators lifted to all even blocks, exactly one commutes with the massless tick: the '
      'body-diagonal one, because it anticommutes with both half-ticks (a chiral-type symmetry); the CL-3 mass breaks it. '
      'The copy SU(2) is not a symmetry of the tick', r_g == 3 and int(np.sum(sv < 1e-9)) == 1 and w3 > 1 - 1e-9
      and anti < 1e-9 and brk > 0.1, f'singular values {np.round(sv, 3).tolist()}, mass a=0.3 breaks by {brk:.2f}')

# ===================== C. link registers =====================
print('== C. link registers (G_L x G_R, link operator in (N, Nbar))')
def gens_su(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E / 2)
            E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; out.append(E / 2)
    for k in range(1, n):
        out.append(np.diag([1] * k + [-k] + [0] * (n - k - 1)).astype(complex) / np.sqrt(2 * k * (k + 1)))
    return out
def link_space(n, Lrep, Rrep, d):
    gs = gens_su(n)
    # linear map on vec(U), U indexed [a, b, i, j]: -[L(X), U^ab] - X_ac U^cb = 0 and -[R(Y), U^ab] + U^ad Y_db = 0
    dim = n * n * d * d; M = []
    for k in range(dim):
        Uv = np.zeros(dim, complex); Uv[k] = 1; Ut = Uv.reshape(n, n, d, d); out = []
        for X, LX in zip(gs, Lrep):
            out.append((-(np.einsum('ik,abkj->abij', LX, Ut) - np.einsum('abik,kj->abij', Ut, LX))
                        - np.einsum('ac,cbij->abij', X, Ut)).ravel())
        for Y, RY in zip(gs, Rrep):
            out.append((-(np.einsum('ik,abkj->abij', RY, Ut) - np.einsum('abik,kj->abij', Ut, RY))
                        + np.einsum('adij,db->abij', Ut, Y)).ravel())
        M.append(np.concatenate(out))
    M = np.array(M).T
    return dim - np.linalg.matrix_rank(M, tol=1e-9)
res = {}
for n in (2, 3):
    gs = gens_su(n); z = np.zeros((n, n))
    L = [np.block([[X, z], [z, z]]) for X in gs]; R = [np.block([[z, z], [z, X]]) for X in gs]
    res[f'({n},1)+(1,{n})'] = link_space(n, L, R, 2 * n)
    Rb = [np.block([[z, z], [z, -X.T]]) for X in gs]
    res[f'({n},1)+(1,{n}bar)'] = link_space(n, L, Rb, 2 * n)
gs = gens_su(2)
res['(2,2)'] = link_space(2, [np.kron(X, np.eye(2)) for X in gs], [np.kron(np.eye(2), X) for X in gs], 4)
check('C1 rederived: (N,1)+(1,N) carries covariant link operators in 2N states (dims 2 for N=2, 1 for N=3); '
      '(2,2) and (3,1)+(1,3bar) carry none', res['(2,1)+(1,2)'] == 2 and res['(3,1)+(1,3)'] == 1
      and res['(2,2)'] == 0 and res['(3,1)+(1,3bar)'] == 0, str({k: int(v) for k, v in res.items()}))
# what a register of m qubits admits (joint direct-sum link, R = tensor of fundamentals of SU(N_i), N_i in 2..8)
def products(maxd):
    out = []
    def rec(start, cur, d):
        if cur: out.append(tuple(cur))
        for k in range(start, 9):
            if d * k <= maxd: rec(k, cur + [k], d * k)
    rec(2, [], 1); return out
tab = []
for m in range(1, 7):
    fits = products(2 ** (m - 1)); exact = [g for g in fits if 2 * int(np.prod(g)) == 2 ** m]
    tab.append((m, len(fits), len(exact), (3, 2) in fits, (3, 2) in exact))
print('   m qubits: #SU-products that fit / that fill exactly / (3,2) fits / (3,2) fills: '
      + '; '.join(f'{t[0]}:{t[1]}/{t[2]}/{int(t[3])}/{int(t[4])}' for t in tab))
check('C2 register size selects nothing: from m = 4 qubits on, many SU products fit; SU(3)xSU(2) never fills '
      'a qubit register exactly (2*6 is not a power of 2), and no SU(3) factor ever does',
      all(not t[4] for t in tab) and tab[3][1] >= 5 and all(3 not in g for m in range(1, 7)
      for g in products(2 ** (m - 1)) if 2 * int(np.prod(g)) == 2 ** m))

# ===================== D. Fock registers =====================
print('== D. Fock register Lambda(C^p + C^q), even-parity sector as left-handed Weyl states')
def anomalies(p, q, a, b, cst):
    n = p + q; out = dict(grav=Fr(0), X3=Fr(0), Sp=Fr(0), Sq=Fr(0), Sp3=Fr(0), dbl=0)
    tp = [Fr(1, 2), Fr(-1, 2)] + [Fr(0)] * (p - 2) if p >= 2 else [Fr(0)] * p
    tq = [Fr(1, 2), Fr(-1, 2)] + [Fr(0)] * (q - 2) if q >= 2 else [Fr(0)] * q
    t8 = [Fr(1), Fr(1), Fr(-2)] + [Fr(0)] * (p - 3) if p >= 3 else [Fr(0)] * p
    for S in itertools.product((0, 1), repeat=n):
        if sum(S) % 2: continue
        n3, n2 = sum(S[:p]), sum(S[p:])
        x = a * n3 + b * n2 + cst
        Tp = sum(t for t, s in zip(tp, S[:p]) if s); Tq = sum(t for t, s in zip(tq, S[p:]) if s)
        out['grav'] += x; out['X3'] += x ** 3; out['Sp'] += x * Tp * Tp; out['Sq'] += x * Tq * Tq
        out['Sp3'] += sum(t for t, s in zip(t8, S[:p]) if s) ** 3
    return out
a, b = Fr(-1, 3), Fr(1, 2)
an = anomalies(3, 2, a, b, Fr(0))
Yof = {k: (a * n3 + b * n2) for k, (n3, n2) in {'Q': (1, 1), 'u^c': (2, 0), 'd^c': (2, 2), 'L': (3, 1), 'e^c': (0, 2), 'nu^c': (0, 0)}.items()}
ratios = [Yof[k] / Yof['Q'] for k in ('Q', 'u^c', 'd^c', 'L', 'e^c')]
check('D1 (3,2): the even sector is (3,2)+(3b,1)+(3b,1)+(1,2)+(1,1)+(1,1); Y = N2/2 - N3/3 is vacuum-neutral, '
      'anomaly-free (grav, Y^3, SU3^2Y, SU2^2Y, SU3^3; 4 doublets) with Q:u^c:d^c:L:e^c = 1:-4:2:-3:6',
      all(v == 0 for k, v in an.items() if k != 'dbl') and [int(r) for r in ratios] == [1, -4, 2, -3, 6],
      f"Y = {', '.join(f'{k} {v}' for k, v in Yof.items())}")
# general (a, b, c): linear anomaly conditions, then the cubic
def lin_rows(p, q):
    rows = []
    for basis in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        an = anomalies(p, q, *map(Fr, basis))
        rows.append([float(an['grav']), float(an['Sp']), float(an['Sq'])])
    return np.array(rows).T
NS = null_space(lin_rows(3, 2))
cub = max(abs(float(anomalies(3, 2, *[Fr(x).limit_denominator(10 ** 6) for x in NS @ rng.normal(size=NS.shape[1])])['X3']))
          for _ in range(5))
BL = NS @ np.linalg.lstsq(NS, np.array([-2 / 3, 0, 1]), rcond=None)[0]
check('D2 dropping vacuum neutrality: the anomaly-free U(1)s form span{Y, B-L} with B-L = 1 - 2 N3/3; the '
      'empty register (nu^c) is neutral only for Y', NS.shape[1] == 2 and cub < 1e-6
      and np.linalg.norm(BL - np.array([-2 / 3, 0, 1])) < 1e-9, f'solution dim {NS.shape[1]}, max X^3 {cub:.0e}')
split = []
for n in range(2, 7):
    for p in range(n - 1, 0, -1):
        q = n - p
        if q > p: continue
        an = anomalies(p, q, Fr(q), Fr(-p), Fr(0))
        nontriv = any(Fr(q) * sum(S[:p]) - p * sum(S[p:]) != 0 for S in itertools.product((0, 1), repeat=n) if sum(S) % 2 == 0)
        ok = all(v == 0 for k, v in an.items() if k != 'dbl') and nontriv
        R = lin_rows(p, q); R0 = R[:, :2]
        uniq = np.linalg.matrix_rank(R0, tol=1e-9) == 1
        split.append((p, q, ok and uniq))
print('   vacuum-neutral anomaly-free U(1) unique and consistent, by split: '
      + ' '.join(f'{p}+{q}:{"yes" if o else "no"}' for p, q, o in split))
check('D3 the same holds for every split with p+q in {4,5,6} and fails for p+q <= 3: anomalies plus vacuum '
      'neutrality fix the U(1) once a split is given but do not choose 3+2',
      all(o for p, q, o in split if p + q >= 4) and not any(o for p, q, o in split if p + q <= 3))
check('D4 a block offers no covariant 3+2 split: rotation-invariant mode subspaces of the twisted block have '
      'dimension 0, 4 or 8 (8 = C^2 x C^4), and of the plain block 1,1,3,3 summands (no 2, no 5)',
      len(ct) == 4 and zdim == 1 and len(cp) == 4)

# ===================== E. many-body commutants =====================
print('== E. Fock-space commutants of the twisted block rotations')
def wedge(V, n):
    subs = [S for S in itertools.combinations(range(8), n)]; ix = {S: i for i, S in enumerate(subs)}
    M = np.zeros((len(subs), len(subs)), complex)
    perm = [int(np.argmax(abs(V[:, a]))) for a in range(8)]
    for S in subs:
        img = [perm[a] for a in S]; coef = np.prod([V[perm[a], a] for a in S]) if S else 1.0
        order = np.argsort(img); sgn = np.linalg.det(np.eye(n)[order]) if n else 1.0
        M[ix[tuple(sorted(img))], ix[S]] = coef * sgn
    return M
mults = {}
for n in range(9):
    Vs = [wedge(V, n) for V in TWIST]; d = Vs[0].shape[0]
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); X = X + X.conj().T
    H = sum(V @ X @ V.conj().T for V in Vs) / 24
    w, Q = np.linalg.eigh(H); groups = []
    i = 0
    while i < d:
        j = i
        while j + 1 < d and abs(w[j + 1] - w[i]) < 1e-8: j += 1
        P = Q[:, i:j + 1] @ Q[:, i:j + 1].conj().T
        prof = np.round([np.trace(V @ P) for V in Vs], 6)
        groups.append((j - i + 1, tuple(prof))); i = j + 1
    cnt = {}
    for dd, prof in groups: cnt[(dd, prof)] = cnt.get((dd, prof), 0) + 1
    mults[n] = sorted(((k[0], v) for k, v in cnt.items()), key=lambda t: (-t[1], -t[0]))
print('   n: (irrep dim, multiplicity) ... ' + ' | '.join(f'{n}: ' + ','.join(f'{d}x{m}' for d, m in mults[n][:4]) for n in range(9)))
mx = max(m for n in mults for d, m in mults[n])
check('E1 many-body sectors carry multiplicities up to {} (so U(m) commutants with m >= 3 occur); these act on '
      'n-particle states, not as one-body transformations of the modes, so they are not minimal-coupling gauge '
      'groups and their sizes are counting, not selection'.format(mx), mx >= 3 and mults[1] == [(4, 2)])

print('== measured reality')
print('   colour factors (LEP event shapes / 4-jet, Kluth 2006): C_A = 2.89 +- 0.21, C_F = 1.30 +- 0.09; SU(3): 3, 4/3')
print('   neutral-matter tests (|q_n| < 1.5e-21) and MICROSCOPE select Y over B-L for the massless U(1) (agents/charge)')
print('supplied: block, 24 rotations, spin-3/2 twist (from the CL-3 coin), one mode per corner; link register '
      'definition; Fock register, split, even sector as left-handed, vacuum neutrality. Not derived: any gauge group, '
      'the split 3+2, chirality, or a carrier for a non-abelian connection under the Qubit axiom.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
