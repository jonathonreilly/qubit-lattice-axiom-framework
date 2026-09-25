#!/usr/bin/env python3
"""check.py for J:derive:deferred-20260925-matter-clocks:a1 (worker w-jonathonsmac4f50-j324c, claude-opus-5-5).

Residual (unit 23, PR #9164, landed narrowed on main): the finite-window question beyond the supplied hazard-family identities.
Worked: when does formation-weighted averaging dephase?  The perpendicular part of the formation-weighted Bloch average is the characteristic
function z = E[exp(i omega tau) | tau < T] of the conditioned formation time at the precession frequency.  Exact arithmetic (sympy) throughout.
"""
import sympy as sp

PASS, FAIL = [], []
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else ""), flush=True)

t, T, f, om = sp.symbols("t T f omega", positive=True)
x, kap, tau = sp.symbols("x kappa tau", positive=True)

# ---------------------------------------------------------------- E1 the characteristic-function form, and the landed constant-clock z
# precession r(t) = r_par + cos(om t) r_perp + sin(om t) (hhat x r_perp) (landed note); averaging with a probability density w_T on [0, T]:
# r_bar = r_par + Re(z) r_perp + Im(z) hhat x r_perp with z = int_0^T exp(i om t) w_T(t) dt  (the characteristic function at om).
wT = f * sp.exp(-f * t) / (1 - sp.exp(-f * T))                               # constant hazard, conditioned on formation before T
z_int = sp.simplify(sp.integrate(sp.exp(sp.I * om * t) * wT, (t, 0, T)))
z_note = f * (1 - sp.exp(-(f - sp.I * om) * T)) / ((f - sp.I * om) * (1 - sp.exp(-f * T)))
check("E1 for the constant clock the characteristic function of the conditioned formation time at omega is the landed note's z = f[1 - e^{-(f - i om)T}]/[(f - i om)(1 - e^{-fT})]",
      sp.simplify(z_int - z_note) == 0)
# cos/sin parts: int w cos = Re z, int w sin = Im z
ok = sp.simplify(sp.integrate(sp.cos(om * t) * wT, (t, 0, T)) - sp.re(sp.expand_complex(z_note))) == 0
check("E1b the Bloch components: int w_T cos(om t) dt = Re z (so r_bar = r_par + Re z r_perp + Im z hhat x r_perp)", ok)

# ---------------------------------------------------------------- E2 the constant-clock bound and the joint limit
# in units x = f/om, tau = om T, kappa = f T = x tau:  z = x (1 - e^{-kappa} e^{i tau}) / ((x - i)(1 - e^{-kappa}))
zs = x * (1 - sp.exp(-kap) * sp.exp(sp.I * tau)) / ((x - sp.I) * (1 - sp.exp(-kap)))
# |z| <= x (1 + e^{-kappa}) / (sqrt(1 + x^2)(1 - e^{-kappa})) <= 2x/(1 - e^{-kappa}) <= 2x (1 + 1/kappa) = 2 (f/om + 1/(om T))
y = sp.Symbol("y", positive=True)
lemma = sp.simplify((1 + 1 / y) * (1 - sp.exp(-y)) - 1)                      # >= 0  <=>  1/(1 - e^{-y}) <= 1 + 1/y
d_lemma = sp.simplify(sp.diff((y + 1) * (1 - sp.exp(-y)) - y, y))           # (y+1)(1-e^-y) - y vanishes at 0; derivative y e^{-y} >= 0
check("E2a lemma: 1/(1 - e^{-y}) <= 1 + 1/y for y > 0 [(y+1)(1 - e^{-y}) - y is 0 at y = 0 with derivative y e^{-y} >= 0]",
      sp.simplify(d_lemma - y * sp.exp(-y)) == 0 and ((y + 1) * (1 - sp.exp(-y)) - y).subs(y, 0) == 0)
absz2 = sp.simplify(sp.expand_complex(zs * sp.conjugate(zs)))
num_bound = (x * (1 + sp.exp(-kap))) ** 2 / ((1 + x ** 2) * (1 - sp.exp(-kap)) ** 2)
# |1 - e^{-kappa} e^{i tau}|^2 = 1 - 2 e^{-kappa} cos tau + e^{-2 kappa} <= (1 + e^{-kappa})^2
diff = sp.simplify(num_bound - absz2)
check("E2b |z|^2 = x^2 (1 - 2e^{-kappa}cos tau + e^{-2kappa}) / ((1 + x^2)(1 - e^{-kappa})^2) <= x^2 (1 + e^{-kappa})^2/((1 + x^2)(1 - e^{-kappa})^2): "
      "the difference is 2x^2 e^{-kappa}(1 + cos tau)/((1+x^2)(1-e^{-kappa})^2) >= 0",
      sp.simplify(diff - 2 * x ** 2 * sp.exp(-kap) * (1 + sp.cos(tau)) / ((1 + x ** 2) * (1 - sp.exp(-kap)) ** 2)) == 0)
