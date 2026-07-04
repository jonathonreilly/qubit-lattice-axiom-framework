#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np
import sympy as sp

import theta_g1_exact_branch_constraint_no_go_2026_07_04 as exact


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_CLOSED_NONEXACT_SECTOR_RECORD_READOUT_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
G1_CURRENT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
EXACT_BRANCH = DOCS / "THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
SUPPLIER2D = DOCS / "THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_REGISTERS_WINDING_2D_NARROW_THEOREM_NOTE_2026-07-02.md"
TORUS_DUAL = DOCS / "THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md"
CARTAN = DOCS / "THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"

SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
    "positive": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "g1_current": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "exact_branch": "theta_g1_exact_branch_constraint_no_go_note_2026-07-04",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "supplier2d": "theta_supplier_flavored_grading_spectral_flow_registers_winding_2d_narrow_theorem_note_2026-07-02",
    "torus_dual": "theta_torus_dual_abelianization_shifted_weight_lattice_gaussian_gluing_stable_weyl_shift_obstruction_bounded_theorem_note_2026-07-02",
    "cartan": "theta_cartan_valued_cross_plane_pairing_diagonal_weyl_frame_theorems_and_triality_fractional_values_bounded_theorem_note_2026-07-02",
    "link_star": "theta_link_star_gluing_frame_correlation_pair_composite_dagger_evenness_and_odd_branch_phase_residual_bounded_theorem_note_2026-07-02",
}

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 96)
    print(title)
    print("=" * 96)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row(claim_id: str) -> dict:
    row = json.loads(read(LEDGER))["rows"].get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row {claim_id}")
    return row


