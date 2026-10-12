"""R15-4 (a, extra): the linear reader through e+e- annihilation (during BBN), content that is NOT a sum of x=3,4 exponentials.

Content: photons + e+e- (in equilibrium, entropy conserved: (s_gamma+s_e) a^3 = const) + 3 neutrino species decoupled
before annihilation (rho_nu = 3 (7/8)(pi^2/15) T_nu^4, T_nu = 1/a in MeV, instant decoupling: a standard idealisation).
Baryons/dark matter neglected (rho_m/rho_r < 1e-4 at T > 10 keV). Vacuum invisible (only E = -d rho/du = 3(rho+p) enters).
Reader: D1 (and D2, D3 for comparison), registers started in equilibrium with pure radiation at T = 30 MeV.
Output: eps(T) = rho_hat/rho_nc - 1 (subtraction: rho_nc = rho_gamma + rho_e + rho_nu exactly), and the equivalent
Delta N_eff := eps * rho_nc / rho_1nu (one neutrino species), for T in [1, 0.07] MeV (BBN) and at T = 0.01 MeV.
Comparator (RECALLED): BBN+CMB Delta N_eff ~ 0.3 (2 sigma scale).
"""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r154_reader import DESIGNS

me = 0.511
c4 = np.pi ** 2 / 15


def e_thermo(T):
    if T < me / 60:
        return 0.0, 0.0
    f = lambda E: 1 / (np.exp(E / T) + 1)
    rho = 4 / (2 * np.pi ** 2) * quad(lambda E: E ** 2 * np.sqrt(E * E - me * me) * f(E), me, me + 60 * T, limit=200)[0]
    p = 4 / (6 * np.pi ** 2) * quad(lambda E: (E * E - me * me) ** 1.5 * f(E), me, me + 60 * T, limit=200)[0]
    return rho, p


def s_tot(T):
    re, pe = e_thermo(T)
    return 4 / 3 * c4 * T ** 3 + (re + pe) / T


T0 = 30.0
a0 = 1 / T0
S0 = s_tot(T0) * a0 ** 3
ugrid = np.linspace(np.log(a0), np.log(1 / 0.005), 4001)
Ts, rho, E = [], [], []
Tg = T0
for u in ugrid:
    a = np.exp(u)
    Tg = brentq(lambda T: s_tot(T) * a ** 3 - S0, 0.2 / a, 2.0 / a)
    re, pe = e_thermo(Tg)
    rg = c4 * Tg ** 4
    rn = 3 * 7 / 8 * c4 * (1 / a) ** 4
    Ts.append(Tg); rho.append(rg + re + rn); E.append(3 * (4 / 3 * rg + re + pe + 4 / 3 * rn))
Ts, rho, E = map(np.array, (Ts, rho, E))
print(f'# check: T_gamma/T_nu at the end = {Ts[-1]*np.exp(ugrid[-1]):.5f} (expected (11/4)^(1/3) = {(11/4)**(1/3):.5f})')
from scipy.interpolate import CubicSpline
Ei = CubicSpline(ugrid, E)
from r154_lagfree_scan import solve, stats
EXTRA = {}
for bs, cons in (((10, 12, 14), [('G', 3), ('G', 4), ('dG', 4)]), ((10, 12), [('G', 3), ('G', 4)]),
                 ((20, 24), [('G', 3), ('G', 4)]), ((40, 48), [('G', 3), ('G', 4)])):
    b_, k_ = solve(bs, cons)
    Hmin, TK, g75, g3, lag = stats(b_, k_)
    print(f'# fast design beta={bs} ({len(cons)} constraints): k={np.round(k_, 2)}, min H={Hmin:+.2e} (positive {Hmin >= -1e-12}), T_K={TK:.3f}, G(0.75)={g75:.3f}')
    EXTRA[f'F beta={bs}'] = (b_, k_)
for name, (b, k) in list(DESIGNS.items()) + list(EXTRA.items()):
    y0 = 4 * rho[0] / (b - 4)
    sol = solve_ivp(lambda u, y: Ei(u) - b * y, (ugrid[0], ugrid[-1]), y0, t_eval=ugrid, rtol=1e-10, atol=1e-30,
                    method='DOP853', max_step=min(0.005, 0.2 / b.max()))
    rh = k @ sol.y
    eps = rh / rho - 1
    r1nu = 7 / 8 * c4 * np.exp(-4 * ugrid)
    dN = eps * rho / r1nu
    bbn = (Ts <= 1.0) & (Ts >= 0.07)
    i_end = -1
    xeff = E / rho
    print(f'reader {name}: x_eff = E/rho min over run = {xeff.min():.4f} (at T={Ts[xeff.argmin()]:.3f} MeV)')
    print(f'   BBN window T in [0.07,1] MeV: max|eps| = {np.max(np.abs(eps[bbn])):.3e}, eps range [{eps[bbn].min():+.3e}, {eps[bbn].max():+.3e}];'
          f' equivalent Delta N_eff range [{dN[bbn].min():+.3f}, {dN[bbn].max():+.3f}]')
    for Tq in (3.0, 1.0, 0.5, 0.2, 0.1, 0.07, 0.03, 0.01):
        i = np.argmin(np.abs(Ts - Tq))
        print(f'     T={Ts[i]:.3f} MeV: eps={eps[i]:+.3e}, Delta N_eff equiv={dN[i]:+.4f}')
