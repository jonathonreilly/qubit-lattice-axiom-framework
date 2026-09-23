from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time
D=Path(__file__).resolve().parent
script,prefix=sys.argv[1:];p=D/script
assert p.resolve().parent==D
out,err,receipt=(D/(prefix+s) for s in ('.stdout','.stderr','_RECEIPT.json'))
assert not any(q.exists() for q in (out,err,receipt))
def row(q):
    b=q.read_bytes();return {'path':str(q),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
started=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
with out.open('wb') as f,err.open('wb') as g:
    r=subprocess.run([sys.executable,'-B',str(p)],stdout=f,stderr=g)
data={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
      'elapsed_seconds':time.perf_counter()-clock,'command':[sys.executable,'-B',str(p)],
      'exit_code':r.returncode,'runner':row(p),'stdout':row(out),'stderr':row(err)}
receipt.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2));print(err.read_text())
