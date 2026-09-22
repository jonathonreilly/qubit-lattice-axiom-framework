#!/usr/bin/env python3
"""J:derive:growth-and-drag-against-attraction:a4 -- exact checks and one integration.

Supplied clause (blocks 44-47, not adopted): a record's content is its direction of travel s (unit vector); it steps
to x + e with probability max(0, s.e)/sqrt3 for each of the six unit vectors e; a capturing site takes up records in
proportion to |s|_1, at q_1 = (sqrt3/2) rho per tick; a body capturing Q per tick draws the wind
<s>_wind = sqrt3 Q/(4 pi r^2 rho (1 - rho)).  EXACT: sympy for the sphere moments, the drift, the solutions of the
equations of motion, the fall time and the coefficients.  FLOATING POINT (labelled): one integration.
"""
import sys
import numpy as np
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------- (a) what a record and a body carry, and how they move
th, ph = sy.symbols("theta phi", real=True)
s = sy.Matrix([sy.sin(th) * sy.cos(ph), sy.sin(th) * sy.sin(ph), sy.cos(th)])
dA = sy.sin(th) / (4 * sy.pi)                                # uniform probability on the sphere


def sphere_avg(f):
    """average over the sphere of an expression with |s_k|: integrate over the first octant and use symmetry"""
    return sy.simplify(8 * sy.integrate(sy.integrate(f * dA, (ph, 0, sy.pi / 2)), (th, 0, sy.pi / 2)))


abs1 = s[0] + s[1] + s[2]                                    # |s|_1 in the first octant
m0 = sphere_avg(abs1)
m11 = sphere_avg(abs1 * s[0] ** 2)
ok = m0 == sy.Rational(3, 2) and m11 == sy.Rational(1, 2)
# first-harmonic wind (1 + 3 u.s)/(4 pi): captured records (weight |s|_1) bring <|s|_1 s>/<|s|_1> = u = <s>_wind
ok &= sy.Rational(3, 1) * m11 / m0 == 1
# drift of a record with content s: sum over the six unit vectors of e max(0, s.e)/sqrt3 = s/sqrt3
# per axis e_k max(0, s_k) - e_k max(0, -s_k) = e_k s_k; checked exactly on vectors with every sign pattern and zeros
for sv in ((sy.Rational(1, 3), sy.Rational(-2, 3), sy.Rational(2, 3)), (0, sy.Rational(-3, 5), sy.Rational(4, 5)),
           (-1, 0, 0), (sy.Rational(-2, 7), sy.Rational(-3, 7), sy.Rational(-6, 7))):
    drift = sy.zeros(3, 1)
    for k in range(3):
        for sgn in (1, -1):
            e = sy.zeros(3, 1)
            e[k] = sgn
            drift += e * sy.Max(0, sgn * sv[k]) / sy.sqrt(3)
    ok &= drift == sy.Matrix(sv) / sy.sqrt(3)
need(ok, "(a) moments and drift")
rec("ok (a) over the uniform sphere <|s|_1> = 3/2 and <|s|_1 s_i s_j> = delta_ij/2, so in a first-harmonic wind "
    "(1 + 3u.s)/(4 pi) the records a site captures (weight |s|_1) bring exactly u = <s>_wind each; a record of "
    "content s drifts at sum_e e max(0, s.e)/sqrt3 = s/sqrt3, linear in s, so a lump of records whose mean content is "
    "p = P/N drifts at p/sqrt3")

