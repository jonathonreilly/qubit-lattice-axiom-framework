"""Necessary scalar environment bounds from a supplied physical static metric."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    "docs/SCALAR_PHYSICAL_CURVATURE_ENVIRONMENT_BOUNDED_THEOREM_NOTE_2026-10-15.md",
    "scripts/scalar_physical_curvature_action.py",
    "scripts/scalar_physical_curvature_geometry.py",
    "docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/EXPONENTIAL_SCALAR_FINITE_BODY_BOUNDED_THEOREM_NOTE_2026-10-14.md",
    "docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    ".claude/science/physics-loops/observations-backward-24h-20261014/finite_environment/NO_GO_DISCIPLINE_CHECKLIST.md",
]
import argparse
import hashlib
import json
from pathlib import Path
import scalar_physical_curvature_action as action
import scalar_physical_curvature_geometry as geometry

ROOT = Path(__file__).resolve().parents[1]


def run():
    components = {"action": action.controls(), "geometry": geometry.controls()}
    checks = [{**row, "name": label + "." + row["name"]}
              for label, value in components.items() for row in value["checks"]]
    return {
        "actual_current_surface_status": "conditional-support",
        "target_claim_type": "bounded_theorem",
        "scope": "Necessary finite-domain scalar ceiling under the complete supplied action, physical static metric, regularity and boundary premises",
        "checks": checks,
        "components": components,
        "counts": {"passed": sum(r["passed"] for r in checks),
                   "failed": sum(not r["passed"] for r in checks)},
        "empirical_tests": 0,
        "observational_datasets_opened": 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path,
                        default=ROOT / "outputs/scalar_physical_curvature")
    args = parser.parse_args()
    result = run()
    result["primary_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["input_sha256"] = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                              for p in AUDIT_INPUT_PATHS}
    result["read_inventory"] = {
        "scientific_inputs": ["Symbolic original action and explicitly frozen synthetic geometries in declared helpers"],
        "integrity_reads": ["This primary and declared note/helper/premise/checklist inputs; no observed arrays, inherited output values or reviewer results loaded"],
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "RESULTS_v1.json").write_text(
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n")
    summary = {k: result[k] for k in [
        "actual_current_surface_status", "target_claim_type", "scope", "counts",
        "empirical_tests", "observational_datasets_opened", "primary_sha256",
        "input_sha256", "read_inventory"]}
    summary["failed_checks"] = [r for r in result["checks"] if not r["passed"]]
    summary["remaining_inputs"] = [
        "Actual complete action and parameters, ambient/initial state",
        "Calibrated static physical metric, curvature errors and complete boundary",
        "Material/metric consistency and dynamical environment realization",
        "Identification of action coefficient or coupling with an actual force/readout",
    ]
    (args.output_dir / "SUMMARY_v1.json").write_text(
        json.dumps(summary, sort_keys=True, indent=2, allow_nan=False) + "\n")
    for label, scope in {
        "per_element": "checked: Weyl coefficients, full scalar variation, Ricci contraction, signs and conformal normalization",
        "per_site": "checked: six synthetic scalar profiles in specified metrics; no actual gravitating body or empirical calibration",
        "per_mode": "checked and not executed: no full dynamical spectrum or force/gradient bound",
        "per_block": "checked: regular finite-domain comparison, spherical Green quadrature and integrated scalar flux",
        "lattice_wide": "checked and not executed: no action/state/scale selection, full Einstein/matter solution or empirical validation",
    }.items():
        print(label + ": " + scope)
    print(json.dumps(summary, sort_keys=True, indent=2, allow_nan=False))
    print(f"TOTAL: PASS={result['counts']['passed']} FAIL={result['counts']['failed']}")
    return int(result["counts"]["failed"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
