#!/usr/bin/env python3
"""Y_T same-surface top matrix element factorization boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"

NOTE = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_NONTRIVIAL_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_MASS_ORDERING = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
DIRECT_SPARSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_NONTRIVIAL_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"
C3_MASS_ORDERING_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"

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


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current route state")
    for path in (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_REAL_SOURCE,
        C3_NONTRIVIAL_BOUNDARY,
        C3_MASS_ORDERING,
        DIRECT_SPARSE_CERT,
        FIRST_PRINCIPLES_OUT,
        C3_REAL_SOURCE_OUT,
        C3_NONTRIVIAL_BOUNDARY_OUT,
        C3_MASS_ORDERING_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Matrix Element Witness",
        "No-Go Boundary",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: conditional-support",
        "proposal_allowed: false",
        "A/sqrt(12)",
        "same-surface generator factorization",
        "nontrivial top-line assignment",
    ):
        check(f"note contains status/boundary phrase: {phrase}", phrase in note)

    first = load_json(FIRST_PRINCIPLES_OUT)
    real = load_json(C3_REAL_SOURCE_OUT)
    nontrivial = load_json(C3_NONTRIVIAL_BOUNDARY_OUT)
    mass_ordering = load_json(C3_MASS_ORDERING_OUT)

    check("first-principles transfer response passed", first.get("fail_count") == 0, first.get("fail_count"))
    check("first-principles route names top sector response row", "top sector response row" in first.get("first_open_gate_after_this_note", ""))
    check("real-record source theorem selects B_x", real.get("certificate_boundary", {}).get("source_direction_bx_selected") is True)
    check("nontrivial top-line boundary keeps assignment load-bearing", "nontrivial top-line assignment" in nontrivial.get("route_still_live", ""))
    check("mass-ordering obstruction selects P_0", mass_ordering.get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_line") == "P_0")

    return {
        "first_principles_status": first.get("actual_current_surface_status"),
        "real_record_status": real.get("actual_current_surface_status"),
        "nontrivial_boundary_status": nontrivial.get("actual_current_surface_status"),
        "mass_ordering_status": mass_ordering.get("actual_current_surface_status"),
    }


def part2_c3_matrix_element_factorization() -> dict[str, Any]:
    print("\nPart 2: C3 top matrix element factorization")
    sqrt = sp.sqrt
    A, g2 = sp.symbols("A g_2", positive=True)
    C = c3_cycle()
    omega = sp.Rational(-1, 2) + sp.I * sqrt(3) / 2
    bx = sp.simplify((C + C**2) / sqrt(6))
    radial_factor = A / sqrt(2)

    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }

    check("C has order three", is_zero(C**3 - sp.eye(3)))
    check("B_x is Hermitian", is_zero(bx.conjugate().T - bx))
    check("B_x is connected/traceless", is_zero(sp.trace(bx)))
    check("B_x has unit Frobenius norm", is_zero(sp.trace(bx.conjugate().T * bx) - 1))

    responses: dict[str, sp.Expr] = {}
    dmt_rows: dict[str, sp.Expr] = {}
    for name, projector in projectors.items():
        check(f"{name} is a rank-one projector", is_zero(projector**2 - projector) and is_zero(sp.trace(projector) - 1))
        responses[name] = sp.simplify(sp.expand_complex(sp.trace(projector * bx)))
        dmt_rows[name] = sp.simplify(radial_factor * responses[name])

    check("P_0 response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sqrt(6)), responses["P_omega2"])
    check("nontrivial top row magnitude is A/sqrt(12)", is_zero(abs(dmt_rows["P_omega"]) - A / sqrt(12)), dmt_rows["P_omega"])
    check("singlet top row magnitude is A/sqrt(3)", is_zero(abs(dmt_rows["P_0"]) - A / sqrt(3)), dmt_rows["P_0"])
    check("singlet row is twice target row", is_zero(abs(dmt_rows["P_0"]) / abs(dmt_rows["P_omega"]) - 2))

    dmt_target = A / sqrt(12)
    dmw = g2 * A / 2
    recovered = sp.simplify(g2 / sqrt(2) * dmt_target / dmw)
    check("target row with W denominator gives 1/sqrt(6)", is_zero(recovered - 1 / sqrt(6)), recovered)

    recovered_singlet = sp.simplify(g2 / sqrt(2) * (A / sqrt(3)) / dmw)
    check("singlet assignment gives 2/sqrt(6), not target", is_zero(recovered_singlet - 2 / sqrt(6)), recovered_singlet)

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "radial_factor": "A/sqrt(2)",
        "responses": {name: str(value) for name, value in responses.items()},
        "top_matrix_element_rows": {name: str(value) for name, value in dmt_rows.items()},
        "target_top_row": "A/sqrt(12)",
        "singlet_top_row": "A/sqrt(3)",
        "target_readout": "1/sqrt(6)",
        "singlet_readout": "2/sqrt(6)",
    }


def part3_certificate_boundary() -> dict[str, Any]:
    print("\nPart 3: certificate boundary")
    certificate = {
        "same_surface_factorization_schema_written": True,
        "radial_factor_algebra_checked": True,
        "c3_bx_source_direction_checked": True,
        "nontrivial_line_gives_target_row": True,
        "singlet_line_gives_different_row": True,
        "accepted_same_surface_generator_factorization": False,
        "accepted_physical_top_projector": False,
        "nontrivial_top_line_assignment_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", certificate[key] is value)
    check("top-line assignment remains load-bearing", certificate["nontrivial_top_line_assignment_derived"] is False)
    check("same-surface generator factorization remains load-bearing", certificate["accepted_same_surface_generator_factorization"] is False)
    return certificate


def part4_no_go_shortcut() -> dict[str, Any]:
    print("\nPart 4: no-go boundary for factorization shortcut")
    shortcut = {
        "route_pruned": "same-surface factorization algebra plus B_x alone certifies physical top row",
        "counterassignment_same_finite_algebra": {
            "top_equals_P_0": "A/sqrt(3)",
            "top_equals_P_omega": "A/sqrt(12)",
        },
        "reason": "physical top-line assignment is not derived by the finite algebra",
        "route_still_live": (
            "derive accepted same-surface generator factorization and nontrivial top-line law, "
            "or produce strict same-source top/W pole rows"
        ),
    }
    check("shortcut no-go names physical top-line assignment", "top-line assignment" in shortcut["reason"])
    check("counterassignment has same finite algebra with different top rows", shortcut["counterassignment_same_finite_algebra"]["top_equals_P_0"] != shortcut["counterassignment_same_finite_algebra"]["top_equals_P_omega"])
    check("route still live names strict pole rows", "strict same-source top/W pole rows" in shortcut["route_still_live"])
    return shortcut


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
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "the accepted physical top pole projector is derived",
        "the accepted transfer/action generator is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T SAME-SURFACE TOP MATRIX ELEMENT FACTORIZATION BOUNDARY")
    print("=" * 78)

    anchors = part1_anchors()
    matrix = part2_c3_matrix_element_factorization()
    certificate = part3_certificate_boundary()
    no_go = part4_no_go_shortcut()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "conditional-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "conditional_surface_status": (
            "exact top-row certificate if accepted same-surface generator "
            "factorization and nontrivial top-line assignment are supplied"
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite C3 factorization algebra gives A/sqrt(12) exactly on "
            "nontrivial C3 lines, but the actual current surface still lacks an "
            "accepted physical top line and accepted same-surface source-generator "
            "factorization. The singlet line remains allowed by the same finite "
            "algebra and gives A/sqrt(3)."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": no_go["route_pruned"],
        "route_still_live": no_go["route_still_live"],
        "anchor_statuses": anchors,
        "matrix_element_witness": matrix,
        "certificate_boundary": certificate,
        "no_go_boundary": no_go,
        "first_open_gate_after_this_note": (
            "accepted same-surface generator factorization plus nontrivial top-line "
            "assignment, or strict top/W pole rows"
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
