"""New subpacket logger; old recorders and sealed writers are not invoked."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
label, filename = sys.argv[1:3]
program = HERE / filename
assert program.parent == HERE and not (HERE / (label + '.execution.json')).exists()
command = [sys.executable, '-B', str(program)]
started = datetime.now(timezone.utc).isoformat()
source_hash = sha256(program.read_bytes()).hexdigest()
t0 = time.monotonic()
run = subprocess.run(command, cwd=HERE, capture_output=True)
receipt = dict(started_utc=started, command=command, source_sha256=source_hash,
               recorder_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               elapsed_seconds=time.monotonic() - t0, exit_code=run.returncode, outputs={})
assert sha256(program.read_bytes()).hexdigest() == source_hash
for kind, raw in [('stdout.txt', run.stdout), ('stderr.txt', run.stderr)]:
    name = label + '.' + kind
    with (HERE / name).open('xb') as out:
        out.write(raw)
    receipt['outputs'][kind] = dict(path=name, sha256=sha256(raw).hexdigest(), bytes=len(raw))
with (HERE / (label + '.execution.json')).open('x') as out:
    out.write(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
print(run.stdout.decode(), end='')
if run.stderr:
    print(run.stderr.decode(), end='', file=sys.stderr)
sys.exit(run.returncode)
