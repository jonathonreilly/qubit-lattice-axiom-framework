#!/usr/bin/env python3
"""Use the repository's canonical content-bound cache, exactly once."""
import json
from pathlib import Path
import sys

repo = Path('/private/tmp/toe-native-dilute-thermodynamics-20260930')
sys.path.insert(0, str(repo/'scripts'))
import runner_cache

runner = 'scripts/native_dilute_thermodynamics_2026_09_30.py'
result_path = Path('/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/native-dilute-thermodynamics-milestone-cold-read/review-correction/REFRESH_CACHE_RESULT.json')
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
