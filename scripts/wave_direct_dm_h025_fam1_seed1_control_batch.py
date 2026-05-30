#!/usr/bin/env python3
"""Audit primary runner for the Fam1 seed-1 H=0.25 direct-dM control note.

The shared batch runner is parameterized by CLI flags and is cited by several
family/seed notes. This wrapper gives the Fam1 seed-1 row a no-argument runner
and therefore a cache keyed to exactly the claimed computation.
"""

from __future__ import annotations


# Same heavy-compute ceiling as the shared batch runner.
AUDIT_TIMEOUT_SEC = 1800

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Explicit package-form imports make the audit packet include the helper
# sources that are load-bearing for `measure_dm`.
import scripts.wave_direct_dm_matched_history_probe as _matched_history_probe  # noqa: F401
import scripts.wave_retardation_continuum_limit as _continuum_limit  # noqa: F401
from scripts.wave_direct_dm_h025_control_batch import main as _batch_main

ARGS = ("--family", "Fam1", "--seed", "1", "--h", "0.25")


def main() -> int:
    original_argv = sys.argv[:]
    sys.argv = [sys.argv[0], *ARGS]
    try:
        return _batch_main()
    finally:
        sys.argv = original_argv


if __name__ == "__main__":
    raise SystemExit(main())
