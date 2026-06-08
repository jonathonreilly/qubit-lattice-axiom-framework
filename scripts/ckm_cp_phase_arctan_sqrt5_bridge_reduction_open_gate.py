#!/usr/bin/env python3
"""CKM CP phase arctan(sqrt5) bridge-reduction open-gate runner.

This runner verifies the exact symbolic reduction

    cos^2(delta) = 1 / n_quark

and exhibits the remaining open bridge choices. It does not assert a global
no-go, register a Tier-A admission, approve a primitive, or use empirical
gamma data as a derivation input.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


RESULTS: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    RESULTS.append((label, bool(condition)))


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def norm_doc(filename: str) -> str:
    text = (DOCS / filename).read_text(encoding="utf-8")
    text = text.replace("`", "").replace("**", "")
    return re.sub(r"\s+", " ", text)


radius, w_sym = sp.symbols("radius w_sym", positive=True)
rho = radius * sp.sqrt(w_sym)
eta = radius * sp.sqrt(1 - w_sym)
cos2_delta = sp.simplify(rho**2 / (rho**2 + eta**2))
check(
    "radius cancellation: cos^2(delta)=rho^2/(rho^2+eta^2)=w_sym",
    sp.simplify(cos2_delta - w_sym) == 0,
)

n = sp.symbols("n", positive=True, integer=True)
democratic_overlap = 1 / sp.sqrt(n)
check(
    "democratic projector: one basis-state weight is |<dem|e_i>|^2=1/n",
    sp.simplify(democratic_overlap**2 - 1 / n) == 0,
)

dem6 = sp.Matrix([1] * 6) / sp.sqrt(6)
projector6 = dem6 * dem6.T
e1 = sp.Matrix([1, 0, 0, 0, 0, 0])
check(
    "explicit six-state projector: <e_1|P_sym|e_1>=1/6",
    sp.simplify((e1.T * projector6 * e1)[0, 0] - sp.Rational(1, 6)) == 0,
)

angle6 = sp.atan(sp.sqrt(5))
check(
    "n_quark=6 choice gives tan(delta)=sqrt(5) and cos(delta)=1/sqrt(6)",
    sp.simplify(sp.tan(angle6) - sp.sqrt(5)) == 0
    and sp.simplify(sp.cos(angle6) - 1 / sp.sqrt(6)) == 0,
)

delta_deg = sp.deg(angle6)
check(
    "delta=65.9051574... degrees for the supplied n_quark=6 bridge",
    abs(float(delta_deg) - 65.9051574478893) < 1e-9,
)


def angle_from_symmetric_block(block_dim: int, total_dim: int) -> sp.Expr:
    return sp.deg(sp.acos(sp.sqrt(sp.Rational(block_dim, total_dim))))


angle_1_plus_5 = angle_from_symmetric_block(1, 6)
angle_2_plus_4 = angle_from_symmetric_block(2, 6)
angle_3_plus_3 = angle_from_symmetric_block(3, 6)
check(
    "projector split is load-bearing: 1+5, 2+4, and 3+3 give different angles",
    abs(float(angle_1_plus_5) - 65.9051574) < 1e-5
    and abs(float(angle_2_plus_4) - 54.7356103) < 1e-5
    and float(angle_3_plus_3) == 45.0,
)

generation3_angle = sp.deg(sp.acos(1 / sp.sqrt(3)))
check(
    "three-generation democratic count gives 54.736 degrees, not arctan(sqrt5)",
    abs(float(generation3_angle) - 54.7356103) < 1e-6
    and sp.simplify(generation3_angle - delta_deg) != 0,
)

rho_value = sp.Rational(1, 6)
eta_value = sp.sqrt(5) / 6
n_pair = 2
n_color = 3
check(
    "inverse-square count identity restates eta=sqrt(5)/6",
    sp.simplify(eta_value**2 - (sp.Rational(1, n_pair**2) - sp.Rational(1, n_color**2))) == 0,
)
check(
    "inverse-square count identity restates the same rho/eta radius",
    sp.simplify(eta_value**2 + rho_value * sp.Rational(n_pair, n_color) - sp.Rational(1, n_pair**2))
    == 0,
)

kr_doc = norm_doc("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
check(
    "K_R carrier note is open_gate and leaves physical tensor-primitive meaning asserted",
    ("Claim type: open_gate" in kr_doc)
    and ("three upstream gaps" in kr_doc)
    and ("physical meaning is asserted" in kr_doc)
    and ("no primitive theorem asserted" in kr_doc),
)

registry = json.loads((DOCS / "audit/data/axiom_premise_nodes.json").read_text(encoding="utf-8"))
approved_paths = {node["current_path"] for node in registry["nodes"].values()}
check(
    "K_R carrier note is not an approved axiom/primitive premise node",
    "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md" not in approved_paths,
)

rho_eta_doc = norm_doc("CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md")
check(
    "rho/eta theorem does not derive the 1+5 projector split",
    ("Does not derive w_axis = 1/6 or w_perp = 5/6" in rho_eta_doc)
    and ("Does not claim that the 1 + 5 decomposition is forced" in rho_eta_doc),
)

atlas_doc = norm_doc("CKM_ATLAS_AXIOM_CLOSURE_NOTE.md")
check(
    "CKM atlas supplies n_quark=2x3=6 and delta_source=2*pi/3 as construction inputs",
    ("n_quark = 2 x 3 = 6" in atlas_doc) and ("delta_source = 2*pi/3" in atlas_doc),
)

passes = sum(1 for _, ok in RESULTS if ok)
fails = sum(1 for _, ok in RESULTS if not ok)
for label, ok in RESULTS:
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
print(f"\nSCORECARD PASS={passes} FAIL={fails}")

if fails:
    raise SystemExit(1)

print(
    "\nRESULT: the exact arctan(sqrt5) angle follows once the supplied bridge "
    "cos^2(delta)=1/n_quark is granted. The runner verifies the forced "
    "projector/trigonometric skeleton and exhibits the open bridge choices; "
    "it does not register an admission, no-go, primitive, or audit verdict."
)
