#!/usr/bin/env python3
"""Guarded serial algebra checker; preserves all existing evidence."""
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
CAP = 800*1024**2
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')


def gate():
    raw = subprocess.check_output(['/usr/bin/memory_pressure', '-Q'], text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%', raw).group(1))
    loads = os.getloadavg()
    return dict(free_percent=free, loads=loads, passed=free >= 30 and max(loads) < 8)


def rss(pid):
    raw = subprocess.run(['/bin/ps', '-o', 'rss=', '-p', str(pid)],
                         capture_output=True, text=True)
    return int(raw.stdout.strip() or '0')*1024


def main():
    attempt = sys.argv[1] if len(sys.argv) > 1 else '01'
    assert re.fullmatch(r'\d\d', attempt)
    prefix = f'k4corr_attempt{attempt}'
    outpath = HERE/(prefix+'_results.json')
    errpath = HERE/(prefix+'_stderr.txt')
    receiptpath = HERE/(prefix+'_run.json')
    assert not any(p.exists() for p in (outpath, errpath, receiptpath)), 'preserve existing evidence'
    report = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  passed=False, cap_bytes=CAP, guards=[], locks=[], pools=False)
    child, locks = None, []
    start = time.monotonic()
    try:
        nice = os.getpriority(os.PRIO_PROCESS, 0)
        assert nice >= 10
        assert all(os.environ.get(t) == '1' for t in THREADS)
        report.update(nice=nice, threads={t: os.environ[t] for t in THREADS})
        for name, mode in (('k4corr_numeric.lock', 'a+'),
                           ('k4match_numeric.lock', 'r'),
                           ('cumul_numeric.lock', 'r'),
                           ('combo_numeric.lock', 'r')):
            lock = (HERE/name).open(mode)
            locks.append(lock)
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            report['locks'].append(name)
        report['source_sha256'] = {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                                  for n in ('k4corr_criteria.md', 'k4corr_exact.py', 'k4corr_run.py')}
        g = gate()
        report['guards'].append(g)
        assert g['passed'], g
        peak, next_gate = rss(os.getpid()), start
        with outpath.open('x') as out, errpath.open('x') as err:
            env = dict(os.environ, K4CORR_WATCHDOG='1')
            child = subprocess.Popen([sys.executable, '-I', '-B', str(HERE/'k4corr_exact.py')],
                                     env=env, stdout=out, stderr=err)
            while child.poll() is None:
                now = time.monotonic()
                peak = max(peak, rss(os.getpid())+rss(child.pid))
                assert peak < CAP and now-start < 60, 'RSS/time guard'
                if now >= next_gate:
                    g = gate()
                    report['guards'].append(g)
                    assert g['passed'], g
                    next_gate = now+0.5
                time.sleep(0.02)
        data = json.loads(outpath.read_text())
        parent_peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if sys.platform != 'darwin':
            parent_peak *= 1024
        peak = max(peak, parent_peak+max((g['peak_rss_bytes'] for g in data['guards']), default=0))
        g = gate()
        report['guards'].append(g)
        report.update(exit_code=child.returncode, assertion_count=data['assertion_count'],
                      peak_combined_rss_bytes=peak,
                      passed=data['passed'] and child.returncode == 0 and g['passed'] and peak < CAP)
    except BaseException as exc:
        if child is not None and child.poll() is None:
            child.kill()
            child.wait()
        report['failure'] = repr(exc)
    finally:
        for lock in reversed(locks):
            lock.close()
    report['elapsed_seconds'] = time.monotonic()-start
    with receiptpath.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
