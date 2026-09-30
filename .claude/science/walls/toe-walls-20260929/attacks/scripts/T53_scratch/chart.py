"""T53 scratch: repo chart, copied (not imported) from
scripts/frontier_pmns_theta23_upper_octant_chamber_closure_prediction.py:104-158  (main_wt, read-only).
Extra: general-sheet observables with PDG extraction of (s12^2, s13^2, s23^2, dCP)."""
import math
import numpy as np
from scipy.optimize import fsolve, brentq

E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
SQ = math.sqrt(8.0 / 3.0)          # chamber constant
T_M = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
T_D = np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]], dtype=complex)
T_Q = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=complex)


def H(m, d, q, gamma=0.5):
    HB = np.array([[0, E1, -E1 - 1j * gamma],
                   [E1, 0, -E2],
                   [-E1 + 1j * gamma, -E2, 0]], dtype=complex)
    return HB + m * T_M + d * T_D + q * T_Q


def obs(m, d, q, gamma=0.5, perm=(2, 1, 0)):
    w, V = np.linalg.eigh(H(m, d, q, gamma))
    o = np.argsort(w.real)
    V = V[:, o]
    P = V[list(perm), :]
    a = np.abs(P) ** 2
    s13 = a[0, 2]
    c13 = 1 - s13
    s12 = a[0, 1] / c13
    s23 = a[1, 2] / c13
    J = (P[0, 0] * np.conj(P[0, 1]) * np.conj(P[1, 0]) * P[1, 1]).imag
    c12, c23 = 1 - s12, 1 - s23
    D = math.sqrt(s12 * c12 * s23 * c23 * s13) * math.sqrt(c13) * 1.0  # placeholder, exact below
    # PDG: J = c12 s12 c23 s23 c13^2 s13' sin d  with s13' = sqrt(s13)
    Dn = math.sqrt(s12 * c12) * math.sqrt(s23 * c23) * (c13) * math.sqrt(s13)
    sind = J / Dn
    # |U_tau1|^2 = s12 s23 + c12 c23 s13 - 2 sqrt(s12 c12 s23 c23 s13) cos d   (squares of sines are s12 etc.)
    cosd = (s12 * s23 + c12 * c23 * s13 - a[2, 0]) / (2 * math.sqrt(s12 * c12 * s23 * c23 * s13))
    dcp = math.degrees(math.atan2(sind, cosd)) % 360.0
    return dict(s12=s12, s13=s13, s23=s23, J=J, sind=sind, cosd=cosd, dcp=dcp,
                chamber=q + d - SQ)


def preimage(s12t, s13t, x0=None):
    """Basin-1 chamber-boundary preimage (m,d), q = SQ - d, of the target (s12^2, s13^2).
    Multistart over the box m in [0.55,0.85], d in [0.88,0.98] (contains the repo's box B);
    returns the roots found (list) so uniqueness in the box can be checked."""
    def f(x):
        o = obs(x[0], x[1], SQ - x[1])
        return [o['s12'] - s12t, o['s13'] - s13t]
    roots = []
    for m0 in np.linspace(0.55, 0.85, 7):
        for d0 in np.linspace(0.88, 0.98, 6):
            x, info, ier, msg = fsolve(f, [m0, d0], xtol=1e-14, full_output=True)
            if max(abs(v) for v in f(x)) < 1e-10 and 0.5 < x[0] < 0.9 and 0.85 < x[1] < 1.0:
                if not any(np.allclose(x, r, atol=1e-7) for r in roots):
                    roots.append(x)
    return roots


if __name__ == '__main__':
    # anchor check: repo pin (0.657061342210, 0.933806343759, 0.715042329587) -> (0.307,0.0218,0.545), dCP 260.88
    o = obs(0.657061342210, 0.933806343759, 0.715042329587)
    print('anchor', {k: round(v, 6) for k, v in o.items()})
