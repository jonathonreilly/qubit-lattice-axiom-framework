"""Capture one actual read-only checkout observation and complete streams."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
label=sys.argv[1];argv=sys.argv[2:]
assert label.replace('_','').isalnum()
assert argv[:2] in [['git','rev-parse'],['git','branch'],['git','status'],['gh','pr']]
if argv[0]=='gh':assert argv[2]=='view'
if argv[1]=='branch':assert argv==['git','branch','--show-current']
if argv[1]=='status':assert argv==['git','status','--porcelain','-z']
D=N/'runs'/label;D.mkdir(exist_ok=False)
def pin(p):
 b=Path(p).read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def now():return datetime.now(timezone.utc).isoformat()
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
cap=D/'recorder_at_launch.py';cap.write_bytes(Path(__file__).read_bytes())
r=dict(argv=argv,cwd=str(W),start_utc=now(),recorder=pin(Path(__file__)),recorder_capture=pin(cap),timeout_seconds=60,child_source_at_launch=None)
write(D/'LAUNCH.json',r);t=time.monotonic()
with (D/'stdout').open('wb') as out,(D/'stderr').open('wb') as err:
 try:p=subprocess.run(argv,cwd=W,stdout=out,stderr=err,stdin=subprocess.DEVNULL,timeout=60);code=p.returncode;timed=False
 except subprocess.TimeoutExpired:code=124;timed=True
r.update(end_utc=now(),elapsed_seconds=time.monotonic()-t,exit_code=code,timed_out=timed,stdout=pin(D/'stdout'),stderr=pin(D/'stderr'))
write(D/'EXECUTION.json',r);print(json.dumps(r));raise SystemExit(code)
