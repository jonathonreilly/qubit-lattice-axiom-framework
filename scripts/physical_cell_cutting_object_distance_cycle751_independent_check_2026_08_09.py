"""Independent Cycle 751 ambient never-sharing graph and embedding checker.

The checker imports no Cycle 751 primary symbols. It live-replays the landed
Cycle 750 streamed-pair helper, computes the ambient metric by Floyd--Warshall
dynamic programming rather than the primary breadth-first/Boolean-power paths,
and recomputes every carrier and control comparison from the streamed matrix.
"""
import contextlib
import copy
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_object_distance_cycle751_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = "scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py"
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_OBJECT_DISTANCE_CYCLE751_NOTE_2026-08-09.md"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_object_distance_cycle751_2026_08_09_"
    "receipt_2026-08-09.json"
)
C749_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FAMILY_SEPARATOR_CYCLE749_NOTE_2026-08-08.md"
C749_PRIMARY_PATH = "scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py"
C749_CHECKER_PATH = (
    "scripts/physical_cell_cutting_family_separator_cycle749_"
    "independent_check_2026_08_08.py"
)
C749_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_family_separator_cycle749_2026_08_08_"
    "receipt_2026-08-08.json"
)
C749_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_family_separator_cycle749_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
C750_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md"
C750_PRIMARY_PATH = "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py"
C750_CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_"
    "independent_check_2026_08_09.py"
)
C750_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09_"
    "receipt_2026-08-09.json"
)
C750_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_object_distance_cycle751_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_OBJECT_DISTANCE_CYCLE751_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py",
    "outputs/physical_cell_cutting_object_distance_cycle751_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_FAMILY_SEPARATOR_CYCLE749_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py",
    "scripts/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08.py",
    "outputs/physical_cell_cutting_family_separator_cycle749_2026_08_08_receipt_2026-08-08.json",
    "outputs/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08_receipt_2026-08-08.json",
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py",
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_independent_check_2026_08_09_receipt_2026-08-09.json",
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
        "schema": "physical-cell-cutting-object-distance-cycle751-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


write_failure("checker has not completed")
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C749 = load(C749_RECEIPT_PATH)
C749I = load(C749_INDEPENDENT_RECEIPT_PATH)
C750 = load(C750_RECEIPT_PATH)
C750I = load(C750_INDEPENDENT_RECEIPT_PATH)

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
    compact = detail if len(detail) <= 110 else detail[:107] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


def cycle749_contract(primary, independent):
    separator = primary.get("family_separator", {})
    reconstruction = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema") == "physical-cell-cutting-family-separator-cycle749-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C749_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and separator.get("family_sizes") == [12, 12, 12, 24, 24, 48]
        and independent.get("schema")
        == "physical-cell-cutting-family-separator-cycle749-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C749_CHECKER_PATH)
        and inputs_current(independent)
        and reconstruction.get("cuttings") == 15800
        and reconstruction.get("weight_sixteen_census_count") == 132
    )


def cycle750_contract(primary, independent):
    metric = primary.get("carrier_cube_metric", {})
    reconstruction = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema") == "physical-cell-cutting-carrier-cube-metric-cycle750-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C750_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and metric.get("shape_counts") == {"four_cube": 60, "two_three_cubes": 72}
        and independent.get("schema")
        == "physical-cell-cutting-carrier-cube-metric-cycle750-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C750_CHECKER_PATH)
        and inputs_current(independent)
        and reconstruction.get("processed_pair_rows") == 15800
        and reconstruction.get("complete_carrier_count") == 132
        and independent.get("carrier_cube_metric", {}).get("shape_counts")
        == {"four_cube": 60, "two_three_cubes": 72}
    )


C749_OK = cycle749_contract(C749, C749I)
C750_OK = cycle750_contract(C750, C750I)
gate("independent.cycle749_contract", C749_OK,
     "current Cycle 749 primary and independent certificates bind all rows and 132 carriers")
gate("independent.cycle750_contract", C750_OK,
     "current Cycle 750 primary and independent certificates bind both carrier graph types")

