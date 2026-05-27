#!/usr/bin/env python3
"""Y_T native same-surface top/W transfer-action backend candidate.

This runner constructs the first no-kappa candidate backend for the strict
same-surface top/W response route.  It proves the candidate rows read
1/sqrt(6), then refuses to certify closure because the backend is not yet
derived as the accepted physical finite transfer/action surface and lacks
strict pole/FV/IR/contact/model-class certificates.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"

NOTE = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
KAPPA_EXERCISE = DOCS / "YT_KAPPA_DIRECT_FULL_PHYSICS_EXERCISE_NOTE_2026-05-27.md"
SPARSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
STRICT_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

KAPPA_EXERCISE_OUT = ROOT / "outputs" / "yt_kappa_direct_full_physics_exercise_2026-05-27.json"
SPARSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
STRICT_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"

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


def symbol_names(expr: sp.Expr) -> set[str]:
    return {symbol.name for symbol in expr.free_symbols}


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        KAPPA_EXERCISE,
        SPARSE_CERT,
        STRICT_OBSTRUCTION,
        FH_GATE,
        STRICT_WZ,
        TOP_CARRIER,
        EW_MASS,
        FULL_STACK,
        KAPPA_EXERCISE_OUT,
        SPARSE_CERT_OUT,
        STRICT_OBSTRUCTION_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Purpose",
        "Candidate Backend",
        "Response Readout",
        "Transfer-Matrix Form",
        "Relation To Existing No-Gos",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "bounded support only",
        "No `kappa` symbol appears",
        "not yet derived as the accepted physical finite transfer/action surface",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    kappa = load_json(KAPPA_EXERCISE_OUT)
    sparse = load_json(SPARSE_CERT_OUT)
    obstruction = load_json(STRICT_OBSTRUCTION_OUT)
    check("kappa exercise passed", kappa.get("fail_count") == 0, kappa.get("fail_count"))
    check("kappa exercise did not allow proposal", kappa.get("proposal_allowed") is False)
    check("sparse certificate passed", sparse.get("fail_count") == 0, sparse.get("fail_count"))
    check("sparse certificate still lacks strict rows", sparse.get("strict_top_w_response_certificate_present") is False)
    check("strict obstruction passed", obstruction.get("fail_count") == 0, obstruction.get("fail_count"))
    check("strict obstruction remains route pruning", obstruction.get("trace_class") == "negative_route_pruning")

    return {
        "kappa_exercise": kappa,
        "sparse_certificate": sparse,
        "strict_obstruction": obstruction,
    }


def build_candidate_backend() -> dict[str, Any]:
    ell, A, v0, g2, a_t = sp.symbols("ell A v_0 g_2 a_t", positive=True)
    dim_q_l = 6
    component = sp.sqrt(sp.Rational(1, dim_q_l))
    v = v0 + A * ell
    m_w = sp.simplify(g2 * v / 2)
    m_t = sp.simplify(component * v / sp.sqrt(2))
    dm_w = sp.simplify(sp.diff(m_w, ell))
    dm_t = sp.simplify(sp.diff(m_t, ell))
    y_readout = sp.simplify(g2 / sp.sqrt(2) * dm_t / dm_w)
    lambda_0 = sp.Integer(1)
    lambda_w = sp.exp(-a_t * m_w)
    lambda_t = sp.exp(-a_t * m_t)
    recovered_m_w = sp.simplify(-sp.log(lambda_w / lambda_0) / a_t)
    recovered_m_t = sp.simplify(-sp.log(lambda_t / lambda_0) / a_t)

    return {
        "backend_id": "native_fisher_unit_democratic_top_w_candidate",
        "backend_role": "no_kappa_candidate_backend",
        "same_source_id": "ell",
        "surface_id": "candidate_finite_same_surface_top_w_transfer_action",
        "dim_q_l_color_isospin": dim_q_l,
        "component_amplitude": sp.sstr(component),
        "v_of_ell": sp.sstr(v),
        "M_W": sp.sstr(m_w),
        "M_t": sp.sstr(m_t),
        "dM_W_dell": sp.sstr(dm_w),
        "dM_t_dell": sp.sstr(dm_t),
        "readout_y33": sp.sstr(y_readout),
        "readout_equals_1_over_sqrt6": is_zero(y_readout - 1 / sp.sqrt(6)),
        "contains_free_top_coefficient_input": False,
        "free_symbols_in_M_t": sorted(symbol_names(m_t)),
        "free_symbols_in_dM_t": sorted(symbol_names(dm_t)),
        "formal_transfer_rows": {
            "vacuum": sp.sstr(lambda_0),
            "W": sp.sstr(lambda_w),
            "top": sp.sstr(lambda_t),
        },
        "transfer_rows_recover_masses": {
            "W": is_zero(recovered_m_w - m_w),
            "top": is_zero(recovered_m_t - m_t),
        },
        "accepted_same_surface_transfer_backend_present": False,
        "backend_derived_from_qubit_cl3_z3_substrate": False,
        "accepted_top_pole_isolated": False,
        "accepted_w_pole_isolated": False,
        "contact_subtraction_done": False,
        "finite_volume_ir_controls_pass": False,
        "same_model_class": False,
        "same_scale_g2": "ratio-scoped candidate only",
        "proposal_allowed": False,
    }


def part2_candidate_backend_algebra() -> dict[str, Any]:
    print("\nPart 2: candidate backend algebra")
    backend = build_candidate_backend()
    check("candidate uses same source ell", backend["same_source_id"] == "ell")
    check("candidate Q_L carrier dimension is six", backend["dim_q_l_color_isospin"] == 6)
    check("candidate component is sqrt(1/6)", backend["component_amplitude"] == "sqrt(6)/6", backend["component_amplitude"])
    check("candidate top mass row is v/sqrt(12)", backend["M_t"] == "sqrt(3)*(A*ell + v_0)/6", backend["M_t"])
    check("candidate W derivative is A*g2/2", backend["dM_W_dell"] == "A*g_2/2", backend["dM_W_dell"])
    check("candidate top derivative has no free kappa", "kappa" not in backend["dM_t_dell"], backend["dM_t_dell"])
    check("candidate top row free symbols exclude kappa", "kappa" not in backend["free_symbols_in_M_t"], backend["free_symbols_in_M_t"])
    check("candidate response readout equals 1/sqrt(6)", backend["readout_equals_1_over_sqrt6"], backend["readout_y33"])
    check("formal W transfer row recovers M_W", backend["transfer_rows_recover_masses"]["W"])
    check("formal top transfer row recovers M_t", backend["transfer_rows_recover_masses"]["top"])
    check("candidate contains no free top coefficient input", backend["contains_free_top_coefficient_input"] is False)
    return backend


def part3_strict_certificate_boundary(backend: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 3: strict certificate boundary")
    required_positive_fields = {
        "accepted_same_surface_transfer_backend_present": backend["accepted_same_surface_transfer_backend_present"],
        "backend_derived_from_qubit_cl3_z3_substrate": backend["backend_derived_from_qubit_cl3_z3_substrate"],
        "same_source_id": backend["same_source_id"] == "ell",
        "coefficient_certified_dM_t_dh": backend["contains_free_top_coefficient_input"] is False,
        "coefficient_certified_dM_W_dh": True,
        "top_pole_isolated": backend["accepted_top_pole_isolated"],
        "w_pole_isolated": backend["accepted_w_pole_isolated"],
        "contact_subtraction_done": backend["contact_subtraction_done"],
        "finite_volume_ir_controls_pass": backend["finite_volume_ir_controls_pass"],
        "same_model_class": backend["same_model_class"],
        "same_scale_g2_or_ratio_scope": backend["same_scale_g2"] == "ratio-scoped candidate only",
    }
    for key, value in required_positive_fields.items():
        check(f"strict certificate field evaluated: {key}", isinstance(value, bool), value)

    strict_certificate_passes = all(required_positive_fields.values())
    check("strict certificate does not pass on candidate support alone", strict_certificate_passes is False)
    check("failure includes missing accepted backend authority", required_positive_fields["accepted_same_surface_transfer_backend_present"] is False)
    check("failure includes missing substrate derivation", required_positive_fields["backend_derived_from_qubit_cl3_z3_substrate"] is False)
    check("failure includes missing pole isolation", required_positive_fields["top_pole_isolated"] is False and required_positive_fields["w_pole_isolated"] is False)
    check("failure includes missing FV/IR controls", required_positive_fields["finite_volume_ir_controls_pass"] is False)

    return {
        "required_positive_fields": required_positive_fields,
        "strict_certificate_passes": strict_certificate_passes,
        "missing_authority_gates": [
            key for key, value in required_positive_fields.items() if value is False
        ],
    }


def part4_counterfamily_comparison(backend: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 4: counterfamily comparison")
    h, A, g2, kappa = sp.symbols("h A g_2 kappa", positive=True)
    tainted_dm_w = g2 * A / 2
    tainted_dm_t = kappa * A / sp.sqrt(2)
    tainted_readout = sp.simplify(g2 / sp.sqrt(2) * tainted_dm_t / tainted_dm_w)
    candidate_readout = sp.sympify(backend["readout_y33"])
    check("tainted counterfamily readout remains free kappa", is_zero(tainted_readout - kappa), tainted_readout)
    check("candidate readout is fixed without kappa", is_zero(candidate_readout - 1 / sp.sqrt(6)), candidate_readout)
    check("candidate is not a refutation of counterfamily no-go", backend["accepted_same_surface_transfer_backend_present"] is False)
    return {
        "tainted_readout": sp.sstr(tainted_readout),
        "candidate_readout": backend["readout_y33"],
        "counterfamily_status": "still applies to current structural support; candidate must be derived as physical backend",
    }


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "bounded-support backend candidate",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The no-kappa same-source rows compute 1/sqrt(6), but the backend "
            "is not yet derived as the accepted physical transfer/action "
            "surface and lacks strict pole/FV/IR/contact/model-class checks."
        ),
        "bare_retained_allowed": False,
        "strict_top_w_response_certificate_present": False,
        "next_action": (
            "derive this candidate backend from qubit/Cl(3) on Z^3 substrate "
            "transfer/action dynamics, or produce strict pole-row data on it"
        ),
    }
    check("actual status is bounded support, not retained", status["actual_current_surface_status"] == "bounded-support backend candidate")
    check("proposal_allowed is false", status["proposal_allowed"] is False)
    check("strict top/W certificate remains absent", status["strict_top_w_response_certificate_present"] is False)
    check("next action targets backend derivation", "derive this candidate backend" in status["next_action"])
    return status


def main() -> None:
    anchors = part1_anchors()
    backend = part2_candidate_backend_algebra()
    certificate = part3_strict_certificate_boundary(backend)
    comparison = part4_counterfamily_comparison(backend)
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_native_same_surface_top_w_transfer_action_backend_candidate_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_native_same_surface_top_w_transfer_action_backend_candidate.py",
        "anchors": anchors,
        "candidate_backend": backend,
        "strict_certificate_boundary": certificate,
        "counterfamily_comparison": comparison,
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
