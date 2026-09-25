"""New POST43 recorder; not a rerun of the sealed PRE recorder."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, os, subprocess, sys, time

HERE=Path(__file__).resolve().parent
label, script=sys.argv[1:3]
command=[sys.executable,'-B',str(HERE/script),*sys.argv[3:]]
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
run=subprocess.run(command,cwd=HERE,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
elapsed=time.perf_counter()-tick
logs={}
for name,data in [('stdout.txt',run.stdout),('stderr.txt',run.stderr)]:
    path=HERE/(label+'.'+name)
    with path.open('xb') as f: f.write(data)
    logs[name]=dict(path=path.name,sha256=sha256(data).hexdigest(),bytes=len(data))
receipt=dict(started_utc=started,command=command,source_sha256=sha256((HERE/script).read_bytes()).hexdigest(),
             recorder_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
             elapsed_seconds=elapsed,exit_code=run.returncode,outputs=logs)
with (HERE/(label+'.execution.json')).open('x') as f:
    json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
print(run.stdout.decode(),end='')
print(run.stderr.decode(),file=sys.stderr,end='')
raise SystemExit(run.returncode)
