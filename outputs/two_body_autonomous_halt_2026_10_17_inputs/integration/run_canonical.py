"""Actual canonical execution through the existing cache authority."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import sys

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
N = Path(__file__).resolve().parents[1]
W = N.parent/'correlation_worktree'
D = N/'two_body_integration'
sys.path.insert(0, str(W/'scripts'))
import runner_cache

runner = 'scripts/two_body_autonomous_halt_2026_10_17.py'
for name in ['two_body_autonomous_halt_2026_10_17.json',
             'two_body_autonomous_halt_2026_10_17_point_witnesses.json']:
    p = W/'outputs'/name
    if not p.exists():
        p.write_text('{"status":"not_executed"}\n')
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result, cache = runner_cache.execute_and_write_cache(runner, timeout_sec=120)
record = {'started_utc': started,
          'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'runner': runner, 'timeout_sec': 120,
          'status': result.get('status'), 'exit_code': result.get('exit_code'),
          'elapsed_sec': result.get('elapsed_sec'),
          'cache_path': str(cache), 'cache_status': runner_cache.cache_status(runner),
          'stdout_bytes': len(result.get('stdout','').encode()),
          'stderr_bytes': len(result.get('stderr','').encode()),
          'stdout_sha256': hashlib.sha256(result.get('stdout','').encode()).hexdigest(),
          'stderr_sha256': hashlib.sha256(result.get('stderr','').encode()).hexdigest(),
          'preexecution_output_slots': 'Missing output files were explicitly initialized as not_executed before identity capture, avoiding output-parent creation during execution.',
          'scope': 'Exact finite certificate and separate checker execution only; no large-clock evolution, infinite-time experiment or retained audit.'}
if cache:
    raw = cache.read_bytes()
    record.update(cache_bytes=len(raw), cache_sha256=hashlib.sha256(raw).hexdigest())
(D/'CANONICAL_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if result.get('exit_code') != 0 or result.get('status') != 'ok':
    print(result.get('stderr',''))
    raise SystemExit(1)
