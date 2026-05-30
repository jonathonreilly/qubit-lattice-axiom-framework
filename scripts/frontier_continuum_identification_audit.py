#!/usr/bin/env python3
"""
Continuum Identification Inventory Audit
========================================

STATUS: bounded-support inventory runner

PURPOSE:
  Verify that every authority note and runner in the gravity continuum
  candidate chain (19 steps) and the gauge positioning inventory exists
  on disk, and report the current audit-ledger status of those authorities.
  This is a structural inventory check, not a theorem runner for continuum
  identification and not a retained-content audit of the listed notes.

PStack experiment: frontier-continuum-identification-audit
Self-contained: json/pathlib only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0

# Resolve repo root from script location
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DOCS = REPO_ROOT / "docs"
SCRIPTS = REPO_ROOT / "scripts"


def check(name, condition, detail="", kind="EXACT"):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    msg = f"  [{status}]{tag} {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def check_note(name):
    """Check that a docs/ authority note exists."""
    path = DOCS / f"{name}.md"
    return check(f"note: {name}", path.exists(), str(path) if not path.exists() else "")


def check_runner(name):
    """Check that a scripts/ runner exists."""
    path = SCRIPTS / f"{name}.py"
    return check(f"runner: {name}", path.exists(), str(path) if not path.exists() else "")


def load_audit_rows():
    path = DOCS / "audit" / "data" / "audit_ledger.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text()).get("rows", {})


def ledger_row_for_note(rows, note_name):
    note_path = f"docs/{note_name}.md"
    for claim_id, row in rows.items():
        if row.get("note_path") == note_path:
            return claim_id, row
    return None, None


def status_counts_for_notes(rows, note_names):
    counts = {}
    missing = []
    for note_name in note_names:
        claim_id, row = ledger_row_for_note(rows, note_name)
        if row is None:
            missing.append(note_name)
            continue
        status = row.get("effective_status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    return counts, missing


# =============================================================================
# Gravity continuum chain (19 steps)
# =============================================================================

GRAVITY_CHAIN = [
    # (note_name, runner_name, description)
    ("UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE",
     "frontier_universal_gr_discrete_global_closure",
     "discrete 3+1 Einstein/Regge on PL S³ × R"),
    ("UNIVERSAL_GR_LORENTZIAN_GLOBAL_ATLAS_CLOSURE_NOTE",
     "frontier_universal_gr_lorentzian_global_atlas_closure",
     "Lorentzian global atlas extension"),
    ("UNIVERSAL_GR_LORENTZIAN_SIGNATURE_EXTENSION_NOTE",
     "frontier_universal_gr_lorentzian_signature_extension",
     "Lorentzian signature extension"),
    ("UNIVERSAL_QG_UV_FINITE_PARTITION_NOTE",
     "frontier_universal_qg_uv_finite_partition",
     "UV-finite partition-density family"),
    ("UNIVERSAL_QG_CANONICAL_REFINEMENT_NET_NOTE",
     "frontier_universal_qg_canonical_refinement_net",
     "barycentric-dyadic refinement net"),
    ("UNIVERSAL_QG_INVERSE_LIMIT_CLOSURE_NOTE",
     "frontier_universal_qg_inverse_limit_closure",
     "inverse-limit Gaussian cylinder"),
    ("UNIVERSAL_QG_ABSTRACT_GAUSSIAN_COMPLETION_NOTE",
     "frontier_universal_qg_abstract_gaussian_completion",
     "abstract Gaussian/Cameron-Martin completion"),
    ("UNIVERSAL_QG_PL_FIELD_INTERFACE_NOTE",
     "frontier_universal_qg_pl_field_interface",
     "PL field realization"),
    ("UNIVERSAL_QG_PL_WEAK_FORM_NOTE",
     "frontier_universal_qg_pl_weak_form",
     "PL weak/Dirichlet-form closure"),
    ("UNIVERSAL_QG_PL_SOBOLEV_INTERFACE_NOTE",
     "frontier_universal_qg_pl_sobolev_interface",
     "PL H¹ Sobolev interface"),
    ("UNIVERSAL_QG_EXTERNAL_FE_SMOOTH_EQUIVALENCE_NOTE",
     "frontier_universal_qg_external_fe_smooth_equivalence",
     "external FE/Galerkin smooth equivalence"),
    ("UNIVERSAL_QG_CANONICAL_TEXTBOOK_WEAK_MEASURE_EQUIVALENCE_NOTE",
     "frontier_universal_qg_canonical_textbook_weak_measure_equivalence",
     "canonical textbook weak/measure equivalence"),
    ("UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_LOCAL_IDENTIFICATION_NOTE",
     "frontier_universal_qg_smooth_gravitational_local_identification",
     "smooth local gravitational identification"),
    ("UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_ATLAS_NOTE",
     "frontier_universal_qg_smooth_gravitational_global_atlas_identification",
     "smooth finite-atlas stationary-family identification"),
    ("UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE",
     "frontier_universal_qg_smooth_gravitational_global_solution_class",
     "smooth global weak/Gaussian solution class"),
    ("UNIVERSAL_QG_CANONICAL_SMOOTH_GRAVITATIONAL_WEAK_MEASURE_NOTE",
     "frontier_universal_qg_canonical_smooth_gravitational_weak_measure",
     "canonical smooth gravitational weak/measure equivalence"),
    ("UNIVERSAL_QG_CANONICAL_SMOOTH_GEOMETRIC_ACTION_NOTE",
     "frontier_universal_qg_canonical_smooth_geometric_action",
     "canonical smooth geometric/action equivalence"),
    ("UNIVERSAL_QG_CANONICAL_TEXTBOOK_GEOMETRIC_ACTION_EQUIVALENCE_NOTE",
     "frontier_universal_qg_canonical_textbook_geometric_action_equivalence",
     "textbook Einstein-Hilbert geometric/action equivalence"),
    ("UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE",
     "frontier_universal_qg_canonical_textbook_continuum_gr_closure",
     "textbook continuum GR closure (capstone)"),
]

# =============================================================================
# Gauge continuum chain
# =============================================================================

GAUGE_CHAIN_NOTES = [
    ("NATIVE_GAUGE_CLOSURE_NOTE", "exact native SU(2) from Cl(3)"),
    ("GRAPH_FIRST_SELECTOR_DERIVATION_NOTE", "graph-first axis selector"),
    ("GRAPH_FIRST_SU3_INTEGRATION_NOTE", "structural SU(3) closure"),
    ("LEFT_HANDED_CHARGE_MATCHING_NOTE", "left-handed charge matching"),
    ("ONE_GENERATION_MATTER_CLOSURE_NOTE", "one-generation matter closure"),
    ("THREE_GENERATION_STRUCTURE_NOTE", "three-generation structure"),
    ("ALPHA_S_DERIVED_NOTE", "α_s(M_Z) = 0.1181 derivation"),
    ("CPT_EXACT_NOTE", "exact CPT on free staggered lattice"),
]

GAUGE_CHAIN_RUNNERS = [
    ("frontier_non_abelian_gauge", "native SU(2) verification"),
    ("frontier_graph_first_selector_derivation", "selector derivation"),
    ("frontier_graph_first_su3_integration", "SU(3) integration"),
    ("frontier_yt_zero_import_chain", "α_s zero-import chain"),
    ("frontier_cpt_exact", "exact CPT"),
]


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 72)
    print("Continuum Identification Inventory Audit")
    print("=" * 72)
    rows = load_audit_rows()

    # --- Gravity chain ---
    print(f"\n=== Gravity continuum chain ({len(GRAVITY_CHAIN)} steps) ===\n")
    for note, runner, desc in GRAVITY_CHAIN:
        check_note(note)
        check_runner(runner)

    gravity_notes = sum(1 for n, _, _ in GRAVITY_CHAIN if (DOCS / f"{n}.md").exists())
    gravity_runners = sum(1 for _, r, _ in GRAVITY_CHAIN if (SCRIPTS / f"{r}.py").exists())
    print(f"\n  Gravity chain: {gravity_notes}/{len(GRAVITY_CHAIN)} notes, "
          f"{gravity_runners}/{len(GRAVITY_CHAIN)} runners")

    check("All 19 gravity chain notes present",
          gravity_notes == len(GRAVITY_CHAIN),
          f"{gravity_notes}/{len(GRAVITY_CHAIN)}")
    check("All 19 gravity chain runners present",
          gravity_runners == len(GRAVITY_CHAIN),
          f"{gravity_runners}/{len(GRAVITY_CHAIN)}")

    gravity_note_names = [note for note, _, _ in GRAVITY_CHAIN]
    gravity_status_counts, gravity_missing_ledger = status_counts_for_notes(rows, gravity_note_names)
    check("Gravity ledger status inventory parsed",
          not gravity_missing_ledger,
          f"counts={gravity_status_counts}; missing={gravity_missing_ledger}",
          kind="BOUNDED")
    retained_gravity = sum(
        count for status, count in gravity_status_counts.items()
        if status in {"retained", "retained_bounded", "retained_no_go", "retained_pending_chain"}
    )
    check("Gravity content-audit closure is not yet complete on this surface",
          retained_gravity < len(GRAVITY_CHAIN),
          f"retained-like {retained_gravity}/{len(GRAVITY_CHAIN)}; counts={gravity_status_counts}",
          kind="BOUNDED")

    # --- Gauge chain ---
    print(f"\n=== Gauge continuum chain ({len(GAUGE_CHAIN_NOTES)} notes, "
          f"{len(GAUGE_CHAIN_RUNNERS)} runners) ===\n")

    for note, desc in GAUGE_CHAIN_NOTES:
        check_note(note)
    for runner, desc in GAUGE_CHAIN_RUNNERS:
        check_runner(runner)

    gauge_notes = sum(1 for n, _ in GAUGE_CHAIN_NOTES if (DOCS / f"{n}.md").exists())
    gauge_runners = sum(1 for r, _ in GAUGE_CHAIN_RUNNERS if (SCRIPTS / f"{r}.py").exists())

    check("All gauge chain notes present",
          gauge_notes == len(GAUGE_CHAIN_NOTES),
          f"{gauge_notes}/{len(GAUGE_CHAIN_NOTES)}")
    check("All gauge chain runners present",
          gauge_runners == len(GAUGE_CHAIN_RUNNERS),
          f"{gauge_runners}/{len(GAUGE_CHAIN_RUNNERS)}")

    gauge_note_names = [note for note, _ in GAUGE_CHAIN_NOTES]
    gauge_status_counts, gauge_missing_ledger = status_counts_for_notes(rows, gauge_note_names)
    check("Gauge ledger status inventory parsed",
          not gauge_missing_ledger,
          f"counts={gauge_status_counts}; missing={gauge_missing_ledger}",
          kind="BOUNDED")
    universality_rows = []
    for claim_id, row in rows.items():
        searchable = " ".join(
            str(row.get(key, "")) for key in ("title", "claim_scope", "claim_id")
        ).lower()
        if "continuum qcd" in searchable or "universality/eft" in searchable:
            universality_rows.append((claim_id, row))
    retained_universality = [
        claim_id for claim_id, row in universality_rows
        if row.get("effective_status") in {"retained", "retained_bounded", "retained_pending_chain"}
    ]
    check("Gauge universality/EFT bridge remains a reported obligation",
          True,
          f"candidate retained bridges={retained_universality or 'none found by inventory scan'}",
          kind="BOUNDED")

    # --- Capstone note ---
    print("\n=== Capstone: continuum identification positioning note ===\n")
    check_note("CONTINUUM_IDENTIFICATION_NOTE")

    # --- Summary ---
    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)

    if FAIL_COUNT > 0:
        print("\n*** MISSING FILES DETECTED — chain integrity compromised ***")
        sys.exit(1)
    else:
        print("\nAll inventory notes and runners present.")
        print("Gravity: 19/19 candidate steps present; retained content audit is separate.")
        print("Gauge: structural inventory present; universality/EFT bridge is separate.")
        sys.exit(0)


if __name__ == "__main__":
    main()
