"""Preserve the first independent control execution and all output."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import time

D = Path(__file__).resolve().parent
P = D / "independent_collision_controls.py"
paths = {name: D / name for name in ["independent_controls.log", "independent_execution.json"]}
assert all(not p.exists() for p in paths.values())
command = ["/opt/homebrew/opt/python@3.13/bin/python3.13", str(P)]
started = time.monotonic()
started_utc = datetime.now(timezone.utc).isoformat()
try:
    r = subprocess.run(command, capture_output=True, text=True, timeout=90)
    stdout, stderr, returncode, timed_out = r.stdout, r.stderr, r.returncode, False
except subprocess.TimeoutExpired as exc:
    stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
    stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
    returncode, timed_out = None, True
log = paths["independent_controls.log"]
log.write_text(stdout+stderr)
record = {"command": command, "started_utc": started_utc,
          "elapsed_seconds": time.monotonic()-started, "timeout_seconds": 90,
          "returncode": returncode, "timed_out": timed_out,
          "source_sha256": hashlib.sha256(P.read_bytes()).hexdigest(),
          "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
          "scope": "Independent exact controls; not a continuum proof or physical-measure check."}
paths["independent_execution.json"].write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
assert returncode == 0 and not timed_out, "Control failure preserved in the complete log"
