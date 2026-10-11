"""Execute one literal publication-primary replay and preserve its full output."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
primary = D.parent / "interspecies_collision_current_rigidity_2026_10_11.py"
log = D / "primary.log"
execution = D / "primary_execution.json"
assert not log.exists() and not execution.exists(), "Preserve previous run evidence"
cmd = [sys.executable, str(primary)]
start = datetime.now(timezone.utc).isoformat()
t = time.monotonic()
timed_out = False
try:
    result = subprocess.run(cmd, cwd=D.parent, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=30)
    code, output = result.returncode, result.stdout
except subprocess.TimeoutExpired as exc:
    timed_out = True
    code, output = 124, (exc.stdout or b"") + b"\nTIMEOUT after 30 seconds\n"
log.write_bytes(output)
execution.write_text(json.dumps({
    "command": cmd, "cwd": str(D.parent), "started_utc": start,
    "elapsed_seconds": time.monotonic() - t, "timeout_seconds": 30,
    "timed_out": timed_out, "exit_code": code,
    "python": sys.version, "platform": platform.platform(),
    "primary_sha256": hashlib.sha256(primary.read_bytes()).hexdigest(),
    "log_sha256": hashlib.sha256(output).hexdigest(),
    "scope": "Author finite-evidence replay only; no new analytic proof, independent review, Lean compilation, semantic whole-primary mutants or audit."
}, indent=2) + "\n")
sys.stdout.buffer.write(output)
print("RECORDED_EXIT", code)
sys.exit(code)
