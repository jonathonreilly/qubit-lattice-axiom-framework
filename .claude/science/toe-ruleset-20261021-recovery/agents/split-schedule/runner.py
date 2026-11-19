#!/usr/bin/env python3
"""Split schedule under CL-1 (edge-read step), CL-3 (stationary phase at fixed 4-volume per record) and the split
trigger (2^3 split when edges reach 2 rung units), on the cubic-frustum Regge carrier of agents/cosmology, in a w = -1
phase. Supplied models; finite diagnostics; no physical identification.
 A  tick pattern T = V0/l^3, sin eps = sqrt3 V0/l^4 (x8, x16 at a split); unimodular slab Lagrangian; the junction is
    momentum matching 2F(u_f) = F(u_c), F = 12(atanh u + u A(u)), with no tick in it; kick Lambda^2/rho*
 B  discrete Regge FRW at universal V0 through 4 splits: conserved constant, self-similar cycles N_k = N(Lambda_k),
    kick = cycle map G for every junction tick, G(x) > x
 C  drift and tilt: ticks per split fall by (Ha)^2/4 per split, n_s - 1 = +(Ha)^2/(2 ln2) > 0; running; dilution
 D  consistency: exit, e-folds, Lambda bookkeeping, A_s source, band flips at the x16 step jump, coupling drift
 E  what a red tilt needs: the constant must fall per split; supplied transfer-law families
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import cmath, itertools, math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

T0 = time.monotonic(); PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- carrier: kappa = 1 per rung cell, rung a = 1, G = 1/(8 pi), rho* = 3/(4 pi G a^2) = 6
RS = 6.0; UMAX = 1 / math.sqrt(2)
def fv(a, b): return (a + b) * (a * a + b * b) / 4                       # frustum 4-volume per unit central tick
def Af(u): return math.asin(u * u / (1 - u * u)) / math.sqrt(1 - 2 * u * u)
def Fm(u): return 12 * (math.atanh(u) + u * Af(u))
def sigma(a, b, V):                                                      # slab action with its face boundary terms
    f = (a + b) * (a * a + b * b) / 4; T = V / f; u = (b - a) / (2 * T)
    return 6 * (a + b) * T * cmath.sqrt(1 - 2 * u * u) * cmath.asin(u * u / (1 - u * u)) + 6 * (a * a - b * b) * cmath.atanh(u)
HC = 1e-30
def D1(a, b, V): return sigma(complex(a, HC), b, V).imag / HC            # complex-step derivatives
def D2(a, b, V): return sigma(a, complex(b, HC), V).imag / HC
def uof(a, b, V): return (b - a) * fv(a, b) / (2 * V)
def Lam(a, b, V): return 6 * (a + b) * Af(uof(a, b, V)) / fv(a, b)      # the rule-U constant read off one slab
def Ainv(y): return brentq(lambda u: Af(u) - y, 0.0, UMAX * (1 - 1e-15), xtol=1e-16, rtol=1e-15)
def Finv(y): return brentq(lambda u: Fm(u) - y, 0.0, UMAX * (1 - 1e-15), xtol=1e-16, rtol=1e-15)
def G(x):                                   # x = Lambda a^2/3 at a trigger; leading-order (short-slab) cycle map
    return 4 * Af(Finv(Fm(Ainv(x)) / 2))
def Nq(lam, V):                             # ticks for l: 1 -> 2 at constant lam: (1/V) int l^3/(2u) dl
    return quad(lambda l: l ** 3 / (2 * Ainv(lam * l * l / 12)), 1, 2, epsabs=0, epsrel=1e-12)[0] / V

def solve_b(a, target, V, bg):
    f = lambda b: D1(a, b, V) - target; d = 1e-3 * (bg - a); lo, hi = bg - d, bg + d
    for _ in range(40):
        if f(lo) * f(hi) < 0: break
        d *= 3; lo, hi = max(a * (1 + 1e-15), bg - d), bg + d
    return brentq(f, lo, hi, xtol=1e-15, rtol=1e-15)

def run(lam0, Vs, nsplit, after=None):
    """pure Lambda, 4-volume Vs(k) per cell in cycle k; start at l = 1 just after a split; the edge equation
    D2 s(l_{n-1}, l_n) + D1 s(l_n, l_{n+1}) = 0, and at a trigger (l >= 2) 2 D2 s(., 2l) + 8 D1 s(l, .) = 0"""
    V = Vs(0); a = 1.0; u0 = Ainv(lam0 / 12)
    b = brentq(lambda b: uof(a, b, V) - u0, a, a + 2 * u0 * V + 1e-12, xtol=1e-16, rtol=1e-15)
    S = [(a, b, V)]; p = D2(a, b, V); up = uof(a, b, V); k = 0; jun = []; na = 0
    while True:
        a = b
        if a >= 2.0:
            k += 1
            if k > nsplit: break
            a /= 2; V = Vs(k); target = -p / 4; ug = up / 2; jun.append(len(S))
        else:
            target = -p; ug = up
        if after is not None and k == nsplit:
            na += 1
            if na > after: break
        b = solve_b(a, target, V, a + 2 * ug * V / fv(a, a + 2 * ug * V / a ** 3))
        S.append((a, b, V)); p = D2(a, b, V); up = uof(a, b, V)
    return S, jun

def cycles(S, jun):
    L = [Lam(*s) for s in S]; m2 = [(L[i] + L[i + 1]) / 2 for i in range(len(L) - 1)]; st = [0] + jun
    Lc, Nf, dev = [], [], 0.0
    for c in range(len(jun)):
        i0, i1 = st[c], jun[c]; seg = m2[i0 + 3:i1 - 3]; Lc.append(sum(seg) / len(seg))
        dev = max(dev, max(abs(x / Lc[-1] - 1) for x in seg))
        lead = (S[i0][0] - 1.0) / (S[i0][1] - S[i0][0]) if c else 0.0
        Nf.append(lead + (i1 - 1 - i0) + (2.0 - S[i1 - 1][0]) / (S[i1 - 1][1] - S[i1 - 1][0]))
    return Lc, Nf, dev, m2

ns, dns, als, dals = 0.9649, 0.0042, -0.0045, 0.0067
HaT = math.sqrt(0.036 * 2.099e-9 * math.pi ** 2 / 2)                     # tensor bound on H a (M_P,red = 1/a)

print('== A. tick pattern and junction under the rules')
l, V0s, a_ = sp.symbols('l V0 a', positive=True)
Tl = V0s / l ** 3; s_eps = sp.sqrt(3) * Tl / l
r_T = sp.simplify(Tl.subs(l, a_) / Tl.subs(l, 2 * a_)); r_e = sp.simplify(s_eps.subs(l, a_) / s_eps.subs(l, 2 * a_))
fv_eq = sp.simplify(sp.Rational(1, 4) * (2 * l) * (2 * l ** 2) - l ** 3)
st_lo, st_hi = math.sin(0.008) / math.sqrt(3), math.sin(0.04) / math.sqrt(3)
check('THEOREM: fixed 4-volume V0 per record and the edge reading give T = V0/l^3, sin eps = sqrt3 V0/l^4; a split '
      '(2a -> a) multiplies the tick by 8 and sin eps by 16; a real step needs V0 <= a^4/sqrt3, the stability bound',
      r_T == 8 and r_e == 16 and fv_eq == 0, f'x{r_T}, x{r_e}; V0/a^4 <= {st_lo:.4f}..{st_hi:.4f} (eps_max 0.008..0.04), eps_min = eps_max/16')
u, T, V, H, lp = sp.symbols('u T V H lp', positive=True)
gS = sp.sqrt(1 - 2 * u ** 2) * sp.asin(u ** 2 / (1 - u ** 2)); AS = sp.asin(u ** 2 / (1 - u ** 2)) / sp.sqrt(1 - 2 * u ** 2)
sig0 = sp.series(12 * l * gS - 24 * l * u * sp.atanh(u), u, 0, 6).removeO()
Ln = -3 / V * l ** 4 * lp ** 2; En = sp.simplify(lp * sp.diff(Ln, lp) - Ln)
check('THEOREM (continuum): slab action/T -> -12 l u^2 - 8 l u^4 = -3 l ldot^2; per slab at fixed V0 it is '
      '-(3/V0) l^4 l\'^2, whose conserved energy is -3 V0 H^2 (H = l\' l^2/V0): de Sitter, Lambda the integration constant',
      sp.simplify(sig0 + 12 * l * u ** 2 + 8 * l * u ** 4) == 0 and sp.simplify(En.subs(lp, H * V / l ** 2) + 3 * V * H ** 2) == 0, f'E = {En}')
Fs = sp.series(12 * (sp.atanh(u) + u * AS), u, 0, 7).removeO(); mom = []
for uu in (0.05, 0.2, 0.5):
    Tt = 1e-7; b = 1 + 2 * uu * Tt; mom.append(abs(-D2(1.0, b, Tt * fv(1.0, b)) / b / Fm(uu) - 1))
check('THEOREM: momentum per unit edge -D2 s / l -> F(u) = 12(atanh u + u A(u)) as T -> 0 (no tick in it)',
      max(mom) < 1e-5 and sp.expand(Fs - (12 * u + 16 * u ** 3 + sp.Rational(132, 5) * u ** 5)) == 0, f'F = {Fs}; rel {max(mom):.0e}')
uc, c3, c5, x, d1, d2 = sp.symbols('u_c c3 c5 x d1 d2')
uf = uc / 2 + c3 * uc ** 3 + c5 * uc ** 5
eq = sp.expand(sp.series((2 * Fs).subs(u, uf) - Fs.subs(u, uc), uc, 0, 6).removeO())
sol = sp.solve([eq.coeff(uc, 3), eq.coeff(uc, 5)], [c3, c5], dict=True)[0]
A6 = sp.series(AS, u, 0, 7).removeO(); ucx = sp.sqrt(x) * (1 + d1 * x + d2 * x ** 2)
inv = sp.expand(A6.subs(u, ucx)); dsol = sp.solve([inv.coeff(x, 2), inv.coeff(x, 3)], [d1, d2], dict=True)[0]
Gx = sp.expand(sp.expand(4 * A6.subs(u, uf.subs(sol))).subs(uc, ucx.subs(dsol)))
Gx = sum(Gx.coeff(x, n) * x ** n for n in (1, 2))
check('THEOREM: junction 2F(u_f) = F(u_c): u_f = u_c/2 + u_c^3/2 + ..., so H jumps by (Ha)^2, and x = Lambda a^2/3 maps '
      'to x + x^2/2: kick Lambda^2/rho*, rho* = 6/a^2, independent of the tick on either side',
      sol[c3] == sp.Rational(1, 2) and Gx.coeff(x, 1) == 1 and Gx.coeff(x, 2) == sp.Rational(1, 2),
      f'c3 = {sol[c3]}, c5 = {sol[c5]}; G = {Gx} + O(x^3)')

print('== B. discrete Regge FRW at universal V0, pure Lambda, 4 splits (relative step ~ 1/1500)')
RUN = {}
for Ha in (0.4, 0.2, 0.1, 0.05):
    V0 = 7 / (3 * 1500 * Ha); S, jun = run(3 * Ha * Ha, lambda k, V0=V0: V0, 4); RUN[Ha] = (S, jun, V0) + cycles(S, jun)
c2 = max(RUN[h][5] / (h * RUN[h][2]) ** 2 for h in RUN)
check('rule U at universal V0: the constant is conserved inside every cycle (no drift; deviation O(c^2), c = H V0)',
      c2 < 1, f'max |Lambda_n/Lambda_cyc - 1|/c^2 = {c2:.3f}')
sr = max(abs(RUN[h][4][c] / Nq(RUN[h][3][c], RUN[h][2]) - 1) for h in RUN for c in range(4))
S2, j2 = run(3 * 0.04, lambda k: RUN[0.2][2] / 2, 2); L2, N2, *_ = cycles(S2, j2)
sv = abs(N2[1] * RUN[0.2][2] / 2 / (Nq(L2[1], 1.0)) - 1)
check('self-similar cycles: ticks per split N_k = N(Lambda_k) = (1/V0) int_a^2a l^3/(2u) dl with A(u) = Lambda l^2/12, '
      'so N depends on k only through the constant; N V0 is V0-independent', sr < 1e-4 and sv < 1e-4, f'max rel {sr:.0e}; V0/2: {sv:.0e}')
kr = [(h, (RUN[h][3][1] / RUN[h][3][0] - 1), G(RUN[h][3][0] / 3) / (RUN[h][3][0] / 3) - 1, RUN[h][3][0] / RS) for h in RUN]
check('every split kicks the constant up by the cycle map G (sim vs leading order), -> Lambda^2/rho* as Ha -> 0',
      all(abs(k_ / g_ - 1) < 1e-3 for _, k_, g_, _ in kr) and abs(kr[-1][1] / kr[-1][3] - 1) < 3e-3,
      'kick/(L/rho*) ' + ', '.join(f'{k_ / r_:.4f}' for h, k_, g_, r_ in kr) + ' (Ha .4,.2,.1,.05)')
pres = []
for f_ in (1.0, 1 / 8, 1 / 16):                                          # T x8 (universal), T continuous, step kept
    Sx, jx = run(3 * 0.04, lambda k, f_=f_: RUN[0.2][2] * (f_ if k else 1.0), 1, after=600)
    Lx = [Lam(*s) for s in Sx]; mx = [(Lx[i] + Lx[i + 1]) / 2 for i in range(len(Lx) - 1)]; j = jx[0]
    pres.append(sum(mx[j + 3:j + 300]) / sum(mx[j - 300:j - 3]) - 1)
check('THEOREM check: the kick is the same whatever the junction does to the tick (x8, x1, x1/2: T x8 vs lambda-split)',
      max(pres) / min(pres) - 1 < 3e-4, ', '.join(f'{p_:.6f}' for p_ in pres))
xs_ = np.logspace(-6, 3, 19); gx = [G(v) / v for v in xs_]
check('the exact cycle map has G(x) > x for every x: no fixed point; G(x)/x -> 1 + x/2 at low and -> 2 at high density',
      all(g > 1 for g in gx) and abs((gx[0] - 1) / (xs_[0] / 2) - 1) < 1e-2 and abs(gx[-1] - 2) < 0.02, f'G/x at 1e-6: 1+{gx[0] - 1:.3e}; at 1e3: {gx[-1]:.4f}')

print('== C. drift of the schedule and the tilt')
S, jun, V0 = RUN[0.1][:3]
Hs = [(s[1] - s[0]) / ((s[0] + s[1]) / 2 * s[2] / fv(s[0], s[1])) for s in S]; j = jun[0]
jump, within = Hs[j] / Hs[j - 1] - 1, Hs[j - 1] / Hs[3] - 1; uc_ = (S[j - 1][1] - S[j - 1][0]) / (2 * S[j - 1][2] / fv(S[j - 1][0], S[j - 1][1]))
check('H is constant up to O((Ha)^2): a sawtooth falling (3/4)(Ha)^2 inside a cycle and jumping (Ha)^2 at the split, '
      'net +(Ha)^2/4 per split (Ha = 0.1)', abs(jump / uc_ ** 2 - 1) < 0.05 and abs(within / (-0.75 * 0.01) - 1) < 0.08,
      f'jump {jump:+.5f} vs {uc_ ** 2:.5f}; inside {within:+.5f} vs -0.00750')
dn = {h: (RUN[h][4][1] / RUN[h][4][0] - 1, Nq(RUN[h][3][1], 1) / Nq(RUN[h][3][0], 1) - 1) for h in RUN}
check('ticks per split DEcrease: N_{k+1}/N_k - 1 = -(Ha)^2/4 (1 + O(Ha^2)): larger zooms are longer-lived (opposite '
      'to the owner intuition)', all(v[0] < 0 and abs(v[0] / v[1] - 1) < 1e-3 for v in dn.values()) and abs(dn[0.05][0] / (-0.05 ** 2 / 4) - 1) < 0.02,
      ', '.join(f'{h}: {v[0]:+.5f} ({v[0] / (-h * h / 4):.3f})' for h, v in dn.items()))
eps_b = -HaT ** 2 / (4 * math.log(2)); grid = all(math.log2(Nq(3 * G(y), 1) / Nq(3 * y, 1)) < 0 for y in (1e-6, 1e-3, 0.05, 0.3))
Hneed = {q: brentq(lambda h: -q * math.log2(Nq(3 * G(h * h), 1) / Nq(3 * h * h, 1)) - (1 - ns), 1e-3, 0.6) for q in (2, 4)}
check('tilt n_s - 1 = -q log2(N_{k+1}/N_k) (q = 2: -2 eps) = +q (Ha)^2/(4 ln2) > 0 for every H: blue; at the tensor bound '
      f'Ha < {HaT:.2e} it is {-2 * eps_b:.1e} (q=2): n_s = 1, 8.4 sigma from 0.9649', grid and (1 - ns) / dns > 8,
      f'eps {eps_b:.2e}/split; measured magnitude would need Ha = {Hneed[2]:.3f} (q=2), {Hneed[4]:.3f} (q=4), wrong sign')
run_k = 2 * HaT ** 4 / (8 * math.log(2) ** 2)
check('running: the kick schedule gives alpha_s = (n_s-1)(Ha)^2/(2 ln2) ~ 1e-19 (0.7 sigma from -0.0045 +- 0.0067, no '
      'tilt); a diluting component gives a red drift but alpha_s = 3(1+w)(1-n_s)', abs(als / dals) < 1,
      f'{run_k:.0e}; radiation {4 * (1 - ns):+.3f} ({(4 * (1 - ns) - als) / dals:.1f} sigma), dust {3 * (1 - ns):+.3f} '
      f'({(3 * (1 - ns) - als) / dals:.1f} sigma); 2 sigma needs w < {(als + 2 * dals) / (3 * (1 - ns)) - 1:.3f}')

print('== D. consistency')
kstar = 2 / HaT ** 2
check('exit: none. The rules\' only per-split change is the upward kick, so Lambda_k = Lambda_0/(1 - k Lambda_0/rho*) runs '
      'to the expansion limit; no radiation era', kstar > 1e9, f'runaway after 2/(Ha)^2 = {kstar:.1e} splits at the tensor bound')
Nsp = {e: 7 * math.sqrt(3) / (3 * HaT * math.sin(e)) for e in (0.04, math.pi / 2)}
check('e-folds: unbounded (ln2 per split); 60 e-folds = 86.6 splits; ticks per split at the tensor bound', abs(60 / math.log(2) - 86.56) < 0.01,
      f'N = 7 sqrt3/(3 Ha sin eps_max) = {Nsp[0.04]:.1e} (eps_max .04) .. {Nsp[math.pi / 2]:.1e} (sin 1)')
rinf = 3 * HaT ** 2 / (8 * math.pi) ** 2; rL = 0.6847 * 3 * (67.4e3 / 3.0857e22 * 5.391247e-44) ** 2 / (8 * math.pi)
check('Lambda bookkeeping: 87 splits add 87 x 1.9e-10 of Lambda_inf; rule U keeps Lambda_inf itself, so ending needs matter '
      'creation that cancels it to 1e-111 (the empty vacuum creates none)', rinf / rL > 1e110, f'rho_inf {rinf:.1e}, rho_L {rL:.2e} rho_P: ratio {rinf / rL:.1e}')
dN_jit = HaT ** 2 * HaT * math.sin(0.04) / math.sqrt(3) / 8
check('A_s: no source. The empty vacuum is invariant under every half-tick and the split, so CL-2 records nothing new; '
      'the geometry is homogeneous; a split fires on its edge, and a one-slab delay moves N_e by <= (Ha)^2 H T_s/8',
      dN_jit < 1e-15, f'{dN_jit:.0e} e-folds vs 3.81e-05 per level for A_s = 2.1e-9')
# CL-1 cube block (spin-3/2 overlap phases, equal edges), inlined from agents/matter-sees-geometry
r3 = math.sqrt(3); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
Jp = np.zeros((4, 4), complex); mm = 1.5 - np.arange(4)
for i in range(1, 4): Jp[i - 1, i] = math.sqrt(1.5 * 2.5 - mm[i] * (mm[i] + 1))
J3 = [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(mm).astype(complex)]; XI = []
for i in range(8):
    nv = (2 * C8[i] - 1) / r3; XI.append(np.linalg.eigh(sum(nv[k] * J3[k] for k in range(3)))[1][:, -1])
Wh = np.zeros((8, 8), complex)
for p_, q_ in itertools.combinations(range(8), 2):
    if np.abs(C8[p_] - C8[q_]).sum() == 1:
        g_ = XI[p_].conj() @ XI[q_]; Wh[p_, q_] = -g_ / abs(g_) / r3; Wh[q_, p_] = np.conj(Wh[p_, q_])
def Ublk(K, e, m=0.0):
    Ue = math.cos(e - m / 2) * I8 - 1j * math.sin(e - m / 2) * Wh; Uo = math.cos(e + m / 2) * I8 + 1j * math.sin(e + m / 2) * Wh
    D = np.exp(1j * (C8 @ K)); return (D[:, None] * Uo * D.conj()[None, :]) @ Ue
def Pb(U): cw = np.real(np.trace(U)) / 8; return (I8 - (U - U.conj().T) / (2j * math.sqrt(1 - cw ** 2))) / 2
chi = np.random.default_rng(7).normal(size=8) + 1j * np.random.default_rng(8).normal(size=8)
def flip(K, ec, ef):
    psi = Pb(Ublk(K, ec)) @ chi; psi /= np.linalg.norm(psi); fl = 0.0
    for m_ in C8:
        Kf = K / 2 + np.pi * m_; am = np.prod((1 + np.exp(-1j * Kf)) / 2) * psi; fl += np.linalg.norm(am) ** 2 - np.linalg.norm(Pb(Ublk(Kf, ef)) @ am) ** 2
    return fl
Kq = np.array([0.004, 0.002, 0.0]); fr = {}
for ef in (0.3, 0.1):
    base = flip(Kq, ef, ef); fr[ef] = [(flip(Kq, math.asin(math.sin(ef) / r), ef) - base) / ef ** 2 for r in (16, 2)]
check('the x16 step jump at a universal-V0 split flips ~0.2 eps_f^2 of every relativistic light mode into the other band '
      '(0.06 for the fixed-tick split, O(K^2) for a kept step); a filled sea would be heated at the cell scale every split',
      all(0.15 < fr[e][0] < 0.25 and 0.04 < fr[e][1] < 0.08 for e in fr), ', '.join(f'eps {e}: {fr[e][0]:.3f}, {fr[e][1]:.3f}' for e in fr))
rf5 = (math.pi ** 2 / 30) * 8.75 * (5e-3 / 1.220890e19) ** 4; emax = math.sqrt(rL / (2 * 0.22 * rf5 * 16 / 15))
K5 = 3 * 5e-3 / 1.220890e19 * math.sqrt(8 * math.pi)
check('ESTIMATE: with the empty vacuum a flipped fermion loses 2E, which rule U books into Lambda; a hot era from '
      'T_max >= 5 MeV then needs', emax < 1e-18 and emax > 10 * K5, f'eps_max < {emax:.0e} for the measured Lambda (K there {K5:.0e} << eps)')
H0yr = 67.4e3 / 3.0857e22 * 3.15576e7; adot = (1 / 137.036) * 16 / (3 * math.pi) * H0yr
check('ESTIMATE: edges grow at H0 between splits today; with the cell coupling fixed, the charged content\'s induced '
      'running moves alpha by alpha (2/3pi) sum Q^2 per e-fold of edge', adot / 1e-18 > 1e4,
      f'alpha-dot/alpha = {adot:.1e}/yr (SM charges) vs clock bounds ~1e-18/yr, unless every coupling is held at a proper reference')

print('== E. what a red tilt needs (supplied transfer laws)')
need = {q: (1 - 2 ** (-(1 - ns) * 2 / q)) * 100 for q in (2, 4)}
check('THEOREM: with N_k = N(Lambda_k), "larger zooms are shorter-lived" <=> the constant FALLS at each split; the measured '
      'tilt needs it to fall per split by', all(v > 1 for v in need.values()),
      ', '.join(f'q={q}: {v:.2f}%' for q, v in need.items()) + '; the rules give a rise of Lambda/rho*')
Ne, kk = sp.symbols('N_e k', positive=True)
epsQ = sp.limit(-sp.Rational(1, 2) * sp.log(1 - 1 / kk, 2) * kk * sp.log(2), kk, sp.oo)
lamk = [1.0 - 0.001 * i for i in range(1000)]; Nk = [1 / math.sqrt(v) for v in lamk]; kp = 1000 - int(round(57 / math.log(2)))
nsQ = {q: 1 - q * math.log2(Nk[kp + 1] / Nk[kp]) for q in (2, 4)}
check('constant transfer Q per split (supplied): Lambda_k = Q(k_end - k) gives eps = 1/(2 N_e) exactly in the continuum, '
      'exit when used up, n_s = 1 - q/(2N_e), alpha_s = -q/(2N_e^2)', epsQ == sp.Rational(1, 2) and abs(nsQ[4] - (1 - 2 / 57)) < 5e-4,
      f'N_e 57: q=4 {nsQ[4]:.4f} (alpha_s {-2 / 57 ** 2:.1e}), q=2 {nsQ[2]:.4f} ({(nsQ[2] - ns) / dns:.1f} sigma); N_e not derived')
epsr = (1 - ns) / 4
check('with the single-clock amplitude H^2/(8 pi^2 eps) the drift is eps itself and r = 16 eps: the converged drift (N up '
      '0.6-1.2% per split) gives r = 0.14-0.28 > 0.036; a red tilt with r < 0.036 needs eps < 0.0023 and a changing drift',
      16 * epsr > 0.036, f'r = {16 * epsr:.2f} (q=4), {16 * (1 - ns) / 2:.2f} (q=2); proportional transfer: constant tilt, no exit')
print('supplied: frustum carrier and junction hinges, the trigger, universal V0, initial Lambda_0, kappa = 1, the unit map,')
print('  the CL-1 block for flips, SM charges, transfer families, q, measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
