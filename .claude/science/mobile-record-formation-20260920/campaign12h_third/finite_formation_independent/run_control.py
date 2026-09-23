from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
here=Path(__file__).resolve().parent
script,prefix=sys.argv[1:]
p=here/script
assert p.resolve().parent==here
out=here/(prefix+'.stdout');err=here/(prefix+'.stderr');rec=here/(prefix+'_RECEIPT.json')
assert not any(q.exists() for q in (out,err,rec))
def row(q):
 b=q.read_bytes();return {'path':str(q),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
a=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
with out.open('wb') as f,err.open('wb') as g:r=subprocess.run([sys.executable,str(p)],stdout=f,stderr=g)
data={'started_utc':a,'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-clock,
 'command':[sys.executable,str(p)],'exit_code':r.returncode,'runner':row(p),'stdout':row(out),'stderr':row(err)}
rec.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2));print(err.read_text())
