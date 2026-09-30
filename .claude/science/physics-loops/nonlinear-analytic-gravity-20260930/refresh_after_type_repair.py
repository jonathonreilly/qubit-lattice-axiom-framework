#!/usr/bin/env python3
"""Actual cache refresh after the authorized documentary source repair."""
import datetime
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

PACK = Path(__file__).resolve().parent
ROOT = PACK.parents[3]
sys.path.insert(0, str(PACK))
from graph_build_monitor import guard, THREAD_NAMES


def child():
    sys.path.insert(0, str(ROOT / 'scripts'))
    import runner_cache
    result, cache = runner_cache.execute_and_write_cache(
        'scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py',
        timeout_sec=180)
    record = {'executed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'reason': 'Source input rebind after Type/Status separator repair; primary code unchanged.',
              'result': result, 'cache': str(cache) if cache else None}
    (PACK / 'PRIMARY_EXECUTION.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'exit_code', 'elapsed_sec')}) , flush=True)
    return 0 if result['status'] == 'ok' and result['exit_code'] == 0 else 1


def main():
    assert guard() is None, guard()
    env = dict(os.environ)
    env.update({key: '1' for key in THREAD_NAMES})
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    started_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.monotonic()
    reason = None
    proc = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), '--child'],
                            cwd=ROOT, env=env, start_new_session=True)
    try:
        while proc.poll() is None:
            reason = guard()
            if reason is None and time.monotonic() - start > 180:
                reason = 'outer_180_second_wall_limit'
            if reason:
                os.killpg(proc.pid, signal.SIGKILL)
                break
            time.sleep(1)
    except BaseException:
        if proc.poll() is None:
            os.killpg(proc.pid, signal.SIGKILL)
        proc.wait()
        raise
    code = proc.wait()
    record = {'started_at': started_at, 'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'wall_seconds': time.monotonic() - start, 'exit_code': code,
              'termination_reason': reason, 'wall_limit_seconds': 180,
              'runner_cpu_soft_limit_seconds': 90, 'runner_cpu_hard_limit_seconds': 95,
              'guard_at_finish': guard(), 'thread_environment': {key: env[key] for key in THREAD_NAMES},
              'runner_method': 'runner_cache.execute_and_write_cache with timeout_sec=180',
              'scope': 'Author reexecution after documentary repair; not independent review.'}
    (PACK / 'TYPE_REPAIR_REFRESH_METRICS.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps(record, indent=2), flush=True)
    return code if code >= 0 else 128 - code


if __name__ == '__main__':
    raise SystemExit(child() if '--child' in sys.argv else main())
