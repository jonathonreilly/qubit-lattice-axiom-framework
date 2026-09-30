#!/usr/bin/env python3
"""One foreground process group, deadline/sentinel/resource guard, full receipt.

This is delivery tooling, not a scientific helper. CPU soft/hard limits are
inherited per process; group CPU/RSS are also polled every 0.5 seconds. RSS is
an observed aggregate threshold, not a claim that macOS enforces RLIMIT_AS.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--cpu', type=int, required=True)
parser.add_argument('--wall', type=int, required=True)
parser.add_argument('--rss-mib', type=int, required=True)
parser.add_argument('--prefix', type=Path, required=True)
parser.add_argument('command', nargs=argparse.REMAINDER)
args = parser.parse_args()
command = args.command[1:] if args.command[:1] == ['--'] else args.command
if not command:
    parser.error('a command is required')
repo = Path(__file__).resolve().parents[4]
runtime = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline = json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
stop = runtime/'STOP_REQUESTED.json'
if stop.exists() or time.time() >= deadline:
    raise SystemExit('Campaign stop/deadline is active; no child launched.')
prefix = args.prefix.resolve()
prefix.parent.mkdir(parents=True, exist_ok=True)
paths = [Path(str(prefix)+suffix) for suffix in ('.stdout.txt', '.stderr.txt', '.execution.json')]
if any(p.exists() for p in paths):
    raise SystemExit('Refusing to overwrite an execution artifact.')
env = dict(os.environ)
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'):
    env[key] = '1'
env['PYTHONDONTWRITEBYTECODE'] = '1'

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (args.cpu, args.cpu+1))

def seconds(value):
    days = 0
    if '-' in value:
        day, value = value.split('-', 1)
        days = int(day)
    parts = list(map(float, value.split(':')))
    result = 0
    for part in parts:
        result = 60*result+part
    return 86400*days+result

started = datetime.now(timezone.utc).isoformat()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
t0 = time.monotonic()
peak_rss = 0
peak_cpu = 0.0
reason = None
with paths[0].open('wb') as stdout, paths[1].open('wb') as stderr:
    proc = subprocess.Popen(command, cwd=repo, env=env, stdout=stdout, stderr=stderr,
                            start_new_session=True, preexec_fn=limits)
    try:
        while proc.poll() is None:
            sample = subprocess.run(['/bin/ps', '-axo', 'pgid=,rss=,time='],
                                    capture_output=True, text=True, check=True)
            rows = [line.split() for line in sample.stdout.splitlines()]
            own = [row for row in rows if len(row) == 3 and int(row[0]) == proc.pid]
            rss = 1024*sum(int(row[1]) for row in own)
            cpu = sum(seconds(row[2]) for row in own)
            peak_rss = max(peak_rss, rss)
            peak_cpu = max(peak_cpu, cpu)
            if stop.exists():
                reason = 'STOP_REQUESTED'
            elif time.time() >= deadline:
                reason = 'campaign_deadline'
            elif time.monotonic()-t0 > args.wall:
                reason = 'wall_limit'
            elif cpu > args.cpu:
                reason = 'aggregate_cpu_limit'
            elif rss > args.rss_mib*1024*1024:
                reason = 'aggregate_rss_polling_limit'
            if reason:
                os.killpg(proc.pid, signal.SIGKILL)
                break
            time.sleep(0.5)
        code = proc.wait()
    except BaseException:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait()
        raise
elapsed = time.monotonic()-t0
after = resource.getrusage(resource.RUSAGE_CHILDREN)
# The OS reaped-child value includes ps sampling overhead and descendant usage
# propagated when the cache worker waits for its runner. Record this conservatively.
cpu_total = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
os_peak = after.ru_maxrss if sys.platform == 'darwin' else after.ru_maxrss*1024
record = {
    'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(),
    'repo': str(repo), 'command': command, 'exit_code': code,
    'termination_reason': reason, 'wall_seconds': elapsed,
    'reaped_children_cpu_seconds_including_monitor': cpu_total,
    'peak_group_cpu_seconds_sampled': peak_cpu,
    'peak_group_rss_bytes_sampled': peak_rss,
    'os_reaped_child_peak_rss_bytes': os_peak,
    'limits': {'cpu_seconds': args.cpu, 'wall_seconds': args.wall,
               'rss_mib_polling_threshold': args.rss_mib, 'poll_seconds': 0.5},
    'deadline_epoch': deadline, 'stop_absent_at_start': True,
    'threads': {key: env[key] for key in env if key.endswith('NUM_THREADS')
                or key == 'VECLIB_MAXIMUM_THREADS'},
    'capture_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths[:2]},
}
paths[2].write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
raise SystemExit(code if code >= 0 else 128-code)
