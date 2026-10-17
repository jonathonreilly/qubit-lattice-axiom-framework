#!/usr/bin/env python3
"""Bounded review launcher; preserves complete source/output for each attempt."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import os
import resource
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
attempts=sorted(ROOT.glob("attempt_[0-9][0-9]"))
assert len(attempts)<3, "predeclared maximum attempts exhausted"
prior=0.0
for a in attempts:
    r=a/"EXECUTION.json"
    if r.exists():prior+=json.loads(r.read_text())["wall_seconds"]
assert prior<180
dest=ROOT/f"attempt_{len(attempts)+1:02d}"
dest.mkdir()
script=ROOT/"check_installed.py"
snapshot=dest/"check_installed.py"
snapshot.write_bytes(script.read_bytes())
env=dict(os.environ)
env.update(PYTHONDONTWRITEBYTECODE="1",OPENBLAS_NUM_THREADS="1",
           OMP_NUM_THREADS="1",MKL_NUM_THREADS="1")
start=time.monotonic()
utc=dt.datetime.now(dt.timezone.utc).isoformat()
timed_out=False
with (dest/"stdout.json").open("wb") as out, (dest/"stderr.txt").open("wb") as err:
    try:
        done=subprocess.run([sys.executable,str(snapshot)],cwd=dest,env=env,
            stdout=out,stderr=err,timeout=min(60,180-prior))
        code=done.returncode
    except subprocess.TimeoutExpired:
        timed_out=True;code=None
elapsed=time.monotonic()-start
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt={
    "start_utc":utc, "end_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
    "command":[sys.executable,str(snapshot)],"cwd":str(dest),
    "wall_seconds":elapsed, "prior_scientific_wall_seconds":prior,
    "exit_code":code,"timed_out":timed_out,
    "user_cpu_seconds":usage.ru_utime,"system_cpu_seconds":usage.ru_stime,
    "peak_rss_raw":usage.ru_maxrss,"peak_rss_platform_units":"bytes on macOS",
    "script_sha256":sha(snapshot),"python_binary":str(Path(sys.executable).resolve()),
    "python_binary_sha256":sha(Path(sys.executable).resolve()),
    "stdout_sha256":sha(dest/"stdout.json"),"stderr_sha256":sha(dest/"stderr.txt"),
    "caps":{"cpu_seconds":45,"wall_seconds":60,"maximum_attempts":3,
            "total_wall_seconds":180,"maximum_matrix_dimension":16},
    "thread_environment_requested":{k:env[k] for k in
        ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")},
    "thread_count_measured":False,
}
(dest/"EXECUTION.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
if code==0:
    parsed=json.loads((dest/"stdout.json").read_text())
    (ROOT/"RESULTS.json").write_bytes((dest/"stdout.json").read_bytes())
    (ROOT/"EXECUTION.json").write_text(json.dumps(receipt,indent=2)+"\n")
else:
    print((dest/"stderr.txt").read_text())
sys.exit(0 if code==0 else 1)
