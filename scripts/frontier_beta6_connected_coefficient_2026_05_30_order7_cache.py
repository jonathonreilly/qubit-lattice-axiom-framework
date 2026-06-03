#!/usr/bin/env python3
"""Cacheable order-7 wrapper for the beta=6 connected-coefficient runner.

`scripts/cached_runner_output.py` caches by runner path and does not accept
argv. This wrapper supplies the audited `maxorder=7` invocation while preserving
the primary computation in `frontier_beta6_connected_coefficient_2026_05_30.py`.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "scripts" / "frontier_beta6_connected_coefficient_2026_05_30.py"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import frontier_beta6_connected_coefficient_2026_05_30 as coeff  # noqa: E402


def main() -> int:
    parent_sha = hashlib.sha256(PARENT.read_bytes()).hexdigest()
    print("ORDER-7 CACHE WRAPPER")
    print("  executes: python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py 7")
    print(f"  parent_sha256: {parent_sha}")
    print()
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(PARENT), "7"]
        return int(coeff.main())
    finally:
        sys.argv = old_argv


if __name__ == "__main__":
    raise SystemExit(main())
