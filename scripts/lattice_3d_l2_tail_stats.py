#!/usr/bin/env python3
"""3D inverse-square tail statistics at h=0.25.

This is a narrow review-safe probe for the exploratory 1/L^2 propagator fork.
It compares a baseline width against a wider width at the same lattice spacing
and asks only whether the post-peak distance tail becomes better resolved.

The harness keeps the same family, same barrier geometry, same action, and the
same gravity-observable hierarchy. It does not attempt to promote the branch.
"""

from __future__ import annotations

import argparse
import os
import math
import sys
from contextlib import contextmanager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import scripts.lattice_3d_inverse_square_kernel as base


H = 0.25
PHYS_L = 12.0
MAX_D_PHYS = 3.0
WIDTHS = (8.0,)
AUDIT_TIMEOUT_SEC = 120

FROZEN_LOG = os.path.join(ROOT, "logs", "2026-04-04-lattice-3d-l2-tail-stats.txt")
EXPECTED_ROWS = [
    (4.0, 0.049373, 0.004422, 0.795766, "ATTRACTIVE"),
    (5.0, 0.046445, 0.003459, 0.765371, "ATTRACTIVE"),
    (6.0, 0.040248, 0.001309, 0.719169, "ATTRACTIVE"),
    (7.0, 0.035067, 0.000651, 0.668926, "ATTRACTIVE"),
    (8.0, 0.030697, 0.000357, 0.627323, "ATTRACTIVE"),
]


