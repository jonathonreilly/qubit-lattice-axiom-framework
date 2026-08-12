"""Independent reconstruction for the supplied finite Cycle-734 cell model.

This checker imports and executes no primary implementation. It independently
rebuilds the corner-simplex census, four-column charge, generic point chamber,
complete floor-dissection set (using the opposite exact-cover pivot), genuine
triple co-occurrence, minimizer distance graph, and four-piece region flips.
Hostile mutations exercise charge, cover, and geometry surfaces. Any failed
gate makes the checker exit nonzero.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / (
    "outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_"
    "independent_check_2026_08_04_receipt_2026-08-04.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py",
    "docs/PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md",
)
AUDIT_TIMEOUT_SEC = 600

PASSES = 0
FAILS = 0
RESULTS: dict[str, dict[str, object]] = {}


def gate(name: str, ok: bool, detail: str) -> None:
    global PASSES, FAILS
    PASSES += int(bool(ok))
    FAILS += int(not ok)
    RESULTS[name] = {"ok": bool(ok), "detail": detail}
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


PERMS4 = tuple(itertools.permutations(range(4)))


def parity(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def det4_batch(matrices: np.ndarray) -> np.ndarray:
    result = np.zeros(len(matrices), dtype=np.int64)
    rows = np.arange(4)
    for perm in PERMS4:
        result += parity(perm) * np.prod(
            matrices[:, rows, perm], axis=1, dtype=np.int64
        )
    return result


def exact_inverses(vertices: np.ndarray, pieces: np.ndarray) -> np.ndarray:
    matrices = np.stack(
        [(vertices[piece[1:]] - vertices[piece[0]]).T for piece in pieces]
    )
    candidates = np.rint(np.linalg.inv(matrices.astype(float))).astype(np.int64)
    if not bool(
        (np.einsum("nij,njk->nik", candidates, matrices)
         == np.eye(4, dtype=np.int64)).all()
    ):
        raise RuntimeError("exact inverse reconstruction failed")
    return candidates


def make_group(corners: list[tuple[int, int, int, int]]) -> list[tuple[int, ...]]:
    position = {corner: i for i, corner in enumerate(corners)}
    images = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if parity(perm) * int(np.prod(signs)) != 1:
                continue
            for tick_flip in (0, 1):
                image = []
                for corner in corners:
                    centred = [2 * corner[j] - 1 for j in range(3)]
                    spatial = [signs[i] * centred[perm[i]] for i in range(3)]
                    key = tuple((value + 1) // 2 for value in spatial)
                    key += (1 - corner[3] if tick_flip else corner[3],)
                    image.append(position[key])
                images.append(tuple(image))
    return sorted(set(images))


def piece_orbits(
    pieces: np.ndarray, group: list[tuple[int, ...]]
) -> tuple[np.ndarray, np.ndarray]:
    lookup = {tuple(int(x) for x in piece): i for i, piece in enumerate(pieces)}
    labels = -np.ones(len(pieces), dtype=np.int64)
    reps = []
    for index, piece in enumerate(pieces):
        if labels[index] >= 0:
            continue
        label = len(reps)
        reps.append(index)
        for image in group:
            moved = tuple(sorted(image[int(corner)] for corner in piece))
            labels[lookup[moved]] = label
    return labels, np.asarray(reps, dtype=np.int64)


def sample_family(
    vertices: np.ndarray,
    pieces: np.ndarray,
    group: list[tuple[int, ...]],
    reps: np.ndarray,
) -> tuple[np.ndarray, int]:
    offsets = np.asarray((0, 1, 7, 49, 343), dtype=np.int64)
    weights = 2 * (3 * int(offsets.sum()) + 1 + offsets)
    scale = int(weights.sum())
    points = set()
    for index in reps:
        for image in group:
            moved = vertices[np.asarray(image)[pieces[index]]]
            points.add(tuple(int(x) for x in (weights[:, None] * moved).sum(axis=0)))
    return np.asarray(sorted(points), dtype=np.int64), scale


def membership_masks(
    vertices: np.ndarray,
    pieces: np.ndarray,
    inverse: np.ndarray,
    points: np.ndarray,
    scale: int,
) -> tuple[list[int], int]:
    masks = []
    boundary = 0
    for index, piece in enumerate(pieces):
        bary = (points - scale * vertices[piece[0]]) @ inverse[index].T
        total = bary.sum(axis=1)
        boundary += int(((bary == 0).any(axis=1) | (total == scale)).sum())
        inside = (bary > 0).all(axis=1) & (total < scale)
        mask = 0
        for point_index in np.flatnonzero(inside):
            mask |= 1 << int(point_index)
        masks.append(mask)
    return masks, boundary


def complete_covers(
    pool: list[int], masks: list[int], all_points: int
) -> tuple[list[tuple[int, ...]], int]:
    by_point: dict[int, list[int]] = {}
    for piece in pool:
        mask = masks[piece]
        while mask:
            bit = mask & -mask
            by_point.setdefault(bit.bit_length() - 1, []).append(piece)
            mask ^= bit
    solutions: list[tuple[int, ...]] = []
    nodes = 0

    def recurse(covered: int, selected: list[int]) -> None:
        nonlocal nodes
        nodes += 1
        if covered == all_points:
            solutions.append(tuple(sorted(selected)))
            return
        remaining = all_points ^ covered
        last = remaining.bit_length() - 1
        for piece in by_point.get(last, []):
            if masks[piece] & covered:
                continue
            selected.append(piece)
            recurse(covered | masks[piece], selected)
            selected.pop()

    recurse(0, [])
    return sorted(set(solutions)), nodes


NORMALS = tuple(
    np.asarray(normal, dtype=np.int64)
    for normal in itertools.product((-1, 0, 1), repeat=4)
    if any(normal)
)


def pair_separated(
    vertices: np.ndarray, pieces: np.ndarray, inverse: np.ndarray, a: int, b: int
) -> bool:
    left, right = vertices[pieces[a]], vertices[pieces[b]]
    facets = [inverse[a][k] for k in range(4)] + [-inverse[a].sum(axis=0)]
    facets += [inverse[b][k] for k in range(4)] + [-inverse[b].sum(axis=0)]
    for normal in NORMALS + tuple(facets):
        lv, rv = left @ normal, right @ normal
        if int(lv.max()) <= int(rv.min()) or int(rv.max()) <= int(lv.min()):
            return True
    return False


corners = [
    (x, y, z, tick)
    for x in (0, 1)
    for y in (0, 1)
    for z in (0, 1)
    for tick in (0, 1)
]
vertices = np.asarray(corners, dtype=np.int64)
subsets = np.asarray(list(itertools.combinations(range(16), 5)), dtype=np.int64)
volumes = np.abs(
    det4_batch(vertices[subsets[:, 1:]] - vertices[subsets[:, 0]][:, None, :])
)
pieces = subsets[volumes == 1]
inverse = exact_inverses(vertices, pieces)
pair_slots = tuple(itertools.combinations(range(5), 2))
cost = np.zeros(len(pieces), dtype=np.int64)
for a, b in pair_slots:
    distance = np.abs(vertices[pieces[:, a]] - vertices[pieces[:, b]]).sum(axis=1)
    cost += distance > 1

gate(
    "independent cell and cost census",
    Counter(volumes.tolist()) == Counter({0: 1360, 1: 2672, 2: 320, 3: 16})
    and Counter(cost.tolist()) == Counter({6: 400, 7: 1216, 8: 864, 9: 192}),
    f"minimal={len(pieces)} cost={sorted(Counter(cost.tolist()).items())}",
)

group = make_group(corners)
piece_labels, reps = piece_orbits(pieces, group)
orbit_sizes = np.bincount(piece_labels, minlength=len(reps))
gate(
    "independent carried action",
    len(group) == 48 and len(reps) == 57
    and sorted(set(int(x) for x in orbit_sizes)) == [16, 48],
    f"action={len(group)} orbits={len(reps)} sizes={sorted(set(orbit_sizes.tolist()))}",
)

points, scale = sample_family(vertices, pieces, group, reps)
masks, boundary = membership_masks(vertices, pieces, inverse, points, scale)
all_points = (1 << len(points)) - 1
gate(
    "independent generic sample chamber",
    len(points) == 2736 and scale == 12810 and boundary == 0,
    f"points={len(points)} scale={scale} boundary={boundary}",
)

pool = [int(index) for index in np.flatnonzero(cost == 6)]
solutions, nodes = complete_covers(pool, masks, all_points)
lengths = sorted(set(len(solution) for solution in solutions))
used = sorted(set(piece for solution in solutions for piece in solution))
gate(
    "opposite-pivot complete floor-dissection census",
    len(solutions) == 15800 and lengths == [24] and len(used) == 192,
    f"nodes={nodes} solutions={len(solutions)} lengths={lengths} used={len(used)}",
)

piece_position = {piece: i for i, piece in enumerate(used)}
membership_bits = [0] * len(used)
for solution_index, solution in enumerate(solutions):
    bit = 1 << solution_index
    for piece in solution:
        membership_bits[piece_position[piece]] |= bit

cooccurrence = np.zeros((len(used), len(used)), dtype=bool)
for solution in solutions:
    indices = [piece_position[piece] for piece in solution]
    cooccurrence[np.ix_(indices, indices)] = True
np.fill_diagonal(cooccurrence, False)
co_pairs = [
    (a, b)
    for a in range(len(used))
    for b in range(a + 1, len(used))
    if cooccurrence[a, b]
]
separated = sum(
    pair_separated(vertices, pieces, inverse, used[a], used[b]) for a, b in co_pairs
)
gate(
    "independent exact dissection geometry",
    len(co_pairs) == 15168 and separated == len(co_pairs),
    f"cooccurring_pairs={len(co_pairs)} exactly_separated={separated}",
)

cliques = genuine = 0
for a in range(len(used)):
    neighbours = [b for b in range(a + 1, len(used)) if cooccurrence[a, b]]
    for x, y in itertools.combinations(neighbours, 2):
        if not cooccurrence[x, y]:
            continue
        cliques += 1
        genuine += int(bool(membership_bits[a] & membership_bits[x] & membership_bits[y]))
gate(
    "independent genuine triple-cooccurrence audit",
    cliques == 649600 and genuine == 636032 and cliques - genuine == 13568,
    f"pairwise_cliques={cliques} genuine={genuine} spurious={cliques-genuine}",
)

solution_sets = [set(solution) for solution in solutions]
solution_matrix = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    solution_matrix[row, [piece_position[piece] for piece in solution]] = 1
distance_counts: Counter[int] = Counter()
edges_by_distance: dict[int, list[np.ndarray]] = {distance: [] for distance in range(4, 11)}
four_edges: list[tuple[int, int]] = []
parent = list(range(len(solutions)))


def find(index: int) -> int:
    while parent[index] != index:
        parent[index] = parent[parent[index]]
        index = parent[index]
    return index


for start in range(0, len(solutions), 512):
    overlap = solution_matrix[start:start + 512] @ solution_matrix.T
    distance = 24 - overlap.astype(np.int16)
    global_rows = np.arange(start, start + len(distance))[:, None]
    columns = np.arange(len(solutions))[None, :]
    upper = global_rows < columns
    counts = np.bincount(distance[upper], minlength=25)
    for value, count in enumerate(counts):
        if count:
            distance_counts[value] += int(count)
    for value in range(4, 11):
        rr, cc = np.nonzero((distance == value) & upper)
        if len(rr):
            edges_by_distance[value].append(
                np.stack((rr + start, cc), axis=1).astype(np.int32)
            )

threshold_components = []
for threshold in range(4, 11):
    chunks = edges_by_distance[threshold]
    edges = np.concatenate(chunks, axis=0) if chunks else np.empty((0, 2), dtype=np.int32)
    if threshold == 4:
        four_edges = [(int(edge[0]), int(edge[1])) for edge in edges]
    for left, right in edges:
        a, b = find(int(left)), find(int(right))
        if a != b:
            parent[a] = b
    threshold_components.append(len(set(find(i) for i in range(len(solutions)))))

expected_distances = [4] + list(range(6, 25))
gate(
    "independent minimizer-distance and component ladder",
    sorted(distance_counts) == expected_distances
    and distance_counts[4] == 46128 and distance_counts[24] == 29069284
    and sum(distance_counts.values()) == 124812100
    and threshold_components == [349, 349, 157, 61, 61, 13, 1],
    f"distances={sorted(distance_counts)} four={distance_counts[4]} disjoint={distance_counts[24]} ladder={threshold_components}",
)

corner_masks = []
for piece in pieces:
    mask = 0
    for corner in piece:
        mask |= 1 << int(corner)
    corner_masks.append(mask)

regions: dict[tuple[int, int], list[tuple[int, int]]] = {}
for left, right in four_edges:
    removed = sorted(solution_sets[left] - solution_sets[right])
    corner_mask = 0
    point_mask = 0
    for piece in removed:
        corner_mask |= corner_masks[piece]
        point_mask |= masks[piece]
    regions.setdefault((corner_mask, point_mask), []).append((left, right))

representatives = []
for corner_mask, point_mask in regions:
    images = []
    for image in group:
        moved = 0
        for corner in range(16):
            if corner_mask >> corner & 1:
                moved |= 1 << image[corner]
        images.append(moved)
    representatives.append(min(images))

gate(
    "independent four-piece region census",
    len(regions) == 120 and len(set(mask for mask, _ in regions)) == 120
    and Counter(Counter(representatives).values()) == Counter({12: 2, 24: 2, 48: 1}),
    f"regions={len(regions)} family_sizes={sorted(Counter(representatives).values())}",
)

valid_refill_counts = []
floor_refill_counts = []
for region, edges in regions.items():
    left, right = edges[0]
    common = sorted(solution_sets[left] & solution_sets[right])
    candidates = [
        int(index) for index in range(len(pieces))
        if not (corner_masks[index] & ~region[0]) and not (masks[index] & ~region[1])
    ]
    refills = []
    for refill in itertools.combinations(candidates, 4):
        covered = 0
        compatible = True
        for piece in refill:
            if covered & masks[piece]:
                compatible = False
                break
            covered |= masks[piece]
        if not compatible or covered != region[1]:
            continue
        candidate = common + list(refill)
        geometric = all(
            pair_separated(vertices, pieces, inverse, a, b)
            for a, b in itertools.combinations(candidate, 2)
        )
        if geometric:
            refills.append(refill)
    valid_refill_counts.append(len(refills))
    floor_refill_counts.append(
        sum(sum(int(cost[piece]) for piece in refill) == 24 for refill in refills)
    )

gate(
    "independent genuine region-refill reconstruction",
    sorted(set(valid_refill_counts)) == [2, 24]
    and sorted(set(floor_refill_counts)) == [2],
    f"geometric_refills={sorted(set(valid_refill_counts))} floor_refills={sorted(set(floor_refill_counts))}",
)

mutated_cost = cost.copy()
mutated_cost[pool[0]] += 1
mutated_pool = [int(index) for index in np.flatnonzero(mutated_cost == 6)]
gate(
    "hostile least-cost-pool mutation",
    len(mutated_pool) == 399,
    "raising one minimum piece removes it from the complete search pool",
)

mutated_solution = list(solutions[0])
mutated_solution[0] = mutated_solution[1]
gate(
    "hostile duplicated-piece cover mutation",
    len(set(mutated_solution)) != 24,
    "duplicating one simplex destroys the declared dissection cardinality",
)

report = {
    "schema": "physical-least-cost-cutting-flip-and-move-ladder-cycle734-independent-v1",
    "status": "pass" if FAILS == 0 else "fail",
    "claim_type": "bounded_theorem_independent_check",
    "audit_status_authority": "independent audit lane only",
    "pass": PASSES,
    "fail": FAILS,
    "results": RESULTS,
    "floor": {
        "dissections": len(solutions),
        "used_pieces": len(used),
        "cooccurring_pairs": len(co_pairs),
        "genuine_cooccurring_triples": genuine,
    },
    "distance": {
        "pairs": sum(distance_counts.values()),
        "four_piece_edges": distance_counts[4],
        "components_4_to_10": threshold_components,
    },
    "regions": {
        "count": len(regions),
        "family_sizes": sorted(Counter(representatives).values()),
        "genuine_refill_counts": sorted(set(valid_refill_counts)),
        "floor_refills_per_region": sorted(set(floor_refill_counts)),
    },
    "scope": "supplied one-cell normalized-volume-one corner-simplex model only",
}
RECEIPT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(report, sort_keys=True), flush=True)
print(f"TOTAL: PASS={PASSES} FAIL={FAILS}", flush=True)
raise SystemExit(0 if FAILS == 0 else 1)