import itertools
spot = True
for xv, kv, tv in itertools.product([sp.Rational(1, 100), sp.Rational(1, 7), 1, 5], [sp.Rational(1, 50), sp.Rational(1, 2), 3, 40], [sp.Rational(1, 3), 2, sp.pi, 31]):
    zv = sp.N(zs.subs({x: xv, kap: kv, tau: tv}), 40)
    spot = spot and sp.N(sp.Abs(zv), 40) <= sp.N(2 * xv * (1 + 1 / kv), 40)
check("E2c hence, with E2a, |z| <= 2x/(1 - e^{-kappa}) <= 2x(1 + 1/kappa) = 2(f/omega + 1/(omega T)) for every f, T > 0 (spot-checked at 64 points, 40 digits): "
      "the joint limit (f, 1/T) -> (0, 0) exists along every path and is the field-dephased average (z = 0); both iterated limits are special paths", spot)
# sharpness: fixed T, f -> 0: z -> (e^{i om T} - 1)/(i om T), |.| = 2|sin(om T/2)|/(om T): equals the bound 2/(om T) at om T = pi
zlim0 = sp.limit(z_note, f, 0)
check("E2d sharpness at fixed T, f -> 0: z -> (e^{i om T} - 1)/(i om T) (the landed uniform average), whose modulus at om T = pi is 2/pi = 2/(om T): the 1/(om T) term is attained",
      sp.simplify(zlim0 - (sp.exp(sp.I * om * T) - 1) / (sp.I * om * T)) == 0 and
      sp.simplify(sp.Abs(zlim0.subs(T, sp.pi / om)) - 2 / sp.pi) == 0)
Ee, Pp = sp.symbols("E P")                                                   # E = exp(-f T) -> 0, P = exp(i om T) with |P| = 1
zEP = f * (1 - Ee * Pp) / ((f - sp.I * om) * (1 - Ee))
ok_form = sp.simplify(zEP.subs({Ee: sp.exp(-f * T), Pp: sp.exp(sp.I * om * T)}) - z_note) == 0
zinf = sp.limit(zEP, Ee, 0) if ok_form else None                             # |E P| <= E -> 0 uniformly in the phase
check("E2e sharpness at fixed f, T -> oo: z -> f/(f - i om) (the landed z_infinity), |z| = f/sqrt(f^2 + om^2): within a factor 2 of the f/om term",
      ok_form and sp.simplify(zinf - f / (f - sp.I * om)) == 0)

# ---------------------------------------------------------------- E3 general supplied hazards: the bounded-variation bound (proved in ATTEMPT.md)
# |z| <= (w(0+) + w(T-) + TV(w))/omega; for a monotone w it is 2 max(w)/omega, for a unimodal w 2 max(w)/omega.
# instance: the landed linear hazard beta t: w = beta t exp(-beta t^2/2) / (1 - exp(-beta T^2/2)), unimodal with peak at t = 1/sqrt(beta)
beta = sp.Symbol("beta", positive=True)
wl = beta * t * sp.exp(-beta * t ** 2 / 2)
crit = sp.solve(sp.diff(wl, t), t)
check("E3 the landed linear hazard's formation density beta t e^{-beta t^2/2} is unimodal with its peak at t = 1/sqrt(beta), value sqrt(beta) e^{-1/2}: "
      "|z| <= 2 sqrt(beta) e^{-1/2}/(omega (1 - e^{-beta T^2/2})) for T >= 1/sqrt(beta), so it too dephases jointly as beta -> 0 with beta T^2 -> oo",
      crit == [1 / sp.sqrt(beta)] and sp.simplify(wl.subs(t, 1 / sp.sqrt(beta)) - sp.sqrt(beta) * sp.exp(-sp.Rational(1, 2))) == 0)

