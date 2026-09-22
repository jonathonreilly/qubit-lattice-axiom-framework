"""Run a named independent local checker once, retaining complete streams."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys,time
here=Path(__file__).resolve().parent
script,prefix=sys.argv[1:]
runner=(here/script).resolve()
assert runner.parent==here
stdout=here/(prefix+'.stdout');stderr=here/(prefix+'.stderr')
receipt=here/(prefix+'_RECEIPT.json')
assert not any(p.exists() for p in (stdout,stderr,receipt)),'Preserve existing attempts.'
command=[sys.executable,str(runner)]
start=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
with stdout.open('wb') as out,stderr.open('wb') as err:
    result=subprocess.run(command,stdout=out,stderr=err,check=False)
def row(path):
    b=path.read_bytes();return {'path':str(path),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
data={'started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),
      'elapsed_seconds':time.perf_counter()-clock,'command':command,'exit_code':result.returncode,
      'runner':row(runner),'stdout':row(stdout),'stderr':row(stderr)}
receipt.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2));print(stderr.read_text())
