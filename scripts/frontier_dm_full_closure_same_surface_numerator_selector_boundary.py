#!/usr/bin/env python3
"""DM same-surface endpoint non-overlap arithmetic certificate.

This runner verifies arithmetic over helper-defined endpoint couplings and
helper-returned certified intervals. It does not prove selector existence,
selector absence, or helper-packet completeness.
"""

from __future__ import annotations

import sys

from canonical_plaquette_surface import CANONICAL_ALPHA_BARE, CANONICAL_ALPHA_LM
from dm_full_closure_minimal_reduced_cycle_extension_map_common import (
    omega_b_from_eta,
    plaquette_supported_alpha_short_distance,
)
from dm_full_closure_same_surface_thermal_support_common import (
    certified_same_surface_ratio_bounds,
)
from dm_leptogenesis_exact_common import ETA_OBS

AUDIT_TIMEOUT_SEC = 120

PASS_COUNT = 0
FAIL_COUNT = 0


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
    print("DM SAME-SURFACE ENDPOINT NON-OVERLAP ARITHMETIC CERTIFICATE")
    print("=" * 88)
    print("Status authority: independent audit lane only.")
    print("Claim boundary: arithmetic over helper-defined outputs only.")

    print("\n" + "=" * 88)
    print("PART 1: HELPER-DEFINED ENDPOINT VALUES")
    print("=" * 88)
    alpha_bare = float(CANONICAL_ALPHA_BARE)
    alpha_lo = float(CANONICAL_ALPHA_LM)
    alpha_hi = float(plaquette_supported_alpha_short_distance())

    check("alpha_bare is positive", alpha_bare > 0.0, f"alpha_bare={alpha_bare:.15f}")
    check("alpha_lo is positive", alpha_lo > 0.0, f"alpha_lo={alpha_lo:.15f}")
    check("alpha_hi is positive", alpha_hi > 0.0, f"alpha_hi={alpha_hi:.15f}")
    check(
        "endpoint ordering is alpha_bare < alpha_lo < alpha_hi",
        alpha_bare < alpha_lo < alpha_hi,
        f"alpha_bare={alpha_bare:.15f}, alpha_lo={alpha_lo:.15f}, alpha_hi={alpha_hi:.15f}",
    )

    print("\n" + "=" * 88)
    print("PART 2: CERTIFIED INTERVAL NON-OVERLAP")
    print("=" * 88)
    r_lo_lo, r_lo_hi, att_lo, rep_lo = certified_same_surface_ratio_bounds(alpha_lo)
    r_hi_lo, r_hi_hi, att_hi, rep_hi = certified_same_surface_ratio_bounds(alpha_hi)
    omega_b = float(omega_b_from_eta(ETA_OBS))
    omega_dm_lo_lo = r_lo_lo * omega_b
    omega_dm_lo_hi = r_lo_hi * omega_b
    omega_dm_hi_lo = r_hi_lo * omega_b
    omega_dm_hi_hi = r_hi_hi * omega_b

    check(
        "R(alpha_lo) certified interval is ordered",
        r_lo_lo <= r_lo_hi,
        f"R_lo=[{r_lo_lo:.12f}, {r_lo_hi:.12f}]",
    )
    check(
        "R(alpha_hi) certified interval is ordered",
        r_hi_lo <= r_hi_hi,
        f"R_hi=[{r_hi_lo:.12f}, {r_hi_hi:.12f}]",
    )
    check(
        "R intervals are disjoint in endpoint order",
        r_lo_hi < r_hi_lo,
        f"R_lo_hi={r_lo_hi:.12f}, R_hi_lo={r_hi_lo:.12f}",
    )
    check(
        "Omega_DM intervals are disjoint after multiplying by Omega_b",
        omega_dm_lo_hi < omega_dm_hi_lo,
        f"Omega_DM_lo=[{omega_dm_lo_lo:.12f}, {omega_dm_lo_hi:.12f}], "
        f"Omega_DM_hi=[{omega_dm_hi_lo:.12f}, {omega_dm_hi_hi:.12f}]",
    )

    print()
    print(f"  trunc_lo = (N_att={att_lo}, N_rep={rep_lo})")
    print(f"  trunc_hi = (N_att={att_hi}, N_rep={rep_hi})")
    print()
    print("Boundary: this runner does not assert selector existence, selector")
    print("absence, or helper-packet completeness.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
