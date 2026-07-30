#!/usr/bin/env python3
"""Cycle 815: apply the Cycle-808 G' label symmetry to Cycle-786 origins.

The Cycle-786 and Cycle-808 pairs are SHA-pinned text/AST inputs and are
runtime-blocklisted.  Their finite allocation and label-action consequences
are reimplemented here.  The landed 46-event battery is rebuilt only from the
lower Cycle-719/750 machinery.

Boundary: exact finite counts and support only; no probability or split rule.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle786_support_independent_check_2026_07_28.py",
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
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[3]:
        "8a717469dfb092ff0fc4e1b39be98c85ceea2ff8256bcaead73a93664867fdac",
    AUDIT_INPUT_PATHS[4]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[5]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[1]: "6d45253baab8040af57582b2fe64bbf49e7ab8e4",
    AUDIT_INPUT_PATHS[2]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[3]: "3a5062ecaba514fda64440c1517c0dfefcfcb6e5",
    AUDIT_INPUT_PATHS[4]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[5]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
SOURCE_COMMITS = {
    "cycle786_pair": "6a4d3a49f68808236403fe6310097459c2f7c07a",
    "cycle808_pair": "74eddf76c0759366eba0b4f245768a627aa41379",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle786_ensemble_support_census_2026_07_28",
    "frontier_cycle786_support_independent_check_2026_07_28",
    "frontier_cycle808_uniformity_from_relabeling_2026_07_28",
    "frontier_cycle808_uniformity_independent_check_2026_07_28",
)

import ast
from collections import Counter, deque
from hashlib import sha1, sha256
import importlib.abc
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()


class _CarriedPairBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PAIR_BLOCKER = _CarriedPairBlocker()
sys.meta_path.insert(0, PAIR_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


ORIGINS = tuple(range(12))
POSITIVE_ORIGINS = tuple(range(6))
NEGATIVE_ORIGINS = tuple(range(6, 12))
ALLOCATION_BANKS = (2, 5, 12)
ALL_BANKS = (1, 2, 3, 5, 12)
GROUP_TOTAL = 19
GROUP_BINS = 6
G_ORDER = 58_599_022_482_000
G_PRIME_ORDER = 117_198_044_964_000
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
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    output: dict[str, ast.AST] = {}
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
                output[target.id] = value
    return output


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function cardinality", name, len(matches)))
    return matches[0]


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

    primary786 = sources[AUDIT_INPUT_PATHS[0]]
    checker786 = sources[AUDIT_INPUT_PATHS[1]]
    primary808 = sources[AUDIT_INPUT_PATHS[2]]
    checker808 = sources[AUDIT_INPUT_PATHS[3]]
    g_map = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "map_occurrence_by_g"
    )
    flip_map = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "map_occurrence_by_flip"
    )
    orbit_builder = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "all_label_orbits"
    )
    moved_action_names = {
        node.id
        for function in (g_map, flip_map)
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
    }
    orbit_literals = {
        node.value
        for node in ast.walk(orbit_builder)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
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
        "runtime_blocker_installed": PAIR_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "cycle786_allocation_anchors": all(
            token in checker786
            for token in (
                "range_audit = weak_composition_audit(19, 6)",
                'range_audit["weak_compositions_enumerated"] == 42_504',
                '"orientation_counts": {"+1": 19, "-1": 19}',
            )
        ),
        "cycle786_origin_partition_anchors": all(
            token in primary786
            for token in (
                "for origin in range(12)",
                '"orientation": 1 if origin < 6 else -1',
                '"origin": origin',
            )
        ),
        "cycle808_exact_group_anchors": all(
            token in primary808 + checker808
            for token in (
                "58_599_022_482_000",
                "117198044964000",
                "EXPECTED_STATIONS = {1: 3, 2: 11, 3: 19, 5: 35, 12: 91}",
            )
        ),
        "cycle808_action_has_no_origin_coordinate": (
            "origin" not in moved_action_names
            and "origin" not in orbit_literals
            and "return bank, epoch, direction, orientation, mapped_selected"
            in primary808
            and (
                "return bank, int(epoch) ^ 1, swapped, "
                "-int(orientation), selected"
            ) in primary808
        ),
        "cycle808_scope_excludes_global_state_action": (
            "not a global automorphism claim on all binary states"
            in primary808
            and "landed 46-event forward/inverse complete-step checkpoint"
            in primary808
        ),
    }


def weak_compositions(total: int, bins: int) -> tuple[tuple[int, ...], ...]:
    output: list[tuple[int, ...]] = []

    def visit(remaining: int, positions: int, prefix: tuple[int, ...]) -> None:
        if positions == 1:
            output.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            visit(remaining - value, positions - 1, prefix + (value,))

    visit(total, bins, ())
    return tuple(output)


def lawful_group_allocation(values: tuple[int, ...]) -> bool:
    return (
        len(values) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in values)
        and sum(values) == GROUP_TOTAL
    )


def allocation_certificate() -> dict[str, object]:
    allocations = weak_compositions(GROUP_TOTAL, GROUP_BINS)
    possible_values = tuple(
        tuple(sorted({row[index] for row in allocations}))
        for index in range(GROUP_BINS)
    )
    return {
        "origins": ORIGINS,
        "orientation_groups": {
            "+1": POSITIVE_ORIGINS,
            "-1": NEGATIVE_ORIGINS,
        },
        "total_per_group": GROUP_TOTAL,
        "bins_per_group": GROUP_BINS,
        "lawfulness": "six nonnegative integer counts summing to 19",
        "allocations": allocations,
        "allocation_count": len(allocations),
        "closed_form_count": comb(GROUP_TOTAL + GROUP_BINS - 1, GROUP_BINS - 1),
        "possible_values_by_origin": possible_values,
        "all_lawful": all(lawful_group_allocation(row) for row in allocations),
        "allocation_sha256": digest(allocations),
    }


def push_allocation(
    values: tuple[int, ...],
    permutation: tuple[int, ...],
) -> tuple[int, ...]:
    if len(values) != len(permutation):
        raise ValueError("allocation/permutation size mismatch")
    output = [0] * len(values)
    for source, target in enumerate(permutation):
        output[target] = values[source]
    return tuple(output)


def permutation_orbits(
    points: tuple[int, ...],
    generators: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    remaining = set(points)
    output = []
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
        ordered = tuple(sorted(orbit))
        output.append(ordered)
        remaining.difference_update(orbit)
    return tuple(output)


def lawful_full_allocation(values: tuple[int, ...]) -> bool:
    return (
        len(values) == len(ORIGINS)
        and all(type(value) is int and value >= 0 for value in values)
        and sum(values[:6]) == GROUP_TOTAL
        and sum(values[6:]) == GROUP_TOTAL
    )


def origin_action_certificate(
    allocation: dict[str, object],
    controls: dict[str, object],
) -> dict[str, object]:
    """Restrict the declared G' coordinate action to the origin coordinate.

    Cycle 808's declared label tuple has no origin coordinate, and its XOR
    action is explicitly not global on binary states.  Thus no nonidentity
    origin permutation is supplied.  On an augmented (label, origin) object,
    the only action inherited without a new lift is the pointwise identity on
    origin.  Every word in the ten displayed generators therefore restricts
    to identity on the origin coordinate.
    """
    identity = ORIGINS
    generators = {
        name: identity for name in G_PRIME_GENERATORS
    }
    generator_permutations = tuple(generators.values())
    orbits = permutation_orbits(ORIGINS, generator_permutations)
    allocations = allocation["allocations"]
    reference = (GROUP_TOTAL,) + (0,) * (GROUP_BINS - 1)
    positive_cases = tuple(row + reference for row in allocations)
    negative_cases = tuple(reference + row for row in allocations)
    lawfulness_cases = 0
    lawfulness_preserved = True
    for permutation in generator_permutations:
        for values in positive_cases + negative_cases:
            lawfulness_cases += 1
            lawfulness_preserved &= (
                lawful_full_allocation(values)
                and lawful_full_allocation(push_allocation(values, permutation))
            )
    return {
        "G_order": G_ORDER,
        "G_prime_order": G_PRIME_ORDER,
        "generator_origin_permutations": generators,
        "origin_orbits": orbits,
        "all_orbits_singletons": all(len(orbit) == 1 for orbit in orbits),
        "all_generator_maps_bijective": all(
            set(permutation) == set(ORIGINS)
            for permutation in generator_permutations
        ),
        "generator_lawfulness_cases": lawfulness_cases,
        "lawfulness_preserved": lawfulness_preserved,
        "nontrivial_origin_lift_derived": False,
        "action_status": "POINTWISE_IDENTITY_ON_UNREACHED_ORIGIN_COORDINATE",
        "source_basis": {
            "G_and_F_label_actions_omit_origin":
                controls["cycle808_action_has_no_origin_coordinate"],
            "XOR_lift_not_global":
                controls["cycle808_scope_excludes_global_state_action"],
            "cycle786_origins_are_separate_twelve_point_domain":
                controls["cycle786_origin_partition_anchors"],
        },
        "closure_lemma": (
            "Each displayed generator restricts to id_O; composition and "
            "inverse preserve id_O, so every element of generated G' fixes "
            "the unreached origin coordinate."
        ),
        "honest_boundary": (
            "No Cycle-808 map supplies a nonidentity permutation of the "
            "twelve Cycle-786 origins.  Adding one would be a new lift, not "
            "a consequence of G'."
        ),
    }


def orbit_constant_for_group(
    values: tuple[int, ...],
    group_origins: tuple[int, ...],
    orbits: tuple[tuple[int, ...], ...],
) -> bool:
    count_by_origin = dict(zip(group_origins, values, strict=True))
    for orbit in orbits:
        in_group = tuple(origin for origin in orbit if origin in count_by_origin)
        if len({count_by_origin[origin] for origin in in_group}) > 1:
            return False
    return True


def constraint_certificate(
    allocation: dict[str, object],
    action: dict[str, object],
) -> dict[str, object]:
    allocations = allocation["allocations"]
    orbits = action["origin_orbits"]
    positive_survivors = tuple(
        row
        for row in allocations
        if orbit_constant_for_group(row, POSITIVE_ORIGINS, orbits)
    )
    negative_survivors = tuple(
        row
        for row in allocations
        if orbit_constant_for_group(row, NEGATIVE_ORIGINS, orbits)
    )
    survivor_count = len(positive_survivors)
    if action["all_orbits_singletons"]:
        verdict = "VACUOUS"
    elif survivor_count == 1:
        verdict = "DETERMINED"
    elif survivor_count < len(allocations):
        verdict = "REDUCED"
    else:
        verdict = "VACUOUS"
    return {
        "finite_invariance_theorem": (
            "For a finite G'-set O, a count function c:O->N satisfying "
            "c(g.o)=c(o) for every generator is constant on each generated "
            "orbit: equality propagates along every finite generator word."
        ),
        "origin_orbits": orbits,
        "unconstrained_count_per_group": len(allocations),
        "surviving_count_per_group": survivor_count,
        "positive_surviving_count": len(positive_survivors),
        "negative_surviving_count": len(negative_survivors),
        "combined_surviving_count": (
            len(positive_survivors) * len(negative_survivors)
        ),
        "positive_survivor_sha256": digest(positive_survivors),
        "negative_survivor_sha256": digest(negative_survivors),
        "survivors_equal_all_lawful_allocations": (
            positive_survivors == allocations
            and negative_survivors == allocations
        ),
        "explicit_survivors": (
            positive_survivors if survivor_count <= 50 else None
        ),
        "verdict": verdict,
        "finding": (
            "G' supplies no nontrivial origin orbit, so orbit constancy adds "
            "no equality between distinct origin counts."
        ),
    }


def landed_occurrence_rows() -> tuple[tuple[object, ...], ...]:
    """Rebuild Cycle 808's 46 label rows from lower landed machinery."""
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
    constraint: dict[str, object],
) -> dict[str, object]:
    rows = landed_occurrence_rows()
    allocation_rows = tuple(row for row in rows if row[0] in ALLOCATION_BANKS)
    full_counts = Counter(int(row[3]) for row in rows)
    projected_counts = Counter(int(row[3]) for row in allocation_rows)
    extra_counts = full_counts - projected_counts
    candidate_sets = tuple(
        POSITIVE_ORIGINS if int(row[3]) == 1 else NEGATIVE_ORIGINS
        for row in allocation_rows
    )

    # A concrete support witness only.  Cycle 786 supplies no actual
    # selector-to-origin join, so this is not asserted as the physical split.
    witness_counts = Counter(min(candidates) for candidates in candidate_sets)
    witness = tuple(witness_counts[origin] for origin in ORIGINS)
    allocations = set(allocation["allocations"])
    witness_survives = (
        witness[:6] in allocations
        and witness[6:] in allocations
        and constraint["survivors_equal_all_lawful_allocations"]
    )

    # Exact universal landed-membership control: each of the 19 rows in a
    # sign class admits exactly all six origins in that class.  Hence every
    # possible landed refinement has a weak-composition vector in A.  Since
    # the survivor set equals A, the (undetermined) actual refinement is a
    # survivor without choosing a split convention.
    universal_actual_membership = all(
        (
            len(rows) == 46,
            full_counts == Counter({1: 23, -1: 23}),
            len(allocation_rows) == 38,
            projected_counts == Counter({1: 19, -1: 19}),
            extra_counts == Counter({1: 4, -1: 4}),
            all(tuple(row[4]) == (0,) for row in rows),
            candidate_sets.count(POSITIVE_ORIGINS) == 19,
            candidate_sets.count(NEGATIVE_ORIGINS) == 19,
            constraint["survivors_equal_all_lawful_allocations"],
            witness_survives,
        )
    )
    return {
        "full_landed_46_event_count": len(rows),
        "full_orientation_counts": {"+1": full_counts[1], "-1": full_counts[-1]},
        "counts_by_bank": {
            str(bank): sum(int(row[0]) == bank for row in rows)
            for bank in ALL_BANKS
        },
        "cycle786_allocation_projection_banks": ALLOCATION_BANKS,
        "cycle786_projection_event_count": len(allocation_rows),
        "cycle786_projection_orientation_counts": {
            "+1": projected_counts[1],
            "-1": projected_counts[-1],
        },
        "outside_cycle786_projection_orientation_counts": {
            "+1": extra_counts[1],
            "-1": extra_counts[-1],
        },
        "landed_rows_sha256": digest(rows),
        "allocation_projection_rows_sha256": digest(allocation_rows),
        "specific_origin_counts_landed": None,
        "specific_origin_status": "UNDETERMINED_BY_LANDED_SURFACES",
        "support_witness_not_claimed_actual": witness,
        "support_witness_survives": witness_survives,
        "actual_landed_refinement_membership": (
            "PASS_UNIVERSALLY_ALL_LAWFUL_REFINEMENTS_SURVIVE"
        ),
        "universal_actual_membership": universal_actual_membership,
        "scope_note": (
            "The full Cycle-808 battery is 46=23+23.  Cycle 786's copied "
            "allocation object is exactly its banks 2/5/12 projection, "
            "38=19+19; the additional bank 1/3 rows are not silently inserted "
            "into the 42,504-count object."
        ),
    }


