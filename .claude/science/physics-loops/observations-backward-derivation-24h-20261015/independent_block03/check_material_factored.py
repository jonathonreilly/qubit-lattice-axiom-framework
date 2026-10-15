#!/usr/bin/env python3
"""Independent Cartesian-center and variational material checks.

No author runner, network, git, or code outside this checker is imported.
All checks are exact symbolic identities or explicit defect controls.
"""

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
checks = []


def red(e):
    return s.factor(s.cancel(s.together(e)))


def zero(name, expressions):
    print("BEGIN: " + name, flush=True)
    if not isinstance(expressions, (list, tuple)):
        expressions = [expressions]
    residuals = [red(e) for e in expressions]
    checks.append({"name": name, "kind": "symbolic_identity", "ok": all(e == 0 for e in residuals),
                   "residuals": [str(e) for e in residuals]})


def nonzero(name, e):
    print("BEGIN: " + name, flush=True)
    e = red(e)
    checks.append({"name": name, "kind": "defect_detected", "ok": e != 0, "residual": str(e)})


# First derive the general metric equations from the unfixed sphere-radius
# reduced action, whose curvature integration-by-parts identity was checked
# independently in block 01. No previous runner is imported or executed.
r = s.symbols("r", positive=True)
N, B, radius, f = [s.Function(n)(r) for n in ("N", "B", "radius", "F")]
Zfun, Vfun = s.Function("Z"), s.Function("V")
fp, np, ap = s.diff(f, r), s.diff(N, r), s.diff(radius, r)
Lgrav = (s.sqrt(B) * ((radius**2 * fp + 2 * radius * f * ap) * np
                     + N * f * ap**2 + 2 * N * radius * fp * ap)
         + N * f / s.sqrt(B) - N * radius**2 * s.sqrt(B) * Zfun(f) * fp**2 / 2
         - N * radius**2 * Vfun(f) / s.sqrt(B))


def EL(L, v):
    return s.diff(L, v) - s.diff(s.diff(L, s.diff(v, r)), r)


Et = red((-s.sqrt(B) * EL(Lgrav, N) / radius**2).subs(radius, r).doit())
Er = red((2 * B * s.sqrt(B) * EL(Lgrav, B) / (N * radius**2)).subs(radius, r).doit())
Ea = red((-s.sqrt(B) * EL(Lgrav, radius) / (2 * N * radius)).subs(radius, r).doit())
n = np / N
Gt = (B - 1) / r**2 + s.diff(B, r) / r
Gr = (B - 1) / r**2 + 2 * B * n / r
Ga = B * (s.diff(n, r) + n**2 + n / r) + s.diff(B, r) * (n + 1 / r) / 2
rho, pr, pt = s.symbols("rho p_r p_t")
K = Zfun(f) * B * fp**2
a, d = Ga - Gt, B * (1 / r - n)
zero("sourced angular-minus-time relation from action variation",
     (Ea - pt) - (Et + rho) - (f * a - d * fp - rho - pt))
zero("sourced radial-minus-time kinetic reconstruction",
     (Er - pr) - (Et + rho)
     - (f * (Gr - Gt) - rho - pr - K - B * s.diff(f, r, 2) - (s.diff(B, r) / 2 - B * n) * fp))
zero("sourced temporal potential reconstruction",
     Et + rho - (f * Gt + rho + K / 2 + Vfun(f)
                 + B * s.diff(f, r, 2) + (s.diff(B, r) / 2 + 2 * B / r) * fp))
M, integral = s.Function("M")(r), s.Function("integral")(r)
u, source = s.Function("u")(r), s.Function("source")(r)
F0 = s.symbols("F0")
affine = M * (F0 - integral)
zero("affine integrating-factor solution",
     (s.diff(affine, r) - u * affine + source).subs({s.diff(M, r): u * M, s.diff(integral, r): source / M}))

