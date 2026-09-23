import subprocess,time,os,signal,json,pathlib,hashlib
b=pathlib.Path('/private/tmp/review-drain-20260915');src=b/'drain8180-independent-controls.py';out=b/'drain8180-independent-controls.stdout';err=b/'drain8180-independent-controls.stderr'
start=time.monotonic();peak=0;samples=0;violation=None
with out.open('xb') as o,err.open('xb') as e:
 p=subprocess.Popen(['/usr/local/bin/python3',str(src)],stdout=o,stderr=e,start_new_session=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1'})
 while p.poll() is None:
  raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True);rows={int(v[0]):(int(v[1]),int(v[2])*1024) for line in raw.splitlines() if len(v:=line.split())==3};family={p.pid}
  while True:
   expanded=family|{k for k,v in rows.items() if v[0] in family}
   if expanded==family:break
   family=expanded
  rss=sum(rows[k][1] for k in family if k in rows);peak=max(peak,rss);samples+=1
  if rss>384*1048576 or time.monotonic()-start>30:
   violation='memory' if rss>384*1048576 else 'time';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.02)
 code=p.wait()
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r={'source':str(src),'source_sha256':h(src),'supervisor_sha256':h(pathlib.Path(__file__)),'exit_code':code,'elapsed_seconds':time.monotonic()-start,'peak_worker_tree_rss_bytes':peak,'samples':samples,'limits':{'seconds':30,'bytes':384*1048576},'violation':violation,'stdout_sha256':h(out),'stderr_sha256':h(err)}
(b/'drain8180-independent-controls-execution.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));assert code==0 and violation is None
