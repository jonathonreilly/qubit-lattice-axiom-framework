#!/usr/bin/env python3
"""Verifier for the record occurrence activation independence note."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


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


def validate_kernel(kernel: dict[str, Fraction], available: set[str]) -> bool:
    allowed = available | {"bot"}
    if set(kernel) != allowed:
        return False
    if any(value < 0 for value in kernel.values()):
        return False
    if sum(kernel.values(), Fraction(0, 1)) != 1:
        return False
    unavailable = set(kernel) - allowed
    return all(kernel.get(value, Fraction(0, 1)) == 0 for value in unavailable)


def activation(kernel: dict[str, Fraction]) -> Fraction:
    return Fraction(1, 1) - kernel["bot"]


def conditional_selection(kernel: dict[str, Fraction], available: set[str]) -> dict[str, Fraction] | None:
    a = activation(kernel)
    if a == 0:
        return None
    return {value: kernel[value] / a for value in sorted(available)}


def make_kernel(available: set[str], activation_value: Fraction, selection: dict[str, Fraction]) -> dict[str, Fraction]:
    kernel = {"bot": Fraction(1, 1) - activation_value}
    for value in sorted(available):
        kernel[value] = activation_value * selection[value]
    return kernel


def main() -> int:
    print("=== Record occurrence activation independence ===")

    files = [
        "docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md",
        "docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md",
        "docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md",
        "docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md",
        "docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md",
        "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    factor = read("docs/RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md")
    normal = read("docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md")
    born = read("docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md")
    checklist = read("docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md")
    instrument = read("docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md")
    pointer = read("docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- current premise boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry or axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("minimal axioms are current four-axiom reset", "Lattice / Physical Locality" in axioms and "Record / Fixed Reality" in axioms)
    check("minimal axioms state admissibility is not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("minimal axioms say no record-production process", "record-production process" in axioms)
    check("occurrence factorization names W_occurrence", "W_occurrence" in factor)
    check("occurrence factorization says neither layer supplies occurrence", "Neither layer supplies occurrence" in factor)
    check("normal form names activation and selection", "activation probability" in normal and "selection probability" in normal)
    check("Born bridge preserves occurrence residual", "W_occurrence" in born and "still open" in born)
    check("new note scopes to current-premise independence", "current-premise independence" in note)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    nodes = registry["nodes"]
    for node_id in expected_ids:
        check(f"registry node present: {node_id}", node_id in nodes)
    minimal_note = nodes["minimal_axioms"]["note"]
    check("minimal axioms registry note says no occurrence rule", "no context-selection rule" in minimal_note and "occurrence rule" in minimal_note)
    flat_scale = flat(scale).lower()
    flat_kinetic = flat(kinetic).lower()
    flat_realized = flat(realized).lower()
    check("scale primitive supplies no probability or dynamics", "zero dimensionless content" in flat_scale and "readout bridge" in flat_scale)
    check("kinetic primitive supplies structural isotropy only", "structural statement" in flat_kinetic and "dimensionless dynamical content" in flat_kinetic and "selector" in flat_kinetic)
    check("realized-state primitive supplies no state-selection/probability", "state-selection rule" in flat_realized and "probability rule" in flat_realized)
    check("no registered P_record_extension", "P_record_extension" not in registry_text)

    print("\nPART C -- finite kernel witness")
    available = {"0", "1"}
    k_none = {"bot": Fraction(1, 1), "0": Fraction(0, 1), "1": Fraction(0, 1)}
    k_zero = {"bot": Fraction(0, 1), "0": Fraction(1, 1), "1": Fraction(0, 1)}
    k_half = {"bot": Fraction(1, 2), "0": Fraction(1, 4), "1": Fraction(1, 4)}
    kernels = {"none": k_none, "zero": k_zero, "half": k_half}
    for name, kernel in kernels.items():
        check(f"{name} kernel is valid on same available set", validate_kernel(kernel, available), kernel)
    check("no-activation kernel has a=0", activation(k_none) == 0)
    check("deterministic kernel has a=1", activation(k_zero) == 1)
    check("stochastic kernel has a=1/2", activation(k_half) == Fraction(1, 2))
    check("same available set supports three activation values", {activation(k) for k in kernels.values()} == {Fraction(0, 1), Fraction(1, 2), Fraction(1, 1)})
    check("empty available set forces no-record kernel", validate_kernel({"bot": Fraction(1, 1)}, set()))
    check("note displays finite kernels", "K_none(bot) = 1" in note and "K_zero(0)   = 1" in note and "K_half(1)   = 1/4" in note)

    print("\nPART D -- conditional weights do not fix activation")
    selection = {"0": Fraction(2, 3), "1": Fraction(1, 3)}
    k_a0 = make_kernel(available, Fraction(0, 1), selection)
    k_a_half = make_kernel(available, Fraction(1, 2), selection)
    k_a1 = make_kernel(available, Fraction(1, 1), selection)
    for name, kernel in [("a0", k_a0), ("a_half", k_a_half), ("a1", k_a1)]:
        check(f"{name} weighted kernel is valid", validate_kernel(kernel, available), kernel)
    check("a=1/2 weighted kernel has expected entries", k_a_half["bot"] == Fraction(1, 2) and k_a_half["0"] == Fraction(1, 3) and k_a_half["1"] == Fraction(1, 6), k_a_half)
    check("a=1 weighted conditional selection is p", conditional_selection(k_a1, available) == selection)
    check("a=1/2 weighted conditional selection is same p", conditional_selection(k_a_half, available) == selection)
    check("a=0 has no conditional selection but remains valid no-record kernel", conditional_selection(k_a0, available) is None and activation(k_a0) == 0)
    check("same p supports different activations", {activation(k) for k in [k_a0, k_a_half, k_a1]} == {0, Fraction(1, 2), 1})
    check("note says conditional weights do not supply activation token", "does not supply the activation token" in flat_note)

    print("\nPART E -- source witness matching")
    check("occurrence factorization says activation plus selection", "Activation" in factor and "Selection" in factor and "Preservation" in factor)
    check("kernel normal form preserves no-record outcome", "{no record at x} union" in normal and "a_x" in normal)
    check("Born bridge says weights not occurrence", "which branch, if any, is written as the actual record" in born)
    check("checklist says kernel-only does not produce record", "kernel-only model supports probabilities over possible records" in checklist)
    check("instrument interface separates probability kernel and atom", "probability kernel" in instrument and "realized record atom" in instrument)
    check("pointer theorem is bounded under explicit hypotheses", "explicit finite model" in pointer and "bounded model input" in pointer)
    check("primitive recommendation names P_record_extension", "P_record_extension" in primitive)
    check("primitive recommendation says never force every site", "does not force every site to record" in flat(primitive))
    check("new note N4 table includes seven witnesses", note.count("| `") >= 7 and "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION" in note)

    print("\nPART F -- minimum update and audit consequence")
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note gives P_record_extension text", "Given a record boundary and available local possibilities" in note)
    check("note says primitive exposes activation/selection/rate", "expose activation, selection, and any" in note)
    check("note says not every site records", "would not force every site to record" in note)
    check("note says downstream rows must keep W_occurrence explicit", "must keep `W_occurrence` explicit" in note)
    check("audit consequence requires normal form plus activation law", "local record-extension kernel normal form" in note and "physical occurrence activation law" in note)

    print("\nPART G -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Availability route",
        "Born-weight route",
        "Record-durability route",
        "Post-record history route",
        "Instrument/kernel route",
        "Controlled-copy route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall set is one wall", "W_occurrence_activation." in note)
    check("N3 classifies activation as missing token", "The missing local production token" in note)
    check("N5 narrows resolution", "one-site finite-kernel resolution" in flat_note)
    check("N6 lists live closure paths", "local Markov/transfer generator" in note and "controlled-copy or pointer dynamics" in note)
    check("N7 steelman is substantive", "same law that supplies the instrument" in flat_note)
    check("N8 cross-cycle echo present", "weights are not tokens" in flat_note and "kernels are not produced records" in flat_note)

    print("\nPART H -- non-overclaim checks")
    forbidden = [
        "therefore records never occur",
        "therefore record production is impossible",
        "requires a new ontology axiom",
        "all sites remain unrecorded",
        "therefore Born weights are excluded",
        "there is no future instrument route",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no terminal no-go", "not a terminal no-go" in note)
    check("note says future bridge derivations remain possible", "not a no-go against future bridge derivations" in note)
    check("note preserves future instrument/Markov routes", "future instrument, Markov generator, transfer rule" in note)
    check("note says not every site records", "not force every site to record" in note)
    check("note avoids measured-value imports", "measured" not in note and "PDG" not in note and "lattice-MC" not in note)
    check("explicit non-claim preserves Born weights", "Born weights are excluded" in note and "This note does not claim" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- occurrence activation independence note is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- current premises do not derive occurrence activation; "
        "the missing update is narrow record-extension content."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