# Vary dust before putting the multiplier constraint on shell. The radial
# current and temporal current are retained until after differentiating.
t = s.symbols("t", real=True)
T = s.Function("T")(t, r)
lam = s.Function("lambda")(t, r)
X = -s.diff(T, t)**2 / N**2 + B * s.diff(T, r)**2
volume = N * radius**2 / s.sqrt(B)
Ldust = -volume * lam * (X + 1) / 2
lambda_EL = s.diff(Ldust, lam)
T_EL = -s.diff(s.diff(Ldust, s.diff(T, t)), t) - s.diff(s.diff(Ldust, s.diff(T, r)), r)
zero("dust multiplier variation", lambda_EL / volume + (X + 1) / 2)
zero("dust scalar variation is current conservation",
     T_EL - (s.diff(-volume * lam * s.diff(T, t) / N**2, t)
             + s.diff(volume * lam * B * s.diff(T, r), r)))
k, density, C, C2 = s.symbols("k density C C2", positive=True)
onshell = {T: t, lam: density, N: s.Integer(1), radius: r, B: 1 - k * r**2}
zero("declared static dust satisfies its constraint and continuity equation",
     [lambda_EL.subs(onshell).doit(), T_EL.subs(onshell).doit()])
dust_lapse = red(s.diff(Ldust, N).subs(onshell).doit())
zero("dust stress from lapse variation before imposing its constraint",
     dust_lapse + density * r**2 / s.sqrt(1 - k * r**2))
zero("dust radial and angular pressures vanish on shell",
     [s.diff(Ldust, B).subs(onshell).doit(), s.diff(Ldust, radius).subs(onshell).doit()])
alpha = s.symbols("alpha", positive=True)
nonzero("wrong dust clock normalization fails the multiplier constraint", 1 - alpha**2)
nonzero("imposing the zero dust Lagrangian before variation loses nonzero density stress", dust_lapse)

# Entire center calculation in regular spatial Cartesian coordinates.
x = s.symbols("x y z", real=True)
ss = sum(v**2 for v in x)
beta = 1 - k * ss
g = s.eye(3) + k * s.Matrix(x) * s.Matrix(x).T / beta
gi = s.eye(3) - k * s.Matrix(x) * s.Matrix(x).T
zero("Cartesian metric inverse", list(g * gi - s.eye(3)))
Gamma = [[[red(sum(gi[a, l] * (s.diff(g[l, j], x[i]) + s.diff(g[l, i], x[j]) - s.diff(g[i, j], x[l])) / 2 for l in range(3)))
           for j in range(3)] for i in range(3)] for a in range(3)]
zero("Cartesian connection is regular at the center",
     [Gamma[a][i][j] - k * x[a] * g[i, j] for a in range(3) for i in range(3) for j in range(3)])
Ricci = s.Matrix(3, 3, lambda i, j: red(sum(
    s.diff(Gamma[a][i][j], x[a]) - s.diff(Gamma[a][i][a], x[j])
    + sum(Gamma[a][i][j] * Gamma[b][a][b] - Gamma[b][i][a] * Gamma[a][j][b] for b in range(3))
    for a in range(3))))
zero("direct Cartesian Ricci tensor", list(Ricci - 2 * k * g))
R4 = red(sum(gi[i, j] * Ricci[i, j] for i in range(3) for j in range(3)))
zero("direct curvature scalar", R4 - 6 * k)

F = (C - density * ss / 2) / beta
Aconst = 2 * k * C - density
grad = [s.diff(F, v) for v in x]
hessian = s.Matrix(3, 3, lambda i, j: red(s.diff(F, x[i], x[j]) - sum(Gamma[a][i][j] * grad[a] for a in range(3))))
norm = red(sum(gi[i, j] * grad[i] * grad[j] for i in range(3) for j in range(3)))
lap = red(sum(gi[i, j] * hessian[i, j] for i in range(3) for j in range(3)))
zero("Cartesian scalar Hessian",
     list(hessian - Aconst * g / beta - 3 * k * Aconst * s.Matrix(x) * s.Matrix(x).T / beta**3))
zero("Cartesian scalar gradient norm and Laplacian",
     [norm - Aconst**2 * ss / beta**3, lap - 3 * Aconst / beta**2])

