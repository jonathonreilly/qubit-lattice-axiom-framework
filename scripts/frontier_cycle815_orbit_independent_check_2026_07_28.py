#!/usr/bin/env python3
"""Cycle 815 independent adversarial origin-orbit checker.

The six carried files are SHA-pinned text/AST inputs only.  This checker
reimplements the finite label maps, the Cycle-786 allocation law, and a
bounded wider relabeling hunt.  In particular it does not import or execute
the Cycle-815 primary.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle805_relabeling_independent_check_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_independent_check_2026_07_28.py",
    "scripts/frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[1]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[2]:
        "dca858db349bddeb2e4e800bf68a0be2f9fabf076529decf7f3700c26a45655f",
    AUDIT_INPUT_PATHS[3]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[4]:
        "8a717469dfb092ff0fc4e1b39be98c85ceea2ff8256bcaead73a93664867fdac",
    AUDIT_INPUT_PATHS[5]:
        "e064b2f431f3e125b8c7f8176e6331f3fee41c2d1dc8ba7e3e65ae97a4ebb6b0",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[1]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[2]: "386face671529fd0fef505d9b04676b42a8b5d97",
    AUDIT_INPUT_PATHS[3]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[4]: "3a5062ecaba514fda64440c1517c0dfefcfcb6e5",
    AUDIT_INPUT_PATHS[5]: "3fbfaf0019af05bbb3121de47de49b9cefec7571",
}

import ast
from collections import deque
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
ORIGINS = tuple(range(12))
POSITIVE = tuple(range(6))
NEGATIVE = tuple(range(6, 12))
ALLOCATION_BANKS = (2, 5, 12)
ALL_BANKS = (1, 2, 3, 5, 12)
STATIONS = {2: 11, 5: 35, 12: 91}
GROUP_TOTAL = 19
GENERATOR_SPECS = (
    ("I1_SOURCE_1", -1, "Q_then_R", "ascending"),
    ("I1_SOURCE_LAST", 1, "Q_then_R", "ascending"),
    ("I2_ROTATE_1", 1, "Q_then_R", "ascending"),
    ("I2_ROTATE_LAST", -1, "Q_then_R", "ascending"),
    ("I3_Q_THEN_R_DESCENDING", 0, "Q_then_R", "descending"),
    ("I3_Q_THEN_R_EVEN_THEN_ODD", 0, "Q_then_R", "even_then_odd"),
    ("I3_R_THEN_Q_ASCENDING", 0, "R_then_Q", "ascending"),
    ("I3_R_THEN_Q_DESCENDING", 0, "R_then_Q", "descending"),
    ("I3_R_THEN_Q_EVEN_THEN_ODD", 0, "R_then_Q", "even_then_odd"),
)
F_NAME = "F_XOR_LIFT"
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PackageBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PACKAGE_BLOCKER = _PackageBlocker()
sys.meta_path.insert(0, PACKAGE_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function cardinality", name, len(rows)))
    return rows[0]


def permutation_orbits(
    points: tuple[int, ...],
    generators: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    remaining = set(points)
    result = []
    while remaining:
        start = min(remaining)
        orbit = {start}
        queue = deque((start,))
        while queue:
            point = queue.popleft()
            for permutation in generators:
                target = permutation[point]
                if target not in orbit:
                    orbit.add(target)
                    queue.append(target)
        row = tuple(sorted(orbit))
        result.append(row)
        remaining.difference_update(row)
    return tuple(result)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Return left after right."""
    return tuple(left[right[index]] for index in range(len(right)))


def orientation(origin: int) -> int:
    return 1 if origin < 6 else -1


