#!/usr/bin/env python3
"""Source-bound conditional scalar/metric reconstruction controls; no data fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_METRIC_RECONSTRUCTION_NOTE_2026-10-16.md",
    "scripts/scalar_metric_geometry.py",
    "scripts/scalar_metric_constraints.py",
    "scripts/scalar_metric_coefficients.py",
    "scripts/scalar_metric_varying_coupling.py",
    "scripts/scalar_metric_joint_gain.py",
    "scripts/scalar_metric_photon_map.py",
    "scripts/scalar_metric_transport.py",
    "scripts/scalar_metric_fixed_background.py",
    "scripts/scalar_metric_conditioning.py",
    "scripts/scalar_metric_local_kernels.py",
)

from pathlib import Path
import hashlib
import json
import sys
import sympy
import numpy
import scipy
import mpmath

import scalar_metric_geometry
import scalar_metric_constraints
import scalar_metric_coefficients
import scalar_metric_varying_coupling
import scalar_metric_joint_gain
import scalar_metric_photon_map
import scalar_metric_transport
import scalar_metric_fixed_background
import scalar_metric_conditioning
import scalar_metric_local_kernels


UNITS = (
    ("geometry", scalar_metric_geometry),
    ("constraints", scalar_metric_constraints),
    ("coefficients", scalar_metric_coefficients),
    ("varying_coupling", scalar_metric_varying_coupling),
    ("joint_gain", scalar_metric_joint_gain),
    ("photon_map", scalar_metric_photon_map),
    ("transport", scalar_metric_transport),
    ("fixed_background", scalar_metric_fixed_background),
    ("conditioning", scalar_metric_conditioning),
    ("local_kernels", scalar_metric_local_kernels),
)


def main():
    root = Path(__file__).resolve().parents[1]
    result = {
        "scope": "Conditional local mathematics and constructed numerical diagnostics; no empirical validation",
        "input_roles": {
            "empirical_data": "None",
            "scientific_computation": "Imported source derives identities and generates the declared forward fixtures and synthetic noise",
            "integrity_reads": ["scripts/scalar_metric_inverse.py", *AUDIT_INPUT_PATHS],
            "external_data_reads": "None",
        },
        "versions": {
            "python": sys.version.split()[0], "sympy": sympy.__version__,
            "numpy": numpy.__version__, "scipy": scipy.__version__,
            "mpmath": mpmath.__version__,
        },
        "units": {},
        "source_sha256": {
            name: hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in ("scripts/scalar_metric_inverse.py", *AUDIT_INPUT_PATHS)
        },
    }
    failed = 0
    for name, module in UNITS:
        checks, details = module.run_checks()
        if not checks:
            raise RuntimeError(f"No checks returned by {name}")
        for check in checks:
            if type(check.get("pass")) is not bool:
                raise TypeError(f"Non-boolean control in {name}: {check.get('name')}")
            print(("PASS" if check["pass"] else "FAIL")+f" [{name}] "+check["name"])
        nfailed = sum(not check["pass"] for check in checks)
        failed += nfailed
        result["units"][name] = {
            "passed": len(checks)-nfailed, "failed": nfailed,
            "checks": checks, "details": details,
        }
    result["failed"] = failed
    result["counting_scope"] = "Unit counts overlap and are not independent experiments; 27 noise cases are diagnostics, not additional pass/fail tests."
    output = root/"outputs/scalar_metric_inverse/result.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(f"UNIT COUNTS: {[(k,v['passed'],v['failed']) for k,v in result['units'].items()]}")
    return int(failed > 0)


if __name__ == "__main__":
    raise SystemExit(main())
