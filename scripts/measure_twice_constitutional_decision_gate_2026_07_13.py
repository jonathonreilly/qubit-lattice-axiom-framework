#!/usr/bin/env python3
"""Executable gate for the July 13 measure-twice constitutional decision."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import json
import math


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "MEASURE_TWICE_CONSTITUTIONAL_DECISION_PACKET_NOTE_2026-07-13.md"
LAW_CONTRACT = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PASS = 0
FAIL = 0
OPEN = -1
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def source_contract() -> None:
    section("A - Authority and recommendation contract")
    note = NOTE.read_text(encoding="utf-8").lower()
    contract = LAW_CONTRACT.read_text(encoding="utf-8").lower()
    normalized_note = note.replace("*", "").replace("`", "")
    normalized_contract = contract.replace("*", "").replace("`", "")
    check("A decision packet is authority-free", "authority: none" in normalized_note)
    check("A law contract is authority-free", "authority: none" in normalized_contract)
    check("A recommendation defers frozen axiom text", "do not freeze axiom text yet" in normalized_note)
    check("A live files are declared untouched", "live axiom and premise-registry files remain untouched" in " ".join(note.split()))
    check("A no universal impossibility claim", "no broad no-go is claimed" in normalized_note)
    check("A N1-N8 is complete", all(f"### n{index}" in note for index in range(1, 9)))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[int, ...], ...]:
    rotations = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(axis_permutation) * math.prod(signs) != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][axis_permutation[row]] = signs[row]
            direction_permutation = []
            for direction in DIRECTIONS:
                rotated = tuple(
                    sum(matrix[row][column] * direction[column] for column in range(3))
                    for row in range(3)
                )
                direction_permutation.append(DIR_INDEX[rotated])
            rotations.append(tuple(direction_permutation))
    return tuple(rotations)


def two_rule_nonuniqueness() -> None:
    section("B - Two distinct structurally admissible availability rules")

    neighborhoods = list(product((OPEN, 0, 1), repeat=6))
    rotations = proper_cubic_rotations()

    def copy_neighbor(neighbors: tuple[int, ...]) -> frozenset[int]:
        represented = frozenset(value for value in neighbors if value != OPEN)
        return represented if represented else frozenset((0, 1))

    def modal_support(neighbors: tuple[int, ...]) -> frozenset[int]:
        recorded = tuple(value for value in neighbors if value != OPEN)
        if not recorded:
            return frozenset((0, 1))
        counts = {value: recorded.count(value) for value in (0, 1)}
        maximum = max(counts.values())
        return frozenset(value for value, count in counts.items() if count == maximum)

    rules = (copy_neighbor, modal_support)
    check("B proper cubic group has 24 rotations", len(set(rotations)) == 24)
    check("B ternary neighborhood domain has 729 profiles", len(neighborhoods) == 729)
    for index, rule in enumerate(rules, start=1):
        check(f"B rule {index} is total and nonempty", all(rule(n) for n in neighborhoods))
        check(f"B rule {index} is invariant under all proper cubic rotations", all(
            rule(n) == rule(tuple(n[position] for position in rotation))
            for n in neighborhoods
            for rotation in rotations
        ))
        check(f"B rule {index} is possibility-swap covariant", all(
            rule(tuple(OPEN if value == OPEN else 1 - value for value in n))
            == frozenset(1 - value for value in rule(n))
            for n in neighborhoods
        ))
        check(f"B rule {index} varies with neighbor conditions", len({rule(n) for n in neighborhoods}) > 1)
    witness = (0, 0, 0, 0, 1, 1)
    check("B the two rules return different availability answers", copy_neighbor(witness) == frozenset((0, 1)) and modal_support(witness) == frozenset((0,)))
    check("B structural wording therefore does not identify one availability table", any(copy_neighbor(n) != modal_support(n) for n in neighborhoods))


def record_nonreconnection_theorem() -> None:
    section("C - Site-tagged immutable extension plus uniqueness implies nonreconnection")

    possible_states = ({}, {"x": 0}, {"x": 1})

    def preserves(source: dict[str, int], target: dict[str, int]) -> bool:
        return all(target.get(site) == content for site, content in source.items())

    branch_zero = {"x": 0}
    branch_one = {"x": 1}
    future_zero = [state for state in possible_states if preserves(branch_zero, state)]
    future_one = [state for state in possible_states if preserves(branch_one, state)]
    check("C every zero-record future preserves site and content", future_zero == [branch_zero])
    check("C every one-record future preserves site and content", future_one == [branch_one])
    check("C conflicting same-site record futures do not reconnect", not any(state in future_one for state in future_zero))
    check("C theorem is conditional on site-tagged immutable-extension semantics", len(set(tuple(sorted(state.items())) for state in future_zero) & set(tuple(sorted(state.items())) for state in future_one)) == 0)


def live_surface_guard() -> None:
    section("D - Live constitution and registry guard")
    axioms = AXIOMS.read_text(encoding="utf-8")
    normalized_axioms = " ".join(axioms.split())
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("D current axiom still says one fixed admissibility rule", "There is one fixed nearest-neighbor admissibility rule" in axioms)
    check("D current Record wording remains unchanged", "A site never carries more than one record; records are permanent." in normalized_axioms)
    check("D no candidate continuation sentence landed", "Every lawful continuation preserves" not in axioms)
    check("D no generated-composition sentence landed", "joint possibility domains are generated" not in axioms)
    expected_ids = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("D premise registry still has exactly four canonical ids", registry.get("canonical_ids") == expected_ids)
    check("D no canonical law premise node was silently added", "canonical_law" not in registry.get("nodes", {}))


def classification_contract() -> None:
    section("E - Complete classification contract")
    note = NOTE.read_text(encoding="utf-8").lower()
    normalized_note = note.replace("`", "")
    required_rows = (
        "exact nearest-neighbor answer",
        "physical carrier / generated composition",
        "complete record state",
        "formation trigger and finite certificate",
        "exact same-site/content permanence",
        "actuality",
        "contextual physical statistics",
        "duration, rate, clock normalization, lapse",
        "exchange statistics, chirality, species, gauge, masses",
        "capacity, active source, entropy, wep, gravity",
        "low-record/low-entropy initial history",
        "two-witness count",
        "reading as formation or locking",
        "clock as final lock",
        "compute/storage limit",
        "possibility-counting sentence",
    )
    for row in required_rows:
        check(f"E classified: {row}", row in note)
    check("E all readiness gates are represented", all(marker in normalized_note for marker in (
        "exact predictive specification written", "law domain/composition fixed", "state sufficiency",
        "formation finite certificate", "permanence under all physical continuations",
        "contextual statistics", "repository o/t/i/g/b checklist from one coherent framework",
    )))


def law_contract_fields() -> None:
    section("F - Canonical law completeness fields")
    text = LAW_CONTRACT.read_text(encoding="utf-8")
    foundational = (
        "`DOMAIN`", "`STATE`", "`CONTEXT`", "`ATOMIC_LAW`", "`CONTINUATION`",
        "`AVAILABILITY`", "`CONCURRENCY`", "`RECORD`", "`ACTUALITY`", "`STATISTICS`",
    )
    interfaces = ("`OPERATIONAL`", "`CLOCK`", "`MATTER`", "`RESOURCE`", "`CONTINUUM`", "`GRAVITY`", "`BOUNDARY`")
    for field in foundational:
        check(f"F foundational field {field}", field in text)
    for field in interfaces:
        check(f"F interface field {field}", field in text)
    check("F predictive-specification checklist remains open", "This checklist is not yet satisfied" in text)


def main() -> int:
    source_contract()
    two_rule_nonuniqueness()
    record_nonreconnection_theorem()
    live_surface_guard()
    classification_contract()
    law_contract_fields()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("RECOMMENDATION: do not freeze axiom text yet; first derive or supply the predictive specification, or prove its physical-equivalence class")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
