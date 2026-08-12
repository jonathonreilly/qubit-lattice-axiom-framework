"""Independent exact SAT and group-action check for Cycle 745.

This checker imports neither the Cycle 745 primary nor its search engine.  It rebuilds
the supplied 15800-by-192 incidence table with the opposite exact-cover pivot, rebuilds
the 48 geometric column permutations, semantically validates the two receipt-carried
extra permutations, and closes their generated action. Exact-weight-16 CNF searches
through one canonical anchor exclude an extra four carrier and every carrier of the
other five readings. Transitivity turns those empty anchored slices into global empty
censuses; all 132 positive witnesses and both orbit folds are checked separately.
"""

import copy
import hashlib
import itertools
import json
import resource
import time
from pathlib import Path

import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Cadical195

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05.py"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_"
    "receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C737_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
C737_PRIMARY_PATH = "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
C737_CHECKER_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C741_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md"
C741_PRIMARY_PATH = "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py"
C741_CHECKER_PATH = (
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py"
)
C741_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json"
)
C741_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
PRIMARY_INPUTS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    C741_NOTE_PATH,
    C741_PRIMARY_PATH,
    C741_CHECKER_PATH,
    C741_RECEIPT_PATH,
    C741_INDEPENDENT_RECEIPT_PATH,
    NOTE_PATH,
    CHECKER_PATH,
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    PRIMARY_PATH,
    PRIMARY_RECEIPT_PATH,
    "requirements.txt",
    "requirements-release.txt",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    C741_NOTE_PATH,
    C741_PRIMARY_PATH,
    C741_CHECKER_PATH,
    C741_RECEIPT_PATH,
    C741_INDEPENDENT_RECEIPT_PATH,
)
AUDIT_TIMEOUT_SEC = 900


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt, required_paths):
    expected = receipt.get("input_sha256", {})
    return set(expected) == set(required_paths) and all(
        expected.get(path) == sha256(path) for path in required_paths
    )


passed = 0
failed = 0
gates = []


def gate(condition, name, detail):
    global passed, failed
    ok = bool(condition)
    passed += int(ok)
    failed += int(not ok)
    gates.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def determinant(matrix):
    if len(matrix) == 1:
        return int(matrix[0][0])
    return sum(
        (-1 if column & 1 else 1) * int(value)
        * determinant([row[:column] + row[column + 1 :] for row in matrix[1:]])
        for column, value in enumerate(matrix[0])
    )


def gf2_basis_indices(rows):
    pivots = {}
    selected = []
    for index, value in enumerate(rows):
        row = int(value)
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                selected.append(index)
                break
            row ^= pivots[pivot]
    return pivots, selected


# Opposite-pivot reconstruction of the exact finite incidence object.
CORNERS = list(itertools.product((0, 1), repeat=4))
VERTICES = np.array(CORNERS, dtype=np.int64)
PIECES = []
INVERSES = []
for subset in itertools.combinations(range(16), 5):
    matrix = (VERTICES[list(subset[1:])] - VERTICES[subset[0]]).T
    if abs(determinant(matrix.tolist())) == 1:
        inverse = np.rint(np.linalg.inv(matrix.astype(float))).astype(np.int64)
        if np.array_equal(matrix @ inverse, np.eye(4, dtype=np.int64)):
            PIECES.append(subset)
            INVERSES.append(inverse)
INVERSES = np.array(INVERSES, dtype=np.int64)
PAIRS = list(itertools.combinations(range(5), 2))


def piece_cost(piece):
    points = VERTICES[list(piece)]
    return sum(
        sum(abs(int(points[a, coordinate]) - int(points[b, coordinate]))
            for coordinate in range(4)) > 1
        for a, b in PAIRS
    )


