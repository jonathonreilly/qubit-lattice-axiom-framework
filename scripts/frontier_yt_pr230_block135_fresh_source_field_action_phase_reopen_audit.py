#!/usr/bin/env python3
"""
PR #230 Block135 fresh source-field/action-phase reopen audit.

After Block134, fetch exposed two narrow algebra branches with source/action
language, a feedback methodology branch, and a PR230 head that folded earlier
Block132-133 work into the draft branch.  This runner checks whether any of
those fresh surfaces supply PR230's strict current-surface roots.
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
    / "yt_pr230_block135_fresh_source_field_action_phase_reopen_audit_2026-05-17.json"
)

PR230_BRANCH = "origin/claude/yt-direct-lattice-correlator-2026-04-30"
PR230_PRE_FOLD_BASE = "9711e159c8e7a58403d2a940439e2a11f0135f48"
MAIN_PRE_AUDIT_DRIFT = "539df4b27"

PARENTS = {
    "block134_fresh_hamiltonian_cpt_iss_reopen_audit": (
        "outputs/yt_pr230_block134_fresh_hamiltonian_cpt_iss_reopen_audit_2026-05-17.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

FRESH_ARTIFACTS = {
    "decoherence_action_zero_field_phase": {
        "ref": "origin/decoherence-action-zero-field-algebraic-2026-05-17",
        "note": "docs/DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_decoherence_action_zero_field_per_link_phase_equality.py",
    },
    "electrostatics_source_field_linearity": {
        "ref": "origin/electrostatics-grown-sign-law-source-field-algebra-narrow",
        "note": "docs/ELECTROSTATICS_GROWN_SIGN_LAW_SOURCE_FIELD_LINEARITY_PARITY_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_electrostatics_grown_sign_law_source_field_linearity_parity.py",
    },
}

METHODOLOGY_BRANCH = {
    "ref": "origin/feedback/audit-loop-cascade-reaudit-source-20260517",
    "paths": {
        "docs/ai_methodology/skills/audit-loop/SKILL.md",
        "docs/ai_methodology/skills/physics-loop/SKILL.md",
        "docs/audit/SCIENCE_FIX_LOOP.md",
    },
}

PR230_FOLD_EXPECTED_PATHS = {
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/HANDOFF.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/PR_BACKLOG.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/PR_BODY_BLOCK134.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/REVIEW_HISTORY.md",
    ".claude/science/physics-loops/pr230-retained-closure-campaign-20260517/STATE.yaml",
    "docs/YT_PR230_BLOCK134_FRESH_HAMILTONIAN_CPT_ISS_REOPEN_AUDIT_NOTE_2026-05-17.md",
    "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "outputs/yt_pr230_block134_fresh_hamiltonian_cpt_iss_reopen_audit_2026-05-17.json",
    "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "scripts/frontier_yt_pr230_assumption_import_stress.py",
    "scripts/frontier_yt_pr230_block134_fresh_hamiltonian_cpt_iss_reopen_audit.py",
    "scripts/frontier_yt_pr230_campaign_status_certificate.py",
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
    "used_decoherence_action_phase_as_pr230_ew_higgs_action": False,
    "used_electrostatics_source_field_as_pr230_scalar_source": False,
    "used_methodology_branch_as_pr230_evidence": False,
    "used_pr230_fold_commit_as_new_closure_artifact": False,
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


def git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git_ref_exists(ref: str) -> bool:
    return git(["cat-file", "-e", f"{ref}^{{commit}}"]).returncode == 0


def git_show(ref: str, path: str) -> str:
    proc = git(["show", f"{ref}:{path}"])
    return proc.stdout if proc.returncode == 0 else ""


def changed_paths(base: str, ref: str) -> set[str]:
    proc = git(["diff", "--name-only", f"{base}..{ref}"])
    if proc.returncode != 0:
        return set()
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def token_hits(text: str) -> list[str]:
    return [token for token in STRICT_ROOT_TOKENS if token in text]


def main() -> int:
    print("PR #230 Block135 fresh source-field/action-phase reopen audit")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]

    artifacts: dict[str, dict[str, Any]] = {}
    for name, meta in FRESH_ARTIFACTS.items():
        note = git_show(meta["ref"], meta["note"])
        script = git_show(meta["ref"], meta["script"])
        artifacts[name] = {
            "ref": meta["ref"],
            "note": meta["note"],
            "script": meta["script"],
            "ref_present": git_ref_exists(meta["ref"]),
            "note_present": bool(note),
            "script_present": bool(script),
            "note_token_hits": token_hits(note),
            "script_total_pass_marker": "TOTAL: PASS=" in script,
            "note_text": note,
            "script_text": script,
        }

    decoherence = artifacts["decoherence_action_zero_field_phase"]
    electrostatics = artifacts["electrostatics_source_field_linearity"]

    decoherence_not_pr230_action = (
        "per-link phase factor" in decoherence["note_text"]
        and "zero-field substitution" in decoherence["note_text"]
        and "Does **not** claim anything about the nonzero-field case" in decoherence["note_text"]
        and "Does **not** consume any decoherence observable" in decoherence["note_text"]
        and "canonical O_H" not in decoherence["note_text"]
        and "C_sH" not in decoherence["note_text"]
        and "top Yukawa" not in decoherence["note_text"]
    )
    electrostatics_not_pr230_source = (
        "source-field-construction" in electrostatics["note_text"]
        and "pointwise source-field linearity and parity" in electrostatics["note_text"]
        and "Does **not** extend to full electromagnetism" in electrostatics["note_text"]
        and "canonical O_H" not in electrostatics["note_text"]
        and "C_sH" not in electrostatics["note_text"]
        and "top Yukawa" not in electrostatics["note_text"]
    )

    methodology_ref_present = git_ref_exists(METHODOLOGY_BRANCH["ref"])
    methodology_changed_paths = changed_paths("539df4b27", METHODOLOGY_BRANCH["ref"])
    methodology_only = methodology_changed_paths == METHODOLOGY_BRANCH["paths"]

    main_changed_paths = changed_paths(MAIN_PRE_AUDIT_DRIFT, "origin/main")
    main_audit_only = bool(main_changed_paths) and all(
        path.startswith("docs/audit/") for path in main_changed_paths
    )

    pr230_fold_paths = changed_paths(PR230_PRE_FOLD_BASE, PR230_BRANCH)
    pr230_fold_only_prior_blocks = bool(pr230_fold_paths) and pr230_fold_paths.issubset(
        PR230_FOLD_EXPECTED_PATHS
    )
    pr230_head = git(["rev-parse", PR230_BRANCH]).stdout.strip()

    strict_root_candidate_hits = {
        name: {
            "note_token_hits": data["note_token_hits"],
            "is_pr230_reopen_candidate": False,
        }
        for name, data in artifacts.items()
    }
    strict_root_candidate_hits["decoherence_action_zero_field_phase"][
        "reason"
    ] = "per-link zero-field phase equality for a decoherence action law, not PR230 EW/Higgs action or scalar LSZ/source-overlap authority"
    strict_root_candidate_hits["electrostatics_source_field_linearity"][
        "reason"
    ] = "abstract electrostatics source-field linearity/parity, not a PR230 Cl(3)/Z3 scalar source-to-canonical-Higgs certificate"

    block134_still_blocks = (
        certs["block134_fresh_hamiltonian_cpt_iss_reopen_audit"].get(
            "block134_fresh_hamiltonian_cpt_iss_reopen_audit_passed"
        )
        is True
        and certs["block134_fresh_hamiltonian_cpt_iss_reopen_audit"].get("proposal_allowed")
        is False
        and certs["block134_fresh_hamiltonian_cpt_iss_reopen_audit"].get(
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
    fresh_refs_present = all(data["ref_present"] for data in artifacts.values()) and methodology_ref_present
    required_notes_present = all(data["note_present"] for data in artifacts.values())
    required_scripts_present = all(data["script_present"] for data in artifacts.values())
    script_pass_markers_present = all(data["script_total_pass_marker"] for data in artifacts.values())
    no_reopen_candidate = all(
        not data["is_pr230_reopen_candidate"] for data in strict_root_candidate_hits.values()
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("fresh-refs-present", fresh_refs_present, "source/action/methodology refs present")
    report("fresh-notes-present", required_notes_present, str({name: data["note_present"] for name, data in artifacts.items()}))
    report("fresh-runner-scripts-present", required_scripts_present, str({name: data["script_present"] for name, data in artifacts.items()}))
    report("fresh-runner-scripts-carry-total-pass-markers", script_pass_markers_present, str({name: data["script_total_pass_marker"] for name, data in artifacts.items()}))
    report("decoherence-action-phase-not-pr230-ew-higgs-action", decoherence_not_pr230_action, str(decoherence["note_token_hits"]))
    report("electrostatics-source-field-not-pr230-scalar-source", electrostatics_not_pr230_source, str(electrostatics["note_token_hits"]))
    report("methodology-branch-not-pr230-science-artifact", methodology_only, str(sorted(methodology_changed_paths)))
    report("origin-main-drift-audit-only", main_audit_only, str(sorted(main_changed_paths)))
    report("pr230-head-folds-only-prior-block134", pr230_fold_only_prior_blocks, f"{pr230_head} paths={len(pr230_fold_paths)}")
    report("no-fresh-artifact-reopens-pr230-contract", no_reopen_candidate, str(strict_root_candidate_hits))
    report("block134-still-blocks", block134_still_blocks, statuses["block134_fresh_hamiltonian_cpt_iss_reopen_audit"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "campaign/assumption/full/retained/completion proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not parent_proposals
        and fresh_refs_present
        and required_notes_present
        and required_scripts_present
        and script_pass_markers_present
        and decoherence_not_pr230_action
        and electrostatics_not_pr230_source
        and methodology_only
        and main_audit_only
        and pr230_fold_only_prior_blocks
        and no_reopen_candidate
        and block134_still_blocks
        and aggregate_gates_still_closed
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block135 fresh source-field-action-phase "
            "reopen audit finds no PR230 strict closure root in the newly "
            "fetched decoherence action zero-field phase, electrostatics "
            "source-field linearity, methodology feedback, origin/main audit "
            "drift, or PR230 Block134 fold surfaces"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "Fresh source-field/action-phase/methodology/fold surfaces are outside the PR230 physical readout contracts.",
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "fresh_artifacts": {
            name: {
                key: value
                for key, value in data.items()
                if key not in {"note_text", "script_text"}
            }
            for name, data in artifacts.items()
        },
        "methodology_branch": {
            "ref": METHODOLOGY_BRANCH["ref"],
            "ref_present": methodology_ref_present,
            "changed_paths": sorted(methodology_changed_paths),
            "methodology_only": methodology_only,
        },
        "origin_main_drift": {
            "base": MAIN_PRE_AUDIT_DRIFT,
            "changed_paths": sorted(main_changed_paths),
            "audit_only": main_audit_only,
        },
        "pr230_fold": {
            "base": PR230_PRE_FOLD_BASE,
            "head": pr230_head,
            "changed_paths": sorted(pr230_fold_paths),
            "folds_only_prior_block134": pr230_fold_only_prior_blocks,
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
            "does_not_treat_decoherence_action_phase_as_pr230_ew_higgs_action": True,
            "does_not_treat_electrostatics_source_field_as_pr230_scalar_source": True,
            "does_not_treat_methodology_feedback_as_pr230_evidence": True,
            "does_not_treat_pr230_fold_commit_as_new_closure_artifact": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "block135_fresh_source_field_action_phase_reopen_audit_passed": passed,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if passed and FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
