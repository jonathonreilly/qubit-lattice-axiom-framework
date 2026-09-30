#!/usr/bin/env python3
"""Supervised author execution envelope; does not confer review standing."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import time

AUDIT_TIMEOUT_SEC = 2500


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True)
    ap.add_argument('--cpu', type=int, required=True)
    ap.add_argument('--wall', type=int, required=True)
    ap.add_argument('--rss', type=int, required=True, help='MiB, sampled process-group sum')
    ap.add_argument('command', nargs=argparse.REMAINDER)
    a = ap.parse_args()
    command = a.command[1:] if a.command[:1] == ['--'] else a.command
    pack = Path(__file__).resolve().parent
    repo = pack.parents[3]
    campaign = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
    deadline = json.loads((campaign/'DEADLINE.json').read_text())['deadline_epoch']
    stops = [campaign/'STOP_REQUESTED', campaign/'STOP_REQUESTED.json']
    assert time.time() < deadline and not any(p.exists() for p in stops)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']:
        env[key] = '1'
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (a.cpu, a.cpu))
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    peak = 0
    reason = None
    with (pack/(a.label+'.stdout')).open('x') as so, (pack/(a.label+'.stderr')).open('x') as se:
        p = subprocess.Popen(command, cwd=repo, env=env, stdout=so, stderr=se,
                             start_new_session=True, preexec_fn=limit)
        running = pack/(a.label+'.RUNNING.json')
        running.write_text(json.dumps({'pid':p.pid,'command':command,'cpu_limit':a.cpu,
                          'wall_limit':a.wall,'group_RSS_MiB_limit':a.rss})+'\n')
        while p.poll() is None:
            ps = subprocess.check_output(['ps','-axo','pgid=,rss='], text=True)
            rss = sum(int(v[1]) for line in ps.splitlines()
                      if len(v:=line.split())==2 and int(v[0])==p.pid)/1024
            peak = max(peak, rss)
            if time.time() >= deadline: reason = 'campaign deadline'
            elif any(x.exists() for x in stops): reason = 'STOP_REQUESTED'
            elif time.monotonic()-start >= a.wall: reason = 'wall limit'
            elif rss > a.rss: reason = 'sampled group RSS limit'
            if reason:
                os.killpg(p.pid,signal.SIGTERM)
                try: p.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(p.pid,signal.SIGKILL)
                    p.wait()
                break
            time.sleep(0.2 if a.wall <= 90 else 2)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    result = {'command':command,'exit_code':p.returncode,'stop_reason':reason,
              'wall_seconds':time.monotonic()-start,'child_cpu_seconds':cpu,
              'sampled_peak_group_RSS_MiB':peak,'price_cpu_seconds':a.cpu,
              'price_wall_seconds':a.wall,'price_RSS_MiB':a.rss,
              'cpu_price_exceeded_at_return':cpu>a.cpu,
              'scope':'author execution evidence; not a science verdict'}
    for suffix in ['stdout','stderr']:
        result[suffix+'_sha256'] = hashlib.sha256((pack/(a.label+'.'+suffix)).read_bytes()).hexdigest()
    (pack/(a.label+'_EXECUTION.json')).write_text(json.dumps(result,indent=2)+'\n')
    running.unlink()
    print(json.dumps(result))
    ok = p.returncode == 0 and reason is None and cpu <= a.cpu
    print('TOTAL: PASS=%d FAIL=%d' % (int(ok),int(not ok)))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
