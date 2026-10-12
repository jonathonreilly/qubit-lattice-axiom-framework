#!/usr/bin/env python3
import argparse, datetime, json, os, signal, subprocess, sys, time
from pathlib import Path
from integrity_guard import verify, digest

p=argparse.ArgumentParser();p.add_argument('--expected',required=True);a=p.parse_args()
root=Path(__file__).resolve().parent
variants=[('baseline','candidate_formula.py')]+[(x,'variants/'+x+'/candidate_formula.py') for x in ['missing_jacobian','reversed_lattice_frame','missing_boost_connection','missing_boost_origin','reversed_alias_phase']]
top=root/'runs';top.mkdir(exist_ok=False)
all_receipts=[]
for name,candidate in variants:
    before=verify(root,a.expected);out=top/name;out.mkdir()
    (out/'OUTER.sources.before.json').write_text(json.dumps(before,indent=2)+'\n')
    cmd=[sys.executable,'-B',str(root/'inner_supervisor.py'),'--root',str(root),'--attempt',str(out),'--candidate',candidate,'--variant',name,'--expected',a.expected]
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();timed_out=False
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
    with (out/'OUTER.stdout').open('xb') as so,(out/'OUTER.stderr').open('xb') as se:
        child=subprocess.Popen(cmd,stdout=so,stderr=se,start_new_session=True,env=env,cwd=root)
        try:rc=child.wait(timeout=50)
        except subprocess.TimeoutExpired:
            timed_out=True
            pidfile=out/'INNER.child.pid'
            if pidfile.exists():
                try:os.killpg(int(pidfile.read_text()),signal.SIGKILL)
                except ProcessLookupError:pass
            os.killpg(child.pid,signal.SIGKILL);rc=child.wait()
        so.flush();se.flush();os.fsync(so.fileno());os.fsync(se.fileno())
    after=verify(root,a.expected)
    (out/'OUTER.sources.after.json').write_text(json.dumps(after,indent=2)+'\n')
    receipt={'layer':'OUTER','variant':name,'timeout_seconds':50,'timeout':timed_out,'exit_code':rc,'command':cmd,'started_utc':started,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'source_manifest_sha256':a.expected,'stdout_sha256':digest(out/'OUTER.stdout'),'stderr_sha256':digest(out/'OUTER.stderr'),'sources_unchanged':before==after}
    (out/'OUTER.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    all_receipts.append(receipt)
    print(json.dumps({'captured':name,'outer_exit':rc,'timeout':timed_out,'attempt':str(out)}),flush=True)
(top/'capture_summary.json').write_text(json.dumps(all_receipts,indent=2)+'\n')
