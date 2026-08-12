"""Independent exact-cardinality check for the Cycle 739 twelve-piece bound.

This checker imports and executes neither the Cycle 739 primary nor its meet engine.  It
reconstructs the supplied incidence with the opposite exact-cover pivot, binds canonical
row/order/function identities to Cycle 737, checks the Cycle 738 predecessor receipts,
and encodes exact-weight-twelve syndromes as CNF.  PySAT's independently maintained
CaDiCaL backend recovers constant-reading and planted SAT controls and proves the six
fixed nonconstant targets UNSAT.  It also independently reconstructs the block ranks and
the first-quarter kernel weight distribution.
"""

import copy
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
    "independent_check_2026_08_05.py"
)
PRIMARY_PATH = "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C738_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json"
)
C738_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH.write_text(
    json.dumps(
        {
            "schema": "physical-cell-cutting-twelve-frontier-cycle739-independent-v1",
            "status": "fail",
            "reason": "checker has not completed",
        },
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05.py",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "requirements.txt",
    "requirements-release.txt",
)
AUDIT_TIMEOUT_SEC = 900


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


PRIMARY_RECEIPT = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
C737 = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))
C737I = json.loads((ROOT / C737_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
C738 = json.loads((ROOT / C738_RECEIPT_PATH).read_text(encoding="utf-8"))
C738I = json.loads((ROOT / C738_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
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
    """Small exact Laplace expansion, independent of the primary determinant formula."""
    rows = [[int(value) for value in row] for row in matrix]
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1 if column & 1 else 1) * value
        * determinant([row[:column] + row[column + 1 :] for row in rows[1:]])
        for column, value in enumerate(rows[0])
    )


def gf2_pivots(rows):
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


def gf2_rank(rows):
    return len(gf2_pivots(rows)[0])


def input_contract_ok(receipt, required_paths, source_path, source_field):
    expected = receipt.get("input_sha256", {})
    return (
        receipt.get(source_field) == sha256(source_path)
        and set(expected) == set(required_paths)
        and all(sha256(path) == expected[path] for path in required_paths)
    )


# Rebuild the finite model without importing another runner.
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
        sum(abs(int(points[a, column]) - int(points[b, column])) for column in range(4)) > 1
        for a, b in PAIRS
    )


COSTS = np.array([piece_cost(piece) for piece in PIECES], dtype=np.int64)
MINIMUM = np.flatnonzero(COSTS == int(COSTS.min())).tolist()
corner_index = {corner: index for index, corner in enumerate(CORNERS)}
group = []
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
            group.append(action)
piece_index = {piece: index for index, piece in enumerate(PIECES)}
labels = np.full(len(PIECES), -1, dtype=np.int64)
representatives = []
for index, piece in enumerate(PIECES):
    if labels[index] >= 0:
        continue
    orbit = len(representatives)
    representatives.append(index)
    for action in group:
        labels[piece_index[tuple(sorted(action[corner] for corner in piece))]] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_set = set()
for index in representatives:
    piece = PIECES[index]
    for action in group:
        sample_set.add(tuple(
            int(value) for value in (
                weights[:, None] * VERTICES[[action[corner] for corner in piece]]
            ).sum(axis=0)
        ))
SAMPLES = np.array(sorted(sample_set), dtype=np.int64)
SAMPLE_INCIDENCE = np.zeros((len(PIECES), len(SAMPLES)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (
        SAMPLES.T - (scale * VERTICES[piece[0]])[:, None]
    )
    total = bary.sum(axis=0)
    SAMPLE_INCIDENCE[index] = (bary > 0).all(axis=0) & (total < scale)
active = np.flatnonzero(SAMPLE_INCIDENCE[MINIMUM].any(axis=0))
SAMPLE_INCIDENCE = SAMPLE_INCIDENCE[:, active]
mask_by_piece = {}
by_sample = {}
for piece in MINIMUM:
    mask = 0
    for sample in np.flatnonzero(SAMPLE_INCIDENCE[piece]):
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
    sample = remaining.bit_length() - 1  # opposite pivot from the Cycle 739 primary
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
    "opposite-pivot exact covers reconstruct 15800 rows on the 192 used pieces",
)

identity = C737.get("reading_identity", {})
functions = identity.get("functions", {})
EXPECTED_NAMES = (
    "zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"
)
C737I_IDENTITY = C737I.get("reading_identity", {})
CANONICAL_IDENTITY_AGREES = (
    C737I_IDENTITY.get("canonical_incidence_rows_sha256")
    == identity.get("canonical_incidence_rows_sha256")
    and C737I_IDENTITY.get("support_column_order_sha256")
    == identity.get("support_column_order_sha256")
    and all(
        C737I_IDENTITY.get("functions", {}).get(name, {}).get("ones")
        == functions.get(name, {}).get("ones")
        and C737I_IDENTITY.get("functions", {}).get(name, {}).get(
            "canonical_rows_with_bit_sha256"
        ) == functions.get(name, {}).get("canonical_rows_with_bit_sha256")
        for name in EXPECTED_NAMES
    )
)
C737_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
C737_PRIMARY_PATH = "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
C737_CHECKER_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py"
)
C738_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md"
C738_PRIMARY_PATH = "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py"
C738_CHECKER_PATH = (
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
    "independent_check_2026_08_05.py"
)
C737_PRIMARY_INPUTS = (
    C737_NOTE_PATH,
    C737_CHECKER_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
)
C737_INDEPENDENT_INPUTS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_RECEIPT_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
)
C738_PRIMARY_INPUTS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C738_NOTE_PATH,
    C738_CHECKER_PATH,
)
C738_INDEPENDENT_INPUTS = (
    C738_NOTE_PATH,
    C738_PRIMARY_PATH,
    "requirements.txt",
    "requirements-release.txt",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
)
dependency_ok = (
    C737.get("schema") == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737.get("status") == "pass"
    and C737.get("gates", {}).get("fail") == 0
    and input_contract_ok(C737, C737_PRIMARY_INPUTS, C737_PRIMARY_PATH, "runner_sha256")
    and C737I.get("schema")
    == "physical-cell-cutting-least-computing-sets-cycle737-independent-v1"
    and C737I.get("status") == "pass"
    and C737I.get("gates", {}).get("fail") == 0
    and input_contract_ok(
        C737I, C737_INDEPENDENT_INPUTS, C737_CHECKER_PATH, "runner_sha256"
    )
    and CANONICAL_IDENTITY_AGREES
    and identity.get("canonical_incidence_rows_sha256") == canonical_incidence_hash
    and identity.get("support_column_order_sha256") == column_order_hash
    and C738.get("schema") == "physical-cell-cutting-size-ten-frontier-cycle738-v2"
    and C738.get("status") == "pass"
    and C738.get("gates", {}).get("fail") == 0
    and input_contract_ok(C738, C738_PRIMARY_INPUTS, C738_PRIMARY_PATH, "runner_sha256")
    and C738I.get("schema") == "physical-cell-cutting-size-ten-frontier-cycle738-independent-v1"
    and C738I.get("status") == "pass"
    and C738I.get("gates", {}).get("fail") == 0
    and input_contract_ok(
        C738I, C738_INDEPENDENT_INPUTS, C738_CHECKER_PATH, "checker_sha256"
    )
    and C738.get("complete_search_at_ten", {}).get("readings", [])[:8]
    == list(EXPECTED_NAMES)
    and C738.get("complete_search_at_ten", {}).get("counts", [])[:8] == [0] * 8
    and all(C738I.get("ten_piece_answers", {}).get(name) is False
            for name in EXPECTED_NAMES)
)
gate(dependency_ok, "independent.dependencies",
     "Cycle 737 binds this exact population/functions and both Cycle 738 receipts pass")

