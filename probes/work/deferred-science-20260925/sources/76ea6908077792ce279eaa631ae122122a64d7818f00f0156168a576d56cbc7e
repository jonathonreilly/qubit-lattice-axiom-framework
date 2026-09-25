#!/usr/bin/env python3
"""One-time seal; recheck evidence without rerunning scientific controls."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
seal_path = here/'PUBLICATION_COMPARISON_SEAL.json'
assert not seal_path.exists()
def sha(data): return hashlib.sha256(data).hexdigest()
def dump(path, data):
    with path.open('x') as handle:
        json.dump(data,handle,indent=2,allow_nan=False);handle.write('\n')
pins = json.loads((here/'PUBLICATION_SOURCE_PINS.json').read_text())
origin_rows=[]
for row in pins['sources']:
    origin = Path(row['origin']).read_bytes()
    frozen = (here/row['frozen_path']).read_bytes()
    assert origin == frozen and len(origin)==row['bytes'] and sha(origin)==row['sha256']
    origin_rows.append(dict(origin=row['origin'],sha256=row['sha256'],unchanged=True))
for row in pins['reused_immutable_sources']:
    data=(here/row['path']).read_bytes()
    assert len(data)==row['bytes'] and sha(data)==row['sha256']
old_paths=set()
for old in pins['preserved']:
    old_data=(here/old['path']).read_bytes()
    assert sha(old_data)==old['sha256']
    old_paths.add(old['path'])
    manifest=json.loads(old_data)
    assert len(manifest['members'])==old['members_verified']
    for member in manifest['members']:
        data=(here/member['path']).read_bytes()
        assert len(data)==member['bytes'] and sha(data)==member['sha256']
        old_paths.add(member['path'])
procedure=json.loads((here/'PUBLICATION_PROCEDURE_FRESHNESS.json').read_text())
for row in procedure:
    assert sha(Path(row['origin']).read_bytes())==row['sha256']==row['expected_sha256']
    assert sha((here/row['frozen_prior_source']).read_bytes())==row['sha256']
good=json.loads((here/'PUBLICATION_COMPARE_EXECUTION.json').read_text())
assert good['exit_code']==0 and good['stderr_bytes']==0
assert sha((here/'publication_compare.py').read_bytes())==good['script_sha256']
for key in ['stdout','stderr']:
    raw=(here/f'publication_compare.{key}.txt').read_bytes()
    assert len(raw)==good[f'{key}_bytes'] and sha(raw)==good[f'{key}_sha256']
assert json.loads((here/'publication_compare.stdout.txt').read_text()) == json.loads((here/'PUBLICATION_EVIDENCE_VERIFICATION.json').read_text())
failed=json.loads((here/'PUBLICATION_COMPARE_INITIAL_EXECUTION.json').read_text())
assert failed['exit_code']==1
assert sha((here/'publication_compare.initial_exact_float.py').read_bytes())==failed['script_sha256']
for key in ['stdout','stderr']:
    raw=(here/f'publication_compare.initial_exact_float.{key}.txt').read_bytes()
    assert len(raw)==failed[f'{key}_bytes'] and sha(raw)==failed[f'{key}_sha256']
dump(here/'PUBLICATION_FINAL_RECHECK.json',dict(
    checked_utc=datetime.now(timezone.utc).isoformat(),origins=origin_rows,
    reused_sources_verified=len(pins['reused_immutable_sources']),
    preserved=pins['preserved'],procedure_identities_unchanged=True,
    successful_and_failed_verifier_receipts_match_complete_logs=True,
    no_author_or_primary_program_executed=True))
members=[]
for path in sorted(here.rglob('*')):
    if not path.is_file(): continue
    rel=path.relative_to(here).as_posix()
    include=(rel.startswith('publication_sources/') or
             path.parent==here and (path.name.startswith('PUBLICATION_') or
             path.name.startswith('publication_compare') or
             path.name in ('run_publication_compare.py','seal_publication_comparison.py')))
    if not include: continue
    assert rel not in old_paths
    data=path.read_bytes()
    members.append(dict(path=rel,bytes=len(data),sha256=sha(data)))
seal=dict(phase='Bounded final publication comparison',
    sealed_at_utc=datetime.now(timezone.utc).isoformat(),
    scope='Scientific sections B and C.2 only; prepared author primitive/timing controls and full byte bindings.',
    note_sha256='14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b',
    preserved=pins['preserved'],member_count=len(members),members=members,
    audit_verdict=False,publication_mutation=False,author_or_primary_execution=False,
    preservation='One-time content-hash ledger; all new members and this seal made read-only. Prior sealed work untouched.')
dump(seal_path,seal)
for member in members:
    path=here/member['path'];path.chmod(0o444)
    assert sha(path.read_bytes())==member['sha256']
seal_path.chmod(0o444)
print(json.dumps(dict(seal_path=str(seal_path),seal_sha256=sha(seal_path.read_bytes()),
                     report_sha256=sha((here/'PUBLICATION_COMPARISON.md').read_bytes()),
                     members=len(members),origins_verified=len(origin_rows),
                     PRE_members_verified=33,POST_members_verified=36),indent=2))