def build_core(controls: dict[str, object]) -> dict[str, object]:
    allocation = allocation_certificate()
    action = origin_action_certificate(allocation, controls)
    constraint = constraint_certificate(allocation, action)
    landed = landed_data_certificate(allocation, constraint)
    allocation_summary = {
        key: value for key, value in allocation.items() if key != "allocations"
    }
    return {
        "allocation": allocation_summary,
        "origin_action": action,
        "constraint": constraint,
        "landed_data": landed,
        "verdict": constraint["verdict"],
    }


def git_index_blobs(paths: tuple[str, ...]) -> dict[str, str]:
    completed = subprocess.run(
        ("git", "ls-files", "-s", "--", *paths),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    output = {}
    for line in completed.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        _mode, blob, _stage = metadata.split()
        output[path] = blob
    return output


def main() -> int:
    input_sha_before = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    input_blob_before = {
        path: git_blob_sha1((ROOT / path).read_bytes())
        for path in AUDIT_INPUT_PATHS
    }
    indexed_pair_blobs = git_index_blobs(AUDIT_INPUT_PATHS[:4])
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
    constraint = first["constraint"]
    landed = first["landed_data"]
    certificate_a = all(
        (
            controls["cycle786_allocation_anchors"],
            controls["cycle786_origin_partition_anchors"],
            allocation["origins"] == ORIGINS,
            allocation["orientation_groups"]
            == {"+1": POSITIVE_ORIGINS, "-1": NEGATIVE_ORIGINS},
            allocation["allocation_count"] == 42_504,
            allocation["closed_form_count"] == 42_504,
            allocation["all_lawful"],
            all(
                values == tuple(range(20))
                for values in allocation["possible_values_by_origin"]
            ),
        )
    )
    certificate_b = all(
        (
            controls["cycle808_exact_group_anchors"],
            controls["cycle808_action_has_no_origin_coordinate"],
            controls["cycle808_scope_excludes_global_state_action"],
            action["G_order"] == G_ORDER,
            action["G_prime_order"] == G_PRIME_ORDER,
            action["all_generator_maps_bijective"],
            action["lawfulness_preserved"],
            action["origin_orbits"]
            == tuple((origin,) for origin in ORIGINS),
            action["all_orbits_singletons"],
            not action["nontrivial_origin_lift_derived"],
        )
    )
    certificate_c = all(
        (
            constraint["unconstrained_count_per_group"] == 42_504,
            constraint["surviving_count_per_group"] == 42_504,
            constraint["positive_surviving_count"] == 42_504,
            constraint["negative_surviving_count"] == 42_504,
            constraint["combined_surviving_count"] == 42_504 ** 2,
            constraint["survivors_equal_all_lawful_allocations"],
            constraint["explicit_survivors"] is None,
        )
    )
    certificate_d = all(
        (
            landed["full_landed_46_event_count"] == 46,
            landed["full_orientation_counts"] == {"+1": 23, "-1": 23},
            landed["counts_by_bank"]
            == {"1": 2, "2": 4, "3": 6, "5": 10, "12": 24},
            landed["cycle786_projection_event_count"] == 38,
            landed["cycle786_projection_orientation_counts"]
            == {"+1": 19, "-1": 19},
            landed["outside_cycle786_projection_orientation_counts"]
            == {"+1": 4, "-1": 4},
            landed["support_witness_survives"],
            landed["universal_actual_membership"],
        )
    )
    certificate_e = (
        constraint["verdict"] == "VACUOUS"
        and action["all_orbits_singletons"]
        and constraint["surviving_count_per_group"]
        == constraint["unconstrained_count_per_group"]
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
        "cycle786_allocation_anchors",
        "cycle786_origin_partition_anchors",
        "cycle808_exact_group_anchors",
        "cycle808_action_has_no_origin_coordinate",
        "cycle808_scope_excludes_global_state_action",
    )
    controls_base = all(
        (
            all(bool(controls[key]) for key in direct_control_keys),
            all(controls["runtime_attempts"].values()),
            input_sha_before == input_sha_after == EXPECTED_SHA256,
            input_blob_before == input_blob_after == EXPECTED_GIT_BLOB_SHA1,
            indexed_pair_blobs
            == {
                path: EXPECTED_GIT_BLOB_SHA1[path]
                for path in AUDIT_INPUT_PATHS[:4]
            },
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
        )
    )

    def render(actual_stdout_bytes: int) -> tuple[str, bool]:
        certificate_f = controls_base and actual_stdout_bytes < STDOUT_LIMIT_BYTES
        certificates = {
            "A_ALLOCATION_OBJECT_RECONSTRUCTED": certificate_a,
            "B_ORIGIN_ACTION_AND_LAWFULNESS": certificate_b,
            "C_ORBIT_CONSTRAINT_COUNTED": certificate_c,
            "D_LANDED_DATA_COMPATIBILITY": certificate_d,
            "E_VERDICT": certificate_e,
            "F_CONTROLS": certificate_f,
        }
        lines = [
            "BOUNDARY exact finite counts and support only; no probability or split rule",
        ]
        for path in AUDIT_INPUT_PATHS:
            lines.append(
                "AUDIT_INPUT_SHA "
                + compact(
                    {
                        "path": path,
                        "sha256": input_sha_after[path],
                        "git_blob_sha1": input_blob_after[path],
                        "indexed_blob_sha1": indexed_pair_blobs.get(path),
                    }
                )
            )
        lines.append("SOURCE_COMMITS " + compact(SOURCE_COMMITS))
        lines.append(
            "CERTIFICATE_A_ALLOCATION_OBJECT "
            + compact(
                {
                    "pass": certificate_a,
                    "origins": allocation["origins"],
                    "orientation_groups": allocation["orientation_groups"],
                    "lawfulness": allocation["lawfulness"],
                    "count_per_group": allocation["allocation_count"],
                    "closed_form": allocation["closed_form_count"],
                    "allocation_sha256": allocation["allocation_sha256"],
                }
            )
        )
        for name, permutation in action["generator_origin_permutations"].items():
            lines.append(
                "ORIGIN_GENERATOR_ACTION "
                + compact({"generator": name, "permutation": permutation})
            )
        lines.append(
            "CERTIFICATE_B_ORIGIN_ACTION "
            + compact(
                {
                    "pass": certificate_b,
                    "action_status": action["action_status"],
                    "origin_orbits": action["origin_orbits"],
                    "lawfulness_preserved": action["lawfulness_preserved"],
                    "lawfulness_cases": action["generator_lawfulness_cases"],
                    "closure_lemma": action["closure_lemma"],
                    "honest_boundary": action["honest_boundary"],
                }
            )
        )
        lines.append("ORIGIN_ORBITS " + compact(action["origin_orbits"]))
        lines.append(
            "CERTIFICATE_C_CONSTRAINT "
            + compact(
                {
                    "pass": certificate_c,
                    "theorem": constraint["finite_invariance_theorem"],
                    "unconstrained_count_per_group":
                        constraint["unconstrained_count_per_group"],
                    "surviving_count_per_group":
                        constraint["surviving_count_per_group"],
                    "combined_surviving_count":
                        constraint["combined_surviving_count"],
                    "explicit_survivors": constraint["explicit_survivors"],
                    "finding": constraint["finding"],
                }
            )
        )
        lines.append(
            "SURVIVING_COUNT_PER_GROUP "
            + str(constraint["surviving_count_per_group"])
        )
        lines.append(
            "CERTIFICATE_D_LANDED_DATA "
            + compact({"pass": certificate_d, **landed})
        )
        lines.append(
            "LANDED_DATA_CONTROL "
            + landed["actual_landed_refinement_membership"]
        )
        lines.append(
            "CERTIFICATE_E_VERDICT "
            + compact(
                {
                    "pass": certificate_e,
                    "verdict": constraint["verdict"],
                    "reason": constraint["finding"],
                }
            )
        )
        lines.append("VERDICT " + constraint["verdict"])
        lines.append(
            "CERTIFICATE_F_CONTROLS "
            + compact(
                {
                    "pass": certificate_f,
                    "source_controls": controls,
                    "input_sha_stable": input_sha_before == input_sha_after,
                    "git_blob_sha_stable": input_blob_before == input_blob_after,
                    "copied_pairs_tracked_at_expected_blobs":
                        indexed_pair_blobs
                        == {
                            path: EXPECTED_GIT_BLOB_SHA1[path]
                            for path in AUDIT_INPUT_PATHS[:4]
                        },
                    "deterministic": deterministic,
                    "first_core_sha256": digest(first),
                    "repeat_core_sha256": digest(second),
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                    "stdout_bytes": actual_stdout_bytes,
                    "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
                }
            )
        )
        report = {
            "cycle": 815,
            "certificates": certificates,
            "all_pass": all(certificates.values()),
            "origin_orbits": action["origin_orbits"],
            "unconstrained_count_per_group":
                constraint["unconstrained_count_per_group"],
            "surviving_count_per_group":
                constraint["surviving_count_per_group"],
            "verdict": constraint["verdict"],
            "landed_data_control":
                landed["actual_landed_refinement_membership"],
            "runtime_seconds": round(elapsed, 6),
        }
        report["stable_report_sha256"] = digest(
            {key: value for key, value in report.items() if key != "runtime_seconds"}
        )
        lines.append("SUMMARY_JSON " + compact(report))
        lines.append(
            "CYCLE815_PER_ORIGIN_ORBIT_CONSTRAINT_CERTIFIED"
            if report["all_pass"]
            else "CYCLE815_CERTIFICATE_FAILURE"
        )
        return "\n".join(lines) + "\n", certificate_f

    stdout_bytes = 0
    output = ""
    certificate_f = False
    for _iteration in range(12):
        output, certificate_f = render(stdout_bytes)
        new_size = len(output.encode("utf-8"))
        if new_size == stdout_bytes:
            break
        stdout_bytes = new_size
    output, certificate_f = render(stdout_bytes)
    final_size = len(output.encode("utf-8"))
    if final_size != stdout_bytes:
        stdout_bytes = final_size
        output, certificate_f = render(stdout_bytes)
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
            certificate_f,
            final_size == stdout_bytes,
        )
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
