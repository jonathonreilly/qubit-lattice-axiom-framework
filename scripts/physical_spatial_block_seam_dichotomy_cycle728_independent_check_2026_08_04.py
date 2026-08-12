"""Independent reconstruction for the supplied finite Cycle-728 block model.

This checker does not import or execute the primary runner.  It reads only the
primary's carried integer witnesses and multiplier vectors from the Python AST,
then rebuilds the corner census, exact determinants, group action, sample-point
incidence matrices, certificate slacks, and invariant-orbit cover census with a
separately written implementation.  A second superincreasing sample chamber is
also checked so the invariant-dissection exclusion is not tied to one point recipe.
"""

from __future__ import annotations

import ast
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py"
NOTE = ROOT / "docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md"
RECEIPT = ROOT / (
    "outputs/physical_spatial_block_seam_dichotomy_cycle728_"
    "independent_check_2026_08_04_receipt_2026-08-04.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py",
    "docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md",
)
AUDIT_TIMEOUT_SEC = 300

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
    wanted = {
        "CELL_UFL", "CELL_ZFL", "CELL_DFL", "CELL_UCL", "CELL_ZCL",
        "CELL_DCL", "CELL_HI", "BLOCK_HI", "BLOCK_UCL", "BLOCK_ZCL",
        "BLOCK_DCL",
    }
    out: dict[str, object] = {}
    tree = ast.parse(PRIMARY.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            out[target.id] = ast.literal_eval(node.value)
    missing = sorted(wanted - out.keys())
    if missing:
        raise RuntimeError("missing carried primary literals: " + repr(missing))
    return out


PERMS4 = tuple(itertools.permutations(range(4)))
SIGNS4 = tuple(
    -1 if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1
    for p in PERMS4
)


def det4_batch(mats: np.ndarray) -> np.ndarray:
    """Exact 4x4 determinant expansion, independent of the primary minors code."""
    out = np.zeros(len(mats), dtype=np.int64)
    rows = np.arange(4)
    for sign, perm in zip(SIGNS4, PERMS4):
        out += sign * np.prod(mats[:, rows, perm], axis=1, dtype=np.int64)
    return out


def det3_batch(mats: np.ndarray) -> np.ndarray:
    return (
        mats[:, 0, 0] * (mats[:, 1, 1] * mats[:, 2, 2]
                         - mats[:, 1, 2] * mats[:, 2, 1])
        - mats[:, 0, 1] * (mats[:, 1, 0] * mats[:, 2, 2]
                           - mats[:, 1, 2] * mats[:, 2, 0])
        + mats[:, 0, 2] * (mats[:, 1, 0] * mats[:, 2, 1]
                           - mats[:, 1, 1] * mats[:, 2, 0])
    )


def volume_only(vertices: np.ndarray, pieces: np.ndarray) -> np.ndarray:
    edges = vertices[pieces[:, 1:]] - vertices[pieces[:, 0]][:, None, :]
    return np.abs(det4_batch(edges))


def volume_and_inverse(vertices: np.ndarray, pieces: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    edges = vertices[pieces[:, 1:]] - vertices[pieces[:, 0]][:, None, :]
    dets = det4_batch(edges)
    if bool((dets == 0).any()):
        raise RuntimeError("inverse requested for a degenerate simplex")
    cof = np.empty_like(edges)
    for i in range(4):
        for j in range(4):
            minor = np.delete(np.delete(edges, i, axis=1), j, axis=2)
            cof[:, i, j] = ((-1) ** (i + j)) * det3_batch(minor)
    # Row-vector coordinates use edges^{-1}; adjugate is cofactor transpose.
    inverse = np.swapaxes(cof, 1, 2)
    inverse = inverse // dets[:, None, None]
    exact = np.einsum("nij,njk->nik", edges, inverse)
    if not bool((exact == np.eye(4, dtype=np.int64)).all()):
        raise RuntimeError("independent exact inverse construction failed")
    return np.abs(dets), inverse


def census(vertices: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    subsets = np.array(list(itertools.combinations(range(len(vertices)), 5)), dtype=np.int64)
    volumes = volume_only(vertices, subsets)
    minimal = subsets[volumes == 1]
    return subsets, volumes, minimal


def charge(vertices: np.ndarray, pieces: np.ndarray, columns: tuple[int, ...]) -> np.ndarray:
    out = np.zeros(len(pieces), dtype=np.int64)
    for a, b in itertools.combinations(range(5), 2):
        delta = np.abs(vertices[pieces[:, a]][:, columns]
                       - vertices[pieces[:, b]][:, columns]).sum(axis=1)
        out += delta > 1
    return out


def determinant3(matrix: np.ndarray) -> int:
    return int(round(np.linalg.det(matrix.astype(float))))


def make_group(corners: list[tuple[int, int, int, int]], centre2: tuple[int, int, int]):
    position = {corner: i for i, corner in enumerate(corners)}
    group = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rotation = np.zeros((3, 3), dtype=np.int64)
            for i, j in enumerate(perm):
                rotation[i, j] = signs[i]
            if determinant3(rotation) != 1:
                continue
            for tick_flip in (0, 1):
                image = []
                for x, y, z, tick in corners:
                    doubled = 2 * np.array((x, y, z), dtype=np.int64)
                    mapped = rotation @ (doubled - centre2) + centre2
                    if bool((mapped % 2).any()):
                        image = []
                        break
                    key = (int(mapped[0] // 2), int(mapped[1] // 2),
                           int(mapped[2] // 2), 1 - tick if tick_flip else tick)
                    if key not in position:
                        image = []
                        break
                    image.append(position[key])
                if image:
                    group.append((rotation, tick_flip, tuple(image)))
    unique = {}
    for item in group:
        unique[item[2]] = item
    return list(unique.values())


def piece_orbits(pieces: np.ndarray, group) -> tuple[np.ndarray, np.ndarray]:
    row = {tuple(int(x) for x in piece): i for i, piece in enumerate(pieces)}
    labels = -np.ones(len(pieces), dtype=np.int64)
    reps = []
    for i, piece in enumerate(pieces):
        if labels[i] >= 0:
            continue
        label = len(reps)
        reps.append(i)
        for _, _, image in group:
            moved = tuple(sorted(image[int(c)] for c in piece))
            labels[row[moved]] = label
    return labels, np.asarray(reps, dtype=np.int64)


def point_family(vertices: np.ndarray, pieces: np.ndarray, group, reps: np.ndarray,
                 offsets: tuple[int, ...], bary_bound: int,
                 centre_numerators) -> tuple[np.ndarray, np.ndarray, int]:
    base = bary_bound * sum(offsets) + 1
    weights = 2 * (base + np.asarray(offsets, dtype=np.int64))
    scale = int(weights.sum())
    labelled: dict[tuple[int, int, int, int], int] = {}
    centre = np.asarray(centre_numerators(scale), dtype=np.int64)
    for label, index in enumerate(reps):
        numerator = (weights[:, None] * vertices[pieces[index]]).sum(axis=0)
        for rotation, tick_flip, _ in group:
            spatial = rotation @ (numerator[:3] - centre) + centre
            key = (int(spatial[0]), int(spatial[1]), int(spatial[2]),
                   scale - int(numerator[3]) if tick_flip else int(numerator[3]))
            previous = labelled.setdefault(key, label)
            if previous != label:
                raise RuntimeError("independent point-family orbit collision")
    keys = sorted(labelled)
    return (np.asarray(keys, dtype=np.int64),
            np.asarray([labelled[key] for key in keys], dtype=np.int64), scale)


def membership(vertices: np.ndarray, pieces: np.ndarray, inverse: np.ndarray,
               points: np.ndarray, point_labels: np.ndarray, orbit_count: int,
               scale: int) -> tuple[np.ndarray, int]:
    matrix = np.zeros((len(pieces), orbit_count), dtype=np.int16)
    boundary = 0
    for i in range(len(pieces)):
        delta = points - scale * vertices[pieces[i, 0]]
        lam = delta @ inverse[i]
        total = lam.sum(axis=1)
        boundary += int(((lam == 0).any(axis=1) | (total == scale)).sum())
        inside = (lam > 0).all(axis=1) & (total < scale)
        matrix[i] = np.bincount(point_labels[inside], minlength=orbit_count)
    return matrix, boundary


def invariant_cover_census(orbit_rows: np.ndarray) -> tuple[int, int]:
    eligible = np.nonzero(orbit_rows.max(axis=1) <= 1)[0]
    target = np.ones(orbit_rows.shape[1], dtype=np.int16)
    lookup = {orbit_rows[index].tobytes(): k for k, index in enumerate(eligible)}
    triples = 0
    for a in range(len(eligible)):
        pair_rows = orbit_rows[eligible[a + 1:]] + orbit_rows[eligible[a]]
        for relative in np.nonzero(pair_rows.max(axis=1) <= 1)[0]:
            third = lookup.get((target - pair_rows[relative]).tobytes())
            if third is not None and third > a + 1 + int(relative):
                triples += 1
    return len(eligible), triples


TERNARY_NORMALS = tuple(
    n for n in itertools.product((-1, 0, 1), repeat=4) if any(n)
)


def separating_count(vertices: np.ndarray, pieces: np.ndarray) -> int:
    points = [vertices[piece] for piece in pieces]
    facets = []
    for piece in pieces:
        edges = (vertices[piece[1:]] - vertices[piece[0]]).T
        inverse = np.rint(np.linalg.inv(edges.astype(float))).astype(np.int64)
        if not bool((inverse @ edges == np.eye(4, dtype=np.int64)).all()):
            raise RuntimeError("witness facet inverse not exact")
        facets.append([inverse[k] for k in range(4)] + [-inverse.sum(axis=0)])
    separated = 0
    for i, j in itertools.combinations(range(len(pieces)), 2):
        for normal in TERNARY_NORMALS + tuple(map(tuple, facets[i] + facets[j])):
            a = points[i] @ normal
            b = points[j] @ normal
            if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                separated += 1
                break
    return separated


def kuhn(position: dict[tuple[int, int, int, int], int]):
    result = []
    for order in itertools.permutations(range(4)):
        vertex = [0, 0, 0, 0]
        path = [tuple(vertex)]
        for coordinate in order:
            vertex[coordinate] += 1
            path.append(tuple(vertex))
        result.append(tuple(sorted(position[p] for p in path)))
    return np.asarray(sorted(result), dtype=np.int64)


data = carried_literals()
corners_block = [(x, y, z, tick) for x in range(3) for y in range(2)
                 for z in range(2) for tick in range(2)]
corners_cell = [(x, y, z, tick) for x in range(2) for y in range(2)
                for z in range(2) for tick in range(2)]
vb = np.asarray(corners_block, dtype=np.int64)
vc = np.asarray(corners_cell, dtype=np.int64)
posb = {corner: i for i, corner in enumerate(corners_block)}
posc = {corner: i for i, corner in enumerate(corners_cell)}

subsets_b, volumes_b, minimal_b = census(vb)
subsets_c, volumes_c, minimal_c = census(vc)
volume_min_b, inverse_b = volume_and_inverse(vb, minimal_b)
volume_min_c, inverse_c = volume_and_inverse(vc, minimal_c)
spatial_b = charge(vb, minimal_b, (0, 1, 2))
transposed_b = charge(vb, minimal_b, (3, 1, 2))
span_b = charge(vb, minimal_b, (0,))
spatial_c = charge(vc, minimal_c, (0, 1, 2))

gate("independent subset and minimal-piece census",
     len(subsets_b) == 42504 and len(minimal_b) == 17280 and len(minimal_c) == 2672,
     f"subsets={len(subsets_b)} block_minimal={len(minimal_b)} cell_minimal={len(minimal_c)}")
gate("independent exact volume spectrum",
     Counter(volumes_b.tolist()) == Counter({0: 13152, 1: 17280, 2: 9840,
                                              3: 1472, 4: 680, 5: 64, 6: 16}),
     repr(sorted(Counter(volumes_b.tolist()).items())))
gate("independent charge ranges",
     (int(spatial_b.min()), int(spatial_b.max()), int(transposed_b.min()),
      int(transposed_b.max()), int(span_b.min()), int(span_b.max())) == (3, 9, 3, 7, 0, 4),
     "spatial=3..9 transposed=3..7 span=0..4")
gate("independent seam split",
     int((span_b == 0).sum()) == 5344 and int((span_b > 0).sum()) == 11936
     and int(spatial_b[span_b == 0].min()) == 3 and int(spatial_b[span_b > 0].min()) == 5,
     "confined=5344 crossing=11936 least charges=3/5")

group_b = make_group(corners_block, (2, 1, 1))
labels_b, reps_b = piece_orbits(minimal_b, group_b)
sizes_b = np.bincount(labels_b, minlength=len(reps_b))
gate("independent carried group and orbit reconstruction",
     len(group_b) == 16 and len(reps_b) == 1080 and int(sizes_b.min()) == 16
     and int(sizes_b.max()) == 16,
     f"group={len(group_b)} orbits={len(reps_b)} size={int(sizes_b.min())}")

points_b, point_labels_b, scale_b = point_family(
    vb, minimal_b, group_b, reps_b, (0, 1, 7, 49, 343), 6,
    lambda scale: (scale, scale // 2, scale // 2),
)
matrix_b, boundary_b = membership(
    vb, minimal_b, inverse_b, points_b, point_labels_b, len(reps_b), scale_b
)
point_sizes_b = np.bincount(point_labels_b, minlength=len(reps_b))
ubl = np.asarray(data["BLOCK_UCL"], dtype=np.int64)
block_slack = matrix_b.astype(np.int64) @ ubl + int(data["BLOCK_ZCL"])
block_slack -= int(data["BLOCK_DCL"]) * spatial_b
block_numerator = int((point_sizes_b * ubl).sum()) + 48 * int(data["BLOCK_ZCL"])
gate("independent block ceiling certificate reconstruction",
     boundary_b == 0 and int(block_slack.min()) == 0
     and block_numerator == 3888 and block_numerator // int(data["BLOCK_DCL"]) == 324,
     f"boundary={boundary_b} least_slack={int(block_slack.min())} bound=324")
gate("hostile block-ceiling constant mutation",
     int((matrix_b.astype(np.int64) @ ubl + int(data["BLOCK_ZCL"]) - 1
          - int(data["BLOCK_DCL"]) * spatial_b).min()) < 0,
     "lowering the carried ceiling constant by one violates an exact piece inequality")

orbit_rows_b = matrix_b[reps_b]
eligible_primary, triples_primary = invariant_cover_census(orbit_rows_b)
gate("independent invariant-cover census in primary sample chamber",
     eligible_primary == 23 and triples_primary == 0,
     f"eligible={eligible_primary} exact_cover_triples={triples_primary}")

points_2, labels_2, scale_2 = point_family(
    vb, minimal_b, group_b, reps_b, (0, 1, 11, 121, 1331), 6,
    lambda scale: (scale, scale // 2, scale // 2),
)
matrix_2, boundary_2 = membership(
    vb, minimal_b, inverse_b, points_2, labels_2, len(reps_b), scale_2
)
eligible_2, triples_2 = invariant_cover_census(matrix_2[reps_b])
gate("second-chamber invariant-cover reconstruction",
     boundary_2 == 0 and eligible_2 == 23 and triples_2 == 0,
     f"boundary={boundary_2} eligible={eligible_2} exact_cover_triples={triples_2}")

group_c = make_group(corners_cell, (1, 1, 1))
labels_c, reps_c = piece_orbits(minimal_c, group_c)
points_c, point_labels_c, scale_c = point_family(
    vc, minimal_c, group_c, reps_c, (0, 1, 7, 49, 343), 3,
    lambda scale: (scale // 2, scale // 2, scale // 2),
)
matrix_c, boundary_c = membership(
    vc, minimal_c, inverse_c, points_c, point_labels_c, len(reps_c), scale_c
)
point_sizes_c = np.bincount(point_labels_c, minlength=len(reps_c))
ufl = np.asarray(data["CELL_UFL"], dtype=np.int64)
ucl = np.asarray(data["CELL_UCL"], dtype=np.int64)
floor_slack = int(data["CELL_DFL"]) * spatial_c
floor_slack -= matrix_c.astype(np.int64) @ ufl + int(data["CELL_ZFL"])
ceiling_slack = matrix_c.astype(np.int64) @ ucl + int(data["CELL_ZCL"])
ceiling_slack -= int(data["CELL_DCL"]) * spatial_c
floor_numerator = int((point_sizes_c * ufl).sum()) + 24 * int(data["CELL_ZFL"])
ceiling_numerator = int((point_sizes_c * ucl).sum()) + 24 * int(data["CELL_ZCL"])
gate("independent one-cell certificate reconstruction",
     boundary_c == 0 and int(floor_slack.min()) == 0 and int(ceiling_slack.min()) == 0
     and floor_numerator // int(data["CELL_DFL"]) == 108
     and ceiling_numerator // int(data["CELL_DCL"]) == 128,
     "zero boundaries and exact certificate bracket [108,128]")
gate("hostile one-cell certificate mutations",
     int((floor_slack - 1).min()) < 0 and int((ceiling_slack - 1).min()) < 0,
     "one-unit strengthening crosses both zero-slack certificate surfaces")

cell_low = kuhn(posc)
cell_high = np.asarray(sorted(tuple(row) for row in data["CELL_HI"]), dtype=np.int64)


def lift(cell_pieces: np.ndarray, offset: int) -> list[tuple[int, ...]]:
    return [tuple(sorted(posb[(int(vc[c, 0]) + offset, int(vc[c, 1]),
                               int(vc[c, 2]), int(vc[c, 3]))] for c in piece))
            for piece in cell_pieces]


block_low = np.asarray(sorted(lift(cell_low, 0) + lift(cell_low, 1)), dtype=np.int64)
block_seam_high = np.asarray(sorted(lift(cell_high, 0) + lift(cell_high, 1)), dtype=np.int64)
block_318 = np.asarray(sorted(tuple(row) for row in data["BLOCK_HI"]), dtype=np.int64)


def witness_summary(pieces: np.ndarray):
    vols, _ = volume_and_inverse(vb, pieces)
    return {
        "unit": bool((vols == 1).all()),
        "volume": int(vols.sum()),
        "separated": separating_count(vb, pieces),
        "pairs": len(pieces) * (len(pieces) - 1) // 2,
        "spatial": int(charge(vb, pieces, (0, 1, 2)).sum()),
        "transposed": int(charge(vb, pieces, (3, 1, 2)).sum()),
        "crossing": int((charge(vb, pieces, (0,)) > 0).sum()),
    }


low_summary = witness_summary(block_low)
seam_high_summary = witness_summary(block_seam_high)
high_summary = witness_summary(block_318)
gate("independent exact witness reconstruction",
     all(item["unit"] and item["volume"] == 48 and item["separated"] == item["pairs"]
         for item in (low_summary, seam_high_summary, high_summary)),
     "all three carried 48-piece families are exact interior-disjoint covers")
gate("independent witness charges and seam counts",
     (low_summary["spatial"], seam_high_summary["spatial"], high_summary["spatial"],
      high_summary["transposed"], high_summary["crossing"]) == (216, 256, 318, 238, 31),
     "spatial=216/256/318 transposed(318)=238 crossings(318)=31")
mutated = block_318.copy()
mutated[0] = mutated[1]
gate("hostile witness duplication mutation",
     separating_count(vb, mutated) < len(mutated) * (len(mutated) - 1) // 2,
     "duplicating one simplex destroys pairwise interior disjointness")
gate("seam-maximizer exclusion inequality",
     high_summary["spatial"] > 2 * 128,
     "attained 318 exceeds the independently reconstructed seam-respecting ceiling 256")

report = {
    "schema": "physical-spatial-block-seam-dichotomy-cycle728-independent-v1",
    "status": "pass" if FAILS == 0 else "fail",
    "pass": PASSES,
    "fail": FAILS,
    "results": RESULTS,
    "primary_sample_chamber": {
        "points": len(points_b), "boundary_incidences": boundary_b,
        "eligible_orbits": eligible_primary, "exact_cover_triples": triples_primary,
    },
    "second_sample_chamber": {
        "points": len(points_2), "boundary_incidences": boundary_2,
        "eligible_orbits": eligible_2, "exact_cover_triples": triples_2,
    },
    "global_maximum_window": [318, 324],
    "global_floor_status": "open; 216 independently confirmed as attained",
}
RECEIPT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(report, sort_keys=True), flush=True)
print(f"TOTAL: PASS={PASSES} FAIL={FAILS}", flush=True)
raise SystemExit(0 if FAILS == 0 else 1)
