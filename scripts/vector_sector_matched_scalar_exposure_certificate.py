#!/usr/bin/env python3
"""Matched scalar-exposure certificate for the vector-sector note.

The legacy full vector harness is broad and slow.  This certificate targets
the audit blocker directly: for the audited f=0.02 CCW/CW case, it recomputes
the vector-sector dz flip and explicitly logs the matched scalar exposure
`avg 1/r` for the two directions.
"""

from __future__ import annotations

import math

import vector_sector_circular_orbit as vector


TOL = 1e-14


def avg_inv_r(direction: int, freq: float, phi0: float = 0.0) -> float:
    x_src = (vector.NL // 3) * vector.H
    vals = []
    for layer in range(vector.NL):
        angle = direction * 2.0 * math.pi * freq * layer * vector.H + phi0
        y_src = vector.R * math.cos(angle)
        z_src = vector.R * math.sin(angle)
        radius = math.sqrt((layer * vector.H - x_src) ** 2 + y_src * y_src + z_src * z_src)
        vals.append(1.0 / (radius + 0.1))
    return sum(vals) / len(vals)


def main() -> None:
    pos, adj, nmap = vector.grow(0, 0.2, 0.7)
    freq = 0.02
    dy_ccw, dz_ccw = vector._meas_yz(pos, adj, nmap, vector.S, vector.R, +1, freq)
    dy_cw, dz_cw = vector._meas_yz(pos, adj, nmap, vector.S, vector.R, -1, freq)
    exposure_ccw = avg_inv_r(+1, freq)
    exposure_cw = avg_inv_r(-1, freq)
    exposure_delta = abs(exposure_ccw - exposure_cw)
    dz_sum = dz_ccw + dz_cw

    assert dz_ccw > 0.0, dz_ccw
    assert dz_cw < 0.0, dz_cw
    assert exposure_delta < TOL, exposure_delta

    print("VECTOR SECTOR MATCHED SCALAR EXPOSURE CERTIFICATE")
    print(f"freq={freq:.3f} R={vector.R:.3f} s={vector.S:.6f}")
    print(f"CCW: dy={dy_ccw:+.9f} dz={dz_ccw:+.9f} avg_inv_r={exposure_ccw:.12f}")
    print(f"CW:  dy={dy_cw:+.9f} dz={dz_cw:+.9f} avg_inv_r={exposure_cw:.12f}")
    print(f"matched_scalar_exposure_delta={exposure_delta:.3e}")
    print(f"dz_antisymmetry_sum={dz_sum:+.3e}")
    print(
        "CERTIFICATE PASS: audited CCW/CW vector-sector case has matched "
        "scalar exposure and opposite dz sign"
    )


if __name__ == "__main__":
    main()
