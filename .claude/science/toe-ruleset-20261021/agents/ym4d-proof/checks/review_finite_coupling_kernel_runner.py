#!/usr/bin/env python3
"""Fresh gated child launcher; never imports or modifies author evidence."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import resource
import signal
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument("--attempt", required=True)
parser.add_argument("--script", default="review_finite_coupling_kernel_01.py")
args = parser.parse_args()
folder = Path(__file__).resolve().parent
root = folder.parents[5]
prefix = folder / ("review_finite_coupling_kernel_" + args.attempt)
now = dt.datetime.now(dt.timezone.utc)
lock = json.loads((root / "logs/physics_worker_lock.json").read_text())
mem = subprocess.run(["/usr/bin/memory_pressure", "-Q"], text=True, capture_output=True)
match = re.search(r"System-wide memory free percentage:\s*(\d+)%", mem.stdout)
free = int(match.group(1)) if match else None
load = os.getloadavg()[0]
lock_ok = (lock.get("owner") == "ym4d-full-proof" and
           lock.get("holder_id") == "01a1873f-103a-7f01-b924-4455238d8a86" and
           dt.datetime.fromisoformat(lock["expires_at"]) > now)
gate = {"utc": now.isoformat(), "free_percent": free, "load1": load,
        "memory_stdout": mem.stdout, "memory_stderr": mem.stderr, "lock": lock,
        "pass": bool(free is not None and free >= 50 and load < 20 and lock_ok)}
with Path(str(prefix) + "_gate.json").open("x") as f:
    json.dump(gate, f, indent=2)
    f.write("\n")
print(json.dumps(gate), flush=True)
if not gate["pass"]:
    sys.exit(2)
script = folder / args.script
env = os.environ.copy()
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
            "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    env[key] = "1"


def limits():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (55, 55))


out_path, err_path = Path(str(prefix) + "_stdout.txt"), Path(str(prefix) + "_stderr.txt")
start = time.monotonic()
peak = 0
reason = None
with out_path.open("x") as out, err_path.open("x") as err:
    child = subprocess.Popen([sys.executable, "-u", str(script)], cwd=root, env=env,
                             stdout=out, stderr=err, preexec_fn=limits, start_new_session=True)
    while child.poll() is None:
        rss = subprocess.run(["/bin/ps", "-o", "rss=", "-p", str(child.pid)], text=True, capture_output=True)
        try:
            peak = max(peak, int(rss.stdout.strip()))
        except ValueError:
            pass
        if peak >= 1_900_000:
            reason = "resident-memory watchdog below 2 GiB"
        if time.monotonic() - start > 60:
            reason = "60-second wall cap"
        if reason:
            os.killpg(child.pid, signal.SIGKILL)
            break
        time.sleep(0.025)
    code = child.wait()
record = {"utc": dt.datetime.now(dt.timezone.utc).isoformat(), "exit_code": code,
          "wall_seconds": time.monotonic() - start, "peak_rss_KiB": peak, "termination_reason": reason,
          "script": str(script.relative_to(root)), "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
          "stdout_sha256": hashlib.sha256(out_path.read_bytes()).hexdigest(),
          "stderr_sha256": hashlib.sha256(err_path.read_bytes()).hexdigest()}
with Path(str(prefix) + "_run.json").open("x") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
print(json.dumps(record, indent=2), flush=True)
print(out_path.read_text(), end="")
print(err_path.read_text(), end="", file=sys.stderr)
sys.exit(code if code >= 0 else 1)
