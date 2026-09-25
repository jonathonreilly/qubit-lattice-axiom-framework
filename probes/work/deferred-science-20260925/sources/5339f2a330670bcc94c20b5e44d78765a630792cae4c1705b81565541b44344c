"""New recorder for one inspected read-only comparison; only this directory is writable."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
source = D / "verify_generation2_readonly.py"
tree = ast.parse(source.read_text())
allowed = {"pathlib", "collections", "ast", "datetime", "hashlib", "json"}
forbidden = {"write", "write_text", "write_bytes", "open", "exec", "eval", "__import__",
             "mkdir", "unlink", "chmod", "rename", "rmdir", "touch", "run", "Popen", "system"}
calls = []
for node in ast.walk(tree):
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        names = ([a.name.split(".")[0] for a in node.names] if isinstance(node, ast.Import)
                 else [node.module.split(".")[0]])
        assert set(names) <= allowed
    if isinstance(node, ast.Call):
        name = (node.func.id if isinstance(node.func, ast.Name)
                else node.func.attr if isinstance(node.func, ast.Attribute) else "")
        assert name not in forbidden
        calls.append(ast.unparse(node.func))

pins = json.loads((D / "SOURCE_PINS_INITIAL.json").read_text())
origins = {Path(row["origin"]) for row in pins["sources"]}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def observe():
    paths = {p for p in D.parent.rglob("*") if p.is_file()} | origins
    result = {}
    for p in sorted(paths):
        st = p.stat()
        result[str(p)] = {"sha256": sha(p), "bytes": st.st_size,
                          "mtime_ns": st.st_mtime_ns, "ctime_ns": st.st_ctime_ns}
    return result

before = observe()
at = datetime.datetime.now(datetime.timezone.utc).isoformat()
start = time.perf_counter()
result = subprocess.run([sys.executable, str(source)], cwd=D, capture_output=True)
elapsed = time.perf_counter() - start
after = observe()
assert before == after
out = D / "verification_attempt01"
assert not out.exists()
out.mkdir()
(out / source.name).write_bytes(source.read_bytes())
(out / "stdout.log").write_bytes(result.stdout)
(out / "stderr.log").write_bytes(result.stderr)
(out / "OBSERVED_SOURCE_MAP.json").write_text(json.dumps(before, indent=2) + "\n")
(out / "INSPECTED_CALLS.json").write_text(json.dumps(sorted(set(calls)), indent=2) + "\n")
receipt = {
    "started_utc": at, "command": [sys.executable, str(source)],
    "source_sha256": sha(source), "recorder_sha256": sha(Path(__file__)),
    "elapsed_seconds": elapsed, "exit_code": result.returncode,
    "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
    "observed_file_count": len(before),
    "observed_content_size_mtime_ctime_unchanged": True,
    "scientific_programs_imported_or_executed": False,
    "prior_source_snapshot_failure": "snapshot_attempt01/FAILURE.md",
}
(out / "EXECUTION.json").write_text(json.dumps(receipt, indent=2) + "\n")
if result.returncode == 0:
    payload = json.loads(result.stdout)
    (out / "VERIFICATION_REPORT.json").write_bytes(result.stdout)
    print(json.dumps({"execution": receipt, "report_sha256": sha(out / "VERIFICATION_REPORT.json"),
                      "source_count": len(payload["sources"]), "repair_resolved": payload["required_generation1_wording_repair_resolved"],
                      "nonruntime_leaves": payload["equal_nonruntime_leaves"],
                      "all_assertions": payload["all_correspondence_assertions_passed"]}, indent=2))
else:
    print(json.dumps(receipt, indent=2))
    print(result.stderr.decode())
