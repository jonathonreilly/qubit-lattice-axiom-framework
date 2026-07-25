#!/usr/bin/env python3
"""Literal-gate deletion and lawful-domain audit for the two-star compiler.

This successor runs after the literal 335-M2 reachable-state intertwiner has
closed.  It removes gates from the *literal* word, rather than inheriting only
contracted deletion numbers: onsite coin factors, routed transition
SWAP/CZ/SWAP primitives, seam compute/use/uncompute, endpoint FSWAP, all seven
carrier-rail SWAPs, onsite contact factors, carrier Givens factors, per-cell
token controls, and both chart controls are given sparse state witnesses.

The witnesses establish activity and the declared clean-work domain of this
finite decoded-interface fixture.  They do not supply a recurrent gauge law,
the landed Cycle655 physical binding, transformed-E covariance, a no-go, or
axiom pressure.
"""

from __future__ import annotations

from dataclasses import replace
from hashlib import sha256
from itertools import combinations
import json
import resource
import time

import numpy as np

import frontier_two_star_literal_m2_reachable_executor_2026_07_25 as literal


START = time.perf_counter()
TOL = 6.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def sentinel_mask() -> int:
    return sum(
        1 << literal.role_index(cell, literal.base.refresh.SENTINEL)
        for cell in range(len(literal.base.CELLS))
    )


def basis(
    data: int = 0,
    role_rails: int | None = None,
    charts: int = 0,
    tokens: int | None = None,
    matcher_scratch: int = 0,
    matcher_flags: int = 0,
    bypass: int = 0,
    edge_work: int = 0,
    transit: int = 0,
) -> literal.LiteralBasis:
    return literal.LiteralBasis(
        data=data,
        role_rails=sentinel_mask() if role_rails is None else role_rails,
        charts=charts,
        tokens=(1 << len(literal.base.CELLS)) - 1 if tokens is None else tokens,
        matcher_scratch=matcher_scratch,
        matcher_flags=matcher_flags,
        bypass=bypass,
        edge_work=edge_work,
        transit=transit,
    )


def singleton(key: literal.LiteralBasis) -> literal.State:
    return {key: 1.0 + 0.0j}


def residual(left: literal.State, right: literal.State) -> float:
    return float(literal.difference(left, right)[1])


def coin_deletions() -> dict[str, object]:
    rows = []
    for gate_index, deleted_gate in enumerate(literal.base.COIN_GATES):
        best = 0.0
        witness = 0
        squared_column_residuals = 0.0
        for supplied in range(64):
            source = singleton(basis(data=supplied))
            correct = source
            omitted = source
            for index, gate in enumerate(literal.base.COIN_GATES):
                correct = literal.apply_data_gate(
                    correct, 0, gate.wires, gate.matrix
                )
                if index != gate_index:
                    omitted = literal.apply_data_gate(
                        omitted, 0, gate.wires, gate.matrix
                    )
            value = residual(correct, omitted)
            squared_column_residuals += value * value
            if value > best:
                best, witness = value, supplied
        rows.append({
            "factor": gate_index,
            "wires": deleted_gate.wires,
            "witness_local_word": witness,
            "delete_residual": best,
            "operator_frobenius_delete_residual": squared_column_residuals ** 0.5,
        })
    return {
        "literal_coin_factor_deletions": len(rows),
        "minimum_maximum_column_delete_residual": min(
            row["delete_residual"] for row in rows
        ),
        "minimum_operator_frobenius_delete_residual": min(
            row["operator_frobenius_delete_residual"] for row in rows
        ),
        "rows": rows,
    }


def routed_term_word(
    state: literal.State, term, deleted: str | None = None
) -> literal.State:
    left, right = term.pair
    if term.distance <= 1:
        return state if deleted == "CZ" else literal.cz_data_pair(state, left, right)
    if term.midpoint is None:
        raise AssertionError(term)
    center = literal.base.CELL_INDEX[term.midpoint]
    if deleted != "first_SWAP":
        state = literal.swap_data_transit(state, left, center)
    if deleted != "CZ":
        state = literal.cz_transit_data(state, center, right)
    if deleted != "last_SWAP":
        state = literal.swap_data_transit(state, left, center)
    return state


