"""Independent Cycle 747 checker.

This executable imports no symbols from the primary.  It reconstructs the exact-cover
population with the opposite pivot convention, re-derives the all-marked weight-eight
classification, consumes the independently checked Cycle 745 lower-size census, and
recomputes the weight-twenty XOR construction from the landed anchored supports.
"""
import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "independent_check_2026_08_08.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_"
    "CYCLE747_NOTE_2026-08-08.md"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "2026_08_08_receipt_2026-08-08.json"
)
C745_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md"
C745_PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py"
C745_CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05.py"
)
C745_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_"
    "receipt_2026-08-05.json"
)
C745_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
C746_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md"
)
C746_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py"
)
C746_CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08.py"
)
C746_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_"
    "receipt_2026-08-08.json"
)
C746_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py",
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08_receipt_2026-08-08.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py",
    "scripts/physical_cell_cutting_sixteen_census_cycle745_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_sixteen_census_cycle745_independent_check_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py",
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08.py",
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_receipt_2026-08-08.json",
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08_receipt_2026-08-08.json",
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
        "schema": (
            "physical-cell-cutting-flip-partner-carrier-bracket-"
            "cycle747-independent-v1"
        ),
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


write_failure("checker has not completed")
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C745 = load(C745_RECEIPT_PATH)
C745I = load(C745_INDEPENDENT_RECEIPT_PATH)
C746 = load(C746_RECEIPT_PATH)
C746I = load(C746_INDEPENDENT_RECEIPT_PATH)

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
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


