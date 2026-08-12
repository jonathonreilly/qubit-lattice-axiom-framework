"""Independent exact reconstruction for the Cycle 733 finite theorem.

The checker never imports or executes the primary.  It reads only carried witness and
certificate literals from the primary AST, rebuilds the four-box, simplices, symmetry,
sample incidence, parity systems, exact-cover census, and geometric validation through
separate code paths, and exercises hostile mutations of the load-bearing semantics.
"""

import ast
import functools
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py",
    "outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_receipt_2026-08-04.json",
    "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py",
    "outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_receipt_2026-08-04.json",
)
ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ROOT / AUDIT_INPUT_PATHS[0]
RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8"))
C731_PRIMARY = ROOT / AUDIT_INPUT_PATHS[2]
C731_RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8"))
GATES = []


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("{0} {1:46s} {2}".format("PASS" if ok else "FAIL", name, detail), flush=True)


def literals(path, wanted):
    found = {}
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in wanted:
                found[name] = ast.literal_eval(node.value)
        elif len(node.targets) == 1 and isinstance(node.targets[0], ast.Tuple):
            names = [item.id for item in node.targets[0].elts if isinstance(item, ast.Name)]
            if names and all(name in wanted for name in names):
                found.update(zip(names, ast.literal_eval(node.value)))
    return found


WANTED = {"WIT", "DU", "FLOOR_U", "FLOOR_D", "FLOOR_Z"}
LIT = literals(PRIMARY, WANTED)
C731_LIT = literals(C731_PRIMARY, {"FLOOR_U", "FLOOR_D", "FLOOR_Z"})
gate("carried literals parse", set(LIT) == WANTED and len(C731_LIT) == 3,
     "Cycle 733 witness/dual/floor data and Cycle 731 floor data")
gate("Cycle 731 certificate is not stale",
     all(LIT[name] == C731_LIT[name] for name in ("FLOOR_U", "FLOOR_D", "FLOOR_Z")),
     "Cycle 733 carries the exact current Cycle 731 spatial-floor certificate")


