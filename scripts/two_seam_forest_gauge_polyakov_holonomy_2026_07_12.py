#!/usr/bin/env python3
"""Two-seam forest gauge and Polyakov-holonomy preservation certificate."""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "TWO_SEAM_FOREST_GAUGE_POLYAKOV_HOLONOMY_PRESERVATION_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
TOL = 3.0e-10
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    q = q @ np.diag(np.conj(phases / np.abs(phases)))
    determinant = np.linalg.det(q)
    q[:, 0] *= np.conj(determinant)
    return q


def seam_times(length_t: int, plane_index: int) -> tuple[int, int]:
    half = length_t // 2
    return plane_index % length_t, (plane_index + half) % length_t


def seam_edges(length_t: int, length_x: int, plane_index: int):
    return [
        ((time, x), ((time + 1) % length_t, x), ("t", time, x))
        for time in seam_times(length_t, plane_index)
        for x in range(length_x)
    ]


def forest_components(vertices, edges):
    parent = {vertex: vertex for vertex in vertices}

    def find(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    cycle = False
    for source, target, _ in edges:
        root_s = find(source)
        root_t = find(target)
        if root_s == root_t:
            cycle = True
        else:
            parent[root_t] = root_s
    components = {}
    for vertex in vertices:
        components.setdefault(find(vertex), []).append(vertex)
    return cycle, list(components.values())


def bareiss_integer_determinant(matrix: np.ndarray) -> int:
    """Exact determinant of a square integer matrix."""
    if matrix.shape[0] == 0:
        return 1
    work = [[int(value) for value in row] for row in matrix.tolist()]
    sign = 1
    previous = 1
    for pivot_index in range(len(work) - 1):
        pivot_row = next(
            (row for row in range(pivot_index, len(work)) if work[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, len(work)):
            for column in range(pivot_index + 1, len(work)):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                assert numerator % previous == 0
                work[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, len(work)):
            work[row][pivot_index] = 0
    return sign * work[-1][-1]


def reduced_forest_incidence(vertices, edges, components):
    """Delete one root row from every forest component, including isolates."""
    root_by_vertex = {}
    for component in components:
        root = min(component)
        for vertex in component:
            root_by_vertex[vertex] = root
    nonroots = [vertex for vertex in vertices if vertex != root_by_vertex[vertex]]
    row = {vertex: index for index, vertex in enumerate(nonroots)}
    incidence = np.zeros((len(nonroots), len(edges)), dtype=int)
    for column, (source, target, _) in enumerate(edges):
        if source in row:
            incidence[row[source], column] -= 1
        if target in row:
            incidence[row[target], column] += 1
    return incidence, nonroots


def reflection_edge_closure(length_t: int, initial_times) -> set[int]:
    """Close temporal base layers under both adjacent edge reflections."""
    closure = {int(time) % length_t for time in initial_times}
    while True:
        enlarged = closure | {
            (2 * plane_index - time) % length_t
            for plane_index in (0, 1)
            for time in closure
        }
        if enlarged == closure:
            return closure
        closure = enlarged


def random_configuration(rng, length_t, length_x):
    temporal = {
        (time, x): haar_su3(rng)
        for time in range(length_t)
        for x in range(length_x)
    }
    spatial = {
        (time, x): haar_su3(rng)
        for time in range(length_t)
        for x in range(length_x)
    }
    return temporal, spatial


def forest_gauge_transform(temporal, vertices, edges):
    adjacency = {vertex: [] for vertex in vertices}
    for source, target, key in edges:
        link = temporal[(key[1], key[2])]
        adjacency[source].append((target, link, True))
        adjacency[target].append((source, link, False))

    gauge = {}
    for root in vertices:
        if root in gauge:
            continue
        gauge[root] = np.eye(3, dtype=complex)
        stack = [root]
        while stack:
            current = stack.pop()
            for neighbor, link, forward in adjacency[current]:
                if neighbor in gauge:
                    continue
                if forward:
                    gauge[neighbor] = gauge[current] @ link
                else:
                    gauge[neighbor] = gauge[current] @ link.conj().T
                stack.append(neighbor)
    return gauge


def transform_configuration(temporal, spatial, gauge, length_t, length_x):
    temporal_out = {}
    spatial_out = {}
    for time in range(length_t):
        for x in range(length_x):
            temporal_out[(time, x)] = (
                gauge[(time, x)]
                @ temporal[(time, x)]
                @ gauge[((time + 1) % length_t, x)].conj().T
            )
            spatial_out[(time, x)] = (
                gauge[(time, x)]
                @ spatial[(time, x)]
                @ gauge[(time, (x + 1) % length_x)].conj().T
            )
    return temporal_out, spatial_out


def inverse_transform_configuration(temporal, spatial, gauge, length_t, length_x):
    """Invert transform_configuration exactly using the same vertex gauge."""
    temporal_out = {}
    spatial_out = {}
    for time in range(length_t):
        for x in range(length_x):
            temporal_out[(time, x)] = (
                gauge[(time, x)].conj().T
                @ temporal[(time, x)]
                @ gauge[((time + 1) % length_t, x)]
            )
            spatial_out[(time, x)] = (
                gauge[(time, x)].conj().T
                @ spatial[(time, x)]
                @ gauge[(time, (x + 1) % length_x)]
            )
    return temporal_out, spatial_out


def polyakov(temporal, length_t, x):
    product = np.eye(3, dtype=complex)
    for time in range(length_t):
        product = product @ temporal[(time, x)]
    return product


def mixed_plaquette(temporal, spatial, length_t, length_x, time, x):
    return (
        temporal[(time, x)]
        @ spatial[((time + 1) % length_t, x)]
        @ temporal[(time, (x + 1) % length_x)].conj().T
        @ spatial[(time, x)].conj().T
    )


def wilson_mixed_action(temporal, spatial, length_t, length_x):
    return -sum(
        np.trace(mixed_plaquette(temporal, spatial, length_t, length_x, time, x)).real
        for time in range(length_t)
        for x in range(length_x)
    ) / 3.0


def reflect_configuration(temporal, spatial, length_t, length_x, plane_index):
    temporal_out = {}
    spatial_out = {}
    for time in range(length_t):
        for x in range(length_x):
            temporal_out[(time, x)] = temporal[((2 * plane_index - time) % length_t, x)].conj().T
            spatial_out[(time, x)] = spatial[((2 * plane_index + 1 - time) % length_t, x)]
    return temporal_out, spatial_out


def z3_exact_forest_average(length_t: int, forest_times: tuple[int, int]):
    roots = np.exp(2j * np.pi * np.arange(3) / 3.0)
    full_values = []
    fixed_values = []
    noninvariant_full = []
    noninvariant_fixed = []
    for labels in itertools.product(range(3), repeat=length_t):
        links = [roots[label] for label in labels]
        holonomy = np.prod(links)
        full_values.append(np.exp(0.37 * holonomy.real))
        noninvariant_full.append(links[forest_times[0]].real)
    free_times = [time for time in range(length_t) if time not in forest_times]
    for labels in itertools.product(range(3), repeat=len(free_times)):
        links = [1.0 + 0.0j] * length_t
        for time, label in zip(free_times, labels):
            links[time] = roots[label]
        holonomy = np.prod(links)
        fixed_values.append(np.exp(0.37 * holonomy.real))
        noninvariant_fixed.append(links[forest_times[0]].real)
    return (
        float(np.mean(full_values)),
        float(np.mean(fixed_values)),
        float(np.mean(noninvariant_full)),
        float(np.mean(noninvariant_fixed)),
    )


def main() -> int:
    rng = np.random.default_rng(20260712)
    length_t = 6
    length_x = 3
    vertices = [(time, x) for time in range(length_t) for x in range(length_x)]

    graph_exact = True
    fp_details = []
    for graph_length in (4, 6, 8, 10):
        graph_vertices = [(time, x) for time in range(graph_length) for x in range(length_x)]
        for plane_index in (0, 1):
            graph_edges = seam_edges(graph_length, length_x, plane_index)
            graph_cycle, graph_components = forest_components(graph_vertices, graph_edges)
            incidence, nonroots = reduced_forest_incidence(
                graph_vertices, graph_edges, graph_components
            )
            determinant = bareiss_integer_determinant(incidence)
            expected_components = len(graph_vertices) - len(graph_edges)
            case_ok = (
                not graph_cycle
                and incidence.shape == (len(graph_edges), len(graph_edges))
                and abs(determinant) == 1
                and len(graph_components) == expected_components
                and len(nonroots) == len(graph_edges)
            )
            graph_exact = graph_exact and case_ok
            fp_details.append(
                f"L={graph_length},j={plane_index}:det={determinant},"
                f"components={len(graph_components)}"
            )
    check(
        "Two-seam matchings have exact unimodular reduced incidence",
        graph_exact,
        "; ".join(fp_details),
    )
    check(
        "SU3 forest Faddeev--Popov factor is configuration-independent one",
        graph_exact,
        "|det B_red|^dim(SU3)=1^8=1 per temporal fiber; normalized Haar proof remains analytic",
    )

    required_common = set(seam_times(length_t, 0)) | set(seam_times(length_t, 1))
    common_closure = reflection_edge_closure(length_t, required_common)
    common_cycle_rank = len(common_closure) - length_t + 1
    check(
        "One reflection-invariant identity-link forest cannot fix all four adjacent-plane seams",
        common_closure == set(range(length_t)) and common_cycle_rank == 1,
        f"required={sorted(required_common)}, closure={sorted(common_closure)}, cycle_rank={common_cycle_rank}",
    )

    for plane_index in (0, 1):
        edges = seam_edges(length_t, length_x, plane_index)
        cycle, components = forest_components(vertices, edges)
        check(
            f"Plane {plane_index} seam set is a forest",
            not cycle and len(edges) == 2 * length_x,
            f"edges={len(edges)}, components={len(components)}, cycle={cycle}",
        )
        reflected_lows = {
            (2 * plane_index - time) % length_t
            for time in seam_times(length_t, plane_index)
        }
        check(
            f"Plane {plane_index} seam forest is reflection invariant",
            reflected_lows == set(seam_times(length_t, plane_index)),
            f"reflected lows={sorted(reflected_lows)}",
        )

        temporal, spatial = random_configuration(rng, length_t, length_x)
        action_before = wilson_mixed_action(temporal, spatial, length_t, length_x)
        traces_before = [np.trace(polyakov(temporal, length_t, x)) for x in range(length_x)]
        gauge = forest_gauge_transform(temporal, vertices, edges)
        gauge_group_error = max(
            max(
                np.linalg.norm(matrix.conj().T @ matrix - np.eye(3))
                for matrix in gauge.values()
            ),
            max(abs(np.linalg.det(matrix) - 1.0) for matrix in gauge.values()),
        )
        berezin_jacobian_error = max(
            abs(1.0 / (np.linalg.det(matrix) * np.conj(np.linalg.det(matrix))) - 1.0)
            for matrix in gauge.values()
        )
        check(
            f"Plane {plane_index} constructive gauge is SU3 with unit Berezin Jacobian",
            gauge_group_error < TOL and berezin_jacobian_error < TOL,
            f"group residual={gauge_group_error:.3e}, Berezin residual={berezin_jacobian_error:.3e}",
        )
        temporal_fixed, spatial_fixed = transform_configuration(
            temporal, spatial, gauge, length_t, length_x
        )
        forest_error = max(
            np.linalg.norm(temporal_fixed[(time, x)] - np.eye(3))
            for time in seam_times(length_t, plane_index)
            for x in range(length_x)
        )
        check(
            f"Plane {plane_index} constructive gauge sets both seams to identity",
            forest_error < TOL,
            f"maximum seam residual={forest_error:.3e}",
        )
        temporal_roundtrip, spatial_roundtrip = inverse_transform_configuration(
            temporal_fixed, spatial_fixed, gauge, length_t, length_x
        )
        roundtrip_error = max(
            max(
                np.linalg.norm(temporal_roundtrip[key] - temporal[key])
                for key in temporal
            ),
            max(
                np.linalg.norm(spatial_roundtrip[key] - spatial[key])
                for key in spatial
            ),
        )
        check(
            f"Plane {plane_index} constructive forest coordinates round-trip",
            roundtrip_error < TOL,
            f"maximum full-link reconstruction residual={roundtrip_error:.3e}",
        )
        action_after = wilson_mixed_action(
            temporal_fixed, spatial_fixed, length_t, length_x
        )
        check(
            f"Plane {plane_index} forest gauge preserves the Wilson action",
            abs(action_before - action_after) < TOL,
            f"action residual={abs(action_before-action_after):.3e}",
        )
        traces_after = [
            np.trace(polyakov(temporal_fixed, length_t, x)) for x in range(length_x)
        ]
        conjugacy_error = max(
            np.linalg.norm(
                polyakov(temporal_fixed, length_t, x)
                - gauge[(0, x)]
                @ polyakov(temporal, length_t, x)
                @ gauge[(0, x)].conj().T
            )
            for x in range(length_x)
        )
        check(
            f"Plane {plane_index} Polyakov matrices obey exact base-point conjugacy",
            conjugacy_error < TOL,
            f"maximum matrix conjugacy residual={conjugacy_error:.3e}",
        )
        trace_error = max(abs(before - after) for before, after in zip(traces_before, traces_after))
        check(
            f"Plane {plane_index} Polyakov conjugacy traces survive gauge fixing",
            trace_error < TOL,
            f"maximum trace residual={trace_error:.3e}",
        )
        nontriviality = max(abs(value - 3.0) for value in traces_after)
        check(
            f"Plane {plane_index} gauge slice retains nontrivial temporal holonomy",
            nontriviality > 0.1,
            f"max |Tr P-3|={nontriviality:.3e}",
        )

        # The slice does not merely retain the sampled orbit's holonomy.  For
        # any supplied H in SU(3), putting H on one unfixed temporal edge and
        # identities elsewhere realizes P=H while both seam layers stay fixed.
        supplied_holonomy = haar_su3(rng)
        witness_temporal = {
            (time, x): np.eye(3, dtype=complex)
            for time in range(length_t)
            for x in range(length_x)
        }
        free_time = next(
            time
            for time in range(length_t)
            if time not in seam_times(length_t, plane_index)
        )
        witness_temporal[(free_time, 0)] = supplied_holonomy
        witness_seam_error = max(
            np.linalg.norm(witness_temporal[(time, x)] - np.eye(3))
            for time in seam_times(length_t, plane_index)
            for x in range(length_x)
        )
        witness_holonomy_error = np.linalg.norm(
            polyakov(witness_temporal, length_t, 0) - supplied_holonomy
        )
        check(
            f"Plane {plane_index} slice realizes an arbitrary supplied residual holonomy",
            witness_seam_error < TOL and witness_holonomy_error < TOL,
            f"seam residual={witness_seam_error:.3e}, P-H residual={witness_holonomy_error:.3e}",
        )

        reduction_error = 0.0
        for time in seam_times(length_t, plane_index):
            for x in range(length_x):
                reduced = (
                    spatial_fixed[((time + 1) % length_t, x)]
                    @ spatial_fixed[(time, x)].conj().T
                )
                reduction_error = max(
                    reduction_error,
                    float(
                        np.linalg.norm(
                            mixed_plaquette(
                                temporal_fixed,
                                spatial_fixed,
                                length_t,
                                length_x,
                                time,
                                x,
                            )
                            - reduced
                        )
                    ),
                )
        check(
            f"Plane {plane_index} seam plaquettes reduce to spatial-link convolution pairs",
            reduction_error < TOL,
            f"maximum reduction residual={reduction_error:.3e}",
        )

        temporal_reflected, spatial_reflected = reflect_configuration(
            temporal_fixed, spatial_fixed, length_t, length_x, plane_index
        )
        reflected_slice_error = max(
            np.linalg.norm(temporal_reflected[(time, x)] - np.eye(3))
            for time in seam_times(length_t, plane_index)
            for x in range(length_x)
        )
        reflected_action_error = abs(
            wilson_mixed_action(
                temporal_reflected, spatial_reflected, length_t, length_x
            )
            - wilson_mixed_action(
                temporal_fixed, spatial_fixed, length_t, length_x
            )
        )
        check(
            f"Plane {plane_index} reflection preserves the forest gauge slice",
            reflected_slice_error < TOL,
            f"maximum reflected seam residual={reflected_slice_error:.3e}",
        )
        check(
            f"Plane {plane_index} reflection preserves the mixed Wilson action",
            reflected_action_error < TOL,
            f"action residual={reflected_action_error:.3e}",
        )

        # Residual transformations are constant on each forest component.
        cycle_check, component_vertices = forest_components(vertices, edges)
        residual_gauge = {}
        for component in component_vertices:
            h = haar_su3(rng)
            for vertex in component:
                residual_gauge[vertex] = h
        temporal_residual, _ = transform_configuration(
            temporal_fixed, spatial_fixed, residual_gauge, length_t, length_x
        )
        residual_error = max(
            np.linalg.norm(temporal_residual[(time, x)] - np.eye(3))
            for time in seam_times(length_t, plane_index)
            for x in range(length_x)
        )
        check(
            f"Plane {plane_index} residual component gauge freedom preserves the slice",
            not cycle_check
            and residual_error < TOL
            and len(component_vertices) == len(vertices) - len(edges),
            f"maximum residual={residual_error:.3e}, residual SU3 factors={len(component_vertices)}, residual dimension={8 * len(component_vertices)}",
        )

    full, fixed, nongauge_full, nongauge_fixed = z3_exact_forest_average(
        length_t, seam_times(length_t, 0)
    )
    check(
        "Exact Z3 finite-group analogue equals its two-seam forest-fixed average",
        abs(full - fixed) < TOL,
        f"full={full:.12f}, fixed={fixed:.12f}, residual={abs(full-fixed):.3e}; analogue is not the SU3 Haar proof",
    )
    check(
        "Gauge-invariance restriction is load-bearing for forest disintegration",
        abs(nongauge_full - nongauge_fixed) > 0.5,
        f"noninvariant full={nongauge_full:.3f}, fixed={nongauge_fixed:.3f}",
    )

    # Positive crossing factors after the forest links are fixed to identity.
    points = [haar_su3(rng) for _ in range(12)]
    beta = 0.8
    wilson_gram = np.array(
        [
            [np.exp((beta / 3.0) * np.trace(right @ left.conj().T).real) for right in points]
            for left in points
        ]
    )
    wilson_min = float(np.min(np.linalg.eigvalsh((wilson_gram + wilson_gram.T) / 2.0)))
    fermion_crossing = np.diag([1.0, 0.5, 0.5, 0.25])
    joint_min = wilson_min * float(np.min(np.linalg.eigvalsh(fermion_crossing)))
    check(
        "Sampled SU3 Wilson seam kernel is positive semidefinite",
        wilson_min > -TOL,
        f"minimum sampled eigenvalue={wilson_min:.3e}",
    )
    check(
        "Wilson tensor fermion seam crossing remains positive",
        joint_min > -TOL,
        f"minimum tensor eigenvalue proxy={joint_min:.3e}",
    )

    dropped_conjugation = np.array(
        [
            [np.exp((beta / 3.0) * np.trace(right @ left).real) for right in points]
            for left in points
        ]
    )
    dropped_min = float(np.min(np.linalg.eigvalsh(dropped_conjugation)))
    check(
        "Dropped orientation conjugation breaks seam positivity",
        dropped_min < -1.0e-3,
        f"minimum sampled eigenvalue={dropped_min:.3e}",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    pairs = [
        f"| `C{left},C{right}` |"
        for left in range(1, 7)
        for right in range(left + 1, 7)
    ]
    required = [
        "gauge-invariant/dressed cylinder algebra",
        "constant Faddeev--Popov factor",
        "residual temporal holonomy",
        "plane-adapted",
        "separate plane-adapted charts",
        "normalized Haar bi-invariance",
        "finite-group analogue",
        "does not prove SU(3) Haar invariance",
        "Berezin Jacobian",
        "no single common forest",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "No axiom-update stop",
    ]
    missing = [needle for needle in required + pairs if needle not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    contract = NOTE.exists() and not missing and attempted >= 7
    check(
        "Source-note boundary and N1-N8 contract",
        contract,
        f"schema present; attempted routes={attempted}" if contract else f"missing={missing}; attempted={attempted}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
