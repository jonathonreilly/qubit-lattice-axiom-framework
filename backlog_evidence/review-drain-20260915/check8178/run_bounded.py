import subprocess,time,os,signal,json,pathlib,sys,hashlib
r=pathlib.Path(__file__).parent;cmd=[sys.executable,str(r/'independent.py')];limit=30;memory=192*1024*1024
plan=dict(command=cmd,wall_limit_seconds=limit,rss_limit_bytes=memory,poll_seconds=.02,scope='supervisor and child process tree sampled RSS; enforce by kill group',simulation_runs=0)
(r/'plan.json').write_text(json.dumps(plan,indent=2));start=time.monotonic();peak=0;samples=0;failure=None
with (r/'stdout.json').open('x') as out,(r/'stderr.txt').open('x') as err:
 p=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 while p.poll() is None:
  rows={int(a):(int(b),int(c)*1024) for a,b,c in (line.split() for line in subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True).splitlines())};family={p.pid}
  while True:
   nxt=family|{pid for pid,(ppid,rss) in rows.items() if ppid in family}
   if nxt==family:break
   family=nxt
  rss=sum(rows.get(pid,(0,0))[1] for pid in family|{os.getpid()});peak=max(peak,rss);samples+=1
  if time.monotonic()-start>limit or rss>memory:
   failure='wall' if time.monotonic()-start>limit else 'RSS';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.02)
 p.wait()
(r/'receipt.json').write_text(json.dumps(dict(plan=plan,exit_code=p.returncode,failure=failure,elapsed=time.monotonic()-start,peak_rss_bytes=peak,samples=samples,script_sha256=hashlib.sha256((r/'independent.py').read_bytes()).hexdigest()),indent=2))
print((r/'receipt.json').read_text())
