#!/usr/bin/env python3
"""Run the actual serialized graph producer in a bounded managed session.

This is mechanical delivery evidence, not a science runner or review receipt.
No detached worker is created: this supervisor waits for and reaps its child.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
PACK = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
WALL_LIMIT = 1200.0
RSS_LIMIT = 500_000_000
THREAD_NAMES = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS')


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def guard():
    if (RUNTIME / 'STOP_REQUESTED.json').exists():
        return 'STOP_REQUESTED'
    deadline = json.loads((RUNTIME / 'DEADLINE.json').read_text())
    if time.time() >= float(deadline['deadline_epoch']):
        return 'campaign_deadline'
    return None


def main():
    reason = guard()
    if reason:
        raise SystemExit('Refusing to start: ' + reason)
    pre = json.loads((PACK / 'GRAPH_PREBUILD.json').read_text())
    for name, digest in pre['protected_files'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    env = dict(os.environ)
    env.update({name: '1' for name in THREAD_NAMES})
    env['PYTHONUNBUFFERED'] = '1'
    command = [sys.executable, 'docs/audit/scripts/run_citation_graph_build.py']
    started_at = utc()
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    peak_sampled = 0
    samples = 0
    last_heartbeat = start
    with (PACK / 'GRAPH_BUILD.log').open('w') as log:
        child = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log,
                                 stderr=subprocess.STDOUT, start_new_session=True)
        print(f'graph producer pid={child.pid} started={started_at}', flush=True)
        try:
            while child.poll() is None:
                elapsed = time.monotonic() - start
                reason = guard()
                if reason is None and elapsed >= WALL_LIMIT:
                    reason = 'wall_limit'
                # Launcher execs the graph builder, keeping the same PID.
                rss_text = subprocess.run(['ps', '-o', 'rss=', '-p', str(child.pid)],
                                          capture_output=True, text=True).stdout.strip()
                if rss_text:
                    rss = int(rss_text) * 1024
                    samples += 1
                    peak_sampled = max(peak_sampled, rss)
                    if rss > RSS_LIMIT:
                        reason = 'rss_limit'
                if reason:
                    os.killpg(child.pid, signal.SIGTERM)
                    try:
                        child.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        os.killpg(child.pid, signal.SIGKILL)
                    break
                if time.monotonic() - last_heartbeat >= 30:
                    print(f'graph active elapsed={elapsed:.1f}s sampled_peak_rss={peak_sampled}', flush=True)
                    last_heartbeat = time.monotonic()
                time.sleep(2)
        except BaseException:
            if child.poll() is None:
                os.killpg(child.pid, signal.SIGKILL)
            child.wait()
            raise
        returncode = child.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    metrics = {
        'scope': 'actual_serialized_graph_build_only_no_audit_or_full_pipeline',
        'command': command, 'cwd': str(ROOT), 'pid': child.pid,
        'started_at': started_at, 'finished_at': utc(),
        'wall_seconds': time.monotonic() - start, 'wall_limit_seconds': WALL_LIMIT,
        'rss_limit_bytes': RSS_LIMIT, 'exit_code': returncode,
        'termination_reason': reason,
        'sampled_producer_peak_rss_bytes': peak_sampled, 'rss_sample_count': samples,
        'children_user_cpu_seconds': after.ru_utime - before.ru_utime,
        'children_system_cpu_seconds': after.ru_stime - before.ru_stime,
        'children_peak_rss_bytes': after.ru_maxrss if sys.platform == 'darwin' else after.ru_maxrss * 1024,
        'resource_note': 'RUSAGE_CHILDREN includes short ps probes; sampled RSS is producer PID only; launcher execs producer in the same PID.',
        'thread_environment': {name: env[name] for name in THREAD_NAMES},
        'deadline_file': str(RUNTIME / 'DEADLINE.json'),
        'stop_file': str(RUNTIME / 'STOP_REQUESTED.json'),
        'deadline_or_stop_at_finish': guard(),
        'base_main': pre['base_main'], 'head': pre['head'],
    }
    metrics['protected_files_unchanged'] = all(
        hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == s
        for p, s in pre['protected_files'].items())
    metrics['log_sha256'] = hashlib.sha256((PACK / 'GRAPH_BUILD.log').read_bytes()).hexdigest()
    (PACK / 'GRAPH_BUILD_METRICS.json').write_text(json.dumps(metrics, indent=2, sort_keys=True) + '\n')
    print(json.dumps(metrics, indent=2, sort_keys=True), flush=True)
    return returncode if returncode >= 0 else 128 - returncode


if __name__ == '__main__':
    raise SystemExit(main())