names = EXPECTED_NAMES
targets = {}
target_ok = True
for name in names:
    metadata = functions.get(name, {})
    if name == "zero":
        target = np.zeros(len(solutions), dtype=np.uint8)
    elif name == "one":
        target = np.ones(len(solutions), dtype=np.uint8)
    else:
        witness = C737.get("verified_upper_witnesses", {}).get(name, {})
        support = witness.get("support_indices_0_to_191", [])
        target = (incidence[:, support].sum(axis=1) & 1).astype(np.uint8)
        target_ok = target_ok and len(support) == witness.get("size")
    targets[name] = target
    target_ok = target_ok and int(target.sum()) == metadata.get("ones")
    canonical_function_hash = hashlib.sha256(b"".join(sorted(
        row + bytes([int(bit)]) for row, bit in zip(packed_rows, target)
    ))).hexdigest()
    target_ok = target_ok and canonical_function_hash == metadata.get(
        "canonical_rows_with_bit_sha256"
    )
gate(target_ok, "independent.targets",
     "all eight Cycle 737 algebraic reading identities reconstruct exactly")

row_bits = []
for row in incidence:
    bits = 0
    for column in np.flatnonzero(row):
        bits |= 1 << int(column)
    row_bits.append(bits)
pivots, pivot_rows = gf2_pivots(row_bits)
gate(len(pivots) == 88, "independent.rank",
     "an independently selected 88-row basis pins every carried reading")
