#!/usr/bin/env python3
"""Y_T C3 phase-ordering cone support boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"

NOTE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_DYNAMICS = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
PERRON_NOGO = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"

C3_DYNAMICS_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
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


def contains_phrase(text: str, phrase: str) -> bool:
    normalized_text = " ".join(text.lower().split())
    normalized_phrase = " ".join(phrase.lower().split())
    return normalized_phrase in normalized_text


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        FULL_STACK,
        C3_DYNAMICS,
        PERRON_NOGO,
        MATRIX_FACTORIZATION,
        C3_DYNAMICS_OUT,
        PERRON_NOGO_OUT,
        MATRIX_FACTORIZATION_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Relation To Current Stack",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: exact-support / open phase-ordering import",
        "proposal_allowed: false",
        "phase-ordering cone",
        "y_0 > sqrt(3) x_0",
        "strict same-source top/W pole rows",
    ):
        check(f"note contains boundary phrase: {phrase}", contains_phrase(note, phrase))

    deps = {
        "c3_dynamics": load_json(C3_DYNAMICS_OUT),
        "perron_nogo": load_json(PERRON_NOGO_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "C3 dynamics leaves phase law open",
        deps["c3_dynamics"].get("certificate_boundary", {}).get("orientation_phase_law_for_y0_derived") is False,
    )
    check(
        "positive Perron shortcut is pruned",
        deps["perron_nogo"].get("certificate_boundary", {}).get("perron_line_is_p0") is True,
    )
    check(
        "matrix factorization target row is known",
        deps["matrix_factorization"].get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)",
    )
    return deps


def eigenvalue_formulas() -> dict[str, sp.Expr]:
    x, y = sp.symbols("x_0 y_0", real=True)
    return {
        "P_0": sp.radsimp(2 * x / sp.sqrt(6)),
        "P_omega": sp.radsimp(-x / sp.sqrt(6) - y / sp.sqrt(2)),
        "P_omega2": sp.radsimp(-x / sp.sqrt(6) + y / sp.sqrt(2)),
    }


def part2_eigenvalue_cone_algebra() -> dict[str, str]:
    print("\nPart 2: eigenvalue cone algebra")
    x, y = sp.symbols("x_0 y_0", real=True)
    lambdas = eigenvalue_formulas()
    omega2_minus_zero = sp.radsimp(lambdas["P_omega2"] - lambdas["P_0"])
    omega_minus_zero = sp.radsimp(lambdas["P_omega"] - lambdas["P_0"])
    omega2_minus_omega = sp.radsimp(lambdas["P_omega2"] - lambdas["P_omega"])

    check(
        "P_omega2 beats P_0 iff y_0 > sqrt(3) x_0",
        is_zero(omega2_minus_zero - (y - sp.sqrt(3) * x) / sp.sqrt(2)),
        omega2_minus_zero,
    )
    check(
        "P_omega beats P_0 iff -y_0 > sqrt(3) x_0",
        is_zero(omega_minus_zero - (-y - sp.sqrt(3) * x) / sp.sqrt(2)),
        omega_minus_zero,
    )
    check(
        "P_omega2 beats P_omega iff y_0 > 0",
        is_zero(omega2_minus_omega - sp.sqrt(2) * y),
        omega2_minus_omega,
    )
    check("P_0 formula recorded", is_zero(lambdas["P_0"] - 2 * x / sp.sqrt(6)), lambdas["P_0"])
    check("P_omega formula recorded", is_zero(lambdas["P_omega"] + x / sp.sqrt(6) + y / sp.sqrt(2)), lambdas["P_omega"])
    check("P_omega2 formula recorded", is_zero(lambdas["P_omega2"] + x / sp.sqrt(6) - y / sp.sqrt(2)), lambdas["P_omega2"])

    return {
        "lambda_P0": sp.sstr(lambdas["P_0"]),
        "lambda_Pomega": sp.sstr(lambdas["P_omega"]),
        "lambda_Pomega2": sp.sstr(lambdas["P_omega2"]),
        "Pomega2_minus_P0": sp.sstr(omega2_minus_zero),
        "Pomega_minus_P0": sp.sstr(omega_minus_zero),
        "Pomega2_minus_Pomega": sp.sstr(omega2_minus_omega),
    }


def top_line_numeric(x_value: sp.Expr, y_value: sp.Expr) -> tuple[str, dict[str, sp.Expr]]:
    x, y = sp.symbols("x_0 y_0", real=True)
    lambdas = eigenvalue_formulas()
    values = {key: sp.radsimp(value.subs({x: x_value, y: y_value})) for key, value in lambdas.items()}
    top = max(values, key=lambda key: float(sp.N(values[key])))
    return top, values


def part3_region_witnesses() -> dict[str, Any]:
    print("\nPart 3: region witnesses")
    sqrt = sp.sqrt
    witnesses = {
        "singlet_region": (sp.Integer(1), sp.Integer(0)),
        "omega2_region": (sp.Integer(0), sp.Integer(1)),
        "omega_region": (sp.Integer(0), sp.Integer(-1)),
        "nontrivial_degenerate_wall": (sp.Integer(-1), sp.Integer(0)),
        "p0_omega2_wall": (sp.Integer(1), sqrt(3)),
        "p0_omega_wall": (sp.Integer(1), -sqrt(3)),
    }
    result: dict[str, Any] = {}
    for name, (x_value, y_value) in witnesses.items():
        top, values = top_line_numeric(x_value, y_value)
        result[name] = {
            "x0": sp.sstr(x_value),
            "y0": sp.sstr(y_value),
            "eigenvalues": {key: sp.sstr(value) for key, value in values.items()},
            "top_by_largest": top,
        }

    check("singlet witness selects P_0", result["singlet_region"]["top_by_largest"] == "P_0", result["singlet_region"])
    check("positive y cone selects P_omega2", result["omega2_region"]["top_by_largest"] == "P_omega2", result["omega2_region"])
    check("negative y cone selects P_omega", result["omega_region"]["top_by_largest"] == "P_omega", result["omega_region"])
    degenerate = top_line_numeric(sp.Integer(-1), sp.Integer(0))[1]
    check("y_0=0 with x_0<0 makes nontrivial top block degenerate", is_zero(degenerate["P_omega"] - degenerate["P_omega2"]))
    wall_plus = top_line_numeric(sp.Integer(1), sqrt(3))[1]
    wall_minus = top_line_numeric(sp.Integer(1), -sqrt(3))[1]
    check("positive boundary has P_0/P_omega2 degeneracy", is_zero(wall_plus["P_0"] - wall_plus["P_omega2"]))
    check("negative boundary has P_0/P_omega degeneracy", is_zero(wall_minus["P_0"] - wall_minus["P_omega"]))
    return result


def part4_source_response_target() -> dict[str, str]:
    print("\nPart 4: source response target")
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
    radial_rows = {name: sp.radsimp(A / sp.sqrt(2) * value) for name, value in responses.items()}
    check("P_0 source response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])
    check("nontrivial radial row magnitude is A/sqrt(12)", is_zero(abs(radial_rows["P_omega"]) - A / sp.sqrt(12)), radial_rows["P_omega"])
    check("singlet radial row is A/sqrt(3)", is_zero(radial_rows["P_0"] - A / sp.sqrt(3)), radial_rows["P_0"])
    return {
        "P_0_row": sp.sstr(radial_rows["P_0"]),
        "P_omega_row": sp.sstr(radial_rows["P_omega"]),
        "P_omega2_row": sp.sstr(radial_rows["P_omega2"]),
    }


def part5_certificate_boundary() -> dict[str, bool]:
    print("\nPart 5: certificate boundary")
    certificate = {
        "phase_ordering_cone_characterized": True,
        "nontrivial_cone_implies_target_row": True,
        "accepted_same_surface_base_operator_derived": False,
        "phase_ordering_law_derived": False,
        "physical_top_line_in_nontrivial_cone_derived": False,
        "strict_pole_rows_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("support remains conditional on phase-ordering law", certificate["phase_ordering_law_derived"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    return certificate


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    text = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in text)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "strict W/top pole rows are supplied",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part7_claim_status() -> dict[str, Any]:
    print("\nPart 7: claim status")
    status = {
        "actual_current_surface_status": "exact-support / open phase-ordering import",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "next_action": (
            "derive the phase-ordering cone from accepted microscopic dynamics, "
            "or produce strict same-source top/W pole rows"
        ),
    }
    check("actual status is exact support/open", status["actual_current_surface_status"] == "exact-support / open phase-ordering import")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 PHASE-ORDERING CONE SUPPORT BOUNDARY")
    print("=" * 78)

    deps = part1_anchors()
    cone = part2_eigenvalue_cone_algebra()
    witnesses = part3_region_witnesses()
    rows = part4_source_response_target()
    certificate = part5_certificate_boundary()
    part6_firewalls()
    status = part7_claim_status()

    result = {
        "claim_id": "yt_c3_phase_ordering_cone_support_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_phase_ordering_cone_support_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "The exact nontrivial C3 phase-ordering cone is characterized, but "
            "the current surface does not derive that the accepted physical top "
            "base operator lies in that cone."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "phase_ordering_cone": cone,
        "region_witnesses": witnesses,
        "source_response_rows": rows,
        "certificate_boundary": certificate,
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
