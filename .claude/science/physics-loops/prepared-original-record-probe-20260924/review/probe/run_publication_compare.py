#!/usr/bin/env python3
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

here = Path(__file__).resolve().parent
script = here / 'publication_compare.py'
started = datetime.now(timezone.utc).isoformat()
tic = time.perf_counter()
run = subprocess.run([sys.executable, str(script)], cwd=here, capture_output=True)
elapsed = time.perf_counter()-tic
for name, data in [('publication_compare.stdout.txt',run.stdout),('publication_compare.stderr.txt',run.stderr)]:
    with (here/name).open('xb') as handle: handle.write(data)
receipt = dict(started_utc=started,executable=sys.executable,argv=[sys.executable,str(script)],
               cwd=str(here),elapsed_seconds=elapsed,exit_code=run.returncode,
               script_sha256=hashlib.sha256(script.read_bytes()).hexdigest(),
               stdout_bytes=len(run.stdout),stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
               stderr_bytes=len(run.stderr),stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
               scope='Read-only scientific source comparison, copying frozen inputs into independent directory; no primary execution.')
with (here/'PUBLICATION_COMPARE_EXECUTION.json').open('x') as handle:
    json.dump(receipt,handle,indent=2);handle.write('\n')
print(json.dumps(receipt,indent=2))
if run.returncode:
    print(run.stderr.decode(),file=sys.stderr)
sys.exit(run.returncode)
