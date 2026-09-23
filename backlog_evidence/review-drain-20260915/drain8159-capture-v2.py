"""Author capture with externally sampled supervisor/worker RSS; no review verdict."""
from pathlib import Path
import sys,json,hashlib,subprocess,threading,time,os,signal,re
w=Path('/private/tmp/review-drain-20260915/review-draft-slot');b=w.parent;sys.path.insert(0,str(w/'scripts'));import runner_cache as c
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
recordpath=b/'drain8159-author-unit-draft-v2.json';record=json.loads(recordpath.read_text());prepath=b/'drain8159-author-cheap-v2.json';pre=json.loads(prepath.read_text());assert pre['mechanical_status']=='ok' and pre['tree']==record['source']['tree'] and not pre['cache_checked'] and pre['record_sha256']==sha(recordpath)
coldpath=b/'drain8159-cold-confirmation-v2.json';assert sha(coldpath)=='547ec70fd0c57b4425026442ab7338be13b73574b0865ba37a462edf1d183e1d';cold=json.loads(coldpath.read_text());assert cold['status']=='AFFECTED COLD SOURCE CONFIRMED; REPAIRED HOLONOMY ELIGIBLE AFTER ROOT FRESH CHEAP PREFLIGHT' and cold['tree']==record['source']['tree']
original_record=json.loads((b/'drain8159-author-unit-draft-v1.json').read_text())
original_cold=b/'drain8159-cold-confirmation-v1.json';assert sha(original_cold)=='ba0ef06b15272b36d374c388afa5d4010d6571b6cb8768ab240a80a65a16e457'
old_sources={x['path']:x['sha256'] for x in original_record['source']['paths']};new_sources={x['path']:x['sha256'] for x in record['source']['paths']}
assert old_sources.keys()==new_sources.keys() and {p for p in old_sources if old_sources[p]!=new_sources[p]}=={'scripts/holonomy_check_2026_09_15.py'}
for category,entries in original_record['inputs'].items():
 old={x['path']:x['sha256'] for x in entries};new={x['path']:x['sha256'] for x in record['inputs'][category]};assert old.keys()==new.keys() and all(old[p]==new[p] or p=='scripts/holonomy_check_2026_09_15.py' for p in old)
inputs={x['path']:x['sha256'] for x in record['source']['paths']}
for entries in record['inputs'].values():
 for x in entries:inputs[x['path']]=x['sha256']
cache_names={'logs/runner-cache/'+Path(h).stem+'.txt' for n in record['notes'] for h in [n['primary_runner'],*n['helpers']]}
def verify():
 for p,h in inputs.items():
  if p not in cache_names:assert sha(w/p)==h,p
assert subprocess.check_output(['git','-C',str(w),'write-tree'],text=True).strip()==record['source']['tree']
records=[];caches=[];raw_outputs=[]
planpath=b/'drain8159-capture-plan-v2.json';assert sha(planpath)=='70d375eb86ff8f5de433bfcd0215f518063c5212e8fb2a343c5752248727120c';plan=json.loads(planpath.read_text());assert len(plan['captures'])==41
assessment=b/'drain8159-holonomy-slab-assessment-v1.json';assert sha(assessment)=='6399c3899fc7fe0180d4351ef4efc765effa67c3e9a111e41afb3c3ba2886677';reuse=json.loads(assessment.read_text())['eligible_prior_captures'];assert len(reuse)==13
reused=set();reuse_identity=[]
for item in reuse:
 runner=item['runner'];receipt=Path(item['receipt']['path']);assert sha(receipt)==item['receipt']['sha256'];e=json.loads(receipt.read_text())
 assert e['status']=='ok' and e['exit_code']==0 and not e['whole_tree_watchdog']['violations']
 assert c.cache_status(runner)=='fresh' and c.declared_input_fingerprint(w/runner)==item['declared_input_fingerprint']
 cache,header,body=c.load_cache(runner);assert header['runner_path']==runner and header['status']=='ok' and header['exit_code']=='0'
 assert body.split('----- stdout -----\n',1)[1].split('----- stderr -----',1)[0].rstrip()==e['stdout'].rstrip()
 raw=w/e['raw_output']['path'];assert sha(raw)==e['raw_output']['sha256'];assert sha(Path(e['capture_script']))==e['capture_script_sha256']
 records.append({'pr':Path(runner).stem,'receipt':str(receipt),'sha256':sha(receipt),'reused_unchanged':True});caches.append(cache.relative_to(w).as_posix());raw_outputs.append(raw.relative_to(w).as_posix());reused.add(runner)
 reuse_identity.append({'runner':runner,'cache_sha256':sha(cache),'raw_sha256':sha(raw),'input_fingerprint':item['declared_input_fingerprint']})
