#!/usr/bin/env python3
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
script=HERE/sys.argv[1];label=sys.argv[2];argv=[sys.executable,str(script)]+sys.argv[3:]
start=datetime.now(timezone.utc).isoformat();tic=time.perf_counter()
run=subprocess.run(argv,cwd=HERE,capture_output=True);elapsed=time.perf_counter()-tic
for suffix,raw in [('stdout.txt',run.stdout),('stderr.txt',run.stderr)]:
 with (HERE/(label+'.'+suffix)).open('xb') as f:f.write(raw)
receipt=dict(started_utc=start,argv=argv,cwd=str(HERE),elapsed_seconds=elapsed,exit_code=run.returncode,
 script_sha256=hashlib.sha256(script.read_bytes()).hexdigest(),
 stdout_bytes=len(run.stdout),stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
 stderr_bytes=len(run.stderr),stderr_sha256=hashlib.sha256(run.stderr).hexdigest())
with (HERE/(label+'.execution.json')).open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
if run.returncode:print(run.stderr.decode(),file=sys.stderr)
sys.exit(run.returncode)
