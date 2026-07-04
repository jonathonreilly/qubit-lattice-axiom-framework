#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G4_THETA_BAR_ASSEMBLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
STRUCTURED = DOCS / "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md"
THETA_ZERO = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"
GAUGE_STATUS = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
ASSEMBLY = DOCS / "THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md"
G1_CARRIER = DOCS / "THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
G1_DEFECT = DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
G3_PHASE = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MASS_W2 = DOCS / "THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md"
MASS_READY = DOCS / "THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md"

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


def ledger_row_by_path(path: str) -> dict | None:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if not matches:
        return None
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def main() -> int:
    print("Theta G4 theta-bar assembly current-surface no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        AXIOMS,
        REGISTRY,
        STRUCTURED,
        THETA_ZERO,
        GAUGE_STATUS,
        ASSEMBLY,
        G1_CARRIER,
        G1_DEFECT,
        G3_PHASE,
        MASS_W2,
        MASS_READY,
    ]

    section("A. source presence and Tier-A boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    tier = json.loads(read(TIER_A))
    axioms = read(AXIOMS)
    registry = read(REGISTRY)
    structured = read(STRUCTURED)
    theta_zero = read(THETA_ZERO)
    gauge_status = read(GAUGE_STATUS)
    assembly = read(ASSEMBLY)
    g1_carrier = read(G1_CARRIER)
    g1_defect = read(G1_DEFECT)
    g3_phase = read(G3_PHASE)
    mass_w2 = read(MASS_W2)
    mass_ready = read(MASS_READY)

    note_flat = flat(note)
    axioms_flat = flat(axioms)
    registry_flat = flat(registry)
    structured_flat = flat(structured)
    theta_zero_flat = flat(theta_zero)
    gauge_flat = flat(gauge_status)
    assembly_flat = flat(assembly)
    g1_carrier_flat = flat(g1_carrier)
    g1_defect_flat = flat(g1_defect)
    g3_flat = flat(g3_phase)
    mass_w2_flat = flat(mass_w2)
    mass_ready_flat = flat(mass_ready)

    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine admitted derivation-target count remains two", tier["genuine_admitted_input_count"] == 2)
    check("theta label is present", theta["label"] == "theta", theta["label"])
    check(
        "theta minimum decomposition has gauge and mass residuals",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check("theta statement names theta_bar", "theta_bar" in theta["statement"])
    check("theta statement names arg det", "arg det" in theta["statement"])
    check("human registry names theta", "strong-CP theta" in registry_flat or "theta" in registry_flat)
    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note says theta is not retired", "Theta is not retired." in note)
    check("note says theta_bar=0 is not derived", "`theta_bar = 0` is not derived" in note)
    for forbidden in [
        "Strong CP is solved",
        "therefore theta closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B. source pins for assembly boundary")
    for phrase in [
        "source/action",
        "physical-observable identification",
        "readout-context selection",
        "downstream open gates",
    ]:
        check(f"minimal axioms withhold {phrase}", phrase in axioms_flat)
    for phrase in [
        "Gauge-side residual",
        "mass-side residual",
        "does not retire",
        "theta_bar",
    ]:
        check(f"structured admission source contains {phrase}", phrase in structured_flat)
    for phrase in [
        "selected-surface",
        "Wilson-plus-staggered scalar-mass surface",
        "It does not derive from the minimal axiom surface",
    ]:
        check(f"theta-zero parent contains {phrase}", phrase in theta_zero_flat)
    for phrase in [
        "G4 physical theta assembly",
        "theta_bar = theta_gauge + arg det",
        "Nontrivial transfer still needs the supplier class",
        "G4 last",
    ]:
        check(f"gauge status contains {phrase}", phrase in gauge_flat)
    for phrase in [
        "paired-shift law",
        "n = 2 tr(eps)",
        "tr(eps) = 0",
        "does not supply either side's physical value",
        "nontrivial transfer",
    ]:
        check(f"assembly source contains {phrase}", phrase in assembly_flat)
    for phrase in [
        "physical 4D carrier",
        "not supply the 4D cubical/gauge carrier",
        "Theta's gauge-side winding account therefore remains live",
    ]:
        check(f"G1 carrier source contains {phrase}", phrase in g1_carrier_flat)
    for phrase in [
        "G1 is not derived",
        "dn=0",
        "defect-suppression",
        "Record axiom's new formation sentence is also not a defect law",
    ]:
        check(f"G1 defect source contains {phrase}", phrase in g1_defect_flat)
    for phrase in [
        "G3 is not derived",
        "phase-type",
        "coefficient",
        "physical registration",
    ]:
        check(f"G3 phase source contains {phrase}", phrase in g3_flat)
    for phrase in [
        "W2 physical registrability",
        "W2 is isolated",
        "theta mass readout",
        "not prove that the physical mass-surface readout is that supplied determinant channel",
    ]:
        check(f"mass W2 source contains {phrase}", phrase in mass_w2_flat)
    for phrase in [
        "not sufficient yet",
        "determinant-channel/readout exhaustion bridge",
        "mass-side determinant-readout atom remains live",
    ]:
        check(f"mass readiness source contains {phrase}", phrase in mass_ready_flat)

    section("C. exact paired-shift algebra")
    theta_g, phi, n, alpha = sp.symbols("theta_g phi n alpha")
    theta_bar = theta_g + phi
    theta_g_prime = theta_g - n * alpha
    phi_prime = phi + n * alpha
    theta_bar_prime = sp.simplify(theta_g_prime + phi_prime)
    check("theta_bar expression is theta_g + phi", theta_bar == theta_g + phi)
    check("paired shift preserves theta_bar", sp.simplify(theta_bar_prime - theta_bar) == 0)
    check("theta_bar has no alpha dependence after shift", sp.diff(theta_bar_prime, alpha) == 0)
    check("theta_bar still depends on theta_g", theta_g in theta_bar_prime.free_symbols)
    check("theta_bar still depends on phi", phi in theta_bar_prime.free_symbols)
    check("invariance does not force zero symbolically", sp.simplify(theta_bar_prime) != 0)
    zero_condition = sp.solve(sp.Eq(theta_bar, 0), phi)
    check("zero value requires a relation between sides", zero_condition == [-theta_g], zero_condition)

    tr_eps = sp.symbols("tr_eps")
    transfer_n = 2 * tr_eps
    check("fixed-grading transfer is n=2 tr(eps)", transfer_n == 2 * tr_eps)
    check("balanced tr(eps)=0 gives n=0", transfer_n.subs(tr_eps, 0) == 0)
    balanced_g = sp.simplify(theta_g - transfer_n.subs(tr_eps, 0) * alpha)
    balanced_phi = sp.simplify(phi + transfer_n.subs(tr_eps, 0) * alpha)
    check("balanced shift leaves gauge side unchanged", balanced_g == theta_g)
    check("balanced shift leaves mass side unchanged", balanced_phi == phi)

    examples = [
        ("zero_pair", sp.Integer(0), sp.Integer(0)),
        ("cancelling_pair", sp.Integer(1), sp.Integer(-1)),
        ("nonzero_pair", sp.Integer(1), sp.Integer(0)),
        ("generic_pair", sp.Rational(2, 3), sp.Rational(1, 5)),
    ]
    values = {}
    for name, g_val, p_val in examples:
        before = sp.simplify(theta_bar.subs({theta_g: g_val, phi: p_val}))
        after = sp.simplify(theta_bar_prime.subs({theta_g: g_val, phi: p_val, n: 3, alpha: sp.Rational(2, 7)}))
        values[name] = before
        check(f"{name} keeps theta_bar invariant under nonzero transfer", before == after, (before, after))
    check("same bookkeeping allows zero and nonzero theta_bar values", values["zero_pair"] == 0 and values["nonzero_pair"] != 0)
    check("cancelling pair is zero by initial relation only", values["cancelling_pair"] == 0)
    check("generic pair is nonzero", values["generic_pair"] != 0)

    section("D. prerequisite gate status")
    expected_rows = {
        "docs/THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md": "open_gate",
        "docs/THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md": "bounded_theorem",
        "docs/THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md": "no_go",
        "docs/THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md": "no_go",
        "docs/THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md": "no_go",
        "docs/THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md": "no_go",
        "docs/THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md": "no_go",
    }
    for path, claim_type in expected_rows.items():
        row = ledger_row_by_path(path)
        check(f"ledger row exists for {Path(path).name}", row is not None)
        if row is not None:
            check(f"{Path(path).name} claim_type is {claim_type}", row.get("claim_type") == claim_type, row.get("claim_type"))
            check(f"{Path(path).name} is not a retained theta retirement authority", row.get("effective_status") != "retained", row.get("effective_status"))
    for phrase in [
        "G1 physical 4D carrier",
        "G2 physical sector/readout registration",
        "G3 phase source",
        "mass-side W2 physical registrability",
        "Full theta-bar assembly theorem",
    ]:
        check(f"note lists remaining route: {phrase}", phrase in note)
    for phrase in [
        "neutron-EDM bound",
        "observed theta value",
        "fitted selector",
        "axion premise",
        "anomaly supplier primitive",
        "registry edit",
    ]:
        check(f"hidden import exclusion recorded: {phrase}", phrase in note_flat)

    section("E. new audit row")
    new_row = ledger_row_by_path("docs/THETA_G4_THETA_BAR_ASSEMBLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md")
    if new_row is None:
        check("new row not required before audit pipeline seeding", True)
    else:
        check("new row claim_type is no_go", new_row.get("claim_type") == "no_go", new_row.get("claim_type"))
        check("new row audit status remains unaudited", new_row.get("audit_status") == "unaudited", new_row.get("audit_status"))
        check("new row effective status remains unaudited", new_row.get("effective_status") == "unaudited", new_row.get("effective_status"))
        deps = new_row.get("deps") or []
        check("new row has at least ten dependencies", len(deps) >= 10, deps)
        for dep in [
            "minimal_axioms",
            "admitted_input_registry_tier_a_note_2026-05-23",
            "strong_cp_theta_bar_structured_admission_2026-06-04",
            "theta_gauge_positive_route_stretch_status_2026-07-04",
            "theta_assembly_paired_shift_fixed_grading_mckean_singer_reduction_narrow_theorem_note_2026-07-02",
            "theta_g1_4d_carrier_supply_current_surface_no_go_note_2026-07-04",
            "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
            "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
            "theta_mass_w2_physical_registrability_stretch_no_go_note_2026-07-04",
            "theta_mass_determinant_bridge_retirement_readiness_no_go_note_2026-07-04",
        ]:
            check(f"new row dependency includes {dep}", dep in deps, deps)

    print("\nTOTAL: PASS=%d FAIL=%d CHECKS=%d" % (PASS, FAIL, PASS + FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