verify()
reusefile=b/'drain8159-capture-reuse-v2.json';assert not reusefile.exists();reusefile.write_text(json.dumps(reuse_identity,indent=2)+'\n')
remaining=[x for x in plan['captures'] if x['runner'] not in reused];assert len(remaining)==28
for row in remaining:
 assert sha(w/row['runner'])==row['sha256']
 assert not (w/'logs/runner-cache'/Path(row['runner']).with_suffix('.json').name).exists(),row['runner']
for row in remaining:
 primary=row['runner'];pr=Path(primary).stem;cap_seconds=row['time_cap_seconds'];cap_bytes=row['process_tree_rss_cap_bytes']
 verify();receipt=b/f'drain8159-execution-v2-{pr}.json';assert not receipt.exists();stop=threading.Event();watch={'limit_bytes':cap_bytes,'interval_sec':0.02,'root_pid':os.getpid(),'samples':0,'peak_tree_rss_bytes':0,'violations':[],'boundary':'Externally sampled supervisor and descendants; timeout is enforced by runner cache process execution.'}
 def monitor():
  family={os.getpid()}
  try:
   while not stop.is_set():
    raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=0.5);rows={int(v[0]):(int(v[1]),int(v[2])*1024) for line in raw.splitlines() if len(v:=line.split())==3};family={os.getpid()}
    while True:
     grown=family|{pid for pid,(ppid,rss) in rows.items() if ppid in family}
     if grown==family:break
     family=grown
    rss=sum(rows.get(pid,(0,0))[1] for pid in family);watch['samples']+=1;watch['peak_tree_rss_bytes']=max(watch['peak_tree_rss_bytes'],rss)
    if rss>watch['limit_bytes']:
     watch['violations'].append({'rss_bytes':rss,'pids':sorted(family)})
     for pid in family-{os.getpid()}:
      try:os.kill(pid,signal.SIGKILL)
      except ProcessLookupError:pass
     return
    stop.wait(0.02)
  except BaseException as e:
   watch['violations'].append({'monitor_error':repr(e)})
   try:family.update(map(int,subprocess.check_output(['pgrep','-P',str(os.getpid())],text=True,timeout=0.5).split()))
   except (subprocess.SubprocessError,ValueError,OSError):pass
   for pid in family-{os.getpid()}:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
 thread=threading.Thread(target=monitor,daemon=True);thread.start()
 r=None;cache=None;capture_error=None
 try:r,cache=c.execute_and_write_cache(primary,cap_seconds)
 except BaseException as error:capture_error=repr(error)
 finally:stop.set();thread.join()
 if capture_error is not None:
  failure={'status':'capture_error','error':capture_error,'whole_tree_watchdog':watch,'execution_result_unavailable':True,'capture_script':str(Path(__file__).resolve()),'capture_script_sha256':sha(Path(__file__))};receipt.write_text(json.dumps(failure,indent=2)+'\n');raise RuntimeError('capture failed; exact watchdog/error receipt preserved')
 raw=w/'logs/runner-cache'/Path(primary).with_suffix('.json').name
 if raw.exists():
  json.loads(raw.read_text());r['raw_output']={'path':raw.relative_to(w).as_posix(),'sha256':sha(raw)};raw_outputs.append(raw.relative_to(w).as_posix())
 r['whole_tree_watchdog']=watch;r['capture_script']=str(Path(__file__).resolve());r['capture_script_sha256']=sha(Path(__file__));receipt.write_text(json.dumps(r,indent=2)+'\n');records.append({'pr':pr,'receipt':str(receipt),'sha256':sha(receipt)})
 assert r['status']=='ok' and r['exit_code']==0 and re.search(r'^TOTAL: PASS=[1-9][0-9]* FAIL=0$',r['stdout'],re.M) and not watch['violations'] and watch['samples']>0,r
 assert raw.exists(),('Missing structured output',primary)
 verify();assert c.cache_status(primary)=='fresh';caches.append(cache.relative_to(w).as_posix());print(pr,re.search(r'^TOTAL: PASS=([0-9]+) FAIL=0$',r['stdout'],re.M).group(1),r['elapsed_sec'],watch['peak_tree_rss_bytes'],flush=True)

assert len(records)==41 and len(set(caches))==41 and len(set(raw_outputs))==41
verify()
for item in reuse_identity:
 assert sha(c.cache_path_for(item['runner']))==item['cache_sha256'] and c.cache_status(item['runner'])=='fresh'
subprocess.run(['git','-C',str(w),'add','--',*caches,*raw_outputs],check=True)
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git','-C',str(w),*args],check=True)
g=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();paths=g('diff','--cached','--name-only').splitlines();result={'role':'author exact evidence binding; no source verdict','base':g('rev-parse','HEAD'),'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'inputs':inputs,'executions':records,'raw_output_hashes':{p:sha(w/p) for p in raw_outputs},'preflight_path':str(prepath),'preflight_sha256':sha(prepath)};(b/'drain8159-author-final-freeze.json').write_text(json.dumps(result,indent=2)+'\n');print('FINAL',result['tree'],flush=True)
