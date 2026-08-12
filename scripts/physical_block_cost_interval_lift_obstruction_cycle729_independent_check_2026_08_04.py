"""Independent exact checker for the supplied finite Cycle 729 theorem.

This file never imports or executes the primary runner.  It parses only carried literals
from the primary and Cycle 728, then reconstructs the cell census, proper-spatial symmetry,
sample-point loads, certificate inequalities, witness covers, charges, and lower-hull
comparators with separate exact algorithms.  A broader primitive-normal sweep supplies an
independent separator route for every witness pair.
"""

import ast
import itertools
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 300
PRIMARY_PATH = (
    "scripts/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04.py"
)
C728_RUNNER_PATH = (
    "scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04.py",
    "scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py",
)
ROOT = Path(__file__).resolve().parents[1]
GATES = []


def gate(name, ok, detail=""):
    """Record one deterministic fail-closed check."""
    GATES.append((name, bool(ok)))
    print(
        "{0} {1:52s} {2}".format("PASS" if ok else "FAIL", name, detail),
        flush=True,
    )


def carried_literals(path, names):
    """Parse selected top-level literal assignments without executing a runner."""
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    found = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in names:
            found[target.id] = ast.literal_eval(node.value)
    if set(found) != set(names):
        raise ValueError("missing literals: {0}".format(sorted(set(names) - set(found))))
    return found


def determinant(matrix):
    """Exact recursive determinant, used only through order four."""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** column
        * matrix[0][column]
        * determinant([row[:column] + row[column + 1 :] for row in matrix[1:]])
        for column in range(len(matrix))
    )


def exact_inverse(matrix):
    """Exact integer inverse of a determinant-plus/minus-one matrix."""
    divisor = determinant(matrix)
    if abs(divisor) != 1:
        raise ValueError("matrix is not unimodular")
    return [
        [
            ((-1) ** (row + column))
            * determinant(
                [
                    source[:row] + source[row + 1 :]
                    for source_index, source in enumerate(matrix)
                    if source_index != column
                ]
            )
            // divisor
            for column in range(4)
        ]
        for row in range(4)
    ]


WANTED = {
    "FLOOR_U", "FLOOR_Z", "FLOOR_D", "FLOOR_VAL",
    "CEIL_U", "CEIL_Z", "CEIL_D", "CEIL_VAL",
    "DEAR", "PRIOR", "HGT_LO", "HGT_PR",
}
DATA = carried_literals(PRIMARY_PATH, WANTED)
C728 = carried_literals(C728_RUNNER_PATH, {"BLOCK_HI"})
gate(
    "independent Cycle 728 witness binding",
    DATA["PRIOR"] == C728["BLOCK_HI"],
    "Cycle 729 PRIOR equals Cycle 728 BLOCK_HI entry by entry",
)


CORNERS = [
    (x, y, z, tick)
    for x in range(3)
    for y in range(2)
    for z in range(2)
    for tick in range(2)
]
CORNER_ARRAY = np.array(CORNERS, dtype=np.int64)


def edge_matrix(cell):
    """Four-by-four matrix with simplex edge vectors as columns."""
    base = CORNERS[cell[0]]
    return [
        [CORNERS[cell[column + 1]][axis] - base[axis] for column in range(4)]
        for axis in range(4)
    ]


def volume(cell):
    return abs(determinant(edge_matrix(cell)))


def charge(cell, axes=(0, 1, 2)):
    return sum(
        sum(abs(CORNERS[left][axis] - CORNERS[right][axis]) for axis in axes) > 1
        for left, right in itertools.combinations(cell, 2)
    )


