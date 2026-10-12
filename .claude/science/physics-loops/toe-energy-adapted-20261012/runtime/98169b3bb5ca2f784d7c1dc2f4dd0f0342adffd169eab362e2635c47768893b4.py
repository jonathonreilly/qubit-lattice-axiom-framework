#!/usr/bin/env python3
import argparse, datetime, json, os, signal, subprocess, sys, time
from pathlib import Path
from integrity_guard import verify, digest

p=argparse.ArgumentParser()
for name in ('root','attempt','candidate','variant','expected'):p.add_argument('--'+name,required=True)
a=p.parse_args();root=Path(a.root).resolve();out=Path(a.attempt).resolve()
started=datetime.datetime.now(datetime.timezone.utc).isoformat();before=verify(root,a.expected)
(out/'INNER.sources.before.json').write_text(json.dumps(before,indent=2)+'\n')
cmd=[sys.executable,'-B',str(root/'independent_suite.py'),'--candidate',str(root/a.candidate),'--variant',a.variant]
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
t=time.monotonic();timed_out=False
with (out/'INNER.stdout').open('xb') as so,(out/'INNER.stderr').open('xb') as se:
    child=subprocess.Popen(cmd,stdout=so,stderr=se,env=env,start_new_session=True,cwd=root)
    (out/'INNER.child.pid').write_text(str(child.pid)+'\n')
    try:rc=child.wait(timeout=40)
    except subprocess.TimeoutExpired:
        timed_out=True;os.killpg(child.pid,signal.SIGKILL);rc=child.wait()
    so.flush();se.flush();os.fsync(so.fileno());os.fsync(se.fileno())
after=verify(root,a.expected)
(out/'INNER.sources.after.json').write_text(json.dumps(after,indent=2)+'\n')
receipt={'layer':'INNER','timeout_seconds':40,'timeout':timed_out,'exit_code':rc,'command':cmd,'variant':a.variant,'started_utc':started,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'source_manifest_sha256':a.expected,'candidate_sha256':digest(root/a.candidate),'stdout_sha256':digest(out/'INNER.stdout'),'stderr_sha256':digest(out/'INNER.stderr'),'sources_unchanged':before==after}
(out/'INNER.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
sys.exit(124 if timed_out else rc)
