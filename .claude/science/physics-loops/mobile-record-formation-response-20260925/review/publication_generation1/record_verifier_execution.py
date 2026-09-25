"""New outer recorder; writes only this packet after the read-only verifier exits."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
I = D.parent
source = D / "verify_publication_readonly.py"
tree = ast.parse(source.read_text())
allowed_modules = {"pathlib", "collections", "ast", "datetime", "hashlib", "json", "re", "sys"}
forbidden_calls = {
    "write", "write_text", "write_bytes", "unlink", "mkdir", "chmod", "rename",
    "rmdir", "touch", "Popen", "run", "system", "exec", "eval", "open", "__import__",
}
calls = []
for node in ast.walk(tree):
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        names = ([x.name.split(".")[0] for x in node.names]
                 if isinstance(node, ast.Import) else [node.module.split(".")[0]])
        assert set(names) <= allowed_modules
    if isinstance(node, ast.Call):
        terminal = (node.func.id if isinstance(node.func, ast.Name)
                    else node.func.attr if isinstance(node.func, ast.Attribute) else "")
        assert terminal not in forbidden_calls, ast.unparse(node.func)
        calls.append(ast.unparse(node.func))

pins = json.loads((D / "SOURCE_PINS_INITIAL.json").read_text())
post = json.loads((I / "POST_SOURCE_PINS.json").read_text())
origins = [
    Path(x["origin"]) for x in
    pins["sources"] + post["author39_sources"] + post["permitted_main_parents"]
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def file_map():
    paths = {p for p in I.rglob("*") if p.is_file()} | set(origins)
    return {str(p): digest(p) for p in sorted(paths)}

before = file_map()
at = datetime.datetime.now(datetime.timezone.utc).isoformat()
start = time.perf_counter()
result = subprocess.run([sys.executable, str(source)], cwd=D, capture_output=True)
elapsed = time.perf_counter() - start
after = file_map()
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
    "source_sha256": digest(source), "recorder_sha256": digest(Path(__file__)),
    "elapsed_seconds": elapsed, "exit_code": result.returncode,
    "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
    "all_observed_source_maps_unchanged": True, "observed_files": len(before),
    "science_programs_executed": False,
    "verifier_AST_read_and_explicit_call_names_checked": True,
    "prior_preflight_failure": "inspection_attempt01/FAILURE.md",
}
(out / "EXECUTION.json").write_text(json.dumps(receipt, indent=2) + "\n")
if result.returncode == 0:
    payload = json.loads(result.stdout)
    (out / "VERIFICATION_REPORT.json").write_bytes(result.stdout)
    print(json.dumps({
        "execution": receipt, "report_sha256": digest(out / "VERIFICATION_REPORT.json"),
        "body": payload["body_correspondence"], "differences": payload["all_differences"],
        "leaf_count": payload["leaf_count"], "geometry_groups": len(payload["geometry"]),
        "row_count": len(payload["complete_scientific_rows"]),
    }, indent=2))
else:
    print(json.dumps(receipt, indent=2))
    print(result.stderr.decode())
