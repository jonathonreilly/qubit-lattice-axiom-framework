"""Bounded launcher. Captures the exact child source before its one run."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
source = root/'check_bounds.py'
raw = source.read_bytes()
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
t0 = time.monotonic()
result = subprocess.run([sys.executable, str(source)], capture_output=True, timeout=10)
elapsed = time.monotonic()-t0
for name, value in [('stdout', result.stdout), ('stderr', result.stderr)]:
    (root/name).write_bytes(value)
receipt = {'start_utc': start, 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'elapsed_seconds': elapsed, 'exit_code': result.returncode,
           'command': [sys.executable, str(source)],
           'source_at_launch': {'path': str(source), 'bytes': len(raw),
                                'sha256': hashlib.sha256(raw).hexdigest()},
           'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
           'stderr_sha256': hashlib.sha256(result.stderr).hexdigest(),
           'caps': {'cpu_seconds': 5, 'wall_seconds': 10,
                    'matrix_dimension': 0, 'quadrature': False, 'dynamics': False}}
(root/'EXECUTION.json').write_text(json.dumps(receipt, indent=2)+'\n')
sys.stdout.buffer.write(result.stdout)
sys.stderr.buffer.write(result.stderr)
sys.exit(result.returncode)
