"""Finalize only this new subpacket. This is a writing seal utility, not a checker."""
import ast
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sha = lambda body: hashlib.sha256(body).hexdigest()
assert HERE.name == "publication_comparison"
destination = HERE / "PUBLICATION_COMPARISON_SEAL.json"
assert not destination.exists()
inventory = json.loads((HERE / "SOURCE_INVENTORY.json").read_text())
assert sha((HERE / "SOURCE_INVENTORY.json").read_bytes()) == "cb27b3a4730678e71cce7931fdf7cda713fb06772e7d52b07556349242fd8947"
for item in inventory["sources"]:
    body = (HERE / item["copy"]).read_bytes()
    assert sha(body) == item["sha256"] and len(body) == item["bytes"]
    assert Path(item["origin"]).read_bytes() == body
prior_count = 0
for seal in inventory["prior_seals"]:
    assert sha(Path(seal["origin"]).read_bytes()) == seal["sha256"]
    for member in seal["members"]:
        body = Path(member["path"]).read_bytes()
        assert sha(body) == member["sha256"] and len(body) == member["bytes"]
        prior_count += 1
assert prior_count == 254
run_rows = []
for name in ["freeze", "comparison_attempt01"]:
    receipt = json.loads((HERE / f"{name}.execution.json").read_text())
    source = Path(receipt["command"][1])
    assert sha(source.read_bytes()) == receipt["source_sha256_before_and_after"]
    for stream in ["stdout", "stderr"]:
        body = (HERE / f"{name}.{stream}.txt").read_bytes()
        assert sha(body) == receipt[f"{stream}_sha256"]
        assert len(body) == receipt[f"{stream}_bytes"]
    assert receipt["exit_code"] == 0 and receipt["stderr_bytes"] == 0
    run_rows.append({"receipt": f"{name}.execution.json", "source_sha256": receipt["source_sha256_before_and_after"],
                     "stdout_sha256": receipt["stdout_sha256"], "exit_code": 0, "stderr_bytes": 0})
comparison = json.loads((HERE / "comparison_attempt01.stdout.txt").read_text())
assert comparison["all_checks_completed"] is True
assert comparison["frozen_sources_and_live_origins_checked"] == 97
assert len(comparison["complete_artifacts"]) == 5 and len(comparison["all_differences"]) == 7
assert comparison["cache"]["cache_bytes_reconstructed_exactly"] is True
checker = ast.parse((HERE / "check_publication_read_only.py").read_text())
for node in ast.walk(checker):
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            assert node.func.id not in {"open", "exec", "eval", "compile", "__import__"}
        if isinstance(node.func, ast.Attribute):
            assert node.func.attr not in {"write_text", "write_bytes", "open", "chmod", "unlink", "mkdir", "rmdir", "rename", "replace", "run", "Popen", "system"}
    if isinstance(node, ast.Import):
        assert all(n.name.split(".")[0] in {"ast", "difflib", "hashlib", "json", "math", "re"} for n in node.names)
    if isinstance(node, ast.ImportFrom):
        assert node.module in {"collections", "fractions", "itertools", "pathlib"}
report = (HERE / "PUBLICATION_COMPARISON.md").read_bytes()
assert b"d709a13f913f0f16cce7f4fe4ae47ebfc90dc8d90b1fcd0cf0c952337bedcf7b" in report
assert b"No mathematical or evidence-binding repair is required" in report
assert not any(x < 32 and x not in [9, 10, 13] for x in report)
verification = {"verified_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "frozen_source_origins": 97, "prior_seals": 9, "prior_members": prior_count,
                "prior_bytes_preserved": True, "complete_artifacts": 5, "exact_leaf_difference_count": 7,
                "input_fingerprint_sha256": comparison["cache"]["input_fingerprint_sha256"],
                "own_run_bindings": run_rows,
                "read_only_checker_static_mutation_scan_completed": True,
                "author_scientific_execution_or_import": False,
                "report_creation_failure_preserved": "REPORT_CREATION_FAILURE.json",
                "report_sha256": sha(report)}
with (HERE / "FINAL_BINDING_VERIFICATION.json").open("x") as out:
    json.dump(verification, out, indent=2)
    out.write("\n")
members = []
for path in sorted(HERE.rglob("*")):
    assert not path.is_symlink()
    if path.is_file():
        assert path != destination
        body = path.read_bytes()
        members.append({"path": str(path.relative_to(HERE)), "sha256": sha(body), "bytes": len(body)})
seal = {"phase": "Final released-source publication correspondence; no audit verdict",
        "sealed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "report": "PUBLICATION_COMPARISON.md", "report_sha256": sha(report),
        "source_inventory": "SOURCE_INVENTORY.json", "source_inventory_sha256": sha((HERE / "SOURCE_INVENTORY.json").read_bytes()),
        "frozen_publication_manifest_sha256": "d0460afcbbcf15a646e655d44888069bde0648552797e5af3b043c7651846b6f",
        "canonical_note_sha256": "d709a13f913f0f16cce7f4fe4ae47ebfc90dc8d90b1fcd0cf0c952337bedcf7b",
        "finding": "No required mathematical or evidence-binding repair. Historical status lines remain unchanged with their interpretation recorded.",
        "existing_PRE_POST_preserved": True, "prior_seals_verified": 9, "prior_members_verified": prior_count,
        "author_scientific_programs_executed": False, "new_primitive_or_eigensolver_run": False,
        "publication_or_campaign_checkpoint_modified": False, "delegation": False,
        "members": members}
with destination.open("x") as out:
    json.dump(seal, out, indent=2)
    out.write("\n")
for item in members:
    path = HERE / item["path"]
    assert sha(path.read_bytes()) == item["sha256"]
    path.chmod(0o444)
destination.chmod(0o444)
print(json.dumps({"report": str(HERE / seal["report"]), "report_sha256": seal["report_sha256"],
                  "seal": str(destination), "seal_sha256": sha(destination.read_bytes()),
                  "member_count": len(members), "source_inventory_sha256": seal["source_inventory_sha256"]}, indent=2))
