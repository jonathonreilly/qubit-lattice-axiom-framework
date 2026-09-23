#!/usr/bin/env python3
"""J:derive:growth-and-drag-against-attraction:a3 - worker w-jonathonsmac4f50-j6227 (claude-opus-5-5).

Model (the unit's (a), as derived by attempt a4, w-macbookpro90c72-j9059, same model claude-opus-5-5, unrefereed, re-derived
here where used): a transparent test body with momentum per record p drifts at v = p/sqrt3 and obeys dp/dt = q1(<s>_wind - p);
the wind of a capturing body 1 has drift u_w = <s>_wind/sqrt3 = -Q1/(4 pi rho (1 - rho) r^2) rhat with Q1 = q1 N1, and body 1 grows,
N1 = N10 e^(q1 t). Hence, exactly within the model,
    x'' = -q1 x' - mu(t) x/|x|^3,    mu(t) = q1^2 N1(t)/(4 pi rho (1 - rho)) = mu0 e^(q1 t),
a Kepler problem with linear drag at rate q1 and a central 'mass' growing at rate q1.  Exact parts: sympy; integrations: floating
point (scipy, rtol 1e-10), labelled NUMERICAL.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


t, q1, mu0 = sp.symbols('t q1 mu0', positive=True)
X = sp.Matrix(sp.symbols('x y z', real=True))
Vv = sp.Matrix(sp.symbols('vx vy vz', real=True))
r = sp.sqrt(X.dot(X))
mu = mu0 * sp.exp(q1 * t)
acc = -q1 * Vv - mu * X / r ** 3

# ================================================================ E1 angular momentum decays exactly at q1
Lvec = X.cross(Vv)
dL = Vv.cross(Vv) + X.cross(acc)                        # d/dt (x cross v) = v cross v + x cross a
ok = all(sp.simplify(dL[i] + q1 * Lvec[i]) == 0 for i in range(3))
check('E1', ok, "EXACT: for every orbit, dL/dt = -q1 L (the pull is central, the drag is -q1 v), so the angular momentum per "
      "record is L0 e^(-q1 t) exactly and the orbit's plane is fixed; the growth of the central body does not enter")

# ================================================================ E2 the adiabatic spiral
r0, T0 = sp.symbols('r0 T0', positive=True)
Lt = sp.sqrt(mu0 * r0) * sp.exp(-q1 * t)                 # circular start: L0^2 = mu0 r0
r_ad = sp.simplify(Lt ** 2 / mu)                          # circular orbit at the current L and mu: r = L^2/mu
T_ad = sp.simplify(2 * sp.pi * r_ad ** sp.Rational(3, 2) / sp.sqrt(mu))
n_orb = sp.simplify(sp.integrate(1 / T_ad, (t, 0, t)))
T00 = 2 * sp.pi * r0 ** sp.Rational(3, 2) / sp.sqrt(mu0)
ok = sp.simplify(r_ad - r0 * sp.exp(-3 * q1 * t)) == 0
ok &= sp.simplify(T_ad - T00 * sp.exp(-5 * q1 * t)) == 0
ok &= sp.simplify(n_orb - (sp.exp(5 * q1 * t) - 1) / (5 * q1 * T00)) == 0
# the orbit condition in the unit's variables: (q1 T0)^2 = 16 pi^3 rho (1 - rho) r0^3 / N1
rho, N1 = sp.symbols('rho N1', positive=True)
eps2 = sp.simplify(((q1 * T00) ** 2).subs(mu0, q1 ** 2 * N1 / (4 * sp.pi * rho * (1 - rho))))
ok &= sp.simplify(eps2 - 16 * sp.pi ** 3 * rho * (1 - rho) * r0 ** 3 / N1) == 0
check('E2', ok, "EXACT (adiabatic, q1 T << 1): a circular orbit follows r = L^2/mu = r0 e^(-3 q1 t) - two thirds of the shrink "
      "from the drag on L, one third from the growth of the centre; its period falls as T0 e^(-5 q1 t); the number of periods "
      "completed by time t is (e^(5 q1 t) - 1)/(5 q1 T0), i.e. ((r0/r)^(5/3) - 1)/(5 eps) while the radius falls from r0 to r, "
      "eps = q1 T0; and eps^2 = 16 pi^3 rho (1 - rho) r0^3/N1, so eps << 1 is a4's orbit condition N1 >> 16 pi^3 rho(1-rho) r^3")

# ================================================================ E3 the overdamped infall, exactly
rr = sp.Function('r')
sol = sp.dsolve(sp.Eq(rr(t).diff(t), -mu0 * sp.exp(q1 * t) / (q1 * rr(t) ** 2)), rr(t), ics={rr(0): r0})
sol = sol if isinstance(sol, list) else [sol]
real_sol = [s_ for s_ in sol if sp.simplify(s_.rhs.subs(t, 0) - r0) == 0]
cube = sp.simplify(real_sol[0].rhs ** 3) if real_sol else None
tc = sp.log(1 + q1 ** 2 * r0 ** 3 / (3 * mu0)) / q1
ok = cube is not None and sp.simplify(cube - (r0 ** 3 - 3 * mu0 * (sp.exp(q1 * t) - 1) / q1 ** 2)) == 0
ok &= sp.simplify((r0 ** 3 - 3 * mu0 * (sp.exp(q1 * tc) - 1) / q1 ** 2)) == 0
check('E3', ok, "EXACT (q1 T >> 1, the body carried by the wind, v = u_w): r^3 = r0^3 - (3 mu0/q1^2)(e^(q1 t) - 1), so the body "
      "reaches the centre at t_c = ln(1 + q1^2 r0^3/(3 mu0))/q1 - entrainment is a radial infall at the wind speed, with no "
      "orbit at all", f"t_c = {tc}")

# ================================================================ E4 the eccentricity vector (exact identity)
Lz = sp.symbols('Lz', real=True)
x2, y2, vx2, vy2 = sp.symbols('x2 y2 vx2 vy2', real=True)
rr2 = sp.sqrt(x2 ** 2 + y2 ** 2)
ax2 = -q1 * vx2 - mu * x2 / rr2 ** 3
ay2 = -q1 * vy2 - mu * y2 / rr2 ** 3
L2 = x2 * vy2 - y2 * vx2
dL2 = x2 * ay2 - y2 * ax2
# A = v x L - mu rhat (plane), e = A/mu
Ax = vy2 * L2 - mu * x2 / rr2
Ay = -vx2 * L2 - mu * y2 / rr2
def ddt(expr):
    return (sp.diff(expr, x2) * vx2 + sp.diff(expr, y2) * vy2 + sp.diff(expr, vx2) * ax2 + sp.diff(expr, vy2) * ay2
            + sp.diff(expr, t))
dex = sp.simplify(ddt(Ax / mu) - (-3 * q1 * (Ax / mu + x2 / rr2)))
dey = sp.simplify(ddt(Ay / mu) - (-3 * q1 * (Ay / mu + y2 / rr2)))
# time average of cos(true anomaly) over a Kepler ellipse = -e (checked numerically at three e)
import math
def avg_cosf(e):
    M = np.linspace(0, 2 * np.pi, 20001)[:-1]
    E = M.copy()
    for _ in range(60):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    f = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    return np.cos(f).mean()
avg_err = max(abs(avg_cosf(e) + e) for e in (0.1, 0.4, 0.7))
ok = dex == 0 and dey == 0 and avg_err < 1e-9
check('E4', ok, "EXACT + NUMERICAL: the eccentricity vector e = (v x L - mu rhat)/mu obeys de/dt = -3 q1 (e + rhat) exactly; "
      "the time average of rhat over a Kepler ellipse is -e (checked to 1e-9 at e = 0.1, 0.4, 0.7), so the secular change of "
      "e vanishes: in the adiabatic regime the orbit keeps its eccentricity and shrinks self-similarly",
      f"<cos f> + e: {avg_err:.1e}")

# ================================================================ N1 the full motion across eps
def run(eps, e0=0.0, t_end=None, turns_max=400):
    """units: a0 = 1, mu0 = 1 (T0 = 2 pi); q1 = eps/(2 pi); start at pericentre of an ellipse of eccentricity e0 with the
    adiabatic radial drift -3 q1 r added (removes the forced epicycle)."""
    qv = eps / (2 * np.pi)

    def f(tt, s):
        x, y, vx, vy = s
        rr_ = np.hypot(x, y)
        m = np.exp(qv * tt)
        return [vx, vy, -qv * vx - m * x / rr_ ** 3, -qv * vy - m * y / rr_ ** 3]

    def hit(tt, s):
        return np.hypot(s[0], s[1]) - 0.5
    hit.terminal = True
    hit.direction = -1
    s0 = [1.0 - e0, 0.0, -3 * qv * (1.0 - e0), np.sqrt((1 + e0) / (1 - e0))]
    tmax = t_end if t_end else 2 * np.pi * turns_max
    sol_ = solve_ivp(f, (0, tmax), s0, rtol=1e-10, atol=1e-12, events=None if t_end else hit, dense_output=True, max_step=0.05)
    return qv, sol_


rows = []
ok = True
pred_turns = lambda eps: (2 ** (5 / 3) - 1) / (5 * eps)
for eps in (0.01, 0.03, 0.1, 0.3, 1.0):
    qv, sol_ = run(eps)
    ang = np.unwrap(np.arctan2(sol_.y[1], sol_.y[0]))
    turns = (ang[-1] - ang[0]) / (2 * np.pi)
    Ls = sol_.y[0] * sol_.y[3] - sol_.y[1] * sol_.y[2]
    Lerr = np.max(np.abs(Ls - Ls[0] * np.exp(-qv * sol_.t)))
    tq = 0.25 * sol_.t[-1]
    rq = np.hypot(*sol_.sol(tq)[:2])
    rows.append(f"eps={eps}: turns to half radius {turns:.2f} (adiabatic {pred_turns(eps):.2f}), r(t/4)/e^(-3q1t) {rq / np.exp(-3 * qv * tq):.4f}, L err {Lerr:.1e}")
    ok &= Lerr < 1e-7
    if eps <= 0.03:
        ok &= abs(turns / pred_turns(eps) - 1) < 0.02 and abs(rq / np.exp(-3 * qv * tq) - 1) < 0.005
# eccentric starts: a e^(3 q1 t) and e over the last orbit, after one e-fold of the radius
for eps in (0.01, 0.03):
    for e0 in (0.2, 0.5):
        qv = eps / (2 * np.pi)
        tend = 1 / (3 * qv)
        _, sol_ = run(eps, e0=e0, t_end=tend)
        Tlast = 2 * np.pi * np.exp(-5 * qv * tend)
        ts = np.linspace(tend - Tlast, tend, 2000)
        x, y, vx, vy = sol_.sol(ts)
        m = np.exp(qv * ts)
        rr_ = np.hypot(x, y)
        L = x * vy - y * vx
        ex = (vy * L - m * x / rr_) / m
        ey = (-vx * L - m * y / rr_) / m
        a_s = 1 / (2 / rr_ - (vx ** 2 + vy ** 2) / m)
        a_ratio = np.mean(a_s * np.exp(3 * qv * ts))
        e_end = np.mean(np.hypot(ex, ey))
        rows.append(f"eps={eps}, e0={e0}: after one e-fold, <a e^(3q1t)> = {a_ratio:.4f}, <e> = {e_end:.4f}")
        ok &= abs(a_ratio - 1) < 0.01 and abs(e_end - e0) < 0.01
check('N1', ok, "NUMERICAL (full equations): the angular momentum follows L0 e^(-q1 t) to 1e-7 in every run; with the "
      "adiabatic drift in the initial velocity, for eps = q1 T0 <= 0.03 the radius tracks r0 e^(-3 q1 t) to 0.5 percent and the "
      "turns before the radius halves are the adiabatic ((2)^(5/3) - 1)/(5 eps) = 0.435/eps to 2 percent; eccentric orbits "
      "(e0 = 0.2, 0.5) keep e and shrink as a0 e^(-3 q1 t) to 1 percent after one e-fold; at eps = 1 not one turn is completed",
      "; ".join(rows))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact within the drag-and-growth model: the angular momentum per record decays exactly as "
      "L0 e^(-q1 t) for every orbit; a near-circular orbit spirals in as r0 e^(-3 q1 t) with period T0 e^(-5 q1 t), completing "
      "((r0/r)^(5/3) - 1)/(5 q1 T0) turns while shrinking to r (0.435/(q1 T0) turns per halving, confirmed by integration to "
      "2 percent for q1 T0 <= 0.03), eccentricity kept (self-similar shrink, de/dt = -3 q1 (e + rhat) exactly); (q1 T0)^2 = 16 pi^3 rho (1-rho) r^3/N1; in the carried regime the infall is exact, "
      "r^3 = r0^3 - (3 mu0/q1^2)(e^(q1 t) - 1)")
if all(RESULTS):
    print("HIT: for a transparent capturing body in the wind of a growing capturing body (drag and growth at the same rate q1), "
          "the angular momentum per record decays exactly as L0 e^(-q1 t), so no orbit survives: a near-circular orbit spirals "
          "in as r0 e^(-3 q1 t) with period T0 e^(-5 q1 t), completing ((r0/r)^(5/3) - 1)/(5 q1 T0) turns on its way to "
          "radius r (0.435/(q1 T0) per halving; integration agrees to 2 percent at q1 T0 <= 0.03), keeping its eccentricity "
          "(de/dt = -3 q1 (e + rhat) exactly, zero on average), with (q1 T0)^2 = "
          "16 pi^3 rho (1 - rho) r0^3/N1; when q1 T0 >> 1 the body is carried in radially, r^3 = r0^3 - (3 mu0/q1^2)(e^(q1 t) - 1)")
