"""Run an independent control once; preserve complete streams and receipt."""
import datetime
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
name, script, *arguments = sys.argv[1:]
targets = [base/f'{name}.stdout', base/f'{name}.stderr', base/f'{name}.receipt.json']
for target in targets:
    if target.exists():
        raise FileExistsError(target)
source = base/script
command = [sys.executable, str(source), *arguments]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
run = subprocess.run(command, cwd=base, capture_output=True)
targets[0].write_bytes(run.stdout)
targets[1].write_bytes(run.stderr)
receipt = {
    'command_argv': command, 'cwd': str(base), 'started_utc': started,
    'finished_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'elapsed_seconds': time.monotonic()-tick, 'exit_code': run.returncode,
    'python': sys.version, 'platform': platform.platform(),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(),
    'stderr_sha256': hashlib.sha256(run.stderr).hexdigest(),
}
targets[2].write_text(json.dumps(receipt, indent=2)+'\n')
sys.stdout.buffer.write(run.stdout)
sys.stderr.buffer.write(run.stderr)
raise SystemExit(run.returncode)
