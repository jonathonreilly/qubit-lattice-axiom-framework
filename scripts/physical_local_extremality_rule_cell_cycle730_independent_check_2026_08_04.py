"""Independent exact reconstruction for the Cycle 730 finite support census.

This checker never imports or executes the primary.  It reads the primary AST
only for its carried integer certificate literals, reconstructs the geometry,
group action, sample incidence, and slacks with separate routines, validates
every landed realization/orphan certificate, and reruns the two ceiling
exhaustions from the opposite end of the point order.
"""

import ast
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "scripts/physical_local_extremality_rule_cell_cycle730_2026_08_04.py",
    "outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_"
    "receipt_2026-08-04.json",
)
ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ROOT / AUDIT_INPUT_PATHS[0]
RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8"))
GATES = []


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("{0} {1:52s} {2}".format("PASS" if ok else "FAIL", name, detail), flush=True)


def determinant(matrix):
    """Exact Leibniz determinant for order at most four."""
    if len(matrix) == 1:
        return matrix[0][0]
    total = 0
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[a] > permutation[b]
            for a in range(len(matrix))
            for b in range(a + 1, len(matrix))
        )
        term = -1 if inversions & 1 else 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def exact_inverse(matrix):
    """Exact inverse of a determinant-plus/minus-one integer matrix."""
    source = matrix.tolist()
    divisor = determinant(source)
    inverse = []
    for row in range(4):
        result_row = []
        for column in range(4):
            minor = [
                values[:row] + values[row + 1 :]
                for source_row, values in enumerate(source)
                if source_row != column
            ]
            result_row.append(((-1) ** (row + column)) * determinant(minor) // divisor)
        inverse.append(result_row)
    return np.array(inverse, dtype=np.int64)


def primary_literals():
    wanted = {"FLOOR_U", "FLOOR_D", "FLOOR_Z", "CEIL_U", "CEIL_D", "CEIL_Z"}
    found = {}
    tree = ast.parse(PRIMARY.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            found[target.id] = ast.literal_eval(node.value)
        elif isinstance(target, ast.Tuple):
            names = [item.id for item in target.elts if isinstance(item, ast.Name)]
            if names and all(name in wanted for name in names):
                values = ast.literal_eval(node.value)
                found.update(zip(names, values))
    return found


LITERALS = primary_literals()
gate("all certificate literals parsed", len(LITERALS) == 6, str(sorted(LITERALS)))

CORNERS = [tuple(bits) for bits in itertools.product((0, 1), repeat=4)]
CORNER_ARRAY = np.array(CORNERS, dtype=np.int64)
POSITION = {corner: index for index, corner in enumerate(CORNERS)}
PIECES = []
INVERSES = []
VOLUME_SPECTRUM = {}
for piece in itertools.combinations(range(16), 5):
    vertices = CORNER_ARRAY[list(piece)]
    matrix = (vertices[1:] - vertices[0]).T
    volume = abs(determinant(matrix.tolist()))
    VOLUME_SPECTRUM[volume] = VOLUME_SPECTRUM.get(volume, 0) + 1
    if volume == 1:
        PIECES.append(tuple(piece))
        INVERSES.append(exact_inverse(matrix))

PIECE_POSITION = {piece: index for index, piece in enumerate(PIECES)}
PIECE_VERTICES = CORNER_ARRAY[np.array(PIECES, dtype=np.int64)]
INVERSES = np.array(INVERSES, dtype=np.int64)
PAIRS = list(itertools.combinations(range(5), 2))
CHARGE = np.array(
    [
        sum(
            sum(abs(CORNERS[piece[a]][axis] - CORNERS[piece[b]][axis]) for axis in range(3))
            > 1
            for a, b in PAIRS
        )
        for piece in PIECES
    ],
    dtype=np.int64,
)
gate(
    "independent piece and charge census",
    VOLUME_SPECTRUM == {0: 1360, 1: 2672, 2: 320, 3: 16}
    and dict(zip(*np.unique(CHARGE, return_counts=True)))
    == {3: 64, 4: 384, 5: 1152, 6: 768, 7: 304},
    "volume {0}; pieces {1}".format(sorted(VOLUME_SPECTRUM.items()), len(PIECES)),
)


def permutation_sign(permutation):
    return -1 if sum(
        permutation[a] > permutation[b]
        for a in range(len(permutation))
        for b in range(a + 1, len(permutation))
    ) & 1 else 1


ROTATIONS = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
            continue
        matrix = np.zeros((3, 3), dtype=np.int64)
        for row, column in enumerate(permutation):
            matrix[row, column] = signs[row]
        ROTATIONS.append(matrix)

GROUP = []
center = np.ones(3, dtype=np.int64)
for rotation in ROTATIONS:
    for tick_flip in (0, 1):
        image = []
        for x, y, z, tick in CORNERS:
            spatial = rotation @ (2 * np.array((x, y, z), dtype=np.int64) - center) + center
            target = (
                int(spatial[0]) // 2,
                int(spatial[1]) // 2,
                int(spatial[2]) // 2,
                1 - tick if tick_flip else tick,
            )
            image.append(POSITION[target])
        GROUP.append((rotation, tick_flip, image))

LABELS = [-1] * len(PIECES)
REPRESENTATIVES = []
for piece_index, piece in enumerate(PIECES):
    if LABELS[piece_index] >= 0:
        continue
    orbit = len(REPRESENTATIVES)
    REPRESENTATIVES.append(piece_index)
    for _, _, image in GROUP:
        transformed = tuple(sorted(image[corner] for corner in piece))
        LABELS[PIECE_POSITION[transformed]] = orbit
LABELS = np.array(LABELS, dtype=np.int64)
gate(
    "independent 48-map orbit reconstruction",
    len(GROUP) == 48
    and len(REPRESENTATIVES) == 57
    and set(np.bincount(LABELS).tolist()) == {16, 48}
    and all(len(set(CHARGE[LABELS == orbit].tolist())) == 1 for orbit in range(57)),
    "piece orbits 57 of sizes {0}".format(sorted(set(np.bincount(LABELS).tolist()))),
)

OFFSETS = np.array([0, 1, 7, 49, 343], dtype=np.int64)
WEIGHTS = 2 * (3 * int(OFFSETS.sum()) + 1 + OFFSETS)
SCALE = int(WEIGHTS.sum())
spatial_center = np.array([SCALE // 2] * 3, dtype=np.int64)
sample_labels = {}
for orbit, piece_index in enumerate(REPRESENTATIVES):
    seed = (WEIGHTS[:, None] * PIECE_VERTICES[piece_index]).sum(axis=0)
    for rotation, tick_flip, _ in GROUP:
        spatial = rotation @ (seed[:3] - spatial_center) + spatial_center
        point = (
            int(spatial[0]),
            int(spatial[1]),
            int(spatial[2]),
            SCALE - int(seed[3]) if tick_flip else int(seed[3]),
        )
        sample_labels.setdefault(point, orbit)
SAMPLES = np.array(sorted(sample_labels), dtype=np.int64)
POINT_ORBITS = np.array([sample_labels[tuple(point)] for point in SAMPLES], dtype=np.int64)

INCIDENCE = np.zeros((len(PIECES), len(SAMPLES)), dtype=bool)
boundary = 0
for piece_index, piece in enumerate(PIECES):
    numerators = INVERSES[piece_index] @ (
        SAMPLES.T - SCALE * CORNER_ARRAY[piece[0]][:, None]
    )
    remainder = SCALE - numerators.sum(axis=0)
    boundary += int(((numerators == 0).any(axis=0) | (remainder == 0)).sum())
    INCIDENCE[piece_index] = (numerators > 0).all(axis=0) & (remainder > 0)
gate(
    "independent generic-sample reconstruction",
    len(SAMPLES) == 2736 and boundary == 0 and SCALE == 12810,
    "points {0}, boundary incidences {1}".format(len(SAMPLES), boundary),
)

MEMBERSHIP = np.zeros((len(PIECES), len(REPRESENTATIVES)), dtype=np.int64)
for piece_index in range(len(PIECES)):
    MEMBERSHIP[piece_index] = np.bincount(
        POINT_ORBITS[INCIDENCE[piece_index]], minlength=len(REPRESENTATIVES)
    )
POINT_COUNTS = np.bincount(POINT_ORBITS, minlength=len(REPRESENTATIVES))


def certificate_slacks(name, upper=False):
    vector = np.zeros(len(REPRESENTATIVES), dtype=np.int64)
    for orbit, value in LITERALS[name + "_U"]:
        vector[orbit] = value
    denominator = LITERALS[name + "_D"]
    offset = LITERALS[name + "_Z"]
    raw = MEMBERSHIP @ vector + offset - denominator * CHARGE
    return (raw if upper else -raw), vector


FLOOR_SLACK, FLOOR_VECTOR = certificate_slacks("FLOOR")
CEILING_SLACK, CEILING_VECTOR = certificate_slacks("CEIL", upper=True)
gate(
    "independent exact zero-gap certificates",
    int(FLOOR_SLACK.min()) == 0
    and int(CEILING_SLACK.min()) == 0
    and int(POINT_COUNTS @ FLOOR_VECTOR) == 24 * 108
    and int(POINT_COUNTS @ CEILING_VECTOR) == 6 * 128
    and int((FLOOR_SLACK == 0).sum()) == 2416
    and int((CEILING_SLACK == 0).sum()) == 1040,
    "tight pieces floor {0}, ceiling {1}".format(
        int((FLOOR_SLACK == 0).sum()), int((CEILING_SLACK == 0).sum())
    ),
)

TERNARY_DIRECTIONS = [
    np.array(direction, dtype=np.int64)
    for direction in itertools.product((-1, 0, 1), repeat=4)
    if any(direction)
]


def facet_normals(piece_index):
    inverse = INVERSES[piece_index]
    return [inverse[row] for row in range(4)] + [-inverse.sum(axis=0)]


def separated(left, right):
    left_vertices = PIECE_VERTICES[left]
    right_vertices = PIECE_VERTICES[right]
    for normal in TERNARY_DIRECTIONS + facet_normals(left) + facet_normals(right):
        left_projection = left_vertices @ normal
        right_projection = right_vertices @ normal
        if int(left_projection.max()) <= int(right_projection.min()):
            return True
        if int(right_projection.max()) <= int(left_projection.min()):
            return True
    return False


ALL_POINTS = (1 << len(SAMPLES)) - 1
MASKS = []
for row in INCIDENCE:
    mask = 0
    for point in np.flatnonzero(row):
        mask |= 1 << int(point)
    MASKS.append(mask)


def valid_dissection(witness, target, slacks):
    if len(witness) != 24 or len(set(witness)) != 24:
        return False
    if sum(int(CHARGE[piece]) for piece in witness) != target:
        return False
    if any(int(slacks[piece]) != 0 for piece in witness):
        return False
    covered = 0
    for piece in witness:
        if covered & MASKS[piece]:
            return False
        covered |= MASKS[piece]
    if covered != ALL_POINTS:
        return False
    return all(separated(left, right) for left, right in itertools.combinations(witness, 2))


support = RECEIPT["support"]
for endpoint, target, slacks in (
    ("floor", 108, FLOOR_SLACK),
    ("ceiling", 128, CEILING_SLACK),
):
    witnesses = support[endpoint]["realization_witnesses"]
    unique = {tuple(value) for value in witnesses.values()}
    all_valid = all(valid_dissection(list(witness), target, slacks) for witness in unique)
    covered_orbits = set()
    for witness in unique:
        covered_orbits.update(int(LABELS[piece]) for piece in witness)
    gate(
        "independent {0} realization witnesses".format(endpoint),
        all_valid
        and covered_orbits == set(support[endpoint]["realized_orbits"])
        and set(map(int, witnesses)) == covered_orbits,
        "{0} geometric witnesses cover {1} orbits".format(len(unique), len(covered_orbits)),
    )

floor_pool = np.flatnonzero(FLOOR_SLACK == 0)
pruning = support["floor"]["pruning_certificates"]
pruning_ok = True
for orbit_text, certificate in pruning.items():
    orbit = int(orbit_text)
    forced = certificate["forced_piece"]
    point = certificate["orphan_point"]
    holders = [piece for piece in floor_pool if INCIDENCE[piece, point]]
    pruning_ok &= int(LABELS[forced]) == orbit and FLOOR_SLACK[forced] == 0
    pruning_ok &= not INCIDENCE[forced, point] and bool(holders)
    pruning_ok &= all(bool((INCIDENCE[piece] & INCIDENCE[forced]).any()) for piece in holders)
gate(
    "independent floor orphan certificates",
    pruning_ok and set(map(int, pruning)) == set(support["floor"]["excluded_orbits"]),
    "{0} orbit certificates".format(len(pruning)),
)


def reverse_forced_cover(pool, forced, cap):
    """Independent DFS choosing the greatest uncovered sample index."""
    by_last = [[] for _ in range(len(SAMPLES))]
    for piece in pool:
        by_last[MASKS[piece].bit_length() - 1].append(int(piece))
    nodes = [0]

    def recurse(covered):
        nodes[0] += 1
        if nodes[0] > cap:
            return "unsettled"
        if covered == ALL_POINTS:
            return "occurs"
        point = ((~covered & ALL_POINTS).bit_length() - 1)
        for piece in by_last[point]:
            if MASKS[piece] & covered:
                continue
            status = recurse(covered | MASKS[piece])
            if status != "absent":
                return status
        return "absent"

    return recurse(MASKS[forced]), nodes[0]


ceiling_pool = np.flatnonzero(CEILING_SLACK == 0)
reverse_results = {}
for orbit_text, certificate in support["ceiling"]["search_certificates"].items():
    status, nodes = reverse_forced_cover(ceiling_pool, certificate["forced_piece"], 20000000)
    reverse_results[int(orbit_text)] = (status, nodes)
gate(
    "independent reverse-order ceiling exhaustion",
    set(reverse_results) == set(support["ceiling"]["excluded_orbits"])
    and all(status == "absent" for status, _ in reverse_results.values()),
    str(reverse_results),
)

# Hostile semantic controls: each mutation must destroy the corresponding certificate.
mutated_floor = FLOOR_VECTOR.copy()
mutated_floor[LITERALS["FLOOR_U"][0][0]] += 1
mutated_floor_slack = -(MEMBERSHIP @ mutated_floor - LITERALS["FLOOR_D"] * CHARGE)
gate(
    "hostile floor-weight mutation is rejected",
    int(mutated_floor_slack.min()) < 0,
    "least mutated slack {0}".format(int(mutated_floor_slack.min())),
)

ceiling_mutation = None
for orbit, _ in LITERALS["CEIL_U"]:
    for delta in (-1, 1):
        candidate = CEILING_VECTOR.copy()
        candidate[orbit] += delta
        candidate_slack = MEMBERSHIP @ candidate - LITERALS["CEIL_D"] * CHARGE
        if int(candidate_slack.min()) < 0:
            ceiling_mutation = (orbit, delta, int(candidate_slack.min()))
            break
    if ceiling_mutation is not None:
        break
gate(
    "hostile ceiling-weight mutation is rejected",
    ceiling_mutation is not None,
    "breaking mutation {0}".format(ceiling_mutation),
)

first_floor_witness = list(next(iter(support["floor"]["realization_witnesses"].values())))
first_floor_witness[0] = next(iter(pruning.values()))["forced_piece"]
gate(
    "hostile realization-witness mutation is rejected",
    not valid_dissection(first_floor_witness, 108, FLOOR_SLACK),
    "excluded forced piece substituted into a floor witness",
)

mutated_orphan_ok = False
first_certificate = next(iter(pruning.values()))
forced = first_certificate["forced_piece"]
for point in np.flatnonzero(~INCIDENCE[forced]):
    holders = [piece for piece in floor_pool if INCIDENCE[piece, point]]
    if holders and not all(bool((INCIDENCE[piece] & INCIDENCE[forced]).any()) for piece in holders):
        mutated_orphan_ok = True
        break
gate(
    "hostile orphan-point mutation is rejected",
    mutated_orphan_ok,
    "a noncertificate point leaves a compatible carrier",
)

mutated_charge = np.array(
    [
        sum(
            sum(abs(CORNERS[piece[a]][axis] - CORNERS[piece[b]][axis]) for axis in range(3))
            > 2
            for a, b in PAIRS
        )
        for piece in PIECES
    ],
    dtype=np.int64,
)
gate(
    "hostile charge-threshold mutation is rejected",
    not np.array_equal(mutated_charge, CHARGE)
    and int((-(MEMBERSHIP @ FLOOR_VECTOR - 24 * mutated_charge)).min()) < 0,
    "mutated charge range {0}".format(sorted(set(mutated_charge.tolist()))),
)

expected_partition = {
    "floor": (38, 13, 51),
    "ceiling": (21, 2, 23),
}
partition_ok = all(
    len(support[name]["realized_orbits"]) == expected[0]
    and len(support[name]["excluded_orbits"]) == expected[1]
    and not (set(support[name]["realized_orbits"]) & set(support[name]["excluded_orbits"]))
    and len(set(support[name]["realized_orbits"]) | set(support[name]["excluded_orbits"]))
    == expected[2]
    for name, expected in expected_partition.items()
)
gate("support partitions are exact and disjoint", partition_ok, str(expected_partition))

passed = sum(ok for _, ok in GATES)
failed = len(GATES) - passed
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(1 if failed else 0)
