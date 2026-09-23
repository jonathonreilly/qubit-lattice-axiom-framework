"""Proposed once-only primary capture. No staging, mutation execution, gate or science verdict."""
from pathlib import Path
import argparse,hashlib,json,os,re,signal,subprocess,sys,time,traceback
assert __debug__
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
def load_checked(path,digest):
    p=Path(path);assert p.is_absolute() and not p.is_symlink() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W)
    assert re.fullmatch('[0-9a-f]{64}',digest) and sha(p)==digest
    return p,json.loads(p.read_text())
def at(d,p):
    assert p.startswith('/')
    for k in p[1:].split('/'):d=d[k.replace('~1','/').replace('~0','~')]
    return d

# Deliberately unbound: a new immutable adapter version must bind the ACTUAL
# original-reviewer cold report path/hash, exact verdict pointer/value and tree.
# Early source clearance is insufficient. No hypothetical verdict is accepted.
COLD_CLEARANCE_BINDING = None
def confirm_cold(cp,cold,tree):
    b=COLD_CLEARANCE_BINDING
    assert isinstance(b,dict), 'BLOCKED: actual same-session cold report schema/clearance has not yet been bound; root must prepare a new immutable adapter version'
    assert str(cp)==b['path'] and sha(cp)==b['sha256']
    assert cold['reviewer_session']=='/root/review_8171'
    def read_pointer(p):
        cur=cold
        for key in p.lstrip('/').split('/'):
            cur=cur[key.replace('~1','/').replace('~0','~')]
        return cur
    assert b['verdict_pointer'].startswith('/') and b['tree_pointer'].startswith('/')
    assert read_pointer(b['verdict_pointer'])==b['verdict_value']
    assert read_pointer(b['tree_pointer'])==tree==b['tree']

