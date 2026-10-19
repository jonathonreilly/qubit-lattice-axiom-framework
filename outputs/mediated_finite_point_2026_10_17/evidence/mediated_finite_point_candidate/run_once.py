#!/usr/bin/env python3
"""Capture one bounded arithmetic subprocess without overwriting prior evidence."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


def pin(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    root = Path(__file__).resolve().parent
    run = root / "runs" / "calculation_001"
    run.mkdir(parents=True, exist_ok=False)
    source, launcher = root / "calculate.py", Path(__file__).resolve()
    source_pin, launcher_pin = pin(source), pin(launcher)
    shutil.copyfile(source, run / "executed_source.py")
    shutil.copyfile(launcher, run / "executed_launcher.py")
    manifest = root / "SOURCE_PINS.json"
    source_rows = json.loads(manifest.read_text())["sources"]
    for row in source_rows:
        assert pin(row["path"]) == row, row["path"]
    output = run / "EXACT_CERTIFICATE.json"
    argv = [sys.executable, str(source), "--output", str(output)]
    prelaunch = {"argv": argv, "cwd": str(root), "timeout_seconds": 120,
                 "cpu_quota": None, "ram_quota": None,
                 "source_at_launch": source_pin, "launcher_at_launch": launcher_pin,
                 "source_capture": pin(run / "executed_source.py"),
                 "launcher_capture": pin(run / "executed_launcher.py"),
                 "premise_manifest": pin(manifest), "planned_at_utc": utc()}
    (run / "PRELAUNCH.json").write_text(json.dumps(prelaunch, indent=2) + "\n")
    started, mono = utc(), time.monotonic()
    timed_out = False
    with (run / "stdout").open("wb") as stdout, (run / "stderr").open("wb") as stderr:
        proc = subprocess.Popen(argv, cwd=root, stdout=stdout, stderr=stderr)
        try:
            code = proc.wait(timeout=120)
        except subprocess.TimeoutExpired:
            timed_out = True
            proc.kill()
            code = proc.wait()
    ended, elapsed = utc(), time.monotonic() - mono
    receipt = dict(prelaunch)
    receipt.update({"started_at_utc": started, "ended_at_utc": ended,
                    "wall_seconds": elapsed, "exit_code": code, "timed_out": timed_out,
                    "stdout": pin(run / "stdout"), "stderr": pin(run / "stderr"),
                    "source_after_run": pin(source), "launcher_after_run": pin(launcher),
                    "output": pin(output) if output.exists() else None,
                    "claim": "one author exact-arithmetic bound evaluation; no dynamics or sweep"})
    (run / "EXECUTION.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"receipt": pin(run / "EXECUTION.json"), "exit_code": code,
                      "timed_out": timed_out, "wall_seconds": elapsed}, indent=2))
    raise SystemExit(code if code >= 0 else 1)


if __name__ == "__main__":
    main()
