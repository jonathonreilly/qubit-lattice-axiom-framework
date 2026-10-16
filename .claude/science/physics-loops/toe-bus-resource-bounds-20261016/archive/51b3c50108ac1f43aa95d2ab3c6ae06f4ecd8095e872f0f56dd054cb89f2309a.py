#!/usr/bin/env python3
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
run = base/'run_002_provenance'
run.mkdir(exist_ok=False)
source = run/'executed_source.py'
source.write_bytes((base/'verify_provenance.py').read_bytes())
(run/'launcher_at_launch.py').write_bytes(Path(__file__).read_bytes())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = [sys.executable, '-B', str(source)]
launch = {'utc': utc(), 'argv': argv, 'cwd': str(base), 'timeout_seconds': 10,
          'source_at_launch_sha256': sha(source),
          'launcher_at_launch_sha256': sha(run/'launcher_at_launch.py')}
(run/'LAUNCH.json').write_text(json.dumps(launch, indent=2)+'\n')
start = time.monotonic()
with (run/'stdout.json').open('wb') as stdout, (run/'stderr.txt').open('wb') as stderr:
    try:
        result = subprocess.run(argv, cwd=base, stdin=subprocess.DEVNULL,
                                stdout=stdout, stderr=stderr, timeout=10, check=False)
        code, timeout = result.returncode, False
    except subprocess.TimeoutExpired:
        code, timeout = None, True
record = dict(launch, ended_utc=utc(), elapsed_seconds=time.monotonic()-start,
              exit_code=code, timed_out=timeout,
              stdout_sha256=sha(run/'stdout.json'), stderr_sha256=sha(run/'stderr.txt'))
(run/'EXECUTION.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
sys.exit(code if code is not None else 124)
