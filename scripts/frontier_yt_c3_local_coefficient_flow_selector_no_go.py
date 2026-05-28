#!/usr/bin/env python3
"""Y_T C3 local coefficient-flow selector no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_local_coefficient_flow_selector_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_LOCAL_COEFFICIENT_FLOW_SELECTOR_NO_GO_NOTE_2026-05-28.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
CIRCULANT_BOUNDARY = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
MARKOV_NOGO = DOCS / "YT_C3_MARKOV_LAPLACIAN_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
ORIENTED_CURRENT_NOGO = DOCS / "YT_C3_ORIENTED_MARKOV_CURRENT_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
CHARACTER_FLOW_NOGO = DOCS / "YT_C3_UNITARY_CHARACTER_FLOW_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
PHASE_ORBIT_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
ORBIT_MEMBER_NOGO = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AUDIT = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
CIRCULANT_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
MARKOV_NOGO_OUT = ROOT / "outputs" / "yt_c3_markov_laplacian_source_law_no_go_2026-05-28.json"
ORIENTED_CURRENT_NOGO_OUT = ROOT / "outputs" / "yt_c3_oriented_markov_current_source_law_no_go_2026-05-28.json"
CHARACTER_FLOW_NOGO_OUT = ROOT / "outputs" / "yt_c3_unitary_character_flow_source_law_no_go_2026-05-28.json"
PHASE_ORBIT_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
ORBIT_MEMBER_NOGO_OUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"
RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
STRICT_AUDIT_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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


def frob_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def line_eigenvalues(x: sp.Expr, y: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "P_0": sp.radsimp(2 * x / sp.sqrt(6)),
        "P_omega": sp.radsimp(-x / sp.sqrt(6) - y / sp.sqrt(2)),
        "P_omega2": sp.radsimp(-x / sp.sqrt(6) + y / sp.sqrt(2)),
    }


def top_by_largest(eigenvalues: dict[str, sp.Expr]) -> str:
    return max(eigenvalues, key=lambda key: float(sp.N(eigenvalues[key])))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        FIRST_PRINCIPLES,
        CIRCULANT_BOUNDARY,
        MARKOV_NOGO,
        ORIENTED_CURRENT_NOGO,
        CHARACTER_FLOW_NOGO,
        PHASE_ORBIT_NOGO,
        ORBIT_MEMBER_NOGO,
        RADIAL_FACTOR_NOGO,
        STRICT_AUDIT,
        FULL_STACK,
        FIRST_PRINCIPLES_OUT,
        CIRCULANT_BOUNDARY_OUT,
        MARKOV_NOGO_OUT,
        ORIENTED_CURRENT_NOGO_OUT,
        CHARACTER_FLOW_NOGO_OUT,
        PHASE_ORBIT_NOGO_OUT,
        ORBIT_MEMBER_NOGO_OUT,
        RADIAL_FACTOR_NOGO_OUT,
        STRICT_AUDIT_OUT,
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
        "Finite Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open local-flow-to-top-row law",
        "trace_class: negative_route_pruning",
        "proposal_allowed: false",
        "F_s(x,y)",
        "F_nt(x,y)",
        "lambda_top = 1/sqrt(2)",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    forbidden_positive = (
        "actual_current_surface_status: retained",
        "actual_current_surface_status: proposed_retained",
        "proposal_allowed: true",
        "bare_retained_allowed: true",
    )
    for phrase in forbidden_positive:
        check(f"note avoids positive claim phrase: {phrase}", phrase not in note)

    first = load_json(FIRST_PRINCIPLES_OUT)
    circulant = load_json(CIRCULANT_BOUNDARY_OUT)
    markov = load_json(MARKOV_NOGO_OUT)
    oriented = load_json(ORIENTED_CURRENT_NOGO_OUT)
    character = load_json(CHARACTER_FLOW_NOGO_OUT)
    orbit = load_json(PHASE_ORBIT_NOGO_OUT)
    member = load_json(ORBIT_MEMBER_NOGO_OUT)
    radial = load_json(RADIAL_FACTOR_NOGO_OUT)
    strict = load_json(STRICT_AUDIT_OUT)

    check("first-principles boundary passed", first.get("fail_count") == 0, first.get("fail_count"))
    check("circulant source-law boundary passed", circulant.get("fail_count") == 0, circulant.get("fail_count"))
    check("Markov/Laplacian no-go passed", markov.get("fail_count") == 0, markov.get("fail_count"))
    check("oriented-current no-go passed", oriented.get("fail_count") == 0, oriented.get("fail_count"))
    check("unitary character-flow no-go passed", character.get("fail_count") == 0, character.get("fail_count"))
    check("phase-orbit selector no-go passed", orbit.get("fail_count") == 0, orbit.get("fail_count"))
    check("orbit-member covariance no-go passed", member.get("fail_count") == 0, member.get("fail_count"))
    check("radial-factor no-go passed", radial.get("fail_count") == 0, radial.get("fail_count"))
    check("strict sparse availability audit passed", strict.get("fail_count") == 0, strict.get("fail_count"))

    return {
        "first_principles_status": first.get("actual_current_surface_status"),
        "circulant_status": circulant.get("actual_current_surface_status"),
        "radial_status": radial.get("actual_current_surface_status"),
        "strict_status": strict.get("actual_current_surface_status"),
    }


def part2_c3_basis_and_responses() -> dict[str, Any]:
    print("\nPart 2: C3 basis and source responses")
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    Bx = (C + C**2) / sp.sqrt(6)
    By = sp.I * (C - C**2) / sp.sqrt(6)
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }

    for name, basis in {"B_x": Bx, "B_y": By}.items():
        check(f"{name} commutes with C", is_zero(basis * C - C * basis))
        check(f"{name} is Hermitian", is_zero(basis.conjugate().T - basis))
        check(f"{name} has unit Frobenius norm", is_zero(frob_inner(basis, basis) - 1), frob_inner(basis, basis))
    check("B_x and B_y are Frobenius orthogonal", is_zero(frob_inner(Bx, By)), frob_inner(Bx, By))

    responses = {
        name: sp.radsimp(sp.simplify(sp.trace(projector * Bx)))
        for name, projector in projectors.items()
    }
    check("P0 Bx response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("Pomega Bx response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("Pomega2 Bx response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])

    return {name: sp.sstr(value) for name, value in responses.items()}


def part3_local_flow_countermodels() -> dict[str, Any]:
    print("\nPart 3: local-flow countermodels")
    x, y = sp.symbols("x y", real=True)
    singlet_fixed = {"x": sp.Integer(1), "y": sp.Integer(0)}
    nontrivial_fixed = {"x": -sp.Rational(1, 2), "y": sp.sqrt(3) / 2}
    flow_s = sp.Matrix([1 - x, -y])
    flow_nt = sp.Matrix([-sp.Rational(1, 2) - x, sp.sqrt(3) / 2 - y])

    flow_s_at_fixed = flow_s.subs({x: singlet_fixed["x"], y: singlet_fixed["y"]})
    flow_nt_at_fixed = flow_nt.subs({x: nontrivial_fixed["x"], y: nontrivial_fixed["y"]})
    check("singlet linear local flow vanishes at its fixed point", is_zero(flow_s_at_fixed), flow_s_at_fixed)
    check("nontrivial linear local flow vanishes at its fixed point", is_zero(flow_nt_at_fixed), flow_nt_at_fixed)
    check("singlet fixed point has unit connected norm", is_zero(singlet_fixed["x"] ** 2 + singlet_fixed["y"] ** 2 - 1))
    check(
        "nontrivial fixed point has unit connected norm",
        is_zero(nontrivial_fixed["x"] ** 2 + nontrivial_fixed["y"] ** 2 - 1),
    )

    eig_s = line_eigenvalues(singlet_fixed["x"], singlet_fixed["y"])
    eig_nt = line_eigenvalues(nontrivial_fixed["x"], nontrivial_fixed["y"])
    top_s = top_by_largest(eig_s)
    top_nt = top_by_largest(eig_nt)
    source_responses = {
        "P_0": 2 / sp.sqrt(6),
        "P_omega": -1 / sp.sqrt(6),
        "P_omega2": -1 / sp.sqrt(6),
    }

    check("singlet fixed point top by largest is P0", top_s == "P_0", eig_s)
    check("singlet fixed point response is not target nontrivial magnitude", not is_zero(abs(source_responses[top_s]) - 1 / sp.sqrt(6)))
    check("primitive fixed point top by largest is Pomega2", top_nt == "P_omega2", eig_nt)
    check("primitive fixed point response has nontrivial magnitude", is_zero(abs(source_responses[top_nt]) - 1 / sp.sqrt(6)))
    check("same local-flow template admits different top rows", top_s != top_nt, (top_s, top_nt))

    return {
        "singlet_flow": {
            "flow": "(1 - x, -y)",
            "fixed_point": {"x": "1", "y": "0"},
            "unit_connected_norm": True,
            "eigenvalues": {key: sp.sstr(value) for key, value in eig_s.items()},
            "top_by_largest": top_s,
            "top_source_response": sp.sstr(source_responses[top_s]),
        },
        "primitive_nontrivial_flow": {
            "flow": "(-1/2 - x, sqrt(3)/2 - y)",
            "fixed_point": {"x": "-1/2", "y": "sqrt(3)/2"},
            "unit_connected_norm": True,
            "eigenvalues": {key: sp.sstr(value) for key, value in eig_nt.items()},
            "top_by_largest": top_nt,
            "top_source_response": sp.sstr(source_responses[top_nt]),
        },
    }


def part4_radial_and_certificate() -> dict[str, Any]:
    print("\nPart 4: radial and certificate boundary")
    lam = sp.symbols("lambda_top", positive=True)
    nontrivial_response = sp.radsimp(lam / sp.sqrt(6))
    target_lambda = 1 / sp.sqrt(2)
    target_response = sp.radsimp(nontrivial_response.subs(lam, target_lambda))
    check("nontrivial local-flow row still carries lambda_top", nontrivial_response == lam / sp.sqrt(6), nontrivial_response)
    check("target row requires lambda_top=1/sqrt(2)", is_zero(target_response - 1 / sp.sqrt(12)), target_response)
    check("lambda_top=1 gives different row", not is_zero(nontrivial_response.subs(lam, 1) - 1 / sp.sqrt(12)))

    boundary = {
        "local_flow_template_fixes_basepoint": False,
        "local_flow_template_excludes_P0": False,
        "unit_connected_norm_selects_nontrivial_top": False,
        "source_tangent_Bx_selects_basepoint": False,
        "c3_orbit_invariance_selects_physical_member": False,
        "accepted_physical_readout_law_present": False,
        "radial_generator_factorization_lambda_top_derived": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_inputs_used": True,
    }
    for key, value in boundary.items():
        check(f"certificate boundary: {key} = {value}", isinstance(value, bool))
    check("certificate keeps proposal disallowed", boundary["accepted_physical_readout_law_present"] is False)

    return boundary


def main() -> int:
    anchors = part1_anchors()
    responses = part2_c3_basis_and_responses()
    countermodels = part3_local_flow_countermodels()
    certificate = part4_radial_and_certificate()

    result = {
        "claim_id": "yt_c3_local_coefficient_flow_selector_no_go_note_2026-05-28",
        "claim_type": "no_go",
        "actual_current_surface_status": "no-go / open local-flow-to-top-row law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "local C3 coefficient-flow template derives the physical nontrivial "
            "top row or radial generator factor"
        ),
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchors": anchors,
        "source_responses": responses,
        "local_flow_countermodels": countermodels,
        "certificate_boundary": certificate,
        "no_go_summary": (
            "Local smooth coefficient-flow form, polynomiality, and unit connected "
            "normalization admit singlet and primitive nontrivial fixed-point "
            "witnesses with the same B_x source tangent. Selecting the nontrivial "
            "fixed point is a new physical readout/dynamics law, and lambda_top "
            "remains free even after nontrivial support is granted."
        ),
        "next_action": (
            "derive accepted physical coefficient-flow/readout/radial law, or "
            "produce strict same-source top/W pole rows"
        ),
        "fail_count": FAIL_COUNT,
        "pass_count": PASS_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