def source_controls() -> dict[str, object]:
    sources = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(source, filename=path)
        for path, source in sources.items()
    }
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    own_assignments: dict[str, ast.AST] = {}
    imported = []
    dynamic_imports = []
    for node in own_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    own_assignments[target.id] = node.value
    for node in ast.walk(own_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
        elif (
            isinstance(node, ast.Call)
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and (
                (isinstance(node.func, ast.Name) and node.func.id == "__import__")
                or (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr == "import_module"
                )
            )
        ):
            dynamic_imports.append(node.args[0].value)

    runtime_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            __import__(module)
        except ImportError as exc:
            runtime_attempts[module] = (
                str(exc) == f"BLOCKLIST forbids import of {module}"
            )
        else:
            runtime_attempts[module] = False

    p786, p805, c805, p808, c808, p815 = AUDIT_INPUT_PATHS
    origin_catalog = function_node(trees[p786], "derive_origin_catalog")
    mapping_805 = function_node(trees[p805], "mapping_table")
    mapping_805_check = function_node(trees[c805], "mapping_certificate")
    maps_808 = function_node(trees[p808], "spec_bank_maps")
    g_808 = function_node(trees[p808], "map_occurrence_by_g")
    f_808 = function_node(trees[p808], "map_occurrence_by_flip")
    xor_808 = function_node(trees[p808], "orientation_candidate_certificate")
    action_815 = function_node(trees[p815], "origin_action_certificate")

    origin_dump = ast.dump(origin_catalog)
    action_815_dump = ast.dump(action_815)
    source_domain_literals = {
        node.value
        for function in (mapping_805, mapping_805_check, maps_808)
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    moved_action_names = {
        node.id
        for function in (g_808, f_808, xor_808)
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
    }
    moved_action_literals = {
        node.value
        for function in (g_808, f_808, xor_808)
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    generator_anchors = all(
        name in sources[p808]
        for name, _rotation, _layer, _order in GENERATOR_SPECS[:4]
    ) and all(
        token in sources[p808]
        for token in (
            '"name": f"I3_{layer}_{order}".upper()',
            '("Q_then_R", "descending")',
            '("Q_then_R", "even_then_odd")',
            '("R_then_Q", "ascending")',
            '("R_then_Q", "descending")',
            '("R_then_Q", "even_then_odd")',
        )
    )
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    declared_node = own_assignments["DECLARED_INPUT_PATHS"]
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "all_sources_parse": all(isinstance(tree, ast.Module) for tree in trees.values()),
        "blocklisted_not_AST_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in imported
        ),
        "blocklisted_not_literal_dynamic_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in dynamic_imports
        ),
        "blocklisted_not_loaded": all(
            name not in sys.modules for name in BLOCKLISTED_MODULES
        ),
        "runtime_blocker_installed": PACKAGE_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "generator_specs_reimplemented_from_AST_text": generator_anchors,
        "cycle786_origin_is_one_hot_matter_index": all(
            token in origin_dump
            for token in (
                "Name(id='origin'",
                "LShift",
                "Constant(value=12)",
                "Constant(value='origin')",
                "keyword(arg='matter'",
            )
        ),
        "cycle786_origin_partition_and_law_anchors": all(
            token in sources[p786]
            for token in (
                '"origin": origin',
                '"orientation": 1 if origin < 6 else -1',
                '"one_origin_refinement_range": [0, 19]',
                'census["exact_orientation_channel_counts"] == {"+1": 19, "-1": 19}',
                '"origin_correspondence": "AMBIGUOUS_SIX_WAY"',
            )
        ),
        "cycle805_declared_domains": tuple(sorted(
            literal for literal in source_domain_literals
            if literal in {
                "station_labels",
                "physical_track_site_slots",
                "logical_bank_indices",
                "epochs",
                "layer_slots",
                "q_traversal_slots",
                "station",
                "physical",
                "q_slots",
            }
        )),
        "cycle805_maps_omit_origin_and_matter": (
            "origin" not in ast.dump(mapping_805).lower()
            and "matter" not in ast.dump(mapping_805).lower()
            and "origin" not in ast.dump(mapping_805_check).lower()
            and "matter" not in ast.dump(mapping_805_check).lower()
        ),
        "cycle808_actions_omit_origin_and_matter": (
            "origin" not in moved_action_names
            and "matter" not in moved_action_names
            and "origin" not in moved_action_literals
            and "matter" not in moved_action_literals
        ),
        "cycle808_flip_anchors": all(
            token in sources[p808]
            for token in (
                "return bank, int(epoch) ^ 1, swapped, -int(orientation), selected",
                "the unique XOR mask transporting paired states x,y is x XOR y",
                "per-typed-checkpoint XOR lift commutes on every landed edge",
            )
        ),
        "cycle808_checker_XOR_extension_anchor": (
            "XOR" in sources[c808]
            and "checkpoint" in sources[c808]
            and "orientation" in sources[c808]
        ),
        "primary_identity_action_detected_by_AST": all(
            token in action_815_dump
            for token in (
                "Name(id='identity'",
                "Name(id='ORIGINS'",
                "Name(id='G_PRIME_GENERATORS'",
            )
        ),
        "primary_blocklisted_text_AST_only": (
            BLOCKLISTED_MODULES[-1] not in sys.modules
            and runtime_attempts[BLOCKLISTED_MODULES[-1]]
        ),
    }


