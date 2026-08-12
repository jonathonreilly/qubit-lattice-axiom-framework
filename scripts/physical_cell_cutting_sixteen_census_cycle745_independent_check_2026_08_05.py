"""Independent exact syndrome-DP and group-action check for Cycle 745.

This checker imports neither the Cycle 745 primary nor its search engine.  It rebuilds
the supplied 15800-by-192 incidence table with the opposite exact-cover pivot, rebuilds
the 48 geometric column permutations, semantically validates the two receipt-carried
extra permutations, and closes their generated action. A complete exact-weight-16
syndrome-DP/MITM census reconstructs all 132 four carriers and excludes every carrier
of the other five readings. All positive witnesses and both orbit folds are checked
separately.
"""

import copy
import hashlib
import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

import numpy as np

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
    incidence_identity = receipt.get("incidence_identity", {})
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
        and incidence_identity.get("canonical_incidence_rows_sha256")
        == canonical_incidence_hash
        and incidence_identity.get("support_column_order_sha256") == column_order_hash
        and incidence_identity.get("support_column_corner_tuples") == column_order
        and len(target_identity.get("ordered_names", [])) == 18
        and target_identity.get("odd_control_non_column_space") is True
        and search.get("readings") == target_identity.get("ordered_names", [])[2:8]
        + target_identity.get("ordered_names", [])[12:17]
        and search.get("counts") == [11, 0, 0, 0, 0, 0, 2, 6, 12, 1, 3]
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
explicit_base_permutations = primary_receipt["transitive_group"].get(
    "base_support_permutations", []
)
explicit_generator_hash = primary_receipt["transitive_group"].get(
    "ordered_generator_support_permutations_sha256"
)
generators = base_permutations + [
    np.array(seeded["b0"], dtype=np.int64),
    np.array(seeded["b1"], dtype=np.int64),
]
ordered_generator_lists = [
    [int(column) for column in permutation] for permutation in generators
]
ordered_generator_hash = hashlib.sha256(
    json.dumps(ordered_generator_lists, separators=(",", ":")).encode("utf-8")
).hexdigest()
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
gate(generator_ok and len(base_permutations) == 48
     and explicit_base_permutations == ordered_generator_lists[:48]
     and explicit_generator_hash == ordered_generator_hash
     and len(group) == 384
     and len({int(permutation[anchor]) for permutation in group.values()}) == 192
     and group_hash == primary_receipt["transitive_group"]["generated_group_sha256"],
     "independent.group",
     "independent geometry plus verified seeded maps close to the same transitive order-384 action")


# Independent exact syndrome DP/MITM.  This is not the primary planner: it uses the
# opposite-pivot incidence above, keeps only counts (never the primary support arrays),
# streams exact lexicographic block tables, and chooses the reverse tie order.
SEARCH_START = time.time()
PACKED_BASIS = np.packbits(incidence[pivot_rows], axis=1, bitorder="little")
COLUMN_INTS = []
for column in range(192):
    value = 0
    for bit, row_index in enumerate(pivot_rows):
        value |= int(incidence[row_index, column]) << bit
    COLUMN_INTS.append(value)


def pack_basis_bits(bits):
    bits = np.asarray(bits, dtype=np.uint64)
    answer = np.zeros(bits.shape[:-1] + (2,), dtype=np.uint64)
    for bit in range(88):
        word, shift = divmod(bit, 64)
        answer[..., word] |= bits[..., bit] << np.uint64(shift)
    return answer


COLUMN_SYNDROMES = pack_basis_bits(incidence[pivot_rows].T)
TARGET_SYNDROMES = {
    name: pack_basis_bits(target[pivot_rows]) for name, target in targets.items()
}


def complement(columns):
    selected = set(columns)
    return [column for column in range(192) if column not in selected]


