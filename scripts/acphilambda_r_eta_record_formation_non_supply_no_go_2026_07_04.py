#!/usr/bin/env python3
"""Verifier for AC R-eta Record-formation non-supply no-go."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_RECORD_FORMATION_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
OCCURRENCE_NO_GO = DOCS / "ACPHILAMBDA_R_ETA_OCCURRENCE_AXIOM_HYGIENE_NO_GO_NOTE_2026-07-04.md"
DIRECT_LICENSE_NO_GO = DOCS / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
ANGLE_NO_GO = DOCS / "ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md"
DELTA_CHAIN = DOCS / "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md"
FIXED = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

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


def powerset(items: tuple[str, ...]) -> list[frozenset[str]]:
    out: list[frozenset[str]] = []
    for size in range(len(items) + 1):
        for combo in itertools.combinations(items, size):
            out.append(frozenset(combo))
    return out


def additive_total(values: dict[str, sp.Expr], records: frozenset[str]) -> sp.Expr:
    return sp.simplify(sum(values[item] for item in records))


def is_additive(values: dict[str, sp.Expr], records: tuple[str, ...]) -> bool:
    subsets = powerset(records)
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
    print("AC_phi_lambda R-eta Record-formation non-supply no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    tier = json.loads(DECISION_HISTORY.read_text(encoding="utf-8"))
    occurrence = OCCURRENCE_NO_GO.read_text(encoding="utf-8")
    direct_license = DIRECT_LICENSE_NO_GO.read_text(encoding="utf-8")
    angle = ANGLE_NO_GO.read_text(encoding="utf-8")
    delta = DELTA_CHAIN.read_text(encoding="utf-8")
    fixed = FIXED.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    occurrence_flat = flat(occurrence)
    direct_license_flat = flat(direct_license)
    angle_flat = flat(angle)
    delta_flat = flat(delta)
    fixed_flat = flat(fixed)
    registry_flat = flat(registry)

    section("A - source and registry boundaries")

    for path in [NOTE, MINIMAL, DECISION_HISTORY, OCCURRENCE_NO_GO, DIRECT_LICENSE_NO_GO, ANGLE_NO_GO, DELTA_CHAIN, FIXED, REGISTRY]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("decision history live premise count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("decision history canonical live IDs are empty", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("live derivation targets are empty on current main", tier.get("derivation_targets", {}) == {}, tier.get("derivation_targets"))
    retirement = ac.get("retirement", {})
    check("AC retired-target record is preserved", bool(ac))
    check("AC obligation correction date is recorded", retirement.get("date") == "2026-07-11", retirement)
    check("AC obligations are reopened", retirement.get("mechanism") == "historical_governance_retirement_withdrawn_obligations_reopened", retirement)
    check(
        "historical AC decomposition retains R-eta",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
            "species_bridge",
        ],
        ac["minimum_decomposition"],
    )
    check("registry prose names R-eta obligation", "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md" in registry)
    check("note keeps R-eta open", "does not retire" in note_flat and "The R-eta derivation obligation remains open." in note)
    check("note denies registry/axiom/primitive edits", "does not create or edit any premise registry" in note_flat and "No registry, axiom, primitive" in note)
    check("note has current-main posture line", "Current-main posture (2026-07-11)" in note)
    check("note records open-obligation posture", "open derivation obligation\nwith zero premise weight" in note)
    check("note says governance is provenance only", "historical governance decision is provenance\nonly" in note)

    section("B - Record formation axiom boundary")

    check("minimal axioms contain formation sentence", "Records form." in minimal)
    excluded_needles = [
        "record-production process",
        "record-production dynamics",
        "time metric",
        "formation rules",
        "at what rate",
        "with what weight",
        "source/action",
        "physical-observable identification",
        "readout-context selection",
    ]
    for needle in excluded_needles:
        check(f"minimal axioms keep outside content outside: {needle}", needle in minimal_flat)
    check("minimal axioms explicitly leave AC outside", "AC_phi_lambda" in minimal)
    check("minimal axioms explicitly leave theta outside", "strong-CP theta gauge and mass-side derivation obligations" in minimal)

    section("C - fixed-locus arithmetic and formation-compatible family")

    omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    term_1 = sp.simplify(1 / ((1 - omega) * (1 - omega**2)))
    term_2 = sp.simplify(1 / ((1 - omega**2) * (1 - omega**4)))
    density = sp.simplify((term_1 + term_2) / 3)
    check("each fixed-locus summand is 1/3", term_1 == sp.Rational(1, 3) and term_2 == sp.Rational(1, 3))
    check("averaged fixed-locus density is 2/9", density == sp.Rational(2, 9), density)
    check("fixed-locus note carries 2/9 arithmetic", "2/9" in fixed_flat and ("fixed-locus" in fixed_flat.lower() or "fixed locus" in fixed_flat.lower()))

    formed = {"j1": True, "j2": True}
    check("bare formation fact is the same for both summands", all(formed.values()) and set(formed) == {"j1", "j2"})
    records = ("j1", "j2")
    assignments: dict[str, dict[str, sp.Expr]] = {
        "direct_density": {"j1": sp.Rational(1, 9), "j2": sp.Rational(1, 9)},
        "cycle_angle_sum": {"j1": sp.Rational(1, 3), "j2": sp.Rational(1, 3)},
        "count": {"j1": sp.Integer(1), "j2": sp.Integer(1)},
        "unit_event_rate": {"j1": sp.Rational(1, 2), "j2": sp.Rational(1, 2)},
        "arbitrary_positive_rate": {"j1": sp.Integer(5), "j2": sp.Integer(5)},
    }
    expected = {
        "direct_density": sp.Rational(2, 9),
        "cycle_angle_sum": sp.Rational(2, 3),
        "count": sp.Integer(2),
        "unit_event_rate": sp.Integer(1),
        "arbitrary_positive_rate": sp.Integer(10),
    }
    totals = {name: additive_total(values, frozenset(records)) for name, values in assignments.items()}
    for name, values in assignments.items():
        check(f"{name} is additive over formed record collections", is_additive(values, records))
        check(f"{name} total is expected", sp.simplify(totals[name] - expected[name]) == 0, totals[name])
    pairwise_different = all(sp.simplify(totals[left] - totals[right]) != 0 for left, right in itertools.combinations(totals, 2))
    check("same formed records support mutually different event/readout assignments", pairwise_different, totals)
    check("formation existence alone does not pick direct density", totals["direct_density"] != totals["count"] and totals["direct_density"] != totals["unit_event_rate"])

    section("D - non-supply conclusion")

    check(
        "occurrence hygiene no-go keeps event/rate content outside",
        "event law plus rate/readout license" in occurrence_flat
        and "A future occurrence theorem is not ruled out." in occurrence,
    )
    check(
        "direct-license no-go keeps Record readout license unsupplied",
        "Every real `beta` satisfies empty-zero" in direct_license_flat
        and "do not entail `beta=1`" in direct_license_flat,
    )
    check("angle no-go keeps occurrence-lane clock/event route live", "Occurrence-lane clock/event route" in angle)
    check(
        "delta chain isolates R-eta as conditional input",
        "R-eta is a dimensionless readout-class" in delta_flat
        or "R-eta is the named conditional input" in delta_flat
        or "R-\u03b7 is a dimensionless readout-class" in delta_flat,
    )
    check("note states formation does not supply event/rate law", "does not supply a formation rule, event rate" in note_flat)
    check("note requires separate occurrence or readout theorem", "requires a separate inhomogeneous readout theorem" in note_flat)
    check("new note is a source-side bounded no-go", "**Claim type:** no_go" in note and "source-side bounded no-go" in note)

    banned = [
        "R-eta is derived",
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "premise registry is edited",
        "Record derives R-eta",
        "all future occurrence-lane routes are closed",
        "audited_clean",
        "retained_no_go",
    ]
    found = [phrase for phrase in banned if phrase in note]
    check("banned overclaim phrases are absent", not found, found)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
