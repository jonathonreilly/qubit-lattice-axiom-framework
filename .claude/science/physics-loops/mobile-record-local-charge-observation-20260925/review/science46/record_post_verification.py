"""Explicit output writer for one inspected read-only POST46 verifier run.

Does not execute any historical/author program. Never rewrites an attempt.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
code = D / 'verify_post_readonly.py'
dest = D / 'post_verification_attempt01'
assert not dest.exists()
dest.mkdir()
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def identity(p):
    s = p.stat()
    return dict(path=str(p), sha256=sha(p), bytes=s.st_size,
                mtime_ns=s.st_mtime_ns, mode=s.st_mode, inode=s.st_ino)
pins = json.loads((D / 'POST_SOURCE_PINS.json').read_text())
baseline = json.loads((D / 'POST_PRESERVATION_BASELINE.json').read_text())
paths = {Path(r['path']) for r in baseline['files']}
paths.update(D / r['snapshot'] for r in pins['sources'])
paths.update([code, D / 'record_post_verification.py', D / 'POST_SOURCE_PINS.json',
              D / 'POST_PRESERVATION_BASELINE.json', D / 'capture_post_sources.py',
              D / 'POST_CAPTURE.stdout.json', D / 'POST_CAPTURE.stderr.txt'])
before = [identity(p) for p in sorted(paths)]
(dest / 'source.py').write_bytes(code.read_bytes())
started = datetime.now(timezone.utc).isoformat()
command = [sys.executable, '-B', str(code)]
clock = time.perf_counter()
proc = subprocess.run(command, cwd=D, capture_output=True)
elapsed = time.perf_counter()-clock
(dest / 'stdout.json').write_bytes(proc.stdout)
(dest / 'stderr.txt').write_bytes(proc.stderr)
after = [identity(p) for p in sorted(paths)]
receipt = dict(started_utc=started, command=command, cwd=str(D),
    elapsed_seconds=elapsed, exit_code=proc.returncode, source_sha256=sha(code),
    stdout_sha256=sha(dest / 'stdout.json'), stderr_sha256=sha(dest / 'stderr.txt'),
    observed_files=len(before), all_byte_stat_unchanged=before == after,
    before=before, after=after)
(dest / 'EXECUTION.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
print(json.dumps({k: v for k, v in receipt.items() if k not in ('before', 'after')}, indent=2))
assert before == after
assert proc.returncode == 0, 'Failed run and its complete streams are preserved; no overwrite permitted.'