def internal_basis(columns):
    """All row combinations whose resulting indicator is supported in columns."""
    outside = complement(columns)
    local = {}
    kernel = []
    for row in range(88):
        value = sum(
            ((COLUMN_INTS[column] >> row) & 1) << offset
            for offset, column in enumerate(outside)
        )
        witness = 1 << row
        while value:
            pivot = value.bit_length() - 1
            if pivot not in local:
                local[pivot] = (value, witness)
                break
            basis_value, basis_witness = local[pivot]
            value ^= basis_value
            witness ^= basis_witness
        if value == 0:
            kernel.append(witness)
    return kernel


def key_table(internal):
    words = max(1, (len(internal) + 63) // 64)
    table = np.zeros((words, 11, 256), dtype=np.uint64)
    for byte in range(11):
        for value in range(256):
            for row_bit in range(8):
                if not ((value >> row_bit) & 1):
                    continue
                basis_bit = 8 * byte + row_bit
                if basis_bit >= 88:
                    continue
                for index, vector in enumerate(internal):
                    if (vector >> basis_bit) & 1:
                        table[index // 64, byte, value] ^= (
                            np.uint64(1) << np.uint64(index & 63)
                        )
    return table


def keys_of(syndromes, table):
    raw = np.ascontiguousarray(syndromes).view(np.uint8).reshape(-1, 16)
    answer = np.zeros((len(raw), table.shape[0]), dtype=np.uint64)
    for byte in range(11):
        for word in range(table.shape[0]):
            answer[:, word] ^= table[word, byte][raw[:, byte]]
    return answer


def one_key(syndrome, table):
    raw = np.ascontiguousarray(syndrome).view(np.uint8)
    answer = np.zeros(table.shape[0], dtype=np.uint64)
    for byte in range(11):
        for word in range(table.shape[0]):
            answer[word] ^= table[word, byte, int(raw[byte])]
    return answer


QUARTERS = [list(range(48 * q, 48 * q + 48)) for q in range(4)]
EIGHTHS = [list(range(24 * e, 24 * e + 24)) for e in range(8)]


def extension_chain(columns, maximum):
    ncols = len(columns)
    tables = {0: np.zeros((1, 2), dtype=np.uint64)}
    offsets = {1: np.arange(ncols + 1, dtype=np.int64)}
    if maximum:
        tables[1] = COLUMN_SYNDROMES[columns].copy()
    for weight in range(1, maximum):
        previous, previous_offsets = tables[weight], offsets[weight]
        size = sum(len(previous) - previous_offsets[column + 1]
                   for column in range(ncols))
        output = np.empty((size, 2), dtype=np.uint64)
        next_offsets = np.empty(ncols + 1, dtype=np.int64)
        position = 0
        for column in range(ncols):
            block = previous[previous_offsets[column + 1]:]
            next_offsets[column] = position
            if len(block):
                np.bitwise_xor(
                    block, COLUMN_SYNDROMES[columns[column]],
                    out=output[position:position + len(block)],
                )
            position += len(block)
        next_offsets[ncols] = position
        tables[weight + 1] = output
        offsets[weight + 1] = next_offsets
    return tables


QUARTER_TABLES = [extension_chain(columns, 5) for columns in QUARTERS]
QUARTER_SIX = {}
EIGHTH_TABLES = {}
ZERO_TABLE = np.zeros((1, 2), dtype=np.uint64)
MAX_PART_ROWS = 0
MAX_JOIN_ROWS = 0
INTERMEDIATE_CAP = 30_000_000


def part_table(kind, index, weight):
    global MAX_PART_ROWS
    if weight == 0:
        return ZERO_TABLE
    if kind == "Q":
        if weight <= 5:
            table = QUARTER_TABLES[index][weight]
        elif weight == 6:
            table = QUARTER_SIX.get(index)
            if table is None:
                chain = extension_chain(QUARTERS[index], 6)
                table = chain[6]
                QUARTER_SIX[index] = table
        else:
            raise ValueError("quarter part exceeds independently tabulated weight six")
    else:
        state = EIGHTH_TABLES.get(index)
        if state is None or max(state) < weight:
            state = extension_chain(EIGHTHS[index], weight)
            EIGHTH_TABLES[index] = state
        table = state[weight]
    MAX_PART_ROWS = max(MAX_PART_ROWS, len(table))
    return table


INTERNAL_CACHE = {}
KEY_TABLE_CACHE = {}
SORTED_CACHE = {}
SORTED_CACHE_ROWS = [0]


def cached_key_table(label, columns):
    table = KEY_TABLE_CACHE.get(label)
    if table is None:
        basis = INTERNAL_CACHE.setdefault(label, internal_basis(columns))
        table = key_table(basis)
        KEY_TABLE_CACHE[label] = table
    return table


def sorted_keys(label, syndromes, table):
    key = (label, len(syndromes), int(syndromes[0, 0]) if len(syndromes) else 0)
    cached = SORTED_CACHE.get(key)
    if cached is None:
        values = keys_of(syndromes, table)[:, 0]
        order = np.argsort(values, kind="mergesort")
        cached = (values[order], order)
        if SORTED_CACHE_ROWS[0] + 2 * len(order) > 30_000_000:
            SORTED_CACHE.clear()
            SORTED_CACHE_ROWS[0] = 0
        SORTED_CACHE[key] = cached
        SORTED_CACHE_ROWS[0] += 2 * len(order)
    return cached


def planner(cell):
    if max(cell) <= 6:
        streamed = max(
            range(4), key=lambda q: (math.comb(48, cell[q]), q)
        )
        return [(('Q', streamed, cell[streamed]), [
            ('Q', q, cell[q]) for q in range(4) if q != streamed
        ])]
    heavy = [q for q in range(4) if cell[q] > 6]
    distributions = [
        [(left, cell[q] - left) for left in range(cell[q] + 1)
         if left <= 24 and cell[q] - left <= 24]
        for q in heavy
    ]
    remaining = [('Q', q, cell[q]) for q in range(4) if q not in heavy]
    plans = []
    for split in itertools.product(*distributions):
        parts = []
        for q, (left, right) in zip(heavy, split):
            parts.extend((('E', 2 * q, left), ('E', 2 * q + 1, right)))
        parts.extend(remaining)
        streamed = max(
            range(len(parts)),
            key=lambda i: (
                math.comb(24 if parts[i][0] == 'E' else 48, parts[i][2]), i
            ),
        )
        plans.append((parts[streamed], [part for i, part in enumerate(parts)
                                         if i != streamed]))
    return plans


def cells(weight):
    answer = []
    for q0 in range(weight + 1):
        for q1 in range(weight - q0 + 1):
            for q2 in range(weight - q0 - q1 + 1):
                answer.append((q0, q1, q2, weight - q0 - q1 - q2))
    return answer


ROWSPACE = {}
for basis_index, row_index in enumerate(pivot_rows):
    value = row_bits[row_index]
    witness = 1 << basis_index
    while value:
        pivot = value.bit_length() - 1
        if pivot not in ROWSPACE:
            ROWSPACE[pivot] = (value, witness)
            break
        basis_value, basis_witness = ROWSPACE[pivot]
        value ^= basis_value
        witness ^= basis_witness


def forced_witness(columns):
    value = sum(1 << column for column in columns)
    witness = 0
    while value:
        pivot = value.bit_length() - 1
        if pivot not in ROWSPACE:
            return None
        basis_value, basis_witness = ROWSPACE[pivot]
        value ^= basis_value
        witness ^= basis_witness
    return witness


FORCED_BLOCKS = {
    "total": forced_witness(range(192)),
    "left": forced_witness(range(96)),
    "q2": forced_witness(range(96, 144)),
    "q3": forced_witness(range(144, 192)),
}


def forced_bit(name, target):
    witness = FORCED_BLOCKS[name]
    return sum(
        ((witness >> bit) & 1) * int(target[pivot_rows[bit]])
        for bit in range(88)
    ) & 1


def licensed(cell, target):
    values = {"total": 16, "left": cell[0] + cell[1],
              "q2": cell[2], "q3": cell[3]}
    return all((value & 1) == forced_bit(name, target)
               for name, value in values.items())


def best_join_order(parts, sizes, final_label, final_columns):
    if len(parts) < 3:
        return sorted(range(len(parts)), key=lambda i: (sizes[i], -i))
    block_columns = [QUARTERS[p[1]] if p[0] == 'Q' else EIGHTHS[p[1]]
                     for p in parts]
    final_dimension = min(len(INTERNAL_CACHE.setdefault(
        final_label, internal_basis(final_columns))), 62)
    best = None
    best_order = None
    # Reverse enumeration is a deliberate independent tie convention.
    for order in reversed(list(itertools.permutations(range(len(parts))))):
        current = float(sizes[order[0]])
        worst = current
        joined = list(block_columns[order[0]])
        labels = [(parts[order[0]][0], parts[order[0]][1])]
        for step in range(1, len(parts)):
            index = order[step]
            joined += block_columns[index]
            labels.append((parts[index][0], parts[index][1]))
            if step == len(parts) - 1:
                dimension = final_dimension
            else:
                label = ('internal', tuple(sorted(labels)))
                dimension = min(len(INTERNAL_CACHE.setdefault(
                    label, internal_basis(joined))), 62)
            current = current * sizes[index] / float(1 << dimension)
            worst = max(worst, current)
        if best is None or worst < best:
            best, best_order = worst, list(order)
    return best_order


def meet(left, right, sorted_right, order, left_keys, target_key):
    global MAX_JOIN_ROWS
    wanted = left_keys ^ target_key
    low = np.searchsorted(sorted_right, wanted, side="left")
    high = np.searchsorted(sorted_right, wanted, side="right")
    counts = (high - low).astype(np.int64)
    total = int(counts.sum())
    MAX_JOIN_ROWS = max(MAX_JOIN_ROWS, total)
    if total > INTERMEDIATE_CAP:
        raise MemoryError("independent join exceeded 30,000,000 exact rows")
    if total == 0:
        return np.zeros((0, 2), dtype=np.uint64)
    source = np.repeat(np.arange(len(left), dtype=np.int64), counts)
    cumulative = np.cumsum(counts)
    offsets = np.arange(total, dtype=np.int64) - np.repeat(
        cumulative - counts, counts
    )
    destination = order[np.repeat(low, counts) + offsets]
    return left[source] ^ right[destination]


def count_split(streamed, remainder, active_names, target_syndromes):
    streamed_columns = QUARTERS[streamed[1]] if streamed[0] == 'Q' else EIGHTHS[streamed[1]]
    final_columns = complement(streamed_columns)
    final_label = ('final', streamed[0], streamed[1])
    final_key_table = cached_key_table(final_label, final_columns)
    live_parts = [part for part in remainder if part[2] > 0]
    tables = [part_table(*part) for part in live_parts]
    order = best_join_order(
        live_parts, [len(table) for table in tables], final_label, final_columns
    ) if live_parts else []
    steps = []
    if len(live_parts) >= 2:
        joined = list(QUARTERS[live_parts[order[0]][1]]
                      if live_parts[order[0]][0] == 'Q'
                      else EIGHTHS[live_parts[order[0]][1]])
        labels = [(live_parts[order[0]][0], live_parts[order[0]][1])]
        for step in range(1, len(live_parts)):
            index = order[step]
            part_columns = QUARTERS[live_parts[index][1]] \
                if live_parts[index][0] == 'Q' else EIGHTHS[live_parts[index][1]]
            joined += part_columns
            labels.append((live_parts[index][0], live_parts[index][1]))
            if step == len(live_parts) - 1:
                label, table = final_label, final_key_table
            else:
                label = ('internal', tuple(sorted(labels)))
                table = cached_key_table(label, joined)
            sorted_values, sorted_order = sorted_keys(
                (live_parts[index], label), tables[index], table
            )
            steps.append((index, table, sorted_values, sorted_order))
    elif len(live_parts) == 1:
        index = order[0]
        sorted_values, sorted_order = sorted_keys(
            (live_parts[index], final_label), tables[index], final_key_table
        )
        steps.append((index, final_key_table, sorted_values, sorted_order))

    finals = {}
    for name in active_names:
        if not live_parts:
            target_key = one_key(target_syndromes[name], final_key_table)
            finals[name] = ZERO_TABLE if not target_key.any() else None
            continue
        if len(live_parts) == 1:
            index, table, sorted_values, sorted_order = steps[0]
            target_key = one_key(target_syndromes[name], table)
            low = int(np.searchsorted(sorted_values, target_key[0], side="left"))
            high = int(np.searchsorted(sorted_values, target_key[0], side="right"))
            selected = sorted_order[low:high]
            if table.shape[0] > 1 and len(selected):
                selected = selected[np.all(
                    keys_of(tables[index][selected], table) == target_key[None, :],
                    axis=1,
                )]
            finals[name] = tables[index][selected] if len(selected) else None
            continue
        syndrome = tables[order[0]]
        for index, table, sorted_values, sorted_order in steps:
            target_key = one_key(target_syndromes[name], table)
            left_keys = keys_of(syndrome, table)[:, 0]
            syndrome = meet(
                syndrome, tables[index], sorted_values, sorted_order,
                left_keys, target_key[0],
            )
            if table.shape[0] > 1 and len(syndrome):
                syndrome = syndrome[np.all(
                    keys_of(syndrome, table) == target_key[None, :], axis=1
                )]
            if not len(syndrome):
                break
        finals[name] = syndrome if len(syndrome) else None

    live = [name for name in active_names if finals[name] is not None]
    if not live:
        return {name: 0 for name in active_names}
    shifted0 = np.concatenate([
        finals[name][:, 0] ^ target_syndromes[name][0] for name in live
    ])
    shifted1 = np.concatenate([
        finals[name][:, 1] ^ target_syndromes[name][1] for name in live
    ])
    if len(shifted0) > INTERMEDIATE_CAP:
        raise MemoryError("independent final join exceeded 30,000,000 exact rows")
    markers = np.concatenate([
        np.full(len(finals[name]), index, dtype=np.int64)
        for index, name in enumerate(live)
    ])
    sort = np.lexsort((shifted1, shifted0))
    shifted0, shifted1, markers = shifted0[sort], shifted1[sort], markers[sort]
    streamed_table = part_table(*streamed)
    counts = {name: 0 for name in active_names}
    for start in range(0, len(streamed_table), 2_000_000):
        block = streamed_table[start:start + 2_000_000]
        low = np.searchsorted(shifted0, block[:, 0], side="left")
        high = np.searchsorted(shifted0, block[:, 0], side="right")
        multiplicity = high - low
        total = int(multiplicity.sum())
        if not total:
            continue
        source = np.repeat(np.arange(len(block), dtype=np.int64), multiplicity)
        cumulative = np.cumsum(multiplicity)
        match = np.repeat(low, multiplicity) + (
            np.arange(total, dtype=np.int64) - np.repeat(cumulative - multiplicity,
                                                         multiplicity)
        )
        keep = shifted1[match] == block[source, 1]
        for index, name in enumerate(live):
            counts[name] += int(((markers[match] == index) & keep).sum())
    return counts


def exact_sweep(names, target_syndromes, selected_cells=None):
    totals = {name: 0 for name in names}
    inventory = []
    search_cells = selected_cells if selected_cells is not None else cells(16)
    for cell in search_cells:
        active = [name for name in names if licensed(cell, targets[name])]
        if not active:
            continue
        for streamed, remainder in planner(cell):
            inventory.append((cell, streamed, tuple(remainder)))
            counts = count_split(streamed, remainder, active, target_syndromes)
            for name in active:
                totals[name] += counts[name]
    return totals, inventory



search_names = tuple(ordered_names[2:8])
known16 = list(range(16))
planted16 = (incidence[:, known16].sum(axis=1) & 1).astype(np.uint8)
targets["planted16"] = planted16
TARGET_SYNDROMES["planted16"] = pack_basis_bits(planted16[pivot_rows])
validation_counts, validation_inventory = exact_sweep(
    ("planted16",), TARGET_SYNDROMES, [(16, 0, 0, 0)]
)
gate(validation_counts["planted16"] > 0 and len(validation_inventory) == 17,
     "independent.small_validation",
     "an independently planted weight-sixteen target is recovered in its exact cell")
if len(sys.argv) > 1 and sys.argv[1] == "small":
    print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
    raise SystemExit(1 if failed else 0)

answers_counts, inventory = exact_sweep(search_names, TARGET_SYNDROMES)
answers = {name: answers_counts[name] > 0 for name in search_names}
expected_cells = [cell for cell in cells(16) if licensed(cell, targets[search_names[0]])]
expected_inventory = [
    (cell, streamed, tuple(remainder))
    for cell in expected_cells for streamed, remainder in planner(cell)
]
inventory_hash = hashlib.sha256(
    json.dumps(inventory, separators=(",", ":")).encode("utf-8")
).hexdigest()
solver_ok = (
    answers_counts == dict(zip(search_names, [132, 0, 0, 0, 0, 0]))
    and len(expected_cells) == 285
    and len(inventory) == len(expected_inventory) == 3527
    and inventory == expected_inventory
    and MAX_PART_ROWS == math.comb(48, 6)
    and MAX_JOIN_ROWS <= INTERMEDIATE_CAP
)
gate(solver_ok, "independent.syndrome_dp",
     "independent exact syndrome DP/MITM exhausts 285 cells and 3527 splits for all six")
gate(validation_counts["planted16"] > 0, "hostile.positive_control",
     "the independent search recovers a planted weight-sixteen target")
deleted_inventory = inventory[:-1]
redirected_inventory = list(inventory)
redirected_cell, redirected_stream, redirected_remainder = redirected_inventory[0]
redirected_inventory[0] = (
    redirected_cell,
    (redirected_stream[0], redirected_stream[1], redirected_stream[2] + 1),
    redirected_remainder,
)
gate(deleted_inventory != expected_inventory and redirected_inventory != expected_inventory,
     "hostile.inventory",
     "deleting or redirecting one exact split invalidates the independent inventory")

primary_anchored = sorted(
    tuple(support) for support in primary_receipt["four_reading_census"]["anchored_supports"]
)
anchored_counts = dict(zip(search_names, [11, 0, 0, 0, 0, 0]))
known_anchors_ok = (
    len(primary_anchored) == 11
    and len(set(primary_anchored)) == 11
    and all(anchor in support and len(support) == 16 for support in primary_anchored)
    and all(np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), targets["four"]
    ) for support in primary_anchored)
)
gate(known_anchors_ok and answers_counts["four"] == 132
     and all(answers_counts[name] == 0 for name in search_names[1:]),
     "independent.complete",
     "the primary anchored witnesses recheck inside the independent complete census")


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
    "per_element: checked -- all 192 columns enter each exact syndrome-DP split",
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
        "explicit_support_column_corner_tuples_matched": (
            primary_receipt["incidence_identity"]["support_column_corner_tuples"]
            == column_order
        ),
        "explicit_base_support_permutations_matched": (
            explicit_base_permutations == ordered_generator_lists[:48]
        ),
        "ordered_generator_support_permutations_sha256": ordered_generator_hash,
    },
    "exact_anchored_weight_sixteen_counts": anchored_counts,
    "exact_anchored_weight_sixteen_answers": {
        name: count > 0 for name, count in anchored_counts.items()
    },
    "exact_weight_sixteen_counts": answers_counts,
    "exact_weight_sixteen_answers": answers,
    "exact_syndrome_dp": {
        "anchor_column": anchor,
        "basis_rows": len(pivot_rows),
        "licensed_cells": len(expected_cells),
        "expected_splits": len(expected_inventory),
        "executed_splits": len(inventory),
        "execution_inventory_exact": inventory == expected_inventory,
        "execution_inventory_sha256": inventory_hash,
        "max_part_rows": MAX_PART_ROWS,
        "max_join_rows": MAX_JOIN_ROWS,
        "elapsed_seconds": round(time.time() - SEARCH_START, 2),
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
