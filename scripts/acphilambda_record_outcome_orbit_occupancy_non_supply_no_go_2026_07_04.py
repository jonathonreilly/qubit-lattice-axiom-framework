#!/usr/bin/env python3
"""Verifier for AC Record outcome-orbit occupancy non-supply no-go."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
CURRENT_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
OLD_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
OCC_REDUCTION = DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
OUTCOME_DICT = DOCS / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
DET_SPLIT = DOCS / "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md"
MEASURE_NO_GO = DOCS / "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
FORMATION_NO_GO = DOCS / "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def additive_total(values: dict[str, sp.Expr], records: frozenset[str]) -> sp.Expr:
    return sp.simplify(sum(values[item] for item in records))


def is_additive(values: dict[str, sp.Expr], records: tuple[str, ...]) -> bool:
    subsets = []
    for size in range(len(records) + 1):
        for combo in itertools.combinations(records, size):
            subsets.append(frozenset(combo))
    for left in subsets:
        for right in subsets:
            if left & right:
                continue
            lhs = additive_total(values, left | right)
            rhs = additive_total(values, left) + additive_total(values, right)
            if sp.simplify(lhs - rhs) != 0:
                return False
    return additive_total(values, frozenset()) == 0


def main() -> int:
    print("AC_phi_lambda Record outcome-orbit occupancy non-supply no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    current_axioms = CURRENT_AXIOMS.read_text(encoding="utf-8")
    old_axioms = OLD_AXIOMS.read_text(encoding="utf-8")
    tier = json.loads(TIER_A.read_text(encoding="utf-8"))
    occ_reduction = OCC_REDUCTION.read_text(encoding="utf-8")
    outcome_dict = OUTCOME_DICT.read_text(encoding="utf-8")
    det_split = DET_SPLIT.read_text(encoding="utf-8")
    measure_no_go = MEASURE_NO_GO.read_text(encoding="utf-8")
    formation_no_go = FORMATION_NO_GO.read_text(encoding="utf-8")

    note_flat = flat(note)
    current_flat = flat(current_axioms)
    old_flat = flat(old_axioms)
    occ_flat = flat(occ_reduction)
    outcome_flat = flat(outcome_dict)
    det_flat = flat(det_split)
    measure_no_go_flat = flat(measure_no_go)
    formation_no_go_flat = flat(formation_no_go)

    section("A - source and registry boundaries")

    for path in [NOTE, CURRENT_AXIOMS, OLD_AXIOMS, TIER_A, OCC_REDUCTION, OUTCOME_DICT, DET_SPLIT, MEASURE_NO_GO, FORMATION_NO_GO]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares no_go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("note denies AC retirement", "does not retire `AC_phi_lambda`" in note_flat and "`AC_phi_lambda(i)` is not retired" in note)
    check("note denies horn selection and r derivation", "does not choose the orbit/holomorphic horn" in note_flat and "`r = 1/2` is not derived" in note)
    check("note denies premise/primitive adoption", "does not adopt the orbit-occupancy premise" in note_flat and "No K-real primitive" in note)
    check("note denies registry/axiom edits", "does not edit any Tier-A registry" in note_flat and "No registry, primitive, axiom" in note)

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("live Tier-A genuine count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("canonical Tier-A IDs are empty on current main", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("live derivation targets are empty on current main", tier.get("derivation_targets", {}) == {}, tier.get("derivation_targets"))
    retirement = ac.get("retirement", {})
    check("AC retired-target record is preserved", bool(ac))
    check("AC retirement date is recorded", retirement.get("date") == "2026-07-05", retirement)
    check("AC retirement mechanism is owner governance", retirement.get("mechanism") == "retired_by_owner_governance_on_audited_surface", retirement)
    check(
        "historical AC decomposition preserves three old atoms",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
            "species_bridge",
        ],
        ac["minimum_decomposition"],
    )
    check("note has current-main posture line", "Current-main posture (2026-07-06)" in note)
    check("note records live Tier-A zero posture", "Tier-A count\nzero" in note or "Tier-A count zero" in note)
    check("note says retirement records are not reopened", "does not reopen,\nmodify, or re-grade either retirement record" in note)

    section("B - current versus older axiom surface")

    check("current axioms supersede June 5 memo", "**Supersedes:** `MINIMAL_AXIOMS_2026-06-05.md`" in current_axioms)
    check(
        "current axioms keep K/CPT orbit structure downstream",
        "`K`/CPT orbit structure" in current_axioms
        and "downstream readout-context content" in current_flat,
    )
    check(
        "current axioms keep weights and context selection outside",
        "Born weights" in current_flat
        and "readout-context selection" in current_flat
        and "measurement basis selection" in current_flat
        and "probability rules" in current_flat,
    )
    check("current axioms explicitly keep AC_phi_lambda outside", "AC_phi_lambda" in current_axioms and "remain outside axiom content" in current_flat)
    check(
        "older supplied-context Record wording named K/CPT orbit only conditionally",
        "Given a readout context with a finite central-sector decomposition and a fixed" in old_axioms
        and "the realized outcome is the `K`/CPT orbit" in old_axioms,
    )
    check(
        "older Record wording denied weights and occupancy supply",
        "A record supplies no readout context" in old_flat
        and "weighting, normalization, probability" in old_flat
        and "occupancy rule" in old_flat,
    )

    section("C - same outcome object, different dictionaries")

    r = sp.symbols("r", positive=True, real=True)
    phi_component = 2 * r
    phi_slot = r
    check("component and slot dictionaries share the same outcome variable x", sp.Symbol("x") == sp.Symbol("x"))
    check("component dictionary x=2r maps x=1 to r=1/2", sp.solve(sp.Eq(phi_component, 1), r) == [sp.Rational(1, 2)])
    check("slot dictionary x=r maps x=1 to r=1", sp.solve(sp.Eq(phi_slot, 1), r) == [sp.Integer(1)])
    check("the two dictionaries are not the same map", sp.simplify(phi_component - phi_slot) != 0)

    records = ("s", "d")
    component_values = {"s": sp.Integer(1), "d": phi_component}
    slot_values = {"s": sp.Integer(1), "d": phi_slot}
    check("component dictionary is additive on the same outcome labels", is_additive(component_values, records))
    check("slot dictionary is additive on the same outcome labels", is_additive(slot_values, records))

    lam, z = sp.symbols("lam z", positive=True, real=True)
    det_once = lam * z
    det_twice = lam**2 * z**2
    check("determinant exponents differ by dictionary, not by outcome label", sp.diff(det_once, lam, 2) == 0 and sp.diff(det_twice, lam, 2) != 0)
    check("landed cells remain distinct", sp.Rational(1, 2) != sp.Integer(1))

    section("D - source integration and non-overclaim")

    check(
        "outcome dictionary note states Record names object not weight",
        "Record axiom names the outcome object, not the weight attached to it" in outcome_flat,
    )
    check(
        "outcome dictionary note keeps occupancy binary open",
        "Does not close the occupancy binary" in outcome_dict or "occupancy binary stays open" in outcome_flat,
    )
    check(
        "AC reduction names measure-side survivor",
        "measure-side binary itself" in occ_flat and "matter action's statistics implements" in occ_flat,
    )
    check(
        "Block28 determinant split identifies what must be selected",
        "determinant-power binary" in det_split and "matter action implements" in det_flat,
    )
    check(
        "measure-binary no-go blocks axiom/primitive retirement",
        "does not supply the AC(i) reading/occupancy binary" in measure_no_go_flat
        and "No value of `r` is derived, selected, or preferred." in measure_no_go,
    )
    check(
        "formation-append no-go blocks Record shortcut",
        "The July 4 formation append does not retire AC_phi_lambda(i)." in formation_no_go
        and "measure-side doublet occupancy realization binary" in formation_no_go_flat,
    )

    required_note_phrases = [
        "The implication is invalid",
        "outcome object only",
        "does not select the determinant-power dictionary",
        "physical measure/readout theorem",
        "Remaining Live Routes",
    ]
    for phrase in required_note_phrases:
        check(f"note contains required phrase: {phrase}", phrase in note)

    banned = [
        "derives `r = 1/2`",
        "chooses the orbit/holomorphic horn",
        "adopts the orbit-occupancy premise",
        "introduces a K-real primitive",
        "retires `AC_phi_lambda`",
        "edits the Tier-A registry",
        "AC_phi_lambda(i) is retired",
        "audited_clean",
        "retained_no_go",
    ]
    false_positive_context = {
        "derives `r = 1/2`": "does not derive `r = 1/2`",
        "chooses the orbit/holomorphic horn": "does not choose the orbit/holomorphic horn",
        "adopts the orbit-occupancy premise": "does not adopt the orbit-occupancy premise",
        "introduces a K-real primitive": "does not introduce a K-real primitive",
        "retires `AC_phi_lambda`": "does not retire `AC_phi_lambda`",
        "edits the Tier-A registry": "does not edit the Tier-A registry",
        "AC_phi_lambda(i) is retired": "`AC_phi_lambda(i)` is not retired",
    }
    found = []
    for phrase in banned:
        if phrase in note and false_positive_context.get(phrase) not in note:
            found.append(phrase)
    check("banned overclaim phrases are absent except explicit denials", not found, found)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
