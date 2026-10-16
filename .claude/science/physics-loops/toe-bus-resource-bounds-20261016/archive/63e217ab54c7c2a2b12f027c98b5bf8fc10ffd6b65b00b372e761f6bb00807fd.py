"""Capture executable and launcher before this single bounded new exact calculation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,time
O=Path(__file__).resolve().parent
R=O/'runs/exact_gram';R.mkdir(parents=True,exist_ok=False)
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def now():return datetime.now(timezone.utc).isoformat()
source=O/'exact_gram_check.py';launcher=Path(__file__).resolve()
(R/'executed_source.py').write_bytes(source.read_bytes());(R/'launcher_source.py').write_bytes(launcher.read_bytes())
(R/'source_inputs.json').write_bytes((O/'SOURCE_MANIFEST.json').read_bytes())
argv=[sys.executable,'-B',str(R/'executed_source.py'),str(O)]
receipt={'argv':argv,'cwd':str(O),'start_utc':now(),'source_at_launch':pin(source),'source_capture':pin(R/'executed_source.py'),
 'launcher_at_launch':pin(launcher),'launcher_capture':pin(R/'launcher_source.py'),'source_inputs':pin(R/'source_inputs.json'),
 'timeout_seconds':60,'scope':'New bounded exposed numerical check; no old-checker replay, Git or canonical mutation.'}
(R/'LAUNCH.json').write_text(json.dumps(receipt,indent=2)+'\n');start=time.monotonic()
env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
with (R/'stdout').open('wb') as out,(R/'stderr').open('wb') as err:
 try:r=subprocess.run(argv,cwd=O,env=env,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=60);code=r.returncode;timeout=False
 except subprocess.TimeoutExpired:code=None;timeout=True
receipt.update(end_utc=now(),elapsed_seconds=time.monotonic()-start,exit_code=code,timed_out=timeout,stdout=pin(R/'stdout'),stderr=pin(R/'stderr'))
(R/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));sys.exit(0 if code==0 else 1)