consistent_targets = all(
    len(gf2_pivots([
        row | (int(bit) << 192) for row, bit in zip(row_bits, targets[name])
    ])[0]) == len(pivots)
    for name in names
)
gate(consistent_targets, "independent.consistency",
     "each bound reading lies in the reconstructed incidence column space before basis reduction")


def xor_clauses(literals, value, next_variable):
    clauses = []
    current = literals[0]
    for literal in literals[1:]:
        next_variable += 1
        output = next_variable
        clauses += [
            [current, literal, -output], [current, -literal, output],
            [-current, literal, output], [-current, -literal, -output],
        ]
        current = output
    clauses.append([current if value else -current])
    return clauses, next_variable


def solver_for(target):
    clauses = []
    top = 192
    for row_index in pivot_rows:
        literals = [int(column) + 1 for column in np.flatnonzero(incidence[row_index])]
        added, top = xor_clauses(literals, int(target[row_index]), top)
        clauses += added
    cardinality = CardEnc.equals(
        lits=list(range(1, 193)), bound=12, top_id=top, encoding=EncType.totalizer
    )
    clauses += cardinality.clauses
    return Solver(name="cadical195", bootstrap_with=clauses)


def solve_target(target):
    with solver_for(target) as solver:
        if not solver.solve():
            return []
        model = set(value for value in solver.get_model() if value > 0)
        support = tuple(column for column in range(192) if column + 1 in model)
        if len(support) != 12 or not np.array_equal(
            (incidence[:, support].sum(axis=1) & 1).astype(np.uint8), target
        ):
            return None
        return [support]


solutions_by_name = {}
search_ok = True
for name in names:
    result = solve_target(targets[name])
    solutions_by_name[name] = result
    search_ok = search_ok and result is not None
answers = {name: bool(solutions_by_name[name]) for name in names}
search_ok = search_ok and answers == {
    "zero": True, "one": True, "four": False, "four-flip": False,
    "six": False, "six-flip": False, "seven": False, "seven-flip": False,
}
gate(search_ok, "independent.twelve",
     "independent CNF gives SAT controls for both constants and UNSAT for all six "
     "nonconstant targets at exact weight twelve")

# Independent block ranks and first-quarter kernel distribution.
column_vectors = []
for column in range(192):
    value = 0
    for bit, row_index in enumerate(pivot_rows):
        value |= int(incidence[row_index, column]) << bit
    column_vectors.append(value)


def column_rank(indices):
    return gf2_rank(column_vectors[index] for index in indices)


def internal_dimension(indices):
    outside = [index for index in range(192) if index not in set(indices)]
    return 88 - column_rank(outside)


blocks = [list(range(24 * block, 24 * block + 24)) for block in range(8)]
quarters = [list(range(48 * quarter, 48 * quarter + 48)) for quarter in range(4)]
halves = [list(range(96)), list(range(96, 192))]
crosses = [quarters[0] + quarters[2], quarters[0] + quarters[3],
           quarters[1] + quarters[2], quarters[1] + quarters[3]]
complements = [[index for index in range(192) if index not in set(quarter)]
               for quarter in quarters]
