#!/usr/bin/env python3
"""Basin probe for the fifth-family radial-shell connectivity slice."""

from __future__ import annotations

import os
import sys
from pathlib import Path
import hashlib
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP import (
    Family,
    _build_radial_shell_connectivity,
    _measure_family,
    _mean,
)
import FIFTH_FAMILY_RADIAL_FM_TRANSFER as fm_transfer
from gate_b_no_restore_farfield import grow


AUDIT_TIMEOUT_SEC = 300

DRIFTS = [0.05, 0.10, 0.20, 0.30, 0.40]
SEEDS = [0, 1]
TRANSFER_RUNNER = Path(SCRIPT_DIR) / "FIFTH_FAMILY_RADIAL_FM_TRANSFER.py"
TRANSFER_CACHE = Path(ROOT) / "logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _transfer_cache_is_current() -> bool:
    if not TRANSFER_CACHE.exists():
        return False
    text = TRANSFER_CACHE.read_text(encoding="utf-8", errors="replace")
    expected_sha = _sha256(TRANSFER_RUNNER)
    required = [
        "===== runner cache v1 =====",
        "runner: scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py",
        f"runner_sha256: {expected_sha}",
        "status: ok",
        "ASSERTIONS: PASS",
    ]
    return all(item in text for item in required)


def transfer_packet_checks() -> bool:
    print()
    print("TRANSFER SOURCE PACKET")
    print(f"  source: scripts/{TRANSFER_RUNNER.name}")
    print(f"  cache: logs/runner-cache/{TRANSFER_CACHE.name}")
    cache_ok = _transfer_cache_is_current()
    print(f"  cache SHA/current assertion: {'PASS' if cache_ok else 'FAIL'}")
    print()
    print(f"{'drift':>5s} {'seed':>4s} {'F~M':>8s} {'ok':>4s}")
    print("-" * 24)

    rows = []
    for drift, seed in fm_transfer.TARGETS:
        fm = fm_transfer._fm(drift, seed)
        ok = not math.isnan(fm) and abs(fm - 1.0) < 0.05
        rows.append((drift, seed, fm, ok))
        print(f"{drift:5.2f} {seed:4d} {fm:8.3f} {'YES' if ok else 'no':>4s}")

    passed = [row for row in rows if row[-1]]
    print(f"  transfer rows passed: {len(passed)}/{len(rows)}")
    if passed:
        print(f"  mean F~M among transfer passes: {_mean([row[2] for row in passed]):.6f}")
    transfer_ok = (
        cache_ok
        and {(row[0], row[1]) for row in passed} == set(fm_transfer.TARGETS)
        and all(abs(row[2] - 1.0) < 0.05 for row in passed)
    )
    print(f"  [{'PASS' if transfer_ok else 'FAIL'} (C)] F~M transfer source/cache packet")
    return transfer_ok


def main() -> None:
    print("=" * 96)
    print("FIFTH FAMILY RADIAL BASIN")
    print("  radial-shell connectivity on the no-restore grown slice")
    print("=" * 96)
    print(f"drifts={DRIFTS}, seeds={SEEDS}")
    print("guards: exact zero-source baseline, exact neutral cancellation, sign orientation")
    print()
    print(f"{'drift':>5s} {'seed':>4s} {'zero':>12s} {'plus':>12s} {'minus':>12s} {'neutral':>12s} {'double':>12s} {'exp':>7s} {'ok':>4s}")
    print("-" * 96)

    rows = []
    for drift in DRIFTS:
        for seed in SEEDS:
            pos, adj, layers, _nmap = grow(drift, seed)
            fam = Family(pos, layers, adj)
            radial = _build_radial_shell_connectivity(fam)
            out = _measure_family(radial.positions, radial.adj, radial.layers)
            rows.append((drift, seed, out.zero, out.plus, out.minus, out.neutral, out.double, out.exponent, out.ok))
            print(
                f"{drift:5.2f} {seed:4d} "
                f"{out.zero:+12.3e} {out.plus:+12.3e} {out.minus:+12.3e} "
                f"{out.neutral:+12.3e} {out.double:+12.3e} {out.exponent:7.3f} "
                f"{'YES' if out.ok else 'no':>4s}"
            )

    passed = [r for r in rows if r[-1]]
    print()
    print("SAFE READ")
    print(f"  passed rows: {len(passed)}/{len(rows)}")
    pass_keys = {(r[0], r[1]) for r in passed}
    assertions_ok = pass_keys == {(0.05, 0), (0.10, 0), (0.30, 0), (0.30, 1)}
    if passed:
        drift_vals = sorted({r[0] for r in passed})
        print(f"  drift coverage: {drift_vals}")
        print(f"  mean exponent among passes: {_mean([r[7] for r in passed]):.6f}")
        print("  this radial-shell family is a real bounded basin, but not family-wide")
    else:
        print("  no row survived the exact zero/neutral gate")
        print("  the radial-shell rule is a diagnosed failure on this slice")
    print(
        f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] finite basin assertion surface"
    )
    transfer_ok = transfer_packet_checks()
    all_ok = assertions_ok and transfer_ok
    print(f"ASSERTIONS: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
