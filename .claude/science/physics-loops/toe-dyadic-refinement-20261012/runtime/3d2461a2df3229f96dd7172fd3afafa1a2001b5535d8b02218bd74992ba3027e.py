"""Complete streams and true process-group timeout, used at both layers."""
import argparse,datetime,hashlib,json,os,signal,subprocess,sys,time
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('--record',required=True)
p.add_argument('--timeout',type=float,required=True)
p.add_argument('--manifest',required=True);p.add_argument('--manifest-sha',required=True)
p.add_argument('argv',nargs=argparse.REMAINDER);a=p.parse_args()
cmd=a.argv[1:] if a.argv and a.argv[0]=='--' else a.argv
base=Path(a.record);base.parent.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def snap(manifest):return {f:sha(f) for f in manifest['files']}
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
manifest_path=Path(a.manifest)
receipt={'argv':cmd,'cwd':os.getcwd(),'start_utc':start,'timeout_seconds':a.timeout,
         'recorder':str(Path(__file__).resolve()),'interpreter':sys.executable,
         'python':sys.version,'manifest_path':str(manifest_path),
         'expected_manifest_sha256':a.manifest_sha,'timeout':False}
out=base.with_suffix('.stdout.txt');err=base.with_suffix('.stderr.txt')
try:
 actual=sha(manifest_path);receipt['actual_manifest_sha256']=actual
 if actual!=a.manifest_sha:raise RuntimeError('external manifest anchor mismatch')
 manifest=json.loads(manifest_path.read_text());before=snap(manifest)
 receipt['source_before']=before
 if before!=manifest['files']:raise RuntimeError('manifest input hash mismatch')
 env=os.environ.copy();env.update({'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
 with out.open('wb') as o,err.open('wb') as e:
  proc=subprocess.Popen(cmd,stdout=o,stderr=e,start_new_session=True,env=env)
  try:rc=proc.wait(timeout=a.timeout)
  except subprocess.TimeoutExpired:
   receipt['timeout']=True;os.killpg(proc.pid,signal.SIGKILL);rc=proc.wait()
 receipt['returncode']=rc;receipt['source_after']=snap(manifest)
 receipt['source_unchanged']=receipt['source_after']==before
except Exception as e:
 receipt['returncode']=2;receipt['error']=repr(e)
 if not out.exists():out.write_text('')
 if not err.exists():err.write_text(repr(e)+'\n')
receipt.update({'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'elapsed_seconds':time.monotonic()-t,
                'stdout':str(out),'stderr':str(err),
                'stdout_sha256':sha(out),'stderr_sha256':sha(err)})
base.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'record':str(base),'returncode':receipt['returncode'],
                  'timeout':receipt['timeout'],'elapsed_seconds':receipt['elapsed_seconds']}),flush=True)
sys.exit(receipt['returncode'] if receipt['returncode']>=0 else 124)