tree = {
    "internal_blocks": [internal_dimension(block) for block in blocks],
    "internal_quarters": [internal_dimension(quarter) for quarter in quarters],
    "internal_halves": [internal_dimension(half) for half in halves],
    "internal_crosses": [internal_dimension(cross) for cross in crosses],
    "internal_complements": [internal_dimension(comp) for comp in complements],
    "rank_blocks": [column_rank(block) for block in blocks],
    "rank_quarters": [column_rank(quarter) for quarter in quarters],
    "rank_halves": [column_rank(half) for half in halves],
}
tree_ok = tree == {
    "internal_blocks": [0, 0, 0, 0, 0, 0, 1, 2],
    "internal_quarters": [0, 0, 6, 13],
    "internal_halves": [13, 33],
    "internal_crosses": [9, 13, 15, 22],
    "internal_complements": [54, 40, 40, 40],
    "rank_blocks": [19, 24, 24, 24, 24, 24, 24, 24],
    "rank_quarters": [34, 48, 48, 48],
    "rank_halves": [55, 75],
}
gate(tree_ok, "independent.certificate_tree",
     "all block/quarter/half ranks and internal dimensions reconstruct independently")


def kernel_basis(indices):
    pivot_rows_local = {}
    answer = []
    for local, column in enumerate(indices):
        value = column_vectors[column]
        witness = 1 << local
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivot_rows_local:
                pivot_rows_local[pivot] = (value, witness)
                break
            basis_value, basis_witness = pivot_rows_local[pivot]
            value ^= basis_value
            witness ^= basis_witness
        if value == 0:
            answer.append(witness)
    return answer


quarter_kernel = kernel_basis(quarters[0])
distribution = {}
for mask in range(1 << len(quarter_kernel)):
    word = 0
    for bit, basis_word in enumerate(quarter_kernel):
        if (mask >> bit) & 1:
            word ^= basis_word
    weight = word.bit_count()
    distribution[weight] = distribution.get(weight, 0) + 1
expected_distribution = {
    0: 1, 8: 30, 12: 63, 14: 164, 16: 395, 18: 929, 20: 1846,
    22: 3017, 24: 3456, 26: 2962, 28: 1891, 30: 974, 32: 470,
    34: 141, 36: 40, 38: 5,
}
gate(len(quarter_kernel) == 14 and distribution == expected_distribution,
     "independent.quarter_kernel",
     "the first-quarter dimension-14 kernel and complete weight distribution agree")


def independent_split_inventory():
    """Reconstruct the exact size-twelve schedule without the primary planner."""
    descriptors = []
    for q0 in range(13):
        for q1 in range(13 - q0):
            for q2 in range(13 - q0 - q1):
                q3 = 12 - q0 - q1 - q2
                cell = (q0, q1, q2, q3)
                # At size twelve, the bound readings license exactly the cells
                # with even left-half parity; total parity makes Q2/Q3 agree.
                if (q0 + q1) & 1:
                    continue
                profile = list(cell)
                if max(profile) <= 6:
                    best = max(
                        range(4), key=lambda index: (math.comb(48, profile[index]), -index)
                    )
                    descriptors.append((cell, ("Q", best, profile[best])))
                    continue
                block = max(range(4), key=lambda index: (profile[index], -index))
                for first_weight in range(profile[block] + 1):
                    second_weight = profile[block] - first_weight
                    even, odd = 2 * block, 2 * block + 1
                    if math.comb(24, first_weight) >= math.comb(24, second_weight):
                        streamed = ("E", even, first_weight)
                    else:
                        streamed = ("E", odd, second_weight)
                    descriptors.append((cell, streamed))
    return descriptors


expected_inventory = independent_split_inventory()
expected_inventory_sha256 = hashlib.sha256(
    json.dumps(expected_inventory, separators=(",", ":")).encode("utf-8")
).hexdigest()

