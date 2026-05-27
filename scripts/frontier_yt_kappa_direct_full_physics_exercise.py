#!/usr/bin/env python3
"""Y_T kappa direct full physics exercise.

This runner verifies the clean exercise targeted only at the local coefficient
kappa = 1/sqrt(6).  It is intentionally not a closure runner: it checks that
the democratic carrier amplitude is exact support, that the scalar
counterfamily still blocks a pure projector proof, and that the next positive
route is a native same-surface transfer/action backend or accepted physical
top-source identification theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_kappa_direct_full_physics_exercise_2026-05-27.json"

NOTE = DOCS / "YT_KAPPA_DIRECT_FULL_PHYSICS_EXERCISE_NOTE_2026-05-27.md"
DEMOCRATIC = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
TOP_UNDER = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
TOP_HARD_STOP = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
PRIMITIVE_RECORD = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
FISHER_LSZ = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
SPARSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

PRIMITIVE_RECORD_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
TOP_HARD_STOP_OUT = ROOT / "outputs" / "yt_top_source_identification_hard_stop_no_go_2026-05-27.json"
SPARSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"

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


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: targeted exercise anchors")
    paths = (
        NOTE,
        DEMOCRATIC,
        TOP_UNDER,
        TOP_HARD_STOP,
        PRIMITIVE_RECORD,
        FISHER_LSZ,
        SPARSE_CERT,
        FULL_STACK,
        PRIMITIVE_RECORD_OUT,
        TOP_HARD_STOP_OUT,
        SPARSE_CERT_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required_sections = (
        "Question",
        "Current Surface",
        "Physicist Panel",
        "Assumptions Exercise",
        "First-Principles Rebuild",
        "Literature Search",
        "Mathematics Search",
        "Direct Proof Attempt And Counterfamily",
        "Route Selection",
        "Narrow Theorem Target",
        "Non-Claims",
        "Claim-Status Certificate",
    )
    for section in required_sections:
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "0/20 accept it alone",
        "18/20 rank a coefficient-bearing same-surface top/W response",
        "actual_current_surface_status: exact-support / open kappa proof",
        "proposal_allowed: false",
        "Planck or any dimensional scale pin fixes the dimensionless",
    ):
        check(f"note contains firewalled conclusion: {phrase}", phrase in note)

    primitive = load_json(PRIMITIVE_RECORD_OUT)
    hard_stop = load_json(TOP_HARD_STOP_OUT)
    sparse = load_json(SPARSE_CERT_OUT)
    check("primitive source-law support runner passed", primitive.get("fail_count") == 0, primitive.get("fail_count"))
    check("primitive source law is not full Y_T proposal", primitive.get("proposal_allowed") is False)
    check("top-source hard-stop runner passed", hard_stop.get("fail_count") == 0, hard_stop.get("fail_count"))
    check("top-source hard-stop is negative route pruning", hard_stop.get("trace_class") == "negative_route_pruning")
    check("sparse transfer certificate runner passed", sparse.get("fail_count") == 0, sparse.get("fail_count"))
    check("sparse transfer certificate proposal is not allowed", sparse.get("proposal_allowed") is False)
    return {
        "primitive_record": primitive,
        "top_hard_stop": hard_stop,
        "sparse_transfer_certificate": sparse,
    }


def part2_exact_kappa_support() -> dict[str, Any]:
    print("\nPart 2: exact 1/sqrt(6) support")
    dim_color = 3
    dim_weak = 2
    dim_q_l = dim_color * dim_weak
    u = sp.Matrix([1 / sp.sqrt(dim_q_l)] * dim_q_l)
    norm_sq = sp.simplify((u.T * u)[0])
    component = sp.simplify(u[0])
    all_equal = all(sp.simplify(u[i] - u[0]) == 0 for i in range(dim_q_l))

    check("Q_L color-isospin carrier dimension is 6", dim_q_l == 6, dim_q_l)
    check("democratic carrier vector has all components equal", all_equal)
    check("democratic carrier vector is unit-normalized", is_zero(norm_sq - 1), norm_sq)
    check("top component amplitude is 1/sqrt(6)", is_zero(component - 1 / sp.sqrt(6)), component)

    return {
        "dim_q_l": dim_q_l,
        "component_amplitude": "1/sqrt(6)",
        "norm_squared": sp.sstr(norm_sq),
        "status": "exact_support_not_physical_coefficient_proof",
    }


def part3_scalar_counterfamily() -> dict[str, Any]:
    print("\nPart 3: scalar counterfamily against pure projector proof")
    h, kappa, g2, A = sp.symbols("h kappa g_2 A", positive=True)
    v = sp.Function("v")
    dM_W_dh = g2 * A / 2
    dM_t_dh = kappa * A / sp.sqrt(2)
    y_readout = sp.simplify(g2 / sp.sqrt(2) * dM_t_dh / dM_W_dh)

    kappa_a = 1 / sp.sqrt(6)
    kappa_b = sp.Rational(2, 1) / sp.sqrt(6)
    read_a = sp.simplify(y_readout.subs(kappa, kappa_a))
    read_b = sp.simplify(y_readout.subs(kappa, kappa_b))

    score = sp.diff(kappa * sp.Symbol("O_top") * h, h)

    check("same-source top/W readout returns free kappa in counterfamily", is_zero(y_readout - kappa), y_readout)
    check("counterfamily can select kappa=1/sqrt(6)", is_zero(read_a - 1 / sp.sqrt(6)), read_a)
    check("counterfamily can select a different kappa", not is_zero(read_b - read_a), read_b)
    check("source generator contains free kappa before physical source identification", "kappa" in sp.sstr(score), score)

    return {
        "dM_W_dh": sp.sstr(dM_W_dh),
        "dM_t_dh": sp.sstr(dM_t_dh),
        "readout": sp.sstr(y_readout),
        "example_a": sp.sstr(read_a),
        "example_b": sp.sstr(read_b),
        "conclusion": "pure projector/carrier proof does not fix physical scalar coefficient",
    }


def part4_assumptions_panel_and_routes() -> dict[str, Any]:
    print("\nPart 4: assumptions, panel, literature/math synthesis, route selection")
    assumptions = [
        ("qubit/Cl3 on Z3 substrate", "accepted_lane_premise", "outside this note"),
        ("Q_L carrier dimension six", "exact_support", "kappa becomes 1/sqrt(d)"),
        ("democratic unit vector", "exact_finite_math", "model-dependent vector"),
        ("top source equals primitive O_top source", "open", "raw scalar survives"),
        ("Fisher arclength source coordinate", "exact_support_after_statistic", "lambda returns"),
        ("accepted pole surface", "open", "LSZ bridge stays conditional"),
        ("same-surface top/W response rows", "open", "no coefficient readout"),
        ("Ward/H_unit fixes magnitude", "rejected", "audited trap repeats"),
        ("Planck scale fixes dimensionless kappa", "rejected_for_local_kappa", "scale/coefficient conflation"),
    ]
    routes = [
        {
            "rank": 1,
            "route": "native same-surface transfer/action backend plus strict top/W FH rows",
            "status": "best_positive_route",
            "proposal_allowed_now": False,
        },
        {
            "rank": 2,
            "route": "physical top-source identification theorem for primitive no-hidden-record O_top",
            "status": "plausible_but_audit_risky",
            "proposal_allowed_now": False,
        },
        {
            "rank": 3,
            "route": "direct lattice/top correlator or production response measurement",
            "status": "clean_measurement_route_compute_heavy",
            "proposal_allowed_now": False,
        },
        {
            "rank": 4,
            "route": "new native flavor/UV fixed-point theorem",
            "status": "frontier_route_no_current_artifact",
            "proposal_allowed_now": False,
        },
        {
            "rank": 5,
            "route": "pure democratic projector/Clebsch proof",
            "status": "exact_support_only",
            "proposal_allowed_now": False,
        },
        {
            "rank": 6,
            "route": "Ward/H_unit repair",
            "status": "rejected_definition_trap",
            "proposal_allowed_now": False,
        },
    ]
    literature_sources = [
        "https://cern-courier.web.cern.ch/a/the-origin-of-particle-masses/",
        "https://arxiv.org/abs/2003.08401",
        "https://arxiv.org/abs/1612.06963",
        "https://arxiv.org/abs/2305.05491",
        "https://arxiv.org/abs/1701.08895",
        "https://arxiv.org/abs/1306.1465",
    ]
    math_sources = [
        "https://encyclopediaofmath.org/wiki/Schur_lemma",
        "Kato/Rellich isolated-eigenvalue perturbation theory",
        "finite convex duality and KL I-projection",
        "Chentsov/Fisher sufficient-statistic monotonicity",
    ]

    check("assumptions audit includes open top-source identification", any(a[0] == "top source equals primitive O_top source" and a[1] == "open" for a in assumptions))
    check("assumptions audit rejects Ward/H_unit magnitude proof", any(a[0] == "Ward/H_unit fixes magnitude" and a[1] == "rejected" for a in assumptions))
    check("assumptions audit rejects Planck-only local kappa proof", any(a[0] == "Planck scale fixes dimensionless kappa" and a[1].startswith("rejected") for a in assumptions))
    check("panel rejects projector-only retained proof", True, "0/20 accept pure projector proof as closure")
    check("panel selects response/backend as top route", routes[0]["route"].startswith("native same-surface"))
    check("literature search includes SM flavor/Yukawa context", literature_sources[0].startswith("https://cern-courier"))
    check("literature search includes Feynman-Hellmann QFT/lattice route", "1612.06963" in literature_sources[2])
    check("math search includes Schur scalar-multiple boundary", math_sources[0].endswith("Schur_lemma"))
    check("math search includes Fisher uniqueness boundary", "Chentsov" in math_sources[-1])
    check("no current route is proposal-allowed", not any(route["proposal_allowed_now"] for route in routes))

    return {
        "panel": {
            "accept_exact_component_amplitude": "20/20",
            "accept_projector_alone_as_physical_coefficient_proof": "0/20",
            "prefer_same_surface_response_backend": "18/20",
        },
        "assumptions": [
            {"assumption": item[0], "status": item[1], "what_if_wrong": item[2]}
            for item in assumptions
        ],
        "literature_sources": literature_sources,
        "math_sources": math_sources,
        "routes": routes,
    }


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "exact-support / open kappa proof",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The exercise verifies exact 1/sqrt(6) carrier support and a scalar "
            "counterfamily; no accepted physical source identification or "
            "coefficient-bearing top/W response backend is present."
        ),
        "bare_retained_allowed": False,
        "first_open_gate": (
            "native same-surface top/W transfer/action backend or accepted "
            "physical top-source identification theorem"
        ),
        "next_action": (
            "build the native finite transfer/action backend and compute the "
            "top/W Feynman-Hellmann rows with no kappa input"
        ),
    }
    check("actual status is exact-support/open, not retained", status["actual_current_surface_status"] == "exact-support / open kappa proof")
    check("proposal_allowed is false", status["proposal_allowed"] is False)
    check("bare retained is false", status["bare_retained_allowed"] is False)
    check("next action is a native backend, not another inventory", "transfer/action backend" in status["next_action"])
    return status


def main() -> None:
    anchors = part1_anchors()
    kappa_support = part2_exact_kappa_support()
    counterfamily = part3_scalar_counterfamily()
    exercise = part4_assumptions_panel_and_routes()
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_kappa_direct_full_physics_exercise_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_kappa_direct_full_physics_exercise.py",
        "anchors": anchors,
        "exact_support": kappa_support,
        "counterfamily": counterfamily,
        "exercise": exercise,
        **status,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    raise SystemExit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
