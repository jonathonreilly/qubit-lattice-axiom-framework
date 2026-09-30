#!/usr/bin/env python3
"""Comparator check for R = Omega_DM / Omega_b in the DM lane notes.

Evidence for the 2026-09-30 corrigendum on the comparator.

The April to June DM notes compare the lane ratio R = Omega_DM/Omega_b with
5.469 (rounded 0.268 / 0.049), 5.47, 5.375 (0.265 / 0.0493), 5.38 or 5.448
(0.268 over the BBN Omega_b for eta = 6.12e-10).  The physical density ratio
is fixed by the two Planck-2018 physical densities, which cancel h:

    R_obs = (Omega_c h^2) / (Omega_b h^2).

External comparator (not derived here; recalled from Planck 2018 results VI,
Table 2, TT,TE,EE+lowE+lensing, and not re-fetched in this session):

    Omega_c h^2 = 0.1200 +/- 0.0012,   Omega_b h^2 = 0.02237 +/- 0.00015.

The sigma below propagates the two errors as independent.  The Planck posterior
correlation between the two densities is not applied; it changes sigma_R at
the ten-percent level and does not change any sign or ordering printed here.

This is a same-family check by its author, not an independent referee.
"""

from __future__ import annotations

import math
import sys

from dm_full_closure_same_surface_thermal_support_common import (
    ALPHA_HI,
    ALPHA_LO,
    converged_same_surface_ratio,
)

PASS_COUNT = 0
FAIL_COUNT = 0

OMEGA_C_H2 = 0.1200
SIGMA_C = 0.0012
OMEGA_B_H2 = 0.02237
SIGMA_B = 0.00015

# Endpoint ratios quoted by the archived half-argument notes.
ARCHIVED_R_LO = 5.442019867867
ARCHIVED_R_HI = 5.482855571890


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def main() -> int:
    print("=" * 88)
    print("DM LANE COMPARATOR: R = Omega_DM/Omega_b AGAINST PLANCK-2018 CENTRAL VALUES")
    print("=" * 88)
    print("Same-family check by its author; the Planck numbers are external comparators.")

    r_obs = OMEGA_C_H2 / OMEGA_B_H2
    sigma = r_obs * math.hypot(SIGMA_C / OMEGA_C_H2, SIGMA_B / OMEGA_B_H2)

    print("\n" + "=" * 88)
    print("PART 1: THE OBSERVED RATIO")
    print("=" * 88)
    check("R_obs = 0.1200 / 0.02237 = 5.3643", abs(r_obs - 5.3643) < 5.0e-4, f"R_obs={r_obs:.4f}")
    check(
        "Independent-error propagation gives sigma_R = 0.065",
        abs(sigma - 0.0646) < 5.0e-4,
        f"sigma_R={sigma:.4f}",
    )

    print("\n" + "=" * 88)
    print("PART 2: WHAT THE ROUNDED COMPARATORS DID")
    print("=" * 88)
    rounded = 0.268 / 0.049
    check(
        "The rounded comparator 0.268/0.049 = 5.469 sits above the Planck-central ratio",
        rounded > r_obs,
        f"5.469 is {100.0 * (rounded / r_obs - 1.0):+.2f}% ({(rounded - r_obs) / sigma:+.1f} sigma) from 5.3643",
    )
    lo_rounded = 0.2675 / 0.0495
    hi_rounded = 0.2685 / 0.0485
    check(
        "Three-digit rounding alone moves the comparator over [5.40, 5.54], wider than sigma_R",
        hi_rounded - lo_rounded > 2.0 * sigma,
        f"0.2675/0.0495 = {lo_rounded:.3f}, 0.2685/0.0485 = {hi_rounded:.3f}",
    )

    for label, val in (
        ("archived R(alpha_lo)", ARCHIVED_R_LO),
        ("archived R(alpha_hi)", ARCHIVED_R_HI),
        ("note headline R = 5.48", 5.48),
    ):
        vs_round = 100.0 * (val / rounded - 1.0)
        vs_obs = 100.0 * (val / r_obs - 1.0)
        print(
            f"  {label:24s} {val:.4f}: {vs_round:+.2f}% from 5.469, "
            f"{vs_obs:+.2f}% ({(val - r_obs) / sigma:+.1f} sigma) from Planck central"
        )
    check(
        "The archived endpoint ratios are +1.2 and +1.8 sigma from the Planck-central ratio (not 0.2-0.5% hits)",
        1.1 < (ARCHIVED_R_LO - r_obs) / sigma < 1.3 and 1.7 < (ARCHIVED_R_HI - r_obs) / sigma < 1.9,
        f"{(ARCHIVED_R_LO - r_obs) / sigma:+.2f} sigma, {(ARCHIVED_R_HI - r_obs) / sigma:+.2f} sigma",
    )
    check(
        "R = 5.48 sits 0.2% above 5.469 but 2.1% above the Planck-central ratio",
        abs(100.0 * (5.48 / rounded - 1.0) - 0.2) < 0.1 and abs(100.0 * (5.48 / r_obs - 1.0) - 2.1) < 0.1,
        f"{100.0 * (5.48 / rounded - 1.0):+.2f}% vs {100.0 * (5.48 / r_obs - 1.0):+.2f}%",
    )

    print("\n" + "=" * 88)
    print("PART 3: THE REPAIRED LANE ENDPOINT RATIOS (2 pi Sommerfeld argument)")
    print("=" * 88)
    r_lo = converged_same_surface_ratio(ALPHA_LO)
    r_hi = converged_same_surface_ratio(ALPHA_HI)
    print(f"  R(alpha_lo) = {r_lo:.6f}: {100.0 * (r_lo / r_obs - 1.0):+.1f}% ({(r_lo - r_obs) / sigma:+.0f} sigma) from Planck central")
    print(f"  R(alpha_hi) = {r_hi:.6f}: {100.0 * (r_hi / r_obs - 1.0):+.1f}% ({(r_hi - r_obs) / sigma:+.0f} sigma) from Planck central")
    check(
        "With the corrected Sommerfeld argument both endpoint ratios exceed the Planck-central ratio by more than 30 percent",
        r_lo / r_obs > 1.3 and r_hi / r_obs > 1.3,
        f"{100.0 * (r_lo / r_obs - 1.0):+.1f}%, {100.0 * (r_hi / r_obs - 1.0):+.1f}%",
    )

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  Against the Planck-2018 central ratio 5.364 +/- 0.065 the archived endpoint ratios")
    print("  5.442 and 5.483 were +1.2 and +1.8 sigma misses, not 0.2-0.5% hits; the smaller")
    print("  offsets came from the rounded comparator 5.469.  With the corrected Sommerfeld")
    print("  argument the endpoint ratios are about 8 and the comparison is moot.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
