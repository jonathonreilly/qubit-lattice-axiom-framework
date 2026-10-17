"""Execute the final canonical source through the repository cache authority."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
sys.path.insert(0, str(W/'scripts'))
import runner_cache

runner = 'scripts/autonomous_boundary_reflection_2026_10_16.py'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result, cache = runner_cache.execute_and_write_cache(runner, timeout_sec=120)
record = {'started_utc': started, 'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'runner':runner, 'timeout_sec':120, 'exit_code':result.get('exit_code'),
          'status':result.get('status'), 'elapsed_sec':result.get('elapsed_sec'),
          'cache_path':str(cache), 'cache_status':runner_cache.cache_status(runner),
          'stdout_bytes':len(result.get('stdout','').encode()),
          'stderr_bytes':len(result.get('stderr','').encode()),
          'stdout_sha256':hashlib.sha256(result.get('stdout','').encode()).hexdigest(),
          'stderr_sha256':hashlib.sha256(result.get('stderr','').encode()).hexdigest(),
          'limitation':'Actual finite computations and exact finite symbolic identities; no finite run verifies all future time or infinite volume.'}
if cache:
    b=cache.read_bytes(); record['cache_bytes']=len(b); record['cache_sha256']=hashlib.sha256(b).hexdigest()
(N/'reflection_integration/CANONICAL_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if result.get('exit_code') != 0 or result.get('status') != 'ok':
    print(result.get('stderr',''))
    raise SystemExit(1)
