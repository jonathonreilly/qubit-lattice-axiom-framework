"""Seal this new correspondence packet only; never execute an original writer."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / 'PUBLICATION_COMPARISON_SEAL.json'
assert not TARGET.exists()
members = []
for path in sorted(HERE.rglob('*')):
    if path.is_file():
        assert not path.is_symlink()
        body = path.read_bytes()
        members.append({'path': path.relative_to(HERE).as_posix(),
                        'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)})
report = next(x for x in members if x['path'] == 'PUBLICATION_COMPARISON.md')
seal = {'sealed_utc': datetime.now(timezone.utc).isoformat(),
        'author': '/root/rotor_upper_tail_check',
        'phase': 'candidate40 final released-source publication correspondence',
        'independence_scope': 'Newly exposed correspondence reviewer; no new blind or primitive reconstruction.',
        'report': report['path'], 'report_sha256': report['sha256'],
        'members': members,
        'original_author_and_prior_PRE_POST_preserved': True,
        'publication_modified': False, 'scientific_runtime_executed_or_imported': False,
        'delegation': False, 'audit_verdict': None,
        'required_publication_repair_identified': None,
        'immutable_semantics': 'Exclusive-create seal and content hashes; original files untouched.',
        'replay': 'python3 -B verify_correspondence.py --seal'}
with TARGET.open('x') as stream:
    json.dump(seal, stream, indent=2); stream.write('\n')
print(json.dumps({'report_sha256': report['sha256'], 'seal_sha256': hashlib.sha256(TARGET.read_bytes()).hexdigest(),
                  'sealed_members': len(members)}, indent=2))
