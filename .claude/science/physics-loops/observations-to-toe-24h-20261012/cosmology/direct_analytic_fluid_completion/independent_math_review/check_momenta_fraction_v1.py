#!/usr/bin/env python3
"""Exact rational Euler--Lagrange and compact-sublevel controls.

This second route does not construct Christoffels, use SymPy, or import any
other checking code.  It differentiates diagonal kinetic coefficients in the
coordinate momentum equations and eliminates H through H^2 and Hdot.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
checks, rows = [], []


def add(name, ok, details):
    checks.append({"name": name, "pass": bool(ok), "details": details})


def model(s, nu, u, x, y):
    a = s * s
    d = 1 + F(2, 3) * (1 + a) * (x * x + y * y)
    k = [F(1), F(4, 9) * a / d, a / (3 * d)]
    dd = [F(0), F(4, 3) * (1 + a) * x, F(4, 3) * (1 + a) * y]
    dk = [[F(0)] * 3, [-F(4, 9) * a * z / d**2 for z in dd], [-a * z / (3 * d**2) for z in dd]]
    f = a / 2 - s * u + 2 * u * u
    potential = F(3, 2) + f * x * x + a * y * y / 3 + nu * u * u / 2
    gradient = [(-s + 4 * u) * x * x + nu * u, 2 * f * x, F(2, 3) * a * y]
    return d, k, dk, potential, gradient


for s in (F(1, 1000), F(1, 50), F(1, 10), F(2)):
    for nu in (F(1, 4), F(1), F(9, 4), F(4)):
        for x, y in ((F(0), F(0)), (F(1), F(0)), (F(0), F(2)), (F(-3, 2), F(2, 3)), (F(4), F(-5))):
            a = s * s
            d, k, dk, potential, gradient = model(s, nu, F(0), x, y)
            h2 = d
            hdot = -(1 + a) * (x * x + F(4, 3) * y * y)
            z = [F(0), -F(3, 2) * x, -2 * y]  # v/H
            acceleration = [F(0), -F(3, 2) * hdot * x + F(9, 4) * h2 * x, -2 * hdot * y + 4 * h2 * y]
            source = [s * x * x, F(0), F(0)]
            kinetic_coordinate_term = [h2 * (sum(dk[i][j] * z[j] * z[i] for j in range(3)) - sum(dk[j][i] * z[j] * z[j] for j in range(3)) / 2) for i in range(3)]
            el = [k[i] * acceleration[i] + kinetic_coordinate_term[i] + 3 * h2 * k[i] * z[i] + gradient[i] + source[i] for i in range(3)]
            idx = len(rows)
            for i, value in enumerate(el):
                add(f"Euler_Lagrange_row_{idx}_component_{i}", value == 0, str(value))
            kinetic = h2 * sum(k[i] * z[i]**2 for i in range(3))
            add(f"kinetic_row_{idx}", kinetic == a * (x * x + F(4, 3) * y * y), str(kinetic))
            rows.append({"s": str(s), "a": str(a), "nu": str(nu), "x": str(x), "y": str(y), "EL": list(map(str, el)), "omitted_metric_derivative_residual": list(map(str, [-z for z in kinetic_coordinate_term]))})

            # An off-trajectory finite state bounds Euclidean fields and velocities.
            uu, vel = F(-3, 5), (F(-2, 3), F(5, 7), F(-1, 2))
            sig, rad = F(2, 5), F(1, 3)
            dd, kk, _, vp, _ = model(s, nu, uu, x, y)
            energy = sum(kk[i] * vel[i]**2 for i in range(3)) / 2 + vp + sig + rad
            excess = energy - F(3, 2)
            dmax = 1 + 34 * (1 + a) * excess / (9 * a)
            kmin = min(F(1), a / (3 * dmax))
            predicates = [uu * uu <= 2 * excess / nu, x * x <= 8 * excess / (3 * a), y * y <= 3 * excess / a, dd <= dmax, min(kk) >= kmin, sum(v * v for v in vel) <= 2 * excess / kmin, sig + rad <= excess]
            add(f"compact_sublevel_row_{idx}", all(predicates), {"energy": str(energy), "checks": predicates})

mutant_rows = [row for row in rows if any(F(z) != 0 for z in row["omitted_metric_derivative_residual"])]
add("omitted_metric_derivatives_detected", len(mutant_rows) == 64, {"detected": len(mutant_rows), "total": len(rows), "zero_rows": "the sixteen x=y=0 vacuum fixtures"})

# Explicit allowed Einstein-expanding state with instantaneous Jordan contraction.
# a=1, H_v=nu=1, fields=0, v_u=-3, sigma=r=0 -> H=2 and H_J=-1.
_, kk, _, vp, _ = model(F(1), F(1), F(0), F(0), F(0))
hsquared = (9 * kk[0] + 2 * vp) / 3
add("Einstein_expansion_does_not_imply_Jordan_expansion", hsquared == 4 and F(2) - 3 == -1, {"a": 1, "H_v": 1, "nu": 1, "u_x_y": [0, 0, 0], "v": [-3, 0, 0], "sigma_r": [0, 0], "H": 2, "A": 1, "H_J": -1})

out = {"method": "stdlib Fraction coordinate-momentum Euler--Lagrange equations; no Christoffels or author helpers", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "rows": rows, "checks": checks, "summary": {"rows": len(rows), "total": len(checks), "passed": sum(c["pass"] for c in checks), "failed": sum(not c["pass"] for c in checks)}}
(ROOT / "MOMENTA_CHECKS_v1.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out["summary"], sort_keys=True))
for check in checks:
    if not check["pass"]:
        print(json.dumps(check, sort_keys=True))
raise SystemExit(1 if out["summary"]["failed"] else 0)
