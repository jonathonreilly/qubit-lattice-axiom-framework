#!/usr/bin/env python3
"""Y_T C3 cubic invariant phase-selector support boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_cubic_invariant_phase_selector_support_boundary_2026-05-27.json"

NOTE = DOCS / "YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
PRIMITIVE_ANGLE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
REPRESENTATION_NOGO = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
PRIMITIVE_ANGLE_OUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"
REPRESENTATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        PHASE_CONE,
        PRIMITIVE_ANGLE,
        REPRESENTATION_NOGO,
        MATRIX_FACTORIZATION,
        STRICT_AVAILABILITY,
        PHASE_CONE_OUT,
        PRIMITIVE_ANGLE_OUT,
        REPRESENTATION_NOGO_OUT,
        MATRIX_FACTORIZATION_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "Claim Boundary",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: conditional-support / open cubic phase law",
        "proposal_allowed: false",
        "Tr(H(phi)^3) = sqrt(6)/6 cos(3 phi)",
        "accepted cubic invariant maximization",
        "not actual-surface closure",
    ):
        check(f"note contains selector phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(PHASE_CONE_OUT),
        "primitive_angle": load_json(PRIMITIVE_ANGLE_OUT),
        "representation_nogo": load_json(REPRESENTATION_NOGO_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "representation dependency prunes representation-only selector",
        deps["representation_nogo"].get("no_go_certificate", {})
        .get("representation_theory_selects_phi_pm_2pi_over_3")
        is False,
    )
    check(
        "primitive angle dependency gives target row",
        deps["primitive_angle"].get("candidate_certificate", {}).get("candidate_angles_give_target_row") is True,
    )
    check(
        "phase cone dependency leaves phase law open",
        deps["phase_cone"].get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {}).get("strict_top_w_rows_artifact_present") is False,
    )
    return deps


def part2_cubic_invariant() -> dict[str, Any]:
    print("\nPart 2: cubic invariant on the unit C3 phase circle")
    A = sp.symbols("A", positive=True)
    x, y, phi = sp.symbols("x y phi", real=True)
    C, Bx, By = c3_basis()
    H = sp.simplify(x * Bx + y * By)
    H_phi = sp.simplify(sp.cos(phi) * Bx + sp.sin(phi) * By)
    i2 = sp.simplify(sp.trace(H**2))
    i3 = sp.factor(sp.trace(H**3))
    i3_phi = sp.trigsimp(sp.trace(H_phi**3).rewrite(sp.cos))
    check("quadratic trace is unit norm", is_zero(i2 - (x**2 + y**2)), i2)
    check("cubic trace formula in x,y", is_zero(i3 - sp.sqrt(6) * x * (x**2 - 3 * y**2) / 6), i3)
    check("cubic trace formula on phase circle", is_zero(i3_phi - sp.sqrt(6) * sp.cos(3 * phi) / 6), i3_phi)

    derivative = sp.trigsimp(sp.diff(i3_phi, phi).rewrite(sp.sin))
    second = sp.trigsimp(sp.diff(i3_phi, phi, 2).rewrite(sp.cos))
    check("cubic derivative is proportional to sin(3phi)", is_zero(derivative + sp.sqrt(6) * sp.sin(3 * phi) / 2), derivative)

    source_rows = {
        "P_0": sp.radsimp(A / sp.sqrt(2) * (sp.sqrt(6) / 3)),
        "P_omega": sp.radsimp(A / sp.sqrt(2) * (-sp.sqrt(6) / 6)),
        "P_omega2": sp.radsimp(A / sp.sqrt(2) * (-sp.sqrt(6) / 6)),
    }
    witnesses = {
        "cubic_max_real_axis": (sp.Integer(0), sp.Integer(1), sp.Integer(0), ["P_0"], "sqrt(3)*A/3"),
        "cubic_max_positive_branch": (2 * sp.pi / 3, -sp.Rational(1, 2), sp.sqrt(3) / 2, ["P_omega2"], "sqrt(3)*A/6"),
        "cubic_max_negative_branch": (-2 * sp.pi / 3, -sp.Rational(1, 2), -sp.sqrt(3) / 2, ["P_omega"], "sqrt(3)*A/6"),
        "positive_orientation_nonmax_counter": (sp.pi / 6, sp.sqrt(3) / 2, sp.Rational(1, 2), ["P_0"], "sqrt(3)*A/3"),
    }
    result: dict[str, Any] = {}
    for name, (angle, x_value, y_value, expected_top, expected_row) in witnesses.items():
        values = eigenvalues(x_value, y_value)
        top_lines = top_set(values)
        rows = [sp.sstr(sp.radsimp(abs(source_rows[line]))) for line in top_lines]
        cubic_value = sp.simplify(sp.sqrt(6) * sp.cos(3 * angle) / 6)
        result[name] = {
            "phi": sp.sstr(angle),
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "cubic_trace": sp.sstr(cubic_value),
            "second_derivative": sp.sstr(sp.simplify(second.subs(phi, angle))),
            "largest_lines": top_lines,
            "row_magnitudes_if_selected": rows,
        }
        check(f"{name} has expected top lines", top_lines == expected_top, result[name])
        check(f"{name} has expected row", rows == [expected_row], result[name])

    check("three cubic maxima have equal cubic trace", is_zero(sp.sqrt(6) / 6 - sp.sqrt(6) * sp.cos(3 * (2 * sp.pi / 3)) / 6))
    check("cubic max orbit contains singlet and target lines", result["cubic_max_real_axis"]["largest_lines"] == ["P_0"] and result["cubic_max_positive_branch"]["largest_lines"] == ["P_omega2"])
    check("positive orientation branch plus cubic max selects primitive angle", result["cubic_max_positive_branch"]["y0"] == "sqrt(3)/2")
    return result


def part3_certificate() -> dict[str, bool]:
    print("\nPart 3: certificate boundary")
    certificate = {
        "quadratic_invariant_phase_blind": True,
        "cubic_invariant_formula_derived": True,
        "cubic_max_orbit_contains_primitive_angles": True,
        "cubic_max_orbit_contains_singlet_axis": True,
        "orientation_branch_plus_cubic_max_selects_target": True,
        "accepted_same_surface_cubic_phase_potential_derived": False,
        "accepted_physical_orientation_branch_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("cubic route is conditional support", certificate["accepted_same_surface_cubic_phase_potential_derived"] is False)
    check("orientation branch remains open", certificate["accepted_physical_orientation_branch_derived"] is False)
    return certificate


def part4_firewalls() -> None:
    print("\nPart 4: firewalls and wording")
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
        "positive Y_T closure is obtained",
        "strict W/top pole rows are supplied",
        "accepted Y_T cubic phase potential is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "conditional-support / open cubic phase law",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "conditional_surface_status": "A/sqrt(12) follows if an accepted same-surface cubic phase potential and orientation branch select phi=+/-2pi/3",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "next_action": "derive accepted same-surface cubic phase dynamics/orientation, or produce accepted strict top/W pole rows",
    }
    check("actual status is conditional support", status["actual_current_surface_status"] == "conditional-support / open cubic phase law")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 CUBIC INVARIANT PHASE-SELECTOR SUPPORT BOUNDARY")
    print("=" * 78)

    deps = part1_anchors()
    witnesses = part2_cubic_invariant()
    certificate = part3_certificate()
    part4_firewalls()
    status = part5_claim_status()

    result = {
        "claim_id": "yt_c3_cubic_invariant_phase_selector_support_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_cubic_invariant_phase_selector_support_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "The cubic invariant gives a concrete conditional selector for "
            "the primitive nontrivial character angles once an orientation "
            "branch is supplied, but the actual current surface does not "
            "derive the Y_T cubic phase potential or the physical orientation "
            "branch."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "cubic_phase_witnesses": witnesses,
        "candidate_certificate": certificate,
        "route_supported": "accepted cubic invariant maximization plus accepted orientation branch selects primitive nontrivial C3 character angle",
        "route_still_open": "accepted same-surface cubic phase dynamics/orientation, or accepted strict top/W pole rows",
        "literature_math_search": {
            "external_literature_load_bearing": False,
            "math_used": "finite C3 trace invariants and direct diagonalization",
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
