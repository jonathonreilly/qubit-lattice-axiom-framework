#!/usr/bin/env python3
"""Compatibility entrypoint for the repaired plaquette finite-MC verifier.

The live audited row `plaquette_self_consistency_note` now uses
`frontier_plaquette_self_consistency_finite_mc_repair.py`, which verifies the
bounded finite Wilson-plaquette diagnostic and explicitly withholds the old
same-surface physical-value certificate. This legacy command is kept only so
older harnesses and runner-triage inventories do not rediscover the obsolete
long MC sweep as a timeout blocker.
"""

from __future__ import annotations

import sys

from frontier_plaquette_self_consistency_finite_mc_repair import main as repaired_main

AUDIT_TIMEOUT_SEC = 120


def main() -> int:
    print("Plaquette self-consistency compatibility runner")
    print("Delegating to frontier_plaquette_self_consistency_finite_mc_repair.py")
    return repaired_main()


if __name__ == "__main__":
    sys.exit(main())
