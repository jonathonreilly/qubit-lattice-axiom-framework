#!/usr/bin/env python3
"""Exact certificate for one further crossing of a selected history carrier.

This intentionally tests only the supplied central crossing, before adding a
new exterior-action insertion.  Because the crossing commutes with physical
conditional-Haar Q on the parent stack, every tested image remains in ker Q.
The decisive quantity is the exact rank of the union of the Block245 raw
carrier and all of its once-more-crossed images.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import numpy as np

import admissibility_exterior_character_jr_r3_q2_six_history_gram_2026_08_29 as block245
import admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29 as temporal
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as brauer
import admissibility_exterior_character_jr_r3_q2_second_crossing_leakage_independent_2026_08_29 as independent


PRIME = 1009
SAMPLE = {0: F(1, 5), 1: F(3, 10), 2: F(2, 5), 3: F(1, 2)}
SIGNED_SAMPLE = {0: F(-2, 7), 1: F(3, 10), 2: F(2, 5), 3: F(4, 9)}
IDENTITY_SAMPLE = {power: F(1) for power in range(4)}
T_ZERO_SAMPLE = {0: F(1, 5), 1: F(0), 2: F(2, 5), 3: F(1, 2)}
ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SIX_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_"
    "ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
MUTATIONS = (
    "drop_physical_q_subtraction",
    "omit_baseline_temporal_crossing",
    "collapse_second_crossing",
    "identify_sample_rank_as_generic_exact",
    "identify_temporal_multiplicity_as_new_irreps",
    "claim_global_minimal_memory",
    "axiom_edit",
)


def factor_components(factors):
    remaining = list(range(len(factors)))
    components = []
    while remaining:
        seed = remaining.pop()
        component = {seed}
        labels = set(factors[seed][1])
        changed = True
        while changed:
            changed = False
            for index in remaining[:]:
                if labels.intersection(factors[index][1]):
                    remaining.remove(index)
                    component.add(index)
                    labels.update(factors[index][1])
                    changed = True
        components.append(sorted(component))
    return components


def disconnected_contract(factors, prime):
    result = 1
    for component in factor_components(factors):
        local = [factors[index] for index in component]
        result = result * brauer.greedy_modular_contract(local, prime) % prime
    return result


def selected_names(endpoint, half, prefix):
    base = ("C1",) if endpoint == "Y" else ("C0", "C1")
    return {f"{prefix}_p{index}" for index in half} | {
        f"{prefix}_{label}" for label in base
    }


def contract_sequences(label_a, label_b, prime, sample):
    sector_a, endpoint_a, sequence_a = label_a
    sector_b, endpoint_b, sequence_b = label_b
    occurrences = block245.pair_occurrences(
        endpoint_a, sector_a, endpoint_b, sector_b
    )
    if any(len(local) % 2 for local in occurrences.values()):
        return 0
    operators = {
        power: block245.temporal_operator(power, prime, sample)
        for power in range(1, 4)
    }
    selections_a = [
        selected_names(endpoint_a, half, "a") for half in sequence_a
    ]
    selections_b = [
        selected_names(endpoint_b, half, "b") for half in sequence_b
    ]
    factors = []
    auxiliary = 100_000
    for local in occurrences.values():
        _basis, pairing, inverse_gram = brauer.modular_moment_factors(
            len(local), prime
        )
        column_tensor = pairing
        labels = [column for _name, _row, column in local] + [auxiliary + 1]
        for chosen_names in (*selections_a, *selections_b):
            chosen = [
                column for name, _row, column in local if name in chosen_names
            ]
            if chosen:
                column_tensor, labels = temporal.apply_group_operator(
                    column_tensor,
                    labels,
                    chosen,
                    operators[len(chosen)],
                    prime,
                )
        factors.extend((
            (pairing, [row for _name, row, _column in local] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (column_tensor, labels),
        ))
        auxiliary += 2
    return disconnected_contract(factors, prime)


def labels_at_depth(sector, depth):
    labels = []
    for endpoint in block245.ENDPOINTS:
        actions, _word, _base = block245.history_data(endpoint, sector)
        choices = tuple(block245.subsets(actions))
        labels.extend(
            (sector, endpoint, tuple(sequence))
            for sequence in product(choices, repeat=depth)
        )
    return tuple(labels)


def gram(labels, prime, sample):
    matrix = np.zeros((len(labels), len(labels)), dtype=np.int64)
    for row, label_a in enumerate(labels):
        for column in range(row, len(labels)):
            value = contract_sequences(label_a, labels[column], prime, sample)
            matrix[row, column] = value
            matrix[column, row] = value
    return matrix


def loop_occurrences(loops_a, loops_b):
    occurrences = defaultdict(list)
    next_node = 0
    for name, loop in loops_a + loops_b:
        nodes = tuple(range(next_node, next_node + len(loop)))
        next_node += len(loop)
        for position, (link, direction) in enumerate(loop):
            first = nodes[position]
            second = nodes[(position + 1) % len(loop)]
            row, column = (first, second) if direction == 1 else (second, first)
            occurrences[link].append((name, row, column))
    return occurrences


def undressed_contract(loops_a, loops_b, prime):
    factors = []
    auxiliary = 900_000
    for local in loop_occurrences(loops_a, loops_b).values():
        if len(local) % 2:
            return 0
        _basis, pairing, inverse_gram = brauer.modular_moment_factors(
            len(local), prime
        )
        factors.extend((
            (pairing, [row for _name, row, _column in local] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (pairing, [column for _name, _row, column in local] + [auxiliary + 1]),
        ))
        auxiliary += 2
    return disconnected_contract(factors, prime)


def prefixed(loops, prefix):
    return [(f"{prefix}_{name}", loop) for name, loop in loops]


def physical_action_residual_certificate(prime, mutation=None):
    """Add one action character on active p0 and apply physical (I-Q).

    At fixed coarse delta0 the p0 holonomy is Haar, so
    Q[chi_V(p0)^2 chi_V(C1)] = chi_V(C1).  The residual is therefore the
    exact two-configuration combination below.  Its O(3) content is
    (1,+) plus (2,+), since (1,-) tensor (1,-) = (0,+)+(1,+)+(2,+).
    """
    old_states = []
    for index, sector in enumerate(block245.SECTORS):
        for endpoint in block245.ENDPOINTS:
            old_states.append([(
                1,
                block245.history_loops(endpoint, sector, f"old{index}{endpoint}"),
            )])
    p0 = block245.block244.plaquette(0)
    c1 = block245.block244.merged(3, 5)
    doubled = [("p0a", p0), ("p0b", p0), ("C1", c1)]
    coarse = [("C1", c1)]
    residual = [(1, doubled), (-1, coarse)]
    if mutation == "drop_physical_q_subtraction":
        residual = [(1, doubled)]
    states = old_states + [residual]
    matrix = np.zeros((len(states), len(states)), dtype=np.int64)
    for row, state_a in enumerate(states):
        for column in range(row, len(states)):
            value = 0
            for coefficient_a, loops_a in state_a:
                for coefficient_b, loops_b in states[column]:
                    value += coefficient_a * coefficient_b * undressed_contract(
                        prefixed(loops_a, "a"), prefixed(loops_b, "b"), prime
                    )
            matrix[row, column] = value % prime
            matrix[column, row] = value % prime
    return {
        "old_rank": block245.modular_rank(matrix[:-1, :-1], prime),
        "augmented_rank": block245.modular_rank(matrix, prime),
        "residual_norm": int(matrix[-1, -1]),
        "nonzero_old_crossings": int(np.count_nonzero(matrix[:-1, -1])),
    }


def dressed_config_contract(
    loops_a,
    selected_a,
    loops_b,
    selected_b,
    prime,
    sample,
):
    occurrences = loop_occurrences(loops_a, loops_b)
    if any(len(local) % 2 for local in occurrences.values()):
        return 0
    operators = {
        power: block245.temporal_operator(power, prime, sample)
        for power in range(1, 4)
    }
    factors = []
    auxiliary = 950_000
    for local in occurrences.values():
        _basis, pairing, inverse_gram = brauer.modular_moment_factors(
            len(local), prime
        )
        column_tensor = pairing
        labels = [column for _name, _row, column in local] + [auxiliary + 1]
        for chosen_names in (selected_a, selected_b):
            chosen = [
                column for name, _row, column in local if name in chosen_names
            ]
            if chosen:
                column_tensor, labels = temporal.apply_group_operator(
                    column_tensor,
                    labels,
                    chosen,
                    operators[len(chosen)],
                    prime,
                )
        factors.extend((
            (pairing, [row for _name, row, _column in local] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (column_tensor, labels),
        ))
        auxiliary += 2
    return disconnected_contract(factors, prime)


def crossed_action_residual_certificate(prime, sample, mutation=None):
    """Cross the exact action residual and augment the Block245 raw Gram."""
    labels, old_gram = block245.raw_gram_matrix(prime, sample)
    old_configs = []
    for sector, endpoint, half in labels:
        loops = block245.history_loops(endpoint, sector, "a")
        selected = block245.selected_names(endpoint, half, "a")
        old_configs.append((loops, selected))

    p0 = block245.block244.plaquette(0)
    c1 = block245.block244.merged(3, 5)
    doubled = [("b_p0a", p0), ("b_p0b", p0), ("b_C1", c1)]
    coarse = [("b_C1", c1)]
    residual_terms = (
        (1, doubled, {"b_p0a", "b_p0b", "b_C1"}),
        (-1, coarse, {"b_C1"}),
    )
    if mutation == "drop_physical_q_subtraction":
        residual_terms = residual_terms[:1]
    if mutation == "omit_baseline_temporal_crossing":
        residual_terms = tuple(
            (coefficient, loops, {name for name in selected if name != "b_C1"})
            for coefficient, loops, selected in residual_terms
        )

    cross = np.zeros(len(labels), dtype=np.int64)
    for index, (loops, selected) in enumerate(old_configs):
        value = 0
        for coefficient, residual_loops, residual_selected in residual_terms:
            value += coefficient * dressed_config_contract(
                loops,
                selected,
                residual_loops,
                residual_selected,
                prime,
                sample,
            )
        cross[index] = value % prime

    residual_norm = 0
    for coefficient_a, loops_a, selected_a in residual_terms:
        for coefficient_b, loops_b, selected_b in residual_terms:
            # The two residual copies need disjoint tensor labels.
            renamed_a = prefixed(loops_a, "left")
            renamed_b = prefixed(loops_b, "right")
            names_a = {f"left_{name}" for name in selected_a}
            names_b = {f"right_{name}" for name in selected_b}
            residual_norm += coefficient_a * coefficient_b * dressed_config_contract(
                renamed_a,
                names_a,
                renamed_b,
                names_b,
                prime,
                sample,
            )
    residual_norm %= prime

    augmented = np.zeros((len(labels) + 1, len(labels) + 1), dtype=np.int64)
    augmented[:-1, :-1] = old_gram
    augmented[:-1, -1] = cross
    augmented[-1, :-1] = cross
    augmented[-1, -1] = residual_norm
    return {
        "old_rank": block245.modular_rank(old_gram, prime),
        "augmented_rank": block245.modular_rank(augmented, prime),
        "residual_norm": int(residual_norm),
        "nonzero_old_crossings": int(np.count_nonzero(cross)),
    }


def scope_check(mutation=None):
    text = " ".join(NOTE.read_text().split())
    if mutation == "identify_sample_rank_as_generic_exact":
        text = text.replace(
            "It is not enough to prove that 72 is the exact generic rank",
            "This proves that 72 is the exact generic rank",
        )
    elif mutation == "identify_temporal_multiplicity_as_new_irreps":
        text = text.replace(
            "the rank-72 temporal witness alone establishes multiplicity growth only",
            "all rank-72 temporal growth consists of new Peter--Weyl sectors",
        )
    elif mutation == "claim_global_minimal_memory":
        text = text.replace(
            "a closed finite history carrier or globally minimal memory",
            "a closed finite history carrier and globally minimal memory",
        )
    elif mutation == "axiom_edit":
        text = text.replace(
            "No axiom or approved primitive is edited",
            "One approved primitive is edited",
        )
    required = (
        "It is not enough to prove that 72 is the exact generic rank",
        "the rank-72 temporal witness alone establishes multiplicity growth only",
        "a closed finite history carrier or globally minimal memory",
        "No axiom or approved primitive is edited",
    )
    return all(phrase in text for phrase in required)


def mutation_detected(mutation):
    if mutation == "drop_physical_q_subtraction":
        result = physical_action_residual_certificate(PRIME, mutation)
        return result["residual_norm"] != 2 or result["nonzero_old_crossings"] != 0
    if mutation == "omit_baseline_temporal_crossing":
        hostile = {0: F(1, 5), 1: F(0), 2: F(2, 5), 3: F(1, 2)}
        result = crossed_action_residual_certificate(PRIME, hostile, mutation)
        return result["residual_norm"] != 0 or result["augmented_rank"] != 0
    if mutation == "collapse_second_crossing":
        total = 0
        for sector in block245.SECTORS:
            single = labels_at_depth(sector, 1)
            collapsed = single + single
            total += block245.modular_rank(gram(collapsed, PRIME, SAMPLE), PRIME)
        return total != 72
    return not scope_check(mutation)


def temporal_rank_certificate(prime, sample, controls=False):
    totals = [0, 0, 0]
    sector_rows = []
    repeated_residuals = []
    reversal_residuals = []
    for sector in block245.SECTORS:
        single = labels_at_depth(sector, 1)
        double = labels_at_depth(sector, 2)
        union = single + double
        matrix = gram(union, prime, sample)
        split = len(single)
        single_matrix = matrix[:split, :split]
        double_matrix = matrix[split:, split:]
        ranks = (
            block245.modular_rank(single_matrix, prime),
            block245.modular_rank(double_matrix, prime),
            block245.modular_rank(matrix, prime),
        )
        totals = [left + right for left, right in zip(totals, ranks)]
        sector_rows.append((tuple(sorted(sector)), *ranks))
        if controls:
            double_lookup = {label: index for index, label in enumerate(double)}
            reversal_residuals.append(max(
                int(np.any((
                    matrix[split + index] - matrix[
                        split + double_lookup[(label[0], label[1], tuple(reversed(label[2])))]
                    ]
                ) % prime))
                for index, label in enumerate(double)
            ))
            repeated = [
                index for index, label in enumerate(double)
                if label[2][0] == label[2][1]
            ]
            repeated_matrix = double_matrix[np.ix_(repeated, repeated)]
            squared_sample = {
                power: value * value for power, value in sample.items()
            }
            squared_parent = gram(single, prime, squared_sample)
            repeated_residuals.append(
                int(np.any((repeated_matrix - squared_parent) % prime))
            )
    return {
        "sector_rows": sector_rows,
        "old_rank": totals[0],
        "twice_crossed_rank": totals[1],
        "union_rank": totals[2],
        "leakage_rank": totals[2] - totals[0],
        "repeated_half_residuals": repeated_residuals,
        "reversal_residuals": reversal_residuals,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        detected = 0
        for mutation in MUTATIONS:
            caught = mutation_detected(mutation)
            detected += int(caught)
            print("mutation", mutation, "detected", caught, flush=True)
        print("mutation_suite", f"{detected}/{len(MUTATIONS)}", flush=True)
        return 0 if detected == len(MUTATIONS) else 1
    if args.mutation:
        caught = mutation_detected(args.mutation)
        print("mutation", args.mutation, "detected", caught)
        return 0 if caught else 1

    checks = []
    def check(label, condition):
        checks.append((label, bool(condition)))
        print("[PASS]" if condition else "[FAIL]", label, flush=True)

    expected_rows = [
        ((0,), 5, 11, 15),
        ((1,), 5, 10, 14),
        ((2,), 6, 13, 17),
        ((0, 1), 4, 6, 8),
        ((0, 2), 4, 6, 8),
        ((1, 2), 5, 8, 10),
    ]
    for name, prime, sample, controls in (
        ("disclosed", 1009, SAMPLE, True),
        ("disclosed", 1013, SAMPLE, False),
        ("disclosed", 1019, SAMPLE, False),
        ("signed", 1009, SIGNED_SAMPLE, False),
        ("signed", 1013, SIGNED_SAMPLE, False),
        ("signed", 1019, SIGNED_SAMPLE, False),
        ("heldout", 10007, SIGNED_SAMPLE, False),
        ("identity", 1009, IDENTITY_SAMPLE, False),
    ):
        result = temporal_rank_certificate(prime, sample, controls)
        print("temporal", name, prime, result, flush=True)
        expected = (12, 12, 12) if name == "identity" else (29, 54, 72)
        check(f"{name} F_{prime}: exact temporal rank triple", (
            result["old_rank"], result["twice_crossed_rank"], result["union_rank"]
        ) == expected)
        if name == "disclosed":
            check(f"{name} F_{prime}: exact sector rank table",
                  result["sector_rows"] == expected_rows)
        if controls:
            check("same-half repetition equals squared multipliers",
                  result["repeated_half_residuals"] == [0] * 6)
            check("two central selections reverse with zero Gram residual",
                  result["reversal_residuals"] == [0] * 6)
    for prime in block245.PRIMES:
        physical = physical_action_residual_certificate(prime)
        crossed = crossed_action_residual_certificate(prime, SAMPLE)
        signed = crossed_action_residual_certificate(prime, SIGNED_SAMPLE)
        identity = crossed_action_residual_certificate(prime, IDENTITY_SAMPLE)
        t_zero = crossed_action_residual_certificate(prime, T_ZERO_SAMPLE)
        print("physical_action_residual", prime, physical, flush=True)
        print("crossed_action_residual", prime, crossed, signed, identity, t_zero,
              flush=True)
        check(f"F_{prime}: physical Q removes scalar action component",
              physical == {"old_rank": 12, "augmented_rank": 13,
                           "residual_norm": 2, "nonzero_old_crossings": 0})
        check(f"F_{prime}: crossed action residual is new at disclosed sample",
              crossed["old_rank"] == 29 and crossed["augmented_rank"] == 30
              and crossed["nonzero_old_crossings"] == 0)
        check(f"F_{prime}: crossed action residual is new at signed sample",
              signed["old_rank"] == 29 and signed["augmented_rank"] == 30
              and signed["nonzero_old_crossings"] == 0)
        check(f"F_{prime}: identity action endpoint has norm two and rank 13",
              identity["old_rank"] == 12 and identity["augmented_rank"] == 13
              and identity["residual_norm"] == 2)
        check(f"F_{prime}: t=0 hostile endpoint vanishes",
              t_zero["old_rank"] == 0 and t_zero["augmented_rank"] == 0
              and t_zero["residual_norm"] == 0)
    check("bounded theorem scope", scope_check())
    check("independent representation-ring and six conditional-Haar reductions",
          independent.all_checks_pass())
    print("per_element: checked and executed — every old and twice-crossed finite original-link history enters the exact Gram rank witness")
    print("per_site: checked and not executed — this finite loop-character carrier constructs no physical lattice-site evolution law")
    print("per_mode: checked and not executed — no continuum or lattice momentum-mode non-invariance statement is made")
    print("per_block: checked and executed — all six proper action-sector Gram blocks are evaluated independently and summed")
    print("lattice_wide: checked and not executed — the result does not claim a lattice-wide dynamics, transfer closure, or memory theorem")
    passed = sum(int(condition) for _label, condition in checks)
    print("TOTAL", f"PASS={passed}", f"FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
