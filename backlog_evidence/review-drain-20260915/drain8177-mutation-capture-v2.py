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

# Deliberately unbound: a new immutable adapter version must bind the ACTUAL
# original-reviewer cold report path/hash, exact verdict pointer/value and tree.
# Early source clearance is insufficient. No hypothetical verdict is accepted.
COLD_CLEARANCE_BINDING = None
def confirm_cold(cp,cold,tree):
    b=COLD_CLEARANCE_BINDING
    assert isinstance(b,dict), 'BLOCKED: actual same-session cold report schema/clearance has not yet been bound; root must prepare a new immutable adapter version'
    assert str(cp)==b['path'] and sha(cp)==b['sha256']
    assert b.get('same_session_provenance'), 'Actual original-reviewer provenance must be recorded in the new binding'
    assert isinstance(b.get('required_predicates'),dict) and b['required_predicates']
    def read_pointer(p):
        cur=cold
        for key in p.lstrip('/').split('/'):
            cur=cur[key.replace('~1','/').replace('~0','~')]
        return cur
    assert b['verdict_pointer'].startswith('/') and b['tree_pointer'].startswith('/')
    assert read_pointer(b['verdict_pointer'])==b['verdict_value']
    assert read_pointer(b['tree_pointer'])==tree==b['tree']
    for p,v in b['required_predicates'].items():assert p.startswith('/') and read_pointer(p)==v

def confirm_reviewed_main(record, expected_base):
    # Preserve the already reviewed source tree; separately bind unchanged inputs
    # and the original reviewer's semantic confirmation of the actual new main.
    b = COLD_CLEARANCE_BINDING
    assert b['frozen_base'] in b['required_predicates'].values() and b['reviewed_main'] in b['required_predicates'].values(), 'Both base identities must be actual cold-report predicates'
    assert git('rev-parse', 'HEAD') == expected_base == record['source']['base'] == b['frozen_base']
    assert git('rev-parse', 'origin/main') == b['reviewed_main'], 'Reviewed current main moved'
    assert git('merge-base', b['frozen_base'], b['reviewed_main']) == b['frozen_base']
    changed = set(git('diff', '--name-only', '--no-renames', b['frozen_base'], b['reviewed_main']).splitlines())
    bound = {e['path'] for e in record['source']['paths'] + sum(record['inputs'].values(), [])}
    assert not changed & bound, 'Current-main advance overlaps frozen source or input paths'

