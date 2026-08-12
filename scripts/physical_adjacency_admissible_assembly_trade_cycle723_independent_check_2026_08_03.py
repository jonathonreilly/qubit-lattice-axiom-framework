"""Independent exact check of the bounded Cycle-723 corner-dissection result.

This checker does not import the primary.  It independently enumerates all
five-corner pieces, all facet tetrahedra, and all pairwise-interior-disjoint
facet covers using exact integer arithmetic.  It also checks the committed
receipt schema and pins the primary source identity.  The floating Cycle-696
matrix measurements remain primary-runner evidence and are not promoted here
to an independent exact result.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "scripts/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.py",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ROOT / AUDIT_INPUT_PATHS[0]
RECEIPT = ROOT / "outputs" / (
    "physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03_"
    "receipt_2026-08-03.json"
)
PRIMARY_SHA256 = "45cc789d0721e329ce6c71c1b78c54490b68ea363ea92d25f675a6eae0800a94"
PINNED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[1]: "2b289407e7cbe339bc25647f829f6831d3e9c1bc09b5dbe15b32ef1246dcea35",
    AUDIT_INPUT_PATHS[2]: "8b82a5129eb098c9f67382340b41d9e931acdeb25991e3f784abd705a91e651b",
    AUDIT_INPUT_PATHS[3]: "dcc397cbdade106d959b4fed41177f4928c8d2d99668b549c31af13ef5f7dcf1",
    AUDIT_INPUT_PATHS[4]: "b5050b0df3d59b713448c399431a5028ea5c28c4c0d63e1a187a431d28a2f31d",
    AUDIT_INPUT_PATHS[5]: "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
}
PASS = 0
FAIL = 0


def gate(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print("[{0}] {1}{2}".format("PASS" if ok else "FAIL", name,
                                (" " + detail) if detail else ""))


def det_int(a: list[list[int]]) -> int:
    """Exact determinant, independently expanded over permutations."""
    n = len(a)
    total = 0
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = -1 if inversions & 1 else 1
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def cross(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, int, int]:
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x * y for x, y in zip(a, b))


def volume4(points: tuple[tuple[int, ...], ...]) -> int:
    return abs(det_int([list(sub(points[i], points[0])) for i in range(1, 5)]))


def volume3(points: tuple[tuple[int, ...], ...]) -> int:
    return abs(dot(sub(points[1], points[0]),
                   cross(sub(points[2], points[0]), sub(points[3], points[0]))))


def weight(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(abs(a[i] - b[i]) for i in range(3))


C4 = tuple(itertools.product((0, 1), repeat=4))
C3 = tuple(itertools.product((0, 1), repeat=3))

pieces = []
spectrum: dict[int, int] = {}
for ids in itertools.combinations(range(16), 5):
    points = tuple(C4[i] for i in ids)
    vol = volume4(points)
    spectrum[vol] = spectrum.get(vol, 0) + 1
    if vol:
        split = sum(p[3] == 0 for p in points)
        excess = sum(weight(points[i], points[j]) > 1
                     for i, j in itertools.combinations(range(5), 2))
        pieces.append((points, vol, split, excess))

floor = {k: min(p[3] for p in pieces if p[2] == k) for k in range(1, 5)}
middle_max = max(p[1] for p in pieces if p[2] in (2, 3))
gate("exact_corner_piece_spectrum",
     spectrum == {0: 1360, 1: 2672, 2: 320, 3: 16} and len(pieces) == 3008,
     "spectrum {0}".format(sorted(spectrum.items())))
gate("exact_piece_floor_by_tick_split", [floor[k] for k in range(1, 5)] == [3, 3, 3, 3])
gate("exact_middle_piece_volume_ceiling", middle_max == 3)


def path_simplices() -> list[tuple[tuple[int, ...], ...]]:
    out = []
    for p in itertools.permutations(range(4)):
        vertices = [[0, 0, 0, 0]]
        for axis in p:
            nxt = list(vertices[-1])
            nxt[axis] = 1
            vertices.append(nxt)
        out.append(tuple(tuple(v) for v in vertices))
    return out


path = path_simplices()
path_cost = [sum(weight(s[i], s[j]) > 1
                 for i, j in itertools.combinations(range(5), 2)) for s in path]
path_split = {k: sorted({path_cost[q] for q, s in enumerate(path)
                         if sum(v[3] == 0 for v in s) == k}) for k in range(1, 5)}
gate("independent_path_stencil", path_split == {1: [5], 2: [4], 3: [4], 4: [5]})

tetra = [t for t in itertools.combinations(C3, 4) if volume3(t)]
volumes = [volume3(t) for t in tetra]
costs = [sum(weight(t[i], t[j]) > 1
             for i, j in itertools.combinations(range(4), 2)) for t in tetra]


def axes(t: tuple[tuple[int, ...], ...]) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    edges = [sub(t[j], t[i]) for i, j in itertools.combinations(range(4), 2)]
    normals = [cross(sub(t[b], t[a]), sub(t[c], t[a]))
               for a, b, c in itertools.combinations(range(4), 3)]
    return edges, normals


axis_data = [axes(t) for t in tetra]


def disjoint(i: int, j: int) -> bool:
    ei, ni = axis_data[i]
    ej, nj = axis_data[j]
    for normal in ni + nj + [cross(a, b) for a in ei for b in ej]:
        if normal == (0, 0, 0):
            continue
        pi = [dot(normal, p) for p in tetra[i]]
        pj = [dot(normal, p) for p in tetra[j]]
        if max(pi) <= min(pj) or max(pj) <= min(pi):
            return True
    return False


separated = {(i, j): disjoint(i, j)
             for i, j in itertools.combinations(range(len(tetra)), 2)}
covers: list[tuple[int, ...]] = []


def search(start: int, chosen: list[int], total_volume: int) -> None:
    if total_volume == 6:
        covers.append(tuple(chosen))
        return
    for i in range(start, len(tetra)):
        if total_volume + volumes[i] <= 6 and all(separated[(j, i)] for j in chosen):
            chosen.append(i)
            search(i + 1, chosen, total_volume + volumes[i])
            chosen.pop()


search(0, [], 0)
facet_floor = min(sum(costs[i] for i in cover) for cover in covers)
cell_floor = 2 * facet_floor + 4 * min(floor[2], floor[3])
gate("exact_facet_census", len(tetra) == 58 and len(covers) == 182
     and sorted({len(c) for c in covers}) == [5, 6])
gate("exact_facet_and_cell_floors", facet_floor == 18 and cell_floor == 48,
     "facet {0}, unit-cell {1}".format(facet_floor, cell_floor))

primary_sha = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
gate("primary_source_pin", primary_sha == PRIMARY_SHA256,
     "observed {0}".format(primary_sha))
observed_inputs = {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                   for path in PINNED_INPUT_SHA256}
gate("supplied_runtime_closure_pins", observed_inputs == PINNED_INPUT_SHA256,
     "all {0} declared supplied inputs match".format(len(observed_inputs)))
try:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
except (OSError, ValueError):
    receipt = {}
gate("primary_receipt_exact_anchors",
     receipt.get("nondegenerate_corner_4_simplices") == 3008
     and receipt.get("facet_corner_dissections") == 182
     and receipt.get("facet_dissection_exceeding_floor") == 18
     and receipt.get("unit_cell_corner_dissection_floor") == 48)
gate("primary_receipt_numerical_scope",
     receipt.get("flat_directions") == {"L3_LT2": 16, "L3_LT3": 24, "L4_LT2": 54}
     and receipt.get("gates", {}).get("fail") == 0
     and float(receipt.get("discarded_mode_gradient_norm", "0")) > 0.0)

print("INDEPENDENT BOUNDARY: exact one-cell corner-piece/facet enumeration only; numerical Cycle-696 rows remain supplied finite evidence")
print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL))
raise SystemExit(1 if FAIL else 0)
