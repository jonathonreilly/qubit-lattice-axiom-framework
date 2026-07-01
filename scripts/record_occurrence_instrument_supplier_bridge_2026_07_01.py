#!/usr/bin/env python3
"""Verifier for the record occurrence instrument supplier bridge."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0
BOT = "bot"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def flat(text: str) -> str:
    return " ".join(text.split())


def diag_trace(prob: list[Fraction], effect: list[Fraction]) -> Fraction:
    return sum(p * e for p, e in zip(prob, effect))


def instrument_kernel(prob: list[Fraction], effects: dict[str, list[Fraction]]) -> dict[str, Fraction]:
    return {outcome: diag_trace(prob, effect) for outcome, effect in effects.items()}


def complete_effects(effects: dict[str, list[Fraction]]) -> bool:
    dim = len(next(iter(effects.values())))
    return all(sum(effect[i] for effect in effects.values()) == 1 for i in range(dim))


def positive_effects(effects: dict[str, list[Fraction]]) -> bool:
    return all(entry >= 0 for effect in effects.values() for entry in effect)


def activation(kernel: dict[str, Fraction]) -> Fraction:
    return 1 - kernel[BOT]


def selection(kernel: dict[str, Fraction], available: set[str]) -> dict[str, Fraction] | None:
    a = activation(kernel)
    if a == 0:
        return None
    return {value: kernel[value] / a for value in sorted(available)}


def valid_kernel(kernel: dict[str, Fraction], available: set[str]) -> bool:
    if set(kernel) != available | {BOT}:
        return False
    if any(value < 0 for value in kernel.values()):
        return False
    return sum(kernel.values(), Fraction(0)) == 1


def product_kernel(kernels: list[dict[str, Fraction]]) -> dict[tuple[str, ...], Fraction]:
    joint: dict[tuple[str, ...], Fraction] = {}
    for combo in product(*[list(kernel) for kernel in kernels]):
        weight = Fraction(1)
        for outcome, kernel in zip(combo, kernels):
            weight *= kernel[outcome]
        joint[combo] = weight
    return joint


def extend(boundary: dict[int, str], sites: list[int], outcome: tuple[str, ...]) -> dict[int, str]:
    out = dict(boundary)
    for site, value in zip(sites, outcome):
        if value == BOT:
            continue
        if site in out:
            raise ValueError("attempted overwrite")
        out[site] = value
    return out


def main() -> int:
    print("=== Record occurrence instrument supplier bridge ===")

    files = [
        "docs/RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md",
        "docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md",
        "docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md",
        "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        "docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md",
        "docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    normal = read("docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md")
    activation_note = read("docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md")
    instrument = read("docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md")
    pointer = read("docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md")
    born = read("docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md")
    checklist = read("docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry or axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("axioms supply available possibilities and fixed records", "available subset of possibilities" in axioms and "A record locks exactly one available local possibility" in axioms)
    check("axioms do not supply production process", "record-production process" in axioms)
    check("normal form names activation and selection", "activation probability" in normal and "selection probability" in normal)
    check("activation independence leaves activation open", "activation law" in activation_note and "does not determine `a_x`" in activation_note)
    check("instrument interface supplies kernel after instrument", "supplied instrument" in instrument and "probability kernel" in instrument)
    check("pointer theorem supplies bounded controlled-copy route", "controlled-copy coupling is sufficient" in pointer)
    check("Born bridge preserves occurrence wall", "W_occurrence" in born and "which branch, if any, is written" in born)
    check("checklist separates kernel from produced record", "kernel-only model supports probabilities over possible records" in checklist)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    for node_id in expected_ids:
        check(f"registry node present: {node_id}", node_id in registry["nodes"])
        check(f"registry source exists: {node_id}", exists(registry["nodes"][node_id]["current_path"]))
    check("minimal axioms registry note says no occurrence rule", "occurrence rule" in registry["nodes"]["minimal_axioms"]["note"])
    check("scale primitive supplies units only", "zero dimensionless content" in flat(scale).lower())
    check("kinetic primitive supplies no dynamics", "does not supply" in flat(kinetic).lower() and "dynamics" in flat(kinetic).lower())
    check("realized primitive supplies no state-selection", "state-selection rule" in flat(realized))
    check("P_record_extension is not registered", "P_record_extension" not in registry_text)

    print("\nPART C -- finite lazy instrument")
    prob = [Fraction(3, 5), Fraction(2, 5)]
    q = Fraction(1, 4)
    effects = {
        BOT: [1 - q, 1 - q],
        "0": [q, 0],
        "1": [0, q],
    }
    kernel = instrument_kernel(prob, effects)
    available = {"0", "1"}
    check("effects are positive", positive_effects(effects), effects)
    check("effects are complete", complete_effects(effects), effects)
    check("instrument kernel is valid", valid_kernel(kernel, available), kernel)
    check("lazy kernel has K(bot)=3/4", kernel[BOT] == Fraction(3, 4), kernel)
    check("lazy kernel has K(0)=3/20", kernel["0"] == Fraction(3, 20), kernel)
    check("lazy kernel has K(1)=1/10", kernel["1"] == Fraction(1, 10), kernel)
    check("activation is q", activation(kernel) == q)
    check("conditional selection is rho diagonal", selection(kernel, available) == {"0": Fraction(3, 5), "1": Fraction(2, 5)})
    check("note displays lazy witness", "rho = diag(3/5, 2/5)" in note and "K(1)   = 1/10" in note)

    print("\nPART D -- special cases and unavailable values")
    effects_q0 = {
        BOT: [1, 1],
        "0": [0, 0],
        "1": [0, 0],
    }
    effects_q1 = {
        BOT: [0, 0],
        "0": [1, 0],
        "1": [0, 1],
    }
    kernel_q0 = instrument_kernel(prob, effects_q0)
    kernel_q1 = instrument_kernel(prob, effects_q1)
    check("q=0 is valid no-record kernel", valid_kernel(kernel_q0, available) and activation(kernel_q0) == 0)
    check("q=1 is valid deterministic activation kernel", valid_kernel(kernel_q1, available) and activation(kernel_q1) == 1)
    check("q=1 selection is Born pointer distribution", selection(kernel_q1, available) == {"0": Fraction(3, 5), "1": Fraction(2, 5)})
    one_available = {"0"}
    effects_one = {
        BOT: [1 - q, 1],
        "0": [q, 0],
    }
    kernel_one = instrument_kernel(prob, effects_one)
    check("one-value effects are complete", complete_effects(effects_one), effects_one)
    check("one-value kernel is valid without value 1 outcome", valid_kernel(kernel_one, one_available), kernel_one)
    check("one-value kernel writes only 0", "1" not in kernel_one and kernel_one["0"] == Fraction(3, 20))
    empty_effects = {BOT: [1, 1]}
    empty_kernel = instrument_kernel(prob, empty_effects)
    check("empty availability gives only bot outcome", valid_kernel(empty_kernel, set()) and activation(empty_kernel) == 0)

    print("\nPART E -- disjoint composition and preservation")
    prob2 = [Fraction(1, 2), Fraction(1, 2)]
    q2 = Fraction(2, 5)
    effects2 = {
        BOT: [1 - q2, 1 - q2],
        "A": [q2, 0],
        "B": [0, q2],
    }
    kernel2 = instrument_kernel(prob2, effects2)
    joint = product_kernel([kernel, kernel2])
    check("second local kernel is valid", valid_kernel(kernel2, {"A", "B"}), kernel2)
    check("joint kernel normalizes", sum(joint.values(), Fraction(0)) == 1)
    check("joint all-bot probability is product", joint[(BOT, BOT)] == kernel[BOT] * kernel2[BOT])
    check("joint double-record probability is product", joint[("0", "A")] == kernel["0"] * kernel2["A"])
    boundary = {-1: "fixed"}
    sites = [0, 1]
    extended = {outcome: extend(boundary, sites, outcome) for outcome in joint}
    check("extensions preserve existing record", all(value[-1] == "fixed" for value in extended.values()))
    check("all-bot leaves boundary unchanged", extended[(BOT, BOT)] == boundary)
    check("single record extends one site", extended[("1", BOT)] == {-1: "fixed", 0: "1"})
    check("double record extends both sites", extended[("1", "B")] == {-1: "fixed", 0: "1", 1: "B"})

    print("\nPART F -- note content")
    required_sections = [
        "Claim",
        "Finite Theorem",
        "Explicit Lazy-Instrument Witness",
        "Relation To The Pointer Record Bridge",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "Minimum Foundation Update If Bridge Work Fails",
        "No-Go Discipline Gate",
    ]
    for section_name in required_sections:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note names W_occurrence", "W_occurrence" in note)
    check("note names W_record_instrument", "W_record_instrument" in note)
    check("note says bridge theorem not ontology update", "This is a bridge theorem, not an ontology update" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note gives P_record_extension text", "Given a record boundary and available local possibilities" in note)
    check("note preserves rate/objectivity boundaries", "clock or rate normalization" in note and "local objectivity" in note)

    print("\nPART G -- residual matching and no-go discipline")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Availability-only route",
        "Born-weight route",
        "Post-record history route",
        "Supplied-instrument route",
        "Controlled-copy pointer route",
        "Markov/transfer route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall is W_record_instrument", "Collapsed residual after this bridge" in note and "W_record_instrument" in note)
    check("N3 classifies supplied instrument", "\"Supplied instrument\" is an explicit bridge input" in note)
    check("N4 has seven witness matches", note.count("| `") >= 7 and "Residual Matching" in note)
    check("N5 narrows finite resolution", "finite one-site and disjoint-site" in note)
    check("N6 lists live closure paths", "local Markov or transfer" in note and "source/action or metric/observable" in note)
    check("N7 steelman preserves objection", "given an instrument" in note and "real physics is entirely in deriving the instrument" in note)
    check("N8 cross-cycle echo present", "kernels from tokens" in note and "histories from production" in note)

    print("\nPART H -- non-overclaim checks")
    forbidden = [
        "therefore records always occur",
        "therefore every site records",
        "therefore the ontology derives an instrument",
        "therefore Born weights are excluded",
        "therefore pointer dynamics is unconditionally derived",
        "requires a new ontology axiom",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no terminal no-go", "not a terminal no-go" in note)
    check("note says instrument cannot be assumed from ontology", "claim that physical record production is derived from the ontology alone" in flat_note)
    check("note preserves future bridge derivations", "possible future supplier" in note and "bridge-first routes fail" in note)
    check("note avoids measured-value imports", "measured constants" in note and "PDG" not in note and "lattice-MC values" in note)
    check("explicit non-claim preserves Born weights", "Born weights are excluded" in note and "This note does not claim" in note)

    print("\nPART I -- assembled conclusion")
    bridge_ok = (
        complete_effects(effects)
        and positive_effects(effects)
        and valid_kernel(kernel, available)
        and activation(kernel) == q
        and selection(kernel, available) == {"0": Fraction(3, 5), "1": Fraction(2, 5)}
        and sum(joint.values(), Fraction(0)) == 1
        and all(value[-1] == "fixed" for value in extended.values())
    )
    check("supplied instrument gives occurrence normal form", bridge_ok)
    check("activation and selection are no longer independent once instrument is supplied", "activation and selection are not independent residuals" in flat_note)
    check("physical instrument/trigger remains the wall", "physical instrument/trigger" in note)
    check("no axiom update requested", "No ontology axiom update follows" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- occurrence instrument supplier bridge is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- a supplied record-writing instrument gives the "
        "record-extension activation/selection kernel; the remaining wall is "
        "physical instrument/trigger derivation."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
