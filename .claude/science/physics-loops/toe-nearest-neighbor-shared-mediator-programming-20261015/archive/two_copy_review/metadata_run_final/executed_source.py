"""Metadata only: identities and receipts, not mathematical verification."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
CANDIDATE = OUT.parent / "local_clock_shared_mediator_candidate"
REPO = Path("/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree")
MANIFEST = json.loads((OUT / "SOURCE_MANIFEST.json").read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

checks = []
def record(kind, name, expected, actual):
    checks.append({"kind": kind, "name": name, "expected": expected,
                   "actual": actual, "matched": expected == actual})

for row in MANIFEST["files"]:
    snapshot = OUT / row["snapshot"]
    record("review_snapshot", row["snapshot"], row["sha256"], sha(snapshot))
    if row["source"].startswith("/"):
        record("current_candidate", row["source"], row["sha256"], sha(Path(row["source"])))

frozen = OUT / "sources" / "candidate"
author_freeze = json.loads((frozen / "FINAL_FREEZE.json").read_text())
for row in author_freeze["members"]:
    record("author_final_member", row["path"], row["sha256"], sha(frozen / row["path"]))

pre = json.loads((frozen / "PRE_EXECUTION_SEAL.json").read_text())
archived = {"selected_exact_fixture.py": "executed_source.py"}
for row in pre["files"]:
    name = archived.get(row["path"], "pre_execution_" + row["path"])
    record("author_pre_execution_member", row["path"], row["sha256"],
           sha(frozen / "runs" / "selected_01" / name))

run = frozen / "runs" / "selected_01"
execution = json.loads((run / "EXECUTION.json").read_text())
record("author_executed_source", "executed_source.py", execution["source_sha256"], sha(run / "executed_source.py"))
record("author_current_runner", "selected_exact_fixture.py", execution["source_sha256"], sha(frozen / "selected_exact_fixture.py"))
record("author_stdout", "stdout", execution["stdout_sha256"], sha(run / "stdout"))
record("author_stderr", "stderr", execution["stderr_sha256"], sha(run / "stderr"))
record("author_pre_execution_seal", "PRE_EXECUTION_SEAL.json", execution["seal_sha256"], sha(frozen / "PRE_EXECUTION_SEAL.json"))

source_origins = json.loads((frozen / "SOURCE_MANIFEST.json").read_text())
rows = source_origins.get("sources", source_origins.get("files", []))
if not rows:
    raise RuntimeError("Unknown author source-manifest structure")
for row in rows:
    record("author_live_source", row["source"], row["sha256"], sha(Path(row["source"])))

for skill in ["physics-claim-reviewer", "workhorse"]:
    installed = Path("/Users/jonreilly/.codex/skills") / skill / "SKILL.md"
    pinned = OUT / "sources" / "instructions" / "docs" / "ai_methodology" / "skills" / skill / "SKILL.md"
    record("installed_skill_vs_pinned_main", skill, sha(pinned), sha(installed))

refs = {name: subprocess.check_output(["git", "rev-parse", name], cwd=REPO, text=True).strip()
        for name in MANIFEST["refs"]}
for name, expected in MANIFEST["refs"].items():
    record("git_ref_stability", name, expected, refs[name])

out = {"checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
       "scope": "Metadata only; no author scientific runner imported or executed.",
       "checks": checks, "all_matched": all(c["matched"] for c in checks), "refs": refs}
(OUT / "SOURCE_FRESHNESS.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"checked_utc": out["checked_utc"], "metadata_comparisons": len(checks),
                  "all_matched": out["all_matched"], "mismatches": [c for c in checks if not c["matched"]],
                  "scientific_program_executions": 0}, indent=2))
raise SystemExit(0 if out["all_matched"] else 1)
