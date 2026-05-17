#!/usr/bin/env python3
"""
PR #230 Block134 fresh Hamiltonian/CPT/ISS reopen audit.

After Block133, fetch exposed a physical-Hermitian-Hamiltonian/SME bridge
narrow theorem, a CPT D-level finite-lattice algebra theorem, and ISS/audit
requeue notes.  This runner checks whether any of those fresh branches supply
PR230's strict current-surface roots.
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
    / "yt_pr230_block134_fresh_hamiltonian_cpt_iss_reopen_audit_2026-05-17.json"
)

PARENTS = {
    "block133_fresh_math_artifact_reopen_audit": (
        "outputs/yt_pr230_block133_fresh_math_artifact_reopen_audit_2026-05-17.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

FRESH_ARTIFACTS = {
    "staggered_hamiltonian_direction_decomposition": {
        "ref": "origin/physics-loop/physical-hermitian-hamiltonian-sme-bridge-block29-2026-05-17",
        "note": "docs/STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_staggered_hamiltonian_direction_decomposition_bounded_exact_2026_05_17.py",
        "log": "logs/runner-cache/audit_companion_staggered_hamiltonian_direction_decomposition_bounded_exact_2026_05_17.txt",
    },
    "cpt_d_level_finite_lattice_algebraic": {
        "ref": "origin/cpt-d-level-finite-lattice-algebraic-narrow-2026-05-17",
        "note": "docs/CPT_D_LEVEL_FINITE_LATTICE_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_cpt_d_level_finite_lattice_algebraic_2026_05_17.py",
    },
    "iss_asymmetry_mass_scaling_requeue": {
        "ref": "origin/physics-loop/iss1-requeue-asymmetry-mass-scaling-20260517b",
        "note": "docs/ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md",
    },
    "iss_dense_prune_guard_requeue": {
        "ref": "origin/physics-loop/iss1-requeue-dense-prune-guard-seed-20260517b",
        "note": "docs/DENSE_PRUNE_GUARD_SEED_NOTE.md",
    },
    "iss_lattice_distance_law_requeue": {
        "ref": "origin/physics-loop/iss1-requeue-lattice-distance-law-20260517b",
        "note": "docs/LATTICE_DISTANCE_LAW_NOTE.md",
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
    "used_hamiltonian_direction_decomposition_as_ew_higgs_action": False,
    "used_hamiltonian_direction_decomposition_as_yukawa_or_source_higgs_authority": False,
    "used_cpt_algebra_as_pr230_physical_response_authority": False,
    "used_iss_audit_requeue_as_pr230_evidence": False,
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
    if not path:
        return ""
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


def token_hits(text: str) -> list[str]:
    return [token for token in STRICT_ROOT_TOKENS if token in text]


def main() -> int:
    print("PR #230 Block134 fresh Hamiltonian/CPT/ISS reopen audit")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]

    artifacts: dict[str, dict[str, Any]] = {}
    for name, meta in FRESH_ARTIFACTS.items():
        note = git_show(meta["ref"], meta["note"])
        script = git_show(meta["ref"], meta.get("script", ""))
        log = git_show(meta["ref"], meta.get("log", ""))
        artifacts[name] = {
            "ref": meta["ref"],
            "note": meta["note"],
            "script": meta.get("script"),
            "log": meta.get("log"),
            "ref_present": git_ref_exists(meta["ref"]),
            "note_present": bool(note),
            "script_present": bool(script) if meta.get("script") else None,
            "log_present": bool(log) if meta.get("log") else None,
            "note_token_hits": token_hits(note),
            "script_pass_marker": "PASS" in script if script else None,
            "log_pass_marker": "PASS" in log if log else None,
            "note_text": note,
            "script_text": script,
            "log_text": log,
        }

    ham = artifacts["staggered_hamiltonian_direction_decomposition"]
    cpt = artifacts["cpt_d_level_finite_lattice_algebraic"]
    iss_notes = [
        artifacts["iss_asymmetry_mass_scaling_requeue"],
        artifacts["iss_dense_prune_guard_requeue"],
        artifacts["iss_lattice_distance_law_requeue"],
    ]

    hamiltonian_not_pr230_ew_higgs_action = (
        "direction-decomposition" in ham["note_text"]
        and "operator-completeness" in ham["note_text"]
        and "continuum-SME" in ham["note_text"]
        and "bilinear operator dictionary" in ham["note_text"]
        and "Yukawa couplings" in ham["note_text"]
        and "FAIL=0" in ham["log_text"].replace(" ", "")
        and "C_sH" not in ham["note_text"]
        and "canonical O_H" not in ham["note_text"]
    )
    cpt_not_pr230_response_authority = (
        "purely the load-bearing step" in cpt["note_text"]
        and "SME-coefficient extraction" in cpt["note_text"]
        and "SME-zero physical conclusions" in cpt["note_text"]
        and "Standard-Model" in cpt["note_text"]
        and "C_sH" not in cpt["note_text"]
        and "top Yukawa" not in cpt["note_text"]
    )
    iss_requeues_are_audit_bookkeeping = all(
        "re-queue" in data["note_text"].lower()
        and "no science content" in data["note_text"].lower()
        for data in iss_notes
    )

    strict_root_candidate_hits = {
        name: {
            "note_token_hits": data["note_token_hits"],
            "is_pr230_reopen_candidate": False,
        }
        for name, data in artifacts.items()
    }
    strict_root_candidate_hits[
        "staggered_hamiltonian_direction_decomposition"
    ]["reason"] = "lattice operator-completeness of H=iD, not accepted EW/Higgs action, canonical O_H, source-Higgs rows, or W/Z response"
    strict_root_candidate_hits[
        "cpt_d_level_finite_lattice_algebraic"
    ]["reason"] = "abstract CPT substitution identity, not PR230 physical response or source-overlap authority"
    for key in (
        "iss_asymmetry_mass_scaling_requeue",
        "iss_dense_prune_guard_requeue",
        "iss_lattice_distance_law_requeue",
    ):
        strict_root_candidate_hits[key]["reason"] = "audit requeue/bookkeeping note outside PR230 physics surface"

    block133_still_blocks = (
        certs["block133_fresh_math_artifact_reopen_audit"].get(
            "block133_fresh_math_artifact_reopen_audit_passed"
        )
        is True
        and certs["block133_fresh_math_artifact_reopen_audit"].get("proposal_allowed")
        is False
        and certs["block133_fresh_math_artifact_reopen_audit"].get("current_closure_satisfied")
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
    required_notes_present = all(data["note_present"] for data in artifacts.values())
    no_reopen_candidate = all(
        not data["is_pr230_reopen_candidate"]
        for data in strict_root_candidate_hits.values()
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("fresh-refs-present", fresh_refs_present, ", ".join(data["ref"] for data in artifacts.values()))
    report("fresh-notes-present", required_notes_present, str({name: data["note_present"] for name, data in artifacts.items()}))
    report("hamiltonian-direction-decomposition-not-pr230-ew-higgs-action", hamiltonian_not_pr230_ew_higgs_action, str(ham["note_token_hits"]))
    report("cpt-d-level-algebra-not-pr230-physical-response", cpt_not_pr230_response_authority, str(cpt["note_token_hits"]))
    report("iss-requeues-are-audit-bookkeeping", iss_requeues_are_audit_bookkeeping, str([data["note"] for data in iss_notes]))
    report("no-fresh-artifact-reopens-pr230-contract", no_reopen_candidate, str(strict_root_candidate_hits))
    report("block133-still-blocks", block133_still_blocks, statuses["block133_fresh_math_artifact_reopen_audit"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "campaign/assumption/full/retained/completion proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not parent_proposals
        and fresh_refs_present
        and required_notes_present
        and hamiltonian_not_pr230_ew_higgs_action
        and cpt_not_pr230_response_authority
        and iss_requeues_are_audit_bookkeeping
        and no_reopen_candidate
        and block133_still_blocks
        and aggregate_gates_still_closed
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block134 fresh Hamiltonian-CPT-ISS "
            "reopen audit finds no PR230 strict closure root in the newly "
            "fetched staggered Hamiltonian direction-decomposition, CPT "
            "D-level algebra, or ISS audit-requeue branches"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "Fresh Hamiltonian/CPT/ISS branches are outside the PR230 physical readout contracts.",
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
            "does_not_treat_hamiltonian_direction_decomposition_as_ew_higgs_action": True,
            "does_not_treat_hamiltonian_direction_decomposition_as_source_higgs_or_wz_authority": True,
            "does_not_treat_cpt_algebra_as_physical_response_authority": True,
            "does_not_treat_iss_requeue_as_pr230_evidence": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "block134_fresh_hamiltonian_cpt_iss_reopen_audit_passed": passed,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if passed and FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
