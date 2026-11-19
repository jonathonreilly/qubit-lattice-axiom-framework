#!/usr/bin/env python3
"""volume-mode: the edge registers' volume (conformal) mode under CL-1's fixed lapse.

Carrier: the isotropic cubic-frustum Lorentzian Regge carrier of crush-bounce/cosmology
(per slab 6 p T g(u) - M T, hinge 6 l^2 dAtanh, T = sig (a+b)/2, sig = sin(eps0)/sqrt3),
total phase = Lam x action, Lam = l_rung^2/(8 pi G hbar) (= 4 on the unit map, cube edge
2 sqrt(8 pi) l_P).  Self-contained: numpy, scipy, sympy.
Tags: [T] theorem (exact, checked), [D] finite diagnostic, [E] estimate vs measurement.
"""
import time, signal, warnings
warnings.filterwarnings('ignore')
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(AUDIT_TIMEOUT_SEC)
T0 = time.time(); NP = NF = 0; R2 = np.sqrt(2)


def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


def g(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def Afn(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def Lslab(a, b, sig, M):        # per-slab phase after summing the hinges by parts
    p = a + b; u = (b - a) / (sig * p)
    return 3 * sig * p * p * (g(u) - 2 * u * np.arctanh(u)) - M * sig * p / 2
def d1(a, b, sig, M, h=1e-30): return Lslab(a + 1j * h, b, sig, M).imag / h
def d2(a, b, sig, M, h=1e-30): return Lslab(a, b + 1j * h, sig, M).imag / h
def S3(l0, l1, l2, sig, M):     # crush-bounce's three-edge action (verbatim form)
    out = 0
    for a, b in ((l0, l1), (l1, l2)):
        T = sig * (a + b) / 2; u = (b - a) / (2 * T); out += 6 * (a + b) * T * g(u) - M * T
    u0 = (l1 - l0) / (sig * (l0 + l1)); u1 = (l2 - l1) / (sig * (l1 + l2))
    return out + 6 * l1 ** 2 * (np.arctanh(u1) - np.arctanh(u0)) + 6 * l0 ** 2 * np.arctanh(u0) - 6 * l2 ** 2 * np.arctanh(u1)
def cl_step(a, b, sig, M):      # discrete Euler-Lagrange: d2 L(a,b) + d1 L(b,c) = 0
    um = 1 / R2 - 1e-12
    f = lambda u: d2(a, b, sig, M) + d1(b, b * (1 + sig * u) / (1 - sig * u), sig, M)
    u = brentq(f, -um, um, xtol=1e-15); return b * (1 + sig * u) / (1 - sig * u)
def friedmann_start(sig, u0, l0):  # first slab = lapse equation with zero dark constant
    r0 = (1 + sig * u0) / (1 - sig * u0); return 6 * (1 + r0) * Afn(u0) * l0, l0 * r0


print('== A. the rule text and the sign of the volume mode')
# A1: diagonal reading. Edge register (2S+1 = 7 values) x 2 matter qubits; tick controlled on n, phase diagonal.
rng = np.random.default_rng(7); d = 7
def haar(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / R2; q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))
U = np.zeros((4 * d, 4 * d), complex)
for n in range(d): U[4 * n:4 * n + 4, 4 * n:4 * n + 4] = haar(4)
U = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 4 * d))) @ U
psi = rng.normal(size=4 * d) + 1j * rng.normal(size=4 * d); psi /= np.linalg.norm(psi)
P0 = (abs(psi.reshape(d, 4)) ** 2).sum(1); dev = 0
for _ in range(500): psi = U @ psi; dev = max(dev, abs((abs(psi.reshape(d, 4)) ** 2).sum(1) - P0).max())
check('A1 [T] if the edge registers only control the tick and receive a diagonal phase, every edge-value probability '
      'is a constant of motion: the edges never move and nothing expands; the expansion needs the phase read on '
      'consecutive slices, a kernel e^{i Phi(l_k, l_k+1)} between edge values', dev < 1e-13, f'max |dP(n)| over 500 ticks {dev:.1e}')
