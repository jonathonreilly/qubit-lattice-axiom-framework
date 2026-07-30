#!/usr/bin/env python3
"""Cycle 782: exact Choi-tableau to LinkState bridge probe.

This runner treats the landed Cycle-720 and Cycle-320 objects as data.  It
attempts only representation changes exposed by those objects.  It makes no
law claim and does not import or execute the Cycle-768/771/774/778 primaries.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "COMPOSITE_PREP_MODULE_ID_2026_07_30.md",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
)
PRIMARY_TEXT_PATHS = AUDIT_INPUT_PATHS[4:]
BLOCKLIST = (
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle774_interference_sector_2026_07_28",
    "frontier_cycle778_norefit_attachment_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "108568254546e1f64e4454b455f4aa866fe9abfbd4a6ca3a82f65b6a29e28974",
    AUDIT_INPUT_PATHS[1]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[2]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    AUDIT_INPUT_PATHS[3]:
        "9d8efaec315d7c1f626018e5761d40b91d9e5b15951d738691d75b906ae64207",
    AUDIT_INPUT_PATHS[4]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[5]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[6]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[7]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
}

# Verbatim operative C_source declarations from the blocklisted landed source.
C_source = (
    "No physical momentum, work, energy, stress, or gravity meaning is assigned.",
    "dimensionless direction/flux only; not physical momentum, work, energy, stress, gravity, or metric",
    "The result is a bounded common-code response/reciprocity proxy, not physical energy, stress, gravity, metric, or time.",
    "finite occupation response only; not energy, stress, gravity, metric, force, or time",
    "does not splice routes, name occupation probability energy, or promote a selected source-port residual to an autonomous-law obstruction.",
    "probability/configuration current, not energy",
    "not physical energy",
    "nothing here calls it physical energy or stress",
)

import ast
from dataclasses import fields, is_dataclass
from fractions import Fraction
import hashlib
import inspect
import json
import math
from pathlib import Path
import sys
import time

import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as T720
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def emit(label: str, value: object | None = None) -> None:
    global STDOUT_BYTES
    line = label
    if value is not None:
        line += " :: " + json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=jsonable
        )
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def certificate(name: str, passed: bool, finding: object) -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    emit(("PASS" if passed else "FAIL") + " " + name, finding)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pauli_data(row: object) -> dict[str, object]:
    phase = int(getattr(row, "phase"))
    x = int(getattr(row, "x"))
    z = int(getattr(row, "z"))
    return {
        "phase": phase,
        "x_hex": hex(x),
        "z_hex": hex(z),
        "active_qubits": tuple(
            index for index in range((x | z).bit_length())
            if ((x | z) >> index) & 1
        ),
    }


def gf2_rank(values: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for original in values:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def stabilizer_group(rows: tuple[object, ...]) -> tuple[object, ...]:
    group = []
    for mask in range(1 << len(rows)):
        product = T720.Pauli()
        for index, row in enumerate(rows):
            if (mask >> index) & 1:
                product = product @ row
        group.append(product)
    return tuple(group)


def stabilizer_expectation(group: tuple[object, ...], query: object) -> int:
    for row in group:
        if int(getattr(row, "x")) != int(getattr(query, "x")):
            continue
        if int(getattr(row, "z")) != int(getattr(query, "z")):
            continue
        phase = int(getattr(row, "phase")) % 4
        if phase == 0:
            return 1
        if phase == 2:
            return -1
        raise ValueError("non-Hermitian Pauli found in stabilizer group")
    return 0


def literal_assignment(source: str, name: str) -> object:
    tree = ast.parse(source)
    matches = [
        node for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one literal assignment to {name}")
    return ast.literal_eval(matches[0].value)


def dataclass_schema(value: object) -> tuple[dict[str, object], ...]:
    if not is_dataclass(value):
        raise TypeError(f"{value!r} is not a dataclass")
    return tuple(
        {
            "name": field.name,
            "type": str(field.type),
            "default": (
                repr(field.default)
                if repr(field.default).find("MISSING_TYPE") < 0
                else "required"
            ),
        }
        for field in fields(value)
    )


def module_function_surface(module: object) -> tuple[dict[str, str], ...]:
    rows = []
    for name, function in inspect.getmembers(module, inspect.isfunction):
        if function.__module__ != getattr(module, "__name__"):
            continue
        rows.append(
            {
                "name": name,
                "signature": str(inspect.signature(function)),
            }
        )
    return tuple(rows)


def cycle720_schema() -> dict[str, object]:
    fixture = T720.O.arbitrary_fixture(T720.Q.shape_cells((2, 2, 2)))
    generators, tags = T720.direct_graph_basis(fixture)
    tree, fills = T720.schedule_tree_plaquettes(
        fixture, min(fixture.cells), (0, 1, 2)
    )
    directions = tuple(
        tuple(int(component) for component in direction)
        for direction in T720.R.DIRECTIONS
    )

    oriented_edges = []
    for edge_index, edge in enumerate(fixture.edges):
        left_index, right_index, owner, axis, left_mode, right_mode = edge
        left = fixture.cells[left_index]
        right = fixture.cells[right_index]
        displacement = tuple(
            right[coordinate] - left[coordinate] for coordinate in range(3)
        )
        direction_index = directions.index(displacement)
        reverse_index = directions.index(
            tuple(-component for component in displacement)
        )
        oriented_edges.append(
            {
                "axis": axis,
                "edge": edge_index,
                "left_cell": left,
                "left_direction": direction_index,
                "left_fixture_mode": left_mode,
                "owner": owner,
                "right_cell": right,
                "right_direction": reverse_index,
                "right_fixture_mode": right_mode,
            }
        )

    plaquettes = tuple(
        {
            "cycle_edge_axes": tuple(
                int(fixture.edges[edge][3]) for edge in cycle
            ),
            "cycle_edges": cycle,
            "new_edge": new_edge,
            "new_edge_axis": int(fixture.edges[new_edge][3]),
        }
        for new_edge, cycle in fills
    )
    plaquette_axis_pairs = tuple(
        sorted(
            {
                tuple(sorted(set(row["cycle_edge_axes"])))
                for row in plaquettes
            }
        )
    )
    generator_table = tuple(
        {
            "index": index,
            "tag": tag,
            **pauli_data(row),
        }
        for index, (row, tag) in enumerate(zip(generators, tags))
    )
    cells = len(fixture.cells)
    qubit_layout = {
        "cell_count": cells,
        "physical_output_matter": {
            "count": fixture.matter_qubits,
            "formula": "6*cell + direction",
            "range": (0, fixture.matter_qubits - 1),
        },
        "physical_output_gauge": {
            "count": fixture.qubits - fixture.matter_qubits,
            "formula": "matter_qubits + 3*cell + local",
            "range": (fixture.matter_qubits, fixture.qubits - 1),
        },
        "pulled_input_reference": {
            "count": fixture.matter_qubits,
            "formula": "qubits + 6*cell + direction",
            "range": (
                fixture.qubits,
                fixture.qubits + fixture.matter_qubits - 1,
            ),
        },
        "total_Choi_system_qubits": fixture.qubits + fixture.matter_qubits,
        "observed_scaling": {
            "matter_qubits": f"6*{cells}={fixture.matter_qubits}",
            "physical_output_qubits": f"9*{cells}={fixture.qubits}",
            "Choi_tableau_qubits":
                f"15*{cells}={fixture.qubits + fixture.matter_qubits}",
        },
    }
    return {
        "class_schemas": {
            "CompanionFixture": dataclass_schema(T720.M.CompanionFixture),
            "Pauli": dataclass_schema(T720.Pauli),
        },
        "directions": directions,
        "direct_graph_basis_source":
            inspect.getsource(T720.direct_graph_basis).strip(),
        "fixture_cells": fixture.cells,
        "fixture_edges": fixture.edges,
        "function_surface": module_function_surface(T720),
        "generator_count": len(generators),
        "generator_formula": f"11*{cells}+{len(fixture.edges)}",
        "generators": generator_table,
        "mode_direction_pairs": tuple(enumerate(directions)),
        "plaquette_axis_pairs": plaquette_axis_pairs,
        "plaquette_fill": plaquettes,
        "qubit_layout": qubit_layout,
        "representation": (
            "tuple[Pauli,...] with integer phase/x/z binary tableau fields, "
            "paired with tuple tags and schedule metadata"
        ),
        "scheduled_tree_edges": tree,
    }


def cycle320_schema() -> dict[str, object]:
    directions = tuple(
        tuple(int(component) for component in row)
        for row in U320.c210.DIRECTIONS
    )
    excited = U320.np.zeros(6, dtype=complex)
    pair = U320.zero_tensor()
    local_output = U320.local_vertex(excited, pair, 0.0)
    exchange, vertex, charge, momenta = U320.link_recoil_vertex(0.0)
    return {
        "LinkState_class": dataclass_schema(U320.LinkState),
        "LinkState_annotations": dict(U320.LinkState.__annotations__),
        "PhysicalKey_runtime": str(U320.PhysicalKey),
        "PhysicalState_runtime": str(U320.PhysicalState),
        "directions": directions,
        "input_column": {
            "active_column_dimension": int(vertex.shape[0]),
            "excited_shape": tuple(excited.shape),
            "excited_slots": "indices 0..5: one complex amplitude per direction",
            "pair_flat_index": "6 + 36*matter + 6*field + auxiliary",
            "pair_shape": tuple(pair.shape),
            "pair_slots": "indices 6..221: complex amplitudes over 6*6*6",
            "lifted_PhysicalKey":
                "(row, matter_mode, source, field_mode, auxiliary_mode)",
            "lifted_column_rule": (
                "extended_column obtains carrier_position from matter_mode; "
                "an excited column sets source to its carrier cell and "
                "field/auxiliary to -1; a pair column sets source=-1 and "
                "uses explicit field and carried auxiliary modes; row "
                "coefficients come from c316.column_items"
            ),
            "extended_column_source":
                inspect.getsource(U320.extended_column).strip(),
        },
        "introspected_signatures": {
            "encode_state": str(inspect.signature(U320.encode_state)),
            "extended_column": str(inspect.signature(U320.extended_column)),
            "link_recoil_vertex":
                str(inspect.signature(U320.link_recoil_vertex)),
            "local_vertex": str(inspect.signature(U320.local_vertex)),
            "vertex_gate": str(inspect.signature(U320.vertex_gate)),
        },
        "matrix_shapes_at_angle_zero": {
            "charge": tuple(charge.shape),
            "exchange": tuple(exchange.shape),
            "momenta": tuple(tuple(row.shape) for row in momenta),
            "vertex": tuple(vertex.shape),
        },
        "zero_input_output_shapes": tuple(
            tuple(row.shape) for row in local_output
        ),
    }


def shared_geometry(
    schema720: dict[str, object], schema320: dict[str, object]
) -> dict[str, object]:
    directions720 = schema720["directions"]
    directions320 = schema320["directions"]
    return {
        "correspondence": tuple(
            {
                "channel": index,
                "Cycle720_mode": index,
                "Cycle720_vector": direction,
                "U320_direction": index,
                "U320_vector": directions320[index],
            }
            for index, direction in enumerate(directions720)
        ),
        "direction_tables_identical": directions720 == directions320,
        "plaquette_axis_pairs": schema720["plaquette_axis_pairs"],
        "scope": (
            "the correspondence identifies only the six cubic direction "
            "labels and the three elementary coordinate planes"
        ),
    }


def prepared_two_channel_composite() -> dict[str, object]:
    fixture = T720.O.arbitrary_fixture(T720.Q.shape_cells((1, 1, 1)))
    generators, tags = T720.direct_graph_basis(fixture)
    full_group = stabilizer_group(generators)
    channels = (0, 1)
    selected_qubits = (
        channels[0],
        channels[1],
        fixture.qubits + channels[0],
        fixture.qubits + channels[1],
    )
    selected_mask = sum(1 << qubit for qubit in selected_qubits)
    reduced_subgroup = tuple(
        row for row in full_group
        if not ((int(getattr(row, "x")) | int(getattr(row, "z")))
                & ~selected_mask)
    )
    selected_tag_rows = tuple(
        {
            "index": index,
            "tag": tag,
            **pauli_data(row),
        }
        for index, (row, tag) in enumerate(zip(generators, tags))
        if tag in {
            ("onsite_Z", 0, channels[0]),
            ("onsite_Z", 0, channels[1]),
            ("onsite_XX", 0, channels[0]),
        }
    )
    rank = gf2_rank(
        tuple(
            int(getattr(row, "x"))
            | (int(getattr(row, "z"))
               << (fixture.qubits + fixture.matter_qubits))
            for row in reduced_subgroup
        )
    )

    correlations = []
    for output_direction in channels:
        correlation_row = []
        for reference_direction in channels:
            query = T720.Pauli(
                z=(
                    (1 << output_direction)
                    | (1 << (fixture.qubits + reference_direction))
                )
            )
            correlation_row.append(
                stabilizer_expectation(full_group, query)
            )
        correlations.append(tuple(correlation_row))
    z_correlation = tuple(correlations)
    trace = sum(
        (Fraction(z_correlation[index][index]) for index in range(2)),
        start=Fraction(),
    )
    normalized_datum = tuple(
        tuple(Fraction(value, 1) / trace for value in row)
        for row in z_correlation
    )
    four_body_x = T720.Pauli(
        x=sum(
            1 << qubit for qubit in selected_qubits
        )
    )
    directions = tuple(
        tuple(int(component) for component in T720.R.DIRECTIONS[channel])
        for channel in channels
    )
    return {
        "channels": channels,
        "directions": directions,
        "fixture_qubits": {
            "matter_qubits": fixture.matter_qubits,
            "physical_output_qubits": fixture.qubits,
            "total_Choi_tableau_qubits":
                fixture.qubits + fixture.matter_qubits,
        },
        "four_body_XX_expectation":
            stabilizer_expectation(full_group, four_body_x),
        "full_generator_count": len(generators),
        "full_stabilizer_group_unique_rows": len(
            {
                (
                    int(getattr(row, "phase")),
                    int(getattr(row, "x")),
                    int(getattr(row, "z")),
                )
                for row in full_group
            }
        ),
        "normalized_two_point_datum": normalized_datum,
        "reduced_density_rank": 2 ** (len(selected_qubits) - rank),
        "reduced_stabilizer_rank": rank,
        "reduced_stabilizer_subgroup": tuple(
            pauli_data(row) for row in reduced_subgroup
        ),
        "reduced_stabilizer_subgroup_size": len(reduced_subgroup),
        "selected_qubits": {
            "output_matter": channels,
            "pulled_input_reference": tuple(
                fixture.qubits + channel for channel in channels
            ),
        },
        "selected_tag_rows": selected_tag_rows,
        "selection_rule": (
            "the first landed onsite_XX tag is ('onsite_XX',0,0), "
            "which joins adjacent modes 0 and 1"
        ),
        "two_point_Z_output_reference": z_correlation,
    }


def bridge_attempt(
    schema720: dict[str, object],
    schema320: dict[str, object],
    composite: dict[str, object],
) -> dict[str, object]:
    surface = schema720["function_surface"]
    if not isinstance(surface, tuple):
        raise TypeError("Cycle-720 function surface is malformed")
    direct_adapters = tuple(
        row for row in surface
        if any(
            token in row["signature"]
            for token in ("LinkState", "PhysicalState", "np.ndarray")
        )
    )
    module_disclaimer = (
        "does not claim a translation-invariant autonomous genesis law, a "
        "deterministic Choi-to-live-input injection"
    )
    normalized_docstring = " ".join((T720.__doc__ or "").split())
    route_a = {
        "route": "a_direct_state_map",
        "attempt": (
            "seek a landed linear representation map from the selected "
            "Cycle-720 Choi/tableau object to six U320 excited amplitudes"
        ),
        "source_contract": {
            "object": "normalized four-qubit reduced stabilizer density operator",
            "rank": composite["reduced_density_rank"],
            "registers": composite["selected_qubits"],
            "tableau_subgroup_size":
                composite["reduced_stabilizer_subgroup_size"],
        },
        "target_contract": {
            "object": "U320 LinkState excited input column",
            "rank": 1,
            "shape": schema320["input_column"]["excited_shape"],
            "entries": "complex amplitudes on mutually exclusive direction slots",
        },
        "landed_adapter_candidates": direct_adapters,
        "module_disclaimer_present":
            module_disclaimer in normalized_docstring,
        "lawfulness_argument": (
            "A mere representation change would supply an explicit linear "
            "identification of the represented state data.  The landed "
            "source is a rank-two density operator on output and reference "
            "qubits, while the target is an amplitude vector.  Selecting a "
            "rank-one vector, removing the reference register, and imposing "
            "a one-hot direction decoding are additional operations; no such "
            "adapter is exposed by the landed module."
        ),
        "status": "FAIL_STRUCTURAL",
        "produced_U320_input": False,
    }

    datum = composite["normalized_two_point_datum"]
    route_b = {
        "route": "b_observable_map",
        "attempt": (
            "normalize the exact matrix <Z_output,d Z_reference,e> on the "
            "selected direction labels into a two-channel mixture/coherence "
            "datum"
        ),
        "exact_candidate": {
            "channels": composite["channels"],
            "matrix": datum,
            "mixture_weights": (datum[0][0], datum[1][1]),
            "coherence": (datum[0][1], datum[1][0]),
            "trace": datum[0][0] + datum[1][1],
        },
        "carried_over": (
            "the common direction labels and the four exact output/reference "
            "two-point Z correlators"
        ),
        "not_carried_over": (
            "the four-body XX stabilizer, the remaining stabilizer products, "
            "the output/reference register roles, the gauge register, a live "
            "complex amplitude vector, and a LinkState or PhysicalState key"
        ),
        "four_body_XX_expectation_omitted":
            composite["four_body_XX_expectation"],
        "lawfulness_argument": (
            "Correlation extraction is lawful as a summary of the landed "
            "tableau.  Promoting that summary to a U320 density operator is "
            "not a representation change exposed by either module: U320 has "
            "no mixture/coherence-datum input surface, and the two-point "
            "matrix does not determine the source stabilizer density "
            "operator.  Treating it as an input would add a decoder rule."
        ),
        "status": "FAIL_AS_U320_INPUT",
        "datum_extracted": True,
        "produced_U320_input": False,
    }
    mismatch = {
        "source": (
            "Cycle-720 Pauli-tableau stabilizer density operator on doubled "
            "output/reference qubit registers"
        ),
        "target": (
            "U320 complex-amplitude LinkState, or its lifted dictionary with "
            "five-integer PhysicalKey labels"
        ),
        "rank_mismatch": {
            "selected_source_density_rank": composite["reduced_density_rank"],
            "target_input_column_rank": 1,
        },
        "index_semantics_mismatch": (
            "Cycle-720 direction modes are independent qubits in each half; "
            "U320 directions are alternative slots of one six-component "
            "column and three indices of a 6x6x6 contact tensor."
        ),
        "missing_landed_operation": (
            "a deterministic Choi/reference decoder or injection producing "
            "LinkState/PhysicalState amplitudes while preserving the six "
            "direction action"
        ),
        "named_derivation_target": (
            "CHOI_TABLEAU_TO_LINKSTATE_DETERMINISTIC_DECODER"
        ),
    }
    route_c = {
        "route": "c_obstruction",
        "status": "OBSTRUCTED",
        "reason": mismatch,
    }
    return {
        "route_log": (route_a, route_b, route_c),
        "outcome": "OBSTRUCTED",
        "produced_U320_input": False,
        "cross_term_census": {
            "status": "NOT_EVALUATED",
            "reason": (
                "no lawful U320 input was produced; applying the vertex to "
                "the correlation datum would itself install the missing map"
            ),
        },
        "response_comparison": {
            "status": "NOT_APPLICABLE",
            "reason": "the obstructed branch reports the exact mismatch",
        },
        "exact_mismatch": mismatch,
        "law_claim": False,
        "response_law_established": False,
    }


def single_channel_controls() -> tuple[tuple[dict[str, object], ...], bool]:
    exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    direction_count = len(U320.c210.DIRECTIONS)
    rows = []
    passed = True
    for channel in range(direction_count):
        expected_flat = (
            direction_count * direction_count * U320.REVERSE[channel]
            + direction_count * channel
            + channel
        )
        exchange_support = tuple(
            flat for flat in range(direction_count ** 3)
            if complex(exchange[direction_count + flat, channel]) != 0j
        )
        vertex_support = tuple(
            flat for flat in range(direction_count ** 3)
            if complex(vertex[direction_count + flat, channel]) != 0j
        )
        source = tuple(
            Fraction(int(value))
            for value in U320.c210.DIRECTIONS[channel]
        )
        target = tuple(
            Fraction(int(value))
            for value in U320.c210.DIRECTIONS[U320.REVERSE[channel]]
        )
        response = (
            tuple(final - initial for final, initial in zip(target, source)),
            source,
            source,
        )
        balance = tuple(
            sum(
                (response[component][axis] for component in range(3)),
                start=Fraction(),
            )
            for axis in range(3)
        )
        row_passed = (
            exchange_support == (expected_flat,)
            and vertex_support == (expected_flat,)
            and not any(balance)
        )
        passed = passed and row_passed
        rows.append(
            {
                "channel": channel,
                "direction": source,
                "expected_branch_flat": expected_flat,
                "expected_branch_tuple":
                    (U320.REVERSE[channel], channel, channel),
                "exchange_branch_support": exchange_support,
                "vertex_branch_support": vertex_support,
                "response_row": response,
                "dimensionless_direction_balance": balance,
                "match": row_passed,
            }
        )
    return tuple(rows), passed


def collect_experiment() -> dict[str, object]:
    schema720 = cycle720_schema()
    schema320 = cycle320_schema()
    geometry = shared_geometry(schema720, schema320)
    composite = prepared_two_channel_composite()
    bridge = bridge_attempt(schema720, schema320, composite)
    return {
        "schemas": {
            "Cycle720_Choi_tableau": schema720,
            "U320_LinkState_PhysicalState": schema320,
        },
        "shared_geometry": geometry,
        "prepared_two_channel_composite": composite,
        "bridge": bridge,
    }


def main() -> int:
    started = time.monotonic()
    blocklist_before = {
        module: module in sys.modules for module in BLOCKLIST
    }
    input_bytes_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    shas_before = {
        path: sha256_bytes(data)
        for path, data in input_bytes_before.items()
    }
    primary_sources = {
        path: input_bytes_before[path].decode("utf-8")
        for path in PRIMARY_TEXT_PATHS
    }
    c_source_768 = literal_assignment(
        primary_sources[PRIMARY_TEXT_PATHS[0]], "C_source"
    )
    c_source_771 = literal_assignment(
        primary_sources[PRIMARY_TEXT_PATHS[1]], "C_source"
    )
    tree774 = ast.parse(primary_sources[PRIMARY_TEXT_PATHS[2]])
    c_source_assignments_774 = tuple(
        node for node in tree774.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "C_source"
            for target in node.targets
        )
    )
    c_source_778 = literal_assignment(
        primary_sources[PRIMARY_TEXT_PATHS[3]], "C_source"
    )
    firewall_exact = (
        c_source_768 == C_source
        and c_source_771 == C_source[:4]
        and not c_source_assignments_774
        and c_source_778 == C_source[:4]
    )
    scout_text = input_bytes_before[AUDIT_INPUT_PATHS[3]].decode("utf-8")

    first = collect_experiment()
    second = collect_experiment()
    deterministic = first == second
    schemas = first["schemas"]
    geometry = first["shared_geometry"]
    composite = first["prepared_two_channel_composite"]
    bridge = first["bridge"]

    emit("CYCLE 782 CHOI TO LINKSTATE BRIDGE PROBE")
    emit("C_source", C_source)
    emit(
        "SCHEMAS SIDE BY SIDE",
        {
            "Cycle720_Choi_tableau": schemas["Cycle720_Choi_tableau"],
            "U320_LinkState_PhysicalState":
                schemas["U320_LinkState_PhysicalState"],
            "shared_geometry": geometry,
        },
    )
    emit("PREPARED TWO-CHANNEL COMPOSITE", composite)
    for route in bridge["route_log"]:
        emit("BRIDGE ATTEMPT " + route["route"], route)
    emit("OUTCOME", bridge["outcome"])
    emit("CROSS-TERM CENSUS", bridge["cross_term_census"])
    emit("EXACT STRUCTURAL MISMATCH", bridge["exact_mismatch"])

    single_rows, single_rows_passed = single_channel_controls()
    for row in single_rows:
        emit("U320 SINGLE-CHANNEL ROW", row)
    pump = T720.pump_algebra_certificate()
    pump_passed = (
        pump["canonical_output_plus_failures"] == 0
        and pump["canonical_trace_preservation_failures"] == 0
    )

    input_bytes_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    shas_after = {
        path: sha256_bytes(data)
        for path, data in input_bytes_after.items()
    }
    blocklist_after = {
        module: module in sys.modules for module in BLOCKLIST
    }

    schema720 = schemas["Cycle720_Choi_tableau"]
    schema320 = schemas["U320_LinkState_PhysicalState"]
    schema_checks = (
        schema720["generator_count"]
        == 11 * len(schema720["fixture_cells"])
        + len(schema720["fixture_edges"])
        and schema720["qubit_layout"]["total_Choi_system_qubits"] == 120
        and schema320["input_column"]["active_column_dimension"] == 222
        and schema320["input_column"]["excited_shape"] == (6,)
        and schema320["input_column"]["pair_shape"] == (6, 6, 6)
        and geometry["direction_tables_identical"]
        and geometry["plaquette_axis_pairs"] == ((0, 1), (0, 2), (1, 2))
    )
    anchor_checks = (
        shas_before == EXPECTED_SHA256
        and shas_after == EXPECTED_SHA256
        and shas_before == shas_after
    )
    blocklist_checks = (
        not any(blocklist_before.values())
        and not any(blocklist_after.values())
    )
    normalized_scout = " ".join(scout_text.split())
    scout_control = (
        "different operational channel space" in normalized_scout
        and "no landed composite-input preparation can be fed directly"
        in normalized_scout
    )

    certificate(
        "CERTIFICATE A anchors blocklist and introspected schemas",
        (
            anchor_checks
            and blocklist_checks
            and schema_checks
            and callable(T720.direct_graph_basis)
            and callable(U320.local_vertex)
            and callable(S322.response_matrix)
        ),
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "blocklist": BLOCKLIST,
            "blocklist_after": blocklist_after,
            "blocklist_before": blocklist_before,
            "primary_access": "text/AST only; never imported or executed",
            "schema_checks": schema_checks,
            "sha256": shas_after,
        },
    )
    route_a, route_b, route_c = bridge["route_log"]
    certificate(
        "CERTIFICATE B route-by-route bridge attempt",
        (
            route_a["status"] == "FAIL_STRUCTURAL"
            and not route_a["produced_U320_input"]
            and route_b["status"] == "FAIL_AS_U320_INPUT"
            and route_b["datum_extracted"]
            and not route_b["produced_U320_input"]
            and route_c["status"] == "OBSTRUCTED"
        ),
        {
            "route_a": route_a,
            "route_b": route_b,
            "route_c": route_c,
        },
    )
    certificate(
        "CERTIFICATE C frozen outcome and cross-term disposition",
        (
            bridge["outcome"] == "OBSTRUCTED"
            and not bridge["produced_U320_input"]
            and bridge["cross_term_census"]["status"] == "NOT_EVALUATED"
            and not bridge["law_claim"]
            and not bridge["response_law_established"]
        ),
        {
            "cross_term_census": bridge["cross_term_census"],
            "law_claim": bridge["law_claim"],
            "outcome": bridge["outcome"],
            "response_law_established":
                bridge["response_law_established"],
        },
    )
    mismatch = bridge["exact_mismatch"]
    certificate(
        "CERTIFICATE D exact obstruction mismatch",
        (
            mismatch["rank_mismatch"]["selected_source_density_rank"] == 2
            and mismatch["rank_mismatch"]["target_input_column_rank"] == 1
            and mismatch["named_derivation_target"]
            == "CHOI_TABLEAU_TO_LINKSTATE_DETERMINISTIC_DECODER"
            and bridge["response_comparison"]["status"] == "NOT_APPLICABLE"
        ),
        {
            "mismatch": mismatch,
            "response_comparison": bridge["response_comparison"],
        },
    )

    runtime = time.monotonic() - started
    projected_stdout_bytes = STDOUT_BYTES + 20_000
    certificate(
        "CERTIFICATE E controls determinism runtime and stdout",
        (
            anchor_checks
            and blocklist_checks
            and firewall_exact
            and pump_passed
            and scout_control
            and single_rows_passed
            and deterministic
            and runtime < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < OUTPUT_LIMIT_BYTES
        ),
        {
            "Cycle720_control": {
                "candidate_sha_anchored": anchor_checks,
                "pump_algebra_certificate": pump,
                "pump_passed": pump_passed,
            },
            "C_source_exact": firewall_exact,
            "determinism_rerun": deterministic,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "scout_control": scout_control,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
            "U320_single_channel_rows_reproduced": single_rows_passed,
        },
    )
    final_runtime = time.monotonic() - started
    emit(
        "FINAL",
        {
            "fail": FAIL,
            "outcome": bridge["outcome"],
            "pass": PASS,
            "response_law_established": False,
            "runtime_sec": final_runtime,
            "stdout_bytes_before_final": STDOUT_BYTES,
        },
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
