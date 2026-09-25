#!/usr/bin/env python3
"""POST evidence writer around a genuinely read-only comparison verifier."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time
base=Path(__file__).resolve().parent
out=base/'post_verification_attempt01'
assert not out.exists()
pre=json.loads((base/'PRE_SEAL.json').read_text())
new=json.loads((base/'POST_SOURCE_PINS.json').read_text())
paths=[base/row['path'] for row in pre['members']]+[base/'PRE_SEAL.json',base/'POST_SOURCE_PINS.json',base/'post_verify_readonly.py',base/'post_record_verification.py',base/'post_capture_sources.py']
for row in new['sources']:
    paths.extend([Path(row['origin']),base/row['snapshot']])
for row in json.loads((base/'SOURCE_PINS.json').read_text())['sources']:
    if '/docs/' in row['origin'] and '/ai_methodology/' not in row['origin']:
        paths.append(Path(row['origin']))
def inventory():
    return {str(p):dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),size=p.stat().st_size,
                        mtime_ns=p.stat().st_mtime_ns,mode=p.stat().st_mode) for p in paths}
before=inventory()
start=datetime.now(timezone.utc).isoformat(); t0=time.perf_counter()
run=subprocess.run([sys.executable,str(base/'post_verify_readonly.py')],cwd=base,capture_output=True)
elapsed=time.perf_counter()-t0
after=inventory()
out.mkdir()
(out/'stdout.json').write_bytes(run.stdout)
(out/'stderr.txt').write_bytes(run.stderr)
receipt=dict(started_utc=start,elapsed_seconds=elapsed,exit_code=run.returncode,
             command=[sys.executable,str(base/'post_verify_readonly.py')],
             verifier_sha256=before[str(base/'post_verify_readonly.py')]['sha256'],
             stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
             observed_before=before,observed_after=after,observed_unchanged=before==after)
(out/'EXECUTION.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(exit_code=run.returncode,elapsed_seconds=elapsed,
                     observed_files=len(before),observed_byte_stat_unchanged=before==after),indent=2))
assert before==after
raise SystemExit(run.returncode)
