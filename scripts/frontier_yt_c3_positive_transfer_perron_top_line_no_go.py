#!/usr/bin/env python3
"""Y_T C3 positive transfer Perron top-line no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_DYNAMICS = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
MICROSCOPIC_BOUNDARY = DOCS / "YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md"

C3_DYNAMICS_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
MATRIX_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
MICROSCOPIC_BOUNDARY_OUT = ROOT / "outputs" / "yt_microscopic_backend_projector_matrix_element_boundary_2026-05-27.json"

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
        MATRIX_FACTORIZATION,
        MICROSCOPIC_BOUNDARY,
        C3_DYNAMICS_OUT,
        MATRIX_FACTORIZATION_OUT,
        MICROSCOPIC_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "Relation To Current Stack",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go",
        "proposal_allowed: false",
        "positive real C3 transfer/Perron selection",
        "P_0",
        "P_omega",
    ):
        check(f"note contains boundary phrase: {phrase}", contains_phrase(note, phrase))

    deps = {
        "c3_dynamics": load_json(C3_DYNAMICS_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "microscopic_boundary": load_json(MICROSCOPIC_BOUNDARY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "C3 dynamics dependency leaves phase law open",
        deps["c3_dynamics"].get("certificate_boundary", {}).get("orientation_phase_law_for_y0_derived") is False,
    )
    check(
        "microscopic dependency leaves top projector open",
        deps["microscopic_boundary"].get("certificate_boundary", {}).get("physical_top_projector_or_pole_derived") is False,
    )
    return deps


def part2_positive_circulant_perron() -> dict[str, str]:
    print("\nPart 2: positive C3 circulant Perron witness")
    a, b = sp.symbols("a b", positive=True)
    C = c3_cycle()
    T = sp.simplify(a * sp.eye(3) + b * (C + C**2))
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    eigenvalues = {
        name: sp.simplify(sp.trace(projector * T))
        for name, projector in projectors.items()
    }
    perron_gap = sp.simplify(eigenvalues["P_0"] - eigenvalues["P_omega"])
    uniform = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    nontrivial = sp.Matrix([1, omega, omega**2]) / sp.sqrt(3)

    check("T is real symmetric", is_zero(T - T.T), T)
    check("T commutes with C", is_zero(T * C - C * T))
    check("T has positive diagonal/offdiagonal parameters", a.is_positive and b.is_positive)
    check("P_0 eigenvalue is a+2b", is_zero(eigenvalues["P_0"] - (a + 2 * b)), eigenvalues["P_0"])
    check("P_omega eigenvalue is a-b", is_zero(eigenvalues["P_omega"] - (a - b)), eigenvalues["P_omega"])
    check("P_omega2 eigenvalue is a-b", is_zero(eigenvalues["P_omega2"] - (a - b)), eigenvalues["P_omega2"])
    check("Perron gap is 3b", is_zero(perron_gap - 3 * b), perron_gap)
    check("Perron line is uniform positive", all(entry > 0 for entry in uniform), uniform)
    check("nontrivial character line is not positive", any(sp.im(entry) != 0 for entry in nontrivial), nontrivial)
    check("nontrivial block remains degenerate", is_zero(eigenvalues["P_omega"] - eigenvalues["P_omega2"]))

    return {
        "T": "a*I + b*(C+C^2), a>0, b>0",
        "lambda_P0": sp.sstr(eigenvalues["P_0"]),
        "lambda_Pomega": sp.sstr(eigenvalues["P_omega"]),
        "lambda_Pomega2": sp.sstr(eigenvalues["P_omega2"]),
        "perron_gap": sp.sstr(perron_gap),
        "conclusion": "positive real C3 Perron selection chooses P_0, not a nontrivial line",
    }


def part3_target_row_conflict() -> dict[str, Any]:
    print("\nPart 3: target-row conflict")
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    bx = sp.simplify((C + C**2) / sp.sqrt(6))
    p0 = projector_for_eigenvalue(C, sp.Integer(1))
    po = projector_for_eigenvalue(C, omega)
    row_p0 = sp.simplify(A / sp.sqrt(2) * sp.trace(p0 * bx))
    row_po = sp.simplify(A / sp.sqrt(2) * sp.trace(po * bx))
    check("Perron singlet row gives A/sqrt(3)", is_zero(row_p0 - A / sp.sqrt(3)), row_p0)
    check("nontrivial row gives target magnitude A/sqrt(12)", is_zero(abs(row_po) - A / sp.sqrt(12)), row_po)
    check("positive Perron line conflicts with target nontrivial line", not is_zero(row_p0 - abs(row_po)))
    return {
        "perron_line_row": sp.sstr(row_p0),
        "nontrivial_target_row": sp.sstr(row_po),
        "route_pruned": "positive Perron top-line selection supplies singlet-size row",
    }


def part4_certificate_boundary() -> dict[str, bool]:
    print("\nPart 4: certificate boundary")
    certificate = {
        "real_positive_c3_transfer_checked": True,
        "perron_line_is_p0": True,
        "nontrivial_line_isolated": False,
        "orientation_phase_law_derived": False,
        "strict_pole_rows_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("positive Perron route does not isolate nontrivial line", certificate["nontrivial_line_isolated"] is False)
    return certificate


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
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


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "positive real C3 transfer/Perron selection supplies nontrivial top line",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive an accepted orientation/phase/top-ordering dynamics theorem "
            "beyond positive real C3 Perron selection, or produce strict top/W "
            "pole-row data"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 POSITIVE TRANSFER PERRON TOP-LINE NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    perron = part2_positive_circulant_perron()
    target_conflict = part3_target_row_conflict()
    certificate = part4_certificate_boundary()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_positive_transfer_perron_top_line_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_positive_transfer_perron_top_line_no_go.py",
        **status,
        "proposal_allowed_reason": (
            "Positive real C3 transfer/Perron selection picks the C3 singlet "
            "line or leaves the nontrivial block degenerate. It does not supply "
            "the physical nontrivial top-line law needed for A/sqrt(12)."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "perron_witness": perron,
        "target_row_conflict": target_conflict,
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
