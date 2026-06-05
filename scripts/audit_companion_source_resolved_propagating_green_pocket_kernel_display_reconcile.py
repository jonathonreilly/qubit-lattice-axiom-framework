#!/usr/bin/env python3
"""Kernel-display reconcile companion verifier.

Source companion runner for the
`source_resolved_propagating_green_pocket_note` kernel-display mismatch:
the parent note displays the Green-kernel family as `exp(-mu r)/(r+eps)`,
while the registered runner evaluates `exp(-mu*(d+eps))/(d+eps)`. This
verifier exhibits the pointwise constant factor relating the two
conventions, shows the runner's self-consistent
`gain = FIELD_TARGET_MAX / _field_abs_max(ref_raw)` calibration step
cancels that factor exactly, and confirms the calibrated Green and
propagating Green fields are bit-identical under the two conventions.
It then re-derives the parent's frozen-table entries from the executed
convention and asserts they match the displayed precision.

Does NOT modify the parent note. Does NOT propose any parent state change.
Introduces no new physics import.
"""

from __future__ import annotations

import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import scripts.minimal_source_driven_field_probe as m  # noqa: E402


# Parameter mirror of scripts/source_resolved_propagating_green_pocket.py.
H = 0.5
NL_PHYS = 20
PW = 3
SOURCE_CLUSTER = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
FIELD_TARGET_MAX = 0.02
GREEN_EPS = 0.5
GREEN_MU = 0.08
MEMORY_MIX = 0.9

# Frozen reference values from the parent note's "Frozen values" table.
FROZEN_MEAN_PROP_OVER_INST_RANGE = (1.41, 1.43)
FROZEN_MEAN_PROP_OVER_GREEN_RANGE = (1.148, 1.151)


def _source_cluster_nodes(lat: m.Lattice3D) -> list[int]:
    gl = lat.nl // 3
    src_y = lat.hw
    src_z = lat.hw + round(m.SOURCE_Z / lat.h)
    nodes: list[int] = []
    for dy, dz in SOURCE_CLUSTER:
        y = src_y + dy
        z = src_z + dz
        if 0 <= y < lat.nw and 0 <= z < lat.nw:
            nodes.append(lat.nmap[(gl, y - lat.hw, z - lat.hw)])
    return nodes


def _green_field(lat, s, src_nodes, *, convention):
    """Source-resolved Green field under either kernel convention."""
    if not src_nodes:
        return [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    src_pos = [lat.pos[i] for i in src_nodes]
    field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    for layer in range(lat.nl):
        ls = lat.layer_start[layer]
        for i in range(lat.npl):
            x, y, z = lat.pos[ls + i]
            val = 0.0
            for mx, my, mz in src_pos:
                d = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2)
                if convention == "executed":
                    r = d + GREEN_EPS
                    val += s * math.exp(-GREEN_MU * r) / r
                elif convention == "displayed":
                    val += s * math.exp(-GREEN_MU * d) / (d + GREEN_EPS)
                else:
                    raise ValueError(convention)
            field[layer][i] = val / len(src_pos)
    return field


def _prop_field(green, *, mix):
    nl, npl = len(green), len(green[0])
    f = [[0.0 for _ in range(npl)] for _ in range(nl)]
    for layer in range(nl):
        if layer == 0:
            f[layer] = green[layer][:]
        else:
            prev, curr = f[layer - 1], green[layer]
            f[layer] = [mix * prev[i] + (1.0 - mix) * curr[i] for i in range(npl)]
    return f


def _field_abs_max(layers):
    return max(abs(v) for row in layers for v in row)


def _scale(layers, g):
    return [[g * v for v in row] for row in layers]


def _max_abs_diff(a, b):
    return max(abs(av - bv) for ra, rb in zip(a, b) for av, bv in zip(ra, rb))


def _fit_power(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x > 0 and y > 0]
    if len(pairs) < 3:
        return None
    lx = [math.log(x) for x, _ in pairs]
    ly = [math.log(y) for _, y in pairs]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    sxx = sum((x - mx) ** 2 for x in lx)
    if sxx < 1e-12:
        return None
    sxy = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    return sxy / sxx


