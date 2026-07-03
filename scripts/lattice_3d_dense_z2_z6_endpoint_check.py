#!/usr/bin/env python3
"""Dedicated z=2..6 endpoint check for the dense spent-delay lattice card."""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.lattice_3d_dense_10prop as dense


def main() -> int:
    phys_l = 12
    h = 1.0
    pos, adj, nl, hw, nmap = dense.generate(phys_l, h)
    n = len(pos)
    det = [
        nmap[(nl - 1, iy, iz)]
        for iy in range(-hw, hw + 1)
        for iz in range(-hw, hw + 1)
    ]
    gl = 2 * nl // 3
    _bi, _sa, _sb, blocked, _bl = dense.setup_slits(pos, nmap, nl, hw)

    field_flat = [0.0] * n
    amps_flat = dense.propagate(pos, adj, field_flat, dense.K, blocked, n)
    _pf, probs_flat = dense.detector_probs(amps_flat, det)
    z_flat = dense.detector_centroid(probs_flat, det, pos)

    rows = []
    print("=" * 92)
    print("3D DENSE SPENT-DELAY z=2..6 ENDPOINT CHECK")
    print("  dedicated finite endpoint runner over the existing dense 10-property harness")
    print("=" * 92)
    print(
        f"{'z':>2s} {'centroid':>12s} {'P_near':>12s} {'bias':>12s} {'sign':>12s}"
    )
    print("-" * 92)

    for z_mass in [2, 3, 4, 5, 6]:
        field_m, source_index = dense.make_field(pos, nmap, gl, z_mass, n)
        if source_index is None:
            raise AssertionError(f"source node missing for z={z_mass}")
        amps_mass = dense.propagate(pos, adj, field_m, dense.K, blocked, n)
        pm, probs_mass = dense.detector_probs(amps_mass, det)
        if pm <= 1e-30:
            raise AssertionError(f"detector probability vanished for z={z_mass}")
        z_mass_centroid = dense.detector_centroid(probs_mass, det, pos)
        delta_centroid = z_mass_centroid - z_flat
        delta_pnear = dense.near_mass_window_gain(
            probs_mass, probs_flat, det, pos, z_mass, half_width=1.0
        )
        delta_bias = dense.mass_side_channel_bias(
            probs_mass, probs_flat, det, pos, z_mass, z_flat
        )
        sign = dense.classify_sign(delta_centroid, delta_pnear, delta_bias)
        rows.append((z_mass, delta_centroid, delta_pnear, delta_bias, sign))
        print(
            f"{z_mass:2d} {delta_centroid:+12.6e} {delta_pnear:+12.6e} "
            f"{delta_bias:+12.6e} {sign:>12s}"
        )

    attractive = [row for row in rows if row[-1] == "ATTRACTIVE"]
    z6 = rows[-1]
    centroids = [row[1] for row in rows]
    lx = [math.log(row[0]) for row in rows]
    ly = [math.log(row[1]) for row in rows]
    mean_x = sum(lx) / len(lx)
    mean_y = sum(ly) / len(ly)
    sxx = sum((x - mean_x) ** 2 for x in lx)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(lx, ly))
    slope = sxy / sxx if sxx > 1e-12 else math.nan
    ss_res = sum((y - (mean_y + slope * (x - mean_x))) ** 2 for x, y in zip(lx, ly))
    ss_tot = sum((y - mean_y) ** 2 for y in ly)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else math.nan

    assertions_ok = (
        len(attractive) == 5
        and z6[0] == 6
        and z6[1] > 0.0
        and z6[2] > 0.0
        and z6[3] > 0.0
        and all(value > 0.0 for value in centroids)
    )

    print()
    print("SAFE READ")
    print(f"  hierarchy-aligned support: {len(attractive)}/5 points")
    print(f"  centroid law over z=2..6: b^({slope:.2f}), R^2={r2:.3f}")
    print("  z=6 endpoint is positive but small; no asymptotic theorem is claimed")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] z=2..6 finite endpoint assertion surface")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
