#!/usr/bin/env python3
"""Corrected eight-term structured-mirror sliced runner.

This registered runner executes every one of the 32 documented slice
configurations on all six canonical seeds.  It preserves the structured-mirror
graph, including two-layer-back edges that can bypass the selected barrier
layer, and evaluates

    I3 = P(ABC)-P(AB)-P(AC)-P(BC)+P(A)+P(B)+P(C)-P(empty).

The runner also exposes the defective legacy seven-term residual and
``P(empty)``.  Hostile controls independently recompute all eight masks on
deterministic bypass/no-bypass graphs, reject a wrong-sign mutant, and check
the exact integer coefficient identity for a quadratic probability of a
strictly linear amplitude sum.

Numerical cancellation at the configured tolerance is finite floating-point
evidence.  The coefficient identity supplies the exact boundary, conditional
on the supplied fixed-graph strictly linear propagator and quadratic detector
probability convention.
"""

from __future__ import annotations

import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.mirror_born_audit import propagate_LINEAR
from scripts.structured_mirror_bornsafe_scan import measure_config, sorkin_born


AUDIT_TIMEOUT_SEC = 180
BORN_SAFETY_THRESHOLD = 1e-14
CONTROL_ABS_TOL = 5e-14
SEEDS = [s * 7 + 3 for s in range(6)]
K_VALUE = 5.0
SLIT_GAP = 2.0


# The registered slice is unchanged: documented old best, grid corners,
# center, near-best neighbourhood, and jittered configurations.
SLICED_CONFIGS: list[tuple[int, int, float, float, float]] = [
    (40, 12, 3.0, 1.25, 0.0),
    (25, 8, 2.5, 1.25, 0.0),
    (25, 8, 4.5, 1.25, 0.0),
    (25, 20, 2.5, 1.25, 0.0),
    (25, 20, 4.5, 1.25, 0.0),
    (40, 8, 2.5, 1.25, 0.0),
    (40, 8, 4.5, 1.25, 0.0),
    (40, 20, 2.5, 1.25, 0.0),
    (40, 20, 4.5, 1.25, 0.0),
    (30, 12, 3.5, 1.25, 0.0),
    (30, 16, 3.5, 1.25, 0.0),
    (40, 12, 2.5, 1.25, 0.0),
    (40, 12, 3.5, 1.25, 0.0),
    (40, 12, 3.0, 1.0, 0.0),
    (40, 12, 3.0, 1.5, 0.0),
    (40, 16, 3.0, 1.25, 0.0),
    (40, 8, 3.0, 1.25, 0.0),
    (30, 12, 3.0, 1.25, 0.0),
    (25, 8, 2.5, 1.0, 0.0),
    (25, 8, 2.5, 1.5, 0.0),
    (40, 20, 4.5, 1.0, 0.0),
    (40, 20, 4.5, 1.5, 0.0),
    (25, 8, 2.5, 1.25, 0.15),
    (25, 8, 2.5, 1.25, 0.30),
    (40, 12, 3.0, 1.25, 0.15),
    (40, 12, 3.0, 1.25, 0.30),
    (40, 20, 4.5, 1.25, 0.15),
    (40, 20, 4.5, 1.25, 0.30),
    (30, 16, 3.5, 1.25, 0.15),
    (30, 16, 3.5, 1.25, 0.30),
    (25, 20, 4.5, 1.5, 0.30),
    (40, 8, 2.5, 1.0, 0.15),
]


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def fmt_config(config: tuple[int, int, float, float, float]) -> str:
    n_layers, npl_half, connect_radius, grid_spacing, layer_jitter = config
    return (
        f"N={n_layers:2d} npl={npl_half:2d} r={connect_radius:.1f} "
        f"g={grid_spacing:.2f} j={layer_jitter:.2f}"
    )


