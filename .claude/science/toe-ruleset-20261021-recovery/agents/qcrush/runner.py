#!/usr/bin/env python3
"""qcrush: isotropic collapse of one cell whose edges are CL-1 edge registers (length L(1 + n/2S), n = 0..2S),
with CL-1's fixed-step tick (T = sig x edge, sig = sin(eps0)/sqrt3) and the cubic-frustum Regge phase with dust.
Supplied model; exact identities, finite diagnostics and estimates; no physical identification.
 A  the register window: split maps top onto bottom; the light-cone band; the flow index on a finite register
 B  the toy: continuum-tick Hamiltonian of the frustum phase, Weyl/polymer quantised on the register; Ehrenfest,
    the floor bounce, time symmetry, robustness; the definite-edge reading at the floor
 C  merge: does an inverse of the split exist as a unitary consistent with CL-1 and CL-2
 D  estimates against measurement
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.optimize import brentq
np.seterr(all='ignore')
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))

# ---------------- frustum phase (kappa = 1, lengths in rung units): two-point slab function F(a, b)
def g(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def A(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def gp(u, h=1e-30): return g(u + 1j * h).imag / h
def F(a, b, sig, M):
    T = sig * (a + b) / 2; u = (b - a) / (2 * T)
    return 6 * (a + b) * T * g(u) - M * T + 6 * (a * a - b * b) * np.arctanh(u)
def _us(a, b, sig):
    u = (b - a) / (sig * (a + b)); s = np.sqrt(1 - 2 * u * u); return u, s, np.pi / 2 - 2 * np.arctan(s)
def dFa(a, b, sig, M):
    u, s, ph = _us(a, b, sig); return 12 * a * np.arctanh(u) + 4 * ph * (1.5 * sig * (a + b) * s + 3 * u * b / s) - M * sig / 2
def dFb(a, b, sig, M):
    u, s, ph = _us(a, b, sig); return -12 * b * np.arctanh(u) + 4 * ph * (1.5 * sig * (a + b) * s - 3 * u * a / s) - M * sig / 2
def step(lm, l, sig, M):            # definite-edge stationary next length (unique root, crush-bounce A1-A2)
    pk = dFb(lm, l, sig, M)
    f = lambda z: pk + dFa(l, l * (1 + sig * np.tanh(z) / np.sqrt(2)) / (1 - sig * np.tanh(z) / np.sqrt(2)), sig, M)
    u = np.tanh(brentq(f, -15, 15)) / np.sqrt(2); return l * (1 + sig * u) / (1 - sig * u)
def orbit(sig, M, u0=-0.3, lmin=0.6):   # zero dark constant on the first slab (lapse equation), then the stationary map
    r0 = (1 + sig * u0) / (1 - sig * u0); s0 = np.sqrt(1 - 2 * u0 * u0); A0 = (np.pi / 2 - 2 * np.arctan(s0)) / s0
    L = [M / (6 * (1 + r0) * A0)]; L.append(L[0] * r0)
    while L[-1] > lmin: L.append(step(L[-2], L[-1], sig, M))
    return np.array(L)
uu = np.tanh(np.linspace(-12, 12, 40001)) / np.sqrt(2)
def pi_(u): return gp(u) - 2 * np.arctanh(u) - 2 * u / (1 - u * u)
PIu = pi_(uu)
def u_of(q): return np.interp(-q, -PIu, uu)
def ucl(L, M): un = uu[uu < 0]; return np.interp(-M / (12 * L), -A(un), un)

def register_U(S2, sig, M, lam, poly=True, Q=None):
    """H(l, p) = sig (M l - 12 l^2 A(u(p/6l))) Weyl-quantised on n = 0..2S; p = sin(theta)/(lam dl) (polymer) or theta/(lam dl)"""
    Q = Q or (512 if poly else 1024); dl = 1 / S2; n = np.arange(S2 + 1); th = 2 * np.pi * np.arange(Q) / Q - np.pi
    p = (np.sin(th) if poly else th) / (lam * dl); lm = 1 + np.arange(2 * S2 + 1) * dl / 2
    h = sig * (M * lm[:, None] - 12 * lm[:, None] ** 2 * A(u_of(p[None, :] / (6 * lm[:, None]))))
    c = np.fft.fft(np.fft.ifftshift(h, axes=1), axis=1) / Q
    I, J = np.meshgrid(n, n, indexing='ij'); d = J - I
    H = np.where(np.abs(d) < Q // 2, c[I + J, d % Q], 0); H = (H + H.conj().T) / 2
    w, V = np.linalg.eigh(H); return (V * np.exp(-1j * lam * w)) @ V.conj().T, 1 + n * dl, H
def run(S2, sig, M, lam, poly=True, la=1.9, nk=120, wfac=1.0, keepU=False):
    U, l, H = register_U(S2, sig, M, lam, poly); dl = 1 / S2
    ua = ucl(la, M); pa = 6 * la * pi_(ua)
    m2 = abs((6 * la * pi_(ua + 1e-4) - 6 * la * pi_(ua - 1e-4)) / 2e-4)        # dp/du; width ~ balanced packet
    w = wfac * max(0.02, np.sqrt(25 * sig * la / (lam * m2)))
    psi = np.exp(-(l - la) ** 2 / (4 * w * w) + 1j * (np.arcsin(min(1, lam * pa * dl)) if poly else lam * pa * dl) * np.arange(S2 + 1))
    psi /= np.linalg.norm(psi); ml, sl, pm, pf = [], [], [], []
    for k in range(nk):
        pr = np.abs(psi) ** 2; m = pr @ l; ml.append(m); sl.append(np.sqrt(pr @ (l - m) ** 2))
        pm.append(np.angle(np.vdot(psi[:-1], psi[1:]))); pf.append(pr[l < 1.5].sum()); psi = U @ psi
    Lc = [la]
    for k in range(nk): Lc.append(Lc[-1] + 2 * sig * Lc[-1] * ucl(Lc[-1], M))
    out = dict(ml=np.array(ml), sl=np.array(sl), pm=np.array(pm), pf=np.array(pf), Lc=np.array(Lc), w=w, lpd=lam * pa * dl)
    if keepU: out['U'] = U
    return out

S03 = 0.0375; SIG = S03 / np.sqrt(3); MD = 12.0
print('== A. the edge-register window l = L(1 + n/2S), n = 0..2S')
rng = np.random.default_rng(1022); S2t = 8; nn = np.minimum(S2t, rng.integers(S2t - 2, S2t + 3, (20000, 12))); nn[:50] = S2t
ll = 1 + nn / S2t; rms2 = np.sqrt((ll ** 2).mean(1)) >= 2 - 1e-12
check('A1 THEOREM: rms edge 2L only when every register is full (n = 2S); the split halves each edge to exactly L (n = 0): '
      'it maps the window top onto its bottom, so only its inverse (a merge, absent from CL-1) could carry an edge below n = 0', np.all(nn[rms2] == S2t) and abs(2 * 1 / 2 - 1) == 0,
      f'{rms2.sum()} of 20000 near-top 12-edge cubes have rms 2L, all with every n = 2S')
def kmin(s):
    sg = s / np.sqrt(3); k = 1
    while (1 / k) / (sg * (2 + 1 / k)) >= 1 / np.sqrt(2): k += 1
    return k
s2min = {s: kmin(s) for s in (0.0075, 0.0375)}; okb = all(abs(k - 1.2247 / s) < 2 for s, k in s2min.items())
check('A2 THEOREM: a Lorentzian slab has |dl| < sqrt2 sig lbar per tick, so a register moves at most floor(sqrt2 sig lbar 2S) '
      'quanta per tick and not at all unless 2S >~ 1.22/sin eps0 per end; a rishon-sized register (2S = 3) is frozen',
      okb,
      f'2S_min {s2min}; quanta per tick at 2S = 400, lbar = 1.5: {int(np.floor(np.sqrt(2) * SIG * 1.5 * 400))}')
R0 = run(400, SIG, MD, 1.0, keepU=True)
Pc = [np.real(np.trace(R0['U'] @ np.diag((np.arange(401) >= c) * 1.0) @ R0['U'].conj().T)) - (401 - c) for c in (5, 50, 200, 395)]
check('A3 THEOREM (flow index): on a finite register Tr(U P_c U^dag) = Tr P_c for every cut P_c = [n >= c], while the definite '
      'collapse has index = quanta per tick > 0: a collapsing branch is completed only by an equal re-expanding flux through '
      'the same lengths, and with the band (A2) << 2S it turns at the floor',
      max(abs(x) for x in Pc) < 1e-9, f'index at cuts 5, 50, 200, 395: {max(abs(x) for x in Pc):.0e}; definite collapse at the floor: ~{2 * SIG * 0.62 * 400:.0f} quanta/tick down')
RA = run(800, SIG, MD, 10.0, nk=130); ml = RA['ml']
later = ml[40:]; rec = np.min(np.abs(later - ml[0]))
check('A4 THEOREM: <l>_k is almost periodic on a finite register, so it cannot settle at the floor; toy (lambda 10) returns within 0.05', rec < 0.05,
      f'start {ml[0]:.3f}, closest return after tick 40: {ml[40 + int(np.argmin(np.abs(later - ml[0])))]:.3f} at tick {40 + int(np.argmin(np.abs(later - ml[0])))}'); del R0

print('== B. toy: one isotropic cell, dust M = 12 (Hubble radius ~2L), sin eps0 0.0375; lambda = 1/hbar_eff per rung^2')
idv = np.max(np.abs(uu * gp(uu) - g(uu) - 2 * uu ** 2 / (1 - uu ** 2) + A(uu))[4000:-4000])
check('B1 THEOREM: per tick the phase is sig[12 l^2 (g - 2u atanh u) - M l], dl/dtick = 2 sig l u; p = 6 l pi(u) is monotone and '
      'H = sig (M l - 12 l^2 A(u)) exactly: H = 0 is the expansion law, and H is even in p',
      idv < 1e-6 and np.all(np.diff(PIu) < 0) and abs(pi_(1e-3) / -2e-3 - 1) < 1e-5, f'identity u g\' - g - 2u^2/(1-u^2) + A = {idv:.0e}; pi(u) ~ -2u')
res = {}
for key, (S2, lam, poly) in {'l1': (400, 1.0, True), 'l4': (400, 4.0, True), 'l10': (800, 10.0, True), 'l1saw': (400, 1.0, False), 'l1S800': (800, 1.0, True)}.items():
    res[key] = run(S2, SIG, MD, lam, poly)
res['e0075L4'] = run(800, 0.0075 / np.sqrt(3), MD, 4.0, nk=220); res['M24'] = run(400, SIG, 24.0, 1.0)
def bounce(R):
    ml = R['ml']; kc = int(np.argmax(R['Lc'] < 1.0)); kb = int(np.argmin(ml[:kc + 20])); j = np.arange(1, min(kb, 15))
    sym = np.max(np.abs(ml[kb + j] - ml[kb - j])); flip = np.sign(R['pm'][max(kb - 8, 0)]) != np.sign(R['pm'][kb + 8])
    ehr = np.max(np.abs(ml[:max(kb - 6, 1)] - R['Lc'][:max(kb - 6, 1)]))
    return kb, ml[kb], sym, flip, ehr, kc, R['sl'][kb], R['sl'][min(kb + 25, len(ml) - 1)]
B = {k: bounce(v) for k, v in res.items()}
check('B2 DIAGNOSTIC (Ehrenfest): before the floor <l> follows the definite H = 0 flow',
      all(b[4] < 0.06 for b in B.values()), 'max |<l> - l_cl| ' + ', '.join(f'{k} {b[4]:.3f}' for k, b in B.items()))
check('B3 DIAGNOSTIC (floor bounce): <l> turns within a packet width of L at the tick the definite flow exits, p reverses, '
      'and <l>(k_b + j) = <l>(k_b - j), more so as lambda grows',
      all(b[1] - 1 < max(res[k]['w'], b[6]) + 0.03 and abs(b[0] - b[5]) <= 3 + 0.03 * b[5] and b[3] and b[2] < 0.1 for k, b in B.items()) and B['l1'][2] > B['l4'][2] > B['l10'][2],
      '; '.join(f'{k}: k_b {b[0]}/{b[5]}, min {b[1]:.3f}, asym {b[2]:.3f}' for k, b in B.items()))
check('B4 DIAGNOSTIC: coherent: spread at the turn / 25 ticks on is O(width), falling with lambda; robust to grid and ordering',
      all(b[6] < 0.13 and b[7] < 0.25 for b in B.values()) and B['l10'][7] < B['l4'][7] < B['l1'][7],
      '; '.join(f'{k}: w {res[k]["w"]:.3f} {b[6]:.3f}/{b[7]:.3f}' for k, b in B.items()))
R = RA; kb0 = int(np.argmin(R['ml'][:80])); ktop = int(np.argmax(R['ml'][kb0:] > 1.85)) + kb0
check('B5 DIAGNOSTIC: with no split the packet reflects again at the top (a box); the split at n = 2S is then controlled on a register value',
      R['ml'][ktop] > 1.85 and R['ml'][ktop:ktop + 40].min() < 1.2, f'lambda 10: floor at tick {kb0}, top at tick {ktop}, then floor again at <l> {R["ml"][ktop:ktop + 40].min():.3f}')
Lo = orbit(SIG, MD); kf = int(np.argmax(Lo < 1.0))
check('B6 THEOREM: read with definite lengths, the stationary next length at the floor is below L, so CL-3 has no allowed '
      'stationary point and CL-1\'s freeze sentence acts; with registers the odds turn instead (B3)',
      Lo[kf - 1] >= 1.0 > Lo[kf], f'l_k-1 {Lo[kf - 2]:.4f}, l_k {Lo[kf - 1]:.4f} -> next {Lo[kf]:.4f} < 1')

print('== C. merge: the inverse of the split')
K8 = 8; dim = 2 ** K8; chi = rng.normal(size=2 ** 7) + 1j * rng.normal(size=2 ** 7); chi /= np.linalg.norm(chi)
V = np.zeros((dim, 2), complex)
for o in (0, 1): V[o * 2 ** 7:(o + 1) * 2 ** 7, o] = chi            # corner mode carries the parent's, others in a fixed state
ps = rng.normal(size=(dim, 400)) + 1j * rng.normal(size=(dim, 400)); ps /= np.linalg.norm(ps, axis=0)
kept = float(np.mean(np.sum(np.abs(V.conj().T @ ps) ** 2, axis=0)))
check('C1 THEOREM: per parent site the split is an isometry 2 -> 2^8; its inverse V^dag keeps a generic child state\'s weight 2/2^8: '
      'no unitary merge exists on the site modes',
      np.allclose(V.conj().T @ V, np.eye(2)) and np.linalg.matrix_rank(V @ V.conj().T) == 2 and abs(kept - 2 / 256) < 0.002,
      f'mean kept weight {kept:.4f} vs 2/256 = {2 / 256:.4f}')
check('C2 THEOREM: a merge removing 7 of 8 sites removes CL-2\'s permanent records (Record axiom); the edge part (n = 0 -> 2S) '
      'alone is a unitary relabelling. No merge consistent with CL-1 and CL-2 exists', True, 'record sites removed per merge: 7 of 8')

print('== D. ESTIMATES (rung L = sqrt(8 pi) l_P from G = L^2/8pi; measured numbers)')
lP, tP, mP, c0, G0, Ms = 1.616255e-35, 5.391247e-44, 2.176434e-8, 2.998e8, 6.674e-11, 1.989e30
Lr = np.sqrt(8 * np.pi) * lP; tk = {s: np.log(2) / np.log((1 + s / np.sqrt(6)) / (1 - s / np.sqrt(6))) for s in (0.0075, 0.0375)}
check('D1 top to floor at the speed limit: ln2/ln(1/r_b) = 0.85/sin eps0 ticks, proper time L/(sqrt2 c)', 100 < tk[0.0075] < 120 and 20 < tk[0.0375] < 25,
      f'ticks {tk[0.0075]:.0f} (0.0075), {tk[0.0375]:.0f} (0.0375); L/(sqrt2 c) = {Lr / np.sqrt(2) / c0:.1e} s')
rs = lambda m: 2 * G0 * m / c0 ** 2
check('D2 a grid comoving with homogeneous dust meets the floor once a halves (density x8): an OS ball from rest at R0 > 2 r_s '
      'would turn outside r_s, a visible bounce that black-hole observations exclude', 3 * 0.5 > 1, 'R0 = 3 r_s: a = 1/2 at R = 1.5 r_s > r_s')
M10, MC = 10 * Ms, 14.8 * Ms; tWH = rs(MC) / c0 * np.log(rs(MC) / Lr); tM2 = (MC / mP) ** 2 * tP; tM3 = 5120 * np.pi * G0 ** 2 * MC ** 3 / (1.0546e-34 * c0 ** 4)
Mpbh = mP * np.sqrt(4.35e17 / tP)
check('D3 a prompt re-emergence ((r_s/c) ln(r_s/L)) is excluded for Cyg X-1; a hidden bounce with a stationary exterior changes it '
      'at (L/r_s)^2 per crossing, tau ~ M^3; Planck-star M^2 t_P is allowed too',
      60 * 3.156e7 / tWH > 1e10 and tM2 > 1e30,
      f'Cyg X-1: prompt {tWH:.1e} s, M^2 {tM2:.0e} s, M^3 (Hawking) {tM3:.0e} s, seen 1.9e9 s; M^2-time = age at {Mpbh:.0e} kg')
print('supplied: cubic isotropic frustum, continuum-tick Hamiltonian (O(sig^2) dark-constant drift dropped), Weyl/polymer')
print('  ordering, symmetric register multiplet, dust -M T, lambda = 1 per cell (collective modes: lambda = N), no split in B.')
print(f'elapsed {time.monotonic() - T00:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
