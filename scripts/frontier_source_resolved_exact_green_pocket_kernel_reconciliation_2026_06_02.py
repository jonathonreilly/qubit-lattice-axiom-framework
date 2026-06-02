#!/usr/bin/env python3
"""Companion verifier: kernel-convention reconciliation for the
source-resolved exact Green pocket.

Repair target (auditor 2026-05-30, codex-cli-gpt-5.5):
  runner_artifact_issue: Reconcile the Green-kernel definition across the
  note, runner print string, and code (distance r versus softened rho+eps),
  refresh the frozen gain/output if the convention changes.

Does NOT modify the parent runner / note / cache. Verifies:
  A. Lemma R numerical identity: K_impl(rho) == exp(-mu eps) K_doc(rho).
  B. Calibration gains satisfy gain_doc = exp(-mu eps) gain_impl, and
     gain_impl matches the parent's frozen 2.131774e+00.
  C. Recomputes the pocket under both conventions and confirms doc-vs-impl
     agreement to machine precision; doc-vs-frozen-cache to printed
     precision (parent cache stored to 6 dp).
  D. Asserts parent's five hard-bar thresholds under the as-documented
     convention (zero reduction, TOWARD 4/4, F~M in [0.95,1.05], ratio in
     [1.10,1.40], gain finite). Exit non-zero on any FAIL.
"""

from __future__ import annotations

import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import scripts.minimal_source_driven_field_probe as m  # noqa: E402


# Parent runner's frozen parameters (literal copy, not modified)
H = 0.5
NL_PHYS = 20
PW = 3
SOURCE_CLUSTER = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
FIELD_TARGET_MAX = 0.02
GREEN_EPS = 0.5
GREEN_MU = 0.08

# Parent's frozen cache values (for printed-precision comparison)
PARENT_GAIN_FROZEN = 2.131774e+00
PARENT_GREEN_VALS = [+2.139974e-03, +4.279368e-03, +8.557987e-03, +1.712572e-02]
PARENT_INST_VALS = [+1.713544e-03, +3.440703e-03, +6.936763e-03, +1.410179e-02]
PARENT_TOWARD_EXPECTED = 4

# Bar tolerances
ALGEBRAIC_TOL = 1e-15
GAIN_RATIO_TOL = 1e-12
BIT_FOR_BIT_TOL = 1e-12         # doc-vs-impl: machine precision
FROZEN_CACHE_TOL = 1e-8         # parent cache stored to 6 dp -> ~5e-9 floor
ZERO_DELTA_TOL = 1e-12
GAIN_FROZEN_TOL = 5e-7          # parent's gain printed as 2.131774e+00


def _source_cluster_nodes(lat):
    gl = lat.nl // 3
    src_y = lat.hw
    src_z = lat.hw + round(m.SOURCE_Z / lat.h)
    nodes = []
    for dy, dz in SOURCE_CLUSTER:
        y, z = src_y + dy, src_z + dz
        if 0 <= y < lat.nw and 0 <= z < lat.nw:
            nodes.append(lat.nmap[(gl, y - lat.hw, z - lat.hw)])
    return nodes


def kernel_impl(rho):
    """As-implemented in parent runner: r := rho + eps in both places."""
    r = rho + GREEN_EPS
    return math.exp(-GREEN_MU * r) / r


def kernel_doc(rho):
    """As-documented in parent note / runner banner / cache."""
    return math.exp(-GREEN_MU * rho) / (rho + GREEN_EPS)


def build_field(lat, kernel_fn, s, source_nodes):
    if not source_nodes:
        return [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    source_pos = [lat.pos[i] for i in source_nodes]
    field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    for layer in range(lat.nl):
        ls = lat.layer_start[layer]
        for i in range(lat.npl):
            x, y, z = lat.pos[ls + i]
            val = 0.0
            for mx, my, mz in source_pos:
                rho = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2)
                val += s * kernel_fn(rho)
            field[layer][i] = val / len(source_pos)
    return field


def _field_abs_max(layers):
    return max(abs(v) for row in layers for v in row)


def _check(label, ok, n_pass, n_fail):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return (n_pass + 1, n_fail) if ok else (n_pass, n_fail + 1)


