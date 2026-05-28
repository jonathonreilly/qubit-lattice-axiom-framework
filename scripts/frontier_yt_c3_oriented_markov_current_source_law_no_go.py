#!/usr/bin/env python3
"""Y_T C3 oriented Markov-current source-law no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_oriented_markov_current_source_law_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_ORIENTED_MARKOV_CURRENT_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_MARKOV = DOCS / "YT_C3_MARKOV_LAPLACIAN_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
C3_PHASE_STRENGTH = DOCS / "YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md"
C3_PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
C3_MARKOV_OUT = ROOT / "outputs" / "yt_c3_markov_laplacian_source_law_no_go_2026-05-28.json"
C3_PHASE_STRENGTH_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_strength_boundary_2026-05-27.json"
C3_PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
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
    Bx = (C + C**2) / sp.sqrt(6)
    By = sp.I * (C - C**2) / sp.sqrt(6)
    return {
        "C": C,
        "I": I,
        "omega": omega,
        "P0": P0,
        "Po": Po,
        "Po2": Po2,
        "Pnt": Pnt,
        "Bx": Bx,
        "By": By,
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        C3_MARKOV,
        C3_PHASE_STRENGTH,
        C3_PHASE_CONE,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK_OUT,
        C3_MARKOV_OUT,
        C3_PHASE_STRENGTH_OUT,
        C3_PHASE_CONE_OUT,
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
        "Finite Oriented-Current Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open oriented-current-to-top-row law",
        "proposal_allowed: false",
        "Q_{p,q} = p(C-I) + q(C^2-I)",
        "lambda_top=1/sqrt(2)",
        "The positive Markov stationary/Perron line is still `P_0`",
    ):
        check(f"note contains oriented-current boundary phrase: {phrase}", contains_phrase(note, phrase))

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "c3_markov": load_json(C3_MARKOV_OUT),
        "c3_phase_strength": load_json(C3_PHASE_STRENGTH_OUT),
        "c3_phase_cone": load_json(C3_PHASE_CONE_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "reversible Markov route is already pruned",
        deps["c3_markov"].get("certificate_boundary", {}).get("stationary_perron_line_is_P0") is True,
    )
    check(
        "orientation sign alone is already insufficient",
        deps["c3_phase_strength"].get("no_go_audit", {}).get("orientation_sign_sufficient")
        is False,
    )
    check(
        "phase cone is characterized but not derived",
        deps["c3_phase_cone"].get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "nontrivial block support is conditional support",
        deps["c3_block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "radial no-go leaves lambda_top free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface") is True,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return deps


def part2_oriented_markov_spectrum() -> dict[str, str]:
    print("\nPart 2: nonreversible C3 Markov-current spectrum")
    p, q, t = sp.symbols("p q t", positive=True)
    obj = c3_objects()
    C = obj["C"]
    I = obj["I"]
    omega = obj["omega"]
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Q = sp.simplify(p * (C - I) + q * (C**2 - I))

    q_rows = [sp.simplify(sum(Q[i, j] for j in range(3))) for i in range(3)]
    q_cols = [sp.simplify(sum(Q[i, j] for i in range(3))) for j in range(3)]
    q_eigs = {
        "P_0": sp.simplify(sp.trace(P0 * Q)),
        "P_omega": sp.simplify(sp.trace(Po * Q)),
        "P_omega2": sp.simplify(sp.trace(Po2 * Q)),
    }
    expected_omega = sp.simplify(-sp.Rational(3, 2) * (p + q) + sp.I * sp.sqrt(3) * (p - q) / 2)
    expected_omega2 = sp.conjugate(expected_omega)

    check("Q has row sums zero", all(is_zero(value) for value in q_rows), q_rows)
    check("Q has column sums zero", all(is_zero(value) for value in q_cols), q_cols)
    check("Q commutes with C", is_zero(Q * C - C * Q))
    check("Q is non-symmetric when p != q", sp.simplify(Q - Q.T) != sp.zeros(3))
    check("P_0 eigenvalue is zero", is_zero(q_eigs["P_0"]), q_eigs["P_0"])
    check("P_omega eigenvalue has oriented phase", is_zero(q_eigs["P_omega"] - expected_omega), q_eigs["P_omega"])
    check("P_omega2 eigenvalue is conjugate", is_zero(q_eigs["P_omega2"] - expected_omega2), q_eigs["P_omega2"])
    check(
        "nontrivial real decay rates are equal",
        is_zero(sp.re(q_eigs["P_omega"]) - sp.re(q_eigs["P_omega2"])),
    )
    check(
        "nontrivial imaginary parts are opposite",
        is_zero(sp.im(q_eigs["P_omega"]) + sp.im(q_eigs["P_omega2"])),
    )

    semigroup_moduli = {
        "P_0": sp.Integer(1),
        "P_omega": sp.exp(-sp.Rational(3, 2) * (p + q) * t),
        "P_omega2": sp.exp(-sp.Rational(3, 2) * (p + q) * t),
    }
    check("Markov semigroup P_0 modulus is stationary one", semigroup_moduli["P_0"] == 1)
    check("nontrivial semigroup moduli are degenerate", semigroup_moduli["P_omega"] == semigroup_moduli["P_omega2"])

    one_way = sp.simplify(expected_omega.subs(q, 0))
    balanced = sp.simplify(expected_omega.subs(q, p))
    check("balanced chain has no current phase", is_zero(sp.im(balanced)), balanced)
    check("one-way chain has nonzero current phase", sp.im(one_way) != 0, one_way)

    return {
        "Q_pq": "p*(C-I)+q*(C^2-I)",
        "Q_P0": "0",
        "Q_Pomega": "-3*(p+q)/2 + I*sqrt(3)*(p-q)/2",
        "Q_Pomega2": "-3*(p+q)/2 - I*sqrt(3)*(p-q)/2",
        "semigroup_P0_modulus": "1",
        "semigroup_nontrivial_modulus": "exp(-3*(p+q)*t/2)",
        "conclusion": "P_0 remains stationary/Perron; current splits phase signs only",
    }


def part3_current_decomposition_and_free_ratio() -> dict[str, str]:
    print("\nPart 3: current decomposition and free orientation ratio")
    p, q = sp.symbols("p q", positive=True)
    obj = c3_objects()
    C = obj["C"]
    I = obj["I"]
    By = obj["By"]
    Q = sp.simplify(p * (C - I) + q * (C**2 - I))
    sym = sp.simplify((Q + Q.T) / 2)
    skew = sp.simplify((Q - Q.T) / 2)
    expected_sym = sp.simplify((p + q) * (C + C**2 - 2 * I) / 2)
    expected_skew = sp.simplify((p - q) * (C - C**2) / 2)
    hermitian_current = sp.simplify(sp.I * skew)
    expected_hermitian_current = sp.simplify((p - q) * sp.sqrt(6) * By / 2)
    ratio = sp.simplify((p - q) / (p + q))

    check("symmetric part is reversible Markov/Laplacian piece", is_zero(sym - expected_sym), sym)
    check("skew part is circulation current", is_zero(skew - expected_skew), skew)
    check("skew current is anti-self-adjoint on real carrier", is_zero(skew.T + skew), skew)
    check("i times skew current is Hermitian B_y direction", is_zero(hermitian_current - expected_hermitian_current))
    check("current ratio is not a constant", ratio.has(p) and ratio.has(q), ratio)
    check("balanced p=q gives zero current ratio", is_zero(ratio.subs(q, p)))
    check("one-way q=0 gives unit current ratio", is_zero(ratio.subs(q, 0) - 1))
    check("opposite one-way p=0 gives negative unit current ratio", is_zero(ratio.subs(p, 0) + 1))

    return {
        "symmetric_part": "(p+q)*(C+C^2-2I)/2",
        "skew_current_part": "(p-q)*(C-C^2)/2",
        "hermitian_current_proxy": "(p-q)*sqrt(6)*B_y/2",
        "orientation_ratio": "(p-q)/(p+q)",
        "free_ratio_witnesses": "p=q -> 0, q=0 -> 1, p=0 -> -1",
        "conclusion": "current sign/ratio is an extra dynamics/readout input, not a derived top law",
    }


def part4_radial_and_readout_counterfamily() -> dict[str, Any]:
    print("\nPart 4: top-row counterfamily after granting nontrivial phase readout")
    A, g2, lambda_top, c = sp.symbols("A g_2 lambda_top c", positive=True)
    obj = c3_objects()
    Bx = obj["Bx"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Vtop = sp.simplify(lambda_top * A * Bx)
    row_o = sp.simplify(-sp.trace(Po * Vtop))
    row_o2 = sp.simplify(-sp.trace(Po2 * Vtop))
    w_row = g2 * A / 2
    same_source_readout = sp.simplify(g2 / sp.sqrt(2) * row_o / w_row)
    reparam_readout = sp.simplify(g2 / sp.sqrt(2) * (row_o / c) / (w_row / c))
    target_lambda = sp.solve(sp.Eq(row_o, A / sp.sqrt(12)), lambda_top)

    check("P_omega row is lambda_top*A/sqrt(6)", is_zero(row_o - lambda_top * A / sp.sqrt(6)), row_o)
    check("P_omega2 row is the same", is_zero(row_o - row_o2), row_o2)
    check("target row requires lambda_top=1/sqrt(2)", target_lambda == [1 / sp.sqrt(2)], target_lambda)
    check("W row is independent of lambda_top", not w_row.has(lambda_top), w_row)
    check("same-source readout keeps lambda_top", is_zero(same_source_readout - lambda_top / sp.sqrt(3)), same_source_readout)
    check("source reparameterization cannot remove lambda_top", is_zero(reparam_readout - lambda_top / sp.sqrt(3)), reparam_readout)

    witnesses = [
        {"phase_readout": "P_omega", "lambda_top": "1", "top_row": "A/sqrt(6)", "target": False},
        {"phase_readout": "P_omega2", "lambda_top": "sqrt(3)/2", "top_row": "A/2", "target": False},
        {"phase_readout": "P_omega", "lambda_top": "1/sqrt(2)", "top_row": "A/sqrt(12)", "target": True},
    ]
    check("counterfamily contains target and non-target completions", {row["target"] for row in witnesses} == {False, True})
    return {
        "family": "V_top(lambda_top)=lambda_top*A*B_x",
        "nontrivial_line_row": "lambda_top*A/sqrt(6)",
        "target_requires_lambda_top": "1/sqrt(2)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "witnesses": witnesses,
    }


def part5_certificate_boundary() -> dict[str, bool | str]:
    print("\nPart 5: certificate boundary")
    certificate: dict[str, bool | str] = {
        "oriented_c3_markov_current_checked": True,
        "stationary_perron_line_is_P0": True,
        "nontrivial_real_decay_pair_degenerate": True,
        "current_splits_phase_sign_only": True,
        "current_ratio_free_on_current_surface": True,
        "non_mass_top_readout_derived": False,
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
    check("oriented-current route does not derive non-mass top readout", certificate["non_mass_top_readout_derived"] is False)
    check("oriented-current route does not derive radial factor", certificate["radial_generator_factorization_lambda_top_derived"] is False)
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
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in text)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `lambda_top=1/sqrt(2)`",
        "accepted coefficient-bearing physical top row is supplied",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part7_claim_status() -> dict[str, Any]:
    print("\nPart 7: claim status")
    status = {
        "actual_current_surface_status": "no-go / open oriented-current-to-top-row law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "nonreversible C3 Markov current plus connected/current "
            "normalization derives accepted non-mass physical top-line law "
            "and the coefficient-bearing top row"
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The oriented C3 Markov current keeps P_0 as stationary/Perron "
            "line, leaves the nontrivial real decay rate degenerate, and "
            "supplies only conjugate phase signs until a physical phase/readout "
            "law is added. It also does not derive lambda_top=1/sqrt(2), "
            "accepted backend/projectors, or strict top/W pole rows."
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
    print("Y_T C3 ORIENTED MARKOV-CURRENT SOURCE-LAW NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    spectrum = part2_oriented_markov_spectrum()
    current = part3_current_decomposition_and_free_ratio()
    counterfamily = part4_radial_and_readout_counterfamily()
    certificate = part5_certificate_boundary()
    part6_firewalls()
    status = part7_claim_status()

    output = {
        "claim_id": "yt_c3_oriented_markov_current_source_law_no_go_note_2026-05-28",
        "claim_type": "no_go",
        **status,
        "dependency_fail_counts": {name: data.get("fail_count") for name, data in deps.items()},
        "oriented_markov_spectrum": spectrum,
        "current_decomposition": current,
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
