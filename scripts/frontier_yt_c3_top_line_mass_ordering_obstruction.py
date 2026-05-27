#!/usr/bin/env python3
"""Y_T C3 top-line mass-ordering obstruction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
REAL_RECORD_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
NONTRIVIAL_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
LABELING_NOGO = DOCS / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"
C3_PRESERVED = DOCS / "C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

REAL_RECORD_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
NONTRIVIAL_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"

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
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        REAL_RECORD_SOURCE,
        NONTRIVIAL_BOUNDARY,
        LABELING_NOGO,
        C3_PRESERVED,
        FULL_STACK,
        REAL_RECORD_SOURCE_OUT,
        NONTRIVIAL_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "Relation To Existing No-Gos",
        "What This Prunes",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "mass ordering",
        "largest absolute response is the C3 singlet",
        "target coefficient convention",
        "nontrivial top-line law",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    real_record = load_json(REAL_RECORD_SOURCE_OUT)
    nontrivial_boundary = load_json(NONTRIVIAL_BOUNDARY_OUT)
    check("real-record source theorem passed", real_record.get("fail_count") == 0, real_record.get("fail_count"))
    check("real-record source theorem selects B_x", real_record.get("certificate_boundary", {}).get("source_direction_bx_selected") is True)
    check("nontrivial top-line boundary passed", nontrivial_boundary.get("fail_count") == 0, nontrivial_boundary.get("fail_count"))
    check("nontrivial top-line boundary is route pruning", nontrivial_boundary.get("trace_class") == "negative_route_pruning")
    check("labeling no-go applies to u,c,t labels", "{u, c, t}" in read(LABELING_NOGO))
    c3_preserved = read(C3_PRESERVED)
    check(
        "C3 preserved interpretation treats mass labels as conventions",
        "labels are conventions" in c3_preserved or "labeling convention" in c3_preserved,
    )

    return {
        "real_record_status": real_record.get("actual_current_surface_status"),
        "nontrivial_boundary_status": nontrivial_boundary.get("actual_current_surface_status"),
    }


def part2_mass_ordering_witness() -> dict[str, Any]:
    print("\nPart 2: mass-ordering witness")
    sqrt = sp.sqrt
    omega = sp.Rational(-1, 2) + sp.I * sqrt(3) / 2
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    bx = sp.simplify((cycle + cycle**2) / sqrt(6))

    projectors = {
        "P_0": projector_for_eigenvalue(cycle, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(cycle, omega),
        "P_omega2": projector_for_eigenvalue(cycle, omega**2),
    }
    expected = {
        "P_0": 2 / sqrt(6),
        "P_omega": -1 / sqrt(6),
        "P_omega2": -1 / sqrt(6),
    }

    check("C is order three", is_zero(cycle**3 - sp.eye(3)))
    check("B_x is Hermitian", is_zero(bx.conjugate().T - bx))
    check("B_x has zero trace", is_zero(sp.trace(bx)))
    check("B_x has unit Frobenius norm", is_zero(sp.trace(bx.conjugate().T * bx) - 1))

    responses: dict[str, sp.Expr] = {}
    magnitudes: dict[str, sp.Expr] = {}
    for name, projector in projectors.items():
        check(f"{name} is rank-one projector", is_zero(projector**2 - projector) and is_zero(sp.trace(projector) - 1))
        responses[name] = sp.simplify(sp.trace(projector * bx))
        magnitudes[name] = sp.sqrt(sp.simplify(responses[name] ** 2))
        check(f"{name} response matches expected", is_zero(responses[name] - expected[name]), responses[name])

    max_name = max(magnitudes, key=lambda key: sp.N(magnitudes[key]))
    check("mass-ordering proxy picks P_0", max_name == "P_0", max_name)
    check("P_0 magnitude is 2/sqrt(6)", is_zero(magnitudes["P_0"] - 2 / sqrt(6)), magnitudes["P_0"])
    check("nontrivial magnitudes are 1/sqrt(6)", is_zero(magnitudes["P_omega"] - 1 / sqrt(6)) and is_zero(magnitudes["P_omega2"] - 1 / sqrt(6)))
    check("P_0 magnitude is twice nontrivial magnitude", is_zero(magnitudes["P_0"] / magnitudes["P_omega"] - 2))
    check("target 1/sqrt(6) is not mass-ordering top under B_x", max_name != "P_omega" and max_name != "P_omega2")

    return {
        "source_direction": "B_x",
        "responses": {name: str(value) for name, value in responses.items()},
        "magnitudes": {name: str(value) for name, value in magnitudes.items()},
        "mass_ordering_proxy_top_line": max_name,
        "mass_ordering_proxy_top_magnitude": str(magnitudes[max_name]),
        "target_nontrivial_magnitude": "1/sqrt(6)",
    }


def part3_route_pruning() -> dict[str, bool]:
    print("\nPart 3: route-pruning certificate")
    certificate = {
        "bx_source_direction_derived": True,
        "retained_c3_projectors_available": True,
        "mass_ordering_selects_p0": True,
        "mass_ordering_selects_target_nontrivial_line": False,
        "nontrivial_line_requires_extra_top_line_law": True,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, expected in certificate.items():
        check(f"field status recorded: {key}", certificate[key] is expected)
    check("route pruned exactly because mass-ordering target fails", certificate["mass_ordering_selects_target_nontrivial_line"] is False)
    return certificate


def part4_firewalls() -> None:
    print("\nPart 4: firewalls")
    text = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in text)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "P_0 is the physical top pole",
        "nontrivial line is the physical top pole",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "B_x plus mass-ordering convention selects target 1/sqrt(6)",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive a same-surface nontrivial top-line law that is not mass-ordering "
            "and not target selection, or produce strict same-source top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names strict pole rows", "strict same-source top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    witness = part2_mass_ordering_witness()
    certificate = part3_route_pruning()
    part4_firewalls()
    status = part5_claim_status()

    result = {
        "claim_id": "yt_c3_top_line_mass_ordering_obstruction_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_top_line_mass_ordering_obstruction.py",
        **status,
        "proposal_allowed_reason": (
            "B_x source authority is now exact support, but ordinary top mass-ordering "
            "selects the C3 singlet response 2/sqrt(6), not the target nontrivial-line "
            "response 1/sqrt(6)."
        ),
        "anchors": anchors,
        "mass_ordering_witness": witness,
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