def q_positions(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        order = tuple(range(stations))
    elif mode == "descending":
        order = tuple(reversed(range(stations)))
    elif mode == "even_then_odd":
        order = tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    else:
        raise ValueError(mode)
    result = [0] * stations
    for slot, station in enumerate(order):
        result[station] = slot
    return tuple(result)


def generator_label_maps(
    spec: tuple[str, int, str, str],
    stations: int,
) -> dict[str, tuple[int, ...]]:
    """Independent Cycle-805/808 normal-form coordinate reimplementation."""
    _name, rotation, layer_order, order_mode = spec
    phase = int(layer_order == "R_then_Q")
    shift = (-rotation - phase) % stations
    station = tuple((value + shift) % stations for value in range(stations))
    q_position = q_positions(stations, order_mode)
    q_slots = tuple(
        q_position[(value - rotation) % stations]
        for value in range(stations)
    )
    physical = tuple(
        2 * ((site // 2 + shift) % stations) + site % 2
        for site in range(2 * stations)
    )
    return {
        "station": station,
        "physical": physical,
        "q_slots": q_slots,
        "layer": (phase, 1 ^ phase),
    }


def xor_algebra_certificate() -> dict[str, object]:
    transport_failures = 0
    involution_failures = 0
    uniqueness_failures = 0
    pairs = 0
    for left in range(16):
        for right in range(16):
            mask = left ^ right
            pairs += 1
            transport_failures += (left ^ mask) != right
            transport_failures += (right ^ mask) != left
            involution_failures += ((left ^ mask) ^ mask) != left
            solutions = tuple(candidate for candidate in range(16) if left ^ candidate == right)
            uniqueness_failures += solutions != (mask,)
    return {
        "bounded_bit_width": 4,
        "ordered_pairs": pairs,
        "transport_failures": transport_failures,
        "involution_failures": involution_failures,
        "unique_mask_failures": uniqueness_failures,
        "pass": not any(
            (transport_failures, involution_failures, uniqueness_failures)
        ),
    }


def origin_action_certificate(controls: dict[str, object]) -> dict[str, object]:
    identity = ORIGINS
    half_swap = tuple(
        origin + 6 if origin < 6 else origin - 6
        for origin in ORIGINS
    )
    g_rows = []
    for spec in GENERATOR_SPECS:
        name = spec[0]
        bank_maps_bijective = all(
            all(
                set(row[key]) == set(range(
                    2 * stations if key == "physical" else stations
                ))
                for key in ("station", "physical", "q_slots")
            )
            for stations in STATIONS.values()
            for row in (generator_label_maps(spec, stations),)
        )
        g_rows.append(
            {
                "generator": name,
                "source_origin_action": "NOT_SUPPLIED",
                "minimal_product_lift": identity,
                "minimal_lift_fixes_origins": True,
                "all_reimplemented_label_maps_bijective": bank_maps_bijective,
                "orientation_action": "fixed",
            }
        )

    identity_flip_compatible = all(
        orientation(identity[origin]) == -orientation(origin)
        for origin in ORIGINS
    )
    half_swap_compatible = all(
        orientation(half_swap[origin]) == -orientation(origin)
        for origin in ORIGINS
    )
    lifted_generators = tuple(
        row["minimal_product_lift"] for row in g_rows
    ) + (half_swap,)
    lifted_orbits = permutation_orbits(ORIGINS, lifted_generators)
    primary_generators = tuple(identity for _row in g_rows) + (identity,)
    primary_orbits = permutation_orbits(ORIGINS, primary_generators)

    words = {
        "I1_SOURCE_1*I2_ROTATE_1":
            compose(identity, identity),
        "I3_R_THEN_Q_DESCENDING*I1_SOURCE_LAST*I2_ROTATE_LAST":
            compose(identity, compose(identity, identity)),
        "F_XOR_LIFT^2": compose(half_swap, half_swap),
        "F_XOR_LIFT*I3_Q_THEN_R_DESCENDING":
            compose(half_swap, identity),
        "I2_ROTATE_1*F_XOR_LIFT*I1_SOURCE_1":
            compose(identity, compose(half_swap, identity)),
    }
    product_checks = {
        name: {
            "permutation": permutation,
            "bijective": set(permutation) == set(ORIGINS),
            "moves_origin": permutation != identity,
        }
        for name, permutation in words.items()
    }
    xor_algebra = xor_algebra_certificate()
    primary_refuted = all(
        (
            controls["cycle786_origin_is_one_hot_matter_index"],
            controls["cycle786_origin_partition_and_law_anchors"],
            controls["cycle805_maps_omit_origin_and_matter"],
            controls["cycle808_actions_omit_origin_and_matter"],
            controls["primary_identity_action_detected_by_AST"],
            not identity_flip_compatible,
            half_swap_compatible,
            lifted_orbits != primary_orbits,
            any(row["moves_origin"] for row in product_checks.values()),
            xor_algebra["pass"],
        )
    )
    return {
        "generator_rows": tuple(g_rows) + (
            {
                "generator": F_NAME,
                "source_origin_action": "NOT_SUPPLIED",
                "primary_chosen_lift": identity,
                "primary_lift_catalog_compatible": identity_flip_compatible,
                "compatible_involutive_witness": half_swap,
                "compatible_witness_moves_every_origin": all(
                    half_swap[origin] != origin for origin in ORIGINS
                ),
                "orientation_action": "flip",
            },
        ),
        "source_restriction_result":
            "NO_CYCLE805_OR_808_ORIGIN_ACTION_EXISTS_TO_RESTRICT",
        "minimal_G_lift_status":
            "NINE_IDENTITY_LIFTS_ARE_ALLOWED_BUT_NOT_DERIVED",
        "primary_F_identity_lift_compatible": identity_flip_compatible,
        "compatible_F_half_swap": half_swap,
        "compatible_F_half_swap_orbits": lifted_orbits,
        "primary_claimed_orbits": primary_orbits,
        "sample_products": product_checks,
        "sample_products_consistent": all(
            row["bijective"] for row in product_checks.values()
        ),
        "origin_identification": {
            "cycle786":
                "one-hot Cycle719 matter-origin index 0..11, with intrinsic "
                "record orientation + on 0..5 and - on 6..11",
            "cycle805":
                "station/site/Q-slot/layer coordinates; logical banks and "
                "epochs fixed; no matter-origin coordinate",
            "cycle808":
                "five-field occurrence label plus typed XOR checkpoint masks; "
                "no matter-origin coordinate",
            "mismatch":
                "absence of an origin coordinate does not derive its identity "
                "action, and the identity lift of F does not preserve the "
                "Cycle786 origin-to-orientation catalog",
        },
        "compatible_involutive_F_lift_count": 720,
        "compatible_orientation_reversing_bijection_count": 720 ** 2,
        "xor_algebra": xor_algebra,
        "primary_all_singleton_refuted": primary_refuted,
        "finding":
            "REFUTED: G' has no supplied action on the Cycle786 matter-origin "
            "coordinate; moreover F's identity lift is incompatible with the "
            "origin catalog, while the lawful involution o<6 ? o+6 : o-6 "
            "moves every origin.",
    }


def lawful_allocations() -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    frontier: list[tuple[tuple[int, ...], int]] = [((), GROUP_TOTAL)]
    for _bin in range(5):
        next_frontier = []
        for prefix, remaining in frontier:
            for value in range(remaining + 1):
                next_frontier.append((prefix + (value,), remaining - value))
        frontier = next_frontier
    for prefix, remaining in frontier:
        rows.append(prefix + (remaining,))
    return tuple(rows)


def allocation_space_certificate() -> dict[str, object]:
    allocations = lawful_allocations()
    dp = [0] * (GROUP_TOTAL + 1)
    dp[0] = 1
    for _bin in range(6):
        updated = [0] * (GROUP_TOTAL + 1)
        for partial_total, ways in enumerate(dp):
            for value in range(GROUP_TOTAL - partial_total + 1):
                updated[partial_total + value] += ways
        dp = updated
    unique = len(set(allocations)) == len(allocations)
    lawful = all(
        len(row) == 6
        and all(type(value) is int and value >= 0 for value in row)
        and sum(row) == GROUP_TOTAL
        for row in allocations
    )
    return {
        "law_rederived_from_cycle786":
            "six nonnegative integer origin counts per orientation fiber, "
            "each in 0..19, summing to the exact orientation count 19",
        "enumeration_method":
            "five-prefix residual enumeration (not Cycle815 recursion)",
        "independent_DP_coefficient": dp[GROUP_TOTAL],
        "allocation_count_per_group": len(allocations),
        "unique": unique,
        "all_lawful": lawful,
        "first": allocations[0],
        "last": allocations[-1],
        "allocation_sha256": digest(allocations),
        "pass": all(
            (
                len(allocations) == 42_504,
                dp[GROUP_TOTAL] == 42_504,
                unique,
                lawful,
            )
        ),
    }


def identity_controls_certificate() -> dict[str, object]:
    full_rows = tuple(
        (bank, event, 1 if event % 2 == 0 else -1)
        for bank in ALL_BANKS
        for event in range(2 * bank)
    )
    projected_rows = tuple(
        (bank, event, 1 if event % 2 == 0 else -1)
        for bank in ALLOCATION_BANKS
        for event in range(2 * bank)
    )
    full_positive = sum(row[2] == 1 for row in full_rows)
    full_negative = sum(row[2] == -1 for row in full_rows)
    projected_positive = sum(row[2] == 1 for row in projected_rows)
    projected_negative = sum(row[2] == -1 for row in projected_rows)
    passed = (
        len(full_rows) == 46
        and (full_positive, full_negative) == (23, 23)
        and len(projected_rows) == 38
        and (projected_positive, projected_negative) == (19, 19)
    )
    return {
        "construction":
            "independent enumeration of 2*bank alternating-orientation epochs",
        "full_banks": ALL_BANKS,
        "full_count": len(full_rows),
        "full_orientation_counts": {"+1": full_positive, "-1": full_negative},
        "projection_banks": ALLOCATION_BANKS,
        "projection_count": len(projected_rows),
        "projection_orientation_counts": {
            "+1": projected_positive,
            "-1": projected_negative,
        },
        "full_rows_sha256": digest(full_rows),
        "projection_rows_sha256": digest(projected_rows),
        "pass": passed,
    }


def abstract_805_checkpoint_bar(
    shifts: tuple[int, int, int],
) -> dict[str, object]:
    comparisons = 0
    failures = []
    for bank, shift in zip(ALLOCATION_BANKS, shifts, strict=True):
        stations = STATIONS[bank]
        mapping = tuple(
            (station + shift) % stations for station in range(stations)
        )
        base_program = tuple(range(stations))
        relabeled_program = [None] * stations
        for source, target in enumerate(mapping):
            relabeled_program[target] = base_program[source]
        rotation = (-shift) % stations
        alternative_program = (
            base_program[rotation:] + base_program[:rotation]
        )
        for event in range(2 * bank):
            for leg, sign in (("forward", 1), ("inverse", -1)):
                for start in range(stations):
                    mapped_start = mapping[start]
                    for checkpoint in range(stations):
                        if leg == "forward":
                            base_active = (start + checkpoint) % stations
                            varied_active = (
                                mapped_start + checkpoint
                            ) % stations
                        else:
                            base_active = (
                                start - checkpoint - 1
                            ) % stations
                            varied_active = (
                                mapped_start - checkpoint - 1
                            ) % stations
                        comparisons += 1
                        expected_role = base_program[base_active]
                        if not all(
                            (
                                mapping[base_active] == varied_active,
                                relabeled_program[varied_active]
                                == expected_role,
                                alternative_program[varied_active]
                                == expected_role,
                            )
                        ):
                            failures.append(
                                {
                                    "bank": bank,
                                    "event": event,
                                    "leg": leg,
                                    "start": start,
                                    "checkpoint": checkpoint,
                                    "sign": sign,
                                }
                            )
                            break
                    if failures:
                        break
                if failures:
                    break
            if failures:
                break
        if failures:
            break
    return {
        "shifts_by_bank": dict(zip(ALLOCATION_BANKS, shifts, strict=True)),
        "declared_bar":
            "every event, forward/inverse leg, token start, and complete-step "
            "checkpoint: cyclic successor/predecessor, relabeled-program role "
            "incidence, and rotated-alternative role incidence (the Cycle805 "
            "arbitrary-data symbolic commutation bar)",
        "comparisons": comparisons,
        "failure": failures[:1],
        "commutes": not failures,
    }


def origin_fiber_rotation(
    positive_shift: int,
    negative_shift: int,
) -> tuple[int, ...]:
    return tuple(
        (
            (origin + positive_shift) % 6
            if origin < 6
            else 6 + ((origin - 6 + negative_shift) % 6)
        )
        for origin in ORIGINS
    )


def wider_element_hunt(
    allocations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    shift_vectors = tuple(
        (left, middle, right)
        for left in (-1, 0, 1)
        for middle in (-1, 0, 1)
        for right in (-1, 0, 1)
    )
    bars = {
        shifts: abstract_805_checkpoint_bar(shifts)
        for shifts in shift_vectors
    }
    lifts = tuple(
        origin_fiber_rotation(positive_shift, negative_shift)
        for positive_shift in range(6)
        for negative_shift in range(6)
    )
    candidates = 0
    commuting = 0
    moving = 0
    failures = []
    for shifts in shift_vectors:
        bar = bars[shifts]
        for lift in lifts:
            candidates += 1
            bijective = set(lift) == set(ORIGINS)
            orientation_preserved = all(
                orientation(lift[origin]) == orientation(origin)
                for origin in ORIGINS
            )
            # The Cycle-805 checkpoint state has no matter-origin coordinate.
            # Its product action therefore commutes exactly iff the station
            # part passes the bar and the origin lift preserves the Cycle-786
            # orientation-support fiber being adjoined.
            commutes = (
                bar["commutes"] and bijective and orientation_preserved
            )
            commuting += commutes
            moving += commutes and lift != ORIGINS
            if not commutes:
                failures.append(
                    {
                        "shifts": shifts,
                        "lift": lift,
                        "bar": bar,
                        "bijective": bijective,
                        "orientation_preserved": orientation_preserved,
                    }
                )

    witness_shifts = (1, 1, 1)
    witness_lift = origin_fiber_rotation(1, 1)
    witness_bar = bars[witness_shifts]
    witness_orbits = permutation_orbits(ORIGINS, (witness_lift,))
    positive_survivors = tuple(
        row for row in allocations if len(set(row)) == 1
    )
    negative_survivors = tuple(
        row for row in allocations if len(set(row)) == 1
    )
    witness_valid = all(
        (
            witness_bar["commutes"],
            set(witness_lift) == set(ORIGINS),
            witness_lift != ORIGINS,
            all(
                orientation(witness_lift[origin]) == orientation(origin)
                for origin in ORIGINS
            ),
            witness_orbits == (POSITIVE, NEGATIVE),
            not positive_survivors,
            not negative_survivors,
        )
    )
    element_name = (
        "BANK_TYPED_STATION_SHIFT_1_WITHIN_ORIENTATION_ORIGIN_ROTATION_1"
    )
    return {
        "declared_bounded_class":
            "bank-typed cyclic station shifts s_b in {-1,0,1} for banks "
            "2/5/12, composed with independent cyclic rotations of the six "
            "Cycle786 matter-origin labels inside each orientation fiber",
        "station_shift_vectors": len(shift_vectors),
        "lawful_origin_lifts": len(lifts),
        "candidates_exhausted": candidates,
        "commuting_candidates": commuting,
        "moving_commuting_candidates": moving,
        "first_failure": failures[:1],
        "all_station_bars_commute": all(
            row["commutes"] for row in bars.values()
        ),
        "bar_comparisons_total": sum(
            row["comparisons"] for row in bars.values()
        ),
        "witness_name": element_name,
        "witness_station_shifts": witness_shifts,
        "witness_origin_permutation": witness_lift,
        "witness_origin_orbits": witness_orbits,
        "witness_bar": witness_bar,
        "unconstrained_count_per_group": len(allocations),
        "surviving_count_per_group_under_witness": len(positive_survivors),
        "combined_surviving_count_under_witness":
            len(positive_survivors) * len(negative_survivors),
        "witness_valid": witness_valid,
        "finding": (
            f"NON_VACUOUS_VIA_{element_name}: the element moves every origin; "
            "its two six-cycles force six equal counts in each total-19 "
            "fiber, so 0 of 42,504 allocations per group survive."
        ),
        "pass": (
            candidates == 27 * 36
            and commuting == candidates
            and moving > 0
            and witness_valid
        ),
    }


def git_index_blobs(paths: tuple[str, ...]) -> dict[str, str]:
    completed = subprocess.run(
        ("git", "ls-files", "-s", "--", *paths),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    result = {}
    for line in completed.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        _mode, blob, _stage = metadata.split()
        result[path] = blob
    return result


def build_core(controls: dict[str, object]) -> dict[str, object]:
    action = origin_action_certificate(controls)
    allocation = allocation_space_certificate()
    identity_control = identity_controls_certificate()
    allocations = lawful_allocations()
    wider = wider_element_hunt(allocations)
    return {
        "origin_action": action,
        "allocation_space": allocation,
        "identity_controls": identity_control,
        "wider_element_hunt": wider,
        "primary_verdict": "REFUTED",
    }


def main() -> int:
    input_bytes_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    input_sha_before = {
        path: sha256(data).hexdigest()
        for path, data in input_bytes_before.items()
    }
    input_blob_before = {
        path: git_blob_sha1(data)
        for path, data in input_bytes_before.items()
    }
    indexed_blobs = git_index_blobs(AUDIT_INPUT_PATHS)
    controls = source_controls()
    first = build_core(controls)
    second = build_core(controls)
    input_bytes_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    input_sha_after = {
        path: sha256(data).hexdigest()
        for path, data in input_bytes_after.items()
    }
    input_blob_after = {
        path: git_blob_sha1(data)
        for path, data in input_bytes_after.items()
    }
    elapsed = monotonic() - START
    deterministic = first == second

    direct_control_keys = (
        "literal_AUDIT_INPUT_PATHS",
        "DECLARED_INPUT_PATHS_alias",
        "paths_worktree_relative",
        "all_paths_exist",
        "all_sources_parse",
        "blocklisted_not_AST_imported",
        "blocklisted_not_literal_dynamic_imported",
        "blocklisted_not_loaded",
        "runtime_blocker_installed",
        "generator_specs_reimplemented_from_AST_text",
        "cycle786_origin_is_one_hot_matter_index",
        "cycle786_origin_partition_and_law_anchors",
        "cycle805_maps_omit_origin_and_matter",
        "cycle808_actions_omit_origin_and_matter",
        "cycle808_flip_anchors",
        "cycle808_checker_XOR_extension_anchor",
        "primary_identity_action_detected_by_AST",
        "primary_blocklisted_text_AST_only",
    )
    controls_base = all(
        (
            all(bool(controls[key]) for key in direct_control_keys),
            all(controls["runtime_attempts"].values()),
            input_sha_before == input_sha_after == EXPECTED_SHA256,
            input_blob_before == input_blob_after == EXPECTED_GIT_BLOB_SHA1,
            indexed_blobs == EXPECTED_GIT_BLOB_SHA1,
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
        )
    )

    action = first["origin_action"]
    allocation = first["allocation_space"]
    identity_control = first["identity_controls"]
    wider = first["wider_element_hunt"]
    certificate_1 = all(
        (
            action["primary_all_singleton_refuted"],
            action["sample_products_consistent"],
            all(
                row.get("all_reimplemented_label_maps_bijective", True)
                for row in action["generator_rows"]
            ),
            not action["primary_F_identity_lift_compatible"],
            action["compatible_F_half_swap_orbits"]
            == tuple((origin, origin + 6) for origin in POSITIVE),
        )
    )
    certificate_2 = allocation["pass"]
    certificate_3 = identity_control["pass"]
    certificate_4 = wider["pass"]

    def render(stdout_bytes: int) -> tuple[str, bool]:
        certificate_5 = controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
        certificates = {
            "1_THE_ORIGIN_ACTION_RE_DERIVATION": certificate_1,
            "2_THE_ALLOCATION_SPACE_CONTROL": certificate_2,
            "3_THE_IDENTITY_CONTROLS": certificate_3,
            "4_THE_WIDER_ELEMENT_HUNT": certificate_4,
            "5_CONTROLS": certificate_5,
        }
        lines = [
            "BOUNDARY text/AST-only carried packages; exact finite landed "
            "allocation/support projection; no probability or split rule",
        ]
        for path in AUDIT_INPUT_PATHS:
            lines.append(
                "AUDIT_INPUT_SHA "
                + compact(
                    {
                        "path": path,
                        "sha256": input_sha_after[path],
                        "git_blob_sha1": input_blob_after[path],
                        "indexed_blob_sha1": indexed_blobs[path],
                    }
                )
            )
        for row in action["generator_rows"]:
            lines.append("ORIGIN_GENERATOR_ACTION " + compact(row))
        for word, row in action["sample_products"].items():
            lines.append(
                "ORIGIN_PRODUCT_ACTION "
                + compact({"word": word, **row})
            )
        lines.append(
            ("PASS" if certificate_1 else "FAIL")
            + " CERTIFICATE_1_THE_ORIGIN_ACTION_RE_DERIVATION :: "
            + compact(
                {
                    "primary_all_singleton_refuted":
                        action["primary_all_singleton_refuted"],
                    "source_restriction_result":
                        action["source_restriction_result"],
                    "primary_claimed_orbits":
                        action["primary_claimed_orbits"],
                    "compatible_F_orbits":
                        action["compatible_F_half_swap_orbits"],
                    "origin_identification":
                        action["origin_identification"],
                    "xor_algebra": action["xor_algebra"],
                    "finding": action["finding"],
                }
            )
        )
        lines.append(
            "FINDING THE_ORIGIN_ACTION_RE_DERIVATION "
            + action["finding"]
        )
        lines.append(
            ("PASS" if certificate_2 else "FAIL")
            + " CERTIFICATE_2_THE_ALLOCATION_SPACE_CONTROL :: "
            + compact(allocation)
        )
        lines.append(
            "FINDING THE_ALLOCATION_SPACE_CONTROL "
            f"{allocation['allocation_count_per_group']}_PER_GROUP"
        )
        lines.append(
            ("PASS" if certificate_3 else "FAIL")
            + " CERTIFICATE_3_THE_IDENTITY_CONTROLS :: "
            + compact(identity_control)
        )
        lines.append(
            "FINDING THE_IDENTITY_CONTROLS "
            "FULL_46_EQ_23_PLUS_23 PROJECTION_38_EQ_19_PLUS_19"
        )
        lines.append(
            ("PASS" if certificate_4 else "FAIL")
            + " CERTIFICATE_4_THE_WIDER_ELEMENT_HUNT :: "
            + compact(wider)
        )
        lines.append(wider["finding"])
        lines.append(
            "NON_VACUOUS_VIA_" + wider["witness_name"]
        )
        lines.append(
            "PRIMARY_CLAIM FAIL :: VACUOUS_REFUTED_BY_MOVING_ORIGIN_ELEMENT"
        )
        lines.append(
            ("PASS" if certificate_5 else "FAIL")
            + " CERTIFICATE_5_CONTROLS :: "
            + compact(
                {
                    "source_controls": controls,
                    "input_sha_stable": input_sha_before == input_sha_after,
                    "git_blob_sha_stable":
                        input_blob_before == input_blob_after,
                    "indexed_at_expected_blobs":
                        indexed_blobs == EXPECTED_GIT_BLOB_SHA1,
                    "primary_runtime_blocklisted":
                        controls["primary_blocklisted_text_AST_only"],
                    "deterministic": deterministic,
                    "first_core_sha256": digest(first),
                    "repeat_core_sha256": digest(second),
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                    "stdout_bytes": stdout_bytes,
                    "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
                }
            )
        )
        report = {
            "cycle": 815,
            "checker": "independent_adversarial",
            "certificates": certificates,
            "all_pass": all(certificates.values()),
            "primary_verdict": "REFUTED",
            "primary_all_singleton_orbits": False,
            "compatible_F_origin_orbits":
                action["compatible_F_half_swap_orbits"],
            "wider_witness": wider["witness_name"],
            "wider_witness_origin_orbits": wider["witness_origin_orbits"],
            "unconstrained_count_per_group":
                wider["unconstrained_count_per_group"],
            "surviving_count_per_group_under_witness":
                wider["surviving_count_per_group_under_witness"],
            "runtime_seconds": round(elapsed, 6),
        }
        report["stable_report_sha256"] = digest(
            {
                key: value
                for key, value in report.items()
                if key != "runtime_seconds"
            }
        )
        lines.append("SUMMARY_JSON " + compact(report))
        lines.append(
            "CYCLE815_ORBIT_INDEPENDENT_CHECK_PASS_PRIMARY_REFUTED"
            if report["all_pass"]
            else "CYCLE815_ORBIT_INDEPENDENT_CHECK_FAILURE"
        )
        return "\n".join(lines) + "\n", certificate_5

    stdout_bytes = 0
    output = ""
    certificate_5 = False
    for _iteration in range(12):
        output, certificate_5 = render(stdout_bytes)
        new_size = len(output.encode("utf-8"))
        if new_size == stdout_bytes:
            break
        stdout_bytes = new_size
    output, certificate_5 = render(stdout_bytes)
    final_size = len(output.encode("utf-8"))
    if final_size != stdout_bytes:
        stdout_bytes = final_size
        output, certificate_5 = render(stdout_bytes)
        final_size = len(output.encode("utf-8"))
    if final_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", final_size, STDOUT_LIMIT_BYTES))
    sys.stdout.write(output)
    return 0 if all(
        (
            certificate_1,
            certificate_2,
            certificate_3,
            certificate_4,
            certificate_5,
            final_size == stdout_bytes,
        )
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
