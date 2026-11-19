#!/usr/bin/env python3
"""block-reading: can an update on one-mode sites carry block positions as exact internal labels?

Supplied: the register's CL-1 cube tick (spin-3/2 edge hop W, step st, mass angle mu, copy mass Mc on copy A), read at
zoom b (coarse cubes = 2b-blocks of two tilings offset by b(1,1,1)), block positions carried in parallel.  [T] theorem or
exact finite check, [D] finite diagnostic, [E] estimate.
 A  an exact symmetry that rotates all block positions (or the (4,2) of the cell) forces rigid block moves: A x 1
 B  A x 1 is a nearest-neighbour circuit: interleave, depth bounds, the moving-frame (shuttle) form, the covariant
    shuttle -i R1 R2 R3, light cone
 C  covariance, records, exactness of U(b^3), what must be read per coarse cube, light content
 D  the 6^3 block: 216 = 27 x 8 two ways
 E  the link rotor from fermion-mode sites: parity bound, Gauss law, covariant placement, budget
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
from collections import deque
from functools import reduce
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)

# ------------------------------------------------ CL-1 cube objects (inlined) ------------------------------------------------
C = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8); IDX = np.array([4, 2, 1])
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    nv = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(nv[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(d2, sign, axis=None):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            dd = C[a] - C[b]
            if round(float(np.sum(dd ** 2))) == d2 and (axis is None or abs(dd[axis]) == 1):
                g = XI[a].conj() @ XI[b]; H[a, b] = sign * g / abs(g) / np.sqrt(3)
    return H
W = hop(1, -1.0); Fh = hop(2, 1.0); Ssub = np.diag([(-1.0) ** int(x.sum()) for x in C]).astype(complex)
PA = (I8 - Ssub @ Fh) / 2                                   # copy A: carries the copy mass
RAX = [np.sqrt(3) * hop(1, -1.0, k) for k in range(3)]      # R_i = sqrt3 W_i, the cube's axis reflections
S123 = -1j * RAX[0] @ RAX[1] @ RAX[2]                       # covariant shuttle
JINV = np.zeros((8, 8)); JINV[7 - np.arange(8), np.arange(8)] = 1
st, mu, Mc = 0.3, 0.05, 0.3
def gates(Mc_):
    return (expm(-1j * ((st - mu / 2) * I8 - Mc_ / 2 * PA) @ W), expm(1j * ((st + mu / 2) * I8 + Mc_ / 2 * PA) @ W))
Me, Mo = gates(Mc)

# ------------------------------------------------ real-space machinery ------------------------------------------------
def apply_cubes(a, G, p, inv):
    """a: (nv, L, L, L); G on the corner labels of every cube with base = p mod 2; label = geometric corner, or 7 - it."""
    nv, L = a.shape[0], a.shape[1]
    x = np.roll(a, shift=(-p, -p, -p), axis=(1, 2, 3))
    x = x.reshape(nv, L // 2, 2, L // 2, 2, L // 2, 2).transpose(0, 1, 3, 5, 2, 4, 6).reshape(nv, L // 2, L // 2, L // 2, 8)
    if inv: x = x[..., ::-1]
    x = x @ G.T
    if inv: x = x[..., ::-1]
    x = x.reshape(nv, L // 2, L // 2, L // 2, 2, 2, 2).transpose(0, 1, 4, 2, 5, 3, 6).reshape(nv, L, L, L)
    return np.roll(x, shift=(p, p, p), axis=(1, 2, 3))
def permute(a, p1):
    out = np.empty_like(a); out[:, p1[:, None, None], p1[None, :, None], p1[None, None, :]] = a; return out
def perm_e(L, b):
    p = np.empty(L, int)
    for x in range(L):
        N, v = divmod(x, 2 * b); g, r = divmod(v, b); p[x] = 2 * b * N + 2 * r + g
    return p
def perm_o(L, b):
    p = np.empty(L, int)
    for x in range(L):
        N, v = divmod((x + b) % L, 2 * b); g, r = divmod(v, b); p[x] = (2 * b * N + 2 * r + g - b) % L
    return p
def pinv(p): q = np.empty_like(p); q[p] = np.arange(len(p)); return q
def exch1(L, p): return np.array([(x + 1) % L if (x - p) % 2 == 0 else (x - 1) % L for x in range(L)])
def to_coarse(a, b):
    nv, L = a.shape[0], a.shape[1]; Lc = L // b
    return a.reshape(nv, Lc, b, Lc, b, Lc, b).transpose(0, 2, 4, 6, 1, 3, 5).reshape(nv * b ** 3, Lc, Lc, Lc)
def from_coarse(x, nv, b):
    Lc = x.shape[1]; L = Lc * b
    return x.reshape(nv, b, b, b, Lc, Lc, Lc).transpose(0, 4, 1, 5, 2, 6, 3).reshape(nv, L, L, L)
def zoom_tick(a, b, Me_=None, Mo_=None, mid=None):
    """the coarse CL-1 tick with every block position carried in parallel (A x 1); mid: optional site-phase layer."""
    Me_ = Me if Me_ is None else Me_; Mo_ = Mo if Mo_ is None else Mo_
    nv = a.shape[0]; x = apply_cubes(to_coarse(a, b), Me_, 0, False); a2 = from_coarse(x, nv, b)
    if mid is not None: a2 = a2 * mid
    return from_coarse(apply_cubes(to_coarse(a2, b), Mo_, 1, True), nv, b)
def moving_tick(a, b, shuttle='plain', Me_=None, Mo_=None):
    Me_ = Me if Me_ is None else Me_; Mo_ = Mo if Mo_ is None else Mo_; L = a.shape[1]
    pars = [(1 + k) % 2 for k in range(b - 1)]
    x = apply_cubes(a, Me_, 0, False)
    for p in pars: x = permute(x, exch1(L, p)) if shuttle == 'plain' else apply_cubes(x, S123, p, p == 1)
    x = apply_cubes(x, Mo_, b % 2, True) if shuttle == 'plain' else apply_cubes(x, Mo_, b % 2, b % 2 == 1)
    for p in reversed(pars): x = permute(x, exch1(L, p)) if shuttle == 'plain' else apply_cubes(x, S123, p, p == 1)
    return x
def rand_state(L, nv=2): return rng.normal(size=(nv, L, L, L)) + 1j * rng.normal(size=(nv, L, L, L))

# ------------------------------------------------ Bloch machinery (unit cell = one 2^3 cube) ------------------------------------------------
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def tickB(K, Me_=Me, Mo_=Mo): return Dg(K) @ Mo_ @ Dg(K).conj().T @ Me_
def exchB(K, p, G):
    if G is None:                                            # plain corner exchange
        if p == 0: return JINV.astype(complex)
        M = np.zeros((8, 8), complex)
        for i, c in enumerate(C): M[7 - i, i] = np.exp(-1j * K @ (2 * c - 1))
        return M
    return G if p == 0 else Dg(K) @ G @ Dg(K).conj().T
def movingB(K, b, G=None):
    M = np.eye(8, dtype=complex)
    for k in range(b - 1): M = exchB(K, (1 + k) % 2, G) @ M
    if b % 2: Go = Dg(K) @ Mo @ Dg(K).conj().T
    else: Go = JINV @ Mo @ JINV if G is None else Mo
    return M.conj().T @ Go @ M @ Me
def angs(U): return np.sort(np.angle(np.linalg.eigvals(U)))

# ------------------------------------------------ rotations ------------------------------------------------
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, perm[i]] = sg[i]
        if round(np.linalg.det(R)) == 1: ROTS.append(R)
def is_even_rot(R):
    t = round(np.trace(R)); return t == 3 or t == 0 or (t == -1 and np.allclose(R, np.diag(np.diag(R))))
TET = [R for R in ROTS if is_even_rot(R)]
def axang(R):
    R = R.astype(float); a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def Dspin(R): n, a = axang(R); return expm(-1j * a * sum(n[k] * J3[k] for k in range(3)))
PHT = [np.array([[XI[y].conj() @ Dspin(R) @ XI[x] for x in range(8)] for y in range(8)]) for R in ROTS]
def corner_rep(ir):
    R = ROTS[ir]; M = np.zeros((8, 8), complex)
    for i in range(8):
        k = int(np.argmin(np.sum(np.abs(C - (R @ (C[i] - 0.5) + 0.5)), 1))); M[k, i] = PHT[ir][k, i]
    return M
def rot_apply(a, ir, cen, lab):
    """x -> R(x - cen) + cen with the spin-3/2 phase of the labels lab(x) (coarse corner or fine corner)."""
    L = a.shape[1]; X = np.array(list(itertools.product(range(L), repeat=3)))
    Y = np.rint((X - cen) @ ROTS[ir].T + cen).astype(int) % L
    ph = PHT[ir][lab(Y), lab(X)].reshape(L, L, L); out = np.zeros_like(a)
    out[:, Y[:, 0].reshape(L, L, L), Y[:, 1].reshape(L, L, L), Y[:, 2].reshape(L, L, L)] = a * ph
    return out
def comm_dim(gens, tol=1e-9):
    n = gens[0].shape[0]; Mm = np.zeros((n * n, n * n), complex)
    for g in gens:
        A = np.kron(g, np.eye(n)) - np.kron(np.eye(n), g.T); Mm += A.conj().T @ A
    ev = np.linalg.eigvalsh(Mm); return int(np.sum(ev < tol * max(1.0, ev.max())))

# ============================================ A. exact block symmetry => rigid moves ============================================
print('== A. exact symmetry on block positions => rigid block moves (A x 1)')
pairs = sorted({tuple(sorted((i, 7 - i))) for i in range(8)}); dmap = {i: k for k, pr in enumerate(pairs) for i in pr}
Phi = np.zeros((8, 8))
for i in range(8): Phi[2 * dmap[i] + int(C[i].sum()) % 2, i] = 1
E4 = [np.outer(np.eye(4)[i], np.eye(4)[j]) for i in range(4) for j in range(4) if i != j]
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
gens42 = [Phi.T @ np.kron(e, np.eye(2)) @ Phi for e in E4] + [Phi.T @ np.kron(np.eye(4), s_) @ Phi for s_ in sig]
cd42 = comm_dim(gens42); cdlem = comm_dim([np.kron(np.eye(3), np.outer(np.eye(8)[a], np.eye(8)[e])) for a, e in [(j, j + 1) for j in range(7)] + [(j + 1, j) for j in range(7)]])
check('A1 [T] SU(4)xSU(2) on the cell corners as (body diagonal, tetrahedron parity) = (4,2) has commutant 1 (it generates '
      'M_8, as U(216) does on a 6^3 block), and the operators commuting with 1 x M_n are B(coarse) x 1',
      cd42 == 1 and cdlem == 9, f'commutant {cd42}; 3 sites x 8: {cdlem} = 3^2')
disp_ok, reach = True, []
for b in (2, 3):
    L = 4 * b; src = [(x, y, z) for x in range(2 * b) for y in range(2 * b) for z in range(2 * b)]
    a = np.zeros((len(src), L, L, L), complex)
    for n_, s_ in enumerate(src): a[n_][s_] = 1
    out = from_coarse(apply_cubes(to_coarse(a, b), Me, 0, False), len(src), b)
    ds = set()
    for n_, s_ in enumerate(src):
        for y in np.argwhere(np.abs(out[n_]) > 1e-13): ds.add(tuple(((y - np.array(s_) + L // 2) % L) - L // 2))
    disp_ok &= all(all(c_ % b == 0 for c_ in d) for d in ds); reach.append(int(max(max(abs(c_) for c_ in d) for d in ds)))
check('A2 [T] so every hop is a rigid move by b{-1,0,1}^3: fine range b per coarse half-tick, and no single nearest-neighbour '
      'step carries the labels; block-position projectors (the register reading) conserve x mod b likewise',
      disp_ok and reach == [2, 3], f'range {reach} (b = 2, 3)')
eB = max(np.abs(angs(movingB(K, b)) - angs(tickB(b * K))).max() for b in (2, 3, 4, 6) for K in rng.uniform(-np.pi, np.pi, (4, 3)))
lightV = max(np.min(np.abs(np.angle(np.linalg.eigvals(movingB(2 * np.pi * np.array(q) / 3, 3))))) for q in itertools.product(range(3), repeat=3))
heavyF = [np.min(np.abs(np.angle(np.linalg.eigvals(tickB(2 * np.pi * np.array([1, 0, 0]) / b))))) for b in (2, 3)]
check('A3 [T] tastes: the zoom-b band at fine momentum K is the coarse band at bK, so all b^3 folded copies are exactly '
      'degenerate and light; on the fine CL-1 tick they are not (hidden-sector A2)',
      eB < 1e-12 and abs(lightV - mu) < 1e-9 and min(heavyF) > 0.3,
      f'err {eB:.0e}; 27 tastes at |w| {lightV:.2f}; fine tick there {heavyF[0]:.2f}, {heavyF[1]:.2f}')

# ============================================ B. the circuit ============================================
print('== B. A x 1 as a circuit of nearest-neighbour cube gates on one-mode sites')
okB1 = True; rnds = []
for b in range(2, 9):
    m = b; target = [y for j in range(m) for y in (j, m + j)]; rk = {lab: i for i, lab in enumerate(target)}
    arr = list(range(2 * m)); rounds = []; par = (b - 1) % 2
    while [rk[y] for y in arr] != list(range(2 * m)) and len(rounds) < 4 * b:
        sw = [p for p in range(par, 2 * m - 1, 2) if rk[arr[p]] > rk[arr[p + 1]]]
        for p in sw: arr[p], arr[p + 1] = arr[p + 1], arr[p]
        rounds.append(par); par ^= 1
    okB1 &= len(rounds) == b - 1 and rounds[-1] == 1 and all(rounds[i] != rounds[i + 1] for i in range(len(rounds) - 1))
    rnds.append(len(rounds))
errB2 = []
for b in (2, 3, 4, 6):
    L = 4 * b; a = rand_state(L); Pe = perm_e(L, b)
    lhs = from_coarse(apply_cubes(to_coarse(a, b), Me, 0, False), 2, b)
    rhs = permute(apply_cubes(permute(a, Pe), Me, 0, False), pinv(Pe)); errB2.append(np.abs(lhs - rhs).max())
check('B1 [T] the interleave b g + r -> 2r + g of each 2b-block is an exchange network of b-1 rounds alternating tilings, '
      'each round one layer of cube permutations', okB1, f'rounds {rnds[0]}..{rnds[-1]} (b = 2..8)')
check('B2 [T] one isolated coarse half-tick = interleave, CL-1 cube gates, de-interleave: depth 2b-1 (3, 5, 7, 11 at '
      'b = 2, 3, 4, 6), chiral-wall A3 in 3D', max(errB2) < 1e-13, f'err {max(errB2):.0e}')
taus = []
for b in (2, 3):
    L = 4 * b; Lset = [(x, y, z) for x in range(b) for y in range(2 * b) for z in range(2 * b)]
    a = np.zeros((len(Lset), L, L, L), complex)
    for n_, s_ in enumerate(Lset): a[n_][s_] = 1
    out = from_coarse(apply_cubes(to_coarse(a, b), Me, 0, False), len(Lset), b)
    T = out[:, b:2 * b, 0:2 * b, 0:2 * b].reshape(len(Lset), -1); taus.append(int(np.sum(np.linalg.svd(T, compute_uv=False) > 1e-10)))
check('B3 [T] lower bound: transfer rank 4b^3 across the mid-plane, at most 4b^2 per crossing layer, crossing layers '
      'alternate: depth >= 2b-1, so B2 is optimal for isolated carriage', taus == [4 * 8, 4 * 27], f'ranks {taus}')
ok1d = True
for b in range(2, 9):
    L = 4 * b; Mb = perm_o(L, b)[pinv(perm_e(L, b))]; comp = np.arange(L)
    for k in range(b - 1): comp = exch1(L, (1 + k) % 2)[comp]
    pred = np.array([(x - (b - 1)) % L if x % 2 == 0 else (x + (b - 1)) % L for x in range(L)])
    ok1d &= np.array_equal(Mb, pred) and np.array_equal(Mb, comp)
errB4, ctrl = [], []
for b in (2, 3, 4, 6):
    L = 4 * b; a = rand_state(L); Pe = perm_e(L, b); lhs = a.copy(); rhs = permute(a, Pe)
    for _ in range(3): lhs = zoom_tick(lhs, b); rhs = moving_tick(rhs, b)
    errB4.append(np.abs(lhs - permute(rhs, pinv(Pe))).max())
    ctrl.append(np.abs(zoom_tick(a, b) - permute(apply_cubes(apply_cubes(permute(a, Pe), Me, 0, False), Mo, 1, True), pinv(Pe))).max())
check('B4 [T] moving frame: de- then re-interleave moves every mode b-1 sites along a body diagonal (b-1 corner-exchange '
      'layers); tick = P^-1 (G_e X^(b-1) G_o X^(b-1)) P exactly: b layers per coarse half-tick, the light-cone minimum',
      ok1d and max(errB4) < 1e-12 and min(ctrl) > 1, f'3 ticks err {max(errB4):.0e}; no-shuttle control {min(ctrl):.1f}')
covS = [np.abs(corner_rep(i) @ S123 @ corner_rep(i).conj().T - (1 if is_even_rot(ROTS[i]) else -1) * S123).max() for i in range(24)]
eBS = max(np.abs(angs(movingB(K, b, S123)) - angs(tickB(b * K))).max() for b in (2, 3, 4, 5, 6) for K in rng.uniform(-np.pi, np.pi, (3, 3)))
gres = []
for b in (2, 3):
    L = 4 * b; n = L ** 3; rows, cols, vA, vB = [], [], [], []
    for s0 in range(0, n, 216):
        idx = np.arange(s0, min(n, s0 + 216)); e = np.zeros((len(idx), n), complex); e[np.arange(len(idx)), idx] = 1
        e = e.reshape(len(idx), L, L, L); A_ = moving_tick(e, b).reshape(len(idx), n); B_ = moving_tick(e, b, 'S').reshape(len(idx), n)
        for j, col in enumerate(idx):
            nz = np.nonzero(np.abs(A_[j]) > 1e-13)[0]; rows += list(nz); cols += [col] * len(nz); vA += list(A_[j, nz]); vB += list(B_[j, nz])
    rows, cols, vA, vB = map(np.array, (rows, cols, vA, vB)); adj = [[] for _ in range(n)]
    for k_, (r_, c_) in enumerate(zip(rows, cols)): adj[r_].append((c_, k_, 0)); adj[c_].append((r_, k_, 1))
    lam = np.full(n, np.nan + 0j)
    for root in range(n):
        if not np.isnan(lam[root]): continue
        lam[root] = 1; dq = deque([root])
        while dq:
            u = dq.popleft()
            for v2, k_, dirn in adj[u]:
                if np.isnan(lam[v2]): lam[v2] = lam[u] * (vA[k_] / vB[k_] if dirn == 0 else vB[k_] / vA[k_]); dq.append(v2)
    gres.append(max(np.abs(lam[rows] * vA / lam[cols] - vB).max(), np.abs(np.abs(vA) - np.abs(vB)).max()))
check('B5 [T] covariant shuttle X = -iR1R2R3: a reflection, |X| = corner exchange, D X D^+ = +-X under the 24 rotations; '
      'every gate layer is then CL-1\'s own cube unitary in CL-1\'s labels, and the circuit is B4\'s up to a site-phase gauge',
      np.abs(S123 - S123.conj().T).max() < 1e-12 and np.abs(S123 @ S123 - I8).max() < 1e-12 and np.abs(np.abs(S123) - JINV).max() < 1e-12
      and max(covS) < 1e-12 and eBS < 1e-12 and max(gres) < 1e-12, f'{max(covS):.0e}, spec {eBS:.0e}, gauge {max(gres):.0e}')
b = 3; L = 30; Lc = L // b; a = np.zeros((1, L, L, L), complex); s0 = np.array([12, 12, 12]); a[0][tuple(s0)] = 1; Pe = perm_e(L, b)
x = permute(a, Pe); T = 2
for _ in range(T): x = moving_tick(x, b)
sup_mov = np.argwhere(np.abs(x[0]) > 1e-15); sp0 = Pe[s0]
fine_ok = all(max(abs(((q - sp0 + L // 2) % L) - L // 2)) <= 2 * b * T for q in sup_mov)
y = permute(x, pinv(Pe)); sup = np.argwhere(np.abs(y[0]) > 1e-15); dd = ((sup - s0 + L // 2) % L) - L // 2
cr = int(np.max(np.abs(dd)) // b)
check('B6 [D] light cone (b = 3, point source, 12 layers): inside the fine cone at every layer; read back, displacements '
      'are multiples of b and reach exactly the coarse strict cone, zero beyond', fine_ok and np.all(dd % b == 0) and cr == 2 * T,
      f'reach {cr} = 2T coarse sites')

# ============================================ C. covariance, records, symmetry, content ============================================
print('== C. covariance, records, exact U(b^3), shared readings, light content')
cov = {}
for Mc_ in (0.0, Mc):
    Me_, Mo_ = gates(Mc_); Rs = range(24) if Mc_ == 0 else [i for i in range(24) if is_even_rot(ROTS[i])]
    for b in (2, 3):
        L = 4 * b; a = rand_state(L, 1); labC = lambda X, b=b: ((X // b) % 2) @ IDX; labF = lambda X: (X % 2) @ IDX
        e1 = max(np.abs(rot_apply(zoom_tick(a, b, Me_, Mo_), i, cen, labC) - zoom_tick(rot_apply(a, i, cen, labC), b, Me_, Mo_)).max()
                 for i in Rs for cen in (np.full(3, b - 0.5), np.full(3, -0.5)))
        e2 = max(np.abs(rot_apply(moving_tick(a, b, 'S', Me_, Mo_), i, cen, labF) - moving_tick(rot_apply(a, i, cen, labF), b, 'S', Me_, Mo_)).max()
                 for i in Rs for cen in (np.full(3, b - 0.5), np.full(3, b + 0.5)))
        e3 = max(np.abs(rot_apply(permute(a, exch1(L, 1)), i, np.full(3, b - 0.5), labF) - permute(rot_apply(a, i, np.full(3, b - 0.5), labF), exch1(L, 1))).max() for i in Rs)
        Pe = perm_e(L, b); cen0 = np.full(3, b - 0.5)
        e4 = max(np.abs(permute(rot_apply(permute(a, Pe), i, cen0, labF), pinv(Pe)) - rot_apply(a, i, cen0, labC)).max() for i in Rs)
        cov[(Mc_, b)] = (e1, e2, e3, e4)
cmax = max(max(v[0], v[1], v[3]) for v in cov.values()); pl = min(v[2] for v in cov.values())
check('C1 [T] covariance: the zoom-b tick commutes with the 24 rotations (12 with copy mass) about both coarse block centres '
      '(coarse-corner spin-3/2 phase x plain label permutation); CL-1\'s own site action induces exactly that and commutes '
      'with the shuttle form; plain swaps are not covariant', cmax < 1e-12 and pl > 1, f'err {cmax:.0e}; plain swap {pl:.1f}')
check('C2 [T] records: a shuttle layer has one unit-modulus entry per column, so CL-2\'s transport through it is a fixed '
      'permutation of configurations: records formed inside a coarse half-tick add no readable information',
      all(np.sum(np.abs(S123[:, j]) > 1e-12) == 1 for j in range(8)) and np.allclose(np.abs(S123).sum(0), 1))
cU = []
for b in (2, 3):
    L = 4 * b; a = rand_state(L, 1); Xr = rng.normal(size=(b ** 3, b ** 3)) + 1j * rng.normal(size=(b ** 3, b ** 3))
    def lab_op(v, b=b, Xr=Xr):
        Lc = v.shape[1] // b; y = v.reshape(1, Lc, b, Lc, b, Lc, b).transpose(0, 1, 3, 5, 2, 4, 6).reshape(1, Lc, Lc, Lc, b ** 3) @ Xr.T
        return y.reshape(1, Lc, Lc, Lc, b, b, b).transpose(0, 1, 4, 2, 5, 3, 6).reshape(v.shape)
    chiC = np.repeat(np.repeat(np.repeat(np.exp(2j * np.pi * rng.random((L // b,) * 3)), b, 0), b, 1), b, 2)
    chiF = np.exp(2j * np.pi * rng.random((L,) * 3))
    nrm = np.abs(lab_op(a)).max()
    cU.append([np.abs(zoom_tick(lab_op(a), b, mid=m_) - lab_op(zoom_tick(a, b, mid=m_))).max() / nrm for m_ in (None, chiC, chiF)])
cU = np.array(cU)
check('C3 [T] U(b^3) is exact; one link phase per coarse site keeps it, independent fine-site phases break it at O(1): edges '
      'and links must be read per coarse cube, alike for every label', cU[:, :2].max() < 1e-12 and cU[:, 2].min() > 0.1,
      f'{cU[:, 0].max():.0e}, {cU[:, 1].max():.0e}; fine {cU[:, 2].min():.2f}')
dims = []
for b in (2, 3, 6):
    pts = [tuple(2 * np.array(p) - (b - 1)) for p in itertools.product(range(b), repeat=3)]; ix = {p: i for i, p in enumerate(pts)}
    Ps = []
    for R in ROTS:
        P = np.zeros((len(pts),) * 2)
        for p in pts: P[ix[tuple(R @ np.array(p))], ix[p]] = 1
        Ps.append(P)
    H = rng.normal(size=(len(pts),) * 2); Ml = sum(P @ (H + H.T) @ P.T for P in Ps) / 24
    ev = np.sort(np.linalg.eigvalsh(Ml)); dims.append(sum(len(g) ** 2 for g in np.split(ev, np.where(np.diff(ev) > 1e-8)[0] + 1)))
w0 = np.sort(np.abs(np.angle(np.linalg.eigvals(tickB(np.zeros(3))))))
check('C4 [T] light content: one light Dirac copy per label (4 states at |w| = mu, partner at mu + M), b^3 in all; generic '
      'covariant label masses leave exact groups of dim 20, 67, 572 (b = 2, 3, 6), which CL-3 would all link',
      np.allclose(w0[:4], mu) and np.allclose(w0[4:], mu + Mc) and dims == [20, 67, 572], f'|w| {w0[0]:.2f}, {w0[4]:.2f}')

# ============================================ D. the 6^3 block ============================================
print('== D. the 6^3 block')
okD = True; r6 = np.array(list(itertools.product(range(6), repeat=3)))
for R in ROTS:
    y = (r6 * 2 - 5) @ R.T; y = (y + 5) // 2
    s, t = r6 // 2, r6 % 2; sy = ((2 * s - 2) @ R.T + 2) // 2; ty = ((2 * t - 1) @ R.T + 1) // 2
    okD &= np.array_equal(y, 2 * sy + ty)
    t2, s2 = r6 // 3, r6 % 3; ty2 = ((2 * t2 - 1) @ R.T + 1) // 2; sy2 = ((s2 - 1) @ R.T) + 1
    okD &= np.array_equal(y, 3 * ty2 + sy2)
turn = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
fix = int(np.sum(np.all(((r6 * 2 - 5) @ turn.T) == (r6 * 2 - 5), 1)))
fs = sum(1 for s in itertools.product(range(3), repeat=3) if np.array_equal(turn @ (np.array(s) - 1), np.array(s) - 1))
check('D1 [T] r = 2s + t (27 sub-cubes x 8 corners) and r = 3t + s (8 octants x 27) both intertwine the 24 rotations with '
      'R_s x R_t, so U(216) holds U(27) x U(8) both ways; the three-fold turn fixes 6 = 3 x 2 positions',
      okD and fix == 6 and fs == 3, f'fixed {fix}, register {fs}')

# ============================================ E. the link rotor ============================================
print('== E. the link rotor from fermion-mode sites')
def ferm(k):
    Zp = np.diag([1.0, -1.0]); an = np.array([[0, 1.0], [0, 0]])
    return [reduce(np.kron, [Zp] * j + [an] + [np.eye(2)] * (k - j - 1)) for j in range(k)]
k = 5; cs = ferm(k); dimF = 2 ** k; occ = np.array(list(itertools.product((0, 1), repeat=k)))
parity = np.diag((-1.0) ** occ.sum(1)); om = np.exp(2j * np.pi / 8)
ev_c = [c_ for c_ in itertools.product((0, 1), repeat=4) if sum(c_) % 2 == 0]; od_c = [c_ for c_ in itertools.product((0, 1), repeat=4) if sum(c_) % 2]
def clock_ops(rot_modes, n_modes, occ_):
    d = len(occ_); X = np.zeros((d, d), complex); Z = np.zeros((d, d), complex); key = {tuple(o): i for i, o in enumerate(occ_)}
    for s_ in range(d):
        rc = tuple(occ_[s_, rot_modes]); lst = ev_c if sum(rc) % 2 == 0 else od_c; j = lst.index(rc); o2 = occ_[s_].copy()
        o2[rot_modes] = lst[(j + 1) % 8]; X[key[tuple(o2)], s_] = 1; Z[s_, s_] = om ** j
    return X, Z
X8, Z8 = clock_ops([0, 1, 2, 3], 5, occ)
okW = (np.abs(np.linalg.matrix_power(X8, 8) - np.eye(dimF)).max() < 1e-12 and np.abs(np.linalg.matrix_power(Z8, 8) - np.eye(dimF)).max() < 1e-12
       and np.abs(Z8 @ X8 - om * X8 @ Z8).max() < 1e-12 and np.abs(X8 @ parity - parity @ X8).max() < 1e-12
       and np.abs(X8 @ cs[4] - cs[4] @ X8).max() < 1e-12 and np.abs(Z8 @ cs[4] - cs[4] @ Z8).max() < 1e-12)
cs4 = ferm(4); occ4 = np.array(list(itertools.product((0, 1), repeat=4))); key4 = {tuple(o): i for i, o in enumerate(occ4)}; Xb = np.zeros((16, 16))
for s_ in range(16):
    v = (int(occ4[s_, :3] @ [4, 2, 1]) + 1) % 8; o2 = occ4[s_].copy(); o2[:3] = [(v >> 2) & 1, (v >> 1) & 1, v & 1]; Xb[key4[tuple(o2)], s_] = 1
p4 = np.diag((-1.0) ** occ4.sum(1))
mix = min(np.abs(Xb @ p4 - p4 @ Xb).max(), np.abs(Xb @ cs4[3] - cs4[3] @ Xb).max(), np.abs(Xb @ cs4[3] + cs4[3] @ Xb).max())
check('E1 [T] k fermion modes: a parity-even Z_N clock pair acts within parity sectors of dim 2^(k-1), so N | 2^(k-1) '
      '(N <= 2^(k-1) with a constraint): three sites give at most Z_4 < 5, and the 3-site binary clock mixes parity; four '
      'sites carry Z_8 exactly', okW and mix > 1, f'binary-clock defect {mix:.0f}')
k = 6; cs6 = ferm(k); occ6 = np.array(list(itertools.product((0, 1), repeat=6)))
Xl, Zl = clock_ops([1, 2, 3, 4], 6, occ6); na, nb = cs6[0].T @ cs6[0], cs6[5].T @ cs6[5]
Hh = cs6[0].T @ Zl @ cs6[5]; Hh = Hh + Hh.conj().T
Ga = expm(2j * np.pi / 8 * na) @ Xl; Gb = expm(2j * np.pi / 8 * nb) @ Xl.conj().T
check('E2 [T] Z_8 Gauss law: matter a, b and a 4-mode link; a^+ U b + h.c. commutes with both Gauss operators w^(n_a) V, '
      'w^(n_b) V^+ (order 8, commuting)', max(np.abs(Hh @ G_ - G_ @ Hh).max() for G_ in (Ga, Gb)) < 1e-12
      and np.abs(np.linalg.matrix_power(Ga, 8) - np.eye(64)).max() < 1e-10 and np.abs(Ga @ Gb - Gb @ Ga).max() < 1e-12)
def orbits(b):
    pts = [tuple(np.array(p) * 2 - (b - 1)) for p in itertools.product(range(b), repeat=3)]; seen = set(); out = []
    for p in pts:
        if p in seen: continue
        o = sorted({tuple(R @ np.array(p)) for R in ROTS}); seen |= set(o); out.append(o)
    return out
def inv_even(pts):
    ix = {p: i for i, p in enumerate(pts)}; tot = 0.0
    for R in ROTS:
        P = np.zeros((len(pts),) * 2)
        for p in pts: P[ix[tuple(R @ np.array(p))], ix[p]] = 1
        tot += (np.linalg.det(np.eye(len(pts)) + P) + np.linalg.det(np.eye(len(pts)) - P)) / 2
    return int(round(tot / 24))
osz = sorted({len(o) for b in range(2, 8) for o in orbits(b)}); ob3 = {len(o): o for o in orbits(3)}
inv_dims = {n_: inv_even(ob3[n_]) for n_ in (6, 8, 12)}
check('E3 [T] covariant placement: rotation orbits in a block have sizes 1, 6, 8, 12, 24 (b = 2..7), so no 4-site rotor set '
      'is invariant; rotation-invariant even states: 6-orbit 2, 8-orbit 8 (one Z_8), 12-orbit 88 = 8 x 11',
      osz == [1, 6, 8, 12, 24] and inv_dims == {6: 2, 8: 8, 12: 88})
r7 = np.array(list(itertools.product(range(-3, 4), repeat=3))); mat = r7[np.all(r7 != 0, 1)]
okE4 = len(mat) == 216
for R in ROTS:
    y = mat @ R.T; sgn, mag = np.sign(mat), np.abs(mat); perm_ = np.abs(R)
    okE4 &= np.array_equal(np.sign(y), sgn @ R.T) and np.array_equal(np.abs(y), mag @ perm_.T)
fm = sum(1 for v in itertools.product((1, 2, 3), repeat=3) if np.array_equal(np.abs(turn) @ np.array(v), np.array(v)))
cp = sorted(len(o) for o in orbits(7) if any(0 in p for p in o))
check('E4 [T] budget: the 6^3 block read as 27 x 8 has no spare site; a 7^3 block holds the 216 labels on {+-1,+-2,+-3}^3 '
      '(8 octants x 27 magnitudes, 3 turn-fixed) plus a covariant Z_8 rotor on a 12-site central-plane orbit (constraint to '
      'its 88 invariant states), 115 sites inert', okE4 and fm == 3 and sum(cp) == 127 and 12 in cp and 8 not in cp)

# ============================================ F. estimates against measurement ============================================
print('== F. estimates against measurement')
print('   216 light Dirac copies at b = 6 before label terms vs N_nu = 2.9963 +- 0.0074 (LEP): label terms, supplied, must')
print('   lift all but the observed labels; speed, strict cone and G per coarse cell unchanged; no chirality (finite circuit).')
print('theorems A1-A3, B1-B5, C1-C4, D1, E1-E4; diagnostic B6. supplied: zoom b, 2b-block grid, per-coarse-cube edge/link')
print('  reading, the shuttle (= the parallel-carriage choice), CL-1 st, mu, Mc, the rotor\'s role-assigned sites + constraint.')
print('  cited: Z_N (N >= 5) Coulomb phase; chiral-wall A3; hidden-sector A2.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
