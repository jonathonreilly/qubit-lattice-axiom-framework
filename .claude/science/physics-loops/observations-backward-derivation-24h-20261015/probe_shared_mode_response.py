#!/usr/bin/env python3
"""Exact development controls for the shared-mode research intake.

This is a rational linear-system probe, not a physical scalar model or data fit.
Inputs: the declared source note and this program for integrity, plus the
literal synthetic matrices below. Output: adjacent JSON evidence.
"""
from pathlib import Path
import hashlib
import json
import platform

import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/RECURSIVE_MECHANISMS_INTAKE_v1.md",
]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
checks = []


def check(name, value):
    checks.append({"name": name, "passed": bool(value)})


def matrix_zero(matrix):
    return all(sp.cancel(x) == 0 for x in matrix)


s = sp.symbols("s")
S = sp.Matrix([[1, 2], [0, 1]])
B = sp.Matrix([[1, 2], [3, 5]])
C = sp.Matrix([[2, 1], [1, 1]])
L = S * sp.diag(s + 1, s + 3) * S.inv()
G = C * L.inv() * B
residue = lambda pole: G.applyfunc(lambda x: sp.cancel((s - pole) * x).subs(s, pole))
R1, R3 = residue(-1), residue(-3)
check("first isolated pole has nonzero rank-one residue", R1.rank() == 1)
check("second isolated pole has nonzero rank-one residue", R3.rank() == 1)
v = S[:, 0]
w = S.inv()[0, :]
denominator = (w * L.diff(s) * v)[0]
check("non-normal residue equals left/right null-vector formula",
      matrix_zero(R1 - (C * v) * (w * B) / denominator))
check("two-channel minor vanishes at isolated pole", sp.cancel(R1.det()) == 0)
check("complete response need not be rank one",
      sp.cancel(G.det() + 1 / ((s + 1) * (s + 3))) == 0)
check("unresolved sum of distinct modes has rank two", (R1 + R3).rank() == 2)
T = sp.Matrix([[1, 1], [1, 2]])
G_changed = (C * T.inv()) * (T * L * T.inv()).inv() * (T * B)
check("consistent internal-coordinate change preserves observed transfer",
      matrix_zero(G_changed - G))
U = sp.Matrix([[2, 0], [1, 3]])
V = sp.Matrix([[1, 1], [0, 2]])
check("invertible channel changes preserve residue rank", (U * R1 * V).rank() == 1)
degenerate = sp.eye(2) / (s + 1)
Rd = degenerate.applyfunc(lambda x: sp.cancel((s + 1) * x).subs(s, -1))
check("two degenerate modes can have rank-two residue", Rd.rank() == 2)
singular = sp.Matrix([[1, 0], [2, 0]])
check("rank-losing readout can hide a second mode", (singular * Rd).rank() == 1)
a, b, c, d = sp.symbols("a b c d")
outer = sp.Matrix([a, b]) * sp.Matrix([[c, d]])
check("generic outer-product channel identity", sp.expand(outer.det()) == 0)

inputs = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
result = {
    "kind": "author-only synthetic linear-response direction probe",
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "input_sha256": inputs,
    "versions": {"python": platform.python_version(), "sympy": sp.__version__},
    "checks": checks,
    "first_residue": str(R1),
    "second_residue": str(R3),
    "full_response_determinant": str(sp.factor(G.det())),
    "passed": all(x["passed"] for x in checks),
    "empirical_validation": False,
    "independent_check": False,
    "scope": "Elementary finite-dimensional pole algebra only; no physical scalar response or mode assumption derived.",
}
output = HERE / "SHARED_MODE_PROBE_v1.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"checks": len(checks), "failures": [x["name"] for x in checks if not x["passed"]], "passed": result["passed"]}))
raise SystemExit(0 if result["passed"] else 1)
