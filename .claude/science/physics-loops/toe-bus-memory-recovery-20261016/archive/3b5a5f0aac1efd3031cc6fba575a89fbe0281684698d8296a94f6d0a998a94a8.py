"""Record an actual metadata-only source-capture execution; no science run."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

o = Path(__file__).resolve().parent
r = o/'metadata_capture'
r.mkdir(exist_ok=False)
source = o/'capture_sources.py'
data = source.read_bytes()
captured = r/'executed_source.py'
captured.write_bytes(data)
# Execute the original path so its directory is the intended output root;
# the immutable source-at-launch bytes are captured immediately beforehand.
argv = [sys.executable, '-B', str(source)]
started = datetime.now(timezone.utc).isoformat()
result = subprocess.run(argv, cwd=str(o), capture_output=True)
ended = datetime.now(timezone.utc).isoformat()
(r/'stdout').write_bytes(result.stdout)
(r/'stderr').write_bytes(result.stderr)
def digest(b):
    return hashlib.sha256(b).hexdigest()
receipt = dict(kind='metadata-only source identity/capture execution', scientific_execution=False,
    started_utc=started, ended_utc=ended, argv=argv, cwd=str(o), exit_code=result.returncode,
    launcher_sha256=digest(Path(__file__).read_bytes()), source=str(source),
    source_at_launch='metadata_capture/executed_source.py', source_bytes=len(data), source_sha256=digest(data),
    source_unchanged_after_run=(source.read_bytes()==data),
    stdout=dict(path='metadata_capture/stdout', bytes=len(result.stdout), sha256=digest(result.stdout)),
    stderr=dict(path='metadata_capture/stderr', bytes=len(result.stderr), sha256=digest(result.stderr)))
(r/'EXECUTION.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
if result.stdout:
    print(result.stdout.decode(), end='')
if result.stderr:
    print(result.stderr.decode(), end='', file=sys.stderr)
sys.exit(result.returncode)
