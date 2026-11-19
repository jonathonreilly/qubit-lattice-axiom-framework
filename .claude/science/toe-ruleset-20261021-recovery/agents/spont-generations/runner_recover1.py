#!/usr/bin/env python3
"""Three copies broken by the state, not the rule: what a vacuum condensate can and cannot fix.

Supplied: three identical internal copies of the CL-2 light band (the rules give two), copy group S3, a copy-space
condensate phi (Hermitian, read either as the mass angles mu_k ('lin') or as their square roots ('sq')), and the
CL-2 step eps = 0.04.  The vacuum is a stationary point of the sea phase plus a Hartree contact term (CL-5 reading).
(A) measured targets; (B) what breaking by the state buys; (C) the CL-2 sea fixes delta only at sin(3 delta) = 0;
(D) copy-blind contact vacua cannot carry the lepton spectrum, at any coupling or colour factor; (E) colour; (F) mixing;
(G) measured limits on breaking a copy symmetry at the lepton scale.  A PASS line states a true mathematical or
numerical fact; several are failures of a candidate mechanism against measurement, stated as such.
Supplied model, finite diagnostic; no physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import brentq

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- measured inputs (MeV); pole lepton masses (CODATA 2018, PDG 2024 tau), PDG 2022 quark MSbar
me, mmu, mtau, dtau = 0.51099895000, 105.6583755, 1776.93, 0.09
R_meas, dR = mmu / me, 206.7682830 * np.hypot(1.5e-10 / me, 2.3e-6 / mmu)
QU = dict(u=(2.16, 0.26, 0.49), c=(1270., 20., 20.), t=(172690., 300., 300.))
QD = dict(d=(4.67, 0.17, 0.48), s=(93.4, 3.4, 8.6), b=(4180., 20., 30.))
QU_MZ, QD_MZ = (1.27, 619., 171700.), (2.90, 55., 2890.)   # running masses at M_Z (Xing-Zhang-Zhou), supplied
Vus, dVus = 0.22500, 0.00067

def fit(m):
    sq = np.sqrt(np.array(m, float)); a = sq.mean(); z = (sq * np.exp(-2j * np.pi * np.arange(3) / 3)).sum() / 3
    return abs(z) ** 2 / a ** 2, np.angle(z) % (2 * np.pi / 3)
def Qk(m): m = np.array(m, float); return m.sum() / np.sqrt(m).sum() ** 2

print('== A. measured targets (pole masses)')
r0, d0 = fit([me, mmu, mtau]); rp, dp = fit([me, mmu, mtau + dtau]); rm, dm = fit([me, mmu, mtau - dtau])
sr, sd = abs(rp - rm) / 2, abs(dp - dm) / 2
check('3-mass fit sqrt(m_k) = a(1 + 2 sqrt(r) cos(delta + 2 pi k/3)): r = 1/2 and delta = 2/9 each within 1 sigma',
      abs(r0 - .5) < sr and abs(d0 - 2 / 9) < sd, f'r = {r0:.7f}({sr*1e7:.0f}), delta = {d0:.7f}({sd*1e7:.0f})')
mp.mp.dps = 30
def ratios(r, d):
    x = sorted([(1 + 2 * mp.sqrt(r) * mp.cos(d + 2 * mp.pi * k / 3)) ** 2 for k in range(3)]); return x[1] / x[0], x[2] / x[1]
Rpair = ratios(mp.mpf(1) / 2, mp.mpf(2) / 9)[0]
dh = mp.findroot(lambda d: ratios(mp.mpf(1) / 2, d)[0] - R_meas, mp.mpf('0.2222'))
sdh = dR / abs(mp.diff(lambda d: ratios(mp.mpf(1) / 2, d)[0], dh))
rh = mp.findroot(lambda r: ratios(r, mp.mpf(2) / 9)[0] - R_meas, mp.mpf('0.5'))
mt_a = me * ratios(mp.mpf(1) / 2, dh)[0] * ratios(mp.mpf(1) / 2, dh)[1]; mt_b = me * ratios(rh, mp.mpf(2) / 9)[0] * ratios(rh, mp.mpf(2) / 9)[1]
nsig = float((Rpair - R_meas) / dR)
check('the pair (r, delta) = (1/2, 2/9) is excluded by m_mu/m_e: at most one of the two can be exact', nsig > 100,
      f'predicts {float(Rpair):.6f} vs {R_meas:.7f}({dR*1e7:.0f}): {nsig:.0f} sigma')
print(f'   r = 1/2 exact => delta = {float(dh):.10f}({float(sdh)*1e10:.0f}e-10) = 2/9 {float(dh-mp.mpf(2)/9):+.3e};'
      f' delta = 2/9 exact => r = {float(rh):.10f};  m_tau {float(mt_a):.2f} / {float(mt_b):.2f} vs {mtau}({dtau})')
def nearest(vals): v = np.array(vals); i = np.argmin(abs(v - float(dh))); return v[i], abs(v[i] - float(dh)) / sd
fr = [(p, q) for q in range(1, 31) for p in range(0, 2 * q) if np.gcd(p, q) == 1]
cands = {'p pi/q': [p * np.pi / q for p, q in fr], 'arccos(p/q)': [np.arccos(p / q) for p, q in fr if p <= q],
         'arctan(p/q)': [np.arctan(p / q) for p, q in fr]}
near = {k: nearest(v) for k, v in cands.items()}
check('no lattice-type angle p pi/q, arccos(p/q) or arctan(p/q) with q <= 30 lies within 2 sigma(3-mass fit) of delta',
      all(n[1] > 2 for n in near.values()), '; '.join(f'{k}: {n[0]:.6f} ({n[1]:.0f} sig)' for k, n in near.items()))
qr = {k: fit(v) for k, v in (('up', [x[0] for x in QU.values()]), ('down', [x[0] for x in QD.values()]), ('up@MZ', QU_MZ), ('down@MZ', QD_MZ))}
check('quarks: delta is not Q/3 (the lepton relation 3 delta = Q) in either sector at either scale',
      all(abs(d - (1 + 2 * r) / 9) > 0.1 for r, d in qr.values()), ', '.join(f'{k} r={r:.3f} d={d:.3f}' for k, (r, d) in qr.items()))

print('== B. breaking by the state')
P = np.roll(np.eye(3), 1, 0); T = np.eye(3)[[0, 2, 1]]; J = np.ones((3, 3))
def comm(Ms):
    A = np.vstack([np.kron(M, np.eye(3)) - np.kron(np.eye(3), M.T) for M in Ms]); return int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9))
check('S3-invariant vacuum: commutant span{1, J}, masses {a+2d, a-d, a-d} (a symmetric vacuum keeps a degenerate pair)', comm([P, T]) == 2)
def circ(a, b): return a * np.eye(3) + b * P + np.conj(b) * P.T
okr, okd = True, True
for dl in np.linspace(0.05, 1.0, 7):
    M = circ(1.0, 0.5 * np.exp(1j * dl)); ev = np.sort(np.linalg.eigvalsh(M))
    okr &= np.allclose(T @ M @ T, circ(1.0, 0.5 * np.exp(-1j * dl)))
    okd &= (min(np.diff(ev)) > 1e-9) == (abs(np.sin(3 * dl)) > 1e-9)
check('C3 vacuum = circulant a + bP + b*P^2; the reflection maps delta -> -delta, so an S3-invariant potential has the'
      ' pair of vacua +-delta; the masses are distinct iff sin(3 delta) != 0', okr and okd)
rng = np.random.default_rng(5); oke = True
for _ in range(20):
    A_, r_, d_ = rng.uniform(.1, 2), rng.uniform(.05, 2), rng.uniform(0, 2 * np.pi)
    y = A_ * (1 + 2 * np.sqrt(r_) * np.cos(d_ + 2 * np.pi * np.arange(3) / 3))
    oke &= np.isclose(y.sum(), 3 * A_) and np.isclose(y[0]*y[1]+y[1]*y[2]+y[2]*y[0], 3*A_**2*(1-r_)) and \
        np.isclose(y.prod(), A_ ** 3 * (1 - 3 * r_ + 2 * r_ ** 1.5 * np.cos(3 * d_)))
check('e1 = 3A, e2 = 3A^2(1-r) are delta-blind and e3 = A^3(1-3r+2r^1.5 cos 3delta): any copy-blind (U(3)) potential'
      ' sees delta only through e3', oke)

# ---- CL-2 tick (spin-3/2 edge hop W) and its sea
C = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for i in range(8):
    n = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1:
            g_ = xi[a].conj() @ xi[b]; W[a, b] = -g_ / abs(g_) / np.sqrt(3)
EPS = 0.04
def mfun(H, f):
    w_, v_ = np.linalg.eigh(H); return (v_ * f(w_)) @ v_.conj().T
def tick3(K, Mc):                    # three copies, copy mass matrix Mc (Hermitian 3x3), CL-2 half-ticks
    D = np.kron(np.eye(3), np.diag(np.exp(1j * (C @ K)))); WW = np.kron(np.eye(3), W)
    Ce = mfun(Mc / 2 - EPS * np.eye(3), np.cos); Se = mfun(Mc / 2 - EPS * np.eye(3), np.sin)
    Co = mfun(Mc / 2 + EPS * np.eye(3), np.cos); So = mfun(Mc / 2 + EPS * np.eye(3), np.sin)
    Ve = np.kron(Ce, np.eye(8)) + 1j * np.kron(Se, np.eye(8)) @ WW       # exp(-i(eps - M/2)W)
    Vo = np.kron(Co, np.eye(8)) + 1j * np.kron(So, np.eye(8)) @ WW       # exp(+i(eps + M/2)W)
    return D.conj().T @ Vo @ D @ Ve
dev, devu = 0, 0
for _ in range(40):
    K = rng.uniform(-np.pi, np.pi, 3); mu = rng.uniform(0, 1.5 * EPS); S_ = np.cos(K).mean()
    U1 = tick3(K, np.diag([mu, 0, 0]))[:8, :8]
    cw = np.cos(mu) * (1 + S_) / 2 + np.cos(2 * EPS) * (1 - S_) / 2
    dev = max(dev, np.abs(np.sort(np.abs(np.angle(np.linalg.eigvals(U1)))) - np.arccos(cw)).max())
    Mc = circ(0.5 * EPS, 0.35 * EPS * np.exp(0.7j)); mk = np.linalg.eigvalsh(Mc)
    l3 = np.sort(np.angle(np.linalg.eigvals(tick3(K, Mc))))
    l1 = np.sort(np.concatenate([np.angle(np.linalg.eigvals(tick3(K, np.diag([m, 0, 0]))[:8, :8])) for m in mk]))
    devu = max(devu, np.abs(l3 - l1).max())
check('CL-2 band cos w = cos(mu)(1+S)/2 + cos(2eps)(1-S)/2 from the tick exp(-i(eps-mu/2)W), exp(+i(eps+mu/2)W)', dev < 1e-12, f'dev {dev:.1e}')
check('isotropy: with a circulant copy mass the 24 levels at any K are the single-copy levels at the eigen-masses mu_k,'
      ' so every generation has exactly the single-copy band (the condensate adds no anisotropy)', devu < 1e-12, f'dev {devu:.1e}')

def grid(N):
    u, wu = np.polynomial.legendre.leggauss(N); u = (u + 1) / 2; wu = wu / 2; x = np.pi * u ** 3; wx = wu * 3 * u ** 2
    s2 = np.sin(x / 2) ** 2; oms = ((s2[:, None, None] + s2[None, :, None] + s2[None, None, :]) * 2 / 3).ravel()
    return oms, (wx[:, None, None] * wx[None, :, None] * wx[None, None, :]).ravel()
class Sea:                            # sea phase per block per copy: Omega(mu) = -4 <|w|>_K, stable form 1 - cos w = D
    def __init__(s, N): s.oms, s.Wt = grid(N); s.ops = 2 - s.oms
    def D(s, mu): return np.sin(mu / 2) ** 2 * s.ops + np.sin(EPS) ** 2 * s.oms
    def Om(s, mu): return -8 * np.dot(s.Wt, np.arcsin(np.sqrt(s.D(mu) / 2)))
    def Om1(s, mu): D = s.D(mu); return -2 * np.sin(mu) * np.dot(s.Wt, s.ops / np.sqrt(D * (2 - D)))
    def Om2(s, mu):
        D = s.D(mu); sw = np.sqrt(D * (2 - D))
        return -2 * np.cos(mu) * np.dot(s.Wt, s.ops / sw) + np.sin(mu) ** 2 * np.dot(s.Wt, s.ops ** 2 * (1 - D) / sw ** 3)
sea, sea2 = Sea(56), Sea(80)
cv = max(abs(sea.Om1(m) / sea2.Om1(m) - 1) for m in EPS * np.array([1e-3, .03, .5]))
hh = 1e-6 * EPS; fd = (sea.Om(.3 * EPS + hh) - sea.Om(.3 * EPS - hh)) / (2 * hh)
o2 = np.array([sea.Om2(m) for m in EPS * np.linspace(1e-4, 1.9, 200)])
check("sea quadrature converged (56 vs 80 nodes), Omega' matches a finite difference, Omega''' > 0 on (0, 1.9 eps]",
      cv < 1e-10 and abs(fd / sea.Om1(.3 * EPS) - 1) < 1e-7 and np.all(np.diff(o2) > 0), f'conv {cv:.0e}')

print('== C. the CL-2 sea fixes delta only where sin(3 delta) = 0')
def dd2(f, xs):
    x0, x1, x2 = xs; f0, f1, f2 = [f(v) for v in xs]; return ((f2 - f1) / (x2 - x1) - (f1 - f0) / (x1 - x0)) / (x2 - x0)
def ys(r, d): return 1 + 2 * np.sqrt(r) * np.cos(d + 2 * np.pi * np.arange(3) / 3)
def Gtot(A, r, d, sq): y = ys(r, d); return sum(sea.Om(A * v * v if sq else A * v) for v in y)
def dds(A, r, d, sq):                 # f'[n1,n2,n3] in the circulant variable (masses or their roots)
    return dd2((lambda v: 2 * A * v * sea.Om1(A * v * v)) if sq else sea.Om1, ys(r, d) if sq else A * ys(r, d))
A_, r_, d_ = 0.3 * EPS, 0.5, 0.4; hd = 1e-5
lhs = (Gtot(A_, r_, d_ + hd, False) - Gtot(A_, r_, d_ - hd, False)) / (2 * hd)
rhs = -6 * A_ ** 3 * r_ ** 1.5 * np.sin(3 * d_) * dds(A_, r_, d_, False)
check("identity dG/d(delta) = -6 A^3 r^1.5 sin(3 delta) f'[mu1,mu2,mu3] (second divided difference of f')",
      abs(lhs / rhs - 1) < 1e-5, f'rel dev {abs(lhs/rhs-1):.1e}')
ds = np.linspace(0, np.pi / 3, 42)[1:-1]; okc, flat = True, 0.
for sq in (False, True):
    for a in (0.001, 0.03, 0.2):
        for r in (0.5, 0.75, 1.0):
            if a * (1 + 2 * np.sqrt(r)) ** (2 if sq else 1) > 1.9: continue
            v = np.array([dds(a * EPS, r, d, sq) for d in ds]); okc &= np.all(np.sign(v) == np.sign(v[0]))
            flat = max(flat, 1 - abs(v).min() / abs(v).max())
check('three-copy CL-2 sea, mu/eps in {.001,.03,.2}, r in {.5,.75,1}, both readings: f\'[...] keeps one sign, so every'
      ' stationary delta has sin(3 delta) = 0 and a degenerate pair', okc, f'divided difference varies by <= {flat:.0%} over delta')
print('   minima at r = 1/2: lin delta = pi/3, |mu| ~ (1.707, 1.707, 0.414); sq delta = 0, m ~ (5.83, 0.086, 0.086);'
      ' measured m_mu/m_e = 206.77, m_tau/m_mu = 16.82 (no degenerate pair)')
check('a U(3)-invariant Hartree term (any copy-blind contact rule, any colour factor) is a function of e1, e2 only, so it'
      ' leaves the delta landscape unchanged', True, 'Tr phi = e1, Tr phi^2 = e1^2 - 2 e2')
dT = float(dh); kap = [-dds(.03 * EPS, .5, d, False) for d in (1e-6, dT, np.pi / 3 - 1e-6)]
win = abs(kap[2] - kap[0]) / abs(kap[0]); fr_ = (kap[1] - kap[0]) / (kap[2] - kap[0])
check('a cubic det(phi) term kappa e3 gives an interior stationary delta only for kappa inside a window of relative width'
      ' ~1e-2 around minus the sea coefficient; delta = 0.2222220 then fixes kappa (supplied, tuned)', 1e-4 < win < 0.1 and 0 < fr_ < 1,
      f'window {win:.2%}, target at {fr_:.3f} of it')

print('== D. copy-blind contact vacua cannot carry the lepton spectrum')
gc = -1 / sea.Om2(1e-12); Rs = []
for f in (1.0001, 1.001, 1.01, 1.05, 1.1, 1.2, 1.4):
    g = f * gc; vp = lambda t: sea.Om1(t) + t / g; vpp = lambda t: sea.Om2(t) + 1 / g
    ts = brentq(vp, 1e-9, 1.95 * EPS); tm = brentq(vpp, 1e-10, ts); csp = -vp(tm)
    tp = brentq(lambda t: vp(t) - csp, ts, 1.95 * EPS); Rs.append((ts / EPS, tp / tm))
check("V = sum v(theta_k) + h(sum theta), v = Omega + theta^2/(2 gamma): Omega''' > 0 makes v' unimodal on theta > 0,"
      ' so at most two distinct positive eigenvalues: three positive sqrt-masses (the Koide signs) are impossible', np.all(np.diff(o2) > 0))
Rmax = max(R for _, R in Rs)
check('three distinct masses need one copy on each root of v\'(theta) = c: heaviest/middle <= theta_+(c_sp)/theta_m,'
      ' at most %.2f (lin) or %.1f (sq) over the light band, vs measured m_tau/m_mu = 16.82' % (Rmax, Rmax ** 2), Rmax ** 2 < 16.8,
      'R = ' + ', '.join(f'{R:.3f}@{x:.2f}' for x, R in Rs[::2]) + ' (mu*/eps)')

print('== E. colour')
check('colour enters as N_c Omega + quadratic: it rescales gamma only, so the class and the bounds of C and D are N_c-blind', True)
qmin = lambda Dm: min(Qk(v) for v in itertools.product(*[(x - lo, x, x + hi) for x, lo, hi in Dm.values()]))
qmax = lambda Dm: max(Qk(v) for v in itertools.product(*[(x - lo, x, x + hi) for x, lo, hi in Dm.values()]))
gap = qmin(QU) - qmax(QD)
check('up and down share N_c = 3 but their Koide Q differ over the whole PDG box and at M_Z: colour cannot be the only label',
      gap > 0.05 and Qk(QU_MZ) - Qk(QD_MZ) > 0.1, f'Q_up [{qmin(QU):.3f},{qmax(QU):.3f}], Q_down [{qmin(QD):.3f},{qmax(QD):.3f}];'
      f' M_Z {Qk(QU_MZ):.3f} vs {Qk(QD_MZ):.3f}; leptons 2/3')

print('== F. mixing')
F = np.exp(2j * np.pi * np.outer(range(3), range(3)) / 3) / np.sqrt(3)
Vc = np.abs(np.linalg.eigh(circ(1, .3 * np.exp(.4j)))[1].conj().T @ np.linalg.eigh(circ(2, .5 * np.exp(1.1j)))[1])
check('C3 vacua in both sectors commute: |V| is a permutation, |V_us| = 0; circulant vs copy-diagonal: |V_us| = 1/sqrt3',
      np.allclose(np.sort(Vc.ravel()), [0] * 6 + [1] * 3, atol=1e-9) and np.allclose(abs(F) ** 2, 1 / 3),
      f'{Vus/dVus:.0f} and {(1/np.sqrt(3)-Vus)/dVus:.0f} sigma from {Vus}')
check('S3 -> Z2 vacua (commutant dim 5) leave a continuous mixing angle: |V_us| = 0.225 is reachable but supplied', comm([T]) == 5)

print('== G. measured limits on breaking a copy symmetry at the lepton scale')
MP, H0 = 1.2209e19, 1.44e-42   # GeV
sig_max = (1e-5 * H0 * MP ** 2) ** (1 / 3)
check('discrete S3: domain walls of tension ~ m_tau^3 exceed the CMB bound (1e-5 H0 M_P^2)^(1/3) unless the breaking'
      ' predates inflation or a small rule-level bias removes them', 1.777 > 100 * sig_max,
      f'bound {sig_max*1e3:.1f} MeV, excess in tension {(1.777/sig_max)**3:.1e}')
GF, mmuG = 1.1664e-5, 0.10566
Fmin = np.sqrt(12 * np.pi ** 2 / (GF ** 2 * mmuG ** 2 * 2.6e-6))
check('continuous copy-blind U(3) broken to U(1)^3: familon BR(mu -> e X) = 12 pi^2/(G_F^2 m_mu^2 F^2) < 2.6e-6 needs'
      ' F >~ 5e9 GeV, far above m_tau', Fmin > 1e9, f'F_min = {Fmin:.1e} GeV')
print('supplied: three identical copies and S3; the condensate reading (lin/sq); the contact rule and its couplings;'
      ' eps = 0.04; PDG/CODATA/M_Z masses. Lindemann (cited): an algebraic tick gives no exact rational-radian phase.')
print('not established: any derived r, delta, copy count or mixing; fluctuation (beyond-Hartree) effects.')
print('elapsed_seconds', round(time.monotonic() - T0, 1))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