SUBSETS = list(itertools.combinations(range(24), 5))
VOLUMES = [volume(cell) for cell in SUBSETS]
CELLS = [cell for cell, cell_volume in zip(SUBSETS, VOLUMES) if cell_volume == 1]
CHARGES = np.array([charge(cell) for cell in CELLS], dtype=np.int64)
gate(
    "independent block cell census",
    len(SUBSETS) == 42504
    and Counter(VOLUMES) == {0: 13152, 1: 17280, 2: 9840, 3: 1472, 4: 680, 5: 64, 6: 16},
    "subsets {0}; unit cells {1}; spectrum {2}".format(
        len(SUBSETS), len(CELLS), sorted(Counter(VOLUMES).items())
    ),
)
gate(
    "independent charge spectrum",
    Counter(CHARGES.tolist()) == {3: 128, 4: 768, 5: 2816, 6: 4928,
                                  7: 5760, 8: 2608, 9: 272},
    str(sorted(Counter(CHARGES.tolist()).items())),
)


def permutation_parity(permutation):
    inversions = sum(
        permutation[left] > permutation[right]
        for left, right in itertools.combinations(range(3), 2)
    )
    return -1 if inversions & 1 else 1


def spatial_matrix(permutation, signs):
    matrix = [[0, 0, 0] for _ in range(3)]
    for row, column in enumerate(permutation):
        matrix[row][column] = signs[row]
    return matrix


def matvec(matrix, vector):
    return [sum(row[column] * vector[column] for column in range(len(vector))) for row in matrix]


POSITION = {corner: index for index, corner in enumerate(CORNERS)}
CENTER2 = [2, 1, 1]
GROUP = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((-1, 1), repeat=3):
        if permutation_parity(permutation) * math.prod(signs) != 1:
            continue
        rotation = spatial_matrix(permutation, signs)
        for tick_flip in (False, True):
            image = []
            for corner in CORNERS:
                shifted = [2 * corner[axis] - CENTER2[axis] for axis in range(3)]
                transformed2 = [
                    value + CENTER2[axis]
                    for axis, value in enumerate(matvec(rotation, shifted))
                ]
                if any(value & 1 for value in transformed2):
                    image = None
                    break
                transformed = tuple(value // 2 for value in transformed2) + (
                    1 - corner[3] if tick_flip else corner[3],
                )
                if transformed not in POSITION:
                    image = None
                    break
                image.append(POSITION[transformed])
            if image is not None:
                GROUP.append((rotation, tick_flip, tuple(image)))
gate("independent supplied block symmetry", len(GROUP) == 16, "group order {0}".format(len(GROUP)))


CELL_POSITION = {cell: index for index, cell in enumerate(CELLS)}
LABELS = [-1] * len(CELLS)
REPRESENTATIVES = []
for index, cell in enumerate(CELLS):
    if LABELS[index] >= 0:
        continue
    orbit = len(REPRESENTATIVES)
    REPRESENTATIVES.append(index)
    for _, _, image in GROUP:
        transformed = tuple(sorted(image[vertex] for vertex in cell))
        LABELS[CELL_POSITION[transformed]] = orbit
ORBIT_SIZES = Counter(LABELS)
gate(
    "independent piece-orbit census",
    len(REPRESENTATIVES) == 1080 and set(ORBIT_SIZES.values()) == {16},
    "orbits {0}; sizes {1}".format(len(REPRESENTATIVES), sorted(set(ORBIT_SIZES.values()))),
)


WEIGHTS = [4802, 4804, 4816, 4900, 5488]
SCALE = sum(WEIGHTS)
POINT_TO_ORBIT = {}
for orbit, representative in enumerate(REPRESENTATIVES):
    cell = CELLS[representative]
    point = [
        sum(WEIGHTS[slot] * CORNERS[vertex][axis] for slot, vertex in enumerate(cell))
        for axis in range(4)
    ]
    for rotation, tick_flip, _ in GROUP:
        centered2 = [2 * point[axis] - SCALE * CENTER2[axis] for axis in range(3)]
        rotated2 = [
            value + SCALE * CENTER2[axis]
            for axis, value in enumerate(matvec(rotation, centered2))
        ]
        if any(value & 1 for value in rotated2):
            raise AssertionError("nonintegral transformed sample point")
        transformed = tuple(value // 2 for value in rotated2) + (
            SCALE - point[3] if tick_flip else point[3],
        )
        if transformed in POINT_TO_ORBIT and POINT_TO_ORBIT[transformed] != orbit:
            raise AssertionError("sample-point orbit collision")
        POINT_TO_ORBIT[transformed] = orbit
