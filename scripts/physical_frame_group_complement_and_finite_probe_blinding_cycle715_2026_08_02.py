#!/usr/bin/env python3
"""Cycle 715 -- finite frame-group complement and probe-blinding census.

For the supplied Cycle-696 open-box static Hessian at L in {3, 4}, this runner
finds the same numerical near-zero-defect sextet at both sizes.  It then checks
the exact finite-group statements conditional on that measured sextet: the
sextet is a subgroup, the independently reconstructed Cycle-707 decorated-source
stabilizer is an order-four complement, and the 24 frame labels split into four
right cosets.  The transported Hessians form four separated numerical clusters.

The subgroup-covering condition S H = G is proved sufficient for a subgroup
average to make the quadratic probe pairing frame-independent.  All 30
subgroups are tested for three disclosed deterministic Gaussian probes at each
size.  This is not a universal necessity theorem: an all-ones probe is carried
as an explicit accidental-symmetry witness that is already blind for H={e}.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_for_c715", MODULE)
c696 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c696)

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md",
    "docs/PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md",
    "scripts/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01.py",
    "outputs/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01_receipt_2026-08-01.json",
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
CLASS_OF = {
    tuple(int(v) for v in DIRECTIONS[cls]): cls for cls in SPATIAL_CLASSES
}
EYE = np.eye(3, dtype=np.int64)
RX = np.asarray(((1, 0, 0), (0, 0, -1), (0, 1, 0)), dtype=np.int64)
SIZES = (3, 4)
SOURCE_STABILIZER_SIZES = (3, 7)
ZERO_TOL = 1.0e-9
CLUSTER_TOL = 1.0e-6
SEPARATION_FLOOR = 1.0
BLIND_TOL = 1.0e-6
PROBE_SEEDS = {L: 7150 + L for L in SIZES}
RECEIPT_NAME = (
    "physical_frame_group_complement_and_finite_probe_blinding_cycle715_"
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
    raise ValueError("matrix is outside the supplied proper-frame table")


MULTIPLY = tuple(
    tuple(frame_index(FRAMES[a] @ FRAMES[b]) for b in range(24))
    for a in range(24)
)
IDENTITY = frame_index(EYE)


def relabel(L: int, frame_index_value: int) -> np.ndarray:
    """Reconstruct the Cycle-696 bounding-box coframe relabeling."""
    index = c696.static_variable_index(L, False)
    site_map = c696.frame_site_map(L, FRAMES[frame_index_value])
    mapping = np.empty(len(index), dtype=np.int64)
    for (cls, site), source in index.items():
        rotated = FRAMES[frame_index_value] @ DIRECTIONS[cls]
        target_site = tuple(
            int(value)
            for value in (
                np.asarray(site_map[site], dtype=np.int64)
                + np.minimum(rotated, 0)
            )
        )
        target_cls = CLASS_OF[tuple(int(value) for value in np.abs(rotated))]
        mapping[source] = index[(target_cls, target_site)]
    return mapping


def subgroup_closure(generators: tuple[int, ...]) -> tuple[int, ...]:
    members = set(generators) | {IDENTITY}
    while True:
        products = {MULTIPLY[a][b] for a in members for b in members}
        if products <= members:
            return tuple(sorted(members))
        members |= products


def all_subgroups() -> list[tuple[int, ...]]:
    result = {(IDENTITY,)}
    for count in (1, 2, 3):
        for generators in itertools.combinations(range(24), count):
            result.add(subgroup_closure(generators))
    return sorted(result, key=lambda subgroup: (len(subgroup), subgroup))


def product_set(left: tuple[int, ...] | list[int],
                right: tuple[int, ...] | list[int]) -> set[int]:
    return {MULTIPLY[a][b] for a in left for b in right}


def source_stabilizer(L: int) -> tuple[int, ...]:
    """Independently reconstruct Cycle 707's centered one-edit domain."""
    anchor = (L - 1) // 2
    domain = c696.build_domain(
        L,
        edits={((anchor, anchor, anchor), (anchor + 1, anchor, anchor)): 5},
    )
    key = c696.domain_key(domain)
    return tuple(
        g for g, frame in enumerate(FRAMES)
        if c696.domain_key(c696.apply_frame_to_domain(domain, frame)) == key
    )


def transformed_source(probe: np.ndarray, mapping: np.ndarray) -> np.ndarray:
    """Apply the source pullback paired with Q[m,m]."""
    return probe[np.argsort(mapping)]


