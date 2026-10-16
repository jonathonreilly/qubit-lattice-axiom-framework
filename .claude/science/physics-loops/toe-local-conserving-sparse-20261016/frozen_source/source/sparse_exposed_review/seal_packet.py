"""Seal only this exposed-review packet after fresh metadata verification.

This is bookkeeping, not a scientific execution or an approval operation.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_exposed_check')
sha = lambda b: hashlib.sha256(b).hexdigest()
assert Path(__file__).resolve() == OUT/'seal_packet.py'
assert not (OUT/'FREEZE.json').exists()
assert not (OUT/'FREEZE.sha256').exists()
assert not (OUT/'SEAL_VERIFICATION.json').exists()
manifest = json.loads((OUT/'SOURCE_MANIFEST.json').read_bytes())
for row in manifest['source_records']:
    original = Path(row['original_path']).read_bytes()
    captured = (OUT/row['capture']).read_bytes()
    assert original == captured
    assert len(captured) == row['bytes'] and sha(captured) == row['sha256']
for row in manifest['prior_parent_review_unchanged']:
    raw = Path(row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
author = OUT/'author_source'
author_freeze = json.loads((author/'FREEZE.json').read_bytes())
for row in author_freeze['members']:
    raw = (author/row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
for name, launcher in [('exact_sparse_check','run_exact_check.py'), ('exact_sparse_check_retry','run_exact_check_retry.py')]:
    run = author/'runs'/name
    receipt = json.loads((run/'EXECUTION.json').read_bytes())
    source = (run/'SOURCE_AT_LAUNCH.py').read_bytes()
    launcher_raw = (run/'LAUNCHER_AT_LAUNCH.py').read_bytes()
    assert source == (author/'exact_sparse_check.py').read_bytes()
    assert launcher_raw == (author/launcher).read_bytes()
    assert sha(source) == receipt['source_sha256'] == receipt['source_sha256_after']
    assert sha(launcher_raw) == receipt['launcher_sha256']
    for stream in ['stdout','stderr']:
        assert sha((run/(stream+'.txt')).read_bytes()) == receipt[stream+'_sha256']
run = OUT/'runs/source_capture'
receipt_raw = (run/'EXECUTION.json').read_bytes()
receipt = json.loads(receipt_raw)
assert receipt['exit_code'] == 0 and receipt['scientific_execution'] is False
assert (run/'executed_source.py').read_bytes() == (OUT/'capture_sources.py').read_bytes()
assert (run/'launcher_source.py').read_bytes() == (OUT/'run_metadata_capture.py').read_bytes()
assert sha((run/'executed_source.py').read_bytes()) == receipt['source_sha256']
assert sha((run/'launcher_source.py').read_bytes()) == receipt['launcher_sha256']
for stream in ['stdout','stderr']:
    raw = (run/stream).read_bytes()
    assert len(raw) == receipt[stream+'_bytes'] and sha(raw) == receipt[stream+'_sha256']
assert json.loads((run/'stdout').read_bytes())['new_reviewer_scientific_executions'] == 0
assert (run/'stderr').read_bytes() == b''
review = (OUT/'REVIEW.md').read_bytes()
coverage = (OUT/'SOURCE_COVERAGE.md').read_bytes()
review.decode('utf-8'); coverage.decode('utf-8')
assert len(review) > 10000 and len(coverage) > 1000
stamp = datetime.now(timezone.utc).isoformat()
verification = {
    'utc': stamp,
    'kind': 'actual_metadata_verification_before_seal',
    'argv': sys.argv,
    'scientific_execution': False,
    'author_original_capture_identities_verified': len(manifest['source_records']),
    'author_freeze_members_verified': len(author_freeze['members']),
    'author_failure_and_success_receipt_source_launcher_streams_verified': True,
    'prior_parent_review_and_freeze_unchanged': True,
    'metadata_capture_receipt_sha256': sha(receipt_raw),
    'metadata_capture_source_launcher_and_full_streams_verified': True,
    'review_bytes': len(review),
    'review_sha256': sha(review),
    'source_coverage_sha256': sha(coverage),
    'scientific_programs_executed_by_reviewer': 0,
    'scope': 'Metadata checks and local sealing only; no scientific replay, approval, canonical or Git operation.'
}
(OUT/'SEAL_VERIFICATION.json').write_text(json.dumps(verification, indent=2)+'\n')
excluded = {'FREEZE.json', 'FREEZE.sha256'}
members = []
for path in sorted(OUT.rglob('*')):
    assert not path.is_symlink()
    if path.is_file():
        rel = path.relative_to(OUT).as_posix()
        if rel not in excluded:
            raw = path.read_bytes()
            members.append({'path': rel, 'bytes': len(raw), 'sha256': sha(raw)})
assert any(row['path'] == 'author_source/FREEZE.json' for row in members)
freeze = {
    'kind': 'final_source_exposed_review_freeze',
    'frozen_at_utc': stamp,
    'disposition': 'qualified_support_with_scope_and_evidence_limits',
    'review_source_exposed': True,
    'retained_audit': False,
    'scientific_replay': False,
    'candidate_derivation_sha256': '6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b',
    'candidate_freeze_sha256': '1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9',
    'exact_root_paths_excluded_from_members': sorted(excluded),
    'members': members
}
freeze_raw = (json.dumps(freeze, indent=2)+'\n').encode()
(OUT/'FREEZE.json').write_bytes(freeze_raw)
(OUT/'FREEZE.sha256').write_text(sha(freeze_raw)+'  FREEZE.json\n')
for row in members:
    raw = (OUT/row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
actual_paths = {p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file()}
assert actual_paths == {row['path'] for row in members} | excluded
print(json.dumps({'frozen_at_utc': stamp, 'member_count': len(members), 'review_bytes': len(review), 'review_sha256': sha(review), 'freeze_sha256': sha(freeze_raw), 'all_members_verified': True, 'exact_file_closure_verified': True, 'scientific_execution': False}, indent=2))
