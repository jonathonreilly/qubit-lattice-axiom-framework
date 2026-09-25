"""Read-only source/cache comparison; never imports or runs a scientific runner."""
from pathlib import Path
import ast
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
PACKET = HERE / sys.argv[1]
PUB = PACKET / "publication"
RUNNER = "scripts/original_formation_record_photon_readout_and_microscopic_bins_2026_09_24.py"
RESULT = "outputs/original_record_photon_bridge_20260924/ORIGINAL_RECORD_PHOTON_BRIDGE_RESULTS.json"
CACHE = "logs/runner-cache/original_formation_record_photon_readout_and_microscopic_bins_2026_09_24.txt"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assignments(tree):
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        out[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    return out


def scientific_floats(value, path=""):
    if isinstance(value, float):
        return {path: value}
    out = {}
    if isinstance(value, dict):
        for key, child in value.items():
            if key != "elapsed_seconds":
                out.update(scientific_floats(child, path + "/" + key))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            out.update(scientific_floats(child, path + "/" + str(i)))
    return out


frozen = json.loads((PACKET / "external/ORIGINAL_RECORD_PUBLICATION_FROZEN_SOURCES.json").read_text())
execution = json.loads((PACKET / "external/ORIGINAL_RECORD_PUBLICATION_CACHE_EXECUTION.json").read_text())
root_report = json.loads((PACKET / "external/ORIGINAL_RECORD_PRIMARY_ROOT_VERIFICATION.json").read_text())
checks = []
for rel, expected in frozen["files_sha256"].items():
    actual = sha(PUB / rel)
    assert actual == expected, rel
    checks.append({"path": rel, "sha256": actual, "bytes": (PUB / rel).stat().st_size})
assert sha(PUB / RESULT) == frozen["result"]

source = (PUB / RUNNER).read_text()
tree = ast.parse(source)
literal = assignments(tree)
paths = literal["AUDIT_INPUT_PATHS"]
assert isinstance(paths, (tuple, list)) and len(paths) == len(set(paths))
fingerprint = hashlib.sha256(b"runner-cache-input-fingerprint-v1\0")
for rel in paths:
    assert not Path(rel).is_absolute() and ".." not in Path(rel).parts
    name = rel.encode("utf-8")
    body = (PUB / rel).read_bytes()
    fingerprint.update(len(name).to_bytes(8, "big"))
    fingerprint.update(name)
    fingerprint.update(len(body).to_bytes(8, "big"))
    fingerprint.update(body)

metadata = execution["metadata"]
assert metadata["runner"] == RUNNER and metadata["exit_code"] == 0
assert metadata["status"] == "ok" and metadata["stderr"] == ""
assert metadata["timeout_sec"] == literal["AUDIT_TIMEOUT_SEC"] == 120
stdout = metadata["stdout"]
result_bytes = (PUB / RESULT).read_bytes()
assert stdout.encode() == result_bytes + b"TOTAL_PASS: 7\n"
result = json.loads(result_bytes)
assert result["source_sha256"] == sha(PUB / RUNNER)
assert result["all_assertions_passed"] is True
assert root_report["runner_sha256"] == sha(PUB / RUNNER)
assert root_report["result_sha256"] == sha(PUB / RESULT)
assert root_report["note_sha256"] == sha(PUB / paths[0])
assert root_report["fresh_execution_elapsed_sec"] == metadata["elapsed_sec"]
expected_cache = (
    "===== runner cache v1 =====\n"
    f"runner: {RUNNER}\n"
    f"runner_sha256: {sha(PUB / RUNNER)}\n"
    f"input_fingerprint_sha256: {fingerprint.hexdigest()}\n"
    f"timeout_sec: {metadata['timeout_sec']}\n"
    f"exit_code: {metadata['exit_code']}\n"
    f"elapsed_sec: {metadata['elapsed_sec']:.2f}\n"
    f"status: {metadata['status']}\n"
    f"----- stdout -----\n{stdout}\n"
    "----- stderr -----\n\n"
)
assert (PUB / CACHE).read_bytes() == expected_cache.encode()
assert len(stdout.encode()) < 200000

author_source = (HERE / "post_sources/magnetic_lag_controls.py").read_text()
author_tree = ast.parse(author_source)
author_probe = next(n for n in author_tree.body if isinstance(n, ast.FunctionDef) and n.name == "probe")
public_probe = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "probe")
assert ast.dump(author_probe, include_attributes=False) == ast.dump(public_probe, include_attributes=False)
assert ast.get_source_segment(author_source, author_probe) == ast.get_source_segment(source, public_probe)
assert ("magnetic-lag-photon-personal/magnetic_lag_controls.py", sha(HERE / "post_sources/magnetic_lag_controls.py")) in literal["ROOT_CONTROL_SOURCES"]
author_result = json.loads((HERE / "post_sources/CONTROL_RESULTS.json").read_text())
old_magnetic = {key: author_result[key] for key in ["probes", "cutoff_comparisons"]}
new_magnetic = result["separate_two_component_rotor"]
old_floats, new_floats = scientific_floats(old_magnetic), scientific_floats(new_magnetic)
assert old_floats.keys() == new_floats.keys()
differences = [{"path": path, "author": old_floats[path], "publication": new_floats[path],
                "absolute_difference": abs(old_floats[path] - new_floats[path])}
               for path in old_floats if old_floats[path] != new_floats[path]]
