#!/usr/bin/env python3
"""Live finite Poisson self-gravity threshold check.

This is a narrow audit companion for the archived stale BACKREACTION_NOTE row.
It does not resurrect the old G_crit ~= 0.011 claim.  It replays the current
`scripts/backreaction_poisson.py` harness on an explicit G grid that includes
the old disputed endpoint region and asserts only the finite live facts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.backreaction_poisson as bp  # noqa: E402


G_GRID = (0.0, 0.001, 0.005, 0.010, 0.011, 0.012, 0.020, 0.050, 0.100)
N_ITERS = 15


@dataclass(frozen=True)
class Row:
    G: float
    iters: int
    delta: float
    escape: float
    f_self_max: float
    converged: bool


def _run_grid() -> tuple[float, list[Row]]:
    nl, hw, nw, npl, offsets, T, pos = bp._build()
    zero_field = np.zeros((nl, npl))
    external_field = bp._ext_field(
        nl, nw, hw, npl, pos, bp.EXT_STRENGTH, bp.MASS_Z
    )

    free = bp._propagate(nl, nw, npl, hw, offsets, T, zero_field, bp.K)
    z_free = bp._cz(free[-1], nw, hw)
    p_free = bp._dp(free[-1])

    grav = bp._propagate(nl, nw, npl, hw, offsets, T, external_field, bp.K)
    z_grav = bp._cz(grav[-1], nw, hw)
    baseline_delta = z_grav - z_free

    rows: list[Row] = []
    for G in G_GRID:
        total_field = external_field.copy()
        prev_delta = None
        converged = False
        delta = 0.0
        escape = 0.0
        iteration = 0

        for iteration in range(N_ITERS):
            amps = bp._propagate(nl, nw, npl, hw, offsets, T, total_field, bp.K)
            delta = bp._cz(amps[-1], nw, hw) - z_free
            escape = bp._dp(amps[-1]) / p_free if p_free > 0 else 0.0
            if prev_delta is not None and abs(delta - prev_delta) < 1e-8:
                converged = True
                break
            prev_delta = delta
            if G > 0.0:
                self_field = bp._self_field_from_amplitude(amps, nl, npl, pos, G)
                total_field = external_field + self_field

        rows.append(
            Row(
                G=G,
                iters=iteration + 1,
                delta=delta,
                escape=escape,
                f_self_max=float((total_field - external_field).max())
                if G > 0.0
                else 0.0,
                converged=converged,
            )
        )

    return baseline_delta, rows


def main() -> int:
    baseline_delta, rows = _run_grid()
    by_g = {row.G: row for row in rows}
    first_subunit = next((row.G for row in rows if row.escape < 1.0), None)

    print("=" * 88)
    print("POISSON SELF-GRAVITY LIVE THRESHOLD CHECK")
    print("  current backreaction_poisson harness; finite G-grid only")
    print("=" * 88)
    print(f"baseline external-field delta = {baseline_delta:+.6e} TOWARD")
    print(
        f"{'G':>7s} {'iters':>5s} {'delta':>13s} {'dir':>7s} "
        f"{'escape':>9s} {'f_self_max':>11s} {'converged':>10s}"
    )
    print("-" * 88)
    for row in rows:
        direction = "TOWARD" if row.delta > 0.0 else "AWAY"
        print(
            f"{row.G:7.3f} {row.iters:5d} {row.delta:+13.6e} {direction:>7s} "
            f"{row.escape:9.4f} {row.f_self_max:11.6f} "
            f"{str(row.converged):>10s}"
        )

    assertions_ok = (
        baseline_delta > 0.0
        and all(row.delta > 0.0 for row in rows)
        and by_g[0.011].escape > 1.0
        and by_g[0.012].escape > 1.0
        and by_g[0.020].escape > 1.0
        and by_g[0.050].escape < 1.0
        and by_g[0.100].escape < by_g[0.050].escape
        and first_subunit == 0.050
    )

    print()
    print("SAFE READ")
    print("  old G_crit ~= 0.011 table is not reproduced by the live harness")
    print(f"  first sub-unit escape on this grid: G={first_subunit}")
    print("  TOWARD deflection is preserved through G=0.100 on this grid")
    print("  finite bounded packet only: no continuum horizon or smooth threshold law")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] live finite threshold surface")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
