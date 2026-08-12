"""Independent reconstruction for the supplied finite Cycle-735 cell model.

This checker imports and executes no primary implementation.  It rebuilds the corner
model, opposite-pivot exact covers, packed-XOR move census, region system, connected and
embedded cubes, and dense-array GF(2) charge algebra.  Hostile mutations fail closed.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
C734_RECEIPT_PATH = ROOT / (
    "outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04_"
    "receipt_2026-08-04.json"
)
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md",
    "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py",
    "outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04_"
    "receipt_2026-08-04.json",
    "scripts/physical_least_cost_cutting_piece_charge_cycle735_2026_08_05.py",
    "docs/PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026-08-05.md",
)
AUDIT_TIMEOUT_SEC = 600

PASS = 0
FAIL = 0


def gate(name: str, ok: bool, detail: str) -> None:
    global PASS, FAIL
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def parity(perm: tuple[int, ...]) -> int:
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i + 1, len(perm))) % 2 else 1


PERMS4 = tuple(itertools.permutations(range(4)))


def det4_batch(matrices: np.ndarray) -> np.ndarray:
    answer = np.zeros(len(matrices), dtype=np.int64)
    rows = np.arange(4)
    for perm in PERMS4:
        answer += parity(perm) * np.prod(matrices[:, rows, perm], axis=1, dtype=np.int64)
    return answer


def group_action(corners: list[tuple[int, int, int, int]]) -> list[tuple[int, ...]]:
    position = {corner: i for i, corner in enumerate(corners)}
    images = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if parity(perm) * math.prod(signs) != 1:
                continue
            for tick_flip in (0, 1):
                image = []
                for corner in corners:
                    centred = [2 * corner[j] - 1 for j in range(3)]
                    spatial = tuple((signs[i] * centred[perm[i]] + 1) // 2 for i in range(3))
                    image.append(position[spatial + (1 - corner[3] if tick_flip else corner[3],)])
                images.append(tuple(image))
    return sorted(set(images))


corners = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
vertices = np.asarray(corners, dtype=np.int64)
subsets = np.asarray(list(itertools.combinations(range(16), 5)), dtype=np.int64)
volumes = np.abs(det4_batch(vertices[subsets[:, 1:]] - vertices[subsets[:, 0]][:, None, :]))
pieces = subsets[volumes == 1]
matrices = np.stack([(vertices[p[1:]] - vertices[p[0]]).T for p in pieces])
inverse = np.rint(np.linalg.inv(matrices.astype(float))).astype(np.int64)
cost = np.zeros(len(pieces), dtype=np.int64)
for a, b in itertools.combinations(range(5), 2):
    cost += np.abs(vertices[pieces[:, a]] - vertices[pieces[:, b]]).sum(axis=1) > 1
gate(
    "independent supplied cell census",
    Counter(volumes.tolist()) == Counter({0: 1360, 1: 2672, 2: 320, 3: 16})
    and Counter(cost.tolist()) == Counter({6: 400, 7: 1216, 8: 864, 9: 192})
    and bool((np.einsum("nij,njk->nik", inverse, matrices) == np.eye(4, dtype=np.int64)).all()),
    "2,672 unit pieces; four-coordinate charge counts 400/1,216/864/192",
)

group = group_action(corners)
piece_lookup = {tuple(int(x) for x in piece): i for i, piece in enumerate(pieces)}
labels = -np.ones(len(pieces), dtype=np.int64)
reps = []
for index, piece in enumerate(pieces):
    if labels[index] >= 0:
        continue
    label = len(reps)
    reps.append(index)
    for image in group:
        labels[piece_lookup[tuple(sorted(image[int(corner)] for corner in piece))]] = label
gate("independent carried action", len(group) == 48 and len(reps) == 57,
     "48 elements and 57 piece orbits")

offsets = np.asarray((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(offsets.sum()) + 1 + offsets)
scale = int(weights.sum())
point_set = set()
for index in reps:
    for image in group:
        point_set.add(tuple(int(x) for x in
                            (weights[:, None] * vertices[np.asarray(image)[pieces[index]]]).sum(axis=0)))
points = np.asarray(sorted(point_set), dtype=np.int64)
masks = []
boundary = 0
for index, piece in enumerate(pieces):
    bary = (points - scale * vertices[piece[0]]) @ inverse[index].T
    total = bary.sum(axis=1)
    boundary += int(((bary == 0).any(axis=1) | (total == scale)).sum())
    inside = (bary > 0).all(axis=1) & (total < scale)
    mask = 0
    for point in np.flatnonzero(inside):
        mask |= 1 << int(point)
    masks.append(mask)
all_points = (1 << len(points)) - 1
gate("independent generic chamber", len(points) == 2736 and scale == 12810 and boundary == 0,
     "2,736 points; no boundary incidence")

pool = [int(index) for index in np.flatnonzero(cost == 6)]
by_point: dict[int, list[int]] = {}
for piece in pool:
    mask = masks[piece]
    while mask:
        bit = mask & -mask
        by_point.setdefault(bit.bit_length() - 1, []).append(piece)
        mask ^= bit
solutions = []
nodes = 0


def cover(covered: int, chosen: list[int]) -> None:
    global nodes
    nodes += 1
    if covered == all_points:
        solutions.append(tuple(sorted(chosen)))
        return
    point = (all_points ^ covered).bit_length() - 1  # opposite pivot from the primary
    for piece in by_point.get(point, []):
        if masks[piece] & covered:
            continue
        chosen.append(piece)
        cover(covered | masks[piece], chosen)
        chosen.pop()


cover(0, [])
solutions = sorted(set(solutions))
used = sorted(set(piece for solution in solutions for piece in solution))
piece_position = {piece: i for i, piece in enumerate(used)}
gate(
    "opposite-pivot complete floor population",
    len(solutions) == 15800 and len(used) == 192 and set(map(len, solutions)) == {24},
    "15,800 covers, 192 used pieces, 24 pieces each",
)

# Broad primitive normals verify every pair that co-occurs in a reconstructed cover.
cooccurs = set()
for solution in solutions:
    cooccurs.update(tuple(sorted(pair)) for pair in itertools.combinations(solution, 2))
normal_rows = []
for normal in itertools.product(range(-4, 5), repeat=4):
    if not any(normal) or math.gcd(*(abs(x) for x in normal)) != 1:
        continue
    if next(x for x in normal if x) > 0:
        normal_rows.append(normal)
normals = np.asarray(normal_rows, dtype=np.int64)
projections = vertices[pieces[np.asarray(used)].reshape(-1)].reshape(len(used), 5, 4) @ normals.T
mins, maxs = projections.min(axis=1), projections.max(axis=1)
separated = 0
for left, right in cooccurs:
    a, b = piece_position[left], piece_position[right]
    separated += int(bool(((maxs[a] <= mins[b]) | (maxs[b] <= mins[a])).any()))
gate("independent exact dissection geometry",
     len(normals) == 2928 and len(cooccurs) == 15168 and separated == len(cooccurs),
     "2,928 primitive normals separate all 15,168 cooccurring pairs")

# Packed-XOR distance is independent of the primary's float Gram matrix.
packed = np.zeros((len(solutions), 3), dtype=np.uint64)
for row, solution in enumerate(solutions):
    for piece in solution:
        column = piece_position[piece]
        packed[row, column // 64] |= np.uint64(1) << np.uint64(column % 64)
edges: dict[int, list[np.ndarray]] = {distance: [] for distance in range(4, 11)}
distance_census: Counter[int] = Counter()
for start in range(0, len(solutions), 64):
    distance = np.bitwise_count(packed[start:start + 64, None, :] ^ packed[None, :, :]).sum(axis=2) // 2
    rows = np.arange(start, start + len(distance))[:, None]
    cols = np.arange(len(solutions))[None, :]
    upper = rows < cols
    counts = np.bincount(distance[upper].astype(np.int64), minlength=25)
    distance_census.update({i: int(n) for i, n in enumerate(counts) if n})
    for value in edges:
        rr, cc = np.nonzero((distance == value) & upper)
        if len(rr):
            edges[value].append(np.stack((rr + start, cc), axis=1).astype(np.int32))
edges = {value: np.concatenate(chunks) if chunks else np.empty((0, 2), dtype=np.int32)
         for value, chunks in edges.items()}
gate("independent packed-XOR move census",
     sum(distance_census.values()) == 124812100 and len(edges[4]) == 46128
     and len(edges[6]) == 31968 and len(edges[7]) == 60096 and len(edges[8]) == 151704,
     "all 124,812,100 pairs; move counts 46,128/31,968/60,096/151,704")

solution_sets = [set(solution) for solution in solutions]
corner_masks = []
for piece in pieces:
    mask = 0
    for corner in piece:
        mask |= 1 << int(corner)
    corner_masks.append(mask)
regions: dict[tuple[int, int], int] = {}
edge_region = np.empty(len(edges[4]), dtype=np.int32)
for edge_index, (left0, right0) in enumerate(edges[4]):
    removed = solution_sets[int(left0)] - solution_sets[int(right0)]
    cmask = 0
    pmask = 0
    for piece in removed:
        cmask |= corner_masks[piece]
        pmask |= masks[piece]
    key = (cmask, pmask)
    regions.setdefault(key, len(regions))
    edge_region[edge_index] = regions[key]
gate("independent region reconstruction", len(regions) == 120,
     "46,128 smallest moves reduce to 120 exact region keys")

C734 = json.loads(C734_RECEIPT_PATH.read_text(encoding="utf-8"))
gate(
    "direct Cycle 734 receipt binding",
    C734.get("status") == "pass"
    and C734.get("floor", {}).get("genuine_dissections") == len(solutions)
    and C734.get("floor", {}).get("used_pieces") == len(used)
    and C734.get("minimizer_distance", {}).get("four_piece_moves") == len(edges[4])
    and C734.get("four_piece_regions", {}).get("regions") == len(regions),
    "Cycle 734 floor, move, and region results match reconstruction",
)

parent = list(range(len(solutions)))


def find(index: int) -> int:
    while parent[index] != index:
        parent[index] = parent[parent[index]]
        index = parent[index]
    return index


for left0, right0 in edges[4]:
    left, right = find(int(left0)), find(int(right0))
    if left != right:
        parent[left] = right
component = np.asarray([find(i) for i in range(len(solutions))])
component_sizes = Counter(component.tolist())
size_census = Counter(component_sizes.values())
adjacency = [dict() for _ in solutions]
for edge_index, (left0, right0) in enumerate(edges[4]):
    left, right, region = int(left0), int(right0), int(edge_region[edge_index])
    adjacency[left][region] = right
    adjacency[right][region] = left

whole_cubes = 0
whole_covered = 0
whole_dimensions = set()
for root, size in component_sizes.items():
    vertices0 = np.flatnonzero(component == root)
    if size & (size - 1):
        continue
    dimension = size.bit_length() - 1
    labels0 = Counter(region for vertex in vertices0 for region in adjacency[int(vertex)])
    degrees = [len(adjacency[int(vertex)]) for vertex in vertices0]
    if (size == 1 or set(degrees) == {dimension}) and len(labels0) == dimension \
            and set(labels0.values()) == {size}:
        whole_cubes += 1
        whole_covered += size
        whole_dimensions.add(dimension)
gate("independent whole-component cube census",
     size_census == Counter({1: 144, 2: 96, 4: 36, 7: 48, 236: 24, 9320: 1})
     and whole_cubes == 276 and whole_covered == 480 and whole_dimensions == {0, 1, 2},
     "349 components; 276 whole cubes cover 480 vertices in dimensions 0..2")

maximum = 0
maximum_cubes: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()


def extend(labels0: list[int], states: set[int], candidates: list[int]) -> None:
    global maximum
    dimension = len(labels0)
    if dimension > maximum:
        maximum = dimension
        maximum_cubes.clear()
    if dimension == maximum and dimension >= 6:
        maximum_cubes.add((tuple(labels0), tuple(sorted(states))))
    for offset, region in enumerate(candidates):
        image = {vertex: adjacency[vertex].get(region) for vertex in states}
        if any(target is None for target in image.values()):
            continue
        targets = list(image.values())
        if len(set(targets)) != len(states) or set(targets) & states:
            continue
        if any(adjacency[target].get(old) != image.get(adjacency[vertex].get(old))
               for vertex, target in image.items() for old in labels0):
            continue
        enlarged = states | set(targets)
        common = set.intersection(*(set(adjacency[vertex]) for vertex in enlarged))
        extend(labels0 + [region], enlarged,
               [other for other in candidates[offset + 1:] if other in common])


for vertex in range(len(solutions)):
    extend([], {vertex}, sorted(adjacency[vertex]))
gate("independent embedded-cube closure",
     maximum == 6 and len(maximum_cubes) == 160,
     "160 labelled dimension-6 cubes; exhaustive closure finds none in dimension 7")

used_masks = []
for solution in solutions:
    mask = 0
    for piece in solution:
        mask ^= 1 << piece_position[piece]
    used_masks.append(mask)
region_rows = []
for key, region in sorted(regions.items(), key=lambda item: item[1]):
    edge_index = int(np.flatnonzero(edge_region == region)[0])
    left, right = map(int, edges[4][edge_index])
    region_rows.append(used_masks[left] ^ used_masks[right])
six_rows = sorted(set(used_masks[int(left)] ^ used_masks[int(right)]
                      for left, right in edges[6]))


def dense_solve(row_masks: list[int], targets: list[int]) -> tuple[np.ndarray | None, int, list[np.ndarray]]:
    matrix = np.zeros((len(row_masks), len(used) + 1), dtype=np.uint8)
    for row, (mask, target) in enumerate(zip(row_masks, targets)):
        for column in range(len(used)):
            matrix[row, column] = (mask >> column) & 1
        matrix[row, -1] = target & 1
    pivot_columns = []
    rank = 0
    for column in range(len(used)):
        candidates = np.flatnonzero(matrix[rank:, column])
        if not len(candidates):
            continue
        selected = rank + int(candidates[0])
        matrix[[rank, selected]] = matrix[[selected, rank]]
        other = np.flatnonzero(matrix[:, column])
        other = other[other != rank]
        matrix[other] ^= matrix[rank]
        pivot_columns.append(column)
        rank += 1
    if bool(((matrix[:, :-1].sum(axis=1) == 0) & (matrix[:, -1] == 1)).any()):
        return None, rank, []
    solution = np.zeros(len(used), dtype=np.uint8)
    for row, column in enumerate(pivot_columns):
        solution[column] = matrix[row, -1]
    free = [column for column in range(len(used)) if column not in pivot_columns]
    nullspace = []
    for column in free:
        vector = np.zeros(len(used), dtype=np.uint8)
        vector[column] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = matrix[row, column]
        nullspace.append(vector)
    return solution, rank, nullspace


part1, rank1, null1 = dense_solve(region_rows, [1] * len(region_rows))
part2, rank2, null2 = dense_solve(region_rows + six_rows,
                                  [1] * len(region_rows) + [0] * len(six_rows))
part3, rank3, _ = dense_solve(region_rows + six_rows,
                              [1] * len(region_rows) + [1] * len(six_rows))
assert part1 is not None and part2 is not None
solution_matrix = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    solution_matrix[row, [piece_position[piece] for piece in solution]] = 1


def gf2_rank(columns: list[np.ndarray]) -> int:
    basis: dict[int, int] = {}
    for column in columns:
        packed0 = np.packbits(column, bitorder="little")
        value = int.from_bytes(packed0.tobytes(), "little")
        while value:
            pivot = (value & -value).bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


image1 = gf2_rank([solution_matrix @ vector & 1 for vector in null1])
image2 = gf2_rank([solution_matrix @ vector & 1 for vector in null2])
charge = solution_matrix @ part2 & 1
sides = sorted(Counter(charge.tolist()).values())
gate("independent dense GF2 charge solve",
     rank1 == 86 and len(null1) == 106 and image1 == 2
     and rank2 == 87 and len(null2) == 105 and image2 == 1
     and sides == [7704, 8096] and part3 is None,
     "ranks 86/87; induced dimensions 2/1; sides 7,704/8,096; reversed-size6 inconsistent")

# Rebuild the region action and verify that no single row carries the rank, while every
# complete carried family does.  This uses corner masks, not the primary's edge maps.
region_by_corner = {key[0]: region for key, region in regions.items()}
rparent = list(range(len(regions)))


def rfind(index: int) -> int:
    while rparent[index] != index:
        rparent[index] = rparent[rparent[index]]
        index = rparent[index]
    return index


for image in group:
    for corner_mask, region in region_by_corner.items():
        moved = 0
        for corner in range(16):
            if (corner_mask >> corner) & 1:
                moved |= 1 << image[corner]
        left, right = rfind(region), rfind(region_by_corner[moved])
        if left != right:
            rparent[left] = right
families: dict[int, list[int]] = {}
for region in range(len(regions)):
    families.setdefault(rfind(region), []).append(region)
single_ranks = {
    dense_solve([row for j, row in enumerate(region_rows) if j != omitted],
                [0] * (len(region_rows) - 1))[1]
    for omitted in range(len(region_rows))
}
family_ranks = sorted(
    (len(family), dense_solve([row for j, row in enumerate(region_rows) if j not in family],
                              [0] * (len(region_rows) - len(family)))[1])
    for family in families.values()
)
gate("independent region-family rank structure",
     single_ranks == {86}
     and family_ranks == [(12, 84), (12, 84), (24, 75), (24, 83), (48, 64)],
     "all single deletions retain rank86; family deletion size/ranks match five families")

reversals = {}
for distance, pairs in edges.items():
    reversals[distance] = int((charge[pairs[:, 0]] != charge[pairs[:, 1]]).sum())
gate("independent larger-move charge readback",
     reversals == {4: 46128, 5: 0, 6: 0, 7: 26880, 8: 28608, 9: 0, 10: 0},
     "reversals by replaced pieces 4..10 are 46128/0/0/26880/28608/0/0")

degree_to_eight = np.zeros(len(solutions), dtype=np.int64)
for distance in range(4, 9):
    degree_to_eight += np.bincount(edges[distance].reshape(-1), minlength=len(solutions))
frozen = np.flatnonzero(degree_to_eight == 0)
smaller = int(np.argmin(np.bincount(charge, minlength=2)))
solution_lookup = {solution: i for i, solution in enumerate(solutions)}
solution_perms = []
for image in group:
    moved_piece = {}
    for piece in used:
        moved_piece[piece] = piece_lookup[tuple(sorted(image[int(corner)] for corner in pieces[piece]))]
    solution_perms.append(np.asarray([
        solution_lookup[tuple(sorted(moved_piece[piece] for piece in solution))]
        for solution in solutions
    ], dtype=np.int32))
frozen_orbit = {int(perm[int(frozen[0])]) for perm in solution_perms}
gate("independent finite move-isolated set",
     len(frozen) == 48 and frozen_orbit == set(map(int, frozen))
     and set(charge[frozen].tolist()) == {smaller}
     and all(bool((charge[perm] == charge).all()) for perm in solution_perms),
     "48 vertices form one symmetry orbit on the smaller, symmetry-fixed charge side")

bad_targets = [1] * len(region_rows)
bad_targets[0] = 0
bad_part, _, _ = dense_solve(region_rows, bad_targets)
bad_cover = list(solutions[0])
bad_cover[0] = bad_cover[1]
gate("hostile independent controls",
     bad_part is None and len(set(bad_cover)) != 24 and part3 is None,
     "one flipped region target, a duplicated cover, and reversed-size6 demands fail")

print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL), flush=True)
sys.exit(0 if FAIL == 0 else 1)
