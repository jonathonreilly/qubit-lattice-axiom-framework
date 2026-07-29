#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-759 postimage obstruction.

The Cycle-759 primary is parsed only as source data.  Every orbit, residual,
reduction case, and geometry classification below is recomputed here from the
three declared suppliers.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/MULTISOURCE_POSTIMAGE_LAW_CYCLE759_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_DATA_PATH = (
    "scripts/frontier_cycle759_multisource_postimage_law_2026_07_28.py"
)
BLOCKLISTED_MODULE = (
    "frontier_cycle759_multisource_postimage_law_2026_07_28"
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_GLOBAL_CENSUS_SHA256 = (
    "d9aca312b50987cad3a88066c62b8667966afdec58124e37d8befd268e3cf627"
)
EXPECTED_POSITION_SIGNATURE_MAP_SHA256 = (
    "afcbd2d5e45bf310549f2ca508519b8eacaabd9c520ee6f18a4a487f1407a363"
)
EXPECTED_ANCHORED_GEOMETRY_MAP_SHA256 = (
    "13d64fcaa53eaee8eb39be701baa442b5a601d3c4c0b71fba58ad14faf98f4db"
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def assignment_table(
    body: list[ast.stmt],
) -> dict[str, ast.expr]:
    assignments: dict[str, ast.expr] = {}
    for node in body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.value is not None
        ):
            assignments[node.target.id] = node.value
    return assignments


def subscript_path(node: ast.AST) -> tuple[str, ...] | None:
    keys: list[str] = []
    cursor = node
    while isinstance(cursor, ast.Subscript):
        key = cursor.slice
        if not (
            isinstance(key, ast.Constant)
            and isinstance(key.value, str)
        ):
            return None
        keys.append(key.value)
        cursor = cursor.value
    if not isinstance(cursor, ast.Name):
        return None
    return (cursor.id, *reversed(keys))


def function_return_dict(
    function: ast.FunctionDef, required_key: str
) -> dict[str, ast.expr]:
    for node in ast.walk(function):
        if not isinstance(node, ast.Return) or not isinstance(
            node.value, ast.Dict
        ):
            continue
        output: dict[str, ast.expr] = {}
        for key, value in zip(node.value.keys, node.value.values):
            if (
                isinstance(key, ast.Constant)
                and isinstance(key.value, str)
            ):
                output[key.value] = value
        if required_key in output:
            return output
    raise AssertionError(("return dictionary not found", function.name))


def function_assignment(
    function: ast.FunctionDef, name: str
) -> ast.expr:
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return node.value
    raise AssertionError(("assignment not found", function.name, name))


def literal_value(node: ast.AST) -> object:
    return ast.literal_eval(node)


def has_literal_compare(
    function: ast.FunctionDef,
    path: tuple[str, ...],
    expected: object,
) -> bool:
    for node in ast.walk(function):
        if not isinstance(node, ast.Compare) or len(node.ops) != 1:
            continue
        if not isinstance(node.ops[0], ast.Eq) or len(node.comparators) != 1:
            continue
        if subscript_path(node.left) != path:
            continue
        try:
            observed = literal_value(node.comparators[0])
        except (ValueError, TypeError):
            continue
        if observed == expected:
            return True
    return False


def has_generated_tuple_compare(
    function: ast.FunctionDef,
    field: str,
    expected: tuple[object, ...],
) -> bool:
    for node in ast.walk(function):
        if not isinstance(node, ast.Compare) or len(node.comparators) != 1:
            continue
        try:
            observed = literal_value(node.comparators[0])
        except (ValueError, TypeError):
            continue
        if observed != expected:
            continue
        if any(
            isinstance(child, ast.Subscript)
            and subscript_path(child) is not None
            and subscript_path(child)[-1] == field
            for child in ast.walk(node.left)
        ):
            return True
    return False


def joined_string_constants(node: ast.AST) -> str:
    return " ".join(
        child.value
        for child in ast.walk(node)
        if isinstance(child, ast.Constant)
        and isinstance(child.value, str)
    )


def extraction() -> dict[str, object]:
    """AST-only extraction of the Cycle-759 primary's declared result."""

    primary_path = ROOT / PRIMARY_DATA_PATH
    source = primary_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(primary_path))
    assignments = assignment_table(tree.body)
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    main = functions["main"]
    residual_function = functions["residual_characterization_census"]
    law_function = functions["law_definition_certificate"]
    quotient_function = functions["quotient_postimage"]
    outcome_function = functions["outcome_certificate"]

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    audit_is_pure_literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    audit_value = (
        tuple(literal_value(audit_node))
        if audit_is_pure_literal
        else ()
    )
    import_aliases = {
        alias.asname or alias.name: alias.name
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    expected_supplier_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }

    residual_return = function_return_dict(
        residual_function, "unique_global_structural_residues"
    )
    global_count_expression = residual_return[
        "unique_global_structural_residues"
    ]
    global_count_rule_exact = (
        isinstance(global_count_expression, ast.Call)
        and isinstance(global_count_expression.func, ast.Name)
        and global_count_expression.func.id == "len"
        and len(global_count_expression.args) == 1
        and isinstance(global_count_expression.args[0], ast.Name)
        and global_count_expression.args[0].id == "unique_global"
    )
    unique_global_expression = function_assignment(
        residual_function, "unique_global"
    )
    unique_global_is_signature_set = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "set"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "all_signatures"
        for node in ast.walk(unique_global_expression)
    )

    residual_claim = {
        "configurations": 44,
        "epochs_per_configuration": 4,
        "lawful_updates": 176,
        "clean_updates": 0,
        "per_epoch_unique_signatures": (1, 1, 12, 14),
        "global_signature_rule": "len(set(all_signatures))",
        "global_signature_count": 25,
        "global_25_source":
            "independent evaluation of the AST-defined count",
    }
    residual_claim_exact = all(
        (
            has_literal_compare(
                main, ("residual", "configurations"), 44
            ),
            has_literal_compare(
                main, ("residual", "epochs_per_configuration"), 4
            ),
            has_literal_compare(
                main, ("residual", "lawful_updates"), 176
            ),
            has_literal_compare(
                main, ("residual", "clean_updates"), 0
            ),
            has_generated_tuple_compare(
                main,
                "uniform_across_44",
                (True, True, False, False),
            ),
            has_generated_tuple_compare(
                main,
                "unique_structural_residues",
                (1, 1, 12, 14),
            ),
            global_count_rule_exact,
            unique_global_is_signature_set,
        )
    )

    law_return = function_return_dict(
        law_function, "derivation_gate"
    )
    instantiated_expression = function_assignment(
        law_function, "instantiated"
    )
    law_strings = joined_string_constants(law_function)
    quotient_body = list(quotient_function.body)
    if (
        quotient_body
        and isinstance(quotient_body[0], ast.Expr)
        and isinstance(quotient_body[0].value, ast.Constant)
        and isinstance(quotient_body[0].value.value, str)
    ):
        quotient_body = quotient_body[1:]
    quotient_body_constants = tuple(
        child.value
        for statement in quotient_body
        for child in ast.walk(statement)
        if isinstance(child, ast.Constant)
    )
    attempted_law_exact = (
        literal_value(law_return["derivation_gate"])
        == "residual.uniform"
        and subscript_path(law_return["gate_value"])
        == ("residual", "uniform")
        and isinstance(instantiated_expression, ast.Call)
        and isinstance(instantiated_expression.func, ast.Name)
        and instantiated_expression.func.id == "bool"
        and len(instantiated_expression.args) == 1
        and subscript_path(instantiated_expression.args[0])
        == ("residual", "uniform")
        and isinstance(
            law_return["law_instantiated"], ast.Name
        )
        and law_return["law_instantiated"].id == "instantiated"
        and not quotient_body_constants
        and "No B_p may be introduced unless" in law_strings
        and "choosing an owned quotient would derive the law by fiat"
        in law_strings
    )

    single_source_exact = (
        has_literal_compare(
            main,
            ("law", "single_source_reduction", "cases"),
            44,
        )
        and has_literal_compare(
            main,
            ("law", "single_source_reduction", "failures"),
            0,
        )
    )

    first_outcome_if = next(
        node
        for node in outcome_function.body
        if isinstance(node, ast.If)
    )
    first_outcome_assignment = next(
        node
        for node in first_outcome_if.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "outcome"
            for target in node.targets
        )
    )
    outcome_return = function_return_dict(
        outcome_function, "scope_statement"
    )
    keys_expression = function_assignment(outcome_function, "keys")
    keys_mapping = {
        key.value: value
        for key, value in zip(
            keys_expression.keys, keys_expression.values
        )
        if isinstance(key, ast.Constant)
        and isinstance(key.value, str)
    } if isinstance(keys_expression, ast.Dict) else {}
    outcome_exact = (
        isinstance(first_outcome_if.test, ast.UnaryOp)
        and isinstance(first_outcome_if.test.op, ast.Not)
        and subscript_path(first_outcome_if.test.operand)
        == ("residual", "uniform")
        and literal_value(first_outcome_assignment.value)
        == "RESIDUAL_NON_UNIFORM"
        and has_literal_compare(
            main,
            ("outcome", "outcome"),
            "RESIDUAL_NON_UNIFORM",
        )
        and literal_value(
            keys_mapping["cycle750_single_source_scope_unchanged"]
        ) is True
        and literal_value(
            keys_mapping["cycle754_scope_unchanged"]
        ) is True
        and "no per-source quotient" in joined_string_constants(
            first_outcome_if
        )
        and "neither changes the Cycle-750 single-source theorem"
        in joined_string_constants(
            outcome_return["scope_statement"]
        )
        and "nor any Cycle-754 scope"
        in joined_string_constants(
            outcome_return["scope_statement"]
        )
    )

    declared_node = assignments.get("DECLARED_INPUT_PATHS")
    header_exact = (
        audit_is_pure_literal
        and audit_value == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and literal_value(assignments["AUDIT_TIMEOUT_SEC"]) == 1800
        and literal_value(assignments["NOTE_PATH"]) == NOTE_PATH
        and {
            alias: import_aliases.get(alias)
            for alias in ("F750", "M736", "K")
        }
        == expected_supplier_imports
    )

    passed = all(
        (
            header_exact,
            residual_claim_exact,
            attempted_law_exact,
            single_source_exact,
            outcome_exact,
        )
    )
    return {
        "pass": passed,
        "audit_tuple_literal_evaluates": audit_is_pure_literal,
        "audit_tuple": audit_value,
        "residual_census": residual_claim,
        "attempted_law": {
            "derivation_gate": "residual.uniform",
            "gate_value": False,
            "law_instantiated": False,
            "ownership_block": True,
            "no_quotient_by_fiat": True,
        },
        "single_source_reduction": {"cases": 44, "failures": 0},
        "outcome": "RESIDUAL_NON_UNIFORM",
        "scope_750_754_untouched": True,
        "primary_25_is_dynamic_not_literal": True,
    }


