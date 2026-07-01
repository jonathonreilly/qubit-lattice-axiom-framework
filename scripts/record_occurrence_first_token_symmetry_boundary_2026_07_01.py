#!/usr/bin/env python3
"""Verifier for the record occurrence first-token symmetry boundary."""

from __future__ import annotations

from itertools import product
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


def cycle_translate_subset(subset: frozenset[int], shift: int, n: int) -> frozenset[int]:
    return frozenset((x + shift) % n for x in subset)


def torus_translate_subset(subset: frozenset[tuple[int, int]], shift: tuple[int, int], size: int) -> frozenset[tuple[int, int]]:
    dx, dy = shift
    return frozenset(((x + dx) % size, (y + dy) % size) for x, y in subset)


def all_subsets(items: list[object]) -> list[frozenset[object]]:
    out: list[frozenset[object]] = []
    count = len(items)
    for mask in range(1 << count):
        out.append(frozenset(items[i] for i in range(count) if mask & (1 << i)))
    return out


def invariant_cycle_subsets(n: int) -> list[frozenset[int]]:
    items = list(range(n))
    return [
        subset
        for subset in all_subsets(items)
        if all(cycle_translate_subset(subset, shift, n) == subset for shift in range(n))
    ]


def invariant_torus_subsets(size: int) -> list[frozenset[tuple[int, int]]]:
    items = [(x, y) for x in range(size) for y in range(size)]
    shifts = [(dx, dy) for dx in range(size) for dy in range(size)]
    return [
        subset
        for subset in all_subsets(items)
        if all(torus_translate_subset(subset, shift, size) == subset for shift in shifts)
    ]


def cycle_translate_partial_record(config: tuple[int | None, ...], shift: int) -> tuple[int | None, ...]:
    n = len(config)
    translated: list[int | None] = [None] * n
    for site, value in enumerate(config):
        translated[(site + shift) % n] = value
    return tuple(translated)


def invariant_binary_partial_records_cycle(n: int) -> list[tuple[int | None, ...]]:
    values: list[int | None] = [None, 0, 1]
    configs = list(product(values, repeat=n))
    return [
        config
        for config in configs
        if all(cycle_translate_partial_record(config, shift) == config for shift in range(n))
    ]


def is_sparse_support(config: tuple[int | None, ...]) -> bool:
    support_size = sum(value is not None for value in config)
    return 0 < support_size < len(config)


