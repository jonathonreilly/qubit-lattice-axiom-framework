#!/usr/bin/env python3
"""Sequential actual source mutations; never modify canonical inputs or caches."""
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

pack=Path(__file__).resolve().parent
repo=pack.parents[3]
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
plan=json.loads((pack/'MUTATION_PLAN.json').read_text())
source=(repo/plan['runner']).read_text()
assert hashlib.sha256(source.encode()).hexdigest()==plan['runner_sha256']
root=pack/'mutations'
root.mkdir(exist_ok=True)
summary=root/'SUMMARY.json'
if summary.exists():raise SystemExit('Refusing to overwrite mutation summary.')
rows=[]
TOTAL_CPU=60
worker_cpu_start=time.process_time()
children_start=resource.getrusage(resource.RUSAGE_CHILDREN)
def used_cpu():
    current=resource.getrusage(resource.RUSAGE_CHILDREN)
    return (time.process_time()-worker_cpu_start+current.ru_utime+current.ru_stime
            -children_start.ru_utime-children_start.ru_stime)
def cpu_seconds(text):
    total=0.0
    for part in text.strip().split(':'):total=60*total+float(part)
    return total
for item in plan['mutations']:
    if time.time()>=deadline or (runtime/'STOP_REQUESTED.json').exists():
        raise SystemExit('Campaign stop/deadline before next mutation.')
    path=root/(item['name']+'.py')
    if path.exists():raise SystemExit('Refusing to overwrite '+str(path))
    assert source.count(item['old'])==1
    altered=source.replace(item['old'],item['new'])
    path.write_text(altered)
    env=dict(os.environ)
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
        env[key]='1'
    env['PYTHONDONTWRITEBYTECODE']='1'
    remaining=TOTAL_CPU-used_cpu()
    if remaining<=2:
        summary.write_text(json.dumps({'outcome':'cumulative CPU budget exhausted before next child','rows':rows,'cpu_seconds':used_cpu()},indent=2)+'\n')
        raise SystemExit('Cumulative mutation CPU budget exhausted.')
    # Reserve at least one CPU second for the supervisor. The live poll below
    # also counts completed children, supervisor work and ps accounting work.
    child_soft=min(10,math.floor(remaining)-1)
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(child_soft,child_soft+1))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=time.monotonic()
    stdout=root/(item['name']+'.stdout.txt');stderr=root/(item['name']+'.stderr.txt')
    reason=None
    with stdout.open('wb') as sout,stderr.open('wb') as serr:
        child=subprocess.Popen([sys.executable,str(path),'--group',item['group']],cwd=repo,
                               env=env,stdout=sout,stderr=serr,preexec_fn=limit)
        try:
            while child.poll() is None:
                sample=subprocess.run(['/bin/ps','-p',str(child.pid),'-o','time='],capture_output=True,text=True)
                live=cpu_seconds(sample.stdout) if sample.stdout.strip() else 0.0
                if used_cpu()+live>=TOTAL_CPU:reason='cumulative_cpu_budget'
                elif time.monotonic()-t>30:reason='mutation_wall_budget'
                elif time.time()>=deadline:reason='campaign_deadline'
                elif (runtime/'STOP_REQUESTED.json').exists():reason='STOP_REQUESTED'
                if reason:
                    child.kill()
                    break
                time.sleep(0.25)
            code=child.wait()
        except BaseException:
            child.kill();child.wait();raise
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    if used_cpu()>=TOTAL_CPU:reason='cumulative_cpu_budget'
    stderr_text=stderr.read_text()
    row={'name':item['name'],'group':item['group'],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'exit_code':code,'termination_reason':reason,'cumulative_cpu_seconds':used_cpu(), 'child_cpu_soft_limit':child_soft,'wall_seconds':time.monotonic()-t,
         'cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
         'assertion_failure':reason is None and code==1 and 'AssertionError' in stderr_text,
         'stdout_sha256':hashlib.sha256(stdout.read_bytes()).hexdigest(),
         'stderr_sha256':hashlib.sha256(stderr.read_bytes()).hexdigest()}
    rows.append(row)
    (root/(item['name']+'.execution.json')).write_text(json.dumps(row,indent=2)+'\n')
    if not row['assertion_failure']:
        summary.write_text(json.dumps({'outcome':'unexpected survivor or infrastructure failure','rows':rows},indent=2)+'\n')
        raise SystemExit('Mutation did not fail by an assertion: '+item['name'])
summary.write_text(json.dumps({'outcome':'all declared mutations failed by assertions','rows':rows,
 'canonical_runner_unchanged':hashlib.sha256((repo/plan['runner']).read_bytes()).hexdigest()==plan['runner_sha256'],
 'finished_utc':datetime.now(timezone.utc).isoformat()},indent=2)+'\n')
print(json.dumps({'mutations':len(rows),'all_assertion_failures':True},indent=2))
