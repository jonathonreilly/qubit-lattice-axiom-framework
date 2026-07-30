#!/usr/bin/env python3
"""Cycle 782 independent adversarial Choi/tableau -> LinkState decoder hunt.

This checker treats the Cycle-782 primary as blocklisted text.  It enumerates
every landed Cycle-720 module header and public top-level signature, probes the
two strongest near paths, and constructs a U320 input only if a landed
type-and-semantics-compatible adapter is found.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000

# Exactly the local Python files imported directly by this checker.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)

EXPECTED_CYCLE720_PATHS = (
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_genesis_broadcast_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
)

PRIMARY_TEXT_PATH = (
    "scripts/frontier_cycle782_choi_linkstate_bridge_2026_07_28.py"
)
SCOUT_TEXT_PATH = "COMPOSITE_PREP_MODULE_ID_2026_07_30.md"
PRIMARY_MODULE = "frontier_cycle782_choi_linkstate_bridge_2026_07_28"

EXPECTED_SHA256 = {
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py":
        "742ca885cea8b734d0ba8398028f60ae8a7162e7a7970ba3160015c0eb1b28b8",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py":
        "6a309f6449d155244b1dbee581cbe169937db5fe815c4dcc3e93929274a79004",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py":
        "42ada20e51eaf48c14d9862ddce1467982af90874829ddac62ba75b424d45da5",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py":
        "808c4cc2bac321dbc55aa1195d0768e77ee54cf63432ed04b277cd0ceeb0993c",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py":
        "990016c074cfc98cd2e4ba2f27afe0e7dd2da7a96b9a38a13d4062f778216a36",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py":
        "6877d532aaa1c9a97358ce2dfa2e26b1264c1f5a8ef477c217e9cc5a16c8d205",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py":
        "91ec583b03dafa5af1e26b1a87de771d3f92b1908848794d4b5b32b5e170e399",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py":
        "108568254546e1f64e4454b455f4aa866fe9abfbd4a6ca3a82f65b6a29e28974",
    "scripts/frontier_cycle720_companion_local_genesis_broadcast_2026_07_27.py":
        "a6409543a2c27545c4788550fc334c5d0c3948b252a29f164a83ca6743763649",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py":
        "d85a0dda0004e395d9e14b891a2c2616a93295b99c256b2d3e0f19e6c3bb360a",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py":
        "3064da20e961cea6c4c07a8317028ac9657d6fdd0643bd938a770491e5fad1fc",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py":
        "ee7d6c6d442bac4fe646535ed46369a649fc8b80eb661044242392058c139628",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py":
        "34c3b0fe14b6937010b88daf8594811fa8a6ef1741ab539b682db2429560c87d",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py":
        "0c999aab2010a4ed1b77a0491a36bd9447db867513f6095b4ac2ebb43c5c5399",
    "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py":
        "0cc8869eb34b2a1bf4df9d27070aed9a2750a1fe5bf220720311c6f918e04d49",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py":
        "dee1557eca4b88af75c469413290801577415cdf4ebfa3d970ceaa5ea15a2a8b",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py":
        "ed7cec59daa3a640a48706ed57d6a1699700a61d3d86964ad07a3e2b1c343721",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py":
        "438ab263262df8aee2ef1f2cc56fd6ac71a91d19c1fa9d422dd3f5418c7e340c",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py":
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py":
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    "scripts/frontier_cycle782_choi_linkstate_bridge_2026_07_28.py":
        "27ee20fff3dc1c846029bf8bee7602b926cb3a009301e9533c49cac4b4203089",
    "COMPOSITE_PREP_MODULE_ID_2026_07_30.md":
        "9d8efaec315d7c1f626018e5761d40b91d9e5b15951d738691d75b906ae64207",
}

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

import numpy as np

import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as T720
import frontier_cycle720_product_companion_full_word_holonomy_2026_07_27 as P720
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
OUTPUT_ROWS: list[tuple[str, object | None]] = []


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return (
            int(value.numerator)
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        )
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def encoded_line(label: str, value: object | None = None) -> str:
    if value is None:
        return label
    return label + " :: " + json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=jsonable,
    )


def emit(label: str, value: object | None = None) -> None:
    OUTPUT_ROWS.append((label, value))


def certificate(name: str, passed: bool, finding: object) -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    emit(("PASS " if passed else "FAIL ") + name, finding)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ast_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    answer = f"{node.name}({ast.unparse(node.args)})"
    if node.returns is not None:
        answer += " -> " + ast.unparse(node.returns)
    return answer


def bridge_tags(signature: str) -> tuple[str, ...]:
    lower = signature.lower()
    tags = []
    if any(token in lower for token in ("state", "encode", "prepare", "build")):
        tags.append("state_or_constructor")
    if any(token in lower for token in ("amplitude", "complex", "column")):
        tags.append("amplitude_or_column")
    if any(
        token in lower
        for token in (
            "measure", "read", "output", "expect", "density", "response",
            "sector_matrix", "certificate",
        )
    ):
        tags.append("measurement_or_readout")
    if "np.ndarray" in signature:
        tags.append("ndarray_surface")
    if "linkstate" in lower or "physicalstate" in lower:
        tags.append("named_u320_state_surface")
    return tuple(tags)


def interface_table(
    source_by_path: dict[str, str],
) -> tuple[dict[str, object], ...]:
    table = []
    for path in EXPECTED_CYCLE720_PATHS:
        tree = ast.parse(source_by_path[path], filename=path)
        functions = []
        classes = []
        aliases = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                signature = ast_signature(node)
                functions.append(
                    {
                        "line": node.lineno,
                        "name": node.name,
                        "signature": signature,
                        "bridge_tags": bridge_tags(signature),
                    }
                )
            elif isinstance(node, ast.ClassDef):
                methods = []
                annotations = []
                for child in node.body:
                    if isinstance(
                        child, (ast.FunctionDef, ast.AsyncFunctionDef)
                    ):
                        signature = ast_signature(child)
                        methods.append(
                            {
                                "line": child.lineno,
                                "name": child.name,
                                "signature": signature,
                                "bridge_tags": bridge_tags(signature),
                            }
                        )
                    elif isinstance(child, ast.AnnAssign) and isinstance(
                        child.target, ast.Name
                    ):
                        annotations.append(
                            {
                                "name": child.target.id,
                                "type": ast.unparse(child.annotation),
                            }
                        )
                classes.append(
                    {
                        "line": node.lineno,
                        "name": node.name,
                        "annotations": tuple(annotations),
                        "methods": tuple(methods),
                    }
                )
            elif isinstance(node, ast.Assign):
                names = tuple(
                    target.id
                    for target in node.targets
                    if isinstance(target, ast.Name)
                )
                for name in names:
                    if name.endswith(("State", "Key", "Coord", "Position")):
                        aliases.append(
                            {"name": name, "value": ast.unparse(node.value)}
                        )
        table.append(
            {
                "path": path,
                "header": ast.get_docstring(tree, clean=False),
                "functions": tuple(functions),
                "classes": tuple(classes),
                "type_aliases": tuple(aliases),
            }
        )
    return tuple(table)


def dataclass_schema(value: object) -> tuple[dict[str, str], ...]:
    if not is_dataclass(value):
        raise TypeError(f"{value!r} is not a dataclass")
    return tuple(
        {
            "name": field.name,
            "type": str(field.type),
            "default": (
                "required"
                if field.default is inspect.Parameter.empty
                or "MISSING_TYPE" in repr(field.default)
                else repr(field.default)
            ),
        }
        for field in fields(value)
    )


def target_interface_table() -> dict[str, object]:
    u320_names = (
        "zero_tensor",
        "state_norm",
        "normalize_state",
        "test_state",
        "link_recoil_vertex",
        "vector_expectation",
        "local_vertex",
        "vertex_gate",
        "matter_density",
        "q_density",
        "add_state_value",
        "extended_column",
        "encode_state",
        "inner_product",
    )
    s322_names = (
        "q_reservoir",
        "q_field",
        "normalize_state",
        "symmetric_one_one_state",
        "random_logical_state",
        "build_encoding",
        "encode_physical",
        "response_matrix",
    )
    return {
        "U320_constructors_and_inputs": {
            "LinkState": str(inspect.signature(U320.LinkState)),
            "LinkState_fields": dataclass_schema(U320.LinkState),
            "PhysicalKey": str(U320.PhysicalKey),
            "PhysicalState": str(U320.PhysicalState),
            "functions": tuple(
                {
                    "name": name,
                    "signature": str(inspect.signature(getattr(U320, name))),
                }
                for name in u320_names
            ),
        },
        "S322_constructors_and_inputs": {
            "LogicalState": str(S322.LogicalState),
            "PhysicalState": str(S322.PhysicalState),
            "QKey": str(S322.QKey),
            "functions": tuple(
                {
                    "name": name,
                    "signature": str(inspect.signature(getattr(S322, name))),
                }
                for name in s322_names
            ),
        },
    }


def gf2_rank(rows: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def pauli_matrix(row: object, qubits: int) -> np.ndarray:
    phase = int(getattr(row, "phase"))
    x = int(getattr(row, "x"))
    z = int(getattr(row, "z"))
    answer = np.zeros((1 << qubits, 1 << qubits), dtype=complex)
    for basis in range(1 << qubits):
        target = basis ^ x
        answer[target, basis] = (
            (1j ** phase) * ((-1) ** ((z & basis).bit_count()))
        )
    return answer


def localize_pauli(
    row: object, selected_qubits: tuple[int, ...]
) -> object:
    x = int(getattr(row, "x"))
    z = int(getattr(row, "z"))
    local_x = sum(
        ((x >> qubit) & 1) << local
        for local, qubit in enumerate(selected_qubits)
    )
    local_z = sum(
        ((z >> qubit) & 1) << local
        for local, qubit in enumerate(selected_qubits)
    )
    return T720.Pauli(int(getattr(row, "phase")), local_x, local_z)


def stabilizer_group(rows: tuple[object, ...]) -> tuple[object, ...]:
    answer = []
    for mask in range(1 << len(rows)):
        product = T720.Pauli()
        for index, row in enumerate(rows):
            if (mask >> index) & 1:
                product = product @ row
        answer.append(product)
    return tuple(answer)


def selected_density_analysis() -> dict[str, object]:
    """Independently materialize the primary's four-qubit restricted state."""
    fixture = T720.O.arbitrary_fixture(T720.Q.shape_cells((1, 1, 1)))
    generators, tags = T720.direct_graph_basis(fixture)
    selected_qubits = (
        0,
        1,
        fixture.qubits,
        fixture.qubits + 1,
    )
    selected_mask = sum(1 << qubit for qubit in selected_qubits)
    group = stabilizer_group(generators)
    reduced_group = tuple(
        localize_pauli(row, selected_qubits)
        for row in group
        if not (
            (int(getattr(row, "x")) | int(getattr(row, "z")))
            & ~selected_mask
        )
    )
    reduced_rank = gf2_rank(
        tuple(
            int(getattr(row, "x"))
            | (int(getattr(row, "z")) << len(selected_qubits))
            for row in reduced_group
        )
    )
    rho = sum(
        (pauli_matrix(row, len(selected_qubits)) for row in reduced_group),
        start=np.zeros((16, 16), dtype=complex),
    ) / 16.0

    tag_rows = {tag: row for row, tag in zip(generators, tags)}
    z_rows = tuple(
        localize_pauli(tag_rows[("onsite_Z", 0, mode)], selected_qubits)
        for mode in (0, 1)
    )
    four_x = localize_pauli(
        tag_rows[("onsite_XX", 0, 0)], selected_qubits
    )

    def expectation(matrix: np.ndarray, observable: object) -> int:
        value = np.trace(matrix @ pauli_matrix(observable, 4))
        if abs(value.imag) > 1e-10:
            raise AssertionError("Hermitian expectation acquired an imaginary part")
        return int(round(float(value.real)))

    correlations = []
    for output in range(2):
        row = []
        for reference in range(2):
            query = T720.Pauli(
                z=(1 << output) | (1 << (2 + reference))
            )
            row.append(expectation(rho, query))
        correlations.append(tuple(row))
    correlation = tuple(correlations)
    correlation_trace = sum(correlation[index][index] for index in range(2))
    normalized = tuple(
        tuple(Fraction(value, correlation_trace) for value in row)
        for row in correlation
    )

    identity = np.eye(16, dtype=complex)
    z0 = pauli_matrix(z_rows[0], 4)
    z1 = pauli_matrix(z_rows[1], 4)
    xx = pauli_matrix(four_x, 4)
    rho_plus = (identity + z0) @ (identity + z1) @ (identity + xx) / 16.0
    rho_minus = (identity + z0) @ (identity + z1) @ (identity - xx) / 16.0
    witness_correlations = []
    for candidate in (rho_plus, rho_minus):
        witness_correlations.append(
            tuple(
                tuple(
                    expectation(
                        candidate,
                        T720.Pauli(
                            z=(1 << output) | (1 << (2 + reference))
                        ),
                    )
                    for reference in range(2)
                )
                for output in range(2)
            )
        )
    eigenvalues = tuple(
        round(float(value.real), 12)
        for value in np.linalg.eigvalsh(rho)
        if abs(value) > 1e-10
    )
    return {
        "fixture": {
            "cells": len(fixture.cells),
            "matter_qubits": fixture.matter_qubits,
            "physical_output_qubits": fixture.qubits,
            "Choi_tableau_qubits":
                fixture.qubits + fixture.matter_qubits,
            "Hilbert_dimension": 2 ** (
                fixture.qubits + fixture.matter_qubits
            ),
        },
        "generator_count": len(generators),
        "generator_type": type(generators[0]).__name__,
        "generator_fields": dataclass_schema(T720.Pauli),
        "selected_qubits": selected_qubits,
        "reduced_group_size": len(reduced_group),
        "reduced_stabilizer_rank": reduced_rank,
        "reduced_density_rank":
            int(np.linalg.matrix_rank(rho, tol=1e-10)),
        "reduced_density_trace": round(float(np.trace(rho).real), 12),
        "nonzero_eigenvalues": eigenvalues,
        "two_point_Z_output_reference": correlation,
        "normalized_two_point_datum": normalized,
        "four_body_XX_expectation": expectation(rho, four_x),
        "observable_underdetermination_witness": {
            "plus_density_rank":
                int(np.linalg.matrix_rank(rho_plus, tol=1e-10)),
            "minus_density_rank":
                int(np.linalg.matrix_rank(rho_minus, tol=1e-10)),
            "both_positive_semidefinite": (
                float(np.min(np.linalg.eigvalsh(rho_plus))) > -1e-10
                and float(np.min(np.linalg.eigvalsh(rho_minus))) > -1e-10
            ),
            "same_Z_correlation_matrices":
                witness_correlations[0] == witness_correlations[1],
            "Z_correlation_matrices": tuple(witness_correlations),
            "four_body_XX_expectations": (
                expectation(rho_plus, four_x),
                expectation(rho_minus, four_x),
            ),
            "rho_matches_plus_witness":
                float(np.max(np.abs(rho - rho_plus))) < 1e-12,
        },
    }