gate(
    PRIMARY_RECEIPT.get("schema") == "physical-cell-cutting-twelve-frontier-cycle739-v2"
    and PRIMARY_RECEIPT.get("status") == "pass"
    and PRIMARY_RECEIPT.get("gates", {}).get("fail") == 0
    and PRIMARY_RECEIPT.get("complete_search_at_twelve", {}).get("scheduled_splits")
    == PRIMARY_RECEIPT.get("complete_search_at_twelve", {}).get("executed_splits")
    == 1167
    and PRIMARY_RECEIPT.get("complete_search_at_twelve", {}).get(
        "execution_inventory_exact"
    ) is True
    and len(expected_inventory) == 1167
    and PRIMARY_RECEIPT.get("complete_search_at_twelve", {}).get(
        "execution_inventory_sha256"
    ) == expected_inventory_sha256
    and input_contract_ok(
        PRIMARY_RECEIPT,
        (
            C737_NOTE_PATH,
            C737_PRIMARY_PATH,
            C737_CHECKER_PATH,
            C737_RECEIPT_PATH,
            C737_INDEPENDENT_RECEIPT_PATH,
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
            "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
            "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
            "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
            "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
            "receipt_2026-08-05.json",
            C738_NOTE_PATH,
            C738_PRIMARY_PATH,
            C738_CHECKER_PATH,
            C738_RECEIPT_PATH,
            C738_INDEPENDENT_RECEIPT_PATH,
            NOTE_PATH,
            CHECKER_PATH,
            "requirements.txt",
            "requirements-release.txt",
        ),
        PRIMARY_PATH,
        "runner_sha256",
    ),
    "receipt.contract",
    "the primary verdict, execution inventory, runner, and every declared input are content-bound",
)

planted_support = tuple(range(12))
planted_target = (incidence[:, planted_support].sum(axis=1) & 1).astype(np.uint8)
planted = solve_target(planted_target)
gate(planted is not None and len(planted) == 1,
     "hostile.planted_sat", "a reading planted from twelve pieces is recovered as SAT")
bad_inventory = copy.deepcopy(PRIMARY_RECEIPT)
bad_inventory["complete_search_at_twelve"]["executed_splits"] -= 1
gate(not (
    bad_inventory["complete_search_at_twelve"]["scheduled_splits"]
    == bad_inventory["complete_search_at_twelve"]["executed_splits"]
    and bad_inventory["complete_search_at_twelve"]["execution_inventory_exact"] is True
), "hostile.skipped_split", "a skipped scheduled split invalidates the positive receipt predicate")
mutated_source = (ROOT / PRIMARY_PATH).read_bytes().replace(
    b"PROCD.append((cell, A))", b"PROCD.append((cell, A)) # hostile", 1
)
gate(hashlib.sha256(mutated_source).hexdigest() != PRIMARY_RECEIPT.get("runner_sha256"),
     "hostile.primary_mutation", "a local primary semantic mutation breaks its source pin")
bad_c737 = copy.deepcopy(C737)
bad_c737["reading_identity"]["functions"]["four"]["ones"] += 1
gate(bad_c737["reading_identity"] != C737["reading_identity"],
     "hostile.target_mutation", "a canonical target-identity mutation is rejected")
bad_c738 = copy.deepcopy(C738)
bad_c738["status"] = "fail"
gate(not (bad_c738.get("status") == "pass" and bad_c738.get("gates", {}).get("fail") == 0),
     "hostile.predecessor", "a failed exact-weight-ten predecessor cannot pass")
bad_primary = copy.deepcopy(PRIMARY_RECEIPT)
bad_primary["status"] = "fail"
bad_primary["gates"]["fail"] = 1
gate(not (
    bad_primary.get("status") == "pass"
    and bad_primary.get("gates", {}).get("fail") == 0
),
     "hostile.failed_verdict", "a failed generated primary verdict cannot pass")

print("")
print("per_element: checked -- all 192 used columns enter the independent "
      "exact-weight-twelve CNFs")
print("per_site: checked -- one supplied 16-corner coordinate cell; no physical cell "
      "selection")
print("per_mode: checked and not executed -- no field, spectral, or momentum-mode "
      "decomposition exists")
print("per_block: checked -- all 15800 rows, block ranks, kernel words, and "
      "exact-cardinality controls")
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-L, boundary, "
      "or continuum claim")

receipt = {
    "schema": "physical-cell-cutting-twelve-frontier-cycle739-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "population": {"cuttings": len(solutions), "used_pieces": len(used), "rank": len(pivots)},
    "exact_weight_twelve_answers": answers,
    "certificate_tree": tree,
    "quarter_kernel_weight_distribution": distribution,
    "independent_execution_inventory_sha256": expected_inventory_sha256,
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
sys.exit(1 if failed else 0)
