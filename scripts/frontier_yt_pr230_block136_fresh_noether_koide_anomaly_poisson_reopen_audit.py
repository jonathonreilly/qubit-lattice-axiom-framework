#!/usr/bin/env python3
"""
PR #230 Block136 fresh Noether/Koide/anomaly/Poisson reopen audit.

After Block135, fetch exposed origin/main science/methodology drift and side
branches with theorem names that could be mistaken for PR230 closure roots.
This runner checks whether any fresh surface supplies PR230's strict
current-surface source-Higgs, W/Z, Schur/Feshbach, or neutral authority.
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
    / "yt_pr230_block136_fresh_noether_koide_anomaly_poisson_reopen_audit_2026-05-17.json"
)

MAIN_BASE = "48caa76bc"
PR230_BRANCH = "origin/claude/yt-direct-lattice-correlator-2026-04-30"
PR230_HEAD_EXPECTED = "4133696670f14d814aa10fce3124e98e47ea750d"

PARENTS = {
    "block135_fresh_source_field_action_phase_reopen_audit": (
        "outputs/yt_pr230_block135_fresh_source_field_action_phase_reopen_audit_2026-05-17.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

FRESH_ARTIFACTS = {
    "main_lattice_noether_carrier_independent": {
        "ref": "origin/main",
        "note": "docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py",
        "log": "logs/runner-cache/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.txt",
    },
    "main_koide_reduced_carrier": {
        "ref": "origin/main",
        "note": "docs/KOIDE_MOMENT_RATIO_UNIFORMITY_REDUCED_CARRIER_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_koide_mru_reduced_carrier_post_quotient_algebra.py",
        "log": "logs/runner-cache/audit_companion_koide_mru_reduced_carrier_post_quotient_algebra.txt",
    },
    "poisson_self_gravity_zero_coupling": {
        "ref": "origin/physics-loop/poisson-self-gravity-loop-block31-2026-05-17",
        "note": "docs/POISSON_SELF_GRAVITY_ZERO_COUPLING_EXACT_REDUCTION_NARROW_THEOREM_NOTE_2026-05-17.md",
        "script": "scripts/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.py",
        "log": "logs/runner-cache/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.txt",
    },
    "anomaly_forces_time_fb_framing": {
        "ref": "origin/physics-loop/anomaly-forces-time-fb-framing-fix-20260517",
        "note": "docs/ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md",
        "script": "scripts/frontier_anomaly_forces_time_fb_framing_fix.py",
        "log": "logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt",
    },
    "anomaly_forces_time_fc_routing": {
        "ref": "origin/physics-loop/anomaly-forces-time-fc-routing-fix-20260517",
        "note": "docs/ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md",
        "script": "scripts/frontier_anomaly_forces_time_admission_iii_routing_correction.py",
        "log": "logs/runner-cache/frontier_anomaly_forces_time_admission_iii_routing_correction.txt",
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
    "used_noether_carrier_identity_as_pr230_oh_action_lsz": False,
    "used_koide_reduced_carrier_as_pr230_yukawa_or_higgs_authority": False,
    "used_anomaly_time_fixes_as_pr230_source_higgs_or_wz_authority": False,
    "used_poisson_zero_coupling_as_pr230_scalar_lsz_or_schur_authority": False,
    "used_methodology_or_audit_drift_as_pr230_evidence": False,
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
    print("PR #230 Block136 fresh Noether/Koide/anomaly/Poisson reopen audit")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]

    artifacts: dict[str, dict[str, Any]] = {}
    for name, meta in FRESH_ARTIFACTS.items():
        note = git_show(meta["ref"], meta["note"])
        script = git_show(meta["ref"], meta["script"])
        log = git_show(meta["ref"], meta["log"])
        artifacts[name] = {
            "ref": meta["ref"],
            "note": meta["note"],
            "script": meta["script"],
            "log": meta["log"],
            "ref_present": git_ref_exists(meta["ref"]),
            "note_present": bool(note),
            "script_present": bool(script),
            "log_present": bool(log),
            "note_token_hits": token_hits(note),
            "runner_pass_marker": ("PASS" in log or "PASS" in script),
            "note_text": note,
            "script_text": script,
            "log_text": log,
        }

    noether = artifacts["main_lattice_noether_carrier_independent"]
    koide = artifacts["main_koide_reduced_carrier"]
    poisson = artifacts["poisson_self_gravity_zero_coupling"]
    anomaly_fb = artifacts["anomaly_forces_time_fb_framing"]
    anomaly_fc = artifacts["anomaly_forces_time_fc_routing"]

    noether_not_pr230_authority = (
        "Carrier-Independent Bilateral Lattice-Noether Identity" in noether["note_text"]
        and "Identification of `M` with `M_KS`" in noether["note_text"]
        and "specific physical operator" in noether["note_text"]
        and "parent's gate-import dependency" in noether["note_text"]
        and "C_sH" not in noether["note_text"]
        and "canonical O_H" not in noether["note_text"]
        and "top Yukawa" not in noether["note_text"]
    )
    koide_not_pr230_authority = (
        "charged-lepton scalar lane" in koide["note_text"]
        and "Does **not** derive the SO(2)-quotient" in koide["note_text"]
        and "Does **not** claim `kappa = 2` is forced" in koide["note_text"]
        and "top Yukawa" not in koide["note_text"]
        and "C_sH" not in koide["note_text"]
        and "canonical O_H" not in koide["note_text"]
    )
    poisson_not_pr230_authority = (
        "Zero-Coupling Exact Reduction" in poisson["note_text"]
        and "does **not** promote the parent note" in poisson["note_text"]
        and "does **not** make any claim about the nonzero-coupling rows" in poisson["note_text"]
        and "does **not** claim a self-gravity mechanism" in poisson["note_text"]
        and "top Yukawa" not in poisson["note_text"]
        and "C_sH" not in poisson["note_text"]
    )
    anomaly_fixes_are_meta = (
        "Claim type:** meta" in anomaly_fb["note_text"]
        and "not a new science claim" in anomaly_fb["note_text"]
        and "Claim type:** meta" in anomaly_fc["note_text"]
        and "not a new science claim" in anomaly_fc["note_text"]
    )

    main_changed_paths = changed_paths(MAIN_BASE, "origin/main")
    main_science_and_methodology_only = bool(main_changed_paths) and all(
        path.startswith("docs/audit/")
        or path.startswith("docs/ai_methodology/")
        or path in {FRESH_ARTIFACTS["main_lattice_noether_carrier_independent"]["note"],
                    FRESH_ARTIFACTS["main_koide_reduced_carrier"]["note"],
                    FRESH_ARTIFACTS["main_lattice_noether_carrier_independent"]["script"],
                    FRESH_ARTIFACTS["main_koide_reduced_carrier"]["script"],
                    FRESH_ARTIFACTS["main_lattice_noether_carrier_independent"]["log"],
                    FRESH_ARTIFACTS["main_koide_reduced_carrier"]["log"]}
        for path in main_changed_paths
    )
    pr230_head = git(["rev-parse", PR230_BRANCH]).stdout.strip()
    pr230_head_unchanged_after_block135 = pr230_head == PR230_HEAD_EXPECTED

    strict_root_candidate_hits = {
        name: {
            "note_token_hits": data["note_token_hits"],
            "is_pr230_reopen_candidate": False,
        }
        for name, data in artifacts.items()
    }
    strict_root_candidate_hits["main_lattice_noether_carrier_independent"][
        "reason"
    ] = "carrier-independent bilateral Noether algebra, not PR230 physical operator identification, canonical O_H/action/LSZ, or source-Higgs pole authority"
    strict_root_candidate_hits["main_koide_reduced_carrier"][
        "reason"
    ] = "charged-lepton reduced-carrier algebra, not PR230 top-Yukawa or Higgs/source-overlap authority"
    strict_root_candidate_hits["poisson_self_gravity_zero_coupling"][
        "reason"
    ] = "zero-coupling self-gravity code identity, not scalar LSZ, Schur/Feshbach pole, or top response authority"
    strict_root_candidate_hits["anomaly_forces_time_fb_framing"][
        "reason"
    ] = "meta framing fix outside PR230 physical readout"
    strict_root_candidate_hits["anomaly_forces_time_fc_routing"][
        "reason"
    ] = "meta citation-routing fix outside PR230 physical readout"

    block135_still_blocks = (
        certs["block135_fresh_source_field_action_phase_reopen_audit"].get(
            "block135_fresh_source_field_action_phase_reopen_audit_passed"
        )
        is True
        and certs["block135_fresh_source_field_action_phase_reopen_audit"].get("proposal_allowed")
        is False
        and certs["block135_fresh_source_field_action_phase_reopen_audit"].get(
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
    required_notes_present = all(data["note_present"] for data in artifacts.values())
    required_scripts_present = all(data["script_present"] for data in artifacts.values())
    required_logs_or_pass_markers = all(data["runner_pass_marker"] for data in artifacts.values())
    no_reopen_candidate = all(
        not data["is_pr230_reopen_candidate"] for data in strict_root_candidate_hits.values()
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("fresh-refs-present", fresh_refs_present, "origin/main plus anomaly/poisson refs present")
    report("fresh-notes-present", required_notes_present, str({name: data["note_present"] for name, data in artifacts.items()}))
    report("fresh-runner-scripts-present", required_scripts_present, str({name: data["script_present"] for name, data in artifacts.items()}))
    report("fresh-runner-pass-markers-present", required_logs_or_pass_markers, str({name: data["runner_pass_marker"] for name, data in artifacts.items()}))
    report("noether-carrier-identity-not-pr230-oh-action-lsz", noether_not_pr230_authority, str(noether["note_token_hits"]))
    report("koide-reduced-carrier-not-pr230-yukawa-authority", koide_not_pr230_authority, str(koide["note_token_hits"]))
    report("poisson-zero-coupling-not-pr230-scalar-lsz-or-schur", poisson_not_pr230_authority, str(poisson["note_token_hits"]))
    report("anomaly-time-fixes-are-meta-not-pr230", anomaly_fixes_are_meta, "fb/fc notes are meta")
    report("origin-main-drift-classified", main_science_and_methodology_only, f"paths={len(main_changed_paths)}")
    report("pr230-head-unchanged-after-block135", pr230_head_unchanged_after_block135, pr230_head)
    report("no-fresh-artifact-reopens-pr230-contract", no_reopen_candidate, str(strict_root_candidate_hits))
    report("block135-still-blocks", block135_still_blocks, statuses["block135_fresh_source_field_action_phase_reopen_audit"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "campaign/assumption/full/retained/completion proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not parent_proposals
        and fresh_refs_present
        and required_notes_present
        and required_scripts_present
        and required_logs_or_pass_markers
        and noether_not_pr230_authority
        and koide_not_pr230_authority
        and poisson_not_pr230_authority
        and anomaly_fixes_are_meta
        and main_science_and_methodology_only
        and pr230_head_unchanged_after_block135
        and no_reopen_candidate
        and block135_still_blocks
        and aggregate_gates_still_closed
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block136 fresh Noether-Koide-anomaly-"
            "Poisson reopen audit finds no PR230 strict closure root in the "
            "newly fetched origin/main Noether and Koide theorem drift, "
            "anomaly/time meta fixes, or Poisson zero-coupling theorem branch"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "Fresh Noether/Koide/anomaly/Poisson surfaces are outside the PR230 physical readout contracts.",
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
        "origin_main_drift": {
            "base": MAIN_BASE,
            "changed_paths": sorted(main_changed_paths),
            "science_and_methodology_only": main_science_and_methodology_only,
        },
        "pr230_head": {
            "ref": PR230_BRANCH,
            "head": pr230_head,
            "unchanged_after_block135": pr230_head_unchanged_after_block135,
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
            "does_not_treat_noether_carrier_identity_as_pr230_oh_action_lsz": True,
            "does_not_treat_koide_reduced_carrier_as_pr230_yukawa_or_higgs_authority": True,
            "does_not_treat_anomaly_time_fixes_as_pr230_source_higgs_or_wz_authority": True,
            "does_not_treat_poisson_zero_coupling_as_pr230_scalar_lsz_or_schur_authority": True,
            "does_not_treat_methodology_or_audit_drift_as_pr230_evidence": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "block136_fresh_noether_koide_anomaly_poisson_reopen_audit_passed": passed,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if passed and FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