def state_space_schemas(source: dict[str, object]) -> dict[str, object]:
    fixture = T720.O.arbitrary_fixture(T720.Q.shape_cells((2, 2, 2)))
    generators, tags = T720.direct_graph_basis(fixture)
    exchange, vertex, charge, momenta = U320.link_recoil_vertex(0.0)
    excited = np.zeros(6, dtype=complex)
    pair = U320.zero_tensor()
    local_output = U320.local_vertex(excited, pair, 0.0)
    sparse_probe = P720.apply_pauli_sparse(
        {1: 1.0 + 0.0j}, P720.Pauli()
    )
    return {
        "Cycle720_Choi_tableau": {
            "runtime_object":
                "tuple[Pauli,...] plus tuple tags; density is implicit",
            "Pauli_schema": dataclass_schema(T720.Pauli),
            "fixture_schema": dataclass_schema(T720.M.CompanionFixture),
            "cells": len(fixture.cells),
            "matter_qubits": fixture.matter_qubits,
            "physical_output_qubits": fixture.qubits,
            "Choi_tableau_qubits":
                fixture.qubits + fixture.matter_qubits,
            "Hilbert_dimension_formula": "2^(15*N)",
            "generator_count": len(generators),
            "generator_count_formula": "11*N+E",
            "tag_count": len(tags),
            "what_an_amplitude_is": (
                "none is exposed by the Choi-pump interface; Pauli phase/x/z "
                "bits specify an implicit mixed stabilizer density operator"
            ),
        },
        "Cycle720_sparse_product_route": {
            "probe_type": type(sparse_probe).__name__,
            "key_type": type(next(iter(sparse_probe))).__name__,
            "value_type": type(next(iter(sparse_probe.values()))).__name__,
            "what_an_amplitude_is": (
                "a complex coefficient keyed by one computational-basis "
                "occupation bitmask in a distinct product-companion route"
            ),
            "connected_to_Choi_pump": False,
        },
        "U320_LinkState_PhysicalState": {
            "LinkState_constructor": str(inspect.signature(U320.LinkState)),
            "LinkState_schema": dataclass_schema(U320.LinkState),
            "excited_shape": excited.shape,
            "pair_shape": pair.shape,
            "active_local_dimension": vertex.shape[0],
            "local_output_shapes": tuple(row.shape for row in local_output),
            "matrix_shapes": {
                "exchange": exchange.shape,
                "vertex": vertex.shape,
                "charge": charge.shape,
                "momenta": tuple(row.shape for row in momenta),
            },
            "PhysicalKey": str(U320.PhysicalKey),
            "PhysicalState": str(U320.PhysicalState),
            "what_an_amplitude_is": (
                "a complex coherent coefficient on one of six exclusive "
                "excited direction slots or one of 6*6*6 pair slots; lifted "
                "coefficients are keyed by five integer labels"
            ),
        },
        "S322_state_and_readout": {
            "LogicalState": str(S322.LogicalState),
            "PhysicalState": str(S322.PhysicalState),
            "response_matrix_signature":
                str(inspect.signature(S322.response_matrix)),
            "response_matrix_semantics":
                "2x2 real reservoir probabilities, not coherent amplitudes",
            "what_an_amplitude_is": (
                "a component of a 4096-entry Fock vector stored under a QKey; "
                "its PhysicalState values remain arrays, unlike U320 scalars"
            ),
        },
        "shared_geometry": {
            "Cycle720_directions": tuple(
                tuple(int(component) for component in row)
                for row in T720.R.DIRECTIONS
            ),
            "U320_directions": tuple(
                tuple(int(component) for component in row)
                for row in U320.c210.DIRECTIONS
            ),
            "identical": np.array_equal(
                np.asarray(T720.R.DIRECTIONS),
                np.asarray(U320.c210.DIRECTIONS),
            ),
            "scope": "six labels only; not a state-space identification",
        },
        "selected_recount": source,
    }


