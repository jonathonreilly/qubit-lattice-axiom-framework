from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
script = HERE / sys.argv[1]
stem = sys.argv[2]
assert script.parent == HERE and script.is_file()
assert not (HERE / (stem + '.receipt.json')).exists(), 'Never overwrite an attempt'
argv = [sys.executable, str(script), *sys.argv[3:]]
start = datetime.now(timezone.utc).isoformat()
clock = time.monotonic()
r = subprocess.run(argv, cwd=HERE, capture_output=True)
end = datetime.now(timezone.utc).isoformat()
stdout = HERE / (stem + '.stdout')
stderr = HERE / (stem + '.stderr')
stdout.write_bytes(r.stdout)
stderr.write_bytes(r.stderr)
def entry(p):
    b = p.read_bytes()
    return dict(path=str(p), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
receipt = dict(argv=argv, cwd=str(HERE), started_utc=start, ended_utc=end,
               wall_seconds=time.monotonic()-clock, returncode=r.returncode,
               script=entry(script), stdout=entry(stdout), stderr=entry(stderr))
(HERE / (stem + '.receipt.json')).write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(r.returncode)
