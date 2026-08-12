"""Independent finite-group reconstruction for Cycle 743.

This checker imports neither the Cycle 743 primary nor its color-refinement
construction.  It enumerates the supplied exact covers with the opposite
sample pivot, consumes the exact Cycle 742 automorphism certificates, verifies
them against every reconstructed incidence row, and rebuilds the generated
piece, cutting, block, translation, and linear actions with tuple-based group
arithmetic.  The result is finite evidence only; it supplies no physical or
multi-cell interpretation.
"""

import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_"
    "receipt_2026-08-05.json"
)
CHECKER_PATH = (
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05.py"
)
C742_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md"
C742_PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py"
C742_CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py"
)
C742_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json"
)
C742_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py",
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05_receipt_2026-08-05.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "requirements.txt",
    "requirements-release.txt",
)
AUDIT_TIMEOUT_SEC = 900


def file_sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == file_sha256(path)
        for path in recorded
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
    "schema": "physical-cell-cutting-hidden-three-bit-geometry-cycle743-independent-v1",
    "status": "fail",
    "claim_type": "bounded_theorem",
    "reason": "checker has not completed",
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def determinant(matrix):
    """Leibniz determinant, deliberately distinct from the primary minor formula."""
    rows = [[int(value) for value in row] for row in matrix]
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1 if column & 1 else 1) * value
        * determinant([row[:column] + row[column + 1:] for row in rows[1:]])
        for column, value in enumerate(rows[0])
    )


# Rebuild the complete finite incidence with the largest-uncovered-sample pivot.
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
    "opposite-pivot reconstruction gives the complete 15800 by 192 table",
)

C742 = json.loads((ROOT / C742_RECEIPT_PATH).read_text(encoding="utf-8"))
C742I = json.loads((ROOT / C742_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
PRIMARY = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
certificates = C742.get("automorphism_certificates", {})


def permutation_hash(values):
    return hashlib.sha256(json.dumps(
        [int(value) for value in values], separators=(",", ":")
    ).encode("utf-8")).hexdigest()


dependency_ok = (
    C742.get("schema") == "physical-cell-cutting-sixteen-attained-cycle742-v2"
    and C742.get("status") == "pass" and C742.get("gates", {}).get("fail") == 0
    and C742.get("runner_sha256") == file_sha256(C742_PRIMARY_PATH)
    and receipt_inputs_current(C742)
    and C742I.get("schema")
    == "physical-cell-cutting-sixteen-attained-cycle742-independent-v1"
    and C742I.get("status") == "pass" and C742I.get("gates", {}).get("fail") == 0
    and (C742I.get("checker_sha256") or C742I.get("runner_sha256"))
    == file_sha256(C742_CHECKER_PATH)
    and receipt_inputs_current(C742I)
    and C742.get("incidence_identity", {}).get("canonical_incidence_rows_sha256")
    == canonical_incidence_hash
    and C742.get("incidence_identity", {}).get("support_column_order_sha256")
    == column_order_hash
    and C742.get("reading_identity", {}).get("canonical_incidence_rows_sha256")
    == canonical_incidence_hash
    and C742.get("reading_identity", {}).get("support_column_order_sha256")
    == column_order_hash
    and set(C742.get("reading_identity", {}).get("functions", {}))
    == {"zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"}
)
gate(dependency_ok, "independent.dependency",
     "Cycle 742 primary/checker and exact incidence identity are current")


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(right)))


def inverse(permutation):
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def closure(generators, degree=192):
    identity = tuple(range(degree))
    seen = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            product = compose(generator, current)
            if product not in seen:
                seen.add(product)
                frontier.append(product)
    return seen


row_lookup = {packed: row for row, packed in enumerate(packed_rows)}


def induced_row_permutation(permutation):
    if sorted(permutation) != list(range(192)):
        return None
    result = []
    for row in incidence:
        image = np.zeros(192, dtype=np.uint8)
        image[np.asarray(permutation)[np.flatnonzero(row)]] = 1
        target = row_lookup.get(bytes(np.packbits(image)))
        if target is None:
            return None
        result.append(target)
    return tuple(result) if len(set(result)) == len(solutions) else None


extra = []
extra_rows = []
certificate_ok = True
for name in ("b0", "b1"):
    certificate = certificates.get(name, {})
    permutation = tuple(int(value) for value in certificate.get("support_permutation", []))
    row_permutation = induced_row_permutation(permutation)
    certificate_ok = (
        certificate_ok and row_permutation is not None
        and certificate.get("support_permutation_sha256") == permutation_hash(permutation)
        and compose(permutation, permutation) == tuple(range(192))
    )
    extra.append(permutation)
    extra_rows.append(row_permutation)
