"""POST-only execution recorder. Child verifier itself remains read-only."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, os, subprocess, sys, time

HERE=Path(__file__).resolve().parent
label,script=sys.argv[1:3]
command=[sys.executable,'-B',str(HERE/script)]
start=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
run=subprocess.run(command,cwd=HERE,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
elapsed=time.perf_counter()-tick
paths={}
for suffix,data in [('stdout.txt',run.stdout),('stderr.txt',run.stderr)]:
    path=HERE/(label+'.'+suffix)
    with path.open('xb') as stream:stream.write(data)
    paths[suffix]={'path':path.name,'bytes':len(data),'sha256':sha256(data).hexdigest()}
receipt={'at_utc':start,'command':command,'source_sha256':sha256((HERE/script).read_bytes()).hexdigest(),
         'recorder_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'elapsed_seconds':elapsed,'exit_code':run.returncode,'outputs':paths}
with (HERE/(label+'.execution.json')).open('x') as stream:json.dump(receipt,stream,indent=2);stream.write('\n')
print(json.dumps(receipt,indent=2))
print(run.stdout.decode(),end='')
print(run.stderr.decode(),file=sys.stderr,end='')
raise SystemExit(run.returncode)
