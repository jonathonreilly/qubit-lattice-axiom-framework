"""Administrative shutdown receipt only; never launches or resumes research."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

RUNTIME = Path(__file__).resolve().parent
WORKTREE = Path('/Users/jonBridger/.codex/worktrees/observations-backward-24h-20261014/New Axioms Lets Go')
DEADLINE = datetime.datetime.fromisoformat('2026-10-15T21:48:44+00:00')
OWNER = 'direct-author-observations-backward'
HOLDER = '01a130f9-fd7f-7d31-9f8f-ac05cdf2c617'
now = datetime.datetime.now(datetime.timezone.utc)
if now < DEADLINE:
    raise SystemExit('Refusing premature deadline closure.')
saved_deadline = json.loads((RUNTIME / 'DEADLINE.json').read_text())
assert datetime.datetime.fromisoformat(saved_deadline['deadline_at']) == DEADLINE

raw = subprocess.check_output(['ps', '-axo', 'pid=,ppid=,etime=,command='], text=True)
processes = {}
for line in raw.splitlines():
    fields = line.strip().split(None, 3)
    if len(fields) == 4:
        pid, parent, elapsed, command = fields
        processes[int(pid)] = {'pid': int(pid), 'ppid': int(parent), 'elapsed': elapsed, 'command': command}
excluded = set()
pid = os.getpid()
while pid in processes and pid not in excluded:
    excluded.add(pid)
    pid = processes[pid]['ppid']
campaigns = [
    'observations-backward-24h-20261014',
    'observations-to-toe-24h-20261012',
    'toe-observation-inversion-24h-20261012',
    'revised-scalar-derivation-24h-20261013',
]
matches = [row for pid, row in processes.items()
           if pid not in excluded and any(name in row['command'] for name in campaigns)]
previous = []
for name in campaigns[1:]:
    path = RUNTIME.parent / name / 'STATUS.json'
    data = path.read_bytes()
    state = json.loads(data)
    previous.append({'campaign': name, 'status_sha256': hashlib.sha256(data).hexdigest(),
                     'status': state.get('status'), 'phase': state.get('phase'),
                     'worker_pid': state.get('worker_pid'), 'supervisor_pid': state.get('supervisor_pid'),
                     'completed_at': state.get('completed_at')})
receipt = {
    'campaign_id': campaigns[0], 'fixed_deadline': DEADLINE.isoformat(),
    'checked_at': now.isoformat(), 'process_check': 'Fresh ps command inventory, excluding this administrative process and its ancestor chain.',
    'excluded_administrative_ancestor_pids': sorted(excluded), 'matching_processes': matches,
    'previous_campaigns': previous, 'scope': 'Owned-process and saved-status verification only; no scientific calculations or raw observation access.',
}
if matches:
    receipt['status'] = 'attention_required_matching_processes'
    (RUNTIME / 'DEADLINE_SHUTDOWN_ATTENTION_v1.json').write_text(json.dumps(receipt, indent=2) + '\n')
    raise SystemExit('Campaign-marked process remains; inspect ownership before any signal.')
assert all(x['worker_pid'] is None and x['supervisor_pid'] is None for x in previous)
lock_command = ['/usr/local/bin/python3', 'scripts/automation_lock.py']
before = json.loads(subprocess.check_output(lock_command + ['status'], cwd=WORKTREE, text=True))
assert before['status'] == 'held'
assert before['lock']['owner'] == OWNER and before['lock']['holder_id'] == HOLDER
released = subprocess.run(lock_command + ['release', '--owner', OWNER, '--holder-id', HOLDER],
                          cwd=WORKTREE, text=True, capture_output=True)
after = json.loads(subprocess.check_output(lock_command + ['status'], cwd=WORKTREE, text=True))
receipt.update(lock_before=before, lock_release={'returncode': released.returncode,
               'stdout': released.stdout, 'stderr': released.stderr}, lock_after=after)
assert released.returncode == 0
remaining = after.get('lock') or {}
assert not (remaining.get('owner') == OWNER and remaining.get('holder_id') == HOLDER)
receipt.update(status='no_owned_research_process_found_matching_lock_released',
               closure_recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               automation='Retirement must be performed by the app tool and recorded separately.')
(RUNTIME / 'DEADLINE_SHUTDOWN_v1.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
