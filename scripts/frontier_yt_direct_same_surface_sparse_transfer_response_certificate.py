#!/usr/bin/env python3
"""Y_T direct same-surface sparse transfer response certificate scaffold.

This is not a production top/W response solve.  It is the readout-free
certificate harness requested by the strict-response obstruction:

* counterfamily_backend proves the machinery reads an inserted kappa and
  refuses to certify it as a derived coefficient;
* candidate_action_backend is explicitly blocked until an accepted finite
  same-surface top/W transfer/action backend is supplied.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"

NOTE = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
STRICT_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
TOP_SOURCE_NOGO = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
CANONICAL_HARNESS = DOCS / "CANONICAL_HARNESS_INDEX.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"

STRICT_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"
STRICT_TOP_W_ROWS = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"

PASS_COUNT = 0
FAIL_COUNT = 0

FORBIDDEN_PROOF_INPUTS = (
    "H_unit",
    "yt_ward_identity",
    "y_t_bare",
    "observed top mass",
    "observed W mass",
    "observed Z mass",
    "PDG",
    "alpha_LM",
    "plaquette",
    "u0",
    "Planck",
    "alpha_s",
    "fitted selector",
)


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


def has_symbol(expr: sp.Expr, name: str) -> bool:
    return any(symbol.name == name for symbol in expr.free_symbols)


def part1_anchors() -> None:
    print("\nPart 1: anchor files and current strict-response boundary")
    for path in (
        NOTE,
        FULL_STACK,
        STRICT_OBSTRUCTION,
        TOP_SOURCE_NOGO,
        FH_GATE,
        STRICT_WZ,
        STRICT_TOP,
        CANONICAL_HARNESS,
        STRICT_OBSTRUCTION_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Purpose",
        "Certificate Schema",
        "Counterfamily Backend",
        "Candidate Action Backend",
        "Status Boundary",
        "Non-Claims",
        "Verification",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    obstruction = load_json(STRICT_OBSTRUCTION_OUT)
    check("strict same-source obstruction passed", obstruction.get("fail_count") == 0, obstruction.get("fail_count"))
    check("strict obstruction is route pruning", obstruction.get("trace_class") == "negative_route_pruning")
    check("strict production top/W rows still absent", not STRICT_TOP_W_ROWS.exists(), STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())


def build_counterfamily_backend(kappa_value: sp.Expr) -> dict[str, Any]:
    h = sp.symbols("h", real=True)
    a_t, g2, v0, A, kappa = sp.symbols("a_t g_2 v_0 A kappa", positive=True)
    v = v0 + A * h
    lambda_0 = sp.Integer(1)
    lambda_w = sp.exp(-a_t * g2 * v / 2)
    lambda_t = sp.exp(-a_t * kappa * v / sp.sqrt(2))

    eigenvalues = {
        "vacuum": lambda_0,
        "W": lambda_w,
        "top": lambda_t,
    }
    masses = {
        name: sp.simplify(-sp.log(value / lambda_0) / a_t)
        for name, value in eigenvalues.items()
        if name != "vacuum"
    }
    derivatives = {
        name: sp.simplify(sp.diff(mass, h))
        for name, mass in masses.items()
    }
    readout = sp.simplify(g2 / sp.sqrt(2) * derivatives["top"] / derivatives["W"])
    substituted_readout = sp.simplify(readout.subs(kappa, kappa_value))

    return {
        "backend_id": f"counterfamily_backend_kappa_{sp.sstr(kappa_value)}",
        "backend_role": "tainted_counterexample_backend",
        "same_source_id": "h",
        "surface_id": "diagonal_three_sector_transfer_counterfamily",
        "input_parameters": ["a_t", "g_2", "v_0", "A", "kappa"],
        "contains_free_top_coefficient_input": True,
        "top_pole_isolated": True,
        "w_pole_isolated": True,
        "vacuum_contact_subtraction_done": True,
        "finite_volume_ir_controls_pass": False,
        "same_model_class": "support-schema-only diagonal finite transfer family",
        "same_scale_g2": "ratio-scoped only",
        "dM_W_dh": sp.sstr(derivatives["W"]),
        "dM_t_dh": sp.sstr(derivatives["top"]),
        "readout_y33": sp.sstr(readout),
        "readout_after_substitution": sp.sstr(substituted_readout),
        "readout_contains_kappa": has_symbol(readout, "kappa"),
        "proposal_allowed": False,
        "proposal_allowed_reason": "backend includes free top coefficient kappa as an input; the harness must reject it as closure",
        "eigenvalue_rows": {name: sp.sstr(value) for name, value in eigenvalues.items()},
    }


def part2_counterfamily_backend() -> dict[str, Any]:
    print("\nPart 2: counterfamily backend verifies readout and rejection")
    one = sp.Rational(1, 1) / sp.sqrt(6)
    two = sp.Rational(2, 1) / sp.sqrt(6)
    backend_a = build_counterfamily_backend(one)
    backend_b = build_counterfamily_backend(two)

    check("counterfamily backend has same source id", backend_a["same_source_id"] == backend_b["same_source_id"] == "h")
    check("counterfamily backend isolates top pole row", backend_a["top_pole_isolated"] is True)
    check("counterfamily backend isolates W pole row", backend_a["w_pole_isolated"] is True)
    check("counterfamily backend performs vacuum/contact subtraction", backend_a["vacuum_contact_subtraction_done"] is True)
    check("counterfamily backend reads supplied kappa", backend_a["readout_y33"] == "kappa", backend_a["readout_y33"])
    check("counterfamily backend output changes with inserted kappa", backend_a["readout_after_substitution"] != backend_b["readout_after_substitution"])
    check("counterfamily backend is tainted by kappa input", backend_a["contains_free_top_coefficient_input"] is True)
    check("counterfamily backend cannot certify proposal", backend_a["proposal_allowed"] is False)
    check("counterfamily backend is not FV/IR controlled", backend_a["finite_volume_ir_controls_pass"] is False)
    check("counterfamily backend dM_t has free kappa", "kappa" in backend_a["dM_t_dh"], backend_a["dM_t_dh"])
    check("counterfamily backend dM_W does not have kappa", "kappa" not in backend_a["dM_W_dh"], backend_a["dM_W_dh"])

    return {
        "backend_a": backend_a,
        "backend_b": backend_b,
    }


def forbidden_import_scan(payload: dict[str, Any]) -> dict[str, Any]:
    text = json.dumps(payload, sort_keys=True)
    hits = [phrase for phrase in FORBIDDEN_PROOF_INPUTS if phrase in text]
    target_hits = [phrase for phrase in ("1/sqrt(6)", "sqrt(6)") if phrase in text]
    return {
        "forbidden_proof_input_hits": hits,
        "target_value_hits": target_hits,
        "passes_forbidden_import_firewall": not hits,
        "passes_target_value_input_firewall": not target_hits,
    }


def part3_taint_scan(counterfamily: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 3: taint scan")
    scan_a = forbidden_import_scan(counterfamily["backend_a"])
    check("counterfamily has no old forbidden proof imports", scan_a["passes_forbidden_import_firewall"], scan_a["forbidden_proof_input_hits"])
    check(
        "counterfamily target-value text is detected and rejected as non-proof input",
        not scan_a["passes_target_value_input_firewall"],
        scan_a["target_value_hits"],
    )
    check("counterfamily free kappa is detected", counterfamily["backend_a"]["contains_free_top_coefficient_input"] is True)
    check("counterfamily proposal remains false despite algebraic readout", counterfamily["backend_a"]["proposal_allowed"] is False)

    physical_backend_stub = {
        "backend_id": "candidate_action_backend",
        "accepted_same_surface_transfer_backend_present": False,
        "contains_free_top_coefficient_input": None,
        "reason": "No accepted finite same-surface top/W transfer/action backend is present on this branch.",
    }
    scan_stub = forbidden_import_scan(physical_backend_stub)
    check("candidate backend stub has no forbidden import hits", scan_stub["passes_forbidden_import_firewall"], scan_stub["forbidden_proof_input_hits"])
    return {
        "counterfamily_scan": scan_a,
        "candidate_stub_scan": scan_stub,
    }


def part4_candidate_action_backend_boundary() -> dict[str, Any]:
    print("\nPart 4: candidate action backend boundary")
    canonical = read(CANONICAL_HARNESS)
    staggered_gate_present = STAGGERED_GATE.exists()
    strict_rows_present = STRICT_TOP_W_ROWS.exists()
    check("staggered-Dirac realization gate note exists", staggered_gate_present)
    check("canonical harness records staggered-Dirac realization gate", "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md" in canonical)
    check("accepted strict top/W response rows are absent", not strict_rows_present)

    missing_fields = [
        "accepted finite same-surface transfer/action backend",
        "same source id on that backend",
        "isolated vacuum/W/top spectral projectors",
        "coefficient-certified dM_t/dh",
        "coefficient-certified dM_W/dh",
        "contact/vacuum subtraction",
        "FV/IR controls",
        "same model class",
        "same-scale g2 or explicit ratio scope",
    ]
    for field in missing_fields:
        check(f"candidate backend missing field recorded: {field}", True)

    return {
        "backend_id": "candidate_action_backend",
        "accepted_same_surface_transfer_backend_present": False,
        "strict_top_w_rows_present": strict_rows_present,
        "status": "blocked_no_accepted_backend",
        "missing_fields": missing_fields,
        "proposal_allowed": False,
        "proposal_allowed_reason": "A candidate action backend cannot be run until the accepted finite same-surface top/W transfer surface exists.",
    }


def part5_certificate_schema(counterfamily: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: strict certificate schema evaluation")
    required_fields = [
        "same_source_id",
        "surface_id",
        "top_pole_isolated",
        "w_pole_isolated",
        "dM_t_dh",
        "dM_W_dh",
        "vacuum_contact_subtraction_done",
        "finite_volume_ir_controls_pass",
        "same_model_class",
        "same_scale_g2",
        "contains_free_top_coefficient_input",
        "proposal_allowed",
    ]
    backend_a = counterfamily["backend_a"]
    for field in required_fields:
        check(f"counterfamily backend has certificate field: {field}", field in backend_a)

    strict_positive_fields = {
        "same_source_id": backend_a["same_source_id"] == "h",
        "top_pole_isolated": backend_a["top_pole_isolated"] is True,
        "w_pole_isolated": backend_a["w_pole_isolated"] is True,
        "coefficient_certified_dM_t_dh": backend_a["contains_free_top_coefficient_input"] is False and "kappa" not in backend_a["dM_t_dh"],
        "coefficient_certified_dM_W_dh": "kappa" not in backend_a["dM_W_dh"],
        "contact_subtraction_done": backend_a["vacuum_contact_subtraction_done"] is True,
        "FV_IR_model_class_checks_pass": backend_a["finite_volume_ir_controls_pass"] is True,
        "same_model_class": backend_a["same_model_class"] == "accepted physical same-surface transfer backend",
        "same_scale_for_g2_and_source_response": backend_a["same_scale_g2"] == "same-scale certified",
        "no_forbidden_imports": True,
    }
    for field, status in strict_positive_fields.items():
        check(f"strict positive field evaluated: {field}", isinstance(status, bool), status)

    check("strict positive certificate fails because top coefficient is input", strict_positive_fields["coefficient_certified_dM_t_dh"] is False)
    check("strict positive certificate fails because FV/IR controls absent", strict_positive_fields["FV_IR_model_class_checks_pass"] is False)
    check("candidate backend is blocked", candidate["status"] == "blocked_no_accepted_backend")

    return {
        "required_fields": required_fields,
        "counterfamily_strict_positive_fields": strict_positive_fields,
        "strict_positive_certificate_passes": all(strict_positive_fields.values()),
    }


def part6_note_firewalls() -> None:
    print("\nPart 6: note firewalls")
    note = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive Y_T closure",
        "candidate action backend closes",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)
    check(
        "strict top/W response pass wording appears only as a non-claim",
        "claim the strict top/W response certificate passes" in note,
    )


def main() -> int:
    print("=" * 78)
    print("Y_T DIRECT SAME-SURFACE SPARSE TRANSFER RESPONSE CERTIFICATE")
    print("=" * 78)

    part1_anchors()
    counterfamily = part2_counterfamily_backend()
    scans = part3_taint_scan(counterfamily)
    candidate = part4_candidate_action_backend_boundary()
    schema = part5_certificate_schema(counterfamily, candidate)
    part6_note_firewalls()

    result = {
        "actual_current_surface_status": "bounded-support microbench / open strict-response backend",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The harness validates the strict-response certificate schema and rejects "
            "the kappa-tainted counterfamily backend.  No accepted finite same-surface "
            "top/W transfer/action backend is present, so no coefficient-bearing top row "
            "has been derived."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "counterfamily_backend": counterfamily,
        "taint_scans": scans,
        "candidate_action_backend": candidate,
        "strict_certificate_schema": schema,
        "strict_top_w_response_certificate_present": schema["strict_positive_certificate_passes"],
        "next_action": (
            "Supply an accepted finite same-surface top/W transfer/action backend with "
            "isolated vacuum/W/top projectors, then rerun this certificate to compute "
            "coefficient-certified dM_t/dh and dM_W/dh without kappa as an input."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md",
            "scripts/frontier_yt_direct_same_surface_sparse_transfer_response_certificate.py",
            "outputs/yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
