#!/usr/bin/env python3
"""Independent reconstruction of the finite Cycle-721 stencil result.

This checker imports no Cycle-721 implementation. It generates the four-cube
paths from coordinate orders, represents signed permutations by pure integer
(permutation, signs) tuples, transports edge endpoints directly, and reads the
primary receipt only after completing its own calculation.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_for_c721_independent", MODULE)
c696 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c696)

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_STENCIL_DERIVED_CENTRALITY_CYCLE721_NOTE_2026-08-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/PHYSICAL_BODY_DIAGONAL_FRAME_FUNCTIONAL_TRANSVERSAL_LAW_CYCLE717_NOTE_2026-08-02.md",
    "scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py",
    "outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json",
    "docs/PHYSICAL_LEVEL_SET_ORBIT_LAW_IMPROPER_CENTER_IDENTITY_CYCLE719_NOTE_2026-08-02.md",
    "scripts/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02.py",
    "outputs/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02_receipt_2026-08-02.json",
    "docs/PHYSICAL_AMBIENT_DOMAIN_SYMMETRY_SPLIT_CYCLE720_NOTE_2026-08-02.md",
    "scripts/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.py",
    "outputs/physical_ambient_domain_symmetry_split_cycle720_2026_08_02_receipt_2026-08-02.json",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "outputs/physical_stencil_derived_centrality_cycle721_2026_08_02_receipt_2026-08-02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SEXTET = (1, 4, 9, 15, 18, 23)
TOL_REL = 1.0e-8

N_PASS = 0
N_FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global N_PASS, N_FAIL
    if condition:
        N_PASS += 1
        label = "PASS"
    else:
        N_FAIL += 1
        label = "FAIL"
    print(f"{label} {name} {detail}")


def parity(perm: tuple[int, int, int]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def candidates() -> tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]:
    return tuple(
        (tuple(perm), tuple(signs))
        for perm in itertools.permutations(range(3))
        for signs in itertools.product((1, -1), repeat=3)
    )


GROUP = candidates()
IDENTITY = ((0, 1, 2), (1, 1, 1))
SIGMA = ((0, 1, 2), (-1, -1, -1))
MIXED = ((0, 1, 2), (1, 1, -1))


def act(g, vector) -> tuple[int, int, int]:
    perm, signs = g
    return tuple(signs[a] * int(vector[perm[a]]) for a in range(3))


def compose(left, right):
    """Return left after right."""
    lp, ls = left
    rp, rs = right
    return (
        tuple(rp[lp[a]] for a in range(3)),
        tuple(ls[a] * rs[lp[a]] for a in range(3)),
    )


def determinant(g) -> int:
    perm, signs = g
    return parity(perm) * signs[0] * signs[1] * signs[2]


def inverse(g):
    return next(
        h for h in GROUP
        if compose(g, h) == IDENTITY and compose(h, g) == IDENTITY
    )


def from_matrix(matrix) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    array = np.asarray(matrix, dtype=np.int64)
    perm = []
    signs = []
    for row in range(3):
        cols = np.flatnonzero(array[row])
        if len(cols) != 1:
            raise ValueError("matrix is not a signed axis permutation")
        perm.append(int(cols[0]))
        signs.append(int(array[row, cols[0]]))
    return tuple(perm), tuple(signs)


def generated_paths() -> tuple[tuple[tuple[int, int, int, int], ...], ...]:
    paths = []
    for order in itertools.permutations(range(4)):
        vertex = [0, 0, 0, 0]
        path = [tuple(vertex)]
        for axis in order:
            vertex = list(vertex)
            vertex[axis] = 1
            path.append(tuple(vertex))
        paths.append(tuple(path))
    return tuple(paths)


PATHS = generated_paths()


def image_path(path, g):
    return tuple(act(g, vertex[:3]) + (vertex[3],) for vertex in path)


def canonical(path, fold_tick: bool):
    minimum = tuple(min(vertex[axis] for vertex in path) for axis in range(3))
    tick_shifts = range(c696.LT) if fold_tick else (0,)
    forms = []
    for shift in tick_shifts:
        forms.append(tuple(sorted(
            (
                vertex[0] - minimum[0],
                vertex[1] - minimum[1],
                vertex[2] - minimum[2],
                (vertex[3] + shift) % c696.LT if fold_tick else vertex[3],
            )
            for vertex in path
        )))
    return min(forms)


def template_stabilizer(fold_tick: bool):
    target = {canonical(path, fold_tick) for path in PATHS}
    return {
        g for g in GROUP
        if {canonical(image_path(path, g), fold_tick) for path in PATHS} == target
    }


DIRECTIONS = {
    cls: tuple(int(value) for value in c696.regge.DIRS15[cls][:3])
    for cls in c696.SPATIAL_CLASSES
}
CLASS_FOR_DIRECTION = {direction: cls for cls, direction in DIRECTIONS.items()}


def site_image(site, g, size: int):
    _, signs = g
    offset = tuple(size - 1 if sign < 0 else 0 for sign in signs)
    linear = act(g, site)
    return tuple(linear[a] + offset[a] for a in range(3))


def endpoint_slot_map(size: int, g) -> np.ndarray:
    index = c696.static_variable_index(size, False)
    mapping = np.full(len(index), -1, dtype=np.int64)
    for (cls, low), source in index.items():
        direction = DIRECTIONS[cls]
        high = tuple(low[a] + direction[a] for a in range(3))
        first = site_image(low, g, size)
        second = site_image(high, g, size)
        image_low = tuple(min(first[a], second[a]) for a in range(3))
        image_direction = tuple(abs(second[a] - first[a]) for a in range(3))
        mapping[source] = index[(CLASS_FOR_DIRECTION[image_direction], image_low)]
    return mapping


def matrix_classes(matrices: list[np.ndarray], tolerance: float):
    classes = []
    for index, matrix in enumerate(matrices):
        for group in classes:
            if float(np.max(np.abs(matrix - matrices[group[0]]))) <= tolerance:
                group.append(index)
                break
        else:
            classes.append([index])
    return {frozenset(group) for group in classes}


def main() -> int:
    compiler_paths = {
        tuple(tuple(int(value) for value in vertex) for vertex in path)
        for path in c696.regge.cell_simplices((0, 0, 0, 0))
    }
    check(
        "independent.paths",
        set(PATHS) == compiler_paths,
        f"generated={len(PATHS)} compiler={len(compiler_paths)}",
    )

    closure = {compose(left, right) for left in GROUP for right in GROUP}
    check(
        "independent.signed_group",
        len(GROUP) == 48 and closure == set(GROUP),
        f"order={len(GROUP)} products={len(closure)}",
    )

    compiler_frames = tuple(from_matrix(frame) for frame in c696.c576.FRAMES)
    proper_group = {g for g in GROUP if determinant(g) == 1}
    check(
        "independent.proper_frames",
        set(compiler_frames) == proper_group,
        f"compiler={len(compiler_frames)} determinant_one={len(proper_group)}",
    )

    folded = template_stabilizer(True)
    rigid = template_stabilizer(False)
    diagonal = {g for g in GROUP if len(set(act(g, (1, 1, 1)))) == 1}
    unsigned = {g for g in GROUP if g[1] == (1, 1, 1)}
    sign_reversed = {
        (g[0], tuple(-sign for sign in g[1]))
        for g in unsigned
    }
    check("independent.folded_stabilizer", len(folded) == 12, f"order={len(folded)}")
    check(
        "independent.body_diagonal",
        folded == diagonal,
        f"agreement={len(folded & diagonal)}/48",
    )
    check(
        "independent.tick_fixed",
        len(rigid) == 6 and rigid == unsigned,
        f"folded={len(folded)} tick_fixed_unsigned={len(rigid)}",
    )
    check(
        "independent.fold_coset",
        not (unsigned & sign_reversed) and folded == unsigned | sign_reversed,
        f"unsigned={len(unsigned)} sign_reversed={len(sign_reversed)}",
    )
    check(
        "independent.tick_fixed_determinants",
        sum(determinant(g) == 1 for g in rigid) == 3
        and sum(determinant(g) == -1 for g in rigid) == 3,
        "split=3+3",
    )
    check(
        "independent.determinants",
        sum(determinant(g) == 1 for g in folded) == 6
        and sum(determinant(g) == -1 for g in folded) == 6,
        "split=6+6",
    )
    check(
        "independent.subgroup",
        {compose(a, b) for a in folded for b in folded} == folded
        and {inverse(g) for g in folded} == folded,
        "product and inverse closure",
    )

    frame_at = {frame: index for index, frame in enumerate(compiler_frames)}
    proper_stabilizer = folded & proper_group
    sextet = tuple(sorted(frame_at[g] for g in proper_stabilizer))
    check("independent.sextet", sextet == SEXTET, f"indices={sextet}")
    exact_cosets = {
        frozenset(
            j
            for j, right in enumerate(compiler_frames)
            if compose(left, inverse(right)) in proper_stabilizer
        )
        for left in compiler_frames
    }
    check(
        "independent.cosets",
        len(exact_cosets) == 4 and {len(coset) for coset in exact_cosets} == {6},
        f"count={len(exact_cosets)} sizes={sorted({len(c) for c in exact_cosets})}",
    )

    for size in (3, 5):
        maps = {g: endpoint_slot_map(size, g) for g in GROUP}
        nslots = len(next(iter(maps.values())))
        check(
            f"independent.slots.L{size}",
            len({mapping.tobytes() for mapping in maps.values()}) == 48
            and all(
                sorted(mapping.tolist()) == list(range(nslots))
                for mapping in maps.values()
            ),
            f"slots={nslots} distinct={len({m.tobytes() for m in maps.values()})}",
        )
        forward = reverse = 0
        for left in GROUP:
            for right in GROUP:
                product = maps[compose(left, right)]
                forward += int(np.count_nonzero(product - maps[left][maps[right]]))
                reverse += int(np.count_nonzero(product - maps[right][maps[left]]))
        check(
            f"independent.action.L{size}",
            forward == 0 and reverse > 0,
            f"forward={forward} reverse={reverse}",
        )
        central = max(
            int(np.count_nonzero(maps[SIGMA][maps[g]] - maps[g][maps[SIGMA]]))
            for g in GROUP
        )
        mixed = sum(
            int(np.count_nonzero(maps[MIXED][maps[g]] - maps[g][maps[MIXED]])) > 0
            for g in GROUP
        )
        check(
            f"independent.centrality.L{size}",
            central == 0 and mixed == 32,
            f"central_residual={central} mixed_noncommuters={mixed}",
        )
        index = c696.static_variable_index(size, False)
        mismatch = 0
        for (cls, low), source in index.items():
            direction = DIRECTIONS[cls]
            target_low = tuple(
                size - 1 - low[a] - direction[a] for a in range(3)
            )
            mismatch += int(maps[SIGMA][source] != index[(cls, target_low)])
        check(
            f"independent.closed_form.L{size}",
            mismatch == 0,
            f"mismatches={mismatch}",
        )

    for size in (3, 4, 5):
        matrix = c696.assemble_static_hessian(size, False)["Q"]
        maps = {g: endpoint_slot_map(size, g) for g in GROUP}
        residual = {
            g: float(
                np.max(np.abs(matrix[np.ix_(maps[g], maps[g])] - matrix))
            )
            for g in GROUP
        }
        tolerance = TOL_REL * max(1.0, float(np.max(np.abs(matrix))))
        measured = {g for g in GROUP if residual[g] <= tolerance}
        inside = max(residual[g] for g in folded)
        outside = min(residual[g] for g in GROUP if g not in folded)
        check(
            f"independent.assembly_group.L{size}",
            measured == folded,
            f"measured={len(measured)} exact={len(folded)}",
        )
        check(
            f"independent.assembly_margin.L{size}",
            inside < tolerance < outside,
            f"inside={inside:.3e} tolerance={tolerance:.3e} outside={outside:.6f}",
        )
        proper_matrices = [
            matrix[np.ix_(maps[frame], maps[frame])] for frame in compiler_frames
        ]
        measured_classes = matrix_classes(proper_matrices, tolerance)
        check(
            f"independent.frame_cosets.L{size}",
            measured_classes == exact_cosets,
            f"classes={len(measured_classes)} sizes={sorted({len(c) for c in measured_classes})}",
        )

    receipt_path = ROOT / "outputs" / (
        "physical_stencil_derived_centrality_cycle721_2026_08_02_"
        "receipt_2026-08-02.json"
    )
    receipt = json.loads(receipt_path.read_text())
    check(
        "independent.primary_receipt",
        receipt.get("fail") == 0
        and receipt.get("notes", {}).get("stencil_order") == 12
        and receipt.get("notes", {}).get("rigid_order") == 6
        and receipt.get("notes", {}).get("rigid_proper") == 3
        and receipt.get("notes", {}).get("rigid_improper") == 3
        and receipt.get("notes", {}).get("tracked_stencils") == 6,
        "primary finite anchors agree after independent reconstruction",
    )

    print(f"TOTAL: PASS={N_PASS} FAIL={N_FAIL}")
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
