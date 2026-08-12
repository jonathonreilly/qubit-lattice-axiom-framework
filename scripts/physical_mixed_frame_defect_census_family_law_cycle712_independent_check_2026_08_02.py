#!/usr/bin/env python3
"""Independent raw-Hessian check of the Cycle-712 finite family census.

This checker does not import the Cycle-712 primary.  It reconstructs the
bounding-box transport, classifies every large entry of the supplied Cycle-696
static Hessian, derives the six count expressions from an explicit component
descriptor census, and compares the primary receipt only after the independent
calculation has finished.  It does not claim exact non-4 surd magnitudes.
"""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
SPEC = importlib.util.spec_from_file_location("c696_independent_for_c712", MODULE)
c696 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c696)

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02.md",
    "docs/PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md",
    "docs/PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md",
    "scripts/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.py",
    "scripts/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.py",
    "outputs/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02_receipt_2026-08-02.json",
    "outputs/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02_receipt_2026-08-02.json",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "outputs/physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02_receipt_2026-08-02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FRAMES = tuple(np.asarray(frame, dtype=np.int64) for frame in c696.c576.FRAMES)
SPATIAL_CLASSES = tuple(c696.SPATIAL_CLASSES)
DIRECTIONS = {
    cls: np.asarray(c696.regge.DIRS15[cls][:3], dtype=np.int64)
    for cls in SPATIAL_CLASSES
}
SIZES = (3, 4, 5, 6, 7)
CENTERS = np.asarray((2.0, 2.0 * math.sqrt(2.0),
                      2.0 * math.sqrt(3.0), 4.0), dtype=np.float64)
CENTER_NAMES = ("two", "two_rt2", "two_rt3", "four")
PAIR_NAMES = ("swap", "wall", "edge")
LARGE_CUT = 1.5
CENSUS_CUT = 2.0
TOP_CUT = 3.9
CENTER_TOL = 2.0e-7
PAIR_LOW = 0.5
PAIR_HIGH = 10.0

EXPECTED_KEYS = (
    ("four", "swap"),
    ("two_rt3", "swap"),
    ("two_rt2", "swap"),
    ("two_rt2", "wall"),
    ("two", "swap"),
    ("two", "edge"),
)
ANCHORS = {3: (64, 224, 136), 7: (1728, 4896, 4056)}
TOP_ANCHORS = {3: 128, 7: 3456}
RECEIPT = ROOT / "outputs" / (
    "physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02_"
    "receipt_2026-08-02.json"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} {detail}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {label} {detail}".rstrip())


def constant_sign(frame: np.ndarray) -> bool:
    entries = frame[frame != 0]
    return bool(np.all(entries == 1) or np.all(entries == -1))


def transport(L: int, index: dict, frame: np.ndarray) -> np.ndarray:
    """Independent reconstruction of the bounding-box dof relabeling."""
    site_map = c696.frame_site_map(L, frame)
    direction_class = {
        tuple(int(v) for v in DIRECTIONS[cls]): cls for cls in SPATIAL_CLASSES
    }
    result = np.empty(len(index), dtype=np.int64)
    for (cls, site), source in index.items():
        rotated = frame @ DIRECTIONS[cls]
        target_class = direction_class[tuple(int(v) for v in np.abs(rotated))]
        target_site = tuple(
            int(v) for v in (
                np.asarray(site_map[site], dtype=np.int64)
                + np.minimum(rotated, 0)
            )
        )
        result[source] = index[(target_class, target_site)]
    return result


def descriptor_count(key: tuple[str, str], L: int) -> int:
    """Evaluate the independently transcribed component descriptor census.

    Margin 1 means a growing axis of length L-1, margin 2 means length L-2,
    and ``None`` denotes a pinned axis of length 1.
    """
    terms = {
        ("four", "swap"): ((8, (1, 1, 1)),),
        ("two_rt3", "swap"): ((8, (1, 1, 1)),),
        ("two_rt2", "swap"): ((12, (1, 1, 1)),),
        ("two_rt2", "wall"): ((16, (None, 1, 1)),),
        ("two", "swap"): ((12, (1, 1, 1)), (8, (1, 1, 2))),
        ("two", "edge"): ((4, (None, None, 1)),),
    }
    total = 0
    for multiplicity, axes in terms[key]:
        volume = 1
        for margin in axes:
            volume *= 1 if margin is None else L - margin
        total += multiplicity * volume
    return total


def written_count(key: tuple[str, str], L: int) -> int:
    m = L - 1
    if key in (("four", "swap"), ("two_rt3", "swap")):
        return 8 * m ** 3
    if key == ("two_rt2", "swap"):
        return 12 * m ** 3
    if key == ("two_rt2", "wall"):
        return 16 * m ** 2
    if key == ("two", "swap"):
        return 12 * m ** 3 + 8 * m ** 2 * (L - 2)
    if key == ("two", "edge"):
        return 4 * m
    raise KeyError(key)


