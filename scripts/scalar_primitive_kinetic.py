#!/usr/bin/env python3
"""Conditional primitive photon kinetic test; no empirical or fitted inputs."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_PRIMITIVE_KINETIC_NOTE_2026-10-16.md",
    "scripts/scalar_primitive_kinetic_action.py",
    "scripts/scalar_primitive_kinetic_core.py",
    "scripts/scalar_primitive_kinetic_bound.py",
)
import hashlib
import json
from pathlib import Path
import sys
import sympy
import scalar_primitive_kinetic_action
import scalar_primitive_kinetic_core
import scalar_primitive_kinetic_bound


def main():
    root = Path(__file__).resolve().parents[1]
    result = {
        "scope": "Conditional primitive photon kinetic test and exact harmonic-error enclosure; no empirical validation",
        "input_roles": {
            "external_scientific_data": "None",
            "computed_inputs": "Explicit original-action fields, integrated photon paths, and chosen compact tests; all development controls",
            "integrity_reads": ["scripts/scalar_primitive_kinetic.py", *AUDIT_INPUT_PATHS],
        },
        "versions": {"python": sys.version.split()[0], "sympy": sympy.__version__},
        "source_sha256": {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
                          for p in ("scripts/scalar_primitive_kinetic.py", *AUDIT_INPUT_PATHS)},
        "units": {},
        "counting_scope": "Overlapping algebraic controls, not independent experiments.",
    }
    action = scalar_primitive_kinetic_action.run_checks()
    primitive, context = scalar_primitive_kinetic_core.run_checks()
    bounds = scalar_primitive_kinetic_bound.run_checks(context)
    failed = 0
    for name, unit in (("original_action", action), ("primitive", primitive), ("exact_bounds", bounds)):
        checks = unit["checks"]
        if not checks:
            raise RuntimeError("Empty control family: " + name)
        for check in checks:
            if type(check.get("pass")) is not bool:
                raise TypeError("Non-boolean control in " + name)
            print(("PASS" if check["pass"] else "FAIL") + " [" + name + "] " + check["name"], flush=True)
        nf = sum(not check["pass"] for check in checks)
        if unit["failed"] != nf or unit["passed"] != len(checks)-nf:
            raise RuntimeError("Inconsistent control counts: " + name)
        failed += nf
        result["units"][name] = unit
    result["failed"] = failed
    target = root / "outputs/scalar_primitive_kinetic/result.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("UNIT COUNTS:", [(k, v["passed"], v["failed"]) for k, v in result["units"].items()])
    return int(failed > 0)


if __name__ == "__main__":
    raise SystemExit(main())