def main():
    ap=argparse.ArgumentParser()
    for k in ['record','record-sha256','cold','cold-sha256','primary-receipt','primary-receipt-sha256','expected-base','mutation']:ap.add_argument('--'+k,required=True)
    ap.add_argument('--capture-authorized',action='store_true',required=True);a=ap.parse_args();assert a.capture_authorized
    rp,record=load(a.record,a.record_sha256);cp,cold=load(a.cold,a.cold_sha256);pp,primary=load(a.primary_receipt,a.primary_receipt_sha256)
    assert record['schema_version']==2 and record['unit_id']=='PR8177'
    confirm_cold(cp,cold,record['source']['tree'])
    assert primary['status']=='CAPTURED; no scientific verdict or staging' and primary['error'] is None
    assert primary['record']==ref(rp) and primary['cold']==ref(cp) and primary['before']==primary['after']
    assert primary['primary_runs_attempted']==1 and primary['mutation_runs']==0 and primary['simulation_runs']==0
    cheap_path,cheap=load(primary['cheap']['path'],primary['cheap']['sha256'])
    assert cheap['mechanical_status']=='ok' and cheap['tree']==record['source']['tree'] and cheap['record_sha256']==sha(rp) and not cheap['cache_checked']
    watch0=primary['whole_tree_watchdog'];assert watch0['samples']>0 and not watch0['violations'] and watch0['limit_seconds']==120 and watch0['limit_bytes']==384*1024*1024
    pr=primary['result']['result'];assert pr['status']=='ok' and pr['exit_code']==0 and re.search(r'^TOTAL: PASS=18 FAIL=0$',pr['stdout'],re.M)
    for e in primary['artifacts']:assert sha(Path(e['path']))==e['sha256'],'Primary evidence changed'
    confirm_reviewed_main(record, a.expected_base)
    assert True
    assert git('write-tree')==record['source']['tree'] and not git('diff','--name-only'),'Run before primary cache staging; source/index must remain frozen'
    owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8177-author' and Path(owner['path']).resolve()==W.resolve()
    planpath=R/'drain8177-capture-plan-v1.json';assert sha(planpath)==PLAN_SHA256;plan=json.loads(planpath.read_text())
    runner=plan['primary'];assert sha(W/runner)==plan['primary_sha256'] and {n['primary_runner'] for n in record['notes']}=={runner}
    tree=ast.parse((W/runner).read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
    mutations=ast.literal_eval(decl['MUTATION_GATE']);assert mutations==plan['all_mutation_definitions'] and len(mutations)==8
    assert a.mutation in plan['mathematical_controls'], 'Only predecessor_profile_wrong is cleared here'
    assert list(ast.literal_eval(decl['AUDIT_INPUT_PATHS']))==[e['path'] for e in plan['runtime_inputs']]
    assert ast.literal_eval(decl['INPUT_SHA256'])=={e['path']:e['sha256'] for e in plan['runtime_inputs']}
    assert ast.literal_eval(decl['AUDIT_TIMEOUT_SEC'])==120
    assert ref(W/plan['cache_destination']) in primary['artifacts']
    ids={}
    for e in record['source']['paths']+sum(record['inputs'].values(),[]):
        assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']
    for p in [W/plan['cache_destination']]:ids[p.relative_to(W).as_posix()]=sha(p)
    def snapshot():
        result={}
        for p,h in ids.items():
            q=W/p;assert not q.is_symlink() and sha(q)==h,p
            st=q.stat();result[p]=dict(sha256=h,device=st.st_dev,inode=st.st_ino,size=st.st_size,mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns)
        return result
    before=snapshot()
    for p,entry in primary['after'].items():assert p in before and before[p]==entry,'Identity generation changed since primary capture'
    name=a.mutation;family=mutations[name];prefix=R/f'drain8177-mutation-{name}-v1'
    stdout=Path(str(prefix)+'.stdout.txt');stderr=Path(str(prefix)+'.stderr.txt');receipt=Path(str(prefix)+'.json')
    for p in [stdout,stderr,receipt]:assert not p.exists(),f'Preserve existing attempt/output: {p}'
    marker=R/f'drain8177-mutation-prepared-v2-{name}-attempt.json'
    with marker.open('x') as f:json.dump(dict(status='RESERVED; exactly one invocation for this name, no automatic retry',mutation=name,record=ref(rp),primary_receipt=ref(pp),cold=ref(cp),adapter=ref(Path(__file__).resolve())),f,indent=2)
    budget=dict(limit_seconds=120,limit_bytes=384*1024*1024,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='External supervisor plus runner and descendants; sampled aggregate RSS, not OS hard reservation')
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
                if elapsed>=120 or rss>384*1024*1024:
                    budget['violations'].append(dict(elapsed_seconds=elapsed,rss_bytes=rss,reason='wall_clock' if elapsed>=120 else 'memory'));raise RuntimeError('External process-tree budget exceeded')
                time.sleep(.02)
            exit_code=proc.returncode
        assert budget['samples']>0 and not budget['violations']
        assert exit_code==1,'Mutation survived or exited abnormally; neither is a successful mutation control'
        body=stdout.read_text();assert not stderr.read_bytes(), 'Unexpected stderr retained for review'
        failures=re.findall(r'^FAIL: ([A-Z][0-9]+) ',body,re.M)
        expected=plan['mathematical_controls'][name]['expected_failed_tags']
        assert failures==expected, f'Wrong failure target: {failures}, expected {expected}'
        failed_families={t[0] for t in failures};assert failed_families=={family}
        assert f'mutation_family_expected: {family}' in body and f"mutation_family_observed: {family}" in body
        assert re.search(r'^TOTAL: PASS=17 FAIL=1$',body,re.M)
        assert len(re.findall(r'^PASS: [A-Z][0-9]+ ',body,re.M))==17
        data=dict(parsed_stdout=True,failed_tags=failures,expected_failed_tags=expected,completed_checks=18,passed=17,failed=1)
        after=snapshot();assert after==before and git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
        confirm_reviewed_main(record, a.expected_base)
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
        receipt.write_text(json.dumps(dict(status='FAILED_OR_SURVIVED; preserve all evidence, no automatic retry or budget increase' if error else 'EXPECTED_MUTATION_REJECTION_OBSERVED; finite diagnostic only, not universal proof',mutation=name,expected_family=family,command=command,exit_code=exit_code,error=error,elapsed_seconds=time.monotonic()-start,whole_tree_watchdog=budget,before=before,after=after,structured_result=data,artifacts=[ref(p) for p in [stdout,stderr] if p.is_file()],primary_receipt=ref(pp),record=ref(rp),cold=ref(cp),adapter=ref(Path(__file__).resolve()),baseline_runs=0,mutation_attempts=1,simulation_runs=0),indent=2)+'\n')
    if error:raise RuntimeError('Mutation attempt failed or survived; evidence '+str(receipt))
    print(json.dumps(ref(receipt)))
PLAN_SHA256='da15e79ffc0ae9fa67ae11229707b6ba1796b1b8389f516544d61d3edaaca105'
if __name__=='__main__':main()
