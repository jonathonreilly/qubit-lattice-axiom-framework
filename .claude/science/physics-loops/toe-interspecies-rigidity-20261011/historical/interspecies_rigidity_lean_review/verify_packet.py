"""Read-only identity and internal-consistency checks for the frozen Lean packet.

This script does not invoke Lean/Lake, build dependencies, or modify sources.
All newly written evidence stays in this separate review directory.
"""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import hashlib
import json
import re
import subprocess

D = Path(__file__).resolve().parent
S = D.parent
P = S / "interspecies_rigidity_lean"
ML = S / "lean_audit/mathlib"
W = S.parent / "walk_worktree"
output = D / "source_verification.json"
assert not output.exists(), "Preserve prior evidence"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(path, expected, group):
    actual = digest(path)
    return {"path": str(path), "expected_sha256": expected, "actual_sha256": actual,
            "matches": actual == expected, "group": group}


receipt_hash = "4f1512919a9e4aa41cac168882d3975e4b95f72cd4620876aa7cc959201c9048"
assert digest(P / "receipt.json") == receipt_hash
receipt = json.loads((P / "receipt.json").read_text())
records = [record(P / "receipt.json", receipt_hash, "author_receipt")]
for group in ["protected_sources", "artifacts"]:
    records.extend(record(Path(r["path"]), r["sha256"], group) for r in receipt[group])
