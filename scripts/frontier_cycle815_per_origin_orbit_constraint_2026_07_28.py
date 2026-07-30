#!/usr/bin/env python3
"""Cycle 815 v2: adopt the origin-rotation witness and quotient allocations.

The Cycle-786, Cycle-805, and Cycle-808 pairs are SHA-pinned text/AST inputs
and runtime-blocklisted.  Their finite consequences and the independent
checker's station-shift/origin-rotation witness are reimplemented here.  The
landed 46-event control is rebuilt only from the lower Cycle-719/750 machinery.

Boundary: exact finite counts, actions, and orbit quotients only; no
probability, physical split rule, or choice between the two honest readings.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle786_support_independent_check_2026_07_28.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle805_relabeling_independent_check_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_independent_check_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[1]:
        "7fdb18bba74a6163a7eae6d080f666a95dbe71f93d88ba9f44da6efc157af7b9",
    AUDIT_INPUT_PATHS[2]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[3]:
        "dca858db349bddeb2e4e800bf68a0be2f9fabf076529decf7f3700c26a45655f",
    AUDIT_INPUT_PATHS[4]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[5]:
        "8a717469dfb092ff0fc4e1b39be98c85ceea2ff8256bcaead73a93664867fdac",
    AUDIT_INPUT_PATHS[6]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[7]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[1]: "6d45253baab8040af57582b2fe64bbf49e7ab8e4",
    AUDIT_INPUT_PATHS[2]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[3]: "386face671529fd0fef505d9b04676b42a8b5d97",
    AUDIT_INPUT_PATHS[4]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[5]: "3a5062ecaba514fda64440c1517c0dfefcfcb6e5",
    AUDIT_INPUT_PATHS[6]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[7]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
SOURCE_COMMITS = {
    "cycle786_pair": "6a4d3a49f68808236403fe6310097459c2f7c07a",
    "cycle808_pair": "74eddf76c0759366eba0b4f245768a627aa41379",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle786_ensemble_support_census_2026_07_28",
    "frontier_cycle786_support_independent_check_2026_07_28",
    "frontier_cycle805_supply_relabeling_tournament_2026_07_28",
    "frontier_cycle805_relabeling_independent_check_2026_07_28",
    "frontier_cycle808_uniformity_from_relabeling_2026_07_28",
    "frontier_cycle808_uniformity_independent_check_2026_07_28",
    "frontier_cycle815_orbit_independent_check_2026_07_28",
)

import ast
from collections import Counter, deque
from hashlib import sha1, sha256
import importlib.abc
import json
from math import comb, gcd
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()


class _CarriedPackageBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PACKAGE_BLOCKER = _CarriedPackageBlocker()
sys.meta_path.insert(0, PACKAGE_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


ORIGINS = tuple(range(12))
POSITIVE_ORIGINS = tuple(range(6))
NEGATIVE_ORIGINS = tuple(range(6, 12))
ALLOCATION_BANKS = (2, 5, 12)
ALL_BANKS = (1, 2, 3, 5, 12)
STATIONS = {2: 11, 5: 35, 12: 91}
GROUP_TOTAL = 19
GROUP_BINS = 6
WITNESS_NAME = (
    "BANK_TYPED_STATION_SHIFT_1_WITHIN_ORIENTATION_ORIGIN_ROTATION_1"
)
WITNESS_STATION_SHIFTS = (1, 1, 1)
V1_ERROR_VERBATIM = (
    "absence of an origin coordinate does not derive its identity action, "
    "and the identity lift of F does not preserve the Cycle786 "
    "origin-to-orientation catalog"
)
V1_REFUTATION_VERBATIM = (
    "REFUTED: G' has no supplied action on the Cycle786 matter-origin "
    "coordinate; moreover F's identity lift is incompatible with the origin "
    "catalog, while the lawful involution o<6 ? o+6 : o-6 moves every origin."
)
G_PRIME_GENERATORS = (
    "I1_SOURCE_1",
    "I1_SOURCE_LAST",
    "I2_ROTATE_1",
    "I2_ROTATE_LAST",
    "I3_Q_THEN_R_DESCENDING",
    "I3_Q_THEN_R_EVEN_THEN_ODD",
    "I3_R_THEN_Q_ASCENDING",
    "I3_R_THEN_Q_DESCENDING",
    "I3_R_THEN_Q_EVEN_THEN_ODD",
    "F_XOR_LIFT",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    result: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                result[target.id] = value
    return result


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function cardinality", name, len(rows)))
    return rows[0]


def source_controls() -> dict[str, object]:
    sources = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(source, filename=path)
        for path, source in sources.items()
    }
    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=str(Path(__file__)))
    own_assignments = top_level_assignments(own_tree)
    imported: list[str] = []
    dynamic: list[str] = []
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
            dynamic.append(node.args[0].value)

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

    p786, c786, p805, c805, p808, c808, _p750, _p719 = AUDIT_INPUT_PATHS
    origin_catalog = function_node(trees[p786], "derive_origin_catalog")
    mapping_805 = function_node(trees[p805], "mapping_table")
    mapping_805_check = function_node(trees[c805], "mapping_certificate")
    maps_808 = function_node(trees[p808], "spec_bank_maps")
    g_808 = function_node(trees[p808], "map_occurrence_by_g")
    f_808 = function_node(trees[p808], "map_occurrence_by_flip")
    source_domain_literals = {
        node.value
        for function in (mapping_805, mapping_805_check, maps_808)
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    moved_808_dump = ast.dump(g_808) + ast.dump(f_808)
    origin_dump = ast.dump(origin_catalog)
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
            for name in dynamic
        ),
        "blocklisted_not_loaded": all(
            name not in sys.modules for name in BLOCKLISTED_MODULES
        ),
        "runtime_blocker_installed": PACKAGE_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "checker_runtime_blocklisted": runtime_attempts[
            "frontier_cycle815_orbit_independent_check_2026_07_28"
        ],
        "cycle786_origin_catalog_reconstructed_from_AST_text": all(
            token in origin_dump
            for token in (
                "Name(id='origin'",
                "LShift",
                "Constant(value=12)",
                "Constant(value='origin')",
                "keyword(arg='matter'",
            )
        ),
        "cycle786_allocation_anchors": all(
            token in sources[p786] + sources[c786]
            for token in (
                '"orientation": 1 if origin < 6 else -1',
                '"origin": origin',
                '"orientation_counts": {"+1": 19, "-1": 19}',
                "range_audit = weak_composition_audit(19, 6)",
            )
        ),
        "cycle805_checkpoint_domains_reconstructed_from_AST_text": {
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
        } >= {
            "station_labels",
            "physical_track_site_slots",
            "logical_bank_indices",
            "epochs",
            "layer_slots",
            "q_traversal_slots",
        },
        "cycle805_maps_omit_origin_and_matter": (
            "origin" not in ast.dump(mapping_805).lower()
            and "matter" not in ast.dump(mapping_805).lower()
            and "origin" not in ast.dump(mapping_805_check).lower()
            and "matter" not in ast.dump(mapping_805_check).lower()
        ),
        "cycle808_actions_omit_origin_and_matter": (
            "origin" not in moved_808_dump.lower()
            and "matter" not in moved_808_dump.lower()
        ),
        "cycle808_flip_anchors": all(
            token in sources[p808] + sources[c808]
            for token in (
                "return bank, int(epoch) ^ 1, swapped, -int(orientation), selected",
                "the unique XOR mask transporting paired states x,y is x XOR y",
                "checkpoint",
            )
        ),
        "v1_error_stated_verbatim": (
            ast.literal_eval(own_assignments["V1_ERROR_VERBATIM"])
            == V1_ERROR_VERBATIM
            and ast.literal_eval(own_assignments["V1_REFUTATION_VERBATIM"])
            == V1_REFUTATION_VERBATIM
        ),
        "v2_status_keys_literal": all(
            token in own_source
            for token in (
                '"vacuous_verdict": "RETRACTED"',
                '"witness_source": "independent_checker"',
                '"fixed_allocations": fixed["fixed_allocations"]',
            )
        ),
    }


def weak_compositions(total: int, bins: int) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []

    def visit(remaining: int, positions: int, prefix: tuple[int, ...]) -> None:
        if positions == 1:
            rows.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            visit(remaining - value, positions - 1, prefix + (value,))

    visit(total, bins, ())
    return tuple(rows)


def lawful_group_allocation(values: tuple[int, ...]) -> bool:
    return (
        len(values) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in values)
        and sum(values) == GROUP_TOTAL
    )


def allocation_certificate() -> dict[str, object]:
    allocations = weak_compositions(GROUP_TOTAL, GROUP_BINS)
    return {
        "allocations": allocations,
        "origins": ORIGINS,
        "orientation_groups": {
            "+1": POSITIVE_ORIGINS,
            "-1": NEGATIVE_ORIGINS,
        },
        "total_per_group": GROUP_TOTAL,
        "bins_per_group": GROUP_BINS,
        "lawfulness": "six nonnegative integer counts summing to 19",
        "allocation_count": len(allocations),
        "closed_form_count": comb(GROUP_TOTAL + GROUP_BINS - 1, GROUP_BINS - 1),
        "all_lawful": all(lawful_group_allocation(row) for row in allocations),
        "allocation_sha256": digest(allocations),
    }


def orientation(origin: int) -> int:
    return 1 if origin < 6 else -1


def compose(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[int, ...]:
    """Return left after right."""
    return tuple(left[right[index]] for index in range(len(right)))


def permutation_cycles(
    permutation: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(permutation)))
    result = []
    while unseen:
        start = min(unseen)
        cycle = []
        point = start
        while point not in cycle:
            cycle.append(point)
            unseen.discard(point)
            point = permutation[point]
        result.append(tuple(cycle))
    return tuple(result)


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


def full_805_checkpoint_bar(
    shifts: tuple[int, int, int],
) -> dict[str, object]:
    """Reimplement the checker's full arbitrary-data checkpoint bar."""
    comparisons = 0
    leg_comparisons = Counter()
    failures = []
    bank_comparisons = Counter()
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
            for leg in ("forward", "inverse"):
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
                        leg_comparisons[leg] += 1
                        bank_comparisons[bank] += 1
                        expected_role = base_program[base_active]
                        if not all(
                            (
                                mapping[base_active] == varied_active,
                                relabeled_program[varied_active] == expected_role,
                                alternative_program[varied_active] == expected_role,
                            )
                        ):
                            failures.append(
                                {
                                    "bank": bank,
                                    "event": event,
                                    "leg": leg,
                                    "start": start,
                                    "checkpoint": checkpoint,
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
    expected_by_bank = {
        bank: 4 * bank * STATIONS[bank] ** 2
        for bank in ALLOCATION_BANKS
    }
    return {
        "shifts_by_bank": dict(zip(ALLOCATION_BANKS, shifts, strict=True)),
        "declared_bar":
            "every event, forward/inverse leg, token start, and complete-step "
            "checkpoint: cyclic successor/predecessor, relabeled-program role "
            "incidence, and rotated-alternative role incidence (the Cycle805 "
            "arbitrary-data symbolic commutation bar)",
        "comparisons": comparisons,
        "comparisons_by_bank": dict(bank_comparisons),
        "expected_comparisons_by_bank": expected_by_bank,
        "comparisons_by_leg": dict(leg_comparisons),
        "failure": failures[:1],
        "commutes": (
            not failures
            and dict(bank_comparisons) == expected_by_bank
            and leg_comparisons["forward"] == leg_comparisons["inverse"]
        ),
    }


def origin_action_certificate(controls: dict[str, object]) -> dict[str, object]:
    """Adopt and independently reconstruct the checker's moving witness."""
    identity = ORIGINS
    # These are the v1 identity lifts being retracted, retained only as an
    # explicit incompatibility control.  They are not the v2 origin action.
    v1_generator_origin_permutations = {
        name: identity for name in G_PRIME_GENERATORS
    }
    half_swap = tuple(
        origin + 6 if origin < 6 else origin - 6
        for origin in ORIGINS
    )
    v1_F_identity_catalog_compatible = all(
        orientation(identity[origin]) == -orientation(origin)
        for origin in ORIGINS
    )
    half_swap_catalog_compatible = all(
        orientation(half_swap[origin]) == -orientation(origin)
        for origin in ORIGINS
    )

    witness = origin_fiber_rotation(1, 1)
    witness_cycles = permutation_cycles(witness)
    powers = [tuple(range(12))]
    for _power in range(1, 6):
        powers.append(compose(witness, powers[-1]))
    witness_powers = tuple(powers)
    checkpoint_bar = full_805_checkpoint_bar(WITNESS_STATION_SHIFTS)
    orientation_preserved = all(
        orientation(witness[origin]) == orientation(origin)
        for origin in ORIGINS
    )
    witness_valid = all(
        (
            checkpoint_bar["commutes"],
            set(witness) == set(ORIGINS),
            all(witness[origin] != origin for origin in ORIGINS),
            orientation_preserved,
            witness_cycles == (POSITIVE_ORIGINS, NEGATIVE_ORIGINS),
            len(set(witness_powers)) == 6,
            witness_powers[-1] != identity,
            compose(witness, witness_powers[-1]) == identity,
            controls["cycle805_maps_omit_origin_and_matter"],
        )
    )
    return {
        "witness_source": "independent_checker",
        "witness_name": WITNESS_NAME,
        "station_shifts": WITNESS_STATION_SHIFTS,
        "origin_permutation": witness,
        "origin_cycles": witness_cycles,
        "moves_every_origin": all(
            witness[origin] != origin for origin in ORIGINS
        ),
        "orientation_preserved": orientation_preserved,
        "group_generated": "C6=<W>",
        "group_order": len(set(witness_powers)),
        "group_elements": witness_powers,
        "full_805_checkpoint_bar": checkpoint_bar,
        "commutes_at_full_805_checkpoint_bar": checkpoint_bar["commutes"],
        "product_coordinate_commutation_basis": (
            "The landed Cycle805 checkpoint coordinates omit matter-origin; "
            "the station action passes every checkpoint, and the adjoined "
            "origin rotation preserves each Cycle786 orientation fiber."
        ),
        "v1_identity_generators_checked": tuple(
            v1_generator_origin_permutations
        ),
        "v1_F_identity_lift_catalog_compatible":
            v1_F_identity_catalog_compatible,
        "compatible_F_half_swap": half_swap,
        "compatible_F_half_swap_catalog_compatible":
            half_swap_catalog_compatible,
        "v1_error_verbatim": V1_ERROR_VERBATIM,
        "v1_refutation_verbatim": V1_REFUTATION_VERBATIM,
        "vacuous_verdict": "RETRACTED",
        "action_status":
            "MOVING_COMMUTING_ORIGIN_ROTATION_WITNESS_ADOPTED",
        "witness_valid": witness_valid,
    }


def rotate_allocation(
    values: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    output = [0] * len(values)
    for source, value in enumerate(values):
        output[(source + shift) % len(values)] = value
    return tuple(output)


def fixed_point_certificate(
    allocation: dict[str, object],
    action: dict[str, object],
) -> dict[str, object]:
    allocations = allocation["allocations"]
    fixed_by_power = {
        power: sum(
            rotate_allocation(row, power) == row
            for row in allocations
        )
        for power in range(action["group_order"])
    }
    witness_fixed = tuple(
        row for row in allocations if rotate_allocation(row, 1) == row
    )
    divisibility_obstruction = {
        power: {
            "coordinate_cycle_length": 6 // gcd(6, power),
            "cycle_length_divides_total_19":
                GROUP_TOTAL % (6 // gcd(6, power)) == 0,
        }
        for power in range(1, 6)
    }
    return {
        "unconstrained_allocations_per_group": len(allocations),
        "fixed_allocations": len(witness_fixed),
        "fixed_allocations_per_group": len(witness_fixed),
        "fixed_by_group_power": fixed_by_power,
        "fixed_witness_sha256": digest(witness_fixed),
        "positive_fixed_allocations": len(witness_fixed),
        "negative_fixed_allocations": len(witness_fixed),
        "combined_fixed_allocations": len(witness_fixed) ** 2,
        "divisibility_obstruction": divisibility_obstruction,
        "finding":
            "0/42,504 allocations per group are invariant under the witness.",
        "pass": all(
            (
                len(allocations) == 42_504,
                fixed_by_power == {
                    0: 42_504,
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                },
                not witness_fixed,
                all(
                    not row["cycle_length_divides_total_19"]
                    for row in divisibility_obstruction.values()
                ),
            )
        ),
    }


def quotient_certificate(
    allocation: dict[str, object],
    fixed: dict[str, object],
) -> dict[str, object]:
    allocations = allocation["allocations"]
    remaining = set(allocations)
    representatives = []
    size_distribution = Counter()
    partition_members = 0
    while remaining:
        seed = min(remaining)
        orbit = {
            rotate_allocation(seed, power)
            for power in range(6)
        }
        representatives.append(min(orbit))
        size_distribution[len(orbit)] += 1
        partition_members += len(orbit)
        remaining.difference_update(orbit)
    burnside_numerator = sum(fixed["fixed_by_group_power"].values())
    burnside_orbits = burnside_numerator // 6
    representatives_tuple = tuple(representatives)
    return {
        "space": "42,504 lawful allocations for one orientation group",
        "group_used": (
            "C6=<W>, the restriction of the verified witness to either "
            "six-origin orientation fiber"
        ),
        "additional_generators_used": (),
        "group_order": 6,
        "orbit_count": len(representatives_tuple),
        "allocation_orbit_count": len(representatives_tuple),
        "orbit_size_distribution": dict(sorted(size_distribution.items())),
        "partition_member_count": partition_members,
        "burnside_fixed_sum": burnside_numerator,
        "burnside_orbit_count": burnside_orbits,
        "free_action": fixed["fixed_by_group_power"] == {
            0: 42_504,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        },
        "representative_sha256": digest(representatives_tuple),
        "combined_two_group_note": (
            "This certificate quotients the requested 42,504-allocation "
            "space per orientation group; it does not add an unverified "
            "independent second generator on the product of the two groups."
        ),
        "pass": all(
            (
                len(representatives_tuple) == 7_084,
                dict(size_distribution) == {6: 7_084},
                partition_members == 42_504,
                burnside_numerator == 42_504,
                burnside_orbits == 7_084,
                not remaining,
            )
        ),
    }


def landed_occurrence_rows() -> tuple[tuple[object, ...], ...]:
    """Rebuild the 46 landed label rows from lower landed machinery."""
    rows = []
    for bank in ALL_BANKS:
        fixtures = S750.k_epoch_fixtures(bank)
        for event, direction, program, before, expected in fixtures:
            selected = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank,
                tuple(range(len(program))),
            )
            banks, links = K719.M.unpack_state(expected, bank)
            chain, decode_order = K719.B.decode_local_graph(banks, links)
            cell = chain.cells[event]
            rows.append(
                (
                    int(bank),
                    int(event),
                    tuple(map(int, direction)),
                    int(cell.orientation),
                    tuple(map(int, selected)),
                    len(program),
                    tuple(decode_order[event]),
                )
            )
    return tuple(rows)


def landed_data_certificate(
    allocation: dict[str, object],
    action: dict[str, object],
    fixed: dict[str, object],
    quotient: dict[str, object],
) -> dict[str, object]:
    rows = landed_occurrence_rows()
    projected = tuple(row for row in rows if row[0] in ALLOCATION_BANKS)
    full_counts = Counter(int(row[3]) for row in rows)
    projected_counts = Counter(int(row[3]) for row in projected)
    extra_counts = full_counts - projected_counts
    allocations = allocation["allocations"]
    counts_preserved_for_every_allocation_and_power = all(
        sum(rotate_allocation(row, power)) == GROUP_TOTAL
        for row in allocations
        for power in range(action["group_order"])
    )
    identity_controls_pass = all(
        (
            len(rows) == 46,
            full_counts == Counter({1: 23, -1: 23}),
            len(projected) == 38,
            projected_counts == Counter({1: 19, -1: 19}),
            extra_counts == Counter({1: 4, -1: 4}),
            all(tuple(row[4]) == (0,) for row in rows),
        )
    )
    counts_are_orbit_invariants = all(
        (
            action["orientation_preserved"],
            counts_preserved_for_every_allocation_and_power,
            quotient["partition_member_count"] == len(allocations),
            all(lawful_group_allocation(row) for row in allocations),
        )
    )
    return {
        "full_landed_46_event_count": len(rows),
        "full_orientation_counts": {"+1": full_counts[1], "-1": full_counts[-1]},
        "counts_by_bank": {
            str(bank): sum(int(row[0]) == bank for row in rows)
            for bank in ALL_BANKS
        },
        "cycle786_projection_event_count": len(projected),
        "cycle786_projection_orientation_counts": {
            "+1": projected_counts[1],
            "-1": projected_counts[-1],
        },
        "outside_projection_orientation_counts": {
            "+1": extra_counts[1],
            "-1": extra_counts[-1],
        },
        "landed_rows_sha256": digest(rows),
        "allocation_projection_rows_sha256": digest(projected),
        "identity_controls_pass": identity_controls_pass,
        "counts_preserved_for_every_allocation_and_power":
            counts_preserved_for_every_allocation_and_power,
        "counts_are_orbit_invariants": counts_are_orbit_invariants,
        "all_allocation_orbits_compatible_with_landed_counts":
            counts_are_orbit_invariants,
        "specific_origin_counts_landed": None,
        "specific_origin_status": "UNDETERMINED_BY_LANDED_SURFACES",
        "branch_i": (
            "No symmetry-invariant per-origin allocation exists."
        ),
        "branch_ii": (
            "Any realized allocation distinguishes origins that the landed "
            "dynamics does not: the per-origin refinement requires "
            "symmetry-breaking input OR the physical object is the orbit "
            "class.  Nothing landed decides between these readings."
        ),
        "branch_iii": (
            "The landed battery counts are compatible with every allocation "
            "orbit because the counts are orbit-invariants."
        ),
        "honest_dichotomy_decided_by_landed_data": False,
        "pass": all(
            (
                identity_controls_pass,
                fixed["fixed_allocations"] == 0,
                counts_are_orbit_invariants,
            )
        ),
    }


def build_core(controls: dict[str, object]) -> dict[str, object]:
    allocation = allocation_certificate()
    action = origin_action_certificate(controls)
    fixed = fixed_point_certificate(allocation, action)
    quotient = quotient_certificate(allocation, fixed)
    landed = landed_data_certificate(
        allocation,
        action,
        fixed,
        quotient,
    )
    allocation_summary = {
        key: value for key, value in allocation.items() if key != "allocations"
    }
    return {
        "allocation": allocation_summary,
        "origin_action": action,
        "fixed_point_census": fixed,
        "allocation_quotient": quotient,
        "two_branch_reading": landed,
        "vacuous_verdict": "RETRACTED",
        "witness_source": "independent_checker",
        "fixed_allocations": fixed["fixed_allocations"],
        "allocation_orbit_count": quotient["allocation_orbit_count"],
        "orbit_size_distribution": quotient["orbit_size_distribution"],
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


def main() -> int:
    input_sha_before = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    input_blob_before = {
        path: git_blob_sha1((ROOT / path).read_bytes())
        for path in AUDIT_INPUT_PATHS
    }
    indexed_blobs = git_index_blobs(AUDIT_INPUT_PATHS)
    controls = source_controls()
    first = build_core(controls)
    second = build_core(controls)
    input_sha_after = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    input_blob_after = {
        path: git_blob_sha1((ROOT / path).read_bytes())
        for path in AUDIT_INPUT_PATHS
    }
    elapsed = monotonic() - START
    deterministic = first == second

    allocation = first["allocation"]
    action = first["origin_action"]
    fixed = first["fixed_point_census"]
    quotient = first["allocation_quotient"]
    landed = first["two_branch_reading"]
    certificate_a = all(
        (
            controls["cycle786_origin_catalog_reconstructed_from_AST_text"],
            controls["cycle805_checkpoint_domains_reconstructed_from_AST_text"],
            controls["cycle805_maps_omit_origin_and_matter"],
            controls["cycle808_actions_omit_origin_and_matter"],
            controls["cycle808_flip_anchors"],
            controls["v1_error_stated_verbatim"],
            allocation["allocation_count"] == 42_504,
            not action["v1_F_identity_lift_catalog_compatible"],
            action["compatible_F_half_swap_catalog_compatible"],
            action["origin_cycles"]
            == (POSITIVE_ORIGINS, NEGATIVE_ORIGINS),
            action["moves_every_origin"],
            action["commutes_at_full_805_checkpoint_bar"],
            action["full_805_checkpoint_bar"]["comparisons"] == 422_956,
            action["witness_valid"],
            action["vacuous_verdict"] == "RETRACTED",
        )
    )
    certificate_b = all(
        (
            fixed["pass"],
            fixed["unconstrained_allocations_per_group"] == 42_504,
            fixed["fixed_allocations"] == 0,
            fixed["positive_fixed_allocations"] == 0,
            fixed["negative_fixed_allocations"] == 0,
            fixed["combined_fixed_allocations"] == 0,
            landed["identity_controls_pass"],
            landed["full_orientation_counts"] == {"+1": 23, "-1": 23},
            landed["cycle786_projection_orientation_counts"]
            == {"+1": 19, "-1": 19},
        )
    )
    certificate_c = all(
        (
            quotient["pass"],
            quotient["group_order"] == 6,
            quotient["allocation_orbit_count"] == 7_084,
            quotient["orbit_size_distribution"] == {6: 7_084},
            quotient["partition_member_count"] == 42_504,
            quotient["burnside_orbit_count"] == 7_084,
            quotient["free_action"],
        )
    )
    certificate_d = all(
        (
            landed["pass"],
            landed["counts_are_orbit_invariants"],
            landed["all_allocation_orbits_compatible_with_landed_counts"],
            landed["specific_origin_counts_landed"] is None,
            not landed["honest_dichotomy_decided_by_landed_data"],
            "symmetry-breaking input OR the physical object is the orbit class"
            in landed["branch_ii"],
        )
    )

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
        "checker_runtime_blocklisted",
        "cycle786_origin_catalog_reconstructed_from_AST_text",
        "cycle786_allocation_anchors",
        "cycle805_checkpoint_domains_reconstructed_from_AST_text",
        "cycle805_maps_omit_origin_and_matter",
        "cycle808_actions_omit_origin_and_matter",
        "cycle808_flip_anchors",
        "v1_error_stated_verbatim",
        "v2_status_keys_literal",
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

    def render(stdout_bytes: int) -> tuple[str, bool]:
        certificate_e = controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
        certificates = {
            "A_CORRECTED_ORIGIN_ACTION": certificate_a,
            "B_FIXED_POINT_CENSUS": certificate_b,
            "C_ALLOCATION_QUOTIENT": certificate_c,
            "D_TWO_BRANCH_READING": certificate_d,
            "E_CONTROLS": certificate_e,
        }
        lines = [
            "BOUNDARY exact finite counts, actions, and orbit quotients only; "
            "no probability, physical split rule, or dichotomy choice",
        ]
        for path in AUDIT_INPUT_PATHS:
            lines.append(
                "AUDIT_INPUT_SHA "
                + compact(
                    {
                        "path": path,
                        "sha256": input_sha_after[path],
                        "git_blob_sha1": input_blob_after[path],
                        "indexed_blob_sha1": indexed_blobs.get(path),
                    }
                )
            )
        lines.append("SOURCE_COMMITS " + compact(SOURCE_COMMITS))
        lines.append("V1_ERROR_VERBATIM " + V1_ERROR_VERBATIM)
        lines.append("V1_REFUTATION_VERBATIM " + V1_REFUTATION_VERBATIM)
        lines.append(
            "CERTIFICATE_A_CORRECTED_ORIGIN_ACTION "
            + compact({"pass": certificate_a, **action})
        )
        lines.append(
            "ORIGIN_ACTION_TWO_SIX_CYCLES "
            + compact(action["origin_cycles"])
        )
        lines.append(
            "FULL_805_CHECKPOINT_BAR "
            + compact(action["full_805_checkpoint_bar"])
        )
        lines.append(
            "CERTIFICATE_B_FIXED_POINT_CENSUS "
            + compact({"pass": certificate_b, **fixed})
        )
        lines.append(
            "FIXED_POINT_CENSUS 0/42,504 allocations per group"
        )
        lines.append(
            "IDENTITY_CONTROLS "
            + compact(
                {
                    "pass": landed["identity_controls_pass"],
                    "full": landed["full_orientation_counts"],
                    "projection":
                        landed["cycle786_projection_orientation_counts"],
                }
            )
        )
        lines.append(
            "CERTIFICATE_C_ALLOCATION_QUOTIENT "
            + compact({"pass": certificate_c, **quotient})
        )
        lines.append(
            "ORBIT_CENSUS "
            + compact(
                {
                    "orbit_count": quotient["allocation_orbit_count"],
                    "orbit_size_distribution":
                        quotient["orbit_size_distribution"],
                }
            )
        )
        lines.append(
            "CERTIFICATE_D_TWO_BRANCH_READING "
            + compact({"pass": certificate_d, **landed})
        )
        lines.append("SCOPED_FINDING_I " + landed["branch_i"])
        lines.append("SCOPED_FINDING_II " + landed["branch_ii"])
        lines.append("SCOPED_FINDING_III " + landed["branch_iii"])
        lines.append(
            "CERTIFICATE_E_CONTROLS "
            + compact(
                {
                    "pass": certificate_e,
                    "source_controls": controls,
                    "input_sha_stable": input_sha_before == input_sha_after,
                    "git_blob_sha_stable":
                        input_blob_before == input_blob_after,
                    "indexed_at_expected_blobs":
                        indexed_blobs == EXPECTED_GIT_BLOB_SHA1,
                    "checker_runtime_blocklisted":
                        controls["checker_runtime_blocklisted"],
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
            "version": 2,
            "certificates": certificates,
            "all_pass": all(certificates.values()),
            "vacuous_verdict": "RETRACTED",
            "witness_source": "independent_checker",
            "witness_name": action["witness_name"],
            "witness_origin_cycles": action["origin_cycles"],
            "fixed_allocations": fixed["fixed_allocations"],
            "unconstrained_allocations_per_group":
                fixed["unconstrained_allocations_per_group"],
            "allocation_orbit_count": quotient["allocation_orbit_count"],
            "orbit_size_distribution": quotient["orbit_size_distribution"],
            "landed_counts_are_orbit_invariants":
                landed["counts_are_orbit_invariants"],
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
            "CYCLE815_V2_ALLOCATION_QUOTIENT_CERTIFIED"
            if report["all_pass"]
            else "CYCLE815_V2_CERTIFICATE_FAILURE"
        )
        return "\n".join(lines) + "\n", certificate_e

    stdout_bytes = 0
    output = ""
    certificate_e = False
    for _iteration in range(12):
        output, certificate_e = render(stdout_bytes)
        new_size = len(output.encode("utf-8"))
        if new_size == stdout_bytes:
            break
        stdout_bytes = new_size
    output, certificate_e = render(stdout_bytes)
    final_size = len(output.encode("utf-8"))
    if final_size != stdout_bytes:
        stdout_bytes = final_size
        output, certificate_e = render(stdout_bytes)
        final_size = len(output.encode("utf-8"))
    if final_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", final_size, STDOUT_LIMIT_BYTES))
    sys.stdout.write(output)
    return 0 if all(
        (
            certificate_a,
            certificate_b,
            certificate_c,
            certificate_d,
            certificate_e,
            final_size == stdout_bytes,
        )
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
