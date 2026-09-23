"""Proposed once-per-program capture; unexecuted and blocked until actual cold binding."""
from pathlib import Path
import argparse,hashlib,json,os,re,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
COLD_CLEARANCE_BINDING={'path': '/private/tmp/review-drain-20260915/drain8032-cold-activation-v2.json', 'sha256': 'c346fd631222c85b5db47bdebe29b246915e07d954b12fe50c8c72775a0cb79b', 'same_session_provenance': '/root/review_8032', 'verdict_pointer': '/verdict', 'verdict_value': 'COLD_SOURCE_PASS_CONDITIONAL_CAPTURE_CLEARANCE', 'tree_pointer': '/source_tree', 'tree': 'd218c35f6ebdc84e6bb8ea8a8b2385ff9ed47ceb', 'frozen_base': 'e46c78efd91d00c8a96ea4f11ea8bc5a8e3ed0e6', 'reviewed_main': '64f53dd443cd02997394e1a8bef16e2baf9f9d39', 'required_predicates': {'/reviewer_session': '/root/review_8032', '/frozen_base': 'e46c78efd91d00c8a96ea4f11ea8bc5a8e3ed0e6', '/reviewed_current_main': '64f53dd443cd02997394e1a8bef16e2baf9f9d39', '/findings': [], '/science_source_confirmed': True, '/input_closure_confirmed': True, '/archive_confirmed': True, '/registry_confirmed': True, '/resource_plan_confirmed': True, '/dual_main_pattern_allowed': True, '/limits/wall_seconds_per_program': 180, '/limits/sampled_aggregate_rss_mib': 256}}
PLAN_SHA256='269e4a415fa6316f4922d9c54c136d0414f85b7c2683d6b712f746f3a74a4b6b'
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
 for k in ['record','record-sha256','cheap','cheap-sha256','cold','cold-sha256','runner','expected-base']:ap.add_argument('--'+k,required=True)
 a=ap.parse_args();rp,record=load(a.record,a.record_sha256);pp,cheap=load(a.cheap,a.cheap_sha256);cp,cold=load(a.cold,a.cold_sha256)
 assert record['unit_id']=='PR8032' and record['schema_version']==2
 assert cheap['mechanical_status']=='ok' and cheap['tree']==record['source']['tree'] and cheap['record_sha256']==h(rp) and not cheap['cache_checked']
 b=COLD_CLEARANCE_BINDING;assert isinstance(b,dict),'Actual cold clearance must be bound in a new immutable adapter revision before execution'
 assert str(cp)==b['path'] and h(cp)==b['sha256'] and b['same_session_provenance']=='/root/review_8032'
 assert at(cold,b['verdict_pointer'])==b['verdict_value'] and at(cold,b['tree_pointer'])==b['tree']==record['source']['tree'] and b['required_predicates']
 for p,v in b['required_predicates'].items():assert at(cold,p)==v
 assert json.loads((R/'review-meta-slot.json').read_text())['owner']=='PR8032-author'
 confirm_reviewed_main(record, a.expected_base)
 assert git('write-tree')==record['source']['tree'] and not git('diff','--name-only')
 planpath=R/'drain8032-author-input-resource-plan-v2.json';assert h(planpath)==PLAN_SHA256;plan=json.loads(planpath.read_text());programs={x['path']:x for x in plan['programs']};assert len(programs)==2 and a.runner in programs
 assert {record['notes'][0]['primary_runner'],*record['notes'][0]['helpers']}==set(programs);program=programs[a.runner]
 ids={}
 for e in record['source']['paths']+sum(record['inputs'].values(),[]):
  assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']
 def snapshot():
  out={}
  for p,d in ids.items():
   q=W/p;assert not q.is_symlink() and h(q)==d;pstat=q.stat();out[p]=dict(sha256=d,device=pstat.st_dev,inode=pstat.st_ino,size=pstat.st_size,mtime_ns=pstat.st_mtime_ns,ctime_ns=pstat.st_ctime_ns)
  return out
 before=snapshot();stem=Path(a.runner).stem;prefix=R/('drain8032-capture-'+stem+'-v1')
 side=Path(str(prefix)+'.sidecar.json');raw=Path(str(prefix)+'.raw-result.json');workerout=Path(str(prefix)+'.worker.json');log=Path(str(prefix)+'.supervisor.txt');receipt=Path(str(prefix)+'.receipt.json');marker=R/('drain8032-prepared-v2-'+stem+'-attempt.json')
 cache=W/program['stdout_cache'];live=cache.parent/'.in-progress'/cache.name
 for p in [side,raw,workerout,log,receipt,cache,live]:assert not p.exists(),str(p)
 with marker.open('x') as f:json.dump(dict(status='RESERVED; no implicit retry',runner=a.runner,record=ref(rp),cold=ref(cp),adapter=ref(Path(__file__).resolve())),f,indent=2)
 worker="import sys,json\nfrom pathlib import Path\nsys.dont_write_bytecode=True\nsys.path.insert(0,sys.argv[1])\nimport runner_cache as c\noriginal=c.execute_runner\ndef preserve(runner_path,timeout_sec):\n r=original(runner_path,timeout_sec=timeout_sec)\n with Path(sys.argv[4]).open('x') as f:json.dump(r,f,indent=2);f.write('\\n')\n return r\nc.execute_runner=preserve\nr,p=c.execute_and_write_cache(sys.argv[2],180)\nwith Path(sys.argv[3]).open('x') as f:json.dump(dict(result=r,cache=str(p) if p else None),f,indent=2)\n"
 watch=dict(limit_seconds=180,limit_bytes=256*1024*1024,sampling_interval_seconds=.02,samples=0,peak_tree_rss_bytes=0,violations=[],scope='Sampled aggregate supervisor, worker and descendants RSS; not OS hard allocation cap')
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
    if rss>watch['limit_bytes'] or elapsed>=180:
     watch['violations'].append(dict(elapsed_seconds=elapsed,rss_bytes=rss));raise RuntimeError('External process-tree budget exceeded')
    time.sleep(.02)
   assert proc.returncode==0
  assert watch['samples'] and not watch['violations'];result=json.loads(workerout.read_text());rr=result['result'];assert rr==json.loads(raw.read_text()) and rr['status']=='ok' and rr['exit_code']==0
  data=json.loads(side.read_text());count=program['mathematical_checks'];assert data['TOTAL']==len(data['checks'])==len(set(data['checks']))==count
  assert data['source_sha256']==program['sha256'] and data['input_sha256']=={e['path']:e['sha256'] for e in program['ordered_inputs']} and data['N5_scopes']==program['N5_scopes']
  assert re.search(r'^TOTAL: '+str(count)+r'$',rr['stdout'],re.M) and Path(result['cache']).resolve()==cache.resolve()
  assert data['resource_limits']=={'seconds':180,'rss_MiB':180} and 0<data['rss_MiB']<180 and data['seconds']<180
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
  with receipt.open('x') as f:json.dump(dict(status='FAILED; preserve evidence, no retry or cap increase' if error else 'CAPTURED; no science verdict',runner=a.runner,error=error,result=result,before=before,after=after,whole_tree_watchdog=watch,elapsed_seconds=time.monotonic()-started,artifacts=[ref(p) for p in [side,raw,workerout,log,cache,live] if p.is_file()],record=ref(rp),cheap=ref(pp),cold=ref(cp),adapter=ref(Path(__file__).resolve()),program_attempts=1,json_reruns=0,mutation_runs=0),f,indent=2);f.write('\n')
 if error:raise RuntimeError('Failed capture preserved at '+str(receipt))
 print(json.dumps(ref(receipt)))
if __name__=='__main__':main()
