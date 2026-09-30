#!/usr/bin/env python3
"""Execute the frozen primary through the repository's actual cache writer."""
from pathlib import Path
import sys
AUDIT_TIMEOUT_SEC = 60
repo = Path(__file__).resolve().parents[4]
sys.path.insert(0,str(repo/'scripts'))
import runner_cache
runner = 'scripts/original_microscopic_local_output_2026_09_30.py'
result, cache_path = runner_cache.execute_and_write_cache(runner, timeout_sec=60)
print(result)
print('CACHE',cache_path)
ok = result.get('status') == 'ok' and result.get('exit_code') == 0 and runner_cache.cache_status(runner) == 'fresh'
print('TOTAL: PASS=%d FAIL=%d' % (int(ok),int(not ok)))
raise SystemExit(0 if ok else 1)