def main() -> int:
    mixed = tuple(i for i, frame in enumerate(FRAMES) if not constant_sign(frame))
    sextet = tuple(i for i, frame in enumerate(FRAMES) if constant_sign(frame))
    check("frame_partition", len(FRAMES) == 24 and len(sextet) == 6
          and len(mixed) == 18, f"sextet={sextet}")

    for key in EXPECTED_KEYS:
        check(f"descriptor_identity_{key[0]}_{key[1]}",
              all(descriptor_count(key, L) == written_count(key, L)
                  for L in range(3, 11)),
              "component factors equal written expression at L=3..10")

    raw_total = 0
    displaced_center_rejections = 0
    wrong_pair_cut_mismatches = 0
    all_counts: dict[tuple[int, int, str, str], int] = {}

    for L in SIZES:
        model = c696.assemble_static_hessian(L, wrap=False)
        matrix, index = model["Q"], model["index"]
        per_frame_counts = []
        rounded_censuses = set()
        top_counts = set()
        for frame_index in mixed:
            permutation = transport(L, index, FRAMES[frame_index])
            transported = matrix[np.ix_(permutation, permutation)]
            defect = transported - matrix
            magnitude = np.abs(defect)
            mask = magnitude > LARGE_CUT
            values = defect[mask]
            absolute = magnitude[mask]
            raw_total += int(absolute.size)

            distances = np.abs(absolute[:, None] - CENTERS[None, :])
            nearest = np.argmin(distances, axis=1)
            deviations = distances[np.arange(absolute.size), nearest]
            check(f"center_tolerance_L{L}_frame{frame_index}",
                  float(deviations.max()) <= CENTER_TOL,
                  f"max={float(deviations.max()):.2e}")

            smaller_side = np.minimum(np.abs(transported[mask]), np.abs(matrix[mask]))
            pair_class = np.where(smaller_side < PAIR_LOW, 0,
                                  np.where(smaller_side < PAIR_HIGH, 1, 2))
            signs = np.where(values > 0, 1, -1)
            observed = {}
            for sign in (-1, 1):
                for center_i, center_name in enumerate(CENTER_NAMES):
                    for pair_i, pair_name in enumerate(PAIR_NAMES):
                        count = int(np.count_nonzero(
                            (signs == sign) & (nearest == center_i)
                            & (pair_class == pair_i)
                        ))
                        if count:
                            observed[(sign, center_name, pair_name)] = count
                            all_counts[(L, sign, center_name, pair_name)] = count
            wanted_keys = {
                (sign, center_name, pair_name)
                for sign in (-1, 1)
                for center_name, pair_name in EXPECTED_KEYS
            }
            counts_ok = set(observed) == wanted_keys
            for sign in (-1, 1):
                for key in EXPECTED_KEYS:
                    counts_ok = counts_ok and (
                        observed.get((sign,) + key) == descriptor_count(key, L)
                    )
            per_frame_counts.append(observed)
            check(f"raw_family_counts_L{L}_frame{frame_index}", counts_ok,
                  "all twelve counts equal component expressions")

            rounded, multiplicity = np.unique(
                np.rint(defect[magnitude > CENSUS_CUT]).astype(np.int64),
                return_counts=True,
            )
            rounded_censuses.add(tuple(zip(rounded.tolist(), multiplicity.tolist())))
            top_counts.add(int(np.count_nonzero(magnitude > TOP_CUT)))

            displaced = CENTERS.copy()
            displaced[2] += 0.25
            bad_distances = np.abs(absolute[:, None] - displaced[None, :])
            displaced_center_rejections += int(np.count_nonzero(
                bad_distances.min(axis=1) > CENTER_TOL
            ))

            wrong_class = np.where(smaller_side < PAIR_LOW, 0,
                                   np.where(smaller_side < 5.0, 1, 2))
            wrong_pair_cut_mismatches += int(np.count_nonzero(wrong_class != pair_class))

        check(f"frame_uniformity_L{L}",
              all(row == per_frame_counts[0] for row in per_frame_counts[1:]),
              "all 18 independently rebuilt frame censuses agree")
        if L in ANCHORS:
            n4, n3, n2 = ANCHORS[L]
            wanted = tuple(sorted(((-4, n4), (-3, n3), (-2, n2),
                                   (2, n2), (3, n3), (4, n4))))
            check(f"rounded_anchor_L{L}", rounded_censuses == {wanted},
                  f"anchor={wanted}")
            check(f"top_family_L{L}", top_counts == {TOP_ANCHORS[L]},
                  f"count={TOP_ANCHORS[L]}")

    check("complete_scan_total", raw_total == 789120, f"entries={raw_total}")
    check("displaced_center_rejector", displaced_center_rejections > 0,
          f"rejected_entries={displaced_center_rejections}")
    check("wrong_pair_cut_rejector", wrong_pair_cut_mismatches > 0,
          f"reclassified_entries={wrong_pair_cut_mismatches}")
    check("wrong_coefficient_rejector",
          any(9 * (L - 1) ** 3 != descriptor_count(("four", "swap"), L)
              for L in SIZES),
          "coefficient 9 cannot replace component multiplicity 8")

    receipt = json.loads(RECEIPT.read_text())
    check("primary_receipt_all_gates_pass",
          bool(receipt["gates"]) and all(gate["pass"] for gate in receipt["gates"].values()))
    receipt_counts = receipt["notes"]["counts_per_sign"]
    expected_receipt = {
        "|".join(key): [descriptor_count(key, L) for L in SIZES]
        for key in EXPECTED_KEYS
    }
    check("primary_receipt_count_agreement", receipt_counts == expected_receipt,
          "receipt counts equal independent component arithmetic")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
