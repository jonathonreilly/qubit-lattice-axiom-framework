#!/usr/bin/env python3
"""Seal only this independent check and verify its prior independent sources."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


root = Path(__file__).resolve().parent
results = json.loads((root / "RESULTS.json").read_text())
assert results["status"] == "all_exact_checks_passed"
assert results["check_count"] == len(results["checks"]) == 66
assert all(item["passed"] is True for item in results["checks"])
assert results["primary_sources_read"] == []
assert (root / "RUN.log").read_bytes() == (root / "RESULTS.json").read_bytes()
assert (root / "PROGRESS.log").read_text().splitlines() == [item["name"] for item in results["checks"]]

expected_dependencies = {
    "independent_context_exchange/REPORT.md": "277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713",
    "independent_context_exchange/PRE_SOURCE_SEAL.json": "7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5",
    "independent_context_euler/REPORT.md": "60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3",
    "independent_context_euler/independent_check.py": "5ebc1ce0750c658649447e0a0d8da146b2ab64bd4fd83d232329281d1df4b3d4",
    "independent_context_euler/PRE_SOURCE_SEAL.json": "48dda0ccb30539906dd6274bbf8736258727077c0018bb89c604f491164a1fa9",
}
dependencies = {}
for name, expected in expected_dependencies.items():
    path = root.parent / name
    actual = sha256(path.read_bytes()).hexdigest()
    assert actual == expected, (name, expected, actual)
    dependencies[str(path)] = actual

names = ["INPUT.md", "REPORT.md", "CHECKPOINT.md", "independent_check.py",
         "RESULTS.json", "RUN.log", "PROGRESS.log", "seal_evidence.py"]
artifacts = {}
for name in names:
    raw = (root / name).read_bytes()
    artifacts[name] = {"bytes": len(raw), "sha256": sha256(raw).hexdigest()}

seal = {
    "kind": "bounded_independent_pre_primary_source_axis_balanced_context_derivation",
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "directory": str(root),
    "input_source": "Supplied task specification reproduced in INPUT.md, plus the explicitly identified earlier independent current/Euler evidence.",
    "dependency_sha256": dependencies,
    "new_primary_author_sources_read": [],
    "primary_simulations_or_outcomes_read": [],
    "external_literature_imports": [],
    "algebraic_result": "Every homogeneous product is exchange-stationary. The nonzero direction-independent current pair exists at every interior density exactly for u=0, B=-3A/2, EA nonzero; the other four modes are zero. The proposed fixed witness satisfies this condition.",
    "euler_status": "The earlier sealed smooth-profile proof applies after explicit verification of the new rate bounds, stationarity, local current, entropy potential, entropy symmetry, and unchanged block and reaction hypotheses. Uniform positivity and a given smooth interior solution remain assumptions.",
    "birth_scope": "Balanced homogeneous growth preserves the all-density current tuning but changes the speed and adds reaction. Microscopic epsilon/N gives finite Euler reaction; fixed microscopic epsilon is a distinct fast-filling scaling.",
    "limitations": "No exact finite-N wave, microscopic fluctuation theorem, continuous rotational symmetry of the nonlinear dynamics, post-shock extension, boundary-density Euler extension, audit, or retained-status verdict is claimed.",
    "validation": {"exact_grouped_checks": 66, "all_passed": True,
                   "run_log_identical_to_results": True,
                   "progress_log_matches_check_list": True,
                   "prior_independent_sources_unchanged": True,
                   "python": results["python"], "sympy": results["sympy"]},
    "actions": "Only the assigned deliverable directory was intentionally written; no Git, PR, audit, external-message, or delegation actions.",
    "artifacts": artifacts,
}
path = root / "PRE_SOURCE_SEAL.json"
path.write_text(json.dumps(seal, indent=2, sort_keys=True) + "\n")
print(json.dumps({"report_sha256": artifacts["REPORT.md"]["sha256"],
                  "checker_sha256": artifacts["independent_check.py"]["sha256"],
                  "results_and_log_sha256": artifacts["RESULTS.json"]["sha256"],
                  "seal_sha256": sha256(path.read_bytes()).hexdigest(),
                  "exact_grouped_checks": 66,
                  "prior_independent_sources_unchanged": True}, indent=2))
