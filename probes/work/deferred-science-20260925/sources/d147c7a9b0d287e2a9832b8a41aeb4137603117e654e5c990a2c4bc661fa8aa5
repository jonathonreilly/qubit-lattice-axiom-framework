#!/usr/bin/env python3
"""Seal the scoped publication comparison without changing earlier packets."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name):
    return json.loads((HERE/name).read_bytes())


old_paths = set()
prior_records = []
for name, expected in [('PRE_SEAL.json','a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'),
                       ('POST_SEAL.json','583af00f065fbc2d9c5de9fff379b441f9c09a67cad630612380929329932369')]:
    raw = (HERE/name).read_bytes()
    assert sha(raw) == expected
    seal = json.loads(raw)
    old_paths.add(name)
    for row in seal['members']:
        member = (HERE/row['path']).read_bytes()
        assert len(member) == row['bytes'] and sha(member) == row['sha256']
        old_paths.add(row['path'])
    prior_records.append(dict(seal=name, sha256=expected, unchanged_members=len(seal['members'])))

old_pins = read('POST_SOURCE_PINS.json')
for row in old_pins['author_sources']:
    raw = (HERE/row['frozen_path']).read_bytes()
    assert raw == Path(row['origin']).read_bytes() and sha(raw) == row['sha256']
for row in old_pins['reused_PRE_sources']:
    assert sha(Path(row['origin']).read_bytes()) == row['sha256']

pins = read('PUBLICATION_SOURCE_PINS.json')
for row in pins['sources']:
    raw = (HERE/row['frozen_path']).read_bytes()
    assert raw == Path(row['origin']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']

receipt = read('publication_compare.execution.json')
assert receipt['exit_code'] == 0
assert receipt['script_sha256'] == sha((HERE/'publication_compare.py').read_bytes())
for stream in ('stdout','stderr'):
    raw = (HERE/('publication_compare.'+stream+'.txt')).read_bytes()
    assert len(raw) == receipt[stream+'_bytes'] and sha(raw) == receipt[stream+'_sha256']
assert not (HERE/'publication_compare.stderr.txt').read_bytes()
assert (HERE/'publication_compare.stdout.txt').read_bytes() == (HERE/'PUBLICATION_CHECK_RESULTS.json').read_bytes()
result = read('PUBLICATION_CHECK_RESULTS.json')
assert result['source_sha256'] == receipt['script_sha256']
assert not result['unallowed_payload_changes'] and result['cache_exact_format_and_tail_of_execution']
assert result['input_fingerprint_sha256'] == pins['input_fingerprint_sha256']

expected = {row['frozen_path'] for row in pins['sources']}
for row in result['Part_B_payload']:
    name = 'publication_sources/Part_B_payload/'+row['result']
    raw = (HERE/name).read_bytes()
    assert len(raw) == row['fresh_stage']['stdout_bytes'] and sha(raw) == row['fresh_stage']['stdout_sha256']
    expected.add(name)
expected |= {'PUBLICATION_COMPARISON.md','PUBLICATION_EVIDENCE_LOG.md','PUBLICATION_SOURCE_PINS.json',
             'PUBLICATION_CHECK_RESULTS.json','PUBLICATION_SCOPED_NOTE.md','PUBLICATION_PART_B_DIFF.txt',
             'publication_compare.py','publication_compare.execution.json','publication_compare.stdout.txt',
             'publication_compare.stderr.txt','publication_seal.py'}
actual = {str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file()} - old_paths
assert actual == expected, dict(unexpected=sorted(actual-expected), missing=sorted(expected-actual))
assert len(expected) == 34
members = []
for name in sorted(expected):
    raw = (HERE/name).read_bytes()
    members.append(dict(path=name,bytes=len(raw),sha256=sha(raw)))
seal = dict(sealed_utc=datetime.now(timezone.utc).isoformat(),
    phase='Final publication correspondence: Part B and shared framing only',
    not_an_audit_verdict=True, prior_packets=prior_records,
    prior_author_origins_unchanged=len(old_pins['author_sources']),
    prior_PRE_origins_unchanged=len(old_pins['reused_PRE_sources']),
    publication_sources_frozen_and_live_equal=len(pins['sources']),
    no_primary_or_author_program_execution=True, no_new_frontier_derivation=True,
    Part_A_scientific_review=False,
    report_sha256=sha((HERE/'PUBLICATION_COMPARISON.md').read_bytes()),
    source_manifest_sha256=sha((HERE/'PUBLICATION_SOURCE_PINS.json').read_bytes()),
    input_fingerprint_sha256=pins['input_fingerprint_sha256'], members=members)
with (HERE/'PUBLICATION_COMPARISON_SEAL.json').open('x') as output:
    json.dump(seal,output,indent=2)
    output.write('\n')
for name in expected | {'PUBLICATION_COMPARISON_SEAL.json'}:
    (HERE/name).chmod(0o444)
for row in members:
    raw = (HERE/row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
print(json.dumps(dict(seal_sha256=sha((HERE/'PUBLICATION_COMPARISON_SEAL.json').read_bytes()),
    members=len(members), report_sha256=seal['report_sha256'],
    PRE_POST_unchanged=True, all_member_files_read_only=True),indent=2))