assert all(row["scaled_contrast_cutoff_differences"] and
           max(row["scaled_contrast_cutoff_differences"]) < 2e-9
           for row in new_magnetic["cutoff_comparisons"])
assert abs(new_magnetic["probes"][-1]["rows"][0]["contrast_over_b_g2"] + 1) < .04

rerun_report = None
delta_path = PACKET / "external/ORIGINAL_RECORD_PUBLICATION_RERUN_DELTA.json"
if delta_path.exists():
    previous = json.loads((HERE / "publication_sources/publication" / RESULT).read_text())
    before, after = scientific_floats(previous), scientific_floats(result)
    assert before.keys() == after.keys()
    changes = [{"path": path, "old": before[path], "new": after[path],
                "difference": after[path] - before[path]}
               for path in before if before[path] != after[path]]
    assert changes == json.loads(delta_path.read_text())["changes"]
    assert changes == root_report["changed_numeric_values"]

    def skeleton(value):
        if isinstance(value, float):
            return "FLOAT_VALUE"
        if isinstance(value, dict):
            return {key: skeleton(child) for key, child in value.items()
                    if key != "elapsed_seconds"}
        if isinstance(value, list):
            return [skeleton(child) for child in value]
        return value

    assert skeleton(previous) == skeleton(result)
    residual_checks = []
    for old_row, new_row in zip(previous["separate_two_component_rotor"]["probes"][7]["rows"],
                                new_magnetic["probes"][7]["rows"]):
        delta_contrast = new_row["contrast_over_b_g2"] - old_row["contrast_over_b_g2"]
        delta_boundary = new_row["boundary_contrast_over_g2"] - old_row["boundary_contrast_over_g2"]
        predicted = (delta_contrast - delta_boundary) * .05**2 / new_row["b"]
        observed = new_row["lag_contrast_remainder_over_b2"] - old_row["lag_contrast_remainder_over_b2"]
        assert abs(predicted - observed) < 3e-14
        residual_checks.append({"family": new_row["family"],
                                "predicted_remainder_change": predicted,
                                "observed_remainder_change": observed,
                                "roundoff_difference": abs(predicted - observed)})
    rerun_report = {"all_632_non_timing_float_paths_compared": len(after) == 632,
                    "changed_float_count": len(changes),
                    "unchanged_float_count": len(after) - len(changes),
                    "all_nonfloat_scientific_structure_and_values_exact": True,
                    "all_changes_exactly_match_root_delta": True,
                    "changes": changes,
                    "residual_denominator_arithmetic": residual_checks}

preserved = {}
for name, expected in [
    ("PRE_SEAL.json", "f306d33f15c2345fda844721d94f5d5cf3a1d6b23eca1e3d3b82a021c82fb9fa"),
    ("POST_SEAL.json", "c5cef638e5ece6c1a46dda7cc5a221c9422862a582228fe2a30c47b76aa6ede4")]:
    assert sha(HERE / name) == expected
    members = json.loads((HERE / name).read_text())["members"]
    for member in members:
        path = HERE / member["path"]
        assert sha(path) == member["sha256"] and path.stat().st_size == member["bytes"]
    preserved[name] = {"sha256": expected, "members_unchanged": len(members)}

report = {
    "scope": "Section B magnetic proof source and control adaptation; complete-output mechanical correspondence, not science review of A/C/D.",
    "snapshot_packet": str(PACKET),
    "verifier_sha256": sha(Path(__file__)),
    "source_checks": checks,
    "cache_sha256": sha(PUB / CACHE),
    "result_sha256": sha(PUB / RESULT),
    "declared_input_fingerprint_sha256": fingerprint.hexdigest(),
    "complete_cache_reconstructed_byte_for_byte": True,
    "complete_execution_stdout_equals_result_plus_total": True,
    "fresh_exit_code": metadata["exit_code"],
    "fresh_elapsed_seconds": metadata["elapsed_sec"],
    "fresh_stderr_empty": True,
    "probe_source_and_AST_identical_to_POST_author": True,
    "magnetic_float_count": len(new_floats),
    "magnetic_payload_exactly_equal_to_POST_author": old_magnetic == new_magnetic,
    "magnetic_changed_floats": differences,
    "all_publication_non_timing_float_count": len(scientific_floats(result)),
    "root_whole_packet_comparison_receipt": root_report,
    "fresh_run_delta_independent_bookkeeping": rerun_report,
    "scope_limit": "The receipt's other seven original-function comparisons and nonmagnetic author-payload comparisons are attributed to root; their original packets were not reopened here.",
    "preserved_seals": preserved,
    "new_primary_or_author_executions": 0,
}
print(json.dumps(report, indent=2))