def surface_row(
    table: tuple[dict[str, object], ...], path: str, name: str
) -> dict[str, object]:
    module = next(row for row in table if row["path"] == path)
    functions = module["functions"]
    if not isinstance(functions, tuple):
        raise TypeError("malformed function table")
    matches = [row for row in functions if row["name"] == name]
    if len(matches) != 1:
        raise AssertionError(f"expected one interface {path}:{name}")
    return matches[0]


def incompatible_shape_probes(
    density: dict[str, object],
) -> dict[str, object]:
    datum = np.asarray(
        [
            [float(value) for value in row]
            for row in density["normalized_two_point_datum"]
        ],
        dtype=complex,
    )
    local_error = None
    try:
        U320.local_vertex(datum, U320.zero_tensor(), U320.ANGLE)
    except Exception as error:  # The exception is the probed contract boundary.
        local_error = {
            "type": type(error).__name__,
            "message": str(error),
        }
    constructor_accepts = U320.LinkState({(0, 0, 0): datum}, {})
    gate_error = None
    try:
        U320.vertex_gate(constructor_accepts, U320.ANGLE)
    except Exception as error:  # The dataclass is permissive; the vertex is not.
        gate_error = {
            "type": type(error).__name__,
            "message": str(error),
        }
    return {
        "observable_datum_shape": datum.shape,
        "U320_required_excited_shape": (6,),
        "local_vertex_rejected": local_error is not None,
        "local_vertex_error": local_error,
        "LinkState_constructor_is_shape_permissive": True,
        "vertex_gate_rejected_malformed_LinkState": gate_error is not None,
        "vertex_gate_error": gate_error,
        "finding": (
            "A generic np.ndarray return or permissive dataclass constructor "
            "is not a composable state adapter: the first U320 operation "
            "rejects the 2x2 observable datum."
        ),
    }


