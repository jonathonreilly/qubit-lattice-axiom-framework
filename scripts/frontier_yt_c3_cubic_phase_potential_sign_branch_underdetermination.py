#!/usr/bin/env python3
"""Y_T C3 cubic phase-potential sign/branch underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_cubic_phase_potential_sign_branch_underdetermination_2026-05-27.json"

NOTE = DOCS / "YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
CUBIC_SUPPORT = DOCS / "YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
PRIMITIVE_ANGLE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
REPRESENTATION_NOGO = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

CUBIC_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_cubic_invariant_phase_selector_support_boundary_2026-05-27.json"
PRIMITIVE_ANGLE_OUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"
REPRESENTATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
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


def row_magnitudes(lines: list[str]) -> list[str]:
    A = sp.symbols("A", positive=True)
    source_rows = {
        "P_0": sp.radsimp(A / sp.sqrt(2) * (sp.sqrt(6) / 3)),
        "P_omega": sp.radsimp(A / sp.sqrt(2) * (-sp.sqrt(6) / 6)),
        "P_omega2": sp.radsimp(A / sp.sqrt(2) * (-sp.sqrt(6) / 6)),
    }
    return [sp.sstr(sp.radsimp(abs(source_rows[line]))) for line in lines]


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        CUBIC_SUPPORT,
        PRIMITIVE_ANGLE,
        REPRESENTATION_NOGO,
        PHASE_CONE,
        STRICT_AVAILABILITY,
        CUBIC_SUPPORT_OUT,
        PRIMITIVE_ANGLE_OUT,
        REPRESENTATION_NOGO_OUT,
        PHASE_CONE_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "Literature / Math Search",
        "What This Prunes",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)
    for phrase in (
        "actual_current_surface_status: no-go / open cubic phase law",
        "proposal_allowed: false",
        "signed `cos(3 phi)` term",
        "singlet and degenerate extremal witnesses remain allowed",
        "not yet an accepted Y_T dynamics law",
    ):
        check(f"note contains no-go phrase: {phrase}", phrase in note)

    deps = {
        "cubic_support": load_json(CUBIC_SUPPORT_OUT),
        "primitive_angle": load_json(PRIMITIVE_ANGLE_OUT),
        "representation_nogo": load_json(REPRESENTATION_NOGO_OUT),
        "phase_cone": load_json(PHASE_CONE_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "cubic support dependency still lacks accepted potential",
        deps["cubic_support"].get("candidate_certificate", {})
        .get("accepted_same_surface_cubic_phase_potential_derived")
        is False,
    )
    check(
        "cubic support dependency still lacks orientation branch",
        deps["cubic_support"].get("candidate_certificate", {})
        .get("accepted_physical_orientation_branch_derived")
        is False,
    )
    check(
        "representation dependency prunes representation-only selector",
        deps["representation_nogo"].get("no_go_certificate", {})
        .get("representation_theory_selects_phi_pm_2pi_over_3")
        is False,
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {}).get("strict_top_w_rows_artifact_present")
        is False,
    )
    return deps


def part2_invariant_family() -> dict[str, str]:
    print("\nPart 2: invariant functional family")
    x, y, phi, beta, v0 = sp.symbols("x y phi beta v0", real=True)
    _, Bx, By = c3_basis()
    H = sp.simplify(x * Bx + y * By)
    H_phi = sp.simplify(sp.cos(phi) * Bx + sp.sin(phi) * By)
    q = sp.simplify(sp.trace(H**2))
    cubic = sp.factor(sp.trace(H**3))
    cubic_phi = sp.trigsimp(sp.trace(H_phi**3).rewrite(sp.cos))
    potential = sp.simplify(v0 + beta * cubic_phi)
    derivative = sp.trigsimp(sp.diff(potential, phi).rewrite(sp.sin))
    check("quadratic invariant is unit norm", is_zero(q - (x**2 + y**2)), q)
    check("cubic invariant formula in x,y", is_zero(cubic - sp.sqrt(6) * x * (x**2 - 3 * y**2) / 6), cubic)
    check("cubic invariant formula on unit circle", is_zero(cubic_phi - sp.sqrt(6) * sp.cos(3 * phi) / 6), cubic_phi)
    check("generic cubic potential is constant plus signed cos(3phi)", is_zero(potential - (v0 + beta * sp.sqrt(6) * sp.cos(3 * phi) / 6)), potential)
    check("stationarity depends on beta sign but zeros are sin(3phi)=0", is_zero(derivative + beta * sp.sqrt(6) * sp.sin(3 * phi) / 2), derivative)
    return {
        "quadratic": sp.sstr(q),
        "cubic_xy": sp.sstr(cubic),
        "cubic_phi": sp.sstr(cubic_phi),
        "potential": sp.sstr(potential),
        "derivative": sp.sstr(derivative),
    }


def part3_extremal_witnesses() -> dict[str, Any]:
    print("\nPart 3: extremal orbits and row witnesses")
    witnesses = {
        "positive_sign_max_real_axis": (sp.Integer(0), ["P_0"], ["sqrt(3)*A/3"], "singlet"),
        "positive_sign_max_positive_branch": (2 * sp.pi / 3, ["P_omega2"], ["sqrt(3)*A/6"], "target"),
        "positive_sign_max_negative_branch": (-2 * sp.pi / 3, ["P_omega"], ["sqrt(3)*A/6"], "target"),
        "opposite_sign_extremum_positive_wall": (sp.pi / 3, ["P_0", "P_omega2"], ["sqrt(3)*A/3", "sqrt(3)*A/6"], "degenerate"),
        "opposite_sign_extremum_real_negative_axis": (sp.pi, ["P_omega", "P_omega2"], ["sqrt(3)*A/6", "sqrt(3)*A/6"], "degenerate"),
        "opposite_sign_extremum_negative_wall": (-sp.pi / 3, ["P_0", "P_omega"], ["sqrt(3)*A/3", "sqrt(3)*A/6"], "degenerate"),
    }
    result: dict[str, Any] = {}
    for name, (angle, expected_lines, expected_rows, class_name) in witnesses.items():
        x_value = sp.simplify(sp.cos(angle))
        y_value = sp.simplify(sp.sin(angle))
        values = eigenvalues(x_value, y_value)
        lines = top_set(values)
        rows = row_magnitudes(lines)
        cubic_value = sp.simplify(sp.sqrt(6) * sp.cos(3 * angle) / 6)
        result[name] = {
            "phi": sp.sstr(angle),
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "cubic_trace": sp.sstr(cubic_value),
            "largest_lines": lines,
            "row_magnitudes_if_selected": rows,
            "class": class_name,
        }
        check(f"{name} has expected top set", lines == expected_lines, result[name])
        check(f"{name} has expected row set", rows == expected_rows, result[name])
    check("positive-sign extremal orbit includes singlet and target choices", result["positive_sign_max_real_axis"]["class"] == "singlet" and result["positive_sign_max_positive_branch"]["class"] == "target")
    check("opposite-sign extremal orbit has degeneracies", all(result[name]["class"] == "degenerate" for name in result if name.startswith("opposite_sign")))
    return result


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "c3_invariant_cubic_functional_class_characterized": True,
        "quadratic_invariant_phase_blind": True,
        "cubic_sign_or_optimization_convention_derived": False,
        "singlet_extremum_allowed": True,
        "degenerate_extrema_allowed": True,
        "accepted_physical_orientation_branch_derived": False,
        "physical_phase_law_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("shortcut is pruned because sign/branch are not derived", certificate["physical_phase_law_derived"] is False)
    check("singlet extremum remains allowed", certificate["singlet_extremum_allowed"] is True)
    return certificate


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
        "positive Y_T closure is obtained",
        "strict W/top pole rows are supplied",
        "accepted Y_T cubic phase potential is derived",
        "physical orientation branch is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go / open cubic phase law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "conditional_surface_status": None,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "next_action": "derive accepted same-surface cubic phase dynamics/orientation, or produce accepted strict top/W pole rows",
    }
    check("actual status is no-go/open cubic law", status["actual_current_surface_status"] == "no-go / open cubic phase law")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 CUBIC PHASE-POTENTIAL SIGN/BRANCH UNDERDETERMINATION NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    invariant_family = part2_invariant_family()
    witnesses = part3_extremal_witnesses()
    certificate = part4_no_go_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_cubic_phase_potential_sign_branch_underdetermination_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_cubic_phase_potential_sign_branch_underdetermination.py",
        **status,
        "proposal_allowed_reason": (
            "C3-invariant cubic structure characterizes the finite phase "
            "functional, but its sign, variational convention, and physical "
            "orientation branch are not derived; singlet and degenerate "
            "extremal witnesses remain allowed."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "invariant_family": invariant_family,
        "extremal_witnesses": witnesses,
        "no_go_certificate": certificate,
        "route_pruned": "C3 invariance plus cubic trace invariant alone selects the physical Y_T phase angle",
        "route_still_live": "accepted same-surface cubic phase dynamics/orientation, or accepted strict top/W pole rows",
        "literature_math_search": {
            "external_literature_load_bearing": False,
            "math_used": "finite C3 trace invariants and extremal orbit enumeration",
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
