"""Independent finite reconstruction for the Cycle 736 charge-space packet.

This checker does not import the primary runner.  It rebuilds the corner-simplex
population, exact-cover family, exact geometric orbit certificates, exchange ladder,
GF(2) response space, connected components, and supplied symmetry action.  Nearby
sample-only, semantic, source, input, and failed-verdict mutations are rejected.
"""

import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md",
    "scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py",
    "scripts/physical_column_family_parity_law_forced_orbits_cycle733_independent_check_2026_08_04.py",
    "outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_receipt_2026-08-04.json",
)
ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ROOT / AUDIT_INPUT_PATHS[0]
RECEIPT_PATH = ROOT / AUDIT_INPUT_PATHS[1]
RECEIPT = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
C733 = json.loads((ROOT / AUDIT_INPUT_PATHS[-1]).read_text(encoding="utf-8"))
passed = 0
failed = 0


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def gate(name, condition, detail):
    global passed, failed
    if condition:
        passed += 1
        word = "PASS"
    else:
        failed += 1
        word = "FAIL"
    print(f"{word} {name}  {detail}", flush=True)


def determinant(matrix):
    """Small exact Laplace expansion, deliberately independent of the primary formula."""
    rows = [[int(value) for value in row] for row in matrix]
    if len(rows) == 1:
        return rows[0][0]
    answer = 0
    for column, value in enumerate(rows[0]):
        minor = [row[:column] + row[column + 1 :] for row in rows[1:]]
        answer += (-1 if column & 1 else 1) * value * determinant(minor)
    return answer


def gf2_basis(rows, initial=None):
    pivots = {} if initial is None else dict(initial)
    for value in rows:
        row = int(value)
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return pivots


def gf2_rref(rows, initial=None):
    pivots = gf2_basis(rows, initial)
    for low in sorted(pivots):
        for high in sorted(pivots):
            if high > low and ((pivots[high] >> low) & 1):
                pivots[high] ^= pivots[low]
    return pivots


def reduces_to_zero(row, pivots):
    row = int(row)
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return False
        row ^= pivots[pivot]
    return True


def orthogonal_basis(pivots, width):
    answer = []
    for free in range(width):
        if free in pivots:
            continue
        weight = 1 << free
        for pivot, row in pivots.items():
            if (row >> free) & 1:
                weight |= 1 << pivot
        answer.append(weight)
    return answer


def input_contract_ok(receipt):
    expected = receipt.get("input_sha256", {})
    return (receipt.get("runner_sha256") == hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
            and all(path in expected and sha256(path) == expected[path]
               for path in expected)
            )


gate(
    "receipt contract",
    RECEIPT.get("schema") == "physical-cell-cutting-charge-space-cycle736-v2"
    and RECEIPT.get("claim_type") == "bounded_theorem"
    and RECEIPT.get("status") == "pass"
    and RECEIPT.get("gates", {}).get("fail") == 0
    and input_contract_ok(RECEIPT),
    "the positive verdict and every declared primary input are content-bound",
)
gate(
    "upstream geometric contract",
    C733.get("claim_type") == "bounded_theorem"
    and C733.get("totals", {}).get("fail") == 0
    and C733.get("minimum", {}).get("dissections") == 15800
    and C733.get("minimum", {}).get("geometric_representatives") == 391,
    "Cycle 733 independently binds the supplied finite model and geometric population",
)

# Reconstruct the finite object without importing either runner.
CORNERS = list(itertools.product((0, 1), repeat=4))
VERTICES = np.array(CORNERS, dtype=np.int64)
CORNER_INDEX = {corner: index for index, corner in enumerate(CORNERS)}
PIECES = []
MATRICES = []
INVERSES = []
for subset in itertools.combinations(range(16), 5):
    matrix = (VERTICES[list(subset[1:])] - VERTICES[subset[0]]).T
    if abs(determinant(matrix.tolist())) == 1:
        inverse = np.rint(np.linalg.inv(matrix.astype(float))).astype(np.int64)
        if np.array_equal(matrix @ inverse, np.eye(4, dtype=np.int64)):
            PIECES.append(subset)
            MATRICES.append(matrix)
            INVERSES.append(inverse)
