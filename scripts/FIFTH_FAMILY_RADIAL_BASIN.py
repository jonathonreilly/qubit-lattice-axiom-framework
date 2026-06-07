#!/usr/bin/env python3
"""Basin probe for the fifth-family radial-shell connectivity slice."""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

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
from gate_b_no_restore_farfield import grow

# Static imports are intentional: the audit packet builder discovers helper
# runner paths from the primary runner's import graph.
import FIFTH_FAMILY_RADIAL_FAILURE_AUDIT as failure_audit
import FIFTH_FAMILY_RADIAL_FM_TRANSFER as fm_transfer
import FIFTH_FAMILY_RADIAL_SWEEP as sweep


AUDIT_TIMEOUT_SEC = 300
ROOT_PATH = Path(ROOT)

DRIFTS = [0.05, 0.10, 0.20, 0.30, 0.40]
SEEDS = [0, 1]
COMPANION_RUNNERS = [
    ("sweep", sweep),
    ("failure_audit", failure_audit),
    ("fm_transfer", fm_transfer),
]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _cache_path(script_path: Path) -> Path:
    return ROOT_PATH / "logs" / "runner-cache" / f"{script_path.stem}.txt"


def _check_companion_packet() -> bool:
    print()
    print("COMPANION PACKET MANIFEST")
    ok = True
    for label, module in COMPANION_RUNNERS:
        script_path = Path(module.__file__).resolve()
        cache_path = _cache_path(script_path)
        source_exists = script_path.is_file()
        cache_exists = cache_path.is_file()
        ok = ok and source_exists and cache_exists
        if source_exists:
            source_rel = script_path.relative_to(ROOT_PATH)
            source_sha = _sha256(script_path)
        else:
            source_rel = script_path
            source_sha = "MISSING"
        if cache_exists:
            cache_rel = cache_path.relative_to(ROOT_PATH)
            cache_text = cache_path.read_text(encoding="utf-8", errors="replace")
            cache_sha = _sha256(cache_path)
            cache_ok = "status: ok" in cache_text and "exit_code: 0" in cache_text
        else:
            cache_rel = cache_path
            cache_sha = "MISSING"
            cache_ok = False
        ok = ok and cache_ok
        print(f"  {label}: source={source_rel} sha256={source_sha}")
        print(f"  {label}: cache={cache_rel} sha256={cache_sha} status_ok={cache_ok}")
    print(f"COMPANION_PACKET: {'PASS' if ok else 'FAIL'}")
    return ok


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
    companion_ok = _check_companion_packet()
    all_ok = assertions_ok and companion_ok
    print(f"ASSERTIONS: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
