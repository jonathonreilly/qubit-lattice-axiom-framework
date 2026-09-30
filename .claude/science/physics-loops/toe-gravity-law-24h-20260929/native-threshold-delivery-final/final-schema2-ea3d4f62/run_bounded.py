from pathlib import Path
import os,sys,time,json,subprocess,resource,signal,datetime,hashlib
root=Path('/private/tmp/toe-native-four-particle-threshold-20260930')
out=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()+720 < deadline
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()=='ea3d4f6236160233f6f9e183b4b6eb5ba3252607'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True).strip()
env=os.environ.copy()
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:env[k]='1'
cmd=[sys.executable,'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py','--repo',str(root),'--record',str(out/'unit-v2.json'),'--cache']
def limits():resource.setrlimit(resource.RLIMIT_CPU,(600,605))
start=time.monotonic();started=datetime.datetime.now(datetime.timezone.utc).isoformat();maxrss=0;reason=None;heartbeat=start
with (out/'receipt.stdout.json').open('wb') as stdout,(out/'receipt.stderr.txt').open('wb') as stderr:
 p=subprocess.Popen(cmd,cwd=root,env=env,stdout=stdout,stderr=stderr,start_new_session=True,preexec_fn=limits)
 print(json.dumps({'started_at_utc':started,'pid':p.pid,'command':cmd}),flush=True)
 while True:
  pid,status,usage=os.wait4(p.pid,os.WNOHANG)
  if pid:break
  now=time.monotonic()
  if (runtime/'STOP_REQUESTED.json').exists():reason='STOP_REQUESTED'
  elif time.time()>=deadline:reason='campaign deadline'
  elif now-start>720:reason='wall limit'
  rows=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True).splitlines()
  data=[tuple(map(int,row.split())) for row in rows if len(row.split())==3]
  descendants={p.pid}
  while True:
   n=descendants|{pid for pid,parent,rss in data if parent in descendants}
   if n==descendants:break
   descendants=n
  rss=1024*sum(rss for pid,parent,rss in data if pid in descendants);maxrss=max(maxrss,rss)
  if rss>400*1024**2:reason='RSS limit'
  if reason:
   os.killpg(p.pid,signal.SIGKILL);pid,status,usage=os.wait4(p.pid,0);break
  if now-heartbeat>=55:
   print(json.dumps({'elapsed_wall_seconds':now-start,'current_process_tree_rss_bytes':rss,'peak_monitored_rss_bytes':maxrss}),flush=True);heartbeat=now
  time.sleep(2)
code=os.waitstatus_to_exitcode(status);p.returncode=code
result={'command':cmd,'started_at_utc':started,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':code,'wall_seconds':time.monotonic()-start,'process_cpu_seconds':usage.ru_utime+usage.ru_stime,'process_peak_rss_bytes':usage.ru_maxrss,'peak_monitored_process_tree_rss_bytes':maxrss,'stop_reason':reason,'record_sha256':hashlib.sha256((out/'unit-v2.json').read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256((out/'receipt.stdout.json').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((out/'receipt.stderr.txt').read_bytes()).hexdigest(),'source_head_after':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'working_tree_clean_after':not subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True).strip()}
(out/'execution.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
sys.exit(0 if code==0 and reason is None else 1)
