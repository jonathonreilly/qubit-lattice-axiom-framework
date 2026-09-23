"""Proposed once-per-name mutation capture; no baseline run, staging, scratch inputs or gate."""
from pathlib import Path
import argparse,ast,hashlib,json,os,re,signal,subprocess,sys,time,traceback
assert __debug__
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
def load(path,digest):
    p=Path(path);assert p.is_absolute() and not p.is_symlink() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W)
    assert re.fullmatch('[0-9a-f]{64}',digest) and sha(p)==digest
    return p,json.loads(p.read_text())
def pointer(d,p):
    assert p.startswith('/')
    for k in p[1:].split('/'):d=d[k.replace('~1','/').replace('~0','~')]
    return d

def main():
    ap=argparse.ArgumentParser()
    for k in ['record','record-sha256','cold','cold-sha256','cold-verdict-pointer','primary-receipt','primary-receipt-sha256','expected-base','mutation']:ap.add_argument('--'+k,required=True)
    ap.add_argument('--capture-authorized',action='store_true',required=True);a=ap.parse_args();assert a.capture_authorized
    rp,record=load(a.record,a.record_sha256);cp,cold=load(a.cold,a.cold_sha256);pp,primary=load(a.primary_receipt,a.primary_receipt_sha256)
    assert record['schema_version']==2 and record['unit_id']=='PR8170'
    assert cold['reviewer_session']=='/root/review_8170' and cold['tree']==record['source']['tree']
    assert pointer(cold,a.cold_verdict_pointer) in {'CAPTURE_ELIGIBLE','CAPTURE_ELIGIBLE on exact frozen source and inputs; no material source blocker. Not final evidence or landing PASS.'},'Unknown cold verdict requires new reviewed adapter, never inferred approval'
    assert primary['status']=='CAPTURED; no scientific verdict or staging' and primary['error'] is None
    assert primary['record']==ref(rp) and primary['cold']==ref(cp) and primary['before']==primary['after']
    assert primary['primary_runs_attempted']==1 and primary['mutation_runs']==0 and primary['simulation_runs']==0
    watch0=primary['whole_tree_watchdog'];assert watch0['samples']>0 and not watch0['violations'] and watch0['limit_seconds']==900 and watch0['limit_bytes']==768*1024*1024
    pr=primary['result']['result'];assert pr['status']=='ok' and pr['exit_code']==0 and re.search(r'^TOTAL: PASS=17 FAIL=0$',pr['stdout'],re.M)
    for e in primary['artifacts']:assert sha(Path(e['path']))==e['sha256'],'Primary evidence changed'
    assert git('rev-parse','HEAD')==a.expected_base==record['source']['base']==git('rev-parse','origin/main')
    assert git('write-tree')==record['source']['tree'] and not git('diff','--name-only'),'Run before primary cache staging; source/index must remain frozen'
    owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8170-author' and Path(owner['path']).resolve()==W.resolve()
    planpath=R/'drain8170-author-input-resource-plan-v2.json';assert sha(planpath)=='481eb44a14431361852b6cebaa6ba9a9fee33619297a1c2b8b5734c74c3b8c04';plan=json.loads(planpath.read_text())
    runner=plan['runner']['path'];assert sha(W/runner)==plan['runner']['sha256'] and {n['primary_runner'] for n in record['notes']}=={runner}
    # Parse metadata without importing the scientific runner or executing --list-mutations.
    tree=ast.parse((W/runner).read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
    mutations=ast.literal_eval(decl['MUTATION_GATE']);assert mutations==plan['mutation_names'] and len(mutations)==14 and a.mutation in mutations
    assert list(ast.literal_eval(decl['AUDIT_INPUT_PATHS']))==[e['path'] for e in plan['ordered_inputs']]
    assert ast.literal_eval(decl['EXPECTED_INPUT_SHA256'])=={e['path']:e['sha256'] for e in plan['ordered_inputs']}
    assert ast.literal_eval(decl['AUDIT_TIMEOUT_SEC'])==900 and ast.literal_eval(decl['AUDIT_MEMORY_MB'])==768
    baseline=W/plan['json_output'];baseline_data=json.loads(baseline.read_text());assert baseline_data['mutation'] is None and baseline_data['passed']==17 and baseline_data['failed']==0
    assert baseline_data['source_sha256']==plan['runner']['sha256'] and baseline_data['input_sha256']==ast.literal_eval(decl['EXPECTED_INPUT_SHA256'])
    assert ref(baseline) in primary['artifacts'] and ref(W/plan['stdout']) in primary['artifacts']
    ids={}
    for e in record['source']['paths']+sum(record['inputs'].values(),[]):
        assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']
    for p in [baseline,W/plan['stdout']]:ids[p.relative_to(W).as_posix()]=sha(p)
    def snapshot():
        result={}
        for p,h in ids.items():
            q=W/p;assert not q.is_symlink() and sha(q)==h,p
            st=q.stat();result[p]=dict(sha256=h,device=st.st_dev,inode=st.st_ino,size=st.st_size,mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns)
        return result
    before=snapshot()
    for p,entry in primary['after'].items():assert p in before and before[p]==entry,'Identity generation changed since primary capture'
    name=a.mutation;family=mutations[name];prefix=R/f'drain8170-mutation-{name}-v1'
    stdout=Path(str(prefix)+'.stdout.txt');stderr=Path(str(prefix)+'.stderr.txt');receipt=Path(str(prefix)+'.json');raw=W/plan['mutation_json_pattern'].replace('<mutation>',name)
    for p in [stdout,stderr,receipt,raw]:assert not p.exists(),f'Preserve existing attempt/output: {p}'
    marker=R/f'drain8170-mutation-prepared-v2-{name}-attempt.json'
    with marker.open('x') as f:json.dump(dict(status='RESERVED; exactly one invocation for this name, no automatic retry',mutation=name,record=ref(rp),primary_receipt=ref(pp),cold=ref(cp),adapter=ref(Path(__file__).resolve())),f,indent=2)
    budget=dict(limit_seconds=900,limit_bytes=768*1024*1024,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='External supervisor plus runner and descendants; sampled aggregate RSS, not OS hard reservation')
    proc=None;known=set();start=time.monotonic();error=None;after=None;data=None;exit_code=None
    command=[sys.executable,'-u',str(W/runner),'--mutation',name]
    try:
        with stdout.open('xb') as out,stderr.open('xb') as err:
            proc=subprocess.Popen(command,cwd=W,stdout=out,stderr=err,start_new_session=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(W/'scripts')});known.add(proc.pid)
            while proc.poll() is None:
                rows={int(v[0]):(int(v[1]),int(v[2])*1024) for line in subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=1).splitlines() if len(v:=line.split())==3}
                family_pids={proc.pid}
                while True:
                    more=family_pids|{pid for pid,(ppid,_) in rows.items() if ppid in family_pids}
                    if more==family_pids:break
                    family_pids=more
                known|=family_pids;rss=sum(rows.get(pid,(0,0))[1] for pid in family_pids|{os.getpid()});elapsed=time.monotonic()-start
                budget['samples']+=1;budget['peak_tree_rss_bytes']=max(budget['peak_tree_rss_bytes'],rss)
                if elapsed>=900 or rss>768*1024*1024:
                    budget['violations'].append(dict(elapsed_seconds=elapsed,rss_bytes=rss,reason='wall_clock' if elapsed>=900 else 'memory'));raise RuntimeError('External process-tree budget exceeded')
                time.sleep(.02)
            exit_code=proc.returncode
        assert budget['samples']>0 and not budget['violations']
        data=json.loads(raw.read_text());assert data['mutation']==name and data['source_sha256']==plan['runner']['sha256'] and data['input_sha256']==baseline_data['input_sha256']
        assert exit_code==1,'Mutation survived or exited abnormally; neither is a successful mutation control'
        checks=data['checks'];assert len(checks)==17 and data['passed']+data['failed']==17
        assert data['failed']==sum(not e['passed'] for e in checks)>0 and data['passed']==sum(bool(e['passed']) for e in checks)
        failed_families={e['tag'][0] for e in checks if not e['passed']};assert family in failed_families,'Expected target family did not fail'
        body=stdout.read_text();assert f'mutation_family_expected: {family}' in body and f"mutation_family_observed: {''.join(sorted(failed_families))}" in body
        assert re.search(r'^TOTAL: PASS='+str(data['passed'])+' FAIL='+str(data['failed'])+'$',body,re.M)
        after=snapshot();assert after==before and git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
        for e in primary['artifacts']:assert sha(Path(e['path']))==e['sha256']
    except BaseException as exc:
        error=dict(error=repr(exc),traceback=traceback.format_exc())
        if proc is not None:
            try:os.killpg(proc.pid,signal.SIGKILL)
            except ProcessLookupError:pass
            for pid in known:
                try:os.kill(pid,signal.SIGKILL)
                except ProcessLookupError:pass
            proc.wait(timeout=5);exit_code=proc.returncode
        try:after=snapshot()
        except BaseException as drift:error['post_identity_error']=repr(drift)
    finally:
        receipt.write_text(json.dumps(dict(status='FAILED_OR_SURVIVED; preserve all evidence, no automatic retry or budget increase' if error else 'EXPECTED_MUTATION_REJECTION_OBSERVED; finite diagnostic only, not universal proof',mutation=name,expected_family=family,command=command,exit_code=exit_code,error=error,elapsed_seconds=time.monotonic()-start,whole_tree_watchdog=budget,before=before,after=after,structured_result=data,artifacts=[ref(p) for p in [stdout,stderr,raw] if p.is_file()],primary_receipt=ref(pp),record=ref(rp),cold=ref(cp),adapter=ref(Path(__file__).resolve()),baseline_runs=0,mutation_attempts=1,simulation_runs=0),indent=2)+'\n')
    if error:raise RuntimeError('Mutation attempt failed or survived; evidence '+str(receipt))
    print(json.dumps(ref(receipt)))
if __name__=='__main__':main()
