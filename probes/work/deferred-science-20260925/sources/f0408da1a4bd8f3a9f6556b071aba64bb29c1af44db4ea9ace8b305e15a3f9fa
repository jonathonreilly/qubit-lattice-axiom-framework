#!/usr/bin/env python3
"""Bound released bytes and inspect recorded tables; never execute author code.

This is source/evidence correspondence, not an independent numerical replication.
Only the two previously authorized parents are opened from the author source pins.
"""
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from hashlib import sha256
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "microscopic-record-readout-personal"
SNAPSHOT = HERE / "post-released"
EXPECTED_PRE_SEAL = "34cbabad0237942680176e23a39bfdd6e9f4f34bbf56f1ff4f50b15178838f41"
EXPECTED_AUTHOR_SEAL = "1c43b31b63f89ba2bf246e50aa5e8dd95d93d77f0e06aafd8d394909966a9146"
NOTE = "MICROSCOPIC_FINITE_BIN_RECORD_BRIDGE_ROOT.md"
EXPECTED_NOTE = "a04e25530ccf1dc8df8a27b41523d04703c09ff758664792a9487a8cea0ce60c"


def digest(data):
    return sha256(data).hexdigest()


def emit(path, data):
    encoded = (json.dumps(data, indent=2) + "\n").encode()
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite existing evidence: {path.name}")
    path.write_bytes(encoded)