# ---------------------------------- equations of motion and their exact bookkeeping
t, q, N0, P0, w = sy.symbols("t q_1 N_0 p_0 w", positive=True)
N = N0 * sy.exp(q * t)
p = w + (P0 - w) * sy.exp(-q * t)                           # constant wind w, momentum per record p
P = N * p
ok = sy.simplify(sy.diff(N, t) - q * N) == 0
ok &= sy.simplify(sy.diff(P, t) - q * N * w) == 0            # dP/dt = q_1 N <s>_wind
ok &= sy.simplify(sy.diff(p, t) - q * (w - p)) == 0          # dp/dt = q_1 (<s>_wind - p)
ok &= sy.simplify(P.subs(t, 0) - N0 * P0) == 0
# a growing source: the wind at a fixed point grows with its capture rate, w = w0 e^(q_1 t); then
# p = (w0/2) e^(q_1 t) + (p_0 - w0/2) e^(-q_1 t): the body is entrained at HALF the local wind
w0 = sy.symbols("w_0", positive=True)
pg = w0 / 2 * sy.exp(q * t) + (P0 - w0 / 2) * sy.exp(-q * t)
ok &= sy.simplify(sy.diff(pg, t) - q * (w0 * sy.exp(q * t) - pg)) == 0 and pg.subs(t, 0) == P0
ok &= sy.limit(pg / (w0 * sy.exp(q * t)), t, sy.oo) == sy.Rational(1, 2)
need(ok, "(a) equations")
rec("ok (a) dN/dt = q_1 N and dP/dt = q_1 N <s>_wind give dp/dt = q_1(<s>_wind - p); in a constant wind "
    "N = N_0 e^(q_1 t), p = w + (p_0 - w) e^(-q_1 t), and P = N p satisfies the momentum bookkeeping exactly; in the "
    "wind of a source that grows at the same q_1, p/<s>_wind -> 1/2 exactly: entrainment at half the local wind")

# ---------------------------------- (b) the fall, the orbit, and the condition
r, r0, GM, rho, N1 = sy.symbols("r r_0 GM rho N_1", positive=True)
# ballistic regime (t << 1/q_1): dv/dt = q_1 <s>_wind / sqrt3 = q_1^2 N_1/(4 pi rho (1-rho) r^2) =: GM / r^2
GM_eff = q ** 2 * N1 / (4 * sy.pi * rho * (1 - rho))
acc = q * (sy.sqrt(3) * q * N1 / (4 * sy.pi * r ** 2 * rho * (1 - rho))) / sy.sqrt(3)
ok = sy.simplify(acc - GM_eff / r ** 2) == 0
# radial fall from rest at r_0: t = int_0^r0 dr / sqrt(2GM(1/r - 1/r0)) = (pi/2) sqrt(r0^3/(2 GM))
u_ = sy.symbols("u", positive=True)
t_ff = sy.integrate(1 / sy.sqrt(2 * GM * (1 / (r0 * u_) - 1 / r0)) * r0, (u_, 0, 1))
ok &= sy.simplify(t_ff - sy.pi / 2 * sy.sqrt(r0 ** 3 / (2 * GM))) == 0
# fall survives growth and drag iff t_ff < 1/q_1  <=>  (4 pi/3) rho r^3 < 8 N_1/(3 pi^2 (1 - rho))
cond_fall = sy.solve(sy.Eq((sy.pi / 2 * sy.sqrt(r0 ** 3 / (2 * GM_eff))) * q, 1), N1)[0]
ok &= sy.simplify(cond_fall - sy.Rational(3, 8) * sy.pi ** 2 * (1 - rho) * (4 * sy.pi / 3) * rho * r0 ** 3) == 0
# a circular orbit's period 2 pi sqrt(r^3/GM) < 1/q_1  <=>  (4 pi/3) rho r^3 < N_1/(12 pi^2 (1 - rho))
cond_orb = sy.solve(sy.Eq(2 * sy.pi * sy.sqrt(r0 ** 3 / GM_eff) * q, 1), N1)[0]
ok &= sy.simplify(cond_orb - 12 * sy.pi ** 2 * (1 - rho) * (4 * sy.pi / 3) * rho * r0 ** 3) == 0
ok &= sy.simplify(cond_orb / cond_fall) == 32
need(ok, "(b) conditions")
coef_fall, coef_orb = sy.Rational(8, 3) / sy.pi ** 2, 1 / (12 * sy.pi ** 2)
rec("ok (b) in the ballistic regime the pull is GM/r^2 with GM = q_1^2 N_1/(4 pi rho (1-rho)); the radial fall from "
    "rest takes (pi/2) sqrt(r^3/(2GM)); it beats the growth-and-drag time 1/q_1 iff (4 pi/3) rho r^3 < "
    "8 N_1/(3 pi^2 (1-rho)) = %.4f N_1/(1-rho) (the supervisor's estimate N_1/6 = 0.1667 N_1); one circular period "
    "beats it iff (4 pi/3) rho r^3 < N_1/(12 pi^2 (1-rho)) = %.5f N_1/(1-rho), 32 times stricter, and n periods "
    "need n^2 times more" % (float(coef_fall), float(coef_orb)))

