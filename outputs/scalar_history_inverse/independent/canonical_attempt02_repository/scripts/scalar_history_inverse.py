#!/usr/bin/env python3
"""Source-bound exact controls for conditional scalar history reconstruction."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md",
    "scripts/scalar_history_inverse_math.py",
)

from pathlib import Path
import hashlib
import json
import sys
import sympy

from scalar_history_inverse_math import run_checks


def main():
    root = Path(__file__).resolve().parents[1]
    checks, algebra = run_checks()
    passed = sum(row["pass"] for row in checks)
    source_paths = ("scripts/scalar_history_inverse.py",) + AUDIT_INPUT_PATHS
    sources = {path: hashlib.sha256((root/path).read_bytes()).hexdigest()
               for path in source_paths}
    result = {
        "schema": "scalar-history-inverse-v1",
        "scope": "Exact conditional identities and constructed controls; no empirical validation",
        "input_roles": {
            "scientific_data": "None; all fixtures constructed in code",
            "repository_reads": "Imported helper executes the algebra; explicit note/primary/helper byte reads bind integrity",
            "external_reads": "None",
        },
        "source_sha256": sources,
        "python_version": sys.version.split()[0],
        "sympy_version": sympy.__version__,
        "passed": passed, "failed": len(checks)-passed,
        "checks": checks, "algebra": algebra,
    }
    output = root/"outputs/scalar_history_inverse/result.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    for row in checks:
        print(("PASS" if row["pass"] else "FAIL")+": "+row["name"])
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
