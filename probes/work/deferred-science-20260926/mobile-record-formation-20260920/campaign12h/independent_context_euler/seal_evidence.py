#!/usr/bin/env python3
"""Validate local evidence and verify the existing independent dependency seal."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


root = Path(__file__).resolve().parent
results = json.loads((root / "RESULTS.json").read_text())
assert results["status"] == "all_focused_checks_passed"
assert results["check_count"] == len(results["checks"]) == 32
assert all(item["passed"] is True for item in results["checks"])
assert results["primary_sources_read"] == []
assert (root / "RUN.log").read_bytes() == (root / "RESULTS.json").read_bytes()

dependency_dir = root.parent / "independent_context_exchange"
expected_dependencies = {
    "INPUT.md": "f20f6ebd367456ee24667bd3dcd52f30961ecd1673a21ffc996cd297bcbcdd96",
    "REPORT.md": "277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713",
    "independent_check.py": "f1c5145fdde96ef17b4a85f738d0d31456b5f32944edcc59af6ebe38ebb58404",
    "PRE_SOURCE_SEAL.json": "7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5",
}
dependencies = {}
for name, expected in expected_dependencies.items():
    path = dependency_dir / name
    actual = sha256(path.read_bytes()).hexdigest()
    assert actual == expected, (str(path), expected, actual)
    dependencies[str(path)] = actual

names = ["INPUT.md", "REPORT.md", "independent_check.py", "RESULTS.json", "RUN.log",
         "INTERRUPTED_SYMBOLIC_ATTEMPT.log", "EXECUTION_NOTES.md", "CHECKPOINT.md", "seal_evidence.py"]
artifacts = {}
for name in names:
    raw = (root / name).read_bytes()
    artifacts[name] = {"bytes": len(raw), "sha256": sha256(raw).hexdigest()}

seal = {
    "kind": "bounded_independent_pre_primary_source_euler_limit_derivation",
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "directory": str(root),
    "input_source": "Supplied Euler-limit task, reproduced in INPUT.md; the previously sealed independent context-exchange report is the only mathematical source dependency.",
    "dependency_sha256": dependencies,
    "new_primary_author_sources_read": [],
    "simulations_or_author_outcomes_read": [],
    "external_literature_imports": [],
    "status": "Smooth-profile relative-entropy and empirical-profile limits proved under the explicit hypotheses in REPORT.md, including the slow-birth extension; not a post-shock, microscopic-wave, audit, or retained-status result.",
    "load_bearing_argument": "Uniform exchange floor controls unrestricted finite-block swaps; a proved m^2 7^m Poincare bound, canonical sampling, and the entropy budget imply block replacement. Flux entropy compatibility and the birth-reference cancellation are derived explicitly.",
    "validation": {"focused_check_groups": 32, "all_passed": True,
                   "run_log_identical_to_results": True,
                   "interrupted_symbolic_attempt_preserved": True,
                   "interrupted_source_sha256": "1ca8aa162584d9c4118ef15ea1cf28d5e621e9fc48f134300b2c6065425e0a04",
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
                  "focused_check_groups": 32,
                  "prior_independent_sources_unchanged": True}, indent=2))
