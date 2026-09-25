"""New-packet execution recorder; writes exclusive local logs, never source inputs."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent
name,program=sys.argv[1:]
p=HERE/program
assert p.parent==HERE and p.is_file()
paths=[HERE/f'{name}.{s}' for s in ['stdout.txt','stderr.txt','execution.json']]
assert not any(p.exists() for p in paths)
sha=lambda b:hashlib.sha256(b).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); code=sha(p.read_bytes());tick=time.monotonic()
r=subprocess.run([sys.executable,str(p)],cwd=HERE,capture_output=True)
elapsed=time.monotonic()-tick
assert sha(p.read_bytes())==code
for path,body in zip(paths,[r.stdout,r.stderr]):
 with path.open('xb') as f:f.write(body)
receipt={'started_utc':started,'command':[sys.executable,str(p)],'source_sha256':code,'elapsed_seconds':elapsed,'exit_code':r.returncode,'stdout_sha256':sha(r.stdout),'stdout_bytes':len(r.stdout),'stderr_sha256':sha(r.stderr),'stderr_bytes':len(r.stderr)}
with paths[2].open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2));sys.exit(r.returncode)
