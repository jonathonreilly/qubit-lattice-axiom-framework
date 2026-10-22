#!/usr/bin/env python3
"""Electroweak on the candidate-law tick: when SU(2) is exact, the weak-decay test, breaking without a scalar, the hierarchy.
Supplied model; finite diagnostics; no physical identification.  Labels: [T] theorem or exact finite check, [M] comparison
with measurement, [E] estimate with supplied comparator inputs.
 A  exact SU(2) on the CL-2 tick: closed form of the sublattice commutator; one-body commutants; content at step pi/2;
    the copy factor; inversion; the Spin(10) pair-square mirror term and the group CL-5 would then link
 B  decay test: Yang-Mills fixes every multiplet's charge scale (sympy); contact-limit rate from Dirac traces and exact
    phase space; Michel parameters of chiral and vector-like links; tau/mu universality ratio; the W-mass floor
 C  breaking without a fundamental scalar: rho from condensates; left-right links; dN = 4 condensates; NJL top
    condensate (tick gap equation, Pagels-Stokar, compositeness RG); QCD-induced breaking
 D  hierarchy: one-loop transmutation, b0 on the content, scales from measured couplings, naturalness
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/CUBE_TICK_KEEPS_A_CHIRAL_WEAK_SU2_ONLY_AT_STEP_HALF_PI_WITH_NO_SPECIES_MASS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.linalg import expm, logm, null_space
from scipy.integrate import solve_ivp

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
rng = np.random.default_rng(20261021)
OM = np.exp(2j * np.pi / 3)

# ------------------------------------------- supplied CL-2 tick (one species, Bloch form) -------------------------------------------
C8 = np.array(list(itertools.product((0, 1), repeat=3))); c8 = C8 - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def img(R, i): return int(np.argmin(np.sum(abs(c8 - R @ c8[i]), 1)))
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
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def Lrot(R):
    n_, a_ = axang(R); Dm = expm(-1j * a_ * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
Ls = [Lrot(R) for R in rots]
iC3 = [i for i, R in enumerate(rots) if int(round(np.trace(R))) == 0 and np.allclose(axang(R)[0], np.ones(3) / np.sqrt(3))][0]
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C8[a] - C8[b])) == 1: g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / np.sqrt(3)
I8 = np.eye(8); S = np.diag((-1.0) ** C8.sum(1)).astype(complex)                 # sublattice sign
def Dg(K): return np.diag(np.exp(1j * (C8 @ K)))
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W                          # exp(i th W), W^2 = 1
def U(K, st, mu=0.0, F=None):                                                    # odd half-tick after even half-tick
    Ue = ex(-(st - mu / 2)); Uod = Dg(K).conj().T @ ex(st + mu / 2) @ Dg(K)
    if F is not None: Ue = F @ Ue @ F; Uod = Dg(K).conj().T @ F @ Dg(K) @ Uod @ Dg(K).conj().T @ F @ Dg(K)
    return Uod @ Ue
KR = rng.uniform(-np.pi, np.pi, (12, 3))
def light_algebra(f, h=1e-5):
    def H(q): return 1j * logm(f(q))
    al = []
    for a in range(3):
        e = np.zeros(3); e[a] = h; A = (H(e) - H(-e)) / (2 * h); al.append((A + A.conj().T) / 2)
    v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); return [A / v for A in al], v
def copy_projectors(al):                       # copies told apart by the internal part of a three-fold turn (CL-2)
    Sig = [-1j * al[1] @ al[2], -1j * al[2] @ al[0], -1j * al[0] @ al[1]]; L = Ls[iC3]
    Mr = np.array([[np.trace(L @ al[a] @ L.conj().T @ al[b]).real / 8 for b in range(3)] for a in range(3)])
    n_, ang = axang(np.round(Mr).T); best = None
    for s_ in (1, -1):
        Sm = expm(-1j * s_ * ang / 2 * sum(n_[k] * Sig[k] for k in range(3)))
        e_ = max(nrm(Sm @ al[q] @ Sm.conj().T - L @ al[q] @ L.conj().T) for q in range(3))
        if best is None or e_ < best[0]: best = (e_, Sm)
    rho = best[1].conj().T @ L; w_, V = np.linalg.eig(rho); P = {}
    for q, lam in ((1, OM), (2, OM ** 2)):
        Vl = V[:, np.abs(w_ - lam) < 1e-5]; Pq = Vl @ np.linalg.pinv(Vl); P[q] = (Pq + Pq.conj().T) / 2
    return P
def commutant_dim(mats, n=8):
    A = np.vstack([np.kron(np.eye(n), X.T) - np.kron(X, np.eye(n)) for X in mats]); return null_space(A, rcond=1e-9).shape[1]

print('== A. which rule keeps a weak SU(2) exact on the CL-2 tick')
worst, cms = 0.0, {}
for st, mu in ((0.3, 0.1), (0.04, 0.0), (1.2, 0.5), (np.pi / 2, 0.0), (np.pi / 2, 0.2)):
    to, te = st + mu / 2, st - mu / 2
    for K in KR[:4]:
        Uk = U(K, st, mu); Wo = Dg(K).conj().T @ W @ Dg(K)
        worst = max(worst, nrm(Uk - S @ Uk @ S - 2j * (np.sin(to) * np.cos(te) * Wo - np.cos(to) * np.sin(te) * W)))
    cms[(round(st, 2), mu)] = max(nrm(S @ U(K, st, mu) - U(K, st, mu) @ S) for K in KR)
others = min(v for k, v in cms.items() if k != (1.57, 0.0))
check('A1 [T] U - sUs = 2i(sin th_o cos th_e W_o(K) - cos th_o sin th_e W_e), th = eps +- mu/2: the sublattice sign s '
      'commutes with the tick iff eps = pi/2 and mu = 0',
      worst < 1e-12 and cms[(1.57, 0.0)] < 1e-12 and others > 0.05, f'residual {worst:.0e}; |[s,U]| {cms[(1.57, 0.0)]:.0e} vs >= {others:.2f}')
dims = [commutant_dim([U(K, st, mu) for K in KR]) for st, mu in ((np.pi / 2, 0), (np.pi / 2, .2), (.3, 0), (.3, .2), (.04, 0), (.04, .01))]
dmu = nrm(U(KR[0], 0.04, 0.010) - U(KR[0], 0.04, 0.012))
check('A2 [T] one-body commutant: span{1,s} at (pi/2, 0), scalars otherwise %s. With the (4,2) cell index in parallel: '
      'U(8)_even x U(8)_odd at (pi/2, 0), else one U(8) acting alike on both chiralities (g_A = 0); masses leave prod U(n_k), '
      'so T+ x 1 needs m_nu = m_e, m_u = m_d' % dims,
      dims == [2, 1, 1, 1, 1, 1] and dmu > 1e-4, f'|U(mu=.010) - U(mu=.012)| = {dmu:.1e}')
al, v = light_algebra(lambda K: U(K, np.pi / 2)); P = copy_projectors(al); s3 = P[1] - P[2]
g5 = 1j * al[0] @ al[1] @ al[2]; g5 = (g5 + g5.conj().T) / 2; PL, PR, Pp = (I8 - g5) / 2, (I8 + g5) / 2, (I8 + S) / 2
cont = [round(np.trace(Pp @ X).real, 6) + 0.0 for X in (PL @ P[1], PL @ P[2], PR @ P[1], PR @ P[2])]
check('A3 [T] at step pi/2: s = -g5 s3 on the light algebra, and the s = +1 cells hold (L, copy w) + (R, copy w^2): an SU(2) '
      'acting as T x (1+s)/2 links one copy\'s L and the other copy\'s R', nrm(S + g5 @ s3) < 1e-8 and cont == [2, 0, 0, 2],
      'traces (L1, L2, R1, R2) on s=+1: ' + ' '.join(f'{c_:.0f}' for c_ in cont))
cf = {M: max(nrm(S @ U(K, np.pi / 2, 0, expm(1j * M * P[1] @ W / 2)) - U(K, np.pi / 2, 0, expm(1j * M * P[1] @ W / 2)) @ S) for K in KR)
      for M in (0.5, 1.0, np.pi)}
check('A4 [T] CL-2\'s copy factor exp(i M P W/2) breaks s at step pi/2 (a copy mass is s-odd; only M = pi, a pi-shift, '
      'keeps it): CL-2 as written has no chiral SU(2) at any step', cf[0.5] > 0.1 and cf[1.0] > 0.1 and cf[np.pi] < 1e-8,
      f'|[s,U]| = {cf[0.5]:.2f}, {cf[1.0]:.2f}, {cf[np.pi]:.0e} at M = .5, 1, pi')
A_ = np.vstack([np.kron(I8, U(K, .3, .2).T) - np.kron(U(-K, .3, .2), I8) for K in KR]); Vi = null_space(A_, rcond=1e-9)
Vi = Vi[:, 0].reshape(8, 8); Vi = Vi / np.sqrt(np.trace(Vi @ Vi.conj().T).real / 8)
inv_ok = nrm(Vi @ Vi.conj().T - I8) < 1e-10 and max(nrm(Vi @ U(K, np.pi / 2) @ Vi.conj().T - U(-K, np.pi / 2)) for K in KR) < 1e-10
check('A5 [T] the block inversion V (V U(K) V+ = U(-K), unique, also at step pi/2) has V s V+ = -s: it swaps SU(2)_even and '
      'SU(2)_odd, so if both are linked their couplings are equal, g_L = g_R', inv_ok and nrm(Vi @ S @ Vi.conj().T + S) < 1e-10)
# Spin(10) pair square on the mirror 16: P_M = sum B^M_ab psi_a,up psi_b,dn (Lorentz scalar), O = sum_M P_M P_M
sz2 = np.diag([1., -1]).astype(complex); am = np.array([[0, 1], [0, 0]], complex)
def kr(*ops):
    M_ = np.array([[1.0 + 0j]])
    for o in ops: M_ = np.kron(M_, o)
    return M_
aa = [kr(*([sz2] * i + [am] + [np.eye(2)] * (4 - i))) for i in range(5)]
Gam = []
for i in range(5): Gam += [aa[i] + aa[i].conj().T, 1j * (aa[i].conj().T - aa[i])]
occ = np.array(list(itertools.product((0, 1), repeat=5))); ev = np.where(occ.sum(1) % 2 == 0)[0]
Cc = Gam[0] @ Gam[2] @ Gam[4] @ Gam[6] @ Gam[8]
Bm = np.array([(Cc @ Gam[M])[np.ix_(ev, ev)] for M in range(10)])
Tt = np.einsum('mab,mcd->abcd', Bm, Bm)
fz = Tt + np.einsum('abcd->acbd', Tt) + np.einsum('abcd->adcb', Tt)
TA = (Tt - np.einsum('abcd->cbad', Tt) - np.einsum('abcd->adcb', Tt) + np.einsum('abcd->cdab', Tt)) / 4
rows = []
for _ in range(700):
    u1, v1, w1, y1 = (rng.normal(size=16) + 1j * rng.normal(size=16) for _ in range(4))
    gg = [np.einsum('ebcd,b,c,d->e', TA, v1, w1, y1), np.einsum('aecd,a,c,d->e', TA, u1, w1, y1),
          np.einsum('abed,a,b,d->e', TA, u1, v1, y1), np.einsum('abce,a,b,c->e', TA, u1, v1, w1)]
    rows.append(sum(np.outer(gq, uq) for gq, uq in zip(gg, (u1, v1, w1, y1))).reshape(-1))
Rm = np.array(rows); svR = np.linalg.svd(Rm, compute_uv=False); stab = int(np.sum(svR / svR[0] < 1e-9))
blk = (occ[ev][:, 3] + occ[ev][:, 4]) % 2; ia, ib = np.where(blk == 0)[0], np.where(blk == 1)[0]
mask = np.zeros((16, 16), bool); mask[np.ix_(ia, ib)] = True; mask[np.ix_(ib, ia)] = True
sv2 = np.linalg.svd(np.vstack([Rm / svR[0], np.eye(256)[mask.reshape(-1)]]), compute_uv=False); stab_blk = int(np.sum(sv2 < 1e-9))
u1_out = min(np.abs(Rm @ np.diag([t[0] if b_ == 0 else t[1] for b_ in blk]).astype(complex).reshape(-1)).max() / svR[0]
             for t in ((1, 0), (0, 1), (1, 1), (1, -1)))
check('A6 [T] mirror term = Spin(10) pair square on the mirror 16 = 8_odd + 8bar_even (Grassmann, two spin components; the '
      'commuting square vanishes by Fierz): stabiliser in gl(16) = 45 = so(10); inside u(8)_e + u(8)_o it is 21 = '
      'su(4)+su(2)+su(2), no U(1): CL-5 would link exactly Pati-Salam, no species-number link',
      nrm(fz + np.einsum('abcd->abdc', fz)) < 1e-12 and nrm(TA) > 1 and stab == 45 and stab_blk == 21 and u1_out > 0.1,
      f'dims {stab}, {stab_blk}; block-U(1) residual >= {u1_out:.2f}')
bmax = {st: max(np.abs(np.angle(np.linalg.eigvals(U(K, st)))).max() for K in np.vstack([KR, np.full((1, 3), np.pi)])) for st in (np.pi / 2, 0.037)}
check('A7 [E] cost: at step pi/2 the band reaches quasi-energy pi (massless charged pi-cone) vs the vacuum bound eps < 0.037 '
      '(band top 0.074): the sublattice route conflicts with vacuum stability; a Xi-graded wall keeps U(8)_A x U(8)_B exact '
      'at small step by its block structure (cited, chiral-wall A6/A9)',
      abs(bmax[np.pi / 2] - np.pi) < 1e-9 and bmax[0.037] < 0.075, f'band max {bmax[np.pi / 2]:.4f}, {bmax[0.037]:.4f}')

print('== B. decay test: degenerate doublets, a W link, and measured weak decays')
x = sp.symbols('x', real=True); gs, lam = sp.symbols('g lambda', positive=True)
al_ = [sp.Function(f'a{k}')(x) for k in range(3)]; Af = [sp.Function(f'A{k}')(x) for k in range(3)]
psi = sp.Matrix([sp.Function('p0')(x), sp.Function('p1')(x)])
Tm = [sp.Matrix([[0, 1], [1, 0]]) / 2, sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2, sp.Matrix([[1, 0], [0, -1]]) / 2]
def dot(c, Ms): return sum((c[k] * Ms[k] for k in range(3)), sp.zeros(2, 2))
dA = [al_[a].diff(x) / gs - sum(sp.LeviCivita(a, b, c) * al_[b] * Af[c] for b in range(3) for c in range(3)) for a in range(3)]
Tl = [lam * t for t in Tm]; dpsi = sp.I * dot(al_, Tl) * psi
lhs = dpsi.diff(x) - sp.I * gs * dot(dA, Tl) * psi - sp.I * gs * dot(Af, Tl) * dpsi
rhs = sp.I * dot(al_, Tl) * (psi.diff(x) - sp.I * gs * dot(Af, Tl) * psi)
resid = sp.expand(lhs - rhs - sp.I * gs * lam * (1 - lam) * dot([sum(sp.LeviCivita(a, b, c) * al_[b] * Af[c] for b in range(3) for c in range(3)) for a in range(3)], Tm) * psi)
check('B1 [T] a doublet with generators lam T^a keeps D = d - i g A.(lam T) covariant only for lam = 1 (defect '
      'i g lam(1-lam) eps^abc a^b A^c T^a psi, sympy): a non-abelian link gives every doublet one g; a U(1) link would not', all(sp.simplify(e) == 0 for e in resid))
# Dirac traces and exact three-body phase space
I2 = np.eye(2); Z2 = np.zeros((2, 2)); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); szz = np.diag([1., -1]).astype(complex)
G0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex); Gi = [np.block([[Z2, s_], [-s_, Z2]]) for s_ in (sx, sy, szz)]
Gs = np.array([G0] + Gi); G5 = 1j * G0 @ Gi[0] @ Gi[1] @ Gi[2]; I4 = np.eye(4); eta = np.array([1., -1, -1, -1])
def slash(p): return np.einsum('...m,mab->...ab', p * eta, Gs)
VTX = {'V-A': np.array([Gs[a] @ (I4 - G5) for a in range(4)]), 'V': Gs.copy()}
def msq(p, s, k, q1, q2, m, me, kind, pol):
    V_ = VTX[kind]; Bv = np.array([G0 @ v_.conj().T @ G0 for v_ in V_])
    Pm = slash(p) + m * I4; Pm = Pm @ (I4 + G5 @ slash(s)) / 2 if pol else Pm / 2
    L1 = np.einsum('...ij,ajk,...kl,bli->...ab', slash(q2), V_, Pm, Bv)
    L2 = np.einsum('...ij,ajk,...kl,bli->...ab', slash(k) + me * I4, V_, slash(q1), Bv)
    return np.real(np.einsum('...ab,a,b,...ab->...', L1, eta, eta, L2)) / 2          # per G^2
def boost(q, Q):
    b = Q[..., 1:] / Q[..., :1]; b2 = np.sum(b ** 2, -1, keepdims=True); gam = 1 / np.sqrt(1 - b2)
    bq = np.sum(b * q[..., 1:], -1, keepdims=True); E = gam[..., 0] * (q[..., 0] + bq[..., 0])
    return np.concatenate([E[..., None], q[..., 1:] + ((gam - 1) * bq / np.maximum(b2, 1e-300) + gam * q[..., :1]) * b], -1)
ct_, wt_ = np.polynomial.legendre.leggauss(6); ph_ = 2 * np.pi * (np.arange(8) + 0.5) / 8
NS = np.stack([np.outer(np.sqrt(1 - ct_ ** 2), np.cos(ph_)), np.outer(np.sqrt(1 - ct_ ** 2), np.sin(ph_)), np.outer(ct_, np.ones(8))], -1).reshape(-1, 3)
WN = np.outer(wt_, np.full(8, 2 * np.pi / 8)).reshape(-1)
def spectrum(m, me, kind='V-A', pol=True, nE=20, nc=2, MW=None):
    """d2Gamma/(dE dcos theta_e)/G^2 for mu- -> e- nubar_e nu_mu, muon spin +z (contact or W propagator)"""
    Emax = (m * m + me * me) / (2 * m); xs, ws = np.polynomial.legendre.leggauss(nE)
    E = (Emax - me) / 2 * xs + (Emax + me) / 2; wE = ws * (Emax - me) / 2; cs, wc = np.polynomial.legendre.leggauss(nc)
    out = np.zeros((nE, nc)); p = np.array([m, 0, 0, 0.]); s = np.array([0, 0, 0, 1.])
    for i, e in enumerate(E):
        kk = np.sqrt(max(e * e - me * me, 0))
        for j, cth in enumerate(cs):
            k = np.array([e, kk * np.sqrt(1 - cth * cth), 0, kk * cth]); Q = p - k; MQ = np.sqrt(Q[0] ** 2 - np.sum(Q[1:] ** 2))
            q1s = np.concatenate([np.full((len(NS), 1), MQ / 2), MQ / 2 * NS], 1); q2s = q1s.copy(); q2s[:, 1:] *= -1
            Qb = np.broadcast_to(Q, q1s.shape); q1, q2 = boost(q1s, Qb), boost(q2s, Qb); kb = np.broadcast_to(k, q1.shape)
            M2 = msq(p, s, kb, q1, q2, m, me, kind, pol)
            if MW is not None:
                QW = kb + q1; M2 = M2 * (MW ** 2 / (MW ** 2 - (QW[:, 0] ** 2 - np.sum(QW[:, 1:] ** 2, 1)))) ** 2
            out[i, j] = (kk * e * 2 * np.pi) / (2 * m * (2 * np.pi) ** 3 * 2 * e * 32 * np.pi ** 2) * np.sum(WN * M2)
    return E, wE, cs, wc, out
def total(m, me=0.0, **kw):
    E, wE, cs, wc, out = spectrum(m, me, pol=False, **kw); return float(np.sum(wE[:, None] * wc[None, :] * out))
ref = lambda m: m ** 5 / (192 * np.pi ** 3)
fx = lambda z: 1 - 8 * z + 8 * z ** 3 - z ** 4 - 12 * z ** 2 * np.log(z)
me_, mmu, mtau = 0.51099895e-3, 0.1056583755, 1.77686
G1, G2 = total(1.0), total(2.0); fnum = total(mmu, me_, nE=160) / ref(mmu)
check('B2 [T] contact limit (V-A): Gamma = G^2 m^5/(192 pi^3) f(m_e^2/m^2) from Dirac traces and exact phase space; m^5 '
      'exact; f reproduced at m_e/m_mu', abs(G1 / ref(1) - 1) < 1e-10 and abs(G2 / G1 - 32) < 1e-8
      and abs(fnum - fx((me_ / mmu) ** 2)) < 1e-8, f'{G1 / ref(1):.12f}, x{G2 / G1:.6f}, f {fnum:.8f}')
def michel(kind):
    E, wE, cs, wc, out = spectrum(1.0, 0.0, kind); xx = 2 * E; iso = out @ wc / 2; asy = (out * cs[None, :]) @ wc * 1.5
    Mf = np.stack([1 - xx, 4 * xx - 3], 1); A, B = np.linalg.lstsq(Mf, iso / xx ** 2, rcond=None)[0]; Ap, Bp = np.linalg.lstsq(Mf, asy / xx ** 2, rcond=None)[0]
    return 9 * B / (2 * A), -3 * Ap / A, (3 * Bp / (2 * Ap) if abs(Ap) > 1e-9 else 0.0)     # xi sign: mu- convention
rVA, rV = michel('V-A'), michel('V')
rho_m, srho, xi_m, sxi = 0.74977, 0.00026, 1.0009, 0.0016
check('B3 [T/M] Michel: chiral link (V-A) gives rho, xi, delta = %.4f, %.4f, %.4f; a vector-like link (pure V, A2 at small step) '
      'gives %.4f, %.4f; measured 0.74977(26), 1.0009(16): vector-like off by %.0f and %.0f sigma' % (*rVA, rV[0], round(rV[1], 6) + 0.0,
      (rho_m - rV[0]) / srho, (xi_m - rV[1]) / sxi), np.allclose(rVA, [0.75, 1, 0.75], atol=1e-9) and np.allclose(rV[:2], [0.375, 0], atol=1e-9))
tmu, ttau, sttau, Be, sBe, smt = 2.1969811e-6, 290.3e-15, 0.5e-15, 0.1782, 0.0004, 0.00012
Rmeas = tmu * Be / ttau * (mmu / mtau) ** 5; sR = Rmeas * np.sqrt((sttau / ttau) ** 2 + (sBe / Be) ** 2 + (5 * smt / mtau) ** 2)
MW0 = 80.3692; rW = lambda m, MW: total(m, MW=MW) / total(m)
rWt = rW(mtau, MW0); rWm = 1 + 0.6 * (mmu / MW0) ** 2
rc = lambda a: 1 + a / (2 * np.pi) * (25 / 4 - np.pi ** 2)
Rpred = fx((me_ / mtau) ** 2) / fx((me_ / mmu) ** 2) * rWt / rWm * rc(1 / 133.4) / rc(1 / 135.90)
check('B4 [M] tau/mu universality: one g and m^5 predict (tau_mu/tau_tau) B_e (m_mu/m_tau)^5 = %.5f (phase space, W propagator %.6f '
      'numeric, QED); measured %.4f +- %.4f: pull %.1f sigma' % (Rpred, rWt, Rmeas, sR, (Rmeas - Rpred) / sR), abs(Rmeas - Rpred) < 2 * sR)
lo, hi = 3.0, 80.0
for _ in range(14):
    md = np.sqrt(lo * hi); Rx = Rpred / rWt * rW(mtau, md)
    if Rx > Rmeas + 2 * sR: lo = md
    else: hi = md
gW, fpi = 0.6517, 0.0921; MWqcd = gW * fpi * np.sqrt(3) / 2
check('B5 [M] m^5 needs a heavy W: the ratio alone gives M_W > %.1f GeV (2 sigma); colour-only breaking (M_W = g f_pi '
      'sqrt3/2 = %.0f MeV < m_mu) makes the W real and rates ~m^3, off by (m_tau/m_mu)^2 = %.0f' % (hi, 1e3 * MWqcd, (mtau / mmu) ** 2),
      10 < hi < 25 and MWqcd < mmu)

print('== C. breaking without a fundamental scalar')
g, gp = 0.6517, 0.3576; sx_, sy_, sz_ = sx, sy, szz
def massmat(conds, gens):
    k = len(gens(conds[0])); M = np.zeros((k, k))
    for f, phi, tag in conds:
        Gs_ = gens((f, phi, tag))
        for i in range(k):
            for j in range(k): M[i, j] += f * f * np.real(phi.conj() @ (Gs_[i] @ Gs_[j] + Gs_[j] @ Gs_[i]) @ phi) / 2
    return M
T1 = [np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / np.sqrt(2), np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / np.sqrt(2), np.diag([1., 0, -1])]
def smg(c_):
    f, phi, Y = c_
    if len(phi) == 2: return [g * sx_ / 2, g * sy_ / 2, g * sz_ / 2, gp * Y * I2]
    return [g * t.astype(complex) for t in T1] + [gp * Y * np.eye(3)]
YL = {'Q': Fr(1, 6), 'L': Fr(-1, 2)}; YR = {'u': Fr(2, 3), 'd': Fr(-1, 3), 'e': Fr(-1), 'n': Fr(0)}
conds = []
for fam in range(3):
    for l_, r_ in (('Q', 'u'), ('Q', 'd'), ('L', 'e'), ('L', 'n')):
        for col in range(3 if l_ == 'Q' else 1):
            Y = YL[l_] - YR[r_]; phi = np.array([1, 0], complex) if Y < 0 else np.array([0, 1], complex)   # Q = T3 + Y = 0
            conds.append((rng.uniform(0.1, 3), phi * np.exp(1j * rng.uniform(0, 6.3)), float(Y)))
cw2 = g * g / (g * g + gp * gp)
def rho_of(M): w = np.sort(np.linalg.eigvalsh(M)); return w, w[1] / (w[3] * cw2)
w0, rho0 = rho_of(massmat(conds, smg))
rT = [rho_of(massmat(conds + [(0.5, ph_, Yt)], smg))[1] for Yt, ph_ in ((1.0, np.array([0, 0, 1], complex)), (0.0, np.array([0, 1, 0], complex)))]
check('C1 [T/M] every bilinear psi_R^dag psi_L of chiral content is a |Y| = 1/2 doublet, so any EM-neutral pattern of '
      'dynamical masses gives a massless photon and rho = 1 exactly: %.12f (%d random condensates); a T = 1 order parameter '
      'gives %.4f (Y = 1), %.4f (Y = 0); measured rho0 = 1.00038(20)' % (rho0, len(conds), rT[0], rT[1]), {abs(c_[2]) for c_ in conds} == {0.5} and abs(rho0 - 1) < 1e-12 and abs(w0[0]) < 1e-12)
# left-right links: SU(2)_L x SU(2)_R x U(1)_(B-L), bidoublet Phi (Phi -> U_L Phi U_R^+), Delta_R (1,3) with (B-L)/2 = 1
gL = gR = g; gBL = 1 / np.sqrt(1 / gp ** 2 - 1 / gR ** 2)
E2 = [np.kron(sx_ / 2, I2), np.kron(sy_ / 2, I2), np.kron(sz_ / 2, I2)]                       # on vec(Phi), row-major: Phi -> s Phi
R2 = [-np.kron(I2, (s_ / 2).T) for s_ in (sx_, sy_, sz_)]                                      # Phi -> -Phi s
def lr(c_):
    f, phi, tag = c_
    if tag == 'bi': return [gL * e for e in E2] + [gR * r for r in R2] + [np.zeros((4, 4))]
    Rd = [np.kron(s_ / 2, I2) - np.kron(I2, (s_ / 2).T) for s_ in (sx_, sy_, sz_)]            # adjoint action on vec(Delta)
    return [np.zeros((4, 4))] * 3 + [gR * r for r in Rd] + [gBL * np.eye(4)]
bi_sym = np.eye(2).reshape(-1).astype(complex); bi_gen = np.diag([1.0, 0.4]).reshape(-1).astype(complex)
dR = np.array([[0, 0], [1, 0]], complex).reshape(-1)
zero = lambda M: int(np.sum(np.abs(np.linalg.eigvalsh(M)) < 1e-10))
z1 = zero(massmat([(1.0, bi_sym / np.linalg.norm(bi_sym), 'bi')], lr)); z2 = zero(massmat([(1.0, bi_gen / np.linalg.norm(bi_gen), 'bi')], lr))
vR = 40.0; Mlr = massmat([(1.0, bi_gen / np.linalg.norm(bi_gen), 'bi'), (vR, dR, 'D')], lr); z3 = zero(Mlr)
wl = np.sort(np.linalg.eigvalsh(Mlr)); rho_lr = wl[1] / (wl[3] * cw2); vRmin = vR * (6000 / 80.37) / np.sqrt(wl[4] / wl[1])
check('C2 [T] with SU(2)_R linked too (A6), bidoublet condensates leave %d massless links if isospin-symmetric and %d '
      'otherwise (photon, B-L); a B-L = 2 nu_R-pair (dN = 2) condensate leaves the photon alone (%d), rho = %.6f at '
      'v_R = 40 v; W_R > 6 TeV needs v_R > %.0f v' % (z1, z2, z3, rho_lr, vRmin),
      (z1, z2, z3) == (4, 2, 1) and abs(rho_lr - 1) < 1e-3)
MZ = 91.1876; ai = {'Y': 127.951 * (1 - 0.23122), '2': 127.951 * 0.23122, '3': 1 / 0.1180}; bY, b2, b3 = 41 / 6, -19 / 6, -7.0
ainv = lambda c_, b_, L: ai[c_] - b_ / (2 * np.pi) * L
Lm = (ai['Y'] - ai['2'] - (2 / 3) * ai['3']) / (bY / (2 * np.pi) + (-b2) / (2 * np.pi) + (2 / 3) * (-b3) / (2 * np.pi))
MPl = 1.220890e19; Mcell = MPl / np.sqrt(8 * np.pi); Lc = np.log(Mcell / MZ)
aY_pred = ainv('2', b2, Lc) + (2 / 3) * ainv('3', b3, Lc) + bY / (2 * np.pi) * Lc
s2_pred = ai['2'] / (ai['2'] + aY_pred)
check('C3 [E] g_L = g_R (A5), g_4 = g_3: 1/alpha_Y = 1/alpha_R + (2/3)/alpha_4 meets the measured couplings (one loop, SM '
      'below) at M_R = %.1e GeV; breaking at the cell scale %.2e GeV gives sin^2 thW(MZ) = %.3f vs 0.2312' % (MZ * np.exp(Lm), Mcell, s2_pred), 1e12 < MZ * np.exp(Lm) < 1e15 and s2_pred < 0.21)
# dN = 4 colour-singlet scalars of one family (left-handed Weyl fields; N = +1 for Q, L and -1 for the conjugates)
fields = {'Q': (Fr(1, 6), 3, 2, 1, Fr(1, 3), 0), 'L': (Fr(-1, 2), 1, 2, 1, 0, 1), 'uc': (Fr(-2, 3), -3, 1, -1, Fr(-1, 3), 0),
          'dc': (Fr(1, 3), -3, 1, -1, Fr(-1, 3), 0), 'ec': (Fr(1), 1, 1, -1, 0, -1), 'nc': (Fr(0), 1, 1, -1, 0, -1)}
ncomp = {'Q': 12, 'L': 4, 'uc': 6, 'dc': 6, 'ec': 2, 'nc': 2}                        # Grassmann components (Fermi limit)
ops = []
for combo in itertools.combinations_with_replacement(fields, 4):
    if any(combo.count(f) > ncomp[f] for f in fields): continue
    Ys = sum(fields[f][0] for f in combo); trip = sum(1 if fields[f][1] == 3 else (-1 if fields[f][1] == -3 else 0) for f in combo)
    N = sum(fields[f][3] for f in combo)
    if abs(N) == 4 and trip % 3 == 0:
        ops.append((combo, Ys, sum(fields[f][2] == 2 for f in combo), sum(fields[f][4] for f in combo), sum(fields[f][5] for f in combo)))
even_d = all(o[2] % 2 == 0 for o in ops); y0 = [o for o in ops if o[1] == 0]
okd = even_d and len(y0) == 3 and all(abs(o[3]) == 1 and abs(o[4]) == 1 for o in y0) and all(o[2] == 0 or o[0] == ('L', 'L', 'L', 'L') for o in ops if o[1] != 0)
check('C4 [T/M] all %d colour- and Fermi-allowed dN = +-4 products of one family hold an even number of doublets, so none '
      'is the doublet of C1; the %d with Y = 0 (QQQL, uude, uddn) are exactly the |B| = |L| = 1 ones: as condensates they '
      'break B and L (tau_p > 2.4e34 yr) with T = 0 or T >= 1; the rest have T = 0, Y != 0 and would break EM' % (len(ops), len(y0)), okd)
# NJL on the step-pi/2 tick (the mass-rule block rule): filled-sea block hop, critical coupling, small-mass law
def Ublk(K, mu):
    Wm = np.cos(mu / 2) * W + 1j * np.sin(mu / 2) * I8; return Dg(K).conj().T @ Wm @ Dg(K) @ Wm
mu_ = 0.37; errB = 0
for K in KR[:6]:
    lam_, V = np.linalg.eig(Ublk(K, mu_)); Vi_ = np.linalg.inv(V); sel = np.angle(lam_) > 0; Pse = (V[:, sel]) @ Vi_[sel]
    Sk = np.cos(K).mean(); sn = np.sin(mu_ / 2)
    errB = max(errB, abs(np.trace(Pse @ W).real - 4 * sn * np.sqrt((1 + Sk) / (1 - Sk + sn * sn * (1 + Sk)))))
def I0g(N):
    gq = (np.arange(N) + 0.5) / N * 2 * np.pi - np.pi; cq = np.cos(gq)
    return sum(np.sum(np.sqrt((1 + (cx + cq[:, None] + cq[None, :]) / 3) / (1 - (cx + cq[:, None] + cq[None, :]) / 3))) for cx in cq) / N ** 3
I0 = (4 * I0g(96) - I0g(48)) / 3; acoef = 3 * np.sqrt(3) / (2 * np.pi ** 2)
mt, vev, mH = 172.69, 246.21965, 125.20; mu_t = 2 / np.sqrt(3) * np.sqrt(8 * np.pi) * mt / MPl
tune = acoef * mu_t ** 2 * np.log(1 / mu_t) / I0 + mu_t ** 2 / 24
mPS = 100.0
for _ in range(60): mPS = 2 * np.pi * vev / np.sqrt(3 * np.log(Mcell ** 2 / mPS ** 2))
gp0 = np.sqrt(4 * np.pi / 127.951 / (1 - 0.23122)); g20 = np.sqrt(4 * np.pi / 127.951 / 0.23122); g30 = np.sqrt(4 * np.pi * 0.1180)
def gauge(t):
    L = t - np.log(MZ); return [1 / np.sqrt(1 / g0 ** 2 - 2 * b_ * L / (8 * np.pi ** 2)) for g0, b_ in ((gp0, bY), (g20, b2), (g30, b3))]
def rge(t, y):
    yt, la = y; gp_, g2_, g3_ = gauge(t); k = 1 / (16 * np.pi ** 2)
    return [k * yt * (4.5 * yt ** 2 - 8 * g3_ ** 2 - 2.25 * g2_ ** 2 - 17 / 12 * gp_ ** 2),
            k * (24 * la ** 2 - 6 * yt ** 4 + 12 * la * yt ** 2 - 3 * la * (3 * g2_ ** 2 + gp_ ** 2) + 3 / 8 * (2 * g2_ ** 4 + (g2_ ** 2 + gp_ ** 2) ** 2))]
res = []
for Y0 in (5.0, 20.0):
    sol = solve_ivp(rge, (np.log(Mcell), np.log(50.0)), [Y0, Y0 ** 2], dense_output=True, rtol=1e-10, atol=1e-12)
    m1 = 200.0; m2 = 200.0
    for _ in range(60): m1 = sol.sol(np.log(m1))[0] * vev / np.sqrt(2); m2 = np.sqrt(2 * sol.sol(np.log(m2))[1]) * vev
    res.append((m1 * (1 + 4 * gauge(np.log(m1))[2] ** 2 / (12 * np.pi ** 2)), m2))
check('C5 [T/E] top condensate on the step-pi/2 tick: sea hop = 4s sqrt((1+S)/(1-S+s^2(1+S))) (err %.0e), g_c = 1/(4 I0), '
      'I0 = %.5f; v needs g/g_c - 1 = %.0e; Pagels-Stokar at the cell cutoff m_t = %.0f, bubble m_H = %.0f; compositeness RG '
      '(y_t -> inf, lambda = y_t^2; SM one loop) m_t = %.0f, m_H = %.0f vs 172.69, 125.20: no 125 GeV scalar'
      % (errB, I0, tune, mPS, 2 * mPS, res[0][0], res[0][1]), errB < 1e-9 and 1e-33 < tune < 1e-30 and min(r[0] for r in res) > 190 and res[0][1] > 200)

print('== D. hierarchy')
b0 = {'SU(3)': 11 - Fr(4, 3) * 3, 'SU(2)_L': Fr(22, 3) - Fr(4, 3) * 3, 'SU(4)': Fr(44, 3) - Fr(4, 3) * 3, 'SU(2)_L+mirror': Fr(22, 3) - Fr(8, 3) * 3}
a3c, a2c = ainv('3', b3, Lc), ainv('2', b2, Lc)
L3 = Mcell * np.exp(-2 * np.pi * a3c / 7); L2 = Mcell * np.exp(-2 * np.pi * a2c / (19 / 6)); need = 2 * np.pi / np.log(Mcell / vev)
check('D1 [T/E] Lambda = M exp(-2pi/(b0 alpha_M)); three families, no scalar: b0 = 7 (SU(3)), 10/3 (SU(2)_L), 32/3 (SU(4)), '
      '-2/3 (SU(2)_L above the mirror mass); U(1) screens. Measured couplings at the cell (1/alpha_3 = %.1f, 1/alpha_2 = %.1f) '
      'confine at %.0e, %.0e GeV; v needs b0 alpha_cell = %.3f (b0 = %.1f at alpha_3): no group in the content' % (a3c, a2c, L3, L2, need, need * a3c),
      b0 == {'SU(3)': 7, 'SU(2)_L': Fr(10, 3), 'SU(4)': Fr(32, 3), 'SU(2)_L+mirror': Fr(-2, 3)} and L3 < 1 and L2 < 1e-15)
mue = 2 / np.sqrt(3) * np.sqrt(8 * np.pi) * me_ / MPl
check('D2 [T/E] naturalness: no scalar, no quadratic sensitivity; at small step the mass zero is unprotected (A2), so each mu '
      'is tuned against O(alpha/4pi) dressing (electron mu = %.1e: ~%.0e); an exact chiral SU(2)_L forbids mass terms, so '
      'vacuum masses are protected and transmutation needs only b0 alpha = %.2f'
      % (mue, mue / (1 / 137 / (4 * np.pi)), need), mue < 1e-21 and dims[2] == 1)
print('supplied: CL-2 tick (eps, mu, copy factor); rung-1 index in parallel; Spin(10) mirror term; Dirac/Fermi contact or W')
print('  propagator; SM one-loop betas; PDG/TWIST: tau_mu, tau_tau, B_e, masses, M_W, rho, xi, rho0, alpha(MZ), sin^2, alpha_s, f_pi.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
