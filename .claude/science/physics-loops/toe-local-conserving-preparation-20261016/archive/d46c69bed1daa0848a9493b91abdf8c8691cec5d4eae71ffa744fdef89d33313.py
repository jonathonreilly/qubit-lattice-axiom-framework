"""Additive inventory closure; never changes any initially frozen member."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_exposed_check')
sha = lambda b: hashlib.sha256(b).hexdigest()
initial_raw = (OUT / 'FREEZE.json').read_bytes()
assert sha(initial_raw) == '775ad07fa82efe4656fdedc3f6ff87e71b12dcd26f30781d109f9676968180b8'
initial = json.loads(initial_raw)
for row in initial['members']:
    raw = (OUT / row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
assert sha((OUT / 'sources' / 'FREEZE.json').read_bytes()) == '1ea6d4edcfff8d4c098f1318ce046da667f831749a16880b53ccb926f26fcb13'
assert not (OUT / 'FINAL_FREEZE.json').exists()
assert not (OUT / 'FINAL_FREEZE.sha256').exists()
members = []
excluded = {'FINAL_FREEZE.json', 'FINAL_FREEZE.sha256'}
for p in sorted(OUT.rglob('*')):
    relative = str(p.relative_to(OUT))
    if p.is_file() and relative not in excluded:
        raw = p.read_bytes()
        members.append({'path': relative, 'bytes': len(raw), 'sha256': sha(raw)})
freeze = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'final_sealed_source_exposed_analytical_review',
    'initial_freeze_sha256': sha(initial_raw),
    'all_initial_members_unchanged': True,
    'scientific_executions': 0,
    'author_result_read': False,
    'metadata_correction': 'See SEAL_CORRECTION.md; source freeze directly included here.',
    'members': members,
}
raw = (json.dumps(freeze, indent=2) + '\n').encode()
(OUT / 'FINAL_FREEZE.json').write_bytes(raw)
(OUT / 'FINAL_FREEZE.sha256').write_text(sha(raw) + '  FINAL_FREEZE.json\n')
print(json.dumps({'members': len(members), 'final_freeze_bytes': len(raw), 'final_freeze_sha256': sha(raw), 'review_sha256': sha((OUT/'REVIEW.md').read_bytes()), 'utc': freeze['utc']}, indent=2))