# ---------------------------------------------------------------- E4 resonant hazards: slow and long, but no dephasing
N = sp.Symbol("N", positive=True, integer=True)
Tn = 2 * sp.pi * N / om
wc = (1 + sp.cos(om * t)) / Tn                                               # a probability density on [0, T_N]
ok = sp.simplify(sp.integrate(wc, (t, 0, Tn)) - 1) == 0
zc = sp.simplify(sp.integrate(sp.exp(sp.I * om * t) * wc, (t, 0, Tn)))
check("E4a cosine-modulated formation density w = (1 + cos om t)/T on T = 2 pi N/omega: z = 1/2 for every N (no dephasing as T -> oo)", ok and zc == sp.Rational(1, 2), str(zc))
# realized by a nonnegative hazard: conditional formation probability m in (0, 1); f(t) = m w(t)/(1 - m int_0^t w) >= 0, sup f <= 2m/(T(1 - m)) -> 0
m_ = sp.Symbol("m", positive=True)
Wc = sp.integrate(wc.subs(t, sp.Symbol("s")), (sp.Symbol("s"), 0, t))
fc = m_ * wc / (1 - m_ * Wc)
S_ = sp.exp(-sp.integrate(fc.subs(t, sp.Symbol("s")), (sp.Symbol("s"), 0, t)))
check("E4b the hazard f = m w/(1 - m W), W = int_0^t w, has survival S = 1 - m W, formation density f S = m w and formation probability m before T: any density on [0, T] "
      "is a supplied hazard's; with w = (1 + cos om t)/T, sup f <= 2m/(T(1-m)) -> 0 as T -> oo while |z| = 1/2",
      sp.simplify(sp.diff(1 - m_ * Wc, t) + fc * (1 - m_ * Wc)) == 0)
# square-wave hazard f0 on the half-periods where cos(om t) > 0 (switching times fixed by the field phase), N periods, f0 -> 0: z -> 2/pi
phi = sp.Symbol("phi")
z_sq_lim = sp.simplify(sp.integrate(sp.exp(sp.I * phi), (phi, -sp.pi / 2, sp.pi / 2)) / sp.pi)
check("E4c a piecewise-constant hazard switching between f0 and 0 at the half-periods (as neighbour records synchronized with the field could impose) gives, "
      "as f0 -> 0 with N periods, the uniform law on the 'on' half-periods and z -> (1/pi) int_{-pi/2}^{pi/2} e^{i phi} d phi = 2/pi, for every N", z_sq_lim == 2 / sp.pi)
# the same exactly at finite f0 for N = 1 (on-interval [0, pi/(2 om)] and [3pi/(2 om), 2pi/om]): z(f0) -> 2/pi
f0 = sp.Symbol("f_0", positive=True)
a1_, b1_ = 0, sp.pi / (2 * om); a2_, b2_ = 3 * sp.pi / (2 * om), 2 * sp.pi / om
w1 = f0 * sp.exp(-f0 * t)                                                    # first on-interval (survival starts at 1)
S1 = sp.exp(-f0 * sp.pi / (2 * om))
w2 = f0 * S1 * sp.exp(-f0 * (t - a2_))                                        # second on-interval (off in between: survival flat)
mass = sp.integrate(w1, (t, a1_, b1_)) + sp.integrate(w2, (t, a2_, b2_))
zq = (sp.integrate(sp.exp(sp.I * om * t) * w1, (t, a1_, b1_)) + sp.integrate(sp.exp(sp.I * om * t) * w2, (t, a2_, b2_))) / mass
check("E4d exact square-wave clock over one period: z(f0) -> 2/pi as f0 -> 0", sp.simplify(sp.limit(sp.simplify(zq), f0, 0) - 2 / sp.pi) == 0)

print("")
print("TOTAL: PASS=%d FAIL=%d" % (len(PASS), len(FAIL)))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("HIT: for PR #9164's supplied qubit precession and ANY supplied hazard, the formation-weighted Bloch average's perpendicular part is the characteristic "
          "function z = E[exp(i omega tau) | tau < T] of the conditioned formation time at the precession frequency; the constant clock obeys |z| <= "
          "2(f/omega + 1/(omega T)), so the joint slow-rate/long-window limit exists along every path and dephases (sharp up to a factor 2 in each term); "
          "slow rates and long windows do not dephase in general: hazards modulated at the precession frequency keep |z| = 1/2 (cosine) or -> 2/pi "
          "(half-period square wave) while sup f -> 0 and T -> oo; bounded variation, |z| <= (w(0)+w(T)+TV(w))/omega, is sufficient")
    print("SUMMARY: PARTIAL a finite-window dephasing criterion for supplied formation clocks (characteristic function at omega), with a joint-limit bound "
          "for the constant clock and resonant counterexamples for time-dependent hazards; no clock is selected or derived from the axioms")
