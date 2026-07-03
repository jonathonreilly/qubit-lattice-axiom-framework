#!/usr/bin/env python3
"""Run the beta6 plaquette connected-coefficient runner on maxorder=7.

The d7 coefficient row asks for completed evidence for:

    python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py 7

The runner-cache system executes scripts without argv, so this first-class
packet runner delegates to the existing primary runner with argv `7` and lets
the cache pin the completed maxorder-7 output.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 420


def main() -> int:
    scripts_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(scripts_dir))
    primary_path = scripts_dir / "frontier_beta6_connected_coefficient_2026_05_30.py"
    primary_sha = hashlib.sha256(primary_path.read_bytes()).hexdigest()

    import frontier_beta6_connected_coefficient_2026_05_30 as primary

    old_argv = sys.argv[:]
    sys.argv = [str(primary_path), "7"]
    try:
        print("=" * 78)
        print("BETA6 D7 MAXORDER=7 SOURCE PACKET")
        print("=" * 78)
        print("delegated_runner: scripts/frontier_beta6_connected_coefficient_2026_05_30.py")
        print("delegated_argv: 7")
        print(f"primary_runner_sha256: {primary_sha}")
        print("evidence_role: completed maxorder-7 cache for the d7 coefficient row")
        return primary.main()
    finally:
        sys.argv = old_argv


if __name__ == "__main__":
    raise SystemExit(main())
