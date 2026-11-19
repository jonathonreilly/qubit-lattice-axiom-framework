#!/usr/bin/env python3
"""Is the cell's own nu^c the dark matter?  (supplied models; exact charge algebra; finite diagnostics; estimates)
 A  one-family charges: nu^c links, N = 3B+L anomalies, the residual Z4 of N, and the identity N = -(B-L) mod 4 on
    colour singlets; census of fermion operators up to four fields (Majorana-type, Delta(B-L) = 4 uniqueness)
 B  Z4 grading in a Fock toy: every Delta N = 2 expectation vanishes to all orders in the Delta N = 4 coupling
 C  condensate route: pairing gap equation on the CL-2 light band (band formula checked on the tick itself);
    critical coupling, M^2 ln(1/M) law, tuning needed for a keV mass
 D  production: splits conserve each species' number; relic arithmetic; Dodelson-Widrow; seesaw; X-ray; Lyman-alpha;
    phase space; N_eff; domain walls
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 90
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
from math import comb
import numpy as np
from scipy.linalg import schur, expm

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- A. one family as left-handed Weyl fields (supplied content: the cell's 16) ----------------
# name: (colour +1=3,-1=3bar, SU2 doublet, Y, B, Lep, multiplicity)
F = {'Q': (1, 1, Fr(1, 6), Fr(1, 3), 0, 6), 'u': (-1, 0, Fr(-2, 3), Fr(-1, 3), 0, 3), 'd': (-1, 0, Fr(1, 3), Fr(-1, 3), 0, 3),
     'L': (0, 1, Fr(-1, 2), 0, 1, 2), 'e': (0, 0, Fr(1), 0, -1, 1), 'n': (0, 0, Fr(0), 0, -1, 1)}
N = {k: 3 * v[3] + v[4] for k, v in F.items()}; BL = {k: v[3] - v[4] for k, v in F.items()}
print('== A. charges, anomalies, residual symmetry (exact rationals)')
check('A1 nu^c: colour and SU(2) singlet, Y = Q = 0; N = 3B+L = -1, B-L = +1 (N is the Dirac mode number: +1 on Q, L, -1 on the conjugates)',
      F['n'][:3] == (0, 0, 0) and N['n'] == -1 and BL['n'] == 1 and all(N[k] == (1 if k in 'QL' else -1) for k in F))
def tr(f, keep=F):
    return sum(f(k, *v) for k, v in F.items() if k in keep)
fam, nonu = set(F), set(F) - {'n'}
an = {'N-grav': lambda k, c, s, y, b, l, m: m * N[k], 'N^3': lambda k, c, s, y, b, l, m: m * N[k] ** 3,
      'N-SU2^2': lambda k, c, s, y, b, l, m: (m // 2) * Fr(1, 2) * N[k] if s else 0,
      'N-SU3^2': lambda k, c, s, y, b, l, m: (m // 3) * Fr(1, 2) * N[k] if c else 0,
      'N-Y^2': lambda k, c, s, y, b, l, m: m * N[k] * y * y, 'N^2-Y': lambda k, c, s, y, b, l, m: m * N[k] ** 2 * y,
      'BL-grav': lambda k, c, s, y, b, l, m: m * BL[k], 'BL^3': lambda k, c, s, y, b, l, m: m * BL[k] ** 3,
      'BL-Y^2': lambda k, c, s, y, b, l, m: m * BL[k] * y * y, 'BL-SU2^2': lambda k, c, s, y, b, l, m: (m // 2) * Fr(1, 2) * BL[k] if s else 0}
A_w = {k: tr(f, fam) for k, f in an.items()}; A_wo = {k: tr(f, nonu) for k, f in an.items()}
z16 = lambda keep: sum(F[k][5] * (1 if N[k] % 4 == 1 else -1) for k in keep) % 16
check('A2 anomaly traces with nu^c: N-grav = N^3 = 0, N-SU2^2 = 2, N-Y^2 = -2, N-SU3^2 = 0; all six B-L traces 0',
      A_w['N-grav'] == 0 and A_w['N^3'] == 0 and A_w['N-SU2^2'] == 2 and A_w['N-Y^2'] == -2 and A_w['N-SU3^2'] == 0
      and all(A_w[k] == 0 for k in A_w if k.startswith('BL')) and A_w['N^2-Y'] == 0, f"without nu^c: N-grav {A_wo['N-grav']}, BL-grav {A_wo['BL-grav']}, BL^3 {A_wo['BL^3']}")
inst2 = sum((F[k][5] // 2) * N[k] for k in F if F[k][1]); inst3 = sum((F[k][5] // 3) * N[k] for k in F if F[k][0])
check('A3 SU(2) instanton changes N by 4 (four doublets), SU(3) by 0: Z_k of N survives iff k | 4; spin-Z4 count (charge 1 minus charge 3 Weyls) = 0 mod 16 with nu^c, 1 without',
      inst2 == 4 and inst3 == 0 and z16(fam) == 0 and z16(nonu) == 1, f'dN(SU2) {inst2}, dN(SU3) {inst3}, Z16: {z16(fam)} / {z16(nonu)}')
# operator census: monomials of 2 and 4 fields from the 6 LH fields and their 6 conjugates; Lorentz: even #LH and even #RH
fields = [(k, +1) for k in F] + [(k, -1) for k in F]
def charges(mono):
    c3 = sum(F[k][0] * s for k, s in mono); nd = sum(F[k][1] for k, s in mono)
    y = sum(F[k][2] * s for k, s in mono); n_ = sum(N[k] * s for k, s in mono); bl = sum(BL[k] * s for k, s in mono)
    nL = sum(1 for k, s in mono if s > 0); return c3, nd, y, n_, bl, nL
ops = []
for r in (2, 4):
    for mono in itertools.combinations_with_replacement(fields, r):
        c3, nd, y, n_, bl, nL = charges(mono)
        if c3 % 3 == 0 and nd % 2 == 0 and y == 0 and nL % 2 == 0:
            ops.append((mono, n_, bl))
ident = all((n_ + bl) % 4 == 0 for _, n_, bl in ops)
maj = [m for m, n_, bl in ops if n_ % 4 == 2]; maj2 = [m for m in maj if len(m) == 2]
bl4 = [m for m, n_, bl in ops if abs(bl) == 4]
withn_dN4 = sorted({''.join(k + ('' if s > 0 else '*') for k, s in m) for m, n_, bl in ops if abs(n_) == 4 and any(k == 'n' for k, s in m)})
check('A4 identity on every colour-singlet operator: N + (B-L) = 4B = 0 mod 4, so the residual Z4 of N acts as Z4 of B-L (the Spin(10) centre on singlets)',
      ident, f'{len(ops)} gauge-allowed scalar monomials (2 and 4 fields)')
check('A5 the only two-field Delta N = 2 singlet is the nu^c Majorana mass nu^c nu^c (Dirac nu nu^c needs a Higgs); Z4 forbids it',
      len(maj2) == 2 and all(all(k == 'n' for k, s in m) for m in maj2), f'{len(maj)} Delta N = 2 mod 4 monomials in all, all forbidden')
check('A6 four-fermion Delta(B-L) = 4 singlets: only (nu^c)^4 and its conjugate; four-fermion Delta N = 4 operators containing nu^c: ' + ', '.join(withn_dN4),
      len(bl4) == 2 and all(all(k == 'n' for k, s in m) for m in bl4))
print('   so with links on every exact current (CL-5), an exact B-L would be a massless link on matter; the measured absence of')
print('   a B-L fifth force (g_BL < ~1e-24) needs B-L broken, and at four-fermion order only a point-split (nu^c)^4 does it')

# ---------------- B. Z4 grading in a Fock toy ----------------
print('== B. Z4 of N in a Fock toy (2 sites x 2 components of nu^c, 2 spectator modes; Jordan-Wigner, 64 states)')
M_ = 6; dim = 2 ** M_
def ann(j):
    a = np.array([[0, 1], [0, 0]]); z = np.diag([1, -1]); op = np.array([[1.0]])
    for i in range(M_): op = np.kron(op, z if i < j else (a if i == j else np.eye(2)))
    return op
c = [ann(j) for j in range(M_)]; Nop = sum(x.T @ x for x in c); rng = np.random.default_rng(7)
def herm(X): return X + X.conj().T
hop = herm(sum(rng.normal() * c[i].T @ c[j] for i in range(M_) for j in range(M_)) / 2)
dens = sum(rng.normal() * (c[i].T @ c[i]) @ (c[j].T @ c[j]) for i in range(M_) for j in range(i))
quad = c[0] @ c[1] @ c[2] @ c[3]                         # nu^c(x)_1 nu^c(x)_2 nu^c(y)_1 nu^c(y)_2
pair4 = herm(quad) ; pair2 = herm(c[0] @ c[1])
Z4 = np.diag(np.exp(1j * np.pi / 2 * np.diag(Nop)))
onsite = c[0] @ c[1] @ c[0] @ c[1]
worst = 0.0
for g in (0.3, 3.0, 30.0):
    H = hop + dens + g * pair4
    w, V = np.linalg.eigh(H); rho = V @ np.diag(np.exp(-(w - w[0]) / 0.7)) @ V.conj().T; rho /= np.trace(rho)
    worst = max(worst, max(abs(np.trace(rho @ c[i] @ c[j])) for i in range(M_) for j in range(M_)), np.linalg.norm(Z4 @ H - H @ Z4))
eps_ = [1e-3, 2e-3]; resp = []
for e in eps_:
    H = hop + dens + 3.0 * pair4 + e * pair2; w, V = np.linalg.eigh(H)
    rho = V @ np.diag(np.exp(-(w - w[0]) / 0.7)) @ V.conj().T; rho /= np.trace(rho); resp.append(abs(np.trace(rho @ c[0] @ c[1])))
check('B1 the Delta N = 4 term commutes with Z4 = i^N; at any coupling (0.3, 3, 30) every pairing <c_i c_j> vanishes exactly (thermal state)',
      worst < 1e-12, f'max |<cc>|, |[Z4,H]| = {worst:.1e}')
check('B2 an explicit Delta N = 2 term eps c c restores <c c> linearly in eps: the Majorana mass is a supplied parameter, not generated',
      resp[0] > 1e-6 and abs(resp[1] / resp[0] - 2) < 1e-2, f'<c0c1> at eps 1e-3, 2e-3: {resp[0]:.3e}, {resp[1]:.3e}')
check('B3 one Weyl nu^c at one point has two components: (nu^c)^4 vanishes there (Pauli), so the term must be point-split over cells',
      np.abs(onsite).max() == 0 and np.abs(quad).max() > 0)

# ---------------- C. condensate route on the CL-2 light band ----------------
print('== C. spontaneous Z4 -> Z2: pairing gap equation 1 = g I(M), I(M) = int_BZ 1/sqrt(w^2+M^2) on the CL-2 band')
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); OPP = 7 - np.arange(8)
def coherent(j, nv):
    th, ph, d = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]; W0 = np.zeros((8, 8), complex)
for s_, t_ in itertools.product(range(8), repeat=2):
    if abs(CORN[s_] - CORN[t_]).sum() == 1: g_ = XI[s_].conj() @ XI[t_]; W0[s_, t_] = -g_ / abs(g_) / np.sqrt(3)
def Wa(a): return np.cos(a) * W0 + 1j * np.sin(a) * np.eye(8)
def half(psi, Wm, odd):
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    b_ = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8) @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T
    p = b_.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p
def blocks(mu, b, L=8):
    We, Wo = Wa(mu / 2 + b), Wa(mu / 2 - b); Nn = L ** 3; E = np.eye(Nn).reshape(Nn, L, L, L)
    Ue, Uo = [np.stack([half(e, Wm, od).ravel() for e in E], 1) for Wm, od in ((We, 0), (Wo, 1))]; U = Uo @ Ue
    s = lambda v: np.ravel_multi_index(tuple(np.asarray(v) % L), (L, L, L)); n0 = np.array([1, 1, 1])
    return {R: np.array([[U[s(2 * (n0 + R) + CORN[a]), s(2 * n0 + CORN[b_])] for b_ in range(8)] for a in range(8)])
            for R in itertools.product((-1, 0, 1), repeat=3)}
def cosw(K, mu, b):
    A = (np.cos(2 * b) + np.cos(mu)) / 2; return A * np.mean(np.cos(K), axis=-1) - (np.cos(2 * b) - np.cos(mu)) / 2
bb = 0.3; errs = []
for mu in (0.0, 0.2):
    BLk = blocks(mu, bb)
    for K in (np.array([0.3, 0.2, 0.1]), np.array([1.0, 0.4, -0.7]), np.array([2.5, -1.9, 0.6])):
        T, _ = schur(sum(Mm * np.exp(-1j * (K @ np.array(R, float))) for R, Mm in BLk.items()), output='complex')
        errs.append(np.abs(np.cos(np.angle(np.diag(T))) - cosw(K, mu, bb)).max())
check('C1 CL-2 band checked on the tick (b = 0.3, mu = 0, 0.2): cos w = A S - (cos 2b - cos mu)/2 with S = (cos K1 + cos K2 + cos K3)/3 on all 8 bands',
      max(errs) < 1e-10, f'max err {max(errs):.1e}')
# radial quadrature over the block Brillouin zone (-pi,pi]^3, light band at mu = 0
gold = np.pi * (3 - np.sqrt(5)); nd = 600; zz = 1 - (2 * np.arange(nd) + 1) / nd
dirs = np.stack([np.sqrt(1 - zz ** 2) * np.cos(gold * np.arange(nd)), np.sqrt(1 - zz ** 2) * np.sin(gold * np.arange(nd)), zz], 1)
rmax = np.pi / np.abs(dirs).max(1); xg, wg = np.polynomial.legendre.leggauss(120)
def I_of(M, b=bb):
    tot = 0.0
    for d_, rm in zip(dirs, rmax):
        u = np.log(1e-9 * rm) + (np.log(rm) - np.log(1e-9 * rm)) * (xg + 1) / 2
        r = np.exp(u); jac = r * (np.log(rm) - np.log(1e-9 * rm)) / 2
        w = 2 * np.arcsin(np.cos(b) * np.sqrt(np.sum(np.sin(np.outer(r, d_) / 2) ** 2, 1) / 3))   # exact: 1 - cos w = cos^2 b (1 - S) at mu = 0
        tot += np.sum(wg * jac * r ** 2 / np.sqrt(w ** 2 + M ** 2))
    return tot * 4 * np.pi / nd / (2 * np.pi) ** 3
v = np.cos(bb) / np.sqrt(3); I0 = I_of(0.0); Ms = np.array([1e-2, 3e-3, 1e-3]); dI = np.array([I0 - I_of(m) for m in Ms])
fM = dI / Ms ** 2; slope = (fM[2] - fM[0]) / np.log(Ms[0] / Ms[2])
check('C2 I(0) is finite (Fermi point, no Fermi surface): a supercritical coupling g_c = 1/I(0) is needed; I(0) - I(M) -> M^2 ln(1/M)/(4 pi^2 v^3), v = sin(eps)/sqrt3',
      np.isfinite(I0) and abs(slope * 4 * np.pi ** 2 * v ** 3 - 1) < 0.05, f'I(0) = {I0:.4f}, log slope x 4pi^2 v^3 = {slope * 4 * np.pi ** 2 * v ** 3:.3f}')
unit = np.sqrt(3) / (2 * np.sqrt(8 * np.pi)) * 1.2209e19      # GeV per rad/tick (a = sqrt(8 pi) l_P, as in agents/dark-matter)
Cc = fM[2] - slope * np.log(1 / Ms[2])
for mk in (7.1e-6, 19.2e-6):
    Mt = mk / unit; print(f'   M = {mk*1e6:.1f} keV = {Mt:.2e} rad/tick: tuning 1 - g_c/g = {(Mt**2*(slope*np.log(1/Mt)+Cc))/I0:.1e}')
b2 = np.pi / 2 - 0.04; v2 = np.cos(b2) / np.sqrt(3); I02 = I_of(0.0, b2); d2 = I02 - I_of(1e-4, b2); C2c = d2 / 1e-8 - np.log(1e4) / (4 * np.pi ** 2 * v2 ** 3)
Mt = 19.2e-6 / unit; print(f'   at the vacuum-stable step eps = 0.04: I(0) = {I02:.3f}, tuning for 19.2 keV = {Mt**2*(np.log(1/Mt)/(4*np.pi**2*v2**3)+C2c)/I02:.1e}')
check('C3 a keV Majorana mass from a cell-scale condensate needs g tuned to g_c within 1e-46 (b = 0.3) to 4e-43 (eps = 0.04): power law, not exponential', (9e-24) ** 2 * (slope * 55 + Cc) / I0 < 1e-44)

# ---------------- D. production and measured bounds (estimates) ----------------
print('== D. production and measured bounds (estimates; formulas and data supplied)')
V1 = np.zeros((16, 8))
for j in range(4):
    for p in (0, 1): V1[[4 * j + p, 4 * j + 2 + p], 2 * j + p] = 1 / np.sqrt(2)
Vsp = np.kron(V1, np.eye(3)); C0 = np.diag(rng.uniform(0, 1, 24)); C1 = Vsp @ C0 @ Vsp.T
nsp = [np.trace(C0[s::3, s::3]) for s in range(3)]; nsp1 = [np.trace(C1[s::3, s::3]) for s in range(3)]
check('D1 a split is an isometry on one-mode amplitudes with the species index carried in parallel: each species number (nu^c included) is unchanged, the empty state maps to itself: splits make no nu^c',
      np.allclose(V1.T @ V1, np.eye(8)) and np.allclose(nsp, nsp1), f'species numbers {np.round(nsp, 3)} -> {np.round(nsp1, 3)}')
heat_f, heat_e = 0.175, 0.213     # agents/cosmology out.txt: half-filled sea, mu=0, per split
a_cm = np.sqrt(8 * np.pi) * 1.616e-33; rho_split = 0.5 * heat_f * heat_e * unit / a_cm ** 3; rho_c = 1.0537e-5 * 0.674 ** 2
print(f'   half-filled sea instead: each split leaves {0.5*heat_f*heat_e:.3f} rad/tick per site = {rho_split:.1e} GeV/cm^3, {rho_split/rho_c:.0e} x rho_c (every split, today included)')
s0, rch = 2891.2, 1.0537e-5; Och = 0.1200; z3 = 1.2020569
Yeq = lambda gs: 135 * z3 / (8 * np.pi ** 4) * 2 / gs
m_th = {gs: Och * rch / (Yeq(gs) * s0) * 1e9 for gs in (106.75, 112.0, 224.0)}
check('D2 if the Delta N = 4 vertex keeps nu^c in equilibrium at the cell scale, Omega_c/Omega_b = 5.36 needs m = 112 eV (g*s 106.75; 117, 235 eV for 112, 224): hot, excluded as all of the DM',
      abs(m_th[106.75] - 112) < 1, ', '.join(f'{k}: {v_:.0f} eV' for k, v_ in m_th.items()))
TxTn = (10.75 / 106.75) ** (1 / 3); mLya = 5.3e3; m_x = TxTn * 4.46e3 * (mLya / 1e3) ** (4 / 3)
print(f'   a nu^c at 7.1 keV in equilibrium at the cell scale gives Omega h^2 = {7.1e3/m_th[106.75]*Och:.1f} (overcloses x{7.1e3/m_th[106.75]:.0f})')
check('D3 Lyman-alpha (thermal WDM > 5.3 keV) maps, for a cell-scale spectrum (T/T_nu = 0.465), to m > 19 keV, i.e. Y/Y_eq < 6e-3 (freeze-in, not equilibrium)',
      18e3 < m_x < 21e3, f'm > {m_x/1e3:.1f} keV, Y/Y_eq < {m_th[106.75]/m_x:.1e}; DW check: T/T_nu = 1 gives 4.46 keV at m_th = 1 keV')
GH = 1 / (1.66 * np.sqrt(106.75)) * 0.5 ** 3 * (1.2209e19 / unit)
print(f'   freeze-in through c/Lambda^2 at Lambda = 1 rad/tick, T_max = 0.5 rad/tick: Gamma/H = {GH:.3f} kappa c^2, Y/Y_eq = {GH/3:.3f} kappa c^2 (kappa ~ 0.1-10 channels)')
vEW, mnu = 174.0, 0.0502e-9; m_ss = vEW ** 2 / unit * 1e9
check('D4 seesaw with a cell-scale Majorana mass (y = 1): m_nu = v^2/M = 1.4e-5 eV, 3500x below sqrt(dm2_atm) = 0.050 eV; M must be < 6e14 GeV',
      abs(m_ss / 1.44e-5 - 1) < 0.05, f'm_nu = {m_ss:.2e} eV, M_max = {vEW**2/mnu:.1e} GeV')
al, GF, hb = 1 / 137.036, 1.1664e-5, 6.582e-25
tau = lambda m, s2: hb / (9 * al * GF ** 2 * s2 * (m * 1e-6) ** 5 / (1024 * np.pi ** 4))
s2_35 = 7e-11; mix = s2_35 / 4 * 7.1e3
check('D5 3.5 keV line (m = 7.1 keV, sin^2 2theta = 7e-11): tau = 6e27 s (>> age 4.4e17 s); that nu^c adds theta^2 M = 1.2e-7 eV to one light mass (rank 1): one nu^c cannot be DM and seesaw partner',
      tau(7.1, s2_35) > 1e27 and mix < 1e-6, f'tau = {tau(7.1, s2_35):.1e} s, theta^2 M = {mix:.1e} eV')
s2_DW = [3e-9 * (Och / 0.1) * (3 / 7.1) ** 1.8, 4 * 3e-9 * (Och / 0.674 ** 2 / 0.2) * (3 / 7.1) ** 1.8]
check('D6 Dodelson-Widrow at 7.1 keV needs sin^2 2theta ~ 0.8-4e-9 (formula spread), >10x the X-ray limit ~1e-10; Lyman-alpha then needs m_DW > 41 keV, where X-ray limits are tighter: DW alone excluded',
      min(s2_DW) > 1e-10 * 5 and 4.46 * 5.3 ** (4 / 3) > 40, f'sin^2 2theta {s2_DW[0]:.1e} .. {s2_DW[1]:.1e}; m_DW > {4.46*5.3**(4/3):.0f} keV')
rho0 = 0.2 * 38.0 * (1.973e-14) ** 3; vmax = 25 / 3e5
mTG = (rho0 * (2 * np.pi) ** 3 / (2 * 4 * np.pi / 3 * vmax ** 3)) ** 0.25 * 1e9
check('D7 Pauli phase-space bound for a dwarf (rho = 0.2 Msun/pc^3, v < 25 km/s): fermion m > ~230 eV, which also excludes the 112 eV relic', 150 < mTG < 400, f'm > {mTG:.0f} eV')
dNeff = (10.75 / 106.75) ** (4 / 3)
check('D8 massless nu^c (exact Z4) thermal at the cell scale: Delta N_eff = 0.047 each, 0.14 for three; Planck 2.99 +- 0.17, ACT+Planck 2.86 +- 0.13 allow it; CMB-S4 (sigma ~0.03) tests it',
      0.04 < dNeff < 0.05, f'Delta N_eff = {dNeff:.4f} per nu^c')
H0, MP = 1.44e-42, 1.2209e19; wall = lambda L: 8 * np.pi * L ** 3 / (3 * H0 * MP ** 2)
check('D9 a cell-scale condensate breaks Z4 -> Z2 spontaneously: walls with sigma ~ Lambda^3 give rho_wall/rho_c ~ 1e59 today (excluded); a 19 keV one is wall-safe',
      wall(unit) > 1e50 and wall(19.2e-6) < 1e-6, f'{wall(unit):.0e}, {wall(19.2e-6):.0e}')
print('theorems: A1-A6 (exact rationals), B1/B3 (exact Z4 grading, Pauli), D1 (species-diagonal isometry). finite: B2, C1-C3. estimates: D2-D9.')
print('supplied: one-family content and assignment, Z4-preserving Delta N = 4 term, coupling c, kappa, T_max, the unit map, contact pairing,')
print('  halo numbers, DW/decay formulas (Abazajian; Pal-Wolfenstein), Lyman-alpha 5.3 keV (Irsic 2017), all measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
