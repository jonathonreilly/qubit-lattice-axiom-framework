#!/usr/bin/env python3
"""Independent dense-matrix check of the Cycle-718 finite result.

This checker does not import the Cycle-718 primary.  It builds explicit dense
permutation matrices, reconstructs the body-diagonal action and subgroup table,
groups numerical eigenspaces independently, and recomputes the spectral-measure,
Rayleigh, regular-coset, and single-slot claims.  It reads the primary receipt
only after completing its own calculation.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_independent_for_c718", MODULE)
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
    "outputs/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02_receipt_2026-08-02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FRAMES = tuple(np.asarray(frame, dtype=np.int64) for frame in c696.c576.FRAMES)
CLASSES = tuple(c696.SPATIAL_CLASSES)
VECTORS = {cls: np.asarray(c696.regge.DIRS15[cls][:3], dtype=np.int64) for cls in CLASSES}
VECTOR_CLASS = {tuple(int(x) for x in VECTORS[cls]): cls for cls in CLASSES}
DIAGONALS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
SIZES = (3, 4)
SEEDS = (7180, 7181)
EXPECTED = {
    3: (14, 0, {1: 2, 3: 2, 7: 2}),
    4: (15, 48, {5: 4, 9: 4, 11: 4, 13: 7}),
}
RECEIPT = ROOT / "outputs" / (
    "physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_"
    "2026_08_02_receipt_2026-08-02.json"
)

PASS = 0
FAIL = 0
RESULTS: dict[str, dict] = {}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name} {detail}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {name} {detail}".rstrip())


def index_of(matrix: np.ndarray) -> int:
    return next(i for i, frame in enumerate(FRAMES) if np.array_equal(frame, matrix))


PRODUCT = tuple(tuple(index_of(FRAMES[a] @ FRAMES[b]) for b in range(24))
                for a in range(24))
IDENTITY = index_of(np.eye(3, dtype=np.int64))
INVERSES = tuple(next(b for b in range(24) if PRODUCT[a][b] == IDENTITY)
                 for a in range(24))


def close(generators: tuple[int, ...]) -> tuple[int, ...]:
    answer = {IDENTITY, *generators}
    while True:
        enlarged = answer | {PRODUCT[a][b] for a in answer for b in answer}
        if enlarged == answer:
            return tuple(sorted(answer))
        answer = enlarged


def canonical_diagonal(vector: np.ndarray | tuple[int, int, int]) -> tuple[int, int, int]:
    result = tuple(int(x) for x in vector)
    return result if result[0] > 0 else tuple(-x for x in result)


DIAGONAL_NUMBER = {canonical_diagonal(value): i for i, value in enumerate(DIAGONALS)}
LABEL = tuple(
    DIAGONAL_NUMBER[canonical_diagonal(FRAMES[g].T @ np.asarray(DIAGONALS[0]))]
    for g in range(24)
)
FIBRE = tuple(tuple(g for g in range(24) if LABEL[g] == label) for label in range(4))
SEXTET = FIBRE[0]
SUBGROUPS = {
    close(generators)
    for count in (1, 2, 3)
    for generators in itertools.combinations(range(24), count)
}
REGULAR = tuple(sorted(
    (group for group in SUBGROUPS
     if len(group) == 4 and len({LABEL[g] for g in group}) == 4),
    key=lambda group: group,
))


def dense_permutation(L: int, g: int) -> np.ndarray:
    index = c696.static_variable_index(L, wrap=False)
    site_map = c696.frame_site_map(L, FRAMES[g])
    permutation = np.zeros((len(index), len(index)), dtype=np.float64)
    for (cls, site), old in index.items():
        image = FRAMES[g] @ VECTORS[cls]
        target_cls = VECTOR_CLASS[tuple(int(x) for x in np.abs(image))]
        target_site = tuple(
            int(x) for x in (
                np.asarray(site_map[site], dtype=np.int64) + np.minimum(image, 0)
            )
        )
        new = index[(target_cls, target_site)]
        permutation[old, new] = 1.0
    return permutation


def clusters(eigenvalues: np.ndarray) -> tuple[tuple[int, ...], ...]:
    result: list[list[int]] = []
    for i in range(len(eigenvalues)):
        if not result or eigenvalues[i] - eigenvalues[result[-1][-1]] > 1.0e-9:
            result.append([i])
        else:
            result[-1].append(i)
    return tuple(tuple(group) for group in result)


def measure(eigenvectors: np.ndarray, groups: tuple[tuple[int, ...], ...],
            vector: np.ndarray) -> np.ndarray:
    unit = vector / np.linalg.norm(vector)
    coefficients = eigenvectors.T @ unit
    return np.asarray([float(np.sum(coefficients[list(group)] ** 2)) for group in groups])


def translated(collection: tuple[int, ...], frame: int) -> tuple[int, ...]:
    return tuple(sorted(PRODUCT[frame][member] for member in collection))


def translates(collection: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted({translated(collection, frame) for frame in range(24)}))


def partition(values: np.ndarray) -> tuple[int, ...]:
    groups: list[list[int]] = []
    for index in range(4):
        candidates = [group for group in groups
                      if any(abs(float(values[index] - values[member])) <= 1.0e-8
                             for member in group)]
        if candidates:
            candidates[0].append(index)
        else:
            groups.append([index])
    groups.sort(key=lambda group: min(group))
    labels = {}
    for label, group in enumerate(groups):
        for member in group:
            labels[member] = label
    return tuple(labels[index] for index in range(4))


check("independent.group", len(SUBGROUPS) == 30 and len(REGULAR) == 4
      and len(SEXTET) == 6 and close(SEXTET) == SEXTET,
      f"subgroups={len(SUBGROUPS)}, regular={len(REGULAR)}, sextet={SEXTET}")

for L in SIZES:
    matrix = np.asarray(c696.assemble_static_hessian(L, wrap=False)["Q"], dtype=float)
    permutations = tuple(dense_permutation(L, g) for g in range(24))
    transported = tuple(P @ matrix @ P.T for P in permutations)
    inverse = np.linalg.inv(matrix)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    eigenspaces = clusters(eigenvalues)
    composition = sum(
        np.array_equal(permutations[PRODUCT[a][b]], permutations[b] @ permutations[a])
        for a in range(24) for b in range(24)
    )
    wrong_composition = sum(
        np.array_equal(permutations[PRODUCT[a][b]], permutations[a] @ permutations[b])
        for a in range(24) for b in range(24)
    )
    check(f"independent.action.L{L}", composition == 576 and wrong_composition == 120,
          f"anti-action={composition}/576, reversed={wrong_composition}/576")
    conjugator = 0.0
    wrong_conjugator = 0.0
    for a in range(24):
        for b in range(24):
            correct = PRODUCT[INVERSES[b]][a]
            wrong = PRODUCT[a][INVERSES[b]]
            conjugator = max(conjugator, float(np.max(np.abs(
                transported[a] - permutations[correct] @ transported[b] @ permutations[correct].T
            ))))
            if correct != wrong:
                wrong_conjugator = max(wrong_conjugator, float(np.max(np.abs(
                    transported[a] - permutations[wrong] @ transported[b] @ permutations[wrong].T
                ))))
    check(f"independent.conjugator.L{L}", conjugator < 1.0e-12 and wrong_conjugator > 1.0,
          f"correct={conjugator:.3e}, reversed witness={wrong_conjugator:.6f}")
    within_matrix = max(
        float(np.max(np.abs(transported[a] - transported[b])))
        for a in range(24) for b in range(a + 1, 24) if LABEL[a] == LABEL[b]
    )
    between_matrix = min(
        float(np.max(np.abs(transported[a] - transported[b])))
        for a in range(24) for b in range(a + 1, 24) if LABEL[a] != LABEL[b]
    )
    check(f"independent.matrix_fibres.L{L}", within_matrix < 1.0e-8 and between_matrix > 1.0,
          f"within={within_matrix:.3e}, cross minimum={between_matrix:.6f}")
    internal = max(eigenvalues[group[-1]] - eigenvalues[group[0]] for group in eigenspaces)
    external = min(eigenvalues[eigenspaces[i + 1][0]] - eigenvalues[eigenspaces[i][-1]]
                   for i in range(len(eigenspaces) - 1))
    check(f"independent.eigenspaces.L{L}", internal < 1.0e-9 and external > 1.0e-3
          and all(len(group) in (1, 2) for group in eigenspaces),
          f"clusters={len(eigenspaces)}, doublets={sum(len(g)==2 for g in eigenspaces)}, "
          f"internal={internal:.3e}, external={external:.3e}")

    probe_summary = []
    for seed in SEEDS:
        probe = np.random.default_rng(seed + L).standard_normal(len(matrix))
        orbit = np.stack([P.T @ probe for P in permutations])
        orbit_measure = np.stack([measure(eigenvectors, eigenspaces, vector) for vector in orbit])
        within_measure = max(
            float(np.sum(np.abs(orbit_measure[a] - orbit_measure[b])))
            for a in range(24) for b in range(a + 1, 24) if LABEL[a] == LABEL[b]
        )
        between_measure = min(
            float(np.sum(np.abs(orbit_measure[a] - orbit_measure[b])))
            for a in range(24) for b in range(a + 1, 24) if LABEL[a] != LABEL[b]
        )
        check(f"independent.orbit_measure.seed{seed}.L{L}", within_measure < 1.0e-8
              and between_measure > 0.1,
              f"within={within_measure:.3e}, cross={between_measure:.6f}")

        H = REGULAR[0]
        collection = tuple(sorted(PRODUCT[h][3] for h in H))
        orbit_sets = translates(collection)
        sources = np.stack([orbit[list(collection_value)].sum(axis=0)
                            for collection_value in orbit_sets])
        source_measure = np.stack([
            measure(eigenvectors, eigenspaces, source) for source in sources
        ])
        source_measure_spread = max(
            float(np.sum(np.abs(source_measure[a] - source_measure[b])))
            for a in range(6) for b in range(a + 1, 6)
        )
        unit_sources = sources / np.linalg.norm(sources, axis=1)[:, None]
        source_distance = min(
            float(np.linalg.norm(unit_sources[a] - unit_sources[b]))
            for a in range(6) for b in range(a + 1, 6)
        )
        values = [float(source @ (inverse @ source)) / float(source @ source)
                  for source in sources]
        value_spread = max(values) - min(values)
        check(f"independent.regular_coset.seed{seed}.L{L}", len(orbit_sets) == 6
              and source_distance > 0.5 and source_measure_spread < 1.0e-8
              and value_spread < 1.0e-8,
              f"distance={source_distance:.6f}, measure={source_measure_spread:.3e}, "
              f"Rayleigh={value_spread:.3e}")

        coefficients = unit_sources @ eigenvectors
        raw_values = []
        for angle in np.linspace(0.0, np.pi / 2.0, 33):
            rotated = coefficients.copy()
            cosine, sine = np.cos(angle), np.sin(angle)
            for group in eigenspaces:
                if len(group) == 2:
                    a, b = group
                    first, second = rotated[:, a].copy(), rotated[:, b].copy()
                    rotated[:, a] = cosine * first + sine * second
                    rotated[:, b] = -sine * first + cosine * second
            raw_values.append(float(np.sum(np.abs(rotated[0] ** 2 - rotated[1] ** 2))))
        basis_range = max(raw_values) - min(raw_values)
        check(f"independent.basis_witness.seed{seed}.L{L}", basis_range > 0.1
              and source_measure_spread < 1.0e-8,
              f"individual-weight rotation range={basis_range:.6f}")
        probe_summary.append((within_measure, between_measure, source_measure_spread,
                              value_spread, basis_range))

    representatives = [fibre[0] for fibre in FIBRE]
    inverses = [np.linalg.inv(transported[frame]) for frame in representatives]
    index = c696.static_variable_index(L, wrap=False)
    inverse_index = {value: key for key, value in index.items()}
    patterns = Counter()
    constant_classes = Counter()
    far_gap = float("inf")
    close_gap = 0.0
    for slot in range(len(matrix)):
        values = np.asarray([item[slot, slot] for item in inverses])
        for a in range(4):
            for b in range(a + 1, 4):
                gap = abs(float(values[a] - values[b]))
                if gap <= 1.0e-8:
                    close_gap = max(close_gap, gap)
                else:
                    far_gap = min(far_gap, gap)
        pattern_value = partition(values)
        patterns[pattern_value] += 1
        if len(set(pattern_value)) == 1:
            constant_classes[inverse_index[slot][0]] += 1
    expected_patterns, expected_finest, expected_classes = EXPECTED[L]
    check(f"independent.census.L{L}", len(patterns) == expected_patterns
          and patterns[(0, 1, 2, 3)] == expected_finest
          and dict(constant_classes) == expected_classes
          and close_gap < 1.0e-8 and far_gap > 1.0e-5,
          f"patterns={len(patterns)}, finest={patterns[(0,1,2,3)]}, "
          f"classes={dict(sorted(constant_classes.items()))}, gaps={close_gap:.3e}/{far_gap:.3e}")

    basis = np.zeros(len(matrix))
    basis[0] = 1.0
    mutated = transported[0] + 1.0e-3 * np.outer(basis, basis)
    mutation_shift = float(np.max(np.abs(
        np.linalg.eigvalsh(mutated) - np.linalg.eigvalsh(transported[0])
    )))
    check(f"independent.spectral_mutation.L{L}", mutation_shift > 1.0e-5,
          f"rank-one mutation shift={mutation_shift:.3e}")
    RESULTS[str(L)] = {
        "within_matrix": within_matrix,
        "between_matrix": between_matrix,
        "eigenspaces": len(eigenspaces),
        "probe_summary": probe_summary,
        "patterns": len(patterns),
        "finest": patterns[(0, 1, 2, 3)],
    }

primary = json.loads(RECEIPT.read_text(encoding="utf-8"))
check("independent.primary_receipt", primary.get("fail") == 0
      and primary.get("pass") == 82
      and primary.get("box_sizes") == [3, 4]
      and primary.get("probe_seeds") == [7180, 7181]
      and primary.get("notes", {}).get("census_L3", {}).get("patterns") == 14
      and primary.get("notes", {}).get("census_L4", {}).get("patterns") == 15,
      "independent results agree with primary finite anchors")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
