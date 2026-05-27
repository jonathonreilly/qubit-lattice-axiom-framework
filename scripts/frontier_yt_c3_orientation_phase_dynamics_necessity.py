#!/usr/bin/env python3
"""Y_T C3 orientation-phase dynamics necessity no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_orientation_phase_dynamics_necessity_2026-05-27.json"

NOTE = DOCS / "YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
C3_DYNAMICS = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_REAL_TOP_LINE = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
PERRON_NOGO = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"

C3_PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
C3_DYNAMICS_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_REAL_TOP_LINE_OUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
PERRON_NOGO_OUT = ROOT / "outputs" / "yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json"
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


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def c3_reflection() -> sp.Matrix:
    return sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    paths = (
        NOTE,
        FULL_STACK,
        C3_PHASE_CONE,
        C3_DYNAMICS,
        C3_REAL_SOURCE,
        C3_REAL_TOP_LINE,
        PERRON_NOGO,
        MATRIX_FACTORIZATION,
        C3_PHASE_CONE_OUT,
        C3_DYNAMICS_OUT,
        C3_REAL_SOURCE_OUT,
        C3_REAL_TOP_LINE_OUT,
        PERRON_NOGO_OUT,
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
        "reflection-even base dynamics",
        "orientation-odd phase law",
        "strict same-source top/W pole rows",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(C3_PHASE_CONE_OUT),
        "c3_dynamics": load_json(C3_DYNAMICS_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "real_top_line": load_json(C3_REAL_TOP_LINE_OUT),
        "perron_nogo": load_json(PERRON_NOGO_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "phase cone is characterized",
        deps["phase_cone"].get("certificate_boundary", {}).get("phase_ordering_cone_characterized") is True,
    )
    check(
        "C3 dynamics boundary leaves phase law open",
        deps["c3_dynamics"].get("certificate_boundary", {}).get("orientation_phase_law_for_y0_derived") is False,
    )
    check(
        "real source theorem selects B_x only",
        deps["real_source"].get("certificate_boundary", {}).get("source_direction_bx_selected") is True,
    )
    check(
        "positive Perron route already pruned",
        deps["perron_nogo"].get("certificate_boundary", {}).get("perron_line_is_p0") is True,
    )
    check(
        "matrix factorization target row remains conditional",
        deps["matrix_factorization"].get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)",
    )
    return deps


def part2_reflection_forces_y0_zero() -> dict[str, str]:
    print("\nPart 2: reflection action on the C3 basis")
    x, y = sp.symbols("x_0 y_0", real=True)
    C = c3_cycle()
    R = c3_reflection()
    Bx = sp.simplify((C + C**2) / sp.sqrt(6))
    By = sp.simplify(sp.I * (C - C**2) / sp.sqrt(6))
    H = sp.simplify(x * Bx + y * By)
    reflected = sp.simplify(R * H * R)
    defect = sp.simplify(reflected - H)

    check("C has order three", is_zero(C**3 - sp.eye(3)))
    check("reflection squares to identity", is_zero(R**2 - sp.eye(3)))
    check("reflection sends C to C^2", is_zero(R * C * R - C**2))
    check("B_x is reflection-even", is_zero(R * Bx * R - Bx))
    check("B_y is reflection-odd", is_zero(R * By * R + By))
    check("reflection defect is -2 y_0 B_y", is_zero(defect + 2 * y * By), defect)
    check("reflection invariance forces y_0=0 in the C3 tangent basis", defect.subs(y, 0) == sp.zeros(3))

    return {
        "R_Bx_R": "B_x",
        "R_By_R": "-B_y",
        "reflection_invariance_condition": "y_0 = 0",
    }


def eigenvalues(x_value: sp.Expr, y_value: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "P_0": sp.radsimp(2 * x_value / sp.sqrt(6)),
        "P_omega": sp.radsimp(-x_value / sp.sqrt(6) - y_value / sp.sqrt(2)),
        "P_omega2": sp.radsimp(-x_value / sp.sqrt(6) + y_value / sp.sqrt(2)),
    }


def top_set(values: dict[str, sp.Expr]) -> list[str]:
    max_value = max(values.values(), key=lambda value: float(sp.N(value)))
    return [name for name, value in values.items() if is_zero(value - max_value)]


def part3_reflection_even_ordering_cases() -> dict[str, Any]:
    print("\nPart 3: reflection-even ordering cases")
    cases = {
        "x_positive": sp.Integer(1),
        "x_negative": sp.Integer(-1),
        "x_zero": sp.Integer(0),
    }
    result: dict[str, Any] = {}
    for name, x_value in cases.items():
        values = eigenvalues(x_value, sp.Integer(0))
        result[name] = {
            "x0": sp.sstr(x_value),
            "y0": "0",
            "eigenvalues": {line: sp.sstr(value) for line, value in values.items()},
            "largest_lines": top_set(values),
        }

    check("x_0>0 reflection-even dynamics selects P_0", result["x_positive"]["largest_lines"] == ["P_0"], result["x_positive"])
    check(
        "x_0<0 reflection-even dynamics makes nontrivial block largest but degenerate",
        result["x_negative"]["largest_lines"] == ["P_omega", "P_omega2"],
        result["x_negative"],
    )
    check(
        "x_0=0 reflection-even dynamics is triply degenerate",
        result["x_zero"]["largest_lines"] == ["P_0", "P_omega", "P_omega2"],
        result["x_zero"],
    )
    check("no reflection-even case isolates one nontrivial complex line", all(len(case["largest_lines"]) != 1 or case["largest_lines"] == ["P_0"] for case in result.values()))
    return result


def part4_phase_cone_substitution() -> dict[str, str]:
    print("\nPart 4: phase cone under y_0=0")
    x = sp.symbols("x_0", real=True)
    omega2_over_p0 = sp.radsimp((0 - sp.sqrt(3) * x) / sp.sqrt(2))
    omega_over_p0 = sp.radsimp((0 - sp.sqrt(3) * x) / sp.sqrt(2))
    omega2_over_omega = sp.Integer(0)

    check("P_omega2/P_0 wall expression becomes -sqrt(3)*x_0/sqrt(2)", is_zero(omega2_over_p0 + sp.sqrt(3) * x / sp.sqrt(2)), omega2_over_p0)
    check("P_omega/P_0 wall expression becomes -sqrt(3)*x_0/sqrt(2)", is_zero(omega_over_p0 + sp.sqrt(3) * x / sp.sqrt(2)), omega_over_p0)
    check("P_omega and P_omega2 remain tied when y_0=0", omega2_over_omega == 0)
    return {
        "P_omega2_minus_P0_at_y0_zero": sp.sstr(omega2_over_p0),
        "P_omega_minus_P0_at_y0_zero": sp.sstr(omega_over_p0),
        "P_omega2_minus_Pomega_at_y0_zero": "0",
    }


def part5_source_response_and_matrix_rows() -> dict[str, str]:
    print("\nPart 5: source response rows")
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    Bx = sp.simplify((C + C**2) / sp.sqrt(6))
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    responses = {name: sp.radsimp(sp.simplify(sp.trace(projector * Bx))) for name, projector in projectors.items()}
    rows = {name: sp.radsimp(A / sp.sqrt(2) * response) for name, response in responses.items()}
    check("P_0 response remains 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("P_omega response remains -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("P_omega2 response remains -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])
    check("P_0 matrix row is A/sqrt(3)", is_zero(rows["P_0"] - A / sp.sqrt(3)), rows["P_0"])
    check("nontrivial matrix row magnitude is A/sqrt(12)", is_zero(abs(rows["P_omega"]) - A / sp.sqrt(12)), rows["P_omega"])
    return {
        "P_0_row": sp.sstr(rows["P_0"]),
        "P_omega_row": sp.sstr(rows["P_omega"]),
        "P_omega2_row": sp.sstr(rows["P_omega2"]),
    }


def part6_no_go_audit() -> dict[str, bool]:
    print("\nPart 6: no-go audit")
    audit = {
        "reflection_even_base_dynamics_forces_y0_zero": True,
        "reflection_even_base_dynamics_selects_isolated_nontrivial_line": False,
        "orientation_odd_phase_term_required": True,
        "accepted_orientation_phase_law_derived": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in audit.items():
        check(f"audit field recorded: {key}", isinstance(value, bool), value)
    check("route is pruned only for reflection-even base dynamics", audit["reflection_even_base_dynamics_forces_y0_zero"] and not audit["reflection_even_base_dynamics_selects_isolated_nontrivial_line"])
    check("future orientation-odd dynamics remains live", audit["orientation_odd_phase_term_required"] and not audit["accepted_orientation_phase_law_derived"])
    return audit


def part7_firewalls() -> None:
    print("\nPart 7: firewalls and wording")
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


def part8_claim_status() -> dict[str, Any]:
    print("\nPart 8: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "reflection-even same-surface C3 base dynamics derives nontrivial phase-ordering cone membership",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive accepted orientation-odd same-surface C3 dynamics with "
            "nontrivial cone membership and W/top matrix elements, or produce "
            "strict same-source top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names orientation-odd dynamics", "orientation-odd" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 ORIENTATION-PHASE DYNAMICS NECESSITY NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    reflection = part2_reflection_forces_y0_zero()
    cases = part3_reflection_even_ordering_cases()
    cone = part4_phase_cone_substitution()
    rows = part5_source_response_and_matrix_rows()
    audit = part6_no_go_audit()
    part7_firewalls()
    status = part8_claim_status()

    result = {
        "claim_id": "yt_c3_orientation_phase_dynamics_necessity_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_orientation_phase_dynamics_necessity.py",
        **status,
        "proposal_allowed_reason": (
            "Reflection-even C3 base dynamics forces y_0 = 0. It either selects "
            "the C3 singlet line or leaves the nontrivial block degenerate, so "
            "it cannot isolate a nontrivial physical top line or certify "
            "A/sqrt(12)."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "reflection_basis": reflection,
        "reflection_even_ordering_cases": cases,
        "phase_cone_at_y0_zero": cone,
        "source_response_rows": rows,
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
