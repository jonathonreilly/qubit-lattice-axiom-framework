from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
script=ROOT/'post_control.py';start=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
with (ROOT/'post_control.stdout.txt').open('wb') as out,(ROOT/'post_control.stderr.txt').open('wb') as err:
    p=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=out,stderr=err)
record=dict(command=[sys.executable,str(script)],cwd=str(ROOT),started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),
            elapsed_seconds=time.perf_counter()-clock,exit_code=p.returncode,python=sys.version,platform=platform.platform(),
            script_sha256=sha(script),stdout_sha256=sha(ROOT/'post_control.stdout.txt'),stderr_sha256=sha(ROOT/'post_control.stderr.txt'))
for field,name in [('result_sha256','POST_CONTROL_RESULTS.json'),('paths_sha256','POST_PATH_CERTIFICATES.json')]:
    if (ROOT/name).exists():record[field]=sha(ROOT/name)
(ROOT/'POST_CONTROL_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));raise SystemExit(p.returncode)
