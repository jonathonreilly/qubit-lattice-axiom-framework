#!/usr/bin/env python3
"""Run one COMBO exact-check child under the registered resource guards."""
from pathlib import Path
import datetime
import fcntl
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')


def gate():
    native = subprocess.check_output(['/usr/bin/memory_pressure', '-Q'], text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%', native).group(1))
    load = os.getloadavg()[0]
    return dict(load1=load, free_percent=free, passed=load < 8 and free >= 30)


def rss(pid):
    output = subprocess.run(['/bin/ps', '-o', 'rss=', '-p', str(pid)],
                            capture_output=True, text=True)
    return int(output.stdout.strip() or '0') * 1024


def main():
    result_path = HERE / 'combo_results.json'
    receipt_path = HERE / 'combo_run.json'
    stderr_path = HERE / 'combo_stderr.txt'
    if any(p.exists() for p in (result_path, receipt_path, stderr_path)):
        raise RuntimeError('Preserve existing run evidence; no implicit overwrite/replay.')
    receipt = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   nice=os.getpriority(os.PRIO_PROCESS, 0),
                   threads={key: os.environ.get(key) for key in THREADS},
                   rss_limit_bytes=800 * 1024 ** 2, time_limit_seconds=60,
                   guards=[], passed=False)
    child = None
    try:
        with (HERE / 'combo_numeric.lock').open('a+') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            receipt['exclusive_lock'] = str(lock.name)
            assert receipt['nice'] >= 10, 'nice guard failed'
            assert all(os.environ.get(key) == '1' for key in THREADS), 'thread guard failed'
            first = gate()
            receipt['guards'].append(first)
            assert first['passed'], 'initial load/memory guard failed'
            env = dict(os.environ, COMBO_GUARDED='1', PYTHONDONTWRITEBYTECODE='1')
            started = time.monotonic()
            next_gate = started
            peak = 0
            with result_path.open('x') as out, stderr_path.open('x') as err:
                child = subprocess.Popen([sys.executable, '-B', str(HERE / 'combo_exact.py')],
                                         stdout=out, stderr=err, env=env)
                while child.poll() is None:
                    now = time.monotonic()
                    peak = max(peak, rss(child.pid) + rss(os.getpid()))
                    assert peak < receipt['rss_limit_bytes'], 'combined RSS guard failed'
                    assert now - started < receipt['time_limit_seconds'], 'time guard failed'
                    if now >= next_gate:
                        current = gate()
                        receipt['guards'].append(current)
                        assert current['passed'], 'runtime load/memory guard failed'
                        next_gate = now + 1
                    time.sleep(0.05)
                receipt['exit_code'] = child.returncode
            receipt['elapsed_seconds'] = time.monotonic() - started
            result = json.loads(result_path.read_text())
            peak = max(peak, result['peak_rss_bytes'] +
                       resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            receipt['peak_combined_rss_bytes'] = peak
            final = gate()
            receipt['guards'].append(final)
            receipt['passed'] = (child.returncode == 0 and result['passed'] and final['passed']
                                 and peak < receipt['rss_limit_bytes']
                                 and receipt['elapsed_seconds'] < receipt['time_limit_seconds'])
            receipt['checks_passed'] = sum(r['passed'] for r in result['records'])
            receipt['checks_total'] = len(result['records'])
            receipt['result_sha256'] = hashlib.sha256(result_path.read_bytes()).hexdigest()
    except BaseException as exc:
        if child is not None and child.poll() is None:
            child.kill()
            child.wait()
        receipt['failure'] = repr(exc)
    with receipt_path.open('x') as out:
        json.dump(receipt, out, indent=2)
        out.write('\n')
    print(json.dumps(receipt, indent=2))
    return 0 if receipt['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
