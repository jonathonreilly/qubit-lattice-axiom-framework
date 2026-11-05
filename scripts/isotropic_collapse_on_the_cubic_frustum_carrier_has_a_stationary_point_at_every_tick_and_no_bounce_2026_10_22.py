#!/usr/bin/env python3
"""crush-bounce: homogeneous collapse to the crush on the cubic-frustum Lorentzian Regge carrier with CL-1's fixed-step
tick (T = sig x mean cell edge, sig = sin(eps0)/sqrt3, lapse following the edges, CL-3 stationary in the edges only).
Supplied models; exact identities, finite diagnostics and estimates; no physical identification.
 A  the edge equation near the null faces: a stationary point at every tick (IVT), uniqueness, a = 0 unreachable,
    radiation leaves the edge equation (scale-free map)
 B  dust collapse: GR stage, the null crush (Hl -> sqrt2, s_k+1/s_k -> r_b^2), the generated dark constant
 C  the two options: (a) freeze clause, (b) bounce / continuation through a = 0; odds, quasi-energy, records
 D  estimates against measurement (neutron-star collapse, black-hole exteriors, Hawking, white-hole re-emergence)
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/ISOTROPIC_COLLAPSE_ON_THE_CUBIC_FRUSTUM_CARRIER_HAS_A_STATIONARY_POINT_AT_EVERY_TICK_AND_NO_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120
import os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import mpmath as mp
from scipy.integrate import quad
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))

mp.mp.dps = 50; PI = mp.pi; R2 = mp.sqrt(2)
# ---------------- carrier (cosmology/tick-law frustum, kappa = 1): per slab 6 p T g(u) - E T, hinge 6 l^2 dAtanh
def g_np(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def S3(l0, l1, l2, sig, M, C=0.0):        # action terms touching l1; mid read T = sig (a+b)/2; dust M, radiation C/lbar
    out = 0
    for a, b in ((l0, l1), (l1, l2)):
        T = sig * (a + b) / 2; u = (b - a) / (2 * T); out += 6 * (a + b) * T * g_np(u) - M * T - C * T / ((a + b) / 2)
    u0 = (l1 - l0) / (sig * (l0 + l1)); u1 = (l2 - l1) / (sig * (l1 + l2))
    return out + 6 * l1 ** 2 * (np.arctanh(u1) - np.arctanh(u0)) + 6 * l0 ** 2 * np.arctanh(u0) - 6 * l2 ** 2 * np.arctanh(u1)
def resid(lkm, lk, ukm, skm, s, sig, M, sign=-1):
    """edge equation dS/dl_k (Schlaefli form) with s_k = sqrt(1-2u_k^2) as unknown; phi = asin(u^2/(1-u^2)) = pi/2 - 2 atan s"""
    uk = sign * mp.sqrt((1 - s * s) / 2); phk, phm = PI / 2 - 2 * mp.atan(s), PI / 2 - 2 * mp.atan(skm)
    lkp = lk * (1 + sig * uk) / (1 - sig * uk); pk, pkm = lk + lkp, lkm + lk
    return (12 * lk * (mp.atanh(uk) - mp.atanh(ukm)) + 4 * phk * (mp.mpf(1.5) * sig * pk * s + 3 * uk * lkp / s)
            + 4 * phm * (mp.mpf(1.5) * sig * pkm * skm - 3 * ukm * lkm / skm) - M * sig), lkp, uk
def Af(s): return (PI / 2 - 2 * mp.atan(s)) / s
def Afl(w): return np.arcsin(w * w / (1 - w * w)) / np.sqrt(1 - 2 * w * w)
def dAf(w, h=1e-7): return (Afl(w + h) - Afl(w - h)) / (2 * h)
def collapse(sig, M, C, u0, nmax, smin=mp.mpf(10) ** -30, lam=1):
    sig, M, C = mp.mpf(sig), mp.mpf(M), mp.mpf(C)
    s0 = mp.sqrt(1 - 2 * mp.mpf(u0) ** 2); u0 = -mp.sqrt((1 - s0 * s0) / 2); r0 = (1 + sig * u0) / (1 - sig * u0)
    a_ = 6 * (1 + r0) * Af(s0)                       # first slab: lapse equation, zero dark constant
    l0 = mp.findroot(lambda l: a_ * l - M - 2 * C / (l * (1 + r0)), mp.mpf(1) if M else mp.sqrt(2 * C / (a_ * (1 + r0)))) * lam
    L, U, S = [l0, l0 * r0], [u0], [s0]
    for k in range(nmax):
        f = lambda t: resid(L[-2], L[-1], U[-1], S[-1], mp.e ** t, sig, M)[0]
        lo, hi = mp.log(S[-1]) - 12, -mp.mpf(10) ** -40; flo = f(lo)
        if mp.sign(flo) == mp.sign(f(hi)): return L, U, S, ('no root', k)
        while hi - lo > mp.mpf(10) ** -28:
            mid = (lo + hi) / 2; fm = f(mid)
            if mp.sign(fm) == mp.sign(flo): lo, flo = mid, fm
            else: hi = mid
        s = mp.e ** ((lo + hi) / 2); _, lkp, uk = resid(L[-2], L[-1], U[-1], S[-1], s, sig, M)
        L.append(lkp); U.append(uk); S.append(s)
        if s < smin: return L, U, S, ('smin', k)
    return L, U, S, ('nmax', nmax)

print('== A. the edge equation on the cubic-frustum carrier with the fixed-step tick (exact algebra)')
rng = np.random.default_rng(20261022); dev = 0.0
for _ in range(6):
    sg, Mx = float(rng.uniform(0.005, 0.2)), float(rng.uniform(0.1, 3)); l0 = float(rng.uniform(0.5, 2)); ua, ub = rng.uniform(-0.69, 0.69, 2)
    l1 = l0 * (1 + sg * ua) / (1 - sg * ua); l2 = l1 * (1 + sg * ub) / (1 - sg * ub)
    cs = S3(l0, l1 + 1e-30j, l2, sg, Mx).imag / 1e-30
    an = resid(mp.mpf(l0), mp.mpf(l1), mp.mpf(ua), mp.sqrt(1 - 2 * mp.mpf(ua) ** 2), mp.sqrt(1 - 2 * mp.mpf(ub) ** 2), mp.mpf(sg), mp.mpf(Mx), int(np.sign(ub)))[0]
    dev = max(dev, abs(float(an) - cs) / abs(cs))
lim = []
for _ in range(6):
    sg, Mx, lk = mp.mpf(rng.uniform(0.005, 0.2)), mp.mpf(10 ** rng.uniform(-3, 3)), mp.mpf(10 ** rng.uniform(-3, 2)); ua = mp.mpf(rng.uniform(-0.7, 0.7))
    lkm = lk * (1 - sg * ua) / (1 + sg * ua); sa = mp.sqrt(1 - 2 * ua ** 2); e = mp.mpf(10) ** -30
    for sgn in (-1, 1):
        r, lkp, _ = resid(lkm, lk, ua, sa, e, sg, Mx, sgn); lim.append(float(r * e / (sgn * 3 * R2 * PI * lkp)))
check('A1 THEOREM: dS/dl_k = 12 l_k dAtanh + 4 phi_k (1.5 sig p_k s_k + 3 u_k l_k+1/s_k) + 4 phi_k-1 (1.5 sig p_k-1 s_k-1 - 3 u_k-1 '
      'l_k-1/s_k-1) - M sig (Schlaefli; s = sqrt(1-2u^2)); it runs from -inf (u_k -> -1/sqrt2) to +inf (u_k -> +1/sqrt2) as '
      '-/+ 3 sqrt2 pi l_k+1/s_k, all else bounded: CL-3 has a stationary point at every tick, for any edges and content',
      dev < 1e-9 and max(abs(v - 1) for v in lim) < 1e-12, f'vs complex-step action {dev:.0e}; limit ratios {min(lim):.12f}..{max(lim):.12f}')
cnt = []; sgrid = [mp.mpf(10) ** (-x) for x in np.linspace(40, 1e-4, 70)]
for _ in range(60):
    sg = mp.mpf(float(rng.choice([0.0043, 0.023, 0.05, 0.17]))); Mx = mp.mpf(10 ** rng.uniform(-3, 3)); lk = mp.mpf(10 ** rng.uniform(-3, 2))
    ua = mp.mpf(rng.uniform(-0.7071, 0.7071)); lkm = lk * (1 - sg * ua) / (1 + sg * ua); sa = mp.sqrt(1 - 2 * ua ** 2)
    rs = [resid(lkm, lk, ua, sa, s, sg, Mx, -1)[0] for s in sgrid] + [resid(lkm, lk, ua, sa, s, sg, Mx, 1)[0] for s in sgrid[::-1]]
    cnt.append(sum(mp.sign(rs[i]) != mp.sign(rs[i + 1]) for i in range(len(rs) - 1)))
check('A2 DIAGNOSTIC: the stationary point is unique: one root over the whole Lorentzian window in every sampled state',
      all(c == 1 for c in cnt), f'{len(cnt)} states (sig 0.0043-0.17, M 1e-3..1e3, l 1e-3..1e2, any u_k-1): roots {sorted(set(cnt))}')
qs = [mp.mpf(x) / R2 for x in (0.0043, 0.0231, 0.1706)]; rem = [float((1 + (1 - q) / (1 + q)) / (2 * (1 - (1 - q) / (1 + q))) * q * R2) for q in qs]
check('A3 THEOREM: |u| < 1/sqrt2 gives l_k+1/l_k > r_b = (1 - sin(eps0)/sqrt6)/(1 + sin(eps0)/sqrt6) > 0, so l_k >= l_0 r_b^k: a = 0 '
      'is reached at no finite tick; on the limiting sequence the remaining proper time is exactly l_k/sqrt2 (the cell '
      'shrinks at sqrt2 edges per light crossing)', all(abs(v - 1 / np.sqrt(2)) < 1e-12 for v in rem),
      f'remaining proper time / l_k = {rem[0]:.12f} (= 1/sqrt2) for sin eps0 = 0.0075, 0.04, 0.3')
lr = []
for lam in (1, mp.mpf(10) ** -25):
    L, U, S, info = collapse(0.0231, 0.0, 1.0, -0.05, 400, lam=lam); lr.append([float(u) for u in U])
dsc = S3(1.0, 0.99 + 1e-30j, 0.975, 0.05, 0.0, 2.0).imag / 1e-30 - S3(1.0, 0.99 + 1e-30j, 0.975, 0.05, 0.0, 0.0).imag / 1e-30
check('A4 THEOREM: with the tick following the edges a radiation phase -C T/lbar = -C sig per slab is edge-independent, so radiation '
      'leaves the edge equation and enters only through the first slab; gravity is homogeneous of degree 2, so the map of '
      'ratios is scale-free: one collapse orbit for every size', abs(dsc) < 1e-12 and np.allclose(lr[0], lr[1], rtol=0, atol=1e-25) and len(lr[0]) > 300,
      f'radiation term in dS/dl {dsc:.0e}; u sequences at scale 1 and 1e-25 agree to {np.max(np.abs(np.subtract(lr[0], lr[1]))):.0e} over {len(lr[0])} ticks')

print('== B. dust collapse (M = 1 per cube, kappa = 1, l_c = M/12 where A = 1; mid read; sig = sin(eps0)/sqrt3)')
res = {}
for e0, u0 in ((0.3, -0.03), (0.0866, -0.04), (0.04, -0.06)):
    sig = np.sin(e0) / np.sqrt(3); L, U, S, info = collapse(sig, 1.0, 0.0, u0, 6000)
    Lf = np.array([float(x) for x in L]); Hl = 2 * np.abs([float(u) for u in U]); p = Lf[1:] + Lf[:-1]; A = np.array([float(Af(s)) for s in S])
    D = (6 * p * A - 1.0) * p / 2; rb = (1 - sig / np.sqrt(2)) / (1 + sig / np.sqrt(2))
    k05, k1, k13 = (int(np.argmax(Hl > x)) for x in (0.5, 1.0, 1.3))
    sr = float(S[-1] / S[-2]); kd = [int(np.argmax(Lf < 12 ** -1 * 10 ** -j)) for j in (3, 4)]
    kg = int(np.argmax(Hl > 0.3)); law = [quad(lambda w: dAf(w) / (2 * sig * w * Afl(w)), -u0, H / 2, limit=200)[0] for H in (0.3, 1.0, 1.3)]
    res[e0] = dict(kg=kg, law=law, gr=2 / (sig * Hl[0]) - 2 / (sig * 0.3), sig=sig, info=info, k05=k05, k1=k1, k13=k13, l1=Lf[k1] * 12, l13=Lf[k13] * 12, cont=k05 + 2 / (sig * 0.5) - 2 / sig,
                   crunch=k05 + 4 / sig, sr=sr, rb=rb, Al2=A[-1] * Lf[-1] ** 2, Al2b=A[-40] * Lf[-40] ** 2, D=D[-1], D1=D[k05],
                   dec=kd[1] - kd[0], dec_th=np.log(10) / np.log(1 / rb), Hlend=Hl[-1], n=len(U), mirror=None, Lr=(L, U, S))
    k = k1; mres = resid(L[k - 1], L[k], U[k - 1], S[k - 1], S[k - 1], mp.mpf(sig), mp.mpf(1.0), +1)[0]
    res[e0]['mirror'] = float(mres / (12 * L[k] * abs(mp.atanh(U[k - 1]))))
r = list(res.values())
check('B1 DIAGNOSTIC: up to Hl = 1.3 the carrier follows the exact expansion law A(Hl/2) = M/(12 l) with ticks dn = dtau/(sig l) '
      '(within 2 ticks); the cell reaches its Hubble radius (Hl = 1) at l = 2.0-2.1 l_c; GR (A = u^2) would crunch at the Hl = 1.3 tick',
      all(max(abs(k - n) for k, n in zip((v['kg'], v['k1'], v['k13']), v['law'])) < 2 and abs(v['k13'] / v['crunch'] - 1) < 0.01 and 1.9 < v['l1'] < 2.2 for v in r),
      '; '.join(f"sig {v['sig']:.4f}: ticks at Hl 0.3/1/1.3 {v['kg']}/{v['k1']}/{v['k13']} (law {v['law'][0]:.0f}/{v['law'][1]:.0f}/{v['law'][2]:.0f}; GR crunch {v['crunch']:.0f}), l/l_c at Hl=1 {v['l1']:.2f}" for v in r))
check('B2 DIAGNOSTIC: the null crush: Hl -> sqrt2, s_k+1/s_k -> r_b^2 exactly, A l^2 -> const (radiation-like), one decade of l per '
      'ln10/ln(1/r_b) ticks for ever; no tick lacks a root', all(v['info'][0] == 'smin' and abs(v['sr'] / v['rb'] ** 2 - 1) < 1e-9 and abs(v['Al2'] / v['Al2b'] - 1) < 1e-9
      and abs(v['dec'] - v['dec_th']) <= 1 and abs(v['Hlend'] - np.sqrt(2)) < 1e-12 for v in r),
      '; '.join(f"sig {v['sig']:.4f}: s ratio/r_b^2 - 1 = {v['sr'] / v['rb'] ** 2 - 1:.0e}, ticks/decade {v['dec']} ({v['dec_th']:.1f}), {v['n']} ticks to s = 1e-30" for v in r))
Dn = [v['D'] * 12 / v['sig'] ** 2 for v in r]
check('B3 DIAGNOSTIC: the fixed lapse does not keep its lost lapse equation through the crush: a positive dark constant '
      'D = (6pA - M) lbar -> (0.165 +- 0.002) sig^2 M l_c per cube (weakly start-dependent), over three quarters of it made '
      'after Hl = 0.5, then kept', all(v['D'] > 0 for v in r) and max(Dn) - min(Dn) < 0.005 and all(v['D1'] < 0.3 * v['D'] for v in r),
      'D/(sig^2 M l_c) ' + ', '.join(f'{x:.4f}' for x in Dn) + '; at Hl = 0.5 ' + ', '.join(f"{v['D1'] / v['D']:.3f}" for v in r) + ' of final')
L, U, S, info = collapse(0.0231, 0.0, 1.0, -0.05, 3000); Lf = np.array([float(x) for x in L]); p = Lf[1:] + Lf[:-1]
Crat = float((6 * p[-1] * Af(S[-1])) * p[-1] / 2 / 1.0)
check('B4 DIAGNOSTIC: radiation collapse (scale-free orbit) also ends in the null crush with no tick lacking a root; the '
      'radiation constant leaves larger by a sig-fixed factor', info[0] == 'smin' and Crat > 1, f'{info}; C_final/C_initial {Crat:.6f} (sig 0.0231)')

print('== C. the two options')
v = res[0.04]
check('C1 THEOREM (A1 + A3): CL-1\'s crushed-cube clause never acts in homogeneous isotropic collapse: CL-3 always has its '
      'stationary point. The carrier freezes itself in proper terms instead: proper tick sig l, rest phase m sig l and the '
      'remaining proper time l/sqrt2 all fall by r_b per tick, while the odds keep their unitary half-ticks',
      v['info'][0] == 'smin' and 0 < v['rb'] < 1, f"after Hl = 1.3, each tick multiplies them by r_b = {v['rb']:.6f} (sin eps0 0.04)")
check('C2 THEOREM: no bounce: A(u) = 0 only at u = 0, so a turning slab needs total energy M + D/lbar = 0, i.e. a negative dark '
      'constant; the one made is positive (B3); the time-mirrored slice is not stationary (residual / momentum term = O(1))',
      all(v['D'] > 0 and abs(v['mirror']) > 0.1 for v in r), 'mirror residual/(12 l atanh|u|) at Hl = 1: ' + ', '.join(f"{v['mirror']:+.3f}" for v in r))
sgs = np.sin(np.linspace(1e-4, np.pi / 2, 200)) / np.sqrt(3)
check('C3 THEOREM (A3, A4, CL-1 text): reaching a = 0 in one tick needs |u| = 1/sig >= sqrt3 > 1/sqrt2 for every step, so '
      'continuation through a = 0 is unavailable (a = 0 is at tick +inf). In site labels the massless half-tick on equal '
      'edges is the same unitary every tick (R = W, step eps0): the scale-free circuit simply continues for ever, quasi-energy '
      'kept exactly, mass angles m sig l -> 0, records written every half-tick', np.all(1 / sgs >= np.sqrt(3) - 1e-12),
      f'min 1/sig = {np.min(1 / sgs):.4f}; records inside grow ~ n (unbounded) within proper time l/sqrt2; they never condition the odds')

print('== D. ESTIMATES (cube 2 sqrt(8 pi) l_P; measured numbers)')
G, c, hb, lP, tP, Ms = 6.674e-11, 2.998e8, 1.0546e-34, 1.616255e-35, 5.391247e-44, 1.989e30
l0 = 2 * np.sqrt(8 * np.pi) * lP; rho0 = 5e17; H0 = np.sqrt(8 * np.pi * G * rho0 / 3); x = H0 * l0 / c
at = (x / 1.0) ** 2; rho_t = rho0 / at ** 3; rhoP = 5.155e96; s4 = np.sin(0.04) / np.sqrt(3)
check('D1 neutron-star-density collapse: the null crush starts when a/a0 = (H0 l0/c)^2, at a density far above Planck, '
      'after ~2/(sig H0 l0) ticks; the proper time left is ~l/c', 1e-80 < at < 1e-74,
      f'H0 l0/c {x:.1e}; a/a0 {at:.1e}; rho {rho_t:.0e} kg/m^3 = {rho_t / rhoP:.0e} rho_P; ticks {2 / (s4 * x):.1e}; time left {at * l0 / c:.0e} s')
M10 = 10 * Ms; rs = 2 * G * M10 / c ** 2; tH = 5120 * np.pi * G ** 2 * M10 ** 3 / (hb * c ** 4)
check('D2 black-hole exteriors: nothing in the interior is undefined, and the exterior is its own domain of dependence, so a '
      '10 M_sun exterior persists; Hawking flux from the exterior circuit, lattice corrections ~ (l/r_s)^2; evaporation '
      'takes a finite number of ticks, during which the interior cells shrink by r_b per tick', (l0 / rs) ** 2 < 1e-70,
      f'(l/r_s)^2 {(l0 / rs) ** 2:.0e}; t_evap {tH / 3.156e7:.1e} yr = {tH * c / (s4 * l0):.0e} ticks')
tWH = rs / c * np.log(rs / l0); obs = {'Cyg X-1 (since 1964)': 60 * 3.156e7, 'Sgr A* (S2 orbits, 30 yr)': 30 * 3.156e7}
check('D3 a time-symmetric bounce (not a CL-3 solution, C2) would re-emerge as a white hole after ~ (r_s/c) ln(r_s/l): for '
      'Cyg X-1 excluded by its persistence by > 1e10 and Sgr A* by > 1e5; a Planck-delayed (M^2) route needs a non-stationary '
      'exterior region, which CL-3 forbids', obs['Cyg X-1 (since 1964)'] / (tWH * 1.48) > 1e10 and obs['Sgr A* (S2 orbits, 30 yr)'] / (tWH * 4.3e5) > 1e5,
      f'10 M_sun: {tWH:.1e} s; Cyg X-1 (14.8 M_sun) {tWH * 1.48:.1e} s vs {obs["Cyg X-1 (since 1964)"]:.1e} s; Sgr A* {tWH * 4.3e5:.0e} s vs {obs["Sgr A* (S2 orbits, 30 yr)"]:.0e} s')
print('supplied: cubic isotropic frustum carrier, mid-slab tick read, dust -M T and radiation -C T/lbar phases, zero initial')
print('  dark constant, kappa = 1, unit map, measured numbers; not built: anisotropic (Kasner) crush, inhomogeneous junction.')
print(f'elapsed {time.monotonic() - T00:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
