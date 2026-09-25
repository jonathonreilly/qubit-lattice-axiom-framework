from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
script=ROOT/'post_check_evidence.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
start=datetime.now(timezone.utc).isoformat();timer=time.perf_counter()
with (ROOT/'post_check_evidence.stdout.txt').open('wb') as out,(ROOT/'post_check_evidence.stderr.txt').open('wb') as err:
    p=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=out,stderr=err)
record=dict(command=[sys.executable,str(script)],cwd=str(ROOT),started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),
            wall_seconds=time.perf_counter()-timer,exit_code=p.returncode,python=sys.version,platform=platform.platform(),
            script_sha256=sha(script),stdout_sha256=sha(ROOT/'post_check_evidence.stdout.txt'),stderr_sha256=sha(ROOT/'post_check_evidence.stderr.txt'))
if (ROOT/'POST_CHECK_RESULTS.json').exists():record['result_sha256']=sha(ROOT/'POST_CHECK_RESULTS.json')
(ROOT/'POST_CHECK_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
raise SystemExit(p.returncode)
