#!/usr/bin/env python3
"""Conditional joint photon/background/calibration controls; no observed fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_PHOTON_CALIBRATION_NOTE_2026-10-16.md",
    "scripts/scalar_photon_reception_core.py",
    "scripts/scalar_photon_separate_gains.py",
    "scripts/scalar_photon_calibration_controls.py",
    "scripts/scalar_photon_weak_controls.py",
)
import hashlib
import json
from pathlib import Path
import sys
import numpy
import sympy
import scalar_photon_reception_core
import scalar_photon_separate_gains
import scalar_photon_calibration_controls
import scalar_photon_weak_controls


def main():
    root=Path(__file__).resolve().parents[1]
    result={
        "scope":"Conditional mathematical identification and constructed diagnostics; no empirical validation",
        "input_roles":{
            "external_scientific_data":"None",
            "computed_inputs":"Original-action local fields, observer-origin integrals and declared synthetic derivative perturbations",
            "integrity_reads":["scripts/scalar_photon_calibration.py",*AUDIT_INPUT_PATHS],
        },
        "versions":{"python":sys.version.split()[0],"sympy":sympy.__version__,"numpy":numpy.__version__},
        "source_sha256":{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ("scripts/scalar_photon_calibration.py",*AUDIT_INPUT_PATHS)},
        "units":{},
        "counting_scope":"Controls overlap. The separate-gain unit repeats the original-action fixture; totals are not independent experiments.",
    }
    failures=0
    for name,module in (("common_reception",scalar_photon_reception_core),("separate_reception",scalar_photon_separate_gains),("conditioning_and_omission",scalar_photon_calibration_controls),("primitive_weak_residual",scalar_photon_weak_controls)):
        checks,details=module.run_checks()
        if not checks:raise RuntimeError("No controls in "+name)
        for c in checks:
            if type(c.get('pass')) is not bool:raise TypeError("Non-boolean control")
            print(("PASS" if c['pass'] else "FAIL")+" ["+name+"] "+c['name'],flush=True)
        nf=sum(not c['pass'] for c in checks);failures+=nf
        result['units'][name]={'passed':len(checks)-nf,'failed':nf,'checks':checks,'details':details}
    result['failed']=failures
    destination=root/'outputs/scalar_photon_calibration/result.json'
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print("UNIT COUNTS:",[(n,v['passed'],v['failed']) for n,v in result['units'].items()])
    return int(failures>0)


if __name__=='__main__':
    raise SystemExit(main())
