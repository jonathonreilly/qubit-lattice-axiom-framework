"""Read-only correspondence verifier: no evidence imports, writes or processes."""
from pathlib import Path
from collections import Counter
import ast
import datetime
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent
EXT = PRIOR.parent
PUBLIC = EXT / "formation-response-publication"
PINS_NAME = "SOURCE_PINS_INITIAL.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify_file(path, expected, size=None):
    assert sha(path) == expected, str(path)
    if size is not None:
        assert path.stat().st_size == size, str(path)


def leaves(value, path=""):
    if isinstance(value, dict):
        out = {}
        for key, child in value.items():
            out.update(leaves(child, path + "/" + key))
        return out
    if isinstance(value, list):
        out = {}
        for index, child in enumerate(value):
            out.update(leaves(child, path + "/" + str(index)))
        return out
    return {path: value}


def literal_assignments(source):
    found = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {
                    "AUDIT_TIMEOUT_SEC", "AUDIT_INPUT_PATHS", "OUTPUT_DIRECTORY", "RUNTIME"
                }:
                    found[target.id] = ast.literal_eval(node.value)
    return found


def ast_functions(source):
    return [
        node.name for node in ast.parse(source).body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def author_row_text(rows):
    result = []
    for row in rows:
        q = "".join({-1: "-", 0: "0", 1: "+"}[x] for x in row["charges"])
        result.append({
            "side": row["side"], "word_index": row["word_index"],
            "charge_encoding": q, "B_occupied": row["B_occupied"],
            "exact_response_in_K": row["exact_response_in_K"],
            "second_differences": row["second_differences"],
            "primitive_paths": row["primitive_paths"],
            "resolved_loss_diagonal": row["resolved_loss_diagonal"],
            "coherent_loss_diagonal": row["coherent_loss_diagonal"],
            "flows": row["flows"],
        })
    return result


def main():
    pins = read_json(HERE / PINS_NAME)
    frozen_sources = {}
    observed = []
    for entry in pins["sources"]:
        origin = Path(entry["origin"])
        snapshot = HERE / entry["snapshot"]
        verify_file(snapshot, entry["sha256"], entry["bytes"])
        verify_file(origin, entry["sha256"], entry["bytes"])
        assert str(origin) not in frozen_sources
        frozen_sources[str(origin)] = snapshot
        observed.append({
            "origin": str(origin), "snapshot": entry["snapshot"],
            "sha256": entry["sha256"], "bytes": entry["bytes"],
        })

    def publication(rel):
        return frozen_sources[str(PUBLIC / rel)]

    def external(name):
        return frozen_sources[str(EXT / name)]

    preserved = []
    for name, expected in [
        ("PRE_SEAL.json", "d65cdc1e27cd6757c9437f62cec7c45bfa7a3c850da4c5f2f2fe510983c00dad"),
        ("POST_SEAL.json", "79359f5d5cddd65d799a6eba47aec005a10d2b3f708a32264b263f9df5f0d9db"),
    ]:
        verify_file(PRIOR / name, expected)
        seal = read_json(PRIOR / name)
        for member in seal["members"]:
            verify_file(PRIOR / member["path"], member["sha256"], member["bytes"])
        preserved.append({"seal": name, "sha256": expected, "members": len(seal["members"])})
    assert [row["members"] for row in preserved] == [30, 21]
    prior_pins = read_json(PRIOR / "POST_SOURCE_PINS.json")
    for entry in prior_pins["author39_sources"]:
        verify_file(Path(entry["origin"]), entry["sha256"], entry["bytes"])
        verify_file(PRIOR / entry["snapshot"], entry["sha256"], entry["bytes"])

    manifest = read_json(external("FORMATION_RESPONSE_PUBLICATION_FROZEN_SOURCES.json"))
    verify_file(external("FORMATION_RESPONSE_PUBLICATION_FROZEN_SOURCES.json"),
                "23b2fce537953a8866ee216eaa372346f81265c0004fec800f21699ff2be5455")
    working = read_json(external("FORMATION_RESPONSE_PUBLICATION_WORKING_SOURCES.json"))
    assert {k: v for k, v in manifest.items() if k != "files_sha256"} == working
    for rel, expected in manifest["files_sha256"].items():
        verify_file(publication(rel), expected)
    for rel, expected in manifest["source_files_sha256"].items():
        assert manifest["files_sha256"][rel] == expected

    note = publication(manifest["note"]).read_text()
    old_note_path = PRIOR / "post_sources/author39/FORMATION_AND_WILSON_RESPONSE_BUDGET_ROOT.md"
    verify_file(old_note_path, "229ec44bb80c1450fbba8b45d6a586a489edebd21aab8fc0db9f43ab74401eaa")
    old_note = old_note_path.read_text()
    assert len(manifest["presentation_replacements"]) == 1
    replacement = manifest["presentation_replacements"][0]
    assert old_note.count(replacement["old"]) == 1
    transformed = old_note.replace(replacement["old"], replacement["new"])
    increment = manifest["heading_level_increment"]
    assert increment == 2
    transformed = re.sub(r"^(#{1,6}) ", lambda m: "#" * (len(m[1]) + increment) + " ",
                         transformed, flags=re.M)
    before, body_and_after = note.split("## Complete personal argument\n\n")
    body, after = body_and_after.split("\n## Reproduction, sources and review scope\n\n")
    assert body == transformed
    assert 'each original formation event reduces\na particular aggregate field-response strength by the same amount.' in before
    assert "If the initial number is not definite, (9) remains valid while" in body
    assert "this publication's root response\nproof does not rely on them" in before
    assert "no retained audit status" in before
    assert "No audit verdict or merge is part of this unit" in after
    headings_before = re.findall(r"^(#{1,6}) (.*)$", old_note, re.M)
    headings_after = re.findall(r"^(#{1,6}) (.*)$", body, re.M)
    assert [(len(a) + increment, b) for a, b in headings_before] == [
        (len(a), b) for a, b in headings_after
    ]

    parents = []
    for rel in manifest["parent_paths"]:
        snapshot = PRIOR / "sources" / Path(rel).name
        assert publication(rel).read_bytes() == snapshot.read_bytes()
        entry = next(x for x in prior_pins["permitted_main_parents"] if x["git_path"] == rel)
        verify_file(Path(entry["origin"]), entry["sha256"], entry["bytes"])
        parents.append({"path": rel, "sha256": sha(snapshot), "PRE_identity_unchanged": True})

    runner_path = publication(manifest["runner"])
    runner_source = runner_path.read_text()
    declarations = literal_assignments(runner_source)
    assert declarations["AUDIT_TIMEOUT_SEC"] == 120
    expected_inputs = [manifest["note"], *manifest["parent_paths"], *manifest["runtime"]]
    assert list(declarations["AUDIT_INPUT_PATHS"]) == expected_inputs
    assert len(expected_inputs) == len(set(expected_inputs)) == 5
    assert declarations["OUTPUT_DIRECTORY"] == manifest["output_directory"]
    assert manifest["runtime"] == [declarations["RUNTIME"]]
    runtime_path = publication(declarations["RUNTIME"])
    prior_runtime = PRIOR / "post_sources/author39/response_sum_controls.py"
    assert runtime_path.read_bytes() == prior_runtime.read_bytes()
    assert ast.dump(ast.parse(runtime_path.read_text()), include_attributes=False) == ast.dump(
        ast.parse(prior_runtime.read_text()), include_attributes=False)
    assert ast_functions(runtime_path.read_text()) == [
        "geometry", "gauss", "flow", "electric", "translated", "response", "words", "primitive", "main"
    ]
    assert ast_functions(runner_source) == ["main"]

    fingerprint = hashlib.sha256(b"runner-cache-input-fingerprint-v1\0")
    for rel in declarations["AUDIT_INPUT_PATHS"]:
        parts = Path(rel)
        assert not parts.is_absolute() and ".." not in parts.parts and parts.as_posix() == rel
        component = PUBLIC
        for part in parts.parts:
            component /= part
            assert not component.is_symlink(), str(component)
        rel_bytes = rel.encode()
        raw = publication(rel).read_bytes()
        fingerprint.update(len(rel_bytes).to_bytes(8, "big"))
        fingerprint.update(rel_bytes)
        fingerprint.update(len(raw).to_bytes(8, "big"))
        fingerprint.update(raw)
    input_digest = fingerprint.hexdigest()
    assert input_digest == "ef494681a8970c1327781a6f5d2b5cec59d78666f8a5970f8886d47ce1a85ce9"

    output_dir = manifest["output_directory"]
    artifact_path = publication(output_dir + "/RESPONSE_SUM_RESULTS.json")
    stdout_path = publication(output_dir + "/response_control.stdout.txt")
    stderr_path = publication(output_dir + "/response_control.stderr.txt")
    assert stdout_path.read_bytes() == artifact_path.read_bytes()
    assert stderr_path.read_bytes() == b""
    artifact = read_json(artifact_path)
    original = read_json(PRIOR / "post_sources/author39/RESPONSE_SUM_RESULTS.json")
    left = leaves(original)
    right = leaves(artifact)
    assert left.keys() == right.keys()
    differences = [
        {"path": key, "original": left[key], "fresh": right[key]}
        for key in left if type(left[key]) is not type(right[key]) or left[key] != right[key]
    ]
    assert len(differences) == 1 and differences[0]["path"] == "/elapsed_seconds"
    assert len(left) == 3234
    types = dict(Counter(type(value).__name__ for value in right.values()))
    assert types == {"str": 2, "int": 3227, "bool": 4, "float": 1}
    assert artifact["source_sha256"] == sha(runtime_path)
    assert artifact["all_assertions_passed"] is True
    assert len(artifact["geometry"]) == 3
    assert [g["side"] for g in artifact["geometry"]] == [2, 4, 6]
    assert len(artifact["rows"]) == 75
    assert sum(len(row["flows"]) for row in artifact["rows"]) == 225
    assert artifact["second_difference_checks"] == 13770
    assert artifact["primitive_paths_checked"] == 27344

    wrapper_path = publication(manifest["result"])
    wrapper = read_json(wrapper_path)
    assert wrapper["source_sha256"] == sha(runner_path)
    assert wrapper["runtime_source_sha256"] == sha(runtime_path)
    assert wrapper["exit_code"] == wrapper["stderr_bytes"] == 0
    assert wrapper["stdout_bytes"] == artifact_path.stat().st_size == 69430
    assert wrapper["stdout_sha256"] == sha(artifact_path)
    assert wrapper["complete_scientific_artifact"] == {
        "path": output_dir + "/RESPONSE_SUM_RESULTS.json",
        "sha256": sha(artifact_path), "bytes": artifact_path.stat().st_size
    }
    assert wrapper["all_assertions_passed"] is True
    execution = read_json(external("FORMATION_RESPONSE_PUBLICATION_CACHE_EXECUTION.json"))
    assert execution["status"] == "ok" and execution["exit_code"] == 0
    assert execution["stderr"] == "" and execution["timeout_sec"] == 120
    assert execution["runner"] == manifest["runner"]
    assert execution["stdout"] == wrapper_path.read_text() + "TOTAL_PASS: 1\n"
    assert len(execution["stdout"]) < 200000 and len(execution["stderr"]) < 50000
    assert 0 < artifact["elapsed_seconds"] < wrapper["elapsed_seconds"] < execution["elapsed_sec"]
    expected_cache = (
        "===== runner cache v1 =====\n"
        f"runner: {manifest['runner']}\n"
        f"runner_sha256: {sha(runner_path)}\n"
        f"input_fingerprint_sha256: {input_digest}\n"
        f"timeout_sec: {execution['timeout_sec']}\n"
        f"exit_code: {execution['exit_code']}\n"
        f"elapsed_sec: {execution['elapsed_sec']:.2f}\n"
        f"status: {execution['status']}\n"
        "----- stdout -----\n"
        f"{execution['stdout']}\n"
        "----- stderr -----\n"
        f"{execution['stderr']}\n"
    )
    assert publication(manifest["cache"]).read_text() == expected_cache
    root_check = read_json(external("FORMATION_RESPONSE_PRIMARY_ROOT_VERIFICATION.json"))
    assert root_check["source_body_exact_except_declared_status_and_headings"] is True
    assert root_check["source_files_sha256"] == manifest["source_files_sha256"]
    assert root_check["input_fingerprint_sha256"] == input_digest
    assert root_check["all_leaf_count"] == len(left)
    assert root_check["unchanged_leaf_count"] == len(left) - len(differences)
    assert root_check["leaf_types"] == types
    assert root_check["all_differences"] == differences
    for key, expected in [
        ("complete_geometry_groups", 3), ("complete_charge_rows", 75), ("complete_flow_rows", 225),
        ("second_difference_checks", 13770), ("primitive_paths_checked", 27344),
        ("scientific_artifact_sha256", sha(artifact_path)), ("runner_result_sha256", sha(wrapper_path)),
        ("cache_sha256", sha(publication(manifest["cache"]))),
        ("outer_elapsed_seconds", execution["elapsed_sec"]),
    ]:
        assert root_check[key] == expected, key

    result = {
        "verified_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Released-source publication correspondence only; no scientific program rerun or new blind proof.",
        "sources": observed, "preserved_seals": preserved,
        "preserved_author_origins": len(prior_pins["author39_sources"]),
        "parents": parents,
        "body_correspondence": {
            "author_sha256": sha(old_note_path), "publication_sha256": sha(publication(manifest["note"])),
            "one_status_replacement": replacement, "heading_increment": increment,
            "headings_shifted": len(headings_before), "remaining_body_exact": True,
        },
        "front_finding": {
            "required_wording_qualification": True,
            "reason": "Expected-count identity is unconditional; fixed normalized-history decrement requires definite initial N.",
            "root_acknowledged": True,
            "publication_edited_by_checker": False,
        },
        "runtime_byte_and_AST_identity": True,
        "runtime_functions": ast_functions(runtime_path.read_text()),
        "wrapper_functions": ast_functions(runner_source),
        "declared_inputs": expected_inputs, "input_fingerprint_sha256": input_digest,
        "cache_entire_bytes_reconstructed": True, "cache_truncation": False,
        "leaf_count": len(left), "leaf_types": types, "all_differences": differences,
        "geometry": artifact["geometry"], "complete_scientific_rows": author_row_text(artifact["rows"]),
        "artifact_metadata": {key: value for key, value in artifact.items() if key not in {"rows", "geometry"}},
        "wrapper_result": wrapper,
        "execution": {key: value for key, value in execution.items() if key not in {"stdout", "live_log"}},
        "all_correspondence_assertions_passed": True,
        "scientific_proof_reused_from_unchanged_PRE_POST": True,
        "new_independent_scientific_validation_claimed": False,
        "program_imports_or_execution": False, "file_writes_or_processes": False,
    }
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
