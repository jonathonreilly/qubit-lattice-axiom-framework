#!/usr/bin/env python3
"""Y_T C3 spectral top-projector route support.

This runner checks that the top-sector corner-label obstruction should not be
overread: C3-preserving nondegenerate circulant dynamics can supply spectral
projectors. The route remains support-only because the physical operator,
ordering, and source-generator matrix elements are not derived.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"

NOTE = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
TOP_PROJECTOR_OBSTRUCTION = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
MIN_BREAKING = DOCS / "GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING_NARROW_THEOREM_NOTE_2026-05-23.md"
ORIENTATION_C3 = DOCS / "POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md"
QUARK_C3_BOUNDARY = DOCS / "QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

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
        TOP_PROJECTOR_OBSTRUCTION,
        MIN_BREAKING,
        ORIENTATION_C3,
        QUARK_C3_BOUNDARY,
        FULL_STACK,
        TOP_PROJECTOR_OBSTRUCTION_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Algebra",
        "What This Repairs",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "not killed by the corner-label no-go",
        "mass-eigenline route, not a corner-label route",
        "accepted_c3_circulant_generation_operator",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    obstruction = load_json(TOP_PROJECTOR_OBSTRUCTION_OUT)
    check("top-sector obstruction passed", obstruction.get("fail_count") == 0, obstruction.get("fail_count"))
    check("top-sector obstruction is scoped to corner-label route", "corner" in read(TOP_PROJECTOR_OBSTRUCTION).lower())
    min_breaking_text = read(MIN_BREAKING)
    check(
        "minimal-breaking note says C3 generic spectra are distinct",
        "Generic spectrum" in min_breaking_text
        and "C_3" in min_breaking_text
        and "3 distinct" in min_breaking_text,
    )
    check("orientation note says C3 lifts generation degeneracy", "lifts the generation mass degeneracy" in read(ORIENTATION_C3))
    check("quark C3 boundary says C3 circulants are carriers, not source laws", "carrier, not a source law" in read(QUARK_C3_BOUNDARY))
    return {"top_projector_obstruction": obstruction}


def part2_c3_spectral_projectors() -> dict[str, Any]:
    print("\nPart 2: C3 spectral projector algebra")
    I = sp.I
    omega = sp.Rational(-1, 2) + sp.sqrt(3) * I / 2
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    a, x, y = sp.symbols("a x y", real=True)
    q = x + I * y
    qbar = x - I * y
    H = a * sp.eye(3) + q * C + qbar * C**2
    H = sp.simplify(H)
    check("C has order three", is_zero(C**3 - sp.eye(3)))
    check("H commutes with C", is_zero(H * C - C * H))
    check("H is Hermitian for real a,r,theta", is_zero(H - H.conjugate().T))

    projectors: list[sp.Matrix] = []
    eigenvalues: list[sp.Expr] = []
    for k in range(3):
        # Projector onto the C eigenvalue omega^k line.
        P = sp.simplify((sp.eye(3) + omega ** (-k) * C + omega ** (-2 * k) * C**2) / 3)
        projectors.append(P)
        lam = sp.simplify(a + q * omega**k + qbar * omega ** (2 * k))
        eigenvalues.append(lam)
        check(f"P{k} is idempotent", is_zero(P * P - P))
        check(f"P{k} has trace one", is_zero(sp.trace(P) - 1), sp.trace(P))
        check(f"P{k} commutes with C", is_zero(P * C - C * P))
        check(f"P{k} is H spectral projector", is_zero(H * P - lam * P))

    check("spectral projectors resolve identity", is_zero(sum(projectors, sp.zeros(3)) - sp.eye(3)))
    check("generic eigenvalue expressions are not all equal", len(set(map(sp.sstr, eigenvalues))) == 3, eigenvalues)

    numeric_values = [sp.N(lam.subs({a: 1, x: sp.Rational(1, 5), y: sp.Rational(1, 7)}), 16) for lam in eigenvalues]
    check("sample C3 circulant has three distinct eigenvalues", len({str(value) for value in numeric_values}) == 3, numeric_values)

    return {
        "eigenvalues": [sp.sstr(sp.simplify(lam)) for lam in eigenvalues],
        "sample_eigenvalues": [str(value) for value in numeric_values],
        "conclusion": "C3-preserving nondegenerate spectral projectors are algebraically available",
    }


def part3_certificate_boundary() -> dict[str, Any]:
    print("\nPart 3: certificate boundary")
    fields = {
        "accepted_c3_circulant_generation_operator": False,
        "operator_derived_on_same_surface": False,
        "nondegenerate_eigenvalues": True,
        "top_line_ordering_derived": False,
        "top_projector_is_spectral_projector": True,
        "source_generator_matrix_element_derived": False,
        "same_surface_w_projector_and_response": False,
        "contact_subtraction_done": False,
        "fv_ir_controls_pass": False,
        "same_model_class": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    positive = all(fields.values())
    check("support route is not a positive YT certificate", positive is False)
    check("operator/source matrix elements are the load-bearing missing parts", fields["operator_derived_on_same_surface"] is False and fields["source_generator_matrix_element_derived"] is False)
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
        "physical top projector is derived",
        "accepted operator is derived",
        "source-generator matrix element is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "exact-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite C3 spectral algebra supplies a live projector route, "
            "but the accepted same-surface dynamics, eigenvalue ordering, and "
            "source-generator matrix elements are not derived."
        ),
        "bare_retained_allowed": False,
        "route_supported": (
            "C3-preserving nondegenerate spectral projector route to top pole"
        ),
        "route_still_open": (
            "derive accepted C3 circulant generation operator and top-line "
            "source response, or produce strict pole-row evidence"
        ),
    }
    check("actual status is exact-support", status["actual_current_surface_status"] == "exact-support")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("supported route is C3-preserving", "C3-preserving" in status["route_supported"])
    return status


def main() -> int:
    anchors = part1_anchors()
    spectral = part2_c3_spectral_projectors()
    fields = part3_certificate_boundary()
    part4_firewalls()
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_c3_spectral_top_projector_route_support_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_spectral_top_projector_route_support.py",
        "anchors": anchors,
        "c3_spectral_projectors": spectral,
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
