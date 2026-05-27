#!/usr/bin/env python3
"""Row-specific certificate for the Fam2 seed-0 H=0.25 boundary note.

The audited row used the reusable single-point runner as its primary runner,
whose cached default invocation is Fam1/seed0.  This certificate removes that
artifact mismatch by replaying exactly the Fam2/seed0/S=0.004 comparison used
by the note at H = 0.50, 0.35, and 0.25, then asserting the stated boundary:
the direct-dM sign survives while the old high-magnitude band collapses at the
fine H=0.25 point.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 1800

import math
import resource
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm


FAMILY = "Fam2"
SEED = 0
STRENGTH = 0.004

POINTS = (
    {
        "h": 0.50,
        "d_early": 0.005565,
        "d_late": 0.009650,
        "delta_hist": -0.004085,
        "r_hist": -0.4233,
    },
    {
        "h": 0.35,
        "d_early": 0.004743,
        "d_late": 0.007617,
        "delta_hist": -0.002874,
        "r_hist": -0.3773,
    },
    {
        "h": 0.25,
        "d_early": 0.005393,
        "d_late": 0.006969,
        "delta_hist": -0.001576,
        "r_hist": -0.2261,
    },
)

PASS_COUNT = 0
FAIL_COUNT = 0


def _family_specs(label: str) -> tuple[str, float, float]:
    for family_label, drift, restore in FAMILIES:
        if family_label == label:
            return family_label, drift, restore
    raise SystemExit(f"unknown family label: {label}")


def _rss_mb() -> float:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        return raw / (1024 * 1024)
    return raw / 1024


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"[PASS] {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL_COUNT += 1
        print(f"[FAIL] {label}" + (f" :: {detail}" if detail else ""))


def close(actual: float, expected: float, abs_tol: float) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=abs_tol)


def main() -> int:
    family_label, drift, restore = _family_specs(FAMILY)
    start = time.time()
    rows = []

    print("WAVE DIRECT-DM H=0.25 FAM2 SEED0 BOUNDARY CERTIFICATE")
    print(f"family={family_label} drift={drift:.2f} restore={restore:.2f}")
    print(f"seed={SEED} strength={STRENGTH:.6f}")
    print()

    for expected in POINTS:
        h = expected["h"]
        row = measure_dm(h, STRENGTH, family_label, drift, restore, seed=SEED)
        rows.append(row)

        print(f"[H={h:.2f}]")
        print(f"  NL={row['NL']}  PW={row['PW']:.3f}  src_layer={row['src_layer']}")
        print(f"  start_z_real={row['iz_start_real']:.3f}  end_z_real={row['iz_end_real']:.3f}")
        print(f"  dM(early)  = {row['d_early']:+.6f}")
        print(f"  dM(late)   = {row['d_late']:+.6f}")
        print(f"  delta_hist = {row['delta_hist']:+.6f}")
        print(f"  R_hist     = {row['r_hist']:+.2%}")

        check(
            f"H={h:.2f} dM(early) matches frozen row",
            close(row["d_early"], expected["d_early"], 5e-6),
            f"got {row['d_early']:+.6f}, expected {expected['d_early']:+.6f}",
        )
        check(
            f"H={h:.2f} dM(late) matches frozen row",
            close(row["d_late"], expected["d_late"], 5e-6),
            f"got {row['d_late']:+.6f}, expected {expected['d_late']:+.6f}",
        )
        check(
            f"H={h:.2f} delta_hist matches frozen row",
            close(row["delta_hist"], expected["delta_hist"], 5e-6),
            f"got {row['delta_hist']:+.6f}, expected {expected['delta_hist']:+.6f}",
        )
        check(
            f"H={h:.2f} R_hist matches frozen row",
            close(row["r_hist"], expected["r_hist"], 5e-4),
            f"got {row['r_hist']:+.4f}, expected {expected['r_hist']:+.4f}",
        )
        check(
            f"H={h:.2f} direct-dM sign survives",
            row["delta_hist"] < 0.0,
            f"delta_hist={row['delta_hist']:+.6f}",
        )
        check(
            f"H={h:.2f} late branch exceeds early branch",
            row["d_late"] > row["d_early"] > 0.0,
            f"early={row['d_early']:+.6f}, late={row['d_late']:+.6f}",
        )
        print()

    coarse, medium, fine = rows
    check(
        "fine-H value remains materially nonzero",
        abs(fine["delta_hist"]) > 1e-3,
        f"delta_hist={fine['delta_hist']:+.6f}",
    )
    check(
        "old high-band magnitude collapses at H=0.25",
        abs(fine["r_hist"]) < abs(medium["r_hist"]) < abs(coarse["r_hist"]),
        (
            f"|R_hist| H=0.25 {abs(fine['r_hist']):.2%}, "
            f"H=0.35 {abs(medium['r_hist']):.2%}, H=0.50 {abs(coarse['r_hist']):.2%}"
        ),
    )
    check(
        "boundary scope excludes a portability positive",
        abs(fine["r_hist"]) < 0.30,
        f"fine |R_hist|={abs(fine['r_hist']):.2%}",
    )

    elapsed = time.time() - start
    print()
    print(f"elapsed_s = {elapsed:.2f}")
    print(f"rss_mb    = {_rss_mb():.1f}")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
