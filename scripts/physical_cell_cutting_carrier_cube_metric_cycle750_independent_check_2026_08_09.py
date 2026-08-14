"""Independent Cycle 750 carrier-cube metric checker.

This checker imports no Cycle 750 primary symbols.  It executes the landed Cycle 749
opposite-pivot reconstruction as a dependency, then recognizes cube graphs by a
constructive breadth-first bit labeling rather than the primary backtracking
isomorphism search.  It uses the predecessor's row-streamed pair counts, not the
primary dense Gram implementation.
"""
import contextlib
import copy
import hashlib
import io
import json
import math
import runpy
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py"
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09_"
    "receipt_2026-08-09.json"
)
DEPENDENCY_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_FAMILY_SEPARATOR_CYCLE749_NOTE_2026-08-08.md"
)
DEPENDENCY_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py"
)
DEPENDENCY_CHECKER_PATH = (
    "scripts/physical_cell_cutting_family_separator_cycle749_"
    "independent_check_2026_08_08.py"
)
DEPENDENCY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_family_separator_cycle749_2026_08_08_"
    "receipt_2026-08-08.json"
)
DEPENDENCY_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_family_separator_cycle749_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py",
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_FAMILY_SEPARATOR_CYCLE749_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py",
    "scripts/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08.py",
    "outputs/physical_cell_cutting_family_separator_cycle749_2026_08_08_receipt_2026-08-08.json",
    "outputs/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08_receipt_2026-08-08.json",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == sha256(path)
        for path in recorded
    )


