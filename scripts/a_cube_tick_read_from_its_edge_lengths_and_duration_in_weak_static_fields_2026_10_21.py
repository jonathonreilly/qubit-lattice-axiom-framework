#!/usr/bin/env python3
"""matter-sees-geometry: a rule for how the CL-2 tick reads CL-5 edge lengths, and its weak-field, induced-response
and cosmological tests.  Supplied models; finite diagnostics and exact identities; no physical identification.
Candidate rule (box reading): each cube reads its tick from its own edges.  Its reflection R = sum_i f_i W_i / f_rms with
f_i = 1/L_i (W_i the axis-i part of the spin-3/2 edge hop, L_i the proper length of its axis-i edges), its step eps from
the light cone (sin eps = sqrt3 tau f_rms, tau the proper duration of its tick edges, block units), and the mass phase
of a species mu = m tau.  Half-ticks exp(-i(eps - mu/2)R) (even) and exp(+i(eps + mu/2)R) (odd), as in CL-2.
 A  rule algebra (exact): Clifford hop parts, exact box bands, cone = null cone, proper-time clocks, covariance,
    Weyl blindness, no shift or shear in the family
 B  weak static field on a z-profile line (eps0 = 0.3): free fall, light deflection, a photon climbing a lapse step
 C  induced response: sea stress under the cone reading, Einstein-Hilbert is not conformal, rung arithmetic
 D  uniform edge growth at fixed tick duration, then a 2^3 split; the matter phase per tick is -E tau
 E  estimates with measured numbers
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/A_CUBE_TICK_READ_FROM_ITS_EDGE_LENGTHS_AND_DURATION_IN_WEAK_STATIC_FIELDS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.spatial.transform import Rotation

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-2 hop (spin-3/2 phases) split by axis
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NV = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NV[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
EDGES = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum(abs(C8[a] - C8[b])) == 1]
W = np.zeros((8, 8), complex); WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a, b in EDGES:
    g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b])))
    for M in (W, WAX[ax]): M[a, b] = x; M[b, a] = np.conj(x)
def Rf(f):
    f = np.asarray(f, float); return sum(f[i] * WAX[i] for i in range(3)) / np.sqrt(f @ f / 3)
def halves(f, eps, mu):
    R = Rf(f); te, to = eps - mu / 2, -(eps + mu / 2)
    return np.cos(te) * I8 - 1j * np.sin(te) * R, np.cos(to) * I8 - 1j * np.sin(to) * R
def ublock(K, f, eps, mu):
    Ue, Uo = halves(f, eps, mu); D = np.exp(1j * (np.atleast_2d(K) @ C8.T))
    return (D[:, :, None] * Uo[None] * D.conj()[:, None, :]) @ Ue
def band(K, f, eps, mu):
    f = np.asarray(f, float); A = (np.cos(mu) - np.cos(2 * eps)) / 2; Sf = (np.cos(np.atleast_2d(K)) @ f ** 2) / (f @ f)
    return np.arccos(np.clip(A * Sf + (np.cos(2 * eps) + np.cos(mu)) / 2, -1, 1))
def cm2(eps, mu):                                 # rest energy / inertial mass, blocks^2 per tick^2
    return (np.cos(mu) - np.cos(2 * eps)) / 6 * (mu / np.sin(mu) if mu else 1.0)
def cone_eps(tau_over_L):                         # sin eps = sqrt3 * tau * rms(1/L), block units
    return np.arcsin(r3 * tau_over_L)

# ------------------------------------------------------------------ A. rule algebra
print('== A. rule algebra (exact)')
Wc = [r3 * X for X in WAX]
cl = max(np.abs(Wc[i] @ Wc[j] + Wc[j] @ Wc[i] - 2 * (i == j) * I8).max() for i in range(3) for j in range(3))
rng = np.random.default_rng(20261021); rf = 0.0
for _ in range(5):
    f = rng.uniform(0.2, 2, 3); R = Rf(f); Ue, Uo = halves(f, rng.uniform(0, 1.5), rng.uniform(0, 0.8))
    rf = max(rf, np.abs(R @ R - I8).max(), abs(np.trace(R)), abs(np.linalg.det(Ue) - 1), abs(np.linalg.det(Uo) - 1),
             np.abs(Ue @ Ue.conj().T - I8).max())
check('A1 theorem: sqrt3 x (axis parts of W) are Clifford generators, W = their sum/sqrt3; so R(f) is a traceless '
      'reflection for every edge set and each half-tick is unitary with det 1', max(cl, np.abs(W - sum(WAX)).max(), rf) < 1e-13,
      f'{max(cl, rf):.1e}')
KR = rng.uniform(-np.pi, np.pi, (400, 3)); dv = rp = 0.0
for f, eps, mu in (([1, .8, 1.2], .3, .1), ([1, 1, .5], 1.1, .4), ([.3, 1, 2], .05, .02), ([2, .7, 1.3], 1.5, 0.9)):
    w = np.sort(np.abs(np.angle(np.linalg.eigvals(ublock(KR, f, eps, mu)))), 1); dv = max(dv, np.abs(w - band(KR, f, eps, mu)[:, None]).max())
    rp = max(rp, np.abs(np.abs(np.angle(np.linalg.eigvals(ublock(np.zeros(3), f, eps, mu)[0]))) - mu).max())
check('A2 theorem: all 8 bands of the box tick obey cos w = A S_f(K) + (cos2eps + cos mu)/2, S_f = sum f_i^2 cos K_i/sum f^2; '
      'at K = 0 every phase is +-mu for any edges, so a clock at rest runs at m x proper time', dv < 1e-12 and rp < 1e-12,
      f'bands {dv:.1e}, rest {rp:.1e}')
k = 1e-3; worst = 0.0
for _ in range(6):
    L = rng.uniform(0.6, 1.6, 3); tau = 0.08; eps = cone_eps(tau * np.sqrt(np.mean(1 / L ** 2)))
    for _ in range(5):
        n = rng.normal(size=3); n /= np.linalg.norm(n); vnull = tau * np.sqrt(np.sum((n / L) ** 2))
        worst = max(worst, abs(np.abs(np.angle(np.linalg.eigvals(ublock(k * n, 1 / L, eps, 0.0)[0]))).min() / k / vnull - 1))
check('A3 cone reading: with sin eps = sqrt3 tau rms(1/L_i) the massless cone is the null ellipsoid v_i = tau/L_i of the '
      'edges in every direction (the reading is forced: v_i is exactly (f_i/f_rms) sin(eps)/sqrt3)', worst < 1e-6, f'max rel dev {worst:.1e} at |K| = 1e-3')
cov = 0.0; nrot = 0
for g in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        G = np.zeros((3, 3)); G[range(3), g] = s
        if np.linalg.det(G) < 0: continue
        nrot += 1; rv = Rotation.from_matrix(G).as_rotvec(); D = expm(-1j * sum(rv[i] * J3[i] for i in range(3)))
        sig = [int(np.argmin(np.abs(NV - G @ NV[a]).sum(1))) for a in range(8)]; V = np.zeros((8, 8), complex)
        for a in range(8): V[sig[a], a] = XI[sig[a]].conj() @ D @ XI[a]
        cov = max(cov, np.abs(V @ W @ V.conj().T - W).max(), np.abs(V.conj().T @ V - I8).max())
        f = rng.uniform(0.3, 2, 3); fg = np.abs(G) @ f
        cov = max(cov, np.abs(V @ Rf(f) @ V.conj().T - Rf(fg)).max())
check('A4 covariance: each of the 24 proper cube rotations is a unitary on the 8 corners that fixes W and maps R(f) to '
      'R(rotated f): the reading rotates with the edges', nrot == 24 and cov < 1e-12, f'{nrot} rotations, {cov:.1e}')
Kp = rng.uniform(-np.pi, np.pi, (50, 3)); asym = np.abs(band(Kp, [1, .7, 1.4], .4, .1) - band(-Kp, [1, .7, 1.4], .4, .1)).max()
check('A5 theorem (limit of the box reading): w(K) = w(-K) and the cone has no K_i K_j cross terms, so a cube read from '
      'its axis lengths and duration cannot carry a shift (tilted tick edges) or a shear between axes', asym < 1e-14)

# ------------------------------------------------------------------ z-profile line (Bloch in x, y)
class Line:
    def __init__(self, Nz, kp, fe, fo, eps0, mu0, rule='cone'):
        self.Nz = Nz; self.Ue = self.cubes(fe, eps0, mu0, False, rule); self.Uo = self.cubes(fo, eps0, mu0, True, rule)
        self.blk = (np.arange(Nz)[:, None] + 1 - C8[:, 2][None, :]) % Nz
        self.ph = np.exp(1j * ((1 - C8[:, 0]) * kp[0] + (1 - C8[:, 1]) * kp[1])); self.tcol = np.arange(8)[None, :]
        self.z = np.arange(Nz)[:, None] + C8[:, 2][None, :] / 2.0
    @staticmethod
    def cubes(fl, eps0, mu0, odd, rule):
        N, L = fl; out = np.empty((len(N), 8, 8), complex)
        for n in range(len(N)):
            F = N[n] / L[n]; eps = np.arcsin(np.sin(eps0) * F) if rule == 'cone' else eps0 * F; mu = mu0 * N[n]
            out[n] = halves([1, 1, 1], eps, mu)[1 if odd else 0]
        return out
    def tick(self, a):
        a = np.einsum('nij,nj->ni', self.Ue, a); v = np.einsum('nij,nj->ni', self.Uo, a[self.blk, self.tcol] * self.ph)
        b = np.empty_like(a); b[self.blk, self.tcol] = v / self.ph; return b
    def zm(self, a):
        p = np.abs(a) ** 2; return (p * self.z).sum() / p.sum()
def packet(Nz, kp, z0, sig, kz0, eps, mu, chi, branch=1):
    a = np.zeros((Nz, 8), complex); m = np.arange(Nz)
    for j in range(Nz):
        Kz = (2 * np.pi * j / Nz + np.pi) % (2 * np.pi) - np.pi; g = np.exp(-((Kz - kz0) * sig) ** 2 / 2)
        if g < 1e-14: continue
        U = ublock(np.array([kp[0], kp[1], Kz]), [1, 1, 1], eps, mu)[0]; cw = np.real(np.trace(U)) / 8
        P = (I8 - branch * (U - U.conj().T) / (2j * np.sqrt(1 - cw * cw))) / 2; c = P @ chi
        a += g * np.exp(1j * Kz * (m - z0))[:, None] * (c / np.linalg.norm(c))[None, :]
    return a / np.linalg.norm(a)
chi0 = rng.normal(size=8) + 1j * rng.normal(size=8)
Nz = 256; zz = (np.arange(Nz) + 0.25, np.arange(Nz) + 0.75)
Om = lambda z: 1 + 0.3 * np.sin(2 * np.pi * z / Nz) ** 2
base = lambda z: (1 + 0.02 * np.cos(2 * np.pi * z / Nz), 1 - 0.02 * np.cos(2 * np.pi * z / Nz))
wb = {}
for mu in (0.0, 0.1):
    for lab, sc in (('g', lambda z: 1.0), ('Omega g', Om)):
        fe = tuple(sc(zz[0]) * q for q in base(zz[0])); fo = tuple(sc(zz[1]) * q for q in base(zz[1]))
        ln = Line(Nz, (0.3, 0.1), fe, fo, 0.3, mu); a = packet(Nz, (0.3, 0.1), 128, 12.0, 0.2, 0.3, mu, chi0)
        for _ in range(300): a = ln.tick(a)
        wb[(mu, lab)] = a
d0 = np.abs(wb[(0.0, 'g')] - wb[(0.0, 'Omega g')]).max(); d1 = np.abs(wb[(0.1, 'g')] - wb[(0.1, 'Omega g')]).max()
check('A6 Weyl blindness: a massless species evolves identically under (N, L) and Omega(z)(N, L), a massive one does not; '
      'null geodesics are conformally invariant, so this is the right invariance for light', d0 < 1e-12 and d1 > 1e-3,
      f'massless {d0:.1e}, massive {d1:.1e} after 300 ticks')

# ------------------------------------------------------------------ B. weak static field
print('== B. weak static field: N = 1 + Phi, L = 1 - gamma Phi, Phi = g z (eps0 = 0.3, g = 2e-5, cone reading)')
Nz, eps0, X0, gs = 2048, 0.3, 900, 2e-5; zc = Nz / 2; c02 = np.sin(eps0) ** 2 / 3; zz = (np.arange(Nz) + 0.25, np.arange(Nz) + 0.75)
def saw(x):
    x = (x + Nz / 2) % Nz - Nz / 2
    return np.where(np.abs(x) <= X0, x, np.sign(x) * X0 - (x - np.sign(x) * X0) * 2 * X0 / (Nz - 2 * X0))
def fld(gam, z):
    Ph = gs * saw(z - zc); return 1 + Ph, 1 - gam * Ph
def accel(mu, kp, gam, sig, T, rule='cone'):
    ln = Line(Nz, kp, fld(gam, zz[0]), fld(gam, zz[1]), eps0, mu, rule); a = packet(Nz, kp, zc, sig, 0.0, eps0, mu, chi0)
    zs = [ln.zm(a)]
    for _ in range(T): a = ln.tick(a); zs.append(ln.zm(a))
    return -2 * np.polyfit(np.arange(T + 1), np.array(zs) - zs[0], 2)[0] / gs
ff = {}
for mu in (0.03, 0.12):
    for gam in (0.0, 1.0):
        r = [accel(mu, (0, 0), gam, s, 200) / cm2(eps0, mu) for s in (80.0, 160.0)]; ff[(mu, gam)] = (4 * r[1] - r[0]) / 3
dff = max(abs(v - 1) for v in ff.values())
check('B1 free fall: a slow packet falls at a = -c_m^2 dPhi/dz for gamma = 0 and 1 (1/sigma^2-extrapolated packets; c_m^2 = '
      'rest energy/inertial mass of the band): the lapse alone drives the fall', dff < 5e-4, f'max |a/(c_m^2 g) - 1| = {dff:.1e}')
eta = 1 - cm2(eps0, 0.12) / cm2(eps0, 0.03); eta_m = 1 - ff[(0.12, 0.0)] * cm2(eps0, 0.12) / (ff[(0.03, 0.0)] * cm2(eps0, 0.03))
eta_f = (0.12 ** 2 - 0.03 ** 2) * (1 / (4 * np.sin(eps0) ** 2) - 1 / 6)
check('B2 universality: species differ only through c_m^2(eps, mu)/c_0^2 = 1 + mu^2 (1/6 - 1/(4 sin^2 eps)) + O(mu^4), '
      'a lattice term in (mu/eps)^2', abs(eta_m - eta) < 1e-3 and abs(eta_f / eta - 1) < 0.01,
      f'eta(mu .03 vs .12, eps .3): packets {eta_m:.4f}, band {eta:.4f}, leading formula {eta_f:.4f}')
kx = 0.4; wl = band(np.array([kx, 0, 0]), [1, 1, 1], eps0, 0.0)[0]; lb = {}
for rule in ('cone', 'angle'):
    for gam in (0.0, 1.0):
        lb[(rule, gam)] = accel(0.0, (kx, 0), gam, 160.0, 800, rule) / c02 * np.cos(wl / 2) ** 2
devc = max(abs(lb[('cone', g)] / (1 + g) - 1) for g in (0.0, 1.0)); fang = lb[('angle', 1.0)] / lb[('cone', 1.0)]
check('B3 light: a massless packet moving along x is pulled across by (1 + gamma) c^2 dPhi/dz (cone reading): twice the '
      'Newtonian pull for gamma = 1. The hop-angle reading multiplies it by eps cot eps', devc < 5e-4 and abs(fang - eps0 / np.tan(eps0)) < 5e-4,
      f'cone: {lb[("cone", 0.0)]:.5f}, {lb[("cone", 1.0)]:.5f} (gamma 0, 1); angle/cone {fang:.5f} vs eps cot eps {eps0/np.tan(eps0):.5f}')
Nz = 1024; zz = (np.arange(Nz) + 0.25, np.arange(Nz) + 0.75); dP = 0.05
stp = lambda z: 0.5 * (np.tanh((z - 512) / 15) - np.tanh((z - 960) / 15))
fl2 = lambda z: (1 + dP * stp(z), 1 - dP * stp(z))
ln = Line(Nz, (0, 0), fl2(zz[0]), fl2(zz[1]), eps0, 0.0); a = packet(Nz, (0, 0), 300, 25.0, 0.4, eps0, 0.0, chi0); zs = []
for t in range(2600):
    a = ln.tick(a)
    if t >= 2200: zs.append(ln.zm(a))
b = a.copy(); b[(np.arange(Nz) < 560) | (np.arange(Nz) > 940)] = 0; tr = (np.abs(b) ** 2).sum()
Fq = np.fft.fft(b, axis=0); pw = (np.abs(Fq) ** 2).sum(1); km = (pw * 2 * np.pi * np.fft.fftfreq(Nz)).sum() / pw.sum()
e2 = np.arcsin(np.sin(eps0) * (1 + dP) / (1 - dP)); w1 = band(np.array([0, 0, 0.4]), [1, 1, 1], eps0, 0)[0]
k2 = np.arccos(3 * (1 - (1 - np.cos(w1)) / np.sin(e2) ** 2) - 2); v2 = np.polyfit(np.arange(len(zs)), zs, 1)[0]
cw = np.cos(band(np.array([0, 0, k2]), [1, 1, 1], e2, 0)[0]); v2p = np.sin(e2) ** 2 * np.sin(k2) / 3 / np.sqrt(1 - cw ** 2)
check('B4 a photon climbing a lapse step keeps its quasi-energy (static tick), so its frequency over the local clock rate '
      '(m N, A2) falls by N_low/N_high: the redshift is exact for clocks at rest; its wavenumber and exit speed follow the band',
      tr > 0.99999 and abs(km - k2) < 1e-4 and abs(v2 / v2p - 1) < 1e-3, f'transmitted {tr:.6f}; k2 {km:.5f} vs {k2:.5f}; speed {v2:.5f} vs {v2p:.5f}')

# ------------------------------------------------------------------ C. induced response of the sea
print('== C. sea response under the reading')
ng = 48; gg = 2 * np.pi * (np.arange(ng) + 0.5) / ng - np.pi; S = np.cos(np.array(np.meshgrid(gg, gg, gg, indexing='ij')).reshape(3, -1).T).sum(1) / 3
Phi = lambda e: -4 * np.mean(np.arccos(np.clip(1 - np.sin(e) ** 2 * (1 - S), -1, 1)))
h = 1e-6; dc, da = {}, {}
for e0 in (0.04, 0.8, np.pi / 2 - 1e-4):
    dc[e0] = (Phi(np.arcsin(np.sin(e0) * (1 - h))) - Phi(np.arcsin(np.sin(e0) * (1 - 2 * h)))) / h / (np.sin(e0) / r3)
    da[e0] = (Phi(e0 * (1 + h)) - Phi(e0 * (1 - h))) / (2 * h) / (np.sin(e0) / r3)
check('C1 the massless sea responds to the cone ratio F = tau/L at every step: dPhi/dF = -9.55 c0 (eps -> 0) to -16.0 c0 '
      '(eps -> pi/2) per block per tick, traceless by Weyl blindness; the zero at pi/2 exists only for the hop-angle reading',
      all(v < -9 for v in dc.values()) and abs(da[np.pi / 2 - 1e-4]) < 1e-3 * abs(dc[np.pi / 2 - 1e-4]),
      ', '.join(f'eps {e:.2f}: cone {dc[e]:+.2f}, angle {da[e]:+.4f}' for e in dc))
x, a_ = sp.symbols('x a'); sg = sp.Function('s')(x); gm = sp.diag(-sp.exp(2 * sg), sp.exp(2 * sg), sp.exp(2 * sg), sp.exp(2 * sg))
X = [sp.Symbol('t'), x, sp.Symbol('y'), sp.Symbol('z')]; gi = gm.inv()
Gam = [[[sum(gi[i, l] * (sp.diff(gm[l, j], X[kk]) + sp.diff(gm[l, kk], X[j]) - sp.diff(gm[j, kk], X[l])) for l in range(4)) / 2
         for kk in range(4)] for j in range(4)] for i in range(4)]
Ric = lambda j, kk: sum(sp.diff(Gam[i][j][kk], X[i]) - sp.diff(Gam[i][j][i], X[kk]) + sum(Gam[i][i][l] * Gam[l][j][kk] - Gam[i][kk][l] * Gam[l][j][i] for l in range(4)) for i in range(4))
Rs = sp.simplify(sum(gi[j, j] * Ric(j, j) for j in range(4)))
dens = sp.simplify(sp.exp(4 * sg) * Rs + 6 * sp.exp(2 * sg) * (sp.diff(sg, x, 2) + sp.diff(sg, x) ** 2))
check('C2 theorem: for g = e^{2s} eta, sqrt(-g) R = -6 e^{2s}(s\'\' + s\'^2) = total derivative + 6 e^{2s} s\'^2, so the '
      'Einstein-Hilbert action depends on the conformal factor; a sea that sees only tau/L cannot induce it, and any q^2 '
      'term it does induce breaks the covariance relating tensor and Newtonian couplings', dens == 0, f'residual {dens}')
R2, Rg, ND = 0.00483, 0.5, 24
rows = [ND * R2 * 4 ** n / Rg for n in range(3)]
check('C3 rung arithmetic (induced-response R2_TT = 0.00483 c0 per Dirac copy, Regge 0.5 c0 at the site rung): G ~ a_rung^2 '
      'and the sea lives on sites, so the sea/Regge ratio grows as 4^n; no CL-5 rung lets the bare term dominate',
      all(r > 0.2 for r in rows), 'rung 0,1,2: ' + ', '.join(f'{r:.2f}' for r in rows) + ' vs Hulse-Taylor 0.002')

# ------------------------------------------------------------------ D. cosmological redshift
print('== D. uniform edge growth at fixed tick duration, then a 2^3 or 2^4 split (eps0 = 0.3)')
def U1(K, eps, mu=0.0): return ublock(np.asarray(K, float), [1, 1, 1], eps, mu)[0]
def Pw(U):
    cw = np.real(np.trace(U)) / 8; return (I8 - (U - U.conj().T) / (2j * np.sqrt(1 - cw ** 2))) / 2, np.arccos(cw)
def grow(Kc, Tg=4000):
    P, w0 = Pw(U1(Kc, eps0)); psi = P @ chi0; psi /= np.linalg.norm(psi)
    for n in range(Tg): psi = U1(Kc, np.arcsin(np.sin(eps0) / (1 + (n + 0.5) / Tg))) @ psi
    Pf, wpre = Pw(U1(Kc, np.arcsin(np.sin(eps0) / 2))); return np.linalg.norm(Pf @ psi) ** 2, wpre / w0
def split(Kc, e_c, e_f):
    P, wc = Pw(U1(Kc, e_c)); psi = P @ chi0; psi /= np.linalg.norm(psi); flip = ws = 0.0
    for m in C8:
        Kf = Kc / 2 + np.pi * m; am = np.prod((1 + np.exp(-1j * Kf)) / 2) * psi; Pp, wf = Pw(U1(Kf, e_f))
        pp = np.linalg.norm(Pp @ am) ** 2; pm = np.linalg.norm(am) ** 2 - pp; flip += pm; ws += (pp - pm) * wf
    return flip, ws / wc
Ka, Kb = np.array([0.3, 0.2, 0.1]), np.array([0.05, 0.02, 0.0]); ga, gb = grow(Ka), grow(Kb)
rest = [np.abs(np.angle(np.linalg.eigvals(U1(np.zeros(3), e, 0.1)))).min() for e in (eps0, np.arcsin(np.sin(eps0) / 2))]
check('D1 edges growing at fixed tau: K is conserved, the photon keeps its band and its quasi-energy falls as 1/L while '
      'the rest phase m tau stays: photons redshift against atoms by L_obs/L_emit (by Weyl blindness, for any lapse schedule)', min(ga[0], gb[0]) > 1 - 1e-4 and abs(gb[1] - 0.5) < 1e-5
      and abs(ga[1] - 0.5) < 2e-3 and abs(rest[0] - rest[1]) < 1e-13,
      f'kept {ga[0]:.7f}, {gb[0]:.7f}; ratio {ga[1]:.5f} (|K| .37), {gb[1]:.7f} (|K| .05); rest {rest[0]:.4f} -> {rest[1]:.4f}')
sp3 = {e: split(Kb, np.arcsin(np.sin(e) / 2), e) for e in (0.3, 0.1)}; sp4 = {e: split(Kb, np.arcsin(np.sin(e) / 2), np.arcsin(np.sin(e) / 2)) for e in (0.3, 0.1)}
xs = {e: (sp3[e][0] - sp4[e][0]) / e ** 2 for e in sp3}; f4k = [split(K, 0.15, 0.15)[0] / (K @ K) for K in (Kb, 2 * Kb)]
_, wb0 = Pw(U1(Ka, eps0)); _, wb1 = Pw(U1(Ka / 2, eps0))
check('D2 a 2^3 split at fixed tau resets eps: frequency stays continuous but ~0.06 eps^2 of every light mode, at all K, '
      'flips band; a 2^4 split (ticks halved too) keeps eps, flips only O(K^2), and photon and atom phases per tick halve '
      'together. A fixed-step reading halves the photon alone',
      all(abs(sp3[e][1] - (1 - 2 * sp3[e][0])) < 5e-4 for e in sp3) and all(0.04 < x < 0.08 for x in xs.values())
      and all(abs(sp4[e][1] - 0.5) < 1e-5 for e in sp4) and abs(f4k[1] / f4k[0] - 1) < 0.1 and abs(wb1 / wb0 - 0.5) < 2e-3,
      f'2^3: ratio {sp3[0.3][1]:.5f}, extra flip/eps^2 {xs[0.3]:.3f}, {xs[0.1]:.3f} (eps .3, .1); 2^4: ratio {sp4[0.3][1]:.6f}, '
      f'flip/K^2 {f4k[0]:.3f}, {f4k[1]:.3f}; fixed step {wb1/wb0:.4f}')
dd = 0.0
for K, m in ((np.array([0.05, 0, 0]), 0.0), (np.array([0.03, 0.02, 0]), 0.5), (np.zeros(3), 0.5)):
    Lb, tau = 1.0, 0.05
    wfun = lambda t: band(K, [1, 1, 1], cone_eps(t / Lb), m * t)[0]
    E = np.sqrt(m ** 2 + K @ K / Lb ** 2); dd = max(dd, abs((wfun(tau + 1e-7) - wfun(tau - 1e-7)) / 2e-7 / E - 1))
check('D3 the matter phase per tick is -E tau to O(eps^2): dw/dtau = proper energy, which is the deposit E(1/2)d(l^2) '
      'and the radiation energy E ~ 1/L that CL-5 work supplied', dd < 3 * np.arcsin(r3 * 0.05) ** 2, f'max rel dev {dd:.1e} (eps = {cone_eps(0.05):.3f})')

# ------------------------------------------------------------------ E. estimates
print('== E. ESTIMATES with measured numbers (not theorems)')
c, gE = 2.99792458e8, 9.80665; pr = gE * 22.5 / c ** 2; MP = 1.220890e19; blk = 2 * np.sqrt(8 * np.pi)
print(f'   Pound-Rebka: N_low/N_high - 1 = gh/c^2 = {pr:.3e} (exact at rest, A2/B4); measured/predicted 0.9990(76); GP-A 1.4e-4')
print(f'   deflection at the limb (1+gamma)/2 x 1.751 arcsec; cone reading adds nothing; hop-angle reading gives gamma_light - 1 '
      f'= -2eps^2/3, so Cassini (2.1 +- 2.3)e-5 needs eps < {np.sqrt(1.5 * 2.5e-5):.4f}')
for nm, m in (('electron', 0.000511), ('top', 172.69), ('1 GeV binding', 1.0)):
    mu_s = m / MP * blk / r3                       # mass phase per tick / sin(eps)
    print(f'   lattice eta ~ mu^2/(4 sin^2 eps) for {nm}: {mu_s ** 2 / 4:.1e} (independent of eps); MICROSCOPE |eta| < ~3e-15')
print('   missing shift: g_0i = -4 U w in the lattice frame is unseen, i.e. alpha1 = -8, alpha2 = -1 vs LLR 1e-4, pulsars 1.6e-9')
check('E1 arithmetic: Pound-Rebka 2.46e-15; lattice eta for the top quark below 1e-30', abs(pr - 2.455e-15) < 1e-17 and (172.69 / MP * blk / r3) ** 2 / 4 < 1e-30)
print('supplied: CL-2 hop and its phases, the box reading (axis lengths + duration), eps0, masses, packets, fields, split map,')
print('  the sea branch, induced-response R2_TT, a = sqrt(8 pi) l_P, all measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