POINTS = np.array(sorted(POINT_TO_ORBIT), dtype=np.int64)
POINT_ORBITS = np.array([POINT_TO_ORBIT[tuple(point)] for point in POINTS], dtype=np.int64)
gate(
    "independent generic sample family",
    len(POINTS) == 17280
    and set(Counter(POINT_ORBITS.tolist()).values()) == {16},
    "points {0}; orbit multiplicity 16".format(len(POINTS)),
)


floor_slacks = []
ceiling_slacks = []
boundary_hits = 0
floor_weights = np.array(DATA["FLOOR_U"], dtype=np.int64)
ceiling_weights = np.array(DATA["CEIL_U"], dtype=np.int64)
for cell, cell_charge in zip(CELLS, CHARGES):
    inverse = np.array(exact_inverse(edge_matrix(cell)), dtype=np.int64)
    displacement = POINTS.T - SCALE * CORNER_ARRAY[cell[0]][:, None]
    numerators = inverse @ displacement
    total = numerators.sum(axis=0)
    boundary_hits += int(((numerators == 0).any(axis=0) | (total == SCALE)).sum())
    interior = (numerators > 0).all(axis=0) & (total < SCALE)
    floor_load = int(floor_weights[POINT_ORBITS[interior]].sum())
    ceiling_load = int(ceiling_weights[POINT_ORBITS[interior]].sum())
    floor_slacks.append(DATA["FLOOR_D"] * int(cell_charge) - floor_load - DATA["FLOOR_Z"])
    ceiling_slacks.append(ceiling_load + DATA["CEIL_Z"] - DATA["CEIL_D"] * int(cell_charge))

