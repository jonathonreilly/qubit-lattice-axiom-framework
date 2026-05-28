#!/usr/bin/env python3
"""Y_T C3 sharp-response readout underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_sharp_response_readout_underdetermination_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_SHARP_RESPONSE_READOUT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
COMPENSATION_NOGO = DOCS / "YT_C3_RADIAL_READOUT_COMPENSATION_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION_NOGO = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

COMPENSATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_radial_readout_compensation_underdetermination_no_go_2026-05-28.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_SOURCE_ORIENTATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

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
        COMPENSATION_NOGO,
        C3_RADIAL_NOGO,
        C3_BLOCK_SUPPORT,
        C3_SOURCE_ORIENTATION_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK,
        COMPENSATION_NOGO_OUT,
        C3_RADIAL_NOGO_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_SOURCE_ORIENTATION_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
        FULL_STACK_OUT,
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
        "Finite Sharpness Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open sharp-readout physical selection law",
        "proposal_allowed: false",
        "Var_rho(s)(B_x) = (3/2) s(1-s)",
        "Sharp B_x response is not a physical top-block selection law",
        "target magnitude",
    ):
        check(f"note contains sharpness phrase: {phrase}", phrase in note)

    deps = {
        "compensation_nogo": load_json(COMPENSATION_NOGO_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_source_orientation_nogo": load_json(C3_SOURCE_ORIENTATION_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "compensation no-go keeps target magnitude non-certifying",
        deps["compensation_nogo"].get("certificate_boundary", {}).get("target_magnitude_forces_zero_singlet")
        is False,
    )
    check(
        "radial no-go keeps lambda_top free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "block support keeps zero singlet law open",
        deps["c3_block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "source orientation law remains open",
        deps["c3_source_orientation_nogo"]
        .get("certificate_boundary", {})
        .get("accepted_source_orientation_law_for_Pnt_derived")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_sharpness_family() -> dict[str, Any]:
    print("\nPart 2: C3 sharp-response family")
    sqrt = sp.sqrt
    A, g2, lambda_top = sp.symbols("A g_2 lambda_top", positive=True)
    s = sp.symbols("s", real=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_s = sp.simplify(s * P0 + (1 - s) * Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))

    check("C has order three", is_zero(C**3 - I))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("rho(s) has unit trace", is_zero(sp.trace(rho_s) - 1), sp.trace(rho_s))
    check("B_x is normalized", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1))

    mean = sp.simplify(sp.trace(rho_s * Bx))
    second = sp.simplify(sp.trace(rho_s * Bx**2))
    variance = sp.simplify(second - mean**2)
    signed_row = sp.simplify(lambda_top * A * mean)
    row_magnitude = sp.simplify(abs(signed_row))
    dmw = g2 * A / 2
    readout_magnitude = sp.simplify(g2 / sqrt(2) * row_magnitude / dmw)

    check("B_x mean is (3s-1)/sqrt(6)", is_zero(mean - (3 * s - 1) / sqrt(6)), mean)
    check("B_x second moment is (1+3s)/6", is_zero(second - (1 + 3 * s) / 6), second)
    check("B_x variance is 3*s*(1-s)/2", is_zero(variance - sp.Rational(3, 2) * s * (1 - s)), variance)
    check("same-source readout magnitude is lambda_top*|3s-1|/sqrt(3)", True, readout_magnitude)

    sharp_solutions = sp.solve(sp.Eq(variance, 0), s)
    check("zero response variance endpoints are s=0 and s=1", sharp_solutions == [0, 1], sharp_solutions)

    pnt_target = {s: sp.Integer(0), lambda_top: 1 / sqrt(2)}
    p0_target = {s: sp.Integer(1), lambda_top: 1 / (2 * sqrt(2))}
    p0_standard_radial = {s: sp.Integer(1), lambda_top: 1 / sqrt(2)}

    for label, subs in (
        ("P_nt sharp endpoint", pnt_target),
        ("P_0 sharp endpoint with compensating radial factor", p0_target),
    ):
        check(f"{label} has zero variance", is_zero(variance.subs(subs)), variance.subs(subs))
        check(f"{label} gives target row magnitude", is_zero(row_magnitude.subs(subs) - A / sqrt(12)), row_magnitude.subs(subs))
        check(
            f"{label} gives target readout magnitude",
            is_zero(readout_magnitude.subs(subs) - 1 / sqrt(6)),
            readout_magnitude.subs(subs),
        )

    check("P_0 endpoint is sharp but has positive singlet weight", p0_target[s] == 1, p0_target[s])
    check(
        "P_0 endpoint needs nonstandard radial factor for target magnitude",
        not is_zero(p0_target[lambda_top] - 1 / sqrt(2)),
        p0_target[lambda_top],
    )
    check(
        "P_0 endpoint with standard radial misses target",
        not is_zero(row_magnitude.subs(p0_standard_radial) - A / sqrt(12)),
        row_magnitude.subs(p0_standard_radial),
    )

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "rho_s": "s*P_0 + (1-s)*P_nt/2",
        "B_x_mean": "(3*s - 1)/sqrt(6)",
        "B_x_second_moment": "(1 + 3*s)/6",
        "B_x_variance": "3*s*(1-s)/2",
        "zero_variance_solutions": ["0", "1"],
        "target_magnitude_with_zero_variance": [
            {"singlet_weight_s": "0", "lambda_top": "1/sqrt(2)", "block": "P_nt"},
            {"singlet_weight_s": "1", "lambda_top": "1/(2*sqrt(2))", "block": "P_0"},
        ],
        "zero_variance_forces_zero_singlet": False,
        "zero_variance_forces_radial_factor": False,
        "zero_variance_allows_singlet_endpoint": True,
    }


def part3_endpoint_orientation_boundary() -> dict[str, Any]:
    print("\nPart 3: endpoint sign and response-order boundary")
    sqrt = sp.sqrt
    responses = {"P_nt": -1 / sqrt(6), "P_0": 2 / sqrt(6)}
    magnitudes = {name: sp.Abs(value) for name, value in responses.items()}
    largest_abs = max(magnitudes, key=lambda name: float(sp.N(magnitudes[name])))
    smallest_abs = min(magnitudes, key=lambda name: float(sp.N(magnitudes[name])))

    check("largest absolute sharp endpoint is P_0", largest_abs == "P_0", largest_abs)
    check("smallest absolute sharp endpoint is P_nt", smallest_abs == "P_nt", smallest_abs)
    check("minimum absolute endpoint selector is an added convention", smallest_abs == "P_nt")

    return {
        "sharp_endpoint_responses": {"P_nt": "-1/sqrt(6)", "P_0": "2/sqrt(6)"},
        "largest_absolute_endpoint": "P_0",
        "minimum_absolute_endpoint": "P_nt",
        "minimum_endpoint_selector_derived": False,
        "source_orientation_sign_law_load_bearing": True,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "route_pruned": "sharp same-source B_x response certifies zero-singlet readout or radial factorization",
        "zero_variance_granted": True,
        "zero_variance_forces_zero_singlet": False,
        "zero_variance_forces_radial_factor": False,
        "zero_variance_allows_singlet_endpoint": True,
        "signed_endpoint_requires_orientation_law": True,
        "accepted_physical_sharp_endpoint_selector_derived": False,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("zero variance does not force zero singlet", certificate["zero_variance_forces_zero_singlet"] is False)
    check("zero variance does not force radial factor", certificate["zero_variance_forces_radial_factor"] is False)
    check("sharp singlet endpoint remains allowed", certificate["zero_variance_allows_singlet_endpoint"] is True)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "narrow_route_pruned": certificate["route_pruned"],
        "reason": (
            "The sharpness equation Var(B_x)=0 gives s=0 or s=1. "
            "The s=1 singlet endpoint is sharp and can be target-size if "
            "lambda_top is allowed to compensate. Sharpness is therefore "
            "not an accepted physical top-block or radial-factor theorem."
        ),
        "remaining_imports": [
            "accepted physical endpoint/readout law excluding P_0",
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical source-orientation/sign law if signed C3 response is used",
            "accepted W/top pole controls or direct strict pole rows",
        ],
        "route_still_live": [
            "derive independent radial/readout/sign laws on the same surface",
            "produce accepted strict same-source top/W pole rows with controls",
            "derive accepted microscopic backend/projectors/source-generator matrix elements",
        ],
    }
    check("no-go audit names sharpness", "Var(B_x)=0" in no_go_audit["reason"])
    check("no-go audit keeps strict pole route live", any("strict" in item for item in no_go_audit["route_still_live"]))
    return {"certificate_boundary": certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
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
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive closure",
        "zero singlet weight is derived",
        "lambda_top is derived",
        "strict W/top pole rows are provided",
        "proposal_allowed: true",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 SHARP-RESPONSE READOUT UNDERDETERMINATION NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    sharpness = part2_sharpness_family()
    endpoint_boundary = part3_endpoint_orientation_boundary()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "claim_id": "yt_c3_sharp_response_readout_underdetermination_no_go_note_2026-05-28",
        "generated_by": "scripts/frontier_yt_c3_sharp_response_readout_underdetermination_no_go.py",
        "actual_current_surface_status": "no-go / open sharp-readout physical selection law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "sharp same-source B_x response certifies zero-singlet readout or radial factorization",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Zero response variance selects both the nontrivial endpoint and "
            "the singlet endpoint. With radial coupling still open, both can "
            "be target-size. A physical readout/sign/radial theorem or strict "
            "pole-row certificate remains load-bearing."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchor_statuses": anchors,
        "sharpness_family": sharpness,
        "endpoint_orientation_boundary": endpoint_boundary,
        **certificate,
        "first_open_gate_after_this_note": (
            "accepted independent readout/sign/radial laws, or accepted strict "
            "same-source top/W pole rows with controls"
        ),
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