def main():
    start = datetime.now(timezone.utc).isoformat()
    pre_seal_bytes = (HERE / "PRE_SEAL.json").read_bytes()
    assert digest(pre_seal_bytes) == EXPECTED_PRE_SEAL
    pre_seal = json.loads(pre_seal_bytes)
    pre_checks = []
    for member in pre_seal["members"]:
        data = (HERE / member["path"]).read_bytes()
        assert digest(data) == member["sha256"]
        assert len(data) == member["bytes"]
        pre_checks.append({**member, "matches_frozen_PRE": True})
    assert len(pre_checks) == 13

    author_seal_bytes = (ROOT / "AUTHOR_CONTROL_SEAL.json").read_bytes()
    assert digest(author_seal_bytes) == EXPECTED_AUTHOR_SEAL
    author_seal = json.loads(author_seal_bytes)
    assert author_seal["files"][NOTE] == EXPECTED_NOTE
    frozen_bytes = {"AUTHOR_CONTROL_SEAL.json": author_seal_bytes}
    for name, expected in author_seal["files"].items():
        assert Path(name).name == name
        data = (ROOT / name).read_bytes()
        assert digest(data) == expected
        frozen_bytes[name] = data
    assert len(frozen_bytes) == 8
    SNAPSHOT.mkdir(exist_ok=False)
    released = []
    for name, data in frozen_bytes.items():
        target = SNAPSHOT / name
        target.write_bytes(data)
        assert target.read_bytes() == data
        target.chmod(0o444)
        released.append({"origin": str(ROOT / name),
                         "snapshot": str(target.relative_to(HERE)),
                         "sha256": digest(data), "bytes": len(data)})

    source_pins = json.loads((HERE / "SOURCE_PINS.json").read_bytes())
    origin_checks = []
    for source in source_pins["sources"]:
        data = subprocess.run(
            ["git", "-C", source["repository"], "show",
             source["revision"] + ":" + source["path"]],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
        assert digest(data) == source["sha256"]
        assert data == (HERE / source["snapshot"]).read_bytes()
        origin_checks.append({**source, "matches_exact_git_bytes": True})
    assert len(origin_checks) == 5

    author_pins = json.loads(frozen_bytes["SOURCE_PINS.json"])
    parent_checks = []
    for source in author_pins["sources"][:2]:
        matches = [row for row in source_pins["sources"]
                   if Path(row["path"]).name == Path(source["path"]).name]
        assert len(matches) == 1
        matched = matches[0]
        assert source["revision"] == matched["revision"]
        assert source["sha256"] == matched["sha256"]
        assert Path(source["path"]) == Path(matched["repository"]) / matched["path"]
        parent_checks.append({"source": source["path"],
                              "sha256": source["sha256"],
                              "matches_verified_PRE_parent": True})
    deferred_pins = [{**row, "read_or_hash_verified_underlying_file": False,
                      "role": "Provisional metadata only; no target-physics judgment"}
                     for row in author_pins["sources"][2:]]

    result_bytes = frozen_bytes["FINITE_REGISTER_CONTROL_RESULTS.json"]
    assert result_bytes == frozen_bytes["CONTROL.stdout.txt"]
    assert frozen_bytes["CONTROL.stderr.txt"] == b""
    result = json.loads(result_bytes)
    execution = json.loads(frozen_bytes["CONTROL_EXECUTION.json"])
    code_hash = digest(frozen_bytes["finite_register_controls.py"])
    assert result["source_sha256"] == execution["script_sha256"] == code_hash
    assert execution["exit_code"] == 0
    assert len(result["waiting_rows"]) == 6
    assert len(result["grid_rows"]) == 5
    assert result["selection_rules"]["legal_append_images_checked"] == 6
    table_checks = []
    with localcontext() as context:
        context.prec = 100
        tolerance = Decimal("1e-72")
        D = Decimal
        target = D(result["waiting_rows"][0]["target_probability"])
        for row in result["waiting_rows"]:
            e = D(row["epsilon"])
            assert D(row["target_probability"]) == target
            difference = abs(D(row["fixed_bin_probability"]) - target)
            assert abs(difference-D(row["fixed_bin_absolute_error"])) < tolerance
            assert D(row["shrinking_bin"]) == e**6
            ratio = D(row["microscopic_CDF_over_kappa_bin"])/(e**4/3)
            assert abs(ratio-D(row["ratio_to_predicted_small_bin_asymptotic"])) < tolerance
            table_checks.append({"waiting_epsilon": row["epsilon"],
                                 "recorded_arithmetic_consistent": True})
        for row in result["grid_rows"]:
            lo, hi, exact = D(row["lower"]), D(row["upper"]), D(row["exact"])
            assert lo <= exact <= hi and exact == target
            assert abs(hi-lo-D(row["sandwich_gap"])) < tolerance
            assert D(row["mesh"])*row["bins"] == D("1.2")
            assert D(row["proved_loose_gap_bound"]) == 8*D(".7")*D(row["mesh"])
            assert hi-lo <= D(row["proved_loose_gap_bound"])
            table_checks.append({"grid_bins": row["bins"],
                                 "recorded_arithmetic_consistent": True})
    for name, data in frozen_bytes.items():
        assert (ROOT / name).read_bytes() == data

    emit(HERE / "POST_SOURCE_PINS.json", {
        "created_utc": start,
        "phase": "Released-source POST",
        "preserved_PRE_seal_sha256": EXPECTED_PRE_SEAL,
        "released_author_files": released,
        "reused_exact_git_sources": origin_checks,
        "provisional_metadata_not_opened": deferred_pins,
        "excluded_actions": ["author code execution", "other active packet read",
                             "publication edit", "audit mutation", "delegation"]})
    check = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Byte bindings and recorded-table arithmetic only; no numerical replication",
        "verifier_sha256": digest(Path(__file__).read_bytes()),
        "PRE_seal_sha256": EXPECTED_PRE_SEAL,
        "PRE_members_unchanged": pre_checks,
        "author_seal_sha256": EXPECTED_AUTHOR_SEAL,
        "author_member_count": len(author_seal["files"]),
        "all_author_member_hashes_match": True,
        "all_released_origins_still_equal_snapshots": True,
        "exact_git_origin_count": len(origin_checks),
        "root_parent_pins": parent_checks,
        "author_execution": execution,
        "author_result_internal_elapsed_seconds": result["elapsed_seconds"],
        "execution_and_result_source_fingerprint": code_hash,
        "stdout_byte_equal_result": True,
        "stderr_bytes": 0,
        "all_six_waiting_and_five_grid_rows_inspected": True,
        "recorded_table_checks": table_checks,
        "author_code_rerun": False,
        "other_provisional_packet_files_opened": False,
        "verification_limitation": "Recorded source/execution/output correspondence; no fresh author run or independent reproduction of numerical values."}
    emit(HERE / "POST_EVIDENCE_CHECK.json", check)
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
