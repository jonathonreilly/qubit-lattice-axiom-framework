#!/usr/bin/env python3
"""Seal the completed component inventory; stdout/stderr are redirected into seal_execution."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def run():
    seal = ROOT / 'FINAL_FREEZE.json'
    if seal.exists():
        raise ValueError('existing freeze is immutable')
    records = []
    for p in sorted((ROOT / 'runs').glob('*/RECEIPT.json')):
        r = json.loads(p.read_text())
        source = p.parent / 'executed_source.py'
        assert hashlib.sha256(source.read_bytes()).hexdigest() == r['source_sha256_before']
        assert r['source_unchanged'] and r['source_sha256_before'] == r['source_sha256_after']
        for stream in ('stdout', 'stderr'):
            q = ROOT / r[stream]['path']
            b = q.read_bytes()
            assert len(b) == r[stream]['bytes'] and hashlib.sha256(b).hexdigest() == r[stream]['sha256']
        records.append({'receipt': identity(p), 'exit_code': r['exit_code'],
                        'source_sha256': r['source_sha256_before']})
    assert all(r['exit_code'] == 0 for r in records), 'inspect any actual nonzero source attempt before sealing'
    assert (ROOT / 'history/BUILD01_RECORDER_FAILURE.json').is_file()
    assert (ROOT / 'history/INITIAL_LOOKUP_FAILURE.json').is_file()
    check = json.loads((ROOT / 'runs/check02/stdout.txt').read_text())
    reproduction = json.loads((ROOT / 'runs/reproduction01/stdout.txt').read_text())
    history = json.loads((ROOT / 'runs/history01/stdout.txt').read_text())
    assert check['note_sha256'] == reproduction['note']['sha256']
    assert check['primary_runner_sha256'] == reproduction['helper']['sha256']
    assert history['files'] == check['payload_files']
    print(json.dumps({'completed_before_seal_write': True, 'recorded_source_attempts': len(records),
                      'recorded_child_nonzero_exits': 0, 'pre_child_or_lookup_failures_preserved': 2,
                      'mathematical_predicates': 0, 'primary_helper_executed': False,
                      'scientific_programs_replayed': 0}, indent=2))
    sys.stdout.flush()
    sys.stderr.flush()
    members = [identity(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and p != seal]
    assert all(not (ROOT / r['path']).is_symlink() for r in members)
    result = {'schema': 'frozen-preparation-moment-components-v1',
              'sealed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'root': str(ROOT), 'members': members, 'complete_file_count': len(members) + 1,
              'payload_file_count': check['payload_files'], 'source_records': check['archive_records'],
              'unique_archive_objects': check['unique_objects'], 'three_source_groups': check['source_group_counts'],
              'inner_aliases': check['inner_alias_counts'], 'recorded_actual_runs': records,
              'current_note_sha256': check['note_sha256'], 'current_primary_sha256': check['primary_runner_sha256'],
              'prior_payload_complete_reconstruction': identity(ROOT / 'history/wrapper_v1/PAYLOAD_RECONSTRUCTION.json'),
              'science_runs': 0, 'mathematical_predicates': 0, 'primary_executions': 0,
              'canonical_git_pr_checkpoint_prompt_axiom_changes': [],
              'integration_authorized': False, 'combined_component_root_acceptance': None,
              'seal_operation': {'kind': 'direct source-only finalizer with full redirected actual streams',
                 'source': identity(Path(__file__)),
                 'stdout': identity(ROOT / 'seal_execution/stdout.txt'),
                 'stderr_at_seal': identity(ROOT / 'seal_execution/stderr.txt'),
                 'outer_exit_code_not_self_asserted': True,
                 'note': 'All logging occurs before the final manifest write. No invented post-exit receipt or self-hash.'}}
    seal.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    run()
