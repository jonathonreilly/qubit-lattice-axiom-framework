#!/usr/bin/env python3
"""One-time POST freeze, referencing and preserving the separate PRE seal."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
target = here / 'POST_SEAL.json'
if target.exists():
    raise RuntimeError('POST already sealed; preserve it')
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
read = lambda name: json.loads((here / name).read_text())
pre_hash = sha(here / 'PRE_SEAL.json')
assert pre_hash == '65ef5734192d3ca88511a992fad2b1788582ad8acf632c2b2d33e866d121cff6'
pre = read('PRE_SEAL.json')
for member in pre['members']:
    assert sha(here / member['path']) == member['sha256']
old_paths = {member['path'] for member in pre['members']} | {'PRE_SEAL.json'}
pins = read('POST_SOURCE_PINS.json')
for source in pins['released_author_files']:
    assert sha(here / source['frozen_path']) == sha(Path(source['origin'])) == source['sha256']
freeze_stdout = [json.loads(line) for line in (here / 'post_freeze_sources.stdout.txt').read_text().splitlines()]
assert freeze_stdout == pins['released_author_files']
assert (here / 'post_freeze_sources.stderr.txt').read_bytes() == b''
execution = read('POST_CHECK_EXECUTION.json')
assert execution['exit_code'] == 0
for name, key in [('run_post_checks.py', 'runner_sha256'),
                  ('post_compare_evidence.py', 'script_sha256'),
                  ('POST_SOURCE_PINS.json', 'POST_SOURCE_PINS_sha256'),
                  ('post_compare_evidence.stdout.txt', 'stdout_sha256'),
                  ('post_compare_evidence.stderr.txt', 'stderr_sha256')]:
    assert sha(here / name) == execution[key]
result = read('POST_CHECK_RESULTS.json')
assert result['script_sha256'] == execution['script_sha256']
assert result['POST_SOURCE_PINS_sha256'] == execution['POST_SOURCE_PINS_sha256']
output = [json.loads(line) for line in (here / 'post_compare_evidence.stdout.txt').read_text().splitlines()]
assert output[:-1] == result['checks']
assert output[-1] == {'completed': True, 'check_count': result['check_count']}
assert result['all_checks_satisfied'] and result['check_count'] == 24
assert (here / 'post_compare_evidence.stderr.txt').read_bytes() == b''
members = []
for path in sorted(here.rglob('*')):
    relative = str(path.relative_to(here))
    if path.is_file() and relative not in old_paths:
        assert not path.is_symlink()
        members.append({'path': relative, 'bytes': path.stat().st_size, 'sha256': sha(path)})
seal = {'phase': 'released-source POST comparison',
        'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'preserved_PRE_seal_sha256': pre_hash,
        'preserved_PRE_member_count': len(pre['members']), 'all_PRE_members_unchanged': True,
        'author_proof_sha256': '6710b11cede13fc0cb8c7d9e83fac816d590acef8401bd1e98f432c3252840ce',
        'author_seal_sha256': '943b8ae9bf740cd2560bd6b77daf91189e8efee33fd857449378fce62ad2d1a2',
        'scope': 'Proof/evidence correspondence only; author controls not executed or imported; no independent POST propagation claim, publication, audit, axiom change or delegation.',
        'member_count': len(members), 'members': members,
        'preservation': 'One-time content-hash ledger; new POST members and seal are set read-only; PRE remains separately sealed.'}
target.write_text(json.dumps(seal, indent=2) + '\n')
for member in members:
    path = here / member['path']
    assert sha(path) == member['sha256']
    path.chmod(0o444)
target.chmod(0o444)
print(json.dumps({'POST_seal': str(target), 'POST_seal_sha256': sha(target),
                  'POST_md_sha256': sha(here / 'POST.md'), 'new_POST_members': len(members),
                  'preserved_PRE_members': len(pre['members']),
                  'all_members_reverified': True}, sort_keys=True))
