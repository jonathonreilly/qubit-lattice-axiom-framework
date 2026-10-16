"""Capture one actual independent execution without reading author code/results."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_DERIVATION_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_INPUTS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_PLAN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_lee2020_calibration/independent_controls_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_lee2020_calibration/run_independent_bounded_v1.py",
]
from datetime import datetime, timezone
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
PREFIX = HERE / "independent_attempt01"
if PREFIX.with_suffix(".run.json").exists():
    raise FileExistsError("Keep the prior attempt immutable; use a new version.")
def binding():
    return {p: {"sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),
                "bytes": (ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
before = binding()
utc = datetime.now(timezone.utc).isoformat()
start = time.monotonic()
usage0 = resource.getrusage(resource.RUSAGE_CHILDREN)
argv = [sys.executable, "-B", str(HERE / "independent_controls_v1.py")]
timed_out = False
try:
    run = subprocess.run(argv, cwd=ROOT, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         timeout=AUDIT_TIMEOUT_SEC, check=False)
    stdout, stderr, code = run.stdout, run.stderr, run.returncode
except subprocess.TimeoutExpired as exc:
    timed_out = True
    stdout, stderr, code = exc.stdout or b"", exc.stderr or b"", None
elapsed = time.monotonic() - start
usage1 = resource.getrusage(resource.RUSAGE_CHILDREN)
PREFIX.with_suffix(".stdout.json").write_bytes(stdout)
PREFIX.with_suffix(".stderr.txt").write_bytes(stderr)
after = binding()
try:
    result = json.loads(stdout)
    parse_error = None
except (ValueError, UnicodeDecodeError) as exc:
    result = None
    parse_error = repr(exc)
meta = {
    "command_argv": argv, "cwd": str(ROOT), "timeout_seconds": AUDIT_TIMEOUT_SEC,
    "PYTHONDONTWRITEBYTECODE": "1", "observer_dont_write_bytecode": sys.dont_write_bytecode,
    "start_utc": utc, "end_utc": datetime.now(timezone.utc).isoformat(),
    "wall_seconds": elapsed, "child_user_seconds": usage1.ru_utime-usage0.ru_utime,
    "child_system_seconds": usage1.ru_stime-usage0.ru_stime,
    "child_peak_rss_platform_units": usage1.ru_maxrss, "platform": sys.platform,
    "returncode": code, "timed_out": timed_out, "python": sys.version,
    "stdout_bytes": len(stdout), "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
    "stderr_bytes": len(stderr), "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
    "source_binding_before": before, "source_binding_after": after,
    "sources_unchanged": before == after, "output_parse_error": parse_error,
    "summary": result["summary"] if result else None,
    "author_runner_or_results_read": False,
}
PREFIX.with_suffix(".run.json").write_text(json.dumps(meta, indent=2)+"\n")
print(json.dumps({k: meta[k] for k in ("wall_seconds", "returncode", "timed_out", "summary", "sources_unchanged")}, indent=2))
if code != 0 or timed_out or before != after:
    sys.exit(1)
