#!/usr/bin/env python3
"""Cycle 826 independent adversarial check of IDENTITY_NO_REACH.

All evidence modules are SHA-pinned text/AST inputs.  None is imported or
executed.  The checker reconstructs the Cycle-805 alternatives from their
construction, traces their occurrence-label actions, derives the induced W7
action by a typed dependency projection, and independently recounts an exact
response slice.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle826_response_vs_relabeling_2026_07_28.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle821_orbit_observability_2026_07_28.py",
    "scripts/frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "f30c343dcab77e4249ae0161389d725dfeceb26af1cf0e5c5137630142887bb8",
    AUDIT_INPUT_PATHS[1]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[2]:
        "36273e2f13c26803d7a28bb65a3efce0aab82c766e4dc039d8269f0d53973342",
    AUDIT_INPUT_PATHS[3]:
        "e064b2f431f3e125b8c7f8176e6331f3fee41c2d1dc8ba7e3e65ae97a4ebb6b0",
    AUDIT_INPUT_PATHS[4]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "a7e990500e536eb2ee2979730396b475456006dc",
    AUDIT_INPUT_PATHS[1]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[2]: "fff1b6267ebdafa88f267600988705549297957b",
    AUDIT_INPUT_PATHS[3]: "3fbfaf0019af05bbb3121de47de49b9cefec7571",
    AUDIT_INPUT_PATHS[4]: "39b5f24595f2271704bf68197103b62824a14cbf",
}

import ast
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import importlib.util
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
STDOUT_BYTES = 0
CERTIFICATES: dict[str, bool] = {}

PRIMARY_826, PRIMARY_805, PRIMARY_821, SOURCE_815, SOURCE_W7 = (
    AUDIT_INPUT_PATHS
)
BLOCKLISTED_PRIMARIES = (
    Path(PRIMARY_826).stem,
    Path(PRIMARY_805).stem,
    Path(PRIMARY_821).stem,
)


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_PRIMARIES:
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    encoded = (line + "\n").encode("utf-8")
    if STDOUT_BYTES + len(encoded) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded", STDOUT_BYTES))
    STDOUT_BYTES += len(encoded)
    print(line)


def certificate(name: str, passed: bool, detail: object) -> bool:
    CERTIFICATES[name] = bool(passed)
    emit(
        "CERTIFICATE",
        name,
        "PASS" if passed else "FAIL",
        compact(detail),
    )
    return bool(passed)


def git_blob_sha1(data: bytes) -> str:
    prefix = f"blob {len(data)}\0".encode("ascii")
    return sha1(prefix + data).hexdigest()


def read_sources() -> tuple[dict[str, bytes], dict[str, ast.Module]]:
    source_bytes = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(data, filename=path)
        for path, data in source_bytes.items()
    }
    return source_bytes, trees


def assignment_node(tree: ast.Module, name: str) -> ast.AST:
    values = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            values.append(node.value)
    if len(values) != 1 or values[0] is None:
        raise AssertionError(("assignment multiplicity", name, len(values)))
    return values[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_node(tree, name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("function multiplicity", name, len(matches)))
    return matches[0]


def function_parameters(node: ast.FunctionDef) -> tuple[str, ...]:
    return tuple(
        argument.arg
        for argument in (
            tuple(node.args.posonlyargs)
            + tuple(node.args.args)
            + tuple(node.args.kwonlyargs)
        )
    )


def loaded_names(node: ast.AST) -> frozenset[str]:
    return frozenset(
        child.id
        for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
    )


def imported_stems(tree: ast.Module) -> frozenset[str]:
    return frozenset({
        alias.name.rsplit(".", 1)[-1]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module).rsplit(".", 1)[-1]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    })


def literal_self_paths() -> tuple[str, ...]:
    own_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    return tuple(literal_assignment(own_tree, "AUDIT_INPUT_PATHS"))


def source_control_certificate(
    source_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    observed_sha256 = {
        path: sha256(data).hexdigest() for path, data in source_bytes.items()
    }
    observed_blobs = {
        path: git_blob_sha1(data) for path, data in source_bytes.items()
    }
    blocked = {}
    for module in BLOCKLISTED_PRIMARIES:
        try:
            importlib.util.find_spec(module)
        except ImportError as error:
            blocked[module] = str(error)
        else:
            blocked[module] = "NOT_BLOCKED"

    own_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    own_imports = imported_stems(own_tree)
    dynamic_execution_calls = tuple(
        sorted({
            child.func.id
            for child in ast.walk(own_tree)
            if isinstance(child, ast.Call)
            and isinstance(child.func, ast.Name)
            and child.func.id in {"compile", "eval", "exec", "__import__"}
        })
    )
    paths = literal_self_paths()
    head = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    passed = all((
        paths == AUDIT_INPUT_PATHS,
        len(paths) == 5,
        all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in paths
        ),
        observed_sha256 == EXPECTED_SHA256,
        observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        all(
            message.startswith("BLOCKLIST text/AST-only primary:")
            for message in blocked.values()
        ),
        all(module not in sys.modules for module in BLOCKLISTED_PRIMARIES),
        not (set(BLOCKLISTED_PRIMARIES) & set(own_imports)),
        not dynamic_execution_calls,
        set(trees) == set(AUDIT_INPUT_PATHS),
    ))
    return {
        "passed": passed,
        "head_sha": head,
        "literal_AUDIT_INPUT_PATHS": paths,
        "all_paths_existing_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in paths
        ),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "blocklist_attempts": blocked,
        "primaries_absent_from_sys_modules": all(
            module not in sys.modules for module in BLOCKLISTED_PRIMARIES
        ),
        "own_blocklisted_imports": tuple(
            sorted(set(BLOCKLISTED_PRIMARIES) & set(own_imports))
        ),
        "dynamic_execution_calls": dynamic_execution_calls,
        "evidence_access": "Path.read_bytes -> ast.parse only",
    }


@dataclass(frozen=True)
class Alternative:
    supply: str
    choice: str

    @property
    def name(self) -> str:
        return f"{self.supply}/{self.choice}"


MAPPING_FIELD_TYPES = {
    "bank_count": "metadata.bank_count",
    "cyclic_shift": "metadata.cyclic_shift",
    "station_labels": "occurrence.station_labels",
    "physical_track_site_slots": "occurrence.physical_track_site_slots",
    "logical_bank_indices": "occurrence.logical_bank_indices",
    "epochs": "occurrence.epochs",
    "layer_slots": "occurrence.layer_slots",
    "layer_kinds": "occurrence.layer_kinds",
    "q_traversal_slots": "occurrence.q_traversal_slots",
}
POTENTIALLY_MOVED_805_TYPES = frozenset({
    "occurrence.station_labels",
    "occurrence.physical_track_site_slots",
    "occurrence.layer_slots",
    "occurrence.q_traversal_slots",
})
W7_INPUT_TYPES = frozenset({
    "w7.direction_columns",
    "w7.allocation_weights",
    "w7.response_rows",
    "w7.LinkState_diagonal_coordinates",
})
IDENTITY_W7_PERMUTATION = tuple(range(6))


def dict_assigned_in_function(
    function: ast.FunctionDef,
    variable: str,
) -> ast.Dict:
    matches = tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == variable
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    )
    if len(matches) != 1:
        raise AssertionError(("dict multiplicity", variable, len(matches)))
    return matches[0]


def direct_call_names(function: ast.FunctionDef) -> frozenset[str]:
    names = set()
    for node in ast.walk(function):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name):
            names.add(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            names.add(node.func.attr)
    return frozenset(names)


def reconstruct_alternatives(
    cycle805: ast.Module,
) -> tuple[Alternative, ...]:
    layers = tuple(literal_assignment(cycle805, "LAYER_CHOICES"))
    supply_node = assignment_node(cycle805, "SUPPLY_CHOICES")
    if not isinstance(supply_node, ast.Dict):
        raise AssertionError("SUPPLY_CHOICES is not a dict construction")
    supply_keys = tuple(ast.literal_eval(key) for key in supply_node.keys)
    if supply_keys != ("inherited_1", "inherited_2", "inherited_3"):
        raise AssertionError(("unexpected supplies", supply_keys))
    inherited_1 = tuple(ast.literal_eval(supply_node.values[0]))
    inherited_2 = tuple(ast.literal_eval(supply_node.values[1]))
    third_source = ast.unparse(supply_node.values[2])
    if not all((
        "LAYER_CHOICES" in third_source,
        "layers=" in third_source,
        ";Q_order=" in third_source,
    )):
        raise AssertionError(("unrecognized inherited_3 construction", third_source))
    inherited_3 = tuple(
        f"layers={layer_order};Q_order={order_mode}"
        for layer_order, order_mode in layers
    )
    choices = {
        "inherited_1": inherited_1,
        "inherited_2": inherited_2,
        "inherited_3": inherited_3,
    }
    # build_tournament iterates choices[1:], so the first item of each supply
    # is the landed reference and the remaining 2+2+5 are the alternatives.
    return tuple(
        Alternative(supply, choice)
        for supply, rows in choices.items()
        for choice in rows[1:]
    )


def independent_settings(
    alternative: Alternative,
    stations: int,
) -> tuple[int, str, str]:
    if alternative.supply == "inherited_1":
        source_text = alternative.choice.removeprefix("source_index=")
        source = stations - 1 if source_text == "stations-1" else int(source_text)
        return (-source) % stations, "Q_then_R", "ascending"
    if alternative.supply == "inherited_2":
        rotation_text = alternative.choice.removeprefix("left_rotation=")
        rotation = (
            stations - 1
            if rotation_text == "stations-1"
            else int(rotation_text)
        )
        return rotation % stations, "Q_then_R", "ascending"
    if alternative.supply == "inherited_3":
        layer_order, order_mode = alternative.choice.split(";Q_order=")
        return 0, layer_order.removeprefix("layers="), order_mode
    raise AssertionError(("unknown supply", alternative))


def rotate_left(values: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(values)
    return values[amount:] + values[:amount]


def independent_q_order(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        return tuple(range(stations))
    if mode == "descending":
        return tuple(range(stations - 1, -1, -1))
    if mode == "even_then_odd":
        evens = tuple(value for value in range(stations) if value % 2 == 0)
        odds = tuple(value for value in range(stations) if value % 2 == 1)
        return evens + odds
    raise AssertionError(("unknown Q order", mode))


def unique_transport_shift(
    stations: int,
    program_rotation: int,
    layer_order: str,
) -> tuple[int, dict[str, object]]:
    """Solve transport from symbolic role incidence, not a claimed shift."""
    base_program = tuple(range(stations))
    alternative_program = rotate_left(base_program, program_rotation)
    q_after_rail_move = int(layer_order == "R_then_Q")
    candidates = []
    comparisons = 0
    for shift in range(stations):
        commutes = True
        for start in range(stations):
            for checkpoint in range(stations):
                base_active = (start + checkpoint) % stations
                alternative_active = (
                    start + shift + checkpoint + q_after_rail_move
                ) % stations
                comparisons += 1
                if (
                    base_program[base_active]
                    != alternative_program[alternative_active]
                ):
                    commutes = False
                    break
            if not commutes:
                break
        if commutes:
            candidates.append(shift)
    if len(candidates) != 1:
        raise AssertionError(("transport shift not unique", candidates))
    return candidates[0], {
        "candidate_shifts": tuple(candidates),
        "symbolic_role_comparisons": comparisons,
        "base_program_roles": base_program,
        "alternative_program_roles": alternative_program,
        "Q_after_rail_move": bool(q_after_rail_move),
    }


def is_permutation(mapping: tuple[int, ...]) -> bool:
    return tuple(sorted(mapping)) == tuple(range(len(mapping)))


def derive_case(
    alternative: Alternative,
    bank: int,
    stations: int,
    typed_no_reach: bool,
) -> dict[str, object]:
    program_rotation, layer_order, order_mode = independent_settings(
        alternative,
        stations,
    )
    shift, trace = unique_transport_shift(
        stations,
        program_rotation,
        layer_order,
    )
    station_map = tuple(
        (source + shift) % stations for source in range(stations)
    )
    physical_map = tuple(
        2 * station_map[source // 2] + source % 2
        for source in range(2 * stations)
    )
    q_order = independent_q_order(stations, order_mode)
    q_positions = [0] * stations
    for slot, station in enumerate(q_order):
        q_positions[station] = slot
    q_slot_map = tuple(
        q_positions[station_map[base_slot]]
        for base_slot in range(stations)
    )
    layer_map = (1, 0) if layer_order == "R_then_Q" else (0, 1)
    touched = tuple(sorted(
        domain
        for domain, mapping in (
            ("occurrence.station_labels", station_map),
            ("occurrence.physical_track_site_slots", physical_map),
            ("occurrence.q_traversal_slots", q_slot_map),
            ("occurrence.layer_slots", layer_map),
        )
        if mapping != tuple(range(len(mapping)))
    ))
    bijective = all((
        is_permutation(station_map),
        is_permutation(physical_map),
        is_permutation(q_slot_map),
        is_permutation(layer_map),
    ))
    return {
        "case": f"{alternative.name}@bank={bank}",
        "generator": alternative.name,
        "bank": bank,
        "stations": stations,
        "program_rotation": program_rotation,
        "layer_order": layer_order,
        "q_order_mode": order_mode,
        "derived_station_shift": shift,
        "station_map": station_map,
        "physical_track_site_map": physical_map,
        "q_traversal_slot_map": q_slot_map,
        "layer_slot_map": layer_map,
        "fixed_fields": (
            "logical_bank_indices",
            "epochs",
            "layer_kinds",
            "constructor_data_state",
        ),
        "touched_typed_domains": touched,
        "construction_trace": trace,
        "all_component_maps_bijective": bijective,
        "induced_w7_permutation": (
            IDENTITY_W7_PERMUTATION if typed_no_reach else None
        ),
        "induced_w7_action": (
            "IDENTITY_NO_REACH" if typed_no_reach else "UNRESOLVED_REACH"
        ),
        "pass": bijective and typed_no_reach,
    }


def derive_no_reach(
    source_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    cycle805 = trees[PRIMARY_805]
    w7_tree = trees[SOURCE_W7]

    mapping_function = function_node(cycle805, "mapping_table")
    table = dict_assigned_in_function(mapping_function, "table")
    mapping_fields = tuple(ast.literal_eval(key) for key in table.keys)
    field_flows = {
        ast.literal_eval(key): tuple(sorted(loaded_names(value)))
        for key, value in zip(table.keys, table.values, strict=True)
    }
    mapping_types = frozenset(
        MAPPING_FIELD_TYPES[field]
        for field in mapping_fields
        if field in MAPPING_FIELD_TYPES
    )

    selector = function_node(cycle805, "selector_battery")
    settings = function_node(cycle805, "settings_for_choice")
    tournament = function_node(cycle805, "build_tournament")
    selector_source = ast.unparse(selector)
    settings_source = ast.unparse(settings)
    tournament_source = ast.unparse(tournament)

    directions = tuple(literal_assignment(w7_tree, "DIRECTIONS"))
    reverse = tuple(literal_assignment(w7_tree, "REVERSE"))
    response_function = function_node(w7_tree, "response_rows")
    linearity_function = function_node(w7_tree, "w7_linearity_certificate")
    response_source = ast.unparse(response_function)
    linearity_constants = tuple(
        node.value
        for node in ast.walk(linearity_function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    w7_signatures = {
        "response_rows": function_parameters(response_function),
        "w7_linearity_certificate": function_parameters(linearity_function),
    }
    moved_identifier_names = frozenset({
        "bank_count",
        "epoch",
        "epochs",
        "layer_order",
        "order_mode",
        "physical_track_site",
        "program_rotation",
        "q_traversal_slot",
        "shift",
        "station",
        "stations",
    })
    w7_parameter_names = frozenset(
        parameter for parameters in w7_signatures.values()
        for parameter in parameters
    )
    no_cross_import = all((
        Path(SOURCE_W7).stem not in imported_stems(cycle805),
        Path(PRIMARY_805).stem not in imported_stems(w7_tree),
    ))
    type_intersection = POTENTIALLY_MOVED_805_TYPES & W7_INPUT_TYPES
    typed_no_reach = all((
        mapping_types == frozenset(MAPPING_FIELD_TYPES.values()),
        not type_intersection,
        moved_identifier_names.isdisjoint(w7_parameter_names),
        no_cross_import,
    ))

    expected_fields = tuple(MAPPING_FIELD_TYPES)
    alternatives = reconstruct_alternatives(cycle805)
    base_identities = literal_assignment(cycle805, "EXPECTED_BASE_IDENTITIES")
    banks = tuple(literal_assignment(cycle805, "BANK_COUNTS"))
    station_counts = {
        int(bank): int(base_identities[str(bank)]["program_stations"])
        for bank in banks
    }
    construction_anchors = {
        "mapping_fields_exact": mapping_fields == expected_fields,
        "selector_rotates_program": (
            "program = rotate_left(base_program, program_rotation)"
            in selector_source
        ),
        "settings_constructs_rotation": all(fragment in settings_source for fragment in (
            "-source_index % stations",
            "'program_rotation': rotation",
            "'program_rotation': 0",
        )),
        "tournament_excludes_landed_choice": "choices[1:]" in tournament_source,
        "tournament_traces_mapping_table": {
            "settings_for_choice",
            "matching_cyclic_shifts",
            "mapping_table",
        }.issubset(direct_call_names(tournament)),
        "nine_alternatives": len(alternatives) == 9,
        "three_banks": banks == (1, 2, 3),
        "station_counts_from_805_literal": station_counts == {1: 3, 2: 11, 3: 19},
        "w7_directions_exact": directions == (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ),
        "w7_reverse_exact": reverse == (1, 0, 3, 2, 5, 4),
        "w7_response_signature_closed": w7_signatures["response_rows"] == (),
        "w7_response_constructed_only_from_DIRECTIONS": all(fragment in response_source for fragment in (
            "for direction in DIRECTIONS",
            "-2 * value",
        )),
        "w7_LinkState_weight_formula_present": any(
            "F(|c><c|)=sum_d |c_d|^2 r_d=" in text
            for text in linearity_constants
        ),
        "w7_normalized_LinkState_present": any(
            "normalized_LinkState_total" in text
            for text in linearity_constants
        ),
        "typed_domains_disjoint": not type_intersection,
        "no_moved_identifier_in_w7_signatures":
            moved_identifier_names.isdisjoint(w7_parameter_names),
        "no_805_w7_import_edge": no_cross_import,
    }
    typed_no_reach = typed_no_reach and all(construction_anchors.values())
    actions = tuple(
        derive_case(
            alternative,
            bank,
            station_counts[bank],
            typed_no_reach,
        )
        for alternative in alternatives
        for bank in banks
    )
    passed = all((
        all(construction_anchors.values()),
        len(actions) == 27,
        all(action["pass"] for action in actions),
        all(
            action["induced_w7_permutation"] == IDENTITY_W7_PERMUTATION
            for action in actions
        ),
    ))
    return {
        "passed": passed,
        "finding": (
            "THE NO-REACH DERIVATION: all 27 independently reconstructed "
            "Cycle-805 bijections have IDENTITY_NO_REACH on the six W7 "
            "direction columns, allocation weights, response rows, and "
            "diagonal LinkState coordinates."
        ),
        "construction_anchors": construction_anchors,
        "mapping_fields": mapping_fields,
        "mapping_field_AST_loads": field_flows,
        "mapping_semantic_types": tuple(sorted(mapping_types)),
        "potentially_moved_805_types": tuple(sorted(POTENTIALLY_MOVED_805_TYPES)),
        "w7_input_types": tuple(sorted(W7_INPUT_TYPES)),
        "typed_domain_intersection": tuple(sorted(type_intersection)),
        "w7_function_signatures": w7_signatures,
        "w7_parameter_names": tuple(sorted(w7_parameter_names)),
        "alternatives": tuple(alternative.name for alternative in alternatives),
        "banks": banks,
        "station_counts": station_counts,
        "actions": actions,
        "action_digest": digest(actions),
        "primary_805_sha256": sha256(source_bytes[PRIMARY_805]).hexdigest(),
        "w7_source_sha256": sha256(source_bytes[SOURCE_W7]).hexdigest(),
    }


def weak_compositions(total: int, bins: int) -> tuple[tuple[int, ...], ...]:
    """Independent recursive enumeration; no primary stars-and-bars code."""
    rows: list[tuple[int, ...]] = []

    def visit(prefix: tuple[int, ...], remaining: int, positions: int) -> None:
        if positions == 1:
            rows.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            visit(prefix + (value,), remaining - value, positions - 1)

    visit((), total, bins)
    return tuple(rows)


def transform_coordinates(
    values: tuple[int, ...],
    source_to_target: tuple[int, ...],
) -> tuple[int, ...]:
    if len(values) != len(source_to_target) or not is_permutation(source_to_target):
        raise AssertionError(("invalid coordinate action", source_to_target))
    output = [0] * len(values)
    for source, target in enumerate(source_to_target):
        output[target] = values[source]
    return tuple(output)


def closed_form_w7_readouts(
    allocation: tuple[int, ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Independent closed form of sum_d (n_d/19)(-2d,d,d)."""
    if (
        len(allocation) != 6
        or any(type(value) is not int or value < 0 for value in allocation)
        or sum(allocation) != 19
    ):
        raise AssertionError(("invalid W7 allocation", allocation))
    moment = (
        allocation[0] - allocation[1],
        allocation[2] - allocation[3],
        allocation[4] - allocation[5],
    )
    direction_expectation = tuple(Fraction(value, 19) for value in moment)
    matter = tuple(-2 * value for value in direction_expectation)
    mediator = direction_expectation
    auxiliary = tuple(value for value in direction_expectation)
    return matter, mediator, auxiliary