def determinant(matrix):
    total = 0
    n = len(matrix)
    for permutation in itertools.permutations(range(n)):
        sign = -1 if sum(permutation[a] > permutation[b]
                         for a in range(n) for b in range(a + 1, n)) & 1 else 1
        term = sign
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def exact_inverse(matrix):
    source = matrix.tolist()
    divisor = determinant(source)
    inverse = []
    for row in range(4):
        values = []
        for column in range(4):
            minor = [line[:row] + line[row + 1 :]
                     for source_row, line in enumerate(source) if source_row != column]
            values.append(((-1) ** (row + column)) * determinant(minor) // divisor)
        inverse.append(values)
    return np.array(inverse, dtype=np.int64)


CORNERS = [tuple(bits) for bits in itertools.product((0, 1), repeat=4)]
VERTICES = np.array(CORNERS, dtype=np.int64)
POSITION = {corner: index for index, corner in enumerate(CORNERS)}
PIECES = []
INVERSES = []
VOLUME_COUNTS = {}
for piece in itertools.combinations(range(16), 5):
    points = VERTICES[list(piece)]
    matrix = (points[1:] - points[0]).T
    volume = abs(determinant(matrix.tolist()))
    VOLUME_COUNTS[volume] = VOLUME_COUNTS.get(volume, 0) + 1
    if volume == 1:
        PIECES.append(tuple(piece))
        INVERSES.append(exact_inverse(matrix))
PIECE_POSITION = {piece: index for index, piece in enumerate(PIECES)}
INVERSES = np.array(INVERSES, dtype=np.int64)
gate("four-box minimal pieces", len(PIECES) == 2672 and sum(VOLUME_COUNTS.values()) == 4368,
     str(sorted(VOLUME_COUNTS.items())))

ROTATIONS = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for row, column in enumerate(permutation):
            rotation[row, column] = signs[row]
        if determinant(rotation.tolist()) == 1:
            ROTATIONS.append(rotation)

GROUP = []
center = np.array([1, 1, 1], dtype=np.int64)
for rotation in ROTATIONS:
    for tick_flip in (0, 1):
        image = []
        for x, y, z, tick in CORNERS:
            spatial = rotation @ (2 * np.array([x, y, z], dtype=np.int64) - center) + center
            key = (int(spatial[0]) // 2, int(spatial[1]) // 2, int(spatial[2]) // 2,
                   1 - tick if tick_flip else tick)
            image.append(POSITION[key])
        GROUP.append(np.array(image, dtype=np.int64))
gate("finite cell group", len(ROTATIONS) == 24 and len(GROUP) == 48,
     "24 proper spatial rotations times the independent tick flip")

LABEL = [-1] * len(PIECES)
REPRESENTATIVES = []
for index, piece in enumerate(PIECES):
    if LABEL[index] >= 0:
        continue
    orbit = len(REPRESENTATIVES)
    REPRESENTATIVES.append(index)
    for action in GROUP:
        transformed = tuple(sorted(int(action[corner]) for corner in piece))
        LABEL[PIECE_POSITION[transformed]] = orbit
ORBIT_SIZES = [LABEL.count(orbit) for orbit in range(len(REPRESENTATIVES))]
gate("piece orbits", len(REPRESENTATIVES) == 57
     and sorted(set(ORBIT_SIZES)) == [16, 48] and sum(ORBIT_SIZES) == 2672,
     "57 complete symmetry orbits")

OFFSETS = np.array([0, 1, 7, 49, 343], dtype=np.int64)
bound = max(
    max(int(np.abs(INVERSES[i] @ (corner - VERTICES[PIECES[i][0]])).max()),
        abs(int((INVERSES[i] @ (corner - VERTICES[PIECES[i][0]])).sum()) - 1))
    for i in range(len(PIECES)) for corner in VERTICES
)
weights = 2 * (bound * int(OFFSETS.sum()) + 1 + OFFSETS)
scale = int(weights.sum())
spatial_center = np.array([scale // 2] * 3, dtype=np.int64)
point_orbit = {}
collisions = 0
for orbit, piece_index in enumerate(REPRESENTATIVES):
    point = (weights[:, None] * VERTICES[list(PIECES[piece_index])]).sum(axis=0)
    for action_index, action in enumerate(GROUP):
        rotation = ROTATIONS[action_index // 2]
        tick_flip = action_index & 1
        spatial = rotation @ (point[:3] - spatial_center) + spatial_center
        key = (int(spatial[0]), int(spatial[1]), int(spatial[2]),
               scale - int(point[3]) if tick_flip else int(point[3]))
        previous = point_orbit.setdefault(key, orbit)
        collisions += previous != orbit
SAMPLE_KEYS = sorted(point_orbit)
SAMPLES = np.array(SAMPLE_KEYS, dtype=np.int64)
INCIDENCE = np.zeros((len(PIECES), len(SAMPLES)), dtype=bool)
on_boundary = 0
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (
        SAMPLES.T - (scale * VERTICES[piece[0]])[:, None]
    )
    total = bary.sum(axis=0)
    on_boundary += int(((bary == 0).any(axis=0) | (total == scale)).sum())
    INCIDENCE[index] = (bary > 0).all(axis=0) & (total < scale)
MASKS = []
for row in INCIDENCE:
    mask = 0
    for point in np.flatnonzero(row):
        mask |= 1 << int(point)
    MASKS.append(mask)
ALL_POINTS = (1 << len(SAMPLES)) - 1
gate("generic sample incidence", bound == 3 and scale == 12810
     and len(SAMPLES) == 2736 and collisions == 0 and on_boundary == 0,
     "2736 points, no collision and no boundary incidence")

PAIRS = list(itertools.combinations(range(5), 2))


def cost(columns):
    answer = []
    for piece in PIECES:
        vertices = VERTICES[list(piece)]
        answer.append(sum(
            sum(abs(int(vertices[a, column]) - int(vertices[b, column]))
                for column in columns) > 1
            for a, b in PAIRS
        ))
    return np.array(answer, dtype=np.int64)


def separating_count(indices):
    normals = [np.array(v, dtype=np.int64)
               for v in itertools.product((-1, 0, 1), repeat=4) if any(v)]
    facets = []
    for index in indices:
        inverse = INVERSES[index]
        facets.append([inverse[row] for row in range(4)] + [-inverse.sum(axis=0)])
    good = 0
    for left, right in itertools.combinations(range(len(indices)), 2):
        left_vertices = VERTICES[list(PIECES[indices[left]])]
        right_vertices = VERTICES[list(PIECES[indices[right]])]
        for normal in normals + facets[left] + facets[right]:
            a = left_vertices @ normal
            b = right_vertices @ normal
            if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                good += 1
                break
    return good


def geometric_dissection(indices):
    return (len(indices) == 24 and len(set(indices)) == 24
            and separating_count(indices) == 276
            and functools.reduce(int.__or__, (MASKS[i] for i in indices), 0) == ALL_POINTS)


PINNED = [sorted((a << 6) + b for a, b in row) for row in LIT["WIT"]]
MONOTONE = []
for ordering in itertools.permutations(range(4)):
    current = [0, 0, 0, 0]
    path = [POSITION[tuple(current)]]
    for column in ordering:
        current[column] = 1
        path.append(POSITION[tuple(current)])
    MONOTONE.append(PIECE_POSITION[tuple(sorted(path))])
MONOTONE.sort()
DISSECTIONS = PINNED + [MONOTONE]
gate("exhibited dissections", len(PINNED) == 12 and len(set(MONOTONE)) == 24
     and all(geometric_dissection(dissection) for dissection in DISSECTIONS),
     "12 carried witnesses plus the independently constructed monotone stencil")

COLUMN_SETS = [columns for size in range(1, 5)
               for columns in itertools.combinations(range(4), size)]
COSTS = {columns: cost(columns) for columns in COLUMN_SETS}
NONZERO = [columns for columns in COLUMN_SETS if int(COSTS[columns].max()) > 0]
PROPER = [columns for columns in NONZERO if len(columns) < 4]
gate("column-cost family", len(COLUMN_SETS) == 15 and len(NONZERO) == 11
     and len(PROPER) == 10
     and all(np.all(COSTS[left] <= COSTS[right])
             for left in COLUMN_SETS for right in COLUMN_SETS
             if set(left) <= set(right)), "four singleton zero costs, eleven nonzero costs")
gate("no nonzero cost is cut-blind",
     all(len({int(COSTS[columns][d].sum()) for d in DISSECTIONS}) >= 2
         for columns in NONZERO), "each varies on the 13 exhibited dissections")

EQUATIONS = [MASKS[index] | (1 << len(SAMPLES)) for index in range(len(PIECES))]


def consistent(rhs, extra=None):
    basis = {}
    rows = list(zip(EQUATIONS, [int(value) & 1 for value in rhs]))
    if extra is not None:
        rows.append(extra)
    for row, value in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (row, value)
                break
            old_row, old_value = basis[pivot]
            row ^= old_row
            value ^= old_value
        if row == 0 and value:
            return False
    return True


SUPPORT_PARITY = ((1 << len(SAMPLES)) - 1, 0)
gate("proper parity systems",
     all(consistent(COSTS[columns])
         and consistent(COSTS[columns], SUPPORT_PARITY) for columns in PROPER),
     "all ten admit an even-support affine GF(2) certificate")
FULL_COLUMNS = (0, 1, 2, 3)
gate("full parity system is inconsistent", not consistent(COSTS[FULL_COLUMNS]),
     "the affine GF(2) system has no solution")

DUAL = list(LIT["DU"])
dual_xor = 0
for index in DUAL:
    dual_xor ^= EQUATIONS[index]
dual_cost = int(COSTS[FULL_COLUMNS][DUAL].sum())
mask_position = {mask: index for index, mask in enumerate(EQUATIONS)}
triple = None
for left in range(len(EQUATIONS)):
    for right in range(left + 1, len(EQUATIONS)):
        third = mask_position.get(EQUATIONS[left] ^ EQUATIONS[right])
        if third is not None and third > right:
            if int(COSTS[FULL_COLUMNS][[left, right, third]].sum()) & 1:
                triple = (left, right, third)
                break
    if triple is not None:
        break
gate("minimal full-set dual obstruction", dual_xor == 0 and dual_cost == 25
     and triple is None and len(set(EQUATIONS)) == len(EQUATIONS),
     "four pieces suffice; no one-, two-, or three-piece odd dual exists")

SPATIAL = COSTS[(0, 1, 2)]
FULL = COSTS[FULL_COLUMNS]
MIXED = []
for piece in PIECES:
    vertices = VERTICES[list(piece)]
    MIXED.append(sum(
        abs(int(vertices[a, 3]) - int(vertices[b, 3])) == 1
        and sum(abs(int(vertices[a, axis]) - int(vertices[b, axis]))
                for axis in range(3)) == 1
        for a, b in PAIRS
    ))
MIXED = np.array(MIXED, dtype=np.int64)
gate("tick-coupled split", np.array_equal(FULL, SPATIAL + MIXED)
     and int(np.sum(FULL == SPATIAL)) == 64,
     "full cost equals spatial plus exactly-one-spatial-step tick pairs")

least = int(FULL.min())
MINIMAL = [index for index, value in enumerate(FULL) if int(value) == least]
BY_POINT = {}
for index in MINIMAL:
    for point in np.flatnonzero(INCIDENCE[index]):
        BY_POINT.setdefault(int(point), []).append(index)
SOLUTIONS = []
NODES = [0]


def exact_covers(covered, chosen):
    NODES[0] += 1
    if covered == ALL_POINTS:
        if len(chosen) == 24:
            SOLUTIONS.append(tuple(sorted(chosen)))
        return
    remaining = ALL_POINTS & ~covered
    point = remaining.bit_length() - 1  # opposite point order from the primary
    for index in BY_POINT[point]:
        if MASKS[index] & covered:
            continue
        chosen.append(index)
        exact_covers(covered | MASKS[index], chosen)
        chosen.pop()


exact_covers(0, [])
gate("opposite-order minimum enumeration", least == 6 and len(MINIMAL) == 400
     and len(SOLUTIONS) == 15800,
     "{0} search nodes, 15800 exact covers".format(NODES[0]))

PERMUTATIONS = []
for action in GROUP:
    PERMUTATIONS.append([
        PIECE_POSITION[tuple(sorted(int(action[corner]) for corner in piece))]
        for piece in PIECES
    ])
seen = set()
representatives = []
orbit_sizes = []
geometric_ok = True
for solution in SOLUTIONS:
    if solution in seen:
        continue
    representatives.append(solution)
    family = {tuple(sorted(permutation[index] for index in solution))
              for permutation in PERMUTATIONS}
    orbit_sizes.append(len(family))
    seen |= family
    geometric_ok = geometric_ok and geometric_dissection(solution)
gate("minimum geometry and symmetry", geometric_ok and len(representatives) == 391
     and len(seen) == len(SOLUTIONS) and sorted(set(orbit_sizes)) == [8, 12, 24, 48],
     "391 geometrically certified representatives cover all 15800 solutions")

USED = sorted({index for solution in SOLUTIONS for index in solution})
USED_ORBITS = sorted({LABEL[index] for index in USED})
gate("four indispensable piece orbits", len(USED) == 192 and len(USED_ORBITS) == 4
     and all(set(LABEL[index] for index in solution) >= set(USED_ORBITS)
             for solution in SOLUTIONS),
     "every minimum dissection uses every one of the four orbits")

floor_vector = np.zeros(len(REPRESENTATIVES), dtype=np.int64)
for orbit, weight in LIT["FLOOR_U"]:
    floor_vector[orbit] = weight
membership = np.zeros((len(PIECES), len(REPRESENTATIVES)), dtype=np.int64)
sample_orbits = np.array([point_orbit[key] for key in SAMPLE_KEYS], dtype=np.int64)
for orbit in range(len(REPRESENTATIVES)):
    membership[:, orbit] = INCIDENCE[:, sample_orbits == orbit].sum(axis=1)
floor_slack = -(membership @ floor_vector + LIT["FLOOR_Z"]
                - LIT["FLOOR_D"] * SPATIAL)
FLOOR_SUPPORT = {index for index, slack in enumerate(floor_slack) if int(slack) == 0}
gate("Cycle 731 spatial-floor consumption", len(FLOOR_SUPPORT) == 1792
     and C731_RECEIPT.get("floor", {}).get("support_pieces") == 1792
     and all(sum(int(SPATIAL[index]) for index in solution) == 108
             and set(solution) <= FLOOR_SUPPORT for solution in SOLUTIONS),
     "all minimum full-cost dissections lie in the bound Cycle 731 support")

gate("single-piece holes are rigid", len(set(MASKS)) == len(MASKS),
     "2672 distinct interior footprints imply 15800*24 unique single-piece refills")
EXCLUDED = [index for index in MINIMAL if index not in set(USED)]
kept_vectors = {tuple(int(COSTS[columns][index]) for columns in NONZERO)
                for index in USED}
excluded_vectors = {tuple(int(COSTS[columns][index]) for columns in NONZERO)
                    for index in EXCLUDED}
gate("full-family support separation", len(EXCLUDED) == 208
     and len(kept_vectors) == 12 and len(excluded_vectors) == 13
     and not (kept_vectors & excluded_vectors),
     "12 kept vectors and 13 excluded vectors are disjoint")

# Hostile controls: the proof paths must reject nearby but wrong semantics.
mutated_cost = cost((0, 1, 2))
gate("hostile full-cost mutation rejected", not np.array_equal(mutated_cost, FULL)
     and int(mutated_cost[DUAL].sum()) % 2 == 0,
     "dropping the tick destroys the four-piece odd obstruction")

substitutions = 0
for position, original in enumerate(DUAL):
    other = DUAL[:position] + DUAL[position + 1 :]
    base_mask = 0
    base_cost = 0
    for index in other:
        base_mask ^= EQUATIONS[index]
        base_cost ^= int(FULL[index]) & 1
    for replacement in range(len(PIECES)):
        if replacement == original:
            continue
        substitutions += (base_mask ^ EQUATIONS[replacement]) == 0 and (base_cost ^ int(FULL[replacement]) & 1)
gate("hostile dual substitution rejected", substitutions == 0,
     "no single-piece replacement preserves the even cover with odd total")

overlap_control = next(
    (left, right) for left in MINIMAL for right in MINIMAL if left < right
    and not (MASKS[left] & MASKS[right]) and separating_count([left, right]) == 0
)
gate("sample-cover geometry hostile control", overlap_control is not None,
     "sample-disjoint simplices can overlap, so the separate geometry gate is load-bearing")

mutated_floor = floor_vector.copy()
mutated_floor[LIT["FLOOR_U"][0][0]] += 1
mutated_slack = -(membership @ mutated_floor + LIT["FLOOR_Z"]
                  - LIT["FLOOR_D"] * SPATIAL)
gate("hostile Cycle 731 weight mutation rejected", int(mutated_slack.min()) < 0,
     "a one-unit floor-certificate mutation violates nonnegative slack")

gate("receipt summary matches reconstruction",
     RECEIPT.get("family", {}).get("proper_sets_certified") == 10
     and RECEIPT.get("minimum", {}).get("dissections") == 15800
     and RECEIPT.get("minimum", {}).get("geometric_representatives") == 391
     and RECEIPT.get("minimum", {}).get("used_pieces") == 192
     and RECEIPT.get("separation", {}).get("intersection") == 0
     and RECEIPT.get("totals", {}).get("fail") == 0,
     "generated primary receipt is consistent with the independent route")

print("")
print("per_element: checked all 2672 minimal pieces, ten proper parity systems, the full "
      "dual obstruction, and both 192/208 least-cost support classes")
print("per_site: checked and not executed — this supplied one-cell theorem has no lattice-site "
      "field beyond its finite corner coordinates")
print("per_mode: checked and not executed — no modal or spectral statement is made")
print("per_block: checked the complete one-cell by one-tick box and independently enumerated "
      "all 15800 minimum exact covers with 391 geometric orbit checks")
print("lattice_wide: checked and not executed — no arbitrary-size, multi-cell, boundary, or "
      "continuum result is claimed")
passed = sum(ok for _, ok in GATES)
failed = len(GATES) - passed
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(1 if failed else 0)
