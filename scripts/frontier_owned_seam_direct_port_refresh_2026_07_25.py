#!/usr/bin/env python3
"""Owned-seam audit and constructive refresh for the Route-B common code.

The first control is intentionally prior to any seam synthesis: it replays the
22-port extractor on the *full* two-star n<=2 branch domain and asks whether a
single fixed owner seam needs any of the sixteen global conflict signatures.
No Gram whitener and no global one-hot selector is constructed here.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product

import frontier_two_overlapping_maximal_star_direct_port_extractor_2026_07_25 as direct
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


def edge_key(edge: direct.Edge) -> tuple[int, int, int, int]:
    return edge.first_cell, edge.first_mode, edge.second_cell, edge.second_mode


def full_domain_owned_seam_scan(length: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    cells = direct.body_cells(length)
    incidence_data = tuple(
        direct.physical_edge_data(code, cells, edge)
        for edge in direct.SOURCE_INCIDENCE_EDGES
    )
    incidence_lookup = {
        frozenset((edge.first_cell, edge.second_cell)): index
        for index, edge in enumerate(direct.SOURCE_INCIDENCE_EDGES)
    }
    owner_to_incidence = tuple(
        incidence_lookup[frozenset((edge.first_cell, edge.second_cell))]
        for edge in direct.SOURCE_EDGES
    )
    cache = {
        (cell, number, label): direct.transformed_local_terms(
            code, cell, cells[cell], number, label
        )
        for cell in range(12)
        for number, label in c311.FOCK_LABELS
        if number <= 2
    }

    # A global physical port word may occur in more than one factor history.
    # Retain both the correct owned-edge datum and the datum returned by that
    # edge's 22-port formula.  This is the exact place where a hidden use of a
    # global one-hot selector would show up.
    truth_by_word = [defaultdict(set) for _edge in direct.SOURCE_EDGES]
    derived_by_word = [defaultdict(set) for _edge in direct.SOURCE_EDGES]
    global_feature_by_word: dict[int, set[int]] = defaultdict(set)
    cases = 0
    first_mismatch = None
    mismatches_by_owner = [0] * len(direct.SOURCE_EDGES)
    multiple_active_candidates = 0

    for label in direct.LABELS:
        active = direct.active_local_cells(label)
        local_rows = [cache[(cell, *direct.local_spec(label, cell))] for cell in active]
        for terms in product(*local_rows) if local_rows else ((),):
            representative = direct.c330.c235.Pauli()
            for term in terms:
                representative = representative @ term.representative
            port_word = (
                representative.x >> code.qubits
            ) & ((1 << len(code.graph.vertices)) - 1)

            truth_incidence = [0] * len(direct.SOURCE_INCIDENCE_EDGES)
            feature_code = 0
            if len(terms) == 2:
                incidence = incidence_lookup.get(frozenset(active))
                if incidence is not None:
                    edge = direct.SOURCE_INCIDENCE_EDGES[incidence]
                    by_cell = dict(zip(active, terms))
                    feature = direct.expected_edge_feature(
                        code,
                        by_cell[edge.first_cell].representative,
                        by_cell[edge.second_cell].representative,
                        incidence_data[incidence],
                    )
                    truth_incidence[incidence] = feature
                    if feature:
                        feature_code = 1 + 2 * incidence + feature - 1
            global_feature_by_word[port_word].add(feature_code)

            candidates = tuple(
                direct.edge_feature_from_ports(code, representative, data)
                for data in incidence_data
            )
            multiple_active_candidates += sum(value != 0 for value in candidates) > 1
            for owner, incidence in enumerate(owner_to_incidence):
                truth = truth_incidence[incidence]
                derived = candidates[incidence]
                truth_by_word[owner][port_word].add(truth)
                derived_by_word[owner][port_word].add(derived)
                if truth != derived:
                    mismatches_by_owner[owner] += 1
                    if first_mismatch is None:
                        edge = direct.SOURCE_EDGES[owner]
                        first_mismatch = {
                            "label": label,
                            "active_cells": active,
                            "owner_edge": owner,
                            "owner_edge_data": edge_key(edge),
                            "truth": truth,
                            "derived": derived,
                            "global_feature_code": feature_code,
                            "port_word": port_word,
                            "active_candidate_edges": tuple(
                                index for index, value in enumerate(candidates) if value
                            ),
                        }
            cases += 1

    conflict_words = {
        word: tuple(sorted(features))
        for word, features in global_feature_by_word.items()
        if len(features) > 1
    }
    owner_truth_ambiguities = [
        sum(len(values) > 1 for values in table.values()) for table in truth_by_word
    ]
    owner_formula_ambiguities = [
        sum(len(values) > 1 for values in table.values()) for table in derived_by_word
    ]
    conflicts_needed = []
    for word, feature_set in conflict_words.items():
        owners = tuple(
            owner
            for owner in range(len(direct.SOURCE_EDGES))
            if len(truth_by_word[owner][word]) > 1
            or any(
                truth != derived
                for truth in truth_by_word[owner][word]
                for derived in derived_by_word[owner][word]
            )
        )
        if owners:
            conflicts_needed.append((word, feature_set, owners))
    first_needed = None
    if conflicts_needed:
        word, feature_set, owners = conflicts_needed[0]
        first_needed = {
            "port_word_sha256": sha256(str(word).encode("ascii")).hexdigest(),
            "feature_class": feature_set,
            "owners": owners,
        }
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "branch_history_cases": cases,
        "full_union_conflict_signatures": len(conflict_words),
        "full_union_conflict_classes": dict(
            Counter(tuple(features) for features in conflict_words.values())
        ),
        "multiple_active_candidate_histories": multiple_active_candidates,
        "owned_seams": len(direct.SOURCE_EDGES),
        "owner_formula_mismatches": tuple(mismatches_by_owner),
        "owner_truth_ambiguities_by_port_word": tuple(owner_truth_ambiguities),
        "owner_formula_ambiguities_by_port_word": tuple(owner_formula_ambiguities),
        "conflict_signatures_needed_by_one_owned_seam": len(conflicts_needed),
        "first_needed_conflict": first_needed,
        "first_formula_mismatch": first_mismatch,
        "whitener_used": False,
        "global_selector_used": False,
        "seam_map_constructed": False,
        "route_specific_failure_only": True,
        "shared_obstruction_claimed": False,
    }


def main() -> None:
    rows = tuple(full_domain_owned_seam_scan(length) for length in (5, 6))
    print("OWNED_SEAM_FULL_DOMAIN_DIRECT_PORT_GATE")
    for row in rows:
        print("scan", row)
    assert all(
        row["full_union_conflict_signatures"] == 16
        and row["conflict_signatures_needed_by_one_owned_seam"] == 16
        and tuple(row["owner_formula_mismatches"])
        == (20000, 0, 4000, 4000, 4000, 4000, 0, 4000, 4000, 4000, 4000)
        and tuple(row["owner_truth_ambiguities_by_port_word"])
        == (8, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2)
        and not any(row["owner_formula_ambiguities_by_port_word"])
        and row["first_formula_mismatch"]["label"] == (0, 18)
        and row["first_formula_mismatch"]["truth"] == 0
        and row["first_formula_mismatch"]["derived"] == 1
        and not row["whitener_used"]
        and not row["global_selector_used"]
        and not row["seam_map_constructed"]
        and row["route_specific_failure_only"]
        and not row["shared_obstruction_claimed"]
        for row in rows
    )
    assert {
        key: value
        for key, value in rows[0].items()
        if key
        not in {
            "L",
            "split",
            "first_needed_conflict",
            "first_formula_mismatch",
        }
    } == {
        key: value
        for key, value in rows[1].items()
        if key
        not in {
            "L",
            "split",
            "first_needed_conflict",
            "first_formula_mismatch",
        }
    }
    print("DIRECT_22_PORT_SAME_E_SEAM_GATE_FAILED_ROUTE_SPECIFIC")


if __name__ == "__main__":
    main()
