#!/usr/bin/env python3
"""Independent block-02 checks, using no author runner and no git/network calls.

Mechanisms: exact product telescoping for the primitive bound, a completed
square for the finite-bin inequality, and resolved bump-coordinate integration
for the sample ambiguity. Numeric controls do not prove the universal bound.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys

import mpmath as mp
import sympy as s


HERE = Path(__file__).resolve().parent
PACK = HERE.parent
SOURCES = {
    "BLOCK02_DERIVATION_v1.md": "2b65e7cc57f06b145792ab4623dd78d78e9b86f747a2bb5b927cff9295e8f448",
    "BLOCK02_DERIVATION_v2.md": "6af03812dccdf6c77322b20591f5cc72300c84e304f7fff56bf680af7e066c1e",
    "BLOCK01_DERIVATION_v5.md": "5c2eb165f317192fbc6c8f3c548e442ce40d60d55915c363e57a4311d4d0f586",
    "BLOCK01_READOUT_INTAKE_v1.md": "6d8dc4094320a13731ee1366cf5343076f82b7c106fded48496807fd6d933e33",
}
checks = []
mp.mp.dps = 70


def reduce(expr):
    return s.factor(s.cancel(s.simplify(expr)))


def zero(name, expr):
    residual = reduce(expr)
    checks.append({"name": name, "kind": "symbolic_identity", "ok": residual == 0,
                   "residual": str(residual)})


def nonzero(name, expr, kind="defect_detected"):
    residual = reduce(expr)
    checks.append({"name": name, "kind": kind, "ok": residual != 0,
                   "residual": str(residual)})


def positive_exact(name, expr):
    value = reduce(expr)
    checks.append({"name": name, "kind": "exact_inequality", "ok": value.is_positive is True,
                   "value": str(value)})


def mstr(value):
    return mp.nstr(value, 35)


r, r0, q, q0, P, P0, R, R0, D, D0, c = s.symbols("r r0 q q0 P P0 R R0 D D0 c", positive=True)
Omega, Omegah = s.symbols("Omega Omegahat", real=True)
rh, qh, Ph, Rh, Dh = s.symbols("rhat qhat Phat Rhat Dhat", positive=True)
S, S0 = P / q, P0 / q0
A, A0 = D / R**2, D0 / R0**2
prefactor_direct = (S / S0) * (r0 / r) * (A0 / A)
prefactor_E = (P / P0) * (q0 / q) * (r0 / r) * (D0 / D) * (R / R0)**2
J = R**4 * P**2 / (q * r * D)
zero("shared-label endpoint factor", prefactor_direct - prefactor_E)
zero("shared-label integral density", R**2 * S**2 * q / (r * A) - J)

jac = s.symbols("positive_relabeling_derivative", positive=True)
zero("endpoint quotient under an orientation-preserving relabeling", (P * jac) / (q * jac) - P / q)
zero("integral density under an orientation-preserving relabeling",
     J.subs({P: P * jac, q: q * jac}, simultaneous=True) - jac * J)
J_wrong = R**4 * P**2 / (q**2 * r * D)
nonzero("omitting the dr/dz factor breaks relabeling covariance",
        J_wrong.subs({P: P * jac, q: q * jac}, simultaneous=True) - jac * J_wrong)

# Finite differences, not gradient estimates, prove the displayed primitive
# coefficients. Every intermediate denominator is bounded by the same minima.
D_direct = R**2 - r**2 * Omega**2 / c**2
Dh_direct = Rh**2 - rh**2 * Omegah**2 / c**2
D_split = Rh**2 - R**2 - ((rh**2 - r**2) * Omegah**2 + r**2 * (Omegah**2 - Omega**2)) / c**2
zero("exact primitive D product split", Dh_direct - D_direct - D_split)
zero("shared-clock change in D when other primitive channels are fixed",
     (Dh_direct - D_direct).subs({rh: r, Omegah: Omega}) - (Rh**2 - R**2))
Jhat = Rh**4 * Ph**2 / (qh * rh * Dh)
J_split = (
    (Rh**4 - R**4) * Ph**2 / (qh * rh * Dh)
    + R**4 * (Ph**2 - P**2) / (qh * rh * Dh)
    + R**4 * P**2 * (1 / qh - 1 / q) / (rh * Dh)
    + R**4 * P**2 / q * (1 / rh - 1 / r) / Dh
    + R**4 * P**2 / (q * r) * (1 / Dh - 1 / D)
)
zero("exact five-factor telescoping identity for J", Jhat - J - J_split)
zero("fourth-power finite difference supplies coefficient 4",
     Rh**4 - R**4 - (Rh - R) * (Rh**3 + Rh**2 * R + Rh * R**2 + R**3))
zero("square finite difference supplies coefficient 2", Ph**2 - P**2 - (Ph - P) * (Ph + P))
zero("reciprocal difference supplies squared denominator minimum",
     1 / qh - 1 / q - (q - qh) / (qh * q))


def primitive_bound(length, limits, errors, omit_D_from_R=False, omit_radius=False):
    rmin, Rmin, qmin, Pmin, Dmin, rmax, Rmax, Omax, Pmax = limits
    er, eR, eO, eP, eq = errors
    if omit_radius:
        er = mp.mpf(0)
    eD = (0 if omit_D_from_R else 2 * Rmax * eR) + 2 * rmax * Omax**2 * er + 2 * rmax**2 * Omax * eO
    KR = 4 * Rmax**3 * Pmax**2 / (qmin * rmin * Dmin)
    KP = 2 * Rmax**4 * Pmax / (qmin * rmin * Dmin)
    Kq = Rmax**4 * Pmax**2 / (qmin**2 * rmin * Dmin)
    Kr = Rmax**4 * Pmax**2 / (qmin * rmin**2 * Dmin)
    KD = Rmax**4 * Pmax**2 / (qmin * rmin * Dmin**2)
    endpoint = 2 * eP / Pmin + 2 * eq / qmin + 2 * er / rmin + 2 * eD / Dmin + 4 * eR / Rmin
    return endpoint + length * (KR * eR + KP * eP + Kq * eq + Kr * er + KD * eD), eD


def primitive_L(data, upper):
    def endpoint(z):
        rv, qv, Pv, Rv, Ov = data(z)
        Dv = Rv**2 - rv**2 * Ov**2
        return mp.log(Pv / (qv * rv)) - mp.log(Dv / Rv**2)

    def density(z):
        rv, qv, Pv, Rv, Ov = data(z)
        Av = 1 - rv**2 * Ov**2 / Rv**2
        # Direct pullback of block 01 rather than the compact J implementation.
        return Rv**2 * (Pv / qv)**2 * qv / (rv * Av)

    return endpoint(upper) - endpoint(0) + mp.quad(density, [0, upper / 2, upper])


# Joint perturbation on z in [0,1]. Bounds are certified by monotonicity and
# exact rational envelope checks, not by taking a sampled maximum.
positive_exact("joint-control R upper envelope",
               s.Rational(28, 25)**4 - s.Rational(3, 2) * s.Rational(201, 200)**4)
positive_exact("joint-control D lower envelope",
               1 - s.Rational(301, 100)**2 * s.Rational(1, 4)**2 - s.Rational(43, 100))


def joint_data(z, perturbed=False):
    rv = 2 + z
    Rv = (rv / 2)**mp.mpf("0.25")
    Ov = mp.mpf("0.5") * Rv / rv
    Pv = 1 + z / 5
    if perturbed:
        return rv + z / 100, mp.mpf("1.01"), Pv + z / 50, Rv * (1 + z / 200), Ov * (1 - z / 250)
    return rv, mp.mpf(1), Pv, Rv, Ov


joint_limits = tuple(map(mp.mpf, ("2", "1", "1", "1", "0.43", "3.01", "1.12", "0.25", "1.22")))
joint_errors = tuple(map(mp.mpf, ("0.01", "0.0056", "0.001", "0.02", "0.01")))
joint_B, joint_eD = primitive_bound(mp.mpf(1), joint_limits, joint_errors)
joint_difference = abs(primitive_L(lambda z: joint_data(z, True), mp.mpf(1)) - primitive_L(joint_data, mp.mpf(1)))
checks.append({"name": "joint primitive perturbation respects the analytic-envelope bound", "kind": "synthetic_numeric_control",
               "ok": joint_difference <= joint_B, "actual_log_error": mstr(joint_difference),
               "bound": mstr(joint_B), "certified_eD": mstr(joint_eD)})

# A physically consistent baseline metric has R=r^p, S=1 and circular v^2=p.
# Perturb only the measured clock channel; noisy hatted data need not satisfy
# exact geodesic consistency. The same perturbation must also enter D.
power, length, clock_error = map(mp.mpf, ("0.999", "0.1", "0.01"))


def clock_data(z, perturbed=False):
    rv = 1 + z
    Rv = rv**power
    Ov = mp.sqrt(power) * Rv / rv
    return rv, mp.mpf(1), mp.mpf(1), Rv * (1 + clock_error * z if perturbed else 1), Ov


clock_Rmax = (1 + length)**power * (1 + clock_error * length)
clock_eR = (1 + length)**power * clock_error * length
clock_limits = (mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), 1 - power,
                1 + length, clock_Rmax, mp.sqrt(power), mp.mpf(1))
clock_errors = (mp.mpf(0), clock_eR, mp.mpf(0), mp.mpf(0), mp.mpf(0))
clock_B, clock_eD = primitive_bound(length, clock_limits, clock_errors)
clock_bad_B, _ = primitive_bound(length, clock_limits, clock_errors, omit_D_from_R=True)
clock_difference = abs(primitive_L(lambda z: clock_data(z, True), length) - primitive_L(clock_data, length))
checks.append({"name": "shared-clock error is retained in the valid bound", "kind": "synthetic_numeric_control",
               "ok": clock_difference <= clock_B, "actual_log_error": mstr(clock_difference), "bound": mstr(clock_B),
               "certified_eD": mstr(clock_eD)})
checks.append({"name": "dropping shared-clock error from D fails on a concrete control", "kind": "defect_detected",
               "ok": clock_difference > clock_bad_B, "actual_log_error": mstr(clock_difference), "incorrect_bound": mstr(clock_bad_B)})

# Radius-only perturbation: r=2+z, rhat=2.1+z, P=2, q=R=1, Omega=0.
# The exact relative inverse is L=3*log(r/r0); omitting er would claim B=0.
radius_difference = abs(3 * mp.log(mp.mpf("3.1") / mp.mpf("2.1")) - 3 * mp.log(mp.mpf("1.5")))
radius_limits = tuple(map(mp.mpf, ("2", "1", "1", "2", "1", "3.1", "1", "0", "2")))
radius_errors = tuple(map(mp.mpf, ("0.1", "0", "0", "0", "0")))
radius_B, _ = primitive_bound(mp.mpf(1), radius_limits, radius_errors)
radius_bad_B, _ = primitive_bound(mp.mpf(1), radius_limits, radius_errors, omit_radius=True)
checks.append({"name": "radius-only perturbation respects the valid bound", "kind": "synthetic_numeric_control",
               "ok": radius_difference <= radius_B, "actual_log_error": mstr(radius_difference), "bound": mstr(radius_B)})
checks.append({"name": "omitting radius uncertainty fails on a concrete control", "kind": "defect_detected",
               "ok": radius_difference > radius_bad_B, "actual_log_error": mstr(radius_difference), "incorrect_bound": mstr(radius_bad_B)})

# An endpoint mutation on R=1, Omega=0, S=r, a=1, b=2 changes only the
# observable endpoint quotient and gives the exact nonzero error below.
nonzero("inverting the slowness endpoint ratio changes the logarithmic inverse", s.log(s.Rational(1, 2)) - s.log(2))

# Complete the square rather than invoke Cauchy–Schwarz numerically. Here the
# identity is evaluated with concrete functions; its general integral proof
# and equality condition are supplied in the report.
x = s.symbols("x", positive=True)
w = 1 / x
a, b = s.Rational(1), s.Rational(2)
H = s.integrate(1 / w, (x, a, b))
delta = s.integrate(1, (x, a, b))
I = s.integrate(w, (x, a, b))
variance = s.integrate(w * (1 - delta / (H * w))**2, (x, a, b))
zero("complete-square identity for a strict finite-bin example", I - delta**2 / H - variance)
k = s.symbols("k", positive=True)
delta_eq = s.integrate(k / w, (x, a, b))
I_eq = s.integrate(w * (k / w)**2, (x, a, b))
zero("finite-bin equality family S=k/w", I_eq - delta_eq**2 / H)
checks.append({"name": "strict finite-bin example has positive gap", "kind": "synthetic_numeric_control",
               "ok": mp.log(2) > mp.mpf(2) / 3, "gap": mstr(mp.log(2) - mp.mpf(2) / 3)})
xx, yy, h, kk = s.symbols("xx yy h kk", positive=True)
zero("exact refinement gain", xx**2 / h + yy**2 / kk - (xx + yy)**2 / (h + kk)
     - (kk * xx - h * yy)**2 / (h * kk * (h + kk)))
refined = s.Rational(1, 4) / s.Rational(5, 8) + s.Rational(1, 4) / s.Rational(7, 8)
positive_exact("two-bin refinement improves the constant-S example", refined - s.Rational(2, 3))
uncertain_lower = s.Rational(2, 5)**2 / s.Rational(9, 10)
positive_exact("clamped uncertain-increment lower bound remains below the exact-bin bound", refined - uncertain_lower)

# An explicit C-infinity bump. The squared integral is evaluated in bump
# coordinates, so shrinking support cannot evade a fixed spatial sample grid.
def raw_bump(t):
    if abs(t) >= mp.mpf("0.5"):
        return mp.mpf(0)
    return mp.exp(-1 / (1 - 4 * t**2))


bump_nodes = [mp.mpf("-0.5"), mp.mpf("-0.25"), mp.mpf(0), mp.mpf("0.25"), mp.mpf("0.5")]
Z = mp.quad(raw_bump, bump_nodes)


def psi(t):
    return raw_bump(t) / Z


amplitude, width, center = mp.mpf("0.25"), mp.mpf("0.8"), mp.mpf("1.5")
baseline_mass_removed = width * mp.e * Z
lam = amplitude / baseline_mass_removed


def baseline(rv):
    return 1 - lam * mp.e * raw_bump((rv - center) / width)


# Since f=e*raw_bump is >=exp(-1/3)>2/3 on |t|<=1/4,
# integral f((r-rc)/h)dr > h/3=4/15, and lam<15/16.
positive_exact("analytic baseline mass bound exceeds the chosen removed area", s.Rational(4, 15) - s.Rational(1, 4))
positive_exact("certified baseline lower bound", 1 - s.Rational(15, 16))
psi2 = mp.quad(lambda t: psi(t)**2, bump_nodes)
baseline_I = mp.quad(lambda rv: baseline(rv)**2 / rv, [1, mp.mpf("1.1"), center, mp.mpf("1.9"), 2])
baseline_integral = mp.quad(baseline, [1, mp.mpf("1.1"), center, mp.mpf("1.9"), 2])
psi_integral = mp.quad(psi, bump_nodes)
gap_increment = baseline_integral + amplitude * psi_integral
bump_results = []
for denominator in (4, 8, 16, 32, 64, 128):
    eps = mp.mpf(1) / denominator
    cross = 2 * amplitude * mp.quad(lambda t: baseline(center + eps * t) * psi(t) / (center + eps * t), bump_nodes)
    spike = amplitude**2 / eps * mp.quad(lambda t: psi(t)**2 / (center + eps * t), bump_nodes)
    actual_I = baseline_I + cross + spike
    lower_I = amplitude**2 * psi2 / (2 * eps)
    endpoints = [baseline(rv) + amplitude / eps * psi((rv - center) / eps) for rv in (mp.mpf(1), mp.mpf(2))]
    bump_results.append({"epsilon": mstr(eps), "I": mstr(actual_I), "lower_bound": mstr(lower_I),
                         "epsilon_times_I": mstr(eps * actual_I),
                         "radar_gap_increment": mstr(gap_increment), "endpoint_S": [mstr(v) for v in endpoints]})
    checks.append({"name": f"finite-sample bump control epsilon=1/{denominator}", "kind": "synthetic_numeric_control",
                   "ok": actual_I >= lower_I and abs(gap_increment - 1) < mp.mpf("1e-60") and all(v == 1 for v in endpoints),
                   **bump_results[-1]})

# Separate intake probe: static coherent turnaround cancels the lapse, while
# radar slowness alone does not fix it. No observational or healthy-action claim.
nu, turnaround, lapse = s.symbols("nu turnaround lapse", positive=True)
zero("static coherent turnaround cancellation", lapse * (turnaround * nu / lapse) - turnaround * nu)
power_symbol = s.symbols("power", positive=True)
metric_N = x**power_symbol
metric_B = x**(-2 * power_symbol)
zero("intake family has unit radial-radar slowness", 1 / (metric_N * s.sqrt(metric_B)) - 1)
zero("intake family has local circular speed squared p", x * s.diff(s.log(metric_N), x) - power_symbol)
nonzero("two intake family metrics have distinct clock ratios", metric_N.subs(power_symbol, s.Rational(1, 4)) - metric_N.subs(power_symbol, s.Rational(1, 2)),
        kind="metric_nonuniqueness_witness")

source_hashes = {}
for name, expected in SOURCES.items():
    actual = hashlib.sha256((PACK / name).read_bytes()).hexdigest()
    source_hashes[name] = actual
    checks.append({"name": f"source identity: {name}", "kind": "provenance", "ok": actual == expected,
                   "actual": actual, "expected": expected})
v1 = (PACK / "BLOCK02_DERIVATION_v1.md").read_text()
v2 = (PACK / "BLOCK02_DERIVATION_v2.md").read_text()
before = "Equation (1) is invariant under any common increasing smooth relabeling of z:\n"
after = "Equation (1) is invariant under a common smooth relabeling of z whose\nderivative is strictly positive throughout the interval:\n"
checks.append({"name": "v2 changes only the confirmed positive-relabeling-derivative condition", "kind": "provenance",
               "ok": v1.count(before) == 1 and v2 == v1.replace(before, after)})

report = {
    "kind": "focused_independent_check_not_formal_audit",
    "utc_time": datetime.now(timezone.utc).isoformat(),
    "source_hashes": source_hashes,
    "git_state": "Not queried; current dispatch forbids git actions.",
    "python": platform.python_version(), "sympy": s.__version__, "mpmath": mp.__version__,
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "bump_normalization": mstr(Z), "bump_squared_integral": mstr(psi2),
    "bump_baseline_lambda": mstr(lam), "bump_asymptotic_epsilon_I": mstr(amplitude**2 * psi2 / center),
    "checks": checks,
    "pass": sum(bool(item["ok"]) for item in checks),
    "fail": sum(not item["ok"] for item in checks),
}
(HERE / "computed_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for item in checks:
    print(f"{'PASS' if item['ok'] else 'FAIL'}: {item['name']}")
    for key in ("residual", "actual_log_error", "bound", "incorrect_bound", "I", "lower_bound"):
        if key in item and str(item[key]) != "0":
            print(f"  {key}: {item[key]}")
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if report["fail"] == 0 else 1)
