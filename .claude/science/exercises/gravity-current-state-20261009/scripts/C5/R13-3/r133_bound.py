"""R13-3 (c): bound regions in V3 + creation.

(1) Exact EdS top-hat: circular orbital period at the virial radius vs the cosmic age at collapse.
(2) LCDM (Omega_m = 0.3) collapse today: numerical spherical collapse -> Delta_vir, T_orb(r_vir) H0, t0 H0.
(3) Unit-lapse normals in the top-hat: theta_n = 3 H_loc -> -infinity at t_coll (closed-FRW interior, cycloid).
(4) Focusing estimate for normals entering a virialized halo (Raychaudhuri lower bound on R_nn).
(5) Best achievable P-T filter error at a given T_orb*H (n-th order low-pass vs lag H*tau).
Subtraction rule: no tail clause. 'Delta_vir' is relative to the background matter density at collapse
(EdS) or to the critical density (LCDM, stated); orbital periods are circular-orbit periods at r_vir.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

# (1) EdS exact
G, t = sp.symbols('G t', positive=True)
rho_bg = 1 / (6 * sp.pi * G * t**2)            # EdS background density
Delta = 18 * sp.pi**2                           # top-hat virial overdensity at t_coll (vs background)
T_orb = 2 * sp.pi / sp.sqrt(sp.Rational(4, 3) * sp.pi * G * Delta * rho_bg)
print('(1) EdS top-hat: T_orb(r_vir)/t_coll =', sp.simplify(T_orb / t), '(exact)')
print('    with t_coll = 2/(3H): T_orb * H(t_coll) =', sp.nsimplify(sp.Rational(2, 3)))
print('    generic Delta_c (vs critical): T_orb*H = 2*pi*sqrt(2/Delta_c); Delta_c=200 ->',
      float(2 * np.pi * np.sqrt(2 / 200)))

# (2) LCDM spherical collapse at z = 0, Omega_m = 0.3, H0 = 1
Om, OL = 0.3, 0.7
Hf = lambda a: np.sqrt(Om / a**3 + OL)
t0 = quad(lambda a: 1 / (a * Hf(a)), 1e-8, 1.0)[0]


def collapse_time(delta_i, a_i=1e-3):
    # shell radius R (units: R_i = a_i), Rddot = -Om/(2 R^3)*M_eff + OL*R ; M chosen so interior density = (1+delta_i)*bg
    Mi = Om * (1 + delta_i) / 2  # GM = (Om/2) H0^2 (1+delta) R_i^3 / a_i^3 with R_i = a_i
    ti = quad(lambda a: 1 / (a * Hf(a)), 1e-8, a_i)[0]
    # growing-mode velocity: v = H R (1 - delta_i/3)
    y0 = [a_i, Hf(a_i) * a_i * (1 - delta_i / 3)]

    def rhs(tt, y):
        return [y[1], -Mi / y[0]**2 + OL * y[0]]
    ev = lambda tt, y: y[0] - 1e-4 * a_i
    ev.terminal = True
    sol = solve_ivp(rhs, [ti, 5 * t0], y0, events=ev, rtol=1e-10, atol=1e-14, max_step=0.01)
    Rmax = sol.y[0].max()
    return (sol.t_events[0][0] if len(sol.t_events[0]) else np.inf), Rmax, Mi


di = brentq(lambda d: collapse_time(d)[0] - t0, 1e-4, 1e-2)
tc, Rmax, Mi = collapse_time(di)
Rvir = Rmax / 2  # standard virial-radius approximation (no Lambda correction to r_vir; stated)
rho_vir = Mi / (4 * np.pi / 3 * Rvir**3) * (3 / (4 * np.pi))  # in units where G rho -> use GM directly
# circular period at Rvir: T = 2 pi sqrt(R^3/(GM)), GM = Mi in H0 units
Tvir = 2 * np.pi * np.sqrt(Rvir**3 / Mi)
rho_c = 3 / (8 * np.pi)          # G = 1, H0 = 1
GM_over = Mi                     # G M
Delta_c = (GM_over / (4 * np.pi / 3 * Rvir**3)) / rho_c
print(f'(2) LCDM Om=0.3, collapse today: delta_i(a=1e-3)={di:.5f}; t0 H0={t0:.4f}; Delta_vir/critical={Delta_c:.1f} '
      f'(Bryan-Norman RECALLED: 101.1); T_orb(r_vir) H0={Tvir:.4f}; T_orb/t0={Tvir/t0:.3f}')

# (3) top-hat interior normals: closed FRW cycloid, theta = 3 Rdot/R
eta = np.array([np.pi * 0.5, np.pi, 1.5 * np.pi, 1.9 * np.pi, 1.99 * np.pi, 1.999 * np.pi])
# R = A(1-cos eta), t = B(eta - sin eta); theta*t_coll  with t_coll = 2 pi B
th = 3 * np.sin(eta) / (1 - np.cos(eta)) / 1.0  # theta in units of 1/B
print('(3) top-hat normals (comoving with dust): eta/pi, t/t_coll, theta*t_coll =')
for e, v in zip(eta, th):
    print(f'      {e/np.pi:.3f}  {(e-np.sin(e))/(2*np.pi):.5f}  {v*2*np.pi:+.4e}')
print('    theta -> -inf as t -> t_coll: the unit-lapse foliation has a point caustic at collapse (exact).')

# (4) normals entering a Delta=200 (vs critical) halo with theta_entry = 3H: time until theta < 0 under R_nn >= 4 pi G rho_vir
Dc = 200.0
tneg = 3.0 / (4 * np.pi * Dc * 3 / (8 * np.pi))   # in units of 1/H : 3H / (4 pi G Dc rho_c)
tff = 1 / np.sqrt(4 * np.pi * Dc * 3 / (8 * np.pi))  # 1/sqrt(4 pi G rho_vir) in units 1/H
Tc = 2 * np.pi * np.sqrt(2 / Dc)
print(f'(4) Delta_c=200 halo: theta_n turns negative after {tneg:.4f}/H; then |theta| grows; Raychaudhuri caustic '
      f'within ~ pi/2 * 1/sqrt(4 pi G rho_vir) = {np.pi/2*tff:.4f}/H (lower-bound R_nn, sigma >= 0); '
      f'crossing time ~ T_orb/4 = {Tc/4:.4f}/H.')
# check (4) by integrating theta' = -theta^2/3 - 4 pi G rho_vir from theta = 3 (H units)
k2 = 4 * np.pi * Dc * 3 / (8 * np.pi)
sol = solve_ivp(lambda s, y: [-y[0]**2 / 3 - k2], [0, 2], [3.0], events=lambda s, y: y[0] + 1e6, rtol=1e-10,
                max_step=1e-4)
print(f'    integrated: theta from +3H reaches -1e6 H at t = {sol.t_events[0][0]:.4f}/H (< crossing time {Tc/4:.4f}/H)')

# (5) filter error floor: n-th order low-pass, lag error ~ H tau, ripple ~ (T H/(2 pi H tau))^n
for TH, lab in ((2 / 3, 'EdS r_vir'), (Tvir, 'LCDM z=0 r_vir'), (0.2, 'r ~ r_vir/5 (rho x 125 for SIS-like... T ~ r)')):
    out = []
    for n in (1, 2, 4, 8):
        f = lambda e: e - (TH / (2 * np.pi * e))**n
        e = brentq(f, 1e-6, 10)
        out.append(f'n={n}: {e:.3f}')
    print(f'(5) T_orb*H={TH:.3f} ({lab}): minimal max(lag, ripple) =', '; '.join(out))
