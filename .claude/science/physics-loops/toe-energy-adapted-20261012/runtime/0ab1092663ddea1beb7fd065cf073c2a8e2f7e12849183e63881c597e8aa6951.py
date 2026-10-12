"""Capture complete streams with real process-group timeout and input hashes."""
import argparse,datetime,hashlib,json,os,signal,subprocess,sys,time
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('--record',required=True)
p.add_argument('--timeout',type=float,required=True);p.add_argument('--manifest',required=True)
p.add_argument('--manifest-sha',required=True);p.add_argument('argv',nargs=argparse.REMAINDER)
a=p.parse_args();cmd=a.argv[1:] if a.argv and a.argv[0]=='--' else a.argv
base=Path(a.record);base.parent.mkdir(parents=True,exist_ok=True)
# Append literal suffixes. Never replace a user label's suffix.
out=Path(str(base)+'.stdout.txt');err=Path(str(base)+'.stderr.txt')
receipt_path=Path(str(base)+'.receipt.json')
if any(p.exists() for p in [out,err,receipt_path]):raise SystemExit('refuse to overwrite evidence')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def snap(m):return {p:sha(p) for p in m['files']}
t=time.monotonic();receipt={'argv':cmd,'cwd':os.getcwd(),
 'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'timeout_seconds':a.timeout,'timeout':False,'recorder':str(Path(__file__).resolve()),
 'interpreter':sys.executable,'python':sys.version,'manifest_path':a.manifest,
 'expected_manifest_sha256':a.manifest_sha}
try:
 actual=sha(a.manifest);receipt['actual_manifest_sha256']=actual
 if actual!=a.manifest_sha:raise RuntimeError('external manifest anchor mismatch')
 manifest=json.loads(Path(a.manifest).read_text());before=snap(manifest)
 receipt['source_before']=before
 if before!=manifest['files']:raise RuntimeError('manifest source mismatch before execution')
 env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 with out.open('xb') as o,err.open('xb') as e:
  child=subprocess.Popen(cmd,stdout=o,stderr=e,start_new_session=True,env=env)
  try:code=child.wait(timeout=a.timeout)
  except subprocess.TimeoutExpired:
   receipt['timeout']=True;os.killpg(child.pid,signal.SIGKILL);code=child.wait()
 receipt['returncode']=code;receipt['source_after']=snap(manifest)
 receipt['source_unchanged']=before==receipt['source_after']
except Exception as exc:
 receipt['returncode']=2;receipt['error']=repr(exc)
 if not out.exists():out.write_text('')
 if not err.exists():err.write_text(repr(exc)+'\n')
receipt.update(end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 elapsed_seconds=time.monotonic()-t,stdout=str(out),stderr=str(err),
 stdout_sha256=sha(out),stderr_sha256=sha(err))
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'record':str(base),'returncode':receipt['returncode'],
                 'timeout':receipt['timeout'],'elapsed_seconds':receipt['elapsed_seconds']}),flush=True)
sys.exit(receipt['returncode'] if receipt['returncode']>=0 else 124)
