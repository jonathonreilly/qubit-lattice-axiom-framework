#!/usr/bin/env python3
"""Capture complete executions of this PRE's two own bounded scripts."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

here = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
runs = []
for stem, script in (("source_verification", "verify_source_pins.py"),
                     ("readout_control", "readout_control.py")):
    command = [sys.executable, str(here / script)]
    started = datetime.now(timezone.utc).isoformat()
    before = time.perf_counter()
    with (here / (stem + ".stdout.txt")).open("wb") as stdout, \
         (here / (stem + ".stderr.txt")).open("wb") as stderr:
        proc = subprocess.run(command, cwd=here, stdout=stdout, stderr=stderr)
    row = {"script": script, "script_sha256": sha(here / script),
           "command": command, "cwd": str(here), "started_utc": started,
           "elapsed_seconds": time.perf_counter() - before,
           "exit_code": proc.returncode,
           "stdout": stem + ".stdout.txt", "stderr": stem + ".stderr.txt",
           "stdout_sha256": sha(here / (stem + ".stdout.txt")),
           "stderr_sha256": sha(here / (stem + ".stderr.txt"))}
    runs.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    if proc.returncode:
        break
out = {"scope": "Fresh own PRE controls; no author code or parent computations run.",
       "runner_sha256": sha(Path(__file__).resolve()),
       "source_manifest_sha256": sha(here / "SOURCE_PINS.json"), "runs": runs}
(here / "EXECUTION.json").write_text(json.dumps(out, indent=2) + "\n")
if any(r["exit_code"] for r in runs):
    sys.exit(1)
