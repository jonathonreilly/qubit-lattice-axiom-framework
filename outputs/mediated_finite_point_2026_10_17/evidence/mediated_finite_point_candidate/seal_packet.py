#!/usr/bin/env python3
"""Metadata-only closure verification. Does not import or rerun calculate.py."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import ast
import json


def pin(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def fraction(row):
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def main():
    root = Path(__file__).resolve().parent
    assert not (root / "FINAL_FREEZE.json").exists()
    run = root / "runs" / "calculation_001"
    receipt = json.loads((run / "EXECUTION.json").read_text())
    for key in ("source_at_launch", "launcher_at_launch", "source_capture", "launcher_capture",
                "premise_manifest", "stdout", "stderr", "source_after_run", "launcher_after_run", "output"):
        assert pin(receipt[key]["path"]) == receipt[key], key
    assert receipt["argv"] == [receipt["argv"][0], str(root / "calculate.py"), "--output", str(run / "EXACT_CERTIFICATE.json")]
    assert receipt["exit_code"] == 0 and receipt["timed_out"] is False
    assert receipt["source_at_launch"]["sha256"] == receipt["source_capture"]["sha256"]
    assert receipt["launcher_at_launch"]["sha256"] == receipt["launcher_capture"]["sha256"]
    assert receipt["source_after_run"] == receipt["source_at_launch"]
    assert receipt["launcher_after_run"] == receipt["launcher_at_launch"]
    assert len(list((root / "runs").iterdir())) == 1
    source_count = 0
    for name in ("SOURCE_PINS.json", "SUPPLEMENTAL_SOURCE_PINS.json"):
        for row in json.loads((root / name).read_text())["sources"]:
            assert pin(row["path"]) == row, row["path"]
            source_count += 1
    certificate = json.loads((run / "EXACT_CERTIFICATE.json").read_text())
    assert certificate["executed_source_sha256"] == receipt["source_at_launch"]["sha256"]
    assert len(certificate["gates"]) == 50
    for row in certificate["gates"]:
        left, right = fraction(row["left"]["hi"]), fraction(row["right"]["lo"])
        ok = left < right if row["comparison"] == "upper(left)<lower(right)" else left <= right
        assert ok and row["passed"] is True, row["name"]
    for row in certificate["intervals"].values():
        assert fraction(row["lo"]) <= fraction(row["hi"])
    stdout = json.loads((run / "stdout").read_text())
    assert stdout["exact_certificate"] == pin(run / "EXACT_CERTIFICATE.json")
    assert stdout["selected_window"] == certificate["selected_window"]
    assert stdout["counts"] == certificate["counts"]
    assert stdout["gate_count"] == 50 and stdout["all_gates_passed"] is True
    for path in root.rglob("*.py"):
        ast.parse(path.read_text())
        assert all(line.rstrip() == line for line in path.read_text().splitlines())
    assert all(line.rstrip() == line for line in (root / "PROPOSAL.md").read_text().splitlines())
    validated_at = datetime.now(timezone.utc).isoformat()
    validation = {
        "kind": "metadata_closure_verification_not_independent_science_check",
        "validated_at_utc": validated_at, "source_identity_count": source_count,
        "actual_scientific_run_count": 1, "preserved_scientific_failure_count": 0,
        "gate_comparisons_rechecked_from_saved_rationals": 50,
        "source_capture_and_stream_pins_verified": True,
        "scientific_program_imported_or_rerun_by_this_validator": False,
        "independent_mathematical_review": None,
        "proposal": pin(root / "PROPOSAL.md"), "calculation_receipt": pin(run / "EXECUTION.json"),
    }
    (root / "METADATA_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n")
    members = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            data = path.read_bytes()
            members.append({"path": str(path.relative_to(root)), "bytes": len(data), "sha256": sha256(data).hexdigest()})
    freeze = {"kind": "source_exposed_single_tuple_author_candidate_freeze",
              "created_at_utc": datetime.now(timezone.utc).isoformat(),
              "independent_review_status": "pending separate review; no verdict created here",
              "files": members, "self_excluded": "FINAL_FREEZE.json"}
    (root / "FINAL_FREEZE.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(json.dumps({"freeze": pin(root / "FINAL_FREEZE.json"), "proposal": pin(root / "PROPOSAL.md"),
                      "members": len(members), "source_identities": source_count,
                      "science_runs": 1, "saved_gate_comparisons": 50}, indent=2))


if __name__ == "__main__":
    main()
