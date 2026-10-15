#!/usr/bin/env python3
"""Independent checks of sections 6–7 through v5; no author-runner imports.

The general error inequality is proved in the companion written report.
The two high-precision examples below are diagnostic controls, not its proof.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

import mpmath as mp
import sympy as s


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCES = {
    "BLOCK01_DERIVATION_v1.md": "266753576b127818bfed666d6cd773954106d0887db4170c2f6c69797609f86b",
    "BLOCK01_DERIVATION_v3.md": "c02f88316ff57d743c6c92d8de671c46136651118e98bcdc27ec53f01b9337fb",
    "BLOCK01_DERIVATION_v4.md": "8830c6bd57902e1cbbd6053c3ce4f9c477a8e9e54b50af32239edb1c00ede1d1",
    "BLOCK01_DERIVATION_v5.md": "5c2eb165f317192fbc6c8f3c548e442ce40d60d55915c363e57a4311d4d0f586",
}
checks = []


def reduce(expr):
    return s.factor(s.cancel(s.simplify(expr)))


def zero(name, expr):
    residual = reduce(expr)
    checks.append({"name": name, "kind": "symbolic_zero", "ok": residual == 0,
                   "residual": str(residual)})


def nonzero(name, expr):
    residual = reduce(expr)
    checks.append({"name": name, "kind": "mutation_detected", "ok": residual != 0,
                   "residual": str(residual)})


r, r0 = s.symbols("r r0", positive=True)
N, B = s.Function("N")(r), s.Function("B")(r)
n = s.diff(N, r) / N
y = 1 / r - n
Gt = (B - 1) / r**2 + s.diff(B, r) / r
Ga = B * (s.diff(n, r) + n**2 + n / r) + s.diff(B, r) * (n + 1 / r) / 2
a, d = Ga - Gt, B * y
expanded = -s.diff(y, r) - 3 * y / r + y**2 - s.diff(B, r) * y / (2 * B) + 1 / (B * r**2)
zero("relative-map numerator identity", a / B - expanded)

# An integrating factor route: the angular relation is equivalent to
# (F*N*sqrt(B)*r^2*y)' = F*N/sqrt(B). Dividing by the product recovers (9).
F = s.Function("F")(r)
integrating_factor = N * s.sqrt(B) * r**2 * y
zero("integrating-factor equation is exactly angular-minus-time equation",
     s.diff(F * integrating_factor, r) - F * N / s.sqrt(B)
     - N * r**2 / s.sqrt(B) * (d * s.diff(F, r) - F * a))
log_integrand = -s.diff(y, r) / y - 2 / r - n - s.diff(B, r) / (2 * B) + 1 / (B * y * r**2)
zero("differentiated integral formula equals the exact inverse", log_integrand - a / d)

p, b = s.symbols("p b", real=True, positive=True)
exponent = 1 / (b * (1 - p)) - 1 - p
zero("power-law field exponent from direct metric inverse",
     (a / d).subs({N: r**p, B: b}).doit() - exponent / r)
zero("power-law exponent stated in v4", exponent - (b * p**2 - b + 1) / (b * (1 - p)))

# Exact reciprocal split used in the deterministic bound. For log endpoints,
# use |log xhat-log x|<=|xhat-x|/min(x,xhat), applied to positive magnitudes.
bh, by, yh, yy = s.symbols("Bhat B yhat y", nonzero=True)
zero("reciprocal split for error bound",
     1 / (bh * yh) - 1 / (by * yy)
     - ((by - bh) / (bh * by * yh) + (yy - yh) / (by * yh * yy)))
Nh, Nv, Nph, Npv = s.symbols("Nhat N Nph Np", nonzero=True)
zero("ratio split for derivative-to-y bound",
     Nph / Nh - Npv / Nv - ((Nph - Npv) / Nh + Npv * (Nv - Nh) / (Nh * Nv)))

# Killing energy E is constant for a photon in the static metric. A static
# observer measures E/N. A photon emitted at r and received at r0 has ratio N/N0.
K, Nv, N0 = s.symbols("K Nv N0", positive=True)
zero("frequency orientation: received at r0 divided by emitted at r",
     (K / N0) / (K / Nv) - Nv / N0)
R, S, R0, S0 = s.symbols("R S R0 S0", positive=True)
zero("reference-clock radar slowness", N0 / (Nv * s.sqrt(B)) - 1 / ((Nv / N0) * s.sqrt(B)))
metric_B = s.symbols("metric_B", positive=True)
solved_B = s.solve(s.Eq(S**2, 1 / (R**2 * metric_B)), metric_B)[0]
zero("metric B recovered from clock ratio and radar slowness", solved_B - 1 / (R**2 * S**2))

# Independently vary the test-particle Lagrangian in the radial coordinate,
# then impose a circular path: rdot=rddot=0.
light_speed, tdot, phidot, rdot = s.symbols("light_speed tdot phidot rdot", positive=True)
L_particle = (-light_speed**2 * N**2 * tdot**2 + rdot**2 / B + r**2 * phidot**2) / 2
radial_circular = s.diff(L_particle, r).subs(rdot, 0)
Omega_squared = s.solve(radial_circular, phidot**2)[0] / tdot**2
zero("circular geodesic angular-frequency relation", Omega_squared - light_speed**2 * N * s.diff(N, r) / r)
zero("local circular speed relation", r**2 * Omega_squared / (light_speed**2 * N**2) - r * n)
Rfun = s.Function("R")(r)
zero("reference-clock circular angular frequency", (Omega_squared / N0**2).subs(N, N0 * Rfun).doit()
     - light_speed**2 * Rfun * s.diff(Rfun, r) / r)

# Endpoint and integral substitutions for equation (15), keeping endpoints
# distinct until the final reference convention R0=1 is applied.
w, w0 = s.symbols("w w0", real=True)
y_now, y_ref = (1 - w) / r, (1 - w0) / r0
B_now, B_ref = 1 / (R**2 * S**2), 1 / (R0**2 * S0**2)
prefactor9 = (y_ref / y_now) * (r0 / r)**2 * (R0 / R) * s.sqrt(B_ref / B_now)
prefactor15 = (S / S0) * (r0 / r) * (1 - w0) / (1 - w)
zero("relative-field endpoint formula cancels the reference lapse", prefactor9 - prefactor15)
zero("relative-field integral substitution", 1 / (B_now * y_now * r**2) - R**2 * S**2 / (r * (1 - w)))

# Two altered data maps must fail with clocks/radar held fixed. None alters a
# data channel in a coordinated manner so that a false consistency is forced.
eta = s.symbols("eta", positive=True)
nonzero("wrong radar map omitting clock ratio changes B",
        (1 / S**2 - 1 / (R**2 * S**2)).subs({R: r**s.Rational(1, 4), S: r**(-s.Rational(1, 4)) / s.sqrt(s.Rational(2, 3))}))
nonzero("perturbed orbital channel fails independent clock-orbit consistency",
        s.diff(s.log(r**p), r) - (p + eta) / r)
nonzero("double-counted endpoint in relative-field formula changes log derivative",
        s.diff(-s.log(r / r0), r))

# Deterministic controls for both signs of y. Uniform bounds below are analytic
# for N=r^p, Nhat=kappa*r^(p+dp), B=b, Bhat=b+db on [1,2].
mp.mp.dps = 70
for label, pstr in (("positive_y", "0.2"), ("negative_y", "1.5")):
    pv = mp.mpf(pstr)
    dp, kappa, bv, db = map(mp.mpf, ("0.05", "1.03", "0.7", "0.02"))
    n0, b0 = mp.mpf(1), bv
    y0 = min(abs(1 - pv), abs(1 - pv - dp)) / 2
    eN = kappa * 2**(pv + dp) - 2**pv
    eB, ey = db, dp
    alpha = 1 / (bv * (1 - pv)) - 1 - pv
    alphahat = 1 / ((bv + db) * (1 - pv - dp)) - 1 - pv - dp
    actual_error = abs((alphahat - alpha) * mp.log(2))
    bound = 2 * eN / n0 + eB / b0 + 2 * ey / y0 + mp.mpf("0.5") * (eB / (b0**2 * y0) + ey / (b0 * y0**2))
    # The direct quadrature uses only the lower-derivative integrand.
    def reconstructed_log(pvalue, bvalue):
        return -(1 + pvalue) * mp.log(2) + mp.quad(lambda rr: 1 / (bvalue * (1 - pvalue) * rr), [1, 2])
    quad_error = abs((reconstructed_log(pv + dp, bv + db) - reconstructed_log(pv, bv)) - (alphahat - alpha) * mp.log(2))
    checks.append({"name": f"deterministic bound control: {label}", "kind": "synthetic_numeric_control",
                   "ok": actual_error <= bound and quad_error < mp.mpf("1e-60"),
                   "actual_log_error": mp.nstr(actual_error, 30), "bound": mp.nstr(bound, 30),
                   "quadrature_identity_error": mp.nstr(quad_error, 8)})

source_hashes = {}
for name, expected in SOURCES.items():
    body = (HERE.parent / name).read_bytes()
    actual = hashlib.sha256(body).hexdigest()
    source_hashes[name] = actual
    checks.append({"name": f"source identity: {name}", "kind": "provenance", "ok": actual == expected,
                   "actual": actual, "expected": expected})
checks.append({"name": "v4 preserves all v1 source bytes as prefix", "kind": "provenance",
               "ok": (HERE.parent / "BLOCK01_DERIVATION_v4.md").read_bytes().startswith((HERE.parent / "BLOCK01_DERIVATION_v1.md").read_bytes())})
checks.append({"name": "v4 preserves all v3 source bytes as prefix", "kind": "provenance",
               "ok": (HERE.parent / "BLOCK01_DERIVATION_v4.md").read_bytes().startswith((HERE.parent / "BLOCK01_DERIVATION_v3.md").read_bytes())})
old_frequency_text = (
    "Let R(r)=N(r)/N(r0), obtained from the emitted/received proper frequency ratio\n"
    "with its direction stated; define rho(r)=c*tau_roundtrip(r)/2, and S=rho'>0.\n"
)
new_frequency_text = (
    "Let R(r)=N(r)/N(r0). For a photon emitted at r and received at r0,\n"
    "R(r)=nu_received(r0)/nu_emitted(r), using the proper frequencies of the\n"
    "identical static clocks. Define rho(r)=c*tau_roundtrip(r)/2, and S=rho'>0.\n"
)
v4 = (HERE.parent / "BLOCK01_DERIVATION_v4.md").read_text()
v5 = (HERE.parent / "BLOCK01_DERIVATION_v5.md").read_text()
checks.append({"name": "v5 changes only the confirmed frequency-direction clarification", "kind": "provenance",
               "ok": v4.count(old_frequency_text) == 1 and v5 == v4.replace(old_frequency_text, new_frequency_text)})

report = {
    "kind": "focused_independent_check_not_formal_audit",
    "utc_time": datetime.now(timezone.utc).isoformat(),
    "source_hashes": source_hashes,
    "worktree_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
    "python": platform.python_version(), "sympy": s.__version__, "mpmath": mp.__version__,
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "pass": sum(bool(item["ok"]) for item in checks),
    "fail": sum(not item["ok"] for item in checks),
}
(HERE / "relative_map_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for item in checks:
    print(f"{'PASS' if item['ok'] else 'FAIL'}: {item['name']}")
    if "residual" in item and item["residual"] != "0":
        print(f"  residual: {item['residual']}")
    if "actual_log_error" in item:
        print(f"  actual_log_error={item['actual_log_error']} bound={item['bound']}")
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if report["fail"] == 0 else 1)
