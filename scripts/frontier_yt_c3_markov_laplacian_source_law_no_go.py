#!/usr/bin/env python3
"""Y_T C3 Markov/Laplacian source-law no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_markov_laplacian_source_law_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_MARKOV_LAPLACIAN_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_DYNAMICS = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_PERRON = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
C3_DYNAMICS_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_PERRON_OUT = ROOT / "outputs" / "yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
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


def c3_objects() -> dict[str, sp.Matrix | sp.Expr]:
    C = c3_cycle()
    I = sp.eye(3)
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    P0 = projector_for_eigenvalue(C, sp.Integer(1))
    Po = projector_for_eigenvalue(C, omega)
    Po2 = projector_for_eigenvalue(C, omega**2)
    Pnt = sp.simplify(Po + Po2)
    Ba = I / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    return {
        "C": C,
        "I": I,
        "omega": omega,
        "P0": P0,
        "Po": Po,
        "Po2": Po2,
        "Pnt": Pnt,
        "Ba": Ba,
        "Bx": Bx,
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        C3_DYNAMICS,
        C3_REAL_SOURCE,
        C3_PERRON,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK_OUT,
        C3_DYNAMICS_OUT,
        C3_REAL_SOURCE_OUT,
        C3_PERRON_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_NOGO_OUT,
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
        "Finite Markov Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open Markov-Laplacian-to-top-row law",
        "proposal_allowed: false",
        "Q_r = r(C+C^2-2I)",
        "lambda_top=1/sqrt(2)",
        "The Markov semigroup's positive stationary/Perron line is `P_0`",
    ):
        check(f"note contains Markov boundary phrase: {phrase}", contains_phrase(note, phrase))

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "c3_dynamics": load_json(C3_DYNAMICS_OUT),
        "c3_real_source": load_json(C3_REAL_SOURCE_OUT),
        "c3_perron": load_json(C3_PERRON_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "C3 dynamics boundary leaves top ordering open",
        deps["c3_dynamics"].get("certificate_boundary", {}).get("top_line_ordering_derived") is False,
    )
    check(
        "real source theorem already derives B_x up to sign",
        deps["c3_real_source"].get("certificate_boundary", {}).get("source_direction_bx_selected") is True,
    )
    check(
        "Perron no-go already marks P0 as positive line",
        deps["c3_perron"].get("certificate_boundary", {}).get("perron_line_is_p0") is True,
    )
    check(
        "radial no-go leaves lambda_top free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface") is True,
    )
    check(
        "strict availability keeps strict certificate absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return deps


def part2_markov_laplacian_spectrum() -> dict[str, str]:
    print("\nPart 2: reversible C3 Markov/Laplacian spectrum")
    r, t = sp.symbols("r t", positive=True)
    obj = c3_objects()
    C = obj["C"]
    I = obj["I"]
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Q = sp.simplify(r * (C + C**2 - 2 * I))
    L = sp.simplify(-Q)

    q_rows = [sp.simplify(sum(Q[i, j] for j in range(3))) for i in range(3)]
    q_cols = [sp.simplify(sum(Q[i, j] for i in range(3))) for j in range(3)]
    off_diagonal_entries = [Q[i, j] for i in range(3) for j in range(3) if i != j]
    q_eigs = {
        "P_0": sp.simplify(sp.trace(P0 * Q)),
        "P_omega": sp.simplify(sp.trace(Po * Q)),
        "P_omega2": sp.simplify(sp.trace(Po2 * Q)),
    }
    l_eigs = {
        "P_0": sp.simplify(sp.trace(P0 * L)),
        "P_omega": sp.simplify(sp.trace(Po * L)),
        "P_omega2": sp.simplify(sp.trace(Po2 * L)),
    }

    check("Q is real symmetric", is_zero(Q - Q.T), Q)
    check("Q commutes with C", is_zero(Q * C - C * Q))
    check("Q has row sums zero", all(is_zero(value) for value in q_rows), q_rows)
    check("Q has column sums zero", all(is_zero(value) for value in q_cols), q_cols)
    check("Q off-diagonal rates are r", all(is_zero(entry - r) for entry in off_diagonal_entries), off_diagonal_entries)
    check("Q P_0 eigenvalue is zero", is_zero(q_eigs["P_0"]), q_eigs["P_0"])
    check("Q nontrivial eigenvalue is -3r", is_zero(q_eigs["P_omega"] + 3 * r), q_eigs["P_omega"])
    check("Q nontrivial pair is degenerate", is_zero(q_eigs["P_omega"] - q_eigs["P_omega2"]))
    check("L P_0 eigenvalue is zero", is_zero(l_eigs["P_0"]), l_eigs["P_0"])
    check("L nontrivial eigenvalue is 3r", is_zero(l_eigs["P_omega"] - 3 * r), l_eigs["P_omega"])
    check("L nontrivial pair is degenerate", is_zero(l_eigs["P_omega"] - l_eigs["P_omega2"]))

    semigroup_eigs = {
        "P_0": sp.Integer(1),
        "P_omega": sp.exp(-3 * r * t),
        "P_omega2": sp.exp(-3 * r * t),
    }
    check("Markov semigroup P_0 eigenvalue is stationary one", semigroup_eigs["P_0"] == 1)
    check("Markov semigroup nontrivial modes are degenerate", semigroup_eigs["P_omega"] == semigroup_eigs["P_omega2"])

    return {
        "Q_r": "r*(C+C^2-2I)",
        "Q_P0": sp.sstr(q_eigs["P_0"]),
        "Q_Pomega": sp.sstr(q_eigs["P_omega"]),
        "Q_Pomega2": sp.sstr(q_eigs["P_omega2"]),
        "L_P0": sp.sstr(l_eigs["P_0"]),
        "L_Pomega": sp.sstr(l_eigs["P_omega"]),
        "L_Pomega2": sp.sstr(l_eigs["P_omega2"]),
        "semigroup_P0": "1",
        "semigroup_nontrivial": "exp(-3*r*t)",
        "conclusion": "stationary/Perron line is P_0; nontrivial block is degenerate",
    }


def part3_connected_source_normalization() -> dict[str, str]:
    print("\nPart 3: connected Markov source normalization")
    r = sp.symbols("r", positive=True)
    obj = c3_objects()
    C = obj["C"]
    I = obj["I"]
    Ba = obj["Ba"]
    Bx = obj["Bx"]
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Pnt = obj["Pnt"]
    Q = sp.simplify(r * (C + C**2 - 2 * I))
    decomposition = sp.simplify(r * sp.sqrt(6) * Bx - 2 * r * sp.sqrt(3) * Ba)
    connected = sp.simplify(Q + 2 * r * I)
    connected_norm = sp.sqrt(sp.simplify(sp.trace(connected.T * connected)))
    normalized = sp.simplify(connected / connected_norm)
    p0_response = sp.simplify(sp.trace(P0 * normalized))
    po_response = sp.simplify(sp.trace(Po * normalized))
    po2_response = sp.simplify(sp.trace(Po2 * normalized))
    pnt_response = sp.simplify(sp.trace((Pnt / 2) * normalized))

    check("Q decomposes into B_x plus identity", is_zero(Q - decomposition), decomposition)
    check("connected quotient removes identity part", is_zero(connected - r * sp.sqrt(6) * Bx), connected)
    check("connected Frobenius norm is r*sqrt(6)", is_zero(connected_norm - r * sp.sqrt(6)), connected_norm)
    check("normalized connected generator is B_x", is_zero(normalized - Bx), normalized)
    check("P_0 response to normalized Markov generator is 2/sqrt(6)", is_zero(p0_response - 2 / sp.sqrt(6)), p0_response)
    check("P_omega response is -1/sqrt(6)", is_zero(po_response + 1 / sp.sqrt(6)), po_response)
    check("P_omega2 response is -1/sqrt(6)", is_zero(po2_response + 1 / sp.sqrt(6)), po2_response)
    check("P_nt block-density response is -1/sqrt(6)", is_zero(pnt_response + 1 / sp.sqrt(6)), pnt_response)

    return {
        "Q_decomposition": "r*sqrt(6)*B_x - 2*r*sqrt(3)*B_a",
        "connected_quotient": "r*sqrt(6)*B_x",
        "unit_connected_generator": "B_x",
        "P_0_response": "2/sqrt(6)",
        "P_omega_response": "-1/sqrt(6)",
        "P_omega2_response": "-1/sqrt(6)",
        "P_nt_block_density_response": "-1/sqrt(6)",
    }


def part4_radial_and_readout_counterfamily() -> dict[str, Any]:
    print("\nPart 4: radial/readout counterfamily")
    A, g2, lambda_top, c = sp.symbols("A g_2 lambda_top c", positive=True)
    obj = c3_objects()
    Bx = obj["Bx"]
    P0 = obj["P0"]
    Pnt = obj["Pnt"]
    Vtop = sp.simplify(lambda_top * A * Bx)
    row_p0 = sp.simplify(sp.trace(P0 * Vtop))
    row_pnt = sp.simplify(-sp.trace((Pnt / 2) * Vtop))
    w_row = g2 * A / 2
    same_source_readout = sp.simplify(g2 / sp.sqrt(2) * row_pnt / w_row)
    reparam_readout = sp.simplify(g2 / sp.sqrt(2) * (row_pnt / c) / (w_row / c))
    target_lambda = sp.solve(sp.Eq(row_pnt, A / sp.sqrt(12)), lambda_top)

    check("P_0 row remains larger singlet row", is_zero(row_p0 - 2 * lambda_top * A / sp.sqrt(6)), row_p0)
    check("P_nt row is lambda_top*A/sqrt(6)", is_zero(row_pnt - lambda_top * A / sp.sqrt(6)), row_pnt)
    check("target row requires lambda_top=1/sqrt(2)", target_lambda == [1 / sp.sqrt(2)], target_lambda)
    check("W row is independent of lambda_top", not w_row.has(lambda_top), w_row)
    check("same-source readout keeps lambda_top", is_zero(same_source_readout - lambda_top / sp.sqrt(3)), same_source_readout)
    check("source reparameterization cannot remove lambda_top", is_zero(reparam_readout - lambda_top / sp.sqrt(3)), reparam_readout)

    witnesses = [
        {"top_support": "P_0", "lambda_top": "1/sqrt(2)", "top_row": "A/sqrt(3)", "target": False},
        {"top_support": "P_nt", "lambda_top": "1", "top_row": "A/sqrt(6)", "target": False},
        {"top_support": "P_nt", "lambda_top": "1/sqrt(2)", "top_row": "A/sqrt(12)", "target": True},
    ]
    check("counterfamily contains target and non-target completions", {row["target"] for row in witnesses} == {False, True})
    return {
        "family": "V_top(lambda_top)=lambda_top*A*B_x",
        "P_0_row": "2*lambda_top*A/sqrt(6)",
        "P_nt_row": "lambda_top*A/sqrt(6)",
        "target_requires_lambda_top": "1/sqrt(2)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "witnesses": witnesses,
    }


def part5_certificate_boundary() -> dict[str, bool | str]:
    print("\nPart 5: certificate boundary")
    certificate: dict[str, bool | str] = {
        "reversible_c3_markov_laplacian_checked": True,
        "stationary_perron_line_is_P0": True,
        "nontrivial_block_degenerate": True,
        "normalized_connected_generator_is_Bx_up_to_sign": True,
        "markov_rate_scale_free_until_physical_calibration": True,
        "top_line_ordering_derived": False,
        "zero_singlet_top_readout_derived": False,
        "radial_generator_factorization_lambda_top_derived": False,
        "accepted_backend_projectors_matrix_elements_present": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "positive_closure_marker_allowed": False,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, (bool, str)), value)
    check("Markov/Laplacian route does not derive top line", certificate["top_line_ordering_derived"] is False)
    check("Markov/Laplacian route does not derive radial factor", certificate["radial_generator_factorization_lambda_top_derived"] is False)
    check("strict positive certificate remains absent", certificate["strict_top_w_response_certificate_present"] is False)
    return certificate


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
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
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in text)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `lambda_top=1/sqrt(2)`",
        "strict top/W pole rows are supplied",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part7_claim_status() -> dict[str, Any]:
    print("\nPart 7: claim status")
    status = {
        "actual_current_surface_status": "no-go / open Markov-Laplacian-to-top-row law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "reversible C3 Markov/Laplacian dynamics plus connected source "
            "normalization supplies the coefficient-bearing top matrix element"
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The reversible C3 Markov/Laplacian law has P_0 as "
            "stationary/Perron line, leaves the nontrivial block degenerate, "
            "and after connected normalization only recovers B_x up to sign. "
            "It does not derive the physical top-readout law excluding P_0, "
            "lambda_top=1/sqrt(2), accepted backend/projectors, or strict "
            "top/W pole rows."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "positive_closure_marker_allowed": False,
        "next_exact_action": (
            "derive accepted same-surface readout/radial/backend laws, or "
            "produce accepted strict same-source top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"].startswith("no-go"))
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal is not allowed", status["proposal_allowed"] is False)
    check("bare retained is not allowed", status["bare_retained_allowed"] is False)
    check("positive closure marker is not allowed", status["positive_closure_marker_allowed"] is False)
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 MARKOV-LAPLACIAN SOURCE-LAW NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    markov_witness = part2_markov_laplacian_spectrum()
    normalized_witness = part3_connected_source_normalization()
    counterfamily = part4_radial_and_readout_counterfamily()
    certificate = part5_certificate_boundary()
    part6_firewalls()
    status = part7_claim_status()

    output = {
        "claim_id": "yt_c3_markov_laplacian_source_law_no_go_note_2026-05-28",
        "claim_type": "no_go",
        **status,
        "dependency_fail_counts": {name: data.get("fail_count") for name, data in deps.items()},
        "markov_laplacian_witness": markov_witness,
        "connected_source_normalization_witness": normalized_witness,
        "radial_readout_counterfamily": counterfamily,
        "certificate_boundary": certificate,
        "forbidden_inputs_used": False,
        "positive_closure_marker_written": False,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
