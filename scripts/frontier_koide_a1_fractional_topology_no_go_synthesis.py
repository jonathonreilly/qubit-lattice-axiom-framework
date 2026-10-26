#!/usr/bin/env python3
"""Propagate finite O13 correction checks; former five-route no-go withdrawn.

No other historical probe's counts are accepted as scientific certification.
"""
from __future__ import annotations
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
import scripts.frontier_koide_a1_cheeger_simons_rz_probe as correction


def main() -> int:
    result = correction.main()
    print('SYNTHESIS_SCOPE=finite correction only; five-route no-go withdrawn')
    print('OPEN=other four probes and physical selection need separate review')
    return result


if __name__ == '__main__':
    raise SystemExit(main())
