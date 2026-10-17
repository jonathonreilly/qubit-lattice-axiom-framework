"""One launch-pinned bounded reviewer calculation; preserve failed attempts."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
run=ROOT/'runs'/sys.argv[1]
run.mkdir(parents=True,exist_ok=False)
script=ROOT/'check_weighted_escape.py'
def identity(p):
    data=p.read_bytes()
    return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
before=identity(script)
shutil.copyfile(script,run/'executed_source.py')
manifest=identity(ROOT/'SOURCE_PINS.json')
shutil.copyfile(ROOT/'SOURCE_PINS.json',run/'SOURCE_PINS_AT_LAUNCH.json')
argv=[sys.executable,str(script),'--output',str(run/'RESULT.json')]
started=datetime.now(timezone.utc).isoformat()
t0=time.monotonic()
timeout=False
with (run/'stdout').open('wb') as stdout,(run/'stderr').open('wb') as stderr:
    child=subprocess.Popen(argv,cwd=ROOT,stdout=stdout,stderr=stderr)
    try:
        status=child.wait(timeout=60)
    except subprocess.TimeoutExpired:
        timeout=True
        child.kill()
        status=child.wait()
receipt={'argv':argv,'cwd':str(ROOT),'start_utc':started,'end_utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':time.monotonic()-t0,'exit_code':status,'timed_out':timeout,
    'cpu_cap_seconds':45,'wall_cap_seconds':60,'source_at_launch':before,
    'source_after_execution':identity(script),'input_manifest_at_launch':manifest,
    'wrapper':identity(Path(__file__)),'stdout':identity(run/'stdout'),'stderr':identity(run/'stderr')}
if (run/'RESULT.json').exists(): receipt['result']=identity(run/'RESULT.json')
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(status if status>=0 else 1)