# Reconstruct the finite object.  The primary chooses the least uncovered sample;
# this checker deliberately chooses the greatest.
def det4(array):
    def minors(row0, row1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (
                    array[:, row0, i] * array[:, row1, j]
                    - array[:, row0, j] * array[:, row1, i]
                )
        return out

    left = minors(0, 1)
    right = minors(2, 3)
    return (
        left[(0, 1)] * right[(2, 3)]
        - left[(0, 2)] * right[(1, 3)]
        + left[(0, 3)] * right[(1, 2)]
        + left[(1, 2)] * right[(0, 3)]
        - left[(1, 3)] * right[(0, 2)]
        + left[(2, 3)] * right[(0, 1)]
    )


corners = [
    (x, y, z, t)
    for x in (0, 1)
    for y in (0, 1)
    for z in (0, 1)
    for t in (0, 1)
]
vectors = np.array(corners, dtype=np.int64)
pairs = list(itertools.combinations(range(5), 2))
subsets = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
volume = np.abs(det4(vectors[subsets[:, 1:]] - vectors[subsets[:, 0]][:, None, :]))
unimodular = subsets[volume == 1]


def adjacency_cost(pieces):
    total = np.zeros(len(pieces), dtype=np.int64)
    for a, b in pairs:
        distance = np.abs(vectors[pieces[:, a]] - vectors[pieces[:, b]]).sum(axis=1)
        total += (distance > 1).astype(np.int64)
    return total


costs = adjacency_cost(unimodular)
least_cost = int(costs.min())
minimum_pieces = [i for i in range(len(unimodular)) if int(costs[i]) == least_cost]
matrices = np.stack([(vectors[piece[1:]] - vectors[piece[0]]).T for piece in unimodular])
inverse = np.rint(np.linalg.inv(matrices.astype(float))).astype(np.int64)
position = {corner: index for index, corner in enumerate(corners)}
rotations = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(permutation):
            rotation[i, j] = signs[i]
        if int(round(np.linalg.det(rotation.astype(float)))) == 1:
            rotations.append(rotation)
center = np.array([1, 1, 1], dtype=np.int64)
geometry = []
for rotation in rotations:
    for time_flip in (0, 1):
        image = []
        for x, y, z, t in corners:
            point = rotation @ (2 * np.array([x, y, z], dtype=np.int64) - center) + center
            key = (
                int(point[0]) // 2,
                int(point[1]) // 2,
                int(point[2]) // 2,
                (1 - t) if time_flip else t,
            )
            image.append(position[key])
        geometry.append((rotation, time_flip, np.array(image, dtype=np.int64)))
piece_index = {
    tuple(int(corner) for corner in support): index
    for index, support in enumerate(unimodular)
}
orbit_label = -np.ones(len(unimodular), dtype=np.int64)
representatives = []
for index in range(len(unimodular)):
    if orbit_label[index] >= 0:
        continue
    label = len(representatives)
    representatives.append(index)
    for _rotation, _time_flip, image in geometry:
        transformed = tuple(sorted(int(image[corner]) for corner in unimodular[index]))
        orbit_label[piece_index[transformed]] = label
offsets = np.array([0, 1, 7, 49, 343], dtype=np.int64)
bound = max(
    int(np.abs(inverse).max()),
    int(np.abs(inverse.sum(axis=2) - 1).max()),
)
weights = 2 * (bound * int(offsets.sum()) + 1 + offsets)
scale = int(weights.sum())

# Generate the orbit-labelled interior samples from the geometric orbit
# representatives.  Exact-cover traversal still uses the opposite pivot below.
spatial_center = np.array([scale // 2, scale // 2, scale // 2], dtype=np.int64)
samples = set()
for index in representatives:
    barycenter = (weights[:, None] * vectors[unimodular[index]]).sum(axis=0)
    for rotation, time_flip, _image in geometry:
        spatial = rotation @ (barycenter[:3] - spatial_center) + spatial_center
        samples.add((
            int(spatial[0]),
            int(spatial[1]),
            int(spatial[2]),
            scale - int(barycenter[3]) if time_flip else int(barycenter[3]),
        ))
sample_array = np.array(sorted(samples), dtype=np.int64)
sample_t = sample_array.T
inside_masks = [0] * len(unimodular)
by_sample = {}
for index in minimum_pieces:
    lam = inverse[index] @ (
        sample_t - (scale * vectors[unimodular[index, 0]])[:, None]
    )
    total = lam.sum(axis=0)
    inside = (lam > 0).all(axis=0) & (total < scale)
    mask = 0
    for sample in np.flatnonzero(inside):
        sample = int(sample)
        mask |= 1 << sample
        by_sample.setdefault(sample, []).append(index)
    inside_masks[index] = mask

all_samples = (1 << len(sample_array)) - 1
solutions = []


def exact_cover(covered, chosen):
    if covered == all_samples:
        solutions.append(tuple(sorted(chosen)))
        return
    remaining = all_samples & ~covered
    sample = remaining.bit_length() - 1
    for index in by_sample[sample]:
        mask = inside_masks[index]
        if mask & covered:
            continue
        chosen.append(index)
        exact_cover(covered | mask, chosen)
        chosen.pop()


exact_cover(0, [])
used = sorted(set(index for solution in solutions for index in solution))
piece_to_column = {piece: column for column, piece in enumerate(used)}
incidence = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    for piece in solution:
        incidence[row, piece_to_column[piece]] = 1

row_weight = sorted(set(int(value) for value in incidence.sum(axis=1)))
column_weight = sorted(set(int(value) for value in incidence.sum(axis=0)))
gate(
    "independent.population",
    len(solutions) == 15800
    and len(used) == 192
    and row_weight == [24]
    and column_weight == [1975],
    "opposite-pivot reconstruction gives 15800 rows, 192 columns, weights 24 and 1975",
)

target_identity = C746.get("direct_dependency", {}).get("target_identity", {})
targets = target_identity.get("targets", {})
four_support = targets.get("four", {}).get("witness_support")
four = (incidence[:, four_support].sum(axis=1) & 1).astype(np.uint8)
four_flip = four ^ 1
one = np.ones(len(solutions), dtype=np.uint8)
gate(
    "independent.targets",
    int(four.sum()) == 5664
    and int(four_flip.sum()) == 10136
    and targets.get("four", {}).get("ones") == 5664
    and targets.get("four-flip", {}).get("ones") == 10136,
    "the reconstructed four target and its complement reproduce the bound target counts",
)

# Exact all-marked classification: lower bound by total incidence, then enumerate
# every eight-clique in the independently rebuilt noncooccurrence graph.
integer_incidence = incidence.astype(np.int32)
cooccurrence = integer_incidence.T @ integer_incidence
nonsharing = cooccurrence == 0
np.fill_diagonal(nonsharing, False)
adjacency = []
for column in range(192):
    mask = 0
    for other in range(192):
        if nonsharing[column, other]:
            mask |= 1 << other
    adjacency.append(mask)

all_marked = []


def extend_clique(chosen, candidates):
    if len(chosen) == 8:
        all_marked.append(tuple(chosen))
        return
    while candidates:
        low = candidates & -candidates
        column = low.bit_length() - 1
        candidates ^= low
        if len(chosen) + 1 + candidates.bit_count() < 8:
            return
        chosen.append(column)
        extend_clique(chosen, candidates & adjacency[column])
        chosen.pop()


extend_clique([], (1 << 192) - 1)
all_marked = sorted(set(all_marked))
all_marked_semantic = all(
    np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), one
    )
    for support in all_marked
)
through = sorted(set(sum(column in support for support in all_marked) for column in range(192)))
pair_counts = {}
for left in range(len(all_marked)):
    for right in range(left + 1, len(all_marked)):
        overlap = len(set(all_marked[left]) & set(all_marked[right]))
        pair_counts[overlap] = pair_counts.get(overlap, 0) + 1
gate(
    "independent.all_marked",
    8 * 1975 == 15800
    and len(all_marked) == 192
    and all_marked_semantic
    and through == [8]
    and pair_counts == {0: 15072, 1: 1920, 2: 960, 4: 384},
    "the counting floor is attained by exactly 192 independently enumerated weight-eight carriers",
)

anchored_four = [
    tuple(int(value) for value in support)
    for support in C745.get("four_reading_census", {}).get("anchored_supports", [])
]
anchored_semantic = len(anchored_four) == 11 and all(
    np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), four
    )
    for support in anchored_four
)
overlap_counts = {}
twenty = set()
for carrier in anchored_four:
    carrier_set = set(carrier)
    for all_one in all_marked:
        all_one_set = set(all_one)
        overlap = len(carrier_set & all_one_set)
        overlap_counts[overlap] = overlap_counts.get(overlap, 0) + 1
        if overlap == 2:
            twenty.add(tuple(sorted(carrier_set ^ all_one_set)))
