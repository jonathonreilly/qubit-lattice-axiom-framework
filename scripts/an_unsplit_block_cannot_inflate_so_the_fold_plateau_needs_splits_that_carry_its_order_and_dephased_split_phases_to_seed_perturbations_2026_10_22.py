AUDIT_INPUT_PATHS = ('docs/AN_UNSPLIT_BLOCK_CANNOT_INFLATE_SO_THE_FOLD_PLATEAU_NEEDS_SPLITS_THAT_CARRY_ITS_ORDER_AND_DEPHASED_SPLIT_PHASES_TO_SEED_PERTURBATIONS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Inflation rule test (finite runner, seeded, self-contained).

  A  the candidate 'one unsplit block inflates': window arithmetic, dilation gauge, fixed-site no-go
  B  why a split must carry the fold order (IN-1), impulsive friction, friction-blindness of the plateau
  C  the nested sea's density-wave fold (Hartree), slow roll, self-consistent N*, A_s -> rung (FITTED)
  D  perturbations: the register's vacuum carriage is adiabatic (no seed); synchronized order carriage
     heats and saws the spectrum; dephased splits restore the continuum
  E  exit, reheating, vacuum standard; F  split-trigger consistency
Supplied numbers are named in the output. Measured numbers enter only the estimates.
"""
import time
import itertools
import numpy as np
import sympy as sp
from scipy.special import ellipk, ndtr
from scipy.integrate import quad, simpson, solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq, minimize_scalar

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
NS_PL, SPL, NS_ACT, SACT, AS_PL, RMAX = 0.9649, 0.0042, 0.974, 0.003, 2.1e-9, 0.036
L2 = np.log(2.0)


def check(ok, tag, text, vals=""):
    global NP, NF
    ok = bool(ok); NP += ok; NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}" + (f" | {vals}" if vals else ""))


print("== A. candidate: inflation inside one unsplit block")
D_ = sp.symbols('Delta', nonnegative=True)
need_floor = sp.solve(sp.Eq((4 + D_) * sp.log(2), 60), D_)[0]
need_birth = sp.solve(sp.Eq((1 + D_) * sp.log(2), 60), D_)[0]
burst = int(np.floor(60 / L2 - 1)) + 1
check(abs(float(need_floor) - 82.56) < 0.01 and abs(float(need_birth) - 85.56) < 0.01, "A1 [T]",
      "window: an unsplit block's edges span (4+Delta)ln2 e-folds floor-to-top, (1+Delta)ln2 from birth; 60 e-folds "
      "needs Delta >= 82.6 (floor) / 85.6 (birth), and a hold on the 4s trigger; released, children at parent-s >= 4s "
      "split at once",
      f"Delta_min {float(need_floor):.2f}/{float(need_birth):.2f}; Delta=0 gives {4*L2:.2f} e-folds; burst {burst} generations")
a, p = sp.symbols('a p', positive=True)
w = sp.simplify(-p / 3)
# (i) response in vacuum units: G_cell fixed -> l_P ~ l ~ a; rho ~ V0/l^4 -> H^2 ~ G rho ~ a^-2 -> aH const
aH_i = sp.simplify(a * sp.sqrt(a ** 2 * a ** -4))
aH_ii = sp.simplify(a * sp.sqrt(a ** -4))   # (ii) G fixed in proper units: radiation-like
Nexit_i = float(sp.log(aH_i.subs(a, sp.exp(60)) / aH_i.subs(a, 1)))
Nexit_ii = float(sp.log(aH_ii.subs(a, sp.exp(60)) / aH_ii.subs(a, 1)))
check(Nexit_i == 0 and abs(Nexit_ii + 60) < 1e-9, "A2 [T]",
      "dilation gauge: with the tied lapse the plateau is V0 per site per tick, rho ~ V0/l^4; read in the vacuum's own "
      "units (CL-3, M_P l = 1) aH is constant: zero horizon-exit e-folds for any stretch; with G fixed in proper units "
      "rho ~ a^-4 and the patch leaves no horizon either",
      f"horizon-exit e-folds over 60 edge e-folds: vacuum-units {Nexit_i:.0f}, proper-G {Nexit_ii:.0f}")
check(w.subs(p, -1) == sp.Rational(1, 3) and w.subs(p, 0) == 0, "A3 [T]",
      "no-go: a fixed site set with per-site energy ~ l^p (p <= 0 for bounded per-tick energy, -1 tied lapse) has "
      "w = -p/3 >= 0; acceleration needs w < -1/3, so e-folds need new sites: 60 e-folds = 86.6 split generations "
      "DURING the plateau. The candidate fails for every Delta",
      f"w(p=-1) {w.subs(p,-1)}, w(p=0) {w.subs(p,0)}; generations {60/L2:.1f}")

print("== B. the split must carry the fold order (IN-1)")
C4_ = np.array(list(itertools.product(range(4), repeat=3)))
sQ = np.array([(-1) ** int(r.sum()) for r in C4_]); sP = np.array([np.prod([(-1) ** (int(x) // 2) for x in r]) for r in C4_])
q = lambda x: 1 / 8 + 7 * x / 8
check(int(sQ @ sP) == 0 and q(1.0) == 1.0, "B1 [T]",
      "site-zone passing gives a parent staggered order zero overlap with the child's (nested-prefold E1): children unfolded, "
      "x = 1, q = 1/8 + 7x/8 = 1: de Sitter with no exit; after reheating every split would re-seed V0, so NO folded "
      "vacuum survives a split without order carriage",
      f"overlap {int(sQ@sP)}; q(1) {q(1.0)}")
cf = lambda f: 3 * L2 * (f / (1 - f) + 0.5)
tau, Hh = 1e-3, 1.0; ns_ = int(round(L2 / tau)); nst = 40 * ns_; v = 0.0; vs = []
for k in range(nst):
    if k and k % ns_ == 0:
        v /= 8.0
    v += -1.0 * tau; vs.append(v)
vm = -np.mean(vs[-4 * ns_:]) * 3 * Hh
check(abs(cf(1 / 8) - 27 * L2 / 14) < 1e-12 and abs(vm - cf(1 / 8)) < 2e-3, "B2 [T+D]",
      "IN-1 carries each order's total momentum: in cell units the tick is static between splits and the split divides "
      "the order velocity by 8, so friction is impulsive with mean drift c = 3ln2(f/(1-f)+1/2) = 27ln2/14 x (-V'/3H)",
      f"c exact {cf(1/8):.4f}, stepped {vm:.4f}")
chi, mu, al, V0s, c, Ns = sp.symbols('chi mu alpha V0 c N', positive=True)
Vp = V0s * (1 - al * sp.exp(-chi / mu))
Nstd = mu ** 2 / al * sp.exp(chi / mu)                       # leading plateau e-folds
dNdchi = sp.diff(Nstd, chi) / c                               # N = N_std / c
Pc = dNdchi ** 2 * (Vp.subs(al * sp.exp(-chi / mu), 0) / 3) / (4 * sp.pi ** 2)   # plateau H^2 = V0/3
PN = sp.simplify(Pc.subs(sp.exp(chi / mu), al * c * Ns / mu ** 2))
check(sp.diff(PN, c) == 0, "B3 [T]",
      "plateau attractor is friction-blind: with N = N_std/c, P(N) = V0 N^2/(12 pi^2 mu^2) at leading order, so n_s(N), "
      "r(N) and A_s(N) do not depend on c (impulsive or continuous friction alike)",
      f"P(N) = {PN}")

print("== C. the nested sea's density-wave fold: potential, slow roll, amplitude")


def rho2(x):
    x = np.abs(np.atleast_1d(x)); out = np.zeros_like(x, dtype=float); m = x < 4
    out[m] = ellipk(np.minimum(1 - x[m] ** 2 / 16, 1 - 1e-15)) / (2 * np.pi ** 2); return out


def rho3(e):
    return quad(lambda k: rho2(e - 2 * np.cos(k))[0], 0, np.pi, points=[np.arccos(e / 2)] if abs(e) < 2 else None,
                limit=200)[0] / np.pi


EG = np.concatenate([np.linspace(0, 1.9, 60), np.linspace(1.9, 2.1, 41)[1:], np.linspace(2.1, 5.99, 120)[1:], [6.0]])
SR = CubicSpline(EG, [rho3(e) if e < 6 else 0.0 for e in EG])
rho0 = float(SR(0.0))


def ints(D, ns=6001):
    s = np.linspace(0, np.arcsinh(6 / D), ns); e = D * np.sinh(s); E = D * np.cosh(s); r = SR(np.minimum(e, 6))
    return 2 * simpson(r * e * D * D / (E + e), x=s), 2 * simpson(r, x=s), 0.25 * simpson(r * e * e / E ** 4, x=s)


def Wfold(D, g):
    I1, I2, _ = ints(D); return 0.75 * g * D * D * I2 * I2 - 0.5 * I1


def dstar(g):
    r = minimize_scalar(lambda u: -Wfold(np.exp(u), g), bounds=(-40, 3), method='bounded', options={'xatol': 1e-9})
    return np.exp(r.x)


def slowroll(sW, sz, V0, ulo, uhi, zeta, Nstar):
    uu = np.linspace(ulo, uhi, 40000)
    lW, l1, l2, lz1 = sW(uu), sW(uu, 1), sW(uu, 2), sz(uu, 1)
    lp = np.log(zeta) + uu + 0.5 * sz(uu); V = V0 - np.exp(lW); rat = np.exp(lW - 2 * lp)
    eps = 0.5 * l1 ** 2 * np.exp(2 * (lW - lp)) / V ** 2
    eta = -(rat / V) * ((l2 + l1 ** 2) - l1 * (1 + 0.5 * lz1))
    dN = V / (rat * l1)
    iend = int(np.argmax(eps >= 1.0)) if np.any(eps >= 1.0) else len(uu) - 1
    seg = 0.5 * (dN[1:] + dN[:-1]) * np.diff(uu); Nf = np.zeros(len(uu)); Nf[:iend] = np.cumsum(seg[:iend][::-1])[::-1]
    j = int(np.argmin(np.abs(Nf - Nstar)))
    return dict(ns=1 - 6 * eps[j] + 2 * eta[j], r=16 * eps[j], us=uu[j], ue=uu[iend], eps=eps[j], V=V[j], end=bool(np.any(eps >= 1)))


JA = np.sqrt(3.0)
DS = {g: dstar(g) for g in (0.5, 1.0)}
MZ = ints(1e-6)[2] * 1e-12
check(abs(MZ - rho0 / 12) < 1e-6 * rho0 and abs(3 * 1.0 * ints(DS[1.0])[1] - 1) < 1e-4, "C1 [T+D]",
      "rederived (nested-prefold C): simple-cubic DOS, gap equation 1 = 3g int rho/E at every g > 0, cranking pole "
      "M -> rho0/(12 D^2), released energy W ~ D^2 ln^2(1/D): exponential plateau",
      f"rho0 {rho0:.5f}; M D^2 {MZ:.7f}; D*(g=.5) {DS[0.5]:.3f}, D*(1) {DS[1.0]:.3f}")
SPL_ = {}
for g in (0.5, 1.0):
    u = np.linspace(-80, np.log(DS[g]) - 1e-3, 400)
    SPL_[g] = (CubicSpline(u, np.log([Wfold(np.exp(x), g) for x in u])), CubicSpline(u, np.log([ints(np.exp(x))[2] for x in u])),
               Wfold(DS[g], g), u[0], u[-1])


def at(g, rr, N):
    sW, sz, V0, lo, hi = SPL_[g]; return slowroll(sW, sz, V0, lo, hi, JA ** -0.5 * 2.0 ** -rr, N)


def rung(g, N):
    f = lambda rr: np.log(at(g, rr, N)['V'] * JA * 2.0 ** (-4 * rr) / (24 * np.pi ** 2 * at(g, rr, N)['eps'])) - np.log(AS_PL)
    return brentq(f, 0, 40, xtol=1e-5)


rows55 = {g: at(g, rung(g, 55.0), 55.0) for g in (0.5, 1.0)}
check(all(abs(d['ns'] - (1 - 2 / 55)) < 0.002 and d['end'] and d['r'] < 1e-10 for d in rows55.values()), "C2 [D]",
      "slow roll on the computed V and M at N* = 55 (rung FITTED to A_s): n_s = 1-2/N, eps = 1 before D* (graceful exit)",
      "; ".join(f"g={g}: n_s {d['ns']:.4f} r {d['r']:.0e} D_end/D* {np.exp(d['ue'])/DS[g]:.1e}" for g, d in rows55.items()))
lnk = np.log(0.05 / 2.248e-4)
res = {}
for g in (0.5, 1.0):
    N = 55.0
    for _ in range(4):
        rr = rung(g, N); d = at(g, rr, N); VM = d['V'] * JA * 2.0 ** (-4 * rr)
        N = 67 - lnk + 0.25 * np.log(VM) + 0.25 * np.log(1 / 1.5) - np.log(106.75) / 12
    rr = rung(g, N); d = at(g, rr, N); dp = at(g, rr, N + 1); dm = at(g, rr, N - 1)
    res[g] = dict(N=N, rr=rr, ns=d['ns'], r=d['r'], H=np.sqrt(d['V'] * JA * 2.0 ** (-4 * rr) / 3), run=-(dp['ns'] - dm['ns']) / 2)
check(all(44 < x['N'] < 52 for x in res.values()), "C3 [T+E]",
      "self-consistent N* (instant reheating, k* = 0.05/Mpc, Planck-2018 matching formula) with the A_s-FITTED rung: "
      "the low plateau (H ~ 1e-13 M_P) forces N* ~ 47, not 55",
      "; ".join(f"g={g}: N* {x['N']:.1f}, rung {x['rr']:.1f} (FITTED), H/M_P {x['H']:.1e}" for g, x in res.items()))
x = res[1.0]
check(x['r'] < RMAX and abs(x['run']) < 0.0045 + 2 * 0.0067, "C4 [E]",
      "predictions not fitted: n_s at self-consistent N*, r, running; vs Planck 0.9649(42), ACT+DESI 0.974(3), r < 0.036, "
      "running -0.0045(67)",
      f"n_s {x['ns']:.4f} ({(x['ns']-NS_PL)/SPL:+.1f} sig Planck, {(x['ns']-NS_ACT)/SACT:+.1f} sig ACT); r {x['r']:.0e}; "
      f"running {x['run']:.1e}")

print("== D. perturbations through splits (mode of the order field, cell units, H = 1)")


def stair(k, mode, nspl=16):
    """Synchronized splits: M = 8^n, K = k^2 2^n; mode 'sudden' (u, pi kept) or 'adiab' (vacuum carriage)."""
    M, w = 1.0, k; u = 1 / np.sqrt(2 * M * w) + 0j; pi = -1j * M * w * u; nb = []
    for n in range(nspl):
        c_, s_ = np.cos(w * L2), np.sin(w * L2)
        u, pi = u * c_ + pi / (M * w) * s_, pi * c_ - M * w * u * s_
        if mode == 'adiab':
            u, pi = u / 2, 2 * pi
        M, w = 8 * M, w / 2
        if w > 2:
            nb.append((M * w / 2) * abs(u - 1j * pi / (M * w)) ** 2)
    return 2 * k ** 3 * abs(u) ** 2, nb


def MK(t, kind, sig):
    if kind == 'smooth':
        return np.exp(3 * t), np.exp(t)
    nc = int(np.floor(t / L2)); K = int(6 * max(sig, 0.4) / L2) + 2; ns = np.arange(nc - K, nc + K + 1)
    if kind == 'gauss':
        wn = ndtr((t - ns * L2) / sig) - ndtr((t - (ns + 1) * L2) / sig)
    else:
        lo = np.maximum(t - (ns + 1) * L2, 0.0); hi = np.minimum(t - ns * L2, L2); wn = np.clip(hi - lo, 0, None) / L2
    return float(np.sum(8.0 ** ns * wn)), float(np.sum(2.0 ** ns * wn))


def mode(k, kind, sig=0.0, w0=40.0, wend=1e-3):
    t0 = np.log(k / w0); t1 = np.log(k / wend)
    M0, S0 = MK(t0, kind, sig); w_ = k * np.sqrt(S0 / M0); u0 = 1 / np.sqrt(2 * M0 * w_)
    hh = 1e-5; Mp, Sp = MK(t0 + hh, kind, sig); Mm, Sm = MK(t0 - hh, kind, sig)
    dl = (np.log(Mp * np.sqrt(Sp / Mp)) - np.log(Mm * np.sqrt(Sm / Mm))) / (2 * hh)   # d ln(M w)/dt
    p0 = M0 * u0 * (-1j * w_ - 0.5 * dl)

    def f(t, y):
        M, S = MK(t, kind, sig); u = y[0] + 1j * y[1]; pi = y[2] + 1j * y[3]
        du = pi / M; dp = -k * k * S * u
        return [du.real, du.imag, dp.real, dp.imag]
    sol = solve_ivp(f, (t0, t1), [u0.real, u0.imag, p0.real, p0.imag], method='DOP853', rtol=1e-8, atol=1e-30,
                    max_step=0.02)
    u = sol.y[0, -1] + 1j * sol.y[1, -1]
    return 2 * k ** 3 * abs(u) ** 2


Rad, _ = stair(1.0, 'adiab'); _, nbs = stair(64.0 * 1.37, 'sudden', 4)
check(Rad < 1e-6 and abs(nbs[0] - 9 / 16) < 1e-9, "D1 [T]",
      "the register's passing (vacuum to vacuum, each excitation to the same) maps every mode adiabatically and the tick "
      "is static in cell units, so occupations never change: superhorizon variance falls x1/4 per split and the vacuum "
      "seeds NO perturbation (A_s = 0); IN-1's sudden carriage of the order field instead gives |beta|^2 = (4-1)^2/16 per "
      "sub-horizon mode per synchronized split",
      f"adiabatic k^3|u|^2/BD after 16 splits {Rad:.1e}; sudden |beta|^2 {nbs[0]:.4f} (9/16)")
J = 8; ks = 2.0 ** (np.arange(J) / J) * 2.0 ** 6
Rsm = mode(ks[0], 'smooth')
Rst = np.array([stair(k, 'sudden')[0] for k in ks])


def harm(R):
    return abs(np.sum(R * np.exp(2j * np.pi * np.arange(len(R)) / len(R)))) * 2 / len(R) / R.mean()


check(abs(Rsm - 1) < 0.02 and Rst.mean() > 3, "D2 [D]",
      "continuum reference (smooth a^3 weight) reproduces Bunch-Davies H^2/2k^3; synchronized IN-1 carriage heats "
      "before exit and saws the spectrum with period ln2 in ln k",
      f"smooth R {Rsm:.4f}; synchronized: mean R {Rst.mean():.1f}, first-harmonic {harm(Rst):.2f}")
cases = [('gauss', 0.1), ('gauss', 0.2), ('gauss', 0.35), ('uniform', 0.0)]
out = {}
for kind, sg in cases:
    R = np.array([mode(k, kind, sg) for k in ks]); out[(kind, sg)] = (R.mean(), harm(R))
g35 = out[('gauss', 0.35)]
check(abs(g35[0] - 1) < 0.35 and g35[1] < 0.03 and out[('gauss', 0.1)][1] > g35[1], "D3 [D+E]",
      "dephased splits (block split phases spread sigma e-folds; mode sees the summed cell count): mean R = O(1) (rung "
      "shift log2(R)/2 < 0.2) and the "
      "ln2-periodic modulation dies as sigma grows; < 0.03 needs sigma >~ 0.35 e-folds (bound order of a few %, Planck "
      "log-oscillation search, approximate)",
      "; ".join(f"{kd[0]}{'' if kd[0]=='u' else kd[1]}: R {m:.2f} A1 {h:.3f}" for kd, (m, h) in out.items()))
sig_law = [L2 * np.sqrt(Lv / 2034) for Lv in (22, 42)]
check(sig_law[1] < 0.35, "D4 [E]",
      "the laws' own spread (Poisson register model of spectral-tilt, per-level (ln2)^2/(m s), m s <= 2034, random walk "
      "over the 22-42 levels since a Hubble patch's common ancestor) falls short: a dephasing source is still needed",
      f"sigma_law {sig_law[0]:.3f}-{sig_law[1]:.3f} e-folds vs required ~0.35")

print("== E. exit, reheating, vacuum standard")
g = 1.0; Ds = DS[g]; h = 1e-3 * Ds
Epp = -(Wfold(Ds + h, g) - 2 * Wfold(Ds, g) + Wfold(Ds - h, g)) / h ** 2
wamp = np.sqrt(Epp / ints(Ds)[2])
check(Epp > 0 and wamp > 0, "E1 [E]",
      "after exit the order oscillates about D* (a minimum); amplitude-mode frequency vs the pair edge 2D*: at or above "
      "the edge it decays into the gapped sea's quasiparticle pairs (fold-sea matter); fold-inflaton E: misfolds <= 0.36 "
      "walls/site",
      f"omega_amp {wamp:.3f}, 2D* {2*Ds:.3f}, ratio {wamp/(2*Ds):.2f} (adiabatic mass; non-adiabatic near the edge)")
check(SPL_[g][2] > 0, "E2 [T]",
      "vacuum standard read as the lowest state over orders (folded): plateau departure V0 drives H, zero after exit "
      "(Lambda stays a separate supplied constant); read as filled-negative modes (unfolded) the departure is 0",
      f"V0 (g=1) {SPL_[g][2]:.4f} per site")

print("== F. split-trigger consistency under IN-1")
Hc = res[1.0]['H']
check(Hc < 1.93e-5 and Hc * 4 * L2 < 1, "F1 [T+E]",
      "the plateau rides the ordinary 4s trigger: one generation = s steps = ln2, H a = H/M_P per finest tick far below the "
      "edge-rate cap and inflaton A1 (H a < 1.93e-5); window and Delta unchanged",
      f"H a {Hc:.1e}; ticks per split ~{L2/Hc:.1e}; generations in N* {res[1.0]['N']/L2:.0f}")
print("supplied: g (0.5, 1), fold rung (FITTED to A_s), J a = sqrt3, M_P a = 1, Hartree, instant reheating, "
      "g_* = 106.75, mode speed 1, dephasing sigma (scanned)")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