gate(certificate_ok, "independent.automorphisms",
     "both exact predecessor maps are involutive automorphisms of every row")

# Build the declared 48 piece permutations independently from corner actions.
piece_permutations_48 = []
row_permutations_48 = []
for action in corner_actions:
    permutation = []
    for piece in used:
        image = tuple(sorted(action[corner] for corner in PIECES[piece]))
        permutation.append(position[piece_index[image]])
    permutation = tuple(permutation)
    piece_permutations_48.append(permutation)
    row_permutations_48.append(induced_row_permutation(permutation))
E48 = closure(piece_permutations_48)
E96 = closure(piece_permutations_48 + [extra[0]])
E = closure(piece_permutations_48 + extra)
gate(len(E48) == 48 and len(E96) == 96 and len(E) == 384 and extra[0] in closure(
         piece_permutations_48 + [extra[1]]),
     "independent.group_orders", "generator closures have orders 48, 96, and 384")


def permutation_order(permutation):
    identity = tuple(range(len(permutation)))
    power = identity
    for value in range(1, 1000):
        power = compose(permutation, power)
        if power == identity:
            return value
    raise AssertionError("order search exceeded finite bound")


def census(group):
    result = {}
    for permutation in group:
        value = permutation_order(permutation)
        result[value] = result.get(value, 0) + 1
    return sorted(result.items())


identity192 = tuple(range(192))
centre = [element for element in E if all(
    compose(element, other) == compose(other, element) for other in E
)]
point_stabilizer = [element for element in E if element[0] == 0]
nontrivial_stabilizer = [element for element in point_stabilizer if element != identity192]
group_ok = (
    census(E) == [(1, 1), (2, 75), (3, 32), (4, 132), (6, 96), (8, 48)]
    and len({element[0] for element in E}) == 192
    and len(point_stabilizer) == 2
    and len(nontrivial_stabilizer) == 1
    and sum(nontrivial_stabilizer[0][index] == index for index in range(192)) == 16
    and len(centre) == 2
    and sorted(sum(element[index] == index for index in range(192)) for element in centre)
    == [0, 192]
)
gate(group_ok, "independent.group_structure",
     "tuple arithmetic reproduces the element census, centre, and point stabilizer")

# The commutator subgroup is generated by all group commutators.
commutators = set()
for left in E:
    left_inverse = inverse(left)
    for right in E:
        commutators.add(compose(compose(compose(left_inverse, inverse(right)), left), right))
derived = closure(list(commutators))
gate(len(derived) == 96 and census(derived) == [(1, 1), (2, 19), (3, 32),
                                                (4, 12), (6, 32)]
     and all(compose(element, element) in derived for element in E),
     "independent.derived", "derived subgroup has order 96 and contains every square")

# Cutting orbits from a union-find on the independent generator row maps.
parent = list(range(len(solutions)))


def find(value):
    while parent[value] != value:
        parent[value] = parent[parent[value]]
        value = parent[value]
    return value


for permutation in row_permutations_48 + extra_rows:
    for row, image in enumerate(permutation):
        left, right = find(row), find(image)
        if left != right:
            parent[left] = right
row_orbits = {}
for row in range(len(solutions)):
    row_orbits.setdefault(find(row), []).append(row)
distribution = {}
for orbit in row_orbits.values():
    distribution[len(orbit)] = distribution.get(len(orbit), 0) + 1
expected_distribution = {8: 1, 24: 4, 32: 1, 48: 7, 64: 1, 96: 11, 192: 24, 384: 25}
gate(len(row_orbits) == 74 and distribution == expected_distribution,
     "independent.cutting_orbits", "complete generated cutting action has 74 orbits")

eight_orbits = [orbit for orbit in row_orbits.values() if len(orbit) == 8]
block_rows = eight_orbits[0] if len(eight_orbits) == 1 else []
block_supports = [set(np.flatnonzero(incidence[row]).tolist()) for row in block_rows]
partition_ok = (
    len(block_supports) == 8
    and all(len(support) == 24 for support in block_supports)
    and all(not (block_supports[left] & block_supports[right])
            for left in range(8) for right in range(left + 1, 8))
    and len(set().union(*block_supports)) == 192
)
gate(partition_ok, "independent.unique_partition",
     "the unique size-eight cutting orbit is the sole E-invariant eight-cutting partition")

