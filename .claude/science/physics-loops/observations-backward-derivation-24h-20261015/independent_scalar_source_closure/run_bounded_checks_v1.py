"""Bounded bytecode-disabled execution; save complete actual stdout/stderr.

Modes are independent, author, and observed_author. Outputs stay beside this
file. The author mode executes the original file, without copying or editing it.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CLOSURE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CLOSURE_v2.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_PLAN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_FROZEN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_scalar_source_closure_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CONTROLS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SIREN_BRIDGE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_scalar_source_closure/independent_controls_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_scalar_source_closure/observe_author_reads_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_scalar_source_closure/run_bounded_checks_v1.py",
]
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
mode = sys.argv[1]
targets = {
    "independent": HERE / "independent_controls_v1.py",
    "author": HERE.parent / "check_scalar_source_closure_v1.py",
    "observed_author": HERE / "observe_author_reads_v1.py",
}
target = targets[mode]
prefix = HERE / (mode + "_attempt01")
if prefix.with_suffix(".run.json").exists():
    raise FileExistsError("Preserve the previous attempt; use a new version for another run")

def binding():
    return {p: {"sha256": hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
                "bytes": (ROOT / p).stat().st_size} for p in AUDIT_INPUT_PATHS}

before = binding()
start_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
start = time.monotonic()
usage0 = resource.getrusage(resource.RUSAGE_CHILDREN)
argv = [sys.executable, "-B", str(target)]
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
timed_out = False
try:
    run = subprocess.run(argv, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, timeout=AUDIT_TIMEOUT_SEC, check=False)
    stdout, stderr, code = run.stdout, run.stderr, run.returncode
except subprocess.TimeoutExpired as exc:
    timed_out = True
    stdout, stderr, code = exc.stdout or b"", exc.stderr or b"", None
elapsed = time.monotonic() - start
usage1 = resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout)
prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after = binding()
parsed = None
parse_error = None
try:
    parsed = json.loads(stdout)
except (ValueError, UnicodeDecodeError) as exc:
    parse_error = repr(exc)
meta = {
    "mode": mode, "command_argv": argv, "cwd": str(ROOT),
    "PYTHONDONTWRITEBYTECODE": "1", "sys_dont_write_bytecode_of_observer": sys.dont_write_bytecode,
    "timeout_seconds": AUDIT_TIMEOUT_SEC, "timed_out": timed_out,
    "start_utc": start_utc, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "wall_seconds": elapsed, "child_user_seconds": usage1.ru_utime - usage0.ru_utime,
    "child_system_seconds": usage1.ru_stime - usage0.ru_stime,
    "child_peak_rss_platform_units": usage1.ru_maxrss, "platform": sys.platform,
    "returncode": code, "python": sys.version,
    "stdout_sha256": hashlib.sha256(stdout).hexdigest(), "stdout_bytes": len(stdout),
    "stderr_sha256": hashlib.sha256(stderr).hexdigest(), "stderr_bytes": len(stderr),
    "source_binding_before": before, "source_binding_after": after,
    "sources_unchanged": before == after, "output_parse_error": parse_error,
    "reported_summary": parsed.get("summary") if isinstance(parsed, dict) else None,
}
if mode in ("author", "observed_author") and isinstance(parsed, dict):
    original_bytes = (HERE.parent / "SCALAR_SOURCE_CONTROLS_v1.json").read_bytes()
    original = json.loads(original_bytes)
    meta["equals_author_controls_bytes"] = stdout == original_bytes
    meta["equals_author_controls_json"] = parsed == original
    meta["actual_check_count"] = len(parsed.get("checks", []))
    meta["actual_failed_check_names"] = [r["name"] for r in parsed.get("checks", []) if not r["passed"]]
prefix.with_suffix(".run.json").write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps({k: meta[k] for k in ("mode", "returncode", "timed_out", "wall_seconds", "reported_summary", "sources_unchanged")}, indent=2))
assert code == 0 and not timed_out and before == after
if parsed and "summary" in parsed:
    assert parsed["summary"]["failed"] == 0
