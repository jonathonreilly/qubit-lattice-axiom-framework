"""Author capture with externally sampled supervisor/worker RSS; no review verdict."""
from pathlib import Path
import sys,json,hashlib,subprocess,threading,time,os,signal,re
w=Path('/private/tmp/review-drain-20260915/drain-author-slot');b=w.parent;sys.path.insert(0,str(w/'scripts'));import runner_cache as c
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
recordpath=b/'drain8160-author-unit-draft-v2.json';record=json.loads(recordpath.read_text());prepath=b/'drain8160-author-cheap-v2.json';pre=json.loads(prepath.read_text());assert pre['mechanical_status']=='ok' and pre['tree']==record['source']['tree'] and not pre['cache_checked'] and pre['record_sha256']==sha(recordpath)
coldpath=b/'drain8160-cold-confirmation-v2.json';assert sha(coldpath)=='152ff943591d204613fb7d56bb67b485e6f86eca5e2084f7c379c3f4f8bfeb54';cold=json.loads(coldpath.read_text());assert cold['status']=='COLD SOURCE CONFIRMED AFTER NARROW OUTPUT FIX; ELIGIBLE FOR BOUNDED CAPTURES ONLY' and cold['source']['tree']==record['source']['tree']
inputs={x['path']:x['sha256'] for x in record['source']['paths']}
for entries in record['inputs'].values():
 for x in entries:inputs[x['path']]=x['sha256']
cache_names={'logs/runner-cache/'+Path(h).stem+'.txt' for n in record['notes'] for h in [n['primary_runner'],*n['helpers']]}
def verify():
 for p,h in inputs.items():
  if p not in cache_names:assert sha(w/p)==h,p
assert subprocess.check_output(['git','-C',str(w),'write-tree'],text=True).strip()==record['source']['tree']
records=[];caches=[];raw_outputs=[]
for _,runner,_ in [('rotor_uniform_compact_response_check_2026_09_16', 'scripts/rotor_uniform_compact_response_check_2026_09_16.py', 120), ('rotor_integer_gaussian_positive_square_check_2026_09_16', 'scripts/rotor_integer_gaussian_positive_square_check_2026_09_16.py', 120), ('rotor_tree_slater_dressing_check_2026_09_16', 'scripts/rotor_tree_slater_dressing_check_2026_09_16.py', 120), ('rotor_joint_characteristic_check_2026_09_16', 'scripts/rotor_joint_characteristic_check_2026_09_16.py', 120), ('rotor_joint_weyl_car_state_check_2026_09_16', 'scripts/rotor_joint_weyl_car_state_check_2026_09_16.py', 120), ('rotor_joint_gauge_propagation_check_2026_09_16', 'scripts/rotor_joint_gauge_propagation_check_2026_09_16.py', 120), ('rotor_joint_rooted_matter_dynamics_check_2026_09_16', 'scripts/rotor_joint_rooted_matter_dynamics_check_2026_09_16.py', 120)]:assert not (w/'logs/runner-cache'/Path(runner).with_suffix('.json').name).exists(),runner
for pr,primary,cap_seconds in [('rotor_uniform_compact_response_check_2026_09_16', 'scripts/rotor_uniform_compact_response_check_2026_09_16.py', 120), ('rotor_integer_gaussian_positive_square_check_2026_09_16', 'scripts/rotor_integer_gaussian_positive_square_check_2026_09_16.py', 120), ('rotor_tree_slater_dressing_check_2026_09_16', 'scripts/rotor_tree_slater_dressing_check_2026_09_16.py', 120), ('rotor_joint_characteristic_check_2026_09_16', 'scripts/rotor_joint_characteristic_check_2026_09_16.py', 120), ('rotor_joint_weyl_car_state_check_2026_09_16', 'scripts/rotor_joint_weyl_car_state_check_2026_09_16.py', 120), ('rotor_joint_gauge_propagation_check_2026_09_16', 'scripts/rotor_joint_gauge_propagation_check_2026_09_16.py', 120), ('rotor_joint_rooted_matter_dynamics_check_2026_09_16', 'scripts/rotor_joint_rooted_matter_dynamics_check_2026_09_16.py', 120)]:
 verify();receipt=b/f'drain8160-execution-v2-{pr}.json';assert not receipt.exists();stop=threading.Event();watch={'limit_bytes':512*1048576,'interval_sec':0.02,'root_pid':os.getpid(),'samples':0,'peak_tree_rss_bytes':0,'violations':[],'boundary':'Externally sampled supervisor and descendants; timeout is enforced by runner cache process execution.'}
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

subprocess.run(['git','-C',str(w),'add','--',*caches,*raw_outputs],check=True)
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git','-C',str(w),*args],check=True)
g=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();paths=g('diff','--cached','--name-only').splitlines();result={'role':'author exact evidence binding; no source verdict','base':g('rev-parse','HEAD'),'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'inputs':inputs,'executions':records,'raw_output_hashes':{p:sha(w/p) for p in raw_outputs},'preflight_path':str(prepath),'preflight_sha256':sha(prepath)};(b/'drain8160-author-final-freeze.json').write_text(json.dumps(result,indent=2)+'\n');print('FINAL',result['tree'],flush=True)
