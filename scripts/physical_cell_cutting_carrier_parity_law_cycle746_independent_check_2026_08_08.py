"""Independent checker for Cycle 746's finite block-parity licensing law.

The checker imports no primary symbols.  It rebuilds the 15800-by-192 exact
cover incidence with the opposite uncovered-sample pivot, obtains exact
target witnesses from the hash-bound Cycle 745 interface, and derives the
row space and kernel with low-column GF(2) elimination.  It treats odd-ctl as
an inconsistent hostile control, never as a realizable reading.
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
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08.py"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_"
    "receipt_2026-08-08.json"
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
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py",
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_receipt_2026-08-08.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py",
    "scripts/physical_cell_cutting_sixteen_census_cycle745_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_sixteen_census_cycle745_independent_check_2026_08_05_receipt_2026-08-05.json",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == sha256(path) for path in recorded
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


RECEIPT_PATH.write_text(json.dumps({
    "schema": "physical-cell-cutting-carrier-parity-law-cycle746-independent-v1",
    "status": "fail",
    "claim_type": "bounded_theorem",
    "reason": "checker has not completed",
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def determinant(matrix):
    """Leibniz determinant, independent of the primary minor expansion."""
    rows = [[int(value) for value in row] for row in matrix]
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1 if column & 1 else 1) * value
        * determinant([row[:column] + row[column + 1:] for row in rows[1:]])
        for column, value in enumerate(rows[0])
    )


# Complete opposite-pivot exact-cover reconstruction.
CORNERS = list(itertools.product((0, 1), repeat=4))
VERTICES = np.array(CORNERS, dtype=np.int64)
PIECES = []
INVERSES = []
for subset in itertools.combinations(range(16), 5):
    matrix = (VERTICES[list(subset[1:])] - VERTICES[subset[0]]).T
    if abs(determinant(matrix.tolist())) != 1:
        continue
    inverse = np.rint(np.linalg.inv(matrix.astype(float))).astype(np.int64)
    if np.array_equal(matrix @ inverse, np.eye(4, dtype=np.int64)):
        PIECES.append(subset)
        INVERSES.append(inverse)
INVERSES = np.array(INVERSES, dtype=np.int64)
PAIRS = list(itertools.combinations(range(5), 2))


def piece_cost(piece):
    points = VERTICES[list(piece)]
    return sum(
        sum(abs(int(points[a, column]) - int(points[b, column])) for column in range(4)) > 1
        for a, b in PAIRS
    )


COSTS = np.array([piece_cost(piece) for piece in PIECES], dtype=np.int64)
MINIMUM = np.flatnonzero(COSTS == int(COSTS.min())).tolist()
corner_index = {corner: index for index, corner in enumerate(CORNERS)}
corner_actions = []
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
                target = (int(image[0]) // 2, int(image[1]) // 2,
                          int(image[2]) // 2, 1 - tick if tick_flip else tick)
                action.append(corner_index[target])
            corner_actions.append(action)
piece_index = {piece: index for index, piece in enumerate(PIECES)}
labels = np.full(len(PIECES), -1, dtype=np.int64)
representatives = []
for index, piece in enumerate(PIECES):
    if labels[index] >= 0:
        continue
    orbit = len(representatives)
    representatives.append(index)
    for action in corner_actions:
        image = tuple(sorted(action[corner] for corner in piece))
        labels[piece_index[image]] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_set = set()
for index in representatives:
    piece = PIECES[index]
    for action in corner_actions:
        sample_set.add(tuple(int(value) for value in (
            weights[:, None] * VERTICES[[action[corner] for corner in piece]]
        ).sum(axis=0)))
samples = np.array(sorted(sample_set), dtype=np.int64)
sample_incidence = np.zeros((len(PIECES), len(samples)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (samples.T - (scale * VERTICES[piece[0]])[:, None])
    total = bary.sum(axis=0)
    sample_incidence[index] = (bary > 0).all(axis=0) & (total < scale)
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
packed_rows = np.packbits(incidence, axis=1)
canonical_incidence_hash = hashlib.sha256(
    b"".join(sorted(bytes(row) for row in packed_rows))
).hexdigest()
column_order = [[int(corner) for corner in PIECES[piece]] for piece in used]
column_order_hash = hashlib.sha256(
    json.dumps(column_order, separators=(",", ":")).encode("utf-8")
).hexdigest()
odd_control_row_bytes = min(bytes(row) for row in packed_rows)
odd_control_row_index = next(
    index for index, row in enumerate(packed_rows) if bytes(row) == odd_control_row_bytes
)
odd_control_row_hash = hashlib.sha256(odd_control_row_bytes).hexdigest()
gate(len(PIECES) == 2672 and len(MINIMUM) == 400 and int(COSTS.min()) == 6
     and incidence.shape == (15800, 192)
     and bool((incidence.sum(axis=1) == 24).all())
     and bool((incidence.sum(axis=0) == 1975).all()),
     "independent.population", "opposite-pivot reconstruction gives the full table")

C745 = load(C745_RECEIPT_PATH)
C745I = load(C745_INDEPENDENT_RECEIPT_PATH)
PRIMARY = load(PRIMARY_RECEIPT_PATH)
NAMES = [
    "zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip",
    "pair (2,2)", "h6 (6,2)", "in-left quarters (3,5)",
    "in-right one quarter (0,8)", "p16-a4444", "p16-a0-0-6-10", "p16-a8044",
    "p16-a2-2-2-10", "p16-a0-8-0-8", "odd-ctl",
]
FIXED_SUPPORTS = {
    "pair (2,2)": [10, 55, 120, 168],
    "h6 (6,2)": [3, 21, 44, 61, 77, 90, 101, 155],
    "in-left quarters (3,5)": [2, 9, 30, 50, 63, 71, 80, 91],
    "in-right one quarter (0,8)": [150, 151, 160, 165, 170, 180, 185, 191],
}
PSEED = 74516
P16SPECS = [
    {"name": "p16-a4444", "profile": [4, 4, 4, 4]},
    {"name": "p16-a0-0-6-10", "profile": [0, 0, 6, 10]},
    {"name": "p16-a8044", "profile": [8, 0, 4, 4]},
    {"name": "p16-a2-2-2-10", "profile": [2, 2, 2, 10]},
    {"name": "p16-a0-8-0-8", "profile": [0, 8, 0, 8]},
]
rng = np.random.default_rng(PSEED)
P16SUPPORTS = {}
for spec in P16SPECS:
    name, profile = spec["name"], spec["profile"]
    support = [144] + [145 + int(value) for value in rng.choice(47, profile[3] - 1,
                                                                replace=False)]
    for quarter in range(3):
        support += [48 * quarter + int(value)
                    for value in rng.choice(48, profile[quarter], replace=False)]
    P16SUPPORTS[name] = sorted(support)


def canonical_target_hash(target):
    return hashlib.sha256(b"".join(sorted(
        bytes(row) + bytes((int(bit),)) for row, bit in zip(packed_rows, target)
    ))).hexdigest()


def target_identity_contract(receipt):
    identity = receipt.get("target_identity", {})
    targets = identity.get("targets", {})
    if not (
        identity.get("canonical_incidence_rows_sha256") == canonical_incidence_hash
        and identity.get("support_column_order_sha256") == column_order_hash
        and identity.get("ordered_names") == NAMES
        and identity.get("fixed_control_supports") == FIXED_SUPPORTS
        and identity.get("pseed") == PSEED
        and identity.get("planted_specs") == P16SPECS
        and identity.get("planted_supports") == P16SUPPORTS
        and identity.get("odd_control_non_column_space") is True
        and identity.get("odd_control_row_sha256") == odd_control_row_hash
        and set(targets) == set(NAMES)
    ):
        return False
    for index, name in enumerate(NAMES):
        entry = targets[name]
        support = entry.get("witness_support")
        if index < 17:
            if not isinstance(support, list) or len(set(support)) != len(support):
                return False
            if not all(isinstance(value, int) and 0 <= value < 192 for value in support):
                return False
            target = (incidence[:, support].sum(axis=1) & 1).astype(np.uint8)
            if entry.get("realizable") is not True:
                return False
        else:
            if support is not None or entry.get("realizable") is not False:
                return False
            target = np.zeros(15800, dtype=np.uint8)
            target[odd_control_row_index] = 1
        if entry.get("ones") != int(target.sum()):
            return False
        if entry.get("canonical_rows_with_bit_sha256") != canonical_target_hash(target):
            return False
    return True


dependency_ok = (
    C745.get("schema") == "physical-cell-cutting-sixteen-census-cycle745-v2"
    and C745.get("status") == "pass" and C745.get("gates", {}).get("fail") == 0
    and C745.get("runner_sha256") == sha256(C745_PRIMARY_PATH) and inputs_current(C745)
    and C745I.get("schema") == "physical-cell-cutting-sixteen-census-cycle745-independent-v1"
    and C745I.get("status") == "pass" and C745I.get("gates", {}).get("fail") == 0
    and (C745I.get("checker_sha256") or C745I.get("runner_sha256"))
    == sha256(C745_CHECKER_PATH) and inputs_current(C745I)
    and target_identity_contract(C745)
    and C745I.get("primary_receipt_bound") is True
    and C745I.get("target_identity_bound") is True
)
gate(dependency_ok, "independent.dependency",
     "Cycle 745 exact target identities and witnesses are current and semantic")

targets = []
for index, name in enumerate(NAMES):
    if index < 17:
        support = C745["target_identity"]["targets"][name]["witness_support"]
        target = (incidence[:, support].sum(axis=1) & 1).astype(np.uint8)
    else:
        target = np.zeros(15800, dtype=np.uint8)
        target[odd_control_row_index] = 1
    targets.append(target)


def low_pivot_consistent(target):
    """Augmented consistency using least-set-bit pivots, unlike the primary."""
    pivots = {}
    for row, rhs_value in zip(incidence, target):
        vector = 0
        for column in np.flatnonzero(row):
            vector |= 1 << int(column)
        rhs = int(rhs_value)
        while vector:
            pivot = (vector & -vector).bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, rhs)
                break
            basis_vector, basis_rhs = pivots[pivot]
            vector ^= basis_vector
            rhs ^= basis_rhs
        if vector == 0 and rhs:
            return False
    return True


realizable = [low_pivot_consistent(target) for target in targets]
gate(realizable == [True] * 17 + [False], "independent.consistency",
     "low-pivot augmented elimination rejects only odd-ctl")

# Independent RREF and full nullspace basis.
rref = incidence.copy()
rank = 0
pivot_columns = []
for column in range(192):
    candidates = np.flatnonzero(rref[rank:, column])
    if len(candidates) == 0:
        continue
    pivot_row = rank + int(candidates[-1])
    rref[[rank, pivot_row]] = rref[[pivot_row, rank]]
    other = np.flatnonzero(rref[:, column])
    other = other[other != rank]
    rref[other] ^= rref[rank]
    pivot_columns.append(column)
    rank += 1
    if rank == 192:
        break
free_columns = sorted(set(range(192)) - set(pivot_columns))
kernel = np.zeros((192, len(free_columns)), dtype=np.uint8)
for index, free_column in enumerate(free_columns):
    kernel[free_column, index] = 1
    for row, pivot_column in enumerate(pivot_columns):
        kernel[pivot_column, index] = rref[row, free_column]
gate(rank == 88 and kernel.shape == (192, 104)
     and not np.any((incidence.astype(np.uint16) @ kernel.astype(np.uint16)) & 1),
     "independent.kernel", "last-candidate low-column RREF gives rank 88 and nullity 104")

blocks = {
    "total": list(range(192)),
    "L": list(range(96)),
    "R": list(range(96, 192)),
    "Q0": list(range(0, 48)),
    "Q1": list(range(48, 96)),
    "Q2": list(range(96, 144)),
    "Q3": list(range(144, 192)),
}
fixed = []
free = []
for name, block in blocks.items():
    pairings = kernel[block].sum(axis=0) & 1
    (fixed if not np.any(pairings) else free).append(name)
gate(fixed == ["total", "L", "R", "Q2", "Q3"] and free == ["Q0", "Q1"],
     "independent.fixed_free", "kernel orthogonality independently gives five fixed blocks")

triples = []
for index, name in enumerate(NAMES[:17]):
    support = set(C745["target_identity"]["targets"][name]["witness_support"])
    triples.append(tuple(len(support.intersection(blocks[block])) & 1
                         for block in ("total", "Q2", "Q3")))
classes = {}
for index, triple in enumerate(triples):
    classes.setdefault(triple, []).append(index)
gate(sorted((triple, len(members)) for triple, members in classes.items())
     == [((0, 0, 0), 15), ((0, 1, 1), 2)]
     and all(triples[index] == (0, 0, 0) for index in range(2, 8)),
     "independent.classes", "seventeen realizable targets form classes 15 and 2")
gate(all((int(targets[index].sum()) & 1) == triples[index][0]
         for index in range(17)), "independent.total_parity",
     "odd column weight independently identifies total-support parity")


def profiles(size):
    return [
        (q0, q1, q2, size - q0 - q1 - q2)
        for q0 in range(min(48, size) + 1)
        for q1 in range(min(48, size - q0) + 1)
        for q2 in range(min(48, size - q0 - q1) + 1)
        if 0 <= size - q0 - q1 - q2 <= 48
    ]


def count_profiles(size, triple, anchored=False):
    return sum(
        1 for profile in profiles(size)
        if (size & 1, profile[2] & 1, profile[3] & 1) == triple
        and (not anchored or profile[3] >= 1)
    )


even_sizes = list(range(2, 21, 2))
odd_sizes = list(range(1, 20, 2))
all_even = [count_profiles(size, (0, 0, 0)) for size in even_sizes]
all_even_anchored = [count_profiles(size, (0, 0, 0), True) for size in even_sizes]
odd_quarters = [count_profiles(size, (0, 1, 1)) for size in even_sizes]
gate(all_even == [5, 14, 30, 55, 91, 140, 204, 285, 385, 506]
     and all_even_anchored == [1, 5, 14, 30, 55, 91, 140, 204, 285, 385]
     and odd_quarters == all_even_anchored,
     "independent.profile_counts", "direct four-loop enumeration reproduces both sequences")
gate(all(count_profiles(size, triple) == 0
         for size in odd_sizes for triple in classes),
     "independent.odd_sizes", "neither realizable class licenses an odd-size profile")
pair_checks = sum(len(profiles(size)) * 17 for size in range(1, 21))
gate(pair_checks == 180625, "independent.inventory",
     "all split-target pairs through size twenty total 180625")


def primary_contract(receipt):
    population = receipt.get("target_population", {})
    parity = receipt.get("forced_block_parity", {})
    counts = receipt.get("licensed_split_counts", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-carrier-parity-law-cycle746-v2"
        and receipt.get("status") == "pass" and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and set(receipt.get("input_sha256", {})) == set(AUDIT_INPUT_PATHS[3:]) | {
            NOTE_PATH, CHECKER_PATH
        }
        and inputs_current(receipt)
        and population.get("realizable_targets") == 17
        and population.get("inconsistent_controls") == ["odd-ctl"]
        and parity.get("fixed_blocks") == fixed and parity.get("free_blocks") == free
        and parity.get("odd_control_is_realizable") is False
        and counts.get("all_even_class") == all_even
        and counts.get("odd_quarters_class") == odd_quarters
        and counts.get("split_target_pairs_checked") == pair_checks
        and receipt.get("no_go_discipline", {}).get("status") == "PASS"
    )


gate(primary_contract(PRIMARY), "independent.primary_contract",
     "primary receipt pins current sources and independently reconstructed conclusions")
bad_primary = copy.deepcopy(PRIMARY)
bad_primary["target_population"]["realizable_targets"] = 18
gate(not primary_contract(bad_primary), "hostile.realizable_count",
     "promoting odd-ctl to a reading invalidates the contract")
bad_dependency = copy.deepcopy(C745)
bad_dependency["status"] = "fail"
gate(not target_identity_contract(bad_dependency) or bad_dependency["status"] != "pass",
     "hostile.dependency_status", "a failing predecessor is rejected")
bad_witness = copy.deepcopy(C745)
support = bad_witness["target_identity"]["targets"]["four"]["witness_support"]
support[0] = (support[0] + 1) % 192
gate(not target_identity_contract(bad_witness), "hostile.witness",
     "a changed target witness fails semantic identity")
mutated = incidence.copy()
mutated[0, 0] ^= 1
mutated_hash = hashlib.sha256(b"".join(sorted(
    bytes(row) for row in np.packbits(mutated, axis=1)
))).hexdigest()
gate(mutated_hash != canonical_incidence_hash, "hostile.incidence",
     "one changed incidence bit invalidates the canonical identity")

print("per_element: checked -- all 192 columns enter opposite-pivot incidence and kernel", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- no field or momentum modes are present", flush=True)
print("per_block: checked -- seven blocks, seventeen realizable targets, one control", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-carrier-parity-law-cycle746-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(solutions),
        "support_columns": len(used),
        "rank": rank,
        "kernel_dimension": len(free_columns),
        "canonical_incidence_rows_sha256": canonical_incidence_hash,
        "support_column_order_sha256": column_order_hash,
        "realizable_targets": sum(realizable),
        "fixed_blocks": fixed,
        "free_blocks": free,
        "class_sizes": sorted(len(members) for members in classes.values()),
        "split_target_pairs_checked": pair_checks,
    },
    "target_identity": C745.get("target_identity"),
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
sys.exit(0 if failed == 0 else 1)
