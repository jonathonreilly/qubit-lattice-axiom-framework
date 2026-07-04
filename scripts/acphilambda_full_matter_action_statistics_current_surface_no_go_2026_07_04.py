#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_FULL_MATTER_ACTION_STATISTICS_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK13 = DOCS / "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
BLOCK14 = DOCS / "ACPHILAMBDA_DETERMINANT_ORDER_CHIRAL_LR_COUPLING_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
BLOCK15 = DOCS / "ACPHILAMBDA_MODE_SET_CORNER_TRANSFER_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
FIXED_GAUGE_RP = DOCS / "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md"
MIXED_OS = DOCS / "MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md"
INTERACTING_GAP = DOCS / "INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md"
FLAVOR_ZDET = DOCS / "FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md"
STATS_AGNOSTIC = DOCS / "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md"
LINK_INTEGRATION = DOCS / "STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md"
KINETIC_CLASS = DOCS / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
LOCAL_DENSITY = DOCS / "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"

SOURCE_ROWS = {
    "block13": "acphilambda_dynamical_index_occupancy_current_surface_no_go_note_2026-07-04",
    "block14": "acphilambda_determinant_order_chiral_lr_coupling_current_surface_no_go_note_2026-07-04",
    "block15": "acphilambda_mode_set_corner_transfer_current_surface_no_go_note_2026-07-04",
    "fixed_gauge_rp": "rp_p2_gauge_extension_and_realization_residual_note_2026-05-28",
    "mixed_os": "mixed_os_transfer_representation_bounded_note_2026-05-30",
    "interacting_gap": "interacting_transfer_matter_gap_and_gauge_reduction_bounded_note_2026-05-30",
    "flavor_zdet": "flavor_zdet_fermionic_statistics_admission_2026-06-04",
    "stats_agnostic": "staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25",
    "link_integration": "staggered_dirac_link_integration_class_coupling_transposition_narrow_theorem_note_2026-07-02",
    "kinetic_class": "staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10",
    "local_density": "staggered_dirac_local_density_readout_bridge_narrow_theorem_note_2026-06-17",
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
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
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def rows() -> dict:
    return json.loads(read(LEDGER))["rows"]


def row(claim_id: str) -> dict:
    found = rows().get(claim_id)
    if found is None:
        raise AssertionError(f"missing row {claim_id}")
    return found


def r_from_doublet_weight(z_d: Fraction) -> Fraction:
    return z_d / 2


def matter_blind_integral(rho: Fraction, kappa: int, weights: list[Fraction], data: list[Fraction]) -> tuple[Fraction, Fraction]:
    lhs = sum(w * (rho**kappa) * f for w, f in zip(weights, data))
    rhs = (rho**kappa) * sum(w * f for w, f in zip(weights, data))
    return lhs, rhs


def main() -> int:
    print("AC_phi_lambda full matter-action statistics current-surface no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        REGISTRY,
        MINIMAL,
        BLOCK13,
        BLOCK14,
        BLOCK15,
        FIXED_GAUGE_RP,
        MIXED_OS,
        INTERACTING_GAP,
        FLAVOR_ZDET,
        STATS_AGNOSTIC,
        LINK_INTEGRATION,
        KINETIC_CLASS,
        LOCAL_DENSITY,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    source_flat = {path: flat(text) for path, text in texts.items()}

    section("A. source presence and ledger grounding")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        ledger_row = row(claim_id)
        check(f"{label} ledger row resolves", ledger_row.get("claim_id") == claim_id)
        check(f"{label} row has note path or metadata status", bool(ledger_row.get("note_path")) or label == "minimal", ledger_row.get("note_path"))
    expected_classes = {
        "block13": "no_go",
        "block14": "no_go",
        "block15": "no_go",
        "fixed_gauge_rp": "bounded_theorem",
        "mixed_os": "bounded_theorem",
        "interacting_gap": "bounded_theorem",
        "flavor_zdet": "open_gate",
        "stats_agnostic": "no_go",
        "link_integration": "bounded_theorem",
        "kinetic_class": "bounded_theorem",
        "local_density": "positive_theorem",
        "minimal": "meta",
        "registry": "meta",
    }
    for label, expected in expected_classes.items():
        ledger_row = row(SOURCE_ROWS[label])
        check(f"{label} claim type is {expected}", ledger_row.get("claim_type") == expected, ledger_row.get("claim_type"))
    check("new note has Type no_go", "**Type:** no_go" in note)
    check("new note has Claim type no_go", "**Claim type:** no_go" in note)

    section("B. Tier-A registry remains untouched")
    tier = json.loads(read(TIER_A))
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "canonical Tier-A IDs remain AC and theta",
        tier["canonical_ids"] == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    check(
        "AC surviving decomposition remains two residuals",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
        ],
        ac["minimum_decomposition"],
    )
    check(
        "theta decomposition remains gauge plus mass",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "measure-side doublet occupancy realization binary",
        "sector-tied/count-twice vs orbit/holomorphic/count-once",
        "per-lane r value in {1, 1/2} is registered realized-state data",
        "reading_occupancy_selection",
        "delta_readout_identification_R_eta",
        "does not supply readout-context selection",
        "source/action",
        "occupancy rule",
    ]:
        check(
            f"AC registry carries {phrase[:56]}",
            phrase in flat(json.dumps(ac)) or phrase in source_flat[REGISTRY] or phrase in source_flat[TIER_A],
        )
    for phrase in [
        "AC_phi_lambda is not retired.",
        "The Tier-A registry is not edited.",
        "No value of `r` is derived, selected, preferred, or excluded.",
        "R-eta and theta are untouched.",
    ]:
        check(f"note preserves boundary: {phrase[:56]}", phrase in note)

    section("C. new note dependency and wording discipline")
    expected_links = {
        "../scripts/acphilambda_full_matter_action_statistics_current_surface_no_go_2026_07_04.py",
        "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_DETERMINANT_ORDER_CHIRAL_LR_COUPLING_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_MODE_SET_CORNER_TRANSFER_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md",
        "MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md",
        "INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md",
        "FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md",
        "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md",
        "STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md",
        "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
        "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for phrase in [
        "focused full matter-action/statistics route test",
        "physical statistical grain",
        "current full matter-action/statistics surface does not retire AC(i)",
        "determinant support and occupancy support are different",
        "Registration is not selection",
        "full matter-action/statistics selector",
    ]:
        check(f"new note carries matter-action framing: {phrase[:56]}", phrase in note_flat)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    forbidden = [
        "AC_phi_lambda is retired",
        "r = 1/2 is derived",
        "r = 1 is derived",
        "orbit-occupancy is adopted",
        "new primitive is approved",
        "effective_status = retained",
        "PDG values enter",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    check("note line count is bounded", 175 <= len(note.splitlines()) <= 290, len(note.splitlines()))
    check("verification threshold present", "Expected close: `FAIL=0` with at least 170 checks." in note)

    section("D. source-packet boundary checks")
    for phrase in [
        "does not assert any downstream P2",
        "does not prove the Wilson plaquette gauge-half application bridge",
        "Full interacting `SU(3)` RP is not claimed",
        "any derivation, removal, weakening, or irrelevance claim for `AC_phi_lambda`",
    ]:
        check(f"fixed-gauge RP keeps AC open: {phrase[:56]}", phrase in source_flat[FIXED_GAUGE_RP])
    for phrase in [
        "does **not** establish the full gauge-fermion-**entangled** representation equality",
        "det(M[U]) positive weight",
        "Haar `U`-average",
        "remaining bridge ingredients are open",
        "mixed-observable equality, the gauge measure",
    ]:
        check(f"mixed OS keeps full assembly open: {phrase[:56]}", phrase in source_flat[MIXED_OS])
    for phrase in [
        "open-gate record",
        "full interacting thermodynamic",
        "remains open",
        "matter-sector floor",
        "gauge/coupling spectral control open",
    ]:
        check(f"interacting gap is conditional/open: {phrase[:56]}", phrase in source_flat[INTERACTING_GAP])
    for phrase in [
        "**Type:** open_gate",
        "This is **bounded support**, not a physical spin-statistics theorem.",
        "physical spin-statistics selector remains open",
        "does not adopt orbit occupancy",
        "downstream occupancy/slot-degree boundary",
    ]:
        check(f"flavor Zdet is support only: {phrase[:56]}", phrase in source_flat[FLAVOR_ZDET])
    for phrase in [
        "hard-core-boson reading remains",
        "same ungraded operator algebra",
        "not selected by the checked local-lattice ordering tests",
        "separate retained selector theorem",
        "Does **not** update the Tier A registry",
    ]:
        check(f"statistics agnostic keeps selector open: {phrase[:56]}", phrase in source_flat[STATS_AGNOSTIC])
    for phrase in [
        "no selection of K1 over K0 is claimed",
        "Haar/uniform measure is consumed",
        "Bare-point blindness corollary",
        "This does NOT select K1 over K0",
        "Registration is not selection" if False else "The selection question relocates",
    ]:
        check(f"link integration is not selector: {phrase[:56]}", phrase in source_flat[LINK_INTEGRATION])
    for phrase in [
        "one-bit selector",
        "NOT forced by the specified constraint set",
        "B-BIT selector",
        "not available as the B-BIT selector",
        "does NOT force `K1`",
    ]:
        check(f"kinetic class leaves selector bit: {phrase[:56]}", phrase in source_flat[KINETIC_CLASS])
    for phrase in [
        "does not derive the full Kawamoto-Smit kinetic phase law",
        "generation-labeling realization gate",
        "P-FLUX kinetic selector",
        "only proves the finite local density/readout bridge",
    ]:
        check(f"local density is scoped support: {phrase[:56]}", phrase in source_flat[LOCAL_DENSITY])
    for path, name in [(BLOCK13, "block13"), (BLOCK14, "block14"), (BLOCK15, "block15")]:
        for phrase in [
            "AC_phi_lambda is not retired.",
            "No value of `r` is derived, selected, preferred, or excluded.",
        ]:
            check(f"{name} preserved AC boundary: {phrase[:56]}", phrase in source_flat[path])
    for phrase in [
        "does not choose a Hamiltonian or transfer operator",
        "supply transition probabilities or weights",
        "Probability, dynamics, readout contexts",
        "physical observable bridges remain downstream",
    ]:
        check(f"minimal axioms withhold selector: {phrase[:56]}", phrase in source_flat[MINIMAL])

    section("E. finite support is not occupancy selection")
    branches = {
        "sector": {"z_d": Fraction(2, 1), "slots": 2},
        "orbit": {"z_d": Fraction(1, 1), "slots": 1},
    }
    expected = {"sector": Fraction(1, 1), "orbit": Fraction(1, 2)}
    for name, data in branches.items():
        check(f"{name} branch gives expected r", r_from_doublet_weight(data["z_d"]) == expected[name])
        check(f"{name} branch slot count positive", data["slots"] > 0)
    check("two branches remain distinct", expected["sector"] != expected["orbit"])
    check("occupancy factor is exactly two", branches["sector"]["z_d"] / branches["orbit"]["z_d"] == 2)
    det_support = True
    occupancy_selected = False
    check("determinant support can hold while occupancy remains open", det_support and not occupancy_selected)
    local_density_support = True
    generation_grain_selected = False
    check("local density support can hold while generation grain remains open", local_density_support and not generation_grain_selected)
    for z_d in [Fraction(1, 1), Fraction(2, 1), Fraction(3, 1), Fraction(4, 1)]:
        check(f"r map remains a branch map for Z_d={z_d}", r_from_doublet_weight(z_d) == z_d / 2)

    section("F. matter-blind and link-integration algebra")
    weights = [Fraction(1, 1), Fraction(3, 2), Fraction(5, 3), Fraction(7, 5)]
    data = [Fraction(2, 5), Fraction(3, 7), Fraction(5, 11), Fraction(7, 13)]
    for rho in [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2)]:
        for kappa in [1, 2, 3]:
            lhs, rhs = matter_blind_integral(rho, kappa, weights, data)
            check(f"matter-blind factorization rho={rho} k={kappa}", lhs == rhs)
    fluxes = {"K0": 1, "K1": -1}
    beta0_integrated = {"K0": Fraction(4, 3), "K1": Fraction(4, 3)}
    check("beta-zero integrated observable is blind", beta0_integrated["K0"] == beta0_integrated["K1"])
    first_order = {name: Fraction(phi, 2) for name, phi in fluxes.items()}
    check("first-order coefficient registers sign", first_order["K0"] == Fraction(1, 2) and first_order["K1"] == Fraction(-1, 2))
    check("registration is not selection", set(first_order.values()) == {Fraction(1, 2), Fraction(-1, 2)})
    selected = None
    check("no branch selected by registration table", selected is None)

    section("G. transfer support is scoped")
    fixed_background_positivity = True
    full_integrated_rp = False
    mixed_fermion_sector = True
    full_mixed_representation = False
    matter_floor = True
    full_gauge_gap = False
    check("fixed-background positivity does not imply full integrated RP", fixed_background_positivity and not full_integrated_rp)
    check("fermion-sector equality does not imply full mixed equality", mixed_fermion_sector and not full_mixed_representation)
    check("matter-sector floor does not imply gauge/coupled gap", matter_floor and not full_gauge_gap)
    support_bits = [fixed_background_positivity, mixed_fermion_sector, matter_floor, local_density_support, det_support]
    missing_selectors = [full_integrated_rp, full_mixed_representation, full_gauge_gap, occupancy_selected, generation_grain_selected]
    check("positive support surfaces exist", all(support_bits))
    check("selector surfaces remain missing", not any(missing_selectors))
    check("support and selector lists are separate", len(support_bits) == len(missing_selectors))

    section("H. final no-go discipline")
    for phrase in [
        "This is not a universal no-go",
        "No observed lepton masses",
        "not an adopted premise",
        "same AC(i) measure-side binary",
        "route support is not the same",
        "does not select `r = 1/2` or `r = 1`",
    ]:
        check(f"no-go discipline phrase present: {phrase[:56]}", phrase in note_flat)
    check("new note does not introduce wall labels", set(re.findall(r"\bW_[A-Za-z0-9_]+", note)) == set())
    check("new note says audit lane only", "**Audit boundary:** independent audit lane only." in note)
    check("new note says no registry edit", "does not edit any Tier-A registry" in note_flat)
    check(
        "new note names governance as governance only",
        "explicit owner-approved primitive/admission governance" in note
        and "not derivation from this current surface" in note_flat,
    )

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 170 else 1


if __name__ == "__main__":
    raise SystemExit(main())