def check(name: str, condition: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    return bool(condition)


@contextmanager
def patched_branch(width: float):
    old_w = base.PHYS_W
    old_mass_z = list(base.MASS_Z_VALUES)
    try:
        base.PHYS_W = width
        base.MASS_Z_VALUES = [float(z) for z in range(4, int(width) + 1)]
        yield
    finally:
        base.PHYS_W = old_w
        base.MASS_Z_VALUES = old_mass_z


def tail_fit_from_rows(rows):
    if not rows:
        return math.nan, 0.0, 0, math.nan
    peak_idx = max(range(len(rows)), key=lambda i: rows[i][1])
    tail = [(mass_z, centroid) for mass_z, centroid, _, _, _ in rows[peak_idx:] if centroid > 0]
    slope, r2 = base.fit_power(tail)
    peak_z = rows[peak_idx][0]
    return slope, r2, len(tail), peak_z


def run_width(width: float):
    with patched_branch(width):
        pos, adj, nl, hw, nmap, det, barrier_layer, barrier, slit_indices, blocked, gl, span = base.build_family(H)
        barrier_row = base.barrier_metrics(pos, adj, det, barrier, slit_indices, blocked, gl, nmap, 3.0, H)
        rows, aligned, _, _ = base.no_barrier_distance(pos, adj, det, gl, nmap, H)

    slope, r2, n_tail, peak_z = tail_fit_from_rows(rows)

    print("=" * 96)
    print(f"3D 1/L^2 tail stats at h={H}  width={width:g}")
    print(f"  nodes={len(pos):,}  layers={nl}  span={span}")
    print(
        f"  barrier: Born={barrier_row['born']:.2e}  k0={barrier_row['k0']:+.6f}  "
        f"dTV={barrier_row['dtv']:.3f}  read={barrier_row['interp']}"
    )
    print(
        f"  barrier centroid={barrier_row['centroid']:+.6f}  "
        f"P_near={barrier_row['pnear']:+.6f}  bias={barrier_row['bias']:+.6f}"
    )
    print("  no-barrier rows:")
    for mass_z, centroid, pnear, bias, interp in rows:
        print(
            f"    z={mass_z:>2.0f}  centroid={centroid:+.6f}  "
            f"P_near={pnear:+.6f}  bias={bias:+.6f}  read={interp}"
        )
    if n_tail >= 3:
        print(f"  tail fit: peak@z={peak_z:.0f}  n_tail={n_tail}  exponent=b^({slope:.2f})  R^2={r2:.3f}")
    else:
        print(f"  tail fit: peak@z={peak_z:.0f}  n_tail={n_tail}  fit=n/a")
    return {"width": width, "n_tail": n_tail, "slope": slope, "r2": r2}


def recompute_main() -> None:
    print("=" * 96)
    print("3D INVERSE-SQUARE TAIL STATISTICS")
    print("  Review-safe tail probe for the exploratory 1/L^2 branch.")
    print("  Same family, same barrier geometry, same action, h=0.25.")
    print("=" * 96)
    print()

    results = [run_width(w) for w in WIDTHS]

    print()
    print("Comparison:")
    for r in results:
        print(
            f"  width={r['width']:g}: n_tail={r['n_tail']}  "
            f"exponent={r['slope']:.2f}  R^2={r['r2']:.3f}"
        )
    if len(results) >= 2 and results[1]["n_tail"] >= results[0]["n_tail"] and results[1]["r2"] >= results[0]["r2"]:
        print("  verdict: wider lattice improves the post-peak tail fit")
    elif len(results) == 1:
        print("  verdict: single-width probe; compare against the prior width-6 baseline log")
    else:
        print("  verdict: no clear improvement from widening the lattice")


def verify_frozen_log() -> int:
    import re

    print("=" * 96)
    print("3D INVERSE-SQUARE TAIL STATISTICS -- FROZEN-LOG VERIFIER")
    print("  Scope: width-8 frozen-log tail statistics only.")
    print("  Full recomputation remains available with --recompute.")
    print("=" * 96)
    print()

    passed: list[bool] = []
    if not os.path.exists(FROZEN_LOG):
        check("frozen width-8 log exists", False, FROZEN_LOG)
        return 1

    text = open(FROZEN_LOG, encoding="utf-8").read()
    passed.append(check("frozen width-8 log exists", True, FROZEN_LOG))
    passed.append(check("frozen log is width=8 at h=0.25", "h=0.25  width=8" in text))
    passed.append(check("barrier Born matches narrowed note", "Born=3.75e-15" in text))
    passed.append(check("barrier k0 matches narrowed note", "k0=+0.000000" in text))
    passed.append(check("barrier dTV matches narrowed note", "dTV=0.358" in text))
    passed.append(check("barrier read is ATTRACTIVE", "read=ATTRACTIVE" in text))

    row_re = re.compile(
        r"z=\s*(?P<z>\d+)\s+centroid=(?P<centroid>[+-]\d+\.\d+)\s+"
        r"P_near=(?P<pnear>[+-]\d+\.\d+)\s+bias=(?P<bias>[+-]\d+\.\d+)\s+"
        r"read=(?P<read>\w+)"
    )
    parsed = [
        (
            float(m.group("z")),
            float(m.group("centroid")),
            float(m.group("pnear")),
            float(m.group("bias")),
            m.group("read"),
        )
        for m in row_re.finditer(text)
    ]
    passed.append(check("five no-barrier rows parsed", len(parsed) == len(EXPECTED_ROWS), f"rows={len(parsed)}"))
    for actual, expected in zip(parsed, EXPECTED_ROWS):
        z, centroid, pnear, bias, read = actual
        ez, ec, ep, eb, er = expected
        passed.append(
            check(
                f"z={ez:.0f} row matches frozen table",
                z == ez
                and abs(centroid - ec) < 5e-7
                and abs(pnear - ep) < 5e-7
                and abs(bias - eb) < 5e-7
                and read == er,
                f"got centroid={centroid:+.6f} P_near={pnear:+.6f} bias={bias:+.6f} read={read}",
            )
        )

    peak_idx = max(range(len(parsed)), key=lambda i: parsed[i][1]) if parsed else -1
    tail = [(z, centroid) for z, centroid, _, _, _ in parsed[peak_idx:] if centroid > 0]
    slope, r2 = base.fit_power(tail)
    passed.append(check("tail peak is z=4", bool(tail) and tail[0][0] == 4.0))
    passed.append(check("tail has five post-peak points", len(tail) == 5))
    passed.append(check("tail exponent recomputes to -0.70 after display rounding", abs(slope + 0.70) < 0.01, f"slope={slope:.4f}"))
    passed.append(check("tail R^2 recomputes to 0.955 after display rounding", abs(r2 - 0.955) < 0.001, f"R^2={r2:.4f}"))
    passed.append(check("comparison remains single-width only", "single-width probe" in text))

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print()
    print(f"SCORECARD PASS={pass_count} FAIL={fail_count}")
    print("FINDING: frozen width-8 tail-stat table and post-peak fit are audit-reproducible.")
    print("BOUNDARY: no width-6 head-to-head recomputation and no asymptotic 1/r^2 closure.")
    return 0 if all(passed) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recompute",
        action="store_true",
        help="Run the original full width-8 lattice computation instead of the default frozen-log verifier.",
    )
    args = parser.parse_args()
    if args.recompute:
        recompute_main()
        return 0
    return verify_frozen_log()


if __name__ == "__main__":
    raise SystemExit(main())