twenty_semantic = all(
    len(support) == 20
    and np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), four_flip
    )
    for support in twenty
)
gate(
    "independent.weight_twenty",
    anchored_semantic
    and overlap_counts == {0: 1216, 1: 384, 2: 512}
    and len(twenty) == 512
    and twenty_semantic,
    "the landed eleven supports and independent weight-eight census give 512 distinct weight-twenty flip carriers",
)


def predecessor_contract(c745, c745i, c746, c746i):
    answers = c745i.get("exact_anchored_weight_sixteen_answers", {})
    exact = c745i.get("exact_syndrome_dp", {})
    forced = c746.get("forced_block_parity", {})
    reconstruction = c746i.get("independent_reconstruction", {})
    return (
        c745.get("schema") == "physical-cell-cutting-sixteen-census-cycle745-v2"
        and c745.get("status") == "pass"
        and c745.get("gates", {}).get("fail") == 0
        and c745.get("runner_sha256") == sha256(C745_PRIMARY_PATH)
        and inputs_current(c745)
        and c745.get("direct_dependencies", {}).get("cycle741_through_fourteen_bound") is True
        and c745i.get("schema")
        == "physical-cell-cutting-sixteen-census-cycle745-independent-v1"
        and c745i.get("status") == "pass"
        and c745i.get("gates", {}).get("fail") == 0
        and (c745i.get("checker_sha256") or c745i.get("runner_sha256"))
        == sha256(C745_CHECKER_PATH)
        and inputs_current(c745i)
        and answers.get("four-flip") is False
        and exact.get("execution_inventory_exact") is True
        and exact.get("executed_splits") == exact.get("expected_splits") == 2004
        and c745i.get("verified_group", {}).get("anchor_orbit_size") == 192
        and c746.get("schema") == "physical-cell-cutting-carrier-parity-law-cycle746-v2"
        and c746.get("status") == "pass"
        and c746.get("gates", {}).get("fail") == 0
        and c746.get("runner_sha256") == sha256(C746_PRIMARY_PATH)
        and inputs_current(c746)
        and forced.get("fixed_blocks") == ["total", "L", "R", "Q2", "Q3"]
        and c746i.get("schema")
        == "physical-cell-cutting-carrier-parity-law-cycle746-independent-v1"
        and c746i.get("status") == "pass"
        and c746i.get("gates", {}).get("fail") == 0
        and (c746i.get("checker_sha256") or c746i.get("runner_sha256"))
        == sha256(C746_CHECKER_PATH)
        and inputs_current(c746i)
        and reconstruction.get("fixed_blocks") == ["total", "L", "R", "Q2", "Q3"]
    )


PREDECESSORS_OK = predecessor_contract(C745, C745I, C746, C746I)
gate(
    "independent.lower_bound",
    PREDECESSORS_OK and len(twenty) == 512,
    "independent through-14 and weight-16 emptiness plus even parity leave 18 as the first candidate, while 20 is attained",
)


