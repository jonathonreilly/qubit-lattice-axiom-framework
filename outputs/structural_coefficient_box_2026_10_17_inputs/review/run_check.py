"""Record one bounded child invocation without replacing historical evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
run = ROOT / 'runs' / sys.argv[1]
run.mkdir(parents=True, exist_ok=False)
script = ROOT / 'check_structural_box.py'


def identity(path):
    raw = path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


before = identity(script)
shutil.copyfile(script,run/'executed_source.py')
pin_before = identity(ROOT/'SOURCE_PINS.json')
shutil.copyfile(ROOT/'SOURCE_PINS.json',run/'SOURCE_PINS_AT_LAUNCH.json')
argv = [sys.executable,str(script),'--output',str(run/'RESULT.json')]
start_utc = datetime.now(timezone.utc).isoformat()
started = time.monotonic()
timed_out = False
with (run/'stdout').open('wb') as out, (run/'stderr').open('wb') as err:
    child = subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=err)
    try:
        status = child.wait(timeout=60)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        status = child.wait()
receipt = {'argv':argv,'cwd':str(ROOT),'start_utc':start_utc,
    'end_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,
    'exit_code':status,'timed_out':timed_out,'cpu_cap_seconds':45,'wall_cap_seconds':60,
    'source_at_launch':before,'source_after_execution':identity(script),
    'input_manifest_at_launch':pin_before,'wrapper':identity(Path(__file__)),
    'stdout':identity(run/'stdout'),'stderr':identity(run/'stderr')}
if (run/'RESULT.json').exists():
    receipt['result'] = identity(run/'RESULT.json')
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(status if status >= 0 else 1)
