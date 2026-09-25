#!/usr/bin/env python3
"""Read-only correspondence checks; no source imports or scientific execution.

The sole subprocess operation is git show of five explicitly pinned parent
objects. This verifier never writes, imports a runner/helper, or follows source
references beyond its own explicit frozen-origin inventory.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import ast
import difflib
import hashlib
import json
import math
import re
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
PUB = BASE / "microscopic-energy-budget-publication"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(rel):
    return (HERE / "snapshot" / rel).read_bytes()


def obj(rel):
    return json.loads(read(rel))


def leaves(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from leaves(child, path + "/" + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from leaves(child, path + "/" + str(index))
    else:
        yield path, value


def main():
    pins = json.loads((HERE / "SOURCE_PINS.json").read_bytes())
    assert pins["source_snapshot_count"] == len(pins["origins"]) == 168
    for row in pins["origins"]:
        frozen = HERE / row["frozen"]
        assert frozen.resolve().is_relative_to(HERE / "snapshot")
        body = frozen.read_bytes()
        assert sha(body) == row["sha256"] and len(body) == row["bytes"]
        assert Path(row["origin"]).read_bytes() == body
    manifest_name = "MICROSCOPIC_ENERGY_BUDGET_PUBLICATION_FROZEN_SOURCES.json"
    assert sha(read("metadata/" + manifest_name)) == "d8908ec842e1e8e4bf565dd4a9032a00dd19c4c691f4062c2d6be58692c855b9"
    manifest = obj("metadata/" + manifest_name)
    working = obj("metadata/MICROSCOPIC_ENERGY_BUDGET_PUBLICATION_WORKING_SOURCES.json")
    assert all(manifest[key] == value for key, value in working.items())
    assert len(manifest["files_sha256"]) == 13
    for path, expected in manifest["files_sha256"].items():
        assert sha(read("publication/" + path)) == expected

    seal_rows = []
    for row in pins["seals"]:
        seal_name = Path(row["origin"]).name
        seal_data = read(row["label"] + "/" + seal_name)
        assert sha(seal_data) == row["sha256"]
        seal = json.loads(seal_data)
        members = seal.get("members", seal.get("files"))
        if isinstance(members, dict):
            members = [{"path": k, "sha256": v if isinstance(v, str) else v["sha256"]}
                       for k, v in members.items()]
        assert len(members) == row["members"]
        for member in members:
            data = read(row["label"] + "/" + member["path"])
            assert sha(data) == member["sha256"]
            if "bytes" in member:
                assert len(data) == member["bytes"]
        seal_rows.append({"label": row["label"], "seal": seal_name,
                          "sha256": row["sha256"], "members_unchanged": len(members)})

    parent_rows = []
    for path in manifest["parent_paths"]:
        command = ["git", "--no-optional-locks", "-C", str(PUB), "show",
                   manifest["base_revision"] + ":" + path]
        proc = subprocess.run(command, capture_output=True, check=True)
        assert proc.stderr == b""
        assert proc.stdout == read("publication/" + path)
        parent_rows.append({"path": path, "sha256": sha(proc.stdout),
                            "revision": manifest["base_revision"], "exact_git_match": True})

    note = read("publication/" + manifest["note"]).decode()
    marker1 = "\n## Part I — transfer to the full microscopic law\n\n"
    marker2 = "\n## Part II — residence and actual energy supply\n\n"
    marker3 = "\n## Verification and physical boundary\n"
    public_sections = [note.split(marker1)[1].split(marker2)[0],
                       note.split(marker2)[1].split(marker3)[0]]
    transformations = []
    for index, (unit, label, name) in enumerate([
        ("microscopic", "author37", "FULL_MICROSCOPIC_ENERGY_AND_FORMATION_ROOT.md"),
        ("budget", "author38", "NATIVE_GROUND_RESIDENCE_AND_ENERGY_BUDGET_ROOT.md"),
    ]):
        source = read(label + "/" + name).decode()
        replacements = [x for x in manifest["presentation_replacements"] if x["unit"] == unit]
        for change in replacements:
            assert source.count(change["old"]) == 1
            source = source.replace(change["old"], change["new"])
        source = re.sub(r"^(#{1,6}) ", lambda m: "#" * (len(m[1]) + 2) + " ", source, flags=re.M)
        assert public_sections[index] == source
        transformations.append({"unit": unit, "declared_presentation_replacements": len(replacements),
                                "heading_level_increment": 2, "entire_section_exact": True,
                                "public_section_sha256": sha(source.encode())})

    runner_bytes = read("publication/" + manifest["runner"])
    tree = ast.parse(runner_bytes)
    literals = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {"AUDIT_INPUT_PATHS", "AUDIT_TIMEOUT_SEC", "OUTPUT_DIRECTORY", "RUNTIME"}:
                    literals[target.id] = ast.literal_eval(node.value)
    expected_inputs = (manifest["note"], *manifest["parent_paths"], *manifest["runtime"])
    assert literals["AUDIT_INPUT_PATHS"] == expected_inputs and len(expected_inputs) == 7
    assert literals["AUDIT_TIMEOUT_SEC"] == 120
    assert literals["RUNTIME"] == manifest["runtime"][0]
    assert literals["OUTPUT_DIRECTORY"] == manifest["output_directory"]
    fingerprint = hashlib.sha256(b"runner-cache-input-fingerprint-v1\0")
    for rel in expected_inputs:
        path = Path(rel)
        assert not path.is_absolute() and ".." not in path.parts and path.as_posix() == rel
        component = PUB
        for part in path.parts:
            component = component / part
            assert not component.is_symlink()
        body = read("publication/" + rel)
        name = rel.encode()
        fingerprint.update(len(name).to_bytes(8, "big")); fingerprint.update(name)
        fingerprint.update(len(body).to_bytes(8, "big")); fingerprint.update(body)
    input_hash = fingerprint.hexdigest()
    assert input_hash == "27e16141755767214fc57fb35a3cb3d22784e7115b86b0738de6f854265b9a6f"
    runtime = read("publication/" + literals["RUNTIME"])
    assert runtime == read("author37/primitive_spin_energy_controls.py")

    original = obj("author37/SPIN_ENERGY_CONTROL_RESULTS.json")
    scientific_path = manifest["output_directory"] + "/SPIN_ENERGY_CONTROL_RESULTS.json"
    fresh_bytes = read("publication/" + scientific_path)
    fresh = json.loads(fresh_bytes)
    old_leaves, fresh_leaves = dict(leaves(original)), dict(leaves(fresh))
    assert old_leaves.keys() == fresh_leaves.keys()
    differences = [{"path": key, "original": old_leaves[key], "fresh": fresh_leaves[key]}
                   for key in old_leaves
                   if type(old_leaves[key]) is not type(fresh_leaves[key]) or old_leaves[key] != fresh_leaves[key]]
    assert [d["path"] for d in differences] == ["/elapsed_seconds"]
    for key, value in fresh_leaves.items():
        if isinstance(value, float):
            assert math.isfinite(value)
    leaf_counts = dict(Counter(type(v).__name__ for v in old_leaves.values()))
    assert leaf_counts == {"str": 10, "int": 90, "float": 81, "bool": 13}
    groups = {k: len(fresh[k]) for k in ["identity_rows", "spectral_rows", "integer_rows"]}
    assert groups == {"identity_rows": 6, "spectral_rows": 4, "integer_rows": 4}
    scientific_leaves = sum(len(dict(leaves(fresh[k]))) for k in groups)
    assert scientific_leaves == 190
    assert fresh["source_sha256"] == sha(runtime)
    assert read("author37/SPIN_ENERGY_CONTROL_RESULTS.json") == read("author37/CONTROL_ATTEMPT02.stdout")
    assert read("publication/" + manifest["output_directory"] + "/microscopic_control.stdout.txt") == fresh_bytes
    assert read("publication/" + manifest["output_directory"] + "/microscopic_control.stderr.txt") == b""

    old_source = read("author37/history/attempt01/primitive_spin_energy_controls.py").decode()
    final_source = runtime.decode()
    source_diff = "".join(difflib.unified_diff(old_source.splitlines(keepends=True), final_source.splitlines(keepends=True),
                                            fromfile="attempt01", tofile="attempt02"))
    assert source_diff == read("author37/history/attempt01/REPAIR.diff").decode()
    function_map = lambda text: {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(text).body
                                 if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    before_functions, after_functions = function_map(old_source), function_map(final_source)
    assert before_functions.keys() == after_functions.keys()
    changed_functions = [name for name in before_functions if before_functions[name] != after_functions[name]]
    assert changed_functions == ["build"]
    assert read("author37/CONTROL_ATTEMPT01.stdout") == b""
    assert obj("author37/EXECUTION_ATTEMPT01.json")["exit_code"] == 1
    assert obj("author37/EXECUTION_ATTEMPT02.json")["exit_code"] == 0
    assert read("author37/CONTROL_ATTEMPT02.stderr") == b""

    numeric_checks = []
    for row in fresh["identity_rows"]:
        assert row["coefficient_identity_max_abs"] < 3e-12
        assert row["second_order_identity_max_abs"] < 3e-14
        assert row["resolved_coherent_loss_max_abs"] < 1e-12
        if row["spin"] == 1:
            assert all(row[k] == 0 for k in ["coefficient_identity_max_abs", "second_order_identity_max_abs", "resolved_coherent_loss_max_abs"])
        assert row["rotor_boundary_paths_retained"] > 0
        numeric_checks.append({"cycle": row["cycle_length"], "spin": row["spin"],
                               "dimension": row["full_dimension"], "coefficient_residual": row["coefficient_identity_max_abs"],
                               "loss_residual": row["resolved_coherent_loss_max_abs"]})
    for row in fresh["spectral_rows"]:
        c = row["spin"] * (row["spin"] + 1)
        assert math.isclose(row["epsilon"] ** 2 * c, .01, rel_tol=1e-14)
        assert math.isclose(row["bare_P_energy"], 400*c, rel_tol=1e-14)
        assert row["bare_P_intensity"] == 0
        assert math.isclose(row["low_block_remainder_norm"] / row["epsilon"]**2,
                            row["remainder_over_epsilon_squared"], rel_tol=1e-14)
        assert math.isclose(row["microscopic_jump_amplitude_error"] / row["epsilon"],
                            row["jump_error_over_epsilon"], rel_tol=1e-14)

    execution = obj("metadata/MICROSCOPIC_ENERGY_BUDGET_PUBLICATION_CACHE_EXECUTION.json")
    result_bytes = read("publication/" + manifest["result"])
    result = json.loads(result_bytes)
    assert result["source_sha256"] == sha(runner_bytes)
    assert result["runtime_source_sha256"] == sha(runtime)
    assert result["stdout_sha256"] == sha(fresh_bytes) and result["stdout_bytes"] == len(fresh_bytes)
    assert result["complete_scientific_artifact"] == {"path": scientific_path, "sha256": sha(fresh_bytes), "bytes": len(fresh_bytes)}
    assert result["exit_code"] == result["stderr_bytes"] == 0
    assert execution["runner"] == manifest["runner"] and execution["status"] == "ok"
    assert execution["exit_code"] == 0 and execution["stderr"] == ""
    assert execution["stdout"] == result_bytes.decode() + "TOTAL_PASS: 1\n"
    expected_cache = (
        "===== runner cache v1 =====\n" + "runner: " + manifest["runner"] + "\n"
        + "runner_sha256: " + sha(runner_bytes) + "\n"
        + "input_fingerprint_sha256: " + input_hash + "\n"
        + f"timeout_sec: {execution['timeout_sec']}\nexit_code: {execution['exit_code']}\n"
        + f"elapsed_sec: {execution['elapsed_sec']:.2f}\nstatus: {execution['status']}\n"
        + "----- stdout -----\n" + execution["stdout"][-200000:] + "\n"
        + "----- stderr -----\n" + execution["stderr"][-50000:] + "\n")
    assert expected_cache.encode() == read("publication/" + manifest["cache"])
    receipt = obj("metadata/MICROSCOPIC_ENERGY_BUDGET_PRIMARY_ROOT_VERIFICATION.json")
    assert receipt["leaf_counts"] == leaf_counts and receipt["all_differences"] == differences
    assert receipt["input_fingerprint_sha256"] == input_hash
    assert receipt["complete_scientific_artifact_sha256"] == sha(fresh_bytes)
    assert receipt["complete_result_groups"] == groups

    print(json.dumps({
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Read-only source, stored-payload and cache correspondence; no scientific rerun or new independent proof.",
        "snapshot_count": 168, "all_snapshots_equal_live_origins": True,
        "canonical_manifest_members": 13, "all_canonical_hashes_match": True,
        "seals": seal_rows, "parent_git_bindings": parent_rows,
        "section_correspondence": transformations,
        "runtime_exact_author_bytes": True, "runtime_sha256": sha(runtime),
        "input_count": 7, "input_fingerprint_sha256": input_hash,
        "runner_sha256": sha(runner_bytes), "helper_sha256": sha(read("tooling/runner_cache.py")),
        "complete_group_counts": groups, "total_leaf_counts": leaf_counts,
        "scientific_group_leaves_exactly_unchanged": scientific_leaves,
        "total_leaves": len(old_leaves), "unchanged_leaves": len(old_leaves)-len(differences),
        "all_payload_differences": differences, "numeric_identity_rows": numeric_checks,
        "failed_attempt_preserved": True, "repair_diff_exact": True,
        "changed_original_functions": changed_functions,
        "max_coefficient_residual": max(r["coefficient_identity_max_abs"] for r in fresh["identity_rows"]),
        "max_ground_residual": max(r["ground_residual_norm"] for r in fresh["spectral_rows"]),
        "source_result_stdout_cache_binding_exact": True,
        "result_sha256": sha(result_bytes), "scientific_artifact_sha256": sha(fresh_bytes),
        "cache_sha256": sha(read("publication/" + manifest["cache"])),
        "timers": {"original_inner": original["elapsed_seconds"], "fresh_inner": fresh["elapsed_seconds"],
                   "fresh_wrapper": result["elapsed_seconds"], "outer_execution": execution["elapsed_sec"]},
        "original_writer_or_scientific_program_executions": [], "file_writes": [],
        "all_requested_checks": True,
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