def averaged_source(probe: np.ndarray, subgroup: tuple[int, ...],
                    mappings: dict[int, np.ndarray]) -> np.ndarray:
    total = np.zeros_like(probe)
    for frame in subgroup:
        total += transformed_source(probe, mappings[frame])
    return total / float(len(subgroup))


def pairing_spread(probe: np.ndarray, subgroup: tuple[int, ...],
                   mappings: dict[int, np.ndarray],
                   transported: dict[int, np.ndarray]) -> tuple[float, float, float]:
    average = averaged_source(probe, subgroup, mappings)
    norm = float(np.linalg.norm(average))
    if norm == 0.0:
        return float("inf"), norm, float("inf")
    average /= norm
    invariance = max(
        float(np.linalg.norm(transformed_source(average, mappings[h]) - average))
        for h in subgroup
    )
    values = [
        float(average @ np.linalg.solve(transported[g], average))
        for g in range(24)
    ]
    return max(values) - min(values), norm, invariance


print("=== Cycle 715: exact frame labels and measured assembly premise ===")
determinants = tuple(round(float(np.linalg.det(frame))) for frame in FRAMES)
check("G.group.frames", len(FRAMES) == 24 and len({frame.tobytes() for frame in FRAMES}) == 24
      and set(determinants) == {1}, "24 distinct determinant-one signed permutations")
check("G.group.identity", all(MULTIPLY[IDENTITY][g] == g and MULTIPLY[g][IDENTITY] == g
                                    for g in range(24)), f"identity frame={IDENTITY}")
check("G.group.associative", all(MULTIPLY[MULTIPLY[a][b]][c] == MULTIPLY[a][MULTIPLY[b][c]]
                                      for a in range(24) for b in range(24) for c in range(24)),
      "24^3 multiplication-table comparisons")

MODELS: dict[int, np.ndarray] = {}
MAPPINGS: dict[int, dict[int, np.ndarray]] = {}
TRANSPORTED: dict[int, dict[int, np.ndarray]] = {}
SEXTETS: dict[int, tuple[int, ...]] = {}
for L in SIZES:
    Q = np.asarray(c696.assemble_static_hessian(L, False)["Q"], dtype=np.float64)
    mappings = {g: relabel(L, g) for g in range(24)}
    transported = {g: Q[np.ix_(mappings[g], mappings[g])] for g in range(24)}
    sextet = tuple(g for g in range(24)
                   if float(np.max(np.abs(transported[g] - Q))) < ZERO_TOL)
    composition_matches = sum(
        np.array_equal(mappings[MULTIPLY[a][b]], mappings[a][mappings[b]])
        for a in range(24) for b in range(24)
    )
    reversed_matches = sum(
        np.array_equal(mappings[MULTIPLY[a][b]], mappings[b][mappings[a]])
        for a in range(24) for b in range(24)
    )
    singular_values = np.linalg.svd(Q, compute_uv=False)
    MODELS[L] = Q
    MAPPINGS[L] = mappings
    TRANSPORTED[L] = transported
    SEXTETS[L] = sextet
    check(f"G.relabel.compose.L{L}", composition_matches == 576,
          f"m_ab=m_a∘m_b for {composition_matches}/576 pairs")
    check(f"G.relabel.reverse_rejector.L{L}", reversed_matches < 576,
          f"reversed order matches only {reversed_matches}/576 pairs")
    check(f"G.sextet.order.L{L}", len(sextet) == 6,
          f"near-zero-defect labels={list(sextet)} at tolerance {ZERO_TOL:.1e}")
    check(f"G.solve.margin.L{L}", float(singular_values[-1]) > 1.0e-3,
          f"min singular={singular_values[-1]:.3e}, condition={singular_values[0]/singular_values[-1]:.3e}")

S = SEXTETS[3]
check("G.sextet.same", SEXTETS[3] == SEXTETS[4],
      f"L3={list(SEXTETS[3])}, L4={list(SEXTETS[4])}")
check("G.sextet.subgroup", subgroup_closure(S) == tuple(sorted(S)),
      f"closure={list(subgroup_closure(S))}")

c4_members = []
power = EYE.copy()
for _ in range(4):
    c4_members.append(frame_index(power))
    power = power @ RX
