"""New POST-only execution logger. No historical writer is invoked."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
label, script = sys.argv[1:3]
assert label.startswith('post_')
program = HERE / script
assert program.parent == HERE and program.exists()
assert not (HERE / (label + '.execution.json')).exists()
command = [sys.executable, '-B', str(program)] + sys.argv[3:]
started = datetime.now(timezone.utc).isoformat(); t0 = time.monotonic()
source_hash = sha256(program.read_bytes()).hexdigest()
result = subprocess.run(command, cwd=HERE, capture_output=True)
receipt = {'started_utc': started, 'command': command, 'source_sha256': source_hash,
           'recorder_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - t0, 'exit_code': result.returncode,
           'outputs': {}}
assert sha256(program.read_bytes()).hexdigest() == source_hash
for suffix, raw in [('stdout.txt', result.stdout), ('stderr.txt', result.stderr)]:
    name = label + '.' + suffix
    with (HERE / name).open('xb') as stream:
        stream.write(raw)
    receipt['outputs'][suffix] = {'path': name, 'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
with (HERE / (label + '.execution.json')).open('x') as stream:
    stream.write(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
print(result.stdout.decode(), end='')
if result.stderr:
    print(result.stderr.decode(), end='', file=sys.stderr)
sys.exit(result.returncode)