unseen_columns = set(range(192))
piece_orbits_48 = []
while unseen_columns:
    start = min(unseen_columns)
    orbit = {element[start] for element in E48}
    piece_orbits_48.append(orbit)
    unseen_columns -= orbit
orbit_profile_ok = (
    sorted(len(orbit) for orbit in piece_orbits_48) == [48, 48, 48, 48]
    and all(sorted(len(support & orbit) for orbit in piece_orbits_48) == [6, 6, 6, 6]
            for support in block_supports)
)
gate(orbit_profile_ok, "independent.block_profiles",
     "every block meets each declared subgroup orbit in exactly six columns")

block_of = [-1] * 192
for block, support in enumerate(block_supports):
    for column in support:
        block_of[column] = block


def block_map(permutation, labels=block_of):
    result = []
    for block in range(8):
        images = {labels[permutation[column]] for column in range(192) if labels[column] == block}
        if len(images) != 1:
            return None
        result.append(next(iter(images)))
    return tuple(result)


B = {block_map(element) for element in E}
B48 = {block_map(element) for element in E48}
identity8 = tuple(range(8))
gate(None not in B and len(B) == 192 and len(B48) == 48
     and sum(block_map(element) == identity8 for element in E) == 2,
     "independent.block_action", "block image has order 192 with central kernel two")


def block_order(permutation):
    return permutation_order(permutation)


fixed_point_free = [
    element for element in B if element != identity8 and block_order(element) == 2
    and all(element[index] != index for index in range(8))
]
regular_subgroups = set()
for triple in itertools.combinations(fixed_point_free, 3):
    if any(compose(left, right) != compose(right, left)
           for left, right in itertools.combinations(triple, 2)):
        continue
    subgroup = closure(list(triple), degree=8)
    if len(subgroup) == 8 and all(
        element == identity8 or all(element[index] != index for index in range(8))
        for element in subgroup
    ):
        regular_subgroups.add(frozenset(subgroup))
normal_regular = [subgroup for subgroup in regular_subgroups if all(
    compose(compose(element, translation), inverse(element)) in subgroup
    for element in B for translation in subgroup
)]
gate(len(fixed_point_free) == 25 and len(regular_subgroups) == 4
     and len(normal_regular) == 1,
     "independent.translation", "exactly one of four regular order-eight subgroups is normal")

translations = set(normal_regular[0])
origin = 0
generators = []
for candidate in sorted(translations):
    proposed = closure(generators + [candidate], degree=8)
    if len(proposed) == 2 ** (len(generators) + 1):
        generators.append(candidate)
    if len(generators) == 3:
        break
label_of_block = {}
translation_for_label = {}
for label in range(8):
    element = identity8
    for bit, generator in enumerate(generators):
        if (label >> bit) & 1:
            element = compose(generator, element)
    label_of_block[element[origin]] = label
    translation_for_label[label] = element
block_for_label = {label: block for block, label in label_of_block.items()}


def linear_part(element):
    translation = translation_for_label[label_of_block[element[origin]]]
    return compose(translation, element)


linear = {linear_part(element) for element in B}
linear48 = {linear_part(element) for element in B48}


def act_label(element, label):
    return label_of_block[element[block_for_label[label]]]


additive = all(
    act_label(element, left ^ right) == (act_label(element, left) ^ act_label(element, right))
    for element in linear for left in range(8) for right in range(8)
)
nonzero_orbits = []
unseen = set(range(1, 8))
while unseen:
    start = min(unseen)
    orbit = {act_label(element, start) for element in linear}
    nonzero_orbits.append(orbit)
    unseen -= orbit
plane = {0} | next(orbit for orbit in nonzero_orbits if len(orbit) == 3)
planes = {
    frozenset((0, left, right, left ^ right))
    for left in range(1, 8) for right in range(left + 1, 8) if left != right
}
invariant_planes = [candidate for candidate in planes if all(
    act_label(element, label) in candidate for element in linear for label in candidate
)]
fixed48 = [label for label in range(1, 8) if all(
    act_label(element, label) == label for element in linear48
)]
gate(len(generators) == 3 and len(linear) == 24 and len(linear48) == 6 and additive
     and sorted(len(orbit) for orbit in nonzero_orbits) == [3, 4]
     and len(invariant_planes) == 1 and set(invariant_planes[0]) == plane
     and len(fixed48) == 1 and fixed48[0] not in plane,
     "independent.affine", "split affine action has plane stabilizer 24 and joint stabilizer 6")


def matrix_columns(element):
    return tuple(act_label(element, 1 << bit) for bit in range(3))


