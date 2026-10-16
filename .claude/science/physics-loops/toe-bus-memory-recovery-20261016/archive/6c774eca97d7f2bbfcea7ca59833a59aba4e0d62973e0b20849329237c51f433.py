from pathlib import Path
import sys, subprocess, hashlib, json, datetime, time
out=Path(__file__).resolve().parent; run=out/'check_run'; run.mkdir(exist_ok=False)
def ident(p):
 b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
source=run/'executed_source.py'; source.write_bytes((out/'check_release_moments.py').read_bytes())
launcher=run/'launcher_at_launch.py'; launcher.write_bytes(Path(__file__).read_bytes())
argv=[sys.executable,'-B',str(source)]
rec={'argv':argv,'cwd':str(out),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_at_launch':ident(source),'launcher_at_launch':ident(launcher),
 'limits':{'child_alarm_seconds':30,'outer_timeout_seconds':40,'physical_matrix_dimension_max':64,'executions':1}}
(run/'LAUNCH.json').write_text(json.dumps(rec,indent=2)+'\n')
t=time.monotonic()
with (run/'stdout.json').open('wb') as stdout,(run/'stderr.txt').open('wb') as stderr:
 try:
  result=subprocess.run(argv,cwd=out,stdout=stdout,stderr=stderr,timeout=40,check=False)
  rec.update(exit_code=result.returncode,timed_out=False)
 except subprocess.TimeoutExpired:
  rec.update(exit_code=None,timed_out=True)
rec.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t,
 stdout=ident(run/'stdout.json'),stderr=ident(run/'stderr.txt'))
(run/'EXECUTION.json').write_text(json.dumps(rec,indent=2)+'\n'); print(json.dumps(rec,indent=2))
