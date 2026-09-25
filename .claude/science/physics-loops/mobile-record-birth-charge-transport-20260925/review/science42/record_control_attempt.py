#!/usr/bin/env python3
"""Execute one NEW local control and record it in a new directory only.
This recorder writes evidence. It is not the later read-only verifier.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

base=Path(__file__).resolve().parent
program=base/sys.argv[1]
assert program.parent == base and program.name in {
    'primitive_birth_charge_control.py','low_wave_remainder_control.py'}
attempt=base/sys.argv[2]
attempt.mkdir(exist_ok=False)
source=program.read_bytes()
(attempt/'source.py').write_bytes(source)
start=datetime.now(timezone.utc).isoformat()
t0=time.perf_counter()
run=subprocess.run([sys.executable,str(program)],cwd=base,capture_output=True)
elapsed=time.perf_counter()-t0
(attempt/'stdout.json').write_bytes(run.stdout)
(attempt/'stderr.txt').write_bytes(run.stderr)
assert source == program.read_bytes()
receipt=dict(started_utc=start,elapsed_seconds=elapsed,exit_code=run.returncode,
             python=sys.executable,command=[sys.executable,str(program)],
             source_sha256=hashlib.sha256(source).hexdigest(),
             stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
             stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
             source_unchanged=True)
(attempt/'EXECUTION.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(attempt=str(attempt),**receipt),indent=2,sort_keys=True))
raise SystemExit(run.returncode)
