"""Proposed once-per-program capture; unexecuted and blocked until actual cold binding."""
from pathlib import Path
import argparse,hashlib,json,os,re,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
COLD_CLEARANCE_BINDING=None
# A future immutable revision binds the actual report path/hash, exact verdict and
# source tree pointers/values, original reviewer provenance and nonempty predicates.
def at(d,p):
 assert p.startswith('/')
 for k in p[1:].split('/'):d=d[k.replace('~1','/').replace('~0','~')]
 return d
def load(p,s):
 p=Path(p);assert p.is_absolute() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W) and not p.is_symlink() and h(p)==s
 return p,json.loads(p.read_text())
def confirm_reviewed_main(record, expected_base):
    # Preserve the already reviewed source tree; separately bind unchanged inputs
    # and the original reviewer's semantic confirmation of the actual new main.
    b = COLD_CLEARANCE_BINDING
    assert git('rev-parse', 'HEAD') == expected_base == record['source']['base'] == b['frozen_base']
    assert git('rev-parse', 'origin/main') == b['reviewed_main'], 'Reviewed current main moved'
    assert git('merge-base', b['frozen_base'], b['reviewed_main']) == b['frozen_base']
    changed = set(git('diff', '--name-only', '--no-renames', b['frozen_base'], b['reviewed_main']).splitlines())
    bound = {e['path'] for e in record['source']['paths'] + sum(record['inputs'].values(), [])}
    assert not changed & bound, 'Current-main advance overlaps frozen source or input paths'

