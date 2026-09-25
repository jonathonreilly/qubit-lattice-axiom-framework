"""Execute only an explicitly supplied local comparison utility; preserve each run.

This recorder writes exclusive-create logs only beside itself. The checker it
runs is separate and must not write files, import author programs, or run them.
"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
tag, source = sys.argv[1:]
program = HERE / source
assert program.parent == HERE and program.is_file()
targets = [HERE / f"{tag}.{x}" for x in ("stdout.txt", "stderr.txt", "execution.json")]
assert not any(p.exists() for p in targets)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
before = hashlib.sha256(program.read_bytes()).hexdigest()
begin = time.monotonic()
result = subprocess.run([sys.executable, str(program)], cwd=HERE, capture_output=True)
elapsed = time.monotonic() - begin
after = hashlib.sha256(program.read_bytes()).hexdigest()
assert before == after
for p, body in zip(targets[:2], (result.stdout, result.stderr)):
    with p.open("xb") as out:
        out.write(body)
receipt = {
    "started_utc": started, "command": [sys.executable, str(program)],
    "cwd": str(HERE), "source_sha256_before_and_after": before,
    "exit_code": result.returncode, "elapsed_seconds": elapsed,
    "stdout_bytes": len(result.stdout), "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
    "stderr_bytes": len(result.stderr), "stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
}
with targets[2].open("x") as out:
    json.dump(receipt, out, indent=2)
    out.write("\n")
print(json.dumps(receipt, indent=2))
sys.exit(result.returncode)