floor_numerator = 16 * sum(DATA["FLOOR_U"]) + 48 * DATA["FLOOR_Z"]
ceiling_numerator = 16 * sum(DATA["CEIL_U"]) + 48 * DATA["CEIL_Z"]
gate(
    "independent exact floor certificate",
    boundary_hits == 0
    and min(floor_slacks) == 0
    and floor_slacks.count(0) == 480
    and floor_numerator == DATA["FLOOR_VAL"]
    and -((-floor_numerator) // DATA["FLOOR_D"]) == 216,
    "least slack {0}; tight pieces {1}; numerator {2}/{3}".format(
        min(floor_slacks), floor_slacks.count(0), floor_numerator, DATA["FLOOR_D"]
    ),
)
gate(
    "independent exact ceiling certificate",
    boundary_hits == 0
    and min(ceiling_slacks) == 0
    and ceiling_slacks.count(0) == 848
    and ceiling_numerator == DATA["CEIL_VAL"]
    and ceiling_numerator // DATA["CEIL_D"] == 320,
    "least slack {0}; tight pieces {1}; numerator {2}/{3}".format(
        min(ceiling_slacks), ceiling_slacks.count(0), ceiling_numerator, DATA["CEIL_D"]
    ),
)


def kuhn(base):
    out = []
    for permutation in itertools.permutations(range(4)):
        vertex = list(base)
        path = [POSITION[tuple(vertex)]]
        for axis in permutation:
            vertex[axis] += 1
            path.append(POSITION[tuple(vertex)])
        out.append(tuple(sorted(path)))
    return sorted(out)


STENCIL = kuhn((0, 0, 0, 0)) + kuhn((1, 0, 0, 0))
DEAREST = [tuple(row) for row in DATA["DEAR"]]
PRIOR = [tuple(row) for row in DATA["PRIOR"]]


NORMALS = set()
for normal in itertools.product(range(-4, 5), repeat=4):
    if not any(normal):
        continue
    divisor = 0
    for value in normal:
        divisor = math.gcd(divisor, abs(value))
    primitive = tuple(value // divisor for value in normal)
    first = next(value for value in primitive if value)
    if first < 0:
        primitive = tuple(-value for value in primitive)
    NORMALS.add(primitive)
NORMAL_ARRAY = np.array(sorted(NORMALS), dtype=np.int64)


def separator_count(witness):
    """Count pairs weakly separated by a primitive normal in [-4,4]^4."""
    separated = 0
    for left, right in itertools.combinations(range(len(witness)), 2):
        left_values = CORNER_ARRAY[list(witness[left])] @ NORMAL_ARRAY.T
        right_values = CORNER_ARRAY[list(witness[right])] @ NORMAL_ARRAY.T
        margin = np.maximum(
            right_values.min(axis=0) - left_values.max(axis=0),
            left_values.min(axis=0) - right_values.max(axis=0),
        )
        separated += bool((margin >= 0).any())
    return separated


def witness_summary(witness):
    return (
        len(witness),
        sum(volume(cell) for cell in witness),
        sum(charge(cell) for cell in witness),
        separator_count(witness),
    )


SUMMARIES = {
    "stencil": witness_summary(STENCIL),
    "cycle728": witness_summary(PRIOR),
    "cost320": witness_summary(DEAREST),
}
gate(
    "independent exact witness covers and costs",
    SUMMARIES == {
        "stencil": (48, 48, 216, 1128),
        "cycle728": (48, 48, 318, 1128),
        "cost320": (48, 48, 320, 1128),
    },
    str(SUMMARIES),
)


BOUNDARY_FACES = [(0, 0), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]


def internal_unpaired_facets(witness):
    facets = Counter(
        face
        for cell in witness
        for face in itertools.combinations(sorted(cell), 4)
    )
    return [
        face
        for face, multiplicity in facets.items()
        if multiplicity == 1
        and not any(
            all(CORNERS[vertex][axis] == value for vertex in face)
            for axis, value in BOUNDARY_FACES
        )
    ]


def lower_hull_margin(witness, heights):
    """Minimum exact height-minus-supporting-plane margin at outside corners."""
    margins = []
    for cell in witness:
        inverse = np.array(exact_inverse(edge_matrix(cell)), dtype=np.int64)
        height_differences = np.array(
            [heights[vertex] - heights[cell[0]] for vertex in cell[1:]],
            dtype=np.int64,
        )
        for vertex in range(24):
            if vertex in cell:
                continue
            displacement = CORNER_ARRAY[vertex] - CORNER_ARRAY[cell[0]]
            barycentric = inverse @ displacement
            plane_height = int(heights[cell[0]] + height_differences @ barycentric)
            margins.append(int(heights[vertex] - plane_height))
    return min(margins), len(margins)


stencil_margin = lower_hull_margin(STENCIL, DATA["HGT_LO"])
prior_margin = lower_hull_margin(PRIOR, DATA["HGT_PR"])
unpaired = {
    "stencil": len(internal_unpaired_facets(STENCIL)),
    "cycle728": len(internal_unpaired_facets(PRIOR)),
    "cost320": len(internal_unpaired_facets(DEAREST)),
}
gate(
    "independent regular comparator heights",
    stencil_margin == (16, 912) and prior_margin == (32, 912),
    "stencil {0}; Cycle 728 witness {1}".format(stencil_margin, prior_margin),
)
gate(
    "independent non-face-to-face obstruction",
    unpaired == {"stencil": 0, "cycle728": 0, "cost320": 16},
    str(unpaired),
)


floor_z_mutation = min(slack - 1 for slack in floor_slacks)
ceiling_z_mutation = min(slack - 1 for slack in ceiling_slacks)
replacement = next(cell for cell in STENCIL if cell not in set(DEAREST))
damaged = list(DEAREST)
damaged[0] = replacement
damaged_pairs = separator_count(damaged)
gate(
    "hostile certificate mutations are rejected",
    floor_z_mutation < 0 and ceiling_z_mutation < 0,
    "floor least {0}; ceiling least {1}".format(floor_z_mutation, ceiling_z_mutation),
)
gate(
    "hostile witness mutation is rejected",
    damaged_pairs < 1128,
    "separated pairs {0}/1128".format(damaged_pairs),
)


npass = sum(ok for _, ok in GATES)
nfail = len(GATES) - npass
print("TOTAL: PASS={0} FAIL={1}".format(npass, nfail), flush=True)
sys.exit(0 if nfail == 0 else 1)
