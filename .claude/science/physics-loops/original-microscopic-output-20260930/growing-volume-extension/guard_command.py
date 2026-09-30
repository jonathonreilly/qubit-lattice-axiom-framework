#!/usr/bin/env python3
"""Bound one author validation command; no scientific or review verdict."""
from __future__ import annotations
import argparse,datetime,hashlib,json,os,resource,signal,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--name',required=True);p.add_argument('--cpu',type=int,required=True);p.add_argument('--wall',type=int,required=True);p.add_argument('--rss',type=int,required=True);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
if not cmd:raise SystemExit('missing command')
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
root=Path(__file__).resolve().parents[5];out=Path(__file__).resolve().parent
limit=json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
if time.time()>=limit or (runtime/'STOP_REQUESTED.json').exists():raise SystemExit('deadline/STOP before launch')
def bounds():resource.setrlimit(resource.RLIMIT_CPU,(a.cpu,a.cpu+1))
env=dict(os.environ)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN);peak=0;reason=None
with (out/(a.name+'.stdout')).open('wb') as so,(out/(a.name+'.stderr')).open('wb') as se:
 child=subprocess.Popen(cmd,cwd=root,env=env,stdout=so,stderr=se,start_new_session=True,preexec_fn=bounds)
 while child.poll() is None:
  if time.time()>=limit:reason='campaign deadline'
  elif (runtime/'STOP_REQUESTED.json').exists():reason='STOP_REQUESTED'
  elif time.monotonic()-start>a.wall:reason='wall limit'
  raw=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True)
  rss=sum(int(b) for x in raw.splitlines() if len(v:=x.split())==2 for g,b in [v] if int(g)==child.pid)
  peak=max(peak,rss)
  if rss>a.rss*1024:reason='sampled process-group RSS limit'
  if reason:
   os.killpg(child.pid,signal.SIGTERM)
   try:child.wait(timeout=3)
   except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
   break
  time.sleep(1)
 code=child.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
x={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'workdir':str(root),'exit_code':code,'stop_reason':reason,'wall_seconds':time.monotonic()-start,'child_cpu_seconds_including_monitor_ps':cpu,'sampled_peak_process_group_RSS_MiB':peak/1024,'limits':{'cpu_seconds_per_inherited_process':a.cpu,'wall_seconds':a.wall,'sampled_group_RSS_MiB':a.rss},'CPU_price_exceeded_at_return':cpu>a.cpu,'BLAS_threads':1,'scope':'Actual author validation execution; RSS is sampled, not an OS allocation limit; no scientific or review verdict.'}
for kind in ('stdout','stderr'):x[kind+'_sha256']=hashlib.sha256((out/(a.name+'.'+kind)).read_bytes()).hexdigest()
(out/(a.name+'_EXECUTION.json')).write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x,indent=2))
raise SystemExit(0 if code==0 and not reason and cpu<=a.cpu else 1)
