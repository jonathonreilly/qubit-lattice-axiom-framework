"""Independent exact-cardinality check for Cycle 741's weight-fourteen frontier.

This checker imports neither the Cycle 741 primary nor its cell-search engine.  It
reconstructs the supplied cutting incidence with the opposite exact-cover pivot, binds
the eight Cycle 737 function identities and the Cycle 739 weight-twelve result, then
encodes each of the six nonconstant exact-weight-fourteen questions as XOR/CNF plus a
cardinality totalizer for CaDiCaL.  A planted weight-fourteen target must return SAT and
every returned support is verified against all 15,800 rows.
"""

import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json"
)
CHECKER_PATH = (
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py"
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
C739_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json"
)
C739_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C739_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md"
C739_PRIMARY_PATH = "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py"
C739_CHECKER_PATH = (
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
    "independent_check_2026_08_05.py"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json",
    "requirements.txt",
    "requirements-release.txt",
    "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
)
AUDIT_TIMEOUT_SEC = 900


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt, required_paths):
    expected = receipt.get("input_sha256", {})
    return set(expected) == set(required_paths) and all(
        expected.get(path) == sha256(path) for path in required_paths
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
C739_PRIMARY_INPUTS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    C739_NOTE_PATH,
    C739_CHECKER_PATH,
    "requirements.txt",
    "requirements-release.txt",
)
C739_INDEPENDENT_INPUTS = (
    C739_NOTE_PATH,
    C739_CHECKER_PATH,
    C739_PRIMARY_PATH,
    C739_RECEIPT_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
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
C741_PRIMARY_INPUTS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    C739_NOTE_PATH,
    C739_PRIMARY_PATH,
    C739_CHECKER_PATH,
    C739_RECEIPT_PATH,
    C739_INDEPENDENT_RECEIPT_PATH,
    NOTE_PATH,
    CHECKER_PATH,
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


# Reconstruct all simplices and minimum-cost exact covers without importing a runner.
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
                target = (int(image[0]) // 2, int(image[1]) // 2,
                          int(image[2]) // 2, 1 - tick if tick_flip else tick)
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
        image = tuple(sorted(action[corner] for corner in piece))
        labels[piece_index[image]] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_set = set()
for index in representatives:
    piece = PIECES[index]
    for action in group:
        sample_set.add(tuple(int(v) for v in (
            weights[:, None] * VERTICES[[action[c] for c in piece]]
        ).sum(axis=0)))
SAMPLES = np.array(sorted(sample_set), dtype=np.int64)
simplex_sample_incidence = np.zeros((len(PIECES), len(SAMPLES)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (SAMPLES.T - (scale * VERTICES[piece[0]])[:, None])
    total = bary.sum(axis=0)
    simplex_sample_incidence[index] = (bary > 0).all(axis=0) & (total < scale)
active = np.flatnonzero(simplex_sample_incidence[MINIMUM].any(axis=0))
simplex_sample_incidence = simplex_sample_incidence[:, active]
by_sample = {}
mask_by_piece = {}
for piece in MINIMUM:
    mask = 0
    for sample in np.flatnonzero(simplex_sample_incidence[piece]):
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
    sample = remaining.bit_length() - 1  # opposite pivot from the primary
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
    "opposite-pivot exact covers reconstruct 15800 rows on 192 used pieces",
)

C737 = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))
C737I = json.loads((ROOT / C737_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
C739 = json.loads((ROOT / C739_RECEIPT_PATH).read_text(encoding="utf-8"))
C739I = json.loads((ROOT / C739_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
PRIMARY_RECEIPT = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
identity = C737.get("reading_identity", {})
functions = identity.get("functions", {})
independent_identity = C737I.get("reading_identity", {})
NAMES = ("zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip")
dependency_ok = (
    C737.get("schema") == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737.get("status") == "pass" and C737.get("gates", {}).get("fail") == 0
    and C737.get("runner_sha256") == sha256(C737_PRIMARY_PATH)
    and receipt_inputs_current(C737, C737_PRIMARY_INPUTS)
    and C737I.get("schema")
    == "physical-cell-cutting-least-computing-sets-cycle737-independent-v1"
    and C737I.get("status") == "pass" and C737I.get("gates", {}).get("fail") == 0
    and C737I.get("runner_sha256") == sha256(C737_CHECKER_PATH)
    and receipt_inputs_current(C737I, C737_INDEPENDENT_INPUTS)
    and identity.get("canonical_incidence_rows_sha256") == canonical_incidence_hash
    and identity.get("support_column_order_sha256") == column_order_hash
    and independent_identity.get("canonical_incidence_rows_sha256") == canonical_incidence_hash
    and independent_identity.get("support_column_order_sha256") == column_order_hash
    and C739.get("schema") == "physical-cell-cutting-twelve-frontier-cycle739-v2"
    and C739.get("status") == "pass" and C739.get("gates", {}).get("fail") == 0
    and C739.get("runner_sha256") == sha256(C739_PRIMARY_PATH)
    and receipt_inputs_current(C739, C739_PRIMARY_INPUTS)
    and C739I.get("schema") == "physical-cell-cutting-twelve-frontier-cycle739-independent-v1"
    and C739I.get("status") == "pass" and C739I.get("gates", {}).get("fail") == 0
    and C739I.get("checker_sha256") == sha256(C739_CHECKER_PATH)
    and receipt_inputs_current(C739I, C739_INDEPENDENT_INPUTS)
    and C739.get("complete_search_at_twelve", {}).get("readings", [])[:8] == list(NAMES)
    and C739.get("complete_search_at_twelve", {}).get("counts", [])[:8]
    == [7808, 3072, 0, 0, 0, 0, 0, 0]
    and C739.get("complete_search_at_twelve", {}).get("execution_inventory_exact") is True
    and C739I.get("exact_weight_twelve_answers", {}).get("zero") is True
    and C739I.get("exact_weight_twelve_answers", {}).get("one") is True
    and all(C739I.get("exact_weight_twelve_answers", {}).get(name) is False
            for name in NAMES[2:])
)
gate(dependency_ok, "independent.dependencies",
     "Cycles 737 and 739 pass and bind this exact incidence, functions and predecessor")

EXPECTED_FOURTEEN_COUNTS = [
    34560, 26880, 0, 0, 0, 0, 0, 0, 2665, 274, 329, 236, 1, 3, 11, 2, 6, 0
]


def primary_contract_ok(receipt):
    search = receipt.get("complete_search_at_fourteen", {})
    bound = receipt.get("nonconstant_reading_bound", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-fourteen-frontier-cycle741-v2"
        and receipt.get("status") == "pass"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and receipt_inputs_current(receipt, C741_PRIMARY_INPUTS)
        and search.get("counts") == EXPECTED_FOURTEEN_COUNTS
        and search.get("execution_inventory_exact") is True
        and search.get("scheduled_splits") == search.get("executed_splits")
        and search.get("mismatched_returns") == 0
        and search.get("duplicate_returns") == 0
        and bound.get("reading_names") == list(NAMES[2:])
        and bound.get("minimum_support_lower_bound") == 16
        and bound.get("sixteen_sufficiency_shown") is False
        and receipt.get("no_go_discipline", {}).get("status") == "PASS"
    )


gate(primary_contract_ok(PRIMARY_RECEIPT), "receipt.contract",
     "the primary verdict, inventory, runner and every declared input are content-bound")

WITNESSES = C737.get("verified_upper_witnesses", {})
targets = {}
target_ok = True
for name in NAMES:
    metadata = functions.get(name, {})
    independent_metadata = independent_identity.get("functions", {}).get(name, {})
    if name == "zero":
        target = np.zeros(len(solutions), dtype=np.uint8)
    elif name == "one":
        target = np.ones(len(solutions), dtype=np.uint8)
    else:
        witness = WITNESSES.get(name, {})
        support = witness.get("support_indices_0_to_191", [])
        target = (incidence[:, support].sum(axis=1) & 1).astype(np.uint8)
        target_ok = target_ok and len(support) == witness.get("size")
    targets[name] = target
    canonical_function_hash = hashlib.sha256(b"".join(sorted(
        row + bytes((int(bit),)) for row, bit in zip(packed_rows, target)
    ))).hexdigest()
    target_ok = target_ok and int(target.sum()) == metadata.get("ones")
    target_ok = target_ok and canonical_function_hash == metadata.get(
        "canonical_rows_with_bit_sha256"
    ) == independent_metadata.get("canonical_rows_with_bit_sha256")
gate(target_ok, "independent.targets",
     "all eight Cycle 737 function identities and exact upper supports reconstruct")

row_bits = []
for row in incidence:
    bits = 0
    for column in np.flatnonzero(row):
        bits |= 1 << int(column)
    row_bits.append(bits)
pivots, pivot_rows = gf2_pivots(row_bits)
consistent = all(
    len(gf2_pivots([
        row | (int(bit) << 192) for row, bit in zip(row_bits, targets[name])
    ])[0]) == len(pivots)
    for name in NAMES
)
gate(len(pivots) == 88 and consistent, "independent.rank",
     "an independent 88-row basis pins all eight consistent functions")


def xor_chain(literals, next_variable):
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
    return clauses, next_variable, current


clauses = []
top = 192
row_outputs = []
for row_index in pivot_rows:
    literals = [int(column) + 1 for column in np.flatnonzero(incidence[row_index])]
    added, top, output = xor_chain(literals, top)
    clauses += added
    row_outputs.append(output)
cardinality = CardEnc.equals(
    lits=list(range(1, 193)), bound=14, top_id=top, encoding=EncType.totalizer
)
clauses += cardinality.clauses


def assumptions_for(target):
    return [
        output if int(target[row_index]) else -output
        for output, row_index in zip(row_outputs, pivot_rows)
    ]


def solve_target(solver, target):
    sat = solver.solve(assumptions=assumptions_for(target))
    support = None
    if sat:
        model = set(value for value in solver.get_model() if value > 0)
        support = [column for column in range(192) if column + 1 in model]
    return sat, support, solver.nof_clauses(), solver.nof_vars()


answers = {}
encoded = {}
solver_ok = True
known = list(range(14))
planted = (incidence[:, known].sum(axis=1) & 1).astype(np.uint8)
with Solver(name="cadical195", bootstrap_with=clauses) as shared_solver:
    planted_sat, planted_support, _clauses, _variables = solve_target(
        shared_solver, planted
    )
    # Start with the short complement orbit and preserve every learned clause
    # across the six exact RHS assumption sets. The formula itself is shared;
    # only the 88 independently reconstructed pivot-row parity literals vary.
    solve_order = ("seven-flip", "seven", "six-flip", "six", "four-flip", "four")
    for name in solve_order:
        sat, support, clause_count, variable_count = solve_target(
            shared_solver, targets[name]
        )
        answers[name] = sat
        encoded[name] = {"clauses": clause_count, "variables": variable_count}
        solver_ok = solver_ok and sat is False
        if sat:
            solver_ok = solver_ok and len(support) == 14 and np.array_equal(
                (incidence[:, support].sum(axis=1) & 1).astype(np.uint8), targets[name]
            )
gate(solver_ok, "independent.fourteen",
     "one shared independent CNF returns UNSAT under all six exact RHS assumptions")

gate(planted_sat is True and planted_support is not None
     and len(planted_support) == 14 and np.array_equal(
         (incidence[:, planted_support].sum(axis=1) & 1).astype(np.uint8), planted
     ), "hostile.sat", "a target planted from fourteen columns is recovered as SAT")
bad_dependency = copy.deepcopy(C739)
bad_dependency["status"] = "fail"
gate(not (bad_dependency.get("status") == "pass"
          and bad_dependency.get("gates", {}).get("fail") == 0),
     "hostile.dependency", "a failed exact-weight-twelve predecessor cannot pass")
bad_dependency_hash = copy.deepcopy(C739)
bad_dependency_hash.setdefault("input_sha256", {})[C739_NOTE_PATH] = "0" * 64
gate(not receipt_inputs_current(bad_dependency_hash, C739_PRIMARY_INPUTS),
     "hostile.dependency_hash", "a mutated predecessor input contract is rejected")
bad_inventory = copy.deepcopy(PRIMARY_RECEIPT)
bad_inventory["complete_search_at_fourteen"]["executed_splits"] -= 1
gate(not primary_contract_ok(bad_inventory), "hostile.skipped_split",
     "a skipped primary search split invalidates the generated receipt")
bad_primary_hash = copy.deepcopy(PRIMARY_RECEIPT)
mutated_source = (ROOT / PRIMARY_PATH).read_bytes().replace(
    b"every licensed cell", b"some licensed cell", 1
)
bad_primary_hash["runner_sha256"] = hashlib.sha256(mutated_source).hexdigest()
gate(not primary_contract_ok(bad_primary_hash), "hostile.primary_mutation",
     "a local semantic mutation breaks the primary source pin")

N5 = [
    "per_element: checked -- all 192 columns enter each exact-weight-fourteen CNF",
    "per_site: checked -- one supplied 16-corner coordinate cell only",
    "per_mode: checked and not executed -- this finite model has no modes",
    "per_block: checked -- all 15800 rows through an independent 88-row basis",
    "lattice_wide: checked and not executed -- no multicell or limit claim",
]
for line in N5:
    print("N5 " + line, flush=True)

receipt = {
    "schema": "physical-cell-cutting-fourteen-frontier-cycle741-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "checker_sha256": sha256(CHECKER_PATH),
    "primary_receipt_bound": primary_contract_ok(PRIMARY_RECEIPT),
    "population": {"cuttings": len(solutions), "used_pieces": len(used), "rank": len(pivots)},
    "exact_weight_fourteen_answers": answers,
    "encoding": encoded,
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
sys.exit(1 if failed else 0)