def main():
    print("=" * 84)
    print("SOURCE-RESOLVED EXACT GREEN POCKET — KERNEL RECONCILIATION COMPANION")
    print("  auditor target: runner_artifact_issue (kernel-convention mismatch)")
    print("  parent: docs/SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md (audited_conditional)")
    print("=" * 84)
    print(f"mu = {GREEN_MU}, eps = {GREEN_EPS}")
    print("K_impl(rho) := exp(-mu (rho + eps)) / (rho + eps)   [as in parent code]")
    print("K_doc(rho)  := exp(-mu rho) / (rho + eps)            [as in parent note]")
    print()

    n_pass, n_fail = 0, 0
    ratio_const = math.exp(-GREEN_MU * GREEN_EPS)

    # ---- Part A: Lemma R algebraic identity ----
    print("PART A. LEMMA R algebraic identity check")
    print(f"  exp(-mu eps) = exp({-GREEN_MU * GREEN_EPS}) = {ratio_const:.15f}")
    test_rhos = [0.0, 0.01, 0.1, 0.5, 1.0, math.sqrt(2.0), 3.0, 5.0, 10.0, 50.0, 100.0]
    max_id_diff = max(abs(kernel_impl(r) - ratio_const * kernel_doc(r)) for r in test_rhos)
    print(f"  sampled rho values: {test_rhos}")
    print(f"  max |K_impl - exp(-mu eps) K_doc| over sample: {max_id_diff:.3e}")
    n_pass, n_fail = _check(
        f"algebraic identity (max diff {max_id_diff:.3e} < {ALGEBRAIC_TOL})",
        max_id_diff < ALGEBRAIC_TOL, n_pass, n_fail,
    )
    print()

    # ---- Part B: calibration gains ----
    print("PART B. Calibration gain reconciliation")
    lat = m.Lattice3D.build(NL_PHYS, PW, H)
    source_nodes = _source_cluster_nodes(lat)
    print(f"  lattice: h={H}, W={PW}, L={NL_PHYS}; in-bounds source nodes: {len(source_nodes)}")
    s_max = max(m.SOURCE_STRENGTHS)
    ref_impl = build_field(lat, kernel_impl, s_max, source_nodes)
    ref_doc = build_field(lat, kernel_doc, s_max, source_nodes)
    max_impl = _field_abs_max(ref_impl)
    max_doc = _field_abs_max(ref_doc)
    gain_impl = FIELD_TARGET_MAX / max_impl if max_impl > 1e-30 else 1.0
    gain_doc = FIELD_TARGET_MAX / max_doc if max_doc > 1e-30 else 1.0
    print(f"  max|f_ref(K_impl)| = {max_impl:.6e}   gain_impl = {gain_impl:.6e}")
    print(f"  max|f_ref(K_doc) | = {max_doc:.6e}   gain_doc  = {gain_doc:.6e}")
    print(f"  gain_doc / gain_impl = {gain_doc / gain_impl:.15f}")
    print(f"  exp(-mu eps)         = {ratio_const:.15f}")
    gain_ratio_diff = abs(gain_doc / gain_impl - ratio_const)
    n_pass, n_fail = _check(
        f"gain_doc/gain_impl == exp(-mu eps) (diff {gain_ratio_diff:.3e} < {GAIN_RATIO_TOL})",
        gain_ratio_diff < GAIN_RATIO_TOL, n_pass, n_fail,
    )
    gain_impl_match = abs(gain_impl - PARENT_GAIN_FROZEN)
    n_pass, n_fail = _check(
        f"gain_impl matches parent frozen gain (diff {gain_impl_match:.3e} < {GAIN_FROZEN_TOL})",
        gain_impl_match < GAIN_FROZEN_TOL, n_pass, n_fail,
    )
    print()

    # ---- Part C: re-run pocket under both conventions ----
    print("PART C. Bit-for-bit reproduction of frozen observables")
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    free = lat.propagate(zero_field, m.K)
    z_free = m._centroid_z(free, lat)
    zero_dyn_doc = build_field(lat, kernel_doc, 0.0, source_nodes)
    zero_amps_doc = lat.propagate([[gain_doc * v for v in row] for row in zero_dyn_doc], m.K)
    zero_delta_doc = m._centroid_z(zero_amps_doc, lat) - z_free
    print(f"  zero-source delta (doc convention): {zero_delta_doc:+.6e}")
    n_pass, n_fail = _check(
        f"zero-source reduction (doc) |delta|={abs(zero_delta_doc):.3e} <= {ZERO_DELTA_TOL}",
        abs(zero_delta_doc) <= ZERO_DELTA_TOL, n_pass, n_fail,
    )

    inst_vals, green_vals_doc, green_vals_impl, ratios = [], [], [], []
    print(f"  {'s':>8s} {'inst':>14s} {'green_doc':>14s} {'green_impl':>14s} {'diff':>10s}")
    print(f"  {'-' * 64}")
    for s in m.SOURCE_STRENGTHS:
        inst_field = m._instantaneous_field_layers(lat, s, m.SOURCE_Z)
        f_doc = [[gain_doc * v for v in row] for row in build_field(lat, kernel_doc, s, source_nodes)]
        f_impl = [[gain_impl * v for v in row] for row in build_field(lat, kernel_impl, s, source_nodes)]
        delta_inst = m._centroid_z(lat.propagate(inst_field, m.K), lat) - z_free
        delta_doc = m._centroid_z(lat.propagate(f_doc, m.K), lat) - z_free
        delta_impl = m._centroid_z(lat.propagate(f_impl, m.K), lat) - z_free
        inst_vals.append(delta_inst)
        green_vals_doc.append(delta_doc)
        green_vals_impl.append(delta_impl)
        ratios.append(abs(delta_doc / delta_inst) if abs(delta_inst) > 1e-30 else float("nan"))
        diff = abs(delta_doc - delta_impl)
        print(f"  {s:8.4f} {delta_inst:+14.6e} {delta_doc:+14.6e} {delta_impl:+14.6e} {diff:10.2e}")

    max_doc_impl_diff = max(abs(d - i) for d, i in zip(green_vals_doc, green_vals_impl))
    n_pass, n_fail = _check(
        f"doc vs impl deflection agreement max diff {max_doc_impl_diff:.3e} <= {BIT_FOR_BIT_TOL}",
        max_doc_impl_diff <= BIT_FOR_BIT_TOL, n_pass, n_fail,
    )
    max_green_diff = max(abs(d - p) for d, p in zip(green_vals_doc, PARENT_GREEN_VALS))
    n_pass, n_fail = _check(
        f"doc green deflections match parent cache to printed precision (max diff {max_green_diff:.3e})",
        max_green_diff <= FROZEN_CACHE_TOL, n_pass, n_fail,
    )
    max_inst_diff = max(abs(d - p) for d, p in zip(inst_vals, PARENT_INST_VALS))
    n_pass, n_fail = _check(
        f"instantaneous comparator unchanged to printed precision (max diff {max_inst_diff:.3e})",
        max_inst_diff <= FROZEN_CACHE_TOL, n_pass, n_fail,
    )
    print()

    # ---- Part D: parent hard-bar set under as-documented kernel ----
    print("PART D. Parent hard-bar set under as-documented kernel")
    toward = sum(1 for v in green_vals_doc if v > 0)
    inst_alpha = m._fit_power(list(m.SOURCE_STRENGTHS), inst_vals)
    green_alpha = m._fit_power(list(m.SOURCE_STRENGTHS), green_vals_doc)
    mean_ratio = sum(ratios) / len(ratios)
    print(f"  TOWARD rows: {toward}/{len(green_vals_doc)}")
    print(f"  instantaneous F~M exponent: {inst_alpha:.3f}" if inst_alpha is not None else "  inst F~M: n/a")
    print(f"  green-kernel  F~M exponent: {green_alpha:.3f}" if green_alpha is not None else "  green F~M: n/a")
    print(f"  mean |green/inst| ratio: {mean_ratio:.3f}")
    n_pass, n_fail = _check(
        f"TOWARD sign {toward}/{len(green_vals_doc)}",
        toward == PARENT_TOWARD_EXPECTED, n_pass, n_fail,
    )
    ga_ok = green_alpha is not None and 0.95 <= green_alpha <= 1.05
    n_pass, n_fail = _check(
        f"green F~M exponent {green_alpha:.3f} in [0.95, 1.05]" if green_alpha is not None
        else "green F~M exponent unavailable",
        ga_ok, n_pass, n_fail,
    )
    n_pass, n_fail = _check(
        f"mean |green/inst| ratio {mean_ratio:.3f} in [1.10, 1.40]",
        1.10 <= mean_ratio <= 1.40, n_pass, n_fail,
    )
    n_pass, n_fail = _check(
        f"gain_doc {gain_doc:.6e} in (0, 100)",
        0.0 < gain_doc < 100.0, n_pass, n_fail,
    )
    print()
    print("=" * 84)
    print(f"TOTAL: PASS={n_pass}, FAIL={n_fail}")
    print("=" * 84)
    return 1 if n_fail > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
