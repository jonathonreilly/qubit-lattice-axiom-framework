#!/usr/bin/env python3
"""Capture actual source-at-launch, argv/cwd, limits, exit, and full streams."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
run = base / 'run_001'
run.mkdir(exist_ok=False)
source = base / 'independent_bitstring_check.py'
executed = run / 'executed_source.py'
executed.write_bytes(source.read_bytes())
(run / 'launcher_at_launch.py').write_bytes(Path(__file__).read_bytes())
argv = [sys.executable, '-B', str(executed)]
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
launch = {'utc': utc(), 'argv': argv, 'cwd': str(base), 'timeout_seconds': 60,
          'python_version': sys.version, 'source_at_launch_sha256': digest(executed),
          'launcher_at_launch_sha256': digest(run/'launcher_at_launch.py'),
          'analytic_findings_sha256': digest(base/'ANALYTIC_FINDINGS.md'),
          'sources': json.loads((base/'SOURCE_MANIFEST.json').read_text())}
(run/'LAUNCH.json').write_text(json.dumps(launch, indent=2)+'\n')
start = time.monotonic()
with (run/'stdout.json').open('wb') as stdout, (run/'stderr.txt').open('wb') as stderr:
    try:
        child = subprocess.run(argv, cwd=base, stdin=subprocess.DEVNULL,
                               stdout=stdout, stderr=stderr, timeout=60, check=False)
        exit_code, timed_out = child.returncode, False
    except subprocess.TimeoutExpired:
        exit_code, timed_out = None, True
execution = {'started_utc': launch['utc'], 'ended_utc': utc(),
             'elapsed_seconds': time.monotonic()-start, 'exit_code': exit_code,
             'timed_out': timed_out, 'argv': argv, 'cwd': str(base),
             'source_at_launch_sha256': digest(executed),
             'stdout_sha256': digest(run/'stdout.json'),
             'stderr_sha256': digest(run/'stderr.txt'),
             'stdout_bytes': (run/'stdout.json').stat().st_size,
             'stderr_bytes': (run/'stderr.txt').stat().st_size}
(run/'EXECUTION.json').write_text(json.dumps(execution, indent=2)+'\n')
print(json.dumps(execution, indent=2))
sys.exit(exit_code if exit_code is not None else 124)
