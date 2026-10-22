#!/usr/bin/env python3
"""family-register: which structure carries the family index of the chiral generator H' = (i/2)[W_o, W_e] with the
mirror's own four-mode term O_A (twist k = 2), and how many families it leaves light.

Model (supplied): CL-1 cube objects (one fermion mode per site, spin-3/2 edge hop W, face-diagonal hop F, copies
s3 = -eps F: A = q1 = mirror, B = q2 = light), H' and its windows Gamma, R; a register X of family copies, each
carrying one H' family, on which the cube's turns act by permuting X (geometric action L_g (x) P_g).
Sections: A register fixed points and the exact mirror anomaly; B turn-invariant Dirac masses on a register (3D cube);
C 1+1D K-matrix toy (3-4-5-0 tastes) with the permuting turn; D which three, masses, mixing; E measurement.
Cited, not rederived: 't Hooft anomaly matching, Haldane's null-vector criterion, the SMG sufficiency conjecture,
families-mod-3 (C1-C2 per-family anomaly of S, the V4 and D8 toy Lagrangians), chiral-step (H', PW),
six-cube-families (A4: odd zooms map CL-1 to itself). The site stabiliser (three-families A1) is rederived in A2.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/ONE_THREE_FOLD_TURN_FIXES_THREE_REGISTER_COPIES_AS_PROTECTED_FAMILIES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, null_space
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
rng = np.random.default_rng(20261022)

# ------------------------------------------------ cube objects (as in families-mod-3 / chiral-step) ------------------------------------------------
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5; I8 = np.eye(8)
EPS = np.diag((-1.0) ** C.sum(1)).astype(complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(d2, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if round(float(np.sum((C[a] - C[b]) ** 2))) == d2: g = XI[a].conj() @ XI[b]; H[a, b] = sign * g / abs(g) / np.sqrt(3)
    return H
W = hop(1, -1.0); F = hop(2, 1.0)
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def img(R, i): return int(np.argmin(np.sum(abs(cc - R @ cc[i]), 1)))
def Lrot(R):
    n_, a = axang(R); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
Ls = [Lrot(R) for R in rots]
TI = [i for i, L in enumerate(Ls) if abs(np.trace(L @ EPS @ L.conj().T @ EPS).real / 8 - 1) < 1e-9]     # 12 tetrahedral turns
R3 = [rots[i] for i in TI if abs(np.trace(rots[i])) < 1e-9 and np.allclose(axang(rots[i])[0], np.ones(3) / np.sqrt(3))][0]
C3I = [i for i in TI if any(np.allclose(rots[i], np.linalg.matrix_power(R3, k)) for k in range(3))]
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Hp(K): D = Dg(K); Wo = D.conj().T @ W @ D; return 0.5j * (Wo @ W - W @ Wo)
AL = [(Hp(1e-6 * np.eye(3)[a]) - Hp(-1e-6 * np.eye(3)[a])) / 2e-6 for a in range(3)]
s3 = -EPS @ F; PA, PB = (I8 + s3) / 2, (I8 - s3) / 2
Pi = np.zeros((8, 8))
for i in range(8): Pi[int((1 - C[i]) @ [4, 2, 1]), i] = 1
php = {0: 1.0 + 0j}
while len(php) < 8:
    for a in list(php):
        for b in range(8):
            if b not in php and abs(W[a, b]) > 0:
                ia, ib = int(np.argmax(Pi[:, a])), int(np.argmax(Pi[:, b])); php[b] = np.conj(W[ia, ib] / (php[a] * W[a, b]))
Pinv = Pi @ np.diag([php[i] for i in range(8)]); PW = Pinv @ W
qa, qb = 2, 1                                   # copy charges of the light (B) and mirror (A) copies (families-mod-3 A2, B1)

# ===================================== A. registers and the mirror anomaly =====================================
print('== A. register fixed points and the exact mirror anomaly')
def axp(R): return [int(np.argmax(np.abs(R[i]))) for i in range(3)]
def regs():
    out = {'rung-1 cell': ([(0,)], lambda R, p: p, lambda p: p, TI)}
    for m in (1, 2, 3, 4):
        v = list(range(-(m - 1), m, 2)); out[f'pos m={m}'] = ([tuple(p) for p in itertools.product(v, repeat=3)],
            lambda R, p: tuple(int(x) for x in np.rint(R @ np.array(p))), lambda p: tuple(-x for x in p), TI)
    for m in (2, 3):
        v = list(range(1, 2 * m, 2)); out[f'mod m={m}'] = ([tuple(p) for p in itertools.product(v, repeat=3)],
            lambda R, p: tuple(p[j] for j in axp(R)), lambda p: p, TI)
    out['axes'] = ([(0,), (1,), (2,)], lambda R, p: (axp(R).index(p[0]),), lambda p: p, TI)
    dg = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
    out['diagonals'] = (dg, lambda R, p: (lambda q: q if q in dg else tuple(-x for x in q))(tuple(int(x) for x in np.rint(R @ np.array(p)))), lambda p: p, TI)
    out['tilings'] = ([tuple(p) for p in itertools.product((0, 1), repeat=3)], lambda R, p: tuple(int(x) % 2 for x in np.rint(np.abs(R) @ np.array(p))), lambda p: p, C3I)
    out['shells'] = ([(1,), (3,), (5,)], lambda R, p: p, lambda p: p, TI)
    out['site block'] = ([tuple(p) for p in itertools.product((-1, 0, 1), repeat=3)], lambda R, p: tuple(int(x) for x in np.rint(R @ np.array(p))), lambda p: tuple(-x for x in p), C3I)
    return out
REG = regs()
def F3(pts, f): return sum(f(R3, p) == p for p in pts)
ok = True
for m in range(1, 10):
    for v in (list(range(-(m - 1), m, 2)), list(range(1, 2 * m, 2))):
        P_ = [tuple(p) for p in itertools.product(v, repeat=3)]; fx = sum(tuple(int(x) for x in R3 @ np.array(p)) == p for p in P_)
        ok &= fx == m and (m ** 3 - fx) % 3 == 0
ok2 = all(sum(np.allclose(R3 @ np.array(p), p) for p in itertools.product([x + 0.5 for x in range(-2 ** (n - 1), 2 ** (n - 1))], repeat=3)) == 2 ** n for n in range(1, 6))
check('A1 theorem: in a (2m)^3 cell one three-fold turn fixes m of the m^3 copies (sub-cubes or moduli) and moves the rest in '
      '(m^3-m)/3 three-cycles (m = 1..9); |X| = F3 mod 3 for every register; blocks of a factor-2 rung have F3 = 2^n, never 0 mod 3',
      ok and ok2, '6^3: 27 = 3 fixed + 8 three-cycles')
stab_ok, spine_ok = True, True
for x in itertools.product((0, 1), repeat=3):
    x = np.array(x); fe = np.ones(3, int) - x; bo = 2 * np.floor((x - 1) / 2).astype(int) + 1; fo = 2 * bo + 1 - x
    d = fe - x; spine_ok &= np.array_equal(fo - x, -d) and np.all(np.abs(d) == 1)
    S = np.diag(d); Rd = S @ R3 @ S
    blk = [x + np.array(p) for p in itertools.product((-1, 0, 1), repeat=3)]
    fixed = [tuple(p) for p in blk if np.array_equal(Rd @ (p - x) + x, p)]
    spine_ok &= sorted(fixed) == sorted([tuple(x - d), tuple(x), tuple(x + d)])
    def keeps(R, par):                                          # does the turn about x map the par-tiling to itself?
        b = 2 * np.floor((x - par) / 2).astype(int) + par; P_ = np.array([R @ (b + np.array(c) - x) + x for c in itertools.product((0, 1), repeat=3)])
        return bool(np.all((P_.min(0) - par) % 2 == 0))
    stab_ok &= sum(keeps(R.astype(int), 0) and keeps(R.astype(int), 1) for R in rots) == 3
check('A2 theorem: every site lies on one body diagonal d shared by its even and odd cube; the rotations about the site that keep '
      'both tilings are the three turns about d; in the site\'s 3^3 block they fix exactly the spine {x-d, x, x+d} (the site '
      'and the far corners of its two cubes) and move the other 24 in 8 three-cycles', stab_ok and spine_ok, 'all 8 site classes')
fx = {k: F3(v[0], v[1]) for k, v in REG.items()}
check('A3 fixed copies of one turn: axes 0, body diagonals 1, aligned tilings 2, shells 3, site block 3, 6^3 cell 3',
      (fx['axes'], fx['diagonals'], fx['tilings'], fx['shells'], fx['site block'], fx['pos m=3'], fx['mod m=3']) == (0, 1, 2, 3, 3, 3, 3))
def sectors(n, nf): f = (n - nf) // 3; return {0: nf + f, 1: f, 2: f}
def S_anom(n, nf, k):                                           # Z3_k x SU(2)_e^2 of S = {Gamma-b, R-a, R-b} over a register
    sec = sectors(n, nf); return -4 * sum(mult * (qa + k + t) for t, mult in sec.items())
ex = (S_anom(27, 3, 2), S_anom(3, 0, 2), S_anom(1, 1, 2), S_anom(3, 3, 2))
allr = all((S_anom(len(v[0]), fx[k], 2) % 3 == 0) == (fx[k] % 3 == 0) and S_anom(len(v[0]), fx[k], 1) % 3 == 0 for k, v in REG.items())
zero_sector = [t for t in range(3) if (qa + 2 + t) % 3 == 0]
check('A4 theorem: on a permuting register Z3_k x SU(2)_e^2 of S is -4(|X|(q_a+k) + n_1 + 2n_2) = -4 F3 (q_a+k) mod 3; at k = 2 the '
      'doublers gap iff 3 | F3 (all registers; at k = 1 always). One three-cycle carries 0, so the count is set by the fixed copies; '
      f'its t = {zero_sector[0]} sector alone is also anomaly-free, so the anomaly alone does not force removals in threes',
      ex == (-528, -60, -16, -48) and allr and zero_sector == [2], f'6^3: S {ex[0]}, three-cycle {ex[1]}, fixed copy {ex[2]}, 3 fixed {ex[3]}')

# ===================================== B. turn-invariant Dirac masses on a register =====================================
print('== B. bilinear protection on H\' (3D cube objects)')
Am = np.vstack([np.kron(I8, a.T) + np.kron(a, I8) for a in AL] + [np.kron(I8, EPS.T) - np.kron(EPS, I8)])
Ns = null_space(Am, rcond=1e-9); B = [Ns[:, i].reshape(8, 8) for i in range(Ns.shape[1])]
Hb = []
for b in B: Hb += [(b + b.conj().T) / 2, (b - b.conj().T) / 2j]
u_, s_, _ = np.linalg.svd(np.array([x.ravel() for x in Hb]).T, full_matrices=False); Hb = [u_[:, i].reshape(8, 8) for i in range(int(np.sum(s_ > 1e-9)))]
Hb = [(x + x.conj().T) / 2 for x in Hb]
Bc = np.array([b.ravel() for b in B]).T
def crep(L): return np.linalg.lstsq(Bc, np.array([(L @ b @ L.conj().T).ravel() for b in B]).T, rcond=None)[0]
ev3 = np.sort(np.angle(np.linalg.eigvals(crep(Lrot(R3)))))
ninv = null_space(np.vstack([Am] + [np.kron(I8, Ls[i].T) - np.kron(Ls[i], I8) for i in TI]), rcond=1e-9).shape[1]
mix = all(nrm(PA @ x @ PA) < 1e-9 and nrm(PB @ x @ PB) < 1e-9 for x in Hb); pwodd = all(nrm(PW @ x @ PW.conj().T + x) < 1e-9 for x in Hb)
check('B1 theorem (chiral-step D1, rederived): eps-keeping Dirac masses at Gamma span 4 dims, every one pairs the light copy with '
      'the mirror copy, the turn gives them charges w, w^2 (twice each), none is invariant under the 12 turns, all are PW-odd',
      len(B) == 4 and len(Hb) == 4 and mix and pwodd and ninv == 0 and np.allclose(ev3, [-2 * np.pi / 3] * 2 + [2 * np.pi / 3] * 2, atol=1e-6),
      'the twist k acts trivially on bilinears')
def invmass(pts, f, finv, grp, d=1.0, P_=False):
    n = len(pts); ix = {p: i for i, p in enumerate(pts)}
    def pm(g):
        M = np.zeros((n, n))
        for p in pts: M[ix[g(p)], ix[p]] = 1
        return M
    PG = {i: pm(lambda p, R=rots[i]: f(R, p)) for i in grp}; PI = pm(finv); M = 0
    for x in Hb:
        Yd = np.diag(rng.normal(size=n)); Yo = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Yo = (Yo + Yo.conj().T) / 2
        M = M + np.kron(x, Yd + d * (Yo - np.diag(np.diag(Yo))))
    M = sum(np.kron(Ls[i], PG[i]) @ M @ np.kron(Ls[i], PG[i]).conj().T for i in grp) / len(grp)
    if P_:
        G = np.kron(Pinv, PI); M = (M + G @ M @ G.conj().T) / 2; G = np.kron(PW, PI); M = (M - G @ M @ G.conj().T) / 2
    return M, PG
def kernel(M, tol=1e-9): w, V = np.linalg.eigh(M); return V[:, np.abs(w) < tol * max(1.0, np.abs(w).max())]
rows, okB = [], True
for name, (pts, f, finv, grp) in REG.items():
    for P_ in (False, True):
        M, PG = invmass(pts, f, finv, grp, P_=P_); K_ = kernel(M); n = len(pts)
        ch = max(abs(np.trace(K_.conj().T @ np.kron(Ls[i], PG[i]) @ K_) - fx[name] * np.trace(Ls[i])) for i in grp)
        okB &= K_.shape[1] == 8 * fx[name] and ch < 1e-8 and max(nrm(M @ np.kron(a, np.eye(n)) + np.kron(a, np.eye(n)) @ M) for a in AL) < 1e-8
    rows.append(f'{name} {K_.shape[1] // 8}')
check('B2 theorem (Lefschetz count; finite check on 12 registers, with and without P and PW): a generic turn-invariant Dirac mass '
      'leaves exactly 8 F3 massless states, which carry F3 copies of the cube\'s representation: protected families = F3',
      okB, ', '.join(rows))
pts, f, finv, grp = REG['mod m=3']; M, PG = invmass(pts, f, finv, TI, d=0.3); g7 = np.linspace(-np.pi, np.pi, 7); zc = {}
for K in itertools.product(g7, g7, g7):
    e = np.abs(np.linalg.eigvalsh(np.kron(Hp(np.array(K)), np.eye(27)) + 0.2 * M)); key = 'G' if np.allclose(np.cos(K), 1) else ('R' if np.allclose(np.cos(K), -1) else 'o')
    zc.setdefault(key, []).append((int(np.sum(e < 1e-9)), e.min()))
check('B3 6^3 register (27 copies) with an invariant mass, 7^3 grid: 24 massless states at Gamma and at R, gapped at every other point',
      all(z == 24 for z, _ in zc['G'] + zc['R']) and min(m for _, m in zc['o']) > 1e-3, f'min gap off the windows {min(m for _, m in zc["o"]):.3f}')

# ===================================== C. 1+1D toy with the permuting turn =====================================
print('== C. 1+1D toy: copies x 4 tastes x (3-4-5-0) x 2 sectors; the turn permutes copies and adds z = q + k')
TASTE = {'Ga': (0, qa, +1), 'Gb': (0, qb, -1), 'Ra': (1, qa, -1), 'Rb': (1, qb, +1)}; T345 = (3, 4, 5, 0); HS = (1, 1, -1, -1)
l1, l2 = np.array([1, -2, 1, 2]), np.array([2, 1, -2, 1]); w1, w2 = np.array([1, 0, 1, 0]), np.array([0, 1, 0, 1])
V4 = np.array([[1, 0, -1, 0, 0, -2, 2, 0], [2, 1, -2, -1, 0, 0, 0, 0], [1, 1, -1, -1, -1, -1, 1, 1], [0, 2, -2, 2, -1, 0, 1, -2]])
def st(v, j, n): o = np.zeros(4 * n, int); o[4 * j:4 * j + 4] = v; return o
D8 = np.array([st(w1, 0, 3) - st(w1, 1, 3), st(w1, 1, 3) - st(w1, 2, 3), st(w2, 0, 3) - st(w2, 1, 3), st(w2, 1, 3) - st(w2, 2, 3),
               sum(st(l1, j, 3) for j in range(3)), sum(st(l2, j, 3) for j in range(3))])
def system(X, perm, k):
    rw = [(sc, c, T, i) for sc in (1, -1) for c in range(X) for T in TASTE for i in range(4)]; pos = {r: n for n, r in enumerate(rw)}
    K = np.array([sc * TASTE[T][2] * HS[i] for sc, c, T, i in rw]); te = np.array([T345[i] * (sc == 1) for sc, c, T, i in rw])
    to = np.array([T345[i] * (sc == -1) for sc, c, T, i in rw]); z = np.array([(TASTE[T][1] + k) % 3 for sc, c, T, i in rw])
    w = np.array([TASTE[T][0] for sc, c, T, i in rw]); Pm = np.zeros(len(rw), int)       # Pm[n] = image index of mode n
    for r, n in pos.items(): Pm[n] = pos[(r[0], perm[r[1]], r[2], r[3])]
    return rw, pos, K, te, to, z, w, Pm
def lag(X, perm, k, fixed, cycles, light='Ga'):
    rw, pos, K, te, to, z, w, Pm = system(X, perm, k); vecs = []
    def put(blocks, Bm):
        for b in Bm:
            v = np.zeros(len(rw), int)
            for (sc, c, T), seg in zip(blocks, np.split(b, len(blocks))):
                for i, x in enumerate(seg): v[pos[(sc, c, T, i)]] = x
            vecs.append(v)
    for cyc in cycles:                                          # light <-> mirror backscattering on every copy of a three-cycle
        for c in cyc:
            for sc in (1, -1):
                for i in range(4):
                    for A_, B_ in (('Ga', 'Gb'), ('Ra', 'Rb')):
                        v = np.zeros(len(rw), int); v[pos[(sc, c, A_, i)]] = 1; v[pos[(sc, c, B_, i)]] = -1; vecs.append(v)
    za = (qa + k) % 3
    for sc in (1, -1):
        for c in fixed: put([(sc, c, 'Rb'), (sc, c, 'Gb')], V4)
        if za == 0:
            for c in fixed: put([(sc, c, 'Ra')], np.array([l1, l2]))
        elif len(fixed) % 3: return None, (rw, pos, K, te, to, z, w, Pm)
        else:
            for j in range(0, len(fixed), 3): put([(sc, c, 'Ra') for c in fixed[j:j + 3]], D8)
    return np.array(vecs), (rw, pos, K, te, to, z, w, Pm)
def valid(L, data, nlight):
    rw, pos, K, te, to, z, w, Pm = data
    def pv(v): o = np.zeros_like(v); o[Pm] = v; return o
    key = {tuple(v): n for n, v in enumerate(L)}; im = [key.get(tuple(pv(v))) for v in L]
    if None in im: return False
    seen, sums = set(), []
    for n in range(len(L)):
        if n in seen: continue
        orb = [n]; m_ = im[n]
        while m_ != n: orb.append(m_); m_ = im[m_]
        seen |= set(orb); sums.append(sum(L[o] for o in orb))
    return (np.abs((L * K) @ L.T).max() == 0 and not np.any(L @ te) and not np.any(L @ to) and not np.any((L @ w) % 2)
            and 2 * L.shape[0] == len(rw) - nlight and np.linalg.matrix_rank(L.astype(float)) == L.shape[0] and not np.any((np.array(sums) @ z) % 3))
def moduli(m):
    v = list(range(1, 2 * m, 2)); P_ = [tuple(p) for p in itertools.product(v, repeat=3)]; ix = {p: i for i, p in enumerate(P_)}
    perm = [ix[(p[2], p[0], p[1])] for p in P_]; fixed = [i for i in range(len(P_)) if perm[i] == i]; seen, cyc = set(fixed), []
    for i in range(len(P_)):
        if i not in seen: o = [i, perm[i], perm[perm[i]]]; seen |= set(o); cyc.append(o)
    return len(P_), perm, fixed, cyc
X, perm, fixed, cyc = moduli(3); Lc, dc = lag(X, perm, 2, [], cyc)
rw, pos, K, te, to, z, w, Pm = dc
v1 = np.zeros(len(rw), int); v1[pos[(1, fixed[0], 'Ga', 0)]] = 1; v1[pos[(1, fixed[0], 'Gb', 0)]] = -1
piv = all(np.sum(Lc[:, int(np.argmax(v == 1))] != 0) == 1 for v in Lc)          # each vector owns a +1 column: unimodular, primitive
check('C1 theorem (twisted Haldane criterion, proof in report: a pi-invariant Lagrangian gaps symmetrically iff z.l = 0 mod 3 on its '
      'pi-fixed part): light-mirror backscattering on the 8 three-cycles is null, neutral, primitive and twisted-neutral; on a fixed '
      'copy it carries z.l = 1', valid(Lc, dc, 32 * 3) and piv and int(v1 @ z) % 3 == 1, f'{Lc.shape[0]} vectors on 24 copies')
grid, ok_all = {}, True
for k in (0, 1, 2):
    for m in (1, 2, 3, 4):
        X, perm, fixed, cyc = moduli(m); L_, data = lag(X, perm, k, fixed, cyc); rw, pos, K, te, to, z, w, Pm = data
        gap = np.array([(r[1] in fixed and r[2] != 'Ga') or (r[1] not in fixed) for r in rw]); an = int(z[gap] @ (K[gap] * te[gap])) % 3
        st_ = 'G' if (L_ is not None and valid(L_, data, 8 * len(fixed))) else ('x' if an else '?')
        grid[(k, m)] = st_; ok_all &= (st_ == 'G') == (an == 0) and st_ != '?'
snf = all(abs(smith_normal_form(Matrix(Bm.tolist()))[i, i]) == 1 for Bm in (V4, D8) for i in range(Bm.shape[0]))
gs = {k: ''.join(grid[(k, m)] for m in (1, 2, 3, 4)) for k in range(3)}
check('C2 theorem + finite: lemma (pi-invariant neutral Lagrangian => K t in L^pi => z.Kt = 0 mod 3 on the gapped set); the (2m)^3 '
      'register gaps S on the fixed copies and everything on the three-cycles iff 2 F3 (q_a+k) = 0 mod 3, else obstructed: at k = 2 only m = 3',
      ok_all and gs == {0: 'xxGx', 1: 'GGGG', 2: 'xxGx'} and snf, f'm = 1..4: k=0 {gs[0]}, k=1 {gs[1]}, k=2 {gs[2]}; V4, D8 Smith form 1')
X, perm, fixed, cyc = moduli(3); rw, pos, K, te, to, z, w, Pm = system(X, perm, 2); G8 = []
for sc in (1, -1):
    for b in D8:
        v = np.zeros(len(rw), int)
        for j, c in enumerate(fixed):
            for i in range(4): v[pos[(sc, c, 'Ga', i)]] = b[4 * j + i]
        G8.append(v)
G8 = np.array(G8)
check('C3 the three protected families are removable together (D8 on their Gamma-a: null, neutral, z-neutral): the anomaly does not '
      'protect them; only bilinears are excluded. In 3D a term made of light-copy modes alone has turn charge = its mode change, so with Z4 it changes mode number by 12',
      np.abs((G8 * K) @ G8.T).max() == 0 and not np.any(G8 @ te) and not np.any(G8 @ to) and not np.any((G8 @ z) % 3) and np.linalg.matrix_rank(G8.astype(float)) == 12)

# ===================================== D. which three, masses, mixing =====================================
print('== D. which three stay light; masses and mixing')
pts, f, finv, grp = REG['mod m=3']; fixd = [i for i, p in enumerate(pts) if f(R3, p) == p]; Pfix = np.kron(I8, np.diag([1.0 * (i in fixd) for i in range(27)]))
wts = {}
for d in (0.0, 0.05, 0.2, 1.0):
    M, PG = invmass(pts, f, finv, TI, d=d); K_ = kernel(M); wts[d] = np.real(np.trace(K_.conj().T @ Pfix @ K_)) / K_.shape[1]
Kd = kernel(invmass(pts, f, finv, TI, d=0.3)[0]); Gq = np.zeros((576, 576), complex)
for i in TI:                                                    # commutant dim = null count of sum_g A_g^+ A_g (Gram form, small memory)
    Rg = Kd.conj().T @ np.kron(Ls[i], PG[i]) @ Kd; Ag = np.kron(np.eye(24), Rg.T) - np.kron(Rg, np.eye(24)); Gq += Ag.conj().T @ Ag
comm = int(np.sum(np.linalg.eigvalsh(Gq) < 1e-8))
cub = null_space(np.vstack([np.kron(I8, Ls[i].T) - np.kron(Ls[i], I8) for i in TI]), rcond=1e-9).shape[1]
check('D1 theorem: on the protected space the turns act as 3 copies of the cube, so the allowed family operators are '
      '(cube commutant) x M_3: any hierarchy and any mixing are allowed, none predicted', comm == cub * 9, f'dim {comm} = {cub} x 9')
check('D2 diagnostic (supplied random textures): with a register-diagonal mass the light families are exactly the fixed copies '
      '(the spine); off-diagonal parts d tilt them inside the 11-dim turn-invariant sector', abs(wts[0.0] - 1) < 1e-9 and wts[1.0] < 0.6,
      'weight on fixed copies ' + ', '.join(f'd={d}: {v:.3f}' for d, v in wts.items()))
M, PG = invmass(pts, f, finv, TI, d=0.5); Kr = kernel(M); wB, VB = np.linalg.eigh(Kr.conj().T @ np.kron(PB, np.eye(27)) @ Kr); KB = Kr @ VB[:, wB > 0.5]
we, Ve = np.linalg.eigh(KB.conj().T @ np.kron((I8 + EPS) / 2, np.eye(27)) @ KB); Ke = KB @ Ve[:, we > 0.5]; Ko = KB @ Ve[:, we < 0.5]
fac = [np.linalg.matrix_rank(np.vstack([Kx[:, j].reshape(8, 27) for j in range(Kx.shape[1])]), tol=1e-8) for Kx in (Ke, Ko)]
Ny = null_space(np.vstack([np.kron(I8, a.T) + np.kron(a, I8) for a in AL] + [np.kron(I8, EPS.T) + np.kron(EPS, I8)]), rcond=1e-9)
yB = [PB @ Ny[:, i].reshape(8, 8) @ PB for i in range(Ny.shape[1])]; uy, sy, _ = np.linalg.svd(np.array([y.ravel() for y in yB]).T, full_matrices=False)
yB = [uy[:, i].reshape(8, 8) for i in range(int(np.sum(sy > 1e-8)))]
def fam(Y):
    A = Ko.conj().T @ Y @ Ke; U, S, Vh = np.linalg.svd(A); return S[::2] / S[0], [Vh[2 * j:2 * j + 2].conj().T for j in range(3)]
def V12(a, b): return np.sqrt(abs(np.trace(a[1][0].conj().T @ b[1][1] @ b[1][1].conj().T @ a[1][0]).real) / 2)
Dr = [sum(np.kron(Ls[i], PG[i]) @ np.kron(I8, np.diag(rng.normal(size=27))) @ np.kron(Ls[i], PG[i]).conj().T for i in TI) / 12 for _ in range(2)]
fu, fd = fam(np.kron(yB[0], np.eye(27))), fam(np.kron(yB[1] + 0.7j * yB[0], np.eye(27)))
gu, gd = fam(np.kron(yB[0], np.eye(27)) @ Dr[0]), fam(np.kron(yB[1], np.eye(27)) @ Dr[1])
lep = (1, 206.7682830, 3477.23); mq = dict(u=2.16, c=1273.0, t=172570.0, d=4.70, s=93.5, b=4183.0)
lr = [np.log(lep[1]) / np.log(lep[2] / lep[1]), np.log(mq['c'] / mq['u']) / np.log(mq['t'] / mq['c']), np.log(mq['s'] / mq['d']) / np.log(mq['b'] / mq['s'])]
check('D3 theorem + [M]: the light left and right families factor as spin x register (C^2 x V_e, C^2 x V_o), so a register-blind vacuum '
      'gives every sector the mass matrix y_s V_o^+ V_e: equal ratios in all sectors and no mixing; measured ratios differ by sector and '
      '|V_us| = 0.2243, so the vacuum must depend on the register', fac == [3, 3] and np.allclose(fu[0], fd[0], atol=1e-8) and V12(fu, fd) < 1e-6
      and V12(gu, gd) > 1e-3 and max(lr) / min(lr) > 2, f'register-blind ratios {np.round(fu[0], 3)} both sectors, |V12| {V12(fu, fd):.0e}; '
      f'register-dependent |V12| {V12(gu, gd):.2f}; measured ln-ratio 1.889/1.299/0.787')

# ===================================== E. measurement =====================================
print('== E. against measurement')
Nnu, sN = 2.9963, 0.0074
print(f'   N_nu (LEP, Janot-Jadach 2020: {Nnu} +- {sN}): F3 = 3 gives 3 ({(3 - Nnu) / sN:.1f} sigma); next allowed F3 = 6 (12^3 cell) '
      f'{(6 - Nnu) / sN:.0f} sigma, F3 = 9 (zoom 9) {(9 - Nnu) / sN:.0f} sigma; F3 = 1, 2, 4, 5 are anomaly-forbidden (A4): no 4th chiral family on any register')
print('   the 24 three-cycle families are vector-like with masses ~ (copy-mixing coefficient) x cell scale: vector-like quark limits '
      '(~1.5 TeV) need a coefficient above ~1e-16 for a Planck-scale cell; no light remnant (B3)')
gR = lambda g: 3 * (10.75 / g) ** (4 / 3)
print(f'   each light family keeps its right-handed neutrino in an SU(2)_odd doublet (Dirac only, Z4): Delta N_eff = {gR(106.75):.2f} '
      f'(decoupling above the weak scale) to {gR(61.75):.2f} (just above QCD) vs Planck 2.99 +- 0.17 (not specific to the register)')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: A1-A4, B1, B2 (Lefschetz), C1-C2 lemma, D1, D3 (factorisation); finite: B2, B3, C2 grid, C3; diagnostics: D2; '
      'estimates: E. Supplied: H\', O_A (k = 2), the zone-corner term, the register reading, generic register masses.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
