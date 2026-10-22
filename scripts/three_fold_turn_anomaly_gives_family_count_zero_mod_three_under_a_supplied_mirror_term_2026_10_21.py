#!/usr/bin/env python3
"""families-mod-3: does a three-fold-turn anomaly fix the family count on the chiral generator H' = (i/2)[W_o, W_e]?

Supplied model: CL-2 cube objects (one fermion mode per site, spin-3/2 edge hop W, face-diagonal hop F, copy sign
s3 = -eps F), the generator H' (chiral-step), its two windows Gamma and R = pi(1,1,1), N stacked families each carrying the
rung-1 internal (4,2) as 4 doublets of SU(2)_e (even sublattice, the weak group) and of SU(2)_o.  Light = the Gamma taste
of copy a that is left-handed on the even sublattice; S = the three tastes to be gapped (Gamma copy b, R copy a, R copy b).
Sections:  A window content of H';  B which twisted turn a four-mode term keeps;  C anomaly algebra of S (exact integers);
D 1+1D K-matrix toy (tastes = 3-4-5-0 multiplets, exact Haldane null vectors, Smith form);  E estimates against measurement.
Cited, not rederived: 't Hooft anomaly matching, crystalline equivalence, Cordova-Ohmori (no symmetric TQFT for anomalies
seen on S^1 x S^4), Haldane's null-vector criterion, the SMG conjecture (anomaly-free => gappable) for sufficiency in 3D.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/THREE_FOLD_TURN_ANOMALY_GIVES_FAMILY_COUNT_ZERO_MOD_THREE_UNDER_A_SUPPLIED_MIRROR_TERM_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
OM = np.exp(2j * np.pi / 3)

# ------------------------------------------------ cube objects ------------------------------------------------
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
iC3 = [i for i, R in enumerate(rots) if abs(np.trace(R)) < 1e-9 and np.allclose(axang(R)[0], np.ones(3) / np.sqrt(3))][0]
L3, R3 = Ls[iC3], rots[iC3]
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Hp(K): D = Dg(K); Wo = D.conj().T @ W @ D; return 0.5j * (Wo @ W - W @ Wo)
Rv = np.full(3, np.pi); rng = np.random.default_rng(20261021); KR = rng.uniform(-np.pi, np.pi, (16, 3))
P2 = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
def lift(al, L):
    Sig = [-1j * al[1] @ al[2], -1j * al[2] @ al[0], -1j * al[0] @ al[1]]
    Mr = np.array([[np.trace(L @ al[a] @ L.conj().T @ al[b]).real / 8 for b in range(3)] for a in range(3)])
    n, ang = axang(np.round(Mr).T); best = None
    for s_ in (1, -1):
        S = expm(-1j * s_ * ang / 2 * sum(n[k] * Sig[k] for k in range(3)))
        e_ = max(nrm(S @ al[q] @ S.conj().T - L @ al[q] @ L.conj().T) for q in range(3))
        if best is None or e_ < best[0]: best = (e_, S)
    return best
def content(K0, h=1e-6):
    al = [(Hp(K0 + h * np.eye(3)[a]) - Hp(K0 - h * np.eye(3)[a])) / (2 * h) for a in range(3)]
    v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); al = [a / v for a in al]
    g5 = 1j * al[0] @ al[1] @ al[2]; g5 = (g5 + g5.conj().T) / 2; err, S = lift(al, L3); rho = S.conj().T @ L3; rows = []
    for gg in (1, -1):
        for q, lam in ((1, OM), (2, OM ** 2)):
            w_, V = np.linalg.eig(rho); Vl = V[:, np.abs(w_ - lam) < 1e-5]
            u, s_, _ = np.linalg.svd((I8 + gg * g5) / 2 @ (Vl @ np.linalg.pinv(Vl))); B = u[:, s_ > 0.5]; A = [B.conj().T @ a @ B for a in al]
            Mm = np.array([[np.trace(A[a] @ P2[i]).real / 2 for a in range(3)] for i in range(3)])
            rows.append((q, 'L' if np.linalg.det(Mm) < 0 else 'R', int(round(np.trace(B.conj().T @ EPS @ B).real / 2)), B.shape[1]))
    return sorted(rows), err, nrm(np.linalg.matrix_power(rho, 3) - I8)

# ===================================== A. window content of H' =====================================
print("== A. windows of H'")
rel = max(max(nrm(Hp(K + Rv) + Hp(K)), nrm(L3 @ Hp(K) @ L3.conj().T - Hp(R3 @ K))) for K in KR)
g8 = np.linspace(-np.pi, np.pi, 8, endpoint=False)
zer = [K for K in itertools.product(g8, g8, g8) if np.abs(np.linalg.eigvalsh(Hp(np.array(K)))).min() < 1e-9]
check("A1 H'(K+R) = -H'(K), the turn maps H'(K) to H'(R3 K), zeros of H' on an 8^3 grid only at Gamma and R", rel < 1e-12
      and sorted(map(tuple, np.round(zer, 6))) == sorted([(0.0, 0.0, 0.0), tuple(np.round(-Rv, 6))]), f'residual {rel:.0e}, zeros {len(zer)}')
rG, eG, oG = content(np.zeros(3)); rR, eR, oR = content(Rv)
flip = sorted((q, {'L': 'R', 'R': 'L'}[h], s, d) for q, h, s, d in rG)
check('A2 Gamma: even sublattice (q2, L) + (q1, R), odd (q1, L) + (q2, R); at R the same copy charges with handedness flipped',
      rG == sorted([(2, 'L', 1, 2), (1, 'R', 1, 2), (1, 'L', -1, 2), (2, 'R', -1, 2)]) and rR == flip and max(eG, eR, oG, oR) < 1e-6,
      'q = copy charge of the internal part of the turn (rho^3 = 1)')
def widx(rows, k, sub): return sum((1 if h == 'L' else -1) * (q + k) for q, h, s, d in rows if s == sub)
tab = {k: (widx(rG, k, 1), widx(rR, k, 1), widx(rG, k, -1), widx(rR, k, -1)) for k in range(3)}
check('A3 theorem: per doublet the Z3_k x SU(2)_e^2 window index is +1 at Gamma and -1 at R for every twist k (each window holds '
      'one L and one R doublet, so the twist cancels); with 4 doublets per family: +-4N, total 0', all(v == (1, -1, -1, 1) for v in tab.values()))
ev = np.linalg.eigvals(-L3); qi = sorted(int(round(np.angle(x) / (2 * np.pi / 3))) % 3 for x in ev)
check('A4 geometric reading: the turn on the 8 corners of a cell has charges {0^4, 1^2, 2^2} (sum 6); if it commutes with the weak '
      'SU(2) each doublet has one charge and the 4 doublets add 3 = 0 mod 3, so 4N(q + k) is reading-independent', qi == [0, 0, 0, 0, 1, 1, 2, 2])

# ===================================== B. which twisted turn a four-mode term keeps =====================================
print('== B. twist selection')
s3 = -EPS @ F; PA, PB = (I8 + s3) / 2, (I8 - s3) / 2
UA = np.linalg.svd(PA)[0][:, :4]; UB = np.linalg.svd(PB)[0][:, :4]; V8 = np.hstack([UA, UB])
TL = [L for L in Ls if nrm(L @ s3 @ L.conj().T - s3) < 1e-9]
chi = [int(round(np.angle(np.linalg.det(UA.conj().T @ L @ UA)) / (2 * np.pi / 3))) % 3 for L in TL]
subs = list(itertools.combinations(range(8), 4)); SUBS = np.array(subs); nA = np.array([sum(i < 4 for i in s) for s in subs])
def L4(G): return np.linalg.det(G[SUBS[:, None, :, None], SUBS[None, :, None, :]])
L4s = [L4(V8.conj().T @ L @ V8) for L in TL]
cnt = {}
for k in range(3):
    for a in range(5):
        ix = np.where(nA == a)[0]; Mk = np.vstack([OM ** (4 * k * c) * A[np.ix_(ix, ix)] - np.eye(len(ix)) for A, c in zip(L4s, chi)])
        sv = np.linalg.svd(Mk, compute_uv=False); m_ = int(np.sum(sv < 1e-8)) + Mk.shape[1] - len(sv)
        if m_: cnt.setdefault(k, {})[(a, 4 - a)] = m_
cA = round(np.angle(np.linalg.det(UA.conj().T @ L3 @ UA)) / (2 * np.pi / 3)) % 3; cB = round(np.angle(np.linalg.det(UB.conj().T @ L3 @ UB)) / (2 * np.pi / 3)) % 3
check('B1 theorem: copy A (s3 = +1) is the q1 copy; the plain turn gives its top form O_A charge 1 and O_B charge 2; a twist '
      'k multiplies a four-mode term by w^(4k) = w^k, so O_A keeps only k = 2 = -q1 and O_B only k = 1 = -q2',
      (cA, cB) == (1, 2) and np.isclose(np.trace(EPS @ PA).real, 0) and len(TL) == 12)
check('B2 one-cube four-mode terms covariant under the 12 twisted tetrahedral turns, by copy content (n_A, n_B): every twist has '
      'number-changing terms, the single-copy one only for k = 2 (mirror-type O_A) and k = 1 (O_B)',
      cnt == {0: {(2, 2): 10}, 1: {(0, 4): 1, (2, 2): 1, (3, 1): 4}, 2: {(1, 3): 4, (2, 2): 1, (4, 0): 1}}, f'{cnt}')

# ===================================== C. anomaly algebra of S (3D content, exact) =====================================
print('== C. anomalies of the gapped set S = {Gamma-b, R-a, R-b}, light = Gamma-a (q_a = 2)')
qa, qb = 2, 1
# each taste: (window, copy q, handedness of its even-sublattice doublets); odd-sublattice doublets have the other hand
TASTE = {'Ga': (0, qa, +1), 'Gb': (0, qb, -1), 'Ra': (1, qa, -1), 'Rb': (1, qb, +1)}
def anom(tastes, N, ke, ko=None, tw=None):
    ko = ke if ko is None else ko; tw = [0] * N if tw is None else tw
    out = dict(e=0, o=0, Ne=0, Z2=0, dbl=0, nu=0, cub=0, grav=0)
    for f in range(N):
        for T in tastes:
            win, q, h = TASTE[T]
            for part, hh, kk in (('e', h, ke), ('o', -h, ko)):        # odd-sublattice doublets have the other hand
                z = q + kk + tw[f]
                out[part] += 4 * hh * z; out['grav'] += 8 * hh * z; out['cub'] += 8 * hh * z ** 3; out['nu'] += 8 * hh
            out['Ne'] += 4 * h; out['Z2'] += 4 * h * win; out['dbl'] += 4
    return out
S = ['Gb', 'Ra', 'Rb']
a1 = anom(S, 1, 0); amir = [anom(['Gb', 'Rb'], 1, k) for k in range(3)]
check('C1 theorem, per family: Z3_k x SU(2)_e^2 of S = -4(q_a + k), x SU(2)_o^2 = +4(q_a + k); U(1)_N x SU(2)_e^2 = -4 (N must break; '
      'Z4 part 0 mod 4); 12 doublets per SU(2) (no Witten anomaly); Z16, Z3^3, Z3-gravity and translation-Z2 parts 0; '
      'the mirror pair {Gamma-b, R-b} is anomaly-free for every k',
      all(anom(S, 1, k)['e'] == -4 * (qa + k) and anom(S, 1, k)['o'] == 4 * (qa + k) and anom(S, 1, k)['cub'] == 0 and anom(S, 1, k)['grav'] == 0
          for k in range(3)) and a1['Ne'] == -4 and a1['Ne'] % 4 == 0 and a1['dbl'] == 12 and a1['nu'] == 0 and a1['Z2'] % 2 == 0
      and all(m['e'] == 0 and m['o'] == 0 and m['Ne'] == 0 for m in amir))
NS = (1, 2, 3, 4, 5, 6, 9)
def S_anom(ql, k, N):                      # from the computed window pieces: light = (ql, L) at Gamma on sublattice sg
    sg = [s for q, h, s, d in rG if q == ql and h == 'L'][0]
    pcs = [p for p in rG if p[2] == sg and not (p[0] == ql and p[1] == 'L')] + [p for p in rR if p[2] == sg]
    return 4 * N * sum((1 if h == 'L' else -1) * (q + k) for q, h, s, d in pcs)
sw = {k: [N for N in NS if S_anom(1, k, N) % 3 == 0] for k in (1, 2)}
ok_set = {k: [N for N in NS if anom(S, N, k)['e'] % 3 == 0 and anom(S, N, k)['o'] % 3 == 0] for k in range(3)}
check('C2 conditional theorem: S can be gapped keeping SU(2)_e x SU(2)_o and the k-twisted turn only if N(q_a + k) = 0 mod 3. The '
      'mirror top form fixes k = -q_b = 2: N = 0 mod 3, smallest N = 3 (no further anomaly). At k = -q_a = 1 every N passes',
      ok_set == {0: [3, 6, 9], 1: list(NS), 2: [3, 6, 9]} and sw == {1: [3, 6, 9], 2: list(NS)},
      f'allowed N per twist k: {ok_set}; from the A2 pieces with light = q1 (SU(2)_o weak): mirror O_B (k = 1) {sw[1]}')
sol = [(ke, ko) for ke in range(3) for ko in range(3) if (cA + 2 * ke + 2 * ko) % 3 == 0]
rescue = [(ke, ko, N) for ke, ko in sol for N in (1, 2, 4, 5) if anom(S, N, ke, ko)['e'] % 3 == 0 and anom(S, N, ke, ko)['o'] % 3 == 0]
check('C3 theorem: sublattice twists exp(2 pi i (k_e N_e + k_o N_o)/3) kept by O_A (2 + 2 modes, so 1 + 2(k_e + k_o) = 0) never '
      'rescue N = 1, 2, 4, 5: SU(2)_e needs k_e = -q_a, SU(2)_o needs k_o = -q_a, and O_A then has charge 2', rescue == [] and len(sol) == 3,
      f'O_A-compatible (k_e, k_o): {sol}')
loc = {k: anom(['Ra', 'Rb'], 1, k)['e'] for k in range(3)}
check('C4 theorem (chiral-smg C6, narrowed): the R window alone carries -4 per family for every twist, so a gap acting on R alone '
      'needs N = 0 mod 3; translations allow terms with two R fields, so the R window need not be gapped alone', set(loc.values()) == {-4})
ftw = {N: [t for t in itertools.product(range(3), repeat=N) if 0 in t and anom(S, N, 2, tw=list(t))['e'] % 3 == 0
           and anom(S, N, 2, tw=list(t))['o'] % 3 == 0] for N in (1, 2, 4)}
check('C5 family-dependent twists (k = 2 plus t_f; O_A on family f needs t_f = 0): O_A on every family forces t = 0 (C2); with O_A '
      'on at least one family, family-dependent rules allow every N >= 2 (N = 1 never), e.g. N = 2 with t = (0,1)', ftw[1] == [] and (0, 1) in ftw[2] and len(ftw[4]) > 0,
      f'solutions: N=2 {len(ftw[2])}, N=4 {len(ftw[4])}')

# ===================================== D. 1+1D K-matrix toy =====================================
print('== D. 1+1D toy: each taste is a 3-4-5-0 multiplet; even sector (U(1)_e) and odd sector (U(1)_o, handedness flipped)')
T345 = (3, 4, 5, 0); HS = (1, 1, -1, -1)
def toy(N, k, tastes=('Gb', 'Ra', 'Rb'), tw=None):
    tw = [0] * N if tw is None else tw; rows = []
    for sec in (1, -1):
        for f in range(N):
            for T in tastes:
                win, q, h = TASTE[T]
                for c, s in zip(T345, HS): rows.append((sec, f, T, c, sec * h * s, (q + k + tw[f]) % 3, win))
    K = np.array([r[4] for r in rows]); te = np.array([r[3] * (r[0] == 1) for r in rows]); to = np.array([r[3] * (r[0] == -1) for r in rows])
    z = np.array([r[5] for r in rows]); w = np.array([r[6] for r in rows]); return rows, K, te, to, z, w
l1, l2 = np.array([1, -2, 1, 2]), np.array([2, 1, -2, 1]); w1, w2 = np.array([1, 0, 1, 0]), np.array([0, 1, 0, 1])
V4 = np.array([[1, 0, -1, 0, 0, -2, 2, 0], [2, 1, -2, -1, 0, 0, 0, 0], [1, 1, -1, -1, -1, -1, 1, 1], [0, 2, -2, 2, -1, 0, 1, -2]])  # on (R-b, Gamma-b)
def st(v, j, n): o = np.zeros(4 * n, int); o[4 * j:4 * j + 4] = v; return o
D8 = np.array([st(w1, 0, 3) - st(w1, 1, 3), st(w1, 1, 3) - st(w1, 2, 3), st(w2, 0, 3) - st(w2, 1, 3), st(w2, 1, 3) - st(w2, 2, 3),
               sum(st(l1, j, 3) for j in range(3)), sum(st(l2, j, 3) for j in range(3))])
FT = np.array([[0, 2, 1, 0, -1, 0, -2, 0], [2, -2, -2, 1, 2, -1, 2, 2], [1, -1, 0, 1, 0, -1, 1, 1], [2, -1, -2, 2, 0, 2, 0, -1]])  # R-a of t=0 and t=1 families
SNF1 = {nm: all(abs(smith_normal_form(Matrix(B.tolist()))[i, i]) == 1 for i in range(B.shape[0])) for nm, B in (('pair', np.array([l1, l2])), ('V4', V4), ('D8', D8), ('FT', FT))}
def build(N, k, tw=None):
    rows, K, te, to, z, w = toy(N, k, tw=tw); pos = {(r[0], r[1], r[2], r[3]): i for i, r in enumerate(rows)}; vecs = []
    def put(blocks, B):
        for b in B:
            v = np.zeros(len(rows), int)
            for (sec, f, T), seg in zip(blocks, np.split(b, len(blocks))):
                for c, x in zip(T345, seg): v[pos[(sec, f, T, c)]] = x
            vecs.append(v)
    for sec in (1, -1):
        for f in range(N): put([(sec, f, 'Rb'), (sec, f, 'Gb')], V4)
        zr = [(qa + k + (tw[f] if tw else 0)) % 3 for f in range(N)]
        if tw is not None and N == 2 and sorted(zr) == [1, 2]:
            put([(sec, zr.index(1), 'Ra'), (sec, zr.index(2), 'Ra')], FT); continue
        free = [f for f in range(N) if zr[f] == 0]; rest = [f for f in range(N) if zr[f] != 0]
        for f in free: put([(sec, f, 'Ra')], np.array([l1, l2]))
        if len(rest) % 3: return None, (rows, K, te, to, z, w)
        for j in range(0, len(rest), 3): put([(sec, f, 'Ra') for f in rest[j:j + 3]], D8)
    return np.array(vecs), (rows, K, te, to, z, w)
def valid(Lg, data):
    rows, K, te, to, z, w = data
    return (Lg.shape[0] * 2 == len(K) and np.abs(Lg @ np.diag(K) @ Lg.T).max() == 0 and not np.any(Lg @ te) and not np.any(Lg @ to)
            and not np.any((Lg @ z) % 3) and not np.any((Lg @ w) % 2) and np.linalg.matrix_rank(Lg.astype(float)) == Lg.shape[0])
res = {}
for k in range(3):
    for N in (1, 2, 3, 4, 6):
        Lg, data = build(N, k); rows, K, te, to, z, w = data
        an = (int(z @ (K * te)) % 3, int(z @ (K * to)) % 3)
        res[(k, N)] = 'gap' if (Lg is not None and valid(Lg, data)) else ('obstructed' if an != (0, 0) else 'open')
check('D1 lemma (proof in report): a neutral Lagrangian L forces K t in L, so z.K t = 0 mod 3; the toy anomaly of S is '
      '-2N(q_a + k) per sector (3 + 4 - 5 = 2 replaces the 4 doublets)', all(int(toy(N, k)[4] @ (toy(N, k)[1] * toy(N, k)[2])) % 3
      == (-2 * N * (qa + k)) % 3 for k in range(3) for N in (1, 2, 4)))
grid = {k: ''.join('G' if res[(k, N)] == 'gap' else ('x' if res[(k, N)] == 'obstructed' else '?') for N in (1, 2, 3, 4, 6)) for k in range(3)}
check('D2 exact toy, N = 1,2,3,4,6: every case is either obstructed (anomaly nonzero) or gapped by an explicit Lagrangian (null, '
      'neutral under U(1)_e, U(1)_o, Z3_k, translation; Smith form all 1): gapped iff N(q_a + k) = 0 mod 3',
      grid == {0: 'xxGxG', 1: 'GGGGG', 2: 'xxGxG'} and all(SNF1.values()), f'k=0 {grid[0]}, k=1 {grid[1]}, k=2 {grid[2]} (G gap, x obstructed)')
mir = [k for k in range(3) if ((qb + k) * int(l1.sum())) % 3 == 0]
rl = all(int(toy(N, k, ('Ra', 'Rb'))[4] @ (toy(N, k, ('Ra', 'Rb'))[1] * toy(N, k, ('Ra', 'Rb'))[2])) % 3 != 0 for k in range(3) for N in (1, 2, 4))
Lf, df = build(2, 2, tw=[0, 1])
check('D3 the mirror-only pair term is neutral only at k = -q_b = 2; a gap acting on the R window alone is obstructed for N = 1, 2, 4 '
      'at every k; the family-twisted N = 2 case (k = 2, t = (0,1)) has an explicit Lagrangian', mir == [2] and rl and Lf is not None and valid(Lf, df))

# ===================================== E. estimates against measurement =====================================
print('== E. estimates')
Nnu, sNu = 2.984, 0.008
print(f'   N_nu (LEP {Nnu} +- {sNu}): an ungapped R-a taste doubles the active neutrinos: N=1 -> 2 ({(Nnu - 2) / sNu:.0f} sigma),'
      f' N=3 -> 6 ({(6 - Nnu) / sNu:.0f} sigma); N=3 with S gapped -> 3 ({(3 - Nnu) / sNu:.1f} sigma)')
dc = 1 / 137.036 / (4 * np.pi)
print(f'   breaking every twisted turn: lattice-scale loops give light-cone anisotropy >~ alpha/4pi = {dc:.0e} vs |c_jk| < ~1e-18 '
      f'(electron, trapped-ion tests): excluded by ~1e{int(np.log10(dc / 1e-18))}, so one twisted turn must stay exact')
print('   4th family: k = 2 forbids N = 4 (and 5); N = 6 is allowed by the anomaly but N_nu = 6 or heavy chiral copies are excluded')
cells = {m: m ** 3 % 3 for m in (1, 2, 3, 4, 6, 8)}
print(f'   family supply: (2m)^3 cells hold m^3 rung-1 families, m^3 mod 3 = {cells}; 2^n zooms never give 3 | N, so with k = 2 the '
      'one-family rung-1 reading is excluded and zoom 3 (6^3, 27 per cell) is the smallest cubic supply')
print(f'   k = 2: every light field has twisted charge q_a - q_b = 1, so Lorentz-scalar light Delta N = 4 operators (charge 4 = 1) are'
      ' forbidden; family-blind, so no mass or mixing pattern follows')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: A3, B1, C1-C5, D1 lemma; finite: A1, A2, A4, B2, D2, D3; estimates: E. Supplied: H\', rung-1 (4,2) with SU(2)_e as '
      'weak group, which copy is light, the twist rule, the toy charges.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
