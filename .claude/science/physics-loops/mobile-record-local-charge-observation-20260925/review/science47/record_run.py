"""New explicit logger; does not modify the child program or earlier receipts."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
label, program = sys.argv[1:3]
path = HERE / program
assert path.parent == HERE and path.exists()
assert not (HERE / (label + '.execution.json')).exists()
command = [sys.executable, '-B', str(path)] + sys.argv[3:]
start = datetime.now(timezone.utc).isoformat()
t0 = time.monotonic()
result = subprocess.run(command, cwd=HERE, capture_output=True)
receipt = {'started_utc': start, 'command': command,
           'source_sha256': sha256(path.read_bytes()).hexdigest(),
           'recorder_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - t0, 'exit_code': result.returncode,
           'outputs': {}}
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
