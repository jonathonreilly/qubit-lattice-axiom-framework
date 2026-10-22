#!/usr/bin/env python3
"""Can a rule fix the size of the cosmological constant? (supplied models; finite diagnostics; no physical identification)
 A  candidate (a), rule U: geometry varied at fixed 4-volume per record, on the cubic-frustum Regge FRW carrier of
    agents/cosmology (edge l_n, central tick T_n): the vacuum cancels exactly; the integration constant is conserved, set
    by the first slab, moved by matter non-conservation, and kicked by every 2^3 split junction
 B  candidate (b), per-new-cell phase conjugate to the cell count: mean + fluctuation, Fano factor of split-phase record
    counts, Sorkin-type estimates in both readings, tracking against BBN
 C  candidate (c), self-tuning through the split trigger: steady split rate, local self-tuning laws, fixed points,
    junction self-tuning in the standard theory
 D  other routes: split non-adiabaticity of the CL-2 corner-preserving split under rule U; frozen-sea area-law noise;
    the de Sitter capacity identity
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
import numpy as np
from scipy.linalg import schur
from scipy.optimize import brentq
np.seterr(all='ignore')
T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- measured numbers and the unit map of the earlier probes (a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c))
hbar, cl, Gn = 1.054571817e-34, 2.99792458e8, 6.67430e-11; lP = np.sqrt(hbar * Gn / cl ** 3); tP = lP / cl
MP = 1.220890e19; GeVs = 6.582119569e-25                       # Planck mass in GeV; hbar in GeV s
H0 = 67.4e3 / 3.0857e22; OL, Om, Or = 0.6847, 0.315, 9.2e-5
rL = OL * 3 * (H0 * tP) ** 2 / (8 * np.pi)                      # rho_Lambda / rho_P
rL_GeV = rL * MP ** 4
a_P, tau_P = np.sqrt(8 * np.pi), 2 * np.sqrt(8 * np.pi) / np.sqrt(3)   # site spacing and tick in Planck units
phiL = rL * a_P ** 3 * tau_P                                     # needed vacuum phase per site per tick
rho_star = 3 / (4 * np.pi * a_P ** 2)                            # lattice maximal density 3/(4 pi G a^2), in rho_P

# ---------------- A. rule U on the frustum Regge carrier (kappa = 1/(8 pi G) = 1 per rung cell)
def Af(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def fv(a, b): return (a + b) * (a * a + b * b) / 4                 # slab 4-volume per unit central tick
def dfa(a, b): return ((a * a + b * b) + (a + b) * 2 * a) / 4
def dfb(a, b): return ((a * a + b * b) + (a + b) * 2 * b) / 4
def Er(a, b, C): return C / (0.5 * (a + b))                        # radiation energy per cell
def dEr(a, b, C): return -C / (2 * (0.5 * (a + b)) ** 2)
def Kslab(a, b, T, C, rv): return 6 * (a + b) * Af((b - a) / (2 * T)) - Er(a, b, C) - rv * fv(a, b)   # dS/dT_n
def dSdl(lm, l0, lp, Tm, T_, Cm, C0, rv):                            # dS/dl_n at fixed ticks (Schlaefli-reduced)
    um, u0 = (l0 - lm) / (2 * Tm), (lp - l0) / (2 * T_); sm, s0 = lm + l0, l0 + lp
    out = 12 * l0 * (np.arctanh(u0) - np.arctanh(um))
    out += (1.5 * Tm * np.sqrt(1 - 2 * um * um) - 1.5 * sm * um / np.sqrt(1 - 2 * um * um)) * 4 * np.arcsin(um * um / (1 - um * um))
    out += (1.5 * T_ * np.sqrt(1 - 2 * u0 * u0) + 1.5 * s0 * u0 / np.sqrt(1 - 2 * u0 * u0)) * 4 * np.arcsin(u0 * u0 / (1 - u0 * u0))
    return out - dEr(lm, l0, Cm) * Tm - dEr(l0, lp, C0) * T_ - rv * (Tm * dfb(lm, l0) + T_ * dfa(l0, lp))
def reference(C, L0, c, lend):                                     # standard theory with vacuum L0, relative step c
    ls, Ts = [1.0], []; up = np.sqrt((C + L0) / 3) / 2
    while ls[-1] < lend:
        l = ls[-1]; T = c * l / (2 * up)
        u = brentq(lambda u: Er(l, l + 2 * u * T, C) + L0 * fv(l, l + 2 * u * T) - 6 * (2 * l + 2 * u * T) * Af(u), 1e-300, (1 - 1e-12) / np.sqrt(2), xtol=1e-300, rtol=1e-15)
        ls.append(l + 2 * u * T); Ts.append(T); up = u
    return np.array(ls), np.array(Ts)
def Gu(n, lm, l0, lp, Tm, V, Cs, rv):                               # rule-U equation dS/dl_n|_V
    T_ = V[n] / fv(l0, lp)
    return (dSdl(lm, l0, lp, Tm, T_, Cs[n - 1], Cs[n], rv) - Tm * dfb(lm, l0) / fv(lm, l0) * Kslab(lm, l0, Tm, Cs[n - 1], rv)
            - T_ * dfa(l0, lp) / fv(l0, lp) * Kslab(l0, lp, T_, Cs[n], rv))
def unimodular(lr, Tr, Cs, rv=0.0, l1=None):
    V = Tr * fv(lr[:-1], lr[1:]); ls = [lr[0], lr[1] if l1 is None else l1]; Ts = [V[0] / fv(ls[0], ls[1])]
    for n in range(1, len(V)):
        g = ls[-1] - ls[-2]; lo, hi = ls[n] + 0.5 * g, ls[n] + 1.5 * g
        f = lambda lp: Gu(n, ls[n - 1], ls[n], lp, Ts[n - 1], V, Cs, rv)
        for _ in range(40):
            if f(lo) * f(hi) < 0: break
            lo, hi = ls[n] + (lo - ls[n]) * 0.7, ls[n] + (hi - ls[n]) * 1.3
        lp = brentq(f, lo, hi, xtol=1e-15, rtol=1e-15); ls.append(lp); Ts.append(V[n] / fv(ls[n], lp))
    ls, Ts = np.array(ls), np.array(Ts)
    Lam = np.array([Kslab(ls[n], ls[n + 1], Ts[n], Cs[n], 0.0) / fv(ls[n], ls[n + 1]) for n in range(len(Ts))])
    return ls, Ts, Lam
mean2 = lambda x: 0.5 * (x[1:] + x[:-1])

print('== A. candidate (a): rule U on the frustum Regge FRW carrier (radiation + Lambda0; kappa = 1)')
C, leq = 1e-4, 10.0; L0 = C / leq ** 4
lr, Tr = reference(C, L0, 0.01, 30.0); V = Tr * fv(lr[:-1], lr[1:]); n = 50
dG = [abs(Gu(n, lr[n - 1], lr[n], lr[n + 1], Tr[n - 1], V, np.full(len(Tr), C), X) - Gu(n, lr[n - 1], lr[n], lr[n + 1], Tr[n - 1], V, np.full(len(Tr), C), 0.0))
      / (X * Tr[n - 1] * dfb(lr[n - 1], lr[n])) for X in (1.0, 1e3)]
check('THEOREM: under rule U every vacuum term -rho_v V cancels identically from the edge equation (fixed V_n: d(rho_v V)=0)',
      max(dG) < 1e-14, f'|Delta G|/(vacuum term) {max(dG):.0e} at rho_v = 1e4..1e7 Lambda0')
runs = {}
for c in (0.02, 0.01, 0.005):
    lr, Tr = reference(C, L0, c, 100.0); lu, Tu, Lam = unimodular(lr, Tr, np.full(len(Tr), C)); Lb = mean2(Lam)
    uu = (lu[1:] - lu[:-1]) / (2 * Tu); rc = 3 * (2 * uu / (0.5 * (lu[1:] + lu[:-1]))) ** 2
    runs[c] = (np.max(abs(Lb - L0) / mean2(rc)) / c ** 2, Lb[-1] / L0 - 1, (rc[-1] - C / (0.5 * (lu[-1] + lu[-2])) ** 4) / Lb[-1],
               np.abs(0.5 * (Lam[1:] - Lam[:-1])).max() / L0, lr, Tr)
k2 = [runs[c][0] for c in runs]
check('rule U conserves its constant with no secular drift: |Lbar_n - Lambda0| <= 4.2 c^2 rho_c(n) at every slab, though '
      'rho_c starts at 1e4 Lambda0; zigzag ~ c^3', max(k2) < 4.5 and max(k2) / min(k2) < 1.1 and runs[0.005][3] < runs[0.02][3] / 30,
      'max/c^2 ' + ', '.join(f'{k:.2f}' for k in k2) + '; end offset ' + ', '.join(f'{runs[c][1]:.0e}' for c in runs) + f' (c = .02, .01, .005); zigzag {runs[0.02][3]:.0e} -> {runs[0.005][3]:.0e}')
check('late expansion obeys Friedmann with the conserved constant: (3H^2 - rho_r)/Lbar -> 1 (w = -1 exactly)',
      all(abs(runs[c][2] - 1) < 3e-4 for c in runs), ', '.join(f'{runs[c][2]:.5f}' for c in runs))
lr, Tr = runs[0.01][4], runs[0.01][5]; fix = []
for e in (1e-9, 1e-7):
    l1 = lr[1] * (1 + e); lu, Tu, Lam = unimodular(lr, Tr, np.full(len(Tr), C), l1=l1)
    fix.append((e, Kslab(lr[0], l1, Tr[0] * fv(lr[0], lr[1]) / fv(lr[0], l1), C, 0.0) / fv(lr[0], l1) / L0, mean2(Lam)[-1] / L0))
check('what fixes it: only the first slab\'s mismatch; a 1e-7 change of l_1 moves Lambda by 20%, so nothing in the rules sets it', all(abs(b / a - 1) < 2e-3 for _, a, b in fix),
      '; '.join(f'dl1/l1 {e:.0e}: first slab {a:.4f}, late {b:.4f} Lambda0' for e, a, b in fix))
jr = []
for c in (0.02, 0.01, 0.005):
    lr, Tr = runs[c][4], runs[c][5]; N = len(Tr); nd = N // 4; Cs = np.where(np.arange(N) < nd, C, C * 0.99)
    lu, Tu, Lam = unimodular(lr, Tr, Cs); Lb = mean2(Lam)
    d1 = 0.01 * C / (0.5 * (lu[nd] + lu[nd + 1])) / fv(lu[nd], lu[nd + 1]); d0 = 0.01 * C / (0.5 * (lu[nd - 1] + lu[nd])) / fv(lu[nd - 1], lu[nd])
    jr.append(((Lb[nd + 4] - Lb[nd - 4]) / np.sqrt(d0 * d1), abs(Lb[-1] / Lb[nd + 4] - 1) / c ** 2))
check('matter non-conservation becomes Lambda: radiation losing 1% at one slab raises Lbar by the lost density, '
      'permanently (discrete Lambda = Lambda0 + int Q dt)', abs(jr[-1][0] - 1) < 1e-4 and jr[0][0] > jr[1][0] > jr[2][0] > 1
      and max(j[1] for j in jr) < 4, 'jump/lost ' + ', '.join(f'{j[0]:.5f}' for j in jr) + f' (c = 0.02, 0.01, 0.005); later drift <= {max(j[1] for j in jr):.2f} c^2')

def split_run(Cd, Lv, step, unimod, nafter=40):
    """dust Cd per coarse cell (Cd/8 per fine), vacuum Lv; one 2^3 split at edge 2 (agents/cosmology remesh carrier)"""
    ls, Ts, mesh = [1.0], [], []; u = np.sqrt((Cd + Lv) / 3) / 2; mc = 0; r = None
    while True:
        if mc == 0 and ls[-1] >= 2.0: r = len(ls) - 1; mc = 1; ls[-1] /= 2
        l = ls[-1]; T = step * l / (2 * u); Em = Cd / 8 ** mc
        uu = brentq(lambda x: Em + Lv * fv(l, l + 2 * x * T) - 6 * (2 * l + 2 * x * T) * Af(x), 1e-300, (1 - 1e-15) / np.sqrt(2), xtol=1e-300, rtol=1e-15)
        ls.append(l + 2 * uu * T); Ts.append(T); mesh.append(mc); u = uu
        if mc == 1 and len(ls) - r > nafter: break
    ls, Ts, mesh = np.array(ls), np.array(Ts), np.array(mesh); M = len(Ts)
    def edges(k, lv): return lv[k], (2 * lv[k + 1] if (mesh[k] == 0 and k + 1 == r) else lv[k + 1])
    Vv = np.array([Ts[k] * fv(*edges(k, ls)) for k in range(M)])
    def slabterm(k, lv, Tk, rv):
        la, lb = edges(k, lv); T = Tk(k, la, lb); uk = (lb - la) / (2 * T); w = 8 ** mesh[k]
        return w * (6 * (la + lb) * T * np.sqrt(1 - 2 * uk * uk) * np.arcsin(uk * uk / (1 - uk * uk)) - Cd / w * T - rv * T * fv(la, lb)), uk
    def hinge(k, ua, ub, lv):
        return (8 ** mesh[k] * 6 * lv[k] ** 2 * (np.arctanh(ub) - np.arctanh(ua)) if mesh[k - 1] == mesh[k] else 6 * (2 * lv[k]) ** 2 * (2 * np.arctanh(ub) - np.arctanh(ua)))
    if not unimod:                                                  # standard theory: signed junction residual of dS/dl_r
        def act(lv, rv):
            S = 0.0; us = []
            for k in range(M):
                s_, uk = slabterm(k, lv, lambda k, la, lb: Ts[k], rv); S += s_; us.append(uk)
            return S + sum(hinge(k, us[k - 1], us[k], lv) for k in range(1, M))
        h = 1e-6 * ls[r]; lp_, lm_ = ls.copy(), ls.copy(); lp_[r] += h; lm_[r] -= h
        return (act(lp_, Lv) - act(lm_, Lv)) / (2 * h) / (6 * (2 * ls[r]) ** 2 * np.arctanh((ls[r + 1] - ls[r]) / (2 * Ts[r]))), 2 * (ls[r + 1] - ls[r]) / (2 * Ts[r])
    TU = lambda k, la, lb: Vv[k] / fv(la, lb)
    def localS(k, lv):
        Sm, um = slabterm(k - 1, lv, TU, 0.0); S0, u0 = slabterm(k, lv, TU, 0.0); out = Sm + S0 + hinge(k, um, u0, lv)
        if k - 1 == 0: out += 6 * lv[0] ** 2 * np.arctanh(um)          # boundary term at the first slice
        if k - 1 >= 1: out += (8 ** mesh[k - 1] * 6 * lv[k - 1] ** 2 * np.arctanh(um) if mesh[k - 2] == mesh[k - 1] else 6 * (2 * lv[k - 1]) ** 2 * 2 * np.arctanh(um))
        if k + 1 <= M - 1: out += (-8 ** mesh[k + 1] * 6 * lv[k + 1] ** 2 * np.arctanh(u0) if mesh[k] == mesh[k + 1] else -6 * (2 * lv[k + 1]) ** 2 * np.arctanh(u0))
        return out
    lu = ls.copy()
    for k in range(1, M - 1):
        def G(lp):
            lv = lu.copy(); lv[k + 1] = lp; h = 1e-7 * lv[k]; p_, q_ = lv.copy(), lv.copy(); p_[k] += h; q_[k] -= h
            return (localS(k, p_) - localS(k, q_)) / (2 * h)
        wd = 0.3 * step * ls[k + 1]
        for _ in range(30):
            if G(ls[k + 1] - wd) * G(ls[k + 1] + wd) < 0: break
            wd *= 1.5
        lu[k + 1] = brentq(G, ls[k + 1] - wd, ls[k + 1] + wd, xtol=1e-15, rtol=1e-14)
    Lam = []
    for k in range(M - 1):
        la, lb = edges(k, lu); T = Vv[k] / fv(la, lb); Lam.append((6 * (la + lb) * Af((lb - la) / (2 * T)) - Cd / 8 ** mesh[k]) / fv(la, lb))
    Lb = mean2(np.array(Lam)); return Lb[r + 4:r + 30].mean() - Lb[r - 12:r - 4].mean(), (Cd / 8 / lu[r] ** 3 + Lv) ** 2 * lu[r] ** 2 / 6
kick = [split_run(Cd, Lv, st, True) for Cd, Lv, st in ((0.05, 1e-9, 0.004), (0.05, 0.005, 0.004), (0.05, 0.005, 0.002), (0.0125, 0.00125, 0.004), (0.1, 0.0, 0.004))]
check('rule U turns the split junction (residual O((Hl)^2), agents/cosmology) into a permanent kick: each synchronous 2^3 '
      'split (dust) adds rho^2/rho* to Lambda, rho* = 3/(4 pi G a^2); step-independent', all(abs(s / p - 1) < 0.01 for s, p in kick)
      and abs(kick[1][0] / kick[2][0] - 1) < 0.01, 'kick/(rho^2/rho*) ' + ', '.join(f'{s / p:.4f}' for s, p in kick))
Tfirst = (np.sqrt(rL * rho_star) * MP ** 4 / (np.pi ** 2 / 30 * 106.75)) ** 0.25
Hinf = np.log(2) / (539 * tau_P); rinf = 3 * Hinf ** 2 / (8 * np.pi); over = (60 / np.log(2)) * rinf ** 2 / rho_star / rL
check('ESTIMATE: under rule U Lambda = Lambda0 + sum rho_s^2/rho* (positive, frozen once rho falls); measured needs the '
      'first rule-U split at T ~ 1 TeV; a Planck start or the cosmology probe\'s inflation overshoots',
      500 < Tfirst < 3000 and over > 1e100, f'first split at T = {Tfirst:.0f} GeV (g* 106.75); 60 e-folds at 539 ticks/split: {over:.0e} x measured')

print('== B. candidate (b): per-new-cell phase conjugate to the cell count')
Ns = np.array([1e2, 1e3, 1e4, 1e5]).astype(int); m_, s_ = 0.3, 1.0; reps = 400
dev = np.array([np.std([rng.normal(m_, s_, k).mean() for _ in range(reps)]) for k in Ns])
check('EXACT (CLT): per-new-cell phases (mean m, sd s) give m/v + s/(v sqrt N): a w = -1 constant of unfixed size m plus '
      'a zero-mean 1/sqrt(N) ~ H^2 term', abs(np.polyfit(np.log(Ns), np.log(dev), 1)[0] + 0.5) < 0.05,
      f'slope {np.polyfit(np.log(Ns), np.log(dev), 1)[0]:.3f}; mean {np.mean([rng.normal(m_, s_, 10 ** 5).mean() for _ in range(5)]):.4f} vs m = {m_}')
Fs = []
for Nc in (100, 1000, 10000):
    ph = rng.random(200000); cnt = Nc * (16 * ph + 256 * (1 - ph)); Fs.append(cnt.var() / cnt.mean() / Nc)
Nnow = np.log(2) / (H0 * tau_P * tP); Fnow = 4800 / 136 * Nnow
check('split-phase noise (independent phases; 8 sites -> 64 at double tick rate) has Fano factor F = 35.3 x ticks per split, '
      'not 1: today F ~ 4e61', all(abs(f - 4800 / 136) < 0.5 for f in Fs), 'F/N_c ' + ', '.join(f'{f:.2f}' for f in Fs) + f' (analytic 35.29); N_c now {Nnow:.1e}')
la = np.linspace(np.log(1e-13), 0, 40001); aa = np.exp(la); Ha = np.sqrt(Or / aa ** 4 + Om / aa ** 3 + OL)
eta = np.concatenate([[0], np.cumsum(0.5 * np.diff(la) * (1 / (aa[1:] * Ha[1:]) + 1 / (aa[:-1] * Ha[:-1])))]) + aa[0] / np.sqrt(Or)
def Vcone(i): e = eta[:i + 1]; return 4 * np.pi / 3 * np.trapezoid(aa[:i + 1] ** 4 * (eta[i] - e) ** 3, e)
v0 = a_P ** 3 * tau_P / 2; toP = 1 / (H0 * tP) ** 4                # one record per site per half-tick (CL-3)
V0 = Vcone(len(aa) - 1) * toP; poi = 1 / np.sqrt(v0 * V0); zeta = np.sqrt(2.1e-9)
est = {'Poisson F=1': poi, 'split noise (U)': poi / np.sqrt(Fnow), 'split noise (C)': poi * np.sqrt(Fnow), 'correlated (U)': 1 / (zeta * V0), 'correlated (C)': zeta / v0}
check('ESTIMATES (Sorkin conjugacy, readings U and C): only Poisson counting lands near measured; split noise is 1e+-31 off, '
      'correlated noise 1e+-116; deterministic splits give no value',
      0.1 < poi / rL < 10 and all(abs(np.log10(v / rL)) > 25 for k, v in est.items() if k != 'Poisson F=1'),
      ', '.join(f'{k} {v / rL:.0e}' for k, v in est.items()))
sd = {}
for z in (4e8, 1090, 0):
    i = int(np.argmin(abs(aa - 1 / (1 + z)))); rc = 3 * (Ha[i] * H0 * tP) ** 2 / (8 * np.pi); sd[z] = 1 / np.sqrt(v0 * Vcone(i) * toP) / rc
check('the Poisson version tracks: sd of Omega_L is O(1) at BBN, recombination and today, against |Omega_L(BBN)| < 0.05 '
      '(Delta N_eff < 0.3) and early dark energy < 2%', min(sd.values()) > 0.05, ', '.join(f'z={z:g}: {v:.2f}' for z, v in sd.items()))

print('== C. candidate (c): self-tuning through the split trigger')
HBBN = 1.66 * np.sqrt(10.75) * (1e-3) ** 2 / MP / GeVs; HL = H0 * np.sqrt(OL)
check('a steady split rate is a constant H (de Sitter at every epoch): at T = 1 MeV the expansion would be too slow by '
      f'{HBBN / HL:.1e}; BBN fixes H to ~10%', HBBN / HL > 1e17)
Hr = lambda A: np.sqrt(Or / A ** 4 + Om / A ** 3 + OL); R = np.arange(0, 140); Aseq = 2.0 ** (R - 139); HR = Hr(Aseq)
out = {}
for lam in (0.0, 1.0):
    eps_ = np.zeros(len(R))
    for k in range(1, len(R)): eps_[k] = lam * eps_[k - 1] + HR[k - 1] ** 2
    kap = OL / (eps_[-1] / HR[-1] ** 2); ib = int(np.argmin(abs(Aseq - 1 / 4e8))); out[lam] = (kap * eps_[ib] / HR[ib] ** 2, eps_[-1] / eps_[1])
check('local self-tuning eps_new = lam eps_parent + k (H tau)^2: lam < 1/16 tracks (Omega at BBN >= today), lam = 1 freezes '
      'the first split\'s value; no lam gives "only today"',
      out[0.0][0] > 0.05 and abs(out[1.0][1] - 16 / 15) < 0.01, f'lam=0: Omega_eps(BBN) {out[0.0][0]:.2f}; lam=1: eps_now/eps_first {out[1.0][1]:.4f}')
xL = HL * tau_P * tP; xs = [(0.385 * al) ** (1 / (2 - p)) for p in (0, 1, 3, 4) for al in (1e-2, 1e2)]
check('de Sitter fixed points x^2 = 0.385 F(x) (x = H tau) for F = alpha x^p, alpha in [1e-2, 1e2]: x* = O(1e-3..1e3); '
      'the measured x needs alpha = 8.3e-121 by hand', min(xs) > 1e-3 and max(xs) < 1e3,
      f'x* in [{min(xs):.1e}, {max(xs):.1e}]; measured {xL:.1e} -> alpha = {xL ** 2 / 0.385:.1e}')
jt = []
for Cd in (0.2, 0.05, 0.0125):
    r0, Hl = split_run(Cd, 0.0, 0.004, False); sl = (split_run(Cd, 1e-3 * Cd, 0.004, False)[0] - split_run(Cd, -1e-3 * Cd, 0.004, False)[0]) / (2e-3 * Cd)
    jt.append((Hl, -r0 / sl / (3 * Hl ** 2)))
check('junction self-tuning (standard theory): cancelling the split\'s O((Hl)^2) residual with a vacuum term needs '
      'rho_v = -rho_c at every H: no small positive constant', all(abs(j[1] + 1) < 0.05 for j in jt),
      ', '.join(f'Hl {h:.3f}: rho_v/rho_c {v:+.3f}' for h, v in jt))

print('== D. other routes')
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); OPP = 7 - np.arange(8)
def coherent(j, nv):
    th, ph, d = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]; W0 = np.zeros((8, 8), complex)
for s1, t1 in itertools.product(range(8), repeat=2):
    if abs(CORN[s1] - CORN[t1]).sum() == 1: g_ = XI[s1].conj() @ XI[t1]; W0[s1, t1] = -g_ / abs(g_) / np.sqrt(3)
def Wa(x): return np.cos(x) * W0 + 1j * np.sin(x) * np.eye(8)
def half(psi, Wm, odd):
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    b_ = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8) @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T
    p = b_.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p
def blocks(mu, b, L=8):
    We, Wo = Wa(mu / 2 + b), Wa(mu / 2 - b); N = L ** 3; E = np.eye(N).reshape(N, L, L, L)
    Ue, Uo = [np.stack([half(e, Wm, od).ravel() for e in E], 1) for Wm, od in ((We, 0), (Wo, 1))]; U = Uo @ Ue
    s = lambda v: np.ravel_multi_index(tuple(np.asarray(v) % L), (L, L, L)); n0 = np.array([1, 1, 1])
    return {Rr: np.array([[U[s(2 * (n0 + Rr) + CORN[x]), s(2 * n0 + CORN[y])] for y in range(8)] for x in range(8)]) for Rr in itertools.product((-1, 0, 1), repeat=3)}
def eigK(BL, K):
    T, Z = schur(sum(M * np.exp(-1j * (np.asarray(K, float) @ np.array(Rr, float))) for Rr, M in BL.items()), output='complex')
    return -np.angle(np.diag(T)), Z
def loss(BL, Kc):                                                    # 1 - E_after/E_before, positive bands, corner split
    omc, Qc = eigK(BL, Kc); out = []
    for j in np.where(omc > 0)[0]:
        es = ez = 0.0
        for m in CORN:
            Kf = Kc / 2 + np.pi * m; amp = np.prod((1 + np.exp(-1j * Kf)) / 2) * Qc[:, j]; omf, Qf = eigK(BL, Kf); e = (np.abs(Qf.conj().T @ amp) ** 2 * omf).sum()
            if m.sum() == 0: es += e
            else: ez += e
        out.append((1 - 2 * (es + ez) / omc[j], 1 - 2 * es / omc[j]))
    return np.array(out).mean(0)
dirs = [np.array([1, 0, 0.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, 2, 3.]) / np.sqrt(14)] + [v / np.linalg.norm(v) for v in rng.standard_normal((3, 3))]
cnet = {}
for b in (0.3, 1.2, 1.53):
    BL = blocks(0.0, b); r_ = np.array([loss(BL, 0.05 * d) for d in dirs]) / 0.05 ** 2; cnet[b] = (r_[:, 0].mean(), r_[:, 0].std(), r_[:, 1].mean())
check('corner-preserving split, massless CL-2 light states: energy changes by -c(eps) K^2 E per split (smooth part loses '
      'K^2/16, zone-edge part returns most); c -> 0.0275 eps^2',
      all(abs(v[2] - 1 / 16) < 1e-4 and v[1] < 1e-2 * v[0] for v in cnet.values()) and cnet[0.3][0] > cnet[1.2][0] > cnet[1.53][0] > 0,
      ', '.join(f'eps {np.pi / 2 - b:.3f}: c {v[0]:.3e} (c/eps^2 {v[0] / (np.pi / 2 - b) ** 2:.4f})' for b, v in cnet.items()))
gE = 2 + (4 + 6) * 31 / 32; co = 16 * 8 * np.pi * (120 * 1.0173430620 / (2 * np.pi ** 2) / 6) / np.log(2)
Tmax = {b: (rL_GeV * MP ** 2 / (co * cnet[b][0] * gE)) ** (1 / 6) for b in (0.3, 1.53)}
Tg = 2.348e-13; dlnr = 16 * cnet[0.3][0] * 8 * np.pi / MP ** 2 / np.log(2) * (6.18 * (2 * Tg ** 6 + 6 * 31 / 32 * (0.714 * Tg) ** 6)) / rL_GeV
check('ESTIMATE, rule U + this split (empty vacuum, thermal plasma from T_max, K = 4aE at the split): rho_L = '
      f'{co:.0f} c g T_max^6/M_P^2; measured needs T_max = {1e3 * Tmax[0.3]:.0f} MeV (eps 1.27) to {1e3 * Tmax[1.53]:.0f} MeV (eps 0.04)',
      5e-3 < Tmax[0.3] < Tmax[1.53] < 0.1 and dlnr < 1e-60, f'BBN floor ~5 MeV; w + 1 today {-dlnr / 3:.0e}; a Planck-hot start gives ~rho_P')
Lb_ = 16; ks = 2 * np.pi * np.arange(Lb_) / Lb_; P = np.zeros((Lb_, Lb_, Lb_, 8, 8), complex); We, Wo = Wa(0.2 + 0.3), Wa(0.2 - 0.3)
for i, j, k in itertools.product(range(Lb_), repeat=3):
    Dk = np.exp(1j * (CORN @ np.array([ks[i], ks[j], ks[k]]))); w_, Vv = np.linalg.eig((Dk[:, None] * Wo * Dk.conj()[None, :]) @ We)
    Q, _ = np.linalg.qr(Vv[:, -np.angle(w_) < 0]); P[i, j, k] = Q @ Q.conj().T
C0 = np.fft.ifftn(P, axes=(0, 1, 2)); FA = np.fft.fftn(abs(C0) ** 2, axes=(0, 1, 2)); dg = np.real(np.diagonal(C0[0, 0, 0]))
def var_w(w): Fw = np.fft.fftn(w, axes=(0, 1, 2)); return np.sum(w ** 2 * dg) - np.real(np.einsum('ijka,ijkab,ijkb->', Fw.conj(), FA, Fw)) / Lb_ ** 3
nn = np.stack(np.meshgrid(*[np.arange(Lb_)] * 3, indexing='ij'), -1); X3 = 2 * nn[:, :, :, None, :] + CORN[None, None, None]
r2 = (((X3 - (Lb_ - 0.5) + Lb_) % (2 * Lb_) - Lb_) ** 2).sum(-1)
sh = [var_w(np.all(X3 < l, -1).astype(float)) / l ** 2 for l in (6, 10)]; gv = [(s, var_w(np.exp(-r2 / (2 * s * s)))) for s in (2.0, 2.5, 3.0, 3.5)]
exg = np.polyfit(np.log([g[0] for g in gv]), np.log([g[1] for g in gv]), 1)[0]
RH = cl / H0 / (a_P * lP); est_sh = (np.pi / 2) * np.sqrt(1.047) * RH / (4 * np.pi / 3 * RH ** 3) / phiL, (np.pi / 2) * np.sqrt(0.5) * RH / RH ** 3 / phiL
est_sm = (np.pi / 2) * np.sqrt(gv[-1][1] / gv[-1][0] * RH) / ((2 * np.pi) ** 1.5 * RH ** 3) / phiL
u1 = hbar / ((a_P * lP) ** 3 * tau_P * tP) / cl ** 2; Lm = 1 / (a_P * lP)
loc = (np.pi / 2) * np.sqrt(0.5) / Lm ** 2 * u1, (np.pi / 2) * np.sqrt(gv[-1][1] / gv[-1][0] * Lm) / ((2 * np.pi) ** 1.5 * Lm ** 3) * u1
check('frozen sea (mu .4, b .3): number variance area-law in sharp cubes, ~sigma in smooth windows; a sharp Hubble '
      'window gives the holographic size, but it tracks and the same noise on 1 m is huge',
      all(abs(s - 0.5) < 0.01 for s in sh) and 0.9 < exg < 1.25 and 0.05 < min(est_sh) and max(est_sh) < 1 and est_sm < 1e-25 and min(loc) > 1e5,
      f'Var/l^2 {sh[0]:.3f}, {sh[1]:.3f}; smooth exponent {exg:.2f}; Hubble: sharp {est_sh[0]:.2f}-{est_sh[1]:.2f}, smooth {est_sm:.0e} x measured; 1 m: {loc[0]:.0e}, {loc[1]:.0e} kg/m^3')
S_dS = np.pi / (HL * tP) ** 2
check('IDENTITY: rho_L/rho_P = 3/(8 S_dS), S_dS = pi/(H_L l_P)^2: a capacity rule needs 2^407.5 qubits per horizon by hand',
      abs(3 / (8 * S_dS) / rL - 1) < 1e-12, f'S_dS {S_dS:.2e} = 2^{np.log2(S_dS / np.log(2)):.1f} ln2')
print('== E. against measurement (w = -1.03 +- 0.03; Omega_L(BBN) < 0.05; EDE(rec) < 0.02; rho_L = %.2e rho_P)' % rL)
print('  (a) U: w = -1 once dense splits stop, BBN/CMB fine, size = Lambda0 + sum rho_s^2/rho* + int Q (history, not rules)')
print('  (b) tracks or 1e+-31 off  (c) tracks, freezes the start, or needs 8e-121 by hand  (d) U + losses: T_max 16-48 MeV;')
print('  sea noise: tracks + local noise; capacity: restates')
print('supplied: frustum carrier, central tick, matter -E T, kappa = 1, rule U itself, split construction and threshold, the CL-2 tick')
print('  at mu, b; empty vacuum and thermal plasma (D), split-phase independence, self-tuning families, unit map, LCDM, measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
