#!/usr/bin/env python3
"""Where could three families come from? Exact counts on the CL-1 geometry, the CL-2 tick and the rung ladder.
Supplied models (CL-1 tilings, CL-2 tick, rung readings); finite exact diagnostics; measured values are comparisons only.

A. Every 3 the CL-1 symmetry can permute is the axis set, and covariant operators on it have at most two levels.
B. The site's C3 admits exactly one label for the CL-2 hop; the two copies carry the two complex C3 labels.
C. Partition schemes, (2m)^3 cells, the 27-site cell and zoom by 3.
D. The rung ladder and the three-zoom hypothesis: mass direction, ratios, windows, lifetimes, a 4th family.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from collections import Counter
import numpy as np
from scipy.linalg import expm

T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ rotations, characters, spin
RI = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, perm[i]] = sg[i]
        if round(np.linalg.det(R)) == 1: RI.append(R)
ROTS = [R.astype(float) for R in RI]
def cname(R):
    t = round(np.trace(R))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    return 'C2f' if np.allclose(R, np.diag(np.diag(R))) else "C2'"
TAB = {'A1': dict(E=1, C3=1, C2f=1, C4=1, **{"C2'": 1}), 'A2': dict(E=1, C3=1, C2f=1, C4=-1, **{"C2'": -1}),
       'E': dict(E=2, C3=-1, C2f=2, C4=0, **{"C2'": 0}), 'T1': dict(E=3, C3=0, C2f=-1, C4=1, **{"C2'": -1}),
       'T2': dict(E=3, C3=0, C2f=-1, C4=-1, **{"C2'": 1})}
def dec(chis):
    return tuple(int(round(np.real(sum(t[cname(R)] * ch for R, ch in zip(RI, chis))) / 24)) for t in TAB.values())
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
def state(j, m, n):
    J = Jm(j); w, v = np.linalg.eigh(sum(n[k] * J[k] for k in range(3))); return v[:, int(np.argmin(abs(w - m)))]
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5
def img(R, i): return int(np.argmin(np.sum(abs(cc - R @ cc[i]), 1)))
def corner_W(j, m):
    XI = [state(j, m, (2 * C[i] - 1.0) / np.sqrt(3)) for i in range(8)]
    GM = np.array([[XI[a].conj() @ XI[b] for b in range(8)] for a in range(8)])
    W = np.zeros((8, 8), complex); ov = 9.0
    for a in range(8):
        for b in range(8):
            if np.sum(abs(C[a] - C[b])) == 1:
                ov = min(ov, abs(GM[a, b]))
                if abs(GM[a, b]) > 1e-12: W[a, b] = -GM[a, b] / abs(GM[a, b]) / np.sqrt(3)
    ix = {tuple(v): i for i, v in enumerate(C)}; f = [ix[(0, 0, 0)], ix[(1, 0, 0)], ix[(1, 1, 0)], ix[(0, 1, 0)]]
    barg = np.prod([GM[f[k], f[(k + 1) % 4]] for k in range(4)])
    return W, XI, ov, barg
W, XI, _, _ = corner_W(1.5, 1.5)                                              # the CL-2 hop
def Ublock(K, eps, mu):
    D = np.diag(np.exp(1j * (C @ K)))
    return D @ expm(1j * (eps + mu / 2) * W) @ D.conj().T @ expm(-1j * (eps - mu / 2) * W)
def band(K, eps, mu):
    b = np.pi / 2 - eps; A = (np.cos(2 * b) + np.cos(mu)) / 2; B = (np.cos(2 * b) - np.cos(mu)) / 2
    return np.arccos(np.clip(A * np.mean(np.cos(K)) - B, -1, 1))
w3 = np.exp(2j * np.pi / 3)

# ================================================================== A. geometric threes
print('== A. every 3 the CL-1 symmetry permutes is the axis set')
one = np.ones(3, int)
C4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
def torus(L):
    st = np.array(list(itertools.product(range(L), repeat=3)))
    def perm_of(R, t):
        im = (st @ R.T + t) % L; return tuple(int(v) for v in (im[:, 0] * L + im[:, 1]) * L + im[:, 2])
    rotc = lambda R: perm_of(R, (one - R @ one) // 2)                        # rotation about (1/2,1/2,1/2)
    gu = [perm_of(np.eye(3, dtype=int), np.array(v)) for v in ((2, 0, 0), (0, 2, 0), (0, 0, 2))] + [rotc(C4z), rotc(C3d)]
    return gu + [perm_of(np.eye(3, dtype=int), one)], gu, perm_of
L = 6; N = L ** 3
GPAIR, GUPD, perm_of = torus(L)
def closure(gens):
    n_ = len(gens[0]); e = tuple(range(n_)); seen = {e}; fr = [e]
    while fr:
        nw = []
        for p in fr:
            for g in gens:
                q = tuple(g[i] for i in p)
                if q not in seen: seen.add(q); nw.append(q)
        fr = nw
    return seen
def uf_classes(par):
    def f(a):
        while par[a] != a: par[a] = par[par[a]]; a = par[a]
        return a
    return frozenset(frozenset(i for i in range(N) if f(i) == r) for r in {f(i) for i in range(N)}), f
def block_counts(gens):
    def minimal(t):
        par = list(range(N)); _, f = uf_classes(par); par[f(t)] = f(0); q = [(0, t)]
        while q:
            a, b = q.pop()
            for g in gens:
                x, y = f(g[a]), f(g[b])
                if x != y: par[y] = x; q.append((g[a], g[b]))
        return uf_classes(par)[0]
    sy = {minimal(t) for t in range(1, N)}; changed = True
    while changed:
        changed = False; ls = list(sy)
        for i in range(len(ls)):
            for k in range(i + 1, len(ls)):
                par = list(range(N)); _, f = uf_classes(par)
                for S in (ls[i], ls[k]):
                    for blk in S:
                        bl = list(blk)
                        for x in bl[1:]:
                            ra, rb = f(bl[0]), f(x)
                            if ra != rb: par[rb] = ra
                J = uf_classes(par)[0]
                if J not in sy: sy.add(J); changed = True
    return sorted({len(S) for S in sy})
info = {}; GROUPS = {}
for nm, gens in (('pair', GPAIR), ('upd', GUPD)):
    G = closure(gens); GROUPS[nm] = G; info[nm] = (len(G), len({p[0] for p in G}), sum(p[0] == 0 for p in G), block_counts(gens))
def coset(x):                                                                 # Z^3 / T, T = 2Z^3 u (111 + 2Z^3)
    x = np.array(x) % 2
    if (x == x[0]).all(): return 0
    y = x if x.sum() == 1 else 1 - x; return 1 + int(np.argmax(y))
s4 = {tuple(coset(R @ v + (one - R @ one) // 2) for v in (np.zeros(3, int), *np.eye(3, dtype=int))) for R in RI}
diag_ok = all(len({coset(v) for v in (c_, 1 - c_)}) == 1 for c_ in C)
check('A1 6^3 torus: tiling-pair group 1296, update group 648, both transitive; site stabiliser D3 (6) and C3 (3); the 4 cosets '
      'of the translation lattice T are the 4 body diagonals, permuted as all of S4',
      info['pair'][:3] == (1296, 216, 6) and info['upd'][:3] == (648, 216, 3) and len(s4) == 24 and diag_ok)
offs = list(itertools.product((0, 1), repeat=3))
act = lambda R, o: tuple(int(v) for v in (np.abs(R) @ np.array(o)) % 2)
c3 = [R for R in RI if cname(R) == 'C3' and np.array_equal(R @ one, one)][0]
orb3 = sorted(len(o) for o in {frozenset(act(np.linalg.matrix_power(c3, k), o) for k in range(3)) for o in offs})
fixed = [o for o in offs if act(c3, o) == o]
prs = list({frozenset([o, tuple((np.array(o) + 1) % 2)]) for o in offs}); cl = [p for p in prs if (0, 0, 0) in p][0]
axp = [[p for p in prs if tuple(np.eye(3, dtype=int)[i]) in p][0] for i in range(3)]
asaxes = all(frozenset(act(R, o) for o in cl) == cl and all(frozenset(act(R, o) for o in axp[i]) ==
             axp[int(np.argmax(np.abs(R[:, i])))] for i in range(3)) for R in RI)
s3img = {tuple(prs.index(frozenset(act(R, o) for o in p)) for p in axp) for R in RI}
check('A2 the 8 aligned 2^3 tilings form site-C3 orbits 1+1+3+3: only CL-1\'s two are C3-fixed (no third tiling); the other six '
      'are 3 Margolus pairs permuted exactly as the 3 axes (all of S3)',
      orb3 == [1, 1, 3, 3] and sorted(fixed) == [(0, 0, 0), (1, 1, 1)] and asaxes and len(s3img) == 6)
fun = {nm: [f for f in itertools.product(range(3), repeat=3) if any(f) and all(all((np.array(f) @ (R @ x) - ef(R) * (np.array(f) @ x)) % 3 == 0
       for x in np.eye(3, dtype=int)) for R in RI)] for nm, ef in (('A1', lambda R: 1), ('A2', lambda R: TAB['A2'][cname(R)]))}
col = {tuple(int(a) for a in (v if v[0] == 1 else -v)) for v in (R.T @ one for R in RI)}
check('A3 no covariant 3-colouring: no block system with 3 blocks (either group); exactly, no nonzero F3 functional on T transforms '
      'by a character, so every 3-element orbit is the axes (O -> S3); colourings x+-y+-z mod 3 form one 4-orbit', 3 not in info['pair'][3] and 3 not in info['upd'][3] and not fun['A1']
      and not fun['A2'] and len(col) == 4, f"block counts {info['pair'][3]}")
D4 = [R for R in RI if abs(R[2, 2]) == 1]; D4i = {tuple(R.ravel()): k for k, R in enumerate(D4)}
chars = [v for v in itertools.product((1, -1), repeat=8) if all(v[D4i[tuple((A @ B).ravel())]] == v[a] * v[b]
         for a, A in enumerate(D4) for b, B in enumerate(D4))]
tr_ = [[R for R in RI if int(np.argmax(np.abs(R[:, 2]))) == i][0] for i in range(3)]
res4 = []
for v in chars:
    M = []
    for R in RI:
        P = np.zeros((3, 3))
        for i in range(3):
            jx = int(np.argmax(np.abs((R @ tr_[i])[:, 2])))
            P[jx, i] = v[D4i[tuple((np.rint(np.linalg.inv(tr_[jx])).astype(int) @ R @ tr_[i]).ravel())]]
        M.append(P)
    Aop = np.vstack([np.kron(P, np.eye(3)) - np.kron(np.eye(3), P.T) for P in M])
    res4.append((dec([np.trace(P) for P in M]), int(np.sum(np.linalg.svd(Aop, compute_uv=False) < 1e-9))))
names = lambda t: '+'.join(k for k, n in zip(TAB, t) if n)
inv = lambda p: tuple(sorted(range(len(p)), key=lambda i: p[i]))
mul = lambda p, q: tuple(p[i] for i in q)                                    # (p o q)(i) = p(q(i))
def n_chars(gens):                                                           # |G/[G,G]| = number of 1-dim characters
    e = tuple(range(len(gens[0]))); hg = list({mul(mul(a, b), mul(inv(a), inv(b))) for a in gens for b in gens} - {e})
    while True:
        H = closure(hg); new = list({mul(mul(g, h), inv(g)) for g in gens for h in hg} - H)
        if not new: return len(closure(gens)) // len(H)
        hg += new
nab = {}
for Lc in (4, 6):
    gp, gu, _ = torus(Lc); nab[Lc] = (n_chars(gp), n_chars(gu))
check('A4 Schur on any axis triplet: the four phased orbits Ind(D4 -> O) are ' + ', '.join(f'{names(t)} ({d})' for t, d in sorted(res4))
      + f' (commutant dims): 2-transitive, so at most 2 levels; e, mu, tau need 3. On 4^3 both groups have {nab[4][0]} one-dim '
      'characters (Gamma or R, times A1 or A2): three of them would be a non-degenerate 3, but no rule picks 3 of 4',
      len(chars) == 4 and sorted(d for _, d in res4) == [1, 1, 2, 2] and nab[4] == (4, 4) and nab[6][0] == 4,
      f'(6^3: {nab[6][0]}, {nab[6][1]}; the update group\'s R needs 4 | L)')
K3 = [np.pi * np.array(v) for v in ((1, 1, 0), (1, 0, 1), (0, 1, 1))]
chi = np.array([[np.exp(1j * K @ C[i]) for K in K3] for i in range(8)])
inv_on_cosets = all(np.allclose(chi[i], chi[k]) for i in range(8) for k in range(8) if coset(C[i]) == coset(C[k]))
perm4 = [np.array([[1.0 if coset(R @ v + (one - R @ one) // 2) == a else 0 for v in (np.zeros(3, int), *np.eye(3, dtype=int))] for a in range(4)]) for R in RI]
d4 = dec([np.trace(P) for P in perm4]); x4 = np.array([[np.exp(1j * K @ v) for K in K3] for v in (np.zeros(3), *np.eye(3))])
check('A5 colour is that 3: functions on Z^3/T = V4 are A1 + T2 (lepton + colour of the rung-1 cell), T2 = its 3 nontrivial '
      'characters (momenta pi(1,1,0), ...); nothing geometric is left for families',
      d4 == (1, 0, 0, 0, 1) and inv_on_cosets and np.allclose(x4.conj().T @ x4, 4 * np.eye(3)) and np.allclose(x4.sum(0), 0))

# ================================================================== B. the site C3
print('== B. the site C3 and its labels')
n = np.ones(3) / np.sqrt(3); g3 = -Dj(1.5, n, 2 * np.pi / 3)
lab = {m: np.round(state(1.5, m, n).conj() @ g3 @ state(1.5, m, n), 9) for m in (1.5, 0.5, -0.5, -1.5)}
check('B1 spin 3/2 along the site diagonal, order-3 lift of its C3: 1, 1, w, w^2 (pair m = +-3/2, w: m = 1/2, w^2: m = -1/2)', np.allclose(np.linalg.matrix_power(g3, 3), np.eye(4)) and np.isclose(lab[1.5], 1)
      and np.isclose(lab[-1.5], 1) and np.isclose(lab[0.5], w3) and np.isclose(lab[-0.5], w3 ** 2))
views = {}
for j, m in ((1.5, 1.5), (1.5, 0.5), (0.5, 0.5), (1.5, -1.5)):
    Dg = Dj(j, n, 2 * np.pi / 3); se, so = state(j, m, -n), state(j, m, n)
    views[(j, m)] = np.isclose(se.conj() @ Dg @ se, so.conj() @ Dg @ so)
xC2 = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]); g_ = C3d
pair_ok = (np.array_equal(xC2 @ g_ @ xC2.T, g_.T) and np.array_equal(xC2 @ one, -one) and perm_of(xC2, np.zeros(3, int)) in GROUPS['pair']
           and perm_of(xC2, np.zeros(3, int)) not in GROUPS['upd'])
check('B2 even and odd cube see a site along opposite diagonals (m -> -m): the C3 phase agrees only for m = +-3/2; the pair '
      'group\'s site half-turn inverts the C3, so the label is real: one site label, not three', views[(1.5, 1.5)] and views[(1.5, -1.5)] and not views[(1.5, 0.5)]
      and not views[(0.5, 0.5)] and pair_ok)
cw = {jm: corner_W(*jm) for jm in ((1.5, 1.5), (1.5, 0.5), (0.5, 0.5), (0.5, -0.5))}
wsq = {jm: np.linalg.norm(v[0] @ v[0] - np.eye(8), 2) for jm, v in cw.items()}
check('B3 corner-state hops: (3/2,3/2) faces -1, W^2 = 1; (3/2,1/2) zero edge overlaps (cos b = 1/3 is a node of d^3/2), no hop; '
      '(1/2,+-1/2) faces e^(-+i pi/3), ||W^2-1|| = 1',
      abs(abs(np.angle(cw[(1.5, 1.5)][3])) - np.pi) < 1e-9 and wsq[(1.5, 1.5)] < 1e-12 and cw[(1.5, 0.5)][2] < 1e-12 and np.isclose(np.angle(cw[(0.5, 0.5)][3]), -np.pi / 3)
      and np.isclose(np.angle(cw[(0.5, -0.5)][3]), np.pi / 3) and min(wsq[(0.5, 0.5)], wsq[(0.5, -0.5)]) > 0.5,
      f'||W^2-1|| {wsq[(1.5, 1.5)]:.0e}, min overlap (3/2,1/2) {cw[(1.5, 0.5)][2]:.0e}')
A2c = {k: TAB['A2'][k] for k in TAB['A2']}
cont = {}
for j, m in ((1.5, 1.5), (0.5, 0.5)):
    X_ = [state(j, m, (2 * C[i] - 1.0) / np.sqrt(3)) for i in range(8)]; tot = np.zeros(3, complex)
    for R in ROTS:
        nn, a = axang(R)
        for s in (1, -1):
            Dm = s * Dj(j, nn, a); Lm = np.zeros((8, 8), complex)
            for i in range(8): k = img(R, i); Lm[k, i] = X_[k].conj() @ Dm @ X_[i]
            e12 = s * np.trace(Dj(0.5, nn, a)); g32 = s * np.trace(Dj(1.5, nn, a))
            tot += np.trace(Lm) * np.conj([e12, e12 * A2c[cname(R)], g32]) / 48
    cont[(j, m)] = tuple(int(round(t.real)) for t in tot)
G6 = lambda a: -1j * np.sqrt(3) * (np.diag(C[:, a]) @ W - W @ np.diag(C[:, a]))
al = [G6(a) @ expm(-0.3j * W) for a in range(3)]
Sp = [-.25j * (al[(k + 1) % 3] @ al[(k + 2) % 3] - al[(k + 2) % 3] @ al[(k + 1) % 3]) for k in range(3)]
Rc3 = c3.astype(float); nn, a = axang(Rc3); Gm = np.zeros((8, 8), complex)
for i in range(8): k = img(Rc3, i); Gm[k, i] = XI[k].conj() @ Dj(1.5, nn, a) @ XI[i]
tau = expm(1j * a * sum(nn[k] * Sp[k] for k in range(3))) @ Gm
labs = Counter(int(round(np.angle(e) / (2 * np.pi / 3))) for e in np.linalg.eigvals(tau))
E_on_T = [TAB['E'][cname(R)] for R in RI if TAB['A2'][cname(R)] == 1]
check('B4 m = +-3/2 corners give 2G3/2 = E1/2 x 2E, m = +-1/2 corners E1/2+E5/2+G3/2; a C3 acts on the CL-2 copies as w x4, w^2 x4: '
      'the copies are the complex labels, label 1 is absent; odd rotations swap w, w^2, only A4 (12 even ones) separates them',
      cont[(1.5, 1.5)] == (0, 0, 2) and cont[(0.5, 0.5)] == (1, 1, 1) and labs == Counter({1: 4, -1: 4})
      and len(E_on_T) == 12 and sum(E_on_T) == 0 and sum(abs(x) ** 2 for x in E_on_T) == 24, f'labels {dict(labs)}')

# ================================================================== C. cells and the factor 3
print('== C. partition schemes, cells and zoom by 3')
Wk = {k: [o for o in offs if sum(o) == k] for k in range(4)}
sizes = sorted(len(S) for S in ([o for k in range(4) if mk >> k & 1 for o in Wk[k]] for mk in range(1, 16))
               if sum(o[0] == 0 for o in S) == sum(o[0] == 1 for o in S))
tri = sum(abs(int((R @ one).sum())) == 3 for R in RI)                         # R(1,1,1) = +-(1,1,1) mod 3
check('C1 uniform cubic partition schemes on aligned 2^3 cubes have 2, 4, 6 or 8 tilings, never 3 (no 3-half-tick tick); 3^3 tilings '
      'offset along a diagonal keep 6 of 24 rotations, and 3^3 cubes are site-centred',
      sizes == [2, 4, 4, 6, 8] and tri == 6, f'sizes {sizes}')
def cellpts(side): return 2 * np.array(list(itertools.product(range(side), repeat=3))) - (side - 1)
def content(pts):
    S = {tuple(p) for p in pts}; return dec([sum(tuple(R @ p) == tuple(p) for p in pts) for R in RI])
sh_ok = True; tab = []
for m in (1, 2, 3, 4):
    pts = cellpts(2 * m); seen = set(); orbs = []
    for p in pts:
        if tuple(p) not in seen:
            o = {tuple(R @ p) for R in RI}; seen |= o; orbs.append(o)
    shells = [o for o in orbs if len(o) == 8]; free = [o for o in orbs if len(o) == 24]
    sc = content(np.array([q for o in shells for q in o]))
    sh_ok &= len(shells) == m and len(free) == m * (m * m - 1) // 3 and len(orbs) == len(shells) + len(free) and sc == (m, m, 0, m, m)
    tab.append(content(pts))
check('C2 a (2m)^3 cell has m C3-shells, each exactly 1:1:3:3, and m(m^2-1)/3 free orbits (m = 1..4): 3 shells need m = 3 (zoom 3), '
      '2^n cells have 2^(n-1); free orbits carry the same irreps',
      sh_ok and tab[2] == (11, 11, 16, 27, 27), f'6^3 cell {tab[2]}')
c27 = content(cellpts(3))
check('C3 the site-centred 3^3 cell is (A1,A2,E,T1,T2) = (4,1,2,3,3): 3 triplets of each kind but 4 + 1 singlets, not 3 generations', c27 == (4, 1, 2, 3, 3))
pts3 = [np.array(v) * 2 * np.pi / 3 for v in itertools.product((0, 1, 2), repeat=3)]
kk = lambda K: tuple(np.round(((K + np.pi) % (2 * np.pi)) - np.pi, 6))
osz = sorted(len(o) for o in {frozenset(kk(R @ K) for R in ROTS) for K in pts3})
gap3 = {}
for eps, mu in ((0.04, 0.01), (0.3, 0.2)):
    lv = [(min(3 * band(K, eps, mu) % (2 * np.pi), 2 * np.pi - 3 * band(K, eps, mu) % (2 * np.pi)), np.allclose(K, 0)) for K in pts3]
    gap3[(eps, mu)] = min(x for x, z in lv if not z)
corners3 = all(np.allclose(np.exp(3j * np.pi * np.array(v)), np.exp(1j * np.pi * np.array(v))) for v in offs)
check('C4 zoom 3: (2pi/3)Z^3 folds in O-orbits 1, 6, 8, 12, corners obey 3K = K, only fine Gamma stays light: no new copy', osz == [1, 6, 8, 12] and corners3 and min(gap3.values()) > 0.1,
      'next |3w| ' + ', '.join(f'{v:.3f}' for v in gap3.values()))

# ================================================================== D. the rung ladder
print('== D. rungs: the three-zoom hypothesis')
err = 0
for eps, mu in ((0.04, 0.01), (0.3, 0.2)):
    for v in offs:
        K = np.pi * np.array(v, float); nv = sum(v)
        pred = np.arccos(((3 - nv) * np.cos(mu) + nv * np.cos(2 * eps)) / 3)
        err = max(err, abs(np.sort(np.abs(np.angle(np.linalg.eigvals(Ublock(K, eps, mu))))) - pred).max())
eps, mu, q = 0.3, 0.2, 1e-3; ex = np.array([1.0, 0, 0])
m0, m1 = band(np.zeros(3), eps, mu), 2 * band(np.zeros(3), eps, mu)
c0 = (band(q * ex, eps, mu) ** 2 - m0 ** 2) / q ** 2; c1 = ((2 * band(q * ex / 2, eps, mu)) ** 2 - m1 ** 2) / q ** 2
ph2 = np.abs(np.angle(np.linalg.eigvals(np.linalg.matrix_power(Ublock(np.zeros(3), eps, mu), 2))))
check('D1 cell-pattern levels cos w_n = ((3-n) cos mu + n cos 2eps)/3 (n pi components); two ticks double the per-tick mass, keep '
      'c^2: rung readings of one field have one physical mass (ratio 1)', err < 1e-12 and np.isclose(m1 / m0, 2) and np.isclose(c0, c1, rtol=1e-5) and np.allclose(ph2, 2 * mu),
      f'residual {err:.0e}, c^2 {c0:.5f} -> {c1:.5f}')
r1, s1 = 206.7682830, 4.6e-6; r2 = 1776.93 / 105.6583755; s2 = 0.09 / 105.6583755
l1, l2 = np.log2(r1), np.log2(r2)
check('D2 species written at rung n with one per-tick mass weigh mu/(2^n tau): finer is heavier, tau finest; consecutive rungs give 2, 2; '
      f'measured log2 ratios {l1:.4f}, {l2:.4f} (sqrt-mass {l1 / 2:.3f}, {l2 / 2:.3f}) are not integers; '
      f'the best gaps 8, 4 give 256 ({256 / r1 - 1:+.1%}, {abs(256 - r1) / s1:.1e} sigma) and 16 ({16 / r2 - 1:+.2%}, {abs(16 - r2) / s2:.0f} '
      'sigma); no integer zoom works (neither ratio is an integer)', abs(l1 - round(l1)) > 0.25 and abs(l2 - round(l2)) > 0.05
      and abs(256 - r1) / s1 > 1e6 and abs(16 - r2) / s2 > 500)
mq = dict(u=2.16, d=4.70, s=93.5, c=1273.0, b=4183.0, t=172570.0)
steps = dict(up=(mq['c'] / mq['u'], mq['t'] / mq['c']), down=(mq['s'] / mq['d'], mq['b'] / mq['s']), lep=(r1, r2))
spread = max(max(v) for v in steps.values()) / min(min(v) for v in steps.values())
check('D3 a rung factor per family gives one step in every sector; measured: up ' + ', '.join(f'{x:.0f}' for x in steps['up'])
      + ', down ' + ', '.join(f'{x:.1f}' for x in steps['down']) + f', leptons {r1:.1f}, {r2:.2f} (s/d against mu/e: x{r1 / steps["down"][0]:.1f}), '
      'not a rung property', spread > 30 and r1 / steps['down'][0] > 5)
alpha = 1 / 137.035999; EP = 1.22089e19
dq = (3 * alpha / (2 * np.pi)) * np.log(r1), (3 * alpha / (2 * np.pi)) * np.log(r2)
check('D4 dressing in the rules: link self-energy splits generations by (3 alpha/2pi) ln ratio = '
      f'{dq[0]:.3f}, {dq[1]:.3f}, gravity by <= m/M_P = {1.77693 / EP:.1e}; consecutive rungs need x{r1 / 2:.0f}, x{r2 / 2:.1f}',
      max(dq) < 0.03 and 1.77693 / EP < 1e-18)
a_ = np.sqrt(8 * np.pi) * 1.616255e-35; hc = 1.973269804e-16
ncomp = [np.log2(hc / m / a_) for m in (0.51099895e-3, 0.1056583755, 1.77693)]
win = {th: int(np.floor(np.log2(th / 0.08))) for th in (0.5, 1.0, np.pi / 2, np.pi)}
ten = dec([{'E': 8, 'C3': 2}.get(cname(R), 0) ** 3 for R in RI]); ten_direct = content(cellpts(8))
n2 = tab[1]
check('D5 windows: a cell is exactly one generation only at rung 1 (rung 2: 4 patterns + 4 E + 8 T); a rung-N cell is the N-fold '
      f'product of the 2^3 pattern (rung 3 {ten} vs 3 generations (3,3,0,3,3)); Compton rungs {ncomp[0]:.1f}, {ncomp[1]:.1f}, {ncomp[2]:.1f}; '
      f'pattern levels (top 2eps) resolve for n <= log2(theta/2eps): eps = 0.04 gives {win[0.5]}, {win[1.0]}, {win[np.pi / 2]}, {win[np.pi]} for '
      'theta = 1/2, 1, pi/2, pi; 3 needs eps in (theta/32, theta/16], a supplied threshold, and it counts readings of the same '
      'states; a species written at its own rung keeps its levels at 2eps per own tick, so it has no window',
      n2 == (4, 4, 4, 8, 8) and ten == ten_direct == (24, 24, 40, 64, 64) and win == {0.5: 2, 1.0: 3, np.pi / 2: 4, np.pi: 5} and 59 < ncomp[2] < ncomp[0] < 73)
MS = dict(A1=.1, A2=.25, T1=.4, T2=.7)
PR = {k: sum(TAB[k][cname(R)] * np.array([[1.0 if img(R, i) == kk_ else 0 for i in range(8)] for kk_ in range(8)])
             for R in ROTS) * TAB[k]['E'] / 24 for k in TAB}
U1 = sum(np.kron(Ublock(np.array([0.7, -0.4, 1.3]), 0.3, MS[k]), PR[k]) for k in MS)
leak = max(np.linalg.norm(U1 @ np.kron(np.eye(8), PR[k]) - np.kron(np.eye(8), PR[k]) @ U1, 2) for k in MS)
GF, hb = 1.1663788e-5, 6.582119569e-25
tmu = hb / (GF ** 2 * 0.1056583755 ** 5 / (192 * np.pi ** 3)); ttau = 0.1782 * hb / (GF ** 2 * 1.77693 ** 5 / (192 * np.pi ** 3))
check('D6 each species number commutes with its tick (multiplet leak 0) and CL-5 couples to conserved currents: no rung-to-rung '
      f'decay, heavier rungs stable; the imported law G_F^2 m^5/192pi^3 gives {tmu * 1e6:.3f} us and {ttau * 1e15:.0f} fs (measured 2.197 us, 290.3 fs)', leak < 1e-12 and abs(tmu / 2.1969811e-6 - 1) < 0.01
      and abs(ttau / 290.3e-15 - 1) < 0.01, f'leak {leak:.0e}')
mcross = np.sqrt(8 * np.pi * np.sqrt(2) / GF); nsig = (4 - 2.9840) / 0.0082
check(f'D7 a 4th rung: finer gives tau\' {2 * 1.77693:.2f}, b\' {2 * 4.183:.1f}, t\' {2 * 172.57:.0f} GeV, coarser e\' {0.51099895 / 2:.3f} MeV; '
      f'its neutrino keeps the family ratio and stays light: N_nu = 4 ({nsig:.0f} sigma from 2.984 +- 0.008); escaping needs >= '
      f'{np.log2(45.6 / 0.0182):.1f} rungs; short life hides nothing (tau\' {290.3 / 32:.1f} fs; Gamma = m at {mcross:.0f} GeV); '
      'the one exact edge: no rung finer than 1',
      nsig > 100 and 1700 < mcross < 1800 and np.log2(45.6 / 0.0182) > 11)
print('== measured (comparisons only): CODATA m_mu/m_e; PDG 2024 m_tau, quark masses (MSbar), G_F, lifetimes; LEP N_nu')
print('supplied: CL-2 (eps, mu), rung readings, species per rung (D2), theta (D5), a = sqrt(8 pi) l_P, weak-decay law (D6-7)')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