# ---------------------------------- (c), (d) one integration (floating point): entrainment and growth
rho_v = 0.3
q1 = np.sqrt(3) / 2 * rho_v
N1_0, r_0 = 50.0, 30.0


def wind(N1_, rr):
    return np.sqrt(3) * q1 * N1_ / (4 * np.pi * rr ** 2 * rho_v * (1 - rho_v))


dt, T = 1e-3, 12.0
N1v, N2v, pv, rv, tt = N1_0, 1.0, 0.0, r_0, 0.0
captured = 0.0
while tt < T and rv > 1.0:
    wv_ = wind(N1v, rv)
    dN1, dN2 = q1 * N1v, q1 * N2v
    pv += dt * q1 * (wv_ - pv)
    rv -= dt * pv / np.sqrt(3)
    captured += dt * dN2
    N1v += dt * dN1
    N2v += dt * dN2
    tt += dt
ok = abs(N2v - 1.0 - captured) < 1e-9 and abs(N1v / N1_0 - np.exp(q1 * tt)) / np.exp(q1 * tt) < 1e-2
ratio = pv / wind(N1v, rv)
ok &= 0.45 < ratio < 0.52 and r_0 - rv < 1.0
need(ok, "(c,d) integration")
rec("ok (c,d) (floating point, one case in the entrained regime: rho = 0.3, q_1 = %.3f, a growing source N_1 = 50 "
    "at r_0 = 30, test body from rest) after t = %.0f = %.1f/q_1 the body has moved to r = %.3f and carries "
    "p = %.3f of the local wind, the exact 1/2 for a source growing at q_1 (up to e^(-2 q_1 t)); N_1 grew by %.1f = "
    "e^(q_1 t) (captures booked exactly to rounding), so the force ~ N_1 N_2/r^2 grows as e^(2 q_1 t)"
    % (q1, tt, q1 * tt, rv, ratio, N1v / N1_0))

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL the equations of motion dN/dt = q_1 N, dp/dt = q_1(<s>_wind - p) with body velocity p/sqrt3 are derived "
      "(captured records bring exactly the wind's mean momentum: <|s|_1> = 3/2, <|s|_1 s_i s_j> = delta_ij/2); "
      "attraction outruns growth and drag for a radial fall iff (4 pi/3) rho r^3 << 8 N_1/(3 pi^2 (1-rho)) "
      "(= 0.270 N_1 at low density, against the supervisor's N_1/6) and for one circular orbit iff "
      "<< N_1/(12 pi^2 (1-rho)); beyond 1/q_1 bodies are entrained, at HALF the local wind when the source grows at "
      "the same q_1, and N grows as e^(q_1 t)."))
if not FAIL:
    print("HIT: for a free transparent body in another body's wind, dN/dt = q_1 N and dp/dt = q_1(<s>_wind - p) with "
          "velocity p/sqrt3 (exact first-harmonic moments), GM = q_1^2 N_1/(4 pi rho (1-rho)); a radial fall "
          "outruns growth and drag iff (4 pi/3) rho r^3 << 8 N_1/(3 pi^2 (1-rho)), a circular orbit iff "
          "<< N_1/(12 pi^2 (1-rho)) (32 times stricter); coefficient 0.270 against the supervisor's 1/6; beyond "
          "1/q_1 a body in the wind of a source growing at the same q_1 is entrained at exactly HALF the local wind, "
          "not at the wind speed.")
sys.exit(1 if FAIL else 0)
