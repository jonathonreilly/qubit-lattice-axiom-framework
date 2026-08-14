"""Independent Cycle 752 induced-Q4 census and pair-total checker.

This checker imports no Cycle 752 primary symbols.  It live-replays the
Cycle 751 streamed-pair checker, enumerates every induced Q4 once at its least
vertex by coordinate completion, and recomputes the reading and pair-total
classifications from the all-row incidence matrix.
"""
import contextlib
import copy
import hashlib
import io
import itertools
import json
import runpy
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_"
    "CYCLE752_NOTE_2026-08-09.md"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
C750_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md"
)
C750_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py"
)
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
C751_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_OBJECT_DISTANCE_CYCLE751_NOTE_2026-08-09.md"
C751_PRIMARY_PATH = "scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py"
C751_CHECKER_PATH = (
    "scripts/physical_cell_cutting_object_distance_cycle751_"
    "independent_check_2026_08_09.py"
)
C751_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_object_distance_cycle751_2026_08_09_"
    "receipt_2026-08-09.json"
)
C751_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_object_distance_cycle751_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_CYCLE752_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py",
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py",
    "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_carrier_cube_metric_cycle750_independent_check_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_OBJECT_DISTANCE_CYCLE751_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py",
    "scripts/physical_cell_cutting_object_distance_cycle751_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_object_distance_cycle751_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_object_distance_cycle751_independent_check_2026_08_09_receipt_2026-08-09.json",
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
        "schema": "physical-cell-cutting-shape-census-cycle752-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


write_failure("checker has not completed")
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C750 = load(C750_RECEIPT_PATH)
C750I = load(C750_INDEPENDENT_RECEIPT_PATH)
C751 = load(C751_RECEIPT_PATH)
C751I = load(C751_INDEPENDENT_RECEIPT_PATH)

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
        and metric.get("four_cube_distance_counts", {}).get("4") == [433]
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


def cycle751_contract(primary, independent):
    ambient = primary.get("ambient_never_sharing_graph", {})
    embedding = primary.get("carrier_embedding", {})
    reconstruction = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema") == "physical-cell-cutting-object-distance-cycle751-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C751_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and ambient.get("vertices") == 192
        and ambient.get("degree") == 33
        and ambient.get("diameter") == 3
        and embedding.get("shape_counts")
        == {"four_cube": 60, "two_three_cubes": 72, "unclassified": 0}
        and embedding.get("four_cube_antipodal_pairs_at_global_distance_three") == 480
        and embedding.get("four_cube_antipodal_pairs_at_global_distance_four") == 0
        and independent.get("schema")
        == "physical-cell-cutting-object-distance-cycle751-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C751_CHECKER_PATH)
        and inputs_current(independent)
        and reconstruction.get("processed_pair_rows") == 15800
        and reconstruction.get("complete_carrier_count") == 132
    )


C750_OK = cycle750_contract(C750, C750I)
C751_OK = cycle751_contract(C751, C751I)
gate("independent.cycle750_contract", C750_OK,
     "current Cycle 750 primary and independent certificates bind the 60 Q4 carriers")
gate("independent.cycle751_contract", C751_OK,
     "current Cycle 751 primary and independent certificates bind the complete ambient graph")

# Replay the all-row streamed implementation read-only.  Its own input-bound
# certificate and every transitive predecessor certificate were validated above.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / C751_INDEPENDENT_RECEIPT_PATH).resolve()


