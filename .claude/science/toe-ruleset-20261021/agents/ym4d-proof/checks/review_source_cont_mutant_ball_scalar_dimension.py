#!/usr/bin/env python3
"""Ball-cut normalization/flux controls; SU(2) Lie dimension D=3.

One symbolic identity and high-precision finite Gaussian diagnostics, not an
actual nonabelian Haar integration or a proof of uniform RG estimates.
"""
from datetime import datetime, timezone
import json
import sys
import time
import mpmath as mp
import sympy as sp

started = time.monotonic()
r = sp.symbols("r", positive=True)
z3 = sp.erf(r / sp.sqrt(2)) - sp.sqrt(2 / sp.pi) * r * sp.exp(-r ** 2 / 2)
surface = 4 * sp.pi * r ** 2 * sp.exp(-r ** 2 / 2) / (2 * sp.pi) ** sp.Rational(3, 2)
checks = {"D3_ball_probability_derivative_equals_full_surface_density": sp.simplify(sp.diff(z3, r) - surface) == 0}
mp.mp.dps = 70
p = mp.mpf(5) / 2
e = mp.mpc(1, 2) / 1000000
C = lambda s: 1 + s * e
z = lambda x: mp.erf(x / mp.sqrt(2)) - mp.sqrt(2 / mp.pi) * x * mp.exp(-x ** 2 / 2)
q = lambda x: mp.sqrt(2 / mp.pi) * x ** 2 * mp.exp(-x ** 2 / 2)
s = mp.mpf(2) / 5
# Direct radial integral including the actual three-dimensional affine Jacobian.
radial = lambda t: C(t) * mp.sqrt(2 / mp.pi) * mp.quad(lambda x: x ** 2 * mp.exp(-C(t) ** 2 * x ** 2 / 2), [0, p])
closed = lambda t: z(C(t) * p)
Z_reduced = C(s) ** (-3) * z(C(s) * p) / z(p)
surface_pin = mp.exp(-(C(s) ** 2 - 1) * p ** 2 / 2)
normalized_flux = q(p) / z(p) * (e * p / C(s)) * surface_pin / Z_reduced
direct_log_derivative = mp.diff(closed, s) / closed(s)
checks["D3_direct_radial_integral_matches_moving_ball_probability"] = abs(radial(s) - closed(s)) < mp.mpf("1e-55")
checks["D3_normalized_flux_matches_direct_log_derivative"] = abs(normalized_flux - direct_log_derivative) < mp.mpf("1e-55")
checks["control_omitting_sphere_radius_power_fails"] = abs(normalized_flux / p ** 2 - direct_log_derivative) > mp.mpf("1e-15")
checks["control_omitting_three_dimensional_jacobian_fails"] = abs(mp.diff(lambda t: closed(t) / C(t) ** 3, s) / (closed(s) / C(s) ** 3) - direct_log_derivative) > mp.mpf("1e-15")
payload = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": time.monotonic() - started,
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "all_checks_pass": all(checks.values()),
    "dimension": 3,
    "symbolic_probability": str(z3),
    "symbolic_surface_density": str(sp.simplify(surface)),
    "complex_affine_scale": str(C(s)),
    "normalized_flux": str(normalized_flux),
    "direct_log_derivative": str(direct_log_derivative),
    "radial_error": str(abs(radial(s) - closed(s))),
    "flux_error": str(abs(normalized_flux - direct_log_derivative)),
    "precision_decimal_digits": mp.mp.dps,
    "scope": "One exact symbolic surface normalization and high-precision complex Gaussian radial diagnostics; not an interval certificate or a Yang--Mills integration.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
sys.exit(0 if payload["all_checks_pass"] else 1)
