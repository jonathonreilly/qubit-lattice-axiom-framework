"""Mechanical Part A correspondence only; never executes an author program.

Combined JSON/cache are parsed in memory for hashes and selected fields. Only
Part A payloads and shared execution metadata are written or displayed.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import collections
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUB = BASE / "input-energy-power-publication"
DEST = HERE / "publication_frozen"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(path.read_bytes())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def read_json(path):
    return json.loads(path.read_text())


def verify_seal(directory, seal_name, expected):
    path = directory / seal_name
    assert digest(path) == expected
    seal = read_json(path)
    for member in seal["members"]:
        source = directory / member["path"]
        assert digest(source) == member["sha256"]
        assert source.stat().st_size == member["bytes"]
    return {"directory": str(directory), "seal": seal_name, "sha256": expected,
            "sealed_utc": seal["sealed_utc"], "members_verified": len(seal["members"])}


def compare(a, b, pointer="", differences=None, leaves=None):
    differences = [] if differences is None else differences
    leaves = collections.Counter() if leaves is None else leaves
    assert type(a) is type(b), (pointer, type(a).__name__, type(b).__name__)
    if isinstance(a, dict):
        assert a.keys() == b.keys(), pointer
        for key in a:
            compare(a[key], b[key], pointer + "/" + key, differences, leaves)
    elif isinstance(a, list):
        assert len(a) == len(b), pointer
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, pointer + "/" + str(i), differences, leaves)
    else:
        leaves[type(a).__name__] += 1
        if a != b:
            differences.append({"path": pointer, "author": a, "publication": b})
    return differences, leaves


def main():
    DEST.mkdir(exist_ok=True)
    old_seals = [
        verify_seal(HERE, "PRE_SEAL.json", "6dfea4b57bd88c1f127e385fa2c11294df50956079f748b48952fbf0b7965c43"),
        verify_seal(HERE, "POST_SEAL.json", "d3bad97dce3041c388754944d1b051aaf84148e6c5b26d16cf5ca423ffa83b80"),
        verify_seal(BASE / "number-offset-observation-independent", "PRE_SEAL.json",
                    "75b6df3f1a085d3f921f9480a633e726c09230d9b027b62bc3e48b3a2898cdef"),
    ]
    frozen_path = BASE / "INPUT_ENERGY_POWER_PUBLICATION_FROZEN_SOURCES.json"
    assert digest(frozen_path) == "7c85aea8ef43782ef1a8e6dea959c8ffd2e74112f9c11be825210c0ff6bd7e76"
    frozen = read_json(frozen_path)
    (DEST / frozen_path.name).write_bytes(frozen_path.read_bytes())
    sources = [{"path": str(frozen_path), "sha256": digest(frozen_path),
                "bytes": frozen_path.stat().st_size, "frozen_path": str((DEST / frozen_path.name).relative_to(HERE)),
                "scope": "Shared source metadata; out-of-scope entries are metadata only."}]
    note_path = PUB / frozen["note"]
    note_data = note_path.read_bytes()
    assert sha(note_data) == "9658836c90ceead6363e4cf91e6cdf2039be4e3587c009dae2447ae79026ad34"
    lines = note_data.decode().splitlines(keepends=True)
    assert lines[53].startswith("## A.") and lines[307].startswith("## B.") and lines[522].startswith("## C.")
    scoped = "".join(lines[:307]) + "\n[Part B scientific body omitted by review scope.]\n\n" + "".join(lines[522:])
    scoped_path = DEST / "PUBLIC_NOTE_PART_A_AND_SHARED_CONTEXT.md"
    scoped_path.write_text(scoped)
    sources.append({"path": str(note_path), "sha256": sha(note_data), "bytes": len(note_data),
                    "frozen_path": str(scoped_path.relative_to(HERE)), "frozen_sha256": digest(scoped_path),
                    "scope": "Original lines 1-307 and 523-end only; whole-file hash is a mechanical identity, not Part B science coverage."})
    part_a = "".join(lines[55:307])
    prior = (HERE / "post_frozen_author/ADDED_REFERENCE_EXCITATION_ACTUAL_ENERGY_ROOT.md").read_text()
    diff = "".join(difflib.unified_diff(prior.splitlines(keepends=True), part_a.splitlines(keepends=True),
                                       fromfile="sealed_author_note", tofile="public_Part_A"))
    (DEST / "PART_A_AUTHOR_TO_PUBLIC.diff").write_text(diff)

    runtime_rows = []
    for origin in frozen["origins"]:
        if "/runtime/energy/" not in origin["publication"]:
            continue
        source = PUB / origin["publication"]
        old = HERE / "post_frozen_author" / source.name
        data = source.read_bytes()
        assert sha(data) == origin["sha256"] == digest(old)
        assert data == old.read_bytes()
        public_ast = ast.dump(ast.parse(data), include_attributes=False)
        assert public_ast == ast.dump(ast.parse(old.read_bytes()), include_attributes=False)
        target = DEST / "runtime_energy" / source.name
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(data)
        runtime_rows.append({"program": source.name, "sha256": sha(data), "bytes": len(data),
                             "byte_identical_to_POST": True, "AST_identical_to_POST": True,
                             "functions": [node.name for node in ast.parse(data).body
                                           if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]})
        sources.append({"path": str(source), "sha256": sha(data), "bytes": len(data),
                        "frozen_path": str(target.relative_to(HERE)), "scope": "Part A runtime; exact disclosed author copy."})
    assert len(runtime_rows) == 2
    runner_path = PUB / frozen["runner"]
    runner_data = runner_path.read_bytes()
    assert sha(runner_data) == "30bcc516487bd268c089793b675cf4a39932e03f8fd2b3afc80183f711af5799"
    (DEST / runner_path.name).write_bytes(runner_data)
    sources.append({"path": str(runner_path), "sha256": sha(runner_data), "bytes": len(runner_data),
                    "frozen_path": str((DEST / runner_path.name).relative_to(HERE)),
                    "scope": "Shared wrapper only; no Part B runtime body read."})
    result_path = PUB / frozen["result"]
    result_data = result_path.read_bytes()
    assert sha(result_data) == "8301e6c5263d2842e1d129b1f30357c659a05fec09a6f11924ab4ec5d0256632"
    result = json.loads(result_data)
    assert result["source_sha256"] == sha(runner_data)
    part_a_names = ("ENERGY_POLYNOMIAL_RESULTS.json", "ENERGY_SPECTRAL_RESULTS.json")
    stages = [stage for stage in result["stages"] if stage["result"] in part_a_names]
    assert len(stages) == 2
    comparisons = []
    for name in part_a_names:
        old_data = (HERE / "post_frozen_author" / name).read_bytes()
        old = json.loads(old_data)
        fresh = result["payload"][name]
        differences, leaves = compare(old, fresh)
        allowed = {"/elapsed_seconds"}
        if name == "ENERGY_SPECTRAL_RESULTS.json":
            allowed.add("/source_sha256")
        assert {row["path"] for row in differences} <= allowed, differences
        stage = next(row for row in stages if row["result"] == name)
        assert stage["exit_code"] == stage["stderr_bytes"] == 0
        stdout = (json.dumps(fresh, indent=2) + "\n").encode()
        assert sha(stdout) == stage["stdout_sha256"]
        assert len(stdout) == stage["stdout_bytes"]
        assert stage["code_sha256"] == next(row["sha256"] for row in runtime_rows if row["program"] == stage["program"])
        target = DEST / name
        target.write_bytes(stdout)
        comparisons.append({"result": name, "author_sha256": sha(old_data),
                            "fresh_stdout_sha256": sha(stdout), "all_scientific_leaves_equal": True,
                            "leaf_counts": dict(leaves), "metadata_differences": differences, "fresh_stage": stage})
    assert result["payload"]["ENERGY_SPECTRAL_RESULTS.json"]["source_sha256"] == stages[0]["stdout_sha256"]
    part_a_result = {"scope": "Part A extracted payloads and shared execution metadata only.",
                     "payload": {name: result["payload"][name] for name in part_a_names},
                     "stages": stages, "runner_sha256": result["source_sha256"],
                     "combined_elapsed_seconds": result["elapsed_seconds"]}
    write_json(DEST / "PART_A_RESULT_EXTRACT.json", part_a_result)
    sources.append({"path": str(result_path), "sha256": sha(result_data), "bytes": len(result_data),
                    "frozen_path": str((DEST / "PART_A_RESULT_EXTRACT.json").relative_to(HERE)),
                    "frozen_sha256": digest(DEST / "PART_A_RESULT_EXTRACT.json"),
                    "scope": "Only two energy payloads extracted; combined digest is mechanical identity only."})

    execution_path = BASE / "INPUT_ENERGY_POWER_PUBLICATION_CACHE_EXECUTION.json"
    execution_data = execution_path.read_bytes()
    execution = json.loads(execution_data)
    info = execution["result"]
    assert info["exit_code"] == 0 and info["stderr"] == ""
    expected_stdout = result_data.decode() + "TOTAL_PASS: 5\n"
    assert info["stdout"] == expected_stdout
    cache_path = Path(execution["cache_path"])
    cache_data = cache_path.read_bytes()
    assert sha(cache_data) == "e2b4b63baf8443841d70afa3a92024402e6a3260414c6dd760a39de0b3a720fd"
    cache = cache_data.decode()
    head, tail = cache.split("----- stdout -----\n", 1)
    # The runner cache is allowed to keep only a suffix of large stdout.
    cache_stdout, cache_stderr = tail.split("----- stderr -----\n", 1)
    suffix = info["stdout"].endswith(cache_stdout)
    if not suffix and cache_stdout.endswith("\n"):
        suffix = info["stdout"].endswith(cache_stdout[:-1])
    assert suffix
    assert not cache_stderr.strip()
    header = {}
    for line in head.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            header[key] = value
    assert header["runner_sha256"] == sha(runner_data)
    assert header["runner"] == frozen["runner"] and header["exit_code"] == "0" and header["status"] == "ok"
    (DEST / "CACHE_HEADER_ONLY.txt").write_text(head)
    scoped_execution = {
        "started_utc": execution["started_utc"], "cache_path": str(cache_path),
        "cache_status": execution["cache_status"],
        "execution_metadata": {key: value for key, value in info.items() if key not in {"stdout", "stderr"}},
        "stderr_bytes": len(info["stderr"].encode()),
        "combined_stdout_sha256": sha(info["stdout"].encode()),
        "combined_stdout_bytes": len(info["stdout"].encode()),
        "combined_stdout_equals_result_plus_summary": True,
        "Part_A_stage_rows": stages,
        "cache_header": header,
        "cache_stdout_bytes": len(cache_stdout.encode()),
        "cache_stdout_is_complete": cache_stdout == info["stdout"],
        "cache_stdout_is_verified_suffix": suffix,
        "cache_stderr_bytes": len(cache_stderr.encode()),
        "scope": "No combined stdout body copied into this scoped evidence."
    }
    write_json(DEST / "EXECUTION_PART_A_AND_SHARED_METADATA.json", scoped_execution)
    sources.extend([
        {"path": str(execution_path), "sha256": sha(execution_data), "bytes": len(execution_data),
         "frozen_path": str((DEST / "EXECUTION_PART_A_AND_SHARED_METADATA.json").relative_to(HERE)),
         "frozen_sha256": digest(DEST / "EXECUTION_PART_A_AND_SHARED_METADATA.json"),
         "scope": "Shared execution metadata, equality check and Part A stage rows only; embedded combined stdout not copied."},
        {"path": str(cache_path), "sha256": sha(cache_data), "bytes": len(cache_data),
         "frozen_path": str((DEST / "CACHE_HEADER_ONLY.txt").relative_to(HERE)),
         "frozen_sha256": digest(DEST / "CACHE_HEADER_ONLY.txt"),
         "scope": "Header extraction and opaque suffix verification only; cache stdout body not copied."}
    ])
    root_receipt_path = BASE / "INPUT_ENERGY_POWER_PRIMARY_ROOT_VERIFICATION.json"
    root_receipt_data = root_receipt_path.read_bytes()
    root_receipt = json.loads(root_receipt_data)
    scoped_root_receipt = {key: value for key, value in root_receipt.items() if key not in {"rows", "leaf_counts"}}
    scoped_root_receipt["rows"] = [row for row in root_receipt["rows"] if row["result"] in part_a_names]
    scoped_root_receipt["reviewer_scope_note"] = "Root process receipt only. Global assertions are not a Part B independent validation."
    write_json(DEST / "ROOT_VERIFICATION_PART_A_AND_SHARED_METADATA.json", scoped_root_receipt)
    sources.append({"path": str(root_receipt_path), "sha256": sha(root_receipt_data), "bytes": len(root_receipt_data),
                    "frozen_path": str((DEST / "ROOT_VERIFICATION_PART_A_AND_SHARED_METADATA.json").relative_to(HERE)),
                    "frozen_sha256": digest(DEST / "ROOT_VERIFICATION_PART_A_AND_SHARED_METADATA.json"),
                    "scope": "Root process evidence; Part A rows selected. No independent proof imported."})
    write_json(HERE / "PUBLICATION_SOURCE_PINS.json", {
        "created_utc": datetime.now(timezone.utc).isoformat(), "sources": sources,
        "prior_seals_verified": old_seals,
        "excluded_science": ["Part B note body", "Part B runtime bodies and scientific payload comparison",
                             "root30/root31/root32 author packets", "other active checkers", "campaign checkpoint/outcome"],
        "scope_incident_record": "PUBLICATION_SCOPE_INCIDENT.json"
    })
    report = {"verified_utc": datetime.now(timezone.utc).isoformat(),
              "prior_seals": old_seals, "runtime_rows": runtime_rows,
              "payload_comparisons": comparisons, "execution": scoped_execution,
              "source_count": len(sources), "comparison_code_sha256": digest(Path(__file__).resolve()),
              "source_pins_sha256": digest(HERE / "PUBLICATION_SOURCE_PINS.json"),
              "author_programs_executed_or_imported": []}
    write_json(HERE / "PUBLICATION_BINDING_RESULTS.json", report)
    print(json.dumps({key: report[key] for key in ("verified_utc", "prior_seals", "runtime_rows",
                                                  "payload_comparisons", "execution", "source_count",
                                                  "comparison_code_sha256", "source_pins_sha256")}, indent=2))


if __name__ == "__main__":
    main()
