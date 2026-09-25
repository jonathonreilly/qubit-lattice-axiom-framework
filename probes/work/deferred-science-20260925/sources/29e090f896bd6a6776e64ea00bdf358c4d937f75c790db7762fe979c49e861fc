#!/usr/bin/env python3
"""Explicit evidence WRITER for one fresh PRE46 program; never imports it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
CHOICES = {'charge_current_control.py': 'primitive_attempt01',
           'fourier_charge_control.py': 'fourier_attempt01'}
assert len(sys.argv) == 2 and sys.argv[1] in CHOICES
program = BASE / sys.argv[1]
out = BASE / CHOICES[sys.argv[1]]
out.mkdir(exist_ok=False)
raw = program.read_bytes()
(out / 'source.py').write_bytes(raw)
started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
run = subprocess.run([sys.executable, str(program)], cwd=BASE, capture_output=True)
elapsed = time.perf_counter()-tick
(out / 'stdout.json').write_bytes(run.stdout)
(out / 'stderr.txt').write_bytes(run.stderr)
receipt = dict(started_utc=started, elapsed_seconds=elapsed, exit_code=run.returncode,
               command=[sys.executable, str(program)], source_sha256=hashlib.sha256(raw).hexdigest(),
               stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
               stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
               source_unchanged=raw == program.read_bytes())
(out / 'EXECUTION.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
print(json.dumps(receipt, indent=2, sort_keys=True))
assert receipt['source_unchanged']
raise SystemExit(run.returncode)
