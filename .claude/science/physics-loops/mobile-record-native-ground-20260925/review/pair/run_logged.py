#!/usr/bin/env python3
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent
script=HERE/sys.argv[1];label=sys.argv[2]
argv=[sys.executable,str(script)]+sys.argv[3:]
start=datetime.now(timezone.utc).isoformat();tic=time.perf_counter()
run=subprocess.run(argv,cwd=HERE,capture_output=True)
receipt=dict(started_utc=start,argv=argv,cwd=str(HERE),elapsed_seconds=time.perf_counter()-tic,
 exit_code=run.returncode,script_sha256=hashlib.sha256(script.read_bytes()).hexdigest())
for stream,raw in [('stdout',run.stdout),('stderr',run.stderr)]:
 with (HERE/(label+'.'+stream+'.txt')).open('xb') as out:out.write(raw)
 receipt[stream+'_bytes']=len(raw);receipt[stream+'_sha256']=hashlib.sha256(raw).hexdigest()
with (HERE/(label+'.execution.json')).open('x') as out:json.dump(receipt,out,indent=2);out.write('\n')
print(json.dumps(receipt,indent=2))
if run.returncode:print(run.stderr.decode(),file=sys.stderr)
sys.exit(run.returncode)
