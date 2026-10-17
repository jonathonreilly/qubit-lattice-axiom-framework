"""Actual canonical execution with one shared CPU60/wall60 process budget."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import sys

os.environ.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
sys.path.insert(0,str(W/'scripts'))
import runner_cache

runner='scripts/structural_coefficient_box_2026_10_17.py'
output=W/'outputs/structural_coefficient_box_2026_10_17.json'
assert not (D/'CANONICAL_EXECUTION.json').exists(),'Preserve this attempt; a rerun needs a distinct receipt.'
if not output.exists():
    output.write_text('{"status":"not_executed"}\n')
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
result,cache=runner_cache.execute_and_write_cache(runner,timeout_sec=60)
def pin(raw): return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
for stream in ('stdout','stderr'):
    (D/('canonical.'+stream)).write_text(result.get(stream,''))
record={'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runner':runner,'cpu_cap_seconds':60,'external_wall_cap_seconds':60,
        'shared_budget':'Both finite calculations in one primary process; no per-body reset.',
        'status':result.get('status'),'exit_code':result.get('exit_code'),'elapsed_sec':result.get('elapsed_sec'),
        'cache_path':str(cache.relative_to(W)) if cache else None,'cache_status':runner_cache.cache_status(runner),
        'stdout':pin(result.get('stdout','').encode()),'stderr':pin(result.get('stderr','').encode()),
        'runner_at_receipt':pin((W/runner).read_bytes()),'canonical_result':pin(output.read_bytes()),
        'preexecution_output_slots':'Missing canonical output was initialized to not_executed before runner identity capture.',
        'scope':'Actual exact finite algebra only. No stationary refit, coefficient grid, time evolution, hardware experiment or retained audit.'}
if cache: record['cache']=pin(cache.read_bytes())
(D/'CANONICAL_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
assert result.get('exit_code')==0 and result.get('status')=='ok',result
