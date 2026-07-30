#!/usr/bin/env python3
"""Cycle 785 independent adversarial check of the origin census.

The Cycle-785 primary is blocklisted as executable evidence: it is read only
as text and parsed as AST.  Catalog construction, the four-origin full
recount, the all-origin light trace, and both classification readings are
implemented here without calling any Cycle-785 function.
"""

from __future__ import annotations

import ast
from dataclasses import fields
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle769_formation_census_2026_07_28.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
PINNED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "249a9f84eb3a89b2a261801e8e2bb15cc0ba1919a61ac6a8e4c731b3ecaedb32",
    AUDIT_INPUT_PATHS[3]:
        "d5403ebbf51d8ecfaf621d5e0983d333b8df9a7d589145095b598c530ac15ab4",
}
PRIMARY_TEXT_ONLY_PATH = (
    "scripts/frontier_cycle785_multiorigin_census_2026_07_28.py"
)
PRIMARY_MODULE = "frontier_cycle785_multiorigin_census_2026_07_28"
SAMPLED_ORIGINS = (0, 5, 6, 11)
MATTER_MODE_COUNT = 12
MATTER_MASK = (1 << MATTER_MODE_COUNT) - 1

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle769_formation_census_2026_07_28 as C769
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def canonical_bytes(value: object) -> bytes:
    return compact(value).encode()


def canonical_digest(value: object) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def decoded_cell_surface(data_basis: int) -> dict[str, object]:
    """Independently read the landed EventChain surface."""
    banks, links = C719.M.unpack_state(
        C719.int_to_tuple(data_basis), C719.BANKS
    )
    try:
        chain, order = C719.B.decode_local_graph(banks, links)
    except ValueError as error:
        return {
            "acceptance_readable": False,
            "cell_rows": [],
            "decode_order": [],
            "decode_refusal": str(error),
        }
    return {
        "acceptance_readable": True,
        "cell_rows": C719.B.cell_rows(chain),
        "decode_order": order,
        "decode_refusal": None,
    }


