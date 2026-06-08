#!/usr/bin/env python3
"""Aggregate runner for the tested static-readout Koide no-go.

Runs the two component checks that carry the claim:

* the rank-2 sesquilinear-modulus wall; and
* the measure-neutrality of the native complex structure J_cs.
"""

from __future__ import annotations

import koide_jcs_measure_neutral_2026_06_08 as jcs
import koide_polarization_wall_verification_2026_06_08 as wall


def main() -> int:
    print("=" * 78)
    print("Koide tested static-readout no-go aggregate runner")
    print("=" * 78)
    print()
    wall_rc = wall.main()
    print()
    print("-" * 78)
    print()
    jcs_rc = jcs.main()
    total_pass = wall.PASS + jcs.PASS
    total_fail = wall.FAIL + jcs.FAIL
    print()
    print("=" * 78)
    print(f"AGGREGATE TOTAL: PASS={total_pass} FAIL={total_fail}")
    print("=" * 78)
    return 0 if wall_rc == 0 and jcs_rc == 0 and total_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
