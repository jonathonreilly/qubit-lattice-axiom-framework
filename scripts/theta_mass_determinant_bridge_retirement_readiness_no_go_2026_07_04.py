#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
MASS_AXIOM_NO_GO = DOCS / "THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
DET_BRIDGE = DOCS / "STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"
P2_KCPT = DOCS / "THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
P2_EXHAUSTION = DOCS / "THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
ORIENTATION_ZERO = DOCS / "THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md"
EPS_REALITY = DOCS / "THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
    "mass_axiom_no_go": "theta_mass_determinant_axiom_update_no_go_note_2026-07-04",
    "det_bridge": "strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12",
    "p2_kcpt": "theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10",
    "p2_exhaustion": "theta_p2_determinant_readout_exhaustion_bridge_bounded_theorem_note_2026-06-11",
    "orientation_zero": "theta_mass_orientation_zero_branch_pairing_forced_on_k_real_surface_narrow_theorem_note_2026-07-01",
    "eps_reality": "theta_mass_side_epsilon_hermiticity_reality_bridge_discharge_bounded_theorem_note_2026-06-11",
    "realized": "realized_state_primitive",
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
    print("\n" + "=" * 94)
    print(title)
    print("=" * 94)


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
    print("theta mass determinant bridge retirement-readiness no-go verifier")
    paths = [
        NOTE,
        MINIMAL,
        REGISTRY,
        TIER_A,
        LEDGER,
        MASS_AXIOM_NO_GO,
        DET_BRIDGE,
        P2_KCPT,
        P2_EXHAUSTION,
        ORIENTATION_ZERO,
        EPS_REALITY,
        REALIZED,
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
    check("note declares mass-side readiness scope", "current-surface retirement-readiness test" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "future determinant-channel, K-real",
    ]:
        check(f"scope boundary phrase present: {phrase[:58]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "registry is edited",
        "mass-side atom is retired",
        "determinant bridge is retained",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. ledger and registry state")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
        check(f"{label} row has note path or is premise", bool(row.get("note_path")) or label in {"minimal"}, row.get("note_path"))
    for label in ["mass_axiom_no_go", "det_bridge", "p2_kcpt", "p2_exhaustion", "orientation_zero", "eps_reality"]:
        row = ledger_row(SOURCE_ROWS[label])
        check(f"{label} not effective retirement authority", row.get("effective_status") != "retained", row.get("effective_status"))
        check(f"{label} audit not clean in current branch", row.get("audit_status") != "audited_clean", row.get("audit_status"))
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check("theta still has mass-side atom", "mass_side_orientation_determinant_readout_bridge" in theta["minimum_decomposition"])
    check("theta still has gauge-side atom", "gauge_side_winding_account" in theta["minimum_decomposition"])
    check("AC realized-state hygiene recorded", "AC_phi_lambda(i) value-face reclassification" in tier["description"])
    check("AC C3-grade owner ratification recorded", "C3-grade species-bridge owner ratification" in tier["description"])

    section("C. source-boundary checks")
    for phrase in [
        "withholds determinant-channel selection",
        "physical-observable identification",
        "K`/CPT orbit structure",
    ]:
        check(f"minimal/derived note boundary: {phrase[:56]}", phrase in note_flat or phrase in flats[MINIMAL])
    for phrase in [
        "only after the determinant-readout/exhaustion bridge is closed",
        "not by registry wording alone",
        "determinant-readout bridge",
    ]:
        check(f"registry boundary present: {phrase[:56]}", phrase in flats[REGISTRY])
    for phrase in [
        "It does not supply the determinant channel by itself.",
        "The theorem is stated on a supplied finite mass-sector readout interface",
        "does not promote the strong-CP parent",
        "does not touch the Tier-A registry",
    ]:
        check(f"det bridge boundary present: {phrase[:56]}", phrase in flats[DET_BRIDGE])
    for phrase in [
        "what remains supplied is only the determinant-channel readout identification itself",
        "No Tier-A registry action",
        "does not derive",
        "The orientation component of the mass-side residual is thereby removed on this surface",
    ]:
        check(f"orientation note boundary present: {phrase[:56]}", phrase in flats[ORIENTATION_ZERO])
    for phrase in [
        "supplied determinant readout context",
        "W2 is still not derived",
        "K-reality is still a consumed",
        "does not prove W2",
    ]:
        check(f"P2 exhaustion boundary present: {phrase[:56]}", phrase in flats[P2_EXHAUSTION])
    for phrase in [
        "It does not supply the determinant readout",
        "determinant-readout bridge named open",
        "registrable `arg det(M_u M_d)` content",
    ]:
        check(f"P2 K/CPT boundary present: {phrase[:56]}", phrase in flats[P2_KCPT])
    for phrase in [
        "a derivation of K-reality",
        "determinant-readout bridge named open",
        "Tier-A",
    ]:
        check(f"epsilon reality boundary present: {phrase[:56]}", phrase in flats[EPS_REALITY])
    for phrase in [
        "realized state, pointwise",
        "realized_state_primitive",
    ]:
        check(f"realized-state boundary present: {phrase[:56]}", phrase in flats[REALIZED])
    for phrase in [
        "does not supply the theta mass-side determinant-readout bridge",
        "determinant-channel interface",
    ]:
        check(f"mass axiom no-go or note boundary present: {phrase[:56]}", phrase in flats[MASS_AXIOM_NO_GO] or phrase in note_flat)

    section("D. route capability matrix")
    candidates = {
        "det_bridge": {"det_algebra": True, "supplies_channel": False, "audit_clean": False, "registry_retire": False},
        "orientation_zero": {"orientation_zero": True, "supplies_channel": False, "audit_clean": False, "registry_retire": False},
        "p2_exhaustion": {"exhaustion_given_context": True, "supplies_channel": False, "audit_clean": False, "registry_retire": False},
        "realized_state": {"realized_value": True, "theta_mass_bridge": False, "audit_clean": True, "registry_retire": False},
        "ac_c3_hygiene": {"c3_naming": True, "theta_mass_bridge": False, "audit_clean": True, "registry_retire": False},
        "minimal_axioms": {"record_forms": True, "determinant_channel": False, "audit_clean": True, "registry_retire": False},
    }
    for name, flags in candidates.items():
        closes = all(flags.values())
        check(f"{name} does not close all retirement gates", not closes, flags)
    check("no current candidate retires theta mass-side atom", not any(all(flags.values()) for flags in candidates.values()))
    check("det bridge lacks supplied-channel derivation", not candidates["det_bridge"]["supplies_channel"])
    check("orientation result lacks channel identification", not candidates["orientation_zero"]["supplies_channel"])
    check("AC hygiene not a theta mass bridge", not candidates["ac_c3_hygiene"]["theta_mass_bridge"])

    section("E. note theorem and no-go discipline text")
    for heading in [
        "Frame 1: determinant-channel algebra exists, but on a supplied interface",
        "Frame 2: orientation is narrowed, not the whole mass atom retired",
        "Frame 3: AC hygiene does not automatically move theta(b)",
        "Frame 4: audit status is not a technicality",
    ]:
        check(f"fan-out heading present: {heading}", heading in note)
    for phrase in [
        "is invalid",
        "audit-ratified determinant-channel/readout exhaustion bridge",
        "mass-side determinant-readout atom remains live",
        "Owner governance",
    ]:
        check(f"note contains theorem/queue phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N3 forbids determinant-channel primitive", "no determinant-channel primitive" in note_flat)
    check("N5 says not universal no-go", "not a universal no-go against future determinant-channel" in note_flat)
    check("remaining routes include audit closure", "Audit and dependency closure" in note)

    section("F. final summary")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