# Replay Cycle 750's streamed-pair checker read-only. Its source and complete
# input-bound receipt are declared above and validated before its data are used.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / C750_INDEPENDENT_RECEIPT_PATH).resolve()


def write_except_dependency(path, data, *args, **kwargs):
    if path.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(path, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = write_except_dependency
try:
    with contextlib.redirect_stdout(io.StringIO()):
        predecessor = runpy.run_path(
            str(ROOT / C750_CHECKER_PATH),
            run_name="__cycle750_independent_dependency__",
        )
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

gate(
    "independent.predecessor_live_replay",
    predecessor.get("failed") == 0 and predecessor.get("passed", 0) > 10,
    "the landed streamed-pair predecessor replays live with every named gate passing",
)

census = predecessor["census"]
pair_counts = predecessor["pair_counts"]
group = predecessor["predecessor"]["group"]
adjacency = pair_counts == 0
np.fill_diagonal(adjacency, False)


def all_pairs_floyd(adjacency_matrix):
    """All-pairs unweighted distance by min-plus dynamic programming."""
    size = len(adjacency_matrix)
    distance = np.full((size, size), 1000, dtype=np.int64)
    distance[adjacency_matrix] = 1
    np.fill_diagonal(distance, 0)
    for middle in range(size):
        distance = np.minimum(
            distance,
            distance[:, middle, None] + distance[None, middle, :],
        )
    return distance


ambient_distance = all_pairs_floyd(adjacency)
degree_values = sorted(set(int(value) for value in adjacency.sum(axis=1)))
edge_count = int(adjacency.sum()) // 2
distance_distribution = {
    distance: int(np.count_nonzero(np.triu(ambient_distance == distance, 1)))
    for distance in sorted(set(int(value) for value in ambient_distance.flat))
    if 0 < distance < 1000
}
symmetry_count = sum(
    np.array_equal(adjacency[np.ix_(element, element)], adjacency)
    for element in group
)
gate(
    "independent.ambient_graph",
    degree_values == [33]
    and edge_count == 3168
    and distance_distribution == {1: 3168, 2: 12576, 3: 2592}
    and symmetry_count == 384,
    "streamed co-incidence and Floyd--Warshall give the exact regular graph and distance census",
)

profile_sets = {1: set(), 2: set(), 3: set()}
for left in range(192):
    for right in range(192):
        distance = int(ambient_distance[left, right])
        if distance == 0:
            continue
        profile_sets[distance].add(tuple(
            int(np.count_nonzero(adjacency[right] & (ambient_distance[left] == layer)))
            for layer in range(distance - 1, distance + 2)
        ))
profile_counts = {key: len(value) for key, value in profile_sets.items()}
gate(
    "independent.distance_partition_profiles",
    profile_counts == {1: 9, 2: 45, 3: 10},
    "rooted neighbor-count profiles vary within each declared ambient distance layer",
)

shape_counts = {"four_cube": 0, "two_three_cubes": 0, "unclassified": 0}
within_three = 0
preserved = 0
distance_three = 0
preserved_three = 0
antipodal = 0
antipodal_at_three = 0
antipodal_at_four = 0
cross_by_ambient = {}
for carrier in census:
    columns = sorted(carrier)
    local_adjacency = adjacency[np.ix_(columns, columns)].copy()
    local_distance = all_pairs_floyd(local_adjacency)
    shape = predecessor["classify_shape"](columns)
    shape_counts[shape if shape in shape_counts else "unclassified"] += 1
    for left in range(16):
        for right in range(left + 1, 16):
            local = int(local_distance[left, right])
            ambient = int(ambient_distance[columns[left], columns[right]])
            if local <= 3:
                within_three += 1
                preserved += int(local == ambient)
                if local == 3:
                    distance_three += 1
                    preserved_three += int(ambient == 3)
            elif local == 4:
                antipodal += 1
                antipodal_at_three += int(ambient == 3)
                antipodal_at_four += int(ambient == 4)
            elif local >= 1000:
                cross_by_ambient[ambient] = cross_by_ambient.get(ambient, 0) + 1

gate(
    "independent.carrier_embedding",
    shape_counts == {"four_cube": 60, "two_three_cubes": 72, "unclassified": 0}
    and within_three == preserved == 10752
    and distance_three == preserved_three == 2496,
    "every carrier-component pair through distance three is preserved, including all 2496 nontrivial triples",
)
gate(
    "independent.embedding_boundaries",
    antipodal == antipodal_at_three == 480
    and antipodal_at_four == 0
    and cross_by_ambient == {2: 4032, 3: 576},
    "all Q4 antipodes shorten and every split-component cross pair gets the exact declared ambient distance",
)

cyclic_columns = list(range(192)) * 2
control_sets = 0
shortened_sets = 0
for spacing in (1, 5, 7, 11):
    for start in range(192):
        columns = sorted(cyclic_columns[start:start + 16 * spacing:spacing])
        local_distance = all_pairs_floyd(adjacency[np.ix_(columns, columns)])
        shortened = any(
            local_distance[left, right] < 1000
            and local_distance[left, right]
            != ambient_distance[columns[left], columns[right]]
            for left in range(16)
            for right in range(left + 1, 16)
        )
        control_sets += 1
        shortened_sets += int(shortened)
gate(
    "independent.declared_controls",
    control_sets == 768 and shortened_sets == 730,
    "the independent metric calculation reproduces all declared cyclic control outcomes",
)

count_to_distance = {}
for left in range(192):
    for right in range(left + 1, 192):
        count_to_distance.setdefault(int(pair_counts[left, right]), set()).add(
            int(ambient_distance[left, right])
        )
ambiguous_counts = sorted(
    count for count, distances in count_to_distance.items() if len(distances) > 1
)
ambiguous_pairs = sum(
    int(pair_counts[left, right]) in ambiguous_counts
    for left in range(192)
    for right in range(left + 1, 192)
)
gate(
    "independent.count_distance_boundary",
    len(count_to_distance) == 47
    and ambiguous_counts == [202, 212, 250]
    and ambiguous_pairs == 1632,
    "exactly three shared-cutting count classes are ambiguous on exactly 1632 ambient pairs",
)


def primary_contract(receipt):
    ambient = receipt.get("ambient_never_sharing_graph", {})
    embedding = receipt.get("carrier_embedding", {})
    controls = receipt.get("declared_controls", {})
    count_boundary = receipt.get("shared_cutting_count_global_boundary", {})
    dependencies = receipt.get("direct_dependencies", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-object-distance-cycle751-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and receipt.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and dependencies.get("cycle749", {}).get("receipt_sha256") == sha256(C749_RECEIPT_PATH)
        and dependencies.get("cycle749", {}).get("independent_receipt_sha256")
        == sha256(C749_INDEPENDENT_RECEIPT_PATH)
        and dependencies.get("cycle750", {}).get("receipt_sha256") == sha256(C750_RECEIPT_PATH)
        and dependencies.get("cycle750", {}).get("independent_receipt_sha256")
        == sha256(C750_INDEPENDENT_RECEIPT_PATH)
        and ambient.get("vertices") == 192
        and ambient.get("degree") == 33
        and ambient.get("edges") == 3168
        and ambient.get("distance_distribution") == {"1": 3168, "2": 12576, "3": 2592}
        and ambient.get("distance_layer_profile_counts") == {"1": 9, "2": 45, "3": 10}
        and embedding.get("shape_counts")
        == {"four_cube": 60, "two_three_cubes": 72, "unclassified": 0}
        and embedding.get("within_component_pairs_preserving_distance") == 10752
        and embedding.get("intrinsic_distance_three_pairs_preserving_distance") == 2496
        and embedding.get("four_cube_antipodal_pairs_at_global_distance_three") == 480
        and embedding.get("four_cube_antipodal_pairs_at_global_distance_four") == 0
        and embedding.get("split_component_cross_pairs_by_global_distance")
        == {"2": 4032, "3": 576}
        and controls.get("cyclic_sixteen_piece_sets") == 768
        and controls.get("sets_with_a_connected_induced_pair_shortened_ambiently") == 730
        and count_boundary.get("ambiguous_count_values") == [202, 212, 250]
        and count_boundary.get("pairs_in_ambiguous_count_classes") == 1632
    )


PRIMARY_OK = primary_contract(PRIMARY)
gate(
    "independent.primary_contract",
    C749_OK and C750_OK and PRIMARY_OK,
    "the Cycle 751 primary receipt equals the independent streamed-pair and Floyd reconstruction",
)

bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate("hostile.primary_status", not primary_contract(bad_primary),
     "a failing primary receipt is rejected")
bad_distance = copy.deepcopy(PRIMARY)
bad_distance["ambient_never_sharing_graph"]["distance_distribution"]["3"] = 2591
gate("hostile.ambient_distance", not primary_contract(bad_distance),
     "a changed ambient distance layer is rejected")
bad_embedding = copy.deepcopy(PRIMARY)
bad_embedding["carrier_embedding"]["within_component_pairs_preserving_distance"] = 10751
gate("hostile.embedding", not primary_contract(bad_embedding),
     "a changed through-three preservation total is rejected")
bad_antipode = copy.deepcopy(PRIMARY)
bad_antipode["carrier_embedding"]["four_cube_antipodal_pairs_at_global_distance_four"] = 1
gate("hostile.antipode", not primary_contract(bad_antipode),
     "a claimed unshortened Q4 antipode is rejected")
bad_count = copy.deepcopy(PRIMARY)
bad_count["shared_cutting_count_global_boundary"]["ambiguous_count_values"] = [202, 212]
gate("hostile.count_boundary", not primary_contract(bad_count),
     "a removed ambiguous count class is rejected")
bad_c750 = copy.deepcopy(C750I)
bad_c750["status"] = "fail"
gate("hostile.cycle750", not cycle750_contract(C750, bad_c750),
     "a failing direct Cycle 750 independent certificate is rejected")

print("per_element: checked -- all 192 pieces enter the streamed ambient graph and Floyd distance calculation", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- this finite binary incidence object has no modal decomposition", flush=True)
print("per_block: checked -- every one of the 15800 cutting rows enters the streamed co-incidence matrix", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, continuum, or physical-metric claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-object-distance-cycle751-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(predecessor["incidence"]),
        "support_columns": len(pair_counts),
        "processed_pair_rows": len(predecessor["incidence"]),
        "pair_counter": "Cycle 750 row-streamed unordered pairs",
        "ambient_metric": "Floyd--Warshall min-plus dynamic programming",
        "complete_carrier_count": len(census),
    },
    "ambient_never_sharing_graph": {
        "degree_values": degree_values,
        "edges": edge_count,
        "distance_distribution": {
            str(key): value for key, value in sorted(distance_distribution.items())
        },
        "symmetries_preserving_adjacency": symmetry_count,
        "distance_layer_profile_counts": {
            str(key): value for key, value in sorted(profile_counts.items())
        },
    },
    "carrier_embedding": {
        "shape_counts": shape_counts,
        "within_component_pairs_through_three": within_three,
        "within_component_pairs_preserved": preserved,
        "distance_three_pairs": distance_three,
        "distance_three_pairs_preserved": preserved_three,
        "four_cube_antipodal_pairs": antipodal,
        "four_cube_antipodal_pairs_at_global_three": antipodal_at_three,
        "four_cube_antipodal_pairs_at_global_four": antipodal_at_four,
        "split_component_cross_pairs_by_global_distance": {
            str(key): value for key, value in sorted(cross_by_ambient.items())
        },
    },
    "declared_controls": {
        "sets": control_sets,
        "sets_with_shortening": shortened_sets,
    },
    "shared_cutting_count_global_boundary": {
        "count_values_occurring": len(count_to_distance),
        "ambiguous_count_values": ambiguous_counts,
        "pairs_in_ambiguous_count_classes": ambiguous_pairs,
    },
    "direct_dependencies": {
        "cycle749": {
            "receipt_sha256": sha256(C749_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C749_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C749_OK,
        },
        "cycle750": {
            "receipt_sha256": sha256(C750_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C750_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C750_OK,
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
