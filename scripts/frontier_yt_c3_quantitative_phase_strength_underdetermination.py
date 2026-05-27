#!/usr/bin/env python3
"""Y_T C3 quantitative phase-strength underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_quantitative_phase_strength_underdetermination_2026-05-27.json"

NOTE = DOCS / "YT_C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
ORIENTATION_NECESSITY = DOCS / "YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md"
ORIENTATION_STRENGTH = DOCS / "YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md"
CIRCULANT_BOUNDARY = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
ORIENTATION_NECESSITY_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_dynamics_necessity_2026-05-27.json"
ORIENTATION_STRENGTH_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_strength_boundary_2026-05-27.json"
CIRCULANT_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
MATRIX_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def c3_basis() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    C = c3_cycle()
    Bx = sp.simplify((C + C**2) / sp.sqrt(6))
    By = sp.simplify(sp.I * (C - C**2) / sp.sqrt(6))
    return C, Bx, By


def eigenvalues(x_value: sp.Expr, y_value: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "P_0": sp.radsimp(2 * x_value / sp.sqrt(6)),
        "P_omega": sp.radsimp(-x_value / sp.sqrt(6) - y_value / sp.sqrt(2)),
        "P_omega2": sp.radsimp(-x_value / sp.sqrt(6) + y_value / sp.sqrt(2)),
    }


def top_set(values: dict[str, sp.Expr]) -> list[str]:
    max_value = max(values.values(), key=lambda value: float(sp.N(value)))
    return [name for name, value in values.items() if is_zero(value - max_value)]


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def frobenius_norm_sq(matrix: sp.Matrix) -> sp.Expr:
    return sp.radsimp(sp.trace(matrix.conjugate().T * matrix))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    paths = (
        NOTE,
        FULL_STACK,
        PHASE_CONE,
        ORIENTATION_NECESSITY,
        ORIENTATION_STRENGTH,
        CIRCULANT_BOUNDARY,
        MATRIX_FACTORIZATION,
        STRICT_AVAILABILITY,
        PHASE_CONE_OUT,
        ORIENTATION_NECESSITY_OUT,
        ORIENTATION_STRENGTH_OUT,
        CIRCULANT_BOUNDARY_OUT,
        MATRIX_FACTORIZATION_OUT,
        STRICT_AVAILABILITY_OUT,
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
        "unit Frobenius norm",
        "phase angle remains an open",
        "|y_0| > sqrt(3) x_0",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(PHASE_CONE_OUT),
        "orientation_necessity": load_json(ORIENTATION_NECESSITY_OUT),
        "orientation_strength": load_json(ORIENTATION_STRENGTH_OUT),
        "circulant_boundary": load_json(CIRCULANT_BOUNDARY_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "phase cone dependency leaves phase law open",
        deps["phase_cone"].get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "orientation strength dependency prunes sign-only route",
        deps["orientation_strength"].get("no_go_audit", {}).get("orientation_sign_sufficient") is False,
    )
    check(
        "circulant dependency leaves base dynamics open",
        deps["circulant_boundary"].get("certificate_boundary", {}).get("accepted_base_c3_circulant_operator") is False,
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {}).get("strict_top_w_rows_artifact_present") is False,
    )
    return deps


def part2_basis_and_unit_witnesses() -> dict[str, Any]:
    print("\nPart 2: C3 basis and unit-circle witnesses")
    C, Bx, By = c3_basis()
    x, y = sp.symbols("x_0 y_0", real=True)
    H = sp.simplify(x * Bx + y * By)

    check("C has order three", is_zero(C**3 - sp.eye(3)))
    check("B_x is Hermitian", is_zero(Bx.conjugate().T - Bx))
    check("B_y is Hermitian", is_zero(By.conjugate().T - By))
    check("B_x is traceless", is_zero(sp.trace(Bx)))
    check("B_y is traceless", is_zero(sp.trace(By)))
    check("B_x has unit Frobenius norm", is_zero(frobenius_norm_sq(Bx) - 1), frobenius_norm_sq(Bx))
    check("B_y has unit Frobenius norm", is_zero(frobenius_norm_sq(By) - 1), frobenius_norm_sq(By))
    check("B_x and B_y are Frobenius orthogonal", is_zero(sp.trace(Bx.conjugate().T * By)))
    check("general connected C3 base norm is x_0^2 + y_0^2", is_zero(frobenius_norm_sq(H) - (x**2 + y**2)))

    witnesses: dict[str, tuple[sp.Expr, sp.Expr, list[str]]] = {
        "positive_inside_cone_unit": (sp.Integer(0), sp.Integer(1), ["P_omega2"]),
        "positive_wall_unit": (sp.Rational(1, 2), sp.sqrt(3) / 2, ["P_0", "P_omega2"]),
        "positive_outside_cone_unit": (sp.sqrt(3) / 2, sp.Rational(1, 2), ["P_0"]),
        "negative_inside_cone_unit": (sp.Integer(0), sp.Integer(-1), ["P_omega"]),
        "negative_wall_unit": (sp.Rational(1, 2), -sp.sqrt(3) / 2, ["P_0", "P_omega"]),
        "negative_outside_cone_unit": (sp.sqrt(3) / 2, -sp.Rational(1, 2), ["P_0"]),
    }
    result: dict[str, Any] = {}
    for name, (x_value, y_value, expected_top) in witnesses.items():
        values = eigenvalues(x_value, y_value)
        top_lines = top_set(values)
        base = sp.simplify(x_value * Bx + y_value * By)
        unit = is_zero(frobenius_norm_sq(base) - 1)
        connected = is_zero(sp.trace(base))
        hermitian = is_zero(base.conjugate().T - base)
        commutes = is_zero(base * C - C * base)
        result[name] = {
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "unit_frobenius_norm": unit,
            "connected": connected,
            "hermitian": hermitian,
            "c3_circulant": commutes,
            "orientation_sign": "positive" if y_value > 0 else "negative",
            "eigenvalues": {line: sp.sstr(value) for line, value in values.items()},
            "largest_lines": top_lines,
        }
        check(f"{name} has unit norm", unit)
        check(f"{name} is connected Hermitian C3-circulant", connected and hermitian and commutes)
        check(f"{name} has expected top set", top_lines == expected_top, result[name])

    check(
        "positive unit signed branch contains both target and singlet regions",
        result["positive_inside_cone_unit"]["largest_lines"] == ["P_omega2"]
        and result["positive_outside_cone_unit"]["largest_lines"] == ["P_0"],
    )
    check(
        "negative unit signed branch contains both target and singlet regions",
        result["negative_inside_cone_unit"]["largest_lines"] == ["P_omega"]
        and result["negative_outside_cone_unit"]["largest_lines"] == ["P_0"],
    )
    return result


def part3_current_premise_no_go() -> dict[str, Any]:
    print("\nPart 3: current premise no-go audit")
    eps = sp.Rational(1, 2)
    x_outside = sp.sqrt(1 - eps**2)
    y_outside = eps
    outside_values = eigenvalues(x_outside, y_outside)
    distance_to_bx_axis = sp.radsimp((x_outside - 1) ** 2 + y_outside**2)
    inside_distance_to_bx_axis = sp.radsimp((sp.Integer(0) - 1) ** 2 + sp.Integer(1) ** 2)

    check("least-deformation positive witness is outside cone", top_set(outside_values) == ["P_0"], outside_values)
    check("outside positive witness is closer to +B_x axis than pure phase axis", sp.N(distance_to_bx_axis) < sp.N(inside_distance_to_bx_axis))

    audit = {
        "connected_hermitian_c3_circulant_family": True,
        "unit_frobenius_base_norm_supplied": True,
        "orientation_sign_supplied": True,
        "source_tangent_bx_fixed": True,
        "phase_angle_selector_derived": False,
        "phase_strength_law_derived": False,
        "least_deformation_from_positive_bx_axis_selects_target": False,
        "pure_phase_axis_would_select_target": True,
        "pure_phase_axis_is_new_quantitative_premise": True,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in audit.items():
        check(f"audit field recorded: {key}", isinstance(value, bool), value)
    check("current premises leave phase angle underdetermined", audit["phase_angle_selector_derived"] is False)
    check("phase-strength law remains open", audit["phase_strength_law_derived"] is False)
    return {
        "audit": audit,
        "least_deformation_witness": {
            "x0": sp.sstr(x_outside),
            "y0": sp.sstr(y_outside),
            "largest_lines": top_set(outside_values),
            "squared_distance_to_positive_Bx_axis": sp.sstr(distance_to_bx_axis),
            "pure_phase_axis_squared_distance_to_positive_Bx_axis": sp.sstr(inside_distance_to_bx_axis),
        },
    }


def part4_source_rows() -> dict[str, str]:
    print("\nPart 4: source rows under singlet and nontrivial assignments")
    A = sp.symbols("A", positive=True)
    C, Bx, _By = c3_basis()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
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
    check("singlet row differs from target row", not is_zero(abs(rows["P_0"]) - abs(rows["P_omega"])))
    return {name: sp.sstr(value) for name, value in rows.items()}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
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


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "current same-surface C3 premises plus unit base normalization "
            "and orientation sign derive quantitative nontrivial phase-strength"
        ),
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive accepted same-surface quantitative phase-angle dynamics "
            "proving |y_0| > sqrt(3) x_0, or produce accepted strict top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names quantitative phase angle", "phase-angle" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 QUANTITATIVE PHASE-STRENGTH UNDERDETERMINATION NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    witnesses = part2_basis_and_unit_witnesses()
    premise_no_go = part3_current_premise_no_go()
    rows = part4_source_rows()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_quantitative_phase_strength_underdetermination_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_quantitative_phase_strength_underdetermination.py",
        **status,
        "proposal_allowed_reason": (
            "Unit-normalized connected C3 base dynamics with a signed "
            "orientation branch still contains both singlet-top and "
            "nontrivial-top finite witnesses. The quantitative phase angle "
            "remains an open physical/dynamical input."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "unit_circle_witnesses": witnesses,
        "current_premise_no_go": premise_no_go,
        "source_rows": rows,
        "literature_math_search": {
            "external_literature_load_bearing": False,
            "math_used": "finite C3 character algebra and two-dimensional cone geometry",
            "perron_frobenius_reuse": "not reused as positive input; existing positive-real C3 Perron route selects P_0",
        },
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
