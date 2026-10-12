from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, platform, subprocess, sys, time

ROOT=Path('/private/tmp/local-vector-final-validation-20261012')
OUT=Path(__file__).resolve().parent
RUNTIME=OUT.parents[1]
DEADLINE=json.loads((RUNTIME/'DEADLINE.json').read_text())
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *args:subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
expected='039198fed41d5599341bbcbc7908dcfae1215421'
tree='57d24afbe33c77b915df34783db40e6f2969fa89'
assert git('rev-parse','HEAD')==expected and git('rev-parse','HEAD^{tree}')==tree
assert not git('status','--porcelain','--untracked-files=no')
commands=[['bash','docs/audit/scripts/run_pipeline.sh','--stage-citation-manifest'],
          [sys.executable,'docs/audit/scripts/audit_lint.py','--strict'],
          [sys.executable,'docs/audit/scripts/check_changed_audit_evidence.py','--base','origin/main','--include-worktree','--json']]
result={'base':git('rev-parse','origin/main'),'commit':expected,'tree':tree,
        'worktree':str(ROOT),'driver_pid':os.getpid(),'started_at':now(),
        'scope':'Exact final source/evidence package; mechanical validation only, no audit or landing.',
        'unit_record_sha256':sha(OUT/'UNIT_v1.json'),'python':sys.version,
        'platform':platform.platform(),'commands':commands,'results':[]}
(OUT/'START_v1.json').write_text(json.dumps(result,indent=2)+'\n')
env={**os.environ,'PATH':'/usr/local/bin:'+os.environ.get('PATH',''),
     'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
for i,command in enumerate(commands,1):
    seconds=min(900,DEADLINE['packaging_epoch']-time.time())
    if seconds<=0:raise RuntimeError('Campaign packaging cutoff reached')
    log=OUT/f'gate-{i}_v1.log';reason=None
    with log.open('x') as f:
        try:code=subprocess.run(command,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=seconds).returncode
        except subprocess.TimeoutExpired:code=None;reason='timeout'
    result['results'].append({'command':command,'exit':code,'reason':reason,'log':str(log),'sha256':sha(log)})
    (OUT/'PROGRESS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['results'][-1]),flush=True)
    if code!=0:break
result['finished_at']=now()
(OUT/'RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
if any(v['exit']!=0 for v in result['results']) or len(result['results'])!=3:raise SystemExit(1)
