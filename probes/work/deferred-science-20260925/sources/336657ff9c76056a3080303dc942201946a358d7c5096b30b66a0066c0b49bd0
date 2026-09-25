"""Focused generation2 correspondence; reads and prints only."""
from pathlib import Path
from collections import Counter
import ast
import datetime
import hashlib
import json

D = Path(__file__).resolve().parent
I = D.parent
G1 = I / "publication_comparison"
E = I.parent
P = E / "formation-response-publication"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def flat(value, path=""):
    if isinstance(value, dict):
        return {k: v for a, b in value.items() for k, v in flat(b, path + "/" + a).items()}
    if isinstance(value, list):
        return {k: v for a, b in enumerate(value) for k, v in flat(b, path + "/" + str(a)).items()}
    return {path: value}


def differences(old, new):
    a, b = flat(old), flat(new)
    assert a.keys() == b.keys()
    return [
        {"path": k, "old": a[k], "new": b[k]}
        for k in a if type(a[k]) is not type(b[k]) or a[k] != b[k]
    ]


def main():
    pins = read(D / "SOURCE_PINS_INITIAL.json")
    paths = {}
    for item in pins["sources"]:
        live, snapshot = Path(item["origin"]), D / item["snapshot"]
        for path in (live, snapshot):
            assert sha(path) == item["sha256"]
            assert path.stat().st_size == item["bytes"]
        paths[str(live)] = snapshot

    def public(rel):
        return paths[str(P / rel)]

    def external(name):
        return paths[str(E / name)]

    for item in pins["prior_seals"]:
        seal_path = Path(item["origin"])
        assert sha(seal_path) == item["sha256"]
        seal = read(seal_path)
        assert len(seal["members"]) == item["members"]
        for member in seal["members"]:
            path = seal_path.parent / member["path"]
            assert sha(path) == member["sha256"]
            assert path.stat().st_size == member["bytes"]
    assert sum(item["members"] for item in pins["prior_seals"]) == 91

    manifest = read(external("FORMATION_RESPONSE_GENERATION2_FROZEN_SOURCES.json"))
    old_manifest_path = G1 / "sources_initial/external/FORMATION_RESPONSE_PUBLICATION_FROZEN_SOURCES.json"
    old_manifest = read(old_manifest_path)
    assert manifest["generation"] == 2
    assert manifest["previous_manifest_sha256"] == sha(old_manifest_path)
    for rel, expected in manifest["files_sha256"].items():
        assert sha(public(rel)) == expected
    for rel, expected in manifest["source_files_sha256"].items():
        assert manifest["files_sha256"][rel] == expected
    unchanged_metadata = set(old_manifest) - {"source_files_sha256", "files_sha256"}
    assert all(manifest[k] == old_manifest[k] for k in unchanged_metadata)
    replacement = read(G1 / "REQUIRED_FRONT_REPLACEMENT.json")
    assert manifest["front_qualification"] == replacement
    old_note = G1 / "sources_initial/publication" / manifest["note"]
    new_note = public(manifest["note"])
    assert sha(old_note) == replacement["publication_sha256"]
    assert old_note.read_text().count(replacement["old"]) == 1
    assert old_note.read_text().replace(replacement["old"], replacement["new"]) == new_note.read_text()
    assert sha(new_note) == "fb7e648244754b469504f08aa4cd251148d3736740af4f55c7e5c63675c23d14"
    assert replacement["old"] not in new_note.read_text()
    assert new_note.read_text().count(replacement["new"]) == 1
    body_start = "## Complete personal argument\n\n"
    assert old_note.read_text().split(body_start)[1] == new_note.read_text().split(body_start)[1]
    source_changes = [rel for rel in manifest["source_files_sha256"]
                      if manifest["source_files_sha256"][rel] != old_manifest["source_files_sha256"][rel]]
    assert source_changes == [manifest["note"]]
    unchanged_source_paths = [rel for rel in manifest["source_files_sha256"] if rel != manifest["note"]]
    for rel in unchanged_source_paths:
        assert public(rel).read_bytes() == (G1 / "sources_initial/publication" / rel).read_bytes()

    repair = read(external("FORMATION_RESPONSE_GENERATION2_REPAIR.json"))
    assert repair["exact_replacement"] == replacement
    assert repair["old_note_sha256"] == sha(old_note)
    assert repair["new_note_sha256"] == sha(new_note)
    assert repair["prior_report_unchanged"] is True
    root_review_path = external("FORMATION_RESPONSE_GENERATION1_ROOT_REVIEW.json")
    assert repair["root_prior_review_sha256"] == sha(root_review_path)
    root_review = read(root_review_path)
    assert root_review["report_sha256"] == sha(G1 / "PUBLICATION_COMPARISON.md")
    assert root_review["seal_sha256"] == sha(G1 / "PUBLICATION_COMPARISON_SEAL.json")
    assert root_review["verifier_sha256"] == sha(G1 / "verify_publication_readonly.py")
    assert root_review["required_repair"] == replacement
    assert root_review["exit_code"] == root_review["stderr_bytes"] == 0
    assert root_review["full_output_exact_except_verified_utc"] is True
    old_report = read(G1 / "verification_attempt01/VERIFICATION_REPORT.json")
    root_report = read(external("FORMATION_RESPONSE_GENERATION1_ROOT_READONLY_RESULT.json"))
    root_report_delta = differences(old_report, root_report)
    assert len(root_report_delta) == 1 and root_report_delta[0]["path"] == "/verified_utc"

    wrapper = public(manifest["runner"])
    assigned = {}
    for node in ast.parse(wrapper.read_text()).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {
                    "AUDIT_INPUT_PATHS", "AUDIT_TIMEOUT_SEC", "RUNTIME", "OUTPUT_DIRECTORY"
                }:
                    assigned[target.id] = ast.literal_eval(node.value)
    declared = assigned["AUDIT_INPUT_PATHS"]
    assert list(declared) == [manifest["note"], *manifest["parent_paths"], *manifest["runtime"]]
    assert len(declared) == len(set(declared)) == 5
    assert assigned["AUDIT_TIMEOUT_SEC"] == 120
    assert assigned["OUTPUT_DIRECTORY"] == manifest["output_directory"]
    assert manifest["runtime"] == [assigned["RUNTIME"]]
    runtime = public(assigned["RUNTIME"])
    old_runtime = G1 / "sources_initial/publication" / assigned["RUNTIME"]
    assert runtime.read_bytes() == old_runtime.read_bytes()
    runtime_functions = [n.name for n in ast.parse(runtime.read_text()).body if isinstance(n, ast.FunctionDef)]
    assert len(runtime_functions) == 9

    fingerprint = hashlib.sha256(b"runner-cache-input-fingerprint-v1\0")
    for rel in declared:
        path = Path(rel)
        assert not path.is_absolute() and ".." not in path.parts and path.as_posix() == rel
        component = P
        for part in path.parts:
            component /= part
            assert not component.is_symlink()
        encoded, content = rel.encode(), public(rel).read_bytes()
        fingerprint.update(len(encoded).to_bytes(8, "big"))
        fingerprint.update(encoded)
        fingerprint.update(len(content).to_bytes(8, "big"))
        fingerprint.update(content)
    fingerprint = fingerprint.hexdigest()
    assert fingerprint == "d924c8c02ab999ab05e2f8cf16d264d5369008911ed0787492144731300c64a1"
    assert fingerprint != old_report["input_fingerprint_sha256"]

    out = manifest["output_directory"]
    artifact_path = public(out + "/RESPONSE_SUM_RESULTS.json")
    artifact = read(artifact_path)
    old_artifact = read(G1 / "sources_initial/publication" / out / "RESPONSE_SUM_RESULTS.json")
    original = read(I / "post_sources/author39/RESPONSE_SUM_RESULTS.json")
    diff_original = differences(original, artifact)
    diff_generation1 = differences(old_artifact, artifact)
    for delta in (diff_original, diff_generation1):
        assert len(delta) == 1 and delta[0]["path"] == "/elapsed_seconds"
    assert len(flat(artifact)) == 3234
    types = dict(Counter(type(v).__name__ for v in flat(artifact).values()))
    assert types == {"str": 2, "int": 3227, "bool": 4, "float": 1}
    assert artifact["source_sha256"] == sha(runtime)
    assert len(artifact["geometry"]) == 3 and len(artifact["rows"]) == 75
    assert sum(len(row["flows"]) for row in artifact["rows"]) == 225
    assert artifact["second_difference_checks"] == 13770
    assert artifact["primitive_paths_checked"] == 27344
    assert artifact["all_assertions_passed"] is True
    assert public(out + "/response_control.stdout.txt").read_bytes() == artifact_path.read_bytes()
    assert public(out + "/response_control.stderr.txt").read_bytes() == b""

    result_path = public(manifest["result"])
    result = read(result_path)
    assert result["source_sha256"] == sha(wrapper)
    assert result["runtime_source_sha256"] == sha(runtime)
    assert result["exit_code"] == result["stderr_bytes"] == 0
    assert result["stdout_bytes"] == artifact_path.stat().st_size == 69430
    assert result["stdout_sha256"] == sha(artifact_path)
    assert result["complete_scientific_artifact"] == {
        "path": out + "/RESPONSE_SUM_RESULTS.json", "sha256": sha(artifact_path), "bytes": 69430
    }
    assert result["all_assertions_passed"] is True
    old_result = read(G1 / "sources_initial/publication" / manifest["result"])
    wrapper_delta = differences(old_result, result)
    assert {d["path"] for d in wrapper_delta} == {
        "/elapsed_seconds", "/stdout_sha256", "/complete_scientific_artifact/sha256"
    }
    execution = read(external("FORMATION_RESPONSE_GENERATION2_CACHE_EXECUTION.json"))
    assert execution["runner"] == manifest["runner"]
    assert execution["status"] == "ok" and execution["exit_code"] == 0
    assert execution["timeout_sec"] == 120 and execution["stderr"] == ""
    assert execution["stdout"] == result_path.read_text() + "TOTAL_PASS: 1\n"
    assert 0 < artifact["elapsed_seconds"] < result["elapsed_seconds"] < execution["elapsed_sec"]
    cache_expected = (
        "===== runner cache v1 =====\n"
        f"runner: {manifest['runner']}\nrunner_sha256: {sha(wrapper)}\n"
        f"input_fingerprint_sha256: {fingerprint}\ntimeout_sec: 120\nexit_code: 0\n"
        f"elapsed_sec: {execution['elapsed_sec']:.2f}\nstatus: ok\n"
        f"----- stdout -----\n{execution['stdout']}\n----- stderr -----\n\n"
    )
    assert public(manifest["cache"]).read_text() == cache_expected
    assert len(execution["stdout"]) < 200000
    root_primary = read(external("FORMATION_RESPONSE_GENERATION2_PRIMARY_ROOT_VERIFICATION.json"))
    expected_diff = [{"path": x["path"], "original": x["old"], "fresh": x["new"]} for x in diff_original]
    assert root_primary["all_differences"] == expected_diff
    assert root_primary["all_leaf_count"] == 3234 and root_primary["unchanged_leaf_count"] == 3233
    assert root_primary["leaf_types"] == types
    assert root_primary["source_files_sha256"] == manifest["source_files_sha256"]
    assert root_primary["input_fingerprint_sha256"] == fingerprint
    assert root_primary["repair"] == replacement
    for key, value in [
        ("scientific_artifact_sha256", sha(artifact_path)), ("runner_result_sha256", sha(result_path)),
        ("cache_sha256", sha(public(manifest["cache"]))), ("outer_elapsed_seconds", execution["elapsed_sec"]),
        ("complete_geometry_groups", 3), ("complete_charge_rows", 75), ("complete_flow_rows", 225),
        ("second_difference_checks", 13770), ("primitive_paths_checked", 27344),
        ("no_other_note_change", True), ("runtime_and_wrapper_unchanged", True),
    ]:
        assert type(root_primary[key]) is type(value) and root_primary[key] == value
    changed_files = [rel for rel in manifest["files_sha256"]
                     if manifest["files_sha256"][rel] != old_manifest["files_sha256"][rel]]
    assert set(changed_files) == {
        manifest["note"], manifest["result"], manifest["cache"],
        out + "/RESPONSE_SUM_RESULTS.json", out + "/response_control.stdout.txt"
    }
    scientific = {k: v for k, v in artifact.items() if k != "elapsed_seconds"}
    scientific_digest = hashlib.sha256(json.dumps(
        scientific, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()).hexdigest()
    report = {
        "verified_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Focused generation2 repair and source/payload/cache binding; unchanged proof review reused.",
        "sources": pins["sources"], "prior_seals": pins["prior_seals"],
        "all_91_prior_members_unchanged": True,
        "sole_note_change_exactly_requested": True,
        "old_note_sha256": sha(old_note), "new_note_sha256": sha(new_note),
        "required_generation1_wording_repair_resolved": True,
        "new_required_repairs": 0, "unchanged_source_paths": unchanged_source_paths,
        "unchanged_runtime_functions": runtime_functions,
        "changed_public_files": changed_files,
        "root_generation1_result_differences": root_report_delta,
        "generation1_root_review_sha256": sha(root_review_path),
        "leaf_count": 3234, "equal_nonruntime_leaves": 3233, "leaf_types": types,
        "artifact_differences_from_original": diff_original,
        "artifact_differences_from_generation1": diff_generation1,
        "wrapper_differences_from_generation1": wrapper_delta,
        "scientific_payload_without_timer_canonical_sha256": scientific_digest,
        "complete_geometry_groups": 3, "complete_charge_rows": 75, "complete_flow_rows": 225,
        "second_difference_checks": 13770, "primitive_paths_checked": 27344,
        "declared_input_fingerprint": fingerprint,
        "full_cache_reconstructed": True, "truncated_cache": False,
        "complete_wrapper_result": result,
        "execution_receipt": {k: v for k, v in execution.items() if k not in {"stdout", "live_log"}},
        "replacement_metadata_interpretation": "applied_in_this_packet:false is retained verbatim inside the historical generation1 requested replacement, not used as generation2 application status; exact bytes prove application.",
        "no_evidence_program_import_or_execution": True,
        "no_writes_or_process_spawns": True,
        "all_correspondence_assertions_passed": True,
    }
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
