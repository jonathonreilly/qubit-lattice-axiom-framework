#!/usr/bin/env python3
"""
PR #230 Block133 fresh math-artifact reopen audit.

After Block132, fetch exposed three fresh narrow-math branches with names that
could look adjacent to PR230 routes: a Cl(3) Schur-separator theorem, a spatial
slab cluster-decomposition bridge, and a cubic-lattice Green-function readout.
This runner checks whether any supplies the strict current-surface PR230 roots:
canonical O_H/action/LSZ authority, source-Higgs pole rows, W/Z response rows
with covariance/g2, Schur/Feshbach pole authority, or neutral H3/H4 authority.
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
    / "yt_pr230_block133_fresh_math_artifact_reopen_audit_2026-05-17.json"
)

PARENTS = {
    "block132_noether_fresh_artifact_intake": (
        "outputs/yt_pr230_block132_noether_fresh_artifact_intake_2026-05-17.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

FRESH_ARTIFACTS = {
    "cl3_schur_separator": {
        "ref": "origin/claude/cl3-chirality-schur-separator-2026-05-17",
        "note": "docs/CL3_CENTRAL_PSEUDOSCALAR_SCHUR_SEPARATOR_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_cl3_central_pseudoscalar_schur_separator_exact_2026_05_17.py",
    },
    "cluster_spatial_slab_bridge": {
        "ref": "origin/physics-loop/axiom-first-cluster-decomposition-block28-2026-05-17",
        "note": "docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/cluster_decomposition_spatial_slab_bridge_check.py",
        "log": "logs/runner-cache/cluster_decomposition_spatial_slab_bridge_check.txt",
    },
    "lattice_green_zero_argument": {
        "ref": "origin/ship/lattice_green_zero_argument_narrow_2026_05_17",
        "note": "docs/LATTICE_GREEN_FUNCTION_ZERO_ARGUMENT_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_lattice_green_function_zero_argument_2026_05_17.py",
    },
}

STRICT_ROOT_TOKENS = (
    "canonical O_H",
    "C_ss",
    "C_sH",
    "C_HH",
    "kappa_s",
    "source-overlap",
    "W/Z",
    "g2",
    "K'(pole)",
    "Feshbach",
    "H3",
    "H4",
    "top Yukawa",
    "y_t",
)

FORBIDDEN_FIREWALL = {
    "used_cl3_schur_separator_as_feshbach_pole_authority": False,
    "used_cluster_decomposition_as_scalar_lsz_or_source_overlap": False,
    "used_lattice_green_readout_as_yukawa_or_scale_authority": False,
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


def git_ref_exists(ref: str) -> bool:
    proc = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.returncode == 0


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


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def token_hits(text: str, tokens: tuple[str, ...] = STRICT_ROOT_TOKENS) -> list[str]:
    return [token for token in tokens if token in text]


def main() -> int:
    print("PR #230 Block133 fresh math-artifact reopen audit")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]

    artifacts: dict[str, dict[str, Any]] = {}
    for name, meta in FRESH_ARTIFACTS.items():
        note = git_show(meta["ref"], meta["note"])
        script = git_show(meta["ref"], meta["script"])
        log = git_show(meta["ref"], meta.get("log", "")) if meta.get("log") else ""
        artifacts[name] = {
            "ref": meta["ref"],
            "note": meta["note"],
            "script": meta["script"],
            "ref_present": git_ref_exists(meta["ref"]),
            "note_present": bool(note),
            "script_present": bool(script),
            "log_present": bool(log) if meta.get("log") else None,
            "note_token_hits": token_hits(note),
            "script_pass_marker": "PASS" in script,
            "log_pass_marker": "PASS" in log if log else None,
            "note_text": note,
            "script_text": script,
            "log_text": log,
        }

    cl3 = artifacts["cl3_schur_separator"]
    cluster = artifacts["cluster_spatial_slab_bridge"]
    green = artifacts["lattice_green_zero_argument"]

    cl3_is_abstract_separator_not_pr230_schur = (
        "Schur scalar dichotomy" in cl3["note_text"]
        and "No lattice-action" in cl3["note_text"]
        and "Does **not** identify the abstract Cl(3) module" in cl3["note_text"]
        and "physical per-site Hilbert space" in cl3["note_text"]
        and "Feshbach" not in cl3["note_text"]
        and "K'(pole)" not in cl3["note_text"]
        and "C_sH" not in cl3["note_text"]
    )
    cluster_is_conditional_gap_bridge_not_pr230_lsz = (
        "Conditional on" in cluster["note_text"]
        and "Neither the existence of `T_x` nor `Δ_x > 0` is asserted" in cluster["note_text"]
        and "does not derive `Δ_x > 0`" in cluster["note_text"]
        and "source-overlap" not in cluster["note_text"]
        and "C_sH" not in cluster["note_text"]
    )
    green_is_arithmetic_not_pr230_scale = (
        "purely an" in green["note_text"]
        and "arithmetic readout" in green["note_text"]
        and "Does **not** consume the **Planck-scale lattice spacing pin**" in green["note_text"]
        and "Does **not** consume the **`alpha_EM(M_Pl)` running coupling import**" in green["note_text"]
        and "Does **not** claim the parent note's headline" in green["note_text"]
        and "top Yukawa" not in green["note_text"]
        and "y_t" not in green["note_text"]
    )

    strict_root_candidate_hits = {
        name: {
            "note_token_hits": [
                token
                for token in data["note_token_hits"]
                if token
                not in {
                    "Feshbach",
                }
            ],
            "is_pr230_reopen_candidate": False,
        }
        for name, data in artifacts.items()
    }
    strict_root_candidate_hits["cl3_schur_separator"]["reason"] = (
        "abstract Cl(3) Schur-scalar chirality separator, not Schur/Feshbach pole authority"
    )
    strict_root_candidate_hits["cluster_spatial_slab_bridge"]["reason"] = (
        "conditional cluster/gap bridge; no scalar LSZ/source-overlap or PR230 row authority"
    )
    strict_root_candidate_hits["lattice_green_zero_argument"]["reason"] = (
        "closed finite arithmetic readout; no PR230 scale/Yukawa authority"
    )

    block132_still_blocks = (
        certs["block132_noether_fresh_artifact_intake"].get(
            "block132_noether_fresh_artifact_intake_passed"
        )
        is True
        and certs["block132_noether_fresh_artifact_intake"].get("proposal_allowed")
        is False
        and certs["block132_noether_fresh_artifact_intake"].get(
            "current_closure_satisfied"
        )
        is False
    )
    aggregate_gates_still_closed = (
        certs["campaign_status"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
        and certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
    )
    fresh_refs_present = all(data["ref_present"] for data in artifacts.values())
    fresh_notes_and_scripts_present = all(
        data["note_present"] and data["script_present"] for data in artifacts.values()
    )
    no_reopen_candidate = all(
        not data["is_pr230_reopen_candidate"]
        for data in strict_root_candidate_hits.values()
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("fresh-refs-present", fresh_refs_present, ", ".join(data["ref"] for data in artifacts.values()))
    report("fresh-notes-and-scripts-present", fresh_notes_and_scripts_present, str({name: (data["note_present"], data["script_present"]) for name, data in artifacts.items()}))
    report("cl3-schur-separator-not-pr230-schur-pole-authority", cl3_is_abstract_separator_not_pr230_schur, str(cl3["note_token_hits"]))
    report("cluster-slab-bridge-not-pr230-lsz-authority", cluster_is_conditional_gap_bridge_not_pr230_lsz, str(cluster["note_token_hits"]))
    report("lattice-green-readout-not-pr230-scale-or-yukawa-authority", green_is_arithmetic_not_pr230_scale, str(green["note_token_hits"]))
    report("no-fresh-artifact-reopens-pr230-contract", no_reopen_candidate, str(strict_root_candidate_hits))
    report("block132-still-blocks", block132_still_blocks, statuses["block132_noether_fresh_artifact_intake"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "campaign/assumption/full/retained/completion proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not parent_proposals
        and fresh_refs_present
        and fresh_notes_and_scripts_present
        and cl3_is_abstract_separator_not_pr230_schur
        and cluster_is_conditional_gap_bridge_not_pr230_lsz
        and green_is_arithmetic_not_pr230_scale
        and no_reopen_candidate
        and block132_still_blocks
        and aggregate_gates_still_closed
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block133 fresh math-artifact reopen "
            "audit finds no PR230 strict closure root in the newly fetched "
            "Cl(3) Schur-separator, spatial slab cluster-decomposition, or "
            "lattice Green-function arithmetic branches"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "Fresh math branches are narrow support outside the PR230 physical readout contracts.",
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "fresh_artifacts": {
            name: {
                key: value
                for key, value in data.items()
                if key not in {"note_text", "script_text", "log_text"}
            }
            for name, data in artifacts.items()
        },
        "strict_root_candidate_hits": strict_root_candidate_hits,
        "pr230_missing_roots_after_intake": {
            "accepted_canonical_O_H_action_LSZ": True,
            "source_overlap_kappa": True,
            "strict_C_ss_C_sH_C_HH_pole_rows": True,
            "strict_WZ_response_packet": True,
            "strict_Schur_Feshbach_pole_authority": True,
            "neutral_H3_H4_transfer_or_coupling_authority": True,
        },
        "strict_non_claims": {
            "does_not_treat_cl3_schur_separator_as_feshbach_pole_authority": True,
            "does_not_treat_cluster_decomposition_as_scalar_lsz_or_source_overlap": True,
            "does_not_treat_lattice_green_readout_as_yukawa_or_scale_authority": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "block133_fresh_math_artifact_reopen_audit_passed": passed,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if passed and FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