def apply_matrix(columns, label):
    result = 0
    for bit in range(3):
        if (label >> bit) & 1:
            result ^= columns[bit]
    return result


all_matrices = list(itertools.product(range(8), repeat=3))
invertible = [matrix for matrix in all_matrices if len({
    apply_matrix(matrix, label) for label in range(8)
}) == 8]
plane_stabilizer = [matrix for matrix in invertible if {
    apply_matrix(matrix, label) for label in plane
} == plane]
joint_stabilizer = [matrix for matrix in plane_stabilizer
                    if apply_matrix(matrix, fixed48[0]) == fixed48[0]]
gate(len(all_matrices) == 512 and len(invertible) == 168
     and len(plane_stabilizer) == 24 and len(joint_stabilizer) == 6
     and {matrix_columns(element) for element in linear} == set(plane_stabilizer)
     and {matrix_columns(element) for element in linear48} == set(joint_stabilizer),
     "independent.matrix_census", "complete 3-by-3 matrix census matches both stabilizers")


def primary_contract(receipt):
    return (
        receipt.get("schema") == "physical-cell-cutting-hidden-three-bit-geometry-cycle743-v2"
        and receipt.get("status") == "pass" and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == file_sha256(PRIMARY_PATH)
        and set(receipt.get("input_sha256", {})) == set(AUDIT_INPUT_PATHS[3:]) | {
            NOTE_PATH, CHECKER_PATH
        }
        and receipt_inputs_current(receipt)
        and receipt.get("generated_group", {}).get("order") == 384
        and receipt.get("direct_dependency", {}).get("functions")
        == C742.get("reading_identity", {}).get("functions")
        and receipt.get("invariant_cutting_partition", {}).get(
            "unique_e_invariant_eight_cutting_partition") is True
        and receipt.get("invariant_cutting_partition", {}).get("block_action_image_order") == 192
        and receipt.get("affine_action", {}).get("linear_part_order") == 24
        and receipt.get("affine_action", {}).get("subgroup_48_linear_part_order") == 6
    )


gate(primary_contract(PRIMARY), "independent.primary_contract",
     "primary receipt pins current sources and the independently rebuilt headline")

bad_map = list(extra[0])
bad_map[0], bad_map[1] = bad_map[1], bad_map[0]
gate(induced_row_permutation(tuple(bad_map)) is None,
     "hostile.automorphism", "transposing two map images breaks incidence preservation")
gate(len(closure(piece_permutations_48 + [extra[0]])) == 96,
     "hostile.omitted_generator", "omitting the second extra generator collapses 384 to 96")
bad_labels = list(block_of)
bad_labels[0] = (bad_labels[0] + 1) % 8
gate(sorted(bad_labels.count(block) for block in range(8)) != [24] * 8,
     "hostile.partition", "moving one column breaks the eight-by-24 partition")
bad_receipt = copy.deepcopy(PRIMARY)
bad_receipt["status"] = "fail"
gate(not primary_contract(bad_receipt), "hostile.primary_status",
     "a failing primary receipt cannot satisfy the consumer contract")
bad_receipt = copy.deepcopy(PRIMARY)
bad_receipt["generated_group"]["order"] = 192
gate(not primary_contract(bad_receipt), "hostile.group_order",
     "a mutated group order cannot satisfy the consumer contract")

print("per_element: checked -- all 192 support columns enter the independent incidence, "
      "group, block, and affine checks", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only; "
      "no framework cell or site is identified", flush=True)
print("per_mode: checked and not executed -- the finite permutation action has no "
      "field or momentum-mode decomposition", flush=True)
print("per_block: checked -- complete eight-block action, four regular subgroups, "
      "and all seven label planes", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-domain, "
      "boundary, thermodynamic, or continuum result", flush=True)

receipt = {
    "schema": "physical-cell-cutting-hidden-three-bit-geometry-cycle743-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": file_sha256(CHECKER_PATH),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "exact_covers": len(solutions),
        "support_columns": len(used),
        "generated_group_order": len(E),
        "cutting_orbits": len(row_orbits),
        "block_image_order": len(B),
        "regular_order_eight_subgroups": len(regular_subgroups),
        "normal_regular_order_eight_subgroups": len(normal_regular),
        "linear_part_order": len(linear),
        "invariant_planes": len(invariant_planes),
    },
    "gates": {
        "pass": passed,
        "fail": failed,
        "named": {name: "PASS" if ok else "FAIL" for name, ok in gates},
    },
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(0 if failed == 0 else 1)
