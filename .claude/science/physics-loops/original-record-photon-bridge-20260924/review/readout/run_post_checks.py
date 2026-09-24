#!/usr/bin/env python3
"""Capture the own bounded POST evidence comparison only."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

here = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
command = [sys.executable, str(here / 'post_compare_evidence.py')]
started = datetime.now(timezone.utc).isoformat()
timer = time.perf_counter()
with (here / 'post_compare_evidence.stdout.txt').open('wb') as stdout, \
     (here / 'post_compare_evidence.stderr.txt').open('wb') as stderr:
    process = subprocess.run(command, cwd=here, stdout=stdout, stderr=stderr)
out = {'command': command, 'started_utc': started, 'elapsed_seconds': time.perf_counter() - timer,
       'exit_code': process.returncode, 'runner_sha256': sha(Path(__file__).resolve()),
       'script_sha256': sha(here / 'post_compare_evidence.py'),
       'POST_SOURCE_PINS_sha256': sha(here / 'POST_SOURCE_PINS.json'),
       'stdout_sha256': sha(here / 'post_compare_evidence.stdout.txt'),
       'stderr_sha256': sha(here / 'post_compare_evidence.stderr.txt'),
       'scope': 'Own correspondence only; no author control run or independent reproduction claim.'}
(here / 'POST_CHECK_EXECUTION.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, sort_keys=True), flush=True)
sys.exit(process.returncode)
