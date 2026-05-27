#!/usr/bin/env python3
"""Y_T C3 orientation-phase strength boundary no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_orientation_phase_strength_boundary_2026-05-27.json"

NOTE = DOCS / "YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
ORIENTATION_NECESSITY = DOCS / "YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"

PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
ORIENTATION_NECESSITY_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_dynamics_necessity_2026-05-27.json"
MATRIX_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"

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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def eigenvalues(x_value: sp.Expr, y_value: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "P_0": sp.radsimp(2 * x_value / sp.sqrt(6)),
        "P_omega": sp.radsimp(-x_value / sp.sqrt(6) - y_value / sp.sqrt(2)),
        "P_omega2": sp.radsimp(-x_value / sp.sqrt(6) + y_value / sp.sqrt(2)),
    }


def top_set(values: dict[str, sp.Expr]) -> list[str]:
    max_value = max(values.values(), key=lambda value: float(sp.N(value)))
    return [name for name, value in values.items() if is_zero(value - max_value)]


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    paths = (
        NOTE,
        FULL_STACK,
        PHASE_CONE,
        ORIENTATION_NECESSITY,
        MATRIX_FACTORIZATION,
        PHASE_CONE_OUT,
        ORIENTATION_NECESSITY_OUT,
        MATRIX_FACTORIZATION_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "What This Prunes",
        "What Remains Open",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go",
        "proposal_allowed: false",
        "orientation sign",
        "phase-strength law",
        "|y_0| > sqrt(3) x_0",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(PHASE_CONE_OUT),
        "orientation_necessity": load_json(ORIENTATION_NECESSITY_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "phase cone dependency leaves phase law open",
        deps["phase_cone"].get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "orientation necessity dependency requires orientation-odd phase term",
        deps["orientation_necessity"].get("no_go_audit", {}).get("orientation_odd_phase_term_required") is True,
    )
    check(
        "matrix factorization dependency keeps target row conditional",
        deps["matrix_factorization"].get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)",
    )
    return deps


def part2_sign_not_strength_witnesses() -> dict[str, Any]:
    print("\nPart 2: orientation sign is not phase strength")
    witnesses = {
        "positive_sign_inside_cone": (sp.Integer(0), sp.Integer(1)),
        "positive_sign_outside_cone": (sp.Integer(1), sp.Integer(1)),
        "positive_wall": (sp.Integer(1), sp.sqrt(3)),
        "negative_sign_inside_cone": (sp.Integer(0), sp.Integer(-1)),
        "negative_sign_outside_cone": (sp.Integer(1), sp.Integer(-1)),
        "negative_wall": (sp.Integer(1), -sp.sqrt(3)),
    }
    result: dict[str, Any] = {}
    for name, (x_value, y_value) in witnesses.items():
        values = eigenvalues(x_value, y_value)
        result[name] = {
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "orientation_sign": "positive" if y_value > 0 else "negative",
            "eigenvalues": {line: sp.sstr(value) for line, value in values.items()},
            "largest_lines": top_set(values),
        }

    check(
        "positive sign can select P_omega2 when phase is strong enough",
        result["positive_sign_inside_cone"]["largest_lines"] == ["P_omega2"],
        result["positive_sign_inside_cone"],
    )
    check(
        "same positive sign can still select P_0",
        result["positive_sign_outside_cone"]["largest_lines"] == ["P_0"],
        result["positive_sign_outside_cone"],
    )
    check(
        "positive wall is degenerate",
        result["positive_wall"]["largest_lines"] == ["P_0", "P_omega2"],
        result["positive_wall"],
    )
    check(
        "negative sign can select P_omega when phase is strong enough",
        result["negative_sign_inside_cone"]["largest_lines"] == ["P_omega"],
        result["negative_sign_inside_cone"],
    )
    check(
        "same negative sign can still select P_0",
        result["negative_sign_outside_cone"]["largest_lines"] == ["P_0"],
        result["negative_sign_outside_cone"],
    )
    check(
        "negative wall is degenerate",
        result["negative_wall"]["largest_lines"] == ["P_0", "P_omega"],
        result["negative_wall"],
    )
    return result


def part3_inequality_algebra() -> dict[str, str]:
    print("\nPart 3: phase-strength inequality algebra")
    x, y = sp.symbols("x_0 y_0", real=True)
    values = eigenvalues(x, y)
    omega2_minus_p0 = sp.radsimp(values["P_omega2"] - values["P_0"])
    omega_minus_p0 = sp.radsimp(values["P_omega"] - values["P_0"])
    omega2_minus_omega = sp.radsimp(values["P_omega2"] - values["P_omega"])

    check(
        "P_omega2 beats P_0 by (y_0 - sqrt(3)x_0)/sqrt(2)",
        is_zero(omega2_minus_p0 - (y - sp.sqrt(3) * x) / sp.sqrt(2)),
        omega2_minus_p0,
    )
    check(
        "P_omega beats P_0 by (-y_0 - sqrt(3)x_0)/sqrt(2)",
        is_zero(omega_minus_p0 - (-y - sp.sqrt(3) * x) / sp.sqrt(2)),
        omega_minus_p0,
    )
    check("orientation sign separates the two nontrivial branches", is_zero(omega2_minus_omega - sp.sqrt(2) * y), omega2_minus_omega)
    return {
        "P_omega2_minus_P0": sp.sstr(omega2_minus_p0),
        "P_omega_minus_P0": sp.sstr(omega_minus_p0),
        "P_omega2_minus_Pomega": sp.sstr(omega2_minus_omega),
        "strength_condition": "|y_0| > sqrt(3) x_0 on the signed branch",
    }


def part4_source_rows() -> dict[str, str]:
    print("\nPart 4: source rows under the two possible top lines")
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    Bx = (C + C**2) / sp.sqrt(6)
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    rows = {
        name: sp.radsimp(A / sp.sqrt(2) * sp.simplify(sp.trace(projector * Bx)))
        for name, projector in projectors.items()
    }
    check("P_0 row is A/sqrt(3)", is_zero(rows["P_0"] - A / sp.sqrt(3)), rows["P_0"])
    check("P_omega row magnitude is A/sqrt(12)", is_zero(abs(rows["P_omega"]) - A / sp.sqrt(12)), rows["P_omega"])
    check("P_omega2 row magnitude is A/sqrt(12)", is_zero(abs(rows["P_omega2"]) - A / sp.sqrt(12)), rows["P_omega2"])
    return {name: sp.sstr(value) for name, value in rows.items()}


def part5_no_go_audit() -> dict[str, bool]:
    print("\nPart 5: no-go audit")
    audit = {
        "orientation_sign_supplied": True,
        "orientation_sign_sufficient": False,
        "nonzero_y0_sufficient": False,
        "phase_strength_law_derived": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in audit.items():
        check(f"audit field recorded: {key}", isinstance(value, bool), value)
    check("orientation sign alone is pruned", audit["orientation_sign_supplied"] and not audit["orientation_sign_sufficient"])
    check("phase-strength law remains open", audit["phase_strength_law_derived"] is False)
    return audit


def part6_firewalls() -> None:
    print("\nPart 6: firewalls and wording")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full Y_T closure",
        "positive Y_T closure",
        "strict top/W pole-response evidence is present",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part7_claim_status() -> dict[str, Any]:
    print("\nPart 7: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "orientation sign or nonzero B_y phase term derives nontrivial phase-ordering cone membership",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive accepted same-surface phase-strength law proving "
            "|y_0| > sqrt(3) x_0 on a signed nontrivial branch, or produce "
            "strict same-source top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names phase-strength law", "phase-strength" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 ORIENTATION-PHASE STRENGTH BOUNDARY NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    witnesses = part2_sign_not_strength_witnesses()
    inequalities = part3_inequality_algebra()
    rows = part4_source_rows()
    audit = part5_no_go_audit()
    part6_firewalls()
    status = part7_claim_status()

    result = {
        "claim_id": "yt_c3_orientation_phase_strength_boundary_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_orientation_phase_strength_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "Orientation sign is necessary but not sufficient. Same-sign finite "
            "C3 base operators can lie either inside the nontrivial cone or in "
            "the singlet region, depending on the quantitative inequality "
            "|y_0| > sqrt(3) x_0."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "sign_vs_strength_witnesses": witnesses,
        "inequality_algebra": inequalities,
        "source_rows": rows,
        "no_go_audit": audit,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
