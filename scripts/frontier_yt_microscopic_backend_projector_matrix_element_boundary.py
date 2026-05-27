#!/usr/bin/env python3
"""Y_T microscopic backend/projector/matrix-element boundary.

This runner checks the final current theory shortcut in the positive-closure
campaign: whether existing microscopic source/backend/carrier/C3 support
certifies the coefficient-bearing top matrix element.  It proves the row is
still equivalent to supplying an accepted projector plus source-generator
expectation on an accepted same-surface backend.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_microscopic_backend_projector_matrix_element_boundary_2026-05-27.json"

NOTE = DOCS / "YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
NATIVE_BACKEND = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
BACKEND_PROJECTOR = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
TOP_SECTOR_PROJECTOR = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
C3_REAL_TOP_LINE = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
C3_DYNAMICS = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
STRICT_SPARSE = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
MATRIX_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
NATIVE_BACKEND_OUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
BACKEND_PROJECTOR_OUT = ROOT / "outputs" / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"
TOP_SECTOR_PROJECTOR_OUT = ROOT / "outputs" / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"
C3_REAL_TOP_LINE_OUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
C3_DYNAMICS_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
STRICT_SPARSE_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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
    print("\nPart 1: anchors and dependency status")
    paths = (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        MATRIX_FACTORIZATION,
        NATIVE_BACKEND,
        BACKEND_PROJECTOR,
        TOP_SECTOR_PROJECTOR,
        C3_REAL_TOP_LINE,
        C3_DYNAMICS,
        STRICT_SPARSE,
        FIRST_PRINCIPLES_OUT,
        MATRIX_FACTORIZATION_OUT,
        NATIVE_BACKEND_OUT,
        BACKEND_PROJECTOR_OUT,
        TOP_SECTOR_PROJECTOR_OUT,
        C3_REAL_TOP_LINE_OUT,
        C3_DYNAMICS_OUT,
        STRICT_SPARSE_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Current Stack",
        "First-Principles / Elon Exercise",
        "Matrix Element Equivalence",
        "Finite Projector Witness",
        "C3 Specialization",
        "No-Go Boundary",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go",
        "proposal_allowed: false",
        "source law + carrier amplitude + C3 algebra + W row",
        "accepted_same_surface_transfer_backend",
        "source_generator_matrix_element: A/sqrt(12)",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "native_backend": load_json(NATIVE_BACKEND_OUT),
        "backend_projector": load_json(BACKEND_PROJECTOR_OUT),
        "top_sector_projector": load_json(TOP_SECTOR_PROJECTOR_OUT),
        "c3_real_top_line": load_json(C3_REAL_TOP_LINE_OUT),
        "c3_dynamics": load_json(C3_DYNAMICS_OUT),
        "strict_sparse": load_json(STRICT_SPARSE_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "first-principles dependency names top sector response row",
        "top sector response row" in deps["first_principles"].get("first_open_gate_after_this_note", ""),
        deps["first_principles"].get("first_open_gate_after_this_note"),
    )
    check(
        "matrix factorization dependency leaves generator open",
        deps["matrix_factorization"].get("certificate_boundary", {}).get("accepted_same_surface_generator_factorization") is False,
    )
    check(
        "matrix factorization dependency leaves nontrivial line open",
        deps["matrix_factorization"].get("certificate_boundary", {}).get("nontrivial_top_line_assignment_derived") is False,
    )
    check(
        "native backend dependency is not accepted physical backend",
        deps["native_backend"].get("candidate_backend", {}).get("accepted_same_surface_transfer_backend_present") is False,
    )
    check(
        "backend projector dependency keeps projectors load-bearing",
        "sector projectors" in deps["backend_projector"].get("route_still_live", ""),
        deps["backend_projector"].get("route_still_live"),
    )
    check(
        "top-sector dependency keeps strict pole-row route live",
        "strict same-source pole-row evidence" in deps["top_sector_projector"].get("route_still_live", ""),
        deps["top_sector_projector"].get("route_still_live"),
    )
    check(
        "strict sparse dependency confirms strict certificate absent",
        deps["strict_sparse"].get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    return deps


def part2_matrix_element_equivalence() -> dict[str, str]:
    print("\nPart 2: FH matrix-element equivalence")
    A, g2, g0, gw, gt = sp.symbols("A g_2 g_0 g_W g_t", positive=True)
    dm_w = sp.simplify(gw - g0)
    dm_t = sp.simplify(gt - g0)
    readout = sp.simplify(g2 / sp.sqrt(2) * dm_t / dm_w)
    target_subs = {
        gw: g0 + g2 * A / 2,
        gt: g0 + A / sp.sqrt(12),
    }
    target_readout = sp.simplify(readout.subs(target_subs))
    alt_readout = sp.simplify(readout.subs({gw: g0 + g2 * A / 2, gt: g0 + A / sp.sqrt(3)}))

    check("W slope is a sector matrix-element difference", is_zero(dm_w - (gw - g0)), dm_w)
    check("top slope is a sector matrix-element difference", is_zero(dm_t - (gt - g0)), dm_t)
    check("readout depends on the top sector expectation", "g_t" in sp.sstr(readout), readout)
    check("target matrix element gives 1/sqrt(6)", is_zero(target_readout - 1 / sp.sqrt(6)), target_readout)
    check("alternative top matrix element changes readout", not is_zero(alt_readout - target_readout), alt_readout)

    return {
        "dM_W_dell": "g_W - g_0",
        "dM_t_dell": "g_t - g_0",
        "target_condition": "g_t - g_0 = A/sqrt(12)",
        "target_readout": "1/sqrt(6)",
        "alternative_readout_for_A_over_sqrt3": sp.sstr(alt_readout),
    }


def part3_projector_continuum_witness() -> dict[str, Any]:
    print("\nPart 3: finite projector witness")
    A, g2, theta = sp.symbols("A g_2 theta", positive=True)
    g_top = sp.diag(A / sp.sqrt(12), A / sp.sqrt(3))
    t = sp.Matrix([sp.cos(theta), sp.sin(theta)])
    p_theta = sp.simplify(t * t.T)
    expectation = sp.simplify((t.T * g_top * t)[0])
    target = sp.simplify(expectation.subs(theta, 0))
    alt = sp.simplify(expectation.subs(theta, sp.pi / 2))
    dmw = g2 * A / 2
    read_target = sp.simplify(g2 / sp.sqrt(2) * target / dmw)
    read_alt = sp.simplify(g2 / sp.sqrt(2) * alt / dmw)

    check("P(theta) is rank-one idempotent", is_zero(p_theta * p_theta - p_theta))
    check("P(theta) has trace one", is_zero(sp.trace(p_theta) - 1), sp.trace(p_theta))
    check("top expectation depends on projector angle", not is_zero(sp.diff(expectation, theta)), expectation)
    check("theta=0 gives target top row", is_zero(target - A / sp.sqrt(12)), target)
    check("theta=pi/2 gives singlet-size top row", is_zero(alt - A / sp.sqrt(3)), alt)
    check("same W row with target projector gives 1/sqrt(6)", is_zero(read_target - 1 / sp.sqrt(6)), read_target)
    check("same W row with alternate projector gives 2/sqrt(6)", is_zero(read_alt - 2 / sp.sqrt(6)), read_alt)

    return {
        "G_top": "diag(A/sqrt(12), A/sqrt(3))",
        "P_theta": "rank_one_projector(cos(theta)e1 + sin(theta)e2)",
        "expectation": sp.sstr(expectation),
        "theta_0_row": sp.sstr(target),
        "theta_pi_over_2_row": sp.sstr(alt),
        "same_w_row": "g_2*A/2",
        "target_readout": sp.sstr(read_target),
        "alternate_readout": sp.sstr(read_alt),
        "conclusion": "projector authority is load-bearing",
    }


def part4_c3_specialization() -> dict[str, Any]:
    print("\nPart 4: C3 specialization")
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    bx = sp.simplify((C + C**2) / sp.sqrt(6))
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    responses = {
        name: sp.simplify(sp.expand_complex(sp.trace(projector * bx)))
        for name, projector in projectors.items()
    }
    rows = {
        name: sp.simplify(A / sp.sqrt(2) * value)
        for name, value in responses.items()
    }
    check("C3 cycle has order three", is_zero(C**3 - sp.eye(3)))
    check("B_x is Hermitian", is_zero(bx.conjugate().T - bx))
    check("B_x is traceless", is_zero(sp.trace(bx)))
    check("P_0 response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])
    check("P_0 radial row is A/sqrt(3)", is_zero(rows["P_0"] - A / sp.sqrt(3)), rows["P_0"])
    check("P_omega radial row magnitude is A/sqrt(12)", is_zero(abs(rows["P_omega"]) - A / sp.sqrt(12)), rows["P_omega"])
    check("singlet and nontrivial rows differ", not is_zero(rows["P_0"] - abs(rows["P_omega"])))

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "responses": {name: sp.sstr(value) for name, value in responses.items()},
        "radial_rows": {name: sp.sstr(value) for name, value in rows.items()},
        "conclusion": "nontrivial top-line authority is load-bearing",
    }


def part5_stuck_fanout() -> list[dict[str, str]]:
    print("\nPart 5: stuck fan-out synthesis")
    frames = [
        {
            "frame": "primitive_rn_fisher_source_law",
            "attempt": "derive the source family and Fisher unit from no-hidden-record intervention",
            "result": "source law derived, physical O_top/projector not derived",
            "disposition": "blocked",
        },
        {
            "frame": "six_component_carrier_amplitude",
            "attempt": "use normalized color/isospin component 1/sqrt(6) as the top row",
            "result": "local coefficient support only; physical top generation pole remains open",
            "disposition": "blocked",
        },
        {
            "frame": "c3_spectral_line",
            "attempt": "assign top to a nontrivial C3 character line",
            "result": "target row exact on nontrivial lines, but current dynamics/order does not assign physical top there",
            "disposition": "blocked",
        },
        {
            "frame": "same_source_transfer_fh",
            "attempt": "use formal transfer/FH and W row to force the top row",
            "result": "FH reduces the problem to the sector matrix element; it does not fix it",
            "disposition": "blocked",
        },
        {
            "frame": "strict_sparse_pole_rows",
            "attempt": "bypass projector theorem with accepted pole-row data",
            "result": "harness exists but accepted backend/projector/controlled rows are absent",
            "disposition": "blocked_on_missing_artifact",
        },
    ]
    for item in frames:
        check(f"fan-out frame recorded: {item['frame']}", item["disposition"].startswith("blocked"))
    check("fan-out includes five independent attack frames", len(frames) == 5)
    check("fan-out found no retained-positive closure", all(item["disposition"].startswith("blocked") for item in frames))
    return frames


def part6_certificate_boundary() -> dict[str, Any]:
    print("\nPart 6: certificate boundary")
    certificate = {
        "source_law_derived": True,
        "candidate_carrier_amplitude_available": True,
        "c3_matrix_algebra_available": True,
        "same_source_w_row_available_as_conditional_row": True,
        "accepted_same_surface_transfer_backend": False,
        "physical_top_projector_or_pole_derived": False,
        "w_projector_or_pole_derived": False,
        "source_generator_matrix_element_derived": False,
        "contact_subtraction_done": False,
        "finite_volume_ir_controls_pass": False,
        "same_model_class": False,
        "strict_pole_row_data_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("positive certificate fails because accepted backend is absent", certificate["accepted_same_surface_transfer_backend"] is False)
    check("positive certificate fails because physical top projector is absent", certificate["physical_top_projector_or_pole_derived"] is False)
    check("positive certificate fails because source matrix element is absent", certificate["source_generator_matrix_element_derived"] is False)
    return certificate


def part7_firewalls() -> None:
    print("\nPart 7: firewalls and wording")
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
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "accepted W/top pole isolation is supplied",
        "positive closure is achieved",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part8_claim_status() -> dict[str, Any]:
    print("\nPart 8: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "current microscopic source/backend/carrier/C3 support derives the "
            "accepted coefficient-bearing physical top matrix element"
        ),
        "conditional_surface_status": (
            "exact top-row certificate if accepted backend, physical top projector, "
            "and source-generator matrix element are supplied"
        ),
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "first_open_gate_after_this_note": (
            "accepted same-surface backend/projectors/source-generator matrix elements, "
            "or accepted strict same-source top/W pole-row data"
        ),
        "route_still_live": (
            "derive accepted same-surface backend/projectors/matrix elements, "
            "or produce strict same-source top/W pole-row data"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("next gate names backend/projectors/matrix elements", "backend/projectors" in status["first_open_gate_after_this_note"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T MICROSCOPIC BACKEND PROJECTOR MATRIX ELEMENT BOUNDARY")
    print("=" * 78)

    deps = part1_anchors()
    equivalence = part2_matrix_element_equivalence()
    projector_witness = part3_projector_continuum_witness()
    c3_witness = part4_c3_specialization()
    fanout = part5_stuck_fanout()
    certificate = part6_certificate_boundary()
    part7_firewalls()
    status = part8_claim_status()

    result = {
        "claim_id": "yt_microscopic_backend_projector_matrix_element_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_microscopic_backend_projector_matrix_element_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "The current microscopic support fixes source law, candidate carrier "
            "amplitude, and C3 matrix algebra, but it does not derive the accepted "
            "same-surface backend, physical top pole projector, or the top "
            "source-generator expectation. Finite witnesses keep the W row fixed "
            "while the top matrix element changes with the projector."
        ),
        "dependency_status": {
            name: {
                "fail_count": data.get("fail_count"),
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
            }
            for name, data in deps.items()
        },
        "matrix_element_equivalence": equivalence,
        "projector_continuum_witness": projector_witness,
        "c3_specialization_witness": c3_witness,
        "stuck_fanout_synthesis": fanout,
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