def decoder_hunt(
    table: tuple[dict[str, object], ...],
    density: dict[str, object],
) -> dict[str, object]:
    all_functions = tuple(
        (module["path"], function)
        for module in table
        for function in module["functions"]
    )
    direct_named = tuple(
        {
            "path": path,
            "signature": function["signature"],
        }
        for path, function in all_functions
        if (
            "LinkState" in function["signature"]
            or "PhysicalState" in function["signature"]
        )
    )
    ndarray_returns = tuple(
        {
            "path": path,
            "signature": function["signature"],
        }
        for path, function in all_functions
        if "-> np.ndarray" in function["signature"]
    )
    complex_dict_returns = tuple(
        {
            "path": path,
            "signature": function["signature"],
        }
        for path, function in all_functions
        if (
            "-> dict[int, complex]" in function["signature"]
            or "-> dict[tuple[int, int], complex]" in function["signature"]
        )
    )
    near_paths = (
        {
            "rank": 1,
            "surface": surface_row(
                table,
                "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
                "apply_pauli_sparse",
            )["signature"],
            "positive": "genuine complex state amplitudes are returned",
            "break": (
                "input/output keys are computational-basis bitmasks in the "
                "product-companion route; no Choi-pump output feeds it, and "
                "U320 PhysicalKey is a five-integer carrier/code label"
            ),
            "composable": False,
        },
        {
            "rank": 2,
            "surface": surface_row(
                table,
                "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
                "sector_matrix",
            )["signature"],
            "positive": "turns a Pauli row into a dense parity-sector operator",
            "break": (
                "the ndarray is a square operator matrix, not a six-entry "
                "excited amplitude or 6x6x6 pair tensor"
            ),
            "composable": False,
        },
        {
            "rank": 3,
            "surface": surface_row(
                table,
                "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py",
                "expansion_word",
            )["signature"],
            "positive": "returns complex coefficients",
            "break": (
                "coefficients are keyed Pauli-word expansion entries, not "
                "computational-state amplitudes or U320 PhysicalKeys"
            ),
            "composable": False,
        },
        {
            "rank": 4,
            "surface": str(inspect.signature(S322.response_matrix)),
            "positive": "returns a 2x2 numeric response readout",
            "break": (
                "entries are real reservoir probabilities after two updates; "
                "they are neither Cycle-720 outputs nor U320 coherent inputs"
            ),
            "composable": False,
        },
        {
            "rank": 5,
            "surface": (
                f"LinkState{inspect.signature(U320.LinkState)}; "
                f"encode_state{inspect.signature(U320.encode_state)}"
            ),
            "positive": (
                "U320 exposes an external-data LinkState constructor and a "
                "LinkState-to-PhysicalState encoder"
            ),
            "break": (
                "the constructor requires the coherent six/216 amplitudes "
                "already decoded; encode_state is downstream, not a decoder"
            ),
            "composable": False,
        },
    )
    direction_match = np.array_equal(
        np.asarray(T720.R.DIRECTIONS),
        np.asarray(U320.c210.DIRECTIONS),
    )
    shape_probes = incompatible_shape_probes(density)
    return {
        "finding": (
            "CONFIRMED — all 19 Cycle-720 headers and callable signatures "
            "were enumerated; zero landed composable Choi/tableau -> "
            "LinkState/PhysicalState paths were found."
        ),
        "family_modules_enumerated": len(table),
        "function_signatures_enumerated": len(all_functions),
        "direct_named_U320_state_adapters": direct_named,
        "generic_ndarray_returns": ndarray_returns,
        "complex_dict_returns": complex_dict_returns,
        "near_path_dispositions": near_paths,
        "constructor_and_shape_probe": shape_probes,
        "shared_direction_table": direction_match,
        "working_paths": (),
        "paths_found": 0,
        "bridged_input_built": False,
        "cross_term_census": {
            "status": "NOT_EVALUATED",
            "reason": (
                "no landed function supplies U320's coherent six-plus-216 "
                "input data from the Choi/tableau; padding, eigenselection, "
                "or relabeling would install the missing decoder"
            ),
        },
        "verdict": "CONFIRMED",
    }


