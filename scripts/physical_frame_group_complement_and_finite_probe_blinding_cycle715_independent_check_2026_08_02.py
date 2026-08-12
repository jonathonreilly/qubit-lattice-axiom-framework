#!/usr/bin/env python3
"""Independent check of the Cycle-715 finite group and probe claims.

This checker does not import the primary runner.  It rebuilds the frame action,
group table, source stabilizer, static Hessians, subgroup lattice, and quadratic
pairings from the Cycle-696 compiler, then compares the primary receipt only
after its own calculations.  It also carries wrong-composition, wrong-coset,
non-complement, and accidental-source witnesses.
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
SPEC = importlib.util.spec_from_file_location("c696_independent_for_c715", MODULE)
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
    "outputs/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02_receipt_2026-08-02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FRAMES = tuple(np.asarray(frame, dtype=np.int64) for frame in c696.c576.FRAMES)
CLASSES = tuple(c696.SPATIAL_CLASSES)
VECTORS = {cls: np.asarray(c696.regge.DIRS15[cls][:3], dtype=np.int64) for cls in CLASSES}
VECTOR_CLASS = {tuple(int(x) for x in VECTORS[cls]): cls for cls in CLASSES}
IDENTITY_MATRIX = np.eye(3, dtype=np.int64)
RX = np.asarray(((1, 0, 0), (0, 0, -1), (0, 1, 0)), dtype=np.int64)
SIZES = (3, 4)
SEEDS = {3: 7153, 4: 7154}
RECEIPT = ROOT / "outputs" / (
    "physical_frame_group_complement_and_finite_probe_blinding_cycle715_"
    "2026_08_02_receipt_2026-08-02.json"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name} {detail}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {name} {detail}".rstrip())


def locate(matrix: np.ndarray) -> int:
    return next(i for i, frame in enumerate(FRAMES) if np.array_equal(frame, matrix))


TABLE = tuple(tuple(locate(FRAMES[a] @ FRAMES[b]) for b in range(24)) for a in range(24))
IDENTITY = locate(IDENTITY_MATRIX)


def permutation(L: int, g: int) -> np.ndarray:
    index = c696.static_variable_index(L, wrap=False)
    sites = c696.frame_site_map(L, FRAMES[g])
    answer = np.empty(len(index), dtype=np.int64)
    for key, old_index in index.items():
        cls, site = key
        image = FRAMES[g].dot(VECTORS[cls])
        image_cls = VECTOR_CLASS[tuple(int(x) for x in np.abs(image))]
        image_site_array = np.asarray(sites[site], dtype=np.int64) + np.minimum(image, 0)
        image_site = tuple(int(x) for x in image_site_array)
        answer[old_index] = index[(image_cls, image_site)]
    return answer


def close(generators: tuple[int, ...]) -> tuple[int, ...]:
    result = {IDENTITY, *generators}
    changed = True
    while changed:
        before = len(result)
        result |= {TABLE[x][y] for x in tuple(result) for y in tuple(result)}
        changed = len(result) != before
    return tuple(sorted(result))


def subgroup_list() -> list[tuple[int, ...]]:
    groups = {(IDENTITY,)}
    for width in (1, 2, 3):
        groups.update(close(gens) for gens in itertools.combinations(range(24), width))
    return sorted(groups, key=lambda group: (len(group), group))


def product_size(first: tuple[int, ...], second: tuple[int, ...]) -> int:
    return len({TABLE[x][y] for x in first for y in second})


def derive_source_stabilizer(L: int) -> tuple[int, ...]:
    a = (L - 1) // 2
    source = c696.build_domain(L, edits={((a, a, a), (a + 1, a, a)): 5})
    source_key = c696.domain_key(source)
    return tuple(g for g in range(24)
                 if c696.domain_key(c696.apply_frame_to_domain(source, FRAMES[g])) == source_key)


def pullback(vector: np.ndarray, perm: np.ndarray) -> np.ndarray:
    answer = np.empty_like(vector)
    answer[perm] = vector
    return answer


def spread(vector: np.ndarray, group: tuple[int, ...], perms: tuple[np.ndarray, ...],
           hessians: tuple[np.ndarray, ...]) -> tuple[float, float]:
    averaged = sum((pullback(vector, perms[g]) for g in group), np.zeros_like(vector))
    averaged /= float(len(group))
    norm = float(np.linalg.norm(averaged))
    averaged /= norm
    invariance = max(float(np.linalg.norm(pullback(averaged, perms[g]) - averaged)) for g in group)
    values = [float(averaged.dot(np.linalg.solve(matrix, averaged))) for matrix in hessians]
    return max(values) - min(values), invariance


subgroups = subgroup_list()
check("I.group", len(subgroups) == 30 and all(len(close(group)) == len(group) for group in subgroups),
      f"subgroups={len(subgroups)}")

c4_values = []
power = IDENTITY_MATRIX.copy()
for _ in range(4):
    c4_values.append(locate(power))
    power = power.dot(RX)
C4 = tuple(sorted(c4_values))
stabilizers = {L: derive_source_stabilizer(L) for L in (3, 7)}
check("I.source_stabilizer", all(value == C4 for value in stabilizers.values()),
      f"C4={C4}, derived={stabilizers}")

results = {}
common_sextet = None
for L in SIZES:
    Q = np.asarray(c696.assemble_static_hessian(L, wrap=False)["Q"], dtype=float)
    perms = tuple(permutation(L, g) for g in range(24))
    hessians = tuple(Q[np.ix_(perm, perm)] for perm in perms)
    sextet = tuple(g for g in range(24) if np.max(np.abs(hessians[g] - Q)) < 1.0e-9)
    if common_sextet is None:
        common_sextet = sextet
    composition = sum(np.array_equal(perms[TABLE[a][b]], perms[a][perms[b]])
                      for a in range(24) for b in range(24))
    wrong_composition = sum(np.array_equal(perms[TABLE[a][b]], perms[b][perms[a]])
                            for a in range(24) for b in range(24))
    check(f"I.action.L{L}", composition == 576 and wrong_composition == 120,
          f"correct={composition}, reversed={wrong_composition}")
    check(f"I.sextet.L{L}", sextet == common_sextet and close(sextet) == sextet,
          f"sextet={sextet}")
    right = tuple(tuple(sorted(TABLE[s][r] for s in sextet)) for r in c4_values)
    left = tuple(tuple(sorted(TABLE[r][s] for s in sextet)) for r in c4_values)
    within = max(float(np.max(np.abs(hessians[g] - hessians[block[0]])))
                 for block in right for g in block)
    across = min(float(np.max(np.abs(hessians[right[a][0]] - hessians[right[b][0]])))
                 for a in range(4) for b in range(a + 1, 4))
    left_spread = max(float(np.max(np.abs(hessians[g] - hessians[block[0]])))
                      for block in left for g in block)
    check(f"I.clusters.L{L}", within < 1.0e-6 and across > 1.0,
          f"within={within:.3e}, across={across:.6f}")
    check(f"I.orientation_witness.L{L}", left_spread > 1.0,
          f"left-block spread={left_spread:.6f}")

    covering = [group for group in subgroups if product_size(sextet, group) == 24]
    count_law = sum((group in covering) == (len(group) == 4 * len(set(group) & set(sextet)))
                    for group in subgroups)
    check(f"I.covering.L{L}", count_law == 30
          and sorted(len(group) for group in covering) == [4, 4, 4, 4, 8, 8, 8, 12, 24],
          f"count-law={count_law}/30")
    bad = (0, 4, 19, 23)
    check(f"I.noncomplement_witness.L{L}", product_size(sextet, bad) == 12,
          f"bad order-four coverage={product_size(sextet, bad)}")

    random = np.random.default_rng(SEEDS[L])
    probes = []
    for _ in range(3):
        vector = random.normal(size=Q.shape[0])
        probes.append(vector / np.linalg.norm(vector))
    classifications = 0
    covering_max = 0.0
    noncovering_min = float("inf")
    invariant_max = 0.0
    for group in subgroups:
        values = [spread(probe, group, perms, hessians) for probe in probes]
        group_spread = max(value[0] for value in values)
        invariant_max = max(invariant_max, max(value[1] for value in values))
        predicted = group in covering
        classifications += int((group_spread < 1.0e-6) == predicted)
        if predicted:
            covering_max = max(covering_max, group_spread)
        else:
            noncovering_min = min(noncovering_min, group_spread)
    check(f"I.probes.L{L}", classifications == 30 and covering_max < 1.0e-6
          and noncovering_min > 1.0e-3 and invariant_max < 1.0e-12,
          f"matches={classifications}/30, cover={covering_max:.3e}, noncover={noncovering_min:.3e}")
    ones = np.ones(Q.shape[0], dtype=float)
    ones /= np.linalg.norm(ones)
    ones_spread, _ = spread(ones, (IDENTITY,), perms, hessians)
    check(f"I.accidental_source.L{L}", ones_spread < 1.0e-6,
          f"identity-subgroup all-ones spread={ones_spread:.3e}")
    results[str(L)] = {"within": within, "across": across,
                       "covering_max": covering_max, "noncovering_min": noncovering_min,
                       "all_ones_identity_spread": ones_spread}

check("I.factorization", common_sextet is not None
      and set(common_sextet) & set(C4) == {IDENTITY}
      and product_size(common_sextet, C4) == 24,
      f"S={common_sextet}, C4={C4}")

primary = json.loads(RECEIPT.read_text(encoding="utf-8"))
check("I.primary_receipt", primary.get("fail") == 0
      and primary.get("notes", {}).get("near_zero_defect_sextet") == list(common_sextet)
      and primary.get("notes", {}).get("source_stabilizer") == list(C4)
      and primary.get("notes", {}).get("subgroup_count") == 30,
      "independent facts agree with the primary receipt")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
