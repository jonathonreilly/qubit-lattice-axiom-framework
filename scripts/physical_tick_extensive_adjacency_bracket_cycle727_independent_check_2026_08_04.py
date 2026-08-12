"""Independent exact checker for the bounded Cycle-727 two-slab packet.

This checker never imports the primary.  It parses only the primary's carried integer
certificate and witness literals, reconstructs the finite geometry with separate exact
determinant/cofactor code, reruns the primary in a subprocess, and requires the committed
receipt to equal the primary's live receipt.  Any failed gate exits nonzero.
"""
import ast
import hashlib
import json
import subprocess
import sys
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "scripts/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.py",
    "docs/PHYSICAL_TICK_EXTENSIVE_ADJACENCY_BRACKET_CYCLE727_NOTE_2026-08-04.md",
    "outputs/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04_receipt_2026-08-04.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md",
)
ROOT = Path(__file__).resolve().parent.parent
PRIMARY_REL = AUDIT_INPUT_PATHS[0]
PRIMARY = ROOT / PRIMARY_REL
RECEIPT = ROOT / AUDIT_INPUT_PATHS[2]
EXPECTED_PRIMARY_SHA256 = "fad12066154112242965529c99d7b98c6eb4afc2d724d3794314ce7d7cac9173"

GATES = []


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("{0} {1:55s} {2}".format("PASS" if ok else "FAIL", name, detail), flush=True)


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def det4(m):
    total = 0
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        term = 1
        for i in range(4):
            term *= int(m[i][p[i]])
        total += (-1 if inv & 1 else 1) * term
    return total


def adjugate4(m):
    out = np.zeros((4, 4), dtype=np.int64)
    for i in range(4):
        rows = [r for r in range(4) if r != i]
        for j in range(4):
            cols = [c for c in range(4) if c != j]
            minor = [[int(m[r][c]) for c in cols] for r in rows]
            out[j, i] = ((-1) ** (i + j)) * det3(minor)
    return out


def literal(tree, name):
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(t, ast.Name) and t.id == name for t in targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def spectrum(values):
    vals, counts = np.unique(values, return_counts=True)
    return {int(v): int(c) for v, c in zip(vals, counts)}


def corners(slabs):
    return np.array([[x, y, z, t] for t in range(slabs + 1)
                     for x in range(2) for y in range(2) for z in range(2)],
                    dtype=np.int64)


def enumerate_pieces(cor):
    cells = []
    vertices = []
    volumes = []
    costs = []
    spans = []
    for cell in combinations(range(len(cor)), 5):
        v = cor[list(cell)]
        m = (v[1:] - v[0]).tolist()
        d = abs(det4(m))
        volumes.append(d)
        if d == 1:
            cells.append(cell)
            vertices.append(v)
            costs.append(sum(1 for a, b in combinations(range(5), 2)
                             if sum(abs(int(v[a, j]) - int(v[b, j]))
                                    for j in range(3)) > 1))
            spans.append(sum(1 for a, b in combinations(range(5), 2)
                             if abs(int(v[a, 3]) - int(v[b, 3])) > 1))
    return (np.array(cells, dtype=np.int64), np.array(vertices, dtype=np.int64),
            np.array(volumes, dtype=np.int64), np.array(costs, dtype=np.int64),
            np.array(spans, dtype=np.int64))


source = PRIMARY.read_text(encoding="utf-8")
tree = ast.parse(source)
sha = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
gate("primary source is pinned", sha == EXPECTED_PRIMARY_SHA256, sha)
gate("declared checker inputs exist", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS),
     "{0} paths".format(len(AUDIT_INPUT_PATHS)))
if not all(ok for _, ok in GATES):
    print("TOTAL: PASS={0} FAIL={1}".format(sum(ok for _, ok in GATES),
                                            sum(not ok for _, ok in GATES)), flush=True)
    sys.exit(1)

floor_u = np.array(literal(tree, "FLOOR_U"), dtype=np.int64)
floor_z = int(literal(tree, "FLOOR_Z"))
floor_d = int(literal(tree, "FLOOR_D"))
ceil_u = np.array(literal(tree, "CEIL_U"), dtype=np.int64)
ceil_z = int(literal(tree, "CEIL_Z"))
ceil_d = int(literal(tree, "CEIL_D"))
one = literal(tree, "ONE")

cor1, cor2 = corners(1), corners(2)
cell2, v2, vol2, bx2, ts2 = enumerate_pieces(cor2)
cell1, v1, vol1, bx1, ts1 = enumerate_pieces(cor1)
gate("independent exact subset and volume census",
     len(vol2) == 42504 and spectrum(vol2) ==
     {0: 13152, 1: 17280, 2: 9840, 3: 1472, 4: 680, 5: 64, 6: 16},
     "subsets {0}; minimal {1}".format(len(vol2), len(cell2)))
