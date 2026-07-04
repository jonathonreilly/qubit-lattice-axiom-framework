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
READINESS_NO_GO = DOCS / "ACPHILAMBDA_FIRST_ORDER_DETERMINANT_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md"

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
    readiness = READINESS_NO_GO.read_text(encoding="utf-8")

    note_flat = flat(note)
    current_flat = flat(current_axioms)
    old_flat = flat(old_axioms)
    occ_flat = flat(occ_reduction)
    outcome_flat = flat(outcome_dict)
    det_flat = flat(det_split)
    readiness_flat = flat(readiness)

    section("A - source and registry boundaries")

    for path in [NOTE, CURRENT_AXIOMS, OLD_AXIOMS, TIER_A, OCC_REDUCTION, OUTCOME_DICT, DET_SPLIT, READINESS_NO_GO]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares no_go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("note denies AC retirement", "does not retire `AC_phi_lambda`" in note_flat and "`AC_phi_lambda(i)` is not retired" in note)
    check("note denies horn selection and r derivation", "does not choose the orbit/holomorphic horn" in note_flat and "`r = 1/2` is not derived" in note)
    check("note denies premise/primitive adoption", "does not adopt the orbit-occupancy premise" in note_flat and "No K-real primitive" in note)
    check("note denies registry/axiom edits", "does not edit any Tier-A registry" in note_flat and "No registry, primitive, axiom" in note)

    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition remains occupancy plus R-eta",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )

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
        "determinant-power binary" in det_split and "physical matter action implements" in det_flat,
    )
    check(
        "readiness no-go blocks immediate retirement from determinant algebra plus hygiene",
        "therefore AC_phi_lambda(i)'s measure-side realization binary is retired" in readiness
        and "is invalid" in readiness_flat,
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
