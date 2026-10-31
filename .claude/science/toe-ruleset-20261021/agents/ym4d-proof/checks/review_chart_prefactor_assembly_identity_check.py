#!/usr/bin/env python3
"""Independent exact algebra for the assembled auxiliary chart.

This is not a physics simulation, integral evaluation, continuum test, or
replacement for the source-first mathematical review. No author runner is used.
"""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREFIX = "review_chart_prefactor_assembly_"
checks = []
controls = []


def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(sp.cancel(x) == 0 for x in expr)
    return sp.simplify(expr) == 0


def check(name, expr):
    passed = zero(expr)
    checks.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError((name, expr))


def reject(name, expr):
    rejected = not zero(expr)
    controls.append({"name": name, "rejected": rejected})
    if not rejected:
        raise AssertionError(("mutation survived", name))


manifest_path = HERE / (PREFIX + "read_manifest.json")
findings_path = HERE / (PREFIX + "source_first_findings.json")
criteria_path = HERE / (PREFIX + "criteria.json")
manifest = json.loads(manifest_path.read_text())
assert manifest["source_first_findings_sha256"] == hashlib.sha256(findings_path.read_bytes()).hexdigest()
assert json.loads(criteria_path.read_text())["scope"].startswith("Exact symbolic algebra")
for row in manifest["files"]:
    data = (ROOT / row["path"]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row["sha256"], row["path"]
    count = len(data.splitlines())
    assert count == row["line_count"]
    assert all(1 <= a <= b <= count for a, b in row["read_ranges_inclusive"])

# Noncommuting matrix products, without evaluating a scientific matrix.
k1, k2, k3, d1, d2, d3, z = sp.symbols("k1 k2 k3 d1 d2 d3 z")
K = sp.Matrix([[k1, k2], [k2, k3]])
Delta = sp.Matrix([[d1, d2], [d2, d3]])
G = K.inv()
I = sp.eye(2)
C = G * (I + Delta * G).inv()
check("actual critical inverse, correct multiplication order", (K + Delta) * C - I)
reject("reversed noncommuting critical inverse order", (K + Delta) * (I + Delta * G).inv() * G - I)
p1, p2, p3 = sp.symbols("p1 p2 p3")
P = sp.Matrix([[p1, p2], [p2, p3]])
R = I - K * P
check("lift residual identity and right Neumann order", P * (I - R).inv() - G)
reject("wrong sign of lift commutator residual", P * (I + R).inv() - G)
A = K + z * Delta
check("Jacobi determinant derivative", sp.diff(A.det(), z) / A.det() - sp.trace(A.inv() * Delta))
check("critical ratio derivative uses same ordered inverse", sp.trace(A.inv() * Delta) - sp.trace((I + z * G * Delta).inv() * G * Delta))

# The normalized Gaussian heat identity includes the determinant derivative.
a, b, e, s, x, y = sp.symbols("a b e s x y")
Cov = sp.Matrix([[a, s * e], [s * e, b]])
vec = sp.Matrix([x, y])
quadratic = (vec.T * Cov.inv() * vec)[0]
log_density = -sp.log(Cov.det()) / 2 - quadratic / 2
mixed_ratio = sp.diff(log_density, x, y) + sp.diff(log_density, x) * sp.diff(log_density, y)
check("off-block heat identity, both symmetric entries", sp.diff(log_density, s) - e * mixed_ratio)
reject("spurious one-half in the off-block heat identity", sp.diff(log_density, s) - e * mixed_ratio / 2)
reject("omitted normalized determinant derivative", -sp.diff(quadratic, s) / 2 - e * mixed_ratio)

# Coefficient-wise proof of CA7 for arbitrary polynomial degree j >= 2.
j = sp.symbols("j", integer=True, positive=True)
stationary_action_coefficient = 1 - j
integrated_hessian_coefficient = -j * (j - 1) / j
check("critical action minus sign and s weight", stationary_action_coefficient - integrated_hessian_coefficient)
reject("opposite critical action sign", stationary_action_coefficient + integrated_hessian_coefficient)
reject("missing s in the critical action integral", stationary_action_coefficient + j)

sigma, p, c, D, n, h = sp.symbols("sigma p c D n h", positive=True)
Q0, Ec, dh, Lhat, ap = sp.symbols("Q0 Ec dh Lhat ap", positive=True)
tau = c * sigma * p
shift = D * tau / sigma
Qs = Q0 * p ** (D - 1) / sigma * (1 + shift) ** (90 * D) * sp.exp(-ap * p ** 2 / 64)
Ktr = Lhat / sigma * (1 + sp.sqrt(2) * Lhat * shift)
hs = Qs * Ec * (tau + dh * D * tau)
htr = Ktr * Qs * Ec * D * tau ** 2
hs_target = Q0 * Ec * c * (1 + dh * D) * p ** D * (1 + D * c * p) ** (90 * D) * sp.exp(-ap * p ** 2 / 64)
htr_target = Q0 * Ec * Lhat * D * c ** 2 * p ** (D + 1) * (1 + sp.sqrt(2) * Lhat * D * c * p) * (1 + D * c * p) ** (90 * D) * sp.exp(-ap * p ** 2 / 64)
check("exact shrinking side budget", hs - hs_target)
check("exact shrinking marked-translation budget", htr - htr_target)
check("no inverse sigma in side budget", sp.diff(hs, sigma))
check("no inverse sigma in marked translation budget", sp.diff(htr, sigma))
reject("missing flux sigma inverse", sigma * hs - hs_target)
reject("lost second critical-field budget in translation mark", Ktr * Qs * Ec * D * tau - htr_target)
check("all side/corner top-form sigma powers", D * n - h - (D - 1) * h - D * (n - h))
check("largest side polynomial degree", (D + 1) + 1 + 90 * D - (91 * D + 2))
beta = sp.symbols("beta", positive=True)
check("four separate support expenditures", beta - 4 * beta / 8 - beta / 2)
check("critical tail precision smallness, worst bound", (sp.Rational(1, 64) / (1 - sp.Rational(1, 4))) - sp.Rational(1, 48))
check("pair-polydisc accretivity margin", 1 - 2 * sp.Rational(1, 8) - sp.Rational(3, 4))
check("pair-polydisc inverse precision fraction", sp.Rational(3, 4) / sp.Rational(5, 4) ** 2 - sp.Rational(12, 25))

# Full exponent accounting; all vacuum and original-source symbols independent.
volume, m0, Wbase, Wsource, Acorr, ell, Hnl = sp.symbols("volume m0 Wbase Wsource Acorr ell Hnl")
logHaar, logGauss, logZt = sp.symbols("logHaar logGauss logZt")
Fb = Wbase + Wsource + sigma ** 2 * (4 * volume * logZt + Acorr)
prefactor_exponent = m0 * volume * logHaar + D * m0 * volume * logGauss / 2 - Fb / sigma ** 2 - ell / 2 + Hnl
assembled_exponent = (m0 * volume * logHaar + D * m0 * volume * logGauss / 2 - 4 * volume * logZt - (Wbase + Wsource) / sigma ** 2 - Acorr - ell / 2 + Hnl)
check("assembled phase, Haar, scale, determinant and kernel vacuum", prefactor_exponent - assembled_exponent)
reject("wrong sign on compact normalizer vacuum", prefactor_exponent - (assembled_exponent + 8 * volume * logZt))
reject("invisible original Wilson-source vacuum cancellation", prefactor_exponent - (assembled_exponent + Wsource / sigma ** 2))
reject("omitted Haar constant", prefactor_exponent - (assembled_exponent - m0 * volume * logHaar))
reject("wrong full determinant square-root factor", prefactor_exponent - (assembled_exponent - ell / 2))
check("shrinking critical-action budget", (c * sigma * p) ** 2 / (8 * sigma ** 2) - c ** 2 * p ** 2 / 8)
kappac, order = sp.symbols("kappac order", positive=True)
check("scaled coarse Cauchy radius", sigma * p * (2 * D / (kappac * c * sigma * p)) - 2 * D / (kappac * c))
reject("unscaled coarse radius treated as fixed", 2 * D / (kappac * c * sigma * p) - 2 * D / (kappac * c))

result = {
    "kind": "independent_exact_symbolic_identity_check",
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "sympy_version": sp.__version__,
    "python_version": sys.version,
    "source_first_findings_sha256": hashlib.sha256(findings_path.read_bytes()).hexdigest(),
    "criteria_sha256": hashlib.sha256(criteria_path.read_bytes()).hexdigest(),
    "read_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "bound_source_files_unchanged": len(manifest["files"]),
    "positive_checks": checks,
    "mutation_controls": controls,
    "scientific_numerical_experiments": 0,
    "author_scripts_executed": 0,
    "scope_limit": "Exact algebraic identities and byte/line provenance only. Analytic convergence, complex nonvanishing and the infinite reader sums are justified by the separate source-first mathematical review, not this finite symbolic check.",
}
out = HERE / (PREFIX + "identity_check.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"positive_checks": len(checks), "mutation_controls_rejected": len(controls), "bound_source_files_unchanged": len(manifest["files"]), "output": str(out)}))
