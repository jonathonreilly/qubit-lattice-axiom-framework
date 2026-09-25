#!/usr/bin/env python3
"""Bind this completed PRE and already inspected evidence; no science verdict."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    seal_path = ROOT / "PRE_SEAL.json"
    assert not seal_path.exists(), "Existing immutable PRE seal must not be replaced"
    pins = json.loads((ROOT / "SOURCE_PINS.json").read_text())
    source_rows = []
    for row in pins["scientific_sources"] + pins["instruction_sources"]:
        p = ROOT / row["snapshot"]
        assert sha(p) == row["sha256"] and p.stat().st_size == row["bytes"]
        source_rows.append({"path": row["snapshot"], "sha256": sha(p)})

    control = json.loads((ROOT / "CONTROL_EXECUTION.json").read_text())
    assert control["returncode"] == 0
    assert control["script_sha256"] == sha(ROOT / "independent_controls.py")
    for name, row in control["outputs"].items():
        assert sha(ROOT / name) == row["sha256"]
        assert (ROOT / name).stat().st_size == row["bytes"]
    result = json.loads((ROOT / "INDEPENDENT_CONTROL_RESULTS.json").read_text())
    assert result["script_sha256"] == control["script_sha256"]
    assert (ROOT / "CONTROL.stdout.txt").read_bytes() == (ROOT / "INDEPENDENT_CONTROL_RESULTS.json").read_bytes()
    assert (ROOT / "CONTROL.stderr.txt").stat().st_size == 0
    assert len(result["two_band_control"]["rows"]) == 12

    source_exec = json.loads((ROOT / "SOURCE_RECHECK_EXECUTION.json").read_text())
    assert source_exec["returncode"] == 0
    for name, row in source_exec["files"].items():
        assert sha(ROOT / name) == row["sha256"]
        assert (ROOT / name).stat().st_size == row["bytes"]
    assert (ROOT / "SOURCE_RECHECK.stdout.txt").read_bytes() == (ROOT / "SOURCE_PINS.json").read_bytes()
    assert (ROOT / "SOURCE_RECHECK.stderr.txt").stat().st_size == 0

    binding = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Mechanical identity checks only; no mathematical or audit verdict",
        "scientific_source_count": len(pins["scientific_sources"]),
        "instruction_source_count": len(pins["instruction_sources"]),
        "source_hashes_reverified": source_rows,
        "control_execution_returncode": control["returncode"],
        "control_script_sha256": control["script_sha256"],
        "control_result_sha256": sha(ROOT / "INDEPENDENT_CONTROL_RESULTS.json"),
        "two_band_output_row_count": len(result["two_band_control"]["rows"]),
        "primitive_zero_field_word_count": len(result["word_control"]["all_zero_field_F_words"]),
        "source_identity_execution_returncode": source_exec["returncode"],
        "pre_sha256": sha(ROOT / "PRE.md"),
        "source_pins_sha256": sha(ROOT / "SOURCE_PINS.json"),
        "candidate_disclosure_state": "No released new candidate read before this PRE seal",
    }
    (ROOT / "FINAL_BINDING_CHECK.json").write_text(json.dumps(binding, indent=2) + "\n")
    members = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        path.chmod(0o444)
        members.append({"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size,
                        "sha256": sha(path), "mode": "0444"})
    seal = {
        "schema": "independent-pre-evidence-seal-v1",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "root": str(ROOT), "phase": "PRE before new root candidate release",
        "member_count": len(members), "members": members,
        "authority": "Hash-bound conditional reconstruction and limited corroborating controls; not an audit verdict",
        "preservation": "Do not replace or edit these PRE members; later comparison uses separate POST files",
    }
    seal_path.write_text(json.dumps(seal, indent=2) + "\n")
    seal_path.chmod(0o444)
    for row in members:
        path = ROOT / row["path"]
        assert sha(path) == row["sha256"]
        assert path.stat().st_mode & 0o222 == 0
    print(json.dumps({"seal": str(seal_path), "seal_sha256": sha(seal_path),
                      "pre_sha256": sha(ROOT / "PRE.md"), "member_count": len(members),
                      "binding_check_sha256": sha(ROOT / "FINAL_BINDING_CHECK.json")}, indent=2))


if __name__ == "__main__":
    main()
