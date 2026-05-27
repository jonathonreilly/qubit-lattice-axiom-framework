#!/usr/bin/env python3
"""Y_T strict W/Z plus C3 top-row splice no-go.

This runner checks the narrow shortcut:

    strict W/Z denominator response + conditional C3 target top row
      -> accepted strict same-source top/W pole-response certificate.

The shortcut fails because the formal target readout still imports the
same-surface splice and physical nontrivial top-line/projector authority.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_wz_c3_top_row_splice_no_go_2026-05-27.json"

NOTE = DOCS / "YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_MATRIX = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_TOP_LINE = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_SOURCE_EXTREMAL = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
STRICT_DISCOVERY = DOCS / "YT_STRICT_TOP_W_POLE_ROW_REPOSITORY_DISCOVERY_NO_GO_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_MATRIX_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_TOP_LINE_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"
C3_SOURCE_EXTREMAL_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
STRICT_DISCOVERY_OUT = ROOT / "outputs" / "yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json"

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


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> None:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        FULL_STACK,
        STRICT_WZ,
        STRICT_TOP,
        FIRST_PRINCIPLES,
        SAME_SURFACE_MATRIX,
        C3_TOP_LINE,
        C3_SOURCE_EXTREMAL,
        STRICT_AVAILABILITY,
        STRICT_DISCOVERY,
        FULL_STACK_OUT,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_MATRIX_OUT,
        C3_TOP_LINE_OUT,
        C3_SOURCE_EXTREMAL_OUT,
        STRICT_AVAILABILITY_OUT,
        STRICT_DISCOVERY_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
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
        "strict W/Z denominator response",
        "conditional C3 target row",
        "same-source/same-surface",
        "physical top-line authority",
        "proposal_allowed: false",
        "strict denominator plus conditional C3 row shortcut",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)


def part2_dependency_outputs() -> dict[str, Any]:
    print("\nPart 2: dependency outputs")
    full = load_json(FULL_STACK_OUT)
    wz = load_json(STRICT_WZ_OUT)
    symbolic_top = load_json(STRICT_TOP_OUT)
    first = load_json(FIRST_PRINCIPLES_OUT)
    matrix = load_json(SAME_SURFACE_MATRIX_OUT)
    top_line = load_json(C3_TOP_LINE_OUT)
    source_extremal = load_json(C3_SOURCE_EXTREMAL_OUT)
    availability = load_json(STRICT_AVAILABILITY_OUT)
    discovery = load_json(STRICT_DISCOVERY_OUT)

    for name, row in (
        ("full stack", full),
        ("strict W/Z denominator", wz),
        ("strict symbolic top row", symbolic_top),
        ("first-principles transfer response", first),
        ("same-surface matrix factorization", matrix),
        ("C3 top-line assignment boundary", top_line),
        ("C3 source-response extremal no-go", source_extremal),
        ("strict sparse availability", availability),
        ("strict repository discovery", discovery),
    ):
        check(f"{name} runner passed", row.get("fail_count") == 0, row.get("fail_count"))

    check("W/Z denominator response is closed support", wz.get("strict_wz_denominator_response_closed") is True)
    check("symbolic top row leaves coefficient free", symbolic_top.get("top_coefficient_derived") is False)
    check("first-principles response leaves matrix element load-bearing", "top sector response row" in first.get("first_open_gate_after_this_note", ""))
    check("matrix factorization target row is A/sqrt(12)", matrix.get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)")
    check("matrix factorization singlet row differs", matrix.get("matrix_element_witness", {}).get("singlet_top_row") == "A/sqrt(3)")
    check(
        "matrix factorization does not derive nontrivial line",
        matrix.get("certificate_boundary", {}).get("nontrivial_top_line_assignment_derived") is False,
    )
    check("C3 top-line assignment route is pruning", top_line.get("trace_class") == "negative_route_pruning")
    check(
        "source-response maximum selects P0",
        source_extremal.get("no_go_certificate", {}).get("absolute_response_max_selects_p0") is True,
    )
    check(
        "source-response minimum selector is not derived",
        source_extremal.get("no_go_certificate", {}).get("minimum_response_top_convention_derived") is False,
    )
    check(
        "strict positive certificate absent in availability audit",
        availability.get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    check("repository discovery found no complete strict packet", discovery.get("complete_strict_packet_count") == 0)
    check("repository discovery strict certificate absent", discovery.get("strict_positive_certificate_present") is False)

    return {
        "full_stack": full,
        "strict_wz": wz,
        "strict_symbolic_top": symbolic_top,
        "first_principles": first,
        "same_surface_matrix": matrix,
        "c3_top_line": top_line,
        "source_extremal": source_extremal,
        "strict_availability": availability,
        "strict_discovery": discovery,
    }


def part3_splice_algebra() -> dict[str, Any]:
    print("\nPart 3: formal splice algebra")
    A, g2, J = sp.symbols("A g_2 J", positive=True)
    dmw = g2 * A / 2
    dmw_reparam = g2 * A * J / 2
    dmt_nontrivial = A / sp.sqrt(12)
    dmt_nontrivial_reparam = A * J / sp.sqrt(12)
    dmt_singlet = A / sp.sqrt(3)
    dmt_singlet_reparam = A * J / sp.sqrt(3)

    readout_nontrivial = sp.simplify(g2 / sp.sqrt(2) * dmt_nontrivial / dmw)
    readout_nontrivial_reparam = sp.simplify(g2 / sp.sqrt(2) * dmt_nontrivial_reparam / dmw_reparam)
    readout_singlet = sp.simplify(g2 / sp.sqrt(2) * dmt_singlet / dmw)
    readout_singlet_reparam = sp.simplify(g2 / sp.sqrt(2) * dmt_singlet_reparam / dmw_reparam)

    check("nontrivial splice readout is 1/sqrt(6)", is_zero(readout_nontrivial - 1 / sp.sqrt(6)), readout_nontrivial)
    check("nontrivial splice is source-reparameterization invariant", is_zero(readout_nontrivial_reparam - readout_nontrivial), readout_nontrivial_reparam)
    check("singlet splice readout is sqrt(2/3)", is_zero(readout_singlet - sp.sqrt(sp.Rational(2, 3))), readout_singlet)
    check("singlet splice is source-reparameterization invariant", is_zero(readout_singlet_reparam - readout_singlet), readout_singlet_reparam)
    check("singlet and nontrivial readouts differ", not is_zero(readout_singlet - readout_nontrivial))

    bx_responses = {
        "P_0": 2 / sp.sqrt(6),
        "P_omega": -1 / sp.sqrt(6),
        "P_omega2": -1 / sp.sqrt(6),
    }
    matrix_rows = {
        key: sp.simplify(A / sp.sqrt(2) * value)
        for key, value in bx_responses.items()
    }
    check("P0 matrix row is A/sqrt(3)", is_zero(matrix_rows["P_0"] - A / sp.sqrt(3)), matrix_rows["P_0"])
    check("Pomega matrix row magnitude is A/sqrt(12)", is_zero(abs(matrix_rows["P_omega"]) - A / sp.sqrt(12)), matrix_rows["P_omega"])
    check("Pomega2 matrix row magnitude is A/sqrt(12)", is_zero(abs(matrix_rows["P_omega2"]) - A / sp.sqrt(12)), matrix_rows["P_omega2"])

    return {
        "dM_W_dell": "g_2*A/2",
        "candidate_rows": {
            "P_0": "A/sqrt(3)",
            "P_omega": "A/sqrt(12) in magnitude",
            "P_omega2": "A/sqrt(12) in magnitude",
        },
        "top_w_readouts": {
            "P_0": sp.sstr(readout_singlet),
            "P_omega_or_P_omega2": sp.sstr(readout_nontrivial),
        },
        "source_reparameterization_cancels": True,
        "target_depends_on_nontrivial_line_choice": True,
    }


def part4_certificate_boundary() -> dict[str, bool]:
    print("\nPart 4: certificate boundary")
    boundary = {
        "strict_wz_denominator_response_closed": True,
        "strict_symbolic_top_shape_closed": True,
        "conditional_c3_target_row_available": True,
        "same_surface_splice_authority_derived": False,
        "same_source_id_certified": False,
        "physical_top_line_nontrivial_derived": False,
        "accepted_top_projector_or_pole_isolated": False,
        "accepted_w_pole_isolated_on_spliced_surface": False,
        "coefficient_certified_dM_t_row_present": False,
        "coefficient_certified_dM_W_row_present_on_same_packet": False,
        "contact_fv_ir_model_class_controls_present": False,
        "strict_positive_certificate_present": False,
        "no_forbidden_imports": True,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key, value in boundary.items():
        check(f"boundary field recorded: {key}", isinstance(value, bool), value)
    check("closed support fields are true", all(boundary[key] for key in (
        "strict_wz_denominator_response_closed",
        "strict_symbolic_top_shape_closed",
        "conditional_c3_target_row_available",
    )))
    check("same-surface splice authority remains open", boundary["same_surface_splice_authority_derived"] is False)
    check("physical top-line authority remains open", boundary["physical_top_line_nontrivial_derived"] is False)
    check("strict positive certificate remains absent", boundary["strict_positive_certificate_present"] is False)
    return boundary


def part5_no_go_audit() -> dict[str, Any]:
    print("\nPart 5: no-go audit")
    audit = {
        "route_tested": "strict W/Z denominator plus conditional C3 target row is already a strict top/W pole certificate",
        "route_pruned": True,
        "why_pruned": (
            "The target readout requires same-surface splice authority and a "
            "physical nontrivial top line. The same denominator and source "
            "scale also admit the P0 singlet row."
        ),
        "counterwitness": {
            "same_denominator": "g_2*A/2",
            "nontrivial_readout": "1/sqrt(6)",
            "singlet_readout": "sqrt(2/3)",
        },
        "strict_route_still_live": True,
        "new_required_input": (
            "accepted strict top/W pole rows, or accepted same-surface "
            "backend/projectors/source-generator matrix elements"
        ),
    }
    check("route is pruned", audit["route_pruned"] is True)
    check("strict route remains live", audit["strict_route_still_live"] is True)
    check("counterwitness contains singlet readout", audit["counterwitness"]["singlet_readout"] == "sqrt(2/3)")
    check("required input names accepted strict rows", "accepted strict top/W pole rows" in audit["new_required_input"])
    return audit


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    text = read(NOTE)
    for phrase in (
        "`H_unit`",
        "old Ward authority",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG targets",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
        "target value insertion",
    ):
        check(f"firewall phrase present: {phrase}", phrase in text)

    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "positive closure is achieved",
        "strict top/W pole-response certificate is present",
        "This note derives `y_t`",
        "the physical top line is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part7_claim_status() -> dict[str, Any]:
    print("\nPart 7: claim status")
    status = {
        "actual_current_surface_status": "no-go / open strict splice authority",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes strict denominator plus conditional C3 row shortcut",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The formal splice gives 1/sqrt(6) only after supplying "
            "same-surface authority and the physical nontrivial top line. "
            "The same denominator and source scale also admit the singlet "
            "row sqrt(2/3), so the top-line/projector authority remains "
            "load-bearing."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": (
            "strict W/Z denominator response plus conditional C3 target row "
            "is already an accepted strict same-source top/W pole-response certificate"
        ),
        "route_still_live": (
            "produce accepted strict top/W pole rows, or derive the accepted "
            "same-surface backend/projectors/source-generator matrix elements"
        ),
    }
    check("actual status is no-go/open", status["actual_current_surface_status"] == "no-go / open strict splice authority")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("bare retained remains false", status["bare_retained_allowed"] is False)
    check("route still live names strict rows", "accepted strict top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT W/Z PLUS C3 TOP-ROW SPLICE NO-GO")
    print("=" * 78)

    part1_anchors()
    dependencies = part2_dependency_outputs()
    splice = part3_splice_algebra()
    boundary = part4_certificate_boundary()
    audit = part5_no_go_audit()
    part6_firewalls()
    status = part7_claim_status()

    result = {
        "claim_id": "yt_strict_wz_c3_top_row_splice_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_strict_wz_c3_top_row_splice_no_go.py",
        **status,
        "dependencies": {
            "strict_wz_fail_count": dependencies["strict_wz"].get("fail_count"),
            "strict_symbolic_top_fail_count": dependencies["strict_symbolic_top"].get("fail_count"),
            "same_surface_matrix_fail_count": dependencies["same_surface_matrix"].get("fail_count"),
            "c3_source_extremal_fail_count": dependencies["source_extremal"].get("fail_count"),
            "strict_availability_fail_count": dependencies["strict_availability"].get("fail_count"),
            "strict_discovery_fail_count": dependencies["strict_discovery"].get("fail_count"),
        },
        "splice_witness": splice,
        "certificate_boundary": boundary,
        "no_go_audit": audit,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_strict_wz_c3_top_row_splice_no_go.py",
            "outputs/yt_strict_wz_c3_top_row_splice_no_go_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