def main() -> int:
    lat = m.Lattice3D.build(NL_PHYS, PW, H)
    src_nodes = _source_cluster_nodes(lat)

    print("=" * 92)
    print("KERNEL-DISPLAY RECONCILE COMPANION")
    print("  parent: SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md")
    print("  source repair target: kernel display versus executed convention")
    print("=" * 92)
    print(f"h={H}, W={PW}, L={NL_PHYS}, source_cluster={len(src_nodes)} nodes, mix={MEMORY_MIX}")
    print(f"GREEN_MU={GREEN_MU}, GREEN_EPS={GREEN_EPS}, FIELD_TARGET_MAX={FIELD_TARGET_MAX}")
    print(f"source strengths: {m.SOURCE_STRENGTHS}")
    print()

    # ---- GATE 1: pointwise constant factor ----
    c_factor = math.exp(-GREEN_MU * GREEN_EPS)
    s_ref = max(m.SOURCE_STRENGTHS)
    ref_exec = _green_field(lat, s_ref, src_nodes, convention="executed")
    ref_disp = _green_field(lat, s_ref, src_nodes, convention="displayed")
    max_ratio_dev = max(
        abs(re_v / rd_v - c_factor)
        for re_row, rd_row in zip(ref_exec, ref_disp)
        for re_v, rd_v in zip(re_row, rd_row)
        if abs(rd_v) > 1e-30
    )
    gate1_ok = max_ratio_dev < 1e-13
    print("GATE 1 — pointwise constant factor")
    print(f"  predicted K_exec(d) / K_disp(d) = exp(-mu*eps) = {c_factor:.16f}")
    print(f"  max |K_exec/K_disp - c| over lattice: {max_ratio_dev:.3e}")
    print(f"  [{'PASS' if gate1_ok else 'FAIL'}] pointwise constant factor")
    print()

    # ---- GATE 2: calibrated Green field bit-identity ----
    gain_exec = FIELD_TARGET_MAX / _field_abs_max(ref_exec)
    gain_disp = FIELD_TARGET_MAX / _field_abs_max(ref_disp)
    max_cal_diff = _max_abs_diff(_scale(ref_exec, gain_exec), _scale(ref_disp, gain_disp))
    gate2_ok = max_cal_diff < 1e-14
    print("GATE 2 — calibrated Green field bit-identity")
    print(f"  gain_exec = {gain_exec:.16e}, gain_disp = {gain_disp:.16e}")
    print(f"  predicted gain_exec / gain_disp = 1/c = {1.0 / c_factor:.16f}")
    print(f"  observed gain_exec / gain_disp     = {gain_exec / gain_disp:.16f}")
    print(f"  max |cal_green_exec - cal_green_disp|: {max_cal_diff:.3e}")
    print(f"  [{'PASS' if gate2_ok else 'FAIL'}] calibrated Green field bit-identity")
    print()

    # ---- GATE 3: calibrated propagating-Green field bit-identity ----
    pe_unscaled = _prop_field(ref_exec, mix=MEMORY_MIX)
    pd_unscaled = _prop_field(ref_disp, mix=MEMORY_MIX)
    max_prop_diff = _max_abs_diff(_scale(pe_unscaled, gain_exec), _scale(pd_unscaled, gain_disp))
    gate3_ok = max_prop_diff < 1e-14
    print("GATE 3 — calibrated propagating-Green field bit-identity")
    print(f"  max |cal_prop_exec - cal_prop_disp|: {max_prop_diff:.3e}")
    print(f"  [{'PASS' if gate3_ok else 'FAIL'}] calibrated propagating-Green field bit-identity")
    print()

    # ---- GATE 4: observable invariance across kernel conventions ----
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    z_free = m._centroid_z(lat.propagate(zero_field, m.K), lat)
    print("GATE 4 — observable invariance across kernel conventions")
    print(f"{'s':>8s} {'green_e':>13s} {'green_d':>13s} {'prop_e':>13s} {'prop_d':>13s} {'|Δ|max':>10s}")
    print("-" * 80)
    max_obs_diff = 0.0
    inst_vals, green_vals_exec, prop_vals_exec = [], [], []
    inst_ratios, green_ratios = [], []
    for s in m.SOURCE_STRENGTHS:
        ge = _green_field(lat, s, src_nodes, convention="executed")
        gd = _green_field(lat, s, src_nodes, convention="displayed")
        pe = _prop_field(ge, mix=MEMORY_MIX)
        pd = _prop_field(gd, mix=MEMORY_MIX)
        inst_field = m._instantaneous_field_layers(lat, s, m.SOURCE_Z)
        inst_d = m._centroid_z(lat.propagate(inst_field, m.K), lat) - z_free
        ge_d = m._centroid_z(lat.propagate(_scale(ge, gain_exec), m.K), lat) - z_free
        gd_d = m._centroid_z(lat.propagate(_scale(gd, gain_disp), m.K), lat) - z_free
        pe_d = m._centroid_z(lat.propagate(_scale(pe, gain_exec), m.K), lat) - z_free
        pd_d = m._centroid_z(lat.propagate(_scale(pd, gain_disp), m.K), lat) - z_free
        obs_diff = max(abs(ge_d - gd_d), abs(pe_d - pd_d))
        max_obs_diff = max(max_obs_diff, obs_diff)
        inst_vals.append(inst_d)
        green_vals_exec.append(ge_d)
        prop_vals_exec.append(pe_d)
        inst_ratios.append(abs(pe_d / inst_d))
        green_ratios.append(abs(pe_d / ge_d))
        print(f"{s:8.4f} {ge_d:+13.6e} {gd_d:+13.6e} {pe_d:+13.6e} {pd_d:+13.6e} {obs_diff:10.2e}")
    gate4_ok = max_obs_diff < 1e-13
    print(f"  max |observable_exec - observable_disp| across ladder: {max_obs_diff:.3e}")
    print(f"  [{'PASS' if gate4_ok else 'FAIL'}] observable invariance")
    print()

    # ---- GATE 5: frozen-table reproduction (executed convention) ----
    mean_inst = sum(inst_ratios) / len(inst_ratios)
    mean_green = sum(green_ratios) / len(green_ratios)
    causal_mem = sum(p - g for p, g in zip(prop_vals_exec, green_vals_exec)) / len(prop_vals_exec)
    toward = sum(1 for v in prop_vals_exec if v > 0)
    inst_a = _fit_power(list(m.SOURCE_STRENGTHS), inst_vals)
    green_a = _fit_power(list(m.SOURCE_STRENGTHS), green_vals_exec)
    prop_a = _fit_power(list(m.SOURCE_STRENGTHS), prop_vals_exec)
    inst_lo, inst_hi = FROZEN_MEAN_PROP_OVER_INST_RANGE
    grn_lo, grn_hi = FROZEN_MEAN_PROP_OVER_GREEN_RANGE
    frozen_ok = (
        inst_lo < mean_inst < inst_hi
        and grn_lo < mean_green < grn_hi
        and causal_mem > 0.0
        and toward == len(prop_vals_exec)
        and inst_a is not None and abs(inst_a - 1.0) < 0.02
        and green_a is not None and abs(green_a - 1.0) < 0.01
        and prop_a is not None and abs(prop_a - 1.0) < 0.01
    )
    print("GATE 5 — frozen-table reproduction (executed convention)")
    print(f"  mean |prop/inst|  = {mean_inst:.3f}  (frozen range {inst_lo}..{inst_hi})")
    print(f"  mean |prop/green| = {mean_green:.3f}  (frozen range {grn_lo}..{grn_hi})")
    print(f"  causal memory (prop - green): {causal_mem:+.6e}  (frozen sign: positive)")
    print(f"  TOWARD rows: {toward}/{len(prop_vals_exec)}  (frozen: 4/4)")
    print(f"  inst F~M = {inst_a:.2f}, green F~M = {green_a:.2f}, prop F~M = {prop_a:.2f}")
    print(f"  [{'PASS' if frozen_ok else 'FAIL'}] frozen-table reproduction")
    print()

    all_ok = gate1_ok and gate2_ok and gate3_ok and gate4_ok and frozen_ok
    print(f"ASSERTIONS: {'PASS' if all_ok else 'FAIL'}  "
          f"(gates: 1={gate1_ok}, 2={gate2_ok}, 3={gate3_ok}, 4={gate4_ok}, 5={frozen_ok})")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
