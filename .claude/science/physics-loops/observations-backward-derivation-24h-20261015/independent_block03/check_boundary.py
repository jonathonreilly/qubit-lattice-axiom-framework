#!/usr/bin/env python3
"""Independent proper-radius check of the separately stipulated boundary probe."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys

import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "BLOCK03_BOUNDARY_PROBE_v1.md"
EXPECTED = "0689282625c3663026b29b8fe71f05de13f5cba1f774a6c423d6f8391bef99bc"
checks = []


def zero(name, exprs):
    if not isinstance(exprs, (list, tuple)):
        exprs = [exprs]
    residuals = [s.simplify(s.trigsimp(e)) for e in exprs]
    checks.append({"name": name, "kind": "symbolic_identity", "ok": all(e == 0 for e in residuals),
                   "residuals": [str(e) for e in residuals]})


chi, theta, phi = s.symbols("chi theta phi", real=True)
k, rho = s.symbols("k rho", positive=True)
amplitude = s.symbols("amplitude", real=True)
warp = s.Function("warp")(chi)
coords = (chi, theta, phi)
g = s.diag(1, warp**2, warp**2 * s.sin(theta)**2)
gi = s.diag(1, 1 / warp**2, 1 / (warp**2 * s.sin(theta)**2))
Gamma = [[[s.simplify(sum(gi[a, l] * (s.diff(g[l, j], coords[i]) + s.diff(g[l, i], coords[j]) - s.diff(g[i, j], coords[l])) / 2 for l in range(3)))
           for j in range(3)] for i in range(3)] for a in range(3)]
Ricci = s.Matrix(3, 3, lambda i, j: s.simplify(sum(
    s.diff(Gamma[a][i][j], coords[a]) - s.diff(Gamma[a][i][a], coords[j])
    + sum(Gamma[a][i][j] * Gamma[b][a][b] - Gamma[b][i][a] * Gamma[a][j][b] for b in range(3))
    for a in range(3))))
areal = s.sin(s.sqrt(k) * chi) / s.sqrt(k)


def sphere(expr):
    return s.simplify(s.trigsimp(expr.subs(warp, areal).doit()))


Gsphere = g.applyfunc(sphere)
Rsphere = Ricci.applyfunc(sphere)
zero("proper-radius Ricci tensor from Christoffel symbols", list(Rsphere - 2 * k * Gsphere))
R4 = sphere(sum(gi[i, j] * Ricci[i, j] for i in range(3) for j in range(3)))
zero("proper-radius four-dimensional product curvature", R4 - 6 * k)
F = s.Function("F")(chi)
angular_hessian = -Gamma[0][1][1] * s.diff(F, chi) / warp**2
zero("angular scalar Hessian before any areal-radius division",
     angular_hessian - s.diff(warp, chi) * s.diff(F, chi) / warp)
coefficient = sphere(-Gamma[0][1][1] / warp**2)
zero("regular-coordinate scalar transport coefficient", coefficient - s.sqrt(k) * s.cot(s.sqrt(k) * chi))
F0 = rho / (2 * k)
solution = F0 + amplitude / s.cos(s.sqrt(k) * chi)**2
zero("off-equator scalar transport solution", 2 * k * solution - rho - coefficient * s.diff(solution, chi))
zero("off-equator invariant amplitude", (solution - F0) * s.cos(s.sqrt(k) * chi)**2 - amplitude)
zero("equator transport coefficient vanishes", coefficient.subs(chi, s.pi / (2 * s.sqrt(k))))
equator_metric = Gsphere.subs(chi, s.pi / (2 * s.sqrt(k)))
zero("proper-radius metric remains regular through the equator",
     list(equator_metric - s.diag(1, 1 / k, s.sin(theta)**2 / k)))
zero("constant branch metric and scalar equations",
     [-3 * k * F0 + rho + rho / 2, -k * F0 + rho / 2, R4 / 2 - 3 * k])
field, higher = s.symbols("field higher", real=True)
smooth_example_V = rho / 2 + 3 * k * (field - F0) + higher * (field - F0)**2
zero("constant branch leaves higher potential coefficients undetermined",
     [smooth_example_V.subs(field, F0) - rho / 2, s.diff(smooth_example_V, field).subs(field, F0) - 3 * k])
C, r = s.symbols("C r", positive=True)
local_F = (C - rho * r**2 / 2) / (1 - k * r**2)
zero("local-center profile becomes the secant-squared form",
     local_F.subs(r, areal) - (F0 + (C - F0) / s.cos(s.sqrt(k) * chi)**2))
zero("local positive branch reaches zero at the stated radius", local_F.subs(r, s.sqrt(2 * C / rho)))

actual = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
checks.append({"name": "exact boundary source identity", "kind": "provenance", "ok": actual == EXPECTED,
               "actual": actual, "expected": EXPECTED})
report = {
    "kind": "focused_independent_check_not_formal_audit",
    "utc_time": datetime.now(timezone.utc).isoformat(),
    "source_sha256": actual, "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": platform.python_version(), "sympy": s.__version__,
    "checks": checks, "pass": sum(bool(c["ok"]) for c in checks), "fail": sum(not c["ok"] for c in checks),
}
(HERE / "boundary_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for item in checks:
    print(f"{'PASS' if item['ok'] else 'FAIL'}: {item['name']}")
    if not item["ok"]:
        print(item)
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if report["fail"] == 0 else 1)