def write_except_dependency(path, data, *args, **kwargs):
    if path.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(path, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = write_except_dependency
try:
    with contextlib.redirect_stdout(io.StringIO()):
        predecessor = runpy.run_path(
            str(ROOT / C751_CHECKER_PATH),
            run_name="__cycle751_independent_dependency__",
        )
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

gate(
    "independent.predecessor_live_replay",
    predecessor.get("failed") == 0 and predecessor.get("passed", 0) >= 16,
    "the all-row Cycle 751 dependency replays live with every named gate passing",
)

pair_counts = predecessor["pair_counts"].copy()
incidence = predecessor["predecessor"]["incidence"]
census = predecessor["census"]
group = predecessor["predecessor"]["predecessor"]["group"]
target_identity = predecessor["predecessor"]["predecessor"]["C746"][
    "direct_dependency"
]["target_identity"]
np.fill_diagonal(pair_counts, 0)
adjacency = pair_counts == 0
np.fill_diagonal(adjacency, False)
neighbors = [set(int(x) for x in np.flatnonzero(adjacency[v])) for v in range(192)]

gate(
    "independent.all_rows",
    incidence.shape == (15800, 192)
    and set(int(value) for value in incidence.sum(axis=0)) == {1975}
    and set(int(value) for value in adjacency.sum(axis=1)) == {33},
    "all 15800 cutting rows and all 192 pieces enter the streamed pair-count graph",
)

# Enumerate each induced Q4 exactly once, rooted at its least-numbered vertex.
# Coordinate masks are completed by exact adjacency to every already assigned
# mask; final induced degrees and edge counts are checked independently.
hamming = [[(left ^ right).bit_count() for right in range(16)] for left in range(16)]
completion_order = sorted(
    (mask for mask in range(16) if mask.bit_count() >= 2),
    key=lambda mask: (mask.bit_count(), mask),
)
shapes = set()
coordinates = {}

for root in range(192):
    labels = {0: root}

    def complete(index):
        if index == len(completion_order):
            shape = tuple(sorted(labels.values()))
            shapes.add(shape)
            coordinates.setdefault(
                shape,
                tuple(next(mask for mask, vertex in labels.items() if vertex == value)
                      for value in shape),
            )
            return
        mask = completion_order[index]
        lower = [mask ^ (1 << bit) for bit in range(4) if (mask >> bit) & 1]
        candidates = set.intersection(*(neighbors[labels[value]] for value in lower))
        for vertex in candidates.difference(labels.values()):
            if vertex <= root:
                continue
            if all(
                (labels[other] in neighbors[vertex]) == (hamming[mask][other] == 1)
                for other in labels
            ):
                labels[mask] = vertex
                complete(index + 1)
                del labels[mask]

    root_neighbors = sorted(vertex for vertex in neighbors[root] if vertex > root)
    for basis in itertools.combinations(root_neighbors, 4):
        if any(
            basis[right] in neighbors[basis[left]]
            for left in range(4)
            for right in range(left + 1, 4)
        ):
            continue
        for bit, vertex in enumerate(basis):
            labels[1 << bit] = vertex
        complete(0)
        for bit in range(4):
            del labels[1 << bit]

through_piece = [0] * 192
bad_shape = 0
for shape in shapes:
    local = adjacency[np.ix_(shape, shape)]
    bad_shape += int(
        int(local.sum()) != 64 or set(int(value) for value in local.sum(axis=1)) != {4}
    )
    for vertex in shape:
        through_piece[vertex] += 1

gate(
    "independent.q4_census",
    len(shapes) == 59736
    and set(through_piece) == {4978}
    and bad_shape == 0
    and 16 * len(shapes) == sum(through_piece),
    "least-vertex coordinate completion gives 59736 induced Q4s and 4978 through every piece",
)

shape_set = set(shapes)
symmetry_failures = 0
for permutation in group:
    if any(tuple(sorted(int(permutation[v]) for v in shape)) not in shape_set for shape in shapes):
        symmetry_failures += 1
gate(
    "independent.symmetry_closure",
    len(group) == 384 and symmetry_failures == 0,
    "all 384 supplied incidence symmetries preserve the complete induced-Q4 set",
)

reading_names = ("zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip")
target_vectors = {}
for name in reading_names:
    support = target_identity["targets"][name]["witness_support"]
    target_vectors[name] = (
        incidence[:, support].sum(axis=1) & 1
    ).astype(np.uint8)
target_packed = {
    np.packbits(vector).tobytes(): name for name, vector in target_vectors.items()
}
packed_columns = np.packbits(incidence.T, axis=1)
shape_reading = {}
for shape in shapes:
    signature = np.bitwise_xor.reduce(packed_columns[list(shape)], axis=0).tobytes()
    name = target_packed.get(signature)
    if name is not None:
        shape_reading[shape] = name
reading_counts = {
    name: sum(value == name for value in shape_reading.values()) for name in reading_names
}
gate(
    "independent.reading_partition",
    len(shape_reading) == 60
    and reading_counts["four"] == 60
    and all(reading_counts[name] == 0 for name in reading_names if name != "four"),
    "59676 induced Q4s realize none of the eight declared readings and 60 realize four",
)

carrier_set = {tuple(sorted(carrier)) for carrier in census}
q4_carriers = shape_set.intersection(carrier_set)
pair_total = {
    shape: int(pair_counts[np.ix_(shape, shape)].sum() // 2) for shape in shapes
}
ordered_shapes = sorted(shapes, key=lambda shape: (pair_total[shape], shape))
carrier_maximum = max(pair_total[shape] for shape in q4_carriers)
noncarrier_minimum = min(pair_total[shape] for shape in shape_set - carrier_set)
gate(
    "independent.pair_total_separation",
    len(q4_carriers) == 60
    and set(shape_reading) == q4_carriers
    and set(ordered_shapes[:60]) == q4_carriers
    and carrier_maximum == 19800
    and noncarrier_minimum == 20338,
    "pair total exactly separates the 60 four-reading Q4s from the 59676 no-reading Q4s",
)

local_gaps = []
local_successes = 0
for vertex in range(192):
    local = sorted(
        (shape for shape in shapes if vertex in shape),
        key=lambda shape: (pair_total[shape], shape),
    )
    local_carriers = [shape for shape in q4_carriers if vertex in shape]
    if len(local) == 4978 and len(local_carriers) == 5 and set(local[:5]) == set(local_carriers):
        local_successes += 1
        local_gaps.append(pair_total[local[5]] - pair_total[local[4]])
gate(
    "independent.local_separation",
    local_successes == 192 and min(local_gaps) == 538,
    "at every piece the five least pair-total Q4s are its carriers, with minimum next-step 538",
)

separate_two_three = 0
separate_three_four = 0
far_all_433 = 0
carrier_bands = {2: set(), 3: set(), 4: set()}
for shape in shapes:
    coordinate = dict(zip(shape, coordinates[shape]))
    bands = {2: [], 3: [], 4: []}
    for left, right in itertools.combinations(shape, 2):
        distance = (coordinate[left] ^ coordinate[right]).bit_count()
        if distance >= 2:
            bands[distance].append(int(pair_counts[left, right]))
    separate_two_three += int(max(bands[2]) < min(bands[3]))
    separate_three_four += int(max(bands[3]) < min(bands[4]))
    far_all_433 += int(min(bands[4]) == max(bands[4]) == 433)
    if shape in q4_carriers:
        for distance in carrier_bands:
            carrier_bands[distance].update(bands[distance])
gate(
    "independent.weaker_tests",
    separate_two_three == 60
    and separate_three_four == 1488
    and far_all_433 == 672,
    "the two/three separation is exact while the three/four and antipodal tests admit 1488 and 672",
)
gate(
    "independent.carrier_distance_bands",
    carrier_bands == {
        2: {170, 171, 173, 174, 178, 183, 184},
        3: {240, 245, 250},
        4: {433},
    },
    "all Q4-carrier pair-count bands reproduce the current Cycle 750 certificate",
)

# Discrete-convex parity floor.  Start each odd row at multiplicity one and
# each even row at zero; every added pair of incidences costs 2m+1 pairs when
# the current row multiplicity is m.  The sum of the cheapest required
# marginal costs is the exact integer-program minimum.
odd_rows = int(target_vectors["four"].sum())
meetings = 16 * int(incidence[:, 0].sum())
increments_needed = (meetings - odd_rows) // 2
marginal_costs = []
for parity in target_vectors["four"]:
    start = int(parity)
    marginal_costs.extend(2 * multiplicity + 1 for multiplicity in range(start, 16, 2))
marginal_costs.sort()
parity_floor = sum(marginal_costs[:increments_needed])
all_carrier_totals = sorted({
    int(pair_counts[np.ix_(tuple(sorted(carrier)), tuple(sorted(carrier)))].sum() // 2)
    for carrier in census
})
best = min(q4_carriers, key=lambda shape: pair_total[shape])
best_histogram = np.bincount(incidence[:, best].sum(axis=1), minlength=17)
gate(
    "independent.parity_floor",
    odd_rows == 5664
    and meetings == 31600
    and increments_needed == 12968
    and parity_floor == 18632
    and min(pair_total[shape] for shape in q4_carriers) >= parity_floor,
    "discrete-convex marginal costs independently derive the 18632 parity floor",
)
gate(
    "independent.minimum_histogram",
    pair_total[best] == 19640
    and [(index, int(value)) for index, value in enumerate(best_histogram) if value]
    == [(0, 252), (1, 2832), (2, 9632), (3, 2832), (4, 252)]
    and sum(index * int(value) for index, value in enumerate(best_histogram)) == meetings
    and sum(index * (index - 1) // 2 * int(value)
            for index, value in enumerate(best_histogram)) == 19640
    and all_carrier_totals == [19640, 19672, 19800, 24216],
    "one minimum Q4 carrier is 1008 above the floor and all 132 carriers have four totals",
)


def primary_contract(receipt):
    census_result = receipt.get("induced_q4_census", {})
    separation = receipt.get("pair_total_separation", {})
    floor = receipt.get("parity_floor", {})
    dependencies = receipt.get("direct_dependencies", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-shape-census-cycle752-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and receipt.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and dependencies.get("cycle750", {}).get("receipt_sha256") == sha256(C750_RECEIPT_PATH)
        and dependencies.get("cycle750", {}).get("independent_receipt_sha256")
        == sha256(C750_INDEPENDENT_RECEIPT_PATH)
        and dependencies.get("cycle751", {}).get("receipt_sha256") == sha256(C751_RECEIPT_PATH)
        and dependencies.get("cycle751", {}).get("independent_receipt_sha256")
        == sha256(C751_INDEPENDENT_RECEIPT_PATH)
        and census_result.get("induced_q4_count") == 59736
        and census_result.get("through_each_piece") == 4978
        and census_result.get("declared_reading_counts") == {"four": 60, "none": 59676}
        and separation.get("q4_carrier_maximum") == 19800
        and separation.get("other_q4_minimum") == 20338
        and floor.get("derived_lower_bound") == 18632
        and floor.get("minimum_q4_carrier_total") == 19640
    )


PRIMARY_OK = primary_contract(PRIMARY)
gate("independent.primary_contract", C750_OK and C751_OK and PRIMARY_OK,
     "the Cycle 752 primary receipt equals the independent all-row reconstruction")
bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate("hostile.primary_status", not primary_contract(bad_primary),
     "a failing primary receipt is rejected")
bad_census = copy.deepcopy(PRIMARY)
bad_census["induced_q4_census"]["induced_q4_count"] = 59735
gate("hostile.q4_census", not primary_contract(bad_census),
     "a changed induced-Q4 census is rejected")
bad_separation = copy.deepcopy(PRIMARY)
bad_separation["pair_total_separation"]["other_q4_minimum"] = 20337
gate("hostile.pair_total", not primary_contract(bad_separation),
     "a changed pair-total boundary is rejected")
bad_c750 = copy.deepcopy(C750I)
bad_c750["status"] = "fail"
gate("hostile.cycle750", not cycle750_contract(C750, bad_c750),
     "a failing direct Cycle 750 independent certificate is rejected")
bad_c751 = copy.deepcopy(C751)
bad_c751["carrier_embedding"]["four_cube_antipodal_pairs_at_global_distance_four"] = 1
gate("hostile.cycle751", not cycle751_contract(bad_c751, C751I),
     "a stale total-isometry predecessor claim is rejected")

print("per_element: checked -- all 192 pieces enter the complete induced-Q4 and pair-total census", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- this finite binary incidence object has no modal decomposition", flush=True)
print("per_block: checked -- every one of the 15800 cutting rows enters the streamed co-incidence matrix", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, causal, or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-shape-census-cycle752-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(incidence),
        "support_columns": incidence.shape[1],
        "processed_pair_rows": len(incidence),
        "pair_counter": "Cycle 751 row-streamed unordered pairs",
        "q4_enumerator": "least-vertex coordinate completion",
        "complete_carrier_count": len(census),
    },
    "induced_q4_census": {
        "induced_q4_count": len(shapes),
        "through_each_piece": through_piece[0] if len(set(through_piece)) == 1 else through_piece,
        "symmetries_preserving_set": len(group) - symmetry_failures,
        "declared_reading_counts": {"four": reading_counts["four"], "none": len(shapes) - len(shape_reading)},
    },
    "pair_total_separation": {
        "q4_carriers": len(q4_carriers),
        "q4_carrier_minimum": min(pair_total[shape] for shape in q4_carriers),
        "q4_carrier_maximum": carrier_maximum,
        "other_q4_minimum": noncarrier_minimum,
        "pieces_with_exact_local_five": local_successes,
        "minimum_local_next_step": min(local_gaps),
        "two_three_separation_count": separate_two_three,
        "three_four_separation_count": separate_three_four,
        "all_antipodes_433_count": far_all_433,
    },
    "parity_floor": {
        "odd_rows": odd_rows,
        "total_meetings": meetings,
        "derived_lower_bound": parity_floor,
        "minimum_q4_carrier_total": pair_total[best],
        "minimum_over_floor": pair_total[best] - parity_floor,
        "minimum_multiplicity_histogram": {
            str(index): int(value) for index, value in enumerate(best_histogram) if value
        },
        "all_carrier_totals": all_carrier_totals,
    },
    "direct_dependencies": {
        "cycle750": {
            "receipt_sha256": sha256(C750_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C750_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C750_OK,
        },
        "cycle751": {
            "receipt_sha256": sha256(C751_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C751_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C751_OK,
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
