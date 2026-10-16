#!/usr/bin/env python3
"""Immutable-source-at-launch receipt wrapper. CPU 90s, wall 120s, no AS limit."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
RUN = ROOT / "runs" / "attempt_01"
RUN.mkdir(parents=True, exist_ok=False)
SOURCE = ROOT / "emitted_word_fixture.py"
SNAPSHOT = RUN / "source_at_launch.py"
shutil.copyfile(SOURCE, SNAPSHOT)
shutil.copyfile(Path(__file__), RUN / "launcher_at_launch.py")


def identity(path):
    data = path.read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def cpu_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))


argv = [sys.executable, str(SNAPSHOT), "--output", str(RUN / "output")]
receipt = {
    "argv": argv, "cwd": str(RUN), "source": identity(SNAPSHOT),
    "launcher": identity(RUN / "launcher_at_launch.py"),
    "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "limits": {"CPU_seconds": 90, "wall_seconds": 120, "address_space": "not imposed"},
    "environment_overrides": {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"},
}
(RUN / "EXECUTION.json").write_text(json.dumps(receipt, indent=2) + "\n")
start = time.monotonic()
try:
    with (RUN / "stdout.txt").open("wb") as stdout, (RUN / "stderr.txt").open("wb") as stderr:
        result = subprocess.run(argv, cwd=RUN, stdout=stdout, stderr=stderr,
                                timeout=120, preexec_fn=cpu_limit,
                                env=dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1"))
    receipt["returncode"] = result.returncode
except Exception as exc:
    receipt["launcher_exception"] = repr(exc)
    receipt["returncode"] = None
finally:
    receipt["elapsed_wall_seconds"] = time.monotonic() - start
    receipt["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    receipt["stdout"] = identity(RUN / "stdout.txt")
    receipt["stderr"] = identity(RUN / "stderr.txt")
    (RUN / "EXECUTION.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2), flush=True)
sys.exit(0 if receipt["returncode"] == 0 else 1)
