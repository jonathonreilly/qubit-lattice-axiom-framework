"""Candidate formula surface. Mutants change this file, never reference tests."""
import numpy as np
from scipy.integrate import solve_ivp

ORIGIN_COEFFICIENT = -0.5
HALF_DENSITY_POWER = 0.5
FLOW_V_POWER = 0
GAUGE_OFFSET = 0.5
SHIFT_ORIENTATION = 1
ROUND_GEOMETRY = True
ROUND_FUNCTION = np.rint


def energy(q, a, m, v):
    return np.sqrt(m*m + 4*v*v*np.sin(a*np.asarray(q)/2)**2/a**2)


def derivative(q, a, m, v):
    return v*v*np.sin(a*np.asarray(q))/(a*energy(q, a, m, v))


def endpoint(q, s, a, m, v):
    q = np.asarray(q, dtype=float)
    if s == 0:
        return q.copy(), {"nfev": 0, "success": True}
    sol = solve_ivp(lambda _t, x: v**FLOW_V_POWER*energy(x, a, m, v),
                    (0.0, float(s)), q, method="DOP853", t_eval=[s],
                    rtol=2e-12, atol=2e-13)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1], {"nfev": sol.nfev, "success": sol.success}


def transport(q, s, a, m, v, f, centered=False):
    F, info = endpoint(q, s, a, m, v)
    ratio = energy(F, a, m, v)/energy(q, a, m, v)
    origin = 0.0 if centered else ORIGIN_COEFFICIENT
    value = ratio**HALF_DENSITY_POWER*np.exp(-1j*origin*a*(F-q))*f(F)
    return value, F, info


def gauge_frequency(n, length):
    return 2*np.pi*(n+GAUGE_OFFSET)/length


def gauge_cycle_phase():
    return np.exp(-2j*np.pi*GAUGE_OFFSET)


def geometric_phase(q, a, y):
    n = ROUND_FUNCTION(y/a) if ROUND_GEOMETRY else y/a
    return np.exp(-1j*SHIFT_ORIENTATION*a*n*np.asarray(q))

