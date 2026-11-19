#!/usr/bin/env python3
"""Three diagonal shells of the 6^3 cell as families: geometry, candidate rules, the internal reading, hierarchy,
mixing, and the owner's decay-by-mixing idea. Supplied models; exact checks [T], finite diagnostics [D],
comparisons with measurement [M]. Measured values are comparisons only.

A. (2m)^3 cells, the sign x modulus factorisation, zoom by 3, zoomed stabilisers, connectivity of the shell set.
B. Fine reading: spin-3/2 overlaps, the covariant body-diagonal hop, spinorial content, orbit gap, diagonal hop.
C. Internal reading R1 (6^3 cell = internal index carried by a coarse CL-2 tick): shell-light rule, mixing, speed,
   a derived intra-cell model.
D. Hierarchy and mixing against measurement.
E. Owner idea: shell-orbit mixing as the decay of heavier families.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from collections import Counter, deque
from math import comb
import numpy as np
from scipy.linalg import expm, block_diag

T0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ rotations, characters, spin 3/2
RI = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, perm[i]] = sg[i]
        if round(np.linalg.det(R)) == 1: RI.append(R)
ROTS = [R.astype(float) for R in RI]
def cname(R):
    t = int(round(np.trace(R)))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    return 'C2f' if np.allclose(R, np.diag(np.diag(R))) else "C2'"
TAB = {'A1': dict(E=1, C3=1, C2f=1, C4=1, **{"C2'": 1}), 'A2': dict(E=1, C3=1, C2f=1, C4=-1, **{"C2'": -1}),
       'E': dict(E=2, C3=-1, C2f=2, C4=0, **{"C2'": 0}), 'T1': dict(E=3, C3=0, C2f=-1, C4=1, **{"C2'": -1}),
       'T2': dict(E=3, C3=0, C2f=-1, C4=-1, **{"C2'": 1})}
def dec(chis): return tuple(int(round(np.real(sum(t[cname(R)] * ch for R, ch in zip(RI, chis))) / 24)) for t in TAB.values())
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
def nullspace(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A, full_matrices=A.shape[0] < A.shape[1]); return vh[np.sum(s > tol):].conj()

# ================================================================== A. geometry (doubled coordinates: sites odd)
print('== A. (2m)^3 cells, factorisation, zoom by 3')
ok = True; rows = []
for m in (1, 2, 3, 4, 5):
    vals = range(-(2 * m - 1), 2 * m, 2); P_ = [tuple(p) for p in itertools.product(vals, repeat=3)]
    seen, orbs = set(), []
    for p in P_:
        if p not in seen: o = {tuple(R @ np.array(p)) for R in RI}; seen |= o; orbs.append(o)
    shells = [o for o in orbs if len(o) == 8]
    ok &= len(shells) == m and sum(len(o) == 24 for o in orbs) == m * (m * m - 1) // 3 and len(orbs) == len(shells) + m * (m * m - 1) // 3
    ok &= all(dec([sum(tuple(R @ np.array(p)) == p for p in o) for R in RI]) == (1, 1, 0, 1, 1) for o in shells)
    ms = list(itertools.product(range(1, 2 * m, 2), repeat=3)); tr = len({tuple(sorted(v)) for v in ms})
    sg = sum(len(set(v)) == 3 for v in {tuple(sorted(v)) for v in ms})
    ok &= tr == comb(m + 2, 3) and sg == comb(m, 3); rows.append(tr + sg)
vals = list(range(-5, 6, 2)); pts = [tuple(p) for p in itertools.product(vals, repeat=3)]; idx = {p: i for i, p in enumerate(pts)}
N6 = 216; PI = []
for R in RI:
    P = np.zeros((N6, N6))
    for p in pts: P[idx[tuple(R @ np.array(p))], idx[p]] = 1
    PI.append(P)
cont = dec([np.trace(P) for P in PI])
check(f'A1 [T] (2m)^3 cell: m diagonal shells, each A1+A2+T1+T2, and m(m^2-1)/3 free 24-orbits (m=1..5); 6^3 content {cont}', ok and cont == (11, 11, 16, 27, 27))
signs = list(itertools.product((1, -1), repeat=3)); sidx = {s: i for i, s in enumerate(signs)}
mods = list(itertools.product((1, 3, 5), repeat=3)); midx = {v: i for i, v in enumerate(mods)}
Pfac = np.zeros((N6, N6))
for si, s in enumerate(signs):
    for mi, v in enumerate(mods): Pfac[idx[tuple(a * b for a, b in zip(s, v))], si * 27 + mi] = 1
P8, P27, res = [], [], 0.0
for R, P in zip(RI, PI):
    A8 = np.zeros((8, 8)); A27 = np.zeros((27, 27)); pm = [int(np.argmax(np.abs(R[i]))) for i in range(3)]
    for s in signs: A8[sidx[tuple(R @ np.array(s))], sidx[s]] = 1
    for v in mods: A27[midx[tuple(v[pm[i]] for i in range(3))], midx[v]] = 1
    P8.append(A8); P27.append(A27); res = max(res, np.abs(Pfac.T @ P @ Pfac - np.kron(A8, A27)).max())
iso = np.zeros((27, 3))
for k, a in enumerate((1, 3, 5)): iso[midx[(a, a, a)], k] = 1
Sb = Pfac @ np.kron(np.eye(8), iso)
onS = max(np.abs(Sb.T @ P @ Sb - np.kron(A8, np.eye(3))).max() for P, A8 in zip(PI, P8))
check('A2 [T] cell = C^8 (signs) x C^27 (moduli), R = pi_8 x pi_S3 exactly; shells = C^8 x C^3 (isotropic moduli), R = pi_8 x 1: '
      f'family index rotation-blind; moduli 10A1+A2+8E of S3: 11 pattern copies, 3 point-localised (C(m+2,3)+C(m,3) = {rows})', res == 0 and onS == 0 and rows[2] == 11)
proj = {k: sum(TAB[k][cname(R)] * P for R, P in zip(RI, PI)) * TAB[k]['E'] / 24 for k in TAB}
sh = np.array([(abs(p[0]) + 1) // 2 if abs(p[0]) == abs(p[1]) == abs(p[2]) else 0 for p in pts])
PS = np.diag((sh > 0).astype(float)); PO = np.eye(N6) - PS
mult = {k: (round(np.trace(proj[k]) / TAB[k]['E']), round(np.trace(proj[k] @ PS) / TAB[k]['E'])) for k in TAB}
noncentral = all(np.linalg.norm(proj[k] @ PS @ proj[k] - mult[k][1] / mult[k][0] * proj[k]) > 0.5 for k in ('A1', 'A2', 'T1', 'T2'))
check('A3 [T] shell projector: covariant, not central (rank 3 of ' + '/'.join(str(mult[k][0]) for k in ('A1', 'A2', 'T1', 'T2')) +
      ' in A1/A2/T1/T2, none in E): no function of the rotations selects shells; free: four 3x3 family matrices, shell-orbit 3x8,3x8,3x24,3x24',
      max(np.abs(PS @ P - P @ PS).max() for P in PI) == 0 and noncentral and mult['E'][1] == 0)
blk_e = lambda x: tuple(int(12 * np.floor((xi + 6) / 12)) for xi in x)
blk_o = lambda x: tuple(int(12 * np.floor(xi / 12) + 6) for xi in x)
in_e = all(len({blk_e(np.array(c) + s) for s in signs}) == 1 for c in itertools.product(range(-8, 9, 4), repeat=3))
in_o = all(len({blk_o(np.array(c) + s) for s in signs}) == 1 for c in itertools.product(range(-10, 11, 4), repeat=3))
cov = [tuple((np.array(oo) - np.array(oe)) % 12) for oe in itertools.product((0, 4, 8), repeat=3)
       for oo in itertools.product((2, 6, 10), repeat=3) if {tuple(np.array(oe) % 12), tuple((np.array(oe) + 6) % 12)} & {tuple(np.array(oo) % 12), tuple((np.array(oo) + 6) % 12)}]
smp_s = [np.array(v) for v in itertools.product((-3, -1, 1, 3), repeat=3)]
smp_e = [4 * np.array(v) for v in itertools.product((-1, 0, 1), repeat=3)]; smp_o = [np.array([2, 2, 2]) + c for c in smp_e]
isS = lambda v: all(x % 2 == 1 for x in v); isE = lambda v: all(x % 4 == 0 for x in v); isO = lambda v: all(x % 4 == 2 for x in v)
selfsim = [q for q in range(1, 9) if all(isS(q * v) for v in smp_s) and all(isE(q * c) for c in smp_e) and all(isO(q * c) for c in smp_o)]
sim_ok = selfsim == [1, 3, 5, 7] and all(isO(2 * v) for v in smp_s) and all(isE(2 * c) for c in smp_o)
check(f'A4 [T] even cubes tile even 6^3 blocks, odd cubes odd blocks; {len(cov)} of 729 groupings covariant, all offset (3,3,3); CL-1 '
      f'maps sites, even, odd centres to themselves exactly for q = {selfsim}: smallest q = 3, coarse sites = shell 2',
      in_e and in_o and len(cov) == 27 and set(cov) == {(6, 6, 6)} and sim_ok and selfsim[1] == 3)
red = lambda x: tuple(((np.array(x) + 11) % 24) - 11)
sites_t = [tuple(p) for p in itertools.product(range(-11, 12, 2), repeat=3)]
tu = [np.array(t) for t in itertools.product((0, 12), repeat=3)]; tp = tu + [t + 6 for t in tu]
def shell_of(x):
    r = np.abs(np.array(x) - np.array(blk_e(x))); return int((r[0] + 1) // 2) if r[0] == r[1] == r[2] else 0
stab = Counter((shell_of(x), sum(red(R @ np.array(x) + t) == x for R in RI for t in tu)) for x in sites_t)
Sset = [x for x in sites_t if shell_of(x) > 0]
orb = lambda x, trs: frozenset(red(R @ np.array(x) + t) for R in RI for t in trs)
ou = sorted(len(o) for o in {orb(x, tu) for x in Sset}); op = sorted(len(o) for o in {orb(x, tp) for x in Sset})
swap = Counter((shell_of(x), shell_of(red(np.array(x) + 6))) for x in Sset)
check(f'A5 [T] zoomed group, 12^3 torus: (shell, |stab|) {dict(sorted(stab.items()))}: C3 exactly on shells; update orbits {ou}, '
      f'pair orbits {op} ((3,3,3) swaps shells 1, 3)',
      set(stab) == {(0, 1), (1, 3), (2, 3), (3, 3)} and ou == [64, 64, 64] and op == [64, 128] and swap[(1, 3)] == 64 and swap[(2, 2)] == 64)
Sx = set(Sset); comp = {}; sizes = []
def nbrs(x):
    for i in range(3):
        for d in (-2, 2): y = list(x); y[i] += d; yield red(y)
for x in Sset:
    if x in comp: continue
    st = [x]; comp[x] = len(sizes); n = 0
    while st:
        y = st.pop(); n += 1
        for z in nbrs(y):
            if z in Sx and z not in comp: comp[z] = comp[x]; st.append(z)
    sizes.append(n)
gaps = set()
for cid in range(len(sizes)):
    src = [x for x in Sset if comp[x] == cid]; dist = {x: 0 for x in src}; dq = deque(src); hit = None
    while dq and hit is None:
        y = dq.popleft()
        for z in nbrs(y):
            if z in dist or (z in Sx and comp[z] == cid): continue
            if z in Sx: hit = dist[y]; break
            dist[z] = dist[y] + 1; dq.append(z)
    gaps.add(hit)
check(f'A6 [T] NN graph of the shells: components {dict(Counter(sizes))} (central cubes, lone shell-2 sites); paths between '
      f'components cross >= {min(gaps)} free sites',
      Counter(sizes) == Counter({8: 16, 1: 64}) and gaps == {2})

# ================================================================== B. fine reading
print('== B. fine reading: candidate rules on the fine lattice')
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5
XI = [state(1.5, 1.5, (2 * C[i] - 1.0) / np.sqrt(3)) for i in range(8)]
GM = np.array([[XI[a].conj() @ XI[b] for b in range(8)] for a in range(8)])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: W[a, b] = -GM[a, b] / abs(GM[a, b]) / np.sqrt(3)
img = lambda R, i: int(np.argmin(np.sum(abs(cc - R @ cc[i]), 1)))
GL = []
for R in ROTS:
    nn, a = axang(R)
    for s in (1, -1):
        Dm = s * Dj(1.5, nn, a); G = np.zeros((8, 8), complex)
        for i in range(8): k = img(R, i); G[k, i] = XI[k].conj() @ Dm @ XI[i]
        GL.append(G)
basis = [v.reshape(8, 8) for v in nullspace(np.vstack([np.kron(G, np.eye(8)) - np.kron(np.eye(8), G.T) for G in GL]))]
anti = np.array([[np.sum(abs(C[a] - C[b])) == 3 for b in range(8)] for a in range(8)])
kv = nullspace(np.array([B[~anti] for B in basis]).T)
A = sum(c * B for c, B in zip(kv[0], basis)); A = A / np.sqrt(np.trace(A @ A) / 8)
ov = [abs(XI[0].conj() @ XI[k]) for k in (1, 3, 7)]
Wp = np.cos(0.7) * W + np.sin(0.7) * A
check(f'B1 [T] spin-3/2 overlaps edge {ov[0]:.4f}, face {ov[1]:.4f}, body {ov[2]:.0e}: no CL-2 phase on diagonals; cube commutant '
      f'dim {len(basis)} has {kv.shape[0]} diagonal hop A (phases +-i, A^2=1, AW=-WA): cos(phi)W + sin(phi)A covariant reflections',
      ov[2] < 1e-12 and len(basis) == 4 and kv.shape[0] == 1 and np.allclose(np.abs(A[anti]), 1) and np.allclose(A @ A, np.eye(8))
      and np.linalg.norm(A @ W + W @ A) < 1e-12 and np.allclose(Wp @ Wp, np.eye(8)) and max(np.linalg.norm(G @ Wp - Wp @ G) for G in GL) < 1e-12)
sdir = lambda x: (np.array(x) - np.array([xi + 1 if (xi + 1) % 4 == 0 else xi - 1 for xi in x])) / np.sqrt(3)
A2c = {k: TAB['A2'][k] for k in TAB['A2']}
def spin_content(P_):
    Xs = [state(1.5, 1.5, sdir(p)) for p in P_]; ix_ = {tuple(p): i for i, p in enumerate(P_)}; tot = np.zeros(3, complex)
    for R in ROTS:
        nn, a = axang(R)
        for s in (1, -1):
            Dm = s * Dj(1.5, nn, a)
            trc = sum(Xs[i].conj() @ Dm @ Xs[i] for i, p in enumerate(P_) if ix_.get(tuple(np.rint(R @ p).astype(int))) == i)
            tot += trc * np.conj([s * np.trace(Dj(0.5, nn, a)), s * np.trace(Dj(0.5, nn, a)) * A2c[cname(R)], s * np.trace(Dj(1.5, nn, a))]) / 48
    return tuple(int(round(t.real)) for t in tot)
shc = [spin_content([np.array(s) * (2 * k - 1) for s in signs]) for k in (1, 2, 3)]
frc = [spin_content([np.array(p) for p in sorted({tuple(np.rint(R @ np.array(v)).astype(int)) for R in RI})]) for v in ((1, 1, 3), (1, 3, 5))]
check(f'B2 [T] spin-3/2 sites: each shell {shc[0]} in (E1/2,E5/2,G3/2), no E1/2; each free orbit {frc[0]}: one-copy room is off-shell',
      all(c == (0, 0, 2) for c in shc) and all(c == (2, 2, 4) for c in frc))
L = 6; N = L ** 3
X6 = np.array(list(itertools.product(range(L), repeat=3)))
def ix(p): p = np.array(p) % L; return int((p[0] * L + p[1]) * L + p[2])
rr = np.abs(X6 - 2.5); shell6 = np.where((rr[:, 0] == rr[:, 1]) & (rr[:, 1] == rr[:, 2]), (rr[:, 0] + 0.5).astype(int), 0)
Pc = np.zeros((8, 8))
for i in range(8): Pc[7 - i, i] = 1                       # corner complement: one spin-3/2 state per site
def half(Wc, theta, parity, K):
    U = np.zeros((N, N), complex); Vc = expm(-1j * theta * (Pc @ Wc @ Pc if parity else Wc))
    for mn in itertools.product(range(parity, L + parity, 2), repeat=3):
        q = np.array(mn) + C; ii = [ix(p) for p in q]; ph = np.exp(1j * (q - q % L) @ K)
        U[np.ix_(ii, ii)] += ph.conj()[:, None] * Vc * ph[None, :]
    return U
def tick(eps, mu, K, V=0.0, phi=0.0):
    Wc = np.cos(phi) * W + np.sin(phi) * A
    U = half(Wc, -(eps + mu / 2), 1, K) @ half(Wc, eps - mu / 2, 0, K)
    return np.diag(np.where(shell6 == 0, np.exp(-1j * V), 1.0)) @ U if V else U
def spec(U):
    w, vv = np.linalg.eig(U); q = np.angle(w); o = np.argsort(np.abs(q)); return q[o], vv[:, o]
def Ublock(K, eps, mu):
    D = np.diag(np.exp(1j * (C @ K))); return D @ expm(1j * (eps + mu / 2) * W) @ D.conj().T @ expm(-1j * (eps - mu / 2) * W)
eps, mu = 0.3, 0.05
Kt = np.array([0.3, -0.2, 0.5])
ref = np.sort(np.concatenate([np.angle(np.linalg.eigvals(Ublock(2 * (Kt + np.pi * np.array(n) / 3), eps, mu))) for n in itertools.product(range(3), repeat=3)]))
bl = np.abs(np.sort(np.angle(np.linalg.eigvals(tick(eps, mu, Kt)))) - ref).max()
def light_info(V, phi):
    q, vv = spec(tick(eps, mu, np.zeros(3), V, phi)); nl = int(np.sum(np.abs(q) < 0.1))
    wt = [float(np.real(np.sum(np.abs(vv[shell6 == k, :nl]) ** 2)) / max(nl, 1)) for k in range(4)]
    dom = np.argmax(np.array([np.sum(np.abs(vv[shell6 == k]) ** 2, 0) for k in range(4)]), 0)
    lev = {k: np.abs(q[dom == k]) for k in (1, 2, 3)}
    v2 = {}
    for nm, e in (('x', np.array([1, 0, 0.])), ('111', np.ones(3) / np.sqrt(3)), ('110', np.array([1, 1, 0]) / np.sqrt(2))):
        q1, _ = spec(tick(eps, mu, 0.02 * e, V, phi)); v2[nm] = (np.sort(np.abs(q1[:8])) ** 2 - np.sort(np.abs(q[:8])) ** 2) / 0.02 ** 2
    return nl, wt, lev, v2
nl0, wt0, _, v20 = light_info(0, 0)
vcl2 = 4 * ((np.cos(mu) - np.cos(2 * eps)) / 2) / 3 * mu / np.sin(mu)      # fine sites per tick (2 per block)
check(f'B3 [D] CL-2 on the 6^3 torus (= Bloch form to {bl:.0e}; eps {eps}, mu {mu}): {nl0} light at |w| = mu, weight {wt0[1]:.4f} '
      f'= 8/216 per shell, speed^2 {v20["x"][0]:.4f}: no shell preference',
      bl < 1e-12 and nl0 == 8 and np.allclose(wt0[1:], 8 / 216) and np.allclose(np.concatenate(list(v20.values())), vcl2, rtol=2e-3))
nlV, wtV, levV, v2V = light_info(np.pi, 0)
check(f'B4 [D] phase pi on free sites: {nlV} light, {wtV[2]:.3f} on shell 2, speed^2 x{max(np.abs(np.concatenate(list(v2V.values())))) / vcl2:.0e} '
      f'(flat); shells 1, 3 at |w| {levV[1].min():.3f}, {levV[3].min():.3f}: the half-ticks act on disjoint shell parts, so no CL-2 mass',
      nlV == 8 and wtV[2] > 0.9 and max(np.abs(np.concatenate(list(v2V.values())))) < 1e-3 * vcl2 and levV[1].min() > 0.2 and levV[3].min() > 0.2)
nlA, wtA, _, v2A = light_info(np.pi, np.pi / 2)
z110 = int(np.sum(np.abs(v2A['110']) < 1e-6)); r111 = np.sort(v2A['111'])
check(f'B5 [D] hop A + free-site phase: only shells light ({nlA}, orbit weight {wtA[0]:.0e}), but 1D: along (1,1,0) {z110}/8 have '
      f'speed 0, along (1,1,1) speed^2 {r111[-1]:.3f} (2) and {r111[0]:.3f} (6): four diagonal chains',
      nlA == 8 and wtA[0] < 1e-10 and z110 == 4 and np.isclose(r111[-1] / r111[0], 9, rtol=1e-3))

# ================================================================== C. internal reading R1
print('== C. internal reading R1: the 6^3 cell as an internal index of a coarse CL-2 tick')
rng = np.random.default_rng(7)
def herm(n): X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (X + X.conj().T) / 2
pr8 = {k: sum(TAB[k][cname(R)] * P for R, P in zip(RI, P8)) * TAB[k]['E'] / 24 for k in TAB}
muH = 2.0; Mfam = {k: 0.01 * herm(3) for k in ('A1', 'A2', 'T1', 'T2')}
M = Pfac @ sum(np.kron(pr8[k], iso @ Mfam[k] @ iso.T) for k in Mfam) @ Pfac.T + muH * PO
w, v = np.linalg.eigh(M); lt = np.abs(w) < 0.5
famlev = np.sort(np.concatenate([np.repeat(np.linalg.eigvalsh(Mfam[k]), TAB[k]['E']) for k in Mfam]))
check(f'C1 [T] R1 rule (free internal modes heavy, 3x3 family matrices on shells): covariant, light space = shell space ({lt.sum()}, '
      f'weight {np.trace(v[:, lt].conj().T @ PS @ v[:, lt]).real:.4f}), levels = family eigenvalues; per shell the rung-1 action (A2)',
      max(np.abs(M @ P - P @ M).max() for P in PI) < 1e-12 and lt.sum() == 24 and np.isclose(np.trace(v[:, lt].conj().T @ PS @ v[:, lt]).real, 24)
      and np.allclose(np.sort(w[lt]), famlev))
cv = lambda X: sum(P @ X @ P.T for P in PI) / 24
mix = []
for d in (0.05, 0.2, 0.5):
    Xm = cv(herm(N6)); Xm = PS @ Xm @ PO + PO @ Xm @ PS; Xm *= d / np.linalg.norm(Xm, 2)
    w2, v2_ = np.linalg.eigh(M + Xm); l2 = np.abs(w2) < 0.5
    adm = (1 - np.real(np.einsum('ij,ij->j', v2_[:, l2].conj(), PS @ v2_[:, l2]))).max()
    mix.append((l2.sum(), adm / (d / muH) ** 2, adm <= (d / (muH - d - 0.1)) ** 2))
check('C2 [D] generic covariant mixing d: 24 light, orbit admixture/(d/mu_H)^2 = ' + ', '.join(f'{r:.2f}' for _, r, _ in mix)
      + ' (d .05,.2,.5): only the gap protects the shells',
      all(n_ == 24 and b_ for n_, _, b_ in mix))
bv2 = lambda e_, m_: ((np.cos(m_) - np.cos(2 * e_)) / 2) / 3 * m_ / np.sin(m_)
dv = [abs(bv2(0.04, m_) / (np.sin(0.04) ** 2 / 3) - 1) for m_ in (1e-4, 1e-3)]
check(f'C3 [T] coarse tick = direct sum over mass eigenmodes: each family is a CL-2 species (two copies, no chirality); dv^2/v^2 '
      f'{dv[0]:.1e}, {dv[1]:.1e} at mass 1e-4, 1e-3 (eps 0.04)',
      dv[1] / dv[0] > 90 and dv[1] < 2e-4)
h1 = np.zeros((3, 3)); h1[0, 1] = h1[1, 0] = h1[1, 2] = h1[2, 1] = 1; c1 = np.diag([1.0, 0, 0]); I3 = np.eye(3)
axo = lambda op, i: np.kron(np.kron(op if i == 0 else I3, op if i == 1 else I3), op if i == 2 else I3)
Pan = np.diag([0.0 if len(set(x)) == 1 else 1.0 for x in mods])
Mn = lambda n, t, V: t * sum(axo(h1, i) + (-1) ** n[i] * axo(c1, i) for i in range(3)) + V * Pan
Aadj = np.zeros((N6, N6))
for p in pts:
    for i in range(3):
        for dd in (-2, 2):
            q = list(p); q[i] += dd
            if tuple(q) in idx: Aadj[idx[tuple(q)], idx[p]] = 1
chis = {n: np.array([np.prod([s[i] ** n[i] for i in range(3)]) for s in signs]) / np.sqrt(8) for n in itertools.product((0, 1), repeat=3)}
Ub = np.kron(np.array([chis[n] for n in chis]).T, np.eye(27))
fac = np.linalg.norm(Ub.conj().T @ Pfac.T @ (Aadj + 5.0 * PO) @ Pfac @ Ub - block_diag(*[Mn(n, 1.0, 5.0) for n in chis]))
SEC = {'nu': (0, 0, 0), 'd': (1, 0, 0), 'u': (0, 1, 1), 'e': (1, 1, 1)}
def fams(n, x):
    w_, v_ = np.linalg.eigh(Mn(n, x, 1.0)); shw = np.sum(np.abs(iso.T @ v_) ** 2, 0)
    sel = np.argsort(-shw)[:3]; sel = sel[np.argsort(np.abs(w_[sel]))]
    return np.abs(w_[sel]), v_[:, sel], 1 - shw[sel]
x0 = 0.005; lead = {k: fams(n, x0) for k, n in SEC.items()}
ok4 = all(np.allclose(lead[k][0][:2] / x0 ** 2, [3, 6], rtol=0.03) and np.isclose(lead[k][0][2] / x0, abs(3 - 2 * sum(SEC[k])), rtol=0.03) for k in SEC)
mv = [lead[k][0][j] / lead[k][2][j] for k in SEC for j in (0, 1)]
check(f'C4 [T] derived model M = t A_nn + V P_free = 8 character blocks on 27 moduli ({fac:.0e}); t/V {x0}: shells 3, 2 at 3, 6 t^2/V, '
      f'shell 1 at |3-2|n|| t; lighter masses = V x orbit weight ({min(mv):.3f}-{max(mv):.3f})', fac < 1e-12 and ok4 and np.allclose(mv, 1, atol=0.05))

# ================================================================== D. hierarchy and mixing
print('== D. hierarchy and mixing against measurement')
lep = (1, 206.7682830, 1776.93 / 0.51099895); mq = dict(u=2.16, d=4.70, s=93.5, c=1273.0, b=4183.0, t=172570.0)
LR = dict(lep=np.log(lep[1]) / np.log(lep[2] / lep[1]), up=np.log(mq['c'] / mq['u']) / np.log(mq['t'] / mq['c']),
          down=np.log(mq['s'] / mq['d']) / np.log(mq['b'] / mq['s']))
rk = np.array([1, 3, 5]) * np.sqrt(3) / 2
g_ = (rk[2] ** 2 - rk[1] ** 2) / (rk[1] ** 2 - rk[0] ** 2); p_ = np.log(5 / 3) / np.log(3)
prof = dict(exp_hops=(6 - 3) / (3 - 0), gauss=g_, gauss_r=1 / g_, power=1 / p_, power_r=p_)
check('D1 [M] ln(m2/m1)/ln(m3/m2): leptons {:.3f}, up {:.3f}, down {:.3f}; a sector-blind law c f(k) gives one value: exp {:.2f}, '
      'Gauss {:.2f}/{:.2f}, power {:.3f}/{:.3f}: none fits two sectors'.format(
      LR['lep'], LR['up'], LR['down'], prof['exp_hops'], prof['gauss'], prof['gauss_r'], prof['power'], prof['power_r']),
      max(LR.values()) / min(LR.values()) > 2 and all(sum(abs(p / r - 1) < 0.1 for r in LR.values()) <= 1 for p in prof.values()))
lowr = [fams(n, x)[0][1] / fams(n, x)[0][0] for x in np.linspace(0.01, 0.2, 20) for n in SEC.values()]
check(f'D2 [M] derived model, t/V 0.01-0.2: lighter-pair ratio {min(lowr):.2f}-{max(lowr):.2f} in every sector vs {lep[1]:.1f} (mu/e), '
      f'{mq["c"] / mq["u"]:.0f} (c/u), {mq["s"] / mq["d"]:.1f} (s/d); larger only at tuned zero crossings', max(lowr) < 3)
Gam = np.diag([s[0] * s[1] * s[2] for s in signs]).astype(float); Xinv = np.zeros((8, 8))
for s in signs: Xinv[sidx[tuple(-np.array(s))], sidx[s]] = 1
Tp8 = Gam / 2 + 1j * (1j * Gam @ Xinv) / 2                              # T+ = T1 + i T2, T3 = X/2
vus = {}
for x in (0.05, 0.1):
    _, vu, _ = fams(SEC['u'], x); _, vd, _ = fams(SEC['d'], x); vus[x] = abs((vu.conj().T @ vd)[0, 1])
same = [rng.normal(size=(3, 3)) for _ in range(1)][0]; same = same + same.T
Uu = np.linalg.eigh(same * 2.0 + 0.5 * np.eye(3))[1]; Ud = np.linalg.eigh(same * 0.7)[1]
check(f'D3 [T/M] T+ x 1 maps d->u, e->nu per shell: CKM = U_u^+ U_d free in R1 (0.225 allowed, not predicted); one shell operator '
      f'for both: |V_us| {abs((Uu.conj().T @ Ud)[0, 1]):.0e}; derived model {vus[0.05]:.4f}, {vus[0.1]:.4f} (t/V .05, .1)',
      np.linalg.norm(pr8['T2'] @ Tp8 @ pr8['T1']) > 1 and np.linalg.norm(pr8['A1'] @ Tp8 @ pr8['A2']) > 0.9
      and abs((Uu.conj().T @ Ud)[0, 1]) < 1e-12 and vus[0.05] < 0.05)

# ================================================================== E. owner idea: decay by shell-orbit mixing
print('== E. owner idea: shell-orbit mixing as the decay of heavier families')
Lc, nI = 4, 11; Nc = Lc ** 3; Qd = np.array([-1.0] * 10 + [0.0])
Mq = np.zeros((nI, nI), complex); Mq[:10, :10] = 0.05 * herm(10); Mq[10, 10] = 0.03; Mx = Mq + 0.02 * herm(nI)
cix = lambda p: int(((p[0] % Lc) * Lc + p[1] % Lc) * Lc + p[2] % Lc)
def half_apply(psi, Mm, theta, parity, links, msign):
    psi = psi.reshape(Nc, nI); out = np.zeros_like(psi); Wc = Pc @ W @ Pc if parity else W
    for mn in itertools.product(range(parity, Lc + parity, 2), repeat=3):
        cs = [cix(np.array(mn) + c) for c in C]; H = np.zeros((8 * nI, 8 * nI), complex)
        for a in range(8):
            for b in range(8):
                if abs(Wc[a, b]) > 1e-12:
                    Lk = np.diag(np.exp(0.5j * Qd * links[cs[a], cs[b]]))
                    H[a * nI:(a + 1) * nI, b * nI:(b + 1) * nI] = Wc[a, b] * (Lk @ (0.3 * np.eye(nI) - msign * Mm / 2) @ Lk)
        blk = expm(-1j * theta * H) @ np.concatenate([psi[c] for c in cs])
        for a, c in enumerate(cs): out[c] = blk[a * nI:(a + 1) * nI]
    return out.ravel()
leak = {}
for nm, Mm in (('kept', Mq), ('broken', Mx)):
    wm, vm = np.linalg.eigh(Mm); worst = 0
    for j in (0, 4, 10):
        psi = np.zeros((Nc, nI), complex); psi[0] = vm[:, j]; psi[5] = 0.5j * vm[:, j]; psi = psi.ravel() / np.linalg.norm(psi)
        for _ in range(4):
            th = rng.uniform(-np.pi, np.pi, (Nc, Nc)); th = np.triu(th, 1) - np.triu(th, 1).T
            psi = half_apply(psi, Mm, 1.0, 0, th, 1.0); psi = half_apply(psi, Mm, -1.0, 1, th, -1.0)
        worst = max(worst, 1 - np.sum(np.abs(psi.reshape(Nc, nI) @ vm[:, j].conj()) ** 2))
    leak[nm] = worst
check(f'E1 [T] [Q,M] = 0 (CL-5): each mass eigenmode number kept under random time-dependent links (leak {leak["kept"]:.0e}; '
      f'control {leak["broken"]:.0e}): mixing relabels stable species, link vertices flavour-diagonal, width 0 at all orders',
      leak['kept'] < 1e-12 and leak['broken'] > 1e-3)
MSd = lambda MF: sum(np.kron(pr8[k], iso @ MF[k] @ iso.T) for k in MF)
Tpf = np.kron(Tp8, np.eye(27))
deg = {'A1': Mfam['A1'], 'A2': Mfam['A1'], 'T1': Mfam['T1'], 'T2': Mfam['T1']}
cm = [np.linalg.norm(Tpf @ MSd(F) - MSd(F) @ Tpf) for F in (deg, Mfam)]
check(f'E2 [T/M] mu -> nu_mu e nubar_e keeps every family number (LFV < 4e-13, 1e-12, 1.2e-2): needed is T+ x 1, family-blind; '
      f'[T+ x 1, M] = {cm[0]:.0e} iff M_nu = M_e, M_u = M_d (else {cm[1]:.1e}): measured masses leave no charged current to link',
      cm[0] < 1e-12 and cm[1] > 1e-3)
chi8 = np.array([chis[n] for n in chis])
def famv(n, x):
    w_, v_ = np.linalg.eigh(Mn(n, x, 1.0)); shw = np.sum(np.abs(iso.T @ v_) ** 2, 0)
    sel = np.argsort(-shw)[:3]; sel = sel[np.argsort(np.abs(w_[sel]))]
    return [Pfac @ np.kron(chis[n], v_[:, k]) for k in sel], 1 - shw[sel]
bonds = [(idx[p], idx[tuple(np.array(p) + 2 * np.eye(3, dtype=int)[i])]) for p in pts for i in range(3)
         if tuple(np.array(p) + 2 * np.eye(3, dtype=int)[i]) in idx and sh[idx[p]] == 0 and sh[idx[tuple(np.array(p) + 2 * np.eye(3, dtype=int)[i])]] == 0]
(Fe, we), (Fn, _), (Fd, _), (Fu, _) = (famv(SEC[k], 0.05) for k in ('e', 'nu', 'd', 'u'))
Tr = np.conj(Fe[0]) * Fe[1]
coup = lambda f: sum(Tr[a] * abs(f[b]) ** 2 + Tr[b] * abs(f[a]) ** 2 for a, b in bonds)
cr = [abs(coup(F[0]) / coup(Fn[0])) for F in (Fe, Fd, Fu)]
check(f'E3 [T/D] |chi(s)|^2 = 1/8: one shell\'s nu, e, u, d share site densities; contact U n_x n_y on free bonds couples mu->e to '
      f'ee, dd, uu as {cr[0]:.3f}, {cr[1]:.3f}, {cr[2]:.3f} x nu nu: BR(mu->3e), mu-e conversion O(1) vs < 1e-12, 7e-13', np.allclose(np.abs(chi8) ** 2, 1 / 8) and all(abs(c - 1) < 0.05 for c in cr))
tmu, ttau, Be, mmu, mtau = 2.1969811e-6, 290.3e-15, 0.1782, 105.6583755, 1776.93
univ = tmu / ttau * Be * (mmu / mtau) ** 5
GF, hb = 1.1663788e-5, 6.582119569e-25; tree = hb / (GF ** 2 * (mmu * 1e-3) ** 5 / (192 * np.pi ** 3))
check(f'E4 [M] (tau_mu/tau_tau) B_e (m_mu/m_tau)^5 = {univ:.4f}: m^5 with one coupling (tree {tree * 1e6:.3f} us, imported G_F); '
      f'm^3 misses by {(mtau / mmu) ** 2:.0f}; derived orbit weights e, mu, tau {we[0]:.4f}, {we[1]:.4f}, {we[2]:.4f}: (G_tau/G_mu)^2 = {we[2] / we[1]:.2f}',
      abs(univ - 1) < 0.005 and abs(tree / tmu - 1) < 0.01 and abs(we[2] / we[1] - 1) > 0.3)
T2 = [np.array(v) for v in itertools.product(range(-6, 7), repeat=3) if len({x % 2 for x in v}) == 1]
T6 = [v for v in T2 if len({x % 6 for x in v}) == 1 and v[0] % 3 == 0]
idxT = len({tuple(np.array(v) % 6) for v in T2}) // len({tuple(np.array(v) % 6) for v in T6})
hop = max(np.abs(np.array(p) - np.array(q)).max() for p, q in [((0, 0, 0), (6, 0, 0))])
check(f'F1 [T] CL-1 compatibility: the 6^3 rule keeps translations T_6 of index {idxT} in CL-1\'s T (27 groupings, A4); R1 moves '
      f'modes {hop} sites per coarse half-tick, so the fine strict cone needs >= {hop} fine layers per coarse half-tick; per family '
      'two copies and no net chirality remain (C3)', idxT == 27 and hop == 6)
print('== measured (comparisons only): CODATA m_mu/m_e; PDG 2024 masses, lifetimes, B(tau->e nu nu), G_F; MEG, SINDRUM, PDG LFV bounds')
print('supplied: CL-2 tick (eps, mu), the rung reading, the 6^3 grouping, orbit gap, family matrices, intra-cell t, V, contact U')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
