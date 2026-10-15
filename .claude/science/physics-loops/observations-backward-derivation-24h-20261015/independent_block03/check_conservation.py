#!/usr/bin/env python3
"""Independent mixed-stress divergence and dimension consistency check."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys

import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "BLOCK03_MATERIAL_CANDIDATE_v1.md"
EXPECTED = "52b32068d094aea7c13d60ede00423bafcd384ac1c4107908ad3d51a842340b7"
t, r, theta, phi = s.symbols("t r theta phi", real=True)
N, B, rho, pr, pt = [s.Function(v)(r) for v in ("N", "B", "rho", "pr", "pt")]
coords = (t, r, theta, phi)
g = s.diag(-N**2, 1 / B, r**2, r**2 * s.sin(theta)**2)
gi = s.diag(-1 / N**2, B, 1 / r**2, 1 / (r**2 * s.sin(theta)**2))
stress = (-rho, pr, pt, pt)
gamma_trace_radial = [s.simplify(sum(gi[a, j] * (
    s.diff(g[j, 1], coords[a]) + s.diff(g[j, a], r) - s.diff(g[a, 1], coords[j])) / 2
    for j in range(4))) for a in range(4)]
divergence_radial = s.diff(pr, r) + sum(gamma_trace_radial[a] * (pr - stress[a]) for a in range(4))
expected = s.diff(pr, r) + (rho + pr) * s.diff(N, r) / N + 2 * (pr - pt) / r
residual = s.simplify(divergence_radial - expected)
checks = [{"name": "general material radial conservation from mixed tensor divergence", "ok": residual == 0,
           "residual": str(residual), "computed_divergence": str(s.simplify(divergence_radial))}]

# Unit exponents are used as arithmetic data; this is an independent consistency
# accounting, not a proof of physical calibration or of any field equation.
dim = {"r": -1, "T": -1, "F": 2, "C": 2, "k": 2, "rho": 4, "Z": -2, "V": 4, "lambda": 4}
checks.append({"name": "declared action and construction dimensions agree", "ok":
               dim["F"] + dim["k"] == 4 and
               dim["Z"] + 2 * (dim["F"] - dim["r"]) == 4 and
               dim["lambda"] + 2 * (dim["T"] - dim["r"]) == 4 and
               dim["rho"] + 2 * dim["r"] == dim["C"] and
               dim["rho"] - dim["k"] == dim["F"] and
               dim["k"] - dim["rho"] == dim["Z"], "mass_dimensions": dim})
actual = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
checks.append({"name": "exact material source identity", "ok": actual == EXPECTED,
               "actual": actual, "expected": EXPECTED})
report = {"kind": "focused_independent_check_not_formal_audit",
          "utc_time": datetime.now(timezone.utc).isoformat(), "source_sha256": actual,
          "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "python": platform.python_version(), "sympy": s.__version__,
          "checks": checks, "pass": sum(bool(c["ok"]) for c in checks),
          "fail": sum(not c["ok"] for c in checks)}
(HERE / "conservation_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for check in checks:
    print(f"{'PASS' if check['ok'] else 'FAIL'}: {check['name']}")
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if not report["fail"] else 1)
