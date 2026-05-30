#!/usr/bin/env python3
"""Corrected boundary packet for source-resolved transverse Green runner."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import source_resolved_transverse_propagating_green as transg  # noqa: E402


def main() -> int:
    lat = transg.m.Lattice3D.build(transg.NL_PHYS, transg.PW, transg.H)
    source_nodes = transg._source_cluster_nodes(lat)
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    free = lat.propagate(zero_field, transg.m.K)
    z_free = transg.m._centroid_z(free, lat)

    zero_same = transg._same_site_memory_field(lat, 0.0, source_nodes)
    zero_trans = transg._transverse_propagating_field(lat, 0.0, source_nodes)
    same_zero = transg.m._centroid_z(lat.propagate(zero_same, transg.m.K), lat) - z_free
    trans_zero = transg.m._centroid_z(lat.propagate(zero_trans, transg.m.K), lat) - z_free

    rows = []
    print("=" * 100)
    print("SOURCE-RESOLVED TRANSVERSE GREEN CORRECTED BOUNDARY PACKET")
    print("  true same-site comparison; stale positive transverse correction blocked")
    print("=" * 100)
    print(f"zero-source same-site shift:   {same_zero:+.6e}")
    print(f"zero-source transverse shift:  {trans_zero:+.6e}")
    print()
    print(
        f"{'s':>8s} {'inst':>12s} {'same':>12s} {'trans':>12s} "
        f"{'trans/inst':>11s} {'trans/same':>11s} {'trans-same':>12s} "
        f"{'d_support':>10s} {'d_Neff':>10s}"
    )
    print("-" * 100)

    inst_vals = []
    same_vals = []
    trans_vals = []
    trans_over_inst = []
    trans_over_same = []
    support_deltas = []
    eff_deltas = []
    for strength in transg.SOURCE_STRENGTHS:
        row = transg._run_case(lat, strength, source_nodes, z_free)
        inst = row["inst"]
        same = row["same"]
        trans = row["trans"]
        ratio_inst = trans / inst if abs(inst) > 1e-30 else 0.0
        ratio_same = trans / same if abs(same) > 1e-30 else 0.0
        d_support = row["trans_support"] - row["same_support"]
        d_eff = row["trans_eff"] - row["same_eff"]

        inst_vals.append(inst)
        same_vals.append(same)
        trans_vals.append(trans)
        trans_over_inst.append(ratio_inst)
        trans_over_same.append(ratio_same)
        support_deltas.append(d_support)
        eff_deltas.append(d_eff)
        rows.append((strength, inst, same, trans, ratio_inst, ratio_same, trans - same, d_support, d_eff))
        print(
            f"{strength:8.4f} {inst:+12.6e} {same:+12.6e} {trans:+12.6e} "
            f"{ratio_inst:11.3f} {ratio_same:11.3f} {trans - same:+12.6e} "
            f"{d_support:+10.3e} {d_eff:+10.3e}"
        )

    inst_alpha = transg._fit_power(transg.SOURCE_STRENGTHS, inst_vals)
    same_alpha = transg._fit_power(transg.SOURCE_STRENGTHS, same_vals)
    trans_alpha = transg._fit_power(transg.SOURCE_STRENGTHS, trans_vals)
    toward = sum(1 for value in trans_vals if value > 0.0)
    mean_trans_inst = sum(trans_over_inst) / len(trans_over_inst)
    mean_trans_same = sum(trans_over_same) / len(trans_over_same)
    mean_trans_minus_same = sum(row[6] for row in rows) / len(rows)
    mean_support_delta = sum(support_deltas) / len(support_deltas)
    mean_eff_delta = sum(eff_deltas) / len(eff_deltas)

    assertions_ok = (
        abs(same_zero) < 1e-14
        and abs(trans_zero) < 1e-14
        and toward == len(trans_vals)
        and all(row[6] < 0.0 for row in rows)
        and 1.15 < mean_trans_inst < 1.18
        and 0.989 < mean_trans_same < 0.992
        and abs(mean_support_delta) < 1e-12
        and mean_eff_delta > 0.0
        and inst_alpha is not None
        and same_alpha is not None
        and trans_alpha is not None
        and abs(inst_alpha - 1.0) < 0.01
        and abs(same_alpha - 1.0) < 0.01
        and abs(trans_alpha - 1.0) < 0.01
    )

    print()
    print("SAFE READ")
    print(f"  mean trans/inst ratio: {mean_trans_inst:.3f}")
    print(f"  corrected mean trans/same ratio: {mean_trans_same:.3f}")
    print(f"  mean trans-same centroid shift: {mean_trans_minus_same:+.3e}")
    print(f"  mean support-fraction delta: {mean_support_delta:+.3e}")
    print(f"  mean N_eff delta: {mean_eff_delta:+.3e}")
    print(f"  exponents inst/same/trans: {inst_alpha:.2f}/{same_alpha:.2f}/{trans_alpha:.2f}")
    print(f"  TOWARD rows: {toward}/{len(trans_vals)}")
    print("  boundary: transverse smoothing is not a positive same-site centroid correction")
    print("  old printed trans/same column is trans/inst and is not used as same-site evidence")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] corrected transverse Green boundary")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
