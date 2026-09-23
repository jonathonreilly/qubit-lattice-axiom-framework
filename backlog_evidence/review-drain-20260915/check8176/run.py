from pathlib import Path
import subprocess,time,resource,json,os,sys
out=Path('/private/tmp/review-drain-20260915/check8176');root=Path('/private/tmp/review-drain-20260915/review-draft-slot')
name=sys.argv[1];cmd=sys.argv[2:]
def limits():resource.setrlimit(resource.RLIMIT_CPU,(25,25))
a=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
with (out/(name+'.out')).open('wb') as f:
 try:code=subprocess.run(cmd,cwd=root,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=f,stderr=subprocess.STDOUT,timeout=35,preexec_fn=limits).returncode
 except subprocess.TimeoutExpired:code='timeout'
b=resource.getrusage(resource.RUSAGE_CHILDREN);d=dict(command=cmd,exit=code,wall=time.monotonic()-start,user_cpu=b.ru_utime-a.ru_utime,system_cpu=b.ru_stime-a.ru_stime,max_rss_bytes=b.ru_maxrss,wall_limit=35,cpu_limit=25,memory_design='finite graphs max225 sites; exact layered subset states max2^10; observed RSS')
(out/(name+'.json')).write_text(json.dumps(d,indent=2));print(d)