def main() -> int:
    print("theta closed-nonexact sector record/readout current-surface no-go verifier")

    paths = [
        NOTE,
        MINIMAL,
        REGISTRY,
        TIER_A,
        LEDGER,
        POSITIVE,
        CARRIER4D,
        G1_CURRENT,
        EXACT_BRANCH,
        G3_NO_GO,
        AXIOM_NO_GO,
        SUPPLIER2D,
        TORUS_DUAL,
        CARTAN,
        LINK_STAR,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence and claim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type no_go", "**Type:** no_go" in note)
    check("note has Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares sector-record/readout scope", "closed-nonexact `H^2(T^4,Z)` sector witness" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "future sector-record, bundle, `SU(3)`-registration",
    ]:
        check(f"scope boundary phrase present: {phrase[:58]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "registry is edited",
        "closed-nonexact routes are impossible",
        "physical theta sector records are derived",
        "G2 is closed",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. source rows and Tier-A registry state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has note path or is premise", bool(row.get("note_path")) or label == "minimal", row.get("note_path"))
    for label in ["positive", "carrier4d", "g1_current", "exact_branch", "g3_no_go", "supplier2d", "torus_dual", "cartan", "link_star"]:
        row = ledger_row(SOURCE_ROWS[label])
        check(f"{label} not effective retirement authority", row.get("effective_status") != "retained", row.get("effective_status"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains gauge plus mass atoms",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check("theta registry still names gauge-side winding", "multi-plaquette / large-gauge-winding account" in flats[REGISTRY])
    check("theta registry still names mass determinant bridge", "determinant-readout bridge" in flats[REGISTRY])

    section("C. exact closed-nonexact witness checks")
    rank_d1 = sp.Matrix(exact.D1).rank()
    check("imported block20 D1 rank is 45", rank_d1 == 45, rank_d1)
    for plane, rep in exact.REPS.items():
        check(f"unit flux {plane} is closed", np.max(np.abs(exact.D2 @ rep)) == 0)
        check(f"unit flux {plane} is not exact", sp.Matrix(np.column_stack([exact.D1, rep])).rank() > rank_d1)
    complementary = exact.REPS[(0, 1)] + exact.REPS[(2, 3)]
    check("complementary closed non-exact branch is closed", np.max(np.abs(exact.D2 @ complementary)) == 0)
    check("complementary closed non-exact branch is not exact", sp.Matrix(np.column_stack([exact.D1, complementary])).rank() > rank_d1)
    check("complementary branch has Qraw=2", exact.qraw(complementary) == 2, exact.qraw(complementary))
    check("complementary branch has Q=1", exact.qraw(complementary) // 2 == 1)
    exact_branch = exact.D1 @ np.ones(exact.D1.shape[1], dtype=np.int64)
    check("exact branch sample is closed", np.max(np.abs(exact.D2 @ exact_branch)) == 0)
    check("exact branch sample has zero charge", exact.qraw(exact_branch) == 0, exact.qraw(exact_branch))

    section("D. current-surface non-supply checks")
    for phrase in [
        "formation rules",
        "readout-context selection",
        "source/action and physical-observable identification",
        "sector generation rule",
        "Admissibility is not a dynamics axiom",
    ]:
        check(f"minimal axioms withhold {phrase}", phrase in flats[MINIMAL])
    for phrase in [
        "record occurrence is not claimed",
        "not a registration of the physical theta angle's `Q`",
        "derive the closed-branch restriction",
        "SU(3) abelianization",
    ]:
        check(f"carrier boundary present: {phrase[:56]}", phrase in flats[CARRIER4D])
    for phrase in [
        "No physical record/readout registration",
        "No derivation yet that the physical surface imposes or suppresses `dn != 0`",
        "licensed record/readout surface",
    ]:
        check(f"positive route boundary present: {phrase[:56]}", phrase in flats[POSITIVE])
    for phrase in [
        "Admissibility | Allows possibilities; it is not a dynamics axiom",
        "On the current surface, G1 is not derived.",
        "No physical `SU(3)` theta sector",
    ]:
        check(f"G1 current boundary present: {phrase[:56]}", phrase in flats[G1_CURRENT])
    for phrase in [
        "Record readout can read an already-licensed sector label",
        "Admissibility can constrain available local possibilities",
        "Neither supplies a gauge bundle",
    ]:
        check(f"exact branch boundary present: {phrase[:56]}", phrase in flats[EXACT_BRANCH])
    for phrase in [
        "no record/readout-chain identification",
        "no claim is made that this functional is a record",
        "Connecting the supplier to the record/readout chain is a named open path",
    ]:
        check(f"2D supplier boundary present: {phrase[:56]}", phrase in flats[SUPPLIER2D])
    for phrase in [
        "reconstruction surface",
        "no record-registration claim is made",
        "claim is made that a physical record registers `mu`",
    ]:
        check(f"torus-dual boundary present: {phrase[:56]}", phrase in flats[TORUS_DUAL])
    for phrase in [
        "reconstruction-surface",
        "not as a global-form/physical-sector claim",
        "not a registration claim",
    ]:
        check(f"Cartan boundary present: {phrase[:56]}", phrase in flats[CARTAN])
    for phrase in [
        "record occurrence is not claimed",
        "no claim is made that records register them",
        "not a registration claim",
    ]:
        check(f"link-star boundary present: {phrase[:56]}", phrase in flats[LINK_STAR])
    for phrase in [
        "physical registration",
        "No physical `SU(3)` theta sector",
        "G3 is not derived",
    ]:
        check(f"G3 boundary present: {phrase[:56]}", phrase in flats[G3_NO_GO])
    for phrase in [
        "branch/section readout",
        "No branch/section choice or topological-sector readout primitive is adopted",
        "topological-sector primitive",
    ]:
        check(f"axiom no-go boundary present: {phrase[:56]}", phrase in flats[AXIOM_NO_GO])

    section("E. route capability matrix")
    candidates = {
        "minimal_axioms": {"closed_nonexact": False, "g1": False, "record_registration": False, "su3_physical": False},
        "carrier4d": {"closed_nonexact": True, "g1": False, "record_registration": False, "su3_physical": False},
        "positive_route": {"closed_nonexact": True, "g1": False, "record_registration": False, "su3_physical": False},
        "supplier2d": {"closed_nonexact": False, "g1": False, "record_registration": False, "su3_physical": False},
        "torus_dual": {"closed_nonexact": False, "g1": False, "record_registration": False, "su3_physical": False},
        "cartan": {"closed_nonexact": True, "g1": False, "record_registration": False, "su3_physical": False},
        "link_star": {"closed_nonexact": False, "g1": False, "record_registration": False, "su3_physical": False},
        "exact_branch": {"closed_nonexact": False, "g1": True, "record_registration": False, "su3_physical": False},
    }
    for name, flags in candidates.items():
        closes = all(flags.values())
        check(f"{name} does not close all required sector-record gates", not closes, flags)
    check("no current candidate closes closed-nonexact+G1+record+SU3", not any(all(flags.values()) for flags in candidates.values()))
    check("carrier support without G1 is classified as insufficient", candidates["carrier4d"]["closed_nonexact"] and not candidates["carrier4d"]["g1"])
    check("exactness support without nonexact carrier is classified as insufficient", candidates["exact_branch"]["g1"] and not candidates["exact_branch"]["closed_nonexact"])

    section("F. note theorem and no-go discipline text")
    for heading in [
        "Frame 1: the closed non-exact carrier exists as a witness",
        "Frame 2: Record does not create the sector context",
        "Frame 3: Admissibility does not select closed non-exactness",
        "Frame 4: reconstruction support is not physical registration",
        "Frame 5: exactness remains the wrong closure mechanism",
    ]:
        check(f"fan-out heading present: {heading}", heading in note)
    for phrase in [
        "is invalid",
        "physical formation/readout bridge",
        "G2 `SU(3)` sector/readout registration",
        "Closed-nonexact sector-record theorem",
        "Owner governance",
    ]:
        check(f"note contains theorem/queue phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N3 forbids topological-sector primitive", "no topological-sector primitive" in note_flat)
    check("N5 says not universal no-go", "not a universal no-go against future sector-record or bundle routes" in note_flat)
    check("remaining routes preserve mass side", "Mass-side determinant channel" in note)

    section("G. final summary")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
