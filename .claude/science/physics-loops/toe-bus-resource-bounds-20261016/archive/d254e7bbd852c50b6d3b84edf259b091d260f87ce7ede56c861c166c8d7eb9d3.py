"""Preserve exact launch source and streams for one new quantitative check."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time
b=Path(__file__).resolve().parent;r=b/'check_run';r.mkdir(exist_ok=False)
def ident(p):
 d=p.read_bytes();return {'path':str(p),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()}
(r/'executed_source.py').write_bytes((b/'check_quantitative.py').read_bytes())
(r/'launcher_at_launch.py').write_bytes(Path(__file__).read_bytes())
argv=[sys.executable,'-B',str(r/'executed_source.py')]
x={'argv':argv,'cwd':str(b),'started_utc':datetime.now(timezone.utc).isoformat(),'source_at_launch':ident(r/'executed_source.py'),'launcher_at_launch':ident(r/'launcher_at_launch.py'),'limits':{'outer_timeout_seconds':40,'child_alarm_seconds':30,'physical_dimension_max':3,'Gram_dimension_max':6}}
(r/'LAUNCH.json').write_text(json.dumps(x,indent=2)+'\n');start=time.monotonic()
with (r/'stdout.json').open('wb') as out,(r/'stderr.txt').open('wb') as err:
 try:
  done=subprocess.run(argv,cwd=b,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=40);x['exit_code']=done.returncode;x['timed_out']=False
 except subprocess.TimeoutExpired:x['exit_code']=None;x['timed_out']=True
x.update({'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stdout':ident(r/'stdout.json'),'stderr':ident(r/'stderr.txt')})
(r/'EXECUTION.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x,indent=2))
sys.exit(x['exit_code'] if x['exit_code'] is not None else 124)
