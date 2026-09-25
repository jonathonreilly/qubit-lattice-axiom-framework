#!/usr/bin/env python3
"""Explicit evidence WRITER around the inspected read-only PRE46 verifier."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time

BASE=Path(__file__).resolve().parent
OUT=BASE/'verification_attempt01'
assert not OUT.exists()
sources=json.loads((BASE/'SOURCE_PINS.json').read_text())['sources']
paths=sorted({p for p in BASE.rglob('*') if p.is_file()} | {Path(r['origin']) for r in sources})
def inventory():
    return {str(p):dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,
                        mode=p.stat().st_mode,mtime_ns=p.stat().st_mtime_ns) for p in paths}
before=inventory();code=BASE/'verify_readonly.py';raw=code.read_bytes()
started=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
run=subprocess.run([sys.executable,str(code)],cwd=BASE,capture_output=True)
elapsed=time.perf_counter()-tick;after=inventory();OUT.mkdir()
(OUT/'source.py').write_bytes(raw);(OUT/'stdout.json').write_bytes(run.stdout);(OUT/'stderr.txt').write_bytes(run.stderr)
receipt=dict(started_utc=started,elapsed_seconds=elapsed,exit_code=run.returncode,
             command=[sys.executable,str(code)],source_sha256=hashlib.sha256(raw).hexdigest(),
             stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
             observed_before=before,observed_after=after,all_byte_stat_unchanged=before==after)
(OUT/'EXECUTION.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(exit_code=run.returncode,elapsed_seconds=elapsed,observed_files=len(paths),
                     all_byte_stat_unchanged=before==after,stdout_sha256=receipt['stdout_sha256']),indent=2))
assert before==after
raise SystemExit(run.returncode)
