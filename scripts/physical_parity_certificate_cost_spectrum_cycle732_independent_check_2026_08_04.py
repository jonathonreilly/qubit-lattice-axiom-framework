"""Independent exact reconstruction of the supplied finite Cycle-732 theorem.

This checker never imports or executes the primary runner.  It parses only pinned
certificate and witness literals, then separately rebuilds the corner-simplex census,
proper-rotation/tick-flip action, generic point incidence, parity solve, subgroup
enumeration, bounds, modulo-three dual relation, and eleven dissections.  Its parity
certificate is solved in the unrestricted point basis and is intentionally different
from the primary's subgroup-restricted certificate.  Any failed gate exits nonzero.
"""

from __future__ import annotations

import ast
import itertools
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04.py"
C731 = ROOT / "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py"
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md",
    "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py",
    "scripts/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04.py",
    "docs/PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026-08-04.md",
)
AUDIT_TIMEOUT_SEC = 300

PASS = 0
FAIL = 0


def gate(name: str, ok: bool, detail: str) -> None:
    global PASS, FAIL
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def literals(path: Path, wanted: set[str]) -> dict[str, object]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    out: dict[str, object] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            out[target.id] = ast.literal_eval(node.value)
        elif isinstance(target, ast.Tuple) and isinstance(node.value, ast.Tuple):
            names = [item.id for item in target.elts if isinstance(item, ast.Name)]
            values = ([ast.literal_eval(item) for item in node.value.elts]
                      if wanted.intersection(names) else [])
            for name, value in zip(names, values):
                if name in wanted:
                    out[name] = value
    missing = wanted - out.keys()
    if missing:
        raise RuntimeError("missing literals in {0}: {1}".format(path, sorted(missing)))
    return out


WANTED = {
    "WIT", "DUAL", "FLOOR_U", "FLOOR_D", "FLOOR_Z",
    "CEIL_U", "CEIL_D", "CEIL_Z",
}
DATA = literals(PRIMARY, WANTED)
C731_DATA = literals(C731, {"FLOOR_U", "FLOOR_D", "FLOOR_Z", "CEIL_U", "CEIL_D", "CEIL_Z"})
gate(
    "direct Cycle 731 literal binding",
    all(DATA[name] == C731_DATA[name] for name in C731_DATA),
    "all six carried floor/ceiling literals agree exactly",
)

PERMS4 = tuple(itertools.permutations(range(4)))


def parity(perm: tuple[int, ...]) -> int:
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))) % 2 else 1


def det4_batch(mats: np.ndarray) -> np.ndarray:
    out = np.zeros(len(mats), dtype=np.int64)
    rows = np.arange(4)
    for perm in PERMS4:
        out += parity(perm) * np.prod(mats[:, rows, perm], axis=1, dtype=np.int64)
    return out


def exact_inverses(mats: np.ndarray) -> np.ndarray:
    candidates = np.rint(np.linalg.inv(mats.astype(float))).astype(np.int64)
    if not bool((np.einsum("nij,njk->nik", candidates, mats) == np.eye(4, dtype=np.int64)).all()):
        raise RuntimeError("integer inverse candidate failed exact multiplication")
    return candidates


corners = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
vertices = np.asarray(corners, dtype=np.int64)
subsets = np.asarray(list(itertools.combinations(range(16), 5)), dtype=np.int64)
mats_all = np.stack([(vertices[p[1:]] - vertices[p[0]]).T for p in subsets])
volumes = np.abs(det4_batch(mats_all))
pieces = subsets[volumes == 1]
mats = np.stack([(vertices[p[1:]] - vertices[p[0]]).T for p in pieces])
inverse = exact_inverses(mats)
charges = np.zeros(len(pieces), dtype=np.int64)
for a, b in itertools.combinations(range(5), 2):
    charges += np.abs(vertices[pieces[:, a], :3] - vertices[pieces[:, b], :3]).sum(axis=1) > 1
