#!/usr/bin/env python3
"""Seal only the completed POST; recheck and leave all PRE bytes unchanged."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name):
    return json.loads((HERE/name).read_bytes())


pre_raw = (HERE/'PRE_SEAL.json').read_bytes()
assert sha(pre_raw) == 'a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'
pre = json.loads(pre_raw)
old_paths = {'PRE_SEAL.json'} | {row['path'] for row in pre['members']}
for row in pre['members']:
    raw = (HERE/row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']

pins = read('POST_SOURCE_PINS.json')
for row in pins['author_sources']:
    raw = (HERE/row['frozen_path']).read_bytes()
    assert raw == Path(row['origin']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
for row in pins['reused_PRE_sources']:
    assert sha(Path(row['origin']).read_bytes()) == row['sha256']

for label, script, result in [('post_freeze','post_freeze.py','POST_SOURCE_PINS.json'),
                              ('post_check','post_check.py','POST_CHECK_RESULTS.json'),
                              ('post_verify','post_verify.py','POST_FINAL_VERIFICATION.json')]:
    receipt = read(label+'.execution.json')
    assert receipt['exit_code'] == 0
    assert receipt['script_sha256'] == sha((HERE/script).read_bytes())
    for stream in ('stdout','stderr'):
        raw = (HERE/(label+'.'+stream+'.txt')).read_bytes()
        assert len(raw) == receipt[stream+'_bytes'] and sha(raw) == receipt[stream+'_sha256']
    assert not (HERE/(label+'.stderr.txt')).read_bytes()
    assert (HERE/(label+'.stdout.txt')).read_bytes() == (HERE/result).read_bytes()

verified = read('POST_FINAL_VERIFICATION.json')
assert verified['report_sha256'] == sha((HERE/'POST.md').read_bytes())
assert verified['source_sha256'] == sha((HERE/'post_verify.py').read_bytes())

expected = {'POST.md','POST_SOURCE_PINS.json','POST_CHECK_RESULTS.json','POST_FINAL_VERIFICATION.json',
            'POST_EVIDENCE_LOG.md','POST_CHECKPOINT.md','post_seal.py'}
for label in ('post_freeze','post_check','post_verify'):
    expected |= {label+'.py', label+'.execution.json', label+'.stdout.txt', label+'.stderr.txt'}
expected |= {row['frozen_path'] for row in pins['author_sources']}
actual = {str(path.relative_to(HERE)) for path in HERE.rglob('*') if path.is_file()} - old_paths
assert actual == expected, dict(unexpected=sorted(actual-expected), missing=sorted(expected-actual))
assert len(expected) == 38

members = []
for name in sorted(expected):
    raw = (HERE/name).read_bytes()
    members.append(dict(path=name, bytes=len(raw), sha256=sha(raw)))
seal = dict(sealed_utc=datetime.now(timezone.utc).isoformat(),
    phase='Released-source POST; bounded independent comparison, not an audit verdict',
    PRE_seal_sha256=sha(pre_raw), PRE_members_unchanged=65,
    author_seal_sha256='b0378a615fdaaca99e563a78e4e1361a19635976e114e2f04f5e5485ceb8a69c',
    author_members_frozen=18, author_code_run_or_imported=False,
    forbidden_other_packets_read=False, all_new_POST_execution_logs_bound=True,
    report_sha256=sha((HERE/'POST.md').read_bytes()), members=members)
raw = json.dumps(seal, indent=2)+'\n'
with (HERE/'POST_SEAL.json').open('x') as output:
    output.write(raw)
for name in expected | {'POST_SEAL.json'}:
    (HERE/name).chmod(0o444)
for row in members:
    raw_member = (HERE/row['path']).read_bytes()
    assert len(raw_member) == row['bytes'] and sha(raw_member) == row['sha256']
print(json.dumps(dict(POST_seal_sha256=sha((HERE/'POST_SEAL.json').read_bytes()),
    POST_members=len(members), report_sha256=seal['report_sha256'],
    PRE_seal_unchanged=sha((HERE/'PRE_SEAL.json').read_bytes()) == sha(pre_raw),
    read_only_member_files=True), indent=2))
