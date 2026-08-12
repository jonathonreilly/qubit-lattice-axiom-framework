"""Independent reconstruction for the supplied finite Cycle-731 cell model.

This checker never imports or executes the primary runner.  It reads only the
primary's carried sparse certificate literals from the Python AST, then rebuilds
the corner-simplex census, charge, carried action, generic sample incidence,
floor indicator, support completions, and ceiling row identity with separately
written code.  Hostile changes exercise certificate, relation, support, and
dissection failure surfaces.  Any failed gate makes the checker exit nonzero.
"""

from __future__ import annotations

import ast
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / (
    "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py"
)
NOTE = ROOT / (
    "docs/PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md"
)
RECEIPT = ROOT / (
    "outputs/physical_cost_identity_indicator_certificate_cycle731_"
    "independent_check_2026_08_04_receipt_2026-08-04.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py",
    "docs/PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md",
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


def carried_literals() -> dict[str, object]:
    wanted = {"FLOOR_U", "FLOOR_D", "FLOOR_Z", "CEIL_U", "CEIL_D", "CEIL_Z"}
    out: dict[str, object] = {}
    tree = ast.parse(PRIMARY.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            out[target.id] = ast.literal_eval(node.value)
        elif isinstance(target, ast.Tuple) and isinstance(node.value, ast.Tuple):
            names = [item.id for item in target.elts if isinstance(item, ast.Name)]
            if wanted.intersection(names):
                values = [ast.literal_eval(item) for item in node.value.elts]
            else:
                values = []
            if values and len(names) == len(values):
                for name, value in zip(names, values):
                    if name in wanted:
                        out[name] = value
    missing = sorted(wanted - out.keys())
    if missing:
        raise RuntimeError("missing carried primary literals: " + repr(missing))
    return out


PERMS4 = tuple(itertools.permutations(range(4)))


def parity(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


SIGNS4 = tuple(parity(perm) for perm in PERMS4)


def det4_batch(mats: np.ndarray) -> np.ndarray:
    """Exact Leibniz expansion, unlike the primary's 2x2-minor formula."""
    answer = np.zeros(len(mats), dtype=np.int64)
    rows = np.arange(4)
    for sign, perm in zip(SIGNS4, PERMS4):
        answer += sign * np.prod(mats[:, rows, perm], axis=1, dtype=np.int64)
    return answer


def integer_rank(rows: np.ndarray) -> int:
    work = [[int(value) for value in row] for row in rows]
    pivot = 0
    for column in range(len(work[0])):
        chosen = next((r for r in range(pivot, len(work)) if work[r][column]), None)
        if chosen is None:
            continue
        work[pivot], work[chosen] = work[chosen], work[pivot]
        pv = work[pivot][column]
        for r in range(len(work)):
            if r == pivot or work[r][column] == 0:
                continue
            factor = work[r][column]
            work[r] = [pv * x - factor * y for x, y in zip(work[r], work[pivot])]
            divisor = math.gcd(*(abs(x) for x in work[r]))
            if divisor > 1:
                work[r] = [x // divisor for x in work[r]]
        pivot += 1
        if pivot == len(work):
            break
    return pivot


def make_group(corners: list[tuple[int, int, int, int]]) -> list[tuple[int, ...]]:
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
                    mapped = [signs[i] * centred[perm[i]] for i in range(3)]
                    key = tuple((value + 1) // 2 for value in mapped)
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


def exact_inverses(vertices: np.ndarray, pieces: np.ndarray) -> np.ndarray:
    # The determinants are +/-1, so rounded floating inverses are candidates only;
    # exact integer multiplication below is the acceptance test.
    matrices = np.stack(
        [(vertices[piece[1:]] - vertices[piece[0]]).T for piece in pieces]
    )
    candidates = np.rint(np.linalg.inv(matrices.astype(float))).astype(np.int64)
    products = np.einsum("nij,njk->nik", candidates, matrices)
    if not bool((products == np.eye(4, dtype=np.int64)).all()):
        raise RuntimeError("candidate inverse failed exact integer multiplication")
    return candidates


def sample_family(
    vertices: np.ndarray,
    pieces: np.ndarray,
    group: list[tuple[int, ...]],
    reps: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, int]:
    offsets = np.asarray((0, 1, 7, 49, 343), dtype=np.int64)
    weights = 2 * (3 * int(offsets.sum()) + 1 + offsets)
    scale = int(weights.sum())
    centre = np.asarray((scale // 2, scale // 2, scale // 2), dtype=np.int64)
    labelled: dict[tuple[int, int, int, int], int] = {}
    for label, index in enumerate(reps):
        numerator = (weights[:, None] * vertices[pieces[index]]).sum(axis=0)
        for image in group:
            # Applying the corner permutation to the same barycentric weights is
            # a direct, matrix-free reconstruction of the point action.
            moved_vertices = vertices[np.asarray(image)[pieces[index]]]
            moved = (weights[:, None] * moved_vertices).sum(axis=0)
            key = tuple(int(x) for x in moved)
            prior = labelled.setdefault(key, label)
            if prior != label:
                raise RuntimeError("point orbit collision")
    keys = sorted(labelled)
    points = np.asarray(keys, dtype=np.int64)
    labels = np.asarray([labelled[key] for key in keys], dtype=np.int64)
    # The unused centre computation is deliberately checked: the point family
    # is centred in the three spatial coordinates.
    if not bool((points[:, :3].min(axis=0) < centre).all()):
        raise RuntimeError("unexpected point chamber")
    return points, labels, scale


def membership(
    vertices: np.ndarray,
    pieces: np.ndarray,
    inverse: np.ndarray,
    points: np.ndarray,
    point_labels: np.ndarray,
    orbit_count: int,
    scale: int,
) -> tuple[np.ndarray, list[int], int]:
    rows = np.zeros((len(pieces), orbit_count), dtype=np.int16)
    masks = []
    boundary = 0
    for i, piece in enumerate(pieces):
        delta = points - scale * vertices[piece[0]]
        bary = delta @ inverse[i].T
        total = bary.sum(axis=1)
        boundary += int(((bary == 0).any(axis=1) | (total == scale)).sum())
        inside = (bary > 0).all(axis=1) & (total < scale)
        rows[i] = np.bincount(point_labels[inside], minlength=orbit_count)
        mask = 0
        for j in np.flatnonzero(inside):
            mask |= 1 << int(j)
        masks.append(mask)
    return rows, masks, boundary


NORMALS = tuple(
    np.asarray(normal, dtype=np.int64)
    for normal in itertools.product((-1, 0, 1), repeat=4)
    if any(normal)
)


def is_dissection(
    vertices: np.ndarray,
    pieces: np.ndarray,
    inverse: np.ndarray,
    masks: list[int],
    indices: list[int],
    all_points: int,
) -> bool:
    if len(indices) != 24 or len(set(indices)) != 24:
        return False
    covered = 0
    for index in indices:
        covered |= masks[index]
    if covered != all_points:
        return False
    point_sets = [vertices[pieces[index]] for index in indices]
    facets = [
        [inverse[index][k] for k in range(4)] + [-inverse[index].sum(axis=0)]
        for index in indices
    ]
    for a, b in itertools.combinations(range(len(indices)), 2):
        separated = False
        for normal in NORMALS + tuple(facets[a] + facets[b]):
            left = point_sets[a] @ normal
            right = point_sets[b] @ normal
            if int(left.max()) <= int(right.min()) or int(right.max()) <= int(left.min()):
                separated = True
                break
        if not separated:
            return False
    return True


def exact_cover(
    pool: list[int], masks: list[int], all_points: int, forced: tuple[int, ...] = (),
) -> list[int] | None:
    point_count = all_points.bit_length()
    by_first_point = [[] for _ in range(point_count)]
    for index in pool:
        mask = masks[index]
        first = (mask & -mask).bit_length() - 1
        by_first_point[first].append(index)
    covered = 0
    current = list(forced)
    for index in forced:
        if covered & masks[index]:
            return None
        covered |= masks[index]

    def recurse(mask: int) -> bool:
        if mask == all_points:
            return len(current) == 24
        if len(current) >= 24:
            return False
        remaining = all_points ^ mask
        first = (remaining & -remaining).bit_length() - 1
        # A compatible piece covering the least uncovered point must have that
        # point as its own least point; otherwise its lower point would also be
        # uncovered.  This compact index is complete, not a search heuristic.
        for index in by_first_point[first]:
            if masks[index] & mask:
                continue
            current.append(index)
            if recurse(mask | masks[index]):
                return True
            current.pop()
        return False

    return sorted(current) if recurse(covered) else None


data = carried_literals()
corners = [
    (x, y, z, tick)
    for x in (0, 1)
    for y in (0, 1)
    for z in (0, 1)
    for tick in (0, 1)
]
vertices = np.asarray(corners, dtype=np.int64)
subsets = np.asarray(list(itertools.combinations(range(16), 5)), dtype=np.int64)
edges = vertices[subsets[:, 1:]] - vertices[subsets[:, 0]][:, None, :]
volumes = np.abs(det4_batch(edges))
pieces = subsets[volumes == 1]
inverse = exact_inverses(vertices, pieces)

pair_slots = tuple(itertools.combinations(range(5), 2))
charges = np.zeros(len(pieces), dtype=np.int64)
for a, b in pair_slots:
    separation = np.abs(
        vertices[pieces[:, a], :3] - vertices[pieces[:, b], :3]
    ).sum(axis=1)
    charges += separation > 1

gate(
    "independent cell census",
    len(subsets) == 4368 and len(pieces) == 2672
    and Counter(volumes.tolist()) == Counter({0: 1360, 1: 2672, 2: 320, 3: 16}),
    f"subsets={len(subsets)} minimal={len(pieces)} volumes={sorted(Counter(volumes.tolist()).items())}",
)
gate(
    "independent adjacency-charge census",
    Counter(charges.tolist()) == Counter({3: 64, 4: 384, 5: 1152, 6: 768, 7: 304}),
    repr(sorted(Counter(charges.tolist()).items())),
)

group = make_group(corners)
piece_labels, reps = piece_orbits(pieces, group)
orbit_sizes = np.bincount(piece_labels, minlength=len(reps))
gate(
    "independent carried action and orbit census",
    len(group) == 48 and len(reps) == 57
    and sorted(set(int(x) for x in orbit_sizes)) == [16, 48],
    f"action={len(group)} orbits={len(reps)} sizes={sorted(set(orbit_sizes.tolist()))}",
)

points, point_labels, scale = sample_family(vertices, pieces, group, reps)
matrix, masks, boundary = membership(
    vertices, pieces, inverse, points, point_labels, len(reps), scale
)
point_census = np.bincount(point_labels, minlength=len(reps)).astype(np.int64)
rows = matrix.astype(np.int64)
all_points = (1 << len(points)) - 1
gate(
    "independent generic incidence reconstruction",
    len(points) == 2736 and scale == 12810 and boundary == 0,
    f"points={len(points)} scale={scale} boundary={boundary}",
)


def vector(name: str) -> np.ndarray:
    result = np.zeros(len(reps), dtype=np.int64)
    for index, value in data[name]:
        result[int(index)] = int(value)
    return result


floor_u = vector("FLOOR_U")
floor_d = int(data["FLOOR_D"])
floor_z = int(data["FLOOR_Z"])
floor_slack = floor_d * charges - (rows @ floor_u + floor_z)
floor_value = int((point_census * floor_u).sum()) + 24 * floor_z
support = np.flatnonzero(floor_slack == 0)
support_orbits = sorted(set(int(piece_labels[i]) for i in support))
gate(
    "independent floor-indicator reconstruction",
    floor_value == 108 * floor_d
    and sorted(set(floor_slack.tolist())) == [0, floor_d]
    and len(support) == 1792 and len(support_orbits) == 38,
    f"value={floor_value} slacks={sorted(set(floor_slack.tolist()))} support={len(support)}/{len(support_orbits)}",
)

hostile_floor = floor_d * charges - (rows @ floor_u + floor_z + 1)
gate(
    "hostile floor-constant mutation",
    int(hostile_floor.min()) < 0,
    f"raising the floor constant by one gives least slack {int(hostile_floor.min())}",
)

support_pool = [int(index) for index in support]
completions: list[tuple[int, list[int] | None]] = []
for orbit in support_orbits:
    completion = exact_cover(
        support_pool, masks, all_points, (int(reps[orbit]),),
    )
    completions.append((orbit, completion))
completion_ok = [
    completion is not None
    and is_dissection(vertices, pieces, inverse, masks, completion, all_points)
    and int(charges[np.asarray(completion)].sum()) == 108
    and bool((floor_slack[np.asarray(completion)] == 0).all())
    for _, completion in completions
]
gate(
    "independent support-orbit completion reconstruction",
    all(completion_ok),
    f"valid exact dissection completions={sum(completion_ok)}/{len(completion_ok)}",
)

bits = []
for _, completion in completions:
    assert completion is not None
    value = 0
    for index in completion:
        value |= 1 << support_orbits.index(int(piece_labels[index]))
    bits.append(value)
full_support = (1 << len(support_orbits)) - 1
seeds = [12, 13, 45, 50, 53, 56]
seed_union = 0
for seed in seeds:
    seed_union |= bits[support_orbits.index(seed)]
five_cover = any(
    bits[a] | bits[b] | bits[c] | bits[d] | bits[e] == full_support
    for a, b, c, d, e in itertools.combinations(range(len(bits)), 5)
)
gate(
    "independent stored-completion covering census",
    seed_union == full_support and not five_cover,
    "six named completions cover all 38; zero of 501942 stored-completion five-subsets do",
)

ceil_u = vector("CEIL_U")
ceil_d = int(data["CEIL_D"])
ceil_z = int(data["CEIL_Z"])
ceil_slack = rows @ ceil_u + ceil_z - ceil_d * charges
ceil_value = int((point_census * ceil_u).sum()) + 24 * ceil_z
relation = ((3, 3), (17, 1), (1, -1), (15, -1), (27, -2))
row_residual = sum(coefficient * rows[reps[orbit]] for orbit, coefficient in relation)
charge_combination = sum(
    coefficient * int(charges[reps[orbit]]) for orbit, coefficient in relation
)
gate(
    "independent ceiling and exact row identity",
    int(ceil_slack.min()) == 0 and ceil_value == 128 * ceil_d
    and sorted(set(ceil_slack.tolist())) == [0, 2, 3, 4]
    and bool((row_residual == 0).all()) and charge_combination == -2,
    f"value={ceil_value} slacks={sorted(set(ceil_slack.tolist()))} residual={int(np.abs(row_residual).max())} charge_combo={charge_combination}",
)

rank = integer_rank(rows[reps])
augmented_rank = integer_rank(np.column_stack((rows[reps], np.ones(len(reps), dtype=np.int64))))
gate(
    "independent exact row-span reconstruction",
    rank == 13 and augmented_rank == 13,
    f"row_rank={rank} constant_augmented_rank={augmented_rank}",
)

changed_relation = list(relation)
changed_relation[0] = (3, 4)
hostile_residual = sum(
    coefficient * rows[reps[orbit]] for orbit, coefficient in changed_relation
)
gate(
    "hostile row-identity mutation",
    bool((hostile_residual != 0).any()),
    f"largest mutated residual={int(np.abs(hostile_residual).max())}",
)

ceiling_pool = [int(index) for index in np.flatnonzero(ceil_slack == 0)]
forced_ceiling = []
for orbit in (17, 1, 15, 27):
    completion = exact_cover(
        ceiling_pool, masks, all_points, (int(reps[orbit]),),
    )
    forced_ceiling.append(completion)
forced_ceiling_ok = [
    completion is not None
    and is_dissection(vertices, pieces, inverse, masks, completion, all_points)
    and int(charges[np.asarray(completion)].sum()) == 128
    for completion in forced_ceiling
]
gate(
    "independent forced ceiling-tight completions",
    all(forced_ceiling_ok),
    f"valid cost-128 dissections={sum(forced_ceiling_ok)}/4",
)

s3 = int(ceil_slack[int(reps[3])])
gate(
    "fixed-family denominator and indicator exclusion",
    3 * s3 == 2 * ceil_d and ceil_d == 3 and not any(3 * bit == 2 for bit in (0, 1)),
    f"3*slack(orbit3)={3 * s3}=2D; no binary solution to 3x=2",
)

known = next(completion for completion in forced_ceiling if completion is not None)
mutated = list(known)
mutated[0] = mutated[1]
gate(
    "hostile dissection-duplication mutation",
    not is_dissection(vertices, pieces, inverse, masks, mutated, all_points),
    "duplicating one simplex destroys the exact dissection predicate",
)

outside = np.ones(len(pieces), dtype=np.int64)
outside[support] = 0
identity_ok = all(
    int(charges[np.asarray(completion)].sum())
    == 108 + int(outside[np.asarray(completion)].sum())
    for _, completion in completions
    if completion is not None
)
mutated_outside = outside.copy()
mutated_outside[piece_labels == support_orbits[0]] ^= 1
identity_mutation_detected = any(
    int(charges[np.asarray(completion)].sum())
    != 108 + int(mutated_outside[np.asarray(completion)].sum())
    for _, completion in completions
    if completion is not None
)
gate(
    "independent cost identity and hostile support mutation",
    identity_ok and identity_mutation_detected,
    "all 38 reconstructed floor completions satisfy the identity; an orbit flip breaks it",
)

report = {
    "schema": "physical-cost-identity-indicator-certificate-cycle731-independent-v1",
    "status": "pass" if FAILS == 0 else "fail",
    "claim_type": "bounded_theorem_independent_check",
    "audit_status_authority": "independent audit lane only",
    "pass": PASSES,
    "fail": FAILS,
    "results": RESULTS,
    "supplied_model": {
        "minimal_pieces": len(pieces),
        "carried_action_order": len(group),
        "piece_orbits": len(reps),
        "sample_points": len(points),
    },
    "floor": {
        "value": floor_value,
        "slack_spectrum": sorted(set(int(x) for x in floor_slack)),
        "support_pieces": len(support),
        "support_orbits": len(support_orbits),
        "valid_forced_completions": sum(completion_ok),
    },
    "ceiling_fixed_family": {
        "value": ceil_value,
        "slack_spectrum": sorted(set(int(x) for x in ceil_slack)),
        "row_relation_residual": int(np.abs(row_residual).max()),
        "forced_tight_completions": sum(forced_ceiling_ok),
        "binary_indicator_excluded": True,
    },
    "scope": (
        "supplied one-cell minimal-piece model and fixed generic-incidence certificate "
        "family only; no physical or arbitrary-domain conclusion"
    ),
}
RECEIPT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(report, sort_keys=True), flush=True)
print(f"TOTAL: PASS={PASSES} FAIL={FAILS}", flush=True)
raise SystemExit(0 if FAILS == 0 else 1)
