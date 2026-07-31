#!/usr/bin/env python3
"""Cycle 826: response surface versus the Cycle-805 relabeling group.

The Cycle-805/808/821 primaries and the six landed W7 sources are SHA-pinned,
text/AST-only inputs.  This runner never imports or executes them.  It
reimplements the 27 primary-bank relabeling cases and the exact W7 response.

The central type check is deliberately explicit.  Cycle 805/808 moves
controller station, physical-track, Q-traversal, and sometimes layer-slot
labels while fixing bank, epoch, occurrence direction, orientation, and the
constructor data state.  W7 consumes a separate ordered six-column direction
family and its six allocation weights.  There is no source-side map from an
805 moved domain to either W7 object, so every induced W7 action is identity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
BASE_HEAD_SHA = "37c7afd1837dc68de4e9686910e74c18a7391c4b"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP14-20260729"

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle821_orbit_observability_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[1]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[2]:
        "36273e2f13c26803d7a28bb65a3efce0aab82c766e4dc039d8269f0d53973342",
    AUDIT_INPUT_PATHS[3]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[4]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[5]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[6]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[7]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[8]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[1]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[2]: "fff1b6267ebdafa88f267600988705549297957b",
    AUDIT_INPUT_PATHS[3]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[4]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[5]: "52abfe3dd54b3969f51ca6816ec4830b42405106",
    AUDIT_INPUT_PATHS[6]: "6bde2222ddfdaf48e3806c0ac0a9c9d6431d945f",
    AUDIT_INPUT_PATHS[7]: "8366a5240d992376d0396a6fdc2c0b33247e8aba",
    AUDIT_INPUT_PATHS[8]: "39b5f24595f2271704bf68197103b62824a14cbf",
}

from dataclasses import dataclass
import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
STDOUT_BYTES = 0
CHECKS: dict[str, bool] = {}
PRIMARY_PATHS = AUDIT_INPUT_PATHS[:3]
W7_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _SourceBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST text/AST-only source: {fullname}")
        return None


SOURCE_BLOCKER = _SourceBlocker()
sys.meta_path.insert(0, SOURCE_BLOCKER)


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
    STDOUT_BYTES += len(encoded)
    if STDOUT_BYTES >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded", STDOUT_BYTES))
    print(line)


def check(label: str, condition: bool, detail: object) -> bool:
    CHECKS[label] = bool(condition)
    emit(
        "CERTIFICATE",
        label,
        "PASS" if condition else "FAIL",
        compact(detail),
    )
    return bool(condition)


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(rows) != 1:
        raise AssertionError(("function multiplicity", name, len(rows)))
    return rows[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_node(tree, name))


def assignment_node(tree: ast.Module, name: str) -> ast.AST:
    rows = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            rows.append(node.value)
    if len(rows) != 1 or rows[0] is None:
        raise AssertionError(("assignment multiplicity", name, len(rows)))
    return rows[0]


def literal_self_paths() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    return tuple(literal_assignment(tree, "AUDIT_INPUT_PATHS"))


def subprocess_text(*command: str) -> str:
    return subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def source_controls(
    input_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    observed_sha256 = {
        path: sha256(data).hexdigest() for path, data in input_bytes.items()
    }
    observed_blobs = {
        path: git_blob_sha1(data) for path, data in input_bytes.items()
    }
    blocked_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.util.find_spec(module)
        except ImportError as error:
            blocked_attempts[module] = str(error)
        else:
            blocked_attempts[module] = "NOT_BLOCKED"

    own_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    imported = {
        alias.name.rsplit(".", 1)[-1]
        for node in ast.walk(own_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module).rsplit(".", 1)[-1]
        for node in ast.walk(own_tree)
        if isinstance(node, ast.ImportFrom)
    }
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", BASE_HEAD_SHA, "HEAD"),
        cwd=ROOT,
        check=False,
        capture_output=True,
    ).returncode == 0
    return {
        "head_sha": subprocess_text("git", "rev-parse", "HEAD"),
        "branch": subprocess_text("git", "branch", "--show-current"),
        "base_is_ancestor": base_is_ancestor,
        "literal_paths": literal_self_paths(),
        "paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "parsed_source_count": len(trees),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "blocked_attempts": blocked_attempts,
        "blocklist_pass": all(
            text.startswith("BLOCKLIST text/AST-only source:")
            for text in blocked_attempts.values()
        ),
        "none_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "no_blocklisted_AST_import": not (
            set(BLOCKLISTED_MODULES) & imported
        ),
    }


@dataclass(frozen=True)
class GeneratorSpec:
    name: str
    supply: str
    choice: str
    rotation: int
    layer_order: str
    order_mode: str


GENERATOR_SPECS = (
    GeneratorSpec(
        "I1_SOURCE_1", "inherited_1", "source_index=1",
        -1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I1_SOURCE_LAST", "inherited_1", "source_index=stations-1",
        1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I2_ROTATE_1", "inherited_2", "left_rotation=1",
        1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I2_ROTATE_LAST", "inherited_2", "left_rotation=stations-1",
        -1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I3_Q_THEN_R_DESCENDING", "inherited_3",
        "layers=Q_then_R;Q_order=descending",
        0, "Q_then_R", "descending",
    ),
    GeneratorSpec(
        "I3_Q_THEN_R_EVEN_THEN_ODD", "inherited_3",
        "layers=Q_then_R;Q_order=even_then_odd",
        0, "Q_then_R", "even_then_odd",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_ASCENDING", "inherited_3",
        "layers=R_then_Q;Q_order=ascending",
        0, "R_then_Q", "ascending",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_DESCENDING", "inherited_3",
        "layers=R_then_Q;Q_order=descending",
        0, "R_then_Q", "descending",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_EVEN_THEN_ODD", "inherited_3",
        "layers=R_then_Q;Q_order=even_then_odd",
        0, "R_then_Q", "even_then_odd",
    ),
)
BANK_STATIONS = ((1, 3), (2, 11), (3, 19))


def q_positions(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        order = tuple(range(stations))
    elif mode == "descending":
        order = tuple(reversed(range(stations)))
    elif mode == "even_then_odd":
        order = (
            tuple(range(0, stations, 2))
            + tuple(range(1, stations, 2))
        )
    else:
        raise ValueError(mode)
    positions = [0] * stations
    for slot, station in enumerate(order):
        positions[station] = slot
    return tuple(positions)


def action_row(
    spec: GeneratorSpec,
    bank: int,
    stations: int,
) -> dict[str, object]:
    rotation = spec.rotation % stations
    phase = int(spec.layer_order == "R_then_Q")
    station_shift = (-spec.rotation - phase) % stations
    station_map = tuple(
        (station + station_shift) % stations
        for station in range(stations)
    )
    q_position = q_positions(stations, spec.order_mode)
    q_slots = tuple(
        q_position[(station - rotation) % stations]
        for station in range(stations)
    )
    return {
        "case": f"{spec.name}@bank={bank}",
        "generator": spec.name,
        "supply": spec.supply,
        "choice": spec.choice,
        "bank": bank,
        "stations": stations,
        "occurrence_action": {
            "station_shift": station_shift,
            "station_map": station_map,
            "physical_track_site_map": tuple(
                2 * ((site // 2 + station_shift) % stations) + site % 2
                for site in range(2 * stations)
            ),
            "q_traversal_slot_map": q_slots,
            "layer_slot_map": (phase, 1 ^ phase),
            "logical_bank": "FIXED",
            "epoch": "FIXED",
            "occurrence_direction": "FIXED",
            "orientation": "FIXED",
            "constructor_data_state": "IDENTITY",
        },
        "w7_input_action": "IDENTITY_NO_REACH",
        "w7_fixed_objects": (
            "six direction-column labels",
            "six allocation weights",
            "fixed response rows",
            "normalized diagonal LinkState weights",
        ),
        "reason": (
            "805/808 maps only station/track/Q/layer labels; no map targets "
            "a W7 direction column, allocation weight, response row, or "
            "LinkState coordinate"
        ),
    }


def dict_keys_from_assignment(
    function: ast.FunctionDef,
    assignment_name: str,
) -> tuple[str, ...]:
    matches = tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == assignment_name
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    )
    if len(matches) != 1:
        raise AssertionError(
            ("dict assignment multiplicity", assignment_name, len(matches))
        )
    return tuple(
        str(ast.literal_eval(key))
        for key in matches[0].keys
        if key is not None
    )


def return_dict_keys(function: ast.FunctionDef) -> tuple[str, ...]:
    matches = tuple(
        node.value
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    )
    if len(matches) != 1:
        raise AssertionError(("return dict multiplicity", function.name))
    return tuple(
        str(ast.literal_eval(key))
        for key in matches[0].keys
        if key is not None
    )


def imported_module_stems(tree: ast.Module) -> set[str]:
    return {
        alias.name.rsplit(".", 1)[-1]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module).rsplit(".", 1)[-1]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }


W7_FUNCTIONAL_SOURCES = {
    W7_PATHS[0]: (
        "extract_frozen_fixtures",
        "evaluate_candidate",
    ),
    W7_PATHS[1]: (
        "derive_recoil_coefficients",
        "derive_response_kernel_candidate",
    ),
    W7_PATHS[2]: (
        "landed_defining_row",
        "row_diff",
    ),
    W7_PATHS[3]: (
        "defining_row",
        "weighted_rows",
        "response_from_probability_tensor",
    ),
    W7_PATHS[4]: (
        "declared_family",
        "landed_defining_rows",
    ),
    W7_PATHS[5]: (
        "response_rows",
        "w7_linearity_certificate",
    ),
}


def extract_w7_contract(
    input_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    citations = []
    for path, names in W7_FUNCTIONAL_SOURCES.items():
        for name in names:
            node = named_function(trees[path], name)
            citations.append(
                (
                    path,
                    name,
                    node.lineno,
                    sha256(
                        ast.dump(
                            node,
                            annotate_fields=True,
                            include_attributes=False,
                        ).encode("utf-8")
                    ).hexdigest(),
                    tuple(
                        argument.arg
                        for argument in (
                            tuple(node.args.posonlyargs)
                            + tuple(node.args.args)
                            + tuple(node.args.kwonlyargs)
                        )
                    ),
                )
            )

    cycle778 = trees[W7_PATHS[4]]
    prediction_source = literal_assignment(cycle778, "PREDICTION_SOURCE")
    if not isinstance(prediction_source, str):
        raise AssertionError("PREDICTION_SOURCE is not literal text")
    prediction_tree = ast.parse(
        prediction_source,
        filename=f"{W7_PATHS[4]}::PREDICTION_SOURCE",
    )
    embedded_citations = []
    for name in ("add_response_rows", "predict_full_family"):
        node = named_function(prediction_tree, name)
        embedded_citations.append(
            (
                f"{W7_PATHS[4]}::PREDICTION_SOURCE",
                name,
                node.lineno,
                sha256(
                    ast.dump(
                        node,
                        annotate_fields=True,
                        include_attributes=False,
                    ).encode("utf-8")
                ).hexdigest(),
                tuple(argument.arg for argument in node.args.args),
            )
        )

    cycle812 = trees[W7_PATHS[5]]
    directions_raw = literal_assignment(cycle812, "DIRECTIONS")
    reverse_raw = literal_assignment(cycle812, "REVERSE")
    directions = tuple(
        tuple(int(value) for value in direction)
        for direction in directions_raw
    )
    reverse = tuple(int(value) for value in reverse_raw)
    rows = tuple(
        (
            tuple(-2 * Fraction(value) for value in direction),
            tuple(Fraction(value) for value in direction),
            tuple(Fraction(value) for value in direction),
        )
        for direction in directions
    )
    response_source = ast.unparse(named_function(cycle812, "response_rows"))
    add_source = ast.unparse(
        named_function(prediction_tree, "add_response_rows")
    )
    predict_source = ast.unparse(
        named_function(prediction_tree, "predict_full_family")
    )
    cycle812_text = input_bytes[W7_PATHS[5]].decode("utf-8")
    passed = (
        directions
        == (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
        and reverse == (1, 0, 3, 2, 5, 4)
        and all(
            directions[reverse[index]]
            == tuple(-value for value in direction)
            for index, direction in enumerate(directions)
        )
        and "for direction in DIRECTIONS" in response_source
        and "-2 * value" in response_source
        and "sum(" in add_source
        and "for row in rows" in add_source
        and (
            'member["channels"]' in predict_source
            or "member['channels']" in predict_source
        )
        and "composition_row = add_response_rows(input_rows)" in predict_source
        and "normalized_LinkState_total" in cycle812_text
        and "return U320.LinkState({ORIGIN: vector}, {})" in cycle812_text
        and len(citations) == 13
        and len(embedded_citations) == 2
    )
    return {
        "directions": directions,
        "reverse": reverse,
        "response_rows": rows,
        "functional_citations": tuple(citations),
        "embedded_prediction_citations": tuple(embedded_citations),
        "input_type": (
            "six nonnegative allocation weights n_d with sum 19; "
            "equivalently normalized diagonal W7 LinkState weights n_d/19"
        ),
        "readout_rule": (
            "unnormalized mixture sum_d n_d r_d and normalized expectation "
            "sum_d (n_d/19) r_d, with r_d=(-2d,d,d)"
        ),
        "passed": passed,
    }


def source_action_contract(
    input_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
    w7: dict[str, object],
) -> dict[str, object]:
    cycle805 = trees[PRIMARY_PATHS[0]]
    cycle808 = trees[PRIMARY_PATHS[1]]
    cycle821 = trees[PRIMARY_PATHS[2]]
    mapping_keys = set(
        dict_keys_from_assignment(
            named_function(cycle805, "mapping_table"),
            "table",
        )
    )
    bank_map_keys = set(
        return_dict_keys(named_function(cycle808, "spec_bank_maps"))
    )
    occurrence_source = ast.unparse(
        named_function(cycle808, "map_occurrence_by_g")
    )
    rotate_source = ast.unparse(
        named_function(cycle821, "rotate_allocation")
    )
    layers = tuple(literal_assignment(cycle805, "LAYER_CHOICES"))
    expected_choices = {
        ("inherited_1", "source_index=1"),
        ("inherited_1", "source_index=stations-1"),
        ("inherited_2", "left_rotation=1"),
        ("inherited_2", "left_rotation=stations-1"),
        *(
            (
                "inherited_3",
                f"layers={layer};Q_order={order}",
            )
            for layer, order in layers[1:]
        ),
    }
    reimplemented_choices = {
        (spec.supply, spec.choice) for spec in GENERATOR_SPECS
    }
    moved_805_domains = {
        "station_labels",
        "physical_track_site_slots",
        "q_traversal_slots",
        "layer_slots",
    }
    w7_input_domains = {
        "w7_direction_columns",
        "allocation_weights",
        "response_rows",
        "LinkState_coordinates",
    }
    primary_imports = (
        imported_module_stems(cycle805)
        | imported_module_stems(cycle808)
    )
    w7_imports = set().union(
        *(imported_module_stems(trees[path]) for path in W7_PATHS)
    )
    w7_parameters = {
        parameter
        for citation in (
            tuple(w7["functional_citations"])
            + tuple(w7["embedded_prediction_citations"])
        )
        for parameter in citation[4]
    }
    moved_parameter_names = {
        "bank",
        "epoch",
        "layer",
        "layer_slot",
        "physical",
        "physical_track_site",
        "q_slot",
        "q_traversal_slot",
        "station",
    }
    no_cross_import = (
        not (set(Path(path).stem for path in W7_PATHS) & primary_imports)
        and not (
            {Path(PRIMARY_PATHS[0]).stem, Path(PRIMARY_PATHS[1]).stem}
            & w7_imports
        )
    )
    anchors = {
        "cycle805_mapping_domains_exact": mapping_keys == {
            "bank_count",
            "cyclic_shift",
            "station_labels",
            "physical_track_site_slots",
            "logical_bank_indices",
            "epochs",
            "layer_slots",
            "layer_kinds",
            "q_traversal_slots",
        },
        "cycle808_action_domains_exact": bank_map_keys == {
            "station",
            "physical",
            "q_slots",
            "layer",
            "epochs",
            "orientations",
        },
        "cycle808_occurrence_action_fixes_nonstation_fields": (
            "return (bank, epoch, direction, orientation, mapped_selected)"
            in occurrence_source
            or "return bank, epoch, direction, orientation, mapped_selected"
            in occurrence_source
        ),
        "cycle805_nine_alternatives_exact":
            expected_choices == reimplemented_choices,
        "moved_and_w7_domains_disjoint":
            moved_805_domains.isdisjoint(w7_input_domains),
        "no_moved_domain_in_W7_function_signatures":
            moved_parameter_names.isdisjoint(w7_parameters),
        "no_primary_W7_import_edge": no_cross_import,
        "cycle808_constructor_data_action_identity": (
            "identity on constructor data state, as in the Cycle-805 maps"
            in input_bytes[PRIMARY_PATHS[1]].decode("utf-8")
        ),
        "w7_contract_reconstructed": bool(w7["passed"]),
        "cycle821_has_distinct_allocation_rotation": (
            "values" in rotate_source
            and "shift" in rotate_source
            and "output" in rotate_source
        ),
    }
    return {
        "anchors": anchors,
        "passed": all(anchors.values()),
        "cycle805_mapping_keys": tuple(sorted(mapping_keys)),
        "cycle808_action_keys": tuple(sorted(bank_map_keys)),
        "cycle808_occurrence_action": (
            "(bank,epoch,direction,orientation,selected) -> "
            "(bank,epoch,direction,orientation,station_map(selected))"
        ),
        "cycle808_constructor_data_action": (
            "identity on constructor data state"
        ),
        "moved_805_domains": tuple(sorted(moved_805_domains)),
        "w7_input_domains": tuple(sorted(w7_input_domains)),
        "w7_function_parameters": tuple(sorted(w7_parameters)),
        "domain_intersection": tuple(
            sorted(moved_805_domains & w7_input_domains)
        ),
        "induced_w7_action": (
            "NO_REACH; identity on W7 LinkState/response inputs"
        ),
        "cycle821_allocation_rotation": (
            "a separate C6 action on the six allocation weights; it is not "
            "the induced action of any Cycle-805 bijection"
        ),
        "source_sha256": {
            path: sha256(input_bytes[path]).hexdigest()
            for path in PRIMARY_PATHS
        },
    }


def stars_and_bars_allocations(
    total: int = 19,
    bins: int = 6,
) -> tuple[tuple[int, ...], ...]:
    output = []
    final_position = total + bins - 2
    for bars in combinations(range(total + bins - 1), bins - 1):
        previous = -1
        row = []
        for bar in bars:
            row.append(bar - previous - 1)
            previous = bar
        row.append(final_position - previous)
        output.append(tuple(row))
    return tuple(output)


READOUT_NAMES = (
    "w7.response_mixture_sum",
    "w7.response_expectation",
    "w7.response_expectation.matter[0]",
    "w7.response_expectation.matter[1]",
    "w7.response_expectation.matter[2]",
    "w7.response_expectation.mediator[0]",
    "w7.response_expectation.mediator[1]",
    "w7.response_expectation.mediator[2]",
    "w7.response_expectation.auxiliary[0]",
    "w7.response_expectation.auxiliary[1]",
    "w7.response_expectation.auxiliary[2]",
)


def w7_readouts(
    allocation: tuple[int, ...],
    rows: tuple[tuple[tuple[Fraction, ...], ...], ...],
) -> tuple[object, ...]:
    total = sum(allocation)
    if len(allocation) != 6 or total <= 0:
        raise ValueError(("invalid W7 allocation", allocation))
    mixture = tuple(
        tuple(
            sum(
                (
                    Fraction(allocation[direction])
                    * rows[direction][component][axis]
                    for direction in range(6)
                ),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )
    expectation = tuple(
        tuple(value / total for value in component)
        for component in mixture
    )
    projections = tuple(
        expectation[component][axis]
        for component in range(3)
        for axis in range(3)
    )
    return (mixture, expectation, *projections)


def contains_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(
            contains_float(key) or contains_float(item)
            for key, item in value.items()
        )
    if isinstance(value, (tuple, list, set, frozenset)):
        return any(contains_float(item) for item in value)
    return False


def invariance_certificate(
    actions: tuple[dict[str, object], ...],
    rows: tuple[tuple[tuple[Fraction, ...], ...], ...],
) -> dict[str, object]:
    allocations = stars_and_bars_allocations()
    values = {
        allocation: w7_readouts(allocation, rows)
        for allocation in allocations
    }
    witnesses = []
    comparisons = 0
    per_generator = {}
    for action in actions:
        generator_witnesses = []
        for allocation in allocations:
            # Certificate A proves that no moved 805/808 domain reaches this
            # six-weight input.  The induced response action is exactly x -> x.
            transformed = tuple(allocation)
            left_values = values[allocation]
            right_values = values[transformed]
            for index, (left, right) in enumerate(
                zip(left_values, right_values, strict=True)
            ):
                comparisons += 1
                if left == right:
                    continue
                witness = {
                    "generator": action["case"],
                    "readout": READOUT_NAMES[index],
                    "input": allocation,
                    "transformed_input": transformed,
                    "value_x": left,
                    "value_g_x": right,
                }
                generator_witnesses.append(witness)
                witnesses.append(witness)
        per_generator[str(action["case"])] = {
            "response_action": action["w7_input_action"],
            "complete_input_count": len(allocations),
            "readout_count": len(READOUT_NAMES),
            "comparisons": len(allocations) * len(READOUT_NAMES),
            "invariant": not generator_witnesses,
            "first_witness":
                generator_witnesses[0] if generator_witnesses else None,
        }
    all_exact = all(
        not contains_float(value)
        for readout_tuple in values.values()
        for value in readout_tuple
    )
    return {
        "input_family": (
            "complete weak compositions of 19 into the six ordered W7 "
            "direction bins"
        ),
        "allocation_count": len(allocations),
        "closed_form_count": comb(24, 5),
        "all_allocations_lawful": all(
            len(row) == 6
            and all(type(value) is int and value >= 0 for value in row)
            and sum(row) == 19
            for row in allocations
        ),
        "allocation_sha256": digest(allocations),
        "generator_case_count": len(actions),
        "nontrivial_induced_response_actions": sum(
            action["w7_input_action"] != "IDENTITY_NO_REACH"
            for action in actions
        ),
        "readout_count": len(READOUT_NAMES),
        "readouts": READOUT_NAMES,
        "exact_comparisons": comparisons,
        "all_values_exact": all_exact,
        "witnesses": tuple(witnesses),
        "per_generator": per_generator,
        "all_invariant": (
            comparisons == len(actions) * len(allocations) * len(READOUT_NAMES)
            and all_exact
            and not witnesses
            and all(row["invariant"] for row in per_generator.values())
        ),
        "value_table_sha256": digest(
            tuple((allocation, values[allocation]) for allocation in allocations)
        ),
    }


def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def relabeled_program(
    base_program: tuple[object, ...],
    mapping: tuple[int, ...],
) -> tuple[object, ...]:
    output = [None] * len(base_program)
    for source, target in enumerate(mapping):
        output[target] = base_program[source]
    if any(value is None for value in output):
        raise AssertionError("incomplete relabeled program")
    return tuple(output)


def q_order(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        return tuple(range(stations))
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return (
            tuple(range(0, stations, 2))
            + tuple(range(1, stations, 2))
        )
    raise ValueError(mode)


def symbolic_commutation_spot(spec: GeneratorSpec) -> dict[str, object]:
    bank = 3
    stations = 19
    base_program = tuple(("arbitrary_macro", index) for index in range(stations))
    phase = int(spec.layer_order == "R_then_Q")
    shift = (-spec.rotation - phase) % stations
    mapping = tuple(
        (station + shift) % stations for station in range(stations)
    )
    relabeled = relabeled_program(base_program, mapping)
    alternative = rotate_left(base_program, spec.rotation)
    order = q_order(stations, spec.order_mode)
    failures = []
    comparisons = 0
    for base_start in range(stations):
        alternative_start = mapping[base_start]
        for step in range(stations):
            landed_station = (alternative_start + step) % stations
            alternative_station = (
                alternative_start + step + phase
            ) % stations
            expected = base_program[(base_start + step) % stations]
            forward_ok = (
                relabeled[landed_station] == expected
                and alternative[alternative_station] == expected
                and (alternative_start + step + 1) % stations
                == mapping[(base_start + step + 1) % stations]
            )
            landed_inverse = (alternative_start - step - 1) % stations
            alternative_inverse = (
                alternative_start
                - step
                - int(spec.layer_order == "Q_then_R")
            ) % stations
            expected_inverse = base_program[
                (base_start - step - 1) % stations
            ]
            inverse_ok = (
                relabeled[landed_inverse] == expected_inverse
                and alternative[alternative_inverse] == expected_inverse
                and landed_inverse
                == mapping[(base_start - step - 1) % stations]
            )
            comparisons += 2
            if not forward_ok or not inverse_ok:
                failures.append(
                    {
                        "base_start": base_start,
                        "step": step,
                        "forward_ok": forward_ok,
                        "inverse_ok": inverse_ok,
                    }
                )
    event_transport = tuple(
        (
            event,
            (0,),
            (mapping[0],),
            (1, 0) if event % 2 == 0 else (0, 1),
        )
        for event in range(2 * bank)
    )
    return {
        "generator": spec.name,
        "bank": bank,
        "stations": stations,
        "arbitrary_program_symbols": len(base_program),
        "forward_inverse_operator_comparisons": comparisons,
        "q_order_is_permutation": (
            len(set(order)) == stations
            and set(order) == set(range(stations))
        ),
        "event_transport_rows": event_transport,
        "declared_complete_step_checkpoints":
            2 * bank * stations * 2,
        "failure": tuple(failures[:1]),
        "commutes_for_arbitrary_data_state": not failures,
    }


def cycle805_spot_control() -> dict[str, object]:
    sample_names = {
        "I1_SOURCE_1",
        "I2_ROTATE_1",
        "I3_R_THEN_Q_DESCENDING",
    }
    rows = tuple(
        symbolic_commutation_spot(spec)
        for spec in GENERATOR_SPECS
        if spec.name in sample_names
    )
    checkpoint_count = sum(
        int(row["declared_complete_step_checkpoints"]) for row in rows
    )
    return {
        "sample_generators": tuple(row["generator"] for row in rows),
        "bank": 3,
        "sample_case_count": len(rows),
        "event_transport_rows": sum(
            len(row["event_transport_rows"]) for row in rows
        ),
        "operator_comparisons": sum(
            int(row["forward_inverse_operator_comparisons"]) for row in rows
        ),
        "checkpoint_count": checkpoint_count,
        "checkpoint_discipline": (
            "after every complete controller step, forward and inverse"
        ),
        "reduction": (
            "equality of arbitrary symbolic macro words proves equality on "
            "every constructor data state at the declared checkpoints"
        ),
        "rows": rows,
        "pass": (
            len(rows) == 3
            and checkpoint_count == 684
            and all(row["q_order_is_permutation"] for row in rows)
            and all(row["commutes_for_arbitrary_data_state"] for row in rows)
        ),
    }


def rotation_image(
    allocation: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    shift %= len(allocation)
    if shift == 0:
        return allocation
    return allocation[-shift:] + allocation[:-shift]


def cycle821_spot_control(
    rows: tuple[tuple[tuple[Fraction, ...], ...], ...],
) -> dict[str, object]:
    witnesses = []
    for index, name in enumerate(READOUT_NAMES):
        if index < 2:
            axis = 0
        else:
            axis = (index - 2) % 3
        source_direction = 2 * axis
        allocation_a = tuple(
            19 if direction == source_direction else 0
            for direction in range(6)
        )
        allocation_b = rotation_image(allocation_a, 1)
        values_a = w7_readouts(allocation_a, rows)
        values_b = w7_readouts(allocation_b, rows)
        witnesses.append(
            {
                "generator": "C6_ALLOCATION_ROTATION_RHO_NOT_CYCLE805",
                "readout": name,
                "input": allocation_a,
                "transformed_input": allocation_b,
                "value_x": values_a[index],
                "value_g_x": values_b[index],
                "unequal": values_a[index] != values_b[index],
            }
        )
    row_flux_exact = all(
        all(
            sum(row[component][axis] for component in range(3)) == 0
            for axis in range(3)
        )
        for row in rows
    )
    return {
        "spot_orbit": (
            "the six pure allocations carrying all 19 units in one W7 bin"
        ),
        "separating_readout_count": sum(
            witness["unequal"] for witness in witnesses
        ),
        "expected_separating_readout_count": 11,
        "witnesses": tuple(witnesses),
        "flux_balance_readout": (
            "exactly zero for every response row and therefore every mixture"
        ),
        "flux_balance_invariant": row_flux_exact,
        "action_distinction": (
            "rho permutes W7 allocation weights; every Cycle-805-induced W7 "
            "action fixes them"
        ),
        "pass": (
            len(witnesses) == 11
            and all(witness["unequal"] for witness in witnesses)
            and row_flux_exact
        ),
    }


def main() -> int:
    input_bytes = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(data, filename=path)
        for path, data in input_bytes.items()
    }
    controls = source_controls(input_bytes, trees)
    actions = tuple(
        action_row(spec, bank, stations)
        for spec in GENERATOR_SPECS
        for bank, stations in BANK_STATIONS
    )
    w7 = extract_w7_contract(input_bytes, trees)
    action_contract = source_action_contract(
        input_bytes,
        trees,
        w7,
    )
    first_invariance = invariance_certificate(
        actions,
        w7["response_rows"],
    )
    second_invariance = invariance_certificate(
        actions,
        w7["response_rows"],
    )
    deterministic = first_invariance == second_invariance
    occurrence_control = cycle805_spot_control()
    separation_control = cycle821_spot_control(w7["response_rows"])

    emit("CYCLE", 826, "RESPONSE_VS_RELABELING")
    emit("HEAD_SHA", controls["head_sha"])
    emit("BRANCH", controls["branch"])
    for path in AUDIT_INPUT_PATHS:
        emit(
            "SOURCE_SHA",
            path,
            controls["sha256"][path],
            controls["git_blob_sha1"][path],
        )
    for action in actions:
        emit(
            "GENERATOR_ACTION",
            compact(
                {
                    "case": action["case"],
                    "choice": action["choice"],
                    "station_shift":
                        action["occurrence_action"]["station_shift"],
                    "layer_slot_map":
                        action["occurrence_action"]["layer_slot_map"],
                    "q_traversal_slot_map_sha256": digest(
                        action["occurrence_action"][
                            "q_traversal_slot_map"
                        ]
                    ),
                    "w7_input_action": action["w7_input_action"],
                    "reason": action["reason"],
                }
            ),
        )

    certificate_a = (
        action_contract["passed"]
        and len(actions) == 27
        and all(
            action["w7_input_action"] == "IDENTITY_NO_REACH"
            for action in actions
        )
    )
    check(
        "A_ACTION_ON_RESPONSE_INPUTS",
        certificate_a,
        {
            "generator_cases": len(actions),
            "per_generator_action": "IDENTITY_NO_REACH",
            "source_action_contract": action_contract,
            "w7_input_contract": {
                "input_type": w7["input_type"],
                "readout_rule": w7["readout_rule"],
                "directions": w7["directions"],
                "response_rows": w7["response_rows"],
                "functional_citations": w7["functional_citations"],
                "embedded_prediction_citations":
                    w7["embedded_prediction_citations"],
            },
        },
    )

    for witness in first_invariance["witnesses"]:
        emit(
            "NON_INVARIANCE_WITNESS",
            "generator=" + str(witness["generator"]),
            "input=" + compact(witness["input"]),
            "readout=" + str(witness["readout"]),
            "value_x=" + compact(witness["value_x"]),
            "value_g_x=" + compact(witness["value_g_x"]),
        )
    certificate_b = (
        first_invariance["allocation_count"] == 42_504
        and first_invariance["closed_form_count"] == 42_504
        and first_invariance["all_allocations_lawful"]
        and first_invariance["generator_case_count"] == 27
        and first_invariance["readout_count"] == 11
        and first_invariance["nontrivial_induced_response_actions"] == 0
        and first_invariance["exact_comparisons"] == 12_623_688
        and first_invariance["all_invariant"]
    )
    check(
        "B_COMPLETE_EXACT_INVARIANCE_TEST",
        certificate_b,
        {
            key: value
            for key, value in first_invariance.items()
            if key not in {"per_generator", "witnesses"}
        },
    )

    verdict = (
        "GAUGE_EXTENDS"
        if certificate_a and certificate_b
        else (
            "GAUGE_OCCURRENCE_SCOPED"
            if first_invariance["witnesses"]
            else "MIXED"
        )
    )
    certificate_c = verdict == "GAUGE_EXTENDS"
    check(
        "C_VERDICT",
        certificate_c,
        {
            "verdict": verdict,
            "verbatim_scope": (
                "the relabeling group is a symmetry of occurrence AND "
                "response at landed scope"
            ),
            "scope_basis": (
                "all 27 verified Cycle-805 primary-bank bijections induce "
                "identity on W7 inputs; generator closure preserves identity"
            ),
            "cycle821_reconciliation": (
                "the 11 Cycle-821 separators respond to the distinct C6 "
                "allocation rotation, not to an induced Cycle-805 action"
            ),
            "scope_annotation_for_5816_required": False,
        },
    )

    for witness in separation_control["witnesses"]:
        emit(
            "CYCLE821_SEPARATOR_WITNESS",
            "generator=" + str(witness["generator"]),
            "input=" + compact(witness["input"]),
            "readout=" + str(witness["readout"]),
            "value_x=" + compact(witness["value_x"]),
            "value_g_x=" + compact(witness["value_g_x"]),
        )
    certificate_d = occurrence_control["pass"] and separation_control["pass"]
    check(
        "D_805_AND_821_SPOT_CONTROLS",
        certificate_d,
        {
            "cycle805_occurrence_commutation_spot": occurrence_control,
            "cycle821_W7_separation_spot": separation_control,
        },
    )

    input_sha_after = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    elapsed = monotonic() - START
    certificate_e = all(
        (
            controls["literal_paths"] == AUDIT_INPUT_PATHS,
            controls["paths_worktree_relative"],
            controls["all_paths_exist"],
            controls["parsed_source_count"] == len(AUDIT_INPUT_PATHS),
            controls["sha256_match"],
            controls["git_blob_match"],
            input_sha_after == EXPECTED_SHA256,
            controls["blocklist_pass"],
            controls["none_loaded"],
            controls["no_blocklisted_AST_import"],
            controls["branch"] == EXPECTED_BRANCH,
            controls["base_is_ancestor"],
            deterministic,
            first_invariance["all_values_exact"],
            elapsed < AUDIT_TIMEOUT_SEC,
            STDOUT_BYTES + 8192 < STDOUT_LIMIT_BYTES,
        )
    )
    check(
        "E_SHAS_BLOCKLIST_EXACT_DETERMINISTIC_BOUNDS",
        certificate_e,
        {
            "head_sha": controls["head_sha"],
            "base_head_sha": BASE_HEAD_SHA,
            "branch": controls["branch"],
            "base_is_ancestor": controls["base_is_ancestor"],
            "literal_AUDIT_INPUT_PATHS": controls["literal_paths"],
            "all_paths_exist": controls["all_paths_exist"],
            "sha256_before": controls["sha256"],
            "sha256_after": input_sha_after,
            "git_blob_sha1": controls["git_blob_sha1"],
            "blocklisted_modules": BLOCKLISTED_MODULES,
            "blocked_attempts": controls["blocked_attempts"],
            "none_loaded": controls["none_loaded"],
            "deterministic_repeat": deterministic,
            "repeat_invariance_sha256": digest(second_invariance),
            "exact_arithmetic": first_invariance["all_values_exact"],
            "runtime_seconds": f"{elapsed:.6f}",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_E": STDOUT_BYTES,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    stable_report = {
        "cycle": 826,
        "action_count": len(actions),
        "action_summary_sha256": digest(actions),
        "w7_contract_sha256": digest(w7),
        "invariance_sha256": digest(first_invariance),
        "occurrence_control_sha256": digest(occurrence_control),
        "separation_control_sha256": digest(separation_control),
        "verdict": verdict,
        "certificates": dict(CHECKS),
    }
    passed = all(CHECKS.values())
    emit(
        "SUMMARY",
        compact(
            {
                "action_classes": {
                    "cyclic_station_shift_I1_I2_cases": 12,
                    "Q_order_only_I3_cases": 6,
                    "R_then_Q_layer_swap_cases": 9,
                },
                "all_27_induced_W7_actions": "IDENTITY_NO_REACH",
                "complete_W7_allocations": 42_504,
                "readouts": 11,
                "exact_comparisons": 12_623_688,
                "non_invariance_witnesses":
                    len(first_invariance["witnesses"]),
                "cycle821_distinct_C6_separators":
                    separation_control["separating_readout_count"],
                "verdict": verdict,
                "certificates": dict(CHECKS),
                "report_sha256": digest(stable_report),
                "runtime_seconds": f"{elapsed:.6f}",
                "stdout_bytes_final_upper_bound": STDOUT_BYTES + 4096,
            }
        ),
    )
    emit("VERDICT", verdict)
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