def six_seed_measurements(config: tuple[int, int, float, float, float]) -> dict:
    """Execute all six seeds; an invalid seed is retained as a hard failure."""
    n_layers, npl_half, connect_radius, grid_spacing, layer_jitter = config
    samples = []
    errors = []
    for seed in SEEDS:
        try:
            row = measure_config(
                n_layers=n_layers,
                npl_half=npl_half,
                connect_radius=connect_radius,
                grid_spacing=grid_spacing,
                layer_jitter=layer_jitter,
                seed=seed,
                k=K_VALUE,
                slit_gap=SLIT_GAP,
                strict=True,
            )
        except ValueError as exc:
            errors.append(f"seed={seed}: {exc}")
            continue
        samples.append({"seed": seed, **row})

    result = {"ok": len(samples), "samples": samples, "errors": errors}
    if len(samples) != len(SEEDS):
        return result

    for key in (
        "born_corrected",
        "born_legacy",
        "p_empty_ratio",
        "dtv",
        "pur_cl",
        "s_norm",
        "gravity",
        "grav_k0",
    ):
        values = [sample[key] for sample in samples]
        result[f"{key}_mean"] = mean(values)
        result[f"{key}_min"] = min(values)
        result[f"{key}_max"] = max(values)
    result["legacy_empty_mismatch_max"] = max(
        abs(sample["born_legacy"] - sample["p_empty_ratio"])
        for sample in samples
    )
    return result


def independent_eight_mask_recompute(
    positions,
    adj,
    src,
    k,
    barrier_nodes,
    slit_a,
    slit_b,
    slit_c,
    det_list,
    field,
):
    """Separately written eight-mask probability recomputation.

    This deliberately does not call ``sorkin_born``.
    """
    barrier = set(barrier_nodes)
    a = set(slit_a)
    b = set(slit_b)
    c = set(slit_c)
    open_sets = (
        ("abc", a | b | c),
        ("ab", a | b),
        ("ac", a | c),
        ("bc", b | c),
        ("a", a),
        ("b", b),
        ("c", c),
        ("empty", set()),
    )
    probabilities = {}
    for label, open_nodes in open_sets:
        blocked = barrier - open_nodes
        amps = propagate_LINEAR(positions, adj, field, src, k, blocked)
        probabilities[label] = sum(abs(amps[d]) ** 2 for d in det_list)
    legacy = (
        probabilities["abc"]
        - probabilities["ab"]
        - probabilities["ac"]
        - probabilities["bc"]
        + probabilities["a"]
        + probabilities["b"]
        + probabilities["c"]
    )
    corrected = legacy - probabilities["empty"]
    return probabilities, legacy, corrected


def deterministic_control_graph(*, bypass: bool):
    """One barrier layer with optional source-to-detector bypass edge."""
    positions = [
        (0.0, 0.0, 0.0),
        (1.0, 3.0, 0.0),
        (1.0, -3.0, 0.0),
        (1.0, 0.0, 0.0),
        (2.0, 0.5, 0.0),
    ]
    adj = {
        0: [1, 2, 3] + ([4] if bypass else []),
        1: [4],
        2: [4],
        3: [4],
    }
    return (
        positions,
        adj,
        [0],
        0.0,
        [1, 2, 3],
        [1],
        [2],
        [3],
        [4],
        [0.0] * 5,
    )


def coefficient_table(*, include_empty: bool, empty_sign: int = -1):
    """Exact integer coefficients of z_i conjugate(z_j) in inclusion-exclusion."""
    masks = [
        (1, {"D", "A", "B", "C"}),
        (-1, {"D", "A", "B"}),
        (-1, {"D", "A", "C"}),
        (-1, {"D", "B", "C"}),
        (1, {"D", "A"}),
        (1, {"D", "B"}),
        (1, {"D", "C"}),
    ]
    if include_empty:
        masks.append((empty_sign, {"D"}))
    names = ("D", "A", "B", "C")
    return {
        (left, right): sum(
            sign for sign, present in masks if left in present and right in present
        )
        for left in names
        for right in names
    }


def report_control(name: str, ok: bool, detail: str) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return ok


