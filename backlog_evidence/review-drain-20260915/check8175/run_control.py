import pathlib,subprocess,time,resource,json,os
r=pathlib.Path('/private/tmp/review-drain-20260915/drain-author-slot');o=pathlib.Path('/private/tmp/review-drain-20260915/check8175');p=next(r.glob('scripts/*sharper_bad_pair_budget_false*.py'))
# Cold clearance: complete primary and declared note read, axiom quote authority checked,
# finite menu input inspected for actual product rule; no external data/dynamic imports.
# 300 cones depth <=8; max165 sites each; finite 225-site witnesses; four exact certs.
# 30 sec wall /20sec CPU, expected <100MiB; resource RSS measured.
cmd=['python3',str(p)];start=time.monotonic()
def limits():resource.setrlimit(resource.RLIMIT_CPU,(20,20))
with (o/'original-primary.out').open('wb') as f:
 try: res=subprocess.run(cmd,cwd=r,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=f,stderr=subprocess.STDOUT,timeout=30,preexec_fn=limits);code=res.returncode
 except subprocess.TimeoutExpired:code='timeout'
u=resource.getrusage(resource.RUSAGE_CHILDREN);data={'command':cmd,'exit':code,'wall_seconds':time.monotonic()-start,'user_cpu':u.ru_utime,'system_cpu':u.ru_stime,'max_rss_bytes':u.ru_maxrss,'wall_limit':30,'cpu_limit':20,'memory_design':'finite 225-site windows; observed RSS; OS AS cap unsupported (preserved failure)'};(o/'original-primary-resource.json').write_text(json.dumps(data,indent=2)+'\n');print(data)
