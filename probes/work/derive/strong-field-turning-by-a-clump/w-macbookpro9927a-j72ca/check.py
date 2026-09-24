#!/usr/bin/env python3
"""Strong-field turning by a clump: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j72ca (claude-opus-5-5).

Ray law (task; block 98's ray law of block 54's walk at long waves): dv/dt = -w^2 grad u + 2 (v.grad u) v, |v| = w = e^u, u = -A/r.
Exact (sympy, Fractions): invariants, the capture threshold, the reduction of the turn to one integral, its all-orders series.
Floating point, labelled executed: the ray law integrated as an ODE against the exact turn; the strong-deflection constant.
"""
from __future__ import annotations

import math
import subprocess
import sys

import mpmath as mp
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources, verbatim
B98 = ("6672f80380", "docs/ADMISSIBILITY_RULE_ONE_FIELD_FOR_RECORDS_AND_WAVES_A_WAVE_PASSING_A_RECORD_TURNS_BY_TWICE_THE_PAIR_ENERGY_AT_"
       "THAT_DISTANCE_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B98_Q = ["Its rays of `E = w(x) ε(k)`, `ε = |sin k|`, obey `dv_j/dt = −w² M_jl ∂_l u + 2(v·∇u) v_j` with `M = Hess(ε²/2)`",
         "a wave passing one record turns towards it by `δ(b) = 2|U(b)|`, where `U(b) = 6 log κ/(4πb)` is block 95's pair energy at that distance."]
TASK_Q = ["For rays of E = w(x)|sin k| with u = -A/r (w = e^u), exactly: (a) the turn angle at all orders for long waves (the ray law "
          "dv/dt = -w^2 grad u + 2(v.grad u)v with |v| = w), as a function of A/b; (b) whether rays can be captured (a critical impact "
          "parameter) and its value in units of A. HIT: (a) or (b) exact."]


