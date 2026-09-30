#!/usr/bin/env python3
"""Sequential actual source mutations; never modify canonical inputs or caches."""
from datetime import datetime, timezone
import hashlib
import json
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
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(45,46))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=time.monotonic()
    result=subprocess.run([sys.executable,str(path),'--group',item['group']],cwd=repo,
                          env=env,capture_output=True,text=True,timeout=120,preexec_fn=limit)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    stdout=root/(item['name']+'.stdout.txt');stderr=root/(item['name']+'.stderr.txt')
    stdout.write_text(result.stdout);stderr.write_text(result.stderr)
    row={'name':item['name'],'group':item['group'],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'exit_code':result.returncode,'wall_seconds':time.monotonic()-t,
         'cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
         'assertion_failure':result.returncode!=0 and 'AssertionError' in result.stderr,
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