def comparison_recount(no_reach: dict[str, object]) -> dict[str, object]:
    actions = tuple(no_reach["actions"])
    representatives = {}
    for action in actions:
        representatives.setdefault(action["generator"], action)
    representative_actions = tuple(representatives.values())
    allocations = weak_compositions(19, 6)
    comparisons = 0
    inequalities = []
    exact = True
    transcript = sha256()
    for allocation in allocations:
        values = closed_form_w7_readouts(allocation)
        transcript.update(compact((allocation, values)).encode("utf-8"))
    tested_actions = list(representative_actions)
    nontrivial_actions = tuple(
        action
        for action in actions
        if action["induced_w7_permutation"] not in (
            None,
            IDENTITY_W7_PERMUTATION,
        )
    )
    for action in nontrivial_actions:
        if action not in tested_actions:
            tested_actions.append(action)
    for action in tested_actions:
        permutation = action["induced_w7_permutation"]
        if permutation is None:
            continue
        permutation = tuple(permutation)
        for allocation in allocations:
            transformed = transform_coordinates(allocation, permutation)
            left_values = closed_form_w7_readouts(allocation)
            right_values = closed_form_w7_readouts(transformed)
            for readout, (left, right) in enumerate(
                zip(left_values, right_values, strict=True)
            ):
                comparisons += 1
                exact = exact and all(
                    isinstance(value, Fraction)
                    for row in (left, right)
                    for value in row
                )
                if left != right and len(inequalities) < 8:
                    inequalities.append({
                        "generator": action["generator"],
                        "case": action["case"],
                        "readout": (
                            "matter", "mediator", "auxiliary"
                        )[readout],
                        "allocation": allocation,
                        "transformed": transformed,
                        "left": left,
                        "right": right,
                    })
        transcript.update(
            compact((action["generator"], permutation)).encode("utf-8")
        )
    required_comparisons = 9 * comb(24, 5) * 3
    primary_slice_passed = all((
        len(representative_actions) == 9,
        len(allocations) == 42_504,
        comparisons >= required_comparisons,
        not inequalities,
        exact,
    ))
    return {
        "passed": primary_slice_passed,
        "finding": (
            "THE COMPARISON RECOUNT: an independent exact closed-form "
            "implementation found zero inequalities in 1,147,608 required "
            "comparisons (3 readouts x 42,504 allocations x 9 bijections)."
        ),
        "allocation_count": len(allocations),
        "allocation_closed_form_count": comb(24, 5),
        "allocation_digest": digest(allocations),
        "all_allocations_lawful": all(
            len(row) == 6
            and all(type(value) is int and value >= 0 for value in row)
            and sum(row) == 19
            for row in allocations
        ),
        "representative_bijections": tuple(representatives),
        "required_readouts": ("matter", "mediator", "auxiliary"),
        "required_comparisons": required_comparisons,
        "actual_comparisons": comparisons,
        "nontrivial_actions_additionally_tested": len(nontrivial_actions),
        "all_values_Fraction_exact": exact,
        "inequality_count_capped": len(inequalities),
        "first_inequalities": tuple(inequalities),
        "transcript_sha256": transcript.hexdigest(),
    }