C4 = tuple(sorted(c4_members))
derived_stabilizers = {L: source_stabilizer(L) for L in SOURCE_STABILIZER_SIZES}
check("G.source_stabilizer.reconstructed", all(stabilizer == C4 for stabilizer in derived_stabilizers.values()),
      f"C4={list(C4)}, derived={{{', '.join(f'{L}: {list(v)}' for L, v in derived_stabilizers.items())}}}")
check("G.complement.intersection", set(S) & set(C4) == {IDENTITY},
      f"intersection={sorted(set(S) & set(C4))}")
check("G.complement.cover", len(product_set(S, C4)) == 24,
      f"|S C4|={len(product_set(S, C4))}")

BAD4 = (0, 4, 19, 23)
check("G.complement.hostile_overlap", len(set(S) & set(BAD4)) == 2
      and len(product_set(S, BAD4)) == 12,
      f"candidate={BAD4}, intersection={len(set(S)&set(BAD4))}, coverage={len(product_set(S, BAD4))}")

RIGHT_COSETS = tuple(tuple(sorted(MULTIPLY[s][representative] for s in S))
                     for representative in c4_members)
LEFT_BLOCKS = tuple(tuple(sorted(MULTIPLY[representative][s] for s in S))
                    for representative in c4_members)
check("G.cosets.partition", sorted(g for block in RIGHT_COSETS for g in block) == list(range(24))
      and len(set(RIGHT_COSETS)) == 4, f"right cosets={RIGHT_COSETS}")

print("=== Transported-Hessian numerical clusters ===")
cluster_rows: dict[int, dict[str, float]] = {}
for L in SIZES:
    Q = MODELS[L]
    transported = TRANSPORTED[L]
    within = max(float(np.max(np.abs(transported[g] - transported[block[0]])))
                 for block in RIGHT_COSETS for g in block)
    representatives = [transported[block[0]] for block in RIGHT_COSETS]
    across = min(float(np.max(np.abs(representatives[a] - representatives[b])))
                 for a in range(4) for b in range(a + 1, 4))
    left_spread = max(float(np.max(np.abs(transported[g] - transported[block[0]])))
                      for block in LEFT_BLOCKS for g in block)
    nonmember_gap = min(float(np.max(np.abs(transported[g] - Q)))
                        for g in range(24) if g not in S)
    mutated = Q.copy()
    mutated[0, 0] += 0.25
    mutation_sextet_spread = max(
        float(np.max(np.abs(mutated[np.ix_(MAPPINGS[L][s], MAPPINGS[L][s])] - mutated)))
        for s in S
    )
    check(f"Q.cluster.within.L{L}", within < CLUSTER_TOL,
          f"within={within:.3e}, tolerance={CLUSTER_TOL:.1e}")
    check(f"Q.cluster.separation.L{L}", across > SEPARATION_FLOOR,
          f"between-cluster minimum={across:.6f}")
    check(f"Q.sextet.gap.L{L}", nonmember_gap > SEPARATION_FLOOR,
          f"nearest nonmember defect={nonmember_gap:.6f}")
    check(f"Q.coset_orientation.hostile.L{L}", left_spread > SEPARATION_FLOOR,
          f"left-block spread={left_spread:.6f}")
    check(f"Q.matrix_mutation.hostile.L{L}", mutation_sextet_spread > 0.1,
          f"single-entry mutation raises sextet spread to {mutation_sextet_spread:.3e}")
    cluster_rows[L] = {"within": within, "across": across,
                       "left_spread": left_spread, "nonmember_gap": nonmember_gap}

print("=== Exact subgroup covering census and finite probe observations ===")
SUBGROUPS = all_subgroups()
check("H.subgroups.count", len(SUBGROUPS) == 30, f"count={len(SUBGROUPS)}")
covering_law_matches = 0
COVERING = []
for subgroup in SUBGROUPS:
    covers = len(product_set(S, subgroup)) == 24
    count_condition = len(subgroup) == 4 * len(set(S) & set(subgroup))
    covering_law_matches += int(covers == count_condition)
    if covers:
        COVERING.append(subgroup)
MINIMAL_COVERING = [subgroup for subgroup in COVERING
                    if len(subgroup) == min(len(candidate) for candidate in COVERING)]
check("H.covering.count_law", covering_law_matches == len(SUBGROUPS),
      f"matches={covering_law_matches}/{len(SUBGROUPS)}")
