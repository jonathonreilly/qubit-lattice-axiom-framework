#!/usr/bin/env python3
"""z3-masses: does the three-family gap term that the twisted-turn anomaly forces on the R doubler induce a Koide circulant?

Supplied model, as in families-mod-3 and family-register: CL-1 cube objects, the chiral generator H' = (i/2)[W_o, W_e],
the mirror top form O_A (twist k = 2), N = 3 stacked families with the rung-1 internal (4,2) of SU(4) x SU(2)_e x SU(2)_o.
Sections: A measured targets; B twisted charges of the copy top forms (cube objects); C 3D selection rules for the
three-family gap term (exact integer arithmetic); D 1+1D K-matrix toy (exact); E finite three-family cluster with exact
second-order perturbation theory and an exact-diagonalisation check; F the spine reading of family-register; G dynamical
phases and a look-elsewhere test; H quarks and mixing.
Cited, not rederived: families-mod-3 (anomaly -4 per family, toy charges, the D8 Lagrangian), smg-verify (its so(12) chains),
mass-law (Clifford Gram point), family-register (spine), Lindemann-Weierstrass, Schur's lemma.
A PASS line states a true mathematical or numerical fact; several record failures of a candidate mechanism.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import brentq
from sympy import Matrix, Poly, symbols
from sympy.matrices.normalforms import smith_normal_form

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
OM = np.exp(2j * np.pi / 3); TP3 = 2 * np.pi / 3
def fold(d): d = d % TP3; return min(d, TP3 - d)           # delta mod 2pi/3, mirror-folded into [0, pi/3]
def brannen(x):                                           # sqrt(m_k) = a(1 + 2 sqrt(r) cos(delta + 2 pi k/3)) fit of |x|
    x = np.abs(np.asarray(x, float)); a = x.mean(); z = (x * np.exp(-2j * np.pi * np.arange(3) / 3)).sum() / 3
    return abs(z) ** 2 / a ** 2, fold(np.angle(z))
def Qk(m): m = np.asarray(m, float); return m.sum() / np.sqrt(m).sum() ** 2
def ratios_rd(r, d):
    x = sorted([(1 + 2 * np.sqrt(r) * np.cos(d + TP3 * k)) ** 2 for k in range(3)]); return x[1] / x[0], x[2] / x[1]

# ===================================== A. measured targets =====================================
print('== A. targets')
me, mmu, mtau, dtau = 0.51099895000, 105.6583755, 1776.93, 0.09
R1, sR1 = mmu / me, 206.7682830 * np.hypot(1.5e-10 / me, 2.3e-6 / mmu); R2, sR2 = mtau / mmu, mtau / mmu * dtau / mtau
mp.mp.dps = 30
def mrat(r, d): x = sorted([(1 + 2 * mp.sqrt(r) * mp.cos(d + 2 * mp.pi * k / 3)) ** 2 for k in range(3)]); return x[1] / x[0]
DT = float(mp.findroot(lambda d: mrat(mp.mpf(1) / 2, d) - R1, mp.mpf('0.2222')))
RT = float(mp.findroot(lambda r: mrat(r, mp.mpf(2) / 9) - R1, mp.mpf('0.5')))
sDT = float(sR1 / abs(mp.diff(lambda d: mrat(mp.mpf(1) / 2, d), DT)))
check(f'A1 [M] r = 1/2 gives delta = {DT:.10f}({sDT:.0e}); delta = 2/9 gives r = {RT:.10f}; m_mu/m_e {R1:.4f}, m_tau/m_mu {R2:.4f}',
      abs(DT - 0.2222220471) < 2e-10 and abs(RT - 0.4999997868) < 2e-10)

# ===================================== B. twisted charges from the cube objects =====================================
print('== B. twisted charges (cube objects)')
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5; I8 = np.eye(8)
EPS = np.diag((-1.0) ** C.sum(1)).astype(complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5)
def coh32(n): n = np.asarray(n, float) / np.linalg.norm(n); w_, v_ = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); return v_[:, -1]
XI = [coh32(2 * C[i] - 1.0) for i in range(8)]
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
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(Rm), 1): rots.append(Rm)
def axang(Rm):
    a = np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9: w_, v_ = np.linalg.eigh((Rm + np.eye(3)) / 2); return v_[:, np.argmax(w_)], a
    return np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(a)), a
def img(Rm, i): return int(np.argmin(np.sum(abs(cc - Rm @ cc[i]), 1)))
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(Rm, i); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
R3 = [Rm for Rm in rots if abs(np.trace(Rm)) < 1e-9 and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]; L3 = Lrot(R3)
s3 = -EPS @ F; UA = np.linalg.svd((I8 + s3) / 2)[0][:, :4]; UB = np.linalg.svd((I8 - s3) / 2)[0][:, :4]
cA = round(np.angle(np.linalg.det(UA.conj().T @ L3 @ UA)) / TP3) % 3; cB = round(np.angle(np.linalg.det(UB.conj().T @ L3 @ UB)) / TP3) % 3
k_tw = 2; zA, zB = (cA + 4 * k_tw) % 3, (cB + 4 * k_tw) % 3
check('B1 [T] plain-turn charges of the top forms: O_A (mirror) 1, O_B (copy a, light and R doubler) 2; at k = 2 O_A 0, O_B 1: one '
      'family\'s doubler top form is forbidden, a product of three allowed', (cA, cB) == (1, 2) and (zA, zB) == (0, 1) and (3 * zB) % 3 == 0)

# ===================================== C. 3D selection rules =====================================
print('== C. three-family gap term in 3D (exact integer arithmetic)')
# R-a fields: h_e (R-handed, (4,2,1), N=+1), h_o (L-handed, (4,1,2), N=+1); a,b,c,d = # h_e, h_o, h_e^+, h_o^+
okc, mins = True, []
for a, b, c, d in itertools.product(range(15), repeat=4):
    n = a + b + c + d
    if n > 14 or (b + c) % 2 or (a + d) % 2 or (a + c) % 2 or (b + d) % 2: continue      # Lorentz scalar, SU(2)_e, SU(2)_o
    dN = a + b - c - d; n4 = dN                                                         # SU(4) N-ality equals mode change
    if n4 % 4 == 0 and dN % 3 == 0 and dN != 0: mins.append((n, abs(dN)))
minfield = min(mins); anomN = [N for N in range(1, 10) if (-4 * N) % 12 == 0]
check('C1 [T] copy-a doubler fields are SU(4) 4s of mode number +1: SU(4) needs dN = 0 mod 4, the twisted turn dN = 0 mod 3, so '
      'number-breaking terms on them have dN in 12Z and >= 12 fields; Z12 x SU(2)_e^2 (-4 per family) vanishes iff N = 0 mod 3',
      minfield == (12, 12) and anomN == [3, 6, 9], f'fewest {minfield[0]} fields; N {anomN}')
dists = [p for p in itertools.product(range(13), repeat=3) if sum(p) == 12]
rel = [p for p in dists if p[0] == p[1] == p[2]]; par = [p for p in dists if all(x % 2 == 0 for x in p)]; allf = [p for p in dists if min(p) > 0]
chiral = [p for p in allf if len(set(p)) == 3]
check('C2 [T] of 91 family splittings of 12 annihilators (55 touch all families) only (4,4,4) = T3 = O_0 O_1 O_2 keeps every '
      'relative family number; 28 keep every family parity; 42 ordered ones come in reflection pairs',
      (len(dists), len(allf), rel, len(par)) == (91, 55, [(4, 4, 4)], 28) and len(chiral) == 42)
z4 = {'T3': (4, 4, 4), 'O_A on f': (4, 0, 0), "H'": (0, 0, 0), 'bilinear f,g': (1, -1, 0)}
neutral = {k: all(x % 4 == 0 for x in v) for k, v in z4.items()}
check('C3 [T] H\' acts inside a family, O_A and T3 change N_f by 4: each family keeps N_f mod 4 (anomaly -4 = 0 mod 4), so '
      'inter-family bilinears (charges +1, -1) are never induced; SU(2)_e x SU(2)_o forbids light masses; a family-blind bidoublet gives m x 1',
      neutral == {'T3': True, 'O_A on f': True, "H'": True, 'bilinear f,g': False} and (-4) % 4 == 0)

# ===================================== D. 1+1D toy =====================================
print('== D. 1+1D toy (3 families of the R-a taste, each a 3-4-5-0 multiplet, z = q_a + k = 1)')
Kd = np.tile([1, 1, -1, -1], 3); tq = np.tile([3, 4, 5, 0], 3); fam = np.repeat(np.arange(3), 4)
l1, l2 = np.array([1, -2, 1, 2]), np.array([2, 1, -2, 1]); w1, w2 = np.array([1, 0, 1, 0]), np.array([0, 1, 0, 1])
def stv(v, j): o = np.zeros(12, int); o[4 * j:4 * j + 4] = v; return o
D8 = np.array([stv(w1, 0) - stv(w1, 1), stv(w1, 1) - stv(w1, 2), stv(w2, 0) - stv(w2, 1), stv(w2, 1) - stv(w2, 2),
               sum(stv(l1, j) for j in range(3)), sum(stv(l2, j) for j in range(3))])
def famnum(L): return [[int(v[fam == f].sum()) for f in range(3)] for v in L]
fnD8 = famnum(D8)
check('D1 [T] the families-mod-3 toy Lagrangian D8 has even family numbers: it keeps each family\'s parity',
      all(x % 2 == 0 for row in fnD8 for x in row) and np.abs(D8 @ np.diag(Kd) @ D8.T).max() == 0, str(fnD8).replace(' ', ''))
LR = np.array([[-1, -3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 0, -1, 1, 0, 0, 0, 0, 0], [0, -3, 3, 0, -1, 0, 0, 1, 0, 0, 0, 0],
               [-3, -14, 15, 0, -3, 1, 0, 0, -3, 1, 0, 0], [-3, -13, 14, 0, -3, 1, 0, 0, -3, 0, 1, 0], [0, -3, 3, 0, 0, 0, 0, 0, -1, 0, 0, 1]])
tau = [(fam == f).astype(int) for f in range(3)]
okLR = (np.abs(LR @ np.diag(Kd) @ LR.T).max() == 0 and not np.any(LR @ tq) and not np.any(LR @ (tau[0] - tau[1])) and not np.any(LR @ (tau[1] - tau[2]))
        and not np.any(LR.sum(1) % 3) and not np.any(LR.sum(1) % 2) and all(abs(smith_normal_form(Matrix(LR.tolist()))[i, i]) == 1 for i in range(6))
        and np.linalg.matrix_rank(LR.astype(float)) == 6 and all(len({x for x in row}) == 1 for row in famnum(LR)))
check('D2 [T] a Lagrangian gapping the three R-a tastes and keeping both relative family U(1)s exists (null; U(1)_e, Z3_k, '
      'translation neutral; Smith 1): the anomaly forces coupling, not mixing', okLR, str(famnum(LR)).replace(' ', ''))

# ===================================== E. finite three-family cluster =====================================
print('== E. finite cluster (supplied): 3 families x 4 doubler modes, T3 = g(O0 O1 O2 + h.c.), bidoublet b, L/R probes v')
def apply(ops, s):
    sign = 1
    for (m, dag) in reversed(ops):
        occ = (s >> m) & 1
        if dag == occ: return None
        if bin(s & ((1 << m) - 1)).count('1') % 2: sign = -sign
        s ^= (1 << m)
    return sign, s
def terms_cluster(NM, g, b, t, phi, idx, extra=()):
    T = []; ann = [(idx(f, m), False) for f in range(3) for m in range(NM)]
    T += [(g, ann), (g, [(m, True) for (m, _) in reversed(ann)])]
    h = NM // 2
    for f in range(3):
        for s in range(h): T += [(b, [(idx(f, s), True), (idx(f, h + s), False)]), (b, [(idx(f, h + s), True), (idx(f, s), False)])]
        if t:
            for m in range(NM):
                T += [(t * np.exp(1j * phi), [(idx(f, m), True), (idx((f + 1) % 3, m), False)]),
                      (t * np.exp(-1j * phi), [(idx((f + 1) % 3, m), True), (idx(f, m), False)])]
    return T + list(extra)
def block(T, L, Nset):
    st = [s for s in range(1 << L) if bin(s).count('1') in Nset]; pos = {s: i for i, s in enumerate(st)}
    H = np.zeros((len(st), len(st)), complex)
    for coef, ops in T:
        for i, s in enumerate(st):
            r = apply(ops, s)
            if r is not None and r[1] in pos: H[pos[r[1]], i] += coef * r[0]
    return H, st, pos
def cvec(m, dag, vec, st, pos_to, dim):
    out = np.zeros(dim, complex)
    for i, s in enumerate(st):
        if abs(vec[i]) > 1e-15:
            r = apply([(m, dag)], s)
            if r is not None and r[1] in pos_to: out[pos_to[r[1]]] += r[0] * vec[i]
    return out
idx4 = lambda f, m: 4 * f + m
def Mcluster(g, b, t, phi):
    T = terms_cluster(4, g, b, t, phi, idx4); B0 = block(T, 12, (0, 12)); B1 = block(T, 12, (1,)); B11 = block(T, 12, (11,))
    w0, v0 = np.linalg.eigh(B0[0]); gs, E0 = v0[:, 0], w0[0]; w1, v1 = np.linalg.eigh(B1[0]); w11, v11 = np.linalg.eigh(B11[0])
    def G(i, j):
        a = v1.conj().T @ cvec(i, True, gs, B0[1], B1[2], len(B1[1])); bb = v1.conj().T @ cvec(j, True, gs, B0[1], B1[2], len(B1[1]))
        a2 = v11.conj().T @ cvec(i, False, gs, B0[1], B11[2], len(B11[1])); b2 = v11.conj().T @ cvec(j, False, gs, B0[1], B11[2], len(B11[1]))
        return np.sum(a.conj() * bb / (E0 - w1)) + np.sum(b2.conj() * a2 / (w11 - E0))
    return np.array([[G(idx4(f, 0), idx4(fp, 2)) for fp in range(3)] for f in range(3)]), E0
def closed(g, b, t, phi):
    e = np.array([2 * t * np.cos(phi + TP3 * k) for k in range(3)]); return np.sort((b / 2) * (1 / ((g + e) ** 2 - b ** 2) + 1 / ((g - e) ** 2 - b ** 2)))
M0, _ = Mcluster(1.0, 0.0, 0.0, 0.0); Mb, E0b = Mcluster(1.0, 0.1, 0.0, 0.0)
check('E1 [F] exact Lehmann sums on 2^12 states (ground state (|0> - |F>)/sqrt2): b = 0 gives M = 0; b = 0.1 g gives '
      'M = b/(g^2-b^2) x 1: no mixing, three equal masses', nrm(M0) < 1e-14
      and nrm(Mb - 0.1 / 0.99 * np.eye(3)) < 1e-13 and abs(E0b + 1) < 1e-12, f'dev {nrm(Mb - 0.1 / 0.99 * np.eye(3)):.0e}')
# exact diagonalisation check on the reduced model (2 doubler modes per family + L, R probes), second order vs exact
def ed_check(v, g=1.0, b=0.1, t=0.05, phi=0.3):
    idx2 = lambda f, m: 2 * f + m; lt = lambda f, s: 6 + 2 * f + s
    ex = []
    for f in range(3):
        for s in range(2): ex += [(v, [(lt(f, s), True), (idx2(f, s), False)]), (v, [(idx2(f, s), True), (lt(f, s), False)])]
    Tr = terms_cluster(2, g, b, t, phi, idx2); Tf = Tr + ex
    Hh0, sth0, ph0 = block(Tr, 6, (0, 6)); Hh1, sth1, ph1 = block(Tr, 6, (1,)); Hh5, sth5, ph5 = block(Tr, 6, (5,))
    w0, v0 = np.linalg.eigh(Hh0); gs, E0 = v0[:, 0], w0[0]; w1, v1 = np.linalg.eigh(Hh1); w5, v5 = np.linalg.eigh(Hh5)
    def G(i, j):
        a = v1.conj().T @ cvec(i, True, gs, sth0, ph1, len(sth1)); bb = v1.conj().T @ cvec(j, True, gs, sth0, ph1, len(sth1))
        a2 = v5.conj().T @ cvec(i, False, gs, sth0, ph5, len(sth5)); b2 = v5.conj().T @ cvec(j, False, gs, sth0, ph5, len(sth5))
        return np.sum(a.conj() * bb / (E0 - w1)) + np.sum(b2.conj() * a2 / (w5 - E0))
    hv = [idx2(f, s) for f in range(3) for s in range(2)]
    Sig = v ** 2 * np.array([[G(i, j) for j in hv] for i in hv])
    HA, stA, pA = block(Tf, 12, (0, 6, 12)); HB, stB, pB = block(Tf, 12, (1, 7))
    ref = np.zeros(len(stA), complex)
    for i, s in enumerate(sth0): ref[pA[s]] = gs[i]
    wA, vA = np.linalg.eigh(HA); Eref = wA[np.argmax(abs(vA.conj().T @ ref))]
    wB, vB = np.linalg.eigh(HB); P1 = np.zeros((len(stB), 6), complex)
    for a_, (f, s) in enumerate([(f, s) for f in range(3) for s in range(2)]): P1[:, a_] = cvec(lt(f, s), True, ref, stA, pB, len(stB))
    wts = np.sum(abs(vB.conj().T @ P1) ** 2, 1); sel = np.sort(wB[np.argsort(wts)[-6:]]) - Eref
    return float(np.abs(sel - np.sort(np.linalg.eigvalsh(Sig))).max()), Sig
e1, Sg = ed_check(0.01); e2, _ = ed_check(0.02)
check('E2 [F] exact diagonalisation with the probes (reduced model): light addition energies = v^2 eig Sigma(0) + O(v^4)',
      e1 < 1e-6 and 12 < e2 / e1 < 20, f'residual {e1:.1e} at v = 0.01, x{e2 / e1:.1f} at 2v')
res = {}
for phi in (0.0, np.pi / 6, np.pi / 3, TP3, 0.3, 0.3 + TP3):
    M, _ = Mcluster(1.0, 0.1, 0.05, phi); ev = np.linalg.eigvals(M)
    circ = nrm(M - np.array([[M[0, (j - i) % 3] for j in range(3)] for i in range(3)]))
    res[round(phi, 6)] = (np.sort(ev.real), nrm(ev.imag), circ, nrm(M - M.conj().T))
deg = lambda x: min(abs(x[1] - x[0]), abs(x[2] - x[1])) < 1e-12
okE3 = (all(deg(res[round(p, 6)][0]) for p in (0.0, np.pi / 6, np.pi / 3, TP3)) and not deg(res[0.3][0])
        and nrm(res[0.3][0] - res[round(0.3 + TP3, 6)][0]) < 1e-13 and nrm(res[0.3][0] - closed(1, 0.1, 0.05, 0.3)) < 1e-13
        and max(v[1] + v[2] + v[3] for v in res.values()) < 1e-12)
check('E3 [T/F] a supplied family hop t e^(i phi): Hermitian circulant, m_k = (b/2) sum_+- 1/((g +- e_k)^2 - b^2), e_k = '
      '2t cos(phi + 2pi k/3); phi = 0, pi/6, pi/3 give a degenerate pair; the twist 2pi/3 per link is a gauge (flux 2pi)', okE3,
      f'phi = 0.3: {np.round(res[0.3][0], 6)}')
def catok(g, b, t, phi):                                   # T3's cat is the ground state iff -g lies below every other Fock level
    e = np.array([2 * t * np.cos(phi + TP3 * k) for k in range(3)]); o = np.concatenate([np.repeat(-b + e, 2), np.repeat(b + e, 2)])
    nneg = int((o < 0).sum()); cand = [o[o < 0].sum()] if 0 < nneg < 12 else []
    return -g < min(cand + [o.min(), -o.max()])
tg = [0.02, 0.05, 0.1]; rdv = [brannen(np.sqrt(closed(1, 0.1, t, 0.3))) for t in tg]
best = (0.0, None); T_, P_ = [a.ravel() for a in np.meshgrid(np.linspace(0, 0.6, 241), np.linspace(0, np.pi / 3, 61))]
E_ = 2 * T_[:, None] * np.cos(P_[:, None] + TP3 * np.arange(3)[None, :])
for b in np.linspace(0.001, 0.2, 120):                     # vectorised scan of the cat-ground-state region
    O_ = np.concatenate([-b + E_, -b + E_, b + E_, b + E_], 1); neg = np.where(O_ < 0, O_, 0).sum(1); nn_ = (O_ < 0).sum(1)
    low = np.minimum(np.where((nn_ > 0) & (nn_ < 12), neg, np.inf), np.minimum(O_.min(1), -O_.max(1))); ok_ = -1 < low
    Mk = (b / 2) * (1 / ((1 + E_) ** 2 - b ** 2) + 1 / ((1 - E_) ** 2 - b ** 2)); rr = np.where(ok_, Mk.max(1) / Mk.min(1), 0)
    j = int(np.argmax(rr))
    if rr[j] > best[0]: best = (rr[j], (b, T_[j], P_[j]))
bb_, tt_, pp_ = best[1]
T4 = terms_cluster(4, 1.0, bb_, tt_, pp_, idx4); Emin = min(np.linalg.eigvalsh(block(T4, 12, (N,) if N not in (0, 12) else (0, 12))[0])[0]
                                                    for N in range(12))
Mx, E0x = Mcluster(1.0, bb_, tt_, pp_)
check(f'E4 [F/E] the dial (r, delta) follows the supplied (t/g, phi, b/g), e.g. ' + ', '.join(f'({r:.0e}, {d:.3f})' for r, d in rdv)
      + f' at t/g = 0.02, 0.05, 0.1; while T3\'s cat stays the ground state the spread is m3/m1 <= {best[0]:.3f} (grid), vs 3477 for '
      'leptons: the poles that would make a hierarchy lie past a level crossing', all(catok(1, 0.1, t, 0.3) for t in tg)
      and best[0] < 1.3 and abs(Emin - E0x) < 1e-12 and nrm(np.sort(np.linalg.eigvalsh((Mx + Mx.conj().T) / 2)) - closed(1, bb_, tt_, pp_)) < 1e-12
      and not catok(1, 0.1, 0.5162, 0.5133))

# ===================================== F. spine reading (family-register) =====================================
print('== F. spine {x-d, x, x+d} of a zoom-3 block (family-register A2)')
x0 = np.zeros(3, int); dv = np.ones(3, int); spine = [tuple(-dv), tuple(x0), tuple(dv)]
stab = [Rm for Rm in rots if np.allclose(Rm @ dv, dv) or np.allclose(Rm @ dv, -dv)]
permimg = sorted({tuple(spine.index(tuple(int(v) for v in np.rint(Rm @ np.array(p)))) for p in spine) for Rm in stab})
three_cycle = any(len(set(p)) == 3 and p != (0, 1, 2) and all(p[i] != i for i in range(3)) for p in permimg)
def commdim(perms):
    Ps = [np.eye(3)[:, list(p)] for p in perms]; A = np.vstack([np.kron(np.eye(3), P.T) - np.kron(P, np.eye(3)) for P in Ps])
    return 9 - np.linalg.matrix_rank(A)
check('F1 [T] site stabiliser (3 turns about d, 3 tiling-swapping half-turns): spine fixed or ends swapped, no 3-cycle, so no '
      'circulant; commutant 5 (Z2) allows any three masses',
      len(stab) == 6 and permimg == [(0, 1, 2), (2, 1, 0)] and not three_cycle and commdim(permimg) == 5, str(permimg).replace(' ', ''))
mod = [(1, 1, 1), (3, 3, 3), (5, 5, 5)]; Tm = lambda p: tuple((v + 1) % 6 + 1 for v in p); Iv = lambda p: tuple(6 - v for v in p)
gen = [tuple(mod.index(Tm(p)) for p in mod), tuple(mod.index(Iv(p)) for p in mod)]
blind = sorted({tuple(mod.index(tuple(p[j] for j in [int(np.argmax(np.abs(Rm[i]))) for i in range(3)])) for p in mod) for Rm in rots})
cd = (commdim(blind), commdim(gen[:1]), commdim(gen))
check('F2 [T] moduli readings: sign-blind (family-register) commutant 9; a one-cube translation along d 3-cycles the spine '
      '(circulant, commutant 3, phase free); inversion or any k -> -k map adds the swap: S3, commutant 2, degenerate doublet',
      blind == [(0, 1, 2)] and gen == [(1, 2, 0), (2, 1, 0)] and cd == (9, 3, 2), str(tuple(int(x) for x in cd)))
Sst = [coh32(dv), coh32(-dv), coh32(dv)]                                    # site states: x-d and x+d along +d, x along -d
Gsp = np.array([[abs(Sst[i].conj() @ Sst[j]) for j in range(3)] for i in range(3)]); egs = np.sort(np.linalg.eigvalsh(Gsp))
Wc = [nrm(np.linalg.matrix_power(W, n)[0, 7]) for n in (1, 2, 3)]
nn = [brannen(np.linalg.eigvalsh(np.array([[1, u, 0], [u, 1, u], [0, u, 1]]))) for u in (0.1, 0.3, 0.5)]
check('F3 [T/F] geometric couplings: one cube\'s tick never joins x to x+d (W^2 = 1): equal |m|; spin-3/2 site-state Gram, '
      'eigenvalues (2,1,0): m_e = 0, Q = 5/9; nearest-neighbour spine coupling, equal on-site: delta = pi/6 for every coupling',
      max(Wc) < 1e-12 and np.allclose(egs, [0, 1, 2]) and abs(Qk(egs ** 2) - 5 / 9) < 1e-12 and all(abs(d - np.pi / 6) < 1e-12 for _, d in nn),
      f'r = 2u^2/3')
def law(u, k): return brannen(np.linalg.eigvalsh(np.array([[1, u, u ** k], [u, 1, u], [u ** k, u, 1]])))
lawres = {}
for k in (2, 4):
    uh = brentq(lambda u: law(u, k)[0] - 0.5, 0.5, 0.95); lawres[k] = (uh, law(uh, k)[1], ratios_rd(0.5, law(uh, k)[1]))
check('F4 [F/E] distance laws u^(r/sqrt3), u^((r/sqrt3)^2) reach r = 1/2 at u = ' + ', '.join(f'{v[0]:.4f}' for v in lawres.values())
      + ' with delta = ' + ', '.join(f'{v[1]:.4f}' for v in lawres.values()) + f' vs {DT:.4f}: m_mu/m_e '
      + ', '.join(f'{v[2][0]:.1f}' for v in lawres.values()) + f' vs {R1:.1f}', all(abs(v[1] - DT) > 1e-3 for v in lawres.values()))

# ===================================== G. dynamical phases, look-elsewhere =====================================
print('== G. dynamical delta and look-elsewhere')
def chain(fn, km):
    b = np.sqrt([fn(k) for k in range(1, km + 1)]); return np.linalg.eigvalsh(np.diag(b, 1) + np.diag(b, -1)).max()
lg = chain(lambda k: 16 * k * (9 - k) * (k + 4) * (13 - k), 8)
LV = dict(E0=lg, D=lg - chain(lambda k: 16 * k * (8 - k) * (k + 5) * (13 - k), 7), Df=lg - chain(lambda k: 16 * k * (8 - k) * (k + 4) * (13 - k), 7),
          D54=lg - chain(lambda k: 16 * k * (7 - k) * (k + 6) * (13 - k), 6))
lam = symbols('lam'); algok = True
for fn, km in ((lambda k: 16 * k * (9 - k) * (k + 4) * (13 - k), 8), (lambda k: 16 * k * (8 - k) * (k + 5) * (13 - k), 7),
               (lambda k: 16 * k * (8 - k) * (k + 4) * (13 - k), 7), (lambda k: 16 * k * (7 - k) * (k + 6) * (13 - k), 6)):
    n_ = km + 1; Jt = Matrix.zeros(n_, n_)
    for k in range(1, km + 1): Jt[k - 1, k] = 1; Jt[k, k - 1] = fn(k)          # same char. polynomial as the symmetric chain
    algok &= all(c.is_integer for c in Poly(Jt.charpoly(lam).as_expr(), lam).all_coeffs())
sx_ = np.array([[0, 1], [1, 0]], complex); sy_ = np.array([[0, -1j], [1j, 0]]); sz_ = np.diag([1., -1]).astype(complex)
def c12(n): n = np.asarray(n, float) / np.linalg.norm(n); w_, v_ = np.linalg.eigh(n[0] * sx_ + n[1] * sy_ + n[2] * sz_); return v_[:, -1], v_[:, 0]
nP, nM = c12([1, 1, 1]); AX = [c12(e)[0] for e in np.eye(3)]; RP, RMm = np.outer(nP, nP.conj()), np.outer(nM, nM.conj())
def gram(t):
    Mx = np.array([[nP.conj() @ np.outer(AX[a], AX[a].conj()) @ (RP + t * RMm) @ np.outer(AX[b], AX[b].conj()) @ nP for b in range(3)] for a in range(3)])
    z = Mx[0, 1] / Mx[0, 0]; return abs(z) ** 2, fold(np.angle(z)), Mx
t1, t2 = brentq(lambda t: gram(t)[0] - 0.5, 0.5, 1.5), brentq(lambda t: gram(t)[0] - 0.5, 5, 30)
ts = brentq(lambda t: gram(t)[1] - DT, 0.5, 0.99); rs = gram(ts)[0]
gq = [gram(LV['D'] / LV['Df'])[:2], gram(LV['Df'] / LV['D'])[:2]]
check(f'G1 [F] two-channel Clifford Gram (mass-law states; intermediate spin along +-d weighted 1, t): circulant; r = 1/2 only at '
      f't = 1, 7 + 4sqrt3, both delta = pi/12; delta = {DT:.4f} needs t = {ts:.4f}, r = {rs:.4f} (Q = {1 / 3 + 2 * rs / 3:.4f}); '
      f't = Delta/Delta_f, Delta_f/Delta: ({gq[0][0]:.3f}, {gq[0][1]:.3f}), ({gq[1][0]:.3f}, {gq[1][1]:.3f})', abs(t1 - 1) < 1e-10 and abs(t2 - 7 - 4 * np.sqrt(3)) < 1e-9 and abs(gram(t1)[1] - np.pi / 12) < 1e-12
      and abs(gram(t2)[1] - np.pi / 12) < 1e-12 and nrm(gram(0.37)[2] - np.roll(np.roll(gram(0.37)[2], 1, 0), 1, 1)) < 1e-14 and abs(rs - 0.5) > 0.04)
check('G2 [T] the smg levels are roots of integer polynomials and the kinematic phases lie in (pi/12)Z: every candidate c1 is '
      'algebraic, so none gives delta = 2/9 exactly (Lindemann-Weierstrass, cited)',
      algok, ', '.join(f'{k} {v:.4f}' for k, v in LV.items()))
vals, names = [], []
lv = list(LV.items()); X = [(f'{a}/{b}', x / y) for (a, x), (b, y) in itertools.permutations(lv, 2)]
for (nx, x) in X:
    for al in range(8):
        for ga in range(24):
            vals.append(fold(al * np.pi / 12 + np.angle(1 + x * np.exp(1j * ga * np.pi / 12)))); names.append(f'{al}pi/12+arg(1+{nx} e^(i{ga}pi/12))')
    for sgn in (1, -1):
        vals.append(gram(sgn * x)[1]); names.append(f'Gram t={sgn}{nx}')
    for n in range(1, 13):
        for fn_, lab in ((lambda v: v * np.pi, 'pi'), (lambda v: v, '1'), (lambda v: np.arctan(v), 'atan')):
            vals.append(fold(fn_(x) / n)); names.append(f'{lab}({nx})/{n}')
    for k in (2, 4):
        if x < 1:
            vals.append(law(x, k)[1]); names.append(f'spine law k={k} u={nx}')
vals = np.array(vals); dmin = np.abs(vals - DT); ib = int(np.argmin(dmin))
rng = np.random.default_rng(7); tgt = rng.uniform(0, np.pi / 3, 4000); vs = np.sort(vals); ii = np.clip(np.searchsorted(vs, tgt), 1, len(vs) - 1)
dr = np.minimum(np.abs(vs[ii] - tgt), np.abs(vs[ii - 1] - tgt))
pval = float(np.mean(dr <= dmin[ib]))
check(f'G3 [E] look-elsewhere over {len(vals)} candidate deltas (smg levels, (pi/12)Z phases, Gram, spine laws): closest '
      f'{names[ib]} = {vals[ib]:.10f}, off by {dmin[ib]:.1e} = {dmin[ib] / sDT:.0e} sigma; random targets do as well with p = {pval:.2f}', dmin[ib] / sDT > 1e3 and pval > 0.05)

# ===================================== H. quarks and mixing =====================================
print('== H. quarks and mixing')
QS = dict(up=(2.16, 1270., 172690.), down=(4.67, 93.4, 4180.))
QB = dict(up=[(2.16, .26, .49), (1270., 20., 20.), (172690., 300., 300.)], down=[(4.67, .17, .48), (93.4, 3.4, 8.6), (4180., 20., 30.)])
def Qbox(s):
    qs = [Qk([m + (hi if e else -lo) for (m, lo, hi), e in zip(QB[s], es)]) for es in itertools.product((0, 1), repeat=3)]; return min(qs), max(qs)
rl, ru, rd_ = brannen(np.sqrt([me, mmu, mtau]) ** 1)[0], brannen(np.sqrt(QS['up']))[0], brannen(np.sqrt(QS['down']))[0]
gapQ = Qbox('up')[0] - Qbox('down')[1]
check(f'H1 [T/E] gap term and dressing keep SU(4) x SU(2)^2: one family matrix, one r for all species (Schur); measured r = '
      f'{rl:.3f}, {rd_:.3f}, {ru:.3f} (lepton, down, up), Q_up - Q_down >= {gapQ:.3f} over the PDG box: excluded',
      gapQ > 0.1 and abs(ru - rd_) > 0.1)
Fm = np.array([[OM ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
Cu = 0.6 * np.eye(3) + 0.3 * np.roll(np.eye(3), 1, 1) * np.exp(0.2j); Cu = Cu + Cu.conj().T
Cd = 0.4 * np.eye(3) + 0.25 * np.roll(np.eye(3), 1, 1) * np.exp(-0.7j); Cd = Cd + Cd.conj().T
Uu, Ud = np.linalg.eigh(Cu)[1], np.linalg.eigh(Cd)[1]; Vck = np.abs(Uu.conj().T @ Ud)
perm_ok = np.allclose(np.sort(Vck.ravel()), [0] * 6 + [1] * 3, atol=1e-10); Vus, sVus = 0.22501, 0.00068
check(f'H2 [T/E] circulants share the Fourier basis: CKM a permutation, |V_us| = 0 vs {Vus}({sVus * 1e5:.0f}), {Vus / sVus:.0f} '
      'sigma; T3 alone keeps each N_f mod 4: CKM = PMNS = 1 at all orders, vs measured oscillations', perm_ok and np.allclose(np.abs(Fm.conj().T @ Cu @ Fm) - np.diag(np.diag(np.abs(Fm.conj().T @ Cu @ Fm))), 0, atol=1e-12))
lam_d, lam_e = np.array([1.0, -2.0, 30.0]), np.array([0.3, 5.0, 60.0])
A_ = (3 * lam_d + lam_e) / 4; B_ = (lam_d - lam_e) / 4
check('H3 [T] colour splits r only via a second supplied matrix: a (15,2,2) gives M_d = Y1 + Y15, M_e = Y1 - 3 Y15, which fit any '
      'd and e spectra (6 for 6)', np.allclose(A_ + B_, lam_d) and np.allclose(A_ - 3 * B_, lam_e))

print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: B1, C1-C3, D1-D2, F1-F2, G2, H3; finite: E1-E4, F3, G1; estimates vs measurement: A1, E4, F4, G3, H1-H2.')
print('supplied: H\', O_A, k = 2, the (4,2) content, 3 stacked families, g, b, v, the hop (t, phi), Gram weights, spine laws; PDG/CODATA.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
