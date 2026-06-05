#!/usr/bin/env python3
"""Reproducibility checks for the three-axiom coverage audit note.

This runner is a *meta* check. It does not derive physics. It verifies that the
coverage classifications in
docs/THREE_AXIOM_COVERAGE_AUDIT_NOTE_2026-06-04.md are grounded in the
origin/main ledger as of the audit date:

  1. each cited ledger row exists and carries the effective_status the table
     claims (or, for "DERIVED" rows, a retained-grade status);
  2. the audit lane's Tier-A admitted-input count is exactly 2 (AC_phi_lambda
     and theta);
  3. the approved-primitive allowlist is exactly {minimal_axioms,
     scale_reference_primitive};
  4. the chiral-vs-vector readout arithmetic that underpins the synthesis is
     correct: a (1,1) singlet:doublet weighting gives r = 1/2 and a (1,2)
     weighting gives r = 1, with Q = 1/3 + (2/3) r mapping these to 2/3 and 1.

It sets no audit status and changes no ledger row.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
TIER_A = REPO_ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PREMISE_NODES = REPO_ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
NOTE = REPO_ROOT / "docs" / "THREE_AXIOM_COVERAGE_AUDIT_NOTE_2026-06-04.md"

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# (claim_id, allowed_effective_statuses) for each cited ledger anchor.
# These are the load-bearing rows named in the 12-item table.
CITED_ROWS = {
    # 1. gauge algebra: derived (retained)
    "native_gauge_closure_note": {"retained"},
    "graph_first_su3_integration_note": {"retained"},
    "cl3_color_automorphism_theorem": {"retained"},
    "qubit_link_u2_connection_algebra_bounded_theorem_note_2026-06-04": {"unaudited"},
    # 2. signature (3,1): derived-modulo-input (bounded bridge)
    "anomaly_forces_time_theorem": {"unaudited"},
    "single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10": {"retained"},
    "clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10": {"retained"},
    # 3. three generations: derived
    "three_generation_observable_theorem_note": {"retained"},
    "three_generation_observable_count_corollary_note_2026-05-03": {"retained"},
    "three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10": {"retained"},
    "three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02": {"retained"},
    # 4. chirality: open gap (audited_conditional / no_go realization)
    "flavor_emergent_chirality_no_transport_note_2026-05-30": {"audited_conditional"},
    "cl3_frame_free_ambient_chiral_grading_no_go_note_2026-06-02": {"unaudited"},
    "cl3_chiral_body_diagonal_axis_forced_doublet_h_not_sourced_narrow_no_go_note_2026-06-04": {"unaudited"},
    # 5. charged-lepton Koide: derived-modulo-input
    "flavor_r_half_is_a_stationary_point_not_forced_2026-06-02": {"retained_bounded"},
    "koide_r_reduces_to_chiral_vs_vector_yukawa_binary_narrow_theorem_note_2026-06-04": {"unaudited"},
    "charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10": {"retained"},
    # 6. quark/neutrino: structure derived-modulo-input
    "pmns_hw1_source_transfer_boundary_note": {"retained_bounded"},
    # 7. hypercharge: derived-modulo-input (inherits ABJ)
    "lh_doublet_su2_squared_hypercharge_anomaly_cancellation_note_2026-05-01": {"unaudited"},
    "su3_anomaly_forced_3bar_completion_theorem_note_2026-05-02": {"unaudited"},
    # 8. internal color: open gap
    "z3_character_isomorphism_color_generation_open_gate_note_2026-05-10": {"unaudited"},
    # 9. Born rule: derived-modulo-input
    "born_rule_from_gleason_busch_derivation_note_2026-05-20": {"unaudited"},
    "gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20": {"unaudited"},
    # 10. CPT: derived
    "cpt_exact_note": {"retained"},
    # 11. gravity/Planck: law derived-modulo-input
    "bh_quarter_wald_newton_coefficient_narrow_theorem_note_2026-05-10": {"retained"},
    "poisson_self_gravity_zero_coupling_exact_reduction_narrow_theorem_note_2026-05-17": {"retained"},
    # 12. Higgs/EWSB: mechanism shape retained, value open
    "ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26": {"retained"},
}

# Targets the note classes as DERIVED must have at least one retained-grade anchor.
DERIVED_ANCHORS = {
    "gauge_algebra": ["native_gauge_closure_note", "graph_first_su3_integration_note"],
    "three_generations": [
        "three_generation_observable_theorem_note",
        "three_generation_observable_count_corollary_note_2026-05-03",
    ],
    "cpt": ["cpt_exact_note"],
}


def main() -> int:
    print("=" * 72)
    print("Three-axiom coverage audit :: ledger-grounding checks")
    print("=" * 72)

    record("note file exists", NOTE.exists(), str(NOTE.name))
    record("ledger file exists", LEDGER.exists())
    record("tier_a file exists", TIER_A.exists())
    record("premise_nodes file exists", PREMISE_NODES.exists())

    ledger = json.loads(LEDGER.read_text())
    rows = ledger["rows"]

    # (1) every cited row exists with the claimed status (or retained-grade).
    for cid, allowed in CITED_ROWS.items():
        row = rows.get(cid)
        if row is None:
            record(f"cited row present: {cid}", False, "MISSING from ledger")
            continue
        es = row.get("effective_status")
        ok = es in allowed
        record(f"cited row status: {cid}", ok, f"effective_status={es} expected in {sorted(allowed)}")

    # (2) DERIVED targets are backed by >=1 retained-grade anchor.
    for target, anchors in DERIVED_ANCHORS.items():
        statuses = [rows.get(a, {}).get("effective_status") for a in anchors]
        ok = any(s in RETAINED_GRADE for s in statuses)
        record(f"DERIVED target retained-grade anchor: {target}", ok, f"anchor statuses={statuses}")

    # (3) Tier-A admitted-input count is exactly 2 (AC_phi_lambda, theta).
    tier_a = json.loads(TIER_A.read_text())
    count = tier_a.get("genuine_admitted_input_count")
    canonical = set(tier_a.get("canonical_ids", []))
    record("Tier-A genuine admitted-input count == 2", count == 2, f"count={count}")
    record(
        "Tier-A canonical ids == {staggered_dirac_realization_gate, strong_cp_theta}",
        canonical == {
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        },
        f"ids={sorted(canonical)}",
    )

    # (4) approved-primitive allowlist is exactly the two nodes.
    nodes = json.loads(PREMISE_NODES.read_text())
    canon = set(nodes.get("canonical_ids", []))
    record(
        "approved primitives == {minimal_axioms, scale_reference_primitive}",
        canon == {"minimal_axioms", "scale_reference_primitive"},
        f"ids={sorted(canon)}",
    )

    # (5) chiral-vs-vector readout arithmetic underpinning the synthesis.
    # weighting (w_s, w_d) -> x = w_s/(w_s+w_d); r = (1-x)/(2x); Q = 1/3 + (2/3) r.
    def r_of(ws: float, wd: float) -> float:
        x = ws / (ws + wd)
        return (1.0 - x) / (2.0 * x)

    def q_of(r: float) -> float:
        return 1.0 / 3.0 + (2.0 / 3.0) * r

    r_vector = r_of(1.0, 2.0)   # (1,2) vector/real readout
    r_chiral = r_of(1.0, 1.0)   # (1,1) chiral/holomorphic readout
    record("vector (1,2) readout gives r = 1", abs(r_vector - 1.0) < 1e-12, f"r={r_vector}")
    record("chiral (1,1) readout gives r = 1/2", abs(r_chiral - 0.5) < 1e-12, f"r={r_chiral}")
    record("Q(r=1) == 1 (det_R / vector lane)", abs(q_of(1.0) - 1.0) < 1e-12, f"Q={q_of(1.0)}")
    record("Q(r=1/2) == 2/3 (charged-lepton lane)", abs(q_of(0.5) - 2.0 / 3.0) < 1e-12, f"Q={q_of(0.5)}")
    record("Q(r=0) == 1/3 (unbroken-S3 lane)", abs(q_of(0.0) - 1.0 / 3.0) < 1e-12, f"Q={q_of(0.0)}")

    # (6) a uniform complex-mode rescale of (1,2) -> (1/2,1) is proportional to
    #     (1,2) and still gives r = 1 (the objection answered in the note).
    r_uniform = r_of(0.5, 1.0)
    record("uniform complex rescale (1/2,1) still gives r = 1", abs(r_uniform - 1.0) < 1e-12, f"r={r_uniform}")

    # (7) note declares claim_type meta and adds no axiom/import.
    text = NOTE.read_text()
    record("note declares claim_type meta", "claim_type_author_hint: meta" in text)
    record(
        "note disclaims status/axiom changes",
        "changes no row's `effective_status`" in text and "adds no axiom" in text,
    )

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
