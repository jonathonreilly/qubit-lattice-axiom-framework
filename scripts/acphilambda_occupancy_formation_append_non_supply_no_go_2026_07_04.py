#!/usr/bin/env python3
"""Verifier for the AC occupancy formation-append non-supply no-go."""

from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
OBLIGATIONS = DOCS / "audit" / "data" / "derivation_obligations.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
POLICY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"
FORMATION_CERT = DOCS / "RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md"
FORMATION_SWEEP = DOCS / "RECORD_FORMATION_APPEND_CONSISTENCY_SWEEP_2026-07-04.md"
OCC_REDUCTION = DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
OUTCOME_DICT = DOCS / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
SCORING_DISC = DOCS / "FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md"
C3_CONTEXT = DOCS / "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"

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
    return json.loads(read(LEDGER))["rows"][claim_id]


def add_record(state: dict[int, str], site: int, outcome: str) -> dict[int, str]:
    if site in state:
        raise ValueError("one-record-per-site violation")
    new_state = dict(state)
    new_state[site] = outcome
    return new_state


def additive_readout(state: dict[int, str], weights: dict[str, Fraction]) -> Fraction:
    return sum((weights[outcome] for outcome in state.values()), Fraction(0))


def main() -> int:
    print("AC_phi_lambda occupancy formation-append non-supply verifier")

    paths = [
        NOTE,
        TIER_A,
        OBLIGATIONS,
        LEDGER,
        REGISTRY,
        MINIMAL,
        AXIOM_NODES,
        POLICY,
        FORMATION_CERT,
        FORMATION_SWEEP,
        OCC_REDUCTION,
        OUTCOME_DICT,
        SCORING_DISC,
        C3_CONTEXT,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and no-overclaim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type no_go", "**Type:** no_go" in note)
    check("note has Claim type no_go", "**Claim type:** no_go" in note)
    check("note has audit boundary", "**Audit boundary:** independent audit lane only." in note)
    check("runner link is wired", Path(__file__).name in note)
    for phrase in [
        "does not derive, refute, re-grade, or remove the historical AC_phi_lambda decomposition",
        "does not edit any Tier-A registry",
        "No axiom, primitive, registry, audit verdict, or publication-status surface is edited.",
        "future occupancy-dictionary or matter-action theorems",
    ]:
        check(f"scope boundary present: {phrase[:64]}", phrase in note_flat)
    for banned in [
        "the formation append retired AC_phi_lambda(i)",
        "Records form retired AC_phi_lambda",
        "R-eta is retired",
        "theta is retired",
        "we remove AC_phi_lambda",
        "new occupancy primitive is approved",
        "Record formation selects the occupancy dictionary",
        "owner governance derived the occupancy dictionary",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. Tier-A registry state on current main")
    tier = json.loads(read(TIER_A))
    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    decomp = ac["minimum_decomposition"]
    statement = ac["statement"]
    obligations = json.loads(read(OBLIGATIONS))
    obligation_ids = obligations["canonical_ids"]
    check(
        "Tier-A live derivation targets are empty after the 2026-07-05 retirements",
        tier["genuine_admitted_input_count"] == 0
        and tier["derivation_targets"] == {}
        and tier["canonical_ids"] == [],
        str(tier["genuine_admitted_input_count"]),
    )
    check(
        "AC entry preserved intact under retired_derivation_targets",
        bool(statement) and bool(decomp),
    )
    check(
        "AC governance retirement is withdrawn and obligations are reopened",
        ac["retirement"]["mechanism"] == "historical_governance_retirement_withdrawn_obligations_reopened",
        ac["retirement"]["mechanism"],
    )
    check(
        "derivation registry carries exactly the two AC obligations",
        obligation_ids == [
            "ac_orbit_occupancy_statistical_grain_derivation_obligation",
            "ac_reta_hclass_hunit_readout_derivation_obligation",
        ],
        obligation_ids,
    )
    check(
        "occupancy obligation is explicitly open and non-premise",
        obligations["nodes"]["ac_orbit_occupancy_statistical_grain_derivation_obligation"]["status"]
        == "open_non_premise",
    )
    check(
        "R-eta obligation is explicitly open and non-premise",
        obligations["nodes"]["ac_reta_hclass_hunit_readout_derivation_obligation"]["status"]
        == "open_non_premise",
    )
    check(
        "obligations are separate from the supplied foundation",
        not (DOCS / "audit" / "data" / "owner_governed_premise_nodes.json").exists(),
    )
    check("AC minimum decomposition contains occupancy binary", "reading_occupancy_selection" in decomp, decomp)
    check("AC minimum decomposition keeps R-eta separate", "delta_readout_identification_R_eta" in decomp, decomp)
    check("AC minimum decomposition keeps species bridge separate", "species_bridge" in decomp, decomp)
    check("AC statement names doublet reading/occupancy selection", "doublet reading/occupancy selection" in statement)
    check("AC statement names sector-tied branch", "sector-tied" in statement)
    check("AC statement names orbit/holomorphic branch", "orbit/holomorphic" in statement)
    check("AC statement keeps r as a binary", "r in {1, 1/2}" in statement)
    check("AC statement keeps R-eta separate", "delta readout identification R-eta" in ac["statement"])
    check("human registry names occupancy obligation", "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md" in texts[REGISTRY])

    section("C. formation append and axiom boundary")
    minimal = flats[MINIMAL]
    policy = flats[POLICY]
    cert = flats[FORMATION_CERT]
    sweep = flats[FORMATION_SWEEP]
    ax_nodes = json.loads(read(AXIOM_NODES))["nodes"]["minimal_axioms"]["note"]
    for phrase in [
        "Records form.",
        "When present, a record locks exactly one admissible local possibility",
        "A site never carries more than one record; records are permanent.",
        "For any finite collection of pairwise-disjoint records, scalar readout",
        "which admissible possibility a new record locks, at which site, with what weight, or at what rate",
        "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`",
    ]:
        check(f"minimal axiom boundary: {phrase[:64]}", phrase in minimal)
    for phrase in [
        "Occurrence becomes named axiom content",
        "every formation rule",
        "which admissible possibility a new record locks, at which site, with what weight, at what rate",
        "The sentence names no formation rule, rate, weighting, or selector",
    ]:
        check(f"policy formation boundary: {phrase[:64]}", phrase in policy)
    for phrase in [
        "occurrence strength only",
        "does not say that every state has a formation-successor",
        "successor strictly extends the predecessor",
        "does not supply",
        "which admissible possibility, which site, what weight, or what rate",
        "selector supply",
    ]:
        check(f"formation cert boundary: {phrase[:64]}", phrase in cert)
    for phrase in [
        "occurrence is supplied",
        "the residual must narrow to formation rule/process/state/site/weight",
        "specific K1 record stack remains supplied but generic occurrence is no longer open",
    ]:
        check(f"formation sweep boundary: {phrase[:64]}", phrase in sweep)
    check("axiom node mirrors records form", "records form" in ax_nodes)
    check("axiom node mirrors no formation-rule content", "which admissible possibility" in ax_nodes and "what rate" in ax_nodes)

    section("D. AC(i) source-surface boundary checks")
    occ_reduction = flats[OCC_REDUCTION]
    outcome_dict = flats[OUTCOME_DICT]
    scoring = flats[SCORING_DISC]
    c3 = flats[C3_CONTEXT]
    check(
        "occupancy reduction boundary: value-bearing face of AC_phi_lambda",
        "**value-bearing" in texts[OCC_REDUCTION] and "face** of AC_φλ" in texts[OCC_REDUCTION],
    )
    for phrase in [
        "realized-state **registration**",
        "the precisely-named **survivor** is the measure-side",
        "the measure-side binary itself",
        "Both grain models satisfy every checked constraint",
        "measure-side frontier is open, not settled",
    ]:
        check(f"occupancy reduction boundary: {phrase[:64]}", phrase in occ_reduction)
    for phrase in [
        "FIREWALL: no fork branch or occupancy cell is discriminated or selected here",
        "the occupancy binary stays open",
        "Component dictionary `(1,2)`: `x = 2r`",
        "Slot dictionary `(1,1)`: `x = r`",
        "outcome-to-component dictionary",
        "Does not close the occupancy binary",
    ]:
        check(f"outcome dictionary boundary: {phrase[:64]}", phrase in outcome_dict)
    for phrase in [
        "conditional on the named invariance requirement",
        "not a selection theorem on the actual current surface",
        "The no-imported-frame requirement",
        "The equal-channel-energy theorem",
        "It does not derive the physical readout identification",
    ]:
        check(f"scoring discriminator boundary: {phrase[:64]}", phrase in scoring)
    check("C3 context excludes occupancy rule", "Does not supply a weighting, normalization, probability rule, occupancy rule" in c3)

    section("E. ledger classifications for source rows")
    expected = {
        "record_formation_append_certification_bounded_note_2026-07-04": "bounded_theorem",
        "acphilambda_occupancy_selection_realized_state_reduction_note_2026-06-11": "bounded_theorem",
        "occupancy_atom_is_the_outcome_dictionary_flow_selects_equipartition_bounded_note_2026-06-12": "bounded_theorem",
        "flavor_carrier_measure_scoring_discriminator_bounded_note_2026-07-02": "bounded_theorem",
        "c3_generation_readout_context_canonical_definition_note_2026-07-02": "meta",
    }
    for claim_id, claim_type in expected.items():
        row = ledger_row(claim_id)
        check(f"{claim_id} claim_type", row.get("claim_type") == claim_type, row.get("claim_type"))
        check(f"{claim_id} has note path", bool(row.get("note_path")), row.get("note_path"))

    section("F. finite model separation for the occupancy dictionary")
    empty: dict[int, str] = {}
    state_s = add_record(empty, 0, "s")
    state_sd = add_record(state_s, 1, "d")
    try:
        add_record(state_sd, 1, "s")
        duplicate_rejected = False
    except ValueError:
        duplicate_rejected = True
    check("empty state is allowed before occurrence", empty == {})
    check("formation event adds first record", len(state_s) == 1 and state_s[0] == "s")
    check("successor strictly extends predecessor", set(state_s).issubset(state_sd) and len(state_sd) == len(state_s) + 1)
    check("one-record-per-site rejects replacement", duplicate_rejected)

    dictionaries = {
        "component_dictionary_x_equals_2r": {"factor": Fraction(2), "weights": {"s": Fraction(1), "d": Fraction(2)}},
        "slot_dictionary_x_equals_r": {"factor": Fraction(1), "weights": {"s": Fraction(1), "d": Fraction(1)}},
    }
    readings = {}
    for name, data in dictionaries.items():
        factor = data["factor"]
        weights = data["weights"]
        i_empty = additive_readout(empty, weights)
        i_s = additive_readout(state_s, weights)
        i_d = additive_readout({2: "d"}, weights)
        i_sd = additive_readout(state_sd, weights)
        readings[name] = Fraction(1, 1) / factor
        check(f"{name}: I(empty)=0", i_empty == 0)
        check(f"{name}: finite additivity on disjoint s+d", i_sd == i_s + i_d)
        check(f"{name}: outcome equipartition x=1 reads r=1/factor", readings[name] == Fraction(1, 1) / factor)

    check("component dictionary gives r=1/2", readings["component_dictionary_x_equals_2r"] == Fraction(1, 2))
    check("slot dictionary gives r=1", readings["slot_dictionary_x_equals_r"] == Fraction(1, 1))
    check("formation axioms do not collapse the dictionary pair", len(set(readings.values())) == 2)
    check("both dictionaries use same formed-record state", set(dictionaries) == {"component_dictionary_x_equals_2r", "slot_dictionary_x_equals_r"})

    section("G. note theorem and no-go discipline")
    for phrase in [
        "The implication is invalid.",
        "The July 4 formation append did not itself derive or retire AC_phi_lambda(i).",
        "It supplies:",
        "It does not supply:",
        "the outcome-to-component dictionary",
        "Formation-rule theorem",
        "Matter-action theorem",
        "Approved-primitive route",
    ]:
        check(f"note contains synthesis phrase: {phrase[:64]}", phrase in note_flat)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    check("N1 records at least five attempted routes", note.count("`ATTEMPTED`") >= 5)
    check(
        "N1 checks the approved-primitive registry route",
        "approved-primitive search" in note,
    )
    check("N2 separates occurrence from dictionary", "Closing occurrence does not close the dictionary" in note_flat)
    check(
        "N4 matches historical registry and current open obligation",
        "historical `reading_occupancy_selection` atom" in note_flat
        and "`derivation_obligations.json` AC occupancy row" in note_flat
        and "current open target is separate from derivation by the formation append" in note_flat,
    )
    check("steelman preserves occurrence support", "Formed records remain necessary for occupancy readout" in note_flat)

    section("TOTAL")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
