from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
script=ROOT/'freeze_post_sources.py';start=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
with (ROOT/'freeze_post_sources.stdout.txt').open('wb') as out,(ROOT/'freeze_post_sources.stderr.txt').open('wb') as err:
    p=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=out,stderr=err)
record=dict(command=[sys.executable,str(script)],cwd=str(ROOT),started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),
            elapsed_seconds=time.perf_counter()-clock,exit_code=p.returncode,script_sha256=sha(script),
            stdout_sha256=sha(ROOT/'freeze_post_sources.stdout.txt'),stderr_sha256=sha(ROOT/'freeze_post_sources.stderr.txt'))
if (ROOT/'POST_SOURCE_PINS.json').exists():record['result_sha256']=sha(ROOT/'POST_SOURCE_PINS.json')
(ROOT/'POST_FREEZE_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));raise SystemExit(p.returncode)