field = s.symbols("field", positive=True)
Z = 3 * k / (density - 2 * k * field)
V = density / 2 + 3 * (density - 2 * k * field)**2 / (2 * (density - 2 * k * C))
Zf, Vf = Z.subs(field, F), V.subs(field, F)
temporal = red(F * R4 / 2 - density - Zf * norm / 2 - Vf - lap)
spatial = s.Matrix(3, 3, lambda i, j: red(
    F * (Ricci[i, j] - g[i, j] * R4 / 2)
    - Zf * (grad[i] * grad[j] - g[i, j] * norm / 2)
    + Vf * g[i, j] - hessian[i, j] + g[i, j] * lap))
scalar = red(R4 / 2 + Zf * lap + s.diff(Z, field).subs(field, F) * norm / 2 - s.diff(V, field).subs(field, F))
zero("entire family: temporal metric equation", temporal)
zero("entire family: all Cartesian spatial metric equations", list(spatial))
zero("entire family: direct scalar equation", scalar)

center = {v: 0 for v in x}
zero("regular center metric and connection", list(g.subs(center) - s.eye(3)) + [Gamma[a][i][j].subs(center) for a in range(3) for i in range(3) for j in range(3)])
zero("regular center field, Hessian and Laplacian",
     [F.subs(center) - C, norm.subs(center), lap.subs(center) - 3 * Aconst]
     + list(hessian.subs(center) - Aconst * s.eye(3)))
zero("finite center kinetic and potential values",
     [Zf.subs(center) - 3 * k / (density - 2 * k * C),
      Vf.subs(center) - (2 * density - 3 * k * C)])
zero("positive-kinetic identity", 2 * field * Z + 3 - 3 * density / (density - 2 * k * field))

beta_r = 1 - k * r**2
profile = (C - density * r**2 / 2) / beta_r
zero("normalized center homogeneous solution", s.diff(1 / beta_r, r) - (2 * k * r / beta_r) / beta_r)
zero("center-based affine integration yields the proposed profile", profile - (C - s.integrate(density * r, (r, 0, r))) / beta_r)
zero("radial profile derivative", s.diff(profile, r) - Aconst * r / beta_r**2)
zero("field-domain denominator identity", density - 2 * k * profile - (density - 2 * k * C) / beta_r)

# Keeping the potential labeled C but inserting the profile labeled C2 is
# not another on-shell family member. All other action/matter data stay fixed.
F2 = F.subs(C, C2)
V2 = V.subs(C, C2)
fixed_potential_metric = red(V.subs(field, F2) - V2.subs(field, F2))
fixed_potential_scalar = red(-s.diff(V, field).subs(field, F2) + s.diff(V2, field).subs(field, F2))
nonzero("changed central scalar at fixed potential fails the mixed temporal metric equation", fixed_potential_metric)
nonzero("changed central scalar at fixed potential fails the scalar equation", fixed_potential_scalar)
eta = s.symbols("eta", nonzero=True)
nonzero("changed source density at fixed geometry/profile/action fails the temporal equation", eta)
zero("different potentials on a common field interval",
     V - V2 - s.Rational(3, 2) * (density - 2 * k * field)**2 * (1 / (density - 2 * k * C) - 1 / (density - 2 * k * C2)))
zero("center potential derivative is independent of C", s.diff(V, field).subs(field, C) + 6 * k)
zero("center V second derivative divided by Z is independent of C",
     (s.diff(V, field, 2) / Z).subs(field, C) - 4 * k)

actual = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
checks.append({"name": "exact source identity", "kind": "provenance", "ok": actual == EXPECTED,
               "actual": actual, "expected": EXPECTED})
report = {
    "kind": "focused_independent_check_not_formal_audit",
    "utc_time": datetime.now(timezone.utc).isoformat(),
    "source_path": str(SOURCE), "source_sha256": actual,
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": platform.python_version(), "sympy": s.__version__,
    "checks": checks, "pass": sum(bool(c["ok"]) for c in checks), "fail": sum(not c["ok"] for c in checks),
}
(HERE / "factored_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for item in checks:
    print(f"{'PASS' if item['ok'] else 'FAIL'}: {item['name']}")
    if "residual" in item:
        print("  " + item["residual"])
    elif not item["ok"]:
        print("  " + str(item.get("residuals", item)))
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if report["fail"] == 0 else 1)
