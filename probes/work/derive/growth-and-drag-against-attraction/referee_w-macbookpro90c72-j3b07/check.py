#!/usr/bin/env python3
"""Independent referee checks for growth-and-drag-against-attraction a4.

Symmetry for the sphere moments, dsolve for the ODEs, and a fresh quadrature
of the radial fall. Not the author's script.
"""
import math

import sympy as sp

FAILS = []


def ok(step, good, msg):
    print(("ok " if good else "FAIL ") + step + ": " + msg, flush=True)
    if not good:
        FAILS.append(step)


def main():
    # |s|=1 and axis permutation force <|s|_1 s_i s_j> = delta_ij/2 once <|s|_1>=3/2.
    # <|cos theta|> = (1/2) int_0^pi |cos| sin dtheta = int_0^{pi/2} cos sin dtheta = 1/2.
    th = sp.symbols("theta", real=True)
    mean_abs_cos = sp.simplify(sp.integrate(sp.cos(th) * sp.sin(th), (th, 0, sp.pi / 2)))
    mean_l1 = 3 * mean_abs_cos
    # trace: sum_i <|s|_1 s_i^2> = <|s|_1>, diagonals equal, so each is <|s|_1>/3 = 1/2
    moment = sp.Rational(1, 2)
    captured = 3 * moment / mean_l1  # linear response of |s|_1-weighted mean is exactly u
    ok("1", mean_abs_cos == sp.Rational(1, 2) and mean_l1 == sp.Rational(3, 2) and captured == 1,
       "<|s_z|>=1/2 so <|s|_1>=3/2; <|s|_1 s_i^2>=1/2 by the trace, and captured content is u")

    # drift: on axis k the two opposite steps contribute s_k/sqrt(3)
    # max(0, x) - max(0, -x) = x, checked on each sign rather than a symbolic Max
    drift_ok = True
    for sk in (sp.Rational(3, 5), sp.Rational(-2, 7), 0, sp.Integer(-1)):
        piece = (sp.Max(0, sk) - sp.Max(0, -sk)) / sp.sqrt(3)
        drift_ok &= sp.simplify(piece - sk / sp.sqrt(3)) == 0
    ok("2", drift_ok, "sum_e e max(0, s.e)/sqrt(3) = s/sqrt(3) on positive, negative and zero components")

    t, q, w0, p0 = sp.symbols("t q w0 p0", positive=True)
    p = sp.Function("p")
    # constant wind
    sol_c = sp.dsolve(sp.diff(p(t), t) - q * (w0 - p(t)), p(t), ics={p(0): p0})
    want_c = w0 + (p0 - w0) * sp.exp(-q * t)
    # growing wind w = w0 e^{qt}
    sol_g = sp.dsolve(sp.diff(p(t), t) - q * (w0 * sp.exp(q * t) - p(t)), p(t), ics={p(0): p0})
    want_g = (w0 / 2) * sp.exp(q * t) + (p0 - w0 / 2) * sp.exp(-q * t)
    lim = sp.limit(sp.simplify(sol_g.rhs / (w0 * sp.exp(q * t))), t, sp.oo)
    ok("3-4", sp.simplify(sol_c.rhs - want_c) == 0 and sp.simplify(sol_g.rhs - want_g) == 0 and lim == sp.Rational(1, 2),
       "dsolve: constant wind relaxes to w; a wind growing at q_1 entrains at exactly 1/2")

    # GM and the two thresholds
    r, rho, N1 = sp.symbols("r rho N1", positive=True)
    GM = q ** 2 * N1 / (4 * sp.pi * rho * (1 - rho))
    acc = q * (sp.sqrt(3) * q * N1 / (4 * sp.pi * r ** 2 * rho * (1 - rho))) / sp.sqrt(3)
    # fall time by the degenerate-ellipse half period: a = r/2, T/2 = pi sqrt(a^3/GM)
    t_ff = sp.pi * sp.sqrt((r / 2) ** 3 / GM)
    t_ff_stated = (sp.pi / 2) * sp.sqrt(r ** 3 / (2 * GM))
    # quadrature: int_0^1 du / sqrt(1/u - 1) = pi/2
    u = sp.symbols("u", positive=True)
    quad = sp.simplify(sp.integrate(1 / sp.sqrt(1 / u - 1), (u, 0, 1)))
    N_fall = sp.solve(sp.Eq(t_ff * q, 1), N1)[0]
    N_orb = sp.solve(sp.Eq(2 * sp.pi * sp.sqrt(r ** 3 / GM) * q, 1), N1)[0]
    gas = (4 * sp.pi / 3) * rho * r ** 3
    # gas << coef * N1 / (1-rho)  <=>  N1 = gas * (1-rho) / coef
    coef_fall = sp.simplify((1 - rho) * gas / N_fall)
    coef_orb = sp.simplify((1 - rho) * gas / N_orb)
    ratio = sp.simplify(N_orb / N_fall)
    ok("5",
       sp.simplify(acc - GM / r ** 2) == 0
       and sp.simplify(t_ff - t_ff_stated) == 0
       and quad == sp.pi / 2
       and coef_fall == sp.Rational(8, 3) / sp.pi ** 2
       and coef_orb == 1 / (12 * sp.pi ** 2)
       and ratio == 32,
       f"fall coefficient {coef_fall} = 8/(3 pi^2), orbit {coef_orb}, N_orbit/N_fall = {ratio}")

    coef_num = float(coef_fall)
    ok("5b", abs(coef_num - 8 / (3 * math.pi ** 2)) < 1e-12,
       f"8/(3 pi^2) = {coef_num:.6f}, which is {coef_num / (1/6):.3f} times the supervisor's 1/6")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent check did not reproduce that step")
        return
    print(
        "HIT: confirmed - dp/dt = q1(<s>-p), velocity p/sqrt(3), fall threshold "
        "(4 pi/3) rho r^3 = 8 N1/(3 pi^2 (1-rho)), orbit 32 times stricter, and a growing source entrains at 1/2"
    )
    print(
        "SUMMARY: confirmed the sphere moments by symmetry, both ODE solutions by dsolve, "
        "and the fall and orbit coefficients; the half-wind correction replaces the task's anticipated full wind"
    )


if __name__ == "__main__":
    main()