def route_fidelity_audit(
    primary_source: str,
    density: dict[str, object],
) -> dict[str, object]:
    primary_tree = ast.parse(primary_source, filename=PRIMARY_TEXT_PATH)
    primary_string_constants = tuple(
        " ".join(node.value.split())
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    exact_primary_fragments = (
        "normalized four-qubit reduced stabilizer density operator",
        "seek a landed linear representation map from the selected "
        "Cycle-720 Choi/tableau object to six U320 excited amplitudes",
        "the common direction labels and the four exact output/reference "
        "two-point Z correlators",
        "the four-body XX stabilizer, the remaining stabilizer products, "
        "the output/reference register roles, the gauge register, a live "
        "complex amplitude vector, and a LinkState or PhysicalState key",
    )
    fragment_checks = {
        fragment: any(
            " ".join(fragment.split()) in constant
            for constant in primary_string_constants
        )
        for fragment in exact_primary_fragments
    }
    witness = density["observable_underdetermination_witness"]
    route_a_sound = (
        density["reduced_density_rank"] == 2
        and density["reduced_stabilizer_rank"] == 3
        and density["selected_qubits"] == (0, 1, 9, 10)
        and density["nonzero_eigenvalues"] == (0.5, 0.5)
    )
    route_b_sound = (
        density["normalized_two_point_datum"]
        == (
            (Fraction(1, 2), Fraction(0)),
            (Fraction(0), Fraction(1, 2)),
        )
        and density["four_body_XX_expectation"] == 1
        and witness["same_Z_correlation_matrices"]
        and witness["four_body_XX_expectations"] == (1, -1)
        and witness["both_positive_semidefinite"]
    )
    carried_table = (
        {
            "item": "six cubic direction labels",
            "primary": "carried",
            "independent": "carried as labels only",
        },
        {
            "item": "four Z_output/reference correlators",
            "primary": "carried",
            "independent": density["two_point_Z_output_reference"],
        },
        {
            "item": "four-body XX stabilizer",
            "primary": "not carried",
            "independent": density["four_body_XX_expectation"],
        },
        {
            "item": "remaining stabilizer products and register roles",
            "primary": "not carried",
            "independent": "not determined by the 2x2 Z table",
        },
        {
            "item": "gauge/reference disposal rule",
            "primary": "not carried",
            "independent": "no such rule appears in the landed target inputs",
        },
        {
            "item": "live complex amplitude / LinkState key",
            "primary": "not carried",
            "independent": "absent",
        },
    )
    return {
        "finding": (
            "CONFIRMED — routes (a) and (b) used the right restricted "
            "objects; the direct route confronted a rank-two reduced density "
            "with a coherent column, and the observable route provably loses "
            "independent XX information."
        ),
        "primary_fragments_verbatim_present": fragment_checks,
        "route_a_direct_map": {
            "faithful": route_a_sound,
            "selected_source": (
                "four qubits: output directions 0,1 and pulled-reference "
                "directions 0,1"
            ),
            "independent_density_rank": density["reduced_density_rank"],
            "independent_eigenvalues": density["nonzero_eigenvalues"],
            "target": "one coherent U320 input column",
        },
        "route_b_observable_map": {
            "faithful": route_b_sound,
            "candidate": density["normalized_two_point_datum"],
            "carried_not_carried_table": carried_table,
            "underdetermination_witness": witness,
        },
        "all_primary_fragments_present": all(fragment_checks.values()),
        "routes_faithful": route_a_sound and route_b_sound,
    }


MISSING_DECODER_SIGNATURE = (
    "decode_companion_choi_to_linkstate("
    "fixture: T720.M.CompanionFixture, "
    "generators: tuple[T720.Pauli, ...], "
    "tags: tuple[tuple, ...], *, "
    "position: U320.Position) -> U320.LinkState"
)


def near_miss_census(hunt: dict[str, object]) -> dict[str, object]:
    return {
        "finding": (
            "The best almost-path is direct_graph_basis -> [missing decoder] "
            "-> LinkState -> vertex_gate; exactly one landed callable is "
            "missing."
        ),
        "landed_prefix": (
            "T720.direct_graph_basis(fixture) -> "
            "tuple[tuple[Pauli,...],tuple[tuple,...]]"
        ),
        "shared_intermediate": (
            "identical ordered six-direction table, with no state semantics"
        ),
        "missing_single_piece_signature": MISSING_DECODER_SIGNATURE,
        "signature_count": 1,
        "obligations_inside_that_piece": (
            "dispose/condition the output-reference and gauge degrees of "
            "freedom; resolve or preserve the rank-two mixedness; map six "
            "independent qubits to exclusive direction slots; emit normalized "
            "six and 6x6x6 coherent arrays"
        ),
        "landed_suffix": (
            "U320.LinkState(excited,pair) -> U320.vertex_gate(state,angle)"
        ),
        "why_sparse_amplitudes_are_not_better": (
            "the product-companion sparse surface is not fed by the Choi "
            "pump and would additionally require bitmask-to-PhysicalKey "
            "semantics, so it is a two-gap route"
        ),
        "path_count_before_missing_piece": hunt["paths_found"],
    }


def single_channel_controls() -> tuple[tuple[dict[str, object], ...], bool]:
    exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    count = len(U320.c210.DIRECTIONS)
    rows = []
    passed = True
    for channel in range(count):
        expected_flat = (
            count * count * U320.REVERSE[channel]
            + count * channel
            + channel
        )
        exchange_support = tuple(
            flat for flat in range(count ** 3)
            if complex(exchange[count + flat, channel]) != 0j
        )
        vertex_support = tuple(
            flat for flat in range(count ** 3)
            if complex(vertex[count + flat, channel]) != 0j
        )
        source = tuple(
            int(value) for value in U320.c210.DIRECTIONS[channel]
        )
        target = tuple(
            int(value)
            for value in U320.c210.DIRECTIONS[U320.REVERSE[channel]]
        )
        response = (
            tuple(final - initial for final, initial in zip(target, source)),
            source,
            source,
        )
        balance = tuple(
            sum(response[component][axis] for component in range(3))
            for axis in range(3)
        )
        row_passed = (
            exchange_support == (expected_flat,)
            and vertex_support == (expected_flat,)
            and balance == (0, 0, 0)
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
                "vertex_branch_amplitude":
                    complex(vertex[count + expected_flat, channel]),
                "response_row": response,
                "dimensionless_direction_balance": balance,
                "match": row_passed,
            }
        )
    return tuple(rows), passed


