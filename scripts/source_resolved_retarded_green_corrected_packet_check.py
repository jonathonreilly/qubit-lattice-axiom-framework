#!/usr/bin/env python3
"""Corrected live packet for source-resolved retarded Green pocket."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import source_resolved_retarded_green_pocket as retg  # noqa: E402


def main() -> int:
    lat = retg.m.Lattice3D.build(retg.NL_PHYS, retg.PW, retg.H)
    source_nodes = retg._source_cluster_nodes(lat)
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    free = lat.propagate(zero_field, retg.m.K)
    z_free = retg.m._centroid_z(free, lat)

    zero_same = retg._same_site_memory_field(lat, 0.0, source_nodes)
    zero_ret = retg._retarded_like_field(lat, 0.0, source_nodes)
    same_zero = retg.m._centroid_z(lat.propagate(zero_same, retg.m.K), lat) - z_free
    ret_zero = retg.m._centroid_z(lat.propagate(zero_ret, retg.m.K), lat) - z_free

    rows = []
    print("=" * 96)
    print("SOURCE-RESOLVED RETARDED GREEN CORRECTED PACKET")
    print("  corrected same-site comparison; finite-lag pocket only")
    print("=" * 96)
    print(f"zero-source same-site shift: {same_zero:+.6e}")
    print(f"zero-source retarded shift:  {ret_zero:+.6e}")
    print()
    print(
        f"{'s':>8s} {'inst':>12s} {'same':>12s} {'ret':>12s} "
        f"{'ret/inst':>10s} {'ret/same':>10s} {'ret-same':>12s}"
    )
    print("-" * 96)

    inst_vals = []
    same_vals = []
    ret_vals = []
    support_deltas = []
    eff_deltas = []
    corrected_ratios = []
    for strength in retg.SOURCE_STRENGTHS:
        row = retg._run_case(lat, strength, source_nodes, z_free)
        inst = row["inst"]
        same = row["same"]
        ret = row["ret"]
        ret_over_inst = abs(ret / inst) if abs(inst) > 1e-30 else 0.0
        ret_over_same = ret / same if abs(same) > 1e-30 else 0.0
        corrected_ratios.append(ret_over_same)
        inst_vals.append(inst)
        same_vals.append(same)
        ret_vals.append(ret)
        support_deltas.append(row["ret_support"] - row["same_support"])
        eff_deltas.append(row["ret_eff"] - row["same_eff"])
        rows.append((strength, inst, same, ret, ret_over_inst, ret_over_same, ret - same))
        print(
            f"{strength:8.4f} {inst:+12.6e} {same:+12.6e} {ret:+12.6e} "
            f"{ret_over_inst:10.3f} {ret_over_same:10.3f} {ret - same:+12.6e}"
        )

    inst_alpha = retg._fit_power(retg.SOURCE_STRENGTHS, inst_vals)
    same_alpha = retg._fit_power(retg.SOURCE_STRENGTHS, same_vals)
    ret_alpha = retg._fit_power(retg.SOURCE_STRENGTHS, ret_vals)
    toward = sum(1 for value in ret_vals if value > 0.0)
    mean_support_delta = sum(support_deltas) / len(support_deltas)
    mean_eff_delta = sum(eff_deltas) / len(eff_deltas)
    mean_corrected_ratio = sum(corrected_ratios) / len(corrected_ratios)

    assertions_ok = (
        abs(same_zero) < 1e-14
        and abs(ret_zero) < 1e-14
        and toward == len(ret_vals)
        and all(row[-1] > 0.0 for row in rows)
        and 1.02 < mean_corrected_ratio < 1.04
        and abs(mean_support_delta) < 1e-12
        and mean_eff_delta > 0.0
        and inst_alpha is not None
        and same_alpha is not None
        and ret_alpha is not None
        and abs(inst_alpha - 1.0) < 0.01
        and abs(same_alpha - 1.0) < 0.01
        and abs(ret_alpha - 1.0) < 0.01
    )

    print()
    print("SAFE READ")
    print(f"  corrected mean ret/same ratio: {mean_corrected_ratio:.3f}")
    print(f"  mean ret-same support delta: {mean_support_delta:+.3e}")
    print(f"  mean ret-same N_eff delta: {mean_eff_delta:+.3e}")
    print(f"  exponents inst/same/ret: {inst_alpha:.2f}/{same_alpha:.2f}/{ret_alpha:.2f}")
    print(f"  TOWARD rows: {toward}/{len(ret_vals)}")
    print("  bounded live packet only: no full retarded field equation")
    print("  old printed ret/same column is ret/inst and is not used")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] corrected retarded Green packet")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