def run_hostile_controls() -> bool:
    print("HOSTILE CONTROLS AND INDEPENDENT CHECKS")
    checks = []

    bypass_args = deterministic_control_graph(bypass=True)
    bypass = sorkin_born(*bypass_args)
    independent_probs, independent_legacy, independent_corrected = (
        independent_eight_mask_recompute(*bypass_args)
    )
    probability_mismatch = max(
        abs(bypass.probabilities[key] - independent_probs[key])
        for key in bypass.probabilities
    )
    scale = max(1.0, bypass.p_abc)
    checks.append(
        report_control(
            "deterministic bypass rejects legacy statistic",
            bypass.empty_ratio > 1e-6
            and abs(bypass.legacy_i3 - bypass.p_empty) <= CONTROL_ABS_TOL * scale
            and bypass.corrected_ratio <= BORN_SAFETY_THRESHOLD,
            (
                f"P0/P={bypass.empty_ratio:.6e}, "
                f"legacy/P={bypass.legacy_ratio:.6e}, "
                f"corrected/P={bypass.corrected_ratio:.6e}"
            ),
        )
    )
    checks.append(
        report_control(
            "independent eight-mask recomputation agrees",
            probability_mismatch <= CONTROL_ABS_TOL * scale
            and abs(independent_legacy - bypass.legacy_i3) <= CONTROL_ABS_TOL * scale
            and abs(independent_corrected - bypass.corrected_i3)
            <= CONTROL_ABS_TOL * scale,
            f"max probability mismatch={probability_mismatch:.3e}",
        )
    )

    no_bypass_args = deterministic_control_graph(bypass=False)
    no_bypass = sorkin_born(*no_bypass_args)
    checks.append(
        report_control(
            "explicit no-bypass graph makes seven and eight terms agree",
            no_bypass.p_empty == 0.0
            and abs(no_bypass.legacy_i3 - no_bypass.corrected_i3)
            <= CONTROL_ABS_TOL * max(1.0, no_bypass.p_abc),
            (
                f"P0={no_bypass.p_empty:.3e}, "
                f"legacy/P={no_bypass.legacy_ratio:.3e}, "
                f"corrected/P={no_bypass.corrected_ratio:.3e}"
            ),
        )
    )

    wrong_sign_i3 = bypass.legacy_i3 + bypass.p_empty
    wrong_sign_ratio = abs(wrong_sign_i3) / bypass.p_abc
    checks.append(
        report_control(
            "wrong-sign empty-term mutant is rejected",
            wrong_sign_ratio > 1e-6,
            f"mutant |I3|/P={wrong_sign_ratio:.6e}",
        )
    )

    corrected_coeffs = coefficient_table(include_empty=True, empty_sign=-1)
    legacy_coeffs = coefficient_table(include_empty=False)
    mutant_coeffs = coefficient_table(include_empty=True, empty_sign=1)
    legacy_nonzero = {
        monomial: value for monomial, value in legacy_coeffs.items() if value
    }
    mutant_nonzero = {
        monomial: value for monomial, value in mutant_coeffs.items() if value
    }
    checks.append(
        report_control(
            "analytic linear-amplitude inclusion coefficients cancel exactly",
            all(value == 0 for value in corrected_coeffs.values())
            and legacy_nonzero == {("D", "D"): 1}
            and mutant_nonzero == {("D", "D"): 2},
            (
                f"corrected_nonzero=0, legacy_nonzero={legacy_nonzero}, "
                f"mutant_nonzero={mutant_nonzero}"
            ),
        )
    )

    print()
    return all(checks)


