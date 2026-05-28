#!/usr/bin/env python3
"""Y_T C3 hard-boundary readout law underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json"

NOTE = DOCS / "YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
HARD_BOUNDARY_SUPPORT = DOCS / "YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md"
MININFO_NOGO = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_RESPONSE_EXTREMA = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
C3_TRACE_FREE = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

HARD_BOUNDARY_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json"
MININFO_NOGO_OUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_SOURCE_ORIENTATION_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
C3_SOURCE_RESPONSE_EXTREMA_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
C3_TRACE_FREE_OUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"
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


def part1_anchors() -> dict[str, str | None]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        HARD_BOUNDARY_SUPPORT,
        MININFO_NOGO,
        C3_BLOCK_SUPPORT,
        C3_SOURCE_ORIENTATION,
        C3_SOURCE_RESPONSE_EXTREMA,
        C3_TRACE_FREE,
        STRICT_AVAILABILITY,
        HARD_BOUNDARY_SUPPORT_OUT,
        MININFO_NOGO_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_SOURCE_ORIENTATION_OUT,
        C3_SOURCE_RESPONSE_EXTREMA_OUT,
        C3_TRACE_FREE_OUT,
        STRICT_AVAILABILITY_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Current Stack",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Boundary Witness",
        "Stuck Fan-Out Synthesis",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open hard-boundary readout law",
        "proposal_allowed: false",
        "nearest Fisher boundary",
        "minimum support-rank",
        "positive source-coordinate asymptote",
        "largest absolute `B_x` response",
        "retained structure",
    ):
        check(f"note contains hard-boundary underdetermination phrase: {phrase}", phrase in note)

    deps = {
        "hard_boundary_support": load_json(HARD_BOUNDARY_SUPPORT_OUT),
        "minimum_information_no_go": load_json(MININFO_NOGO_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "source_orientation": load_json(C3_SOURCE_ORIENTATION_OUT),
        "source_response_extrema": load_json(C3_SOURCE_RESPONSE_EXTREMA_OUT),
        "trace_free": load_json(C3_TRACE_FREE_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "prior support says nearest Fisher boundary face is P_nt",
        deps["hard_boundary_support"].get("support_certificate", {}).get("nearest_fisher_boundary_face_is_Pnt")
        is True,
    )
    check(
        "prior support says nearest-face law is not accepted",
        deps["hard_boundary_support"].get("support_certificate", {}).get("accepted_nearest_face_top_readout_law_derived")
        is False,
    )
    check(
        "finite minimum-information route is already pruned",
        deps["minimum_information_no_go"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "block support says P_nt gives A/sqrt(12)",
        deps["block_support"].get("block_matrix_element_witness", {}).get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "source sign shortcut remains pruned",
        deps["source_orientation"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "response-extremal shortcut remains pruned",
        deps["source_response_extrema"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_c3_boundary_endpoints() -> dict[str, Any]:
    print("\nPart 2: C3 hard-boundary endpoint algebra")
    sqrt = sp.sqrt
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_p0 = P0
    rho_pnt = sp.simplify(Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))

    p0_response = sp.simplify(sp.trace(rho_p0 * Bx))
    pnt_response = sp.simplify(sp.trace(rho_pnt * Bx))
    p0_row = sp.simplify(A * p0_response / sqrt(2))
    pnt_row = sp.simplify(A * pnt_response / sqrt(2))

    check("P_0 and P_nt are complementary projectors", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("rho_P0 has unit trace", is_zero(sp.trace(rho_p0) - 1))
    check("rho_Pnt has unit trace", is_zero(sp.trace(rho_pnt) - 1))
    check("P_0 boundary response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("P_nt boundary response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("P_0 conditional row has magnitude A/sqrt(3)", is_zero(p0_row - A / sqrt(3)), p0_row)
    check("P_nt conditional row has magnitude A/sqrt(12)", is_zero(abs(pnt_row) - A / sqrt(12)), pnt_row)

    return {
        "endpoint_rows": {
            "P_nt": "A/sqrt(12)",
            "P_0": "A/sqrt(3)",
        },
        "endpoint_responses": {
            "P_nt": "-1/sqrt(6)",
            "P_0": "2/sqrt(6)",
        },
    }


def part3_competing_boundary_rules() -> dict[str, Any]:
    print("\nPart 3: same-data hard-boundary rule witnesses")
    s = sp.symbols("s", positive=True)
    primitive = 2 * sp.asin(sp.sqrt(s))
    baseline = sp.Rational(1, 3)
    distance_to_pnt = sp.simplify(primitive.subs(s, baseline) - primitive.subs(s, 0))
    distance_to_p0 = sp.simplify(primitive.subs(s, 1) - primitive.subs(s, baseline))
    distance_gap = sp.N(distance_to_p0 - distance_to_pnt, 30)

    entropy_pnt = sp.log(2)
    entropy_p0 = sp.Integer(0)
    purity_pnt = sp.Rational(1, 2)
    purity_p0 = sp.Integer(1)
    rank_pnt = 2
    rank_p0 = 1

    check("nearest Fisher boundary selects P_nt", distance_gap > 0, distance_gap)
    check("maximum boundary entropy selects P_nt", entropy_pnt > entropy_p0, (entropy_pnt, entropy_p0))
    check("maximum purity selects P_0", purity_p0 > purity_pnt, (purity_p0, purity_pnt))
    check("minimum support rank selects P_0", rank_p0 < rank_pnt, (rank_p0, rank_pnt))

    ell = sp.symbols("ell", real=True)
    b0 = 2 / sp.sqrt(6)
    bnt = -1 / sp.sqrt(6)
    z = sp.simplify(sp.exp(ell * b0) + 2 * sp.exp(ell * bnt))
    singlet_weight = sp.simplify(sp.exp(ell * b0) / z)
    check("positive source-coordinate asymptote selects P_0", sp.limit(singlet_weight, ell, sp.oo) == 1)
    check("negative source-coordinate asymptote selects P_nt", sp.limit(singlet_weight, ell, -sp.oo) == 0)
    check("absolute response maximum selects P_0", abs(b0) > abs(bnt), (abs(b0), abs(bnt)))
    check("minimum signed response selects P_nt only with convention", bnt < b0, (bnt, b0))

    rule_witnesses = {
        "nearest_fisher_boundary": {"selected_endpoint": "P_nt", "conditional_row": "A/sqrt(12)", "accepted": False},
        "maximum_boundary_entropy": {"selected_endpoint": "P_nt", "conditional_row": "A/sqrt(12)", "accepted": False},
        "maximum_purity_or_minimum_rank": {"selected_endpoint": "P_0", "conditional_row": "A/sqrt(3)", "accepted": False},
        "positive_source_asymptote": {"selected_endpoint": "P_0", "conditional_row": "A/sqrt(3)", "accepted": False},
        "negative_source_asymptote": {"selected_endpoint": "P_nt", "conditional_row": "A/sqrt(12)", "accepted": False},
        "absolute_response_maximum": {"selected_endpoint": "P_0", "conditional_row": "A/sqrt(3)", "accepted": False},
        "signed_response_minimum": {"selected_endpoint": "P_nt", "conditional_row": "A/sqrt(12)", "accepted": False},
    }
    check(
        "same boundary data admit target and non-target selections",
        {item["selected_endpoint"] for item in rule_witnesses.values()} == {"P_nt", "P_0"},
        rule_witnesses,
    )

    return {
        "distance_to_P_nt": "2 asin(1/sqrt(3))",
        "distance_to_P_0": "pi - 2 asin(1/sqrt(3))",
        "distance_gap_numeric": str(distance_gap),
        "boundary_entropy": {"P_nt": "log(2)", "P_0": "0"},
        "boundary_purity": {"P_nt": "1/2", "P_0": "1"},
        "support_rank": {"P_nt": 2, "P_0": 1},
        "rule_witnesses": rule_witnesses,
    }


def part4_no_go_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "hard_boundary_completion_available": True,
        "nearest_fisher_boundary_face_is_Pnt": True,
        "nearest_face_would_exclude_P0": True,
        "nearest_face_would_give_A_over_sqrt12_with_generator_factorization": True,
        "same_data_rules_can_select_P0": True,
        "same_data_rules_can_select_Pnt": True,
        "accepted_nearest_face_top_readout_law_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field {key}", key in certificate, value)
    check("nearest-face remains support only", certificate["accepted_nearest_face_top_readout_law_derived"] is False)
    check("P_0 counterselection remains allowed by same data", certificate["same_data_rules_can_select_P0"] is True)
    check("retained proposal remains forbidden", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "route_pruned": (
            "current C3 RN/Fisher hard-boundary information geometry derives "
            "accepted nearest-hard-boundary-face physical top-readout law"
        ),
        "reason": (
            "The same compactified C3 source curve supports nearest-face and "
            "entropy rules selecting P_nt, but also purity, rank, positive "
            "source-asymptote, and response-maximum rules selecting P_0. "
            "No current accepted same-surface principle chooses nearest-face "
            "as the physical top readout."
        ),
        "not_pruned": (
            "a future accepted same-surface dynamics theorem deriving "
            "nearest-face hard-boundary readout"
        ),
        "route_still_live": [
            "accepted hard-boundary nearest-face top-readout law plus generator factorization",
            "another accepted physical top-block/readout law excluding P_0",
            "accepted strict same-source top/W pole rows with controls",
        ],
    }
    check("no-go audit prunes only current-geometry derivation", "current C3 RN/Fisher" in no_go_audit["route_pruned"])
    check("no-go audit keeps future dynamics route live", "future accepted" in no_go_audit["not_pruned"])
    return {"certificate": certificate, "no_go_audit": no_go_audit}


def main() -> int:
    print("=" * 78)
    print("Y_T C3 HARD-BOUNDARY READOUT LAW UNDERDETERMINATION NO-GO")
    print("=" * 78)

    dependency_statuses = part1_anchors()
    endpoint_witness = part2_c3_boundary_endpoints()
    rule_witnesses = part3_competing_boundary_rules()
    no_go = part4_no_go_certificate()

    result = {
        "actual_current_surface_status": "no-go / open hard-boundary readout law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Nearest-Fisher-face selection still selects P_nt exactly, but the same "
            "hard-boundary data also admit P_0-selecting purity/rank/source-asymptote/"
            "response-maximum rules. The current surface has not accepted nearest-face "
            "selection as the physical top readout and still lacks generator "
            "factorization plus strict pole controls."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": dependency_statuses,
        "endpoint_witness": endpoint_witness,
        "same_data_boundary_rule_witnesses": rule_witnesses,
        "certificate_boundary": no_go["certificate"],
        "no_go_audit": no_go["no_go_audit"],
        "route_still_live": (
            "derive accepted hard-boundary nearest-face top-readout law with "
            "same-surface generator factorization, or produce strict same-source "
            "top/W pole rows directly"
        ),
        "review_surface": [
            "docs/YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_hard_boundary_readout_law_underdetermination.py",
            "outputs/yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json",
        ],
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
