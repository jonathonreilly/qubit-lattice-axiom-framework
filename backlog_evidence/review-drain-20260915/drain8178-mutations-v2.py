"""Proposed four-new-controls capture only. No baseline or old mutation reruns."""
from pathlib import Path
import argparse,hashlib,json,os,re,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
COLD_CLEARANCE_BINDING=None
NEW_CONTROLS={'fourier_sign_wrong':'F','real_modes_independent_wrong':'F','zero_start_stationary_wrong':'F','integer_crossing_floor_wrong':'F'}
def at(d,p):
 assert p.startswith('/')
 for k in p[1:].split('/'):d=d[k.replace('~1','/').replace('~0','~')]
 return d
def load(p,s):
 p=Path(p);assert p.is_absolute() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W) and not p.is_symlink() and h(p)==s
 return p,json.loads(p.read_text())
def confirm_reviewed_main(record,expected_base):
 b=COLD_CLEARANCE_BINDING
 assert git('rev-parse','HEAD')==expected_base==record['source']['base']==b['frozen_base']
 assert git('rev-parse','origin/main')==b['reviewed_main'],'Reviewed main moved'
 assert git('merge-base',b['frozen_base'],b['reviewed_main'])==b['frozen_base']
 changed=set(git('diff','--name-only','--no-renames',b['frozen_base'],b['reviewed_main']).splitlines())
 bound={e['path'] for e in record['source']['paths']+sum(record['inputs'].values(),[])}
 assert not changed & bound,'Main advance overlaps frozen source/input closure'
