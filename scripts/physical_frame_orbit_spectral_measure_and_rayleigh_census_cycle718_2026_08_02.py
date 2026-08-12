#!/usr/bin/env python3
"""Cycle 718 -- finite frame-orbit spectral measures and Rayleigh census.

This runner reconstructs the Cycle-696 open-box static Hessian and proper-frame
action at L in {3, 4}.  It checks the exact finite permutation algebra, the
source-transfer identity, and the numerical body-diagonal fibre structure.

The load-bearing correction to the submitted cycle is that individual
eigenvector weights are not invariant when an eigenvalue is degenerate.  The
runner therefore groups weights over numerically isolated eigenspaces.  For two
declared deterministic Gaussian probes, the spectral measures agree within each
body-diagonal fibre and across the six translates of a selected regular-subgroup
coset.  The source vectors remain distinct.  A common basis rotation inside all
doublet eigenspaces moves the submitted per-eigenvector comparison while leaving
the eigenspace-summed measure unchanged.

The single-slot Rayleigh partition census is a finite L={3,4} measurement.  No
arbitrary-size, continuum, source-generic, or universal blindness claim is made.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_for_c718", MODULE)
c696 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c696)

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_FRAME_ORBIT_SPECTRAL_MEASURE_AND_RAYLEIGH_CENSUS_CYCLE718_NOTE_2026-08-02.md",
    "docs/PHYSICAL_ASSEMBLY_DEFECT_ISOSPECTRALITY_AND_SOURCE_PAIRING_CYCLE714_NOTE_2026-08-02.md",
    "scripts/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.py",
    "outputs/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02_receipt_2026-08-02.json",
    "docs/PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md",
    "scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.py",
    "outputs/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02_receipt_2026-08-02.json",
    "docs/PHYSICAL_COMPLETE_AVERAGING_SET_FRAME_BLINDNESS_CLASSIFICATION_CYCLE716_NOTE_2026-08-02.md",
    "scripts/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.py",
    "outputs/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02_receipt_2026-08-02.json",
    "docs/PHYSICAL_BODY_DIAGONAL_FRAME_FUNCTIONAL_TRANSVERSAL_LAW_CYCLE717_NOTE_2026-08-02.md",
    "scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py",
    "outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FRAMES = tuple(np.asarray(frame, dtype=np.int64) for frame in c696.c576.FRAMES)
SPATIAL_CLASSES = tuple(c696.SPATIAL_CLASSES)
DIRECTIONS = {
    cls: np.asarray(c696.regge.DIRS15[cls][:3], dtype=np.int64)
    for cls in SPATIAL_CLASSES
}
DIRECTION_CLASS = {
    tuple(int(value) for value in DIRECTIONS[cls]): cls for cls in SPATIAL_CLASSES
}
BODY_DIAGONALS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
SIZES = (3, 4)
PROBE_SEEDS = (7180, 7181)
GENERIC_CENSUS_COUNT = 20
WRAP = False

MATRIX_TOL = 1.0e-12
NUMERICAL_FIBRE_TOL = 1.0e-8
EIGEN_CLUSTER_TOL = 1.0e-9
SPECTRAL_MEASURE_TOL = 1.0e-8
LEVEL_GAP_FLOOR = 1.0e-4
MEASURE_GAP_FLOOR = 1.0e-1
SLOT_FAR_GAP_FLOOR = 1.0e-5
VECTOR_DISTANCE_FLOOR = 5.0e-1
RANK_ONE_BUMP = 1.0e-3
BASIS_SENSITIVITY_FLOOR = 1.0e-1
PARTITION_COUNT = 15
FINEST_PARTITION = (0, 1, 2, 3)

EXPECTED_CENSUS = {
    3: {"patterns": 14, "finest": 0, "constant": 6,
        "classes": {1: 2, 3: 2, 7: 2}},
    4: {"patterns": 15, "finest": 48, "constant": 19,
        "classes": {5: 4, 9: 4, 11: 4, 13: 7}},
}

RECEIPT_NAME = (
    "physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_"
    "2026_08_02_receipt_2026-08-02.json"
)

PASS = 0
FAIL = 0
GATES: dict[str, dict] = {}
NOTES: dict[str, object] = {}


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    condition = bool(condition)
    if condition:
        PASS += 1
    else:
        FAIL += 1
    GATES[name] = {"pass": condition, "detail": detail}
    print(f"{'PASS' if condition else 'FAIL'} {name} {detail}".rstrip())
    return condition


def frame_index(matrix: np.ndarray) -> int:
    for index, frame in enumerate(FRAMES):
        if np.array_equal(frame, matrix):
            return index
    raise ValueError("matrix is not in the supplied proper-frame table")


MULTIPLY = tuple(
    tuple(frame_index(FRAMES[a] @ FRAMES[b]) for b in range(24))
    for a in range(24)
)
IDENTITY = frame_index(np.eye(3, dtype=np.int64))
INVERSE = tuple(
    next(b for b in range(24) if MULTIPLY[a][b] == IDENTITY)
    for a in range(24)
)


def subgroup_closure(generators: tuple[int, ...]) -> tuple[int, ...]:
    members = set(generators) | {IDENTITY}
    while True:
        enlarged = members | {MULTIPLY[a][b] for a in members for b in members}
        if enlarged == members:
            return tuple(sorted(members))
        members = enlarged


def all_subgroups() -> list[tuple[int, ...]]:
    result = {(IDENTITY,)}
    for count in (1, 2, 3):
        for generators in itertools.combinations(range(24), count):
            result.add(subgroup_closure(generators))
    return sorted(result, key=lambda subgroup: (len(subgroup), subgroup))


def unoriented_diagonal(vector: np.ndarray | tuple[int, int, int]) -> tuple[int, int, int]:
    value = tuple(int(x) for x in vector)
    return value if value[0] > 0 else tuple(-x for x in value)


DIAGONAL_INDEX = {
    unoriented_diagonal(diagonal): index
    for index, diagonal in enumerate(BODY_DIAGONALS)
}


def diagonal_label(frame: int) -> int:
    image = FRAMES[frame].T @ np.asarray(BODY_DIAGONALS[0], dtype=np.int64)
    return DIAGONAL_INDEX[unoriented_diagonal(image)]


DIAGONAL_LABELS = tuple(diagonal_label(frame) for frame in range(24))
FIBRES = tuple(
    tuple(frame for frame in range(24) if DIAGONAL_LABELS[frame] == label)
    for label in range(4)
)
SEXTET = FIBRES[0]
SUBGROUPS = all_subgroups()
REGULAR_SUBGROUPS = tuple(
    subgroup for subgroup in SUBGROUPS
    if len(subgroup) == 4
    and len({DIAGONAL_LABELS[member] for member in subgroup}) == 4
)


def left_translate(collection: tuple[int, ...] | frozenset[int], frame: int) -> tuple[int, ...]:
    return tuple(sorted(MULTIPLY[frame][member] for member in collection))


def left_translates(collection: tuple[int, ...] | frozenset[int]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted({left_translate(collection, frame) for frame in range(24)}))


def relabel(L: int, frame: int) -> np.ndarray:
    index = c696.static_variable_index(L, WRAP)
    site_map = c696.frame_site_map(L, FRAMES[frame])
    mapping = np.empty(len(index), dtype=np.int64)
    for (cls, site), old_index in index.items():
        image = FRAMES[frame] @ DIRECTIONS[cls]
        target_site = tuple(
            int(value)
            for value in (
                np.asarray(site_map[site], dtype=np.int64)
                + np.minimum(image, 0)
            )
        )
        target_cls = DIRECTION_CLASS[tuple(int(value) for value in np.abs(image))]
        mapping[old_index] = index[(target_cls, target_site)]
    return mapping


def eigen_clusters(eigenvalues: np.ndarray) -> tuple[tuple[int, ...], ...]:
    clusters: list[list[int]] = []
    for index, value in enumerate(eigenvalues):
        if not clusters or abs(value - eigenvalues[clusters[-1][0]]) > EIGEN_CLUSTER_TOL:
            clusters.append([index])
        else:
            clusters[-1].append(index)
    return tuple(tuple(cluster) for cluster in clusters)


def normalized(vector: np.ndarray) -> tuple[np.ndarray, float]:
    norm = float(np.linalg.norm(vector))
    if norm == 0.0:
        return vector.copy(), norm
    return vector / norm, norm


def source_pullback(vector: np.ndarray, mapping: np.ndarray) -> np.ndarray:
    return vector[np.argsort(mapping)]


def averaged_source(pulled_sources: np.ndarray,
                    collection: tuple[int, ...] | frozenset[int]) -> np.ndarray:
    return pulled_sources[list(collection)].sum(axis=0)


def spectral_measure(context: dict, vector: np.ndarray) -> np.ndarray:
    unit, norm = normalized(vector)
    if norm == 0.0:
        return np.full(len(context["clusters"]), np.nan)
    coefficients = context["eigenvectors"].T @ unit
    return np.asarray([
        float(np.sum(coefficients[list(cluster)] ** 2))
        for cluster in context["clusters"]
    ])


def individual_weights(context: dict, vector: np.ndarray) -> np.ndarray:
    unit, norm = normalized(vector)
    if norm == 0.0:
        return np.full(context["n"], np.nan)
    coefficients = context["eigenvectors"].T @ unit
    return coefficients * coefficients


def rayleigh(context: dict, vector: np.ndarray) -> float:
    unit, norm = normalized(vector)
    if norm == 0.0:
        return float("nan")
    return float(unit @ (context["inverse"] @ unit))


def partition(values: np.ndarray) -> tuple[int, ...]:
    parent = list(range(4))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a in range(4):
        for b in range(a + 1, 4):
            if abs(float(values[a] - values[b])) <= NUMERICAL_FIBRE_TOL:
                union(a, b)
    labels: dict[int, int] = {}
    result = []
    for index in range(4):
        root = find(index)
        labels.setdefault(root, len(labels))
        result.append(labels[root])
    return tuple(result)


ALL_PARTITIONS = {
    candidate
    for candidate in itertools.product(range(4), repeat=4)
    if candidate[0] == 0
    and all(candidate[index] <= max(candidate[:index]) + 1 for index in range(1, 4))
}


def build_context(L: int) -> dict:
    matrix = np.asarray(c696.assemble_static_hessian(L, WRAP)["Q"], dtype=np.float64)
    mappings = tuple(relabel(L, frame) for frame in range(24))
    transported = tuple(matrix[np.ix_(mapping, mapping)] for mapping in mappings)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    inverse = np.linalg.inv(matrix)
    clusters = eigen_clusters(eigenvalues)
    return {
        "L": L,
        "Q": matrix,
        "n": matrix.shape[0],
        "mappings": mappings,
        "transported": transported,
        "inverse": inverse,
        "transported_inverse": tuple(
            inverse[np.ix_(mapping, mapping)] for mapping in mappings
        ),
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
        "clusters": clusters,
    }


def check_group_and_matrix(context: dict) -> None:
    L = context["L"]
    expected_n = 3 * (L - 1) * L * L + 3 * (L - 1) ** 2 * L + (L - 1) ** 3
    check(f"group.frame_table.L{L}", len(FRAMES) == 24
          and len({frame.tobytes() for frame in FRAMES}) == 24
          and all(round(float(np.linalg.det(frame))) == 1 for frame in FRAMES),
          "24 distinct determinant-one signed permutations")
    check(f"group.dof_bijections.L{L}", context["n"] == expected_n
          and all(sorted(mapping.tolist()) == list(range(context["n"]))
                  for mapping in context["mappings"]),
          f"n={context['n']}, expected={expected_n}, 24 bijections")
    composition = sum(
        np.array_equal(
            context["mappings"][MULTIPLY[a][b]],
            context["mappings"][a][context["mappings"][b]],
        )
        for a in range(24) for b in range(24)
    )
    reversed_composition = sum(
        np.array_equal(
            context["mappings"][MULTIPLY[a][b]],
            context["mappings"][b][context["mappings"][a]],
        )
        for a in range(24) for b in range(24)
    )
    check(f"group.composition.L{L}", composition == 576,
          f"m_ab=m_a∘m_b for {composition}/576 pairs")
    check(f"group.composition_reverse_witness.L{L}", reversed_composition == 120,
          f"reversed order matches {reversed_composition}/576 pairs")
    check(f"group.body_diagonal_action.L{L}", len(SUBGROUPS) == 30
          and len(SEXTET) == 6 and subgroup_closure(SEXTET) == SEXTET
          and len(REGULAR_SUBGROUPS) == 4,
          f"sextet={SEXTET}, subgroups={len(SUBGROUPS)}, regular={len(REGULAR_SUBGROUPS)}")

    symmetry = float(np.max(np.abs(context["Q"] - context["Q"].T)))
    roundtrip = 0.0
    for mapping, transported in zip(context["mappings"], context["transported"]):
        inverse_mapping = np.argsort(mapping)
        roundtrip = max(
            roundtrip,
            float(np.max(np.abs(transported[np.ix_(inverse_mapping, inverse_mapping)]
                                - context["Q"]))),
        )
    check(f"matrix.symmetry_roundtrip.L{L}", symmetry <= MATRIX_TOL and roundtrip == 0.0,
          f"symmetry={symmetry:.3e}, permutation roundtrip={roundtrip:.3e}")

    conjugator_residual = 0.0
    wrong_residual = 0.0
    wrong_pairs = 0
    for a in range(24):
        for b in range(24):
            correct = MULTIPLY[INVERSE[b]][a]
            wrong = MULTIPLY[a][INVERSE[b]]
            mapping = context["mappings"][correct]
            predicted = context["transported"][b][np.ix_(mapping, mapping)]
            conjugator_residual = max(
                conjugator_residual,
                float(np.max(np.abs(context["transported"][a] - predicted))),
            )
            if correct != wrong:
                wrong_pairs += 1
                wrong_mapping = context["mappings"][wrong]
                wrong_prediction = context["transported"][b][
                    np.ix_(wrong_mapping, wrong_mapping)
                ]
                wrong_residual = max(
                    wrong_residual,
                    float(np.max(np.abs(context["transported"][a] - wrong_prediction))),
                )
    check(f"matrix.conjugator.L{L}", conjugator_residual == 0.0,
          f"inverse-left residual={conjugator_residual:.3e} over 576 pairs")
    check(f"matrix.conjugator_reverse_witness.L{L}", wrong_pairs == 456
          and wrong_residual > 1.0,
          f"reversed product differs on {wrong_pairs} pairs, residual={wrong_residual:.6f}")

    same_fibre = max(
        float(np.max(np.abs(context["transported"][a] - context["transported"][b])))
        for a in range(24) for b in range(a + 1, 24)
        if DIAGONAL_LABELS[a] == DIAGONAL_LABELS[b]
    )
    cross_fibre = min(
        float(np.max(np.abs(context["transported"][a] - context["transported"][b])))
        for a in range(24) for b in range(a + 1, 24)
        if DIAGONAL_LABELS[a] != DIAGONAL_LABELS[b]
    )
    check(f"matrix.fibre_separation.L{L}", same_fibre < NUMERICAL_FIBRE_TOL
          and cross_fibre > 1.0,
          f"within max={same_fibre:.3e}, cross minimum={cross_fibre:.6f}")

    spectra = tuple(np.linalg.eigvalsh(matrix) for matrix in context["transported"])
    spectrum_residual = max(
        float(np.max(np.abs(spectrum - spectra[IDENTITY]))) for spectrum in spectra
    )
    trace_residual = max(float(np.trace(matrix)) for matrix in context["transported"]) \
        - min(float(np.trace(matrix)) for matrix in context["transported"])
    frobenius_residual = max(float(np.linalg.norm(matrix)) for matrix in context["transported"]) \
        - min(float(np.linalg.norm(matrix)) for matrix in context["transported"])
    determinant_signs = {int(np.linalg.slogdet(matrix)[0]) for matrix in context["transported"]}
    logabs = [float(np.linalg.slogdet(matrix)[1]) for matrix in context["transported"]]
    logabs_residual = max(logabs) - min(logabs)
    check(f"matrix.spectral_consistency.L{L}", spectrum_residual < 1.0e-9
          and trace_residual < 1.0e-9 and frobenius_residual < 1.0e-9
          and len(determinant_signs) == 1 and logabs_residual < 1.0e-9,
          f"eigen={spectrum_residual:.3e}, trace={trace_residual:.3e}, "
          f"frobenius={frobenius_residual:.3e}, logabsdet={logabs_residual:.3e}, "
          f"det-sign={sorted(determinant_signs)}")
    basis = np.zeros(context["n"])
    basis[0] = 1.0
    bumped = np.linalg.eigvalsh(
        context["Q"] + RANK_ONE_BUMP * np.outer(basis, basis)
    )
    bump_shift = float(np.max(np.abs(bumped - context["eigenvalues"])))
    check(f"matrix.rank_one_spectral_witness.L{L}", bump_shift > 1.0e-5,
          f"bump={RANK_ONE_BUMP:.1e}, spectrum shift={bump_shift:.3e}")

    minimum_absolute_eigenvalue = float(np.min(np.abs(context["eigenvalues"])))
    check(f"matrix.inverse_margin.L{L}", minimum_absolute_eigenvalue > 1.0e-3,
          f"minimum |eigenvalue|={minimum_absolute_eigenvalue:.3e}")
    clusters = context["clusters"]
    internal_gap = max(
        float(context["eigenvalues"][cluster[-1]] - context["eigenvalues"][cluster[0]])
        for cluster in clusters
    )
    external_gap = min(
        float(context["eigenvalues"][clusters[index + 1][0]]
              - context["eigenvalues"][clusters[index][-1]])
        for index in range(len(clusters) - 1)
    )
    doublets = sum(len(cluster) == 2 for cluster in clusters)
    check(f"matrix.eigenspace_resolution.L{L}", all(len(cluster) in (1, 2) for cluster in clusters)
          and internal_gap < EIGEN_CLUSTER_TOL and external_gap > 1.0e-3,
          f"clusters={len(clusters)}, doublets={doublets}, "
          f"internal max={internal_gap:.3e}, external min={external_gap:.3e}")
    NOTES[f"matrix_L{L}"] = {
        "within_fibre": same_fibre,
        "cross_fibre_minimum": cross_fibre,
        "spectrum_residual": spectrum_residual,
        "rank_one_shift": bump_shift,
        "eigenspaces": len(clusters),
        "doublets": doublets,
        "eigenspace_internal_gap": internal_gap,
        "eigenspace_external_gap": external_gap,
    }


def check_probe(context: dict, probe: np.ndarray, tag: str) -> None:
    L = context["L"]
    pulled = np.stack([
        source_pullback(probe, mapping) for mapping in context["mappings"]
    ])
    orbit_distance = min(
        float(np.linalg.norm(pulled[a] - pulled[b]))
        for a in range(24) for b in range(a + 1, 24)
    )
    check(f"probe.{tag}.orbit_distinct.L{L}", orbit_distance > 1.0,
          f"minimum raw orbit distance={orbit_distance:.6f}")

    measures = np.stack([spectral_measure(context, vector) for vector in pulled])
    measure_within = max(
        float(np.sum(np.abs(measures[a] - measures[b])))
        for a in range(24) for b in range(a + 1, 24)
        if DIAGONAL_LABELS[a] == DIAGONAL_LABELS[b]
    )
    measure_between = min(
        float(np.sum(np.abs(measures[a] - measures[b])))
        for a in range(24) for b in range(a + 1, 24)
        if DIAGONAL_LABELS[a] != DIAGONAL_LABELS[b]
    )
    check(f"probe.{tag}.spectral_measure_fibres.L{L}",
          measure_within < SPECTRAL_MEASURE_TOL
          and measure_between > MEASURE_GAP_FLOOR,
          f"within L1 max={measure_within:.3e}, cross L1 min={measure_between:.6f}")

    values = np.asarray([rayleigh(context, vector) for vector in pulled])
    value_within = max(
        float(np.max(values[list(fibre)]) - np.min(values[list(fibre)]))
        for fibre in FIBRES
    )
    fibre_means = [float(np.mean(values[list(fibre)])) for fibre in FIBRES]
    value_between = min(
        abs(fibre_means[a] - fibre_means[b])
        for a in range(4) for b in range(a + 1, 4)
    )
    check(f"probe.{tag}.rayleigh_fibres.L{L}",
          value_within < NUMERICAL_FIBRE_TOL and value_between > LEVEL_GAP_FLOOR,
          f"within max={value_within:.3e}, cross mean gap={value_between:.6f}")

    test_collections = (
        (IDENTITY,),
        (1, 4),
        (0, 5, 11),
        FIBRES[0],
    )
    transfer_residual = 0.0
    minimum_average_norm = float("inf")
    hull_margin = float("inf")
    inverse_eigenvalues = 1.0 / context["eigenvalues"]
    hull_low = float(np.min(inverse_eigenvalues))
    hull_high = float(np.max(inverse_eigenvalues))
    weighted_residual = 0.0
    for collection in test_collections:
        average = averaged_source(pulled, collection)
        average_unit, average_norm = normalized(average)
        minimum_average_norm = min(minimum_average_norm, average_norm)
        for frame in range(24):
            lhs = float(
                average_unit @ (
                    context["transported_inverse"][frame] @ average_unit
                )
            )
            translated = left_translate(collection, frame)
            rhs = rayleigh(context, averaged_source(pulled, translated))
            transfer_residual = max(transfer_residual, abs(lhs - rhs))
            hull_margin = min(hull_margin, lhs - hull_low, hull_high - lhs)
        weights = individual_weights(context, average)
        weighted_residual = max(
            weighted_residual,
            abs(float(np.sum(weights * inverse_eigenvalues)) - rayleigh(context, average)),
        )
    check(f"probe.{tag}.transfer_identity.L{L}", transfer_residual < 1.0e-9
          and minimum_average_norm > 1.0e-8,
          f"residual={transfer_residual:.3e}, minimum average norm={minimum_average_norm:.6f}")
    check(f"probe.{tag}.weighted_hull.L{L}", weighted_residual < 1.0e-9
          and hull_margin > 0.0,
          f"weighted residual={weighted_residual:.3e}, hull=[{hull_low:.6f},{hull_high:.6f}], "
          f"minimum margin={hull_margin:.6f}")

    regular = REGULAR_SUBGROUPS[0]
    collection = tuple(sorted(MULTIPLY[member][3] for member in regular))
    translates = left_translates(collection)
    covering = {MULTIPLY[s][h] for s in SEXTET for h in regular}
    check(f"probe.{tag}.regular_cover.L{L}", len(covering) == 24
          and len(translates) == 6,
          f"|S H|={len(covering)}, distinct left translates={len(translates)}")
    symmetry_labels: dict[tuple[int, ...], int] = {}
    for translated in translates:
        matches = [s for s in SEXTET if left_translate(collection, s) == translated]
        if matches:
            symmetry_labels[translated] = matches[0]
    check(f"probe.{tag}.translate_symmetry_labels.L{L}", len(symmetry_labels) == 6,
          f"six translates represented by sextet labels={sorted(symmetry_labels.values())}")

    sources = np.stack([
        averaged_source(pulled, translated) for translated in translates
    ])
    unit_sources = sources / np.linalg.norm(sources, axis=1)[:, None]
    normalized_distance = min(
        float(np.linalg.norm(unit_sources[a] - unit_sources[b]))
        for a in range(6) for b in range(a + 1, 6)
    )
    base_source = averaged_source(pulled, collection)
    source_relation = 0.0
    for index, translated in enumerate(translates):
        label = symmetry_labels[translated]
        predicted = source_pullback(base_source, context["mappings"][label])
        source_relation = max(
            source_relation,
            float(np.linalg.norm(sources[index] - predicted))
            / max(float(np.linalg.norm(predicted)), 1.0),
        )
    check(f"probe.{tag}.translated_sources_distinct.L{L}",
          normalized_distance > VECTOR_DISTANCE_FLOOR and source_relation < 1.0e-12,
          f"normalized distance min={normalized_distance:.6f}, symmetry relation={source_relation:.3e}")

    translated_measures = np.stack([
        spectral_measure(context, source) for source in sources
    ])
    measure_spread = max(
        float(np.sum(np.abs(translated_measures[a] - translated_measures[b])))
        for a in range(6) for b in range(a + 1, 6)
    )
    translated_values = [rayleigh(context, source) for source in sources]
    value_spread = max(translated_values) - min(translated_values)
    check(f"probe.{tag}.translated_spectral_measure.L{L}",
          measure_spread < SPECTRAL_MEASURE_TOL and value_spread < NUMERICAL_FIBRE_TOL,
          f"measure L1 max={measure_spread:.3e}, Rayleigh spread={value_spread:.3e}")

    coefficients = unit_sources @ context["eigenvectors"]
    base_raw_distance = float(np.sum(np.abs(coefficients[0] ** 2 - coefficients[1] ** 2)))
    rotated_distances = []
    for angle in np.linspace(0.0, np.pi / 2.0, 33):
        rotated = coefficients.copy()
        cosine, sine = float(np.cos(angle)), float(np.sin(angle))
        for cluster in context["clusters"]:
            if len(cluster) != 2:
                continue
            first, second = cluster
            old_first = rotated[:, first].copy()
            old_second = rotated[:, second].copy()
            rotated[:, first] = cosine * old_first + sine * old_second
            rotated[:, second] = -sine * old_first + cosine * old_second
        rotated_distances.append(
            float(np.sum(np.abs(rotated[0] ** 2 - rotated[1] ** 2)))
        )
    basis_range = max(rotated_distances) - min(rotated_distances)
    check(f"probe.{tag}.individual_weight_basis_witness.L{L}",
          basis_range > BASIS_SENSITIVITY_FLOOR
          and measure_spread < SPECTRAL_MEASURE_TOL,
          f"individual-weight L1={base_raw_distance:.6f}, rotation range={basis_range:.6f}; "
          f"eigenspace measure max={measure_spread:.3e}")

    contrast = tuple(FIBRES[0][:4])
    contrast_translates = left_translates(contrast)
    contrast_sources = np.stack([
        averaged_source(pulled, translated) for translated in contrast_translates
    ])
    contrast_values = [rayleigh(context, source) for source in contrast_sources]
    contrast_measures = np.stack([
        spectral_measure(context, source) for source in contrast_sources
    ])
    contrast_measure_max = max(
        float(np.sum(np.abs(contrast_measures[a] - contrast_measures[b])))
        for a in range(len(contrast_translates))
        for b in range(a + 1, len(contrast_translates))
    )
    contrast_value_spread = max(contrast_values) - min(contrast_values)
    check(f"probe.{tag}.nonregular_contrast.L{L}", len(contrast_translates) == 24
          and contrast_measure_max > MEASURE_GAP_FLOOR
          and contrast_value_spread > LEVEL_GAP_FLOOR,
          f"translates={len(contrast_translates)}, measure L1 max={contrast_measure_max:.6f}, "
          f"Rayleigh spread={contrast_value_spread:.6f}")

    NOTES[f"probe_{tag}_L{L}"] = {
        "orbit_distance": orbit_distance,
        "orbit_measure_within": measure_within,
        "orbit_measure_between": measure_between,
        "orbit_rayleigh_within": value_within,
        "orbit_rayleigh_between": value_between,
        "transfer_residual": transfer_residual,
        "translated_source_distance": normalized_distance,
        "translated_source_relation": source_relation,
        "translated_measure_spread": measure_spread,
        "translated_rayleigh_spread": value_spread,
        "individual_weight_basis_range": basis_range,
        "contrast_measure_max": contrast_measure_max,
        "contrast_rayleigh_spread": contrast_value_spread,
    }


def check_single_slot_census(context: dict) -> None:
    L = context["L"]
    representatives = tuple(fibre[0] for fibre in FIBRES)
    representative_inverse = tuple(
        context["transported_inverse"][frame] for frame in representatives
    )
    fibre_inverse_residual = max(
        float(np.max(np.abs(
            np.diag(context["transported_inverse"][frame])
            - np.diag(context["transported_inverse"][representatives[label]])
        )))
        for label, fibre in enumerate(FIBRES) for frame in fibre
    )
    check(f"census.fibre_representative.L{L}", fibre_inverse_residual < NUMERICAL_FIBRE_TOL,
          f"maximum single-slot within-fibre residual={fibre_inverse_residual:.3e}")

    index = c696.static_variable_index(L, WRAP)
    inverse_index = {value: key for key, value in index.items()}
    counts: Counter = Counter()
    constant_classes: Counter = Counter()
    close_max = 0.0
    separated_min = float("inf")
    for slot in range(context["n"]):
        values = np.asarray([matrix[slot, slot] for matrix in representative_inverse])
        for a in range(4):
            for b in range(a + 1, 4):
                difference = abs(float(values[a] - values[b]))
                if difference <= NUMERICAL_FIBRE_TOL:
                    close_max = max(close_max, difference)
                else:
                    separated_min = min(separated_min, difference)
        pattern = partition(values)
        counts[pattern] += 1
        if len(set(pattern)) == 1:
            constant_classes[inverse_index[slot][0]] += 1
    expected = EXPECTED_CENSUS[L]
    check(f"census.classifier_margin.L{L}", close_max < NUMERICAL_FIBRE_TOL
          and separated_min > SLOT_FAR_GAP_FLOOR,
          f"close max={close_max:.3e}, separated min={separated_min:.3e}")
    check(f"census.partition_count.L{L}", sum(counts.values()) == context["n"]
          and set(counts) <= ALL_PARTITIONS
          and len(counts) == expected["patterns"],
          f"slots={sum(counts.values())}, patterns={len(counts)}/{PARTITION_COUNT}")
    check(f"census.finest_count.L{L}", counts[FINEST_PARTITION] == expected["finest"],
          f"finest-pattern slots={counts[FINEST_PARTITION]}")
    check(f"census.constant_slots.L{L}", sum(constant_classes.values()) == expected["constant"]
          and dict(constant_classes) == expected["classes"],
          f"constant slots={sum(constant_classes.values())}, classes={dict(sorted(constant_classes.items()))}")

    generic_finest = 0
    generic_gap = float("inf")
    for sample in range(GENERIC_CENSUS_COUNT):
        probe = np.random.default_rng(900 + sample + L).standard_normal(context["n"])
        probe_unit, _ = normalized(probe)
        values = np.asarray([
            float(probe_unit @ (matrix @ probe_unit))
            for matrix in representative_inverse
        ])
        generic_gap = min(
            generic_gap,
            min(abs(float(values[a] - values[b]))
                for a in range(4) for b in range(a + 1, 4)),
        )
        generic_finest += int(partition(values) == FINEST_PARTITION)
    check(f"census.deterministic_gaussian_sample.L{L}",
          generic_finest == GENERIC_CENSUS_COUNT and generic_gap > SLOT_FAR_GAP_FLOOR,
          f"finest={generic_finest}/{GENERIC_CENSUS_COUNT}, minimum pair gap={generic_gap:.3e}")
    NOTES[f"census_L{L}"] = {
        "patterns": len(counts),
        "finest": counts[FINEST_PARTITION],
        "constant": sum(constant_classes.values()),
        "constant_classes": dict(sorted(constant_classes.items())),
        "close_max": close_max,
        "separated_min": separated_min,
        "generic_finest": generic_finest,
        "generic_gap": generic_gap,
    }


def main() -> int:
    print("=== Cycle 718: finite frame-orbit spectral measures and Rayleigh census ===")
    for L in SIZES:
        print(f"--- L={L} ---")
        context = build_context(L)
        check_group_and_matrix(context)
        for probe_index, seed in enumerate(PROBE_SEEDS):
            probe = np.random.default_rng(seed + L).standard_normal(context["n"])
            check_probe(context, probe, f"seed{seed}")
        check_single_slot_census(context)
    receipt = {
        "runner": Path(__file__).name,
        "pass": PASS,
        "fail": FAIL,
        "box_sizes": list(SIZES),
        "body_diagonals": [list(diagonal) for diagonal in BODY_DIAGONALS],
        "probe_seeds": list(PROBE_SEEDS),
        "gates": GATES,
        "notes": NOTES,
    }
    output = ROOT / "outputs" / RECEIPT_NAME
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
