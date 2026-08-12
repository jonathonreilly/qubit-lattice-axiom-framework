"""Independent reconstruction for the bounded Cycle-720 symmetry census.

This checker does not import the Cycle-720 primary.  It constructs signed
permutations and low-endpoint slot maps from transformed edge endpoints, builds
orbits with a graph search, and compares pairwise value-equivalence relations.
It also checks the conditional restriction lemma on an exact integer matrix and
requires perturbed-matrix and wrong-coset controls to fail.
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
from collections import deque
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
COMPILER = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_for_c720_independent", COMPILER)
c696 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c696)

AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 300

TOL_SYM = 1.0e-9
TOL_LEVEL = 1.0e-7
FRAMES = tuple(np.asarray(x, dtype=np.int64) for x in c696.c576.FRAMES)
DIRS = c696.regge.DIRS15
SPATIAL = tuple(c696.SPATIAL_CLASSES)
CLASS_BY_DIRECTION = {
    tuple(abs(int(x)) for x in DIRS[c][:3]): c for c in SPATIAL
}

passed = 0
failed = 0


def check(name: str, condition: bool, detail: str) -> None:
    global passed, failed
    if condition:
        passed += 1
        print("PASS {} {}".format(name, detail))
    else:
        failed += 1
        print("FAIL {} {}".format(name, detail))


def signed_permutation_group() -> tuple[np.ndarray, ...]:
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=np.int64)
            for row, col in enumerate(perm):
                matrix[row, col] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                out.append(matrix)
    return tuple(out)


def axis_permutations() -> tuple[np.ndarray, ...]:
    out = []
    for perm in itertools.permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=np.int64)
        for row, col in enumerate(perm):
            matrix[row, col] = 1
        out.append(matrix)
    return tuple(out)


def slot_map(L: int, rotation: np.ndarray, index: dict) -> np.ndarray:
    """Map each edge slot by transforming both endpoints about the box centre."""
    shift = np.asarray(
        [(L - 1) if np.min(rotation[row]) < 0 else 0 for row in range(3)],
        dtype=np.int64,
    )
    result = np.empty(len(index), dtype=np.int64)
    for (cls, site), source in index.items():
        low = np.asarray(site, dtype=np.int64)
        high = low + np.asarray(DIRS[cls][:3], dtype=np.int64)
        image_low = rotation @ low + shift
        image_high = rotation @ high + shift
        target_low = np.minimum(image_low, image_high)
        target_direction = tuple(abs(int(x)) for x in image_high - image_low)
        target_cls = CLASS_BY_DIRECTION[target_direction]
        result[source] = index[(target_cls, tuple(int(x) for x in target_low))]
    return result


def components(maps: list[np.ndarray], domain: np.ndarray) -> list[list[int]]:
    positions = {int(slot): local for local, slot in enumerate(domain)}
    adjacency = [set() for _ in domain]
    for mapping in maps:
        for local, slot in enumerate(domain):
            other = positions[int(mapping[int(slot)])]
            adjacency[local].add(other)
            adjacency[other].add(local)
    unseen = set(range(len(domain)))
    result = []
    while unseen:
        start = min(unseen)
        queue = deque([start])
        unseen.remove(start)
        comp = []
        while queue:
            node = queue.popleft()
            comp.append(node)
            for other in adjacency[node]:
                if other in unseen:
                    unseen.remove(other)
                    queue.append(other)
        result.append(sorted(comp))
    return result


def equivalence(values: np.ndarray, tol: float) -> list[list[int]]:
    adjacency = [set() for _ in values]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if abs(float(values[i] - values[j])) <= tol:
                adjacency[i].add(j)
                adjacency[j].add(i)
    unseen = set(range(len(values)))
    result = []
    while unseen:
        start = min(unseen)
        queue = deque([start])
        unseen.remove(start)
        comp = []
        while queue:
            node = queue.popleft()
            comp.append(node)
            for other in adjacency[node]:
                if other in unseen:
                    unseen.remove(other)
                    queue.append(other)
        result.append(sorted(comp))
    return sorted(result)


def domains(L: int, inverse_index: dict, size: int) -> list[tuple[str, np.ndarray]]:
    total = np.asarray([
        sum(inverse_index[i][1]) + sum(int(x) for x in DIRS[inverse_index[i][0]][:3])
        for i in range(size)
    ])
    first = np.asarray([
        inverse_index[i][1][0] + int(DIRS[inverse_index[i][0]][0])
        for i in range(size)
    ])
    result = [("full", np.arange(size, dtype=np.int64))]
    result.extend(("corner{}".format(k), np.flatnonzero(total <= k)) for k in (2, 3, 4))
    result.append(("slab", np.flatnonzero(first <= 1)))
    return result


def main() -> int:
    proper = signed_permutation_group()
    keyed = {tuple(x.ravel()): i for i, x in enumerate(proper)}
    compiler_keys = {tuple(x.ravel()) for x in FRAMES}
    check("i01_frame_reconstruction", len(proper) == 24 and set(keyed) == compiler_keys,
          "independently constructed 24 proper signed permutations")

    permutations = axis_permutations()
    group12 = permutations + tuple(-x for x in permutations)
    group12_keys = {tuple(x.ravel()) for x in group12}
    determinant = [int(round(np.linalg.det(x))) for x in group12]
    sextet_matrices = tuple(x for x, det in zip(group12, determinant) if det == 1)
    sextet_keys = {tuple(x.ravel()) for x in sextet_matrices}
    closed = all(tuple((a @ b).ravel()) in group12_keys for a in group12 for b in group12)
    check("i02_group12", len(group12_keys) == 12 and sum(d == 1 for d in determinant) == 6
          and closed and sextet_keys <= compiler_keys,
          "12 distinct, determinant split 6+6, closed, proper kernel is compiler sextet")

    all_rows = 0
    exact_lemma_done = False
    for L in (3, 4, 5):
        index = c696.static_variable_index(L, False)
        inverse_index = {value: key for key, value in index.items()}
        Q = c696.assemble_static_hessian(L, False)["Q"]
        frame_maps = [slot_map(L, frame, index) for frame in FRAMES]
        g12_maps = [slot_map(L, frame, index) for frame in group12]
        frame_index = {tuple(frame.ravel()): i for i, frame in enumerate(FRAMES)}
        sextet = [frame_index[tuple(frame.ravel())] for frame in sextet_matrices]
        centre = slot_map(L, -np.eye(3, dtype=np.int64), index)

        compiler_match = True
        for frame in FRAMES:
            site_map = c696.frame_site_map(L, frame.astype(float))
            shift = np.asarray(
                [(L - 1) if np.min(frame[row]) < 0 else 0 for row in range(3)],
                dtype=np.int64,
            )
            for site, target in site_map.items():
                direct = frame @ np.asarray(site, dtype=np.int64) + shift
                compiler_match &= tuple(int(x) for x in direct) == tuple(target)
        check("i03_endpoint_maps_L{}".format(L), compiler_match
              and all(len(set(mapping.tolist())) == len(index) for mapping in frame_maps),
              "endpoint construction is bijective and site-compatible")

        ambient = max(float(np.max(np.abs(Q[np.ix_(frame_maps[s], frame_maps[s])] - Q)))
                      for s in sextet)
        reflection = float(np.max(np.abs(Q[np.ix_(centre, centre)] - Q)))
        outside = min(float(np.max(np.abs(Q[np.ix_(frame_maps[g], frame_maps[g])] - Q)))
                      for g in range(24) if g not in sextet)
        check("i04_ambient_L{}".format(L), ambient <= TOL_SYM
              and reflection <= TOL_SYM and outside >= 1.0,
              "within {:.3e} reflection {:.3e} outside {:.3e}".format(
                  ambient, reflection, outside))

        if not exact_lemma_done:
            seed = np.arange(len(index) ** 2, dtype=np.int64).reshape(len(index), len(index))
            seed = seed + seed.T
            exact_q = sum((seed[np.ix_(frame_maps[s], frame_maps[s])] for s in sextet),
                          np.zeros_like(seed))
            skew_domain = np.asarray(sorted({0, 2, 3, 7, 11, 19, 23, 31, 43}), dtype=np.int64)
            exact_ok = True
            for g, frame in enumerate(FRAMES):
                for s in sextet:
                    sg = frame_index[tuple((FRAMES[s] @ frame).ravel())]
                    left = exact_q[np.ix_(frame_maps[sg][skew_domain], frame_maps[sg][skew_domain])]
                    right = exact_q[np.ix_(frame_maps[g][skew_domain], frame_maps[g][skew_domain])]
                    exact_ok &= np.array_equal(left, right)
            check("i05_exact_restriction_lemma", exact_ok,
                  "integer-symmetrized matrix, skew nine-slot domain, all 144 (s,g) pairs")
            exact_lemma_done = True

        for name, domain in domains(L, inverse_index, len(index)):
            dset = set(int(x) for x in domain)
            local_maps = []
            local_det = []
            positions = {int(slot): local for local, slot in enumerate(domain)}
            for mapping, det in zip(g12_maps, determinant):
                if {int(mapping[int(slot)]) for slot in domain} != dset:
                    continue
                local = np.asarray([positions[int(mapping[int(slot)])] for slot in domain])
                if np.max(np.abs(Q[np.ix_(domain, domain)][np.ix_(local, local)]
                                 - Q[np.ix_(domain, domain)])) <= TOL_SYM:
                    local_maps.append(mapping)
                    local_det.append(det)
            orbit_partition = sorted(components(local_maps, domain))
            eigenvalues, eigenvectors = np.linalg.eigh(Q[np.ix_(domain, domain)])
            values = np.sum(
                (eigenvectors * eigenvectors) / eigenvalues[np.newaxis, :], axis=1
            )
            value_partition = equivalence(values, TOL_LEVEL)

            assemblies = [Q[np.ix_(mapping[domain], mapping[domain])] for mapping in frame_maps]
            frame_graph = [set() for _ in range(24)]
            for i in range(24):
                for j in range(i + 1, 24):
                    if np.max(np.abs(assemblies[i] - assemblies[j])) <= TOL_SYM:
                        frame_graph[i].add(j)
                        frame_graph[j].add(i)
            unseen = set(range(24))
            frame_components = []
            while unseen:
                start = min(unseen)
                queue = deque([start])
                unseen.remove(start)
                comp = []
                while queue:
                    node = queue.popleft()
                    comp.append(node)
                    for other in frame_graph[node]:
                        if other in unseen:
                            unseen.remove(other)
                            queue.append(other)
                frame_components.append(comp)

            split_ok = sum(x == 1 for x in local_det) == sum(x == -1 for x in local_det) > 0
            partitions_ok = orbit_partition == value_partition
            classes_ok = sorted(len(x) for x in frame_components) == [6, 6, 6, 6]
            check("i06_row_L{}_{}".format(L, name),
                  split_ok and partitions_ok and classes_ok,
                  "sym {}={}+{} levels/orbits {} frames {}".format(
                      len(local_det), sum(x == 1 for x in local_det),
                      sum(x == -1 for x in local_det), len(value_partition),
                      sorted(len(x) for x in frame_components)))
            all_rows += 1

    L = 4
    index = c696.static_variable_index(L, False)
    inverse_index = {value: key for key, value in index.items()}
    Q = c696.assemble_static_hessian(L, False)["Q"].copy()
    domain = domains(L, inverse_index, len(index))[2][1]
    Q[int(domain[0]), int(domain[0])] += 1
    surviving = 0
    for frame in group12:
        mapping = slot_map(L, frame, index)
        if set(mapping[domain].tolist()) != set(domain.tolist()):
            continue
        positions = {int(slot): local for local, slot in enumerate(domain)}
        local = np.asarray([positions[int(mapping[int(slot)])] for slot in domain])
        surviving += int(np.max(np.abs(Q[np.ix_(domain, domain)][np.ix_(local, local)]
                                           - Q[np.ix_(domain, domain)])) <= TOL_SYM)
    check("i07_hostile_bump", surviving < 6,
          "single diagonal mutation leaves {} of 6 symmetries".format(surviving))
    check("i08_row_count", all_rows == 15, "independently checked {} rows".format(all_rows))

    print("TOTAL: PASS={} FAIL={}".format(passed, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
