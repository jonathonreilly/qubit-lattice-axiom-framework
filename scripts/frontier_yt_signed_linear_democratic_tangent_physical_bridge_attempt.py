#!/usr/bin/env python3
"""Signed-linear democratic tangent physical-bridge attempt for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_signed_linear_democratic_tangent_physical_bridge_attempt_2026-05-25.json"

NOTE = DOCS / "YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
LSP_SOURCE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
SIGNED_LINEAR = DOCS / "YT_QUBIT_SIGNED_LINEAR_SOURCE_RESPONSE_BRIDGE_CANDIDATE_NOTE_2026-05-25.md"
WARD = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    rows = json.loads(read(LEDGER))["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current authority")
    for path in (NOTE, AXIOMS, SOURCE_ACTION, LSP_SOURCE, ONE_HIGGS, SYMBOLIC_TOP, SIGNED_LINEAR, WARD, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Normalized Physical Trilinear Tensor",
        "Signed-Linear Source Tangent",
        "Exact Lambda Obstruction",
        "Primitive-Unit Branch",
        "Current Status",
        "Why This Is Not The Old Ward Trap",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    status_rows = {
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22"),
        "lsp_source": ledger_row("yt_lsp_signed_record_source_readout_support_note_2026-05-24"),
        "one_higgs": ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26"),
        "ew_mass": ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26"),
    }
    statuses = {key: None if row is None else row.get("effective_status") for key, row in status_rows.items()}
    check("source-action support row is present in the audit ledger (presence only)", status_rows["source_action"] is not None)
    check("LSP signed-record source support row is present in the audit ledger (presence only)", status_rows["lsp_source"] is not None)
    check("one-Higgs gauge selection row is present in the audit ledger (presence only)", status_rows["one_higgs"] is not None)
    check("EW mass theorem row is present in the audit ledger (presence only)", status_rows["ew_mass"] is not None)
    print(f"  [info] live effective statuses (audit-lane-owned; not gated): {statuses}")
    return statuses


def part2_normalized_trilinear_tensor() -> dict[str, str]:
    print("\nPart 2: normalized physical trilinear tensor")
    nc = sp.Integer(3)
    niso = sp.Integer(2)
    color = 1 / sp.sqrt(nc)
    iso = 1 / sp.sqrt(niso)
    combined = sp.simplify(color * iso)
    check("color singlet coefficient is 1/sqrt(3)", is_zero(color - 1 / sp.sqrt(3)), color)
    check("isospin singlet coefficient is 1/sqrt(2)", is_zero(iso - 1 / sp.sqrt(2)), iso)
    check("combined normalized trilinear coefficient is 1/sqrt(6)", is_zero(combined - 1 / sp.sqrt(6)), combined)

    # Unit norm of the factorized color x isospin singlet.
    coeffs = [combined for _color in range(3) for _iso in range(2)]
    norm = sum(c**2 for c in coeffs)
    check("six component coefficients have unit norm", is_zero(norm - 1), norm)
    check("each component coefficient is equal", len({sp.simplify(c) for c in coeffs}) == 1, coeffs[0])
    return {
        "color": "1/sqrt(3)",
        "isospin": "1/sqrt(2)",
        "combined": "1/sqrt(6)",
    }


def part3_signed_linear_tangent() -> dict[str, str]:
    print("\nPart 3: signed-linear democratic source tangent")
    n = 6
    s = sp.symbols("s")
    ops = sp.symbols("O0:6")
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    tangent_action = s * sum(u[i] * ops[i] for i in range(n))
    for i in (0, 2, 5):
        tangent_i = sp.diff(tangent_action, s).coeff(ops[i])
        check(f"component {i} tangent coefficient is 1/sqrt(6)", is_zero(tangent_i - 1 / sp.sqrt(6)), tangent_i)
    return {"primitive_unit_tangent_component": "1/sqrt(6)"}


def part4_lambda_family_obstruction() -> dict[str, str]:
    print("\nPart 4: lambda family obstruction")
    lam = sp.symbols("lambda", positive=True)
    coefficient = sp.simplify(lam / sp.sqrt(6))
    check("lambda family gives y_33(lambda)=lambda/sqrt(6)", is_zero(coefficient - lam / sp.sqrt(6)), coefficient)

    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    ray_lam = sp.simplify((lam * u) / sp.sqrt((lam * u).dot(lam * u)))
    check("positive lambda preserves the democratic ray", ray_lam == u, ray_lam)

    probability = sp.simplify((u[0]) ** 2)
    probability_lam_ray = sp.simplify((ray_lam[0]) ** 2)
    check("LSP projective probability remains 1/6 on the ray", is_zero(probability_lam_ray - sp.Rational(1, 6)), probability_lam_ray)
    check("projective probability cannot distinguish lambda", is_zero(probability_lam_ray - probability), probability_lam_ray - probability)

    y_a, y_b, g2 = sp.symbols("y_a y_b g_2", positive=True)
    ratio_a = sp.sqrt(2) * y_a / g2
    ratio_b = sp.sqrt(2) * y_b / g2
    check("same W denominator row admits different top coefficients", sp.simplify(ratio_a - ratio_b) != 0, ratio_a - ratio_b)
    return {
        "lambda_family": "y_33(lambda)=lambda/sqrt(6)",
        "structural_shortcut_closed": "false",
    }


def part5_primitive_unit_branch() -> dict[str, Any]:
    print("\nPart 5: primitive-unit branch")
    lam = sp.symbols("lambda", positive=True)
    eps = sp.symbols("epsilon", nonzero=True)
    score = lam * eps
    primitive_score = eps
    solution = sp.solve(sp.Eq(score, primitive_score), lam)
    check("primitive signed-record score forces lambda=1", solution == [1], solution)
    coefficient_at_unit = sp.simplify((lam / sp.sqrt(6)).subs(lam, 1))
    check("primitive-unit branch gives y_33=1/sqrt(6)", is_zero(coefficient_at_unit - 1 / sp.sqrt(6)), coefficient_at_unit)

    physical_source_premise_closed = False
    check("physical Yukawa equals primitive source tangent remains open", not physical_source_premise_closed)
    return {
        "conditional_if_primitive_physical_source": "y_33=1/sqrt(6)",
        "physical_source_premise_closed": physical_source_premise_closed,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls and old-trap audit")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status: retained",
        "proposed_retained",
        "positive retained Y_T closure",
        "unconditional y_33",
        "full retained closure",
        "old Ward route is repaired",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    ward = read(WARD).lower()
    check("old Ward note records H_unit definition trap", "definition of y_t_bare" in ward and "h_unit" in ward)
    check("new note does not import old Ward as authority", "ward/h_unit authority" not in note.lower())


def main() -> int:
    print("=" * 88)
    print("Y_T SIGNED-LINEAR DEMOCRATIC TANGENT PHYSICAL-BRIDGE ATTEMPT")
    print("=" * 88)

    statuses = part1_anchors()
    trilinear = part2_normalized_trilinear_tensor()
    tangent = part3_signed_linear_tangent()
    obstruction = part4_lambda_family_obstruction()
    primitive_unit = part5_primitive_unit_branch()
    part6_firewalls()

    result = {
        "status": "conditional support plus exact obstruction",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The primitive-unit branch proves y_33=1/sqrt(6) only if the physical "
            "top Yukawa deformation is accepted as the primitive signed-linear "
            "source/action tangent. Without that premise, lambda remains free."
        ),
        "bare_retained_allowed": False,
        "trilinear": trilinear,
        "signed_linear_tangent": tangent,
        "lambda_obstruction": obstruction,
        "primitive_unit_branch": primitive_unit,
        "upstream_statuses": statuses,
        "remaining_bridge": (
            "derive physical top Yukawa deformation = primitive unit signed-linear "
            "source/action tangent on the normalized top trilinear"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md",
            "scripts/frontier_yt_signed_linear_democratic_tangent_physical_bridge_attempt.py",
            "outputs/yt_signed_linear_democratic_tangent_physical_bridge_attempt_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
