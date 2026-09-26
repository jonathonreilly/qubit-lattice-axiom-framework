#!/usr/bin/env python3
"""Validate and seal only this independent deliverable directory."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


root = Path(__file__).resolve().parent
results = json.loads((root / "RESULTS.json").read_text())
assert results["status"] == "all_exact_checks_passed"
assert results["check_count"] == len(results["checks"]) == 46
assert all(item["passed"] is True for item in results["checks"])
assert (root / "RUN.log").read_bytes() == (root / "RESULTS.json").read_bytes()

names = ["INPUT.md", "REPORT.md", "independent_check.py", "RESULTS.json",
         "RUN.log", "INITIAL_SYNTAX_FAILURE.log", "CHECKPOINT.md", "seal_evidence.py"]
artifacts = {}
for name in names:
    raw = (root / name).read_bytes()
    artifacts[name] = {"bytes": len(raw), "sha256": sha256(raw).hexdigest()}

seal = {
    "kind": "bounded_independent_pre_primary_source_mathematical_check",
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "directory": str(root),
    "input_source": "Parent-supplied task specification, reproduced in INPUT.md",
    "primary_sources_read": [],
    "other_research_sources_read_or_imported": [],
    "external_literature_imports": [],
    "independence": "Derivation and checker completed before any primary context-exchange, streaming, or current-classification calculation was accessed.",
    "actions": "Only the assigned deliverable directory was intentionally written. No Git, PR, audit, delegation, or external communication actions.",
    "validation": {"exact_grouped_checks": 46, "all_passed": True,
                   "run_log_identical_to_results": True,
                   "initial_syntax_only_failure_preserved": True},
    "scientific_scope": "Rate validity, product stationarity, homogeneous currents, current Jacobian and its isotropy classification, homogeneous birth flow. No hydrodynamic or microscopic-wave theorem, and no audit or retained-status verdict.",
    "artifacts": artifacts,
}
path = root / "PRE_SOURCE_SEAL.json"
path.write_text(json.dumps(seal, indent=2, sort_keys=True) + "\n")
print(json.dumps({"report_sha256": artifacts["REPORT.md"]["sha256"],
                  "checker_sha256": artifacts["independent_check.py"]["sha256"],
                  "results_and_log_sha256": artifacts["RESULTS.json"]["sha256"],
                  "seal_sha256": sha256(path.read_bytes()).hexdigest(),
                  "exact_grouped_checks": 46}, indent=2))
