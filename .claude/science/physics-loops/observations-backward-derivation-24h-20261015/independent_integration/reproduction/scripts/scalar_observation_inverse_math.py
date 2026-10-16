"""Pure symbolic/analytic helpers for the conditional scalar inverse note.

These functions supply candidate mathematics, not physical measurement models.
No file reads, fits, observational inputs or action-selection rules occur here.
"""
from __future__ import annotations

import sympy as s


def spherical_geometry(r, lapse, radial):
    ellp = s.diff(lapse, r) / lapse
    bp = s.diff(radial, r)
    gt = (radial - 1) / r**2 + bp / r
    gr = (radial - 1) / r**2 + 2 * radial * ellp / r
    ga = radial * (s.diff(ellp, r) + ellp**2 + ellp / r) + bp * (ellp + 1 / r) / 2
    d = radial * (1 / r - ellp)
    return gt, gr, ga, d


def vacuum_inverse(r, lapse, radial):
    gt, gr, ga, d = spherical_geometry(r, lapse, radial)
    ellp = s.diff(lapse, r) / lapse
    u = (ga - gt) / d
    h = gr - gt - radial * (s.diff(u, r) + u**2) - (s.diff(radial, r) / 2 - radial * ellp) * u
    w = -gt - h / 2 - radial * (s.diff(u, r) + u**2) - (s.diff(radial, r) / 2 + 2 * radial / r) * u
    return u, h / (radial * u**2), w


def observation_parts(radius, radius_derivative, clock_ratio, radar_derivative, orbit_rate, light_speed=1):
    """Return endpoint E and density J on a common, increasing record label."""
    r, q, R, P, O, c = radius, radius_derivative, clock_ratio, radar_derivative, orbit_rate, light_speed
    D = R**2 - r**2 * O**2 / c**2
    E = s.log(P) - s.log(q) - s.log(r) - s.log(D) + 2 * s.log(R)
    J = R**4 * P**2 / (q * r * D)
    return E, J


def primitive_bound(lower, upper, error, label_length, light_speed=1):
    """Deterministic bound; all envelopes and errors must be supplied/certified.

    Keys: lower r,R,q,P,D; upper r,R,O,P; error r,R,O,q,P.
    This does not estimate these inputs or claim a probability coverage.
    """
    if min(lower.values()) <= 0 or min(error.values()) < 0 or label_length < 0 or light_speed <= 0:
        raise ValueError("positive lower envelopes, light speed, and nonnegative errors/length required")
    r, R, O, P = (upper[k] for k in ("r", "R", "O", "P"))
    rl, Rl, ql, Pl, Dl = (lower[k] for k in ("r", "R", "q", "P", "D"))
    er, eR, eO, eq, eP = (error[k] for k in ("r", "R", "O", "q", "P"))
    eD = 2 * R * eR + 2 * r * O**2 * er / light_speed**2 + 2 * r**2 * O * eO / light_speed**2
    KR = 4 * R**3 * P**2 / (ql * rl * Dl)
    KP = 2 * R**4 * P / (ql * rl * Dl)
    Kq = R**4 * P**2 / (ql**2 * rl * Dl)
    Kr = R**4 * P**2 / (ql * rl**2 * Dl)
    KD = R**4 * P**2 / (ql * rl * Dl**2)
    bound = 2 * eP / Pl + 2 * eq / ql + 2 * er / rl + 2 * eD / Dl + 4 * eR / Rl
    bound += label_length * (KR * eR + KP * eP + Kq * eq + Kr * er + KD * eD)
    return bound, eD


def bin_lower_bound(increments, inverse_weight_integrals):
    if len(increments) != len(inverse_weight_integrals) or not increments:
        raise ValueError("matching nonempty bins required")
    if any(h <= 0 for h in inverse_weight_integrals):
        raise ValueError("positive inverse-weight integrals required")
    return sum(x**2 / h for x, h in zip(increments, inverse_weight_integrals))


def dust_family(r, field, k, density_parameter, center_parameter):
    """k and density_parameter are fixed couplings once an action is chosen."""
    rho, C = density_parameter, center_parameter
    B = 1 - k * r**2
    F = (C - rho * r**2 / 2) / B
    Z = 3 * k / (rho - 2 * k * field)
    V = rho / 2 + 3 * (rho - 2 * k * field)**2 / (2 * (rho - 2 * k * C))
    return B, F, Z, V


def sphere_transport_profile(chi, k, rho, integration_constant):
    return rho / (2 * k) + integration_constant / s.cos(s.sqrt(k) * chi)**2
