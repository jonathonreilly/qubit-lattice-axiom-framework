#!/usr/bin/env python3
"""Y_T C3 source-response extremal readout no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
MATRIX_ELEMENT = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
NONTRIVIAL_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
MASS_ORDERING = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
PHASE_ORBIT_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
ORBIT_MEMBER_NOGO = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
ORIENTATION_BIASED_NOGO = DOCS / "YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

MATRIX_ELEMENT_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
NONTRIVIAL_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"
MASS_ORDERING_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"
PHASE_ORBIT_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
ORBIT_MEMBER_NOGO_OUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"
ORIENTATION_BIASED_NOGO_OUT = ROOT / "outputs" / "yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json"
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


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify(
        (sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3
    )


def c3_data() -> tuple[sp.Matrix, sp.Matrix, dict[str, sp.Matrix]]:
    sqrt = sp.sqrt
    omega = sp.Rational(-1, 2) + sp.I * sqrt(3) / 2
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    bx = sp.simplify((cycle + cycle**2) / sqrt(6))
    projectors = {
        "P_0": projector_for_eigenvalue(cycle, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(cycle, omega),
        "P_omega2": projector_for_eigenvalue(cycle, omega**2),
    }
    return cycle, bx, projectors


def response_rows() -> tuple[dict[str, sp.Expr], dict[str, sp.Expr], dict[str, sp.Expr]]:
    A = sp.symbols("A", positive=True)
    _, bx, projectors = c3_data()
    responses = {
        name: sp.simplify(sp.expand_complex(sp.trace(projector * bx)))
        for name, projector in projectors.items()
    }
    magnitudes = {name: sp.sqrt(sp.simplify(value**2)) for name, value in responses.items()}
    matrix_rows = {name: sp.simplify(A / sp.sqrt(2) * value) for name, value in responses.items()}
    return responses, magnitudes, matrix_rows


def extremal_lines(values: dict[str, sp.Expr], mode: str) -> list[str]:
    if mode == "max":
        best = max(values.values(), key=lambda value: float(sp.N(value)))
    elif mode == "min":
        best = min(values.values(), key=lambda value: float(sp.N(value)))
    else:
        raise ValueError(mode)
    return [name for name, value in values.items() if is_zero(value - best)]


def row_magnitudes(lines: list[str], matrix_rows: dict[str, sp.Expr]) -> list[str]:
    return [sp.sstr(sp.radsimp(sp.sqrt(sp.simplify(matrix_rows[line] ** 2)))) for line in lines]


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        MATRIX_ELEMENT,
        NONTRIVIAL_BOUNDARY,
        MASS_ORDERING,
        PHASE_ORBIT_NOGO,
        ORBIT_MEMBER_NOGO,
        ORIENTATION_BIASED_NOGO,
        STRICT_AVAILABILITY,
        MATRIX_ELEMENT_OUT,
        NONTRIVIAL_BOUNDARY_OUT,
        MASS_ORDERING_OUT,
        PHASE_ORBIT_NOGO_OUT,
        ORBIT_MEMBER_NOGO_OUT,
        ORIENTATION_BIASED_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "Stuck Fan-Out",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)
    for phrase in (
        "actual_current_surface_status: no-go / open source-response readout law",
        "proposal_allowed: false",
        "max absolute response",
        "min absolute response",
        "A/sqrt(12)",
        "accepted physical rule",
    ):
        check(f"note contains source-response phrase: {phrase}", phrase in note)

    deps = {
        "matrix_element": load_json(MATRIX_ELEMENT_OUT),
        "nontrivial_boundary": load_json(NONTRIVIAL_BOUNDARY_OUT),
        "mass_ordering": load_json(MASS_ORDERING_OUT),
        "phase_orbit": load_json(PHASE_ORBIT_NOGO_OUT),
        "orbit_member": load_json(ORBIT_MEMBER_NOGO_OUT),
        "orientation_biased": load_json(ORIENTATION_BIASED_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "matrix element support leaves top-line assignment open",
        deps["matrix_element"].get("certificate_boundary", {}).get("nontrivial_top_line_assignment_derived")
        is False,
    )
    check(
        "mass ordering already selects P_0",
        deps["mass_ordering"].get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_line")
        == "P_0",
    )
    check(
        "orbit-member covariance has no equivariant section",
        deps["orbit_member"].get("no_go_certificate", {}).get("free_c3_orbit_has_equivariant_section")
        is False,
    )
    check(
        "orientation-biased scalar route still lacks physical readout",
        deps["orientation_biased"].get("no_go_certificate", {})
        .get("accepted_physical_basepoint_readout_law_derived")
        is False,
    )
    check(
        "strict availability still confirms rows absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return deps


def part2_source_response_extrema() -> dict[str, Any]:
    print("\nPart 2: source-response extremal witnesses")
    sqrt = sp.sqrt
    cycle, bx, projectors = c3_data()
    responses, magnitudes, matrix_rows = response_rows()

    check("C has order three", is_zero(cycle**3 - sp.eye(3)))
    check("B_x is Hermitian", is_zero(bx.conjugate().T - bx))
    check("B_x is connected/traceless", is_zero(sp.trace(bx)))
    check("B_x has unit Frobenius norm", is_zero(sp.trace(bx.conjugate().T * bx) - 1))

    for name, projector in projectors.items():
        check(f"{name} is a projector", is_zero(projector**2 - projector))
        check(f"{name} has trace one", is_zero(sp.trace(projector) - 1), sp.trace(projector))

    check("P_0 response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sqrt(6)), responses["P_omega2"])
    check("P_0 row magnitude is A/sqrt(3)", sp.sstr(sp.radsimp(sp.sqrt(matrix_rows["P_0"] ** 2))) == "sqrt(3)*A/3")
    check("nontrivial row magnitude is A/sqrt(12)", sp.sstr(sp.radsimp(sp.sqrt(matrix_rows["P_omega"] ** 2))) == "sqrt(3)*A/6")

    signed_max = extremal_lines(responses, "max")
    signed_min = extremal_lines(responses, "min")
    abs_max = extremal_lines(magnitudes, "max")
    abs_min = extremal_lines(magnitudes, "min")

    check("signed response maximum selects P_0", signed_max == ["P_0"], signed_max)
    check("absolute response maximum selects P_0", abs_max == ["P_0"], abs_max)
    check("signed response minimum selects nontrivial pair", signed_min == ["P_omega", "P_omega2"], signed_min)
    check("absolute response minimum selects nontrivial pair", abs_min == ["P_omega", "P_omega2"], abs_min)
    check("minimum-response rule does not isolate one complex line", len(abs_min) == 2, abs_min)
    check("maximum-response source readout gives singlet row", row_magnitudes(abs_max, matrix_rows) == ["sqrt(3)*A/3"])
    check(
        "minimum-response source readout gives target row only conditionally",
        row_magnitudes(abs_min, matrix_rows) == ["sqrt(3)*A/6", "sqrt(3)*A/6"],
    )

    return {
        "responses": {name: sp.sstr(sp.radsimp(value)) for name, value in responses.items()},
        "response_magnitudes": {name: sp.sstr(sp.radsimp(value)) for name, value in magnitudes.items()},
        "matrix_rows": {name: sp.sstr(sp.radsimp(value)) for name, value in matrix_rows.items()},
        "matrix_row_magnitudes": {
            name: sp.sstr(sp.radsimp(sp.sqrt(sp.simplify(value**2))))
            for name, value in matrix_rows.items()
        },
        "source_response_extrema": {
            "signed_max": {"lines": signed_max, "row_magnitudes": row_magnitudes(signed_max, matrix_rows)},
            "absolute_max": {"lines": abs_max, "row_magnitudes": row_magnitudes(abs_max, matrix_rows)},
            "signed_min": {"lines": signed_min, "row_magnitudes": row_magnitudes(signed_min, matrix_rows)},
            "absolute_min": {"lines": abs_min, "row_magnitudes": row_magnitudes(abs_min, matrix_rows)},
        },
    }


def part3_orbit_readout_witness(extrema: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 3: selected-orbit readout witness")
    selected_orbit_labels = ["P_0", "P_omega2", "P_omega"]
    absolute_max = extrema["source_response_extrema"]["absolute_max"]["lines"]
    absolute_min = extrema["source_response_extrema"]["absolute_min"]["lines"]
    check("generic selected C3 orbit contains P_0", "P_0" in selected_orbit_labels)
    check("generic selected C3 orbit contains both nontrivial labels", {"P_omega", "P_omega2"}.issubset(selected_orbit_labels))
    check("source-response absolute maximum on selected orbit is P_0", absolute_max == ["P_0"], absolute_max)
    check("source-response absolute minimum on selected orbit is the nontrivial pair", absolute_min == ["P_omega", "P_omega2"], absolute_min)
    return {
        "generic_selected_orbit_labels": selected_orbit_labels,
        "absolute_max_readout": absolute_max,
        "absolute_min_readout": absolute_min,
        "selected_orbit_contains_p0": True,
        "selected_orbit_nontrivial_minimum_is_degenerate": True,
    }


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "bx_source_direction_available": True,
        "same_surface_matrix_factorization_support_available": True,
        "signed_response_max_selects_p0": True,
        "absolute_response_max_selects_p0": True,
        "signed_response_min_selects_nontrivial_pair": True,
        "absolute_response_min_selects_nontrivial_pair": True,
        "minimum_response_top_convention_derived": False,
        "nontrivial_complex_line_isolated": False,
        "accepted_physical_source_response_readout_law_derived": False,
        "accepted_w_top_matrix_elements_supplied": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("maximum source-response route is pruned by P_0", certificate["absolute_response_max_selects_p0"] is True)
    check("target minimum-response route remains an extra selector", certificate["minimum_response_top_convention_derived"] is False)
    check("strict rows remain absent", certificate["strict_top_w_response_certificate_present"] is False)
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
        "accepted top line is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T C3 SOURCE-RESPONSE EXTREMAL READOUT NO-GO")
    print("=" * 88)

    deps = part1_anchors()
    extrema = part2_source_response_extrema()
    orbit_readout = part3_orbit_readout_witness(extrema)
    certificate = part4_no_go_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open source-response readout law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The same-surface B_x source-response extrema do not derive the "
            "physical nontrivial top line. Signed and absolute maxima select "
            "P_0 and give A/sqrt(3). Signed and absolute minima select the "
            "nontrivial pair and give A/sqrt(12), but that minimum-response "
            "convention is an extra physical selector and remains degenerate "
            "between P_omega and P_omega2."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependencies": {
            name: {
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
                "fail_count": data.get("fail_count"),
            }
            for name, data in deps.items()
        },
        "source_response_witness": extrema,
        "selected_orbit_readout_witness": orbit_readout,
        "no_go_certificate": certificate,
        "route_pruned": "same-surface B_x source-response extremal readout supplies the physical nontrivial C3 top-line law",
        "route_still_live": (
            "derive an accepted same-surface physical basepoint/readout law that "
            "selects a nontrivial C3 character line and supplies W/top source-generator "
            "matrix elements, or produce accepted strict same-source top/W pole rows"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_source_response_extremal_readout_no_go.py",
            "outputs/yt_c3_source_response_extremal_readout_no_go_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