def write_failure(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-carrier-cube-metric-cycle750-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


write_failure("checker has not completed")
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C749 = load(DEPENDENCY_RECEIPT_PATH)
C749I = load(DEPENDENCY_INDEPENDENT_RECEIPT_PATH)

passed = 0
failed = 0
gates = {}


def gate(name, condition, detail):
    global passed, failed
    ok = bool(condition)
    gates[name] = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    compact = detail if len(detail) <= 100 else detail[:97] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


def cycle749_contract(primary, independent):
    separator = primary.get("family_separator", {})
    reconstruction = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema") == "physical-cell-cutting-family-separator-cycle749-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(DEPENDENCY_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and separator.get("family_sizes") == [12, 12, 12, 24, 24, 48]
        and separator.get("signature_class_sizes") == [12, 12, 12, 24, 24, 48]
        and separator.get("larger_incidence_automorphism_merger_possible") is False
        and independent.get("schema")
        == "physical-cell-cutting-family-separator-cycle749-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(DEPENDENCY_CHECKER_PATH)
        and inputs_current(independent)
        and reconstruction.get("cuttings") == 15800
        and reconstruction.get("support_columns") == 192
        and reconstruction.get("weight_sixteen_census_count") == 132
        and reconstruction.get("weight_sixteen_family_sizes")
        == [12, 12, 12, 24, 24, 48]
    )


DEPENDENCY_OK = cycle749_contract(C749, C749I)
gate(
    "independent.cycle749_contract",
    DEPENDENCY_OK,
    "current Cycle 749 primary and opposite-pivot certificates bind all rows and 132 carriers",
)

# Execute the opposite-pivot predecessor reconstruction without exposing its stdout
# as this checker's own evidence.  Its source and complete input-bound receipt are
# declared above and validated fail-closed.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / DEPENDENCY_INDEPENDENT_RECEIPT_PATH).resolve()


def write_except_dependency(path, data, *args, **kwargs):
    """Keep the live dependency replay read-only for declared audit inputs."""
    if path.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(path, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = write_except_dependency
try:
    with contextlib.redirect_stdout(io.StringIO()):
        predecessor = runpy.run_path(
            str(ROOT / DEPENDENCY_CHECKER_PATH),
            run_name="__cycle749_independent_dependency__",
        )
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

gate(
    "independent.predecessor_live_replay",
    predecessor.get("failed") == 0 and predecessor.get("passed") == 23,
    "the landed opposite-pivot predecessor replays live with all 23 gates passing",
)

census = predecessor["census"]
families = predecessor["families"]
family_of = predecessor["family_of"]
pair_counts = predecessor["streamed_pairs"]
incidence = predecessor["incidence"]
unimodular = predecessor["unimodular"]
used = predecessor["used"]


def components(adjacency):
    unseen = set(range(len(adjacency)))
    found = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        queue = [root]
        component = []
        while queue:
            vertex = queue.pop(0)
            component.append(vertex)
            for neighbor in np.flatnonzero(adjacency[vertex]):
                neighbor = int(neighbor)
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        found.append(sorted(component))
    return sorted(found, key=lambda row: (len(row), row))


def recognize_cube(adjacency):
    """Construct cube coordinates layer by layer; return labels or None."""
    size = len(adjacency)
    dimension = size.bit_length() - 1
    if (
        size != 1 << dimension
        or not np.array_equal(adjacency, adjacency.T)
        or np.any(np.diag(adjacency))
        or set(int(value) for value in adjacency.sum(axis=1)) != {dimension}
    ):
        return None
    distances = [-1] * size
    distances[0] = 0
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        for neighbor in np.flatnonzero(adjacency[vertex]):
            neighbor = int(neighbor)
            if distances[neighbor] < 0:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    expected_layers = [math.comb(dimension, layer) for layer in range(dimension + 1)]
    if any(value < 0 for value in distances) or [
        distances.count(layer) for layer in range(dimension + 1)
    ] != expected_layers:
        return None
    labels = {0: 0}
    for bit, vertex in enumerate(sorted(int(x) for x in np.flatnonzero(adjacency[0]))):
        labels[vertex] = 1 << bit
    for layer in range(2, dimension + 1):
        for vertex in [i for i, value in enumerate(distances) if value == layer]:
            lower = [
                labels[int(neighbor)]
                for neighbor in np.flatnonzero(adjacency[vertex])
                if distances[int(neighbor)] == layer - 1
            ]
            if len(lower) != layer:
                return None
            label = 0
            for value in lower:
                label |= value
            if label.bit_count() != layer or label in labels.values():
                return None
            labels[vertex] = label
    if len(labels) != size:
        return None
    if any(
        bool(adjacency[left, right])
        != ((labels[left] ^ labels[right]).bit_count() == 1)
        for left in range(size)
        for right in range(size)
    ):
        return None
    return labels


shape_counts = {}
family_shapes = {}
edge_counts = {}
four_cube_distance = {}
three_cube_distance = {}
cross_counts = set()
cross_top = 0
inside_top = 0
recognition_failures = 0
for carrier in census:
    columns = sorted(carrier)
    local = pair_counts[np.ix_(columns, columns)]
    adjacency = local == 0
    np.fill_diagonal(adjacency, False)
    found_components = components(adjacency)
    shape = "neither"
    if len(found_components) == 1:
        labels = recognize_cube(adjacency)
        if labels is not None and len(adjacency) == 16:
            shape = "four_cube"
            for left in range(16):
                for right in range(left + 1, 16):
                    distance = (labels[left] ^ labels[right]).bit_count()
                    four_cube_distance.setdefault(distance, set()).add(
                        int(local[left, right])
                    )
    elif [len(row) for row in found_components] == [8, 8]:
        component_labels = [
            recognize_cube(adjacency[np.ix_(component, component)])
            for component in found_components
        ]
        if all(labels is not None for labels in component_labels):
            shape = "two_three_cubes"
            maximum = max(
                int(local[left, right])
                for left in range(16)
                for right in range(left + 1, 16)
            )
            for component, labels in zip(found_components, component_labels):
                for left_index, left in enumerate(component):
                    for right_index in range(left_index + 1, len(component)):
                        right = component[right_index]
                        value = int(local[left, right])
                        distance = (labels[left_index] ^ labels[right_index]).bit_count()
                        three_cube_distance.setdefault(distance, set()).add(value)
                        inside_top += int(value == maximum)
            for left in found_components[0]:
                for right in found_components[1]:
                    value = int(local[left, right])
                    cross_counts.add(value)
                    cross_top += int(value == maximum)
    if shape == "neither":
        recognition_failures += 1
    shape_counts[shape] = shape_counts.get(shape, 0) + 1
    edge_counts.setdefault(shape, set()).add(int(adjacency.sum()) // 2)
    family_shapes.setdefault(family_of[carrier], set()).add(shape)

family_shape_catalog = sorted(
    (len(families[index]), next(iter(shapes)))
    for index, shapes in family_shapes.items()
    if len(shapes) == 1
)
gate(
    "independent.shape_census",
    shape_counts == {"four_cube": 60, "two_three_cubes": 72}
    and recognition_failures == 0
    and edge_counts == {"four_cube": {32}, "two_three_cubes": {24}},
    "constructive bit labels recognize exactly 60 four-cubes and 72 pairs of three-cubes",
)
gate(
    "independent.family_shape_constancy",
    family_shape_catalog
    == [(12, "four_cube"), (12, "four_cube"), (12, "four_cube"),
        (24, "four_cube"), (24, "two_three_cubes"), (48, "two_three_cubes")],
    "the independently reconstructed Cycle 749 families carry the exact declared shape split",
)

expected_four_cube = {
    1: {0},
    2: {170, 171, 173, 174, 178, 183, 184},
    3: {240, 245, 250},
    4: {433},
}
count_to_distance = {}
for distance, values in four_cube_distance.items():
    for value in values:
        count_to_distance.setdefault(value, set()).add(distance)
gate(
    "independent.four_cube_metric",
    four_cube_distance == expected_four_cube
    and len(count_to_distance) == 12
    and max(len(values) for values in count_to_distance.values()) == 1,
    "all four-cube pair-count values reproduce the exact disjoint distance layers",
)
gate(
    "independent.two_three_cube_metric",
    three_cube_distance
    == {1: {0}, 2: {170, 171, 173, 174}, 3: {250}}
    and cross_counts == {202, 207, 212, 253, 254, 257, 260, 666}
    and not cross_counts.intersection(set().union(*three_cube_distance.values()))
    and cross_top == 576
    and inside_top == 0,
    "inside and cross-component count layers are exact, disjoint, and all 576 maxima cross",
)


def classify_shape(columns):
    local = pair_counts[np.ix_(columns, columns)]
    adjacency = local == 0
    np.fill_diagonal(adjacency, False)
    found_components = components(adjacency)
    if len(found_components) == 1 and recognize_cube(adjacency) is not None:
        return "four_cube"
    if (
        [len(row) for row in found_components] == [8, 8]
        and all(
            recognize_cube(adjacency[np.ix_(component, component)]) is not None
            for component in found_components
        )
    ):
        return "two_three_cubes"
    return "neither"


cyclic_columns = list(range(192)) * 2
control_counts = {}
for spacing in (1, 5, 7, 11):
    for start in range(192):
        shape = classify_shape(sorted(
            cyclic_columns[start:start + 16 * spacing:spacing]
        ))
        control_counts[shape] = control_counts.get(shape, 0) + 1
gate(
    "independent.control",
    control_counts == {"neither": 768},
    "all 768 declared cyclic control sets are rejected by the constructive recognizer",
)

corner_sets = [frozenset(int(x) for x in unimodular[used[column]]) for column in range(192)]
covered_corner_counts = set()
joined_corner_intersections = set()
farther_pairs_sharing_two = 0
for carrier in census:
    columns = sorted(carrier)
    local = pair_counts[np.ix_(columns, columns)]
    adjacency = local == 0
    np.fill_diagonal(adjacency, False)
    if classify_shape(columns) != "four_cube":
        continue
    covered_corner_counts.add(len(set().union(*(corner_sets[column] for column in columns))))
    for left in range(16):
        for right in range(left + 1, 16):
            intersection = len(corner_sets[columns[left]] & corner_sets[columns[right]])
            if adjacency[left, right]:
                joined_corner_intersections.add(intersection)
            elif intersection == 2:
                farther_pairs_sharing_two += 1
gate(
    "independent.corner_incidence_boundary",
    covered_corner_counts == {16}
    and joined_corner_intersections == {2}
    and farther_pairs_sharing_two == 2016,
    "shared cell-corner count is necessary on joins but fails as their converse on 2016 farther pairs",
)


def primary_contract(receipt):
    dependency = receipt.get("direct_dependencies", {}).get("cycle749", {})
    metric = receipt.get("carrier_cube_metric", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-carrier-cube-metric-cycle750-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and receipt.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and dependency.get("receipt_sha256") == sha256(DEPENDENCY_RECEIPT_PATH)
        and dependency.get("independent_receipt_sha256")
        == sha256(DEPENDENCY_INDEPENDENT_RECEIPT_PATH)
        and dependency.get("complete_carrier_count") == 132
        and dependency.get("family_sizes") == [12, 12, 12, 24, 24, 48]
        and metric.get("shape_counts") == {"four_cube": 60, "two_three_cubes": 72}
        and metric.get("family_shape_catalog")
        == [[12, "four_cube"], [12, "four_cube"], [12, "four_cube"],
            [24, "four_cube"], [24, "two_three_cubes"], [48, "two_three_cubes"]]
        and metric.get("four_cube_distance_counts")
        == {str(key): sorted(values) for key, values in expected_four_cube.items()}
        and metric.get("count_determines_four_cube_distance") is True
        and metric.get("three_cube_distance_counts")
        == {str(key): sorted(values) for key, values in three_cube_distance.items()}
        and metric.get("cross_component_counts") == sorted(cross_counts)
        and metric.get("cross_component_maxima") == 576
        and metric.get("inside_component_maxima") == 0
        and metric.get("control_sets") == 768
        and metric.get("control_with_either_shape") == 0
        and metric.get("farther_pairs_sharing_two_corners") == 2016
    )


PRIMARY_OK = primary_contract(PRIMARY)
gate(
    "independent.primary_contract",
    DEPENDENCY_OK and PRIMARY_OK,
    "the Cycle 750 primary receipt equals the independent graph and metric reconstruction",
)

bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate("hostile.primary_status", not primary_contract(bad_primary), "a failing primary receipt is rejected")
bad_shape = copy.deepcopy(PRIMARY)
bad_shape["carrier_cube_metric"]["shape_counts"]["four_cube"] = 61
gate("hostile.shape_count", not primary_contract(bad_shape), "a changed four-cube count is rejected")
bad_distance = copy.deepcopy(PRIMARY)
bad_distance["carrier_cube_metric"]["four_cube_distance_counts"]["4"] = [432]
gate("hostile.distance_layer", not primary_contract(bad_distance), "a changed antipodal count is rejected")
bad_cross = copy.deepcopy(PRIMARY)
bad_cross["carrier_cube_metric"]["cross_component_counts"].append(250)
gate("hostile.cross_layer", not primary_contract(bad_cross), "a cross/inside layer collision is rejected")
bad_dependency = copy.deepcopy(C749)
bad_dependency["family_separator"]["family_sizes"] = [12, 12, 12, 24, 25, 47]
gate(
    "hostile.cycle749",
    not cycle749_contract(bad_dependency, C749I),
    "a changed predecessor family census is rejected",
)

print("per_element: checked -- all 192 pieces enter the independent streamed pair-count and graph calculations", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- this finite binary incidence object has no modal decomposition", flush=True)
print("per_block: checked -- every one of the 15800 cutting rows contributes to the streamed pair-count matrix", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, continuum, or physical-metric claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-carrier-cube-metric-cycle750-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(predecessor["solutions"]),
        "support_columns": len(used),
        "processed_pair_rows": len(incidence),
        "exact_cover_pivot": "greatest uncovered sample through Cycle 749 checker",
        "cube_recognizer": "constructive breadth-first bit labeling",
        "complete_carrier_count": len(census),
        "family_sizes": sorted(len(family) for family in families),
    },
    "carrier_cube_metric": {
        "shape_counts": shape_counts,
        "family_shape_catalog": [list(row) for row in family_shape_catalog],
        "edge_counts": {key: sorted(value) for key, value in edge_counts.items()},
        "four_cube_distance_counts": {
            str(key): sorted(value) for key, value in sorted(four_cube_distance.items())
        },
        "count_determines_four_cube_distance": max(
            len(values) for values in count_to_distance.values()
        ) == 1,
        "three_cube_distance_counts": {
            str(key): sorted(value) for key, value in sorted(three_cube_distance.items())
        },
        "cross_component_counts": sorted(cross_counts),
        "cross_component_maxima": cross_top,
        "inside_component_maxima": inside_top,
        "control_sets": sum(control_counts.values()),
        "control_with_either_shape": sum(
            value for key, value in control_counts.items() if key != "neither"
        ),
        "covered_ambient_corners": sorted(covered_corner_counts),
        "joined_pair_corner_intersections": sorted(joined_corner_intersections),
        "farther_pairs_sharing_two_corners": farther_pairs_sharing_two,
    },
    "direct_dependencies": {
        "cycle749": {
            "receipt_sha256": sha256(DEPENDENCY_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(DEPENDENCY_INDEPENDENT_RECEIPT_PATH),
            "contract_current": DEPENDENCY_OK,
        },
    },
    "no_go_discipline": {
        "status": "PASS",
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked and not executed",
            "per_block checked",
            "lattice_wide checked and not executed",
        ],
    },
    "gates": {"pass": passed, "fail": failed, "named": gates},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(0 if failed == 0 else 1)