def main() -> int:
    controls_ok = run_hostile_controls()

    print("=" * 116)
    print("STRUCTURED MIRROR CORRECTED EIGHT-TERM SLICED RUNNER")
    print("Source note: docs/STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md")
    print(f"Corrected numerical threshold: |I3|/P <= {BORN_SAFETY_THRESHOLD:.0e}")
    print(f"Seeds per configuration: {len(SEEDS)}; slice size: {len(SLICED_CONFIGS)}")
    print("Geometry: original structured mirror, including two-layer-back bypass edges")
    print("=" * 116)
    print()
    print(
        f"  {'config':<42s} {'I3/P mean':>11s} {'I3/P max':>11s} "
        f"{'legacy':>10s} {'P0/P':>10s} {'d_TV':>7s} {'pur_cl':>7s} "
        f"{'gravity':>9s} {'ok':>3s}"
    )
    print("  " + "-" * 112)

    rows = []
    all_valid = True
    for config in SLICED_CONFIGS:
        result = six_seed_measurements(config)
        rows.append((config, result))
        if result["ok"] != len(SEEDS):
            all_valid = False
            print(
                f"  {fmt_config(config):<42s} {'INVALID':>11s} {'INVALID':>11s} "
                f"{'INVALID':>10s} {'INVALID':>10s} {'-':>7s} {'-':>7s} "
                f"{'-':>9s} {result['ok']:3d}"
            )
            for error in result["errors"]:
                print(f"      {error}")
            continue
        print(
            f"  {fmt_config(config):<42s} "
            f"{result['born_corrected_mean']:11.3e} "
            f"{result['born_corrected_max']:11.3e} "
            f"{result['born_legacy_mean']:10.3e} "
            f"{result['p_empty_ratio_mean']:10.3e} "
            f"{result['dtv_mean']:7.4f} "
            f"{result['pur_cl_mean']:7.4f} "
            f"{result['gravity_mean']:+9.4f} "
            f"{result['ok']:3d}"
        )

    print()
    if not all_valid:
        print("FAIL: at least one registered configuration did not produce ok=6.")
        return 1

    max_corrected = max(
        (
            sample["born_corrected"],
            config,
            sample["seed"],
        )
        for config, result in rows
        for sample in result["samples"]
    )
    max_legacy_empty_mismatch = max(
        result["legacy_empty_mismatch_max"] for _, result in rows
    )
    diagnostic_ranges = {}
    for key in ("dtv", "pur_cl", "s_norm", "gravity", "grav_k0"):
        values = [
            sample[key]
            for _, result in rows
            for sample in result["samples"]
        ]
        diagnostic_ranges[key] = (min(values), max(values))
    joint_rows = [
        config
        for config, result in rows
        if result["pur_cl_mean"] < 0.95 and result["gravity_mean"] > 0.0
    ]

    print("AGGREGATE")
    print(f"  valid executions: {len(SLICED_CONFIGS) * len(SEEDS)}/192")
    print(
        f"  maximum corrected |I3|/P: {max_corrected[0]:.6e} "
        f"at {fmt_config(max_corrected[1])}, seed={max_corrected[2]}"
    )
    print(
        "  maximum |legacy/P - P(empty)/P|: "
        f"{max_legacy_empty_mismatch:.6e}"
    )
    for key, (minimum, maximum) in diagnostic_ranges.items():
        print(f"  {key} range over 192 executions: [{minimum:+.6e}, {maximum:+.6e}]")
    print(
        "  configurations meeting the scan's finite ancillary screen "
        f"(mean pur_cl<0.95 and mean gravity>0): {len(joint_rows)}/32"
    )
    print()

    if not controls_ok:
        print("FAIL: one or more hostile controls failed.")
        return 1
    if max_corrected[0] > BORN_SAFETY_THRESHOLD:
        print("FAIL: corrected numerical residual exceeds the declared threshold.")
        return 1
    if max_legacy_empty_mismatch > BORN_SAFETY_THRESHOLD:
        print("FAIL: legacy residual does not track the bypass background.")
        return 1

    print("PASS: all 32 configurations produced ok=6 and the corrected eight-term")
    print("      residual stayed below the explicit 1e-14 numerical threshold.")
    print("      The nonzero legacy residual is the measured P(empty) bypass term.")
    print("      Exact cancellation is conditional on the separately checked")
    print("      fixed-graph linear-amplitude/quadratic-probability identity; floating-")
    print("      point cancellation alone is not presented as an exact proof.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