def watched_bank_coordinates() -> tuple[tuple[str, int], ...]:
    names_and_wires = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    names_and_wires.extend(
        (f"FRESH[{index}]", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    names_and_wires.extend(
        (f"ZERO_WORK[{index}]", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    names_and_wires.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(names_and_wires)


def independent_residual(
    after: int, bank_count: int
) -> tuple[tuple[str, str, int, int], ...]:
    """Recompute the landed nonzero projection without Cycle-759 code."""

    banks, links = K.M.unpack_state(after, bank_count)
    coordinates: list[tuple[str, str, int, int]] = []
    source_wire = K.R3.X.SOURCE_POINTER
    source_value = after[source_wire]
    if source_value:
        coordinates.append(
            ("source", "SOURCE_POINTER", source_wire, source_value)
        )
    named_wires = watched_bank_coordinates()
    coordinates.extend(
        (f"bank[{bank_index}]", name, wire, bank[wire])
        for bank_index, bank in enumerate(banks)
        for name, wire in named_wires
        if bank[wire]
    )
    coordinates.extend(
        (f"link[{link_index}]", f"WIRE[{wire}]", wire, value)
        for link_index, link in enumerate(links)
        for wire, value in enumerate(link)
        if value
    )
    return tuple(coordinates)


def separated_k2_positions() -> tuple[tuple[int, int], ...]:
    census = M736.configuration_census()
    return tuple(
        M736.occupied_sites(configuration)
        for configuration in census["configurations"]
        if sum(configuration) == 2
    )


def circular_distance(positions: tuple[int, int]) -> int:
    left, right = positions
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def residual_recount() -> tuple[
    dict[str, object], tuple[dict[str, object], ...]
]:
    positions = separated_k2_positions()
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    rows: list[dict[str, object]] = []
    lawful_updates = 0
    clean_updates = 0
    for event, direction, program, before, _landed_expected in fixtures:
        for source_positions in positions:
            tokens = tuple(
                int(station in source_positions)
                for station in range(len(program))
            )
            composition = M736.synchronous_composition_word(
                program, source_positions
            )
            independently_expected = K.A.apply_semantic(
                before, composition
            )
            after, rail_a, rail_b, _trace = K.run_orbit(
                before,
                program,
                token_positions=source_positions,
            )
            restored, inverse_a, inverse_b, _inverse_trace = (
                K.run_orbit(
                    after,
                    program,
                    token_positions=source_positions,
                    reverse=True,
                )
            )
            signature = independent_residual(after, FIXTURE_BANKS)
            lawful = all(
                (
                    after == independently_expected,
                    rail_a == tokens,
                    not any(rail_b),
                    restored == before,
                    inverse_a == rail_a,
                    inverse_b == rail_b,
                )
            )
            lawful_updates += lawful
            clean_updates += not signature
            rows.append(
                {
                    "epoch": event,
                    "direction": direction,
                    "positions": source_positions,
                    "distance": circular_distance(source_positions),
                    "signature": signature,
                    "lawful": lawful,
                    "program": program,
                }
            )

    global_counts = Counter(row["signature"] for row in rows)
    signature_order = tuple(
        sorted(global_counts, key=compact)
    )
    signature_ids = {
        signature: index
        for index, signature in enumerate(signature_order)
    }
    global_census = tuple(
        (signature, global_counts[signature])
        for signature in signature_order
    )
    position_signature_map = tuple(
        (
            row["epoch"],
            row["positions"],
            signature_ids[row["signature"]],
        )
        for row in rows
    )
    per_epoch_counts = tuple(
        Counter(
            row["signature"]
            for row in rows
            if row["epoch"] == epoch
        )
        for epoch in range(len(fixtures))
    )
    per_epoch_unique = tuple(
        len(counts) for counts in per_epoch_counts
    )
    per_epoch_histograms = tuple(
        tuple(sorted(counts.values()))
        for counts in per_epoch_counts
    )
    distance_histogram = Counter(
        source_distance
        for source_distance in map(circular_distance, positions)
    )
    all_binary = all(
        coordinate[3] == 1
        for row in rows
        for coordinate in row["signature"]
    )
    passed = all(
        (
            len(positions) == 44,
            len(fixtures) == 4,
            len(rows) == 176,
            lawful_updates == 176,
            clean_updates == 0,
            per_epoch_unique == (1, 1, 12, 14),
            len(global_counts) == 25,
            distance_histogram == Counter({2: 11, 3: 11, 4: 11, 5: 11}),
            all_binary,
            digest(global_census) == EXPECTED_GLOBAL_CENSUS_SHA256,
            digest(position_signature_map)
            == EXPECTED_POSITION_SIGNATURE_MAP_SHA256,
        )
    )
    certificate = {
        "pass": passed,
        "configurations": len(positions),
        "epochs": len(fixtures),
        "lawful_updates": lawful_updates,
        "clean_updates": clean_updates,
        "per_epoch_unique_signatures": per_epoch_unique,
        "per_epoch_signature_multiplicities": per_epoch_histograms,
        "global_unique_signatures": len(global_counts),
        "global_signature_multiplicities":
            tuple(sorted(global_counts.values())),
        "global_census_sha256": digest(global_census),
        "position_signature_map_sha256":
            digest(position_signature_map),
        "all_residual_contents_binary": all_binary,
    }
    return certificate, tuple(rows)


def symmetry_representative(
    positions: tuple[int, int], *, reflect: bool
) -> tuple[int, int]:
    signs = (1, -1) if reflect else (1,)
    images = []
    for sign in signs:
        for shift in range(RING_STATIONS):
            images.append(
                tuple(
                    sorted(
                        (sign * position + shift) % RING_STATIONS
                        for position in positions
                    )
                )
            )
    return min(images)


def classify_geometry(
    rows: tuple[dict[str, object], ...],
    signature_ids: dict[object, int],
    feature,
) -> dict[str, object]:
    groups: defaultdict[object, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[feature(row)].append(row)
    collisions = []
    for key, members in groups.items():
        observed = {
            signature_ids[member["signature"]]
            for member in members
        }
        if len(observed) > 1:
            collisions.append(
                {
                    "feature": key,
                    "signature_ids": tuple(sorted(observed)),
                    "positions": tuple(
                        member["positions"] for member in members
                    ),
                }
            )
    return {
        "exact": not collisions,
        "feature_cells": len(groups),
        "collision_cells": len(collisions),
        "max_signatures_per_cell": max(
            len(
                {
                    signature_ids[member["signature"]]
                    for member in members
                }
            )
            for members in groups.values()
        ),
        "first_collision": collisions[0] if collisions else None,
    }


def structure_probe(
    rows: tuple[dict[str, object], ...]
) -> dict[str, object]:
    """Seek a signature law from bounded configuration geometry."""

    signatures = tuple(
        sorted({row["signature"] for row in rows}, key=compact)
    )
    signature_ids = {
        signature: index for index, signature in enumerate(signatures)
    }

    def midpoint_phase(row: dict[str, object]) -> int:
        # 6 is the inverse of 2 modulo the odd ring size 11.
        return (6 * sum(row["positions"])) % RING_STATIONS

    def program_shape_pair(
        row: dict[str, object],
    ) -> tuple[tuple[str, int, int], ...]:
        program = row["program"]
        return tuple(
            sorted(
                (
                    program[position][0],
                    program[position][1],
                    len(program[position][2]),
                )
                for position in row["positions"]
            )
        )

    probes = {
        "epoch_only": classify_geometry(
            rows,
            signature_ids,
            lambda row: row["epoch"],
        ),
        "epoch_token_distance": classify_geometry(
            rows,
            signature_ids,
            lambda row: (row["epoch"], row["distance"]),
        ),
        "epoch_cyclic_position_orbit": classify_geometry(
            rows,
            signature_ids,
            lambda row: (
                row["epoch"],
                symmetry_representative(
                    row["positions"], reflect=False
                ),
            ),
        ),
        "epoch_dihedral_position_orbit": classify_geometry(
            rows,
            signature_ids,
            lambda row: (
                row["epoch"],
                symmetry_representative(
                    row["positions"], reflect=True
                ),
            ),
        ),
        "epoch_midpoint_phase": classify_geometry(
            rows,
            signature_ids,
            lambda row: (row["epoch"], midpoint_phase(row)),
        ),
        "epoch_distance_program_row_shape": classify_geometry(
            rows,
            signature_ids,
            lambda row: (
                row["epoch"],
                row["distance"],
                program_shape_pair(row),
            ),
        ),
        "epoch_distance_midpoint_phase": classify_geometry(
            rows,
            signature_ids,
            lambda row: (
                row["epoch"],
                row["distance"],
                midpoint_phase(row),
            ),
        ),
    }

    anchored_map = tuple(
        sorted(
            (
                row["epoch"],
                row["distance"],
                midpoint_phase(row),
                signature_ids[row["signature"]],
            )
            for row in rows
        )
    )
    frozen_digest = digest(anchored_map)
    distance_probe = probes["epoch_token_distance"]
    cyclic_probe = probes["epoch_cyclic_position_orbit"]
    dihedral_probe = probes["epoch_dihedral_position_orbit"]
    shape_probe = probes["epoch_distance_program_row_shape"]
    anchored_probe = probes["epoch_distance_midpoint_phase"]
    per_epoch_unique = tuple(
        len(
            {
                row["signature"]
                for row in rows
                if row["epoch"] == epoch
            }
        )
        for epoch in range(4)
    )
    no_compressive_exact_law = (
        not distance_probe["exact"]
        and not cyclic_probe["exact"]
        and not dihedral_probe["exact"]
        and not probes["epoch_midpoint_phase"]["exact"]
        and not shape_probe["exact"]
        and anchored_probe["exact"]
        and anchored_probe["feature_cells"] == len(rows)
    )
    passed = all(
        (
            per_epoch_unique == (1, 1, 12, 14),
            distance_probe["feature_cells"] == 16,
            distance_probe["collision_cells"] == 8,
            cyclic_probe["collision_cells"] == 8,
            dihedral_probe["collision_cells"] == 8,
            shape_probe["feature_cells"] == 172,
            shape_probe["collision_cells"] == 1,
            anchored_probe["feature_cells"] == 176,
            anchored_probe["collision_cells"] == 0,
            frozen_digest == EXPECTED_ANCHORED_GEOMETRY_MAP_SHA256,
            no_compressive_exact_law,
        )
    )
    return {
        "pass": passed,
        "result": (
            "No nontrivial exact symmetry-reduced correlation. "
            "Signature=f(epoch,distance,midpoint mod 11) is exact only "
            "because those 176 keys encode all 176 anchored configurations; "
            "that uncompressed map is frozen, not promoted to a quotient."
        ),
        "partial_structure": (
            "Epochs 0 and 1 are uniform; epochs 2 and 3 split into 12 "
            "and 14 signatures. Distance and cyclic/dihedral pair orbits "
            "do not determine the residue."
        ),
        "per_epoch_unique_signatures": per_epoch_unique,
        "probes": probes,
        "frozen_anchored_geometry_map_sha256": frozen_digest,
        "frozen_map_rows": len(anchored_map),
        "compressive_exact_law_found": False,
    }


def reduction_recount() -> dict[str, object]:
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    singleton_positions = tuple(
        M736.occupied_sites(configuration)
        for configuration
        in M736.configuration_census()["configurations"]
        if sum(configuration) == 1
    )
    cases = 0
    failures = 0
    lawful_cases = 0
    clean_cases = 0
    for _event, _direction, program, before, _expected in fixtures:
        for positions in singleton_positions:
            composition = M736.synchronous_composition_word(
                program, positions
            )
            expected_after = K.A.apply_semantic(before, composition)
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions
            )
            restored, inverse_a, inverse_b, _inverse_trace = (
                K.run_orbit(
                    after,
                    program,
                    token_positions=positions,
                    reverse=True,
                )
            )
            tokens = tuple(
                int(station in positions)
                for station in range(len(program))
            )
            lawful_cases += all(
                (
                    after == expected_after,
                    rail_a == tokens,
                    not any(rail_b),
                    restored == before,
                    inverse_a == rail_a,
                    inverse_b == rail_b,
                )
            )
            residual = independent_residual(after, FIXTURE_BANKS)
            landed_clean = not residual
            empty_owned_block: frozenset[
                tuple[str, str, int, int]
            ] = frozenset()
            reduced_clean = not any(
                coordinate not in empty_owned_block
                for coordinate in residual
            )
            cases += 1
            failures += reduced_clean != landed_clean
            clean_cases += landed_clean
    passed = all(
        (
            len(singleton_positions) == 11,
            len(fixtures) == 4,
            cases == 44,
            lawful_cases == 44,
            failures == 0,
        )
    )
    return {
        "pass": passed,
        "cases": cases,
        "lawful_cases": lawful_cases,
        "landed_clean_cases": clean_cases,
        "failures": failures,
        "identity": "R\\emptyset=R",
    }


def discipline(
    extraction_certificate: dict[str, object],
    runtime_seconds: float,
) -> dict[str, object]:
    self_source = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=__file__)
    assignments = assignment_table(self_tree.body)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    audit_literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    audit_value = (
        tuple(literal_value(audit_node)) if audit_literal else ()
    )
    imported_modules = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_from = {
        node.module or ""
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
    }
    prohibited_dynamic_calls = {
        node.func.id
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {
            "compile",
            "eval",
            "exec",
            "__import__",
        }
    }
    blocklist_clean = (
        BLOCKLISTED_MODULE not in imported_modules
        and BLOCKLISTED_MODULE not in imported_from
        and not prohibited_dynamic_calls
        and PRIMARY_DATA_PATH not in audit_value
    )
    language = {
        "outcome": "RESIDUAL_NON_UNIFORM",
        "quotient": "no quotient by fiat",
        "scopes": "the 750/754 scopes untouched",
    }
    passed = all(
        (
            audit_literal,
            audit_value == AUDIT_INPUT_PATHS,
            blocklist_clean,
            extraction_certificate["outcome"]
            == "RESIDUAL_NON_UNIFORM",
            extraction_certificate["scope_750_754_untouched"],
            language["quotient"] == "no quotient by fiat",
            language["scopes"] == "the 750/754 scopes untouched",
            literal_value(assignments["AUDIT_TIMEOUT_SEC"])
            == AUDIT_TIMEOUT_SEC
            == 1800,
            literal_value(assignments["NOTE_PATH"]) == NOTE_PATH,
            runtime_seconds < AUDIT_TIMEOUT_SEC,
        )
    )
    return {
        "pass": passed,
        "blocklist_clean": blocklist_clean,
        "primary_treatment": "AST data only; never imported or executed",
        "audit_tuple_literal_evaluates": audit_literal,
        "audit_input_paths": audit_value,
        "outcome_language": language,
        "runtime_under_1800_seconds": runtime_seconds < AUDIT_TIMEOUT_SEC,
    }


def public_certificate(
    name: str, certificate: dict[str, object]
) -> dict[str, object]:
    return {"name": name, **certificate}


def main() -> int:
    started = monotonic()
    extracted = extraction()
    recount, rows = residual_recount()
    # The primary defines the global value dynamically; the independent
    # recount supplies and freezes its numerical value.
    extracted["pass"] = bool(
        extracted["pass"]
        and recount["global_unique_signatures"] == 25
    )
    probe = structure_probe(rows)
    reduction = reduction_recount()
    elapsed = monotonic() - started
    disciplined = discipline(extracted, elapsed)

    certificates = (
        public_certificate("extraction", extracted),
        public_certificate("residual_recount", recount),
        public_certificate("structure_probe", probe),
        public_certificate("reduction_recount", reduction),
        public_certificate("discipline", disciplined),
    )
    all_pass = all(certificate["pass"] for certificate in certificates)
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "certificates": certificates,
        "checks_failed": sum(
            not certificate["pass"] for certificate in certificates
        ),
        "checks_passed": sum(
            certificate["pass"] for certificate in certificates
        ),
        "pass": all_pass,
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE759_POSTIMAGE_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE759_POSTIMAGE_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    output_lines = [
        (
            f"{'PASS' if certificate['pass'] else 'FAIL'} "
            f"{certificate['name']} :: {compact(certificate)}"
        )
        for certificate in certificates
    ]
    output_lines.append(compact(report))
    output = "\n".join(output_lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout exceeds 150KB", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