COSTS = np.array([piece_cost(piece) for piece in PIECES], dtype=np.int64)
MINIMUM = np.flatnonzero(COSTS == int(COSTS.min())).tolist()
corner_index = {corner: index for index, corner in enumerate(CORNERS)}
geometric_actions = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for row, column in enumerate(permutation):
            rotation[row, column] = signs[row]
        if round(np.linalg.det(rotation.astype(float))) != 1:
            continue
        for tick_flip in (False, True):
            action = []
            for x, y, z, tick in CORNERS:
                image = rotation @ (2 * np.array((x, y, z), dtype=np.int64) - 1) + 1
                target = (
                    int(image[0]) // 2,
                    int(image[1]) // 2,
                    int(image[2]) // 2,
                    1 - tick if tick_flip else tick,
                )
                action.append(corner_index[target])
            geometric_actions.append(action)
piece_index = {piece: index for index, piece in enumerate(PIECES)}
labels = np.full(len(PIECES), -1, dtype=np.int64)
representatives = []
for piece_number, piece in enumerate(PIECES):
    if labels[piece_number] >= 0:
        continue
    orbit = len(representatives)
    representatives.append(piece_number)
    for action in geometric_actions:
        image = tuple(sorted(action[corner] for corner in piece))
        labels[piece_index[image]] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_set = set()
for representative in representatives:
    piece = PIECES[representative]
    for action in geometric_actions:
        sample_set.add(tuple(int(value) for value in (
            weights[:, None] * VERTICES[[action[corner] for corner in piece]]
        ).sum(axis=0)))
samples = np.array(sorted(sample_set), dtype=np.int64)
sample_incidence = np.zeros((len(PIECES), len(samples)), dtype=np.uint8)
for piece_number, piece in enumerate(PIECES):
    bary = INVERSES[piece_number] @ (
        samples.T - (scale * VERTICES[piece[0]])[:, None]
    )
    sample_incidence[piece_number] = (bary > 0).all(axis=0) & (bary.sum(axis=0) < scale)
active = np.flatnonzero(sample_incidence[MINIMUM].any(axis=0))
sample_incidence = sample_incidence[:, active]
by_sample = {}
mask_by_piece = {}
for piece in MINIMUM:
    mask = 0
    for sample in np.flatnonzero(sample_incidence[piece]):
        mask |= 1 << int(sample)
        by_sample.setdefault(int(sample), []).append(piece)
    mask_by_piece[piece] = mask
all_samples = (1 << len(active)) - 1
solutions = []


def covers(covered, chosen):
    if covered == all_samples:
        solutions.append(tuple(sorted(chosen)))
        return
    remaining = all_samples & ~covered
    sample = remaining.bit_length() - 1
    for piece in by_sample[sample]:
        mask = mask_by_piece[piece]
        if mask & covered:
            continue
        chosen.append(piece)
        covers(covered | mask, chosen)
        chosen.pop()


covers(0, [])
used = sorted({piece for solution in solutions for piece in solution})
position = {piece: index for index, piece in enumerate(used)}
incidence = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    incidence[row, [position[piece] for piece in solution]] = 1
packed_rows = [bytes(row) for row in np.packbits(incidence, axis=1)]
canonical_incidence_hash = hashlib.sha256(b"".join(sorted(packed_rows))).hexdigest()
column_order = [[int(corner) for corner in PIECES[piece]] for piece in used]
column_order_hash = hashlib.sha256(
    json.dumps(column_order, separators=(",", ":")).encode("utf-8")
).hexdigest()
gate(
    len(PIECES) == 2672 and len(MINIMUM) == 400 and int(COSTS.min()) == 6
    and len(solutions) == 15800 and len(used) == 192
    and all(len(solution) == 24 for solution in solutions),
    "independent.population",
    "opposite-pivot exact covers reconstruct all 15800 rows on 192 used pieces",
)

primary_receipt = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))


