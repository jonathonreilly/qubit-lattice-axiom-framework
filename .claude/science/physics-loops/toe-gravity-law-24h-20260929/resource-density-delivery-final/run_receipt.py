from pathlib import Path
import os,subprocess,time,signal,json,hashlib,resource
out=Path(__file__).parent; repo=Path('/private/tmp/toe-autonomous-resource-density-20260930'); campaign=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((campaign/'DEADLINE.json').read_text())['deadline_epoch']
stops=[campaign/'STOP_REQUESTED.json',campaign/'STOP_REQUESTED']
assert time.time()<deadline and not any(x.exists() for x in stops)
cmd=['python3','docs/ai_methodology/skills/review-loop/scripts/review_receipt.py','--repo',str(repo),'--record',str(out/'unit-v2.json'),'--cache']
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:env[k]='1'
def limit(): resource.setrlimit(resource.RLIMIT_CPU,(600,600))
start=time.monotonic(); peak=0;reason=None;before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'unit-check.stdout').open('x') as so,(out/'unit-check.stderr').open('x') as se:
 p=subprocess.Popen(cmd,cwd=repo,env=env,stdout=so,stderr=se,start_new_session=True,preexec_fn=limit)
 (out/'RUNNING.json').write_text(json.dumps({'pid':p.pid,'command':cmd,'deadline_epoch':deadline,'cpu_limit':600,'wall_limit':720,'rss_limit_MiB':400})+'\n')
 while p.poll() is None:
  ps=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True)
  rss=sum(int(v[1]) for line in ps.splitlines() if len(v:=line.split())==2 and int(v[0])==p.pid)/1024
  peak=max(peak,rss)
  if time.time()>=deadline:reason='campaign deadline'
  elif any(x.exists() for x in stops):reason='STOP_REQUESTED'
  elif time.monotonic()-start>=720:reason='wall limit'
  elif rss>400:reason='aggregate RSS limit'
  if reason:
   os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=5)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
   break
  time.sleep(2)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
result={'command':cmd,'exit_code':p.returncode,'stop_reason':reason,'wall_seconds':time.monotonic()-start,'cpu_seconds_children':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'sampled_peak_group_RSS_MiB':peak,'record_sha256':hashlib.sha256((out/'unit-v2.json').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256((repo/cmd[1]).read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256((out/'unit-check.stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((out/'unit-check.stderr').read_bytes()).hexdigest(),'scope':'one actual schema2 cache check; no scientific execution, audit or combined integration gate'}
(out/'unit-check-execution.json').write_text(json.dumps(result,indent=2)+'\n');(out/'RUNNING.json').unlink();print(json.dumps(result));raise SystemExit(p.returncode)