def main() -> int:
    print("=== Record occurrence first-token symmetry boundary ===")

    files = [
        "docs/RECORD_OCCURRENCE_FIRST_TOKEN_SYMMETRY_BOUNDARY_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md",
        "docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md",
        "docs/RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01.md",
        "docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md",
        "docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md",
        "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/RECORD_OCCURRENCE_FIRST_TOKEN_SYMMETRY_BOUNDARY_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry = read("docs/audit/data/axiom_premise_nodes.json")
    factor = read("docs/RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md")
    normal = read("docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md")
    instrument = read("docs/RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01.md")
    activation = read("docs/RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md")
    formation = read("docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md")
    pointer = read("docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no axiom/registry edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("axioms include translations", "standard translations" in axioms)
    check("axioms include records as one available possibility", "A record locks exactly one available local possibility" in axioms)
    check("axioms say Admissibility is not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("axioms say no record-production process", "record-production process" in axioms)
    check("registry does not approve P_record_extension", "P_record_extension" not in registry)

    print("\nPART B -- finite transitive subset witnesses")
    inv_cycle = invariant_cycle_subsets(5)
    check("cycle C5 has exactly two invariant subsets", len(inv_cycle) == 2, inv_cycle)
    check("cycle C5 invariant subsets are empty and full", set(map(len, inv_cycle)) == {0, 5}, inv_cycle)
    check("cycle C5 has no invariant singleton support", all(len(s) != 1 for s in inv_cycle), inv_cycle)
    check("cycle C5 has no invariant sparse support", all(len(s) in {0, 5} for s in inv_cycle), inv_cycle)

    inv_torus = invariant_torus_subsets(3)
    check("3x3 torus has exactly two invariant subsets", len(inv_torus) == 2, inv_torus)
    check("3x3 torus invariant subsets are empty and full", set(map(len, inv_torus)) == {0, 9}, inv_torus)
    check("3x3 torus has no invariant one-site support", all(len(s) != 1 for s in inv_torus), inv_torus)
    check("3x3 torus has no invariant sparse support", all(len(s) in {0, 9} for s in inv_torus), inv_torus)

    print("\nPART C -- binary partial-record witnesses")
    inv_records = invariant_binary_partial_records_cycle(5)
    expected_records = {
        (None, None, None, None, None),
        (0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1),
    }
    check("C5 binary invariant partial records are exactly none/all-0/all-1", set(inv_records) == expected_records, inv_records)
    check("C5 invariant partial records have no sparse support", not any(is_sparse_support(config) for config in inv_records), inv_records)
    check("all-record invariant configurations are constant", all(len({v for v in config if v is not None}) <= 1 for config in inv_records), inv_records)
    check("no-record configuration is invariant", (None, None, None, None, None) in inv_records)
    check("all-zero configuration is invariant", (0, 0, 0, 0, 0) in inv_records)
    check("all-one configuration is invariant", (1, 1, 1, 1, 1) in inv_records)

    print("\nPART D -- covariance argument")
    input_state = "empty"
    output_support = frozenset({0})
    translated_input_same = input_state == "empty"
    translated_output_differs = cycle_translate_subset(output_support, 1, 5) != output_support
    check("homogeneous input is translation invariant", translated_input_same)
    check("singleton output is not translation invariant", translated_output_differs)
    check("covariance forbids singleton output from invariant input", translated_input_same and translated_output_differs)
    full_support = frozenset(range(5))
    check("full support is translation invariant", all(cycle_translate_subset(full_support, s, 5) == full_support for s in range(5)))
    empty_support = frozenset()
    check("empty support is translation invariant", all(cycle_translate_subset(empty_support, s, 5) == empty_support for s in range(5)))

    print("\nPART E -- note states the theorem and finite witnesses")
    check("note names homogeneous no-record input", "homogeneous no-record input" in note)
    check("note names deterministic translation-covariant route", "deterministic" in note and "translation-covariant" in note)
    check("note defines sparse/nonempty proper support", "Nonempty proper record support" in note or "nonempty proper record support" in note)
    check("note says output must be translation invariant", "The output is translation invariant" in note)
    check("note states empty/full support result", "empty support" in note and "full support" in note)
    check("note includes C5 witness", "cyclic five-site lattice" in note)
    check("note includes 3x3 torus witness", "`3 x 3` periodic square lattice" in note)
    check("note includes valued record witness", "all sites record 0" in note and "all sites record 1" in note)

    print("\nPART F -- relation to occurrence stack")
    check("factorization names activation and selection", "Activation" in factor and "Selection" in factor)
    check("factorization says neither layer supplies occurrence", "Neither layer supplies occurrence" in factor)
    check("normal form names no-record outcome", "{no record at x} union" in normal)
    check("instrument bridge leaves physical trigger open", "physical derivation or approval" in instrument and "record-writing instrument" in instrument)
    check("activation independence says same available set supports different activation", "same available set supports three activation values" in activation or "Activation Independence" in activation)
    check("formation no-go has no-record witnesses", "H = 0" in formation and "no record" in formation)
    check("pointer theorem remains bounded supplier", "nonzero local controlled-copy coupling is sufficient" in pointer)
    check("primitive recommendation names P_record_extension", "P_record_extension" in primitive)

    print("\nPART G -- audit consequence and minimum update")
    check("note says W_occurrence is narrowed", "narrows `W_occurrence`" in note)
    check("note says occurrence bridge needs symmetry-breaking/stochastic/instrumental content", "symmetry-breaking, stochastic, instrumental, or boundary" in note)
    check("note safe dependency shapes include deterministic boundary route", "record boundary + local deterministic extension law" in note)
    check("note safe dependency shapes include stochastic route", "stochastic extension law + realized draw" in note)
    check("note safe dependency shapes include instrument route", "instrument/trigger + extension kernel" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note sharpens P_record_extension text", "Sparse first-token production also" in note)

    print("\nPART H -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    for route in [
        "Bare deterministic covariance route",
        "Full-support deterministic route",
        "Boundary route",
        "Stochastic route",
        "Instrument/trigger route",
        "Pointer/decoherence route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall is W_sparse_activation_supplier", "W_sparse_activation_supplier" in note)
    check("N3 hidden-wall table classifies deterministic", "| `deterministic` | Explicit route being tested" in note)
    check("N4 residual table includes occurrence witnesses", "RECORD_OCCURRENCE_GATE_FACTORIZATION" in note and "LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM" in note)
    check("N5 narrows the proven sentence", "The proven sentence is only" in note)
    check("N6 lists stochastic and instrument closure paths", "stochastic local record-extension law" in note and "physical trigger or instrument" in note)
    check("N7 steelman preserves stochastic route", "physical occurrence should be stochastic from the start" in flat_note)
    check("N8 cross-cycle echo says sparse realized records need realized draw", "sparse realized records require either a" in flat_note)

    print("\nPART I -- non-overclaim checks")
    overclaim_assertions = [
        "therefore records never occur",
        "therefore record production is impossible",
        "therefore a new ontology axiom is required",
        "therefore all sites must record",
        "therefore all sites must remain unrecorded",
        "therefore Born weights are excluded",
        "therefore stochastic laws fail",
        "therefore instrument routes fail",
    ]
    for phrase in overclaim_assertions:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in flat_note)
    check("note has explicit non-claims section", "## Non-Claims" in note and "This note does not claim:" in note)
    check("non-claims list preserves records-can-occur boundary", "- records never occur;" in note)
    check("non-claims list preserves no-new-ontology boundary", "- a new ontology axiom is required;" in note)
    check("non-claims list preserves stochastic/instrument routes", "stochastic laws, instruments" in note)
    check("note explicitly says not terminal no-go", "not a terminal no-go against record occurrence" in flat_note)
    check("note explicitly leaves stochastic routes open", "Stochastic route" in note and "OPEN" in note)
    check("note explicitly leaves instrument routes open", "Instrument/trigger route" in note and "OPEN/PARTIAL BY PRIOR" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
