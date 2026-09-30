#!/usr/bin/env python3
"""Use the repository's canonical content-bound cache, exactly once."""
import json
from pathlib import Path
import sys

repo = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(repo/'scripts'))
import runner_cache

runner = 'scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py'
result_path = Path(__file__).resolve().parent/'primary'/'cache_result.json'
if result_path.exists():
    raise SystemExit('Refusing to overwrite primary result evidence.')
result_path.parent.mkdir(parents=True, exist_ok=True)
result, cache = runner_cache.execute_and_write_cache(runner, timeout_sec=180)
result_path.write_text(json.dumps({'result': result, 'cache': str(cache),
    'freshness_after_execution': runner_cache.cache_status(runner)}, indent=2)+'\n')
print(result['stdout'], end='')
if result.get('stderr'):
    print(result['stderr'], file=sys.stderr, end='')
raise SystemExit(0 if result['status'] == 'ok' and result['exit_code'] == 0 else 1)
