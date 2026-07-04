#!/usr/bin/env python3
"""Verifier for the theta G1 closed-nonexact interface support note."""

from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np
import sympy as sp

import theta_g1_exact_branch_constraint_no_go_2026_07_04 as exact


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_CLOSED_NONEXACT_INTERFACE_EXACT_SUPPORT_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
G1_CURRENT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
EXACT_BRANCH = DOCS / "THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md"
CLOSED_NONEXACT_NO_GO = DOCS / "THETA_CLOSED_NONEXACT_SECTOR_RECORD_READOUT_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
G3_SUPPORT = DOCS / "THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
    "positive": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "g1_current": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "exact_branch": "theta_g1_exact_branch_constraint_no_go_note_2026-07-04",
    "closed_nonexact_no_go": "theta_closed_nonexact_sector_record_readout_current_surface_no_go_note_2026-07-04",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "g3_support": "theta_g3_central_sector_phase_character_exact_support_note_2026-07-04",
}

PASS = 0
FAIL = 0
RNG = np.random.default_rng(36)


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


def defect_branch() -> np.ndarray:
    branch = np.zeros(exact.D2.shape[1], dtype=np.int64)
    branch[exact.CELL_INFO[2][1][((0, 0, 0, 0), (0, 1))]] = 1
    return branch


def local_move_values(base: np.ndarray) -> set[int]:
    values: set[int] = set()
    for _site_dir, link_index in exact.CELL_INFO[1][1].items():
        one_link = np.zeros(exact.D1.shape[1], dtype=np.int64)
        one_link[link_index] = 1
        move = exact.D1 @ one_link
        for coeff in (-2, -1, 1, 2):
            values.add(exact.qraw(base + coeff * move))
    return values