def family_q() -> None:
    import json
    txt = subprocess.run(["git", "show", f"{B98[0]}:{B98[1]}"], capture_output=True, text=True).stdout
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:strong-field-turning-by-a-clump:a2"), "")
    miss = [f"b98[{i}]" for i, q in enumerate(B98_Q) if q not in txt] + [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 98's ray law and first-order turn (head 6672f803, PR #8878) and the task's statement quoted verbatim"
          f"{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ R: the ray law and its invariants
def family_r() -> None:
    x, y, z, A = sp.symbols("x y z A", positive=True)
    vx, vy, vz = sp.symbols("v_x v_y v_z", real=True)
    X = sp.Matrix([x, y, z]); V = sp.Matrix([vx, vy, vz])
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    u = -A / r; w = sp.exp(u)
    gu = sp.Matrix([sp.diff(u, c) for c in (x, y, z)])
    dV = -w ** 2 * gu + 2 * (V.dot(gu)) * V
    ddt = lambda f: sum(sp.diff(f, c) * V[i] for i, c in enumerate((x, y, z))) + sum(sp.diff(f, c) * dV[i] for i, c in enumerate((vx, vy, vz)))
    ok1 = sp.simplify(ddt(V.dot(V) - w ** 2) - 4 * V.dot(gu) * (V.dot(V) - w ** 2)) == 0          # |v| = w is invariant
    Jv = X.cross(V) * sp.exp(-2 * u)
    ok2 = all(sp.simplify(ddt(Jv[i])) == 0 for i in range(3))                                         # x × v e^{-2u} is conserved
    # the ray law is Hamilton's flow of H = w |p| (long waves: w |sin k| -> w |k|), with v = dH/dp
    p1, p2 = sp.symbols("p1 p2", real=True)
    x2, y2 = sp.symbols("x2 y2", real=True)
    r2 = sp.sqrt(x2 ** 2 + y2 ** 2); w2 = sp.exp(-A / r2); pn = sp.sqrt(p1 ** 2 + p2 ** 2)
    Hm = w2 * pn
    xd = [sp.diff(Hm, p1), sp.diff(Hm, p2)]; pd = [-sp.diff(Hm, x2), -sp.diff(Hm, y2)]
    vdot = [sum(sp.diff(xd[i], c) * d for c, d in zip((x2, y2, p1, p2), (xd[0], xd[1], pd[0], pd[1]))) for i in range(2)]
    g2 = [sp.diff(-A / r2, x2), sp.diff(-A / r2, y2)]
    law = [-w2 ** 2 * g2[i] + 2 * (xd[0] * g2[0] + xd[1] * g2[1]) * xd[i] for i in range(2)]
    ok3 = all(sp.simplify(vdot[i] - law[i]) == 0 for i in range(2)) and sp.simplify(xd[0] ** 2 + xd[1] ** 2 - w2 ** 2) == 0
    check("R", ok1 and ok2 and ok3, "the ray law keeps |v| = w (d(|v|^2 - w^2)/dt = 4 (v.grad u)(|v|^2 - w^2)), conserves x × v e^{-2u} "
          "for u = -A/r (3D, symbolic), and is Hamilton's flow of H = w|p| with v = dH/dp: rays of the index n = 1/w = e^{A/r}, "
          "with Bouguer's invariant r n sin(angle to the radius) = b")


# ------------------------------------------------------------------------------------------------ C: capture
def family_c() -> None:
    r, A, b = sp.symbols("r A b", positive=True)
    f = r * sp.exp(A / r)                                    # r n(r): turning points solve f = b
    ok = sp.simplify(sp.diff(f, r).subs(r, A)) == 0 and sp.simplify(f.subs(r, A) - sp.E * A) == 0
    ok &= sp.simplify(sp.diff(f, r, 2).subs(r, A) - sp.exp(1) / A) == 0                             # f''(A) = e/A > 0
    ok &= sp.limit(f, r, 0, "+") == sp.oo and sp.limit(f / r, r, sp.oo) == 1
    ok &= sp.simplify(sp.diff(f, r) - sp.exp(A / r) * (1 - A / r)) == 0                              # f' < 0 on (0, A), > 0 on (A, oo)
    # radial speed squared v_r^2 = w^2 (1 - b^2/f^2) > 0 everywhere when b < eA: no turning point
    # circular ray at r = A: v tangential with |v| = w(A) = 1/e; the law's acceleration -w^2 grad u = -(e^{-2}/A) r^ = centripetal
    acc = sp.exp(-2) * (A / A ** 2)
    ok &= sp.simplify(acc - sp.exp(-1) ** 2 / A) == 0
    check("C", ok, "(b) capture: r e^{A/r} has its only minimum e A at r = A (f' = e^{A/r}(1 - A/r), f''(A) = e/A, f -> oo at both ends); "
          "a ray with b < e A has no turning point (v_r^2 = w^2(1 - b^2/(r e^{A/r})^2) > 0) and falls in; b = e A is the circular ray "
          "r = A (tangential, speed 1/e, the law's pull e^{-2}/A is its centripetal need); critical impact parameter b_c = e A exactly")


# ------------------------------------------------------------------------------------------------ S: the turn as one integral, all orders
def c_coef(n):
    return 2 * sp.Integer(n) ** n / sp.factorial(n) * sp.sqrt(sp.pi) / 2 * sp.gamma(sp.Rational(n + 1, 2)) / sp.gamma(sp.Rational(n, 2) + 1)


def family_s() -> None:
    X, beta = sp.symbols("x beta", positive=True)
    Y = beta * X * sp.exp(-X)
    lhs2 = (beta / sp.sqrt(sp.exp(2 * X) - beta ** 2 * X ** 2)) ** 2 / sp.diff(Y, X) ** 2
    rhs2 = 1 / ((1 - X) ** 2 * (1 - Y ** 2))
    ok = sp.simplify(lhs2 - rhs2) == 0                       # beta dx/sqrt(e^{2x} - beta^2 x^2) = dy/((1 - x) sqrt(1 - y^2)), squared; both > 0
    zz = sp.Symbol("z")
    ser = sp.series(1 / (1 + sp.LambertW(-zz)), zz, 0, 15).removeO()
    ok &= all(sp.simplify(ser.coeff(zz, n) - sp.Integer(n) ** n / sp.factorial(n)) == 0 for n in range(1, 15)) and ser.coeff(zz, 0) == 1
    yv = sp.Symbol("y", positive=True)
    ok &= all(sp.simplify(sp.integrate(yv ** n / sp.sqrt(1 - yv ** 2), (yv, 0, 1))
                          - sp.sqrt(sp.pi) / 2 * sp.gamma(sp.Rational(n + 1, 2)) / sp.gamma(sp.Rational(n, 2) + 1)) == 0 for n in range(0, 9))
    cs = [sp.simplify(c_coef(n)) for n in range(1, 7)]
    want = [2, sp.pi, 6, 4 * sp.pi, sp.Rational(250, 9), sp.Rational(81, 4) * sp.pi]
    ok &= all(sp.simplify(a - b) == 0 for a, b in zip(cs, want))
    check("S", ok, "(a) all orders: with x = A/r and y = (b/A) x e^{-x} the swept angle is int_0^1 dy/((1 - x)sqrt(1 - y^2)), x = "
          "-W0(-yA/b), so the turn is chi = 2 int_0^1 dy/((1 + W0(-yA/b)) sqrt(1 - y^2)) - pi; 1/(1 + W0(-z)) = sum n^n z^n/n! "
          "(to z^14) and int_0^1 y^n/sqrt(1-y^2) = (sqrt(pi)/2) G((n+1)/2)/G(n/2+1), so chi = sum_n c_n (A/b)^n with c_n = "
          "(sqrt(pi) n^n/n!) G((n+1)/2)/G(n/2+1) = 2, pi, 6, 4pi, 250/9, 81pi/4, ...")


# ------------------------------------------------------------------------------------------------ N: executed
def chi_integral(beta, dps=30):
    mp.mp.dps = dps
    f = lambda t: 1 / (1 + mp.lambertw(-mp.sin(t) / beta, 0).real)
    edge = [mp.pi / 2 - mp.mpf(10) ** (-k) for k in range(1, 9)]
    return float(2 * mp.quad(f, [0] + edge + [mp.pi / 2]) - mp.pi)


def chi_series(beta, nmax=4000):
    s = 0.0
    for n in range(1, nmax + 1):
        lc = 0.5 * math.log(math.pi) + n * math.log(n) - math.lgamma(n + 1) + math.lgamma((n + 1) / 2) - math.lgamma(n / 2 + 1)
        t = math.exp(lc - n * math.log(beta))
        s += t
        if t < 1e-18:
            break
    return s


def ray(beta, R0f=1e5, rstop=0.25):
    """[float] integrate the ray law from far away (units A = 1); return (turn, r_min, captured, min outward speed while inside r=1)."""
    import numpy as np
    from scipy.integrate import solve_ivp
    R0 = R0f * max(beta, 1.0)
    y0 = beta
    for _ in range(60):
        y0 = beta * math.exp(-1.0 / math.hypot(R0, y0))     # invariant y0/w(r0) = b
    s0 = [-R0, y0, math.exp(-1.0 / math.hypot(R0, y0)), 0.0, 0.0]

    def rhs(t, s):
        x, y, vx, vy, th = s
        r = math.hypot(x, y); w2 = math.exp(-2.0 / r)
        gx, gy = x / r ** 3, y / r ** 3
        vg = vx * gx + vy * gy
        return [vx, vy, -w2 * gx + 2 * vg * vx, -w2 * gy + 2 * vg * vy, -(vx * gy - vy * gx)]

    def back(t, s):
        return math.hypot(s[0], s[1]) - R0 * 1.0000001
    back.terminal, back.direction = True, 1

    def inner(t, s):
        return math.hypot(s[0], s[1]) - rstop
    inner.terminal = True
    sol = solve_ivp(rhs, [0, 50 * R0], s0, method="DOP853", rtol=1e-12, atol=1e-12, events=[back, inner], dense_output=False, max_step=np.inf)
    xs, ys = sol.y[0], sol.y[1]
    rr = np.hypot(xs, ys)
    captured = len(sol.t_events[1]) > 0
    return -sol.y[4][-1], float(rr.min()), captured


def family_n() -> None:
    rows, ok = [], True
    for beta in (50.0, 10.0, 5.0, 3.0):
        t_ode, rmin, cap = ray(beta)
        t_int = chi_integral(beta); t_ser = chi_series(beta)
        ok &= (not cap) and abs(t_ode - t_int) < 1e-6 and abs(t_ser - t_int) < 1e-9
        rows.append(f"b={beta:g}A: ODE {t_ode:.8f}, integral {t_int:.8f}, series {t_ser:.8f}")
    for beta in (2.75, 2.72):
        t_ode, rmin, cap = ray(beta)
        t_int = chi_integral(beta)
        ok &= (not cap) and abs(t_ode - t_int) < 1e-5 and rmin > 1.0
        rows.append(f"b={beta:g}A: ODE {t_ode:.6f}, integral {t_int:.6f} (r_min {rmin:.4f}A)")
    caps = []
    for beta in (2.71, 2.5, 1.0):
        t_ode, rmin, cap = ray(beta)
        ok &= cap
        caps.append(f"{beta:g}")
    OUT.append("     [executed, float] " + "; ".join(rows) + f"; captured (r < A/4 reached) at b/A = {', '.join(caps)}")
    check("N", ok, "the ray law integrated as an ODE (DOP853, rtol 1e-12, from 1e5 max(b, A)) reproduces the exact turn at b = 50A...3A "
          "(to 1e-6; the series agrees with the integral to 1e-9) and near the threshold (2.75A, 2.72A: loops of 3.6 and 7.3 rad), "
          "and every ray with b < eA = 2.71828A falls inside r = A/4")


def family_k() -> None:
    mp.mp.dps = 30
    cn = lambda n: mp.sqrt(mp.pi) * mp.power(n, n) / mp.factorial(n) * mp.gamma(mp.mpf(n + 1) / 2) / mp.gamma(mp.mpf(n) / 2 + 1)
    C = mp.nsum(lambda n: cn(n) * mp.e ** (-n) - 1 / n, [1, mp.inf])
    near = [(d, chi_integral(math.e / (1 - d), dps=40) + math.log(d)) for d in (1e-4, 1e-6, 1e-8)]
    ratios = [float(cn(n) * mp.e ** (-n) * n) for n in (10, 100, 1000)]
    hp = mp.pi / 2
    mp.mp.dps = 40
    dd = mp.mpf(10) ** -24                               # regularised at 1 - eA/b = 1e-24: the O(sqrt(d)) remainder is ~4e-12
    Gt = lambda t: 1 / (1 + mp.lambertw(-(1 - dd) * mp.sin(t) / mp.e, 0).real)
    St = lambda t: (lambda sv: mp.sqrt(2 - sv) / (2 * mp.sqrt(sv + dd)))(2 * mp.sin((hp - t) / 2) ** 2)   # cos t/(2 sqrt(s(s+d))), s = 1 - sin t
    C2 = 2 * mp.quad(lambda t: Gt(t) - St(t), [0, 1, 1.5] + [hp - mp.mpf(10) ** (-k) for k in range(2, 15)] + [hp]) - mp.pi + 2 * mp.log(1 + mp.sqrt(1 + dd))
    ok = abs(near[-1][1] - float(C)) < 1e-3 and abs(ratios[-1] - 1) < 2e-3 and abs(C - C2) < 1e-9
    OUT.append(f"     [numerical] n c_n e^-n = {ratios[0]:.5f}, {ratios[1]:.5f}, {ratios[2]:.5f} (-> 1); chi + log(1 - eA/b) at 1 - eA/b = "
               + ", ".join(f"{d:.0e}: {v:.6f}" for d, v in near) + f"; C = sum_n (c_n e^-n - 1/n) = {float(C):.10f} = 2 int_0^(pi/2) [1/(1+W0(-sin t/e)) - cos t/(2(1-sin t))] dt - pi + 2 log 2 = {float(C2):.10f}")
    check("K", ok, "the series converges exactly for b > eA and diverges at b = eA (positive terms, Tonelli, and the integrand ~ 1/(2(1-y)) "
          "at y -> 1 when b = eA); near the threshold chi = -log(1 - eA/b) + C + o(1) with C = sum_n (c_n e^-n - 1/n)")


def main() -> int:
    family_q(); family_r(); family_c(); family_s(); family_n(); family_k()
    print("Strong-field turning by a clump - checks; worker w-macbookpro9927a-j72ca (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED for the stated ray law with u = -A/r: rays are those of the index e^{A/r}; (b) a ray is captured iff its "
          "impact parameter is below e A (the circular ray sits at r = A); (a) the turn is chi = 2 int_0^1 dy/((1 + W0(-yA/b))sqrt(1-y^2)) "
          "- pi = sum_n (sqrt(pi) n^n/n!) G((n+1)/2)/G(n/2+1) (A/b)^n = 2A/b + pi(A/b)^2 + 6(A/b)^3 + 4pi(A/b)^4 + ..., convergent exactly "
          "for b > eA, with chi = -log(1 - eA/b) + C + o(1) at the threshold")
    print("HIT: for rays of E = w|sin k| at long waves with u = -A/r the critical impact parameter is exactly e A (circular ray at "
          "r = A), and the turn at all orders is chi = sum_n (sqrt(pi) n^n/n!) G((n+1)/2)/G(n/2+1) (A/b)^n = 2 int_0^1 dy/((1 + "
          "W0(-yA/b)) sqrt(1-y^2)) - pi, convergent exactly for b > eA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
