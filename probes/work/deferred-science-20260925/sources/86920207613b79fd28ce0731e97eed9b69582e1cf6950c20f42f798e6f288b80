from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
script=ROOT/'prepared_probe_control.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
timer=time.perf_counter();start=datetime.now(timezone.utc).isoformat()
with (ROOT/'prepared_probe_control.stdout.txt').open('wb') as out,(ROOT/'prepared_probe_control.stderr.txt').open('wb') as err:
    p=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=out,stderr=err)
record=dict(command=[sys.executable,str(script)],cwd=str(ROOT),started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),
            wall_seconds=time.perf_counter()-timer,exit_code=p.returncode,python=sys.version,platform=platform.platform(),
            script_sha256=sha(script),stdout_sha256=sha(ROOT/'prepared_probe_control.stdout.txt'),stderr_sha256=sha(ROOT/'prepared_probe_control.stderr.txt'))
for field,name in [('result_sha256','CONTROL_RESULTS.json'),('path_certificate_sha256','PATH_CERTIFICATES.json')]:
    if (ROOT/name).exists():record[field]=sha(ROOT/name)
(ROOT/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
raise SystemExit(p.returncode)