gate(
    "independent cell and charge census",
    len(subsets) == 4368 and len(pieces) == 2672
    and Counter(volumes.tolist()) == Counter({0: 1360, 1: 2672, 2: 320, 3: 16})
    and Counter(charges.tolist()) == Counter({3: 64, 4: 384, 5: 1152, 6: 768, 7: 304}),
    "4,368 subsets; 2,672 unit pieces; charge multiplicities 64/384/1152/768/304",
)


def group_data() -> list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int]]:
    position = {corner: i for i, corner in enumerate(corners)}
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if parity(perm) * math.prod(signs) != 1:
                continue
            for tick_flip in (0, 1):
                image = []
                for corner in corners:
                    centred = [2 * corner[j] - 1 for j in range(3)]
                    mapped = tuple((signs[i] * centred[perm[i]] + 1) // 2 for i in range(3))
                    image.append(position[mapped + (1 - corner[3] if tick_flip else corner[3],)])
                out.append((tuple(image), tuple(perm), tuple(signs), tick_flip))
    return sorted(out)


group = group_data()
piece_lookup = {tuple(int(x) for x in piece): i for i, piece in enumerate(pieces)}
piece_labels = -np.ones(len(pieces), dtype=np.int64)
reps = []
for i, piece in enumerate(pieces):
    if piece_labels[i] >= 0:
        continue
    label = len(reps)
    reps.append(i)
    for image, _, _, _ in group:
        piece_labels[piece_lookup[tuple(sorted(image[int(c)] for c in piece))]] = label
reps = np.asarray(reps, dtype=np.int64)
gate(
    "independent finite action",
    len(group) == 48 and len(reps) == 57
    and sorted(set(np.bincount(piece_labels).tolist())) == [16, 48]
    and all(len(set(charges[piece_labels == o].tolist())) == 1 for o in range(len(reps))),
    "48 elements; 57 charge-constant piece orbits of sizes 16 and 48",
)

offsets = np.asarray((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(offsets.sum()) + 1 + offsets)
scale = int(weights.sum())
labelled: dict[tuple[int, int, int, int], int] = {}
for label, index in enumerate(reps):
    for image, _, _, _ in group:
        moved = (weights[:, None] * vertices[np.asarray(image)[pieces[index]]]).sum(axis=0)
        key = tuple(int(x) for x in moved)
        if labelled.setdefault(key, label) != label:
            raise RuntimeError("point orbit collision")
keys = sorted(labelled)
points = np.asarray(keys, dtype=np.int64)
point_labels = np.asarray([labelled[key] for key in keys], dtype=np.int64)

incidence = np.zeros((len(pieces), len(points)), dtype=np.int8)
masks: list[int] = []
boundary = 0
for i, piece in enumerate(pieces):
    bary = (points - scale * vertices[piece[0]]) @ inverse[i].T
    total = bary.sum(axis=1)
    boundary += int(((bary == 0).any(axis=1) | (total == scale)).sum())
    inside = (bary > 0).all(axis=1) & (total < scale)
    incidence[i] = inside
    mask = 0
    for j in np.flatnonzero(inside):
        mask |= 1 << int(j)
    masks.append(mask)
gate(
    "independent generic incidence",
    len(points) == 2736 and scale == 12810 and boundary == 0
    and (int(incidence.sum(axis=1).min()), int(incidence.sum(axis=1).max())) == (6, 409)
    and (int(incidence.sum(axis=0).min()), int(incidence.sum(axis=0).max())) == (90, 224),
    "2,736 boundary-free points; row loads 6..409 and column loads 90..224",
)


def gf2_solve(row_bits: list[int], target: np.ndarray) -> tuple[int | None, int]:
    basis: dict[int, tuple[int, int]] = {}
    for bits, rhs0 in zip(row_bits, target.tolist()):
        rhs = int(rhs0) & 1
        while bits:
            pivot = (bits & -bits).bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (bits, rhs)
                break
            old, value = basis[pivot]
            bits ^= old
            rhs ^= value
        if bits == 0 and rhs:
            return None, len(basis)
    solution = 0
    for pivot in sorted(basis, reverse=True):
        bits, rhs = basis[pivot]
        rhs ^= ((bits & ~(1 << pivot) & solution).bit_count() & 1)
        if rhs:
            solution |= 1 << pivot
    return solution, len(basis)


solution, rank2 = gf2_solve(masks, charges & 1)
assert solution is not None
parity_ok = all(((mask & solution).bit_count() & 1) == (int(charge) & 1) for mask, charge in zip(masks, charges))
selected = solution.bit_count()
gate(
    "independent unrestricted GF2 certificate",
    rank2 == 465 and parity_ok and selected == 168 and selected % 2 == 0,
    "pure-big-integer elimination gives rank 465 and a distinct even 168-point certificate",
)

# Independently enumerate the subgroup lattice and test invariant solvability in every
# subgroup of order at least 12.  This validates only the fixed point-incidence ansatz.
elements = [row[0] for row in group]
index = {element: i for i, element in enumerate(elements)}
table = [[index[tuple(elements[a][elements[b][i]] for i in range(16))] for b in range(48)] for a in range(48)]
identity = index[tuple(range(16))]


def generated(seed: frozenset[int], extra: int) -> frozenset[int]:
    closed = set(seed) | {extra}
    frontier = [extra]
    while frontier:
        a = frontier.pop()
        for b in list(closed):
            for product in (table[a][b], table[b][a]):
                if product not in closed:
                    closed.add(product)
                    frontier.append(product)
    return frozenset(closed)


subgroups = {frozenset((identity,))}
todo = list(subgroups)
while todo:
    subgroup = todo.pop()
    for extra in range(48):
        if extra in subgroup:
            continue
        joined = generated(subgroup, extra)
        if joined not in subgroups:
            subgroups.add(joined)
            todo.append(joined)

point_position = {tuple(int(x) for x in point): i for i, point in enumerate(points)}
point_perms = []
for _, perm, signs, tick_flip in group:
    moved = np.empty(len(points), dtype=np.int64)
    for i, point in enumerate(points):
        spatial = tuple((signs[j] * (2 * int(point[perm[j]]) - scale) + scale) // 2 for j in range(3))
        key = spatial + (scale - int(point[3]) if tick_flip else int(point[3]),)
        moved[i] = point_position[key]
    point_perms.append(moved)

big = sorted((h for h in subgroups if len(h) >= 12), key=lambda h: (-len(h), sorted(h)))
winners = []
for subgroup in big:
    labels = -np.ones(len(points), dtype=np.int64)
    orbit = 0
    for i in range(len(points)):
        if labels[i] >= 0:
            continue
        for g in subgroup:
            labels[point_perms[g][i]] = orbit
        orbit += 1
    compressed = []
    for row in incidence:
        counts = np.bincount(labels[row.astype(bool)], minlength=orbit) & 1
        bits = 1 << orbit  # constant column
        for j in np.flatnonzero(counts):
            bits |= 1 << int(j)
        compressed.append(bits)
    invariant, _ = gf2_solve(compressed, charges & 1)
    if invariant is not None:
        winners.append((subgroup, orbit, invariant))

order_census = Counter(len(h) for h in big)
gate(
    "independent subgroup-ladder census",
    len(subgroups) == 98 and order_census == Counter({48: 1, 24: 3, 16: 3, 12: 5})
    and len(winners) == 1 and len(winners[0][0]) == 12,
    "98 subgroups; among 12 of order >=12 exactly one order-12 subgroup is soluble",
)


def vector(name: str) -> np.ndarray:
    out = np.zeros(len(reps), dtype=np.int64)
    for i, value in DATA[name]:
        out[int(i)] = int(value)
    return out


orbit_rows = np.zeros((len(pieces), len(reps)), dtype=np.int64)
for orbit in range(len(reps)):
    orbit_rows[:, orbit] = incidence[:, point_labels == orbit].sum(axis=1)
point_census = np.bincount(point_labels, minlength=len(reps)).astype(np.int64)
floor_u, ceil_u = vector("FLOOR_U"), vector("CEIL_U")
floor_d, floor_z = int(DATA["FLOOR_D"]), int(DATA["FLOOR_Z"])
ceil_d, ceil_z = int(DATA["CEIL_D"]), int(DATA["CEIL_Z"])
floor_slack = floor_d * charges - (orbit_rows @ floor_u + floor_z)
ceil_slack = orbit_rows @ ceil_u + ceil_z - ceil_d * charges
floor_value = int(point_census @ floor_u) + 24 * floor_z
ceil_value = int(point_census @ ceil_u) + 24 * ceil_z
gate(
    "independent exact bound certificates",
    int(floor_slack.min()) == 0 and int(ceil_slack.min()) == 0
    and floor_value == 108 * floor_d and ceil_value == 128 * ceil_d,
    "all 2,672 rows hold; values are 108*216 and 128*3",
)

dual = [(int(i), int(c)) for i, c in DATA["DUAL"]]
dual_rows = sum(c * incidence[i].astype(np.int64) for i, c in dual)
dual_charge = sum(c * int(charges[i]) for i, c in dual)
gate(
    "independent fixed-ansatz mod3 dual",
    set(dual_rows.tolist()) == {0, 3} and sum(c for _, c in dual) % 3 == 0
    and dual_charge == 31 and dual_charge % 3 == 1,
    "four-row relation is zero modulo 3 but weighted charge is 31",
)

primitive = []
for normal in itertools.product(range(-4, 5), repeat=4):
    if not any(normal) or math.gcd(*(abs(x) for x in normal)) != 1:
        continue
    first = next(x for x in normal if x)
    if first > 0:
        primitive.append(normal)
normals = np.asarray(primitive, dtype=np.int64)
witnesses = [[(int(a) << 6) + int(b) for a, b in row] for row in DATA["WIT"]]
used = sorted(set(i for witness in witnesses for i in witness))
intervals = {}
for i in used:
    projections = vertices[pieces[i]] @ normals.T
    intervals[i] = (projections.min(axis=0), projections.max(axis=0))


def witness_ok(witness: list[int]) -> tuple[bool, int]:
    separated = 0
    for a, b in itertools.combinations(witness, 2):
        amin, amax = intervals[a]
        bmin, bmax = intervals[b]
        if bool(((amax <= bmin) | (bmax <= amin)).any()):
            separated += 1
    covered = 0
    for i in witness:
        covered |= masks[i]
    once = bool((incidence[np.asarray(witness)].sum(axis=0) == 1).all())
    return len(witness) == len(set(witness)) == 24 and separated == 276 and covered == (1 << len(points)) - 1 and once, separated


witness_results = [witness_ok(witness) for witness in witnesses]
costs = [int(charges[np.asarray(witness)].sum()) for witness in witnesses]
gate(
    "independent broad-normal witness validation",
    len(normals) == 2928 and all(ok for ok, _ in witness_results)
    and costs == list(range(108, 129, 2)),
    "2,928 primitive normals validate all 276 pairs in each of 11 witnesses; costs 108..128",
)
gate(
    "independent exact spectrum deduction",
    selected % 2 == 0 and floor_value // floor_d == 108 and ceil_value // ceil_d == 128
    and costs == list(range(108, 129, 2)),
    "parity plus exact bounds plus attainment leaves exactly eleven even values",
)

bad_floor = floor_d * charges - (orbit_rows @ floor_u + floor_z + 1)
bad_dual = list(dual)
bad_dual[0] = (bad_dual[0][0], bad_dual[0][1] + 1)
bad_dual_rows = sum(c * incidence[i].astype(np.int64) for i, c in bad_dual)
bad_parity = solution ^ 1
gate(
    "hostile independent controls",
    int(bad_floor.min()) < 0 and bool((bad_dual_rows % 3 != 0).any())
    and any(((mask & bad_parity).bit_count() & 1) != (int(charge) & 1) for mask, charge in zip(masks, charges)),
    "tightened floor, mutated dual, and toggled parity certificate all fail closed",
)

print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL), flush=True)
sys.exit(0 if FAIL == 0 else 1)