def main():
 ap=argparse.ArgumentParser()
 for k in ['record','record-sha256','cheap','cheap-sha256','cold','cold-sha256','runner','expected-base','expected-current-main','plan','plan-sha256']:ap.add_argument('--'+k,required=True)
 a=ap.parse_args();rp,record=load(a.record,a.record_sha256);pp,cheap=load(a.cheap,a.cheap_sha256);cp,cold=load(a.cold,a.cold_sha256)
 assert record['unit_id']=='PR8178' and record['schema_version']==2
 assert cheap['mechanical_status']=='ok' and cheap['tree']==record['source']['tree'] and cheap['record_sha256']==h(rp) and not cheap['cache_checked']
 b=COLD_CLEARANCE_BINDING;assert isinstance(b,dict),'Actual cold clearance must be bound in a new immutable adapter revision before execution'
 assert str(cp)==b['path'] and h(cp)==b['sha256'] and b['same_session_provenance']=='/root/review_8178'
 assert at(cold,b['verdict_pointer'])==b['verdict_value'] and at(cold,b['tree_pointer'])==b['tree']==record['source']['tree'] and b['required_predicates']
 for p,v in b['required_predicates'].items():assert at(cold,p)==v
 assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8178-author'
 assert a.expected_current_main==b['reviewed_main'], 'CLI main must equal actual cold-reviewed main'
 confirm_reviewed_main(record, a.expected_base)
 assert git('write-tree')==record['source']['tree'] and not git('diff','--name-only')

 planpath,plan=load(a.plan,a.plan_sha256);assert ref(planpath) in record['reviewer']['references'] and plan['actual_tree']==record['source']['tree'] and plan['actual_base']==record['source']['base']
 assert a.runner==plan['runner']['path']==record['notes'][0]['primary_runner'] and record['notes'][0]['helpers']==[]
 program=dict(plan['runner'],mathematical_checks=11,ordered_inputs=plan['ordered_inputs'],stdout_cache=plan['output_contract']['canonical_stdout_cache'])
 assert plan['limits']['wall_seconds']==60 and plan['limits']['sampled_aggregate_process_tree_rss_bytes']==384*1024*1024
 assert plan['planned_checks']=={'total':16,'mathematical':11,'metadata':5,'families':{'A':4,'B':2,'C':2,'D':3,'F':4,'G':1}}
 ids={}
 for e in record['source']['paths']+sum(record['inputs'].values(),[]):
  assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']
 def snapshot():
  out={}
  for p,d in ids.items():
   q=W/p;assert not q.is_symlink() and h(q)==d;pstat=q.stat();out[p]=dict(sha256=d,device=pstat.st_dev,inode=pstat.st_ino,size=pstat.st_size,mtime_ns=pstat.st_mtime_ns,ctime_ns=pstat.st_ctime_ns)
  return out
 before=snapshot();stem=Path(a.runner).stem;prefix=R/('drain8178-capture-'+stem+'-v1')
 side=Path(str(prefix)+'.sidecar.json');raw=Path(str(prefix)+'.raw-result.json');workerout=Path(str(prefix)+'.worker.json');log=Path(str(prefix)+'.supervisor.txt');receipt=Path(str(prefix)+'.receipt.json');marker=R/('drain8178-prepared-v1-'+stem+'-attempt.json')
 cache=W/program['stdout_cache'];live=cache.parent/'.in-progress'/cache.name
 for p in [side,raw,workerout,log,receipt,cache,live]:assert not p.exists(),str(p)
 with marker.open('x') as f:json.dump(dict(status='RESERVED; no implicit retry',runner=a.runner,record=ref(rp),cold=ref(cp),adapter=ref(Path(__file__).resolve())),f,indent=2)
 worker="import sys,json\nfrom pathlib import Path\nsys.dont_write_bytecode=True\nsys.path.insert(0,sys.argv[1])\nimport runner_cache as c\noriginal=c.execute_runner\ndef preserve(runner_path,timeout_sec):\n r=original(runner_path,timeout_sec=timeout_sec)\n with Path(sys.argv[4]).open('x') as f:json.dump(r,f,indent=2);f.write('\\n')\n return r\nc.execute_runner=preserve\nr,p=c.execute_and_write_cache(sys.argv[2],60)\nwith Path(sys.argv[3]).open('x') as f:json.dump(dict(result=r,cache=str(p) if p else None),f,indent=2)\n"
 watch=dict(limit_seconds=60,limit_bytes=384*1024*1024,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='Sampled aggregate supervisor, worker and descendants RSS; not OS hard allocation cap')
 proc=None;known=set();error=None;after=None;result=None;started=time.monotonic()
 try:
  with log.open('x') as out:
   proc=subprocess.Popen([sys.executable,'-c',worker,str(W/'scripts'),a.runner,str(workerout),str(raw)],cwd=W,stdout=out,stderr=subprocess.STDOUT,start_new_session=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','AUDIT_RESULT_SIDECAR':str(side)});known.add(proc.pid)
   while proc.poll() is None:
    rows={int(v[0]):(int(v[1]),int(v[2])*1024) for line in subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=1).splitlines() if len(v:=line.split())==3};family={proc.pid}
    while True:
     more=family|{pid for pid,(parent,_) in rows.items() if parent in family}
     if more==family:break
     family=more
    known|=family;rss=sum(rows.get(pid,(0,0))[1] for pid in family|{os.getpid()});elapsed=time.monotonic()-started;watch['samples']+=1;watch['peak_tree_rss_bytes']=max(watch['peak_tree_rss_bytes'],rss)
    if rss>watch['limit_bytes'] or elapsed>=60:
     watch['violations'].append(dict(elapsed_seconds=elapsed,rss_bytes=rss));raise RuntimeError('External process-tree budget exceeded')
    time.sleep(.02)
   assert proc.returncode==0
  assert watch['samples'] and not watch['violations'] and time.monotonic()-started<=60;result=json.loads(workerout.read_text());rr=result['result'];assert rr==json.loads(raw.read_text()) and rr['status']=='ok' and rr['exit_code']==0
  data=json.loads(side.read_text());assert data['passed']==16 and data['failed']==0 and data['failed_families']==[] and data['mutation'] is None and data['expected_mutation_family'] is None
  assert data['input_sha256']=={e['path']:e['sha256'] for e in program['ordered_inputs']}
  assert re.search(r'^TOTAL: PASS=16 FAIL=0$',rr['stdout'],re.M) and Path(result['cache']).resolve()==cache.resolve()
  assert len(re.findall(r'^PASS: ',rr['stdout'],re.M))==16 and not re.search(r'^FAIL: ',rr['stdout'],re.M)
  after=snapshot();assert before==after and git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
  confirm_reviewed_main(record, a.expected_base)
 except BaseException as ex:
  error=dict(error=repr(ex),traceback=traceback.format_exc())
  if proc is not None:
   try:os.killpg(proc.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   for pid in known:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
   proc.wait(timeout=5)
  try:after=snapshot()
  except BaseException as drift:error['identity_error']=repr(drift)
 finally:
  partial=Path(str(prefix)+'.partial-live.txt')
  if live.is_file():
   with partial.open('xb') as f:f.write(live.read_bytes())
  with receipt.open('x') as f:json.dump(dict(status='FAILED; preserve evidence, no retry or cap increase' if error else 'CAPTURED; no science verdict',runner=a.runner,error=error,result=result,before=before,after=after,whole_tree_watchdog=watch,elapsed_seconds=time.monotonic()-started,artifacts=[ref(p) for p in [side,raw,workerout,log,cache,live,partial] if p.is_file()],record=ref(rp),cheap=ref(pp),cold=ref(cp),adapter=ref(Path(__file__).resolve()),program_attempts=1,json_reruns=0,mutation_runs=0),f,indent=2);f.write('\n')
 if error:raise RuntimeError('Failed capture preserved at '+str(receipt))
 print(json.dumps(ref(receipt)))
if __name__=='__main__':main()
