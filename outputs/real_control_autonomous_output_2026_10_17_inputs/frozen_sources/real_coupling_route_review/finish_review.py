#!/usr/bin/env python3
"""Assemble one complete report and freeze; bookkeeping, no scientific execution."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

R = Path(__file__).resolve().parent

def identity(p):
    b = p.read_bytes()
    return {'bytes': len(b), 'sha256': sha256(b).hexdigest()}

def save_bytes(p, b):
    with p.open('xb') as f:
        f.write(b)
        f.flush()
        os.fsync(f.fileno())

af = json.loads((R / 'ANALYTIC_FREEZE.json').read_text())
for e in af['files']:
    assert identity(R / e['path']) == {k: e[k] for k in ('bytes', 'sha256')}

parts = ['REVIEW_HEADER.md', 'PRECHECK_ANALYSIS.md', 'REVIEW_POSTCHECK.md']
save_bytes(R / 'REVIEW.md', b'\n'.join((R / p).read_bytes() for p in parts))
# The copied author and input FREEZE files must also be included; exclude only our final file.
files = [{'path': str(p.relative_to(R)), **identity(p)}
         for p in sorted(R.rglob('*')) if p.is_file() and p != R / 'FREEZE.json']
freeze = {
    'frozen_utc': datetime.now(timezone.utc).isoformat(),
    'primary': 'REVIEW.md', 'primary_identity': identity(R / 'REVIEW.md'),
    'disposition': 'Supported conditional narrow worked failure; no material mathematical correction found; not publication or retained-audit approval',
    'author_primary_sha256': 'c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018',
    'author_freeze_sha256': '16fa2cbf13386826cd6939cc412f66c9224a89eaadd133b2163c5b3130e5829b',
    'analytic_result_frozen_before_author_checker_output_exposure': True,
    'analytic_freeze_identity': identity(R / 'ANALYTIC_FREEZE.json'),
    'review_scientific_executions': 0,
    'author_checker_replayed_or_imported': False,
    'full_author_packet_copied': True,
    'model_or_effort_override': False, 'subdelegation': False,
    'source_prompt_axiom_audit_git_worktree_checkpoint_changes': False,
    'editable_prompt_files_changed': [],
    'independence_limit': 'Same-model substantial prior source authorship/exposure; selective new derivation, no blind full-dependency review',
    'files': files, 'self_in_inventory': False,
}
save_bytes(R / 'FREEZE.json', (json.dumps(freeze, indent=2, sort_keys=True)+'\n').encode())
fd = os.open(R, os.O_RDONLY)
try:
    os.fsync(fd)
finally:
    os.close(fd)
print(json.dumps({'frozen_entries': len(files), 'report': identity(R/'REVIEW.md'),
                  'freeze': identity(R/'FREEZE.json')}, indent=2))