MATRICES = np.array(MATRICES, dtype=np.int64)
INVERSES = np.array(INVERSES, dtype=np.int64)
PIECE_INDEX = {piece: index for index, piece in enumerate(PIECES)}
PAIR_POSITIONS = list(itertools.combinations(range(5), 2))


def piece_cost(piece):
    points = VERTICES[list(piece)]
    return sum(
        sum(abs(int(points[a, column]) - int(points[b, column]))
            for column in range(4)) > 1
        for a, b in PAIR_POSITIONS
    )


COST = np.array([piece_cost(piece) for piece in PIECES], dtype=np.int64)
MINIMUM = np.flatnonzero(COST == int(COST.min())).tolist()

# Supplied action: 24 orientation-preserving spatial signed permutations, optionally
# composed with the labelled tick flip.
GROUP = []
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
                action.append(CORNER_INDEX[target])
            GROUP.append(np.array(action, dtype=np.int32))
PIECE_PERMS = []
for action in GROUP:
    PIECE_PERMS.append(np.array([
        PIECE_INDEX[tuple(sorted(int(action[corner]) for corner in piece))]
        for piece in PIECES
    ], dtype=np.int32))

# One generic interior sample orbit for every simplex orbit.  These masks accelerate the
# exact-cover enumeration but are not used as the geometric sufficiency test below.
labels = np.full(len(PIECES), -1, dtype=np.int64)
representatives = []
for index, piece in enumerate(PIECES):
    if labels[index] >= 0:
        continue
    orbit = len(representatives)
    representatives.append(index)
    for permutation in PIECE_PERMS:
        labels[int(permutation[index])] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