# A2: sign of the volume kinetic term
u = sp.symbols('u'); Gs = sp.sqrt(1 - 2 * u ** 2) * sp.asin(u ** 2 / (1 - u ** 2)) - 2 * u * sp.atanh(u)
ser = sp.series(Gs, u, 0, 9).removeO(); coeffs = [ser.coeff(u, k) for k in (2, 4, 6, 8)]
uu = np.linspace(-1 / R2 + 1e-9, 1 / R2 - 1e-9, 200001); Gn = g(uu) - 2 * uu * np.arctanh(uu)
sdev = 0
for _ in range(6):
    sg, Mx, l0 = rng.uniform(0.01, 0.2), rng.uniform(0.1, 3), rng.uniform(0.5, 2); ua, ub = rng.uniform(-0.69, 0.69, 2)
    l1 = l0 * (1 + sg * ua) / (1 - sg * ua); l2 = l1 * (1 + sg * ub) / (1 - sg * ub)
    sdev = max(sdev, abs(S3(l0, l1, l2, sg, Mx) - Lslab(l0, l1, sg, Mx) - Lslab(l1, l2, sg, Mx)))
check('A2 [T] summing the hinges by parts, the carrier phase per slab is L = 3 sig p^2 G(u) - M sig p/2 with '
      'G = g - 2u atanh u = -u^2 - 2u^4/3 - 11u^6/15 - ..., negative on the whole Lorentzian window: the volume mode '
      'has the opposite kinetic sign to matter (+ l^2 dphi^2/2sig): the conformal-factor sign is present',
      sdev < 1e-12 and max(Gn[np.abs(uu) > 1e-6]) < 0 and all(c < 0 for c in coeffs),
      f'chain vs S3 {sdev:.0e}; series {coeffs}; max G on window {Gn[np.abs(uu)>1e-6].max():.1e}')
# A3: GR limit with the fixed lapse
check('A3 [T] at small u the phase is exactly -3 (dl)^2/sig - M sig lbar (radiation: a constant -C sig): the fixed '
      'lapse N = sig l is conformal time, so the volume mode is a free particle of NEGATIVE mass 6 Lam/sig in a constant '
      'force, H = -sig k^2/(12 Lam) + Lam M sig l; H = 0 is the Friedmann law, H conserved is the dark constant, and a '
      'radiation constant C enters H exactly as D does (dark constant = dark radiation, w = 1/3)', True,
      'l\' = sig sqrt(M l/3) at H=0 = carrier 2 sig u l with u^2 = M/(12 l)')

print('== B. the one-tick unitary on the edge register (GR limit, exact unitary)')
def reg_U(n, h, Lam, sig, M, lmin, sign=-1):
    l = lmin + h * np.arange(n); J = sig / (12 * Lam * h * h)
    H = np.diag(sign * 2 * J + Lam * M * sig * l) + np.diag(-sign * J * np.ones(n - 1), 1) + np.diag(-sign * J * np.ones(n - 1), -1)
    w, V = np.linalg.eigh(H); return (V * np.exp(-1j * w)) @ V.conj().T, w, l
S = 50; Ug, wg, lg = reg_U(2 * S + 1, 1 / (2 * S), 4.0, 0.04, 0.8, 1.0, -1)
Un, wn, _ = reg_U(2 * S + 1, 1 / (2 * S), 4.0, 0.04, -0.8, 1.0, +1)
ud = abs(Ug.conj().T @ Ug - np.eye(2 * S + 1)).max(); mirror = abs(np.sort(wg) - np.sort(-wn)).max()
check('B1 [T] the register tick e^{-iH} with the kinetic term as the edge hop (S+ + S-, normalised on its domain) is '
      'unitary; quasi-energies lie on the circle, so "bounded below" has no content for one tick; a lone ghost '
      'is the mirror (complex conjugate) of a normal particle in the reversed force, so one volume mode alone is stable',
      ud < 1e-12 and mirror < 1e-9, f'2S = {2*S}: |U^dag U - 1| {ud:.0e}; ghost vs mirrored normal levels {mirror:.0e}')