def primary_contract_ok(receipt):
    target_identity = receipt.get("target_identity", {})
    search = receipt.get("complete_anchored_search_at_sixteen", {})
    group = receipt.get("transitive_group", {})
    boundary = receipt.get("nonconstant_reading_boundary", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-sixteen-census-cycle745-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and receipt_inputs_current(receipt, PRIMARY_INPUTS)
        and target_identity.get("canonical_incidence_rows_sha256")
        == canonical_incidence_hash
        and target_identity.get("support_column_order_sha256") == column_order_hash
        and len(target_identity.get("ordered_names", [])) == 18
        and target_identity.get("odd_control_non_column_space") is True
        and search.get("counts") == [11, 0, 0, 0, 0, 0, 2, 6, 12, 1, 3, 0]
        and search.get("scheduled_splits") == search.get("executed_splits") == 2004
        and search.get("execution_inventory_exact") is True
        and search.get("mismatched_returns") == search.get("duplicate_returns") == 0
        and group.get("generated_order") == 384
        and group.get("anchor_orbit_size") == 192
        and boundary.get("next_unsearched_size") == 18
        and boundary.get("attainment_at_eighteen_shown") is False
        and receipt.get("no_go_discipline", {}).get("status") == "PASS"
    )


gate(primary_contract_ok(primary_receipt), "receipt.contract",
     "the primary verdict, source, inputs, inventory and bounded claim are content-bound")

target_identity = primary_receipt["target_identity"]
ordered_names = target_identity["ordered_names"]
targets = {}
target_ok = True
for name in ordered_names:
    metadata = target_identity["targets"][name]
    if name == "odd-ctl":
        target = np.zeros(len(solutions), dtype=np.uint8)
        least_row = min(packed_rows)
        target[packed_rows.index(least_row)] = 1
        target_ok = target_ok and hashlib.sha256(least_row).hexdigest() == target_identity.get(
            "odd_control_row_sha256"
        )
    else:
        support = metadata.get("witness_support")
        target_ok = target_ok and isinstance(support, list)
        target = (incidence[:, support].sum(axis=1) & 1).astype(np.uint8)
    canonical_hash = hashlib.sha256(b"".join(sorted(
        row + bytes((int(bit),)) for row, bit in zip(packed_rows, target)
    ))).hexdigest()
    target_ok = target_ok and int(target.sum()) == metadata.get("ones")
    target_ok = target_ok and canonical_hash == metadata.get(
        "canonical_rows_with_bit_sha256"
    )
    targets[name] = target
row_bits = [sum(int(bit) << column for column, bit in enumerate(row)) for row in incidence]
basis, basis_rows = gf2_basis_indices(row_bits)
realizable = {}
for name, target in targets.items():
    augmented = [
        row | (int(bit) << 192) for row, bit in zip(row_bits, target)
    ]
    augmented_rank = len(gf2_basis_indices(augmented)[0])
    realizable[name] = augmented_rank == len(basis)
    target_ok = target_ok and realizable[name] == bool(
        target_identity["targets"][name].get("realizable")
    )
gate(target_ok and len(basis) == 88 and all(realizable[name] for name in ordered_names[:-1])
     and not realizable["odd-ctl"], "independent.targets",
     "all 18 canonical targets reconstruct; exactly the canonical odd control is inconsistent")

# Independently rebuild the 48 geometry permutations, then semantically validate b0/b1.
base_permutations = []
for action in geometric_actions:
    permutation = []
    for piece in used:
        image = tuple(sorted(action[corner] for corner in PIECES[piece]))
        permutation.append(position[piece_index[image]])
    base_permutations.append(np.array(permutation, dtype=np.int64))
seeded = primary_receipt["transitive_group"]["seeded_support_permutations"]
generators = base_permutations + [
    np.array(seeded["b0"], dtype=np.int64),
    np.array(seeded["b1"], dtype=np.int64),
]
row_lookup = {
    tuple(int(column) for column in np.flatnonzero(row)): index
    for index, row in enumerate(incidence)
}
generator_ok = True
for permutation in generators:
    generator_ok = generator_ok and sorted(permutation.tolist()) == list(range(192))
    image_rows = []
    for row in incidence:
        image_support = tuple(sorted(int(permutation[column]) for column in np.flatnonzero(row)))
        image_rows.append(row_lookup.get(image_support, -1))
    generator_ok = generator_ok and -1 not in image_rows
    if -1 not in image_rows:
        image_rows = np.array(image_rows, dtype=np.int64)
        generator_ok = generator_ok and all(
            np.array_equal(targets[name][image_rows], targets[name])
            for name in ordered_names[2:8]
        )
