"""Independent certificate and exact-cardinality check for Cycle 742.

This checker imports neither the Cycle 742 primary nor its construction. It rebuilds the
15,800 by 192 incidence with the opposite exact-cover pivot, validates the Cycle 741
lower-bound contract, reconstructs all eight functions from Cycle 737 identities, and
independently verifies the submitted automorphism and carrier certificates. A separate
CaDiCaL exact-weight-sixteen solve recovers the positive four-reading witness.
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
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json"
)
CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py"
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
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
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
PRIMARY_REQUIRED_INPUTS = tuple(
    path for path in AUDIT_INPUT_PATHS
    if path not in (PRIMARY_PATH, PRIMARY_RECEIPT_PATH)
) + (CHECKER_PATH,)


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
    C741_NOTE_PATH,
    C741_CHECKER_PATH,
)
C741_INDEPENDENT_INPUTS = (
    C741_NOTE_PATH,
    C741_PRIMARY_PATH,
    C741_RECEIPT_PATH,
    "requirements.txt",
    "requirements-release.txt",
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
    "schema": "physical-cell-cutting-sixteen-attained-cycle742-independent-v1",
    "status": "fail",
    "claim_type": "bounded_theorem",
    "reason": "checker has not completed",
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
C741 = json.loads((ROOT / C741_RECEIPT_PATH).read_text(encoding="utf-8"))
C741I = json.loads((ROOT / C741_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
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
    and C741.get("schema") == "physical-cell-cutting-fourteen-frontier-cycle741-v2"
    and C741.get("status") == "pass" and C741.get("gates", {}).get("fail") == 0
    and C741.get("runner_sha256") == sha256(C741_PRIMARY_PATH)
    and receipt_inputs_current(C741, C741_PRIMARY_INPUTS)
    and C741.get("nonconstant_reading_bound", {}).get("reading_names")
    == list(NAMES[2:])
    and C741.get("nonconstant_reading_bound", {}).get("complete_even_sizes")
    == [2, 4, 6, 8, 10, 12, 14]
    and C741.get("nonconstant_reading_bound", {}).get("minimum_support_lower_bound") == 16
    and C741.get("nonconstant_reading_bound", {}).get("sixteen_sufficiency_shown") is False
    and C741I.get("schema")
    == "physical-cell-cutting-fourteen-frontier-cycle741-independent-v1"
    and C741I.get("status") == "pass" and C741I.get("gates", {}).get("fail") == 0
    and C741I.get("checker_sha256") == sha256(C741_CHECKER_PATH)
    and receipt_inputs_current(C741I, C741_INDEPENDENT_INPUTS)
    and C741I.get("exact_weight_fourteen_answers")
    == {name: False for name in NAMES[2:]}
)
gate(dependency_ok, "independent.dependencies",
     "Cycles 737, 739 and 741 bind the exact incidence, functions and lower bound")

def primary_contract_ok(receipt):
    four = receipt.get("four_weight_sixteen", {})
    population = receipt.get("population", {})
    incidence_identity = receipt.get("incidence_identity", {})
    reading_identity = receipt.get("reading_identity", {})
    primary_functions = reading_identity.get("functions", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-sixteen-attained-cycle742-v2"
        and receipt.get("status") == "pass"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and receipt_inputs_current(receipt, PRIMARY_REQUIRED_INPUTS)
        and population.get("cuttings") == 15800
        and population.get("pieces") == 192
        and population.get("processed_rows") == 15800
        and population.get("four_move_pairs") == 46128
        and population.get("six_move_pairs") == 31968
        and incidence_identity.get("canonical_incidence_rows_sha256")
        == canonical_incidence_hash
        and incidence_identity.get("support_column_order_sha256") == column_order_hash
        and reading_identity.get("canonical_incidence_rows_sha256")
        == canonical_incidence_hash
        and reading_identity.get("support_column_order_sha256") == column_order_hash
        and set(primary_functions) == set(NAMES)
        and all(
            primary_functions.get(name, {}).get("ones")
            == functions.get(name, {}).get("ones")
            and primary_functions.get(name, {}).get("canonical_rows_with_bit_sha256")
            == functions.get(name, {}).get("canonical_rows_with_bit_sha256")
            for name in NAMES
        )
        and four.get("enumerated_seed_count") == 36
        and four.get("closure_count") == 120
        and four.get("minimum_support") == 16
        and receipt.get("no_go_discipline", {}).get("status") == "PASS"
    )


gate(primary_contract_ok(PRIMARY_RECEIPT), "receipt.contract",
     "the Cycle 742 verdict, complete traversal, runner and inputs are content-bound")

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

# Reconstruct the original 48 support permutations and its first-appearance orbits.
column_permutations = []
for action in group:
    permutation = []
    for piece in used:
        image_piece = tuple(sorted(action[corner] for corner in PIECES[piece]))
        image_global = piece_index[image_piece]
        permutation.append(position[image_global])
    column_permutations.append(np.asarray(permutation, dtype=np.int64))
parent = list(range(192))


def find(value):
    while parent[value] != value:
        parent[value] = parent[parent[value]]
        value = parent[value]
    return value


for permutation in column_permutations:
    for column in range(192):
        left, right = find(column), find(int(permutation[column]))
        if left != right:
            parent[left] = right
orbit_labels = np.full(192, -1, dtype=np.int64)
next_label = 0
for column in range(192):
    if orbit_labels[column] < 0:
        root = find(column)
        orbit_labels[[find(candidate) == root for candidate in range(192)]] = next_label
        next_label += 1
orbits = [np.flatnonzero(orbit_labels == label).tolist() for label in range(4)]


def restricted_rank(columns, target=None):
    rows = []
    for row_index in range(len(solutions)):
        value = 0
        for local, column in enumerate(columns):
            value |= int(incidence[row_index, column]) << local
        if target is not None:
            value |= int(target[row_index]) << len(columns)
        rows.append(value)
    return len(gf2_pivots(rows)[0])


single_ranks = [restricted_rank(columns) for columns in orbits]
single_augmented = [restricted_rank(columns, targets["four"]) for columns in orbits]
pair_indices = [(0, 1), (1, 2), (0, 3), (1, 3), (0, 2), (2, 3)]
pair_columns = [orbits[left] + orbits[right] for left, right in pair_indices]
pair_ranks = [restricted_rank(columns) for columns in pair_columns]
pair_consistent = []
for columns, rank in zip(pair_columns, pair_ranks):
    pair_consistent.append([
        name for name in NAMES if restricted_rank(columns, targets[name]) == rank
    ])
restriction_ok = (
    [len(orbit) for orbit in orbits] == [48, 48, 48, 48]
    and single_ranks == [48, 48, 41, 41]
    and single_augmented == [49, 49, 42, 42]
    and pair_ranks == [81, 80, 80, 69, 69, 59]
    and pair_consistent[0] == ["zero", "four", "six", "seven-flip"]
    and all(value == ["zero", "one", "four", "four-flip"]
            for value in pair_consistent[1:])
)
gate(restriction_ok, "independent.restrictions",
     "independent single-orbit and six-pair ranks reproduce every finite inconsistency")


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


def solve_target(target, weight):
    clauses = []
    top = 192
    for row_index in pivot_rows:
        literals = [int(column) + 1 for column in np.flatnonzero(incidence[row_index])]
        added, top = xor_clauses(literals, int(target[row_index]), top)
        clauses += added
    cardinality = CardEnc.equals(
        lits=list(range(1, 193)), bound=weight, top_id=top, encoding=EncType.totalizer
    )
    clauses += cardinality.clauses
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        sat = solver.solve()
        support = None
        if sat:
            model = set(value for value in solver.get_model() if value > 0)
            support = [column for column in range(192) if column + 1 in model]
        return sat, support, solver.nof_clauses(), solver.nof_vars()


four_sat, four_support, clause_count, variable_count = solve_target(targets["four"], 16)
solver_ok = four_sat is True and four_support is not None and len(four_support) == 16 and np.array_equal(
    (incidence[:, four_support].sum(axis=1) & 1).astype(np.uint8), targets["four"]
)
gate(solver_ok, "independent.sixteen",
     "independent CNF recovers an exact weight-sixteen four-reading carrier")

known = list(range(16))
planted = (incidence[:, known].sum(axis=1) & 1).astype(np.uint8)
sat, support, _clauses, _variables = solve_target(planted, 16)
gate(sat is True and support is not None and len(support) == 16 and np.array_equal(
         (incidence[:, support].sum(axis=1) & 1).astype(np.uint8), planted
     ), "hostile.sat", "a target planted from sixteen columns is recovered as SAT")
bad_dependency = copy.deepcopy(C741)
bad_dependency["status"] = "fail"
gate(not (bad_dependency.get("status") == "pass"
          and bad_dependency.get("gates", {}).get("fail") == 0),
     "hostile.dependency", "a failed exact-weight-fourteen predecessor cannot pass")
bad_dependency_hash = copy.deepcopy(C741)
first_dep_input = next(iter(bad_dependency_hash.get("input_sha256", {})), None)
if first_dep_input:
    bad_dependency_hash["input_sha256"][first_dep_input] = "0" * 64
gate(not receipt_inputs_current(bad_dependency_hash, C741_PRIMARY_INPUTS),
     "hostile.dependency_hash", "a mutated predecessor input contract is rejected")
bad_inventory = copy.deepcopy(PRIMARY_RECEIPT)
bad_inventory["population"]["processed_rows"] -= 1
gate(not primary_contract_ok(bad_inventory), "hostile.skipped_row",
     "a skipped primary construction row invalidates the generated receipt")
bad_reading_identity = copy.deepcopy(PRIMARY_RECEIPT)
bad_reading_identity["reading_identity"]["functions"]["four"][
    "canonical_rows_with_bit_sha256"
] = "0" * 64
gate(not primary_contract_ok(bad_reading_identity), "hostile.reading_identity",
     "a local reading-name identity mutation invalidates the primary contract")
bad_primary_hash = copy.deepcopy(PRIMARY_RECEIPT)
mutated_source = (ROOT / PRIMARY_PATH).read_bytes().replace(
    b"hi = min(lo + 200, NS)", b"hi = min(lo + 100, NS)", 1
)
bad_primary_hash["runner_sha256"] = hashlib.sha256(mutated_source).hexdigest()
gate(not primary_contract_ok(bad_primary_hash), "hostile.primary_mutation",
     "a local semantic mutation breaks the primary source pin")

row_key = {bytes(np.packbits(row)): index for index, row in enumerate(incidence)}


def certificate_ok(permutation):
    if sorted(permutation) != list(range(192)):
        return False, None
    image_rows = []
    for row in incidence:
        image = np.zeros(192, dtype=np.uint8)
        image[np.asarray(permutation)[np.flatnonzero(row)]] = 1
        key = bytes(np.packbits(image))
        if key not in row_key:
            return False, None
        image_rows.append(row_key[key])
    return len(set(image_rows)) == len(solutions), np.asarray(image_rows, dtype=np.int64)


certs = PRIMARY_RECEIPT.get("automorphism_certificates", {})
cert_ok = True
cert_permutations = []
for name in ("b0", "b1"):
    certificate = certs.get(name, {})
    permutation = certificate.get("support_permutation", [])
    expected_hash = hashlib.sha256(json.dumps(
        permutation, separators=(",", ":")
    ).encode("utf-8")).hexdigest()
    ok, row_permutation = certificate_ok(permutation)
    cert_ok = cert_ok and ok and row_permutation is not None
    cert_ok = cert_ok and certificate.get("support_permutation_sha256") == expected_hash
    cert_permutations.append(np.asarray(permutation, dtype=np.int64))
    cert_ok = cert_ok and all(
        np.array_equal(targets[target_name][row_permutation], targets[target_name])
        for target_name in NAMES
    )
gate(cert_ok, "independent.automorphisms",
     "both supplied piece permutations independently induce cutting permutations and fix all readings")

all_supports = [tuple(value) for value in PRIMARY_RECEIPT.get(
    "four_weight_sixteen", {}).get("all_verified_supports", [])]
supports_ok = len(all_supports) == len(set(all_supports)) == 120 and all(
    len(value) == 16 and np.array_equal(
        (incidence[:, value].sum(axis=1) & 1).astype(np.uint8), targets["four"]
    ) for value in all_supports
)
gate(supports_ok, "independent.carriers",
     "all 120 supplied supports are distinct exact weight-sixteen four-reading carriers")

seed_supports = set(tuple(value) for value in PRIMARY_RECEIPT.get(
    "four_weight_sixteen", {}).get("enumerated_seed_supports", []))
generator_permutations = column_permutations + cert_permutations
closure = set(seed_supports)
frontier = list(seed_supports)
while frontier:
    current = frontier.pop()
    for permutation in generator_permutations:
        image = tuple(sorted(int(permutation[column]) for column in current))
        if image not in closure:
            closure.add(image)
            frontier.append(image)


def support_orbit_sizes(supports):
    remaining = set(supports)
    sizes = []
    while remaining:
        start = remaining.pop()
        orbit = {start}
        work = [start]
        while work:
            current = work.pop()
            for permutation in generator_permutations:
                image = tuple(sorted(int(permutation[column]) for column in current))
                if image not in orbit:
                    orbit.add(image)
                    work.append(image)
        remaining -= orbit
        sizes.append(len(orbit))
    return sorted(sizes)


transitive_parent = list(range(192))


def transitive_find(value):
    while transitive_parent[value] != value:
        transitive_parent[value] = transitive_parent[transitive_parent[value]]
        value = transitive_parent[value]
    return value


for permutation in generator_permutations:
    for column in range(192):
        left, right = transitive_find(column), transitive_find(int(permutation[column]))
        if left != right:
            transitive_parent[left] = right
group_ok = (
    closure == set(all_supports)
    and support_orbit_sizes(all_supports) == [12, 12, 24, 24, 48]
    and len({transitive_find(column) for column in range(192)}) == 1
)
gate(group_ok, "independent.group_closure",
     "the explicit generators act transitively and close the 36 seeds to five orbits on 120 carriers")

bad_certificate = copy.deepcopy(PRIMARY_RECEIPT)
bad_certificate["automorphism_certificates"]["b0"]["support_permutation"][0] = (
    bad_certificate["automorphism_certificates"]["b0"]["support_permutation"][0] + 1
) % 192
bad_ok, _ = certificate_ok(
    bad_certificate["automorphism_certificates"]["b0"]["support_permutation"]
)
gate(not bad_ok, "hostile.automorphism_mutation",
     "a one-entry automorphism mutation is rejected by independent incidence verification")

N5 = [
    "per_element: checked -- all 192 columns enter the exact weight-sixteen CNF and certificates",
    "per_site: checked -- one supplied 16-corner coordinate cell only",
    "per_mode: checked and not executed -- this finite model has no modes",
    "per_block: checked -- all 15800 rows enter certificate and carrier verification",
    "lattice_wide: checked and not executed -- no multicell or limit claim",
]
for line in N5:
    print("N5 " + line, flush=True)

receipt = {
    "schema": "physical-cell-cutting-sixteen-attained-cycle742-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "checker_sha256": sha256(CHECKER_PATH),
    "primary_receipt_bound": primary_contract_ok(PRIMARY_RECEIPT),
    "population": {"cuttings": len(solutions), "used_pieces": len(used), "rank": len(pivots)},
    "incidence_identity": {
        "canonical_incidence_rows_sha256": canonical_incidence_hash,
        "support_column_order_sha256": column_order_hash,
    },
    "exact_weight_sixteen_four": {
        "answer": bool(four_sat), "support": four_support,
        "clauses": clause_count, "variables": variable_count,
    },
    "automorphism_certificates_verified": bool(cert_ok),
    "automorphism_support_permutation_sha256": {
        name: certs[name]["support_permutation_sha256"] for name in ("b0", "b1")
    },
    "verified_carrier_supports": len(all_supports) if supports_ok else 0,
    "restricted_ranks": {
        "single": single_ranks,
        "single_augmented_four": single_augmented,
        "pairs": pair_ranks,
        "pair_consistent_readings": pair_consistent,
    },
    "extended_group": {
        "piece_transitive": bool(group_ok),
        "closure_count": len(closure),
        "carrier_orbit_sizes": support_orbit_sizes(all_supports),
    },
    "n5_execution_certificate": N5,
    "gates": {
        "pass": passed,
        "fail": failed,
        "named": {name: "PASS" if ok else "FAIL" for name, ok in gates},
    },
}
receipt_tmp = RECEIPT_PATH.with_suffix(RECEIPT_PATH.suffix + ".tmp")
receipt_tmp.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
receipt_tmp.replace(RECEIPT_PATH)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(1 if failed else 0)