def main():
    ap=argparse.ArgumentParser()
    for k in ['record','record-sha256','cheap','cheap-sha256','cold','cold-sha256','expected-base','version']:ap.add_argument('--'+k,required=True)
    ap.add_argument('--capture-authorized',action='store_true',required=True);a=ap.parse_args()
    assert a.capture_authorized and re.fullmatch('v[1-9][0-9]*',a.version)
    rp,record=load_checked(a.record,a.record_sha256);pp,pre=load_checked(a.cheap,a.cheap_sha256);cp,cold=load_checked(a.cold,a.cold_sha256)
    assert record['unit_id']=='PR8171' and record['schema_version']==2
    assert pre['mechanical_status']=='ok' and pre['tree']==record['source']['tree'] and pre['record_sha256']==sha(rp) and not pre['cache_checked']
    confirm_cold(cp,cold,record['source']['tree'])
    assert git('rev-parse','HEAD')==a.expected_base==record['source']['base']==git('rev-parse','origin/main') and git('write-tree')==record['source']['tree']
    owner=json.loads((R/'author-draft-slot.json').read_text());assert owner['owner']=='PR8171-author' and Path(owner['path']).resolve()==W.resolve()
    assert not git('diff','--name-only')
    planpath=R/'drain8171-capture-plan-v1.json';assert sha(planpath)==PLAN_SHA256;plan=json.loads(planpath.read_text())
    early=R/'drain8171-early-review-v2.json';assert sha(early)=='5da6fcfb236143f5a01623be0ec909d7dd4b1fde666b77e8c2c37debd1fd6995'
    primary=plan['primary'];assert {n['primary_runner'] for n in record['notes']}=={primary} and all(not n['helpers'] for n in record['notes'])
    cache=W/plan['cache_destination'];live=W/'logs/runner-cache/.in-progress'/cache.name
    for p in [cache,live]:assert not p.exists(),f'Existing evidence must not be overwritten: {p}'
    identities={}
    for e in record['source']['paths']+sum(record['inputs'].values(),[]):
        assert e['path'] not in identities or identities[e['path']]==e['sha256'];identities[e['path']]=e['sha256']
    def snapshot():
        out={}
        for p,h in identities.items():
            q=W/p;assert not q.is_symlink() and sha(q)==h,p
            st=q.stat();out[p]=dict(sha256=h,device=st.st_dev,inode=st.st_ino,size=st.st_size,mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns)
        return out
    before=snapshot()
    receipt=R/f'drain8171-execution-{a.version}.json';worker_result=R/f'drain8171-worker-{a.version}.json';supervisor_log=R/f'drain8171-supervisor-{a.version}.txt';raw_result=R/f'drain8171-raw-result-{a.version}.json'
    assert all(not p.exists() for p in [receipt,worker_result,supervisor_log,raw_result])
    marker=R/'drain8171-primary-prepared-v2-attempt.json'
    with marker.open('x') as f:json.dump(dict(status='ATTEMPT RESERVED; never retry automatically',record=ref(rp),cold=ref(cp),script=ref(Path(__file__).resolve())),f,indent=2)
    limit_sec=60;limit_bytes=384*1024*1024
    watch=dict(limit_seconds=limit_sec,limit_bytes=limit_bytes,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='External supervisor plus worker process group and descendants; sampled RSS, not an OS hard-memory reservation')
    worker="import sys,json\nfrom pathlib import Path\nsys.dont_write_bytecode=True\nsys.path.insert(0,sys.argv[1])\nimport runner_cache as c\noriginal_execute_runner=c.execute_runner\ndef preserve_execute_runner(runner_path,timeout_sec):\n    result=original_execute_runner(runner_path,timeout_sec=timeout_sec)\n    with Path(sys.argv[4]).open('x') as evidence:\n        json.dump(result,evidence,indent=2)\n        evidence.write('\\n')\n    return result\nc.execute_runner=preserve_execute_runner\nr,p=c.execute_and_write_cache(sys.argv[2],60)\nPath(sys.argv[3]).write_text(json.dumps(dict(result=r,cache=str(p) if p else None),indent=2)+'\\n')\n"
    proc=None;started=time.monotonic();error=None;after=None;result=None
    try:
        with supervisor_log.open('x') as log:
            proc=subprocess.Popen([sys.executable,'-c',worker,str(W/'scripts'),primary,str(worker_result),str(raw_result)],cwd=W,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
            known={proc.pid}
            while proc.poll() is None:
                rows={int(v[0]):(int(v[1]),int(v[2])*1024) for line in subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=1).splitlines() if len(v:=line.split())==3}
                family={proc.pid}
                while True:
                    more=family|{pid for pid,(ppid,_) in rows.items() if ppid in family}
                    if more==family:break
                    family=more
                known|=family
                rss=sum(rows.get(pid,(0,0))[1] for pid in family|{os.getpid()});watch['samples']+=1;watch['peak_tree_rss_bytes']=max(watch['peak_tree_rss_bytes'],rss)
                elapsed=time.monotonic()-started
                if rss>limit_bytes or elapsed>=limit_sec:
                    watch['violations'].append(dict(elapsed_seconds=elapsed,rss_bytes=rss,reason='memory' if rss>limit_bytes else 'wall_clock'))
                    raise RuntimeError('External process-tree budget exceeded')
                time.sleep(.02)
            assert proc.returncode==0,f'Capture worker exited {proc.returncode}'
        assert watch['samples']>0 and not watch['violations']
        result=json.loads(worker_result.read_text());r=result['result'];assert json.loads(raw_result.read_text())==r
        assert r['status']=='ok' and r['exit_code']==0 and re.search(r'^TOTAL: PASS=16 FAIL=0$',r['stdout'],re.M)
        assert Path(result['cache']).resolve()==cache.resolve() and cache.exists()
        after=snapshot();assert after==before and git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
    except BaseException as exc:
        error=dict(error=repr(exc),traceback=traceback.format_exc())
        if proc is not None:
            try:os.killpg(proc.pid,signal.SIGKILL)
            except ProcessLookupError:pass
            for pid in known:
                try:os.kill(pid,signal.SIGKILL)
                except ProcessLookupError:pass
            proc.wait(timeout=5)
        try:after=snapshot()
        except BaseException as drift:error['post_identity_error']=repr(drift)
    finally:
        artifacts=[ref(p) for p in [cache,live,worker_result,supervisor_log,raw_result] if p.is_file()]
        receipt.write_text(json.dumps(dict(status='FAILED; preserve all partial evidence, no automatic retry or budget increase' if error else 'CAPTURED; no scientific verdict or staging',error=error,whole_tree_watchdog=watch,elapsed_seconds=time.monotonic()-started,before=before,after=after,result=result,artifacts=artifacts,record=ref(rp),cheap=ref(pp),cold=ref(cp),adapter=ref(Path(__file__).resolve()),primary_runs_attempted=1,mutation_runs=0,simulation_runs=0),indent=2)+'\n')
    if error:raise RuntimeError('Capture failed; preserved '+str(receipt))
    print(json.dumps(ref(receipt)))
PLAN_SHA256='12b72e616fd0579db2e76fbe74c8b18884db853416da60a460bca3662d68b352'
if __name__=='__main__':main()
