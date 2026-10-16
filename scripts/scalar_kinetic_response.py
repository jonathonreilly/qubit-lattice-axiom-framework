#!/usr/bin/env python3
"""Conditional kinetic response inference; no fitted or observed data."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_KINETIC_RESPONSE_NOTE_2026-10-16.md",
    "scripts/scalar_kinetic_background.py",
    "scripts/scalar_kinetic_response_core.py",
    "scripts/scalar_kinetic_zero.py",
    "scripts/scalar_kinetic_phase.py",
    "scripts/scalar_kinetic_weak.py",
)
import hashlib
import json
from pathlib import Path
import sys
import sympy
import scalar_kinetic_background
import scalar_kinetic_response_core
import scalar_kinetic_zero
import scalar_kinetic_phase
import scalar_kinetic_weak


def main():
    root = Path(__file__).resolve().parents[1]
    result = {
        "scope": "Conditional kinetic coefficient identification and constructed original-action controls; no empirical validation",
        "input_roles": {
            "external_scientific_data": "None",
            "computed_inputs": "Explicit action solutions, registered synthetic response fields, and declared perturbation error bounds",
            "integrity_reads": ["scripts/scalar_kinetic_response.py", *AUDIT_INPUT_PATHS],
        },
        "versions": {"python": sys.version.split()[0], "sympy": sympy.__version__},
        "source_sha256": {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
                          for p in ("scripts/scalar_kinetic_response.py", *AUDIT_INPUT_PATHS)},
        "units": {},
        "counting_scope": "Control sets overlap; these counts are not independent observations or experiments.",
    }
    failed = 0
    for name, module in (
        ("general_action", scalar_kinetic_background),
        ("response_inverse", scalar_kinetic_response_core),
        ("regular_zero", scalar_kinetic_zero),
        ("real_phase_and_jets", scalar_kinetic_phase),
        ("weak_rejection", scalar_kinetic_weak),
    ):
        unit = module.run_checks()
        checks = unit["checks"]
        if not checks:
            raise RuntimeError("Empty check family: " + name)
        for check in checks:
            if type(check.get("pass")) is not bool:
                raise TypeError("Non-boolean control in " + name)
            print(("PASS" if check["pass"] else "FAIL") + " [" + name + "] " + check["name"], flush=True)
        nf = sum(not check["pass"] for check in checks)
        if unit["failed"] != nf or unit["passed"] != len(checks)-nf:
            raise RuntimeError("Inconsistent count in " + name)
        failed += nf
        result["units"][name] = unit
    result["failed"] = failed
    target = root / "outputs/scalar_kinetic_response/result.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("UNIT COUNTS:", [(k, v["passed"], v["failed"]) for k, v in result["units"].items()])
    return int(failed > 0)


if __name__ == "__main__":
    raise SystemExit(main())
