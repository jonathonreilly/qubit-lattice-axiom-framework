#!/usr/bin/env python3
"""One serial numeric child with an exclusive lock and resource watchdog."""
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
THREADS = ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')


def gate():
    memory = subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%',memory).group(1))
    load = os.getloadavg()[0]
    return dict(load1=load,free_percent=free,passed=load < 8 and free >= 30)


def rss(pid):
    p = subprocess.run(['/bin/ps','-o','rss=','-p',str(pid)],capture_output=True,text=True)
    return int(p.stdout.strip() or '0')*1024


def main():
    receipt = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   nice=os.getpriority(os.PRIO_PROCESS,0),
                   threads={k:os.environ.get(k) for k in THREADS},
                   limit_bytes=800*1024**2,guards=[],passed=False)
    target = HERE/'cumul_results.json'
    receipt_path = HERE/'cumul_run.json'
    if target.exists() or receipt_path.exists():
        raise RuntimeError('Preserve existing run evidence; choose a separately registered replay filename.')
    child = None
    try:
        with (HERE/'cumul_numeric.lock').open('a+') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
            receipt['exclusive_lock'] = str(lock.name)
            assert receipt['nice'] >= 10, 'nice guard failed'
            assert all(os.environ.get(k) == '1' for k in THREADS), 'thread guard failed'
            initial = gate()
            receipt['guards'].append(initial)
            assert initial['passed'], 'initial load/memory guard failed'
            env = dict(os.environ,CUMUL_GUARDED='1',PYTHONDONTWRITEBYTECODE='1')
            start = time.monotonic()
            peak = 0
            next_gate = start
            with target.open('x') as out, (HERE/'cumul_stderr.txt').open('x') as err:
                child = subprocess.Popen([sys.executable,'-B',str(HERE/'cumul_exact.py')],
                                         stdout=out,stderr=err,env=env)
                while child.poll() is None:
                    now = time.monotonic()
                    current = rss(child.pid)+rss(os.getpid())
                    peak = max(peak,current)
                    assert current < receipt['limit_bytes'], 'RSS guard failed'
                    assert now-start < 90, 'wall-time guard failed'
                    if now >= next_gate:
                        g = gate()
                        receipt['guards'].append(g)
                        assert g['passed'], 'runtime load/memory guard failed'
                        next_gate = now+1
                    time.sleep(0.1)
                receipt['exit_code'] = child.returncode
            receipt['elapsed_seconds'] = time.monotonic()-start
            data = json.loads(target.read_text())
            peak = max(peak,data['peak_rss_bytes']+resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            receipt['peak_combined_rss_bytes'] = peak
            final = gate()
            receipt['guards'].append(final)
            receipt['passed'] = (child.returncode == 0 and data['passed'] and final['passed']
                                 and peak < receipt['limit_bytes'])
            receipt['result_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    except BaseException as exc:
        if child is not None and child.poll() is None:
            child.kill()
            child.wait()
        receipt['failure'] = repr(exc)
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
    return 0 if receipt['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