check("H.covering.orders", sorted(len(subgroup) for subgroup in COVERING)
      == [4, 4, 4, 4, 8, 8, 8, 12, 24],
      f"orders={sorted(len(subgroup) for subgroup in COVERING)}")
check("H.covering.minimum", len(MINIMAL_COVERING) == 4
      and all(len(subgroup) == 4 for subgroup in MINIMAL_COVERING)
      and C4 in MINIMAL_COVERING,
      f"minimum covering subgroups={MINIMAL_COVERING}")

probe_rows: dict[int, dict[str, float | int]] = {}
for L in SIZES:
    rng = np.random.default_rng(PROBE_SEEDS[L])
    probes = []
    for _ in range(3):
        probe = rng.normal(size=MODELS[L].shape[0])
        probes.append(probe / np.linalg.norm(probe))
    observed_matches = 0
    covering_worst = 0.0
    noncovering_best = float("inf")
    minimum_average_norm = float("inf")
    maximum_invariance_residual = 0.0
    for subgroup in SUBGROUPS:
        spreads = []
        for probe in probes:
            spread, norm, invariance = pairing_spread(
                probe, subgroup, MAPPINGS[L], TRANSPORTED[L]
            )
            spreads.append(spread)
            minimum_average_norm = min(minimum_average_norm, norm)
            maximum_invariance_residual = max(maximum_invariance_residual, invariance)
        worst_spread = max(spreads)
        covers = subgroup in COVERING
        observed_matches += int((worst_spread < BLIND_TOL) == covers)
        if covers:
            covering_worst = max(covering_worst, worst_spread)
        else:
            noncovering_best = min(noncovering_best, worst_spread)
    ones = np.ones(MODELS[L].shape[0], dtype=np.float64)
    ones /= np.linalg.norm(ones)
    accidental_spread, accidental_norm, accidental_invariance = pairing_spread(
        ones, (IDENTITY,), MAPPINGS[L], TRANSPORTED[L]
    )
    check(f"H.probes.scan.L{L}", observed_matches == 30,
          f"three seed-{PROBE_SEEDS[L]} Gaussian probes agree on {observed_matches}/30 subgroups")
    check(f"H.probes.covering_sufficiency.L{L}", covering_worst < BLIND_TOL,
          f"covering worst={covering_worst:.3e}")
    check(f"H.probes.noncovering_witness.L{L}", noncovering_best > 1.0e-3,
          f"smallest noncovering Gaussian spread={noncovering_best:.3e}")
    check(f"H.probes.average_invariance.L{L}", maximum_invariance_residual < 1.0e-12,
          f"max H-invariance residual={maximum_invariance_residual:.3e}")
    check(f"H.probes.no_cancellation.L{L}", minimum_average_norm > 1.0e-8,
          f"minimum pre-normalization average norm={minimum_average_norm:.3e}")
    check(f"H.accidental_ones.L{L}", accidental_spread < BLIND_TOL
          and accidental_norm > 0.99 and accidental_invariance < 1.0e-12,
          f"H={{e}} all-ones spread={accidental_spread:.3e}")
    probe_rows[L] = {
        "seed": PROBE_SEEDS[L],
        "observed_matches": observed_matches,
        "covering_worst": covering_worst,
        "noncovering_best": noncovering_best,
        "average_invariance_residual": maximum_invariance_residual,
        "minimum_average_norm": minimum_average_norm,
        "all_ones_identity_spread": accidental_spread,
    }

NOTES.update({
    "sizes": list(SIZES),
    "near_zero_defect_tolerance": ZERO_TOL,
    "near_zero_defect_sextet": list(S),
    "source_stabilizer": list(C4),
    "right_cosets": [list(block) for block in RIGHT_COSETS],
    "subgroup_count": len(SUBGROUPS),
    "covering_orders": sorted(len(subgroup) for subgroup in COVERING),
    "minimum_covering_subgroups": [list(subgroup) for subgroup in MINIMAL_COVERING],
    "cluster_rows": cluster_rows,
    "probe_rows": probe_rows,
})
receipt = {
    "box_sizes": list(SIZES),
    "pass": PASS,
    "fail": FAIL,
    "gates": GATES,
    "notes": NOTES,
    "runner": Path(__file__).name,
}
(ROOT / "outputs").mkdir(exist_ok=True)
(ROOT / "outputs" / RECEIPT_NAME).write_text(
    json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8"
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
