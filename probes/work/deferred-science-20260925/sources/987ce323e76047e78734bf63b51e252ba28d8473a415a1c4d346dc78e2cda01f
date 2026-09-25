#!/usr/bin/env python3
"""Evidence WRITER around the separately read-only verifier; fresh directory only."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

base=Path(__file__).resolve().parent
out=base/'verification_attempt01'
assert not out.exists()
pins=json.loads((base/'EVIDENCE_PINS.json').read_text())
sources=json.loads((base/'SOURCE_PINS.json').read_text())['sources']
paths=[base/row['path'] for row in pins['members']]+[base/'EVIDENCE_PINS.json']
paths.extend(Path(row['origin']) for row in sources)
def inventory():
    return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory()
start=datetime.now(timezone.utc).isoformat()
t0=time.perf_counter()
run=subprocess.run([sys.executable,str(base/'verify_readonly.py')],cwd=base,capture_output=True)
elapsed=time.perf_counter()-t0
after=inventory()
out.mkdir()
(out/'stdout.json').write_bytes(run.stdout)
(out/'stderr.txt').write_bytes(run.stderr)
receipt=dict(started_utc=start,elapsed_seconds=elapsed,exit_code=run.returncode,
             command=[sys.executable,str(base/'verify_readonly.py')],
             verifier_sha256=before[str(base/'verify_readonly.py')],
             stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
             stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
             observed_before=before,observed_after=after,
             observed_unchanged=before==after)
(out/'EXECUTION.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(exit_code=run.returncode,observed_files=len(before),
                     observed_unchanged=before==after,elapsed_seconds=elapsed),indent=2))
assert before==after
raise SystemExit(run.returncode)
