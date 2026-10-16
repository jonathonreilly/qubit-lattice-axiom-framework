"""Validate the review's metadata evidence and seal the local packet only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_exposed_check')
sha = lambda b: hashlib.sha256(b).hexdigest()
if (OUT / 'FREEZE.json').exists() or (OUT / 'FREEZE.sha256').exists():
    raise RuntimeError('Refusing to replace an existing freeze')

manifest = json.loads((OUT / 'SOURCE_MANIFEST.json').read_text())
for row in manifest['sources']:
    original = Path(row['original_path']).read_bytes()
    captured = (OUT / row['captured_path']).read_bytes()
    assert sha(original) == sha(captured) == row['sha256']
    assert len(original) == len(captured) == row['bytes']

capture_run = OUT / 'runs' / 'source_capture'
capture = json.loads((capture_run / 'EXECUTION.json').read_text())
assert capture['exit_code'] == 0 and capture['scientific_execution'] is False
assert sha((capture_run / 'executed_source.py').read_bytes()) == capture['source_sha256']
assert (capture_run / 'executed_source.py').read_bytes() == (OUT / 'capture_sources.py').read_bytes()
assert sha((capture_run / 'launcher_source.py').read_bytes()) == capture['launcher_sha256']
assert (capture_run / 'launcher_source.py').read_bytes() == (OUT / 'run_metadata_capture.py').read_bytes()

render_run = OUT / 'runs' / 'page16_render'
render = json.loads((render_run / 'EXECUTION.json').read_text())
assert render['exit_code'] == 0 and render['scientific_execution'] is False
assert sha((render_run / 'executed_source.py').read_bytes()) == render['source_sha256']
assert (render_run / 'executed_source.py').read_bytes() == (OUT / 'render_page16.py').read_bytes()
for run, receipt in [(capture_run, capture), (render_run, render)]:
    for stream in ['stdout', 'stderr']:
        raw = (run / stream).read_bytes()
        assert len(raw) == receipt[stream + '_bytes']
        assert sha(raw) == receipt[stream + '_sha256']

assert json.loads((capture_run / 'stdout').read_text()) == manifest
assert b'CoreGraphics PDF has logged an error' in (render_run / 'stderr').read_bytes()
assert (OUT / 'PRIMARY_PAGE16.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
verification = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Metadata integrity only, not a scientific execution or retained audit.',
    'authorized_source_identities_rechecked_at_seal': True,
    'source_at_launch_and_launcher_captures_match': True,
    'full_stream_hashes_match': True,
    'metadata_run_exit_codes': {'source_capture': capture['exit_code'], 'page16_render': render['exit_code']},
    'render_warning_retained': True,
    'scientific_executions': 0,
    'separate_author_exposure': False,
    'root_acceptance': 'pending',
    'canonical_or_editable_prompt_changes': False,
}
(OUT / 'SEAL_VERIFICATION.json').write_text(json.dumps(verification, indent=2) + '\n')
members = []
for path in sorted(OUT.rglob('*')):
    if path.is_file() and path.name not in ['FREEZE.json', 'FREEZE.sha256']:
        raw = path.read_bytes()
        members.append({'path': str(path.relative_to(OUT)), 'bytes': len(raw), 'sha256': sha(raw)})
freeze = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'packet': str(OUT),
    'status': 'sealed_source_exposed_analytical_review',
    'scientific_executions': 0,
    'author_result_read': False,
    'scope': 'Root proposal and saved primary only; same inherited model and effort; no retained audit or root acceptance claimed.',
    'members': members,
}
raw = (json.dumps(freeze, indent=2) + '\n').encode()
(OUT / 'FREEZE.json').write_bytes(raw)
(OUT / 'FREEZE.sha256').write_text(sha(raw) + '  FREEZE.json\n')
review = (OUT / 'REVIEW.md').read_bytes()
print(json.dumps({'member_count': len(members), 'review_bytes': len(review), 'review_sha256': sha(review), 'freeze_bytes': len(raw), 'freeze_sha256': sha(raw), 'utc': freeze['utc']}, indent=2))