identity_permutation = np.arange(192, dtype=np.int64)
group = {identity_permutation.tobytes(): identity_permutation}
frontier = [identity_permutation]
while frontier:
    following = []
    for permutation in frontier:
        for generator in generators:
            product = generator[permutation]
            key = product.tobytes()
            if key not in group:
                group[key] = product
                following.append(product)
    frontier = following
group_hash = hashlib.sha256(b"".join(sorted(group))).hexdigest()
anchor = primary_receipt["transitive_group"]["anchor_column"]
gate(generator_ok and len(base_permutations) == 48 and len(group) == 384
     and len({int(permutation[anchor]) for permutation in group.values()}) == 192
     and group_hash == primary_receipt["transitive_group"]["generated_group_sha256"],
     "independent.group",
     "independent geometry plus verified seeded maps close to the same transitive order-384 action")


def append_xor(cnf, literals, right_hand_side, top_id):
    if not literals:
        if right_hand_side:
            cnf.append([])
        return top_id
    accumulator = literals[0]
    for literal in literals[1:]:
        top_id += 1
        auxiliary = top_id
        cnf.extend([
            [-accumulator, -literal, -auxiliary],
            [accumulator, literal, -auxiliary],
            [accumulator, -literal, auxiliary],
            [-accumulator, literal, auxiliary],
        ])
        accumulator = auxiliary
    cnf.append([accumulator if right_hand_side else -accumulator])
    return top_id


def anchored_additional_solution(target, anchor_column, known_supports=()):
    """Return one anchored solution outside a supplied exact list, or None."""
    cnf = CNF()
    top_id = 192
    for row in basis_rows:
        literals = [column + 1 for column in np.flatnonzero(incidence[row])]
        top_id = append_xor(cnf, literals, int(target[row]), top_id)
    cardinality = CardEnc.equals(
        lits=list(range(1, 193)), bound=16, top_id=top_id, encoding=EncType.totalizer
    )
    cnf.extend(cardinality.clauses)
    cnf.append([anchor_column + 1])
    for support in known_supports:
        cnf.append([-(column + 1) for column in support])
    with Cadical195(bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None
        model = solver.get_model()
        support = tuple(column for column in range(192) if model[column] > 0)
        if len(support) != 16:
            raise AssertionError("cardinality encoding returned a non-sixteen support")
        return support


search_names = ordered_names[2:8]
search_start = time.time()
primary_anchored = sorted(
    tuple(support) for support in primary_receipt["four_reading_census"]["anchored_supports"]
)
known_anchors_ok = (
    len(primary_anchored) == 11
    and len(set(primary_anchored)) == 11
    and all(anchor in support and len(support) == 16 for support in primary_anchored)
    and all(np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), targets["four"]
    ) for support in primary_anchored)
)
additional_solutions = {
    name: anchored_additional_solution(
        targets[name], anchor, primary_anchored if name == "four" else ()
    )
    for name in search_names
}
anchored_counts = {
    name: (len(primary_anchored) if name == "four" else 0)
    + int(additional_solutions[name] is not None)
    for name in search_names
}
gate(known_anchors_ok and all(solution is None for solution in additional_solutions.values())
     and anchored_counts == dict(zip(search_names, [11, 0, 0, 0, 0, 0])),
     "independent.sat",
     "orthogonal CNF excludes every extra four carrier and any carrier for the other five")
gate(all(anchored_counts[name] == 0 for name in ordered_names[3:8]),
     "independent.empty", "the five named nonconstant anchored slices are exactly empty")

complete_census = sorted(
    tuple(support) for support in primary_receipt["four_reading_census"]["complete_supports"]
)
generated_census = {
    tuple(sorted(int(permutation[column]) for column in support))
    for permutation in group.values() for support in primary_anchored
}
census_ok = (
    len(complete_census) == len(set(complete_census)) == len(generated_census) == 132
    and set(complete_census) == generated_census
    and all(np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), targets["four"]
    ) for support in complete_census)
)