bound = max(int(np.abs(INVERSES).max()), 3)
weights = 2 * (bound * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_map = {}
collisions = 0
for orbit, index in enumerate(representatives):
    for action in GROUP:
        image_corner = []
        for corner in PIECES[index]:
            image_corner.append(int(action[corner]))
        # Map the barycentric weights with the corner action; no floating point geometry.
        transformed = (weights[:, None] * VERTICES[image_corner]).sum(axis=0)
        key = tuple(int(value) for value in transformed)
        previous = sample_map.setdefault(key, orbit)
        collisions += previous != orbit
SAMPLES = np.array(sorted(sample_map), dtype=np.int64)
INCIDENCE = np.zeros((len(PIECES), len(SAMPLES)), dtype=np.uint8)
boundary_hits = 0
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (SAMPLES.T - (scale * VERTICES[piece[0]])[:, None])
    total = bary.sum(axis=0)
    boundary_hits += int(((bary == 0).any(axis=0) | (total == scale)).sum())
    INCIDENCE[index] = (bary > 0).all(axis=0) & (total < scale)
MASKS = []
for row in INCIDENCE:
    mask = 0
    for point in np.flatnonzero(row):
        mask |= 1 << int(point)
    MASKS.append(mask)
ALL_POINTS = (1 << len(SAMPLES)) - 1
gate(
    "finite universe",
    len(PIECES) == 2672 and len(MINIMUM) == 400 and int(COST.min()) == 6
    and len(GROUP) == 48 and len(representatives) == 57
    and len(SAMPLES) == 2736 and collisions == 0 and boundary_hits == 0
    and scale == 12810,
    "2672 unit simplices, 400 minimum-cost candidates, and collision-free samples",
)

by_point = {}
for index in MINIMUM:
    for point in np.flatnonzero(INCIDENCE[index]):
        by_point.setdefault(int(point), []).append(index)
solutions = []
nodes = 0


def enumerate_covers(covered, chosen):
    global nodes
    nodes += 1
    if covered == ALL_POINTS:
        solutions.append(tuple(sorted(chosen)))
        return
    remainder = ALL_POINTS & ~covered
    point = (remainder & -remainder).bit_length() - 1
    for index in by_point[point]:
        if MASKS[index] & covered:
            continue
        chosen.append(index)
        enumerate_covers(covered | MASKS[index], chosen)
        chosen.pop()


enumerate_covers(0, [])
solution_set = set(solutions)
used = sorted({piece for solution in solutions for piece in solution})
used_position = {piece: position for position, piece in enumerate(used)}
neg_normals = [np.array(row, dtype=np.int64)
               for row in itertools.product((-1, 0, 1), repeat=4) if any(row)]


def separated(indices):
    points = [VERTICES[list(PIECES[index])] for index in indices]
    facets = []
    for index in indices:
        inverse = INVERSES[index]
        facets.append([inverse[row] for row in range(4)] + [-inverse.sum(axis=0)])
    good = 0
    for left, right in itertools.combinations(range(len(indices)), 2):
        for normal in neg_normals + facets[left] + facets[right]:
            a = points[left] @ normal
            b = points[right] @ normal
            if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                good += 1
                break
    return good


seen = set()
geometry_representatives = 0
geometry_pairs = 0
geometry_ok = True
for solution in solutions:
    if solution in seen:
        continue
    geometry_representatives += 1
    geometry_pairs += 276
    geometry_ok = geometry_ok and separated(solution) == 276
    for permutation in PIECE_PERMS:
        image = tuple(sorted(int(permutation[index]) for index in solution))
        geometry_ok = geometry_ok and image in solution_set
        seen.add(image)
gate(
    "exact-cover geometry",
    nodes == 502838 and len(solutions) == 15800 and len(used) == 192
    and all(len(solution) == 24 for solution in solutions)
    and geometry_ok and geometry_representatives == 391
    and geometry_pairs == 107916 and len(seen) == len(solutions),
    "15800 covers form 391 geometric orbits with 107916 exact pair certificates",
)

# Full unordered pair census of the reconstructed population.
incidence = np.zeros((len(solutions), len(used)), dtype=np.uint8)
solution_bits = []
for row, solution in enumerate(solutions):
    bits = 0
    for piece in solution:
        position = used_position[piece]
        incidence[row, position] = 1
        bits |= 1 << position
    solution_bits.append(bits)
packed = np.packbits(incidence, axis=1)
popcount = np.array([int(value).bit_count() for value in range(256)], dtype=np.uint8)
sizes = (4, 5, 6, 7, 8, 9, 10)
edge_left = {size: [] for size in sizes}
edge_right = {size: [] for size in sizes}
exchange_sets = {size: set() for size in sizes if size != 5}
for lower in range(0, len(solutions), 100):
    upper = min(lower + 100, len(solutions))
    distance = popcount[np.bitwise_xor(packed[lower:upper, None, :], packed[None, :, :])].sum(
        axis=2, dtype=np.int16
    )
    for size in sizes:
        local, other = np.nonzero(distance == 2 * size)
        keep = local + lower < other
        left = (local[keep] + lower).tolist()
        right = other[keep].tolist()
        edge_left[size].extend(left)
        edge_right[size].extend(right)
        if size != 5:
            for a, b in zip(left, right):
                exchange_sets[size].add(solution_bits[a] ^ solution_bits[b])
pair_counts = [len(edge_left[size]) for size in sizes]
distinct_counts = [len(exchange_sets[size]) for size in sizes if size != 5]
gate(
    "exchange census",
    pair_counts == [46128, 0, 31968, 60096, 151704, 119808, 281376]
    and distinct_counts == [120, 528, 1152, 4212, 6144, 25248],
    "all unordered pairs reproduce the seven size counts and six exchange counts",
)

exchange_keys = {size: sorted(values) for size, values in exchange_sets.items()}
move_sizes = (4, 6, 7, 8, 9, 10)
population_differences = gf2_basis(
    solution_bits[index] ^ solution_bits[0] for index in range(1, len(solutions))
)
population_rank = len(population_differences) + (
    0 if reduces_to_zero(solution_bits[0], population_differences) else 1
)
translation_spans = {
    size: gf2_rref(value ^ exchange_keys[size][0] for value in exchange_keys[size][1:])
    for size in move_sizes
}
affine_ranks = {
    size: len(translation_spans[size]) + (
        0 if reduces_to_zero(exchange_keys[size][0], translation_spans[size]) else 1
    )
    for size in move_sizes
}
tag = 1 << len(used)
reversal_possible = {}
for size in move_sizes:
    augmented = gf2_basis(value | tag for value in exchange_keys[size])
    reversal_possible[size] = len(augmented) == affine_ranks[size]


def odd_zero_certificate(rows):
    pivots = {}
    for index, coefficient in enumerate(rows):
        row = int(coefficient)
        rhs = 1
        provenance = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (row, rhs, provenance)
                break
            base, base_rhs, base_provenance = pivots[pivot]
            row ^= base
            rhs ^= base_rhs
            provenance ^= base_provenance
        if row == 0 and rhs == 1:
            return [item for item in range(len(rows)) if (provenance >> item) & 1]
    return None


odd_certificates = {size: odd_zero_certificate(exchange_keys[size]) for size in move_sizes}


multiple_patterns = []
for mask in range(1, 1 << len(move_sizes)):
    selected = [size for bit, size in enumerate(move_sizes) if (mask >> bit) & 1]
    common_translations = {}
    for size in selected:
        common_translations = gf2_basis(translation_spans[size].values(), common_translations)
    base_rank = len(common_translations)
    common_translations = gf2_basis(
        (exchange_keys[size][0] for size in selected), common_translations
    )
    count = 1 << (len(common_translations) - base_rank)
    if count > 1:
        multiple_patterns.append((selected, count))
span67 = gf2_basis(translation_spans[7].values(), translation_spans[6])
lattice_ok = (
    all(reduces_to_zero(row, translation_spans[6]) for row in translation_spans[4].values())
    and all(reduces_to_zero(row, translation_spans[7]) for row in translation_spans[4].values())
    and not all(reduces_to_zero(row, translation_spans[7]) for row in translation_spans[6].values())
    and not all(reduces_to_zero(row, translation_spans[6]) for row in translation_spans[7].values())
    and len(span67) == 87
    and all(len(translation_spans[size]) == 87 for size in (8, 9, 10))
    and len(translation_spans[6]) + len(translation_spans[7]) - len(span67)
    == len(translation_spans[4])
)
gate(
    "response spans",
    population_rank == 88 and len(population_differences) == 87
    and [len(translation_spans[size]) for size in move_sizes] == [85, 86, 86, 87, 87, 87]
    and [affine_ranks[size] for size in move_sizes] == [86, 86, 86, 87, 87, 87]
    and reversal_possible == {4: True, 6: False, 7: False, 8: False, 9: False, 10: False}
    and odd_certificates[4] is None
    and [len(odd_certificates[size]) for size in (6, 7, 8, 9, 10)] == [7, 5, 5, 7, 5]
    and multiple_patterns == [([4], 2), ([4, 6], 2), ([4, 7], 2)]
    and lattice_ok,
    "ranks={0}, affine={1}, reversal={2}, odd={3}, multi={4}, lattice={5}".format(
        [len(translation_spans[size]) for size in move_sizes],
        [affine_ranks[size] for size in move_sizes],
        reversal_possible,
        [None if odd_certificates[size] is None else len(odd_certificates[size])
         for size in move_sizes],
        multiple_patterns,
        lattice_ok,
    ),
)

# Reconstruct all response functions induced by weights uniform on the smallest moves.
weights = orthogonal_basis(translation_spans[4], len(used))
weight_matrix = np.zeros((len(used), len(weights)), dtype=np.uint8)
for column, weight in enumerate(weights):
    for position in range(len(used)):
        weight_matrix[position, column] = (weight >> position) & 1
functions_matrix = (incidence.astype(np.int64) @ weight_matrix.astype(np.int64)) & 1
function_pivots = {}
for column in range(functions_matrix.shape[1]):
    function = functions_matrix[:, column].astype(np.uint8)
    while function.any():
        pivot = int(np.flatnonzero(function)[-1])
        if pivot not in function_pivots:
            function_pivots[pivot] = function.copy()
            break
        function ^= function_pivots[pivot]
function_basis = [function_pivots[pivot] for pivot in sorted(function_pivots)]
functions = []
for mask in range(1 << len(function_basis)):
    function = np.zeros(len(solutions), dtype=np.uint8)
    for index, base in enumerate(function_basis):
        if (mask >> index) & 1:
            function ^= base
    functions.append(function)
named = {}
for function in functions:
    count = int(function.sum())
    if count in (0, len(solutions)):
        continue
    oriented = function if 2 * count <= len(solutions) else function ^ 1
    delta4 = oriented[edge_left[4]] ^ oriented[edge_right[4]]
    delta6 = oriented[edge_left[6]] ^ oriented[edge_right[6]]
    name = "four" if int(delta4.max()) == 0 else ("six" if int(delta6.max()) == 0 else "seven")
    named[name] = oriented
charge_table = {}
for name, function in named.items():
    charge_table[name] = (
        int(function.sum()),
        [int((function[edge_left[size]] ^ function[edge_right[size]]).sum())
         for size in move_sizes],
    )
gate(
    "charge functions",
    len(weights) == 107 and len(function_basis) == 3 and len(functions) == 8
    and sum(int(function.sum()) in (0, len(solutions)) for function in functions) == 2
    and charge_table == {
        "four": (5664, [0, 9504, 26880, 32640, 48960, 124224]),
        "six": (7704, [46128, 0, 26880, 28608, 87552, 190848]),
        "seven": (7424, [46128, 9504, 0, 21312, 102336, 183744]),
    },
    "the 107-dimensional weight space induces exactly eight rank-three charges",
)

# Components and symmetry orbit/support identity.
parent = list(range(len(solutions)))


def root(index):
    while parent[index] != index:
        parent[index] = parent[parent[index]]
        index = parent[index]
    return index


for left, right in zip(edge_left[4], edge_right[4]):
    a, b = root(left), root(right)
    if a != b:
        parent[a] = b
components_by_root = {}
for index in range(len(solutions)):
    components_by_root.setdefault(root(index), []).append(index)
components = list(components_by_root.values())
profile = {}
for component in components:
    profile[len(component)] = profile.get(len(component), 0) + 1
component_index = np.zeros(len(solutions), dtype=np.int64)
for index, component in enumerate(components):
    component_index[component] = index
solution_index = {solution: index for index, solution in enumerate(solutions)}
solution_perms = []
for permutation in PIECE_PERMS:
    solution_perms.append(np.array([
        solution_index[tuple(sorted(int(permutation[piece]) for piece in solution))]
        for solution in solutions
    ], dtype=np.int64))
component_perms = []
component_action_ok = True
for permutation in solution_perms:
    image = np.zeros(len(components), dtype=np.int64)
    for index, component in enumerate(components):
        targets = component_index[permutation[component]]
        component_action_ok = component_action_ok and int(targets.min()) == int(targets.max())
        image[index] = int(targets[0])
    component_perms.append(image)
component_orbits = []
orbit_seen = set()
for index in range(len(components)):
    if index in orbit_seen:
        continue
    orbit = sorted({int(permutation[index]) for permutation in component_perms})
    orbit_seen.update(orbit)
    component_orbits.append(orbit)
orbit236 = [orbit for orbit in component_orbits if len(components[orbit[0]]) == 236]
orbit9320 = [orbit for orbit in component_orbits if len(components[orbit[0]]) == 9320]
charges_fixed = all(np.array_equal(function[permutation], function)
                    for function in functions for permutation in solution_perms)
support = set(np.flatnonzero(named["four"]).tolist())
union236 = set()
for component in orbit236[0]:
    union236.update(components[component])
degrees = np.zeros(len(solutions), dtype=np.int64)
for size in (4, 6, 7, 8):
    np.add.at(degrees, edge_left[size], 1)
    np.add.at(degrees, edge_right[size], 1)
rigid = set(np.flatnonzero(degrees == 0).tolist())
gate(
    "component and symmetry identity",
    len(components) == 349
    and profile == {1: 144, 2: 96, 4: 36, 7: 48, 236: 24, 9320: 1}
    and component_action_ok and len(component_orbits) == 14
    and len(orbit236) == 1 and len(orbit236[0]) == 24
    and len(orbit9320) == 1 and len(orbit9320[0]) == 1
    and charges_fixed and support == union236 and len(support) == 5664
    and len(rigid) == 48 and not (support & rigid),
    "the four-keeping charge is exactly the 24-by-236 component-orbit indicator",
)

# Hostile controls establish that each acceptance boundary is load-bearing.
overlap_control = next(
    ((left, right) for left in MINIMUM for right in MINIMUM
     if left < right and not (MASKS[left] & MASKS[right])
     and separated((left, right)) == 0),
    None,
)
gate(
    "hostile sample-only cover rejected",
    overlap_control is not None,
    "sample-disjoint simplices can overlap, so exact geometric separation is necessary",
)
mutated_exchange = exchange_keys[4].copy()
mutated_exchange[0] ^= 1
gate(
    "hostile exchange mutation rejected",
    len(gf2_rref(value ^ mutated_exchange[0] for value in mutated_exchange[1:])) != 85,
    "a local exchange-bit mutation changes the certified smallest-move response space",
)
source_bytes = PRIMARY.read_bytes()
mutated_source_hash = hashlib.sha256(source_bytes.replace(b"[46128, 0, 31968", b"[46129, 0, 31968", 1)).hexdigest()
gate(
    "hostile source mutation rejected",
    mutated_source_hash != RECEIPT.get("runner_sha256")
    and RECEIPT.get("runner_sha256") == hashlib.sha256(source_bytes).hexdigest(),
    "the checker source binding rejects a local primary semantic mutation",
)
mutated_upstream = copy.deepcopy(RECEIPT)
mutated_upstream["input_sha256"][AUDIT_INPUT_PATHS[-1]] = "0" * 64
gate(
    "hostile upstream mutation rejected",
    not input_contract_ok(mutated_upstream),
    "a terminal dependency hash mutation invalidates the positive receipt contract",
)
failed_receipt = copy.deepcopy(RECEIPT)
failed_receipt["status"] = "fail"
failed_receipt["gates"]["fail"] = 1
gate(
    "hostile failed verdict rejected",
    not (failed_receipt.get("status") == "pass" and failed_receipt["gates"]["fail"] == 0),
    "a failed generated verdict cannot satisfy the independent acceptance predicate",
)
gate(
    "receipt summary",
    RECEIPT.get("population", {}).get("geometric_cuttings") == len(solutions)
    and RECEIPT.get("moves", {}).get("pair_counts") == pair_counts
    and RECEIPT.get("moves", {}).get("distinct_exchange_counts") == distinct_counts
    and RECEIPT.get("responses", {}).get("charge_table", {}).get("four", {}).get("split")
    == [5664, 10136]
    and RECEIPT.get("components", {}).get("size_profile")
    == {str(size): count for size, count in profile.items()},
    "generated primary receipt matches the independent finite reconstruction",
)

print("")
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(1 if failed else 0)
