"""Independent Cycle 753 forced-mean and multiplicity-ranking checker.

This checker imports no Cycle 753 primary symbols.  It live-replays the
structurally independent Cycle 752 least-vertex/row-streamed checker, then
computes every cutting-multiplicity histogram in row blocks rather than the
primary's shape-blocked profile path.
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
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_"
    "CYCLE753_NOTE_2026-08-09.md"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
C752_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_"
    "CYCLE752_NOTE_2026-08-09.md"
)
C752_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py"
)
C752_CHECKER_PATH = (
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "independent_check_2026_08_09.py"
)
C752_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "2026_08_09_receipt_2026-08-09.json"
)
C752_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_CYCLE753_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py",
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_CYCLE752_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py",
    "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_shape_census_least_sharing_cycle752_independent_check_2026_08_09_receipt_2026-08-09.json",
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
        (ROOT / path).is_file() and recorded.get(path) == sha256(path)
        for path in recorded
    )


def write_failure(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-shared-count-variance-cycle753-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    compact = detail if len(detail) <= 112 else detail[:109] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


def cycle752_contract(primary, independent):
    census = primary.get("induced_q4_census", {})
    separation = primary.get("pair_total_separation", {})
    independent_census = independent.get("induced_q4_census", {})
    independent_separation = independent.get("pair_total_separation", {})
    return (
        primary.get("schema") == "physical-cell-cutting-shape-census-cycle752-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C752_PRIMARY_PATH)
        and inputs_current(primary)
        and census.get("induced_q4_count") == 59736
        and census.get("declared_reading_counts") == {"four": 60, "none": 59676}
        and separation.get("q4_carrier_minimum") == 19640
        and separation.get("other_q4_minimum") == 20338
        and independent.get("schema")
        == "physical-cell-cutting-shape-census-cycle752-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("claim_type") == "bounded_theorem"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C752_CHECKER_PATH)
        and inputs_current(independent)
        and independent_census.get("induced_q4_count") == 59736
        and independent_census.get("declared_reading_counts")
        == {"four": 60, "none": 59676}
        and independent_separation.get("q4_carrier_minimum") == 19640
        and independent_separation.get("other_q4_minimum") == 20338
    )


def primary_contract(receipt):
    forced = receipt.get("forced_mean_identity", {})
    floor = receipt.get("parity_floor", {})
    rankings = receipt.get("finite_q4_rankings", {})
    twice = rankings.get("twice_met", {})
    odd = rankings.get("odd_met", {})
    dependency = receipt.get("direct_dependencies", {}).get("cycle752", {})
    boundary = receipt.get("boundary", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-shared-count-variance-cycle753-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and dependency.get("contract_current") is True
        and dependency.get("receipt_sha256") == sha256(C752_RECEIPT_PATH)
        and dependency.get("independent_receipt_sha256")
        == sha256(C752_INDEPENDENT_RECEIPT_PATH)
        and forced.get("induced_q4_count") == 59736
        and forced.get("total_meetings") == 31600
        and forced.get("identity_failures") == 0
        and floor.get("derived_lower_bound") == 18632
        and floor.get("minimum_carrier_total") == 19640
        and rankings.get("q4_carriers") == 60
        and twice.get("top_set_is_exactly_carriers") is True
        and twice.get("least_carrier_value") == 9616
        and twice.get("next_noncarrier_value") == 8688
        and odd.get("strictly_above") == 57972
        and odd.get("equal") == 60
        and odd.get("strictly_below") == 1704
        and odd.get("equality_set_is_exactly_carriers") is True
        and boundary.get("odd_count_equality_also_classifies_q4_carriers") is True
        and boundary.get("twice_met_threshold_is_unique_possible_classifier") is False
    )


write_failure("checker has not completed")
C752 = load(C752_RECEIPT_PATH)
C752I = load(C752_INDEPENDENT_RECEIPT_PATH)
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C752_OK = cycle752_contract(C752, C752I)
gate("independent.cycle752_contract", C752_OK,
     "current Cycle 752 primary and helper receipts bind the complete induced-Q4 population")

# Execute the existing independent predecessor without allowing it to rewrite
# its canonical receipt.  Its least-vertex enumerator and row-streamed pair
# counter are deliberately different from the Cycle 753 primary path.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / C752_INDEPENDENT_RECEIPT_PATH).resolve()


def guarded_write_text(self, data, *args, **kwargs):
    if self.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(self, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = guarded_write_text
capture = io.StringIO()
try:
    with contextlib.redirect_stdout(capture):
        predecessor = runpy.run_path(str(ROOT / C752_CHECKER_PATH), run_name="__main__")
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

predecessor_stdout = capture.getvalue()
gate(
    "independent.cycle752_live_replay",
    predecessor.get("failed") == 0
    and "FAIL " not in predecessor_stdout
    and "TOTAL: PASS=19 FAIL=0" in predecessor_stdout,
    "the structurally independent Cycle 752 checker completes live with all 19 gates",
)

incidence = np.asarray(predecessor["incidence"], dtype=np.float32)
shapes = sorted(tuple(int(value) for value in shape) for shape in predecessor["shapes"])
q4_carriers = {tuple(int(value) for value in shape)
               for shape in predecessor["q4_carriers"]}
all_carriers = [tuple(sorted(int(value) for value in carrier))
                for carrier in predecessor["census"]]
pair_counts = np.asarray(predecessor["pair_counts"], dtype=np.int64)
target_four = np.asarray(predecessor["target_vectors"]["four"], dtype=np.int64)

nshape = len(shapes)
shape_index = np.asarray(shapes, dtype=np.int64)
indicator = np.zeros((192, nshape), dtype=np.float32)
indicator[shape_index.ravel(), np.repeat(np.arange(nshape), 16)] = 1.0
histogram = np.zeros((17, nshape), dtype=np.int64)
for lower in range(0, incidence.shape[0], 200):
    upper = min(lower + 200, incidence.shape[0])
    multiplicity = incidence[lower:upper] @ indicator
    for value in range(17):
        histogram[value] += np.count_nonzero(multiplicity == value, axis=0)
del indicator, incidence

values = np.arange(17, dtype=np.int64)
profile_rows = histogram.sum(axis=0)
profile_weight = (histogram * values[:, None]).sum(axis=0)
squared_spread = (histogram * ((values - 2) ** 2)[:, None]).sum(axis=0)
odd_count = histogram[1::2].sum(axis=0)
twice_count = histogram[2]
maximum_multiplicity = np.max(
    np.where(histogram > 0, values[:, None], -1), axis=0
)
pair_total = np.asarray([
    int(pair_counts[np.ix_(shape, shape)].sum() // 2) for shape in shapes
], dtype=np.int64)
carrier_mask = np.asarray([shape in q4_carriers for shape in shapes], dtype=bool)

gate(
    "independent.complete_profiles",
    nshape == 59736
    and np.all(profile_rows == 15800)
    and np.all(profile_weight == 31600)
    and np.all(maximum_multiplicity <= 8),
    "all 59736 profiles contain 15800 rows, weight 31600, and multiplicity at most eight",
)
gate(
    "independent.forced_mean_identity",
    np.all(2 * pair_total == 2 * 15800 + squared_spread)
    and np.all((squared_spread & 1) == 0),
    "row-blocked profiles independently give T = 15800 + squared spread/2 for every Q4",
)

odd_rows = int(target_four.sum())
floor = 15800 + odd_rows // 2
equality_profile = {1: odd_rows // 2, 2: 15800 - odd_rows, 3: odd_rows // 2}
best_index = min(np.flatnonzero(carrier_mask), key=lambda index: pair_total[index])
best_profile = {
    int(index): int(value) for index, value in enumerate(histogram[:, best_index]) if value
}
gate(
    "independent.parity_floor",
    odd_rows == 5664
    and floor == 18632
    and equality_profile == {1: 2832, 2: 10136, 3: 2832}
    and np.all(pair_total[carrier_mask] >= floor),
    "parity plus the forced mean independently gives floor 18632 and the unique equality profile",
)
gate(
    "independent.minimum_profile",
    pair_total[best_index] == 19640
    and best_profile == {0: 252, 1: 2832, 2: 9632, 3: 2832, 4: 252},
    "the minimum Q4 carrier is 1008 over the floor with the independently rebuilt five-bin profile",
)

ncarrier = int(np.count_nonzero(carrier_mask))
twice_order = np.argsort(-twice_count, kind="stable")
twice_top = {shapes[int(index)] for index in twice_order[:ncarrier]}
least_carrier_twice = int(twice_count[twice_order[ncarrier - 1]])
next_twice = int(twice_count[twice_order[ncarrier]])
gate(
    "independent.twice_met_ranking",
    ncarrier == 60
    and twice_top == q4_carriers
    and least_carrier_twice == 9616
    and next_twice == 8688
    and int(np.count_nonzero(twice_count > 9616)) == 36
    and int(np.count_nonzero(twice_count == 9616)) == 24,
    "the 60 largest twice-met counts are exactly the Q4 carriers with the 9616/8688 boundary",
)

odd_above = int(np.count_nonzero(odd_count > odd_rows))
odd_equal = int(np.count_nonzero(odd_count == odd_rows))
odd_below = int(np.count_nonzero(odd_count < odd_rows))
odd_equal_set = {shapes[int(index)] for index in np.flatnonzero(odd_count == odd_rows)}
gate(
    "independent.odd_met_ranking",
    odd_above == 57972
    and odd_equal == 60
    and odd_below == 1704
    and odd_equal_set == q4_carriers,
    "odd-count equality also classifies the carriers, while descending rank places 57972 shapes above them",
)

linear_form = 2 * pair_total == 3 * (31600 - odd_count) - 4 * twice_count
capped_at_four = maximum_multiplicity <= 4
gate(
    "independent.cap_four_linear_form",
    int(maximum_multiplicity.max()) == 8
    and int(np.count_nonzero(maximum_multiplicity > 4)) == 42192
    and int(np.count_nonzero(linear_form)) == 17544
    and np.array_equal(linear_form, capped_at_four),
    "the odd/twice linear form holds exactly on the 17544 Q4s capped at multiplicity four",
)

all_carrier_spreads = sorted({
    int((((np.asarray(predecessor["incidence"])[:, carrier].sum(axis=1)) - 2) ** 2).sum())
    for carrier in all_carriers
})
gate(
    "independent.all_carrier_spreads",
    len(all_carriers) == 132
    and all_carrier_spreads == [7680, 7744, 8000, 16832],
    "all 132 minimum carriers independently have exactly four squared-spread values",
)

PRIMARY_OK = primary_contract(PRIMARY)
gate("independent.primary_contract", C752_OK and PRIMARY_OK,
     "the Cycle 753 primary receipt matches the independent forced-mean and ranking reconstruction")
bad_primary = copy.deepcopy(PRIMARY)
bad_primary["finite_q4_rankings"]["odd_met"]["equality_set_is_exactly_carriers"] = False
gate("hostile.primary_odd_classifier", not primary_contract(bad_primary),
     "a reversion that hides the odd-count equality classifier is rejected")
bad_cycle752 = copy.deepcopy(C752I)
bad_cycle752["status"] = "fail"
gate("hostile.cycle752_status", not cycle752_contract(C752, bad_cycle752),
     "a failing direct Cycle 752 independent certificate is rejected")

print("per_element: checked -- all 192 pieces enter the independently replayed Q4 multiplicity census", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- this finite binary incidence object has no modal decomposition", flush=True)
print("per_block: checked -- every one of the 15800 cutting rows enters the row-blocked profile reconstruction", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, causal, or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-shared-count-variance-cycle753-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle752": {
            "receipt_sha256": sha256(C752_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C752_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C752_OK,
            "live_replay_passed": predecessor.get("failed") == 0,
        },
    },
    "independent_reconstruction": {
        "cuttings": 15800,
        "support_columns": 192,
        "induced_q4_count": nshape,
        "q4_carriers": ncarrier,
        "profile_method": "row-blocked incidence multiplication after least-vertex Q4 enumeration",
    },
    "forced_mean_identity": {
        "total_meetings": 31600,
        "mean_multiplicity": 2,
        "identity_failures": int(np.count_nonzero(2 * pair_total != 31600 + squared_spread)),
    },
    "parity_floor": {
        "odd_rows": odd_rows,
        "derived_lower_bound": floor,
        "equality_profile": {str(key): value for key, value in equality_profile.items()},
        "minimum_carrier_total": int(pair_total[best_index]),
        "minimum_profile": {str(key): value for key, value in best_profile.items()},
    },
    "finite_q4_rankings": {
        "twice_met": {
            "top_set_is_exactly_carriers": twice_top == q4_carriers,
            "least_carrier_value": least_carrier_twice,
            "next_noncarrier_value": next_twice,
        },
        "odd_met": {
            "carrier_value": odd_rows,
            "strictly_above": odd_above,
            "equal": odd_equal,
            "strictly_below": odd_below,
            "equality_set_is_exactly_carriers": odd_equal_set == q4_carriers,
        },
        "maximum_multiplicity": int(maximum_multiplicity.max()),
        "shapes_above_multiplicity_four": int(np.count_nonzero(maximum_multiplicity > 4)),
        "linear_form_shapes": int(np.count_nonzero(linear_form)),
    },
    "all_minimum_carriers": {
        "count": len(all_carriers),
        "distinct_squared_spreads": all_carrier_spreads,
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
