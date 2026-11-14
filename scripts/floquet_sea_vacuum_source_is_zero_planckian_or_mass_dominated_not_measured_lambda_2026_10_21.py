#!/usr/bin/env python3
"""Vacuum gravitational source under the draft rules (CL-2 tick, CL-6 conditional canonical stress,
filled negative-quasi-energy sea, G = a^2/(8 pi) per cell), against the measured rho_Lambda.
A. bands of the supplied CL-2 tick: det U = 1 sum rule, the mu = 0 pi-shift symmetry, the sea phase
   per block, Floquet Hellmann-Feynman, the massive residual, zone dependence of the sea's kinetic stress.
B. one-block model M1 (relay-number agent): dressed-vacuum Born-mean source, K-conserving and with a
   supplied counter-rotating pair+quantum term; Floquet second-order shift -(g^2/2) cot(Delta/2).
C. condensate rule (mass-rule agent, Hartree): condensation energy of the dressed sea.
D. unit conversion, measured rho_Lambda, zero-mean record-noise wander under a unimodular reading.
Supplied models; no physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, logm
from numpy.polynomial.legendre import leggauss

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- supplied CL-2 block hop (same construction as the mass-rule runner)
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
I8 = np.eye(8)
def Wm(mu): return np.cos(mu / 2) * W + 1j * np.sin(mu / 2) * I8
def Uk(Ks, mu):
    Dg = np.exp(1j * (np.atleast_2d(Ks) @ C.T)); X = Wm(mu)
    return (Dg.conj()[:, :, None] * X[None] * Dg[:, None, :]) @ X[None]
def bands(Ks, mu):                        # quasi-energies w = -arg(lambda) in (-pi, pi], sorted
    return np.sort(-np.angle(np.linalg.eigvals(Uk(Ks, mu))), axis=1)
N = 20; g1 = (np.arange(N) + 0.5) / N * 2 * np.pi - np.pi
KG = np.array(list(itertools.product(g1, g1, g1)))
PI3 = np.pi * np.ones(3)

print('== A. bands, sum rules and the sea phase (per block = 8 sites; per tick)')
mu = 0.37
check('det U(K) = 1 at every K (W(mu) = e^{i mu/2} exp(i(pi-mu)P_-), rank P_- = 4): sum of all 8 quasi-energies = 0',
      np.abs(np.linalg.det(Uk(KG[::7], mu)) - 1).max() < 1e-12 and np.abs(bands(KG[::7], mu).sum(1)).max() < 1e-10)
w0 = bands(KG, 0.0); wsh = bands(((KG + np.pi + np.pi) % (2 * np.pi)) - np.pi, 0.0)
neg0 = np.where(w0 < 0, w0, 0).sum(1); negsh = np.where(wsh < 0, wsh, 0).sum(1)
check('spectrum symmetric w <-> -w; 4 negative and 4 positive bands at each K (mu = 0.37)',
      np.allclose(np.sort(-bands(KG[::7], mu), 1), bands(KG[::7], mu)) and np.all((bands(KG[::7], mu) < 0).sum(1) == 4))
check('mu = 0: K -> K + pi(1,1,1) maps |w| -> pi - |w|, so occupied phases of each K pair sum to -4 pi exactly',
      np.abs(neg0 + negsh + 4 * np.pi).max() < 1e-9, f'max dev {np.abs(neg0 + negsh + 4 * np.pi).max():.1e}')
Esea0 = neg0.mean()
check('mu = 0 sea phase per block per tick = -2 pi exactly (= 0 mod 2 pi: the vacuum odds return to themselves each tick); '
      'generator (i log U) reading: -pi/4 per site', abs(Esea0 + 2 * np.pi) < 1e-9, f'<E_sea>/block = {Esea0:.12f}')
def Esea(mu, K=KG):
    w = bands(K, mu); return np.where(w < 0, w, 0).sum(1).mean()
def Bsea(Ks, mu):                          # closed form per K (mass-rule runner, rederived there)
    s = np.sin(mu / 2); S1m = (2 * np.sin(np.atleast_2d(Ks) / 2) ** 2).sum(1) / 3; S1p = 2 - S1m
    return 4 * s * np.sqrt(S1p / (S1m + s * s * S1p))
hh = 1e-4; fd = []
for mu in (0.2, 0.6, 1.2):
    fd.append(abs((Esea(mu + hh) - Esea(mu - hh)) / (2 * hh) + Bsea(KG, mu).mean()))
check('Floquet Hellmann-Feynman: dE_sea/dmu = -<B> per block per tick (-<B>/2 from each half-tick), i.e. -<B>/8 per site',
      max(fd) < 1e-6, f'max dev {max(fd):.1e}')
res = {m: Esea(m) - Esea0 for m in (0.05, 0.1, 0.2)}
# zone integral I0 by pyramid quadrature (as in the mass-rule runner)
gu, wu = leggauss(48); et = np.concatenate([[0.0], np.geomspace(1e-12, 1.0, 60)]); gt, wt = leggauss(14)
tn = np.concatenate([(a + b) / 2 + (b - a) / 2 * gt for a, b in zip(et[:-1], et[1:])])
tw = np.concatenate([(b - a) / 2 * wt for a, b in zip(et[:-1], et[1:])])
UU, VV = np.meshgrid(gu, gu, indexing='ij'); WUV = np.outer(wu, wu)
hx = (np.sin(np.pi * tn / 2) ** 2)[:, None, None]
hy = np.sin(np.pi * tn[:, None, None] * UU[None] / 2) ** 2; hz = np.sin(np.pi * tn[:, None, None] * VV[None] / 2) ** 2
S1m = 2 * (hx + hy + hz) / 3; S1p = 2 - S1m; WT = (tw * tn ** 2)[:, None, None] * WUV[None] * 6 * np.pi ** 3 / (2 * np.pi) ** 3
R0 = np.sqrt(S1p / S1m)
I0 = float(np.sum(WT * R0))
def D_of(s):                               # I0 - I(s), cancellation-free
    x = s * s * S1p / S1m; r = np.sqrt(1 + x); return float(np.sum(WT * R0 * x / (r * (1 + r))))
def dI_ds(s):
    x = s * s * S1p / S1m; return -float(np.sum(WT * R0 * s * S1p / S1m * (1 + x) ** -1.5))
fixed = {m: -I0 * m * m for m in res}
print(f'   I0 = {I0:.10f}; massive-sea residual per block (E_sea(mu) - E_sea(0)) vs -I0 mu^2: ' +
      '; '.join(f'mu={m}: {res[m]:.4e} / {fixed[m]:.4e}' for m in res))
check('fixed-mass residual: E_sea(mu) + 2 pi = -I0 mu^2 (1 + O(mu^2 ln mu)) per block per tick (does not cancel)',
      all(abs(res[m] / fixed[m] - 1) < 0.08 for m in res) and abs(res[0.05] / fixed[0.05] - 1) < abs(res[0.2] / fixed[0.2] - 1))
# kinetic stress T_xx = <sum_occ K_x dE_occ/dK_x> over a zone = <E_occ>_face - <E_occ> (integration by parts)
g2 = (np.arange(60) + 0.5) / 60 * 2 * np.pi - np.pi
def face(kx, mu):
    KK = np.array([[kx, a, b] for a in g2 for b in g2]); w = bands(KK, mu); return np.where(w < 0, w, 0).sum(1).mean()
for mu in (0.0,):
    fpi, f0 = face(np.pi, mu), face(0.0, mu)
    p_pi, p_0 = fpi - Esea0, f0 - Esea0
print(f'   sea kinetic stress, mu = 0: zone [-pi,pi): p = {p_pi:.4f}, zone [0,2pi): p = {p_0:.4f}; rho = {Esea0:.4f} per block')
check('the sea\'s pressure is zone-dependent (opposite sign for the two inversion-symmetric zones): the rules do not fix the '
      'vacuum equation of state; neither zone gives p = -rho (w = -1)', abs(p_pi + p_0) < 1e-6 and abs(p_pi) > 0.1
      and abs(p_pi / Esea0 + 1) > 0.1 and abs(p_0 / Esea0 + 1) > 0.1,
      f'w = p/rho = {p_pi / Esea0:.4f} or {p_0 / Esea0:.4f}')

print('== B. one-block model M1: dressed vacuum')
NC = 8
sm = np.array([[0, 1], [0, 0]], float); Z = np.diag([1.0, -1.0]); I2 = np.eye(2); Ic = np.eye(NC)
cb = np.diag(np.sqrt(np.arange(1, NC)), 1)
A = np.kron(np.kron(sm, I2), Ic); B = np.kron(np.kron(Z, sm), Ic); Cc = np.kron(np.kron(I2, I2), cb)
na, nb, nc = A.T @ A, B.T @ B, Cc.T @ Cc
EPS, G = 0.3, 0.12
Vr = A.T @ B.T @ Cc; Vr = Vr + Vr.T; Vc = A.T @ B.T @ Cc.T; Vc = Vc + Vc.T
def m1(Om, g=G, gc=0.0):
    H0 = EPS * (na + nb) + Om * nc; return expm(-1j * H0) @ expm(-1j * (g * Vr + gc * Vc)), H0
def dressed_vac(U):
    lam, V = np.linalg.eig(U); j = np.argmax(abs(V[0])); v = V[:, j] / np.linalg.norm(V[:, j])
    return v, -np.angle(lam[j])
U, H0 = m1(2 * EPS)
v, e = dressed_vac(U)
check('K-conserving M1 (as supplied, coupling a+ b+ c + h.c.): the empty state is an exact Floquet eigenstate with phase 0; '
      'dressed vacuum = bare vacuum, Born-mean source exactly 0', abs(abs(v[0]) - 1) < 1e-14 and abs(e) < 1e-14,
      f'|<0|vac>| - 1 = {abs(v[0]) - 1:.1e}, quasi-energy {e:.1e}')
rows = []
for Dl in (1.2, np.pi, 2 * np.pi - 1.2):
    Om = Dl - 2 * EPS
    for gc in (0.02, 0.01):
        U, H0 = m1(Om, gc=gc); v, e = dressed_vac(U)
        HF = 1j * logm(U); src = (v.conj() @ HF @ v).real; dep = (v.conj() @ H0 @ v).real
        rows.append((Dl, gc, e, src, dep, -(gc ** 2 / 2) / np.tan(Dl / 2)))
print('   (Delta, gc): source / formula: ' + '; '.join(f'({r[0]:.2f},{r[1]}) {r[3]:+.3e}/{r[5]:+.3e}' for r in rows))
ok = all(abs(r[3] - r[2]) < 1e-12 for r in rows)
def pure(Dl, gc):                          # rotating coupling off: isolates the counter-rotating dressing
    U, _ = m1(Dl - 2 * EPS, g=0.0, gc=gc); return dressed_vac(U)[1]
pr = [(Dl, gc, pure(Dl, gc), -(gc ** 2 / 2) / np.tan(Dl / 2)) for Dl in (1.2, 2 * np.pi - 1.2) for gc in (0.02, 0.01)]
ok2 = all(abs(p[2] / p[3] - 1) < 3 * p[1] ** 2 for p in pr) and all(abs(r[2] / r[5] - 1) < 0.03 for r in rows if abs(r[5]) > 1e-8)
print('   rotating coupling off: shift / formula - 1 = ' + ', '.join(f'{p[2] / p[3] - 1:+.1e}' for p in pr) +
      '; with g = 0.12 on, the O(g^2) cross-dressing adds about 2 percent')
pi_rows = [r for r in rows if abs(r[0] - np.pi) < 1e-9]
ok3 = all(abs(r[2]) < 2 * r[1] ** 4 + 2 * G ** 2 * r[1] ** 2 for r in pi_rows)
check('counter-rotating variant (supplied a+ b+ c+ + h.c.): Born-mean source <i log U> of the dressed vacuum = its quasi-energy '
      '= -(gc^2/2) cot(Delta/2) + O(gc^4), Delta = 2 eps + Omega; vanishes at Delta = pi, flips sign above', ok and ok2 and ok3)
r12 = [r for r in rows if abs(r[0] - 1.2) < 1e-9 and r[1] == 0.02][0]; r52 = [r for r in rows if abs(r[0] - (2 * np.pi - 1.2)) < 1e-9 and r[1] == 0.02][0]
print(f'   Delta and 2pi - Delta shifts: {r12[2]:+.6e} and {r52[2]:+.6e} (sum {r12[2] + r52[2]:+.2e}); the bare deposit is '
      f'{r12[4]:.2e} > 0 while the total is < 0: the interaction share carries the sign')
# sum rule: one vacuum coupled to two pair channels at Delta and 2 pi - Delta
def three(Dl, g):
    H0 = np.diag([0.0, Dl, 2 * np.pi - Dl]); V = np.zeros((3, 3)); V[0, 1] = V[1, 0] = V[0, 2] = V[2, 0] = 1
    U = expm(-1j * H0) @ expm(-1j * g * V); v, e = dressed_vac(U); return e
s1, s2 = three(1.2, 0.02), three(1.2, 0.01)
def two(Dl, g):
    H0 = np.diag([0.0, Dl]); V = np.array([[0, 1.0], [1.0, 0]]); U = expm(-1j * H0) @ expm(-1j * g * V); return dressed_vac(U)[1]
s3 = three(1.2, 0.3)
check('Floquet sum rule: channels at Delta and 2 pi - Delta (= -Delta mod 2 pi) cancel the vacuum shift; in this balanced toy to '
      'machine precision at every g tried, while one channel alone gives -(g^2/2) cot(Delta/2)',
      max(abs(s1), abs(s2), abs(s3)) < 1e-12 and abs(two(1.2, 0.02) / (-(0.02 ** 2 / 2) / np.tan(0.6)) - 1) < 1e-3,
      f'balanced shift {s1:.1e} (g=0.02), {s3:.1e} (g=0.3); single channel {two(1.2, 0.02):.4e}')

print('== C. condensate rule (Hartree): dressed-sea condensation energy per site per tick')
a_th = 3 * np.sqrt(3) / (2 * np.pi ** 2)
def Bx(x): s = np.sin(x / 2); return 4 * s * (I0 - D_of(s))
def dBx_over_x(x):                         # d/dx (B/x)
    s = np.sin(x / 2); f = 4 * s / x; df = (2 * np.cos(x / 2) * x - 4 * s) / x ** 2
    return df * (I0 - D_of(s)) + f * dI_ds(s) * np.cos(x / 2) / 2
def dE_cond(mu):                           # per site: (1/16) int_0^mu x^2 d/dx(B/x) dx   [= -(1/8) int B + mu B/16]
    xg, wg = leggauss(40); x = mu * (xg + 1) / 2
    return (mu / 2) * sum(w_ * xx ** 2 * dBx_over_x(xx) for xx, w_ in zip(x, wg)) / 16
mu = 0.3; xg, wg = leggauss(40); x = mu * (xg + 1) / 2
direct = -(mu / 2) * sum(w_ * Bx(xx) for xx, w_ in zip(x, wg)) / 8 + mu * Bx(mu) / 16
check('mean-field vacuum energy E_sea(mu) - E_sea(0) + mu^2/(32 g) at the gap root: integration by parts consistent',
      abs(direct - dE_cond(mu)) < 1e-12, f'{dE_cond(mu):.6e}')
cond = {m: dE_cond(m) for m in (1e-2, 1e-3, 1e-4)}
lead = {m: -(a_th / 16) * m ** 4 * np.log(1 / m) for m in cond}
print('   condensation energy per site:', '; '.join(f'mu={m:g}: {cond[m]:.4e} (lead {lead[m]:.4e})' for m in cond))
check('the mu^2 (m^2 M_P^2-type) term cancels at the gap root; residual = -(a/16) mu^4 ln(1/mu) + O(mu^4), a = 3 sqrt3/(2 pi^2)',
      all(cond[m] < 0 for m in cond) and abs(cond[1e-4] / lead[1e-4] - 1) < 0.15 and
      abs(cond[1e-4] / lead[1e-4] - 1) < abs(cond[1e-2] / lead[1e-2] - 1))

print('== D. units, measured value, noise wander')
hbar, c, Gn = 1.054571817e-34, 2.99792458e8, 6.67430e-11
lP, tP = np.sqrt(hbar * Gn / c ** 3), np.sqrt(hbar * Gn / c ** 5); rhoP = c ** 7 / (hbar * Gn ** 2)
cell4 = 2 * (8 * np.pi) ** 2 / np.sqrt(3)  # a^3 tau in Planck units: a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c)
H0 = 67.4e3 / 3.0857e22; OmL = 0.6847
rhoL = OmL * 3 * H0 ** 2 / (8 * np.pi * Gn) * c ** 2
x_meas = rhoL / rhoP
E4 = (2.3e-3 * 1.602176634e-19) ** 4 / (hbar * c) ** 3
print(f'   measured (Planck 2018): rho_L = {rhoL:.3e} J/m^3 = {x_meas:.3e} rho_P; Lambda l_P^2 = {3 * OmL * (H0 * tP) ** 2:.3e}; '
      f'(2.3 meV)^4 = {E4:.2e} J/m^3')
check('measured rho_Lambda / rho_P = 1.13e-123 (Omega_L 0.6847 +- 0.0073, H0 67.4 +- 0.5): nonzero at > 90 sigma',
      1.0e-123 < x_meas < 1.3e-123 and 0.6847 / 0.0073 > 90)
conv = lambda e_site: e_site / cell4      # radians per tick per site -> rho / rho_P
Mp = 1.220890e19
muof = lambda m_GeV: 2 / np.sqrt(3) * np.sqrt(8 * np.pi) * m_GeV / Mp
cases = [('massless sea, generator reading (-pi/4 /site)', conv(np.pi / 4)),
         ('massless sea, phase-mod-2pi reading', 0.0),
         ('band-relative (relays relative to the sea)', 0.0),
         ('fixed-mass residual, electron', conv(I0 / 8 * muof(0.51099895e-3) ** 2)),
         ('fixed-mass residual, top', conv(I0 / 8 * muof(172.7) ** 2)),
         ('condensate residual, electron', conv(a_th / 16 * muof(0.51099895e-3) ** 4 * np.log(1 / muof(0.51099895e-3)))),
         ('condensate residual, top', conv(a_th / 16 * muof(172.7) ** 4 * np.log(1 / muof(172.7)))),
         ('condensate residual, 50 meV neutrino', conv(a_th / 16 * muof(5e-11) ** 4 * np.log(1 / muof(5e-11))))]
for nm, v in cases:
    print(f'   {nm:48s} |rho|/rho_P = {v:.2e}' + (f'  (x {v / x_meas:.1e} measured)' if v > 0 else '  (= 0, measured excludes 0)'))
check('no rule-level vacuum source lands within 3 orders of measured: Planckian, zero, or >= 1e30 too large for any charged species',
      all(v == 0 or v / x_meas > 1e3 or v / x_meas < 1e-3 for _, v in cases))
# zero-mean record noise, unimodular reading: one record per relay per half-tick, independent zero-mean jumps delta
tau = 2 * np.sqrt(8 * np.pi) / np.sqrt(3) * tP; t0 = 13.8e9 * 3.156e7; VH = 4 / 3 * np.pi * (c / H0) ** 3
nrec = 2 * t0 / tau
eV = 1.602176634e-19
relays = [('relic neutrinos 336/cm^3, delta = 0.05 eV', 3.36e8, 0.05 * eV), ('electrons 0.22/m^3, delta = m_e', 0.22, 0.511e6 * eV),
          ('baryons 0.25/m^3, delta = m_p', 0.25, 938.3e6 * eV), ('same neutrinos, Planck-size jumps pi hbar/tau', 3.36e8, np.pi * hbar / tau)]
wand = []
for nm, n, d in relays:
    drho = d * np.sqrt(n * nrec / VH); wand.append(drho / rhoP)
    print(f'   wander over the Hubble volume after 13.8 Gyr ({nrec:.1e} half-ticks), {nm:44s}: {drho / rhoP:.1e} rho_P')
check('zero-mean record noise: Hubble-volume rms wander with relay-scale jumps is 1e-11 to 1e-19 of the measured value; '
      'only Planck-size jumps per record reach it (and overshoot)', max(wand[:3]) < 1e-10 * x_meas and wand[3] > x_meas,
      f'max relay-scale {max(wand[:3]):.1e}, Planck-jump {wand[3]:.1e}')
Ncell = VH * t0 / (cell4 * lP ** 3 * tP)
print(f'   not in the rules (literature scaling, Sorkin-type): rho_P/sqrt(N_cells) with N_cells = {Ncell:.1e} in the Hubble '
      f'4-volume -> {1 / np.sqrt(Ncell):.1e} rho_P (x {1 / np.sqrt(Ncell) / x_meas:.0f} measured); needs Poisson cell-count noise a regular lattice lacks')
print(f'   same scaling counted in Planck 4-volumes: {1 / np.sqrt(VH * t0 / (lP ** 3 * tP)):.1e} rho_P; the factor is convention, the H^2 scaling is the content')
print('supplied: the CL-2 hop and mass parameter, the sea filling and log branch, the M1 couplings (counter-rotating term is a variant),')
print('  the B^2 rule + Hartree, the unit map a = sqrt(8 pi) l_P and tau = 2a/(sqrt3 c), unimodular reading, jump sizes, densities.')
print('elapsed_seconds', round(time.monotonic() - T0, 1))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
