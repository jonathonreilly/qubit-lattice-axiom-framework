"""Record only the new read-only correspondence checker, preserving each attempt."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
folders = [HERE / ('verification_attempt%02d' % n) for n in range(1, 100)]
target = next(p for p in folders if not p.exists())
target.mkdir()
command = [sys.executable, '-B', str(HERE / 'verify_correspondence.py')]
start = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
run = subprocess.run(command, cwd=HERE, capture_output=True)
elapsed = time.perf_counter() - tick
(target / 'stdout.json').write_bytes(run.stdout)
(target / 'stderr.txt').write_bytes(run.stderr)
record = {'started_utc': start, 'command': command,
          'purpose': 'Execute our new read-only source/payload/cache correspondence checker only.',
          'elapsed_seconds': elapsed, 'exit_code': run.returncode,
          'checker_sha256': hashlib.sha256((HERE / 'verify_correspondence.py').read_bytes()).hexdigest(),
          'stdout_bytes': len(run.stdout), 'stderr_bytes': len(run.stderr),
          'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(),
          'stderr_sha256': hashlib.sha256(run.stderr).hexdigest()}
(target / 'EXECUTION.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'attempt': target.name, **record}, indent=2))
if run.returncode:
    print(run.stderr.decode(), file=sys.stderr)
sys.exit(run.returncode)
