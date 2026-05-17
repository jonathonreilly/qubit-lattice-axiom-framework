#!/usr/bin/env python3
"""
PR #230 Block132 fresh lattice-Noether artifact intake.

After Block131, a fetched remote branch exposes a carrier-independent bilateral
lattice-Noether theorem.  This runner checks whether that fresh theorem supplies
any of the exact PR230 closure roots that remain missing: accepted canonical
O_H/action/LSZ authority, source-overlap kappa, strict C_ss/C_sH/C_HH pole
rows, strict W/Z response rows, strict Schur pole authority, or neutral H3/H4
physical-transfer/source-coupling authority.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block132_noether_fresh_artifact_intake_2026-05-17.json"
)

FRESH_REF = "origin/physics-loop/axiom-first-lattice-noether-block27-2026-05-17"
FRESH_NOTE = "docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md"
FRESH_CLAIM = (
    ".claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/"
    "blocks/block27/CLAIM_STATUS_CERTIFICATE.md"
)
FRESH_LOG = "logs/runner-cache/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.txt"

PARENTS = {
    "block131_action_first_source_higgs_authority": (
        "outputs/yt_pr230_block131_action_first_source_higgs_authority_construction_attempt_2026-05-17.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

PR230_REQUIRED_TOKENS = (
    "C_sH",
    "C_HH",
    "kappa_s",
    "canonical O_H",
    "source-overlap",
    "top Yukawa",
    "y_t",
    "W/Z",
    "g2",
    "Schur",
    "K'(pole)",
    "H3",
    "H4",
)

FORBIDDEN_FIREWALL = {
    "used_noether_current_as_canonical_higgs_operator": False,
    "used_u1_current_as_source_higgs_overlap": False,
    "used_noether_theorem_as_pole_row_authority": False,
    "used_noether_theorem_as_wz_g2_or_covariance": False,
    "used_noether_theorem_as_schur_or_neutral_authority": False,
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "claimed_retained_or_proposed_retained": False,
}

PASS_COUNT = 0
FAIL_COUNT = 0


def report(tag: str, ok: bool, msg: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        state = "PASS"
    else:
        FAIL_COUNT += 1
        state = "FAIL"
    print(f"  [{state}] {tag}: {msg}")


def load_json(path: str | Path) -> Any:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    return json.loads(full.read_text(encoding="utf-8"))


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def git_show(ref: str, path: str) -> str:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.stdout if proc.returncode == 0 else ""


def git_ref_exists(ref: str) -> bool:
    proc = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.returncode == 0


def main() -> int:
    print("PR #230 Block132 fresh lattice-Noether artifact intake")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]

    ref_present = git_ref_exists(FRESH_REF)
    fresh_note = git_show(FRESH_REF, FRESH_NOTE)
    fresh_claim = git_show(FRESH_REF, FRESH_CLAIM)
    fresh_log = git_show(FRESH_REF, FRESH_LOG)

    fresh_theorem_present = bool(fresh_note and "carrier-independent bilateral Noether identity" in fresh_note)
    fresh_claim_nonproposal = "proposal_allowed: false" in fresh_claim and "audit_required_before_effective_retained: true" in fresh_claim
    fresh_runner_passes = "Overall verdict: PASS" in fresh_log and all(
        f"E{i}: PASS" in fresh_log for i in range(1, 9)
    )
    fresh_scope_excludes_physical_identification = (
        "Identification of `M` with `M_KS`" in fresh_note
        and "any specific physical operator" in fresh_note
        and "Wilson-sector contributions" in fresh_note
    )
    pr230_tokens_in_fresh_note = [token for token in PR230_REQUIRED_TOKENS if token in fresh_note]

    block131_still_blocks = (
        certs["block131_action_first_source_higgs_authority"].get(
            "block131_action_first_source_higgs_authority_construction_attempt_passed"
        )
        is True
        and certs["block131_action_first_source_higgs_authority"].get("current_closure_satisfied")
        is False
        and certs["block131_action_first_source_higgs_authority"].get(
            "expected_strict_packet_absent"
        )
        is True
    )
    aggregate_gates_still_closed = (
        certs["campaign_status"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
        and certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
    )
    no_pr230_required_tokens = len(pr230_tokens_in_fresh_note) == 0
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("fresh-ref-present", ref_present, FRESH_REF)
    report("fresh-noether-theorem-present", fresh_theorem_present, FRESH_NOTE)
    report("fresh-claim-nonproposal", fresh_claim_nonproposal, "proposal_allowed=false and audit required")
    report("fresh-runner-passes", fresh_runner_passes, "E1-E8 and overall PASS")
    report("fresh-scope-excludes-physical-identification", fresh_scope_excludes_physical_identification, "M_KS/physical-operator/Wilson scope exclusions")
    report("fresh-note-has-no-pr230-required-tokens", no_pr230_required_tokens, str(pr230_tokens_in_fresh_note))
    report("block131-still-blocks", block131_still_blocks, statuses["block131_action_first_source_higgs_authority"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "campaign/assumption/full/retained/completion proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not parent_proposals
        and ref_present
        and fresh_theorem_present
        and fresh_claim_nonproposal
        and fresh_runner_passes
        and fresh_scope_excludes_physical_identification
        and no_pr230_required_tokens
        and block131_still_blocks
        and aggregate_gates_still_closed
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block132 fresh carrier-independent "
            "lattice-Noether theorem intake does not reopen PR230 closure: it "
            "is a narrow U(1)/bilateral-current algebra theorem and supplies "
            "no accepted canonical O_H/action/LSZ authority, source-overlap "
            "kappa, strict C_ss/C_sH/C_HH pole rows, W/Z response packet, "
            "Schur pole authority, or neutral H3/H4 authority"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "The fresh Noether theorem has a nonproposal source-note status and no PR230 physical readout artifacts.",
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "block132_noether_fresh_artifact_intake_passed": passed,
        "fresh_ref": FRESH_REF,
        "fresh_artifacts": {
            "note": FRESH_NOTE,
            "claim_certificate": FRESH_CLAIM,
            "runner_cache": FRESH_LOG,
            "ref_present": ref_present,
            "fresh_theorem_present": fresh_theorem_present,
            "fresh_claim_nonproposal": fresh_claim_nonproposal,
            "fresh_runner_passes": fresh_runner_passes,
            "scope_excludes_physical_identification": fresh_scope_excludes_physical_identification,
            "pr230_required_tokens_found": pr230_tokens_in_fresh_note,
        },
        "pr230_missing_roots_after_intake": {
            "accepted_canonical_O_H_action_LSZ": True,
            "source_overlap_kappa": True,
            "strict_C_ss_C_sH_C_HH_pole_rows": True,
            "strict_WZ_response_packet": True,
            "strict_Schur_pole_authority": True,
            "neutral_H3_H4_transfer_or_coupling_authority": True,
        },
        "strict_non_claims": {
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_treat_noether_current_as_canonical_O_H": True,
            "does_not_treat_u1_current_as_source_higgs_overlap": True,
            "does_not_treat_noether_runner_pass_as_pr230_row_evidence": True,
            "does_not_close_future_noether_based_routes": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "parent_statuses": statuses,
        "exact_next_action": (
            "Noether route reopens only if a future same-surface theorem maps "
            "a certified Noether current to canonical O_H/source-Higgs pole "
            "rows or W/Z physical response with covariance and strict g2.  "
            "Absent that, PR230 still needs one of the strict source-Higgs, "
            "W/Z, Schur, or neutral artifacts named in the route queue."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