gate("independent exact charge censuses",
     spectrum(bx2) == {3: 432, 4: 2592, 5: 7488, 6: 4896, 7: 1872}
     and spectrum(ts2) == {0: 5344, 1: 1744, 2: 4944, 3: 3040, 4: 2208}
     and int(ts1.max()) == 0,
     "spatial {0}; slab-span {1}".format(sorted(spectrum(bx2).items()),
                                         sorted(spectrum(ts2).items())))

rots = []
for pm in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        r = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(pm):
            r[i, j] = signs[i]
        if det3(r.tolist()) == 1:
            rots.append(r)
index = {tuple(c): i for i, c in enumerate(cor2.tolist())}
group = []
for r in rots:
    for reverse in (False, True):
        image = []
        for c in cor2:
            w = r @ (2 * c[:3] - 1)
            tick = 2 - int(c[3]) if reverse else int(c[3])
            image.append(index[tuple(((w + 1) // 2).tolist() + [tick])])
        group.append(image)
group = np.array(group, dtype=np.int64)
lookup = {tuple(c): i for i, c in enumerate(cell2.tolist())}
orbit = -np.ones(len(cell2), dtype=np.int64)
reps = []
for p in range(len(cell2)):
    if orbit[p] >= 0:
        continue
    label = len(reps)
    reps.append(p)
    for g in group:
        orbit[lookup[tuple(sorted(g[cell2[p]].tolist()))]] = label
sizes = np.bincount(orbit)
gate("independent group and piece-orbit reconstruction",
     len(group) == 48 and len(reps) == 364 and spectrum(sizes) == {16: 6, 48: 358},
     "group 48; orbits 364")

# Independently pinned generic point recipe.  The primary derives this vector from the
# exact global barycentric bound C=6; the checker fixes its resulting public value.
weights = np.array([4802, 4804, 4816, 4900, 5488], dtype=np.int64)
den = int(weights.sum())
points = []
for p in reps:
    q = (weights[:, None] * v2[p]).sum(axis=0)
    for g in range(48):
        spatial = rots[g // 2] @ (2 * q[:3] - den)
        tick = 2 * den - int(q[3]) if g & 1 else int(q[3])
        points.append(((spatial + den) // 2).tolist() + [tick])
points = np.array(points, dtype=np.int64)
gate("independent point-orbit reconstruction",
     len(points) == 17472 and len(np.unique(points, axis=0)) == 17472,
     "17472 distinct integer numerators")

inverse = np.zeros((len(v2), 4, 4), dtype=np.int64)
for i, vertices in enumerate(v2):
    matrix = (vertices[1:] - vertices[0]).T
    determinant = det4(matrix.tolist())
    inverse[i] = adjugate4(matrix) * determinant

bo = np.zeros((len(v2), len(reps)), dtype=np.int64)
boundary = 0
for start in range(0, len(v2), 96):
    stop = min(start + 96, len(v2))
    lam = np.einsum("cij,cpj->cpi", inverse[start:stop],
                    points[None, :, :] - den * v2[start:stop, :1, :])
    total = lam.sum(axis=2)
    inside = ((lam > 0).all(axis=2) & (total < den)).astype(np.int64)
    boundary += int(((lam == 0).any(axis=2) | (total == den)).sum())
    bo[start:stop] = inside.reshape(stop - start, len(reps), 48).sum(axis=2)
gate("independent exact point membership is boundary free", boundary == 0,
     "all 17280 by 17472 incidences checked in integer arithmetic")
gate("uncompressed rows respect the independently built orbits",
     bool((bo == bo[np.array(reps)][orbit]).all()),
     "{0} distinct membership rows".format(len(np.unique(bo, axis=0))))

floor_slack = floor_d * bx2 - (bo @ floor_u + floor_z)
ceil_slack = bo @ ceil_u + ceil_z - ceil_d * bx2
gate("independent floor certificate arithmetic",
     len(floor_u) == 364 and int(floor_slack.min()) == 0
     and int((floor_slack == 0).sum()) == 13392
     and 48 * (int(floor_u.sum()) + floor_z) == 216 * floor_d,
     "least slack {0}; tight {1}".format(int(floor_slack.min()),
                                         int((floor_slack == 0).sum())))
gate("independent ceiling certificate arithmetic",
     len(ceil_u) == 364 and int(ceil_slack.min()) == 0
     and int((ceil_slack == 0).sum()) == 6336
     and 48 * (int(ceil_u.sum()) + ceil_z) == 256 * ceil_d,
     "least slack {0}; tight {1}".format(int(ceil_slack.min()),
                                         int((ceil_slack == 0).sum())))


def stencil(t0):
    result = []
    for order in permutations((4, 2, 1, 8)):
        current = 8 * t0
        path = [current]
        for step in order:
            current += step
            path.append(current)
        result.append(path)
    return result


def witness_cost(cells, cor):
    vertices = cor[np.array(cells, dtype=np.int64)]
    volumes = [abs(det4((v[1:] - v[0]).tolist())) for v in vertices]
    costs = [sum(1 for a, b in combinations(range(5), 2)
                 if sum(abs(int(v[a, j]) - int(v[b, j])) for j in range(3)) > 1)
             for v in vertices]
    normals = [np.array(x, dtype=np.int64)
               for x in product((-1, 0, 1), repeat=4) if any(x)]
    for v in vertices:
        matrix = (v[1:] - v[0]).T
        d = det4(matrix.tolist())
        adj = adjugate4(matrix) * (1 if d > 0 else -1)
        normals.extend(list(adj))
        normals.append(-adj.sum(axis=0))
    separated = 0
    nmat = np.unique(np.array(normals, dtype=np.int64), axis=0)
    for i, j in combinations(range(len(vertices)), 2):
        a = vertices[i] @ nmat.T
        b = vertices[j] @ nmat.T
        separated += int(bool(((a.max(axis=0) <= b.min(axis=0)) |
                               (b.max(axis=0) <= a.min(axis=0))).any()))
    return sum(volumes), sum(costs), separated, len(vertices) * (len(vertices) - 1) // 2


families = [
    (stencil(0) + stencil(1), cor2, 48, 216),
    (one + [[i + 8 for i in c] for c in one], cor2, 48, 256),
    (stencil(0), cor1, 24, 108),
    (one, cor1, 24, 128),
]
observed = [witness_cost(cells, cor) for cells, cor, _, _ in families]
gate("independent exact attaining-witness verification",
     all(volume == 24 * (2 if count == 48 else 1)
         and cost == expected and separated == pairs
         for (volume, cost, separated, pairs), (_, _, count, expected)
         in zip(observed, families)),
     "costs {0}".format([x[1] for x in observed]))

# Hostile mathematical controls exercise different load-bearing mechanisms without
# trusting the primary's named gates.
mutated_costs = np.array([sum(1 for a, b in combinations(range(5), 2)
                              if sum(abs(int(v[a, j]) - int(v[b, j]))
                                     for j in range(3)) > 2) for v in v2])
bad_floor = floor_d * bx2 - (bo @ floor_u + (floor_z + 1))
bad_ceiling_value = 48 * (int(ceil_u.sum()) + ceil_z) == 256 * (ceil_d + 1)
bad_witness = [list(c) for c in (stencil(0) + stencil(1))]
bad_witness[0][0] = bad_witness[0][1]
bad_witness_result = witness_cost(bad_witness, cor2)
gate("hostile cost/certificate/witness controls are rejected",
     spectrum(mutated_costs) != {3: 432, 4: 2592, 5: 7488, 6: 4896, 7: 1872}
     and int(bad_floor.min()) < 0 and not bad_ceiling_value
     and bad_witness_result[0] != 48,
     "spatial threshold, floor constant, ceiling denominator, witness corner")

live = subprocess.run([sys.executable, str(PRIMARY)], cwd=ROOT, text=True,
                      capture_output=True, timeout=AUDIT_TIMEOUT_SEC)
lines = [line[len("RECEIPT "):] for line in live.stdout.splitlines()
         if line.startswith("RECEIPT ")]
live_receipt = json.loads(lines[-1]) if len(lines) == 1 else None
committed_receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
gate("primary direct run is fail-closed green",
     live.returncode == 0 and "TOTAL: PASS=" in live.stdout
     and "FAIL=0" in live.stdout.splitlines()[-1],
     "exit {0}; one terminal verdict".format(live.returncode))
gate("committed receipt equals the live primary receipt",
     live_receipt == committed_receipt,
     "schema and every gate-bound value match")
gate("receipt binds the primary and every declared primary input",
     live_receipt is not None and live_receipt.get("source_sha256") == sha
     and live_receipt.get("input_sha256") == {
         path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
         for path in literal(tree, "AUDIT_INPUT_PATHS")
     }, "source and input SHA-256 map")

npass = sum(ok for _, ok in GATES)
nfail = len(GATES) - npass
print("CHECKER_RECEIPT " + json.dumps({
    "claim_type": "bounded_theorem",
    "primary_sha256": sha,
    "exact_minimal_piece_bracket": [216, 256],
    "independent_membership_rows": int(len(np.unique(bo, axis=0))),
    "hostile_controls": ["spatial_threshold", "floor_constant",
                         "ceiling_denominator", "witness_corner"],
    "gates": {"pass": npass, "fail": nfail},
}, sort_keys=True), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(npass, nfail), flush=True)
sys.exit(0 if nfail == 0 else 1)
