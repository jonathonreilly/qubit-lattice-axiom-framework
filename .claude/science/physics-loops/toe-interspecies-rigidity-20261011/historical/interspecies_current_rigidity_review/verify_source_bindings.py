"""Verify source bindings without rerunning or modifying authored evidence."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess

D = Path(__file__).resolve().parent
S = D.parent
W = S.parent / "walk_worktree"
output = D / "source_verification.json"
assert not output.exists(), "Preserve prior verification evidence"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify(record):
    path = Path(record["path"])
    actual = digest(path)
    return {"path": str(path), "expected_sha256": record["sha256"],
            "actual_sha256": actual, "matches": actual == record["sha256"]}


pre = json.loads((D / "pre_helper_receipt.json").read_text())
author_path = S / "interspecies_current_rigidity/receipt.json"
assert digest(author_path) == "283511b410dafa614c1e4453483b540e744604e66b538a803516c8294379267f"
author = json.loads(author_path.read_text())
groups = {
    "pre_helper_frozen_inputs": [verify(r) for r in pre["records"]],
    "author_receipt_records": [verify(r) for r in author["protected_sources"] + author["artifacts"]],
    "frozen_pre_helper_reconstruction": [verify(pre["reconstruction"])],
}
instructions = [
    (Path("/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md"), "9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455"),
    (Path("/Users/jonreilly/.codex/skills/physics-loop/references/proof-search-governance.md"), "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"),
    (W / "AGENTS.md", "f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f"),
    (W / "docs/ai_methodology/SCIENCE_WORKFLOW.md", "05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce"),
]
groups["reused_applicable_instruction_identities"] = [
    verify({"path": str(p), "sha256": h}) for p, h in instructions]
guards = [
    ("FINAL_EXCLUDED_WALK_QUANTITATIVE_MEMORY_TRANSFER_NOTE.md", "284686962fe4cce3c59a93b89a9fc33776ffa2310dbc9c8e9c1e8bda809d049e"),
    ("excluded_walk_quantitative_memory_transfer_2026_10_11.py", "bf1a83f21e06818ba1182bfa186d13ccf971777afb52f70a09da0c69e0eaa85d"),
    ("quantitative_memory_transfer_composition/reconstruction_map.json", "c29df627eeedeaa21f1ce04abdec65f04aa58d5e3ce0b5266342497a5c9d586f"),
    ("quantitative_memory_transfer_composition/receipt.json", "c1e09e3b251469b7c27d02d79e8a1221c99598850454f02e42ba287f8592269e"),
]
groups["prior_composition_freeze_guards"] = [
    verify({"path": str(S / p), "sha256": h}) for p, h in guards]
git_records = []
for record in pre["c1_exact_git_sources"]:
    blob = subprocess.run(["git", "show", record["revision"] + ":" + record["repo_path"]],
                          cwd=W, check=True, capture_output=True, timeout=30).stdout
    copy = Path(record["copy_path"]).read_bytes()
    git_records.append({**record, "git_blob_sha256": hashlib.sha256(blob).hexdigest(),
                        "git_blob_equals_copy": blob == copy,
                        "expected_sha256_matches": digest(record["copy_path"]) == record["sha256"]})
passed = all(r["matches"] for rows in groups.values() for r in rows)
passed = passed and all(r["git_blob_equals_copy"] and r["expected_sha256_matches"] for r in git_records)
result = {"verified_utc": datetime.now(timezone.utc).isoformat(), "groups": groups,
          "group_record_counts": {k: len(v) for k, v in groups.items()},
          "exact_c1_git_blobs": git_records, "all_match": passed,
          "limits": "Identity checks establish source binding, not correctness of unreviewed protected instruction or historical science files. Repeated records are counted separately. No author control replay occurred."}
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(output), "sha256": digest(output),
                  "groups": result["group_record_counts"], "exact_git_blobs": len(git_records),
                  "all_match": passed}, indent=2))
assert passed, "Source mismatch preserved in source_verification.json"
