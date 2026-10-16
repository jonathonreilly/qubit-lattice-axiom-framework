#!/usr/bin/env python3
"""Conditional reconstruction of a quadratic hidden-mode action; synthetic checks."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy
import scipy
import sympy

from ringdown_action_math import common_controls, reconstruction_controls

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md",
    "scripts/ringdown_action_math.py",
]
ROOT = Path(__file__).resolve().parents[1]


def main():
    parent = common_controls()
    extension, inverse_details = reconstruction_controls(parent)
    checks = [
        dict(row, family=family)
        for family, rows in [("common action", parent["checks"]),
                             ("coefficient reconstruction", extension)]
        for row in rows
    ]
    passed = sum(row["passed"] for row in checks)
    failed = len(checks) - passed
    files = ["scripts/ringdown_action_inverse.py", *AUDIT_INPUT_PATHS]
    result = {
        "scope": "Exact-class algebra and synthetic controls, not empirical validation",
        "summary": {"passed": passed, "failed": failed},
        "checks": checks,
        "common_action_details": parent["details"],
        "inverse_details": inverse_details,
        "source_hashes": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in files
        },
        "versions": {"numpy": numpy.__version__, "scipy": scipy.__version__,
                     "sympy": sympy.__version__},
        "empirical_validation": False,
        "data_roles": {
            "calibration": "Synthetic force/displacement spectra; fitted pole features",
            "development": "61 synthetic environments for coefficient reconstruction",
            "reserved": "Three synthetic initial states at existing environments; first 60 samples fit preparation, last 541 predict force",
            "independent_empirical_test": "none",
        },
        "read_inventory": {
            "external_scientific_inputs": [],
            "package_integrity_reads": files,
            "imported_computation": "scripts/ringdown_action_math.py",
        },
    }
    destination = ROOT / "outputs/ringdown_action_inverse/controls.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print("Conditional action-function inverse: exact algebra and synthetic controls")
    print("No measured data, physical action selection, quantum identification or gravity identification.")
    for row in checks:
        print(f"{'PASS' if row['passed'] else 'FAIL'}: {row['family']}: {row['name']}")
    print("DETAILS: " + json.dumps(inverse_details, sort_keys=True))
    print("READS: imported helper plus note/runner/helper integrity hashes; no external scientific files.")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
