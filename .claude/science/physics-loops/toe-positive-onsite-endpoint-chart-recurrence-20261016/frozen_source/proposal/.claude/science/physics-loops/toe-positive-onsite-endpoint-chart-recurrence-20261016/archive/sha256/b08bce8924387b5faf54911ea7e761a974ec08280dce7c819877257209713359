"""Execute only a named new packaging program with original actual receipts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys,time
O=Path(__file__).resolve().parent
label,expected,source=sys.argv[1:4]; expected=int(expected); source=Path(source).resolve()
assert label and '/' not in label and label not in ['.','..']
assert O in source.parents
run=O/'metadata_runs'/label; run.mkdir(parents=True,exist_ok=False)
def pin(p):
    b=p.read_bytes(); return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def now(): return datetime.now(timezone.utc).isoformat()
capture=run/'source_at_launch.py'; capture.write_bytes(source.read_bytes())
recorder=run/'recorder_at_launch.py'; recorder.write_bytes(Path(__file__).read_bytes())
argv=[sys.executable,'-B',str(capture)]+sys.argv[4:]
launch=dict(start_utc=now(),argv=argv,cwd=str(O),source_original=pin(source),source_at_launch=pin(capture),
            recorder_at_launch=pin(recorder),expected_exit=expected,timeout_seconds=60,
            scope='New source-only packaging metadata; no historical science execution')
(run/'LAUNCH.json').write_text(json.dumps(launch,indent=2)+'\n'); start=time.monotonic()
with (run/'stdout').open('wb') as out,(run/'stderr').open('wb') as err:
    try:
        result=subprocess.run(argv,cwd=O,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=60,check=False)
        code=result.returncode; timed=False
    except subprocess.TimeoutExpired: code=None; timed=True
record=dict(launch,end_utc=now(),elapsed_seconds=time.monotonic()-start,exit_code=code,timed_out=timed,
            stdout=pin(run/'stdout'),stderr=pin(run/'stderr'))
(run/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2)); print((run/'stdout').read_text()); print((run/'stderr').read_text())
sys.exit(0 if code==expected and not timed else 1)
