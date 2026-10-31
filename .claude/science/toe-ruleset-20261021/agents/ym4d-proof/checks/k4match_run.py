#!/usr/bin/env python3
"""Serial numeric child; actual combined RSS monitored below 800 MiB."""
from pathlib import Path
import datetime
import json
import os
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CAP = 800*1024**2


def gate():
    s = subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%',s).group(1))
    load = os.getloadavg()
    return dict(loads=load,free_percent=free,passed=max(load)<8 and free>=30)


def rss(pid):
    s = subprocess.run(['/bin/ps','-o','rss=','-p',str(pid)],capture_output=True,text=True)
    return int(s.stdout.strip() or '0')*1024


def main():
    report = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  cap_bytes=CAP,passed=False,guards=[])
    outpath = HERE/'k4match_results_guarded.json'
    errpath = HERE/'k4match_stderr_guarded.txt'
    receipt = HERE/'k4match_run.json'
    child = None
    try:
        assert not any(p.exists() for p in (outpath,errpath,receipt)), 'preserve existing evidence'
        assert os.getpriority(os.PRIO_PROCESS,0)>=10
        g = gate()
        report['guards'].append(g)
        assert g['passed'], g
        start = time.monotonic()
        peak = 0
        next_gate = start
        with outpath.open('x') as out,errpath.open('x') as err:
            env = dict(os.environ,K4MATCH_WATCHDOG='1',PYTHONDONTWRITEBYTECODE='1')
            child = subprocess.Popen([sys.executable,'-B',str(HERE/'k4match_exact.py')],
                                     stdout=out,stderr=err,env=env)
            while child.poll() is None:
                now = time.monotonic()
                peak = max(peak,rss(child.pid)+rss(os.getpid()))
                assert peak<CAP and now-start<90, 'RSS/time guard'
                if now>=next_gate:
                    g=gate()
                    report['guards'].append(g)
                    assert g['passed'], g
                    next_gate=now+1
                time.sleep(0.02)
        data=json.loads(outpath.read_text())
        peak=max(peak,max((g['peak_rss_bytes'] for g in data['guards']),default=0)
                 +resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        g=gate()
        report['guards'].append(g)
        report.update(exit_code=child.returncode,peak_combined_rss_bytes=peak,
                      elapsed_seconds=time.monotonic()-start,
                      passed=child.returncode==0 and data['passed'] and g['passed'] and peak<CAP)
    except BaseException as exc:
        if child is not None and child.poll() is None:
            child.kill()
            child.wait()
        report['failure']=repr(exc)
    with receipt.open('x') as f:
        json.dump(report,f,indent=2)
        f.write('\n')
    print(json.dumps(report,indent=2))
    return 0 if report['passed'] else 1


if __name__=='__main__':
    sys.exit(main())