def primary_contract(receipt):
    all_one = receipt.get("all_marked_weight_eight", {})
    anchor = receipt.get("anchor_completeness", {})
    search = receipt.get("exact_search_through_sixteen", {})
    construction = receipt.get("weight_twenty_construction", {})
    residual = receipt.get("weight_eighteen_incomplete_search", {})
    bracket = receipt.get("minimum_bracket", {})
    primary_all_marked = sorted(tuple(row) for row in all_one.get("carriers", []))
    primary_twenty = sorted(tuple(row) for row in construction.get("distinct_flip_carriers", []))
    return (
        receipt.get("schema")
        == "physical-cell-cutting-flip-partner-carrier-bracket-cycle747-v2"
        and receipt.get("status") == "pass"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and primary_all_marked == all_marked
        and all_one.get("carrier_count") == 192
        and all_one.get("carriers_through_each_piece") == 8
        and anchor.get("geometric_piece_orbits") == [48, 48, 48, 48]
        and anchor.get("generated_piece_orbits") == [192]
        and anchor.get("all_eight_targets_transitive") is True
        and search.get("all_sweeps_complete") is True
        and search.get("four_flip_counts") == [0] * 8
        and search.get("weight_sixteen_splits") == 2004
        and construction.get("maximum_intersection") == 2
        and construction.get("distinct_flip_carrier_count") == 512
        and primary_twenty == sorted(twenty)
        and residual.get("licensed_anchor_cells") == 285
        and residual.get("scheduled_splits") == 4796
        and residual.get("searched_splits") == 4770
        and residual.get("refused_splits") == 26
        and residual.get("complete") is False
        and bracket == {
            "lower_bound": 18,
            "parity_forces_even": True,
            "upper_bound": 20,
            "weight_eighteen_resolved": False,
        }
    )


PRIMARY_OK = primary_contract(PRIMARY)
gate(
    "independent.primary_contract",
    PRIMARY_OK,
    "the final primary receipt equals the independent reconstruction and preserves the unresolved weight-18 residual",
)

bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate("hostile.primary_status", not primary_contract(bad_primary), "a failing primary receipt is rejected")
bad_all_marked = copy.deepcopy(PRIMARY)
bad_all_marked.setdefault("all_marked_weight_eight", {})["carriers"] = [[0]]
gate("hostile.all_marked", not primary_contract(bad_all_marked), "a changed weight-eight carrier is rejected")
bad_twenty = copy.deepcopy(PRIMARY)
bad_twenty.setdefault("weight_twenty_construction", {})["maximum_intersection"] = 3
gate("hostile.overlap", not primary_contract(bad_twenty), "a changed overlap ceiling is rejected")
bad_residual = copy.deepcopy(PRIMARY)
bad_residual.setdefault("weight_eighteen_incomplete_search", {})["complete"] = True
gate("hostile.eighteen", not primary_contract(bad_residual), "a false weight-18 completion claim is rejected")
bad_predecessor = copy.deepcopy(C745I)
bad_predecessor["exact_anchored_weight_sixteen_answers"]["four-flip"] = True
gate(
    "hostile.lower_bound",
    not predecessor_contract(C745, bad_predecessor, C746, C746I),
    "a reverted weight-16 emptiness certificate is rejected",
)

print("per_element: checked -- all 192 columns enter the independent incidence and clique calculations", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- the finite binary object has no modes", flush=True)
print("per_block: checked -- all 15800 rows and every predecessor search block are bound", flush=True)
print("lattice_wide: checked and not executed -- no multicell or continuum claim", flush=True)

receipt = {
    "schema": (
        "physical-cell-cutting-flip-partner-carrier-bracket-"
        "cycle747-independent-v1"
    ),
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(solutions),
        "support_columns": len(used),
        "pieces_per_cutting": row_weight[0],
        "cuttings_per_piece": column_weight[0],
        "exact_cover_pivot": "greatest uncovered sample",
        "all_marked_weight_eight_count": len(all_marked),
        "all_marked_through_each_piece": through[0],
        "all_marked_pair_intersection_counts": {
            str(key): value for key, value in sorted(pair_counts.items())
        },
        "anchored_four_count": len(anchored_four),
        "four_all_marked_overlap_counts": {
            str(key): value for key, value in sorted(overlap_counts.items())
        },
        "weight_twenty_flip_carrier_count": len(twenty),
    },
    "dependency_boundary": {
        "cycle745_and_independent_bound": PREDECESSORS_OK,
        "cycle746_and_independent_bound": PREDECESSORS_OK,
        "weight_eighteen_resolved": False,
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