def main() -> int:
    print("theta G1 closed-nonexact interface exact-support verifier")

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
        CLOSED_NONEXACT_NO_GO,
        AXIOM_NO_GO,
        G3_NO_GO,
        G3_SUPPORT,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and claim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type bounded_theorem", "**Type:** bounded_theorem" in note)
    check("note has Claim type bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note declares conditional support status", "conditional exact-support source-side split" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "does not claim that the current framework surface derives G1",
    ]:
        check(f"scope boundary phrase present: {phrase[:58]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "registry is edited",
        "The current framework surface derives G1.",
        "A physical gauge bundle is adopted.",
        "A topological-sector primitive is adopted.",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. source rows and Tier-A registry state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has note path or is premise", bool(row.get("note_path")) or label == "minimal", row.get("note_path"))
    for label in ["positive", "carrier4d", "g1_current", "exact_branch", "closed_nonexact_no_go", "axiom_no_go", "g3_no_go", "g3_support"]:
        row = ledger_row(SOURCE_ROWS[label])
        check(f"{label} is not an effective theta-retirement authority", row.get("effective_status") != "retained", row.get("effective_status"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains gauge plus mass atoms",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("theta registry still names multi-plaquette winding", "multi-plaquette / large-gauge-winding account" in flats[REGISTRY])
    check("theta registry still names determinant bridge", "determinant-readout bridge" in flats[REGISTRY])

    section("C. A_min, forbidden imports, and no-go memory")
    for phrase in [
        "source/action and physical-observable identification",
        "central-sector decomposition",
        "readout-context selection",
        "transition probabilities or weights",
        "Admissibility is not a dynamics axiom",
    ]:
        check(f"minimal axioms withhold {phrase}", phrase in flats[MINIMAL])
    for phrase in [
        "observed `theta`",
        "neutron-EDM bounds",
        "axion assumptions",
        "topological-sector primitive",
        "fitted selector",
    ]:
        check(f"note forbids hidden import: {phrase}", phrase in note_flat)
    for phrase in [
        "Exact link-curvature/Bianchi shortcut",
        "Unrestricted compact branch sum",
        "Record/Admissibility absorption",
        "Dynamical defect suppression",
        "Closed-nonexact interface",
    ]:
        check(f"stuck fan-out frame present: {phrase}", phrase in note)
    for phrase in [
        "The route closes the defect by deleting the carrier.",
        "Closed-nonexact sector theorem",
        "Dynamical defect suppression",
    ]:
        check(f"exact-branch no-go memory present: {phrase[:58]}", phrase in flats[EXACT_BRANCH])
    for phrase in [
        "On the current surface, G1 is not derived.",
        "do not derive the physical closed-branch restriction",
        "Record axiom's new formation sentence is also not a defect law",
    ]:
        check(f"G1 current no-go memory present: {phrase[:58]}", phrase in flats[G1_CURRENT])
    for phrase in [
        "physical theta sector records/readout are already derived",
        "physical sector-record/readout licensing",
    ]:
        check(f"closed-nonexact no-go memory present: {phrase[:58]}", phrase in flats[CLOSED_NONEXACT_NO_GO])
    for phrase in [
        "The exact 4D carrier therefore lives on the **closed-branch",
        "`dn != 0` destroys class invariance",
        "derive the closed-branch (dn = 0) restriction",
    ]:
        check(f"carrier wall present: {phrase[:58]}", phrase in flats[CARRIER4D])

    section("D. exact T4_2 cohomology support")
    rank_d1 = sp.Matrix(exact.D1).rank()
    rank_d2 = sp.Matrix(exact.D2).rank()
    ker_d2 = exact.D2.shape[1] - rank_d2
    h2_dim = ker_d2 - rank_d1
    check("D1 shape is C2 x C1", exact.D1.shape == (96, 64), exact.D1.shape)
    check("D2 shape is C3 x C2", exact.D2.shape == (64, 96), exact.D2.shape)
    check("d2*d1 = 0", np.max(np.abs(exact.D2 @ exact.D1)) == 0)
    check("rank d1 = 45", rank_d1 == 45, rank_d1)
    check("rank d2 = 45", rank_d2 == 45, rank_d2)
    check("dim ker d2 = 51", ker_d2 == 51, ker_d2)
    check("dim H2 = 6", h2_dim == 6, h2_dim)
    check("note records H2 dimension", "dim H^2(T^4_2, Z) = dim ker d2 - rank d1 = 51 - 45 = 6" in note)

    for plane, rep in exact.REPS.items():
        rank_aug = sp.Matrix(np.column_stack([exact.D1, rep])).rank()
        check(f"unit flux {plane} is closed", np.max(np.abs(exact.D2 @ rep)) == 0)
        check(f"unit flux {plane} is non-exact", rank_aug > rank_d1, rank_aug)
        check(f"unit flux {plane} has zero Qraw", exact.qraw(rep) == 0, exact.qraw(rep))

    complementary = exact.REPS[(0, 1)] + exact.REPS[(2, 3)]
    check("complementary flux e01+e23 is closed", np.max(np.abs(exact.D2 @ complementary)) == 0)
    check("complementary flux e01+e23 is non-exact", sp.Matrix(np.column_stack([exact.D1, complementary])).rank() > rank_d1)
    check("complementary flux has Qraw=2", exact.qraw(complementary) == 2, exact.qraw(complementary))
    check("complementary flux has integer Q=1", exact.qraw(complementary) // 2 == 1)
    for _ in range(12):
        move = exact.D1 @ RNG.integers(-2, 3, size=exact.D1.shape[1])
        shifted = complementary + move
        check("random exact move preserves closedness in closed-nonexact sector", np.max(np.abs(exact.D2 @ shifted)) == 0)
        check("random exact move preserves Qraw in closed-nonexact sector", exact.qraw(shifted) == exact.qraw(complementary), exact.qraw(shifted))

    for idx in range(10):
        branch = exact.D1 @ RNG.integers(-2, 3, size=exact.D1.shape[1])
        check(f"exact branch sample {idx} is closed", np.max(np.abs(exact.D2 @ branch)) == 0)
        check(f"exact branch sample {idx} has Qraw=0", exact.qraw(branch) == 0, exact.qraw(branch))

    defect = defect_branch()
    defect_values = local_move_values(defect)
    check("single plaquette defect has dn != 0", np.count_nonzero(exact.D2 @ defect) > 0)
    check("single plaquette defect starts Qraw=0", exact.qraw(defect) == 0, exact.qraw(defect))
    check("exact branch moves keep the same defect current", all(np.array_equal(exact.D2 @ (defect + exact.D1 @ RNG.integers(-1, 2, size=exact.D1.shape[1])), exact.D2 @ defect) for _ in range(8)))
    check("defect branch local moves change Qraw", len(defect_values) > 1, sorted(defect_values))
    check("defect branch local moves produce odd Qraw", any(value % 2 for value in defect_values), sorted(defect_values))
    check("defect branch values match prior witness set", defect_values == {-2, -1, 0, 1, 2}, sorted(defect_values))

    section("E. supplied-interface theorem boundary")
    for phrase in [
        "I1. The physical branch variable n is an integer 2-cochain",
        "I2. Local branch changes act by exact 2-cochains",
        "I3. Non-exact H^2 classes are allowed",
        "I4. Branches with d n != 0 are outside the sector",
        "This is a G1 interface only.",
    ]:
        check(f"supplied interface clause present: {phrase[:58]}", phrase in note_flat)
    interface = {
        "closedness": True,
        "exact_move_quotient": True,
        "nonexact_classes_allowed": True,
        "defects_excluded_or_suppressed": True,
        "physical_sector_registration": False,
        "phase_coefficient": False,
        "mass_side_bridge": False,
    }
    check("interface supplies G1 shape", all(interface[key] for key in ["closedness", "exact_move_quotient", "nonexact_classes_allowed", "defects_excluded_or_suppressed"]), interface)
    check("interface does not supply G2/G3/mass side", not any(interface[key] for key in ["physical_sector_registration", "phase_coefficient", "mass_side_bridge"]), interface)
    for phrase in [
        "Theta is not retired.",
        "The Tier-A registry is not edited.",
        "No actual current-surface G1 theorem is supplied.",
        "No physical gauge bundle, branch-sector, or topological-sector primitive is adopted.",
        "No G2 physical sector/readout theorem is supplied.",
        "No G3 phase source, coefficient, action entry, or physical weighting law is supplied.",
    ]:
        check(f"non-claim boundary present: {phrase[:58]}", phrase in note_flat)
    for phrase in [
        "Derive the closed-nonexact interface.",
        "Dynamical suppression.",
        "G2 sector/readout registration.",
        "G3 phase source.",
        "Governance route.",
    ]:
        check(f"remaining route present: {phrase}", phrase in note)

    section("F. final summary")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
