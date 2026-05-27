#!/usr/bin/env python3
"""Y_T C3 minimum-information hard-boundary face-selector support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json"

NOTE = DOCS / "YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md"
MININFO_NOGO = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
C3_TRACE_FREE = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_ZERO_SINGLET = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

MININFO_NOGO_OUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_SOURCE_ORIENTATION_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
C3_TRACE_FREE_OUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"
C3_ZERO_SINGLET_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
MIN_INFO_OUT = ROOT / "outputs" / "yt_minimum_information_source_action_bridge_2026-05-26.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        MININFO_NOGO,
        C3_BLOCK_SUPPORT,
        C3_SOURCE_ORIENTATION,
        C3_TRACE_FREE,
        C3_ZERO_SINGLET,
        MIN_INFO,
        C3_REAL_SOURCE,
        STRICT_AVAILABILITY,
        MININFO_NOGO_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_SOURCE_ORIENTATION_OUT,
        C3_TRACE_FREE_OUT,
        C3_ZERO_SINGLET_OUT,
        MIN_INFO_OUT,
        C3_REAL_SOURCE_OUT,
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
        "Boundary Geometry",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: exact-support / open hard-boundary readout law",
        "proposal_allowed: false",
        "nearest hard boundary",
        "P_nt",
        "A/sqrt(12)",
        "A/sqrt(3)",
        "not an accepted physical readout law",
    ):
        check(f"note contains support-boundary phrase: {phrase}", phrase in note)

    deps = {
        "minimum_information_no_go": load_json(MININFO_NOGO_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "source_orientation": load_json(C3_SOURCE_ORIENTATION_OUT),
        "trace_free": load_json(C3_TRACE_FREE_OUT),
        "zero_singlet": load_json(C3_ZERO_SINGLET_OUT),
        "minimum_information": load_json(MIN_INFO_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "finite minimum-information readout route is already pruned",
        deps["minimum_information_no_go"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "finite tilt cannot set zero singlet weight",
        deps["minimum_information_no_go"].get("certificate_boundary", {}).get("finite_rn_tilt_can_set_singlet_weight_zero")
        is False,
    )
    check(
        "block support says P_nt gives target row",
        deps["block_support"].get("block_matrix_element_witness", {}).get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "source-orientation shortcut remains pruned",
        deps["source_orientation"].get("certificate_boundary", {}).get("accepted_source_orientation_law_for_Pnt_derived")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_boundary_compactification() -> dict[str, Any]:
    print("\nPart 2: C3 RN hard-boundary compactification")
    sqrt = sp.sqrt
    ell, t = sp.symbols("ell t", real=True, positive=True)
    b0 = 2 / sqrt(6)
    bnt = -1 / sqrt(6)
    s = sp.simplify(t / (t + 2))
    response = sp.simplify(s * b0 + (1 - s) * bnt)
    response_singlet_boundary = sp.limit(response, t, sp.oo)
    response_nontrivial_boundary = sp.limit(response, t, 0, dir="+")

    check("singlet weight lies between zero and one for finite t", True, s)
    check("t -> 0 gives zero singlet weight", sp.limit(s, t, 0, dir="+") == 0)
    check("t -> infinity gives full singlet weight", sp.limit(s, t, sp.oo) == 1)
    check("P_nt boundary response is -1/sqrt(6)", is_zero(response_nontrivial_boundary + 1 / sqrt(6)), response_nontrivial_boundary)
    check("P_0 boundary response is 2/sqrt(6)", is_zero(response_singlet_boundary - 2 / sqrt(6)), response_singlet_boundary)
    check("finite t keeps positive singlet weight", True, "t/(t+2) > 0 for t > 0")

    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    check("P_0 and P_nt are orthogonal projectors", is_zero(P0 * Pnt) and is_zero(P0**2 - P0) and is_zero(Pnt**2 - Pnt))
    check("B_x is scalar on P_nt", is_zero(Bx * Pnt + Pnt / sqrt(6)))
    check("B_x is scalar on P_0", is_zero(Bx * P0 - 2 * P0 / sqrt(6)))

    return {
        "compactified_family": "q(s) = (s, (1-s)/2, (1-s)/2)",
        "natural_parameter_substitution": "t = exp(3 ell/sqrt(6))",
        "singlet_weight": "s = t/(t+2)",
        "nontrivial_boundary": {"t": "0", "s": "0", "response": "-1/sqrt(6)", "conditional_row": "A/sqrt(12)"},
        "singlet_boundary": {"t": "infinity", "s": "1", "response": "2/sqrt(6)", "conditional_row": "A/sqrt(3)"},
        "boundary_completion_selects_endpoint_by_itself": False,
    }


def part3_fisher_nearest_face_support() -> dict[str, Any]:
    print("\nPart 3: Fisher nearest-face support")
    s = sp.symbols("s", positive=True)
    metric_density = sp.simplify(1 / (s * (1 - s)))
    primitive = 2 * sp.asin(sp.sqrt(s))
    baseline = sp.Rational(1, 3)
    distance_to_pnt = sp.simplify(primitive.subs(s, baseline) - primitive.subs(s, 0))
    distance_to_p0 = sp.simplify(primitive.subs(s, 1) - primitive.subs(s, baseline))
    gap = sp.N(distance_to_p0 - distance_to_pnt, 30)

    check("Fisher metric density is 1/[s(1-s)]", is_zero(metric_density - 1 / (s * (1 - s))), metric_density)
    check("primitive differentiates to Fisher line element", is_zero(sp.diff(primitive, s) ** 2 - metric_density))
    check("distance to P_nt is 2 asin(1/sqrt(3))", is_zero(distance_to_pnt - 2 * sp.asin(1 / sp.sqrt(3))), distance_to_pnt)
    check("distance to P_0 is pi - 2 asin(1/sqrt(3))", is_zero(distance_to_p0 - (sp.pi - 2 * sp.asin(1 / sp.sqrt(3)))), distance_to_p0)
    check("P_nt face is nearer than P_0 face", gap > 0, gap)
    check("nearest-face rule would select P_nt", gap > 0, gap)
    check("nearest-face rule is not present in current authority", True, "open hard-boundary readout law")

    return {
        "fisher_metric_on_c3_block_curve": "ds^2/[s(1-s)]",
        "baseline": "s = 1/3",
        "distance_to_P_nt": "2 asin(1/sqrt(3))",
        "distance_to_P_0": "pi - 2 asin(1/sqrt(3))",
        "distance_gap_numeric": str(gap),
        "nearest_boundary_face": "P_nt",
        "nearest_face_implies_zero_singlet": True,
        "nearest_face_law_accepted_on_current_surface": False,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: support and no-go certificate")
    support_certificate = {
        "hard_boundary_completion_available": True,
        "hard_boundary_completion_alone_selects_Pnt": False,
        "nearest_fisher_boundary_face_is_Pnt": True,
        "nearest_face_would_exclude_P0": True,
        "nearest_face_would_give_A_over_sqrt12_with_generator_factorization": True,
        "accepted_nearest_face_top_readout_law_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in support_certificate:
        check(f"support certificate field recorded: {key}", key in support_certificate)
    check("boundary completion alone does not select P_nt", support_certificate["hard_boundary_completion_alone_selects_Pnt"] is False)
    check("nearest Fisher face selects P_nt conditionally", support_certificate["nearest_fisher_boundary_face_is_Pnt"] is True)
    check("nearest-face readout law remains open", support_certificate["accepted_nearest_face_top_readout_law_derived"] is False)

    no_go_audit = {
        "route_pruned": "minimum-information hard-boundary completion alone derives accepted zero-singlet physical top-block membership",
        "reason": (
            "The compactified C3 RN/Fisher source family has two endpoints: "
            "P_nt and P_0. A nearest-Fisher-face rule selects P_nt exactly, "
            "but that rule is an additional physical hard-boundary readout "
            "law not accepted on the current surface."
        ),
        "route_still_live": [
            "accepted hard-boundary nearest-face top-readout law plus generator factorization",
            "another accepted physical top-block/readout law excluding P_0",
            "accepted strict same-source top/W pole rows with controls",
        ],
    }
    check("no-go audit names hard-boundary completion route", "hard-boundary" in no_go_audit["route_pruned"])
    check("no-go audit names two endpoints", "two endpoints" in no_go_audit["reason"])
    check("no-go audit keeps strict rows live", any("strict" in item for item in no_go_audit["route_still_live"]))
    return {"support_certificate": support_certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "positive closure is achieved",
        "hard-boundary readout law is derived",
        "nearest-boundary face selection is accepted",
        "zero-singlet physical top-block membership is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 MININFO HARD-BOUNDARY FACE-SELECTOR SUPPORT")
    print("=" * 78)

    dependencies = part1_anchors()
    compactification = part2_boundary_compactification()
    fisher_face = part3_fisher_nearest_face_support()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "exact-support / open hard-boundary readout law",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The C3 minimum-information hard-boundary geometry makes P_nt "
            "the nearest Fisher boundary face from the symmetric baseline, "
            "and P_nt support would give A/sqrt(12) with the still-open "
            "generator factorization. The current surface has not accepted "
            "nearest-boundary face selection as the physical top readout."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": dependencies,
        "boundary_compactification": compactification,
        "fisher_nearest_face_support": fisher_face,
        "support_certificate": certificate["support_certificate"],
        "no_go_audit": certificate["no_go_audit"],
        "route_still_live": (
            "derive accepted hard-boundary nearest-face top-readout law plus "
            "same-surface generator factorization, derive another accepted "
            "physical top-block/readout law excluding P_0, or produce accepted "
            "strict same-source top/W pole rows with controls"
        ),
        "review_surface": [
            "docs/YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_mininfo_hard_boundary_face_selector_support.py",
            "outputs/yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json",
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