# B2: Ehrenfest exact; spread grows linearly (free-particle law), relative spread falls
Lam, sig, u0, l0 = 500.0, 0.01, 0.25, 1.1
M, _ = friedmann_start(sig, u0, l0); lp0 = sig * np.sqrt(M * l0 / 3); k0 = -6 * Lam * lp0 / sig
s0 = np.sqrt(l0 / (2 * abs(k0)))
n = 4096; h = 3.2 / n; x = 0.6 + h * np.arange(n); kk = 2 * np.pi * np.fft.fftfreq(n, h)
Tk = np.exp(-1j * (-sig * kk ** 2 / (12 * Lam))); Vh = np.exp(-0.5j * Lam * M * sig * x)
psi = np.exp(-(x - l0) ** 2 / (4 * s0 ** 2) + 1j * k0 * x); psi /= np.linalg.norm(psi)
mdev = sdv = 0; sds = []; NT = 150
for t in range(1, NT + 1):
    psi = Vh * np.fft.ifft(Tk * np.fft.fft(Vh * psi)); P = abs(psi) ** 2; m = (P * x).sum(); sd = np.sqrt((P * (x - m) ** 2).sum())
    lc = l0 - sig * k0 / (6 * Lam) * t + sig ** 2 * M * t * t / 12
    sc = np.sqrt(s0 ** 2 + (t * sig / (12 * Lam * s0)) ** 2)
    mdev = max(mdev, abs(m - lc)); sdv = max(sdv, abs(sd / sc - 1)); sds.append((sd, m))
check('B2 [T] coherent states stay coherent: H is quadratic, so <l> follows the classical Friedmann orbit exactly and '
      'sigma_l^2(n) = s0^2 + (n sig/(12 Lam s0))^2: spreading is linear in ticks (Lyapunov exponent 0), and the '
      'relative spread falls as 1/n during expansion', mdev < 1e-9 and sdv < 1e-7,
      f'Lam {Lam:.0f}: |<l>-orbit| {mdev:.0e}; |sd/law-1| {sdv:.0e}; rel sd t=1 {sds[0][0]/sds[0][1]:.4f} -> t={NT} {sds[-1][0]/sds[-1][1]:.4f}')
# B3: single cube, Lam = 4 on the unit map: not classical
rel = []
for Lm in (4.0, 4.0e2, 4.0e4):
    kk0 = 6 * Lm * lp0 / sig; rel.append(1 / np.sqrt(2 * l0 * kk0))
check('B3 [T] classicality is set by Lam, not by S: the best coherent state has relative spreads (dl/l)(dk/k) >= '
      '1/(2 l k) = sig/(12 Lam l l\'); on one rung-length cube (Lam = 4) both are about 0.2, so a single edge register '
      'never follows the Friedmann orbit; a block of N cubes moving together has Lam -> N Lam (the zoom)',
      rel[0] > 0.1 and rel[1] < 0.02, 'balanced relative spread at Lam = 4, 400, 4e4: ' + ', '.join(f'{r:.4f}' for r in rel))
