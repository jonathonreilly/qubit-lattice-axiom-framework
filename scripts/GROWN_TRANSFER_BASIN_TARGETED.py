#!/usr/bin/env python3
"""Targeted narrow-basin replay around the prior grown-row positives.

This runner keeps the claim surface tiny:

- fixed-field signed-source transfer on nearby grown rows
- exact grown-row complex-action carryover on the same nearby rows

It is intentionally not a family-wide sweep. The goal is to test whether the
prior moderate-drift positives survive on a small neighborhood of nearby
grown rows.
"""

from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.GROWN_TRANSFER_BASIN_SWEEP import _score_row
from scripts.GROWN_TRANSFER_BASIN_SWEEP import BETA
from scripts.GROWN_TRANSFER_BASIN_SWEEP import H
from scripts.GROWN_TRANSFER_BASIN_SWEEP import K
from scripts.GROWN_TRANSFER_BASIN_SWEEP import MAX_D_PHYS
from scripts.GROWN_TRANSFER_BASIN_SWEEP import NL
from scripts.GROWN_TRANSFER_BASIN_SWEEP import PW
from scripts.GROWN_TRANSFER_BASIN_SWEEP import complex_action_survives
from scripts.GROWN_TRANSFER_BASIN_SWEEP import signed_source_survives


AUDIT_TIMEOUT_SEC = 2400


ROWS = [
    (0.15, 0.60),
    (0.20, 0.60),
    (0.20, 0.70),
    (0.25, 0.80),
]


def main() -> None:
    print("=" * 92)
    print("GROWN TRANSFER BASIN TARGETED")
    print("  narrow neighborhood around the prior grown-row positives")
    print("=" * 92)
    print(f"H={H}, K={K}, BETA={BETA}, NL={NL}, PW={PW}, MAX_D_PHYS={MAX_D_PHYS}")
    print("rows:", ROWS)
    print()
    print(
        f"{'drift':>5s} {'restore':>7s} {'zero':>12s} {'neutral':>12s} "
        f"{'plus':>12s} {'exp':>7s} {'g0':>12s} {'g05':>12s} "
        f"{'F0':>6s} {'F05':>6s} {'toward':>11s} {'away':>11s} "
        f"{'signed':>7s} {'complex':>7s} {'both':>5s}"
    )
    print("-" * 128)

    survivors = 0
    for drift, restore in ROWS:
        row = _score_row(drift, restore)
        signed_ok = signed_source_survives(row)
        complex_ok = complex_action_survives(row)
        both_ok = signed_ok and complex_ok
        print(
            f"{drift:5.2f} {restore:7.2f} "
            f"{row.signed_zero:+12.3e} {row.signed_neutral:+12.3e} "
            f"{row.signed_single:+12.3e} {row.signed_exponent:7.3f} "
            f"{row.action_gamma0:+12.3e} {row.action_gamma05:+12.3e} "
            f"{row.action_fm0:6.3f} {row.action_fm05:6.3f} "
            f"{row.action_toward!s:>11s} {row.action_away!s:>11s} "
            f"{str(signed_ok):>7s} {str(complex_ok):>7s} {str(both_ok):>5s}"
        )

        if both_ok:
            survivors += 1

    print()
    print("SAFE READ")
    print(f"  nearby rows surviving both observables: {survivors}/{len(ROWS)}")
    print("  gamma=0.5 away-sign survivors require away_count == 3/3 and mean deflection < 0")
    if survivors:
        print("  the prior grown-row positives survive on a narrow nearby basin")
    else:
        print("  the prior positives do not survive this nearby basin")


if __name__ == "__main__":
    main()