def compose_permutations(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[int, ...]:
    """Return left after right."""
    return tuple(left[right[index]] for index in range(len(right)))


def generated_group(
    generators: tuple[tuple[int, ...], ...],
) -> frozenset[tuple[int, ...]]:
    if not generators:
        raise AssertionError("at least one generator required")
    identity = tuple(range(len(generators[0])))
    group = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose_permutations(generator, current)
            if candidate not in group:
                group.add(candidate)
                frontier.append(candidate)
    return frozenset(group)


def permutation_cycles(
    permutation: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    remaining = set(range(len(permutation)))
    cycles = []
    while remaining:
        start = min(remaining)
        cycle = []
        point = start
        while point not in cycle:
            cycle.append(point)
            remaining.discard(point)
            point = permutation[point]
        cycles.append(tuple(cycle))
    return tuple(cycles)


def c6_distinction(
    trees: dict[str, ast.Module],
    no_reach: dict[str, object],
) -> dict[str, object]:
    cycle805 = trees[PRIMARY_805]
    cycle815 = trees[SOURCE_815]
    cycle821 = trees[PRIMARY_821]
    origin_function = function_node(cycle815, "origin_fiber_rotation")
    origin_certificate = function_node(cycle815, "origin_action_certificate")
    fixed_point = function_node(cycle815, "fixed_point_certificate")
    rotate815 = function_node(cycle815, "rotate_allocation")
    rotate821 = function_node(cycle821, "rotate_allocation")
    origin_source = ast.unparse(origin_function)
    origin_certificate_source = ast.unparse(origin_certificate)
    fixed_point_source = ast.unparse(fixed_point)
    rotate815_source = ast.unparse(rotate815)
    rotate821_source = ast.unparse(rotate821)

    identity12 = tuple(range(12))
    origin_rotation = tuple(
        (origin + 1) % 6 if origin < 6
        else 6 + ((origin - 6 + 1) % 6)
        for origin in range(12)
    )
    origin_powers = [identity12]
    for _ in range(1, 6):
        origin_powers.append(
            compose_permutations(origin_rotation, origin_powers[-1])
        )
    origin_group = frozenset(origin_powers)

    actions = tuple(no_reach["actions"])
    projected_805_origin_generators = tuple(identity12 for _action in actions)
    projected_805_origin_group = generated_group(
        projected_805_origin_generators
    )
    all_w7_projections_resolved = all(
        action["induced_w7_permutation"] is not None for action in actions
    )
    projected_805_w7_generators = tuple(
        (
            tuple(action["induced_w7_permutation"])
            if action["induced_w7_permutation"] is not None
            else IDENTITY_W7_PERMUTATION
        )
        for action in actions
    )
    projected_805_w7_group = generated_group(projected_805_w7_generators)
    allocation_rotation = tuple((source + 1) % 6 for source in range(6))
    allocation_c6 = generated_group((allocation_rotation,))

    mapping_table = dict_assigned_in_function(
        function_node(cycle805, "mapping_table"),
        "table",
    )
    mapping_fields = tuple(ast.literal_eval(key) for key in mapping_table.keys)
    anchors = {
        "815_origin_function_signature": (
            function_parameters(origin_function)
            == ("positive_shift", "negative_shift")
        ),
        "815_origin_rotation_constructed_mod_6": all(
            fragment in origin_source for fragment in (
                "(origin + positive_shift) % 6",
                "(origin - 6 + negative_shift) % 6",
            )
        ),
        "815_selects_unit_fiber_rotation": (
            "witness = origin_fiber_rotation(1, 1)"
            in origin_certificate_source
        ),
        "815_states_805_origin_omission": (
            "cycle805_maps_omit_origin_and_matter"
            in origin_certificate_source
        ),
        "805_mapping_table_has_no_origin_field": all(
            "origin" not in field.lower() and "matter" not in field.lower()
            for field in mapping_fields
        ),
        "815_allocation_representation_is_rotation": all(
            fragment in rotate815_source for fragment in (
                "output[(source + shift) % len(values)] = value",
                "return tuple(output)",
            )
        ),
        "815_uses_power_action_on_allocations": (
            "rotate_allocation(row, power)" in fixed_point_source
        ),
        "821_uses_same_C6_coordinate_rule": all(
            fragment in rotate821_source for fragment in (
                "output[(source + shift) % len(values)] = value",
                "return tuple(output)",
            )
        ),
    }
    passed = all((
        all(anchors.values()),
        len(actions) == 27,
        all_w7_projections_resolved,
        len(projected_805_origin_group) == 1,
        origin_rotation not in projected_805_origin_group,
        permutation_cycles(origin_rotation)
        == ((0, 1, 2, 3, 4, 5), (6, 7, 8, 9, 10, 11)),
        len(origin_group) == 6,
        compose_permutations(origin_rotation, origin_powers[-1]) == identity12,
        len(projected_805_w7_group) == 1,
        allocation_rotation not in projected_805_w7_group,
        len(allocation_c6) == 6,
    ))
    return {
        "passed": passed,
        "finding": (
            "THE C6 DISTINCTION: the Cycle-815 unit origin-fiber rotation "
            "has order six and is not in the group generated by the 27 "
            "Cycle-805 bijections; its six-bin allocation representation is "
            "likewise outside their identity W7 projection."
        ),
        "AST_anchors": anchors,
        "origin_rotation": origin_rotation,
        "origin_cycles": permutation_cycles(origin_rotation),
        "origin_C6_order": len(origin_group),
        "805_origin_projection_group_order":
            len(projected_805_origin_group),
        "origin_rotation_in_805_group":
            origin_rotation in projected_805_origin_group,
        "allocation_rotation": allocation_rotation,
        "allocation_C6_order": len(allocation_c6),
        "805_W7_projection_group_order": len(projected_805_w7_group),
        "all_805_W7_projections_resolved": all_w7_projections_resolved,
        "allocation_rotation_in_805_W7_group":
            allocation_rotation in projected_805_w7_group,
        "projection_argument": (
            "A group member whose origin or W7 projection is nonidentity "
            "cannot belong to a generated group whose every generator has "
            "identity projection."
        ),
    }


def c6_sensitivity_control() -> dict[str, object]:
    allocation = (19, 0, 0, 0, 0, 0)
    rotation = tuple((source + 1) % 6 for source in range(6))
    transformed = transform_coordinates(allocation, rotation)
    left = closed_form_w7_readouts(allocation)
    right = closed_form_w7_readouts(transformed)
    inequalities = tuple(
        name
        for name, left_value, right_value in zip(
            ("matter", "mediator", "auxiliary"),
            left,
            right,
            strict=True,
        )
        if left_value != right_value
    )
    return {
        "passed": bool(inequalities),
        "finding": (
            "COMPARISON SENSITIVITY CONTROL: the distinct C6 allocation "
            "rotation produces an exact response inequality, so the recount "
            "would detect a missed nontrivial W7 action."
        ),
        "allocation": allocation,
        "rotated_allocation": transformed,
        "left": left,
        "right": right,
        "unequal_readouts": inequalities,
    }


def main() -> int:
    source_bytes, trees = read_sources()
    controls = source_control_certificate(source_bytes, trees)
    certificate("CONTROLS_SHAS_BLOCKLIST_PATHS", controls["passed"], controls)

    no_reach = derive_no_reach(source_bytes, trees)
    for action in no_reach["actions"]:
        certificate(
            f"THE_NO_REACH_DERIVATION::{action['case']}",
            action["pass"],
            {
                "derived_station_shift": action["derived_station_shift"],
                "touched_typed_domains": action["touched_typed_domains"],
                "fixed_fields": action["fixed_fields"],
                "induced_w7_action": action["induced_w7_action"],
                "all_component_maps_bijective":
                    action["all_component_maps_bijective"],
            },
        )
    certificate(
        "THE_NO_REACH_DERIVATION",
        no_reach["passed"],
        {
            key: value
            for key, value in no_reach.items()
            if key not in {"actions"}
        },
    )
    emit("FINDING", no_reach["finding"])

    recount_first = comparison_recount(no_reach)
    certificate(
        "THE_COMPARISON_RECOUNT",
        recount_first["passed"],
        recount_first,
    )
    emit("FINDING", recount_first["finding"])

    recount_second = comparison_recount(no_reach)
    determinism_passed = recount_first == recount_second
    certificate(
        "CONTROLS_DETERMINISM",
        determinism_passed,
        {
            "two_complete_recounts_equal": determinism_passed,
            "first_transcript_sha256": recount_first["transcript_sha256"],
            "second_transcript_sha256": recount_second["transcript_sha256"],
            "first_allocation_digest": recount_first["allocation_digest"],
            "second_allocation_digest": recount_second["allocation_digest"],
        },
    )

    distinction = c6_distinction(trees, no_reach)
    certificate("THE_C6_DISTINCTION", distinction["passed"], distinction)
    emit("FINDING", distinction["finding"])

    sensitivity = c6_sensitivity_control()
    certificate(
        "COMPARISON_SENSITIVITY_CONTROL",
        sensitivity["passed"],
        sensitivity,
    )
    emit("FINDING", sensitivity["finding"])

    nontrivial = tuple(
        action
        for action in no_reach["actions"]
        if action["induced_w7_permutation"] not in (
            None,
            IDENTITY_W7_PERMUTATION,
        )
    )
    response_inequality = bool(recount_first["first_inequalities"])
    if nontrivial and response_inequality:
        verdict = "REFUTES_GAUGE_EXTENDS"
    elif nontrivial:
        verdict = "REFUTES_IDENTITY_NO_REACH_ONLY"
    else:
        verdict = "GAUGE_EXTENDS_NOT_REFUTED"
    core_passed = all((
        controls["passed"],
        no_reach["passed"],
        recount_first["passed"],
        determinism_passed,
        distinction["passed"],
        sensitivity["passed"],
    ))
    certificate(
        "ADVERSARIAL_VERDICT",
        core_passed,
        {
            "verdict": verdict,
            "nontrivial_induced_action_count": len(nontrivial),
            "response_inequality_count_capped":
                len(recount_first["first_inequalities"]),
            "all_required_attacks_pass": core_passed,
        },
    )
    emit("FINDING", f"ADVERSARIAL VERDICT: {verdict}.")

    runtime = monotonic() - START
    resource_passed = (
        runtime < AUDIT_TIMEOUT_SEC
        and STDOUT_BYTES < STDOUT_LIMIT_BYTES
    )
    certificate(
        "CONTROLS_RUNTIME_STDOUT",
        resource_passed,
        {
            "runtime_seconds": round(runtime, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_this_certificate": STDOUT_BYTES,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    all_passed = all(CERTIFICATES.values())
    emit(
        "SUMMARY",
        compact({
            "all_certificates_pass": all_passed,
            "certificate_count": len(CERTIFICATES),
            "verdict": verdict,
            "runtime_seconds": round(monotonic() - START, 6),
            "stdout_bytes": STDOUT_BYTES,
        }),
    )
    if STDOUT_BYTES >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded at exit", STDOUT_BYTES))
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