def main():
 ap=argparse.ArgumentParser()
 for k in ['record','record-sha256','cheap','cheap-sha256','cold','cold-sha256','runner','expected-base','expected-current-main','plan','plan-sha256','primary-receipt','primary-receipt-sha256']:ap.add_argument('--'+k,required=True)
 ap.add_argument('--mutation',required=True,choices=sorted(NEW_CONTROLS));a=ap.parse_args()
 rp,record=load(a.record,a.record_sha256);pp,cheap=load(a.cheap,a.cheap_sha256);cp,cold=load(a.cold,a.cold_sha256);bp,baseline=load(a.primary_receipt,a.primary_receipt_sha256);planpath,plan=load(a.plan,a.plan_sha256)
 assert record['unit_id']=='PR8178' and record['schema_version']==2
 assert cheap['mechanical_status']=='ok' and cheap['tree']==record['source']['tree'] and cheap['record_sha256']==h(rp) and not cheap['cache_checked']
 b=COLD_CLEARANCE_BINDING;assert isinstance(b,dict),'Actual cold approval binding required in a new immutable revision'
 assert str(cp)==b['path'] and h(cp)==b['sha256'] and b['same_session_provenance']=='/root/review_8178'
 assert at(cold,b['verdict_pointer'])==b['verdict_value'] and at(cold,b['tree_pointer'])==b['tree']==record['source']['tree'] and b['required_predicates']
 for p,v in b['required_predicates'].items():assert at(cold,p)==v
 assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8178-author'
 assert a.expected_current_main==b['reviewed_main'];confirm_reviewed_main(record,a.expected_base)
 assert git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
 assert ref(planpath) in record['reviewer']['references'] and plan['actual_tree']==record['source']['tree'] and plan['actual_base']==record['source']['base']
 assert a.runner==plan['runner']['path']==record['notes'][0]['primary_runner'] and record['notes'][0]['helpers']==[]
 assert plan['limits']['wall_seconds']==60 and plan['limits']['sampled_aggregate_process_tree_rss_bytes']==384*1024*1024
 assert set(plan['future_changed_claim_controls'])==set(NEW_CONTROLS) and plan['declared_mutations'][a.mutation]=='F'
 assert baseline['status']=='CAPTURED; no science verdict' and baseline['runner']==a.runner and baseline['error'] is None and baseline['record']==ref(rp) and baseline['cheap']==ref(pp) and baseline['cold']==ref(cp) and baseline['program_attempts']==1 and baseline['json_reruns']==0 and baseline['mutation_runs']==0
 assert baseline['before']==baseline['after'] and not baseline['whole_tree_watchdog']['violations'] and baseline['result']['result']['status']=='ok' and baseline['result']['result']['exit_code']==0
 for e in baseline['artifacts']:assert h(Path(e['path']))==e['sha256']
 assert re.search(r'^TOTAL: PASS=16 FAIL=0$',baseline['result']['result']['stdout'],re.M)
 ids={}
 for e in record['source']['paths']+sum(record['inputs'].values(),[]):
  assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']
 def snapshot():
  out={}
  for p,d in ids.items():
   q=W/p;assert not q.is_symlink() and h(q)==d;s=q.stat();out[p]=dict(sha256=d,device=s.st_dev,inode=s.st_ino,size=s.st_size,mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns)
  return out
 before=snapshot();assert before==baseline['after'],'Source/input stat identity changed after primary'
 prefix=R/('drain8178-mutation-'+a.mutation+'-v2');side=Path(str(prefix)+'.sidecar.json');stdout=Path(str(prefix)+'.stdout.txt');stderr=Path(str(prefix)+'.stderr.txt');raw=Path(str(prefix)+'.raw-result.json');receipt=Path(str(prefix)+'.receipt.json');marker=R/('drain8178-prepared-v2-'+a.mutation+'-attempt.json')
 for p in [side,stdout,stderr,raw,receipt]:assert not p.exists()
 with marker.open('x') as f:json.dump(dict(status='RESERVED; no automatic retry',mutation=a.mutation,record=ref(rp),cold=ref(cp),primary=ref(bp),adapter=ref(Path(__file__).resolve())),f,indent=2)
 watch=dict(limit_seconds=60,limit_bytes=384*1024*1024,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='Sampled aggregate supervisor and descendant RSS')
 proc=None;known=set();error=None;after=None;result=None;started=time.monotonic()
 try:
  with stdout.open('x') as out,stderr.open('x') as err:
   proc=subprocess.Popen([sys.executable,str(W/a.runner),'--mutation',a.mutation],cwd=W,stdout=out,stderr=err,start_new_session=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','AUDIT_RESULT_SIDECAR':str(side)});known.add(proc.pid)
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
  # Full raw streams and actual process result persist before any identity or
  # expectation rejection; neither failed controls nor survivors are discarded.
  result=dict(exit_code=proc.returncode,stdout=stdout.read_text(),stderr=stderr.read_text(),elapsed_seconds=time.monotonic()-started)
  with raw.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
  assert watch['samples'] and not watch['violations'] and time.monotonic()-started<=60
  data=json.loads(side.read_text());assert data['mutation']==a.mutation and data['expected_mutation_family']=='F'
  assert result['exit_code']!=0 and data['failed']>0 and 'F' in data['failed_families'],'Mutation survived or failed outside intended family'
  assert data['passed']+data['failed']==16 and data['input_sha256']=={e['path']:e['sha256'] for e in plan['ordered_inputs']}
  assert re.search(r'^FAIL: F[1-4] ',result['stdout'],re.M) and 'mutation_family_expected: F' in result['stdout']
  assert re.search(r'^TOTAL: PASS='+str(data['passed'])+r' FAIL='+str(data['failed'])+r'$',result['stdout'],re.M)
  after=snapshot();assert before==after and git('write-tree')==record['source']['tree'] and not git('diff','--name-only');confirm_reviewed_main(record,a.expected_base)
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
  if not raw.exists():
   result=dict(exit_code=proc.returncode if proc else None,stdout=stdout.read_text() if stdout.exists() else '',stderr=stderr.read_text() if stderr.exists() else '',elapsed_seconds=time.monotonic()-started)
   with raw.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
  with receipt.open('x') as f:json.dump(dict(status='FAILED OR SURVIVED; preserve without retry' if error else 'EXPECTED MUTATION REJECTION; not universal proof',mutation=a.mutation,runner=a.runner,error=error,result=result,before=before,after=after,whole_tree_watchdog=watch,artifacts=[ref(p) for p in [stdout,stderr,side,raw] if p.is_file()],record=ref(rp),cheap=ref(pp),cold=ref(cp),primary=ref(bp),adapter=ref(Path(__file__).resolve()),program_attempts=1,baseline_reruns=0,json_reruns=0),f,indent=2);f.write('\n')
 if error:raise RuntimeError('Failure preserved at '+str(receipt))
 print(json.dumps(ref(receipt)))
if __name__=='__main__':main()
