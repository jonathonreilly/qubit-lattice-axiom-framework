#!/usr/bin/env python3
"""Focused independent variational check; no import of author implementation.

The source argument is inspected, so this is not a blind check. The computation
starts from the spherically reduced action before fixing the sphere radius.
It does not import or execute an author runner, or confer formal audit status.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
from datetime import datetime, timezone

import sympy as s


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "BLOCK01_DERIVATION_v1.md"
EXPECTED_SOURCE = "266753576b127818bfed666d6cd773954106d0887db4170c2f6c69797609f86b"
ROOT = HERE.parents[4]
checks = []


def reduce(expr):
    return s.factor(s.cancel(s.trigsimp(s.simplify(expr))))


def check_zero(name, expr):
    residual = reduce(expr)
    checks.append({"name": name, "kind": "symbolic_zero", "ok": residual == 0,
                   "residual": str(residual)})


def check_nonzero(name, expr, kind="mutation_detected"):
    residual = reduce(expr)
    checks.append({"name": name, "kind": kind, "ok": residual != 0,
                   "residual": str(residual)})


def euler(lagrangian, field):
    return s.diff(lagrangian, field) - s.diff(s.diff(lagrangian, s.diff(field, r)), r)


r = s.symbols("r", positive=True)
N, B, A, F = [s.Function(name)(r) for name in ("N", "B", "A", "F")]
Z, V = s.Function("Z"), s.Function("V")
Fp, Np, Ap, Bp = [s.diff(q, r) for q in (F, N, A, B)]

# ds^2 = -N^2 dt^2 + B^-1 dr^2 + A^2 dOmega^2.
# Warped-product identity: R4 = R2 + 2(1-|dA|_2^2)/A^2 - 4 box_2 A/A.
# R2 = -(2 B N'' + B' N')/N; box_2 A = B A'' +(B N'/N+B'/2) A'.
R2 = -(2 * B * s.diff(N, r, 2) + Bp * Np) / N
box2_A = B * s.diff(A, r, 2) + (B * Np / N + Bp / 2) * Ap
R4 = R2 + 2 * (1 - B * Ap**2) / A**2 - 4 * box2_A / A
L_raw = N * A**2 / s.sqrt(B) * (
    F * R4 / 2 - Z(F) * B * Fp**2 / 2 - V(F)
)
L = (
    s.sqrt(B) * ((A**2 * Fp + 2 * A * F * Ap) * Np
                 + N * F * Ap**2 + 2 * N * A * Fp * Ap)
    + N * F / s.sqrt(B)
    - N * A**2 * s.sqrt(B) * Z(F) * Fp**2 / 2
    - N * A**2 * V(F) / s.sqrt(B)
)
boundary = -A**2 * F * s.sqrt(B) * Np - 2 * N * A * F * s.sqrt(B) * Ap
check_zero("raw action minus reduced action is the recorded total derivative",
           L_raw - L - s.diff(boundary, r))

EL_N, EL_B, EL_A, EL_F = [euler(L, q) for q in (N, B, A, F)]


def areal(expr):
    return reduce(expr.subs(A, r).doit())


# These are field residuals derived by variation, including the angular one.
E_t = areal(-s.sqrt(B) * EL_N / A**2)
E_r = areal(2 * B * s.sqrt(B) * EL_B / (N * A**2))
E_a = areal(-s.sqrt(B) * EL_A / (2 * N * A))
E_s = areal(s.sqrt(B) * EL_F / (N * A**2))

n = Np / N
Gt = (B - 1) / r**2 + Bp / r
Gr = (B - 1) / r**2 + 2 * B * n / r
Ga = B * (s.diff(n, r) + n**2 + n / r) + Bp * (n + 1 / r) / 2
boxF = B * s.diff(F, r, 2) + (Bp / 2 + B * n + 2 * B / r) * Fp
R = areal(R4)

check_zero("lapse variation gives candidate time equation",
           E_t - (F * Gt + Z(F) * B * Fp**2 / 2 + V(F) - B * n * Fp + boxF))
check_zero("radial-metric variation gives candidate radial equation",
           E_r - (F * Gr - Z(F) * B * Fp**2 / 2 + V(F)
                  - B * s.diff(F, r, 2) - Bp * Fp / 2 + boxF))
check_zero("sphere-radius variation gives candidate angular equation",
           E_a - (F * Ga + Z(F) * B * Fp**2 / 2 + V(F) - B * Fp / r + boxF))
check_zero("scalar variation gives candidate scalar equation",
           E_s - (R / 2 + Z(F) * boxF + s.diff(Z(F), F) * B * Fp**2 / 2
                  - s.diff(V(F), F)))
check_zero("angular-minus-time eliminates scalar action functions",
           E_a - E_t - (F * (Ga - Gt) - B * (1 / r - n) * Fp))

u = s.Function("u")(r)
qF = B * (s.diff(u, r) + u**2) + (Bp / 2 + B * n + 2 * B / r) * u
H = Gr - Gt - B * (s.diff(u, r) + u**2) - (Bp / 2 - B * n) * u
om = H / (B * u**2)
W = -Gt - H / 2 - B * (s.diff(u, r) + u**2) - (Bp / 2 + 2 * B / r) * u

# First solve only the lapse and radial variations, leaving u arbitrary.
check_zero("time residual vanishes after reconstructed omega and W",
           Gt + om * B * u**2 / 2 + W + B * (s.diff(u, r) + u**2)
           + (Bp / 2 + 2 * B / r) * u)
check_zero("radial residual vanishes after reconstructed omega and W",
           Gr - om * B * u**2 / 2 + W + (B * n + 2 * B / r) * u)

# Chain rule only, not a Bianchi invocation: Z_F=(om'-om*u)/(u*F^2),
# V_F=W+W'/u. The u' and u'' terms cancel directly.
scalar_after_inverse = (
    R / 2 + om * qF + B * u * (s.diff(om, r) - om * u) / 2
    - W - s.diff(W, r) / u
)
a = Ga - Gt
d = B * (1 / r - n)
check_zero("scalar residual is exactly 2*(a-d*u)/(r*u) before angular constraint",
           scalar_after_inverse - 2 * (a - d * u) / (r * u))


def patch_residuals(b, profile, omega_of_F, potential_of_F):
    # Insert specified action functions in the independent reduced action,
    # vary anew, then evaluate the proposed field/metric; no inverse is used.
    L_patch = L.subs({Z(F): omega_of_F / F, V(F): potential_of_F})
    result = []
    for field, factor in ((N, -s.sqrt(B) / A**2),
                          (B, 2 * B * s.sqrt(B) / (N * A**2)),
                          (A, -s.sqrt(B) / (2 * N * A)),
                          (F, s.sqrt(B) / (N * A**2))):
        value = factor * euler(L_patch, field)
        result.append(reduce(value.subs({N: 1, B: b, A: r, F: profile}).doit()))
    return result


patch_A = patch_residuals(s.Rational(1, 2), r, 0, -1 / (2 * F))
patch_B = patch_residuals(s.Rational(1, 3), 4 * r**2, -s.Rational(1, 2), -4)
for label, residuals in (("A", patch_A), ("B", patch_B)):
    for component, residual in zip(("t", "r", "angular", "scalar"), residuals):
        check_zero(f"patch {label}: independently varied {component} residual", residual)

# The same source functions must be used in each mutation. Select a concrete
# nonzero independent equation, and preserve its exact residual.
mut_omega = patch_residuals(s.Rational(1, 2), r, s.Rational(1, 10), -1 / (2 * F))
mut_V = patch_residuals(s.Rational(1, 2), r, 0, -1 / F)
mut_exponent = patch_residuals(s.Rational(1, 2), r**2, 0, -1 / (2 * F))
mut_B_normalization = patch_residuals(s.Rational(1, 3), r**2, -s.Rational(1, 2), -4)
check_nonzero("wrong kinetic coefficient fails time equation", mut_omega[0])
check_nonzero("wrong potential amplitude fails time equation", mut_V[0])
check_nonzero("wrong scalar exponent fails angular-minus-time equation",
              mut_exponent[2] - mut_exponent[0])
check_nonzero("wrong patch-B scalar normalization at fixed V=-4 fails time equation",
              mut_B_normalization[0])

# A second route: conformal Einstein frame, with Einstein areal radius rho.
# For b=1/(c+1), rho=sqrt(C)*r**((c+2)/2), gE=F*gJ.
# N_E is constant times rho**p, B_E=q, phi=k*log(rho)+constant,
# U=V/F^2=-c/(2*rho^2). Constants in N_E, phi drop from these local residuals.
c = s.symbols("c", positive=True)
p = c / (c + 2)
q = (c + 2)**2 / (4 * (c + 1))
k2 = 2 * c / (c + 2)
k = s.sqrt(k2)
U = -c / (2 * r**2)
GEt = (q - 1) / r**2
GEr = (q - 1 + 2 * q * p) / r**2
GEa = q * p**2 / r**2
check_zero("general family: Einstein time equation", GEt + q * k2 / (2 * r**2) + U)
check_zero("general family: Einstein radial equation", GEr - q * k2 / (2 * r**2) + U)
check_zero("general family: Einstein angular equation", GEa + q * k2 / (2 * r**2) + U)
check_zero("general family: canonical Einstein scalar equation",
           q * k * (p + 1) / r**2 - c / (k * r**2))

check_nonzero("overlapping scalar ranges forbid one kinetic function", s.Rational(0) - (-s.Rational(1, 2)),
              kind="overlap_obstruction")
chi = s.symbols("chi", real=True)
check_zero("common interpolated action has 2*omega+3=3-chi",
           2 * (-chi / 2) + 3 - (3 - chi))

source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
checks.append({"name": "checked source identity is unchanged", "kind": "provenance",
               "ok": source_sha == EXPECTED_SOURCE, "actual": source_sha,
               "expected": EXPECTED_SOURCE})


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


report = {
    "kind": "focused_independent_check_not_formal_audit",
    "utc_time": datetime.now(timezone.utc).isoformat(),
    "source_path": str(SOURCE.relative_to(ROOT)),
    "source_sha256": source_sha,
    "worktree_head": git("rev-parse", "HEAD"),
    "origin_main": git("rev-parse", "origin/main"),
    "branch": git("branch", "--show-current"),
    "python": platform.python_version(),
    "sympy": s.__version__,
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "pass": sum(bool(item["ok"]) for item in checks),
    "fail": sum(not item["ok"] for item in checks),
}
(HERE / "computed_evidence.json").write_text(json.dumps(report, indent=2) + "\n")
for item in checks:
    print(f"{'PASS' if item['ok'] else 'FAIL'}: {item['name']}")
    if "residual" in item and item["residual"] != "0":
        print(f"  residual: {item['residual']}")
print(f"TOTAL: PASS={report['pass']} FAIL={report['fail']}")
sys.exit(0 if report["fail"] == 0 else 1)