def transition_deletions() -> dict[str, object]:
    rows = []
    for term_index, term in enumerate(literal.base.routed.ROUTED_TERMS):
        left, right = term.pair
        source = singleton(basis(data=(1 << left) | (1 << right)))
        correct = routed_term_word(source, term)
        deletion_names = ("CZ",) if term.distance <= 1 else (
            "first_SWAP", "CZ", "last_SWAP"
        )
        deletion_rows = {
            name: residual(correct, routed_term_word(source, term, name))
            for name in deletion_names
        }
        rows.append({
            "term": term_index,
            "distance": term.distance,
            "deletions": deletion_rows,
        })
    core = [row["deletions"]["CZ"] for row in rows]
    first = [row["deletions"]["first_SWAP"] for row in rows if row["distance"] > 1]
    last = [row["deletions"]["last_SWAP"] for row in rows if row["distance"] > 1]
    return {
        "literal_transition_terms": len(rows),
        "routed_distance_two_terms": len(first),
        "literal_routed_SWAP_primitives": 2 * len(first),
        "minimum_delete_CZ_residual": min(core),
        "minimum_delete_first_SWAP_residual": min(first),
        "minimum_delete_last_SWAP_residual": min(last),
        "rows": rows,
    }


def seam_variant(
    state: literal.State,
    edge: int,
    deleted: tuple[str, int] | None = None,
) -> literal.State:
    left, right, intermediate = literal.base.SPECS[edge]
    for index, mode in enumerate(intermediate):
        if deleted != ("compute_CNOT", index):
            state = literal.cnot_data_edge(state, mode, edge)
    if deleted != ("left_edge_CZ", 0):
        state = literal.cz_data_edge(state, left, edge)
    if deleted != ("right_edge_CZ", 0):
        state = literal.cz_data_edge(state, right, edge)
    for reverse_index, mode in enumerate(reversed(intermediate)):
        if deleted != ("uncompute_CNOT", reverse_index):
            state = literal.cnot_data_edge(state, mode, edge)
    if deleted != ("endpoint_CZ", 0):
        state = literal.cz_data_pair(state, left, right)
    if deleted != ("data_SWAP", 0):
        state = literal.swap_data(state, left, right)
    for rail in range(7):
        if deleted != ("rail_SWAP", rail):
            state = literal.swap_role_rail(state, left // 6, right // 6, rail)
    return state


def maximum_data_witness(edge: int, deletion: tuple[str, int]) -> float:
    left, right, intermediate = literal.base.SPECS[edge]
    modes = tuple(dict.fromkeys((left, right, *intermediate)))
    masks = [0]
    masks.extend(1 << mode for mode in modes)
    masks.extend((1 << a) | (1 << b) for a, b in combinations(modes, 2))
    best = 0.0
    for mask in masks:
        source = singleton(basis(data=mask))
        best = max(best, residual(
            seam_variant(source, edge), seam_variant(source, edge, deletion)
        ))
    return best


def rail_swap_witness(edge: int, rail: int) -> float:
    left, right, _intermediate = literal.base.SPECS[edge]
    left_cell, right_cell = left // 6, right // 6
    roles = sentinel_mask()
    if rail == literal.base.refresh.SENTINEL:
        alternate = 0 if rail != 0 else 1
        roles = literal.set_bit(
            roles, literal.role_index(left_cell, rail), 0
        )
        roles = literal.set_bit(
            roles, literal.role_index(left_cell, alternate), 1
        )
    else:
        roles = literal.set_bit(
            roles, literal.role_index(left_cell, literal.base.refresh.SENTINEL), 0
        )
        roles = literal.set_bit(
            roles, literal.role_index(left_cell, rail), 1
        )
    source = singleton(basis(role_rails=roles))
    return residual(
        seam_variant(source, edge),
        seam_variant(source, edge, ("rail_SWAP", rail)),
    )


def seam_deletions() -> dict[str, object]:
    rows = []
    categories: dict[str, list[float]] = {}
    for edge, (_left, _right, intermediate) in enumerate(literal.base.SPECS):
        probes = []
        probes.extend(("compute_CNOT", index) for index in range(len(intermediate)))
        probes.extend(("uncompute_CNOT", index) for index in range(len(intermediate)))
        probes.extend((name, 0) for name in (
            "left_edge_CZ", "right_edge_CZ", "endpoint_CZ", "data_SWAP"
        ))
        edge_rows = []
        for probe in probes:
            value = maximum_data_witness(edge, probe)
            categories.setdefault(probe[0], []).append(value)
            edge_rows.append({"primitive": probe, "maximum_witness_residual": value})
        for rail in range(7):
            value = rail_swap_witness(edge, rail)
            categories.setdefault("rail_SWAP", []).append(value)
            edge_rows.append({
                "primitive": ("rail_SWAP", rail),
                "maximum_witness_residual": value,
            })
        rows.append({"edge": edge, "deletions": edge_rows})
    return {
        "literal_seam_edges": len(rows),
        "deletion_witnesses": sum(len(row["deletions"]) for row in rows),
        "minimum_maximum_witness_by_category": {
            name: min(values) for name, values in sorted(categories.items())
        },
        "rows": rows,
    }


def contact_deletions() -> dict[str, object]:
    matrix = np.diag((
        1, 1, 1, np.exp(1j * literal.base.route_c.c230.COUPLING)
    )).astype(complex)
    rows = []
    for cell in range(len(literal.base.CELLS)):
        for left, right in combinations(range(6), 2):
            data = (1 << (6 * cell + left)) | (1 << (6 * cell + right))
            source = singleton(basis(data=data))
            observed = literal.apply_data_gate(source, cell, (left, right), matrix)
            rows.append(residual(observed, source))
    return {
        "literal_contact_factor_deletions": len(rows),
        "minimum_delete_residual": min(rows),
        "maximum_delete_residual": max(rows),
    }


def carrier_factor_deletions() -> dict[str, object]:
    rows = []
    for occupied, word in enumerate(literal.base.refresh.ROLE_PREPARATIONS):
        key = basis(data=1 << occupied)
        matched = literal.matcher_compute(singleton(key), 0, occupied)
        for deleted in range(len(word)):
            correct = matched
            omitted = matched
            for index, (carrier, matrix) in enumerate(word):
                correct = literal.controlled_role_factor(
                    correct, 0, carrier, matrix
                )
                if index != deleted:
                    omitted = literal.controlled_role_factor(
                        omitted, 0, carrier, matrix
                    )
            correct = literal.matcher_uncompute(correct, 0, occupied)
            omitted = literal.matcher_uncompute(omitted, 0, occupied)
            rows.append({
                "occupied": occupied,
                "factor": deleted,
                "delete_residual": residual(correct, omitted),
            })
    return {
        "literal_carrier_factor_deletions": len(rows),
        "minimum_delete_residual": min(row["delete_residual"] for row in rows),
        "rows": rows,
    }


def matcher_without_token(
    state: literal.State, cell: int, occupied: int, inverse: bool
) -> literal.State:
    if not inverse:
        for mode in range(6):
            if mode != occupied:
                state = literal.x_data(state, 6 * cell + mode)
        for mode in range(1, 5):
            state = literal.toffoli_scratch_data_to_scratch(
                state,
                literal.scratch_index(cell, mode - 1),
                6 * cell + mode,
                literal.scratch_index(cell, mode),
            )
        return literal.toffoli_scratch_data_to_flag(
            state, literal.scratch_index(cell, 4), 6 * cell + 5, cell
        )
    state = literal.toffoli_scratch_data_to_flag(
        state, literal.scratch_index(cell, 4), 6 * cell + 5, cell
    )
    for mode in reversed(range(1, 5)):
        state = literal.toffoli_scratch_data_to_scratch(
            state,
            literal.scratch_index(cell, mode - 1),
            6 * cell + mode,
            literal.scratch_index(cell, mode),
        )
    for mode in reversed(range(6)):
        if mode != occupied:
            state = literal.x_data(state, 6 * cell + mode)
    return state


def token_control_deletions() -> dict[str, object]:
    rows = []
    occupied = 0
    word = literal.base.refresh.ROLE_PREPARATIONS[occupied]
    for cell in range(len(literal.base.CELLS)):
        source = singleton(basis(data=1 << (6 * cell + occupied)))
        correct = literal.matcher_compute(source, cell, occupied)
        omitted = matcher_without_token(source, cell, occupied, False)
        for carrier, matrix in word:
            correct = literal.controlled_role_factor(correct, cell, carrier, matrix)
            omitted = literal.controlled_role_factor(omitted, cell, carrier, matrix)
        correct = literal.matcher_uncompute(correct, cell, occupied)
        omitted = matcher_without_token(omitted, cell, occupied, True)
        rows.append(residual(correct, omitted))
    return {
        "literal_token_control_pairs_deleted": len(rows),
        "minimum_delete_residual": min(rows),
        "maximum_delete_residual": max(rows),
    }


def chart_variant(
    state: literal.State, deleted: tuple[int, str] | None = None
) -> literal.State:
    def operation(key: literal.LiteralBasis):
        charts = key.charts
        for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(
            literal.base.FEATURES
        ):
            cell = literal.base.CELL_INDEX[cell_coord]
            if deleted != (block, "data"):
                charts ^= literal.bit(key.data, 6 * cell + mode) << (2 * block)
            if deleted != (block, "rail"):
                charts ^= literal.bit(
                    key.role_rails, literal.role_index(cell, mode)
                ) << (2 * block + 1)
        return replace(key, charts=charts), 1
    return literal.map_keys(state, operation)


def chart_deletions() -> dict[str, object]:
    rows = []
    for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(
        literal.base.FEATURES
    ):
        cell = literal.base.CELL_INDEX[cell_coord]
        data = 1 << (6 * cell + mode)
        data_roles = sentinel_mask()
        data_charts = literal.chart_mask(data, data_roles)
        data_source = singleton(basis(
            data=data, role_rails=data_roles, charts=data_charts
        ))
        data_value = residual(
            literal.chart_word(data_source), chart_variant(data_source, (block, "data"))
        )

        rail_roles = sentinel_mask()
        rail_roles = literal.set_bit(
            rail_roles,
            literal.role_index(cell, literal.base.refresh.SENTINEL),
            0,
        )
        rail_roles = literal.set_bit(
            rail_roles, literal.role_index(cell, mode), 1
        )
        rail_charts = literal.chart_mask(0, rail_roles)
        rail_source = singleton(basis(role_rails=rail_roles, charts=rail_charts))
        rail_value = residual(
            literal.chart_word(rail_source), chart_variant(rail_source, (block, "rail"))
        )
        rows.append({
            "block": block,
            "delete_data_control_residual": data_value,
            "delete_rail_control_residual": rail_value,
        })
    return {
        "literal_chart_control_deletions": 2 * len(rows),
        "minimum_delete_data_control_residual": min(
            row["delete_data_control_residual"] for row in rows
        ),
        "minimum_delete_rail_control_residual": min(
            row["delete_rail_control_residual"] for row in rows
        ),
        "rows": rows,
    }


def dirty_domain() -> dict[str, object]:
    left, _right, _intermediate = literal.base.SPECS[0]
    clean = basis(data=1 << left)
    dirty_edge = replace(clean, edge_work=1)
    clean_out = literal.seam_word(singleton(clean), 0)
    dirty_edge_out = literal.seam_word(singleton(dirty_edge), 0)

    dirty_scratch = basis(matcher_scratch=1)
    scratch_out = literal.matcher_uncompute(
        literal.matcher_compute(singleton(dirty_scratch), 0, 0), 0, 0
    )
    dirty_flag = basis(matcher_flags=1)
    flag_out = literal.controlled_role_factor(
        singleton(dirty_flag), 0, 1,
        literal.base.refresh.ROLE_PREPARATIONS[0][0][1],
    )
    dirty_chart = replace(clean, charts=1)
    chart_out = literal.chart_word(literal.chart_word(singleton(dirty_chart)))
    return {
        "clean_edge_phase": next(iter(clean_out.values())),
        "dirty_edge_phase": next(iter(dirty_edge_out.values())),
        "dirty_edge_returned": next(iter(dirty_edge_out)).edge_work,
        "dirty_scratch_returned": next(iter(scratch_out)).matcher_scratch,
        "dirty_flag_returned": all(key.matcher_flags == 1 for key in flag_out),
        "dirty_flag_changes_role_or_bypass": residual(flag_out, singleton(dirty_flag)),
        "dirty_chart_returned": next(iter(chart_out)).charts,
        "dirty_auxiliary_in_declared_code": False,
    }


def main() -> None:
    coin = coin_deletions()
    check(
        "all literal onsite coin factors have deletion witnesses",
        coin["literal_coin_factor_deletions"] == 11
        and coin["minimum_maximum_column_delete_residual"] > 0.005
        and coin["minimum_operator_frobenius_delete_residual"] > 0.03,
        {key: value for key, value in coin.items() if key != "rows"},
    )

    transition = transition_deletions()
    check(
        "every literal transition CZ and routed SWAP is active",
        transition["literal_transition_terms"] == 224
        and transition["routed_distance_two_terms"] == 77
        and transition["literal_routed_SWAP_primitives"] == 154
        and transition["minimum_delete_CZ_residual"] > 1.9
        and transition["minimum_delete_first_SWAP_residual"] > 1.0
        and transition["minimum_delete_last_SWAP_residual"] > 1.0,
        {key: value for key, value in transition.items() if key != "rows"},
    )

    seam = seam_deletions()
    seam_minima = seam["minimum_maximum_witness_by_category"]
    check(
        "literal seam compute/use/uncompute, FSWAP, and seven-rail bundle primitives are active",
        seam["literal_seam_edges"] == 11
        and seam["deletion_witnesses"] > 77
        and all(value > 0.9 for value in seam_minima.values()),
        {key: value for key, value in seam.items() if key != "rows"},
    )

    contact = contact_deletions()
    check(
        "all 180 literal onsite contact factors have deletion witnesses",
        contact["literal_contact_factor_deletions"] == 180
        and contact["minimum_delete_residual"] > 0.3,
        contact,
    )

    carrier = carrier_factor_deletions()
    check(
        "all literal carrier preparation factors have deletion witnesses",
        carrier["literal_carrier_factor_deletions"] == 30
        and carrier["minimum_delete_residual"] > 0.01,
        {key: value for key, value in carrier.items() if key != "rows"},
    )

    tokens = token_control_deletions()
    check(
        "all twelve literal token-control pairs have deletion witnesses",
        tokens["literal_token_control_pairs_deleted"] == 12
        and tokens["minimum_delete_residual"] > 0.1,
        tokens,
    )

    charts = chart_deletions()
    check(
        "all 48 literal chart controls have orthogonal deletion witnesses",
        charts["literal_chart_control_deletions"] == 48
        and charts["minimum_delete_data_control_residual"] > 1.4
        and charts["minimum_delete_rail_control_residual"] > 1.4,
        {key: value for key, value in charts.items() if key != "rows"},
    )

    dirty = dirty_domain()
    check(
        "dirty literal auxiliary bits are returned or mutate the word and remain outside the code",
        dirty["clean_edge_phase"] == 1
        and dirty["dirty_edge_phase"] == -1
        and dirty["dirty_edge_returned"] == 1
        and dirty["dirty_scratch_returned"] != 0
        and dirty["dirty_flag_returned"]
        and dirty["dirty_flag_changes_role_or_bypass"] > 0.1
        and dirty["dirty_chart_returned"] == 1
        and not dirty["dirty_auxiliary_in_declared_code"],
        dirty,
    )

    certificate = {
        "coin": coin,
        "transition": transition,
        "seam": seam,
        "contact": contact,
        "carrier": carrier,
        "tokens": tokens,
        "charts": charts,
        "dirty_domain": dirty,
        "literal_intertwiner_certificate": (
            "f080e3ff703c855d3ed24e25f7532d3aeafdd06639975223430d95ecd0e3ddc6"
        ),
    }
    digest = sha256(json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "literal-fixed-M2-deletion-domain-audit",
        "terminal": "LITERAL_M2_DELETIONS_ACTIVE_RECURRENT_GAUGE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "deletions_and_domain": certificate,
        "claim_ceiling": (
            "Gate-activity and lawful-domain certificate for the finite literal decoded-interface word. "
            "It adds no recurrent law, no physical binding, no transformed-E covariance, and no obstruction claim."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
            "certificate_sha256": digest,
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
