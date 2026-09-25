"""Bounded final correspondence; parses sources/data and never runs science code."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import difflib
import json
import math
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUB = BASE / "unrestricted-observation-publication"
NOTE = "docs/LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md"
RUNNER = "scripts/local_background_and_unrestricted_original_record_counts_2026_09_24.py"
RESULT = "outputs/unrestricted_original_records_20260924/UNRESTRICTED_ORIGINAL_RECORD_RESULTS.json"
CACHE = "logs/runner-cache/local_background_and_unrestricted_original_record_counts_2026_09_24.txt"
INITIAL_NOTE_SHA = "3b808676ba912bc0024581356a4b8d54bc33e5028c7bc7db18df18618f580a9b"
RUNNER_SHA = "a58a09da5c9673462c3fad051b37fa921cfdbfebcb4e56a7c633ca00d6549dce"
PRE_SEAL_SHA = "b6e0c33fe1286a876f1230759cb62769d57475d76c2ea1a6aae633064e2ba9d0"
POST_SEAL_SHA = "da4ec87b40713ab6fa744f4cb6c9fef8dce28faf441f53dd422575256275f2ba"


def identity(path):
    data = path.read_bytes()
    return {"sha256": sha256(data).hexdigest(), "bytes": len(data)}


def verify(path, expected):
    got = identity(path)
    if isinstance(expected, str):
        expected = {"sha256": expected}
    assert got["sha256"] == expected["sha256"], (str(path), got, expected)
    if "bytes" in expected:
        assert got["bytes"] == expected["bytes"]
    return got


def snapshot(origin, relative, expected=None, scope="source correspondence"):
    got = identity(origin) if expected is None else verify(origin, expected)
    data = origin.read_bytes()
    assert sha256(data).hexdigest() == got["sha256"]
    dest = HERE / relative
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        verify(dest, got)
    else:
        with dest.open("xb") as out:
            out.write(data)
        dest.chmod(0o444)
    return {"origin": str(origin), "snapshot": relative, **got, "scope": scope}


def prior_seal(name, expected):
    verify(HERE / name, expected)
    seal = json.loads((HERE / name).read_text())
    for member in seal["members"]:
        verify(HERE / member["path"], member)
    assert len(seal["members"]) == seal["frozen_member_count"]
    return seal


def functions(source):
    return {node.name: node for node in ast.parse(source).body
            if isinstance(node, ast.FunctionDef)}


def literal_assignments(source):
    result = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        result[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    return result


pre = prior_seal("PRE_SEAL.json", PRE_SEAL_SHA)
post = prior_seal("POST_SEAL.json", POST_SEAL_SHA)
manifest_path = BASE / "UNRESTRICTED_PUBLICATION_FROZEN_SOURCES.json"
execution_path = BASE / "UNRESTRICTED_PUBLICATION_CACHE_EXECUTION.json"
manifest = json.loads(manifest_path.read_text())
execution = json.loads(execution_path.read_text())
assert manifest["note"] == NOTE and manifest["runner"] == RUNNER and manifest["result"] == RESULT
assert manifest["files_sha256"][NOTE] == INITIAL_NOTE_SHA
assert manifest["files_sha256"][RUNNER] == RUNNER_SHA
sources = [snapshot(manifest_path, "publication-released/external/" + manifest_path.name),
           snapshot(execution_path, "publication-released/external/" + execution_path.name)]
for rel, digest in manifest["files_sha256"].items():
    scope = "Public note read completely; scientific comparison limited to B/C and scope" if rel == NOTE else (
        "Public runner read completely, without execution" if rel == RUNNER else
        "Declared parent byte identity; existing scientific premises are reused, not independently recertified")
    sources.append(snapshot(PUB / rel, "publication-released/publication/" + rel, digest, scope))
sources.append(snapshot(PUB / RESULT, "publication-released/publication/" + RESULT))
sources.append(snapshot(PUB / CACHE, "publication-released/publication/" + CACHE))
sources.append(snapshot(PUB / "scripts/runner_cache.py", "publication-released/protocol/runner_cache.py",
                        scope="Only declared-input fingerprint and cache serialization definitions inspected; module not imported"))

base_rev = manifest["base_revision"]
assert base_rev == "04dcf088de81990632d869142f30a59e881a8f31"
current_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=PUB, text=True).strip()
parent_git_checks = []
for rel, digest in manifest["files_sha256"].items():
    if rel in (NOTE, RUNNER):
        continue
    data = subprocess.check_output(["git", "show", base_rev + ":" + rel], cwd=PUB)
    assert sha256(data).hexdigest() == digest
    parent_git_checks.append({"path": rel, "revision": base_rev, "sha256": digest,
                              "bytes": len(data), "exact_git_bytes_match": True})

code = (PUB / RUNNER).read_text()
assignments = literal_assignments(code)
inputs = assignments["AUDIT_INPUT_PATHS"]
assert isinstance(inputs, tuple) and len(inputs) == 5 and len(set(inputs)) == 5
assert assignments["AUDIT_TIMEOUT_SEC"] == 120
assert assignments["RESULT_PATH"] == RESULT
assert set(inputs) == set(manifest["files_sha256"]) - {RUNNER}
fp = sha256()
fp.update(b"runner-cache-input-fingerprint-v1\0")
input_rows = []
for rel in inputs:
    assert not Path(rel).is_absolute() and ".." not in Path(rel).parts
    body = (PUB / rel).read_bytes()
    path_bytes = rel.encode("utf-8")
    fp.update(len(path_bytes).to_bytes(8, "big")); fp.update(path_bytes)
    fp.update(len(body).to_bytes(8, "big")); fp.update(body)
    input_rows.append({"path": rel, "sha256": sha256(body).hexdigest(), "bytes": len(body)})
fingerprint = fp.hexdigest()
assert fingerprint == "d367e69856c73a203517e7ff954b427e9f1875ce35df0a31d21c82eaddb3ec4f"

local_dir = BASE / "local-record-background-personal"
local_seal_pin = "455aaba6c0bd18da70176272ed9df914c04f8101bd8e826a81a78495f9af1b18"
verify(local_dir / "AUTHOR_CONTROL_SEAL.json", local_seal_pin)
local_seal = json.loads((local_dir / "AUTHOR_CONTROL_SEAL.json").read_text())
for name, digest in local_seal["files"].items():
    verify(local_dir / name, digest)
for name in ("local_background_controls.py", "LOCAL_BACKGROUND_CONTROL_RESULTS.json", "CONTROL_EXECUTION.json"):
    sources.append(snapshot(local_dir / name, "publication-released/local-author/" + name,
                            local_seal["files"][name], "Released root control evidence only; no Section A theorem certification"))
local_old = json.loads((local_dir / "LOCAL_BACKGROUND_CONTROL_RESULTS.json").read_text())
local_execution = json.loads((local_dir / "CONTROL_EXECUTION.json").read_text())
assert local_execution["script_sha256"] == local_seal["files"]["local_background_controls.py"]
assert local_execution["exit_code"] == 0
assert local_old["script_sha256"] == local_execution["script_sha256"]
assert (local_dir / "CONTROL.stdout.txt").read_bytes() == (local_dir / "LOCAL_BACKGROUND_CONTROL_RESULTS.json").read_bytes()
assert (local_dir / "CONTROL.stderr.txt").read_bytes() == b""

public_funcs = functions(code)
function_checks = []
for root_rel, root_sha in assignments["ROOT_CONTROL_SOURCES"]:
    origin = BASE / root_rel
    verify(origin, root_sha)
    root_source = origin.read_text()
    for name, node in functions(root_source).items():
        if name not in manifest["root_function_sha256"]:
            continue
        pub_node = public_funcs[name]
        original_ast = ast.dump(node, include_attributes=False)
        public_ast = ast.dump(pub_node, include_attributes=False)
        assert original_ast == public_ast
        original_segment = ast.get_source_segment(root_source, node)
        public_segment = ast.get_source_segment(code, pub_node)
        assert original_segment == public_segment
        segment_sha = sha256(public_segment.encode()).hexdigest()
        assert segment_sha == manifest["root_function_sha256"][name]
        function_checks.append({"name": name, "root_origin": root_rel, "root_source_sha256": root_sha,
                                "source_segment_sha256": segment_sha,
                                "AST_sha256_without_locations": sha256(public_ast.encode()).hexdigest(),
                                "AST_identical": True, "source_segment_identical": True})
assert len(function_checks) == 8
assert {r["name"] for r in function_checks} == set(manifest["root_function_sha256"])

result_bytes = (PUB / RESULT).read_bytes()
result = json.loads(result_bytes)
assert result["source_sha256"] == RUNNER_SHA and result["all_assertions_passed"] is True
count_old = json.loads((HERE / "post-released/COUNT_WINDOW_RESULTS.json").read_text())
payloads = []
for key, old in [("diagonal_rotor", local_old), ("chain_rows", local_old),
                 ("poisson_proposal_rows", count_old), ("finite_history_register", count_old)]:
    assert result[key] == old[key], key
    numeric = []
    def leaves(value):
        if isinstance(value, dict):
            for child in value.values(): leaves(child)
        elif isinstance(value, list):
            for child in value: leaves(child)
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            assert math.isfinite(value)
            numeric.append(value)
    leaves(result[key])
    payloads.append({"payload": key, "exact_parsed_equality": True, "numeric_leaves": len(numeric),
                     "maximum_absolute_numeric_difference": 0.0})
assert len(result["diagonal_rotor"]["rows"]) == 4
assert len(result["chain_rows"]) == 24
assert len(result["poisson_proposal_rows"]) == 12
assert len(result["finite_history_register"]["rows"]) == 4
max_quad = max(row["quadrature_difference"] for row in result["chain_rows"])
assert max_quad < 1.44e-8
chain_summaries = []
for row in result["chain_rows"]:
    actual, fine, qerr = (row[k] for k in ("local_observable_full_vs_hamiltonian_norm",
                                        "summed_disturbance_integral_32", "quadrature_difference"))
    assert actual <= fine + max(1e-10, 3 * qerr)
    chain_summaries.append({"sites": row["sites"], "K": row["K"], "time": row["time"],
                            "root_and_public_payload_exact": True,
                            "quadrature_difference": qerr,
                            "fine_integral_minus_actual_norm": fine-actual})

run = execution["result"]
assert run["runner"] == RUNNER and run["status"] == "ok" and run["exit_code"] == 0
assert run["timeout_sec"] == 120 and run["stderr"] == ""
assert run["stdout"].encode() == result_bytes + b"TOTAL_PASS: 4\n"
assert execution["path"] == str(PUB / CACHE)
assert 0 < result["elapsed_seconds"] < run["elapsed_sec"] < execution["runtime_wrapper_seconds"]
expected_cache = (
    "===== runner cache v1 =====\n"
    f"runner: {RUNNER}\nrunner_sha256: {RUNNER_SHA}\n"
    f"input_fingerprint_sha256: {fingerprint}\n"
    f"timeout_sec: 120\nexit_code: 0\nelapsed_sec: {run['elapsed_sec']:.2f}\nstatus: ok\n"
    f"----- stdout -----\n{run['stdout']}\n----- stderr -----\n{run['stderr']}\n")
assert (PUB / CACHE).read_text() == expected_cache

public_note = (PUB / NOTE).read_text()
old_note = (HERE / "post-released/UNRESTRICTED_FINITE_BIN_RECORD_CONTRAST_ROOT.md").read_text()
root_body = "## 1. The different statistic\n" + old_note.split("## 1. The different statistic\n", 1)[1]
public_b = public_note.split("## B. Positive windows, variance and microscopic counts\n\n", 1)[1].split("\n## C.", 1)[0]
public_b = public_b.replace("### ", "## ")
diff = "\n".join(difflib.unified_diff(root_body.splitlines(), public_b.splitlines(),
        fromfile="frozen-author-count-body", tofile="public-Section-B-with-normalized-headings", lineterm="")) + "\n"
with (HERE / "PUBLICATION_COUNT_DIFF.diff").open("x") as handle:
    handle.write(diff)

for pin in sources:
    verify(Path(pin["origin"]), pin); verify(HERE / pin["snapshot"], pin)
prior_seal("PRE_SEAL.json", PRE_SEAL_SHA); prior_seal("POST_SEAL.json", POST_SEAL_SHA)
pins = {"created_utc": datetime.now(timezone.utc).isoformat(),
        "phase": "Bounded final publication correspondence",
        "scope": "Scientific comparison of Sections B/C and public scope; Section A proof remains conditional. AST/payload/cache bindings cover the disclosed controls, not independent numerical replication.",
        "preserved_PRE_seal_sha256": PRE_SEAL_SHA, "preserved_POST_seal_sha256": POST_SEAL_SHA,
        "publication_base_revision": base_rev, "HEAD_at_check": current_head,
        "sources": sources, "declared_inputs_in_order": input_rows,
        "input_fingerprint_sha256": fingerprint, "parent_exact_git_bytes": parent_git_checks,
        "reused_local_author_seal": {"snapshot": "sources/external/local-record-background-personal/AUTHOR_CONTROL_SEAL.json", "sha256": local_seal_pin},
        "root_count_evidence": "Unchanged post-released directory bound by POST_SEAL.json",
        "publication_PARENT_note_scope": "The published readout-parent byte identity is checked, but its science is not newly recertified in this final comparison; prior sealed root/register/lag premises remain explicit."}
with (HERE / "PUBLICATION_SOURCE_PINS.json").open("x") as handle:
    json.dump(pins, handle, indent=2); handle.write("\n")
report = {"scope": pins["scope"], "all_correspondence_checks_passed": True,
          "PRE_members_unchanged": len(pre["members"]), "POST_members_unchanged": len(post["members"]),
          "publication_sources": {rel: identity(PUB / rel) for rel in (NOTE,RUNNER,RESULT,CACHE)},
          "external_manifest_sha256": identity(manifest_path)["sha256"],
          "external_execution_sha256": identity(execution_path)["sha256"],
          "all_five_declared_input_bytes_bound": True, "input_fingerprint_sha256": fingerprint,
          "parent_exact_git_bytes": parent_git_checks, "function_comparisons": function_checks,
          "four_payload_comparisons": payloads, "all_24_chain_correspondence_rows": chain_summaries,
          "max_chain_quadrature_discrepancy": max_quad,
          "count_proposal_rows": 12, "count_register_rows": 4,
          "register_bracket_gaps": [r["aggregate_bracket_gap"] for r in result["finite_history_register"]["rows"]],
          "canonical_execution": {k:v for k,v in run.items() if k not in ("stdout","stderr")},
          "canonical_stderr_bytes": len(run["stderr"].encode()),
          "canonical_wrapper_seconds": execution["runtime_wrapper_seconds"],
          "canonical_payload_internal_seconds": result["elapsed_seconds"],
          "result_plus_pass_line_equals_execution_stdout": True,
          "cache_matches_execution_and_fingerprint_byte_for_byte": True,
          "author_control_or_canonical_executions_by_checker": 0,
          "new_physics_controls_executed": 0, "Section_A_independently_certified": False,
          "other_active_science_or_checker_packets_read": False,
          "PUBLICATION_SOURCE_PINS": identity(HERE / "PUBLICATION_SOURCE_PINS.json"),
          "PUBLICATION_COUNT_DIFF": identity(HERE / "PUBLICATION_COUNT_DIFF.diff")}
print(json.dumps(report, indent=2, allow_nan=False))