extra = [
    (S / "INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md", "78c3bc3c8f223b988713cb5bd5210c1a801e8cdc5f428ee648d6284c400d97d6", "prior independent analytic review"),
    (S / "interspecies_current_rigidity_review/receipt.json", "1c3c02926c6c35277fdde7a4b174b85d2471c3c3ec4da9d39681a3c9f2f68de7", "prior independent analytic review receipt"),
    (Path("/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md"), "9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455", "reused applicable instruction"),
    (Path("/Users/jonreilly/.codex/skills/physics-loop/references/proof-search-governance.md"), "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "reused applicable instruction"),
    (W / "AGENTS.md", "f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f", "reused applicable instruction"),
    (W / "docs/ai_methodology/SCIENCE_WORKFLOW.md", "05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce", "reused applicable instruction"),
]
records.extend(record(path, expected, role) for path, expected, role in extra)
assert all(r["matches"] for r in records)


def git_text(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True,
                          text=True, timeout=30).stdout.strip()


commit = git_text(ML, "rev-parse", "HEAD")
tracked_status = git_text(ML, "status", "--porcelain", "--untracked-files=no")
assert commit == receipt["mathlib_commit"] and not tracked_status
packages = []
for name, expected in receipt["packages"].items():
    checkout = ML / ".lake/packages" / name
    actual = git_text(checkout, "rev-parse", "HEAD")
    status = git_text(checkout, "status", "--porcelain", "--untracked-files=no")
    assert actual == expected and not status
    packages.append({"name": name, "commit": actual, "tracked_status": status})

theorems = []
for filename, namespace in [("RigidityGeometry.lean", "InterspeciesRigidity"),
                            ("ControlData.lean", "RigidityControls")]:
    source = (P / filename).read_text()
    assert not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", source)
    theorems.extend(namespace + "." + match.group(1)
                    for match in re.finditer(r"^theorem\s+(\w+)", source, re.M))
axioms_log = (P / "axioms.txt").read_text()
axioms = {name: [v.strip() for v in values.split(",")]
          for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", axioms_log)}
assert set(theorems) == set(axioms) == set(receipt["theorem_axioms"])
assert axioms == receipt["theorem_axioms"]
assert all(set(a) == {"propext", "Classical.choice", "Quot.sound"} for a in axioms.values())

history = []
for meta_path in sorted((P / "logs").glob("*.json")):
    meta = json.loads(meta_path.read_text())
    label = meta_path.stem
    snapshot = Path(meta["source_snapshot"])
    assert snapshot == P / "logs" / (label + ".lean")
    assert digest(snapshot) == meta["source_sha256"]
    assert meta["timeout_seconds"] == 120
    assert meta["elapsed_seconds"] < 120
    log = (P / "logs" / (label + ".log")).read_text()
    assert "PROCESS TIMEOUT" not in log
    if label == "controls01":
        assert meta["exit"] == 1 and "Application type mismatch" in log and "sorryAx" in log
    elif label.startswith("false_"):
        assert meta["exit"] == 1 and "unsolved goals" in log and "⊢ False" in log
    else:
        assert meta["exit"] == 0
        assert not any(x in log for x in ["error:", "warning:", "sorryAx"])
    history.append({"label": label, "execution": meta,
                    "log_path": str(P / "logs" / (label + ".log")),
                    "log_sha256": digest(P / "logs" / (label + ".log"))})
assert len(history) == 9
for name, label in [("RigidityGeometry", "attempt02"), ("ControlData", "controls02"),
                    ("AxiomInventory", "axiom_inventory")]:
    assert (P / (name + ".lean")).read_bytes() == (P / "logs" / (label + ".lean")).read_bytes()
for target, source in [("final_compiler.log", "logs/attempt02.log"),
                       ("positive_compiler.log", "logs/controls02.log"),
                       ("axioms.txt", "logs/axiom_inventory.log")]:
    assert (P / target).read_bytes() == (P / source).read_bytes()
false_manifest = json.loads((P / "false_controls_manifest.json").read_text())
assert false_manifest == receipt["false_controls"]
for item in false_manifest:
    name = item["case"]
    assert digest(P / (name + ".lean")) == item["source_sha256"]
    assert digest(P / "logs" / ("false_" + name + ".log")) == item["log_sha256"]
    assert (P / (name + ".lean")).read_bytes() == (P / "logs" / ("false_" + name + ".lean")).read_bytes()
    assert not (P / (name + ".olean")).exists()
    assert item["execution"] == json.loads((P / "logs" / ("false_" + name + ".json")).read_text())
    assert item["actual_exit"] == item["wrapper_exit"] == 1
    assert item["reached_intended_mathematical_goal"] and not item["unexpected_failure_markers"]
    wrapper = (P / "logs" / ("false_" + name + ".wrapper.log")).read_text()
    log = (P / "logs" / ("false_" + name + ".log")).read_text()
    assert wrapper == log + "\nCOMPILER_EXIT 1\n"
for execution in receipt["successful_compilations"] + [receipt["axiom_inventory_execution"]]:
    label = Path(execution["source_snapshot"]).stem
    assert execution == json.loads((P / "logs" / (label + ".json")).read_text())

diffs = {}
for before, after in [("logs/attempt01.lean", "RigidityGeometry.lean"),
                       ("logs/controls01.lean", "ControlData.lean")]:
    diff = "".join(difflib.unified_diff((P / before).read_text().splitlines(keepends=True),
                                       (P / after).read_text().splitlines(keepends=True),
                                       fromfile=before, tofile=after))
    diffs[before + " -> " + after] = diff
control_before = (P / "logs/controls01.lean").read_text()
assert control_before.replace("weightedVSub_eq_linear_combination hw", "weightedVSub_eq_linear_combination Finset.univ hw") == (P / "ControlData.lean").read_text()

result = {"verified_utc": datetime.now(timezone.utc).isoformat(), "all_match": True,
          "author_receipt_sha256": receipt_hash, "source_records": records,
          "counts": {"author_protected": len(receipt["protected_sources"]),
                     "author_artifacts": len(receipt["artifacts"]), "file_records": len(records),
                     "principal_theorems": 6, "control_theorems": 8, "execution_records": len(history)},
          "mathlib_commit": commit, "mathlib_tracked_status": tracked_status, "packages": packages,
          "axioms": axioms, "execution_history": history, "historical_source_diffs": diffs,
          "lean_runtime_invoked_by_reviewer": False,
          "trust_boundary": "Pinned binaries and selected cached objects rehashed; no full transitive cache rebuild or independent executable provenance verification. No additional compiler execution was needed to resolve a statement concern."}
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(output), "sha256": digest(output), "counts": result["counts"],
                  "mathlib_commit": commit, "tracked_status_clean": not tracked_status,
                  "package_commits_and_tracked_status_match": len(packages), "all_match": True}, indent=2))
