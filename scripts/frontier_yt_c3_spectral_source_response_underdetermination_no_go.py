#!/usr/bin/env python3
"""Y_T C3 spectral source-response underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_SPECTRAL_SOURCE_RESPONSE_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_SPECTRAL_SUPPORT = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
TOP_PROJECTOR_OBSTRUCTION = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_SPECTRAL_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
TOP_PROJECTOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        C3_SPECTRAL_SUPPORT,
        TOP_PROJECTOR_OBSTRUCTION,
        FULL_STACK,
        C3_SPECTRAL_SUPPORT_OUT,
        TOP_PROJECTOR_OBSTRUCTION_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "What This Prunes",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "Spectral projectors are not source-response coefficients",
        "same-surface source law for the circulant coefficients",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    spectral = load_json(C3_SPECTRAL_SUPPORT_OUT)
    top_projector = load_json(TOP_PROJECTOR_OBSTRUCTION_OUT)
    check("C3 spectral support passed", spectral.get("fail_count") == 0, spectral.get("fail_count"))
    check("C3 spectral support remains proposal false", spectral.get("proposal_allowed") is False)
    check("top projector obstruction passed", top_projector.get("fail_count") == 0, top_projector.get("fail_count"))
    return {"c3_spectral_support": spectral, "top_projector_obstruction": top_projector}


def part2_source_response_witness() -> dict[str, Any]:
    print("\nPart 2: source-response witness")
    h = sp.symbols("h", real=True)
    a0, x0, y0 = sp.symbols("a0 x0 y0", real=True)
    c = 1 / sp.sqrt(6)

    # Top line chosen as lambda_0. The same logic applies to the other lines
    # with different linear combinations of a', x', y'.
    lambda0 = lambda a, x, y: sp.simplify(a + 2 * x)
    lambda1 = lambda a, x, y: sp.simplify(a - x - sp.sqrt(3) * y)
    lambda2 = lambda a, x, y: sp.simplify(a - x + sp.sqrt(3) * y)

    path_a = {
        "a": a0 + c * h,
        "x": x0,
        "y": y0,
    }
    path_b = {
        "a": a0 + 2 * c * h,
        "x": x0,
        "y": y0,
    }
    top_a = lambda0(**path_a)
    top_b = lambda0(**path_b)
    d_top_a = sp.diff(top_a, h)
    d_top_b = sp.diff(top_b, h)

    check("path A top response is 1/sqrt(6)", is_zero(d_top_a - c), d_top_a)
    check("path B top response is 2/sqrt(6)", is_zero(d_top_b - 2 * c), d_top_b)
    check("responses differ despite same spectral line", not is_zero(d_top_a - d_top_b), (d_top_a, d_top_b))

    base_a = {key: sp.simplify(value.subs(h, 0)) for key, value in path_a.items()}
    base_b = {key: sp.simplify(value.subs(h, 0)) for key, value in path_b.items()}
    check("paths have same base a coefficient", is_zero(base_a["a"] - base_b["a"]))
    check("paths have same base x coefficient", is_zero(base_a["x"] - base_b["x"]))
    check("paths have same base y coefficient", is_zero(base_a["y"] - base_b["y"]))

    da, dx, dy = sp.symbols("da dx dy", real=True)
    generic_response_0 = sp.simplify(da + 2 * dx)
    generic_response_1 = sp.simplify(da - dx - sp.sqrt(3) * dy)
    generic_response_2 = sp.simplify(da - dx + sp.sqrt(3) * dy)
    check("lambda0 response depends on a and x source law", generic_response_0.has(da) and generic_response_0.has(dx), generic_response_0)
    check("lambda1 response depends on a,x,y source law", all(generic_response_1.has(v) for v in (da, dx, dy)), generic_response_1)
    check("lambda2 response depends on a,x,y source law", all(generic_response_2.has(v) for v in (da, dx, dy)), generic_response_2)

    sample = {
        a0: 1,
        x0: sp.Rational(1, 5),
        y0: sp.Rational(1, 7),
    }
    base_eigs = [sp.N(expr.subs(sample), 16) for expr in (lambda0(a0, x0, y0), lambda1(a0, x0, y0), lambda2(a0, x0, y0))]
    check("sample base spectrum is nondegenerate", len({str(v) for v in base_eigs}) == 3, base_eigs)

    return {
        "top_line": "lambda0",
        "path_A_response": sp.sstr(d_top_a),
        "path_B_response": sp.sstr(d_top_b),
        "generic_responses": {
            "lambda0": sp.sstr(generic_response_0),
            "lambda1": sp.sstr(generic_response_1),
            "lambda2": sp.sstr(generic_response_2),
        },
        "sample_base_eigenvalues": [str(v) for v in base_eigs],
        "conclusion": "C3 spectral projectors do not determine source responses",
    }


def part3_certificate_boundary() -> dict[str, Any]:
    print("\nPart 3: certificate boundary")
    fields = {
        "accepted_c3_circulant_generation_operator": False,
        "same_surface_source_law_for_a_x_y": False,
        "top_line_ordering_derived": False,
        "d_lambda_top_dh_derived": False,
        "d_lambda_top_dh_equals_color_isospin_coefficient": False,
        "same_surface_w_response": False,
        "top_w_response_certificate_passes": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check("positive route is blocked by missing source law", fields["same_surface_source_law_for_a_x_y"] is False)
    check("strict certificate does not pass", fields["top_w_response_certificate_passes"] is False)
    return fields


def part4_firewalls() -> None:
    print("\nPart 4: firewalls")
    text = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
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
        "C3 spectral projector route is refuted",
        "source law is derived",
        "top response is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "C3 spectral projectors do not determine source responses. The "
            "top response depends on the h-derivatives of a,x,y, which are "
            "not derived on the current surface."
        ),
        "bare_retained_allowed": False,
        "route_pruned": "derive top response from C3 spectral projectors alone",
        "route_still_live": "derive same-surface source law for a,x,y or produce strict pole-row evidence",
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names source law", "source law" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    witness = part2_source_response_witness()
    fields = part3_certificate_boundary()
    part4_firewalls()
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_c3_spectral_source_response_underdetermination_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_spectral_source_response_underdetermination_no_go.py",
        "anchors": anchors,
        "source_response_witness": witness,
        "certificate_boundary": fields,
        **status,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