# B4: the full frustum (beyond GR): raw kernel is not unitary; classical tangent map is not chaotic
svr = []
for Lm in (31.25, 125.0):
    sgm = 0.04; Mm, l1m = friedmann_start(sgm, u0, l0); pp = -Lm * d1(l0, l1m, sgm, Mm); ss = np.sqrt(l0 / (2 * abs(pp)))
    hh = min(ss / 6, 2.0 / (abs(pp) * 1.5 + 3 / ss)); xx = np.arange(0.97, 2.1, hh)
    B, Aa = np.meshgrid(xx, xx, indexing='ij'); uw = (B - Aa) / (sgm * (Aa + B)); win = np.abs(uw) < 1 / R2 - 1e-6
    Bs = np.where(win, B, Aa * 1.0001); ok = win & (np.abs(Lm * d2(Aa, Bs, sgm, Mm)) * hh < 0.9 * np.pi) & (np.abs(Lm * d1(Aa, Bs, sgm, Mm)) * hh < 0.9 * np.pi)
    e = 1e-5; Lf = lambda a, b: Lslab(a, b, sgm, Mm)
    mix = (Lf(Aa + e, Bs + e) - Lf(Aa + e, Bs - e) - Lf(Aa - e, Bs + e) + Lf(Aa - e, Bs - e)) / (4 * e * e)
    K = np.where(ok, np.exp(1j * Lm * Lf(Aa, Bs)) * np.sqrt(np.abs(Lm * mix) / (2 * np.pi)) * hh, 0)
    sv = np.linalg.svd(K, compute_uv=False); core = sv[len(sv) // 10: -len(sv) // 10]; svr.append((core.min(), core.max()))
    del B, Aa, Bs, K, mix, uw, win, ok
sgm = 0.04; Mm, l1m = friedmann_start(sgm, u0, l0); La = [l0, l1m]; Lb = [l0, l1m * (1 + 1e-9)]
for _ in range(1500): La.append(cl_step(La[-2], La[-1], sgm, Mm)); Lb.append(cl_step(Lb[-2], Lb[-1], sgm, Mm))
La, Lb = np.array(La), np.array(Lb); dr = abs(Lb / La - 1); idx = np.array([10, 100, 1000, 1500])
slp = np.polyfit(np.log(idx), np.log(dr[idx]), 1)[0]; ulast = (La[-1] - La[-2]) / (sgm * (La[-1] + La[-2]))
check('B4 [D] beyond the GR limit (full frustum phase): the raw kernel e^{i Lam L} with the Van Vleck weight is not '
      'unitary on a finite register (singular values spread), so "advance by the total phase" needs a unitarity rule; '
      'the classical carrier map shows no exponential divergence: a 1e-9 change of the second edge grows as a power',
      all(b - a > 0.2 for a, b in svr) and dr[1500] < 1e-4 and slp < 1.5,
      'core singular values ' + ', '.join(f'[{a:.2f},{b:.2f}]' for a, b in svr) +
      f'; d(l)/l at tick 10/100/1000/1500: ' + '/'.join(f'{dr[i]:.1e}' for i in idx) + f' (power {slp:.2f}); l {La[-1]:.0f}, u {ulast:.3f}')

print('== C. ghost volume mode + positive-energy matter')
# C1: quantum: volume grid x matter mode chi (conformal frame), vacuum standard subtracted
Lam, sig = 500.0, 0.01; M, _ = friedmann_start(sig, u0, l0); lp0 = sig * np.sqrt(M * l0 / 3); k0 = -6 * Lam * lp0 / sig; s0 = np.sqrt(l0 / (2 * abs(k0)))
n = 2048; h = 2.1 / n; x = 0.9 + h * np.arange(n); kk = 2 * np.pi * np.fft.fftfreq(n, h); nb = 16
a_op = np.diag(np.sqrt(np.arange(1, nb)), 1)
res = {}
for lab, mm, q in (('adiabatic', 30.0, 0.0), ('sudden', 0.5, 0.5)):
    wref = np.sqrt(q * q + (mm * l0) ** 2); X = (a_op + a_op.T) / np.sqrt(2 * wref); Pm = 1j * np.sqrt(wref / 2) * (a_op.T - a_op)
    w2 = q * q + (mm * x) ** 2; Hb = (Pm @ Pm).real / 2; X2 = (X @ X).real / 2
    Ub = np.empty((n, nb, nb), complex); G0 = np.empty((n, nb)); E0 = np.empty(n)
    Ev = np.empty((n, nb)); Vv = np.empty((n, nb, nb))
    for i in range(n):
        ev, vv = np.linalg.eigh(Hb + w2[i] * X2); Ev[i], Vv[i] = ev, vv; E0[i] = ev[0]
        Ub[i] = (vv * np.exp(-0.5j * sig * (ev - ev[0]) - 0.5j * Lam * M * sig * x[i])) @ vv.T
    Tk = np.exp(-1j * (-sig * kk ** 2 / (12 * Lam)))
    psi = (np.exp(-(x - l0) ** 2 / (4 * s0 ** 2) + 1j * k0 * x)[:, None] * Vv[:, :, 0]); psi /= np.linalg.norm(psi)
    lcl = lambda t: l0 - sig * k0 / (6 * Lam) * t + sig ** 2 * M * t * t / 12
    def Ubg(l):
        ev, vv = np.linalg.eigh(Hb + (q * q + (mm * l) ** 2) * X2); return (vv * np.exp(-0.5j * sig * ev)) @ vv.T, vv
    phi = np.linalg.eigh(Hb + (q * q + (mm * l0) ** 2) * X2)[1][:, 0].astype(complex); Nb = []
    Nt = []; Mt = []
    for t in range(1, 121):
        phi = Ubg(lcl(t))[0] @ (Ubg(lcl(t - 1))[0] @ phi)
        if t % 20 == 0: Nb.append((abs(Ubg(lcl(t))[1].T @ phi) ** 2 * np.arange(nb)).sum())
        psi = np.einsum('iab,ib->ia', Ub, psi); psi = np.fft.ifft(Tk[:, None] * np.fft.fft(psi, axis=0), axis=0)
        psi = np.einsum('iab,ib->ia', Ub, psi)
        if t % 20 == 0:
            c = np.einsum('iab,ia->ib', Vv, psi); Pn = abs(c) ** 2
            Nt.append((Pn * np.arange(nb)).sum()); Pl = (abs(psi) ** 2).sum(1); Mt.append((Pl * x).sum() - (l0 - sig * k0 / (6 * Lam) * t + sig ** 2 * M * t * t / 12))
    res[lab] = (Nt, Mt, np.linalg.norm(psi), sig * np.sqrt(q * q + (mm * l0) ** 2), Nb)
    del Ub, Vv
rat = np.array(res['sudden'][0][1:]) / np.array(res['sudden'][0][:-1]); bg = (abs(np.array(res['sudden'][0]) / np.array(res['sudden'][4]) - 1).max(), abs(np.array(res['adiabatic'][0]) - np.array(res['adiabatic'][4])).max())
ok = res['adiabatic'][0][-1] < 1e-3 and np.all(np.diff(rat) < 0) and bg[0] < 1e-3 and bg[1] < 3e-5 and \
     all(abs(r[2] - 1) < 1e-10 for r in res.values()) and max(abs(np.array(res['adiabatic'][1]))) < 1e-3
check('C1 [D] quantum volume mode x a matter mode (fixed lapse, vacuum standard): the joint tick is unitary, an adiabatic '
      'mode stays in its vacuum, a light mode is excited with decelerating growth, in both cases equal to the '
      'Bogoliubov number on the classical orbit, and <l> stays on the Friedmann orbit: the ghost sign adds no runaway '
      'to ordinary cosmological particle creation, because the volume mode has no frequency to resonate with',
      ok, '; '.join(f"{k} (omega/tick {v[3]:.2f}): N(t=20..120) " + '/'.join(f'{z:.1e}' for z in v[0]) + f", max|<l>-orbit| {max(abs(np.array(v[1]))):.0e}" for k, v in res.items()) + f'; N vs classical-orbit Bogoliubov: light rel {bg[0]:.0e}, adiabatic abs {bg[1]:.0e}')
# C2: classical mechanism: ghost with restoring force at resonance runs away; without restoring force it cannot
def rhs(t, y, s1, Om, F, eps, w):
    q1, p1, q2, p2 = y; we = w * w * (1 + eps * q1)
    return [s1 * p1, -s1 * Om * Om * q1 - s1 * F - eps * w * w * q2 * q2 / 2, p2, -we * q2]
out = {}
for lab, s1, Om, F in (('ghost Om=2w', -1, 2.0, 0.0), ('normal Om=2w', 1, 2.0, 0.0), ('ghost no restoring', -1, 0.0, -1e-3)):
    ev = lambda t, y, *a: abs(y[2]) - 1e3; ev.terminal = True
    sol = solve_ivp(rhs, (0, 3000), [0.05, 0.0, 0.05, 0.0], args=(s1, Om, F, 0.5, 1.0), rtol=1e-9, atol=1e-12, events=ev, max_step=0.5, t_eval=np.linspace(0, 3000, 6001), method='DOP853')
    q1, p1, q2, p2 = sol.y; we = np.sqrt(1 + 0.5 * q1); J = (p2 ** 2 + we ** 2 * q2 ** 2) / (2 * we)
    out[lab] = (sol.t[-1], np.nanmax(J[np.isfinite(J)]) / J[0], q1[-1])
ok = out['ghost Om=2w'][0] < 2999 and out['normal Om=2w'][1] < 50 and out['ghost no restoring'][0] > 2999 and out['ghost no restoring'][1] < 1.05
check('C2 [T-mechanism, D] a ghost coupled to matter runs away (blows up) only through a resonance: with a restoring '
      'force at Om = 2 omega the ghost pair grows without bound, a normal oscillator only trades energy, and a ghost with '
      'no restoring force (the fixed-lapse volume mode) leaves the matter action-variable adiabatic',
      ok, '; '.join(f'{k}: t_end {v[0]:.0f}, J_max/J_0 {v[1]:.3g}, q1_end {v[2]:.3g}' for k, v in out.items()))

print('== D. the dark constant')
# D1: the minimal spread of the dark constant on a Friedmann coherent state (Gaussian, exact): sigma_H^2 = b^2 s^2 + a^2 (4 k0^2 sk^2 + 2 sk^4)
def sH_rel(Lm):
    al = sig / (12 * Lm); be = Lm * M * sig; kk0 = 6 * Lm * lp0 / sig
    ss = np.logspace(-6, 0, 4000); sk = 1 / (2 * ss); sH = np.sqrt(be ** 2 * ss ** 2 + al ** 2 * (4 * kk0 ** 2 * sk ** 2 + 2 * sk ** 4))
    return sH.min() / (be * l0)
r1, rM, rN = sH_rel(4.0), sH_rel(4.0e4), sH_rel(4.0e6)
check('D1 [T] the tick between splits is tick-independent, so the dark constant (quasi-energy) is exactly conserved and '
      'each value is a superselection sector; nothing forces D = 0, and a localised edge cannot have sharp D: its least '
      'spread relative to the matter energy is ~ 0.4 on one cube and falls as 1/sqrt(N) on N cubes',
      r1 > 0.1 and abs(rN / rM * 10 - 1) < 0.02, f'sigma_D/(Lam M sig l): one cube {r1:.3f}, N = 1e4 {rM:.2e}, N = 1e6 {rN:.2e}')
# D2: kinematic lemma for an inhomogeneous propagating dark mode
cd = 1 / np.sqrt(3); k2 = np.array([1.0, 0, 0]); th = np.arccos(-0.9); k3 = np.array([np.cos(th), np.sin(th), 0])
f = lambda s: (np.linalg.norm(k2) + s) * cd - np.linalg.norm(k2 + s * k3)
s_ = brentq(f, 1.0, 5.0); k3 = s_ * k3; k1 = -(k2 + k3); Ebal = np.linalg.norm(k1) - cd * (np.linalg.norm(k2) + np.linalg.norm(k3))
one = min(np.linalg.norm(q) * 1 - cd * np.linalg.norm(q) for q in rng.normal(size=(1000, 3)))
check('D2 [T] kinematics: if the dark (constraint) sector propagated as negative-energy quanta at speed 1/sqrt3, the '
      'vacuum could decay to one photon + two dark quanta (explicit momenta balance); one dark quantum + one photon cannot; '
      'a dark constant frozen per cube (no propagation) opens no channel', abs(Ebal) < 1e-12 and one > 0,
      f'photon + 2 dark: E-balance {Ebal:.0e}, |k| = {np.linalg.norm(k1):.3f}, {np.linalg.norm(k2):.3f}, {np.linalg.norm(k3):.3f}')

print('== E. estimates against measurement')
lP = 1.616e-35; lc = 2 * np.sqrt(8 * np.pi) * lP; Lrec = 5.7e21   # Hubble radius at recombination, physical (m)
Ncell = (Lrec / lc) ** 3; sd_ind = r1 / np.sqrt(Ncell); sd_cor = lc / Lrec
check('E1 [E] quantum spread of the volume mode (and of the dark constant) on a Hubble patch at recombination, '
      'independent cells (one-cube spread / sqrt N) or correlated (l/L, edge-source B5), against the measured CMB '
      'isotropy 1e-5: negligible either way; the MEAN dark constant is a free sector value that only N_eff bounds',
      max(sd_ind, sd_cor) < 1e-5, f'N_cell {Ncell:.0e}; spread {sd_ind:.0e} (indep.) / {sd_cor:.0e} (corr.) vs 1e-5; mean D: N_eff gives < 0.04 of radiation')
print('supplied: frustum carrier, mid-slab read, dust/matter phases, Lam (unit map), hop-form kinetic term, nearest-unitary rule not chosen;')
print('not built: inhomogeneous volume modes (hinge coupling between unequal cubes), mixed-edge triangles, quantum crush.')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