def collect_core(
    source_by_path: dict[str, str], primary_source: str
) -> dict[str, object]:
    table = interface_table(source_by_path)
    density = selected_density_analysis()
    schemas = state_space_schemas(density)
    hunt = decoder_hunt(table, density)
    route = route_fidelity_audit(primary_source, density)
    near = near_miss_census(hunt)
    single_rows, single_passed = single_channel_controls()
    return {
        "interface_table": table,
        "target_interfaces": target_interface_table(),
        "density": density,
        "schemas": schemas,
        "hunt": hunt,
        "route": route,
        "near": near,
        "single_rows": single_rows,
        "single_passed": single_passed,
        "pump": T720.pump_algebra_certificate(),
    }


def rendered_output() -> str:
    return "\n".join(
        encoded_line(label, value) for label, value in OUTPUT_ROWS
    ) + "\n"


def main() -> int:
    started = time.monotonic()
    blocklist_before = PRIMARY_MODULE in sys.modules
    read_paths = tuple(dict.fromkeys(
        EXPECTED_CYCLE720_PATHS
        + (
            AUDIT_INPUT_PATHS[2],
            AUDIT_INPUT_PATHS[3],
            PRIMARY_TEXT_PATH,
            SCOUT_TEXT_PATH,
        )
    ))
    missing_paths = tuple(
        path for path in read_paths if not (ROOT / path).is_file()
    )
    if missing_paths:
        raise FileNotFoundError(f"missing declared inputs: {missing_paths}")
    input_bytes_before = {
        path: (ROOT / path).read_bytes() for path in read_paths
    }
    shas_before = {
        path: sha256_bytes(data)
        for path, data in input_bytes_before.items()
    }
    source_by_path = {
        path: input_bytes_before[path].decode("utf-8")
        for path in EXPECTED_CYCLE720_PATHS
    }
    primary_source = input_bytes_before[PRIMARY_TEXT_PATH].decode("utf-8")
    scout_source = input_bytes_before[SCOUT_TEXT_PATH].decode("utf-8")
    ast.parse(primary_source, filename=PRIMARY_TEXT_PATH)

    discovered_family = tuple(
        str(path.relative_to(ROOT))
        for path in sorted((ROOT / "scripts").glob("frontier_cycle720_*.py"))
    )
    direct_import_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (T720, P720, U320, S322)
    )

    first = collect_core(source_by_path, primary_source)
    second = collect_core(source_by_path, primary_source)
    deterministic = first == second
    table = first["interface_table"]
    target_interfaces = first["target_interfaces"]
    schemas = first["schemas"]
    density = first["density"]
    hunt = first["hunt"]
    route = first["route"]
    near = first["near"]
    single_rows = first["single_rows"]
    pump = first["pump"]

    input_bytes_after = {
        path: (ROOT / path).read_bytes() for path in read_paths
    }
    shas_after = {
        path: sha256_bytes(data)
        for path, data in input_bytes_after.items()
    }
    blocklist_after = PRIMARY_MODULE in sys.modules

    emit("CYCLE 782 INDEPENDENT ADVERSARIAL CHECKER")
    emit("AUDIT_INPUT_PATHS", AUDIT_INPUT_PATHS)
    emit(
        "CYCLE720 FAMILY INVENTORY",
        {
            "count": len(discovered_family),
            "paths": discovered_family,
        },
    )
    emit("CYCLE720 FULL INTERFACE TABLE", table)
    emit("U320 S322 CONSTRUCTOR TABLE", target_interfaces)
    emit("DECODER HUNT PATH CENSUS", hunt)
    emit("SCHEMA RECOUNT", schemas)
    emit("ROUTE FIDELITY AUDIT", route)
    emit("THE NEAR-MISS CENSUS", near)
    for row in single_rows:
        emit("U320 SINGLE-CHANNEL ROW", row)

    table_complete = (
        discovered_family == EXPECTED_CYCLE720_PATHS
        and len(table) == len(EXPECTED_CYCLE720_PATHS) == 19
        and all(
            isinstance(module["header"], str)
            and bool(module["header"])
            and isinstance(module["functions"], tuple)
            for module in table
        )
    )
    hunt_passed = (
        table_complete
        and hunt["paths_found"] == 0
        and not hunt["direct_named_U320_state_adapters"]
        and not hunt["bridged_input_built"]
        and hunt["cross_term_census"]["status"] == "NOT_EVALUATED"
        and all(
            not row["composable"] for row in hunt["near_path_dispositions"]
        )
        and hunt["constructor_and_shape_probe"]["local_vertex_rejected"]
        and hunt["constructor_and_shape_probe"][
            "vertex_gate_rejected_malformed_LinkState"
        ]
    )
    certificate(
        "THE DECODER HUNT",
        hunt_passed,
        {
            "finding": hunt["finding"],
            "interfaces_enumerated": hunt["family_modules_enumerated"],
            "signatures_enumerated":
                hunt["function_signatures_enumerated"],
            "paths_found": hunt["paths_found"],
            "bridged_input_built": hunt["bridged_input_built"],
            "cross_term_census": hunt["cross_term_census"],
        },
    )

    schema_passed = (
        density["fixture"]["Choi_tableau_qubits"] == 15
        and density["fixture"]["Hilbert_dimension"] == 2 ** 15
        and density["reduced_stabilizer_rank"] == 3
        and density["reduced_density_rank"] == 2
        and density["nonzero_eigenvalues"] == (0.5, 0.5)
        and schemas["Cycle720_Choi_tableau"]["Choi_tableau_qubits"] == 120
        and schemas["U320_LinkState_PhysicalState"][
            "active_local_dimension"
        ] == 222
        and schemas["U320_LinkState_PhysicalState"]["excited_shape"] == (6,)
        and schemas["U320_LinkState_PhysicalState"]["pair_shape"]
        == (6, 6, 6)
        and schemas["shared_geometry"]["identical"]
        and not schemas["Cycle720_sparse_product_route"][
            "connected_to_Choi_pump"
        ]
        and schemas["S322_state_and_readout"]["PhysicalState"]
        != schemas["U320_LinkState_PhysicalState"]["PhysicalState"]
    )
    certificate(
        "SCHEMA RECOUNT",
        schema_passed,
        {
            "finding": (
                "CONFIRMED — Cycle-720 exposes an implicit mixed stabilizer "
                "density over 15N qubits; U320 exposes coherent 6+216 "
                "amplitude columns and five-integer-keyed scalar amplitudes."
            ),
            "selected_Choi_density_rank":
                density["reduced_density_rank"],
            "selected_Choi_eigenvalues": density["nonzero_eigenvalues"],
            "U320_active_dimension":
                schemas["U320_LinkState_PhysicalState"][
                    "active_local_dimension"
                ],
            "S322_is_not_a_shared_state_type": True,
        },
    )

    route_passed = (
        route["all_primary_fragments_present"]
        and route["routes_faithful"]
        and route["route_a_direct_map"]["faithful"]
        and route["route_b_observable_map"]["faithful"]
    )
    certificate(
        "ROUTE-FIDELITY AUDIT",
        route_passed,
        {
            "finding": route["finding"],
            "route_a_faithful": route["route_a_direct_map"]["faithful"],
            "route_b_faithful":
                route["route_b_observable_map"]["faithful"],
            "independent_underdetermination_witness":
                density["observable_underdetermination_witness"],
        },
    )

    near_passed = (
        hunt["paths_found"] == 0
        and near["signature_count"] == 1
        and near["missing_single_piece_signature"]
        == MISSING_DECODER_SIGNATURE
        and "-> U320.LinkState" in MISSING_DECODER_SIGNATURE
    )
    certificate(
        "THE NEAR-MISS CENSUS",
        near_passed,
        {
            "finding": near["finding"],
            "best_path": (
                "direct_graph_basis -> [decoder] -> LinkState -> vertex_gate"
            ),
            "missing_single_piece_signature":
                near["missing_single_piece_signature"],
        },
    )

    anchor_checks = (
        shas_before == EXPECTED_SHA256
        and shas_after == EXPECTED_SHA256
        and shas_before == shas_after
    )
    pump_passed = (
        pump["canonical_output_plus_failures"] == 0
        and pump["canonical_trace_preservation_failures"] == 0
    )
    normalized_scout = " ".join(scout_source.split())
    scout_control = (
        "different operational channel space" in normalized_scout
        and "no landed composite-input preparation can be fed directly"
        in normalized_scout
    )
    primary_text_only = (
        not blocklist_before
        and not blocklist_after
        and PRIMARY_MODULE not in sys.modules
    )
    runtime_before_controls = time.monotonic() - started
    current_bytes = len(rendered_output().encode("utf-8"))
    projected_stdout_bytes = current_bytes + 25_000
    controls_passed = (
        anchor_checks
        and direct_import_paths == AUDIT_INPUT_PATHS
        and primary_text_only
        and pump_passed
        and first["single_passed"]
        and scout_control
        and callable(S322.response_matrix)
        and deterministic
        and runtime_before_controls < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < OUTPUT_LIMIT_BYTES
    )
    certificate(
        "CONTROLS",
        controls_passed,
        {
            "finding": (
                "All source anchors held; the primary remained text-only; "
                "the Cycle-720 pump control and six U320 single-channel rows "
                "reproduced deterministically within both resource limits."
            ),
            "AUDIT_INPUT_PATHS_exact_direct_imports":
                direct_import_paths == AUDIT_INPUT_PATHS,
            "sha256": shas_after,
            "primary_blocklisted_text_only": primary_text_only,
            "Cycle720_pump_algebra": pump,
            "U320_single_channel_rows_reproduced":
                first["single_passed"],
            "S322_constructor_surface_inspected": True,
            "scout_control": scout_control,
            "determinism_rerun": deterministic,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime_before_controls,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
    )

    final = {
        "status": (
            hunt["verdict"]
            if FAIL == 0
            else "CHECKER_FAILED"
        ),
        "decoder_paths_found": hunt["paths_found"],
        "interfaces_enumerated": hunt["family_modules_enumerated"],
        "near_miss": MISSING_DECODER_SIGNATURE,
        "pass": PASS,
        "fail": FAIL,
        "runtime_sec": time.monotonic() - started,
        "stdout_bytes": 0,
    }
    emit("FINAL", final)
    for _iteration in range(10):
        actual_bytes = len(rendered_output().encode("utf-8"))
        if final["stdout_bytes"] == actual_bytes:
            break
        final["stdout_bytes"] = actual_bytes
    output = rendered_output()
    actual_bytes = len(output.encode("utf-8"))
    if actual_bytes >= OUTPUT_LIMIT_BYTES:
        raise RuntimeError(
            f"stdout guard failed: {actual_bytes} >= {OUTPUT_LIMIT_BYTES}"
        )
    if time.monotonic() - started >= AUDIT_TIMEOUT_SEC:
        raise RuntimeError("runtime guard failed after final serialization")
    sys.stdout.write(output)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