def initial_branches(origin: int) -> tuple[int, ...]:
    """Apply MATTER_WORD directly; do not use Cycle-719's catalog helper."""
    banks, links = C719.B.chain_genesis(C719.BANKS)
    packed = C719.tuple_to_int(
        C719.M.pack_state(banks, links, matter=1 << origin)
    )
    sparse = C719.C713.apply_sparse_word(
        {packed: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return tuple(sorted(sparse))


def mode_of(source_basis: int) -> int:
    matter = source_basis & MATTER_MASK
    if matter.bit_count() != 1:
        raise AssertionError(("not-one-particle", source_basis, matter))
    return matter.bit_length() - 1


def controller_ast_evidence(
    controller_text: str, controller_tree: ast.Module
) -> dict[str, object]:
    """Recover the declared origin domain from syntax, not report payloads."""
    banks_literal = None
    for node in controller_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "BANKS"
            for target in node.targets
        ):
            banks_literal = ast.literal_eval(node.value)

    instrument = next(
        node
        for node in controller_tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "instrument_transition"
    )
    source_loops = []
    for node in ast.walk(instrument):
        if not isinstance(node, ast.For):
            continue
        if not isinstance(node.target, ast.Name) or node.target.id != "source":
            continue
        call = node.iter
        if (
            isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id == "range"
            and len(call.args) == 1
        ):
            source_loops.append({
                "stop": ast.literal_eval(call.args[0]),
                "lineno": node.lineno,
                "source": ast.get_source_segment(controller_text, node.iter),
            })

    lines = controller_text.splitlines()
    literal_lines = [
        {"lineno": index, "source": line.strip()}
        for index, line in enumerate(lines, 1)
        if (
            line.strip() == "BANKS = 12"
            or "for source in range(12)" in line
            or "matter = basis & ((1 << 12) - 1)" in line
            or "for origin in range(12)" in line
        )
    ]
    return {
        "BANKS_literal": banks_literal,
        "instrument_source_loops": source_loops,
        "literal_domain_lines": literal_lines,
    }


def derive_catalog(
    origins: tuple[int, ...],
) -> tuple[dict[int, tuple[int, ...]], list[dict[str, object]]]:
    families = {origin: initial_branches(origin) for origin in origins}
    rows = []
    for origin in origins:
        branch_rows = [
            {
                "mode": mode_of(basis),
                "endpoint_pointer": (
                    basis >> C719.R3_SOURCE_POINTER()
                ) & 1,
            }
            for basis in families[origin]
        ]
        rows.append({
            "origin": origin,
            "seed": 1 << origin,
            "branch_count": len(branch_rows),
            "modes_in_basis_order": [
                row["mode"] for row in branch_rows
            ],
            "mode_support": sorted(row["mode"] for row in branch_rows),
            "pointer_modes": sorted(
                row["mode"]
                for row in branch_rows
                if row["endpoint_pointer"]
            ),
        })
    return families, rows


def independent_compiled_row(
    origin: int,
    source_basis: int,
    pointer_site: tuple[int, int, int],
) -> dict[str, object]:
    """Own literal compiled-word trace with the Cycle-769 row contract."""
    source_mode = mode_of(source_basis)
    source_full = C719.controller_full_input(source_basis)
    full = source_full
    data_writes: list[dict[str, object]] = []
    record_pipeline: list[dict[str, object]] = []

    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before = C719.controller_register_rows(full)
        live_a = tuple(
            index for index, value in enumerate(before["A"]) if value
        )
        before_data = int(before["data"])
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        after = C719.controller_register_rows(full)
        after_data = int(after["data"])
        if before_data == after_data:
            continue

        station = live_a[0] if len(live_a) == 1 else None
        kind = (
            C719.PROGRAM[station][0]
            if station is not None else "invalid-sector"
        )
        index = (
            C719.PROGRAM[station][1]
            if station is not None else None
        )
        decoded_after = decoded_cell_surface(after_data)
        point = {
            "orbit_step": orbit_step,
            "live_A_station": station,
            "program_kind": kind,
            "program_index": index,
            "changed_data_bits": (
                before_data ^ after_data
            ).bit_count(),
            "accepted_cell_readable_after":
                decoded_after["acceptance_readable"],
            "accepted_cell_rows_after": decoded_after["cell_rows"],
            "decode_refusal_after": decoded_after["decode_refusal"],
        }
        data_writes.append(point)
        if kind == "bank":
            record_pipeline.append({
                "orbit_step": orbit_step,
                "program_kind": kind,
                "role": (
                    "packet_payload_written_to_bank; auxiliaries still dirty"
                ),
                "accepted_cell_readable_after": False,
            })
        if decoded_after["cell_rows"]:
            record_pipeline.append({
                "orbit_step": orbit_step,
                "program_kind": kind,
                "role": (
                    "accepted EventCell becomes exactly decodable after "
                    "finalizer"
                ),
                "accepted_cell_readable_after": True,
                "cell_rows": decoded_after["cell_rows"],
            })

    observed = C719.controller_register_rows(full)
    observed_data = int(observed["data"])
    host_data, host_a, host_b, _trace = K.run_orbit(
        C719.int_to_tuple(source_basis), C719.PROGRAM
    )
    restored = full
    for _step in range(C719.CONTROLLER_STATIONS):
        restored = C719.apply_fast_int(
            restored, C719.CONTROLLER_H_INVERSE_FAST
        )
    compiled_equals_host = (
        observed_data == C719.tuple_to_int(host_data)
    )
    a0_return = (
        observed["A"] == host_a
        == (1,) + (0,) * (C719.CONTROLLER_STATIONS - 1)
    )
    b_vacuum_return = (
        observed["B"] == host_b
        == (0,) * C719.CONTROLLER_STATIONS
    )
    work_return = not any(observed["work"])
    inverse_exact = restored == source_full
    decoded = decoded_cell_surface(observed_data)
    cell_rows = list(decoded["cell_rows"])
    accepted_equivalent = bool(cell_rows) and all(
        row["binder"] == row["valid"] == 1
        for row in cell_rows
    )
    formation_witness = {
        "positive_permanent_lock": None,
        "negative_nonformation": None,
        "decision": None,
        "reason": (
            "The landed output is exactly invertible reversible packet "
            "history; no physical permanence/locking Record bridge is "
            "supplied."
        ),
    }
    return {
        "branch_key": f"origin{origin}->mode{source_mode}",
        "origin": origin,
        "source_matter_mode": source_mode,
        "candidate_record_site": pointer_site,
        "R693_six_neighbor_pattern": None,
        "R693_neighbor_reason": (
            "Cycle719 supplies no R693 six-neighbor occupancy on this chart."
        ),
        "endpoint_pointer_antecedent": (
            source_basis >> C719.R3_SOURCE_POINTER()
        ) & 1,
        "lawful_compiled_branch": bool(
            compiled_equals_host
            and a0_return
            and b_vacuum_return
            and work_return
            and inverse_exact
        ),
        "conditioning_is_supplied_not_formation": {
            "BINDER": 1,
            "ACTUAL": 1,
            "ADMISS": 1,
            "LAW": 1,
            "clean_bank_link_route_genesis": True,
            "token_sector": "one A0 token; B/work vacuum",
            "local_refusal_truth": "A AND NOT (B OR work)",
        },
        "compiled_equals_host": compiled_equals_host,
        "A0_return": a0_return,
        "B_vacuum_return": b_vacuum_return,
        "work_return": work_return,
        "inverse_exact_anchor": inverse_exact,
        "data_write_points": data_writes,
        "record_cell_pipeline_points": record_pipeline,
        "decoded_EventCell_rows": cell_rows,
        "accepted_cell_equivalent_present": accepted_equivalent,
        "reversible_record_shaped_write": accepted_equivalent,
        "durable_permanent_record_write": None,
        "formation_witness": formation_witness,
        "formation_decision": None,
    }


def full_recount(
    origins: tuple[int, ...],
    families: dict[int, tuple[int, ...]],
    pointer_site: tuple[int, int, int],
) -> list[dict[str, object]]:
    return [
        independent_compiled_row(origin, basis, pointer_site)
        for origin in origins
        for basis in families[origin]
    ]


def landed_769_oracle_row(
    independent_row: dict[str, object],
    source_basis: int,
    pointer_site: tuple[int, int, int],
) -> dict[str, object]:
    """Use landed 769 only as a post-hoc exact-row comparator."""
    anchor = {
        "source_matter_mode": independent_row["source_matter_mode"],
        "endpoint_pointer": independent_row[
            "endpoint_pointer_antecedent"
        ],
        "compiled_equals_host": independent_row["compiled_equals_host"],
        "A0_return": independent_row["A0_return"],
        "B_vacuum_return": independent_row["B_vacuum_return"],
        "work_return": independent_row["work_return"],
        "inverse_exact": independent_row["inverse_exact_anchor"],
    }
    row = C769.compiled_branch_trace(
        source_basis, anchor, pointer_site
    )
    origin = int(independent_row["origin"])
    if origin:
        row = dict(row)
        row["branch_key"] = (
            f"origin{origin}->mode{row['source_matter_mode']}"
        )
        row["origin"] = origin
    return row


def light_host_trace(source_basis: int) -> dict[str, object]:
    """Structural station-level trace for the non-sampled origins."""
    data = C719.int_to_tuple(source_basis)
    stations = C719.CONTROLLER_STATIONS
    a = (1,) + (0,) * (stations - 1)
    b = (0,) * stations
    writes = []
    for orbit_step in range(stations):
        live = tuple(index for index, value in enumerate(a) if value)
        before_data = C719.tuple_to_int(data)
        data, a, b = K.apply_controller_step(
            data, C719.PROGRAM, a, b
        )
        after_data = C719.tuple_to_int(data)
        if before_data == after_data:
            continue
        station = live[0] if len(live) == 1 else None
        decoded = decoded_cell_surface(after_data)
        writes.append({
            "orbit_step": orbit_step,
            "program_kind": (
                C719.PROGRAM[station][0]
                if station is not None else "invalid-sector"
            ),
            "program_index": (
                C719.PROGRAM[station][1]
                if station is not None else None
            ),
            "accepted_cell_readable_after":
                decoded["acceptance_readable"],
            "cell_rows_after": decoded["cell_rows"],
        })
    final = decoded_cell_surface(C719.tuple_to_int(data))
    cell_rows = list(final["cell_rows"])
    return {
        "source_matter_mode": mode_of(source_basis),
        "endpoint_pointer_antecedent": (
            source_basis >> C719.R3_SOURCE_POINTER()
        ) & 1,
        "writes": writes,
        "decoded_EventCell_rows": cell_rows,
        "reversible_record_shaped_write": (
            bool(cell_rows)
            and all(
                row["binder"] == row["valid"] == 1
                for row in cell_rows
            )
        ),
        "A0_return": a == (1,) + (0,) * (stations - 1),
        "B_vacuum_return": not any(b),
    }


def classification_name(decisions: list[object]) -> str:
    if any(value is None for value in decisions):
        return "unidentified"
    if not any(decisions):
        return "empty"
    if all(decisions):
        return "all"
    return "structured"


def dual_reading(rows: list[dict[str, object]]) -> dict[str, object]:
    strict = [row["formation_decision"] for row in rows]
    exhaustive = [
        row["formation_decision"]
        if row["reversible_record_shaped_write"] else False
        for row in rows
    ]

    def evidence(decisions: list[object]) -> dict[str, object]:
        return {
            "classification": classification_name(decisions),
            "decidable_rows": sum(
                value is not None for value in decisions
            ),
            "positive_rows": sum(value is True for value in decisions),
            "negative_rows": sum(value is False for value in decisions),
            "unidentified_rows": sum(
                value is None for value in decisions
            ),
        }

    return {
        "exhaustive_no_write_is_negative": evidence(exhaustive),
        "no_write_is_not_negative_evidence": evidence(strict),
    }


def anchor_from_independent_row(
    row: dict[str, object],
) -> dict[str, object]:
    return {
        "source_matter_mode": row["source_matter_mode"],
        "endpoint_pointer": row["endpoint_pointer_antecedent"],
        "compiled_equals_host": row["compiled_equals_host"],
        "A0_return": row["A0_return"],
        "B_vacuum_return": row["B_vacuum_return"],
        "work_return": row["work_return"],
        "inverse_exact": row["inverse_exact_anchor"],
    }


def own_literal_audit_tuple(tree: ast.Module) -> tuple[str, ...]:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            if not isinstance(value, tuple):
                raise AssertionError("AUDIT_INPUT_PATHS is not literal tuple")
            return value
    raise AssertionError("missing AUDIT_INPUT_PATHS")


def repo_import_modules(tree: ast.Module) -> tuple[str, ...]:
    prefixes = ("frontier_", "physical_")
    names = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            names.extend(
                alias.name
                for alias in node.names
                if alias.name.startswith(prefixes)
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(prefixes)
        ):
            names.append(node.module)
    return tuple(names)


def main() -> int:
    started = perf_counter()

    actual_sha256 = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    controller_path = ROOT / AUDIT_INPUT_PATHS[0]
    controller_text = controller_path.read_text(encoding="utf-8")
    controller_tree = ast.parse(
        controller_text, filename=str(controller_path)
    )
    ast_evidence = controller_ast_evidence(
        controller_text, controller_tree
    )

    primary_path = ROOT / PRIMARY_TEXT_ONLY_PATH
    primary_text = primary_path.read_text(encoding="utf-8")
    primary_tree = ast.parse(
        primary_text, filename=str(primary_path)
    )
    own_path = Path(__file__).resolve()
    own_text = own_path.read_text(encoding="utf-8")
    own_tree = ast.parse(own_text, filename=str(own_path))
    own_audit_tuple = own_literal_audit_tuple(own_tree)
    imported_repo_modules = repo_import_modules(own_tree)
    expected_modules = tuple(
        Path(path).stem for path in AUDIT_INPUT_PATHS
    )
    blocklist_evidence = {
        "primary_path": PRIMARY_TEXT_ONLY_PATH,
        "primary_sha256": sha256(primary_text.encode()).hexdigest(),
        "primary_ast_nodes": sum(1 for _node in ast.walk(primary_tree)),
        "primary_in_sys_modules": PRIMARY_MODULE in sys.modules,
        "primary_imported_by_checker_ast":
            PRIMARY_MODULE in imported_repo_modules,
        "checker_repo_import_modules": imported_repo_modules,
        "checker_literal_AUDIT_INPUT_PATHS": own_audit_tuple,
    }
    blocklist_pass = (
        PRIMARY_MODULE not in sys.modules
        and PRIMARY_MODULE not in imported_repo_modules
        and own_audit_tuple == AUDIT_INPUT_PATHS
        and imported_repo_modules == expected_modules
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    )

    source_stops = tuple(
        int(row["stop"])
        for row in ast_evidence["instrument_source_loops"]
    )
    declared_stop = (
        source_stops[0] if len(source_stops) == 1 else -1
    )
    origins = tuple(range(declared_stop)) if declared_stop >= 0 else ()
    families, catalog_rows = derive_catalog(origins)
    seeds = tuple(1 << origin for origin in origins)
    conditioned_keys = {
        (origin, basis)
        for origin in origins
        for basis in families[origin]
    }
    unique_postmatter_basis = {
        basis
        for origin in origins
        for basis in families[origin]
    }
    support_partition: dict[
        tuple[tuple[int, ...], tuple[int, ...]], list[int]
    ] = {}
    for row in catalog_rows:
        key = (
            tuple(row["mode_support"]),
            tuple(row["pointer_modes"]),
        )
        support_partition.setdefault(key, []).append(int(row["origin"]))
    support_partition_rows = [
        {
            "origins": value,
            "mode_support": list(key[0]),
            "pointer_modes": list(key[1]),
        }
        for key, value in sorted(
            support_partition.items(), key=lambda item: item[1]
        )
    ]
    catalog_findings = {
        "module_structural_evidence": ast_evidence,
        "declared_origin_labels": origins,
        "unique_one_hot_origin_seeds": len(set(seeds)),
        "origins_censused": len(families),
        "branches_per_origin": {
            str(row["origin"]): row["branch_count"]
            for row in catalog_rows
        },
        "origin_conditioned_transition_entries": len(conditioned_keys),
        "unique_postmatter_basis_states": len(unique_postmatter_basis),
        "support_partition": support_partition_rows,
        "alias_boundary": (
            "72 is the number of distinct (origin, post-MATTER basis) "
            "transition entries.  There are 12 distinct post-MATTER basis "
            "states because each six-origin chart group shares a support; "
            "the origin label prevents transition-entry double counting."
        ),
        "outside_lawful_origin_family": None,
    }
    catalog_pass = (
        ast_evidence["BANKS_literal"] == MATTER_MODE_COUNT
        and source_stops == (MATTER_MODE_COUNT,)
        and origins == tuple(range(MATTER_MODE_COUNT))
        and len(set(seeds)) == MATTER_MODE_COUNT
        and all(seed.bit_count() == 1 for seed in seeds)
        and all(seed & MATTER_MASK == seed for seed in seeds)
        and len(families) == MATTER_MODE_COUNT
        and all(
            len(family) == 6
            and len(set(family)) == 6
            for family in families.values()
        )
        and len(conditioned_keys) == 72
        and all(
            0 <= mode_of(basis) < MATTER_MODE_COUNT
            for family in families.values()
            for basis in family
        )
    )

    pointer_site = tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][
            C719.R3_SOURCE_POINTER()
        ]
    )
    record_fields = tuple(field.name for field in fields(R693.Record))
    event_cell_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventCell)
    )
    event_chain_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventChain)
    )
    operationalization_pass = (
        record_fields == ("site", "content")
        and event_cell_fields == (
            "identity",
            "rotor",
            "carry",
            "predecessor",
            "binder",
            "valid",
            "orientation",
        )
        and event_chain_fields
        == ("bank", "cells", "admitted_ticks", "exhausted")
        and pointer_site == (-8, -1, 1)
    )

    first_recount = full_recount(
        SAMPLED_ORIGINS, families, pointer_site
    )
    first_pairs = [
        (origin, basis)
        for origin in SAMPLED_ORIGINS
        for basis in families[origin]
    ]
    landed_oracle = [
        landed_769_oracle_row(row, basis, pointer_site)
        for row, (_origin, basis) in zip(first_recount, first_pairs)
    ]
    exact_row_matches = [
        observed == expected
        for observed, expected in zip(first_recount, landed_oracle)
    ]
    second_recount = full_recount(
        SAMPLED_ORIGINS, families, pointer_site
    )

    recount_by_origin = {
        origin: [
            row for row in first_recount
            if row["origin"] == origin
        ]
        for origin in SAMPLED_ORIGINS
    }
    oracle_matches_by_origin = {
        origin: sum(
            exact
            for exact, row in zip(
                exact_row_matches, first_recount
            )
            if row["origin"] == origin
        )
        for origin in SAMPLED_ORIGINS
    }
    recount_rows = []
    for origin in SAMPLED_ORIGINS:
        rows = recount_by_origin[origin]
        record_rows = [
            row for row in rows
            if row["reversible_record_shaped_write"]
        ]
        recount_rows.append({
            "origin": origin,
            "rows": len(rows),
            "exact_landed_769_row_matches":
                oracle_matches_by_origin[origin],
            "row_digest": canonical_digest(rows),
            "record_shaped_count": len(record_rows),
            "record_shaped_modes": [
                row["source_matter_mode"] for row in record_rows
            ],
            "data_write_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["data_write_points"]
            ],
            "data_write_kinds": [
                point["program_kind"]
                for row in record_rows
                for point in row["data_write_points"]
            ],
            "pipeline_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["record_cell_pipeline_points"]
            ],
            "decoded_EventCell_rows": [
                cell
                for row in record_rows
                for cell in row["decoded_EventCell_rows"]
            ],
        })

    origin0_rows = recount_by_origin[0]
    origin0_anchor = {
        "rows": [
            anchor_from_independent_row(row)
            for row in origin0_rows
        ]
    }
    landed_origin0 = C769.run_census(
        origin0_anchor, pointer_site
    )
    origin0_bytes = canonical_bytes(origin0_rows)
    landed_origin0_bytes = canonical_bytes(landed_origin0)
    origin0_identity = {
        "byte_match": origin0_bytes == landed_origin0_bytes,
        "independent_sha256": sha256(origin0_bytes).hexdigest(),
        "landed_769_sha256": sha256(
            landed_origin0_bytes
        ).hexdigest(),
        "independent_bytes": len(origin0_bytes),
        "landed_769_bytes": len(landed_origin0_bytes),
    }

    light_rows_by_origin: dict[int, list[dict[str, object]]] = {}
    light_structure_rows = []
    for origin in origins:
        rows = [
            light_host_trace(basis) for basis in families[origin]
        ]
        light_rows_by_origin[origin] = rows
        record_rows = [
            row for row in rows
            if row["reversible_record_shaped_write"]
        ]
        light_structure_rows.append({
            "origin": origin,
            "record_shaped_count": len(record_rows),
            "record_shaped_modes": [
                row["source_matter_mode"] for row in record_rows
            ],
            "write_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["writes"]
            ],
            "write_kinds": [
                point["program_kind"]
                for row in record_rows
                for point in row["writes"]
            ],
            "readable_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["writes"]
                if point["cell_rows_after"]
            ],
            "decoded_EventCell_rows": [
                cell
                for row in record_rows
                for cell in row["decoded_EventCell_rows"]
            ],
            "nonrecord_write_count": sum(
                len(row["writes"])
                for row in rows
                if not row["reversible_record_shaped_write"]
            ),
            "rail_return_failures": sum(
                not row["A0_return"] or not row["B_vacuum_return"]
                for row in rows
            ),
        })

    expected_record_mode = {
        origin: 6 if origin < 6 else 1
        for origin in origins
    }
    expected_orientation = {
        origin: 1 if origin < 6 else -1
        for origin in origins
    }
    all_origin_structure_pass = all(
        row["record_shaped_count"] == 1
        and row["record_shaped_modes"]
        == [expected_record_mode[int(row["origin"])]]
        and row["write_steps"] == [0, 1, 125]
        and row["write_kinds"] == ["source", "bank", "finalizer"]
        and row["readable_steps"] == [125]
        and len(row["decoded_EventCell_rows"]) == 1
        and row["decoded_EventCell_rows"][0]["binder"] == 1
        and row["decoded_EventCell_rows"][0]["valid"] == 1
        and row["decoded_EventCell_rows"][0]["orientation"]
        == expected_orientation[int(row["origin"])]
        and row["nonrecord_write_count"] == 0
        and row["rail_return_failures"] == 0
        for row in light_structure_rows
    )
    sampled_full_pass = (
        len(first_recount) == 24
        and all(exact_row_matches)
        and all(row["lawful_compiled_branch"] for row in first_recount)
        and all(
            row["rows"] == 6
            and row["exact_landed_769_row_matches"] == 6
            and row["record_shaped_count"] == 1
            and row["record_shaped_modes"]
            == [expected_record_mode[int(row["origin"])]]
            and row["data_write_steps"] == [0, 1, 125]
            and row["data_write_kinds"]
            == ["source", "bank", "finalizer"]
            and row["pipeline_steps"] == [1, 125]
            and len(row["decoded_EventCell_rows"]) == 1
            and row["decoded_EventCell_rows"][0]["binder"] == 1
            and row["decoded_EventCell_rows"][0]["valid"] == 1
            and row["decoded_EventCell_rows"][0]["orientation"]
            == expected_orientation[int(row["origin"])]
            for row in recount_rows
        )
    )
    census_findings = {
        "sampled_origins_full_compiled_recount": recount_rows,
        "remaining_origins_independent_light_pass": [
            row for row in light_structure_rows
            if row["origin"] not in SAMPLED_ORIGINS
        ],
        "all_origin_light_pass_digest":
            canonical_digest(light_structure_rows),
        "origin0_landed_769_identity": origin0_identity,
    }
    census_pass = (
        operationalization_pass
        and sampled_full_pass
        and all_origin_structure_pass
    )

    source_macro = tuple(
        (gate.kind, tuple(gate.wires))
        for gate in C719.PROGRAM[0][2]
    )
    bank0_base = K.R3.MATTER_WIDTH
    mechanism_wires = {
        "source_pointer": C719.R3_SOURCE_POINTER(),
        "bank0_base": bank0_base,
        "bank0_pointer": bank0_base + C719.A.POINTER,
        "bank0_U_TO_V": bank0_base + C719.A.U_TO_V,
        "bank0_V_TO_U": bank0_base + C719.A.V_TO_U,
        "bank0_DIRECTION_OK": bank0_base + C719.A.DIRECTION_OK,
    }
    expected_source_macro = (
        ("CNOT", (
            mechanism_wires["source_pointer"],
            mechanism_wires["bank0_pointer"],
        )),
        ("TOF", (
            mechanism_wires["source_pointer"],
            6,
            mechanism_wires["bank0_U_TO_V"],
        )),
        ("TOF", (
            mechanism_wires["source_pointer"],
            1,
            mechanism_wires["bank0_V_TO_U"],
        )),
        ("CNOT", (
            mechanism_wires["bank0_U_TO_V"],
            mechanism_wires["bank0_DIRECTION_OK"],
        )),
        ("CNOT", (
            mechanism_wires["bank0_V_TO_U"],
            mechanism_wires["bank0_DIRECTION_OK"],
        )),
    )
    expected_partition = [
        {
            "origins": list(range(6)),
            "mode_support": [0, 2, 3, 4, 5, 6],
            "pointer_modes": [6],
        },
        {
            "origins": list(range(6, 12)),
            "mode_support": [1, 7, 8, 9, 10, 11],
            "pointer_modes": [1],
        },
    ]
    pattern_findings = {
        "decoded_MATTER_WORD_support_partition":
            support_partition_rows,
        "controller_source_macro": source_macro,
        "mechanism_wires": mechanism_wires,
        "mechanism": (
            "The decoded two-cell MATTER_WORD maps origins 0-5 to a "
            "six-mode support whose sole endpoint-pointer branch is mode 6, "
            "and origins 6-11 to a support whose sole pointer branch is mode "
            "1.  PROGRAM[0] then latches mode 6 onto bank0 U_TO_V and mode 1 "
            "onto bank0 V_TO_U under source pointer wire 40.  The common bank "
            "and finalizer pipeline therefore decodes orientations +1 and -1 "
            "respectively; the flip is wiring, not branch-list ordering."
        ),
        "observed_modes_by_origin": {
            str(row["origin"]): row["record_shaped_modes"]
            for row in light_structure_rows
        },
        "observed_orientations_by_origin": {
            str(row["origin"]):
                row["decoded_EventCell_rows"][0]["orientation"]
            for row in light_structure_rows
            if row["decoded_EventCell_rows"]
        },
    }
    pattern_pass = (
        support_partition_rows == expected_partition
        and source_macro == expected_source_macro
        and all_origin_structure_pass
    )

    classification_rows = []
    for origin in SAMPLED_ORIGINS:
        rows = recount_by_origin[origin]
        classification_rows.append({
            "origin": origin,
            **dual_reading(rows),
        })
    sampled_global_classification = dual_reading(first_recount)
    all_origin_structural_rows = [
        {
            "reversible_record_shaped_write":
                row["reversible_record_shaped_write"],
            "formation_decision": None,
        }
        for origin in origins
        for row in light_rows_by_origin[origin]
    ]
    all_origin_global_classification = dual_reading(
        all_origin_structural_rows
    )
    classification_findings = {
        "sampled_per_origin": classification_rows,
        "sampled_global": sampled_global_classification,
        "all_72_structural_global":
            all_origin_global_classification,
    }
    classification_pass = (
        all(
            row["exhaustive_no_write_is_negative"][
                "classification"
            ] == "unidentified"
            and row["exhaustive_no_write_is_negative"][
                "negative_rows"
            ] == 5
            and row["exhaustive_no_write_is_negative"][
                "unidentified_rows"
            ] == 1
            and row["no_write_is_not_negative_evidence"][
                "classification"
            ] == "unidentified"
            and row["no_write_is_not_negative_evidence"][
                "unidentified_rows"
            ] == 6
            for row in classification_rows
        )
        and sampled_global_classification[
            "exhaustive_no_write_is_negative"
        ]["classification"] == "unidentified"
        and sampled_global_classification[
            "no_write_is_not_negative_evidence"
        ]["classification"] == "unidentified"
        and all_origin_global_classification[
            "exhaustive_no_write_is_negative"
        ] == {
            "classification": "unidentified",
            "decidable_rows": 60,
            "positive_rows": 0,
            "negative_rows": 60,
            "unidentified_rows": 12,
        }
        and all_origin_global_classification[
            "no_write_is_not_negative_evidence"
        ] == {
            "classification": "unidentified",
            "decidable_rows": 0,
            "positive_rows": 0,
            "negative_rows": 0,
            "unidentified_rows": 72,
        }
    )

    determinism_pass = (
        first_recount == second_recount
        and canonical_digest(first_recount)
        == canonical_digest(second_recount)
    )
    sha_pass = actual_sha256 == PINNED_SHA256
    write_uniformity_pass = all(
        row["write_steps"] == [0, 1, 125]
        and row["readable_steps"] == [125]
        for row in light_structure_rows
    )
    controls_without_runtime_stdout = (
        sha_pass
        and blocklist_pass
        and origin0_identity["byte_match"]
        and determinism_pass
        and write_uniformity_pass
    )
    runtime_sec = perf_counter() - started
    controls_findings_base = {
        "sha_actual": actual_sha256,
        "sha_pinned": PINNED_SHA256,
        "primary_blocklist": blocklist_evidence,
        "origin0_byte_identity": origin0_identity,
        "determinism": {
            "first_sha256": canonical_digest(first_recount),
            "second_sha256": canonical_digest(second_recount),
            "exactly_equal": determinism_pass,
        },
        "write_pattern_every_origin": {
            str(row["origin"]): {
                "steps": row["write_steps"],
                "readable_steps": row["readable_steps"],
            }
            for row in light_structure_rows
        },
        "runtime_sec": runtime_sec,
        "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
    }

    noncontrol_conditions = {
        "1_CATALOG_ATTACK": catalog_pass,
        "2_CENSUS_RECOUNT": census_pass,
        "3_PATTERN_BOUNDARY_PROBE": pattern_pass,
        "4_DUAL_READING_CLASSIFICATION": classification_pass,
    }
    findings = {
        "1_CATALOG_ATTACK": catalog_findings,
        "2_CENSUS_RECOUNT": census_findings,
        "3_PATTERN_BOUNDARY_PROBE": pattern_findings,
        "4_DUAL_READING_CLASSIFICATION": classification_findings,
    }

    stdout_bytes = 0
    final_lines: list[str] = []
    final_conditions: dict[str, bool] = {}
    for _iteration in range(12):
        controls_findings = {
            **controls_findings_base,
            "stdout_bytes": stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        controls_pass = (
            controls_without_runtime_stdout
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and stdout_bytes < STDOUT_LIMIT_BYTES
        )
        final_conditions = {
            **noncontrol_conditions,
            "5_CONTROLS": controls_pass,
        }
        all_findings = {
            **findings,
            "5_CONTROLS": controls_findings,
        }
        final_lines = [
            (
                ("PASS" if final_conditions[name] else "FAIL")
                + f" CERTIFICATE_{name} :: "
                + compact(all_findings[name])
            )
            for name in final_conditions
        ]
        confirmed = all(final_conditions.values())
        final_lines.append(
            (
                "CONFIRMED CYCLE785_INDEPENDENT_ADVERSARIAL_CHECK :: "
                if confirmed else
                "REFUTED CYCLE785_INDEPENDENT_ADVERSARIAL_CHECK :: "
            )
            + (
                pattern_findings["mechanism"]
                if confirmed else
                "one or more adversarial certificates failed; inspect the "
                "verbatim finding above"
            )
        )
        next_size = len(("\n".join(final_lines) + "\n").encode())
        if next_size == stdout_bytes:
            break
        stdout_bytes = next_size

    print("\n".join(final_lines))
    return 0 if all(final_conditions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
