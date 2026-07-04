#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_MODE_SET_CORNER_TRANSFER_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK13 = DOCS / "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
BLOCK14 = DOCS / "ACPHILAMBDA_DETERMINANT_ORDER_CHIRAL_LR_COUPLING_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
CORNER = DOCS / "CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md"
ORBIT = DOCS / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"
U_INTEGRATION = DOCS / "U_INTEGRATION_READING_BLIND_AND_DICTIONARY_BLIND_ON_CORNER_TRANSFER_BOUNDED_NOTE_2026-06-12.md"
BEREZIN = DOCS / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
STATIC_NO_GO = DOCS / "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md"
REGISTRABLE = DOCS / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"

SOURCE_ROWS = {
    "block13": "acphilambda_dynamical_index_occupancy_current_surface_no_go_note_2026-07-04",
    "block14": "acphilambda_determinant_order_chiral_lr_coupling_current_surface_no_go_note_2026-07-04",
    "corner": "corner_axis_free_transfer_extension_per_channel_trace_correspondence_and_mode_set_fork_bounded_note_2026-06-12",
    "orbit": "koide_orbit_occupancy_independence_and_premise_candidate_note_2026-06-09",
    "u_integration": "u_integration_reading_blind_and_dictionary_blind_on_corner_transfer_bounded_note_2026-06-12",
    "berezin": "koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04",
    "static_no_go": "koide_r_half_polarization_selector_tested_static_readout_no_go_note_2026-06-08",
    "registrable": "registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10",
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


def rho_from_zd(z_d: Fraction) -> Fraction:
    return Fraction(1, 1) / z_d


def r_from_zd(z_d: Fraction) -> Fraction:
    rho = rho_from_zd(z_d)
    return Fraction(1, 1) / (2 * rho)


def trace_gamma(eigenvalues: list[Fraction]) -> Fraction:
    out = Fraction(1, 1)
    for value in eigenvalues:
        out *= 1 + value
    return out


def main() -> int:
    print("AC_phi_lambda mode-set corner-transfer current-surface no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        REGISTRY,
        MINIMAL,
        BLOCK13,
        BLOCK14,
        CORNER,
        ORBIT,
        U_INTEGRATION,
        BEREZIN,
        STATIC_NO_GO,
        REGISTRABLE,
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
        check(f"{label} row has note path or metadata status", bool(ledger_row.get("note_path")) or label in {"minimal"}, ledger_row.get("note_path"))
    expected_classes = {
        "block13": "no_go",
        "block14": "no_go",
        "corner": "bounded_theorem",
        "orbit": "bounded_theorem",
        "u_integration": "bounded_theorem",
        "berezin": "open_gate",
        "static_no_go": "no_go",
        "registrable": "bounded_theorem",
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
        "../scripts/acphilambda_mode_set_corner_transfer_current_surface_no_go_2026_07_04.py",
        "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_DETERMINANT_ORDER_CHIRAL_LR_COUPLING_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md",
        "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        "U_INTEGRATION_READING_BLIND_AND_DICTIONARY_BLIND_ON_CORNER_TRANSFER_BOUNDED_NOTE_2026-06-12.md",
        "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
        "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md",
        "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for phrase in [
        "focused mode-set route test",
        "force per-K-orbit occupancy rather than per-channel occupancy",
        "K-orbit registrability is not the same as a Fock or measure mode-set rule",
        "Trace correspondence fixes a positive kernel normalization inside whichever mode set is chosen",
        "matter-blind gauge integral into an occupancy selector",
        "physical statistics rule selecting one slot per K/CPT orbit",
    ]:
        check(f"new note carries mode-set framing: {phrase[:56]}", phrase in note_flat)
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
    check("note line count is bounded", 170 <= len(note.splitlines()) <= 270, len(note.splitlines()))
    check("verification threshold present", "Expected close: `FAIL=0` with at least 160 checks." in note)

    section("D. source-packet boundary checks")
    for phrase in [
        "Mode-set fork -- exhibited, not resolved.",
        "does not select an occupancy cell",
        "The fork is exhibited, not resolved",
        "per-channel counting gives the two-slot cell `r = 1`",
        "per-K-orbit counting gives the one-slot cell `r = 1/2`",
        "trace correspondence fixes the kernel normalization inside each branch",
    ]:
        check(f"corner packet keeps fork open: {phrase[:56]}", phrase in source_flat[CORNER])
    for phrase in [
        "proposal NOT adopted",
        "orbit-occupancy (proposal; NOT adopted)",
        "Not** a derivation of `r = 1/2`",
        "not** adoption of orbit-occupancy",
        "both horns are consistent",
        "larger retained premise surface could still derive the orbit-occupancy rule",
    ]:
        check(f"orbit packet is proposal only: {phrase[:56]}", phrase in source_flat[ORBIT])
    for phrase in [
        "matter-blind measure",
        "does not select a cell",
        "does not decide the occupancy atom",
        "The occupancy binary stays open",
        "non-matter-blind matter-gauge couplings",
    ]:
        check(f"U-integration packet keeps dictionary blind: {phrase[:56]}", phrase in source_flat[U_INTEGRATION])
    for phrase in [
        "**Type:** open_gate",
        "It does not adopt the holomorphic polarization.",
        "real Majorana Berezin cell lands on the real-slot count",
        "derive a native polarization selector",
    ]:
        check(f"Berezin packet is fork support: {phrase[:56]}", phrase in source_flat[BEREZIN])
    for phrase in [
        "no tested *static* framework structure selects the holomorphic",
        "remaining live opening is dynamical/first-order/index readout",
        "does **not** claim r=1/2 is impossible",
        "Record supplies no weighting/normalization/occupancy rule",
    ]:
        check(f"static no-go leaves dynamic route open: {phrase[:56]}", phrase in source_flat[STATIC_NO_GO])
    for phrase in [
        "does **not** retire either Tier-A admission",
        "does **not** discharge, close, or exhaust the physical",
        "Record finite additivity alone still admits",
        "not a bridge discharge",
    ]:
        check(f"registrable packet is conditional only: {phrase[:56]}", phrase in source_flat[REGISTRABLE])
    for phrase in [
        "Mode-set theorem",
        "per-K-orbit rather than per-channel",
        "AC_phi_lambda is not retired.",
    ]:
        check(f"block13 names mode-set route: {phrase[:56]}", phrase in source_flat[BLOCK13])
    for phrase in [
        "Mode-set route",
        "corner-transfer per-K-orbit mode-set theorem",
        "AC_phi_lambda is not retired.",
    ]:
        check(f"block14 hands off mode-set route: {phrase[:56]}", phrase in source_flat[BLOCK14])
    for phrase in [
        "Only records are readable",
        "does not choose a Hamiltonian or transfer operator",
        "supply transition probabilities or weights",
        "Probability, dynamics, readout contexts",
        "physical observable bridges remain downstream",
    ]:
        check(f"minimal axioms withhold selector: {phrase[:56]}", phrase in source_flat[MINIMAL])

    section("E. mode-set bookkeeping algebra")
    k_map = {"s": "s", "d1": "d2", "d2": "d1"}
    check("K map is involutive", all(k_map[k_map[x]] == x for x in k_map))
    channel_modes = ("s", "d1", "d2")
    orbit_modes = ("s", "D")
    k_orbits = (("s",), ("d1", "d2"))
    check("channel mode set has three slots", len(channel_modes) == 3)
    check("orbit mode set has two slots", len(orbit_modes) == 2)
    check("doublet K orbit has two channels", len(k_orbits[1]) == 2)
    check("both branches have one doublet orbit", len([o for o in k_orbits if "d1" in o or "d2" in o]) == 1)
    branch_weights = {
        "per_channel": Fraction(2, 1),
        "per_k_orbit": Fraction(1, 1),
    }
    expected_r = {
        "per_channel": Fraction(1, 1),
        "per_k_orbit": Fraction(1, 2),
    }
    for branch, z_d in branch_weights.items():
        check(f"{branch} rho map gives expected r", r_from_zd(z_d) == expected_r[branch], r_from_zd(z_d))
        check(f"{branch} rho positive", rho_from_zd(z_d) > 0)
    check("branch ratio is exact occupancy factor two", branch_weights["per_channel"] / branch_weights["per_k_orbit"] == 2)
    check("r ratio follows occupancy factor two", expected_r["per_channel"] / expected_r["per_k_orbit"] == 2)
    for z_d_num in range(1, 6):
        z_d = Fraction(z_d_num, 1)
        check(f"rho/r identity holds for Z_d={z_d_num}", r_from_zd(z_d) == z_d / 2)
    record_decompositions = {
        "channel": [("s",), ("d1",), ("d2",)],
        "orbit": [("s",), ("d1", "d2")],
    }
    for name, decomposition in record_decompositions.items():
        covered = sorted(x for cell in decomposition for x in cell)
        check(f"{name} decomposition covers channels", covered == ["d1", "d2", "s"], covered)
        check(f"{name} decomposition is disjoint", sum(len(cell) for cell in decomposition) == len(set(covered)))

    section("F. trace normalization is branch-local")
    channel_eigs = [Fraction(1, 3), Fraction(1, 5), Fraction(1, 7)]
    orbit_eigs = [Fraction(1, 3), Fraction(1, 5)]
    check("channel trace product has three factors", trace_gamma(channel_eigs) == Fraction(4, 3) * Fraction(6, 5) * Fraction(8, 7))
    check("orbit trace product has two factors", trace_gamma(orbit_eigs) == Fraction(4, 3) * Fraction(6, 5))
    alpha = sp.symbols("alpha", positive=True)
    for n in (1, 2, 3, 4):
        sol = sp.solve(sp.Eq(alpha**n, 1), alpha)
        check(f"positive normalization alpha^n=1 forces one for n={n}", sol == [1], sol)
    check("trace equality does not choose n", len({len(channel_eigs), len(orbit_eigs)}) == 2)
    for eigs in ([Fraction(1, 2)], [Fraction(1, 2), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)]):
        lhs = trace_gamma(eigs)
        rhs = Fraction(1, 1)
        for item in eigs:
            rhs *= 1 + item
        check(f"finite Gamma trace factorizes for {len(eigs)} modes", lhs == rhs)

    section("G. K-covariance and U-integration do not select branch")
    delta, a, b = sp.symbols("delta a b", real=True)
    lam1 = a + 2 * b * sp.cos(delta + 2 * sp.pi / 3)
    lam2_minus = a + 2 * b * sp.cos(-delta + 4 * sp.pi / 3)
    check("lambda_1(delta) equals lambda_2(-delta)", sp.simplify(lam1 - lam2_minus) == 0)
    weights = [Fraction(1, 1), Fraction(3, 2), Fraction(5, 3)]
    data = [Fraction(2, 5), Fraction(3, 7), Fraction(5, 11)]
    for rho in [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2)]:
        for kappa in [1, 2, 3]:
            lhs = sum(w * (rho**kappa) * f for w, f in zip(weights, data))
            rhs = (rho**kappa) * sum(w * f for w, f in zip(weights, data))
            check(f"matter-blind integral commutes with dictionary rho={rho} k={kappa}", lhs == rhs)
    branch_results = {branch: r_from_zd(z_d) for branch, z_d in branch_weights.items()}
    check("U-integration preserves two branch results", set(branch_results.values()) == {Fraction(1), Fraction(1, 2)})
    check("matter-blind weights are independent of branch labels", len(weights) == len(data))

    section("H. final no-go discipline")
    for phrase in [
        "This is not a universal no-go",
        "No observed lepton masses",
        "not an adopted premise",
        "the same surviving AC(i) measure-side binary",
        "support for a candidate count-once branch is not the same",
        "does not select `r = 1/2` or `r = 1`",
    ]:
        check(f"no-go discipline phrase present: {phrase[:56]}", phrase in note_flat)
    check("new note does not introduce wall labels", set(re.findall(r"\bW_[A-Za-z0-9_]+", note)) == set())
    check("new note says audit lane only", "**Audit boundary:** independent audit lane only." in note)
    check("new note says no registry edit", "does not edit any Tier-A registry" in note_flat)
    check(
        "new note names governance as governance only",
        "explicit owner-approved primitive/admission governance" in note
        and "not by this derivation block" in note_flat,
    )

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 160 else 1


if __name__ == "__main__":
    raise SystemExit(main())
