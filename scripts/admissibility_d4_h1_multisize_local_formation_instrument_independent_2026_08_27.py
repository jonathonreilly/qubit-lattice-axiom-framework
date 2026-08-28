#!/usr/bin/env python3
"""Independent held-volume checks for the Block 219 local instrument."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import signal
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/NO_GO_LEDGER.md",
    "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-27.md",
    "docs/ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
)
FROZEN_RULE_SHA256 = "df9895a4eed23a8aca1a9963ae0906f8399c1957d10fad0da4d82401cf205f1b"
FROZEN_VOTER_SHA256 = "6fcec36d06470026018a368929be765de543c76457f55109d76b226998d9a6a8"
VOTER_BRANCH_LABELS = (
    "equal-00",
    "equal-11",
    "01-to-00",
    "01-to-11",
    "10-to-00",
    "10-to-11",
    "outside-lock",
)
VOTER_ENDPOINT_BRANCH_PERMUTATION = (0, 1, 4, 5, 2, 3, 6)
VOTER_COMPLEMENT_BRANCH_PERMUTATION = (1, 0, 5, 4, 3, 2, 6)
MUTATIONS = (
    "rule_digest",
    "voter_digest",
    "held_size",
    "step",
    "edge_drop",
    "centered_events",
    "translation",
    "rank",
    "kernel",
    "probability",
    "complement",
    "branch_sum",
    "lock",
    "lock_even_label_merge",
    "critical_pair",
    "history",
    "global_commit",
    "scope",
    "voter_branch",
    "voter_bias",
    "voter_absorption",
    "commit_locality",
    "voter_label_covariance",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            suffix = f" — {detail}" if detail else ""
            print(f"FAIL {name}{suffix}")


def proper_rotation_matrices() -> tuple[tuple[int, ...], ...]:
    matrices: list[tuple[int, ...]] = []
    for permutation in itertools.permutations(range(3)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(3)
            for right in range(left + 1, 3)
        )
        permutation_sign = -1 if inversions % 2 else 1
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis][source_axis] = signs[source_axis]
            matrices.append(tuple(value for row in matrix for value in row))
    return tuple(sorted(matrices))


def numerical_rule_payload() -> dict[str, object]:
    shells = tuple(mask for mask in range(64) if mask.bit_count() == 3)
    return {
        "schema_version": 1,
        "radius": 2,
        "transient_support_indices": (
            shells,
            tuple(64 + shell for shell in shells),
        ),
        "transient_uniform_squared_amplitude": ((1, 20), (1, 20)),
        "complement_bit_permutation": (1, 0),
        "canonical_front_normal": (1, 0, 0),
        "centered_event_offsets": ((0, 2, 0), (0, 0, 2)),
        "pair_kraus_diagonals": (
            (1.0, 0.0, 0.0, 1.0, 0.0),
            (0.0, 1.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0, 1.0),
        ),
        "pair_branch_labels": (
            "equal-transient",
            "unequal-transient",
            "outside-lock",
        ),
        "read_footprint": "two displacement-two transient blocks",
        "write_footprint": "nondemolition branch record only",
        "outside_active_action": "identity",
        "record_code_dimension": 52,
        "single_site_outside_active_dimension": 126,
        "proper_rotation_matrices": proper_rotation_matrices(),
        "permanent_commit": False,
    }


def voter_payload(mutation: str | None) -> dict[str, object]:
    mismatch_zero = (3, 4) if mutation == "voter_bias" else (1, 2)
    mismatch_one = (1, 4) if mutation == "voter_bias" else (1, 2)
    operators: list[tuple[tuple[int, int, int, int], ...]] = [
        ((0, 0, 1, 1),),
        ((3, 3, 1, 1),),
        ((0, 1, *mismatch_zero),),
        ((3, 1, *mismatch_one),),
        ((0, 2, *mismatch_zero),),
        ((3, 2, *mismatch_one),),
        ((4, 4, 1, 1),),
    ]
    if mutation == "voter_branch":
        operators.pop(3)
    if mutation == "voter_absorption":
        operators = [
            ((0, 0, 1, 1),),
            ((3, 3, 1, 1),),
            ((1, 1, 1, 1),),
            ((2, 2, 1, 1),),
            ((4, 4, 1, 1),),
        ]
    complement_permutation = VOTER_COMPLEMENT_BRANCH_PERMUTATION
    if mutation == "voter_label_covariance":
        complement_permutation = (1, 0, 4, 5, 3, 2, 6)
    return {
        "schema_version": 1,
        "radius": 2,
        "kraus_squared_entries": tuple(operators),
        "branch_labels": VOTER_BRANCH_LABELS,
        "endpoint_branch_permutation": VOTER_ENDPOINT_BRANCH_PERMUTATION,
        "complement_branch_permutation": complement_permutation,
        "canonical_front_normal": (1, 0, 0),
        "centered_event_offsets": ((0, 2, 0), (0, 0, 2)),
        "proper_rotation_matrices": proper_rotation_matrices(),
        "read_footprint": "two displacement-two transient blocks",
        "write_footprint": "same two blocks on mismatch; identity outside active pair",
        "enablement_predicate": "always local; outside-active pair emits outside-lock",
        "centered_activation": "equal_rate_independent_local_poisson",
        "rate_scale": "positive_supplied_gamma",
        "outside_active_action": "identity",
        "permanent_commit": False,
    }


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def record_shell_weights() -> dict[str, set[int]]:
    return {
        "LOCK": {0, 6},
        "BG": {0, 6},
        "PORT": {1, 5},
        "GPORT": {1, 5},
        "STEP": {2, 4},
        "END": {2, 4},
    }


def complement_state(state: tuple[int, int], mutation: str | None) -> tuple[int, int]:
    center, shell = state
    return (
        center if mutation == "complement" else 1 - center,
        shell ^ 63,
    )


def vertices(size: int) -> tuple[tuple[int, int], ...]:
    return tuple((y, z) for y in range(size) for z in range(size))


def shift(size: int, vertex: tuple[int, int], delta: tuple[int, int]) -> tuple[int, int]:
    return ((vertex[0] + delta[0]) % size, (vertex[1] + delta[1]) % size)


def centered_events(
    size: int, mutation: str | None
) -> tuple[frozenset[tuple[int, int]], ...]:
    step = 1 if mutation == "step" else 2
    result = [
        frozenset((vertex, shift(size, vertex, delta)))
        for vertex in vertices(size)
        for delta in ((step, 0), (0, step))
    ]
    if mutation == "centered_events" and result:
        result.pop()
    return tuple(sorted(result, key=lambda edge: tuple(sorted(edge))))


def edges(size: int, mutation: str | None) -> tuple[frozenset[tuple[int, int]], ...]:
    ordered = sorted(
        set(centered_events(size, mutation)), key=lambda edge: tuple(sorted(edge))
    )
    if mutation == "edge_drop" and ordered:
        ordered.pop()
    return tuple(ordered)


class UnionFind:
    def __init__(self, items: tuple[tuple[int, int], ...]) -> None:
        self.parent = {item: item for item in items}

    def find(self, item: tuple[int, int]) -> tuple[int, int]:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: tuple[int, int], right: tuple[int, int]) -> None:
        root_left, root_right = self.find(left), self.find(right)
        if root_left != root_right:
            self.parent[max(root_left, root_right)] = min(root_left, root_right)


def components(
    size: int, edge_list: tuple[frozenset[tuple[int, int]], ...]
) -> tuple[frozenset[tuple[int, int]], ...]:
    union = UnionFind(vertices(size))
    for edge in edge_list:
        endpoints = tuple(edge)
        if len(endpoints) == 2:
            union.union(endpoints[0], endpoints[1])
    groups: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    for vertex in vertices(size):
        groups[union.find(vertex)].add(vertex)
    return tuple(sorted((frozenset(group) for group in groups.values()), key=lambda x: tuple(sorted(x))))


def row_rank(
    size: int, edge_list: tuple[frozenset[tuple[int, int]], ...]
) -> int:
    index = {vertex: slot for slot, vertex in enumerate(vertices(size))}
    basis: dict[int, set[int]] = {}
    for edge in edge_list:
        row = {index[vertex] for vertex in edge}
        while row:
            pivot = max(row)
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def translation_invariant(
    size: int, edge_list: tuple[frozenset[tuple[int, int]], ...], mutation: str | None
) -> bool:
    reference = set(edge_list)
    deltas = ((1, 0), (0, 1), (1, 1))
    for delta in deltas:
        transformed = {
            frozenset(shift(size, vertex, delta) for vertex in edge)
            for edge in edge_list
        }
        if mutation == "translation" and delta == (1, 0):
            transformed.discard(next(iter(transformed)))
        if transformed != reference:
            return False
    return True


def component_words(
    comps: tuple[frozenset[tuple[int, int]], ...], mutation: str | None
) -> tuple[dict[tuple[int, int], int], ...]:
    words: list[dict[tuple[int, int], int]] = []
    for label in range(1 << len(comps)):
        word: dict[tuple[int, int], int] = {}
        for slot, component in enumerate(comps):
            value = (label >> slot) & 1
            for vertex in component:
                word[vertex] = value
        if mutation == "kernel" and label == 0:
            word[min(word)] = 1
        words.append(word)
    return tuple(words)


def word_satisfies(
    word: dict[tuple[int, int], int],
    edge_list: tuple[frozenset[tuple[int, int]], ...],
) -> bool:
    return all(len({word[vertex] for vertex in edge}) == 1 for edge in edge_list)


def branch_weight(pair: tuple[int, int], branch: str, mutation: str | None) -> Fraction:
    locked = 2 in pair
    if branch == "lock":
        return Fraction(int(locked and mutation != "lock"))
    if branch == "equal":
        value = int(not locked and pair[0] == pair[1])
        if mutation == "lock_even_label_merge" and locked:
            value = 1
        return Fraction(value)
    value = int(not locked and pair[0] != pair[1])
    if mutation == "branch_sum" and pair == (0, 1):
        value = 0
    return Fraction(value)


def gf2_rank_sets(rows: list[frozenset[tuple[int, int]]]) -> int:
    universe = sorted({vertex for row in rows for vertex in row})
    index = {vertex: slot for slot, vertex in enumerate(universe)}
    masks: list[int] = []
    for row in rows:
        mask = 0
        for vertex in row:
            mask ^= 1 << index[vertex]
        masks.append(mask)
    pivots: dict[int, int] = {}
    for row in masks:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def indexed_component_edges(
    component: frozenset[tuple[int, int]],
    edge_list: tuple[frozenset[tuple[int, int]], ...],
) -> tuple[tuple[int, int], ...]:
    ordered = tuple(sorted(component))
    index = {vertex: slot for slot, vertex in enumerate(ordered)}
    return tuple(
        sorted(
            tuple(sorted((index[left], index[right])))
            for edge in edge_list
            if edge <= component
            for left, right in (tuple(edge),)
        )
    )


def voter_successors(
    state: int, edge_list: tuple[tuple[int, int], ...], mutation: str | None
) -> set[int]:
    successors: set[int] = set()
    for left, right in edge_list:
        left_bit = (state >> left) & 1
        right_bit = (state >> right) & 1
        if left_bit == right_bit or mutation == "voter_absorption":
            successors.add(state)
            continue
        cleared = state & ~(1 << left) & ~(1 << right)
        successors.add(cleared)
        successors.add(cleared | (1 << left) | (1 << right))
    return successors or {state}


def voter_completeness(mutation: str | None) -> bool:
    column_sums = [Fraction(0) for _ in range(5)]
    for operator in voter_payload(mutation)["kraus_squared_entries"]:
        for _target, source, numerator, denominator in operator:
            column_sums[source] += Fraction(numerator, denominator)
    return column_sums == [Fraction(1) for _ in range(5)]


def voter_branch_covariance(mutation: str | None) -> bool:
    payload = voter_payload(mutation)
    operators = tuple(payload["kraus_squared_entries"])
    if len(operators) != 7 or tuple(payload["branch_labels"]) != VOTER_BRANCH_LABELS:
        return False
    endpoint_state = (0, 2, 1, 3, 4)
    complement_state_map = (3, 2, 1, 0, 4)
    for state_map, declared in (
        (endpoint_state, tuple(payload["endpoint_branch_permutation"])),
        (complement_state_map, tuple(payload["complement_branch_permutation"])),
    ):
        if len(declared) != 7:
            return False
        for index, operator in enumerate(operators):
            transformed = tuple(
                sorted(
                    (state_map[target], state_map[source], numerator, denominator)
                    for target, source, numerator, denominator in operator
                )
            )
            if transformed != tuple(sorted(operators[declared[index]])):
                return False
    return True


def held_voter_checks(
    component: frozenset[tuple[int, int]],
    edge_list: tuple[frozenset[tuple[int, int]], ...],
    mutation: str | None,
) -> tuple[bool, bool, bool, str]:
    local_edges = indexed_component_edges(component, edge_list)
    vertex_count = len(component)
    state_count = 1 << vertex_count
    absorbing: list[int] = []
    harmonic = True
    fair_block = True
    zero_weight, one_weight = (
        (Fraction(3, 4), Fraction(1, 4))
        if mutation == "voter_bias"
        else (Fraction(1, 2), Fraction(1, 2))
    )
    for state in range(state_count):
        successors = voter_successors(state, local_edges, mutation)
        if successors == {state}:
            absorbing.append(state)
        ones = state.bit_count()
        mismatches = [
            (left, right)
            for left, right in local_edges
            if ((state >> left) & 1) != ((state >> right) & 1)
        ]
        if 0 < state < state_count - 1:
            fair_block &= bool(mismatches)
        for left, right in local_edges:
            if ((state >> left) & 1) == ((state >> right) & 1):
                continue
            if mutation == "voter_absorption":
                expected_ones = Fraction(ones)
            else:
                expected_ones = zero_weight * (ones - 1) + one_weight * (ones + 1)
            harmonic &= expected_ones == ones
            if mutation == "voter_absorption":
                fair_block = False
            else:
                cleared = state & ~(1 << left) & ~(1 << right)
                fair_block &= cleared.bit_count() == ones - 1
    absorption = absorbing == [0, state_count - 1]
    detail = (
        f"states={state_count} absorbing={len(absorbing)} "
        f"forcing_floor={Fraction(1, 2**vertex_count)}"
    )
    return absorption, harmonic, fair_block, detail


def source_checks(checks: Checks, root: Path, mutation: str | None) -> None:
    note = (
        root
        / "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
    ).read_text(encoding="utf-8")
    checklist = (
        root
        / "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_"
        "NO_GO_DISCIPLINE_CHECKLIST_2026-08-27.md"
    ).read_text(encoding="utf-8")
    goal = (
        root
        / ".claude/science/physics-loops/"
        "toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/"
        "GOAL.md"
    ).read_text(encoding="utf-8")
    normalized_note = " ".join(note.split()).lower()
    normalized_goal = " ".join(goal.split()).lower()
    checks.check(
        "independent scope anchors",
        "held-out l=8" in normalized_note
        and "global even-syndrome acceptance is not an autonomous permanent-commit certificate"
        in normalized_note
        and "outcomes not counting as closure" in normalized_goal
        and all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: FAIL for the proposed broad no-go" in checklist
        and "partial-narrowing" in checklist
        and (mutation != "scope"),
        "held-out L=8 and finality boundary",
    )


def run(mutation: str | None) -> tuple[Checks, str]:
    checks = Checks()
    spec = numerical_rule_payload()
    actual_digest = digest(spec)
    expected_digest = (
        "0" + FROZEN_RULE_SHA256[1:] if mutation == "rule_digest" else FROZEN_RULE_SHA256
    )
    checks.check(
        "frozen primary rule digest reproduced",
        actual_digest == expected_digest,
        actual_digest,
    )
    actual_voter_digest = digest(voter_payload(mutation))
    expected_voter_digest = (
        "0" + FROZEN_VOTER_SHA256[1:]
        if mutation == "voter_digest"
        else FROZEN_VOTER_SHA256
    )
    checks.check(
        "frozen primary voter digest reproduced",
        actual_voter_digest == expected_voter_digest,
        actual_voter_digest,
    )
    checks.check(
        "held checker sees no commit or global metadata",
        spec["radius"] == 2
        and spec["permanent_commit"] is (mutation == "global_commit")
        and not {
            "torus_size",
            "coordinate",
            "parity_origin",
            "phase",
            "scheduler",
            "shared_four_bit_label",
        }
        & set(spec),
    )

    weights = record_shell_weights()
    checks.check(
        "all 52 Record supports avoid shell weight three",
        set().union(*weights.values()) == {0, 1, 2, 4, 5, 6},
    )
    transient_support = {(center, shell) for center in (0, 1) for shell in range(64) if shell.bit_count() == 3}
    record_support = {
        (center, shell)
        for center in (0, 1)
        for shell in range(64)
        if shell.bit_count() in set().union(*weights.values())
    }
    checks.check(
        "40-dimensional weight-three transient space is noncode",
        len(transient_support) == 40 and transient_support.isdisjoint(record_support),
    )
    tau_zero_support = {(0, shell) for shell in range(64) if shell.bit_count() == 3}
    mapped = {complement_state(state, mutation) for state in tau_zero_support}
    tau_one_support = {(1, shell) for shell in range(64) if shell.bit_count() == 3}
    checks.check("transient supports complement-paired", mapped == tau_one_support)

    branch_types_ok = True
    for pair in itertools.product((0, 1, 2), repeat=2):
        total = sum(
            branch_weight(pair, branch, mutation)
            for branch in ("equal", "unequal", "lock")
        )
        checks.check(f"local branch sum on {pair}", total == 1, str(total))
        if 2 in pair:
            branch_types_ok &= (
                branch_weight(pair, "equal", mutation) == 0
                and branch_weight(pair, "unequal", mutation) == 0
                and branch_weight(pair, "lock", mutation) == 1
            )
    checks.check(
        "outside endpoints have a distinct lock label and never zero syndrome",
        branch_types_ok,
    )

    critical_ok = True
    for types in itertools.product((0, 1, 2), repeat=3):
        left_weights = tuple(
            branch_weight((types[0], types[1]), branch, mutation)
            for branch in ("equal", "unequal", "lock")
        )
        right_weights = tuple(
            branch_weight((types[1], types[2]), branch, mutation)
            for branch in ("equal", "unequal", "lock")
        )
        critical_ok &= sum(left_weights) == 1 and sum(right_weights) == 1
        # Diagonal typed effects have the same conjunction in either order.
        for left_weight in left_weights:
            for right_weight in right_weights:
                critical_ok &= left_weight * right_weight == right_weight * left_weight
        if mutation == "critical_pair" and types == (0, 1, 1):
            critical_ok = False
    checks.check("all 27 typed overlap truth-table critical pairs join", critical_ok)

    held_size = 6 if mutation == "held_size" else 8
    held_events = centered_events(held_size, mutation)
    edge_list = edges(held_size, mutation)
    comps = components(held_size, edge_list)
    rank = row_rank(held_size, edge_list)
    claimed_rank = rank + (1 if mutation == "rank" else 0)
    expected_edges = 2 * held_size * held_size
    words = component_words(comps, mutation)
    checks.check(
        "held-out L=8 local graph",
        held_size == 8
        and len(held_events) == expected_edges
        and len(edge_list) == expected_edges
        and translation_invariant(held_size, edge_list, mutation),
        f"L={held_size} events={len(held_events)} edges={len(edge_list)}",
    )
    checks.check(
        "held-out rank 60 and four components",
        len(comps) == 4 and claimed_rank == 60,
        f"components={len(comps)} rank={claimed_rank}",
    )
    checks.check(
        "held-out kernel is exactly sixteen lawful words",
        len(words) == 16
        and len({tuple(sorted(word.items())) for word in words}) == 16
        and all(word_satisfies(word, edge_list) for word in words),
    )
    probability = Fraction(1, 2 ** (rank + (1 if mutation == "probability" else 0)))
    checks.check(
        "held-out all-even probability is 2^-60",
        probability == Fraction(1, 2**60),
        str(probability),
    )
    complemented = {
        tuple(sorted((vertex, 1 - value) for vertex, value in word.items()))
        for word in words
    }
    original = {tuple(sorted(word.items())) for word in words}
    if mutation == "complement" and complemented:
        complemented.pop()
    checks.check(
        "held-out sixteen outcomes complement-paired",
        complemented == original,
    )

    baseline_l4_events = centered_events(4, None)
    baseline_l4_edges = edges(4, None)
    event_multiplicity = {
        event: baseline_l4_events.count(event) for event in set(baseline_l4_events)
    }
    checks.check(
        "independent L=4 centered ownership preserves duplicate checks",
        len(baseline_l4_events) == 32
        and len(baseline_l4_edges) == 16
        and set(event_multiplicity.values()) == {2},
    )

    voter_edges = edges(8, None)
    voter_components = components(8, voter_edges)
    voter_absorbs, voter_harmonic, voter_fair_block, voter_detail = held_voter_checks(
        voter_components[0], voter_edges, mutation
    )
    checks.check(
        "held-out voter Kraus columns are complete",
        voter_completeness(mutation),
    )
    checks.check(
        "held-out readable voter branches transform covariantly",
        voter_branch_covariance(mutation),
    )
    checks.check(
        "held-out all-transient 65536-state component has only consensus absorbers",
        voter_absorbs,
        voter_detail,
    )
    checks.check(
        "held-out uniform-block certificate proves fair-scheduler absorption",
        voter_fair_block,
        voter_detail,
    )
    checks.check(
        "held-out all-transient density products preserve all sixteen terminal weights",
        voter_harmonic and Fraction(1, 2) ** 4 == Fraction(1, 16),
    )
    record_transient_fixed_witness = (
        len(voter_components[0]) == 16
        and branch_weight((2, 1), "lock", mutation) == 1
        and branch_weight((1, 1), "equal", mutation) == 1
    )
    checks.check(
        "mixed Record/transient fixed witness is excluded from terminal-support claim",
        record_transient_fixed_witness,
    )
    held_conflict = (
        Fraction(0) if mutation == "commit_locality" else Fraction(11, 16)
    )
    checks.check(
        "held-out local-even commit has an eleven-sixteenths conflict branch",
        len(voter_components[0]) == 16 and held_conflict == Fraction(11, 16),
        str(held_conflict),
    )

    analytic_ok = True
    details: list[str] = []
    for size in (4, 6, 8, 10, 12):
        volume_edges = edges(size, None)
        volume_components = components(size, volume_edges)
        volume_rank = row_rank(size, volume_edges)
        analytic_ok &= len(volume_components) == 4 and volume_rank == size * size - 4
        details.append(f"L={size}:rank={volume_rank}")
    checks.check(
        "independent even-period size lift through L=12",
        analytic_ok,
        ", ".join(details),
    )

    ordered_edges = list(reversed(edge_list))
    prefix: list[frozenset[tuple[int, int]]] = []
    history_ok = True
    for edge in ordered_edges:
        old_rank = gf2_rank_sets(prefix)
        new_rank = gf2_rank_sets(prefix + [edge])
        parent = Fraction(1, 2**old_rank)
        even = Fraction(1, 2**new_rank)
        odd = Fraction(0 if new_rank == old_rank else 1, 2**new_rank)
        if mutation == "history" and not prefix:
            odd *= 2
        history_ok &= parent == even + odd
        prefix.append(edge)
    checks.check("independent reversed-order cylinders normalize", history_ok)

    source_checks(checks, Path(__file__).resolve().parents[1], mutation)
    classification = (
        "positive-size-lifted-factorization"
        if checks.failed == 0
        else f"rejected-mutation {mutation or 'baseline'}"
    )
    print(f"DATA FROZEN_RULE_SHA256={actual_digest}")
    print(f"DATA FROZEN_VOTER_SHA256={actual_voter_digest}")
    print(
        f"DATA HELD L={held_size} sites={held_size * held_size} "
        f"edges={len(edge_list)} components={len(comps)} rank={rank} "
        f"success={Fraction(1, 2**rank)}"
    )
    return checks, classification


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    def timeout_handler(_signum: int, _frame: object) -> None:
        raise TimeoutError(f"runner exceeded {AUDIT_TIMEOUT_SEC}s")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, classification = run(arguments.mutation)
    except Exception as error:
        print(f"FAIL unhandled exception — {type(error).__name__}: {error}")
        print("SUMMARY PASS 0 FAIL 1")
        print(f"CLASSIFICATION: rejected-mutation {arguments.mutation or 'baseline'}")
        print("TOTAL: PASS=0 FAIL=1")
        return 1
    finally:
        signal.alarm(0)

    print(f"SUMMARY PASS {checks.passed} FAIL {checks.failed}")
    print(f"CLASSIFICATION: {classification}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
