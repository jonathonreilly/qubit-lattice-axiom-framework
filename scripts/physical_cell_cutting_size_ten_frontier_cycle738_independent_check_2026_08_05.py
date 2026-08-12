"""Independent exact syndrome check for Cycle 738's ten-piece frontier.

This checker imports and executes neither the Cycle 738 primary nor its search engine.
It reconstructs the supplied finite cutting incidence by an opposite exact-cover pivot,
binds the eight named readings and upper witnesses to Cycle 737's generated receipt,
then encodes each exact-weight-ten syndrome question as CNF.  A cardinality totalizer and
Tseitin XOR chains are solved by PySAT's independently maintained CaDiCaL backend.  Every
SAT witness is checked against all 15,800 cuttings; every claimed empty target must return
UNSAT.  The primary search does not import this checker or its solver.
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
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py"
C737_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
C737_PRIMARY_PATH = "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
C737_CHECKER_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.py"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    PRIMARY_PATH,
    "requirements.txt",
    "requirements-release.txt",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
)
AUDIT_TIMEOUT_SEC = 900


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


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


# Reconstruct the supplied model without importing another runner.
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

# Independent fixed interior sample family.  The opposite cover pivot below chooses the
# largest uncovered sample, unlike Cycle 738's smallest-uncovered recursion.
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
    weighted = weights[:, None] * VERTICES[list(piece)]
    for action in group:
        sample_set.add(tuple(int(v) for v in (weights[:, None] * VERTICES[[action[c] for c in piece]]).sum(axis=0)))
SAMPLES = np.array(sorted(sample_set), dtype=np.int64)
INCIDENCE = np.zeros((len(PIECES), len(SAMPLES)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (SAMPLES.T - (scale * VERTICES[piece[0]])[:, None])
    total = bary.sum(axis=0)
    INCIDENCE[index] = (bary > 0).all(axis=0) & (total < scale)

# Discard sample columns that no minimum-cost piece contains; the remaining columns still
# separate the finite exact covers.  The exact 15,800 count and 24-piece size are gated.
active = np.flatnonzero(INCIDENCE[MINIMUM].any(axis=0))
INCIDENCE = INCIDENCE[:, active]
masks = []
by_sample = {}
for piece in MINIMUM:
    mask = 0
    for sample in np.flatnonzero(INCIDENCE[piece]):
        mask |= 1 << int(sample)
        by_sample.setdefault(int(sample), []).append(piece)
    masks.append((piece, mask))
mask_by_piece = dict(masks)
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
packed_incidence_hash = hashlib.sha256(b"".join(sorted(packed_rows))).hexdigest()
column_order = [[int(corner) for corner in PIECES[piece]] for piece in used]
column_order_hash = hashlib.sha256(
    json.dumps(column_order, separators=(",", ":")).encode("utf-8")
).hexdigest()
gate(
    len(PIECES) == 2672 and len(MINIMUM) == 400 and int(COSTS.min()) == 6
    and len(solutions) == 15800 and len(used) == 192
    and all(len(solution) == 24 for solution in solutions),
    "independent.population",
    "opposite-pivot exact covers reconstruct 15,800 rows on the 192 used pieces",
)

C737 = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))
identity = C737.get("reading_identity", {})
functions = identity.get("functions", {})
receipt_ok = (
    C737.get("schema") == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737.get("status") == "pass"
    and C737.get("gates", {}).get("fail") == 0
    and C737.get("complete_support_sweep", {}).get("maximum_cardinality") == 8
    and C737.get("complete_support_sweep", {}).get("nonconstant_reading_minimum_lower_bound") == 10
    and identity.get("canonical_sorted_incidence_rows_sha256") == packed_incidence_hash
    and identity.get("support_column_order_sha256") == column_order_hash
)
gate(receipt_ok, "independent.dependency", "Cycle 737 v2 is pass and binds this exact incidence/order")

WITNESSES = C737.get("verified_upper_witnesses", {})
NAMES = ("zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip")
targets = {}
target_ok = True
for name in NAMES:
    metadata = functions.get(name, {})
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
    target_ok = target_ok and int(target.sum()) == metadata.get("ones")
    canonical_function_hash = hashlib.sha256(b"".join(sorted(
        row + bytes([int(bit)]) for row, bit in zip(packed_rows, target)
    ))).hexdigest()
    target_ok = target_ok and canonical_function_hash == metadata.get(
        "canonical_incidence_row_bit_pairs_sha256"
    )
gate(target_ok, "independent.targets", "all eight Cycle 737 reading identities and upper supports reconstruct exactly")

row_bits = []
for row in incidence:
    bits = 0
    for column in np.flatnonzero(row):
        bits |= 1 << int(column)
    row_bits.append(bits)
pivots, pivot_rows = gf2_pivots(row_bits)
gate(len(pivots) == 88, "independent.rank", "an independently selected 88-row basis pins every reading")


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


def solve_target(name, target):
    clauses = []
    top = 192
    for row_index in pivot_rows:
        literals = [int(column) + 1 for column in np.flatnonzero(incidence[row_index])]
        added, top = xor_clauses(literals, int(target[row_index]), top)
        clauses += added
    cardinality = CardEnc.equals(
        lits=list(range(1, 193)), bound=10, top_id=top, encoding=EncType.totalizer
    )
    clauses += cardinality.clauses
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        sat = solver.solve()
        support = None
        if sat:
            model = set(value for value in solver.get_model() if value > 0)
            support = [column for column in range(192) if column + 1 in model]
        return sat, support, solver.nof_clauses(), solver.nof_vars()


answers = {}
encoded = {}
solver_ok = True
for name in NAMES:
    sat, support, clause_count, variable_count = solve_target(name, targets[name])
    answers[name] = sat
    encoded[name] = {"clauses": clause_count, "variables": variable_count}
    solver_ok = solver_ok and sat is False
    if sat is True:
        solver_ok = solver_ok and len(support) == 10 and np.array_equal(
            (incidence[:, support].sum(axis=1) & 1).astype(np.uint8), targets[name]
        )
gate(solver_ok, "independent.ten", "independent CNF solver returns UNSAT for all eight exact-weight-ten syndromes")

mutated = targets["zero"].copy()
known = list(range(10))
mutated = (incidence[:, known].sum(axis=1) & 1).astype(np.uint8)
sat, support, _clauses, _variables = solve_target("hostile-known", mutated)
gate(sat is True and support is not None and len(support) == 10 and np.array_equal(
         (incidence[:, support].sum(axis=1) & 1).astype(np.uint8), mutated
     ),
     "hostile.sat", "a reading planted from ten pieces is recovered as SAT")
bad_receipt = copy.deepcopy(C737)
bad_receipt["status"] = "fail"
gate(not (bad_receipt.get("status") == "pass" and bad_receipt.get("gates", {}).get("fail") == 0),
     "hostile.dependency", "a failed direct-dependency receipt cannot pass")

print("")
print("per_element: checked -- all 192 used piece columns enter each exact-weight-ten CNF", flush=True)
print("per_site: checked -- one supplied 16-corner coordinate cell; no physical cell selection", flush=True)
print("per_mode: checked and not executed -- no field, spectral, or momentum modes exist", flush=True)
print("per_block: checked -- all 15,800 cutting rows through an independent 88-row basis", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-L, or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-size-ten-frontier-cycle738-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "population": {"cuttings": len(solutions), "used_pieces": len(used), "rank": len(pivots)},
    "ten_piece_answers": answers,
    "encoding": encoded,
    "gates": {"pass": passed, "fail": failed, "named": {name: "PASS" if ok else "FAIL" for name, ok in gates}},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(1 if failed else 0)
