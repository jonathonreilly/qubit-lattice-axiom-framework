from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time

ROOT=Path(__file__).resolve().parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
script=ROOT/'verify_evidence.py'
start=datetime.now(timezone.utc).isoformat();timer=time.perf_counter()
with (ROOT/'verify_evidence.stdout.txt').open('wb') as stdout, (ROOT/'verify_evidence.stderr.txt').open('wb') as stderr:
    p=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=stdout,stderr=stderr)
result=dict(started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-timer,
            command=[sys.executable,str(script)],cwd=str(ROOT),exit_code=p.returncode,
            script_sha256=sha(script),stdout_sha256=sha(ROOT/'verify_evidence.stdout.txt'),
            stderr_sha256=sha(ROOT/'verify_evidence.stderr.txt'))
if (ROOT/'EVIDENCE_VERIFICATION.json').exists(): result['result_sha256']=sha(ROOT/'EVIDENCE_VERIFICATION.json')
(ROOT/'VERIFY_EXECUTION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
raise SystemExit(p.returncode)
