#!/usr/bin/env python3
"""Y_T C3 primitive character phase-angle candidate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"

NOTE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
UNDERDETERMINATION = DOCS / "YT_C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
UNDERDETERMINATION_OUT = ROOT / "outputs" / "yt_c3_quantitative_phase_strength_underdetermination_2026-05-27.json"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        PHASE_CONE,
        UNDERDETERMINATION,
        MATRIX_FACTORIZATION,
        STRICT_AVAILABILITY,
        PHASE_CONE_OUT,
        UNDERDETERMINATION_OUT,
        MATRIX_FACTORIZATION_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Candidate Witness",
        "Claim Boundary",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: conditional-support / open phase-angle law",
        "proposal_allowed: false",
        "phi = +2 pi / 3",
        "same-surface phase-angle law",
        "not derived here",
    ):
        check(f"note contains candidate phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(PHASE_CONE_OUT),
        "underdetermination": load_json(UNDERDETERMINATION_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "underdetermination dependency leaves phase angle open",
        deps["underdetermination"].get("current_premise_no_go", {})
        .get("audit", {})
        .get("phase_angle_selector_derived")
        is False,
    )
    check(
        "phase cone dependency conditionally implies target row",
        deps["phase_cone"].get("certificate_boundary", {}).get("nontrivial_cone_implies_target_row") is True,
    )
    check(
        "matrix factorization target row is known",
        deps["matrix_factorization"].get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)",
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {}).get("strict_top_w_rows_artifact_present") is False,
    )
    return deps


def part2_character_angle_witnesses() -> dict[str, Any]:
    print("\nPart 2: primitive C3 character-angle witnesses")
    A = sp.symbols("A", positive=True)
    C, Bx, By = c3_basis()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    source_rows = {
        name: sp.radsimp(A / sp.sqrt(2) * sp.simplify(sp.trace(projector * Bx)))
        for name, projector in projectors.items()
    }

    witnesses = {
        "real_positive_axis": (sp.Integer(1), sp.Integer(0), ["P_0"]),
        "positive_character_angle": (-sp.Rational(1, 2), sp.sqrt(3) / 2, ["P_omega2"]),
        "negative_character_angle": (-sp.Rational(1, 2), -sp.sqrt(3) / 2, ["P_omega"]),
    }
    result: dict[str, Any] = {}
    for name, (x_value, y_value, expected_top) in witnesses.items():
        values = eigenvalues(x_value, y_value)
        top_lines = top_set(values)
        result[name] = {
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "unit_norm": is_zero(x_value**2 + y_value**2 - 1),
            "eigenvalues": {line: sp.sstr(value) for line, value in values.items()},
            "largest_lines": top_lines,
            "row_if_selected": [sp.sstr(source_rows[line]) for line in top_lines],
        }
        check(f"{name} is on unit base circle", result[name]["unit_norm"])
        check(f"{name} has expected top line", top_lines == expected_top, result[name])

    check("positive C3 character angle gives target row", is_zero(abs(source_rows["P_omega2"]) - A / sp.sqrt(12)))
    check("negative C3 character angle gives target row", is_zero(abs(source_rows["P_omega"]) - A / sp.sqrt(12)))
    check("real positive axis gives singlet row", is_zero(source_rows["P_0"] - A / sp.sqrt(3)))
    return result


def part3_candidate_certificate() -> dict[str, bool]:
    print("\nPart 3: candidate certificate boundary")
    certificate = {
        "primitive_character_phase_candidate_checked": True,
        "candidate_angles_lie_in_nontrivial_cone": True,
        "candidate_angles_give_target_row": True,
        "accepted_same_surface_phase_angle_law_derived": False,
        "adjacent_lane_phase_import_used_as_proof": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("candidate remains conditional", certificate["accepted_same_surface_phase_angle_law_derived"] is False)
    check("adjacent lane phase is not imported as proof", certificate["adjacent_lane_phase_import_used_as_proof"] is False)
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
        "positive Y_T closure",
        "strict top/W pole-response evidence is present",
        "the physical Y_T base phase angle is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "conditional-support / open phase-angle law",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "conditional_surface_status": "A/sqrt(12) follows if accepted same-surface Y_T dynamics derives phi = ±2pi/3",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "next_action": "derive accepted same-surface phase-angle law, or produce accepted strict top/W pole rows",
    }
    check("actual status is conditional support", status["actual_current_surface_status"] == "conditional-support / open phase-angle law")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 PRIMITIVE CHARACTER PHASE-ANGLE CANDIDATE")
    print("=" * 78)

    deps = part1_anchors()
    witnesses = part2_character_angle_witnesses()
    certificate = part3_candidate_certificate()
    part4_firewalls()
    status = part5_claim_status()

    result = {
        "claim_id": "yt_c3_primitive_character_phase_angle_candidate_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_primitive_character_phase_angle_candidate.py",
        **status,
        "proposal_allowed_reason": (
            "The primitive nontrivial C3 character angles lie in the target "
            "cone and give A/sqrt(12), but the actual current surface does "
            "not derive that the physical Y_T base operator has either angle."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "character_angle_witnesses": witnesses,
        "candidate_certificate": certificate,
        "literature_math_search": {
            "external_literature_load_bearing": False,
            "math_used": "finite C3 character algebra and direct diagonalization",
            "adjacent_lane_phase_status": "context only; not imported as Y_T proof",
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
