from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time

N=Path(__file__).resolve().parent
T=N.parent
label=sys.argv[1]
assert label and '/' not in label and label not in ['.','..']
D=N/'runs'/label
D.mkdir(parents=True,exist_ok=False)
argv=sys.argv[2:]
assert len(argv)>1 and Path(argv[0]).name.startswith('python')
source_path=Path(argv[1])
assert source_path.is_absolute() and source_path.is_file()
def pin(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
source=pin(source_path)
(D/'executed_source.py').write_bytes(source_path.read_bytes())
capture=pin(D/'executed_source.py')
assert source['sha256']==capture['sha256'] and source['bytes']==capture['bytes']
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
t=time.monotonic()
p=subprocess.run(argv,cwd=T,capture_output=True)
(D/'stdout').write_bytes(p.stdout)
(D/'stderr').write_bytes(p.stderr)
r={'argv':argv,'cwd':str(T),'start_utc':start,
   'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'elapsed_seconds':time.monotonic()-t,'exit_code':p.returncode,
   'stdout':pin(D/'stdout'),'stderr':pin(D/'stderr'),
   'child_source_at_launch':source,'source_capture':capture,'recorder':pin(Path(__file__))}
(D/'EXECUTION.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
if len(p.stdout)<=10000:
    print(p.stdout.decode(errors='replace'))
if p.returncode and len(p.stderr)<=10000:
    print(p.stderr.decode(errors='replace'))
sys.exit(p.returncode)