def orbit_distribution(permutations, supports):
    support_set = set(supports)
    unseen = set(supports)
    distribution = {}
    while unseen:
        seed = next(iter(unseen))
        orbit = {
            tuple(sorted(int(permutation[column]) for column in seed))
            for permutation in permutations
        }
        if not orbit <= support_set:
            return None
        unseen -= orbit
        distribution[len(orbit)] = distribution.get(len(orbit), 0) + 1
    return distribution


base_distribution = orbit_distribution(base_permutations, complete_census)
full_distribution = orbit_distribution(list(group.values()), complete_census)
gate(census_ok and base_distribution == {6: 10, 12: 4, 24: 1}
     and full_distribution == {12: 3, 24: 2, 48: 1},
     "independent.census",
     "all 132 witnesses recheck and independently fold 15 ways under 48 and 6 under 384")

planted_names = ordered_names[12:17]
planted_ok = all(
    len(target_identity["targets"][name]["witness_support"]) == 16
    and anchor in target_identity["targets"][name]["witness_support"]
    and np.array_equal(
        (incidence[:, target_identity["targets"][name]["witness_support"]].sum(axis=1) & 1)
        .astype(np.uint8), targets[name]
    )
    for name in planted_names
)
gate(planted_ok, "independent.controls",
     "all five seeded size-16 controls independently reconstruct and hold the anchor")

# Hostile controls: each load-bearing contract must fail closed under local mutation.
bad_receipt = copy.deepcopy(primary_receipt)
bad_receipt["complete_anchored_search_at_sixteen"]["executed_splits"] -= 1
gate(not primary_contract_ok(bad_receipt), "hostile.skipped_split",
     "a skipped primary split invalidates the content-bound receipt")
bad_receipt = copy.deepcopy(primary_receipt)
bad_receipt["runner_sha256"] = "0" * 64
gate(not primary_contract_ok(bad_receipt), "hostile.primary_source",
     "a primary source mutation invalidates its runner hash")
bad_generator = generators[-1].copy()
bad_generator[0] = bad_generator[1]
gate(sorted(bad_generator.tolist()) != list(range(192)), "hostile.group",
     "a non-permutation mutation of a seeded map is rejected")
bad_target = copy.deepcopy(target_identity)
bad_target["targets"]["four"]["witness_support"][0] ^= 1
bad_support = bad_target["targets"]["four"]["witness_support"]
bad_function = (incidence[:, bad_support].sum(axis=1) & 1).astype(np.uint8)
gate(not np.array_equal(bad_function, targets["four"]), "hostile.target",
     "a local target-support mutation changes the exact reading and is rejected")

N5 = [
    "per_element: checked -- all 192 columns enter each exact anchored CNF",
    "per_site: checked -- one supplied 16-corner coordinate cell only",
    "per_mode: checked and not executed -- this finite system has no modes",
    "per_block: checked -- all 15800 rows reduce through an independent rank-88 basis",
    "lattice_wide: checked and not executed -- no multicell or limiting claim",
]
for line in N5:
    print("N5 " + line, flush=True)

receipt = {
    "schema": "physical-cell-cutting-sixteen-census-cycle745-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "primary_receipt_bound": primary_contract_ok(primary_receipt),
    "population": {"cuttings": len(solutions), "used_pieces": len(used), "rank": len(basis)},
    "target_identity_bound": target_ok,
    "verified_group": {
        "order": len(group),
        "anchor_orbit_size": len({int(permutation[anchor]) for permutation in group.values()}),
        "generated_group_sha256": group_hash,
    },
    "exact_anchored_weight_sixteen_counts": anchored_counts,
    "exact_anchored_weight_sixteen_answers": {
        name: count > 0 for name, count in anchored_counts.items()
    },
    "exact_sat": {
        "anchor_column": anchor,
        "basis_rows": len(basis_rows),
        "elapsed_seconds": round(time.time() - search_start, 2),
        "peak_memory_mb": round(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0, 2
        ),
    },
    "n5_execution_certificate": N5,
    "gates": {
        "pass": passed,
        "fail": failed,
        "named": {name: "PASS" if ok else "FAIL" for name, ok in gates},
    },
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
raise SystemExit(1 if failed else 0)
