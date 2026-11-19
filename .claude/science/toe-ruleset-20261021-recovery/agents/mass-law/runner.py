#!/usr/bin/env python3
"""Can the CL-2 geometry supply a copy-structured mass law (Koide r, Brannen delta)?

Copy-index candidates: the three edge neighbours of a site, the three cube axes, the C3 stabiliser of a site about its
body diagonal, the T1 triplet of a cell.  (A) measured targets; (B) the CL-2 hop is a Clifford algebra on the axes
(exact); (C) the site stabiliser and its oriented body diagonal; (D) the tick is pi-flux real, so its time reversal
pairs the C3 characters omega <-> omega-bar and every hop-built circulant has a degenerate pair; (E) the Clifford
Gram point: axis projections give r = 1/2 exactly but delta = pi/12 exactly (one massless member); (F) the spin-j
coherent Gram class and the CL-2 site states; (G) phase arithmetic against delta; (H) quark sectors.
Supplied model, finite diagnostic, no physical identification.  A PASS line states a true mathematical or numerical
fact; several are failures of a candidate mechanism against measurement, stated as such.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools, time
from collections import deque
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import expm, schur
from scipy.optimize import brentq

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- measured inputs (MeV): CODATA 2018 e, mu; PDG 2024 tau; PDG quark MSbar; running masses at M_Z
me, mmu, mtau, dtau = 0.51099895000, 105.6583755, 1776.93, 0.09
R_meas, dR = mmu / me, 206.7682830 * np.hypot(1.5e-10 / me, 2.3e-6 / mmu)
QSETS = dict(up=(2.16, 1270., 172690.), down=(4.67, 93.4, 4180.), upMZ=(1.27, 619., 171700.), downMZ=(2.90, 55., 2890.))
QBOX = dict(up=[(2.16, .26, .49), (1270., 20., 20.), (172690., 300., 300.)], down=[(4.67, .17, .48), (93.4, 3.4, 8.6), (4180., 20., 30.)])
def fit(m):
    sq = np.sqrt(np.array(m, float)); a = sq.mean(); z = (sq * np.exp(-2j * np.pi * np.arange(3) / 3)).sum() / 3
    return abs(z) ** 2 / a ** 2, np.angle(z) % (2 * np.pi / 3)
def Qk(m): m = np.array(m, float); return m.sum() / np.sqrt(m).sum() ** 2

print('== A. measured targets')
mp.mp.dps = 30
def ratios(r, d):
    x = sorted([(1 + 2 * mp.sqrt(r) * mp.cos(d + 2 * mp.pi * k / 3)) ** 2 for k in range(3)]); return x[1] / x[0], x[2] / x[1]
dh = mp.findroot(lambda d: ratios(mp.mpf(1) / 2, d)[0] - R_meas, mp.mpf('0.2222'))
sdh = float(dR / abs(mp.diff(lambda d: ratios(mp.mpf(1) / 2, d)[0], dh)))
rh = mp.findroot(lambda r: ratios(r, mp.mpf(2) / 9)[0] - R_meas, mp.mpf('0.5'))
DT, RT = float(dh), float(rh)
RTM, sRTM = mtau / mmu, mtau / mmu * dtau / mtau
qfit = {k: (Qk(v),) + fit(v) for k, v in QSETS.items()}
check('targets: r = 1/2 => delta = %.10f(%d); delta = 2/9 => r = %.10f; m_tau/m_mu = %.4f(%d)' % (DT, round(sdh * 1e10), RT, RTM, round(sRTM * 1e4)),
      abs(DT - 0.2222220471) < 2e-10 and abs(RT - 0.4999997868) < 2e-10)
print('   quarks (Q, r, delta): ' + '; '.join(f'{k} {q:.3f},{r:.3f},{d:.4f}' for k, (q, r, d) in qfit.items()))

# ---------------- CL-2 hop on one cube from spin-3/2 coherent states along the body diagonals
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def coh(j, n):
    J = Jm(j); n = np.asarray(n, float); n = n / np.linalg.norm(n)
    w, v = np.linalg.eigh(sum(n[k] * J[k] for k in range(3))); x = v[:, -1]; k = np.argmax(abs(x) > 1e-9)
    return x * abs(x[k]) / x[k]
CN = list(itertools.product((0, 1), repeat=3)); ci = {c: i for i, c in enumerate(CN)}
XI = {c: coh(1.5, 2 * np.array(c) - 1.0) for c in CN}
W = np.zeros((8, 8), complex); Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for a in CN:
    for b in CN:
        dd = np.array(a) - np.array(b)
        if abs(dd).sum() == 1:
            g = XI[a].conj() @ XI[b]; W[ci[a], ci[b]] = -g / abs(g) / np.sqrt(3); Wa[int(np.nonzero(dd)[0][0])][ci[a], ci[b]] = W[ci[a], ci[b]]
Gam = [np.sqrt(3) * w for w in Wa]
eta = [lambda c: 1, lambda c: (-1) ** c[0], lambda c: (-1) ** (c[0] + c[1])]          # Kogut-Susskind real gauge
GKS = [sp.zeros(8, 8) for _ in range(3)]
for a in range(3):
    for c in CN:
        if c[a] == 0:
            c2 = list(c); c2[a] = 1; c2 = tuple(c2); GKS[a][ci[c2], ci[c]] = GKS[a][ci[c], ci[c2]] = eta[a](c)
th = np.full(8, np.nan); th[0] = 0; dq = deque([0]); WKS = np.array(sum(GKS, sp.zeros(8, 8)), dtype=float) / np.sqrt(3)
while dq:
    u = dq.popleft()
    for v in np.nonzero(abs(W[:, u]) > 1e-12)[0]:
        if np.isnan(th[v]): th[v] = th[u] + np.angle(W[v, u] / WKS[v, u]); dq.append(v)
Dg = np.diag(np.exp(1j * th))

print('== B. the CL-2 hop is a Clifford algebra on the three axes')
anti = max(np.abs(Gam[a] @ Gam[b] + Gam[b] @ Gam[a] - 2 * (a == b) * np.eye(8)).max() for a in range(3) for b in range(3))
check('W^2 = 1; Gamma_a = sqrt3 W_a obey {Gamma_a, Gamma_b} = 2 delta_ab, so the 3 edge neighbours are the 3 axes'
      ' and W = (Gx + Gy + Gz)/sqrt3', np.abs(W @ W - np.eye(8)).max() < 1e-13 and anti < 1e-13, f'{anti:.0e}')
check('CL-2 W is gauge-equivalent to the real Kogut-Susskind hop (same pi flux on every face)', np.abs(W - Dg @ WKS @ Dg.conj().T).max() < 1e-13)
s3 = sp.sqrt(3); Gx, Gy, Gz = GKS; WS = (Gx + Gy + Gz) / s3; I8 = sp.eye(8); PS = Gx * Gy * Gz
exB = all((GKS[a] * GKS[b] + GKS[b] * GKS[a] - 2 * (a == b) * I8).is_zero_matrix for a in range(3) for b in range(3))
check('exact: Clifford relations, W^2 = 1, P = GxGyGz (the body-diagonal hop) has P^2 = -1, tr P = 0 (P = +-i, 4 + 4)',
      exB and sp.simplify(WS * WS - I8).is_zero_matrix and (PS * PS + I8).is_zero_matrix and PS.trace() == 0)

print('== C. the site stabiliser and its oriented body diagonal')
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: rots.append(M)
cc = np.array([.5, .5, .5]); stab = {}
for M in rots:
    t = M @ cc - cc                                # g(x) = M(x - c) + c + t fixes 0
    if np.allclose(np.mod(t, 2), 0) or np.allclose(np.mod(t - 1, 2), 0):
        stab[M.tobytes()] = ('keep' if np.allclose(np.mod(t, 2), 0) else 'swap', M)
kinds = sorted(k for k, _ in stab.values())
dok = all(np.allclose(np.full(3, .5) - np.where(np.array(s) == 0, -.5, 1.5), [(-1) ** v for v in s]) and
          np.allclose(2 * np.array(s) - 1, [-(-1) ** v for v in s]) for s in CN)
check('site 0 is fixed by exactly 6 symmetries (D3): C3 about (1,1,1) keeps the tilings, 3 half-turns swap them; each site'
      ' has the oriented axis d(s) = c_even - c_odd = ((-1)^s_i), and its spin-3/2 state points along -d(s)', len(stab) == 6 and
      kinds.count('keep') == 3 and dok)

def cperm(M):                                       # plain corner permutation of a rotation about the cell centre
    P_ = np.zeros((8, 8))
    for a in CN: P_[ci[tuple(np.rint(M @ (np.array(a) - cc) + cc).astype(int))], ci[a]] = 1
    return P_
Pl = [cperm(M) for M in rots]; chiT1 = lambda M: np.trace(M)              # T1 = vector rep: character = trace of M
PT1 = sum(chiT1(M) * P_ for M, P_ in zip(rots, Pl)) * 3 / 24
vT, uT = np.linalg.eigh(PT1); BT = uT[:, vT > .5]
C3p = BT.T @ cperm(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])) @ BT; C2p = BT.T @ cperm(np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])) @ BT
def cdim(Ms): A = np.vstack([np.kron(M, np.eye(3)) - np.kron(np.eye(3), M.T) for M in Ms]); return int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9))
check('T1 triplet of a cell (plain action): O-covariant mass is one value (Schur); under the site C3 it is 1 + w + w-bar'
      ' (free circulant, commutant 3); adding the tiling-swapping half-turn gives A2 + E (commutant 2, degenerate pair)',
      BT.shape[1] == 3 and cdim([BT.T @ P_ @ BT for P_ in Pl]) == 1 and cdim([C3p]) == 3 and cdim([C3p, C2p]) == 2)

print('== D. the tick is pi-flux real: time reversal pairs omega with omega-bar')
L = 4; N = L ** 3; idx = lambda s: ((s[0] % L) * L + (s[1] % L)) * L + (s[2] % L)
sites = [np.array(s) for s in itertools.product(range(L), repeat=3)]
def hop(par):
    H = np.zeros((N, N), complex)
    for o in itertools.product(range(0, L, 2), repeat=3):
        o = np.array(o) + par
        for a in CN:
            for b in CN:
                if abs(np.array(a) - np.array(b)).sum() == 1:
                    sa, sb = o + np.array(a), o + np.array(b); g = XI[tuple(sa % 2)].conj() @ XI[tuple(sb % 2)]
                    H[idx(sa), idx(sb)] = -g / abs(g) / np.sqrt(3)
    return H
We, Wo = hop(0), hop(1); Wt = We + Wo; hol = []
for s in sites:
    for a, b in ((0, 1), (1, 2), (0, 2)):
        ea, eb = np.eye(3, dtype=int)[a], np.eye(3, dtype=int)[b]; p = [s, s + ea, s + ea + eb, s + eb]
        hol.append(np.prod([Wt[idx(p[(k + 1) % 4]), idx(p[k])] * np.sqrt(3) for k in range(4)]))
thl = np.full(N, np.nan); thl[0] = 0; dq = deque([0])
while dq:
    u = dq.popleft()
    for v in np.nonzero(abs(Wt[:, u]) > 1e-12)[0]:
        if np.isnan(thl[v]): thl[v] = thl[u] + np.angle(Wt[v, u]); dq.append(v)
Lam = np.diag(np.exp(-1j * thl)); WeR, WoR = Lam @ We @ Lam.conj().T, Lam @ Wo @ Lam.conj().T
Rm = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); nn = np.ones(3) / np.sqrt(3); J3 = Jm(1.5)
DR = expm(-1j * (2 * np.pi / 3) * sum(nn[k] * J3[k] for k in range(3))); Gl = np.zeros((N, N), complex)
for s in sites:
    t = Rm @ s; Gl[idx(t), idx(s)] = XI[tuple(t % 2)].conj() @ DR @ XI[tuple(s % 2)]
GR = Lam @ Gl @ Lam.conj().T; GR = GR * np.exp(-1j * np.angle(GR[np.abs(GR) > .5][0]))
check('L = 4 torus: all 192 plaquettes of Z^3 carry -1 (pi flux), so one gauge makes both half-tick hops real; the site C3'
      ' commutes with them, cubes to -1, and is a real signed permutation there', np.abs(np.array(hol) + 1).max() < 1e-12 and
      max(np.abs(WeR.imag).max(), np.abs(WoR.imag).max(), np.abs(GR.imag).max()) < 1e-12 and
      max(np.abs(Gl @ We - We @ Gl).max(), np.abs(Gl @ Wo - Wo @ Gl).max(), np.abs(np.linalg.matrix_power(Gl, 3) + np.eye(N)).max()) < 1e-12)
eps, mu = 0.3, 0.1; Vh = expm(-1j * (eps - mu / 2) * WeR / 2); Us = Vh @ expm(1j * (eps + mu / 2) * WoR) @ Vh
Tq, Zq = schur(Us, output='complex'); Hs = Zq @ np.diag(-np.angle(np.diag(Tq))) @ Zq.conj().T
orbs = [[(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(-1, 0, 0), (0, -1, 0), (0, 0, -1)], [(1, 1, 0), (0, 1, 1), (1, 0, 1)]]
gap = 0.
for ob in orbs:
    ii = [idx(np.array(v)) for v in ob]
    for X in (Us, Us @ Us, Hs):
        ev = np.sort_complex(np.linalg.eigvals(X[np.ix_(ii, ii)])); gap = max(gap, min(abs(ev[0] - ev[1]), abs(ev[1] - ev[2]), abs(ev[0] - ev[2])))
check('symmetric-frame tick U_s is complex symmetric (U_s^T = U_s: time reversal is complex conjugation); its blocks on the'
      ' three C3 orbits around a site (U_s, U_s^2, log U_s) always have a degenerate pair', np.abs(Us - Us.T).max() < 1e-12 and gap < 1e-12,
      f'min level split {gap:.0e}')
Gc = np.zeros((8, 8), complex)
for a in CN: t = tuple(Rm @ np.array(a)); Gc[ci[t], ci[a]] = XI[t].conj() @ DR @ XI[a]
w8, v8 = np.linalg.eigh(W); Vp = v8[:, w8 > 0]; chi = np.angle(np.linalg.eigvals(Vp.conj().T @ Gc @ Vp)) / np.pi
check('at rest each 4-fold level carries site-C3 characters exp(-i pi/3), exp(+i pi/3), -1, -1 (spin projections 1/2, -1/2,'
      ' +-3/2 of one multiplet, Kramers paired), so C3 labels spin states, not species', np.allclose(np.sort(np.abs(chi)), [1 / 3, 1 / 3, 1, 1]))
s3_ = sp.sqrt(3); WSx = sum(GKS, sp.zeros(8, 8)) / s3_; on = [ci[(1, 0, 0)], ci[(0, 1, 0)], ci[(0, 0, 1)]]
Vsite = sp.Matrix(3, 3, lambda k, l: WSx[on[k], 0] * WSx[0, on[l]]); Wsq = (WSx * WSx).extract(on, on); Vfar = Wsq - Vsite
spec = lambda M: sorted(sp.nsimplify(e) for e, m in M.eigenvals().items() for _ in range(m))
check('hop-built orbit circulants (exact, from W): W^2 -> 1 (r = 0); paths via the site -> spectrum (0, 0, 1) (r = 1); via the'
      ' far corners -> (0, 1, 1) (r = 1/4): every one has a degenerate pair', Wsq == sp.eye(3) and spec(Vsite) == [0, 0, 1] and
      spec(Vfar) == [0, 1, 1])

print('== E. the Clifford Gram point')
def null(M): return M.nullspace()
psi = None
for sgn in (1, -1):
    B = (WS - I8).col_join(PS - sgn * sp.I * I8); ns = null(B); psi = ns[0] if sgn == 1 else psi
    if sgn == 1: nsp = len(ns)
def gram(ps):
    v = [((I8 + G) / 2) * ps for G in GKS]; nr = [sp.sqrt(sp.simplify((x.H * x)[0])) for x in v]
    return sp.Matrix(3, 3, lambda a, b: sp.simplify((v[a].H * v[b])[0] / (nr[a] * nr[b])))
Gm = gram(psi); bar = sp.simplify(sp.expand_complex(Gm[0, 1] * Gm[1, 2] * Gm[2, 0])); lam = sp.symbols('lam')
cp = sp.factor(sp.simplify((Gm - lam * sp.eye(3)).det()))
psi2 = null((WS - I8).col_join(PS + sp.I * I8))[0]; bar2 = sp.simplify(sp.expand_complex(gram(psi2)[0, 1] * gram(psi2)[1, 2] * gram(psi2)[2, 0]))
check('exact: on W = 1, P = +i (dim %d) the axis projections (1 + Gamma_a)psi/2 have |G_ab|^2 = 1/2 (r = 1/2) and Bargmann'
      ' (1 + i)/4 = e^(i pi/4)/(2 sqrt2) (singlet weight 3a^2 = doublet weight 6|b|^2); P = -i gives (1 - i)/4: |delta| = pi/12' % nsp,
      all(sp.simplify(sp.Abs(Gm[a, b]) ** 2 - sp.Rational(1, 2)) == 0 for a, b in ((0, 1), (1, 2), (0, 2))) and
      sp.simplify(bar - (1 + sp.I) / 4) == 0 and sp.simplify(bar2 - (1 - sp.I) / 4) == 0)
check('exact: Gram spectrum = roots of lam (lam^2 - 3 lam + 3/2) = (3 +- sqrt3)/2, 0, the levels of the frame operator'
      ' sum_a (1 + Gamma_a)/2 = (3 + sqrt3 W)/2 plus a kernel: rank 2', sp.simplify(cp + lam * (lam ** 2 - 3 * lam + sp.Rational(3, 2))) == 0)
g0 = gram(sp.Matrix([1, 0, 0, 0, 0, 0, 0, 0]))
check('exact: the time-reversal-even corner reference gives G_ab = 1/2 (r = 1/4, delta = 0, degenerate pair)', g0 == sp.Matrix(3, 3, lambda a, b: 1 if a == b else sp.Rational(1, 2)))
rng = np.random.default_rng(7); Gn = [np.array(G, dtype=float) for G in GKS]; WK = sum(Gn) / np.sqrt(3); PK = Gn[0] @ Gn[1] @ Gn[2]
GK = Dg.conj().T @ Gc @ Dg; wG, vG = np.linalg.eig(GK); devf, cov = 0., set()
for lamG in (-1, np.exp(-1j * np.pi / 3), np.exp(1j * np.pi / 3)):
    Bq, _ = np.linalg.qr(vG[:, np.isclose(wG, lamG)])
    for _ in range(100):
        ps = Bq @ (rng.normal(size=Bq.shape[1]) + 1j * rng.normal(size=Bq.shape[1])); ps /= np.linalg.norm(ps)
        v = [(np.eye(8) + G) @ ps / 2 for G in Gn]; nv = [np.linalg.norm(x) for x in v]; g01 = v[0].conj() @ v[1] / (nv[0] * nv[1])
        D_ = (ps.conj() @ WK @ ps).real / np.sqrt(3); S_ = (ps.conj() @ (-1j * PK) @ WK @ ps).real / np.sqrt(3)
        devf = max(devf, abs(g01 - (1 + 2 * D_ + 1j * S_) / (2 * (1 + D_))), abs(v[1].conj() @ v[2] / (nv[1] * nv[2]) - g01))
    for w_ in (1, -1):
        for p_ in (1j, -1j):
            M_ = np.vstack([(WK - w_ * np.eye(8)) @ Bq, (PK - p_ * np.eye(8)) @ Bq])
            if np.sum(np.linalg.svd(M_, compute_uv=False) < 1e-9) > 0: cov.add((lamG == -1, w_, p_))
gx = np.linspace(-1, 1, 1201) / np.sqrt(3); Dm, Sm = np.meshgrid(gx, gx); Gv = (1 + 2 * Dm + 1j * Sm) / (2 * (1 + Dm))
dv = np.angle(Gv) % (2 * np.pi / 3); dv = np.minimum(dv, 2 * np.pi / 3 - dv); rv = abs(Gv) ** 2
rmx = lambda d: rv[abs(dv - d) < 1e-3].max()
check('every C3-symmetric reference: G = (1 + 2D + iS)/(2(1 + D)), D = <W>/sqrt3, S = <-iPW>/sqrt3 (time-reversal odd) on the'
      ' square |D|,|S| <= 1/sqrt3; r <= 1/2 iff 2D^2 + S^2 <= 1, equal only at the corners, where tan delta = 2 - sqrt3 (pi/12);'
      ' at delta = %.4f (or 2/9) the best is r = %.4f (Q = %.4f)' % (DT, rmx(DT), 1 / 3 + 2 * rmx(DT) / 3), devf < 1e-12 and
      len([c for c in cov if c[0]]) == 4 and max(rmx(DT), rmx(2 / 9)) < 0.4915 and rv.max() < 0.5 + 1e-12, f'{devf:.0e}')
rgp = float(7 + 4 * sp.sqrt(3))
check('Gram point vs measurement: Q = 2/3 but m_e = 0, m_tau/m_mu = 7 + 4 sqrt3 = %.3f vs %.4f (%.0f sigma), delta = pi/12 vs'
      ' %.10f (%.1e sigma): excluded' % (rgp, RTM, (RTM - rgp) / sRTM, DT, (np.pi / 12 - DT) / sdh), (RTM - rgp) / sRTM > 1e3)

def axang(M):
    an = np.arccos(np.clip((np.trace(M) - 1) / 2, -1, 1))
    if an < 1e-9: return np.array([0., 0., 1.]), 0.
    if abs(an - np.pi) < 1e-9: w_, v_ = np.linalg.eigh((M + M.T) / 2); return v_[:, -1], an
    return np.array([M[2, 1] - M[1, 2], M[0, 2] - M[2, 0], M[1, 0] - M[0, 1]]) / (2 * np.sin(an)), an
PW = Gam[0] @ Gam[1] @ Gam[2]; sgP = []
for M in rots:
    n_, an = axang(M.astype(float)); Dm_ = expm(-1j * an * sum(n_[k] * J3[k] for k in range(3))); R_ = np.zeros((8, 8), complex)
    for a in CN: t = tuple(np.rint(M @ (np.array(a) - cc) + cc).astype(int)); R_[ci[t], ci[a]] = XI[t].conj() @ Dm_ @ XI[a]
    if np.abs(R_ @ W @ R_.conj().T - W).max() > 1e-9: sgP.append(0)
    else: sgP.append(int(np.sign((np.trace(R_ @ PW @ R_.conj().T @ PW.conj().T)).real)) * (np.abs(R_ @ PW @ R_.conj().T @ PW.conj().T - np.eye(8) * np.sign(np.trace(R_ @ PW @ R_.conj().T @ PW.conj().T).real)).max() < 1e-9))
par = [int(round(np.linalg.det(np.abs(M)))) for M in rots]
check('the sign of delta is the chirality P: P is kept by the 12 rotations of T and reversed by the 12 that permute the axes'
      ' oddly (90-degree turns, face-diagonal half-turns, incl. the tiling swaps), and by time reversal', sgP == par and sgP.count(1) == 12)

print('== F. the spin-j coherent Gram class')
def omega(c):
    ca2 = (2 * c + 1) / 3; ca = np.sqrt(ca2); return 2 * np.arctan2(3 * np.sqrt(3) * (1 - ca2) * ca, 9 * ca2 - 1)
e3 = np.ones(3) / np.sqrt(3); e1 = np.array([1, -1, 0]) / np.sqrt(2); e2 = np.cross(e3, e1); dev = 0.
for j in (0.5, 1.0, 1.5, 2.0):
    for c in (-0.4, -1 / 3, 0.0, 0.3, 0.5, 0.8):
        ca = np.sqrt((2 * c + 1) / 3); sa = np.sqrt(1 - ca ** 2)
        vs = [coh(j, ca * e3 + sa * (np.cos(2 * np.pi * k / 3) * e1 + np.sin(2 * np.pi * k / 3) * e2)) for k in range(3)]
        Gj = np.array([[x.conj() @ y for y in vs] for x in vs]); bj = Gj[0, 1] * Gj[1, 2] * Gj[2, 0]
        dev = max(dev, abs(abs(Gj[0, 1]) ** 2 - ((1 + c) / 2) ** (2 * j)), abs(np.exp(1j * np.angle(bj)) - np.exp(1j * j * omega(c))))
check('spin-j coherent triples at mutual cos c: r = ((1 + c)/2)^(2j), Bargmann phase = j Omega(c) (solid angle), verified for'
      ' j = 1/2..2', dev < 1e-12, f'{dev:.0e}')
bd = [2 * np.array(c) - 1. for c in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
vs = [coh(1.5, n) for n in bd]; Gs = np.array([[x.conj() @ y for y in vs] for x in vs]); bs = Gs[0, 1] * Gs[1, 2] * Gs[2, 0]
check('CL-2 site states (spin 3/2 along body diagonals): every C3 orbit of sites has Omega = pi, so r = 1/27, 3 delta = pi/2,'
      ' sqrt-masses (4/3, 1, 2/3), Q = 29/81', abs(abs(Gs[0, 1]) ** 2 - 1 / 27) < 1e-13 and abs(abs(np.angle(bs)) - np.pi / 2) < 1e-12 and
      np.allclose(np.sort(np.linalg.eigvalsh(Gs)), [2 / 3, 1, 4 / 3]))
fd = lambda c: np.log(2) * omega(c) / (-6 * np.log((1 + c) / 2))
cstar = brentq(lambda c: fd(c) - DT, 1e-6, .999); j2 = np.log(2) / (-np.log((1 + cstar) / 2))
djs = [fd(2 * .5 ** (1 / (2 * j)) - 1) for j in (1.0, 1.5)]
check('on r = 1/2 the class gives delta in (sqrt3 ln2/6, pi/12] = (%.5f, %.5f]; integer directions reach r = 1/2 only at'
      ' j = 1/2, c = 0 (delta = pi/12); j = 1, 3/2 give %.4f, %.4f; the target needs 2j = %.3f: no member' % (np.sqrt(3) * np.log(2) / 6,
      np.pi / 12, *djs, j2), abs(fd(1e-9) - np.pi / 12) < 1e-8 and abs(j2 - round(j2)) > 0.2)
sp_pred = {k: omega(2 * r - 1) / 6 for k, (q, r, d) in qfit.items()}; sp_pred['lep'] = np.pi / 12
check('spin-1/2 triple law delta = Omega/6 at each measured r overshoots every sector: lep %.4f vs %.4f, ' % (np.pi / 12, DT) +
      ', '.join(f'{k} {sp_pred[k]:.4f} vs {qfit[k][2]:.4f}' for k in ('up', 'down')), all(sp_pred[k] > qfit[k][2] * 1.05 for k in qfit))

print('== G. phase arithmetic')
dk = [abs(k * np.pi / 12 - DT) for k in range(8)]
check('W holonomies are +-1 and the site and Clifford Bargmann phases lie in (pi/4)Z, so delta lies in (pi/12)Z; 2/9 is not of that'
      ' form (pi irrational); nearest to the r = 1/2 target: pi/12, %.4f rad = %.0e sigma away' % (min(dk), min(dk) / sdh),
      int(np.argmin(dk)) == 1 and min(dk) > 0.03)
alg = {'face-diag j=3/2': np.arctan(np.sqrt(2) / 5), 'face-diag j=1/2': np.arctan(np.sqrt(2) / 5) / 3, 'axes j=3/2': np.pi / 4}
check('non-site triples give args of algebraic numbers (Lindemann-Weierstrass, cited: never exactly 2/9): ' +
      ', '.join(f'{k} {v:.4f}' for k, v in alg.items()) + ' vs %.4f' % DT, min(abs(v - DT) for v in alg.values()) > 0.02)

print('== H. quark sectors')
gapQ = min(Qk(v) for v in itertools.product(*[(x - lo, x, x + hi) for x, lo, hi in QBOX['up']])) - \
       max(Qk(v) for v in itertools.product(*[(x - lo, x, x + hi) for x, lo, hi in QBOX['down']]))
check('species-blind CL-2 geometry gives one (r, delta) for all sectors; measured Q_up - Q_down > %.3f over the PDG box, and quark'
      ' r > 1/2 lies outside the Clifford family (r <= 1/2)' % gapQ, gapQ > 0.05 and all(qfit[k][1] > 0.5 for k in qfit))
qup = [Qk(v) for v in itertools.product(*[(x - lo, x, x + hi) for x, lo, hi in QBOX['up']])]
check('nearest lattice coherent triple for up quarks (face diagonals, 60 deg, j = 1/2): Q = 5/6 lies outside the PDG box'
      ' [%.3f, %.3f]' % (min(qup), max(qup)), 5 / 6 < min(qup))
print('supplied: the copy index, the Gram (sqrt-mass) reading, the reference state and its P sector; PDG/CODATA inputs.')
print('not established: any derived delta, copy count, quark Koide value or mixing; r = 1/2 only at the m_e = 0 edge.')
print('elapsed_seconds', round(time.monotonic() - T0, 1))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
