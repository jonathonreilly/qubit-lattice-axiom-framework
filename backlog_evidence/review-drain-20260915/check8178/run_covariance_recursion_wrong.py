import subprocess,time,os,signal,json,pathlib,sys,hashlib
r=pathlib.Path(__file__).parent;cmd=[sys.executable, '/private/tmp/review-drain-20260915/review-draft-slot/scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py','--mutation', 'covariance_recursion_wrong'];limit=60;memory=384*1024*1024
plan=dict(command=cmd,wall_limit_seconds=limit,rss_limit_bytes=memory,poll_seconds=.02,scope='supervisor and child process tree sampled RSS; enforce by kill group',simulation_runs=0)
(r/'covariance_recursion_wrong-plan.json').write_text(json.dumps(plan,indent=2));start=time.monotonic();peak=0;samples=0;failure=None
with (r/'covariance_recursion_wrong.stdout.txt').open('x') as out,(r/'covariance_recursion_wrong.stderr.txt').open('x') as err:
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
(r/'covariance_recursion_wrong-receipt.json').write_text(json.dumps(dict(plan=plan,exit_code=p.returncode,failure=failure,elapsed=time.monotonic()-start,peak_rss_bytes=peak,samples=samples,script_sha256=hashlib.sha256(pathlib.Path(cmd[1]).read_bytes()).hexdigest()),indent=2))
print((r/'covariance_recursion_wrong-receipt.json').read_text())
