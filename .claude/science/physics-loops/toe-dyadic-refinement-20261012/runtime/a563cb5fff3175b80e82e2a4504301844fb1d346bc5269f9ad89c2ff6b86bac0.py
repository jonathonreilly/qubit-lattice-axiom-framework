"""Recorder writes complete inner streams and outer receipt before display."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time,os
root=Path(__file__).resolve().parent
target=root/sys.argv[1];name=sys.argv[2]
out=root/'runs'/name
out.mkdir(parents=True,exist_ok=False)
def sha(b):return hashlib.sha256(b).hexdigest()
cmd=[sys.executable,str(target)]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',OMP_NUM_THREADS='1')
receipt={'command':cmd,'cwd':str(root),'source_sha256':sha(target.read_bytes()),'protocol_sha256':sha((root/'CONTROL_SPEC.md').read_bytes()),'timeout_seconds':60,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(out/'PREEXEC.json').write_text(json.dumps(receipt,indent=2)+'\n')
start=time.monotonic()
try:
    p=subprocess.run(cmd,cwd=root,env=env,capture_output=True,timeout=60)
    stdout,stderr=p.stdout,p.stderr
    receipt.update(returncode=p.returncode,timed_out=False)
except subprocess.TimeoutExpired as e:
    stdout,stderr=e.stdout or b'',e.stderr or b''
    receipt.update(returncode=None,timed_out=True)
receipt.update(elapsed_seconds=time.monotonic()-start,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
(out/'INNER.stdout').write_bytes(stdout);(out/'INNER.stderr').write_bytes(stderr)
receipt.update(stdout_sha256=sha(stdout),stderr_sha256=sha(stderr),stdout_bytes=len(stdout),stderr_bytes=len(stderr))
(out/'INNER.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
outer={'inner_receipt_sha256':sha((out/'INNER.receipt.json').read_bytes()),'inner_stdout_sha256':sha(stdout),'inner_stderr_sha256':sha(stderr),'recorded_before_inspection':True,'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':receipt['source_sha256'],'status':'timeout' if receipt['timed_out'] else ('completed_zero' if receipt['returncode']==0 else 'completed_nonzero')}
(out/'OUTER.receipt.json.tmp').write_text(json.dumps(outer,indent=2)+'\n')
(out/'OUTER.receipt.json.tmp').replace(out/'OUTER.receipt.json')
print(json.dumps({'run':str(out),'outer':outer,'elapsed_seconds':receipt['elapsed_seconds']},indent=2))
