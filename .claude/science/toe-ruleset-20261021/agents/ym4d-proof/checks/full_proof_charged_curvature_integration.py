"""Mechanical integration of the charged review, REC correction, and author freezes.

This checks bytes, documentation, and recorded reproductions. It does not add
an independent mathematical review, certify either new author argument, run
the whole repository pipeline, apply audit grades, or complete either target.
"""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import re
import subprocess
import tempfile

L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C = L / 'checks'
OUT = C / 'full_proof_charged_curvature_integration_validation.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(name):
    return json.loads((C / name).read_bytes())


def bind(record):
    data = Path(record['path']).read_bytes()
    assert sha(data) == record['sha256'], record['path']
    if 'bytes' in record:
        assert len(data) == record['bytes'], record['path']


receipt_pins = {
    'review_charged_jet_receipt.json': 'ad4226851b1b1d7b29e87f19c42c18a021fd8dd7afbfb5a85eeff5007120962d',
    'review_rec_tensor_fix_receipt.json': '599b901309efc62ad8e7bffcf428fbb03d4a236ef2f6fc83c6f4971e4104d0fd',
    'bottom_second_curvature_receipt.json': '88d659a2a512fcc57b95dc077836ceb555dbeea177be36cde0abf4f6d0f977b4',
    'covariant_soft_background_receipt.json': '5613420d87a16c573b2848cf43d2385cad7961dac3f0d0379fd5ce975d97e5df',
}
for name, digest in receipt_pins.items():
    assert sha((C / name).read_bytes()) == digest, name

charged = read('full_proof_charged_review_bindings.json')
author_packets = [
    ('bottom_second_curvature_receipt.json', 'owned_artifacts'),
    ('covariant_soft_background_receipt.json', 'files'),
]
artifact_records = list(charged['artifacts'])
for name, key in author_packets:
    artifact_records += read(name)[key]
    p = C / name
    artifact_records.append({'path': str(p), 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size})
for row in artifact_records + charged['source_and_supporting_proof_inputs']:
    bind(row)

rec = read('review_rec_tensor_fix_receipt.json')
for key in ['source', 'coordinator_fix', 'original_review', 'report']:
    bind(rec[key])
fix = read('full_proof_rec_tensor_fix.json')
before = subprocess.check_output(['git', 'show', fix['original_source_commit'] + ':' + fix['source']])
after = Path(fix['source']).read_bytes()
assert sha(before) == fix['before_sha256'] == rec['original_source']['sha256']
assert sha(after) == fix['after_sha256']
assert before.decode().count(fix['original_paragraph']) == 1
assert before.decode().replace(fix['original_paragraph'], fix['replacement_paragraph']).encode() == after
assert before[:5169] == after[:5169]
assert sha(after[:5169]) == rec['prefix_5169_sha256']
lines = after.decode().splitlines(keepends=True)
for row in rec['source_read_ranges']:
    assert sha(''.join(lines[row['start'] - 1:row['end']]).encode()) == row['sha256'], row

replays = read('full_proof_charged_review_replay_summary.json')
assert replays['all_ok'] and len(replays['runs']) == 4
for run in replays['runs']:
    assert run['exit_code'] == 0 and run['exact_non_time_json_match']
    assert run['passed'] == run['total']
    for key in ['stdout', 'stderr', 'reference']:
        bind(run[key])
    assert not Path(run['stderr']['path']).read_bytes()
    actual = json.loads(Path(run['stdout']['path']).read_bytes())
    reference = json.loads(Path(run['reference']['path']).read_bytes())
    for key in run['excluded_top_level_fields']:
        actual.pop(key, None)
        reference.pop(key, None)
    assert actual == reference, run['label']

paths = {row['path'] for row in artifact_records}
paths.update(str(p) for p in C.glob('full_proof_charged_review_*'))
paths.update(str(L / name) for name in [
    'HANDOFF.md', 'APPROACH_REGISTRY.md', 'SESSION25_RESULTS.md', 'PROOF.md',
    'REC_LIB.md', 'REVIEW_REC_TENSOR_FIX_ASTRA.md', 'LITERATURE_BRIDGES.md',
    'ASSUMPTIONS_AND_IMPORTS.md',
])
paths.update(str(C / name) for name in [
    'review_rec_tensor_fix_receipt.json', 'full_proof_rec_tensor_fix.json',
    'full_proof_charged_rec_summary_update.json',
    'full_proof_curvature_background_freeze_status.json',
    'full_proof_primary_followup_20261029.json',
    'full_proof_charged_curvature_integration.py',
])
assert str(OUT) not in paths
records = []
markdown = []
local_links = []
empty_json = []
header_dir = Path(tempfile.mkdtemp(prefix='ym-charged-curvature-integration-'))
for name in sorted(paths):
    p = Path(name)
    data = p.read_bytes()
    records.append({'path': name, 'sha256': sha(data), 'bytes': len(data)})
    if p.suffix == '.py':
        ast.parse(data, filename=name)
    if p.suffix == '.json':
        if data:
            json.loads(data)
        else:
            assert p.name == 'review_charged_jet_n1_01_out.json'
            empty_json.append(name)
    if p.suffix != '.md':
        continue
    text = data.decode()
    if p.name == 'PROOF.md':
        text, legacy = text.split('> **PROVENANCE WARNING', 1)
        assert sha(('> **PROVENANCE WARNING' + legacy).encode()) == '4efdee19aa03123a89053e466525f0ef5e9d8a4b8eb1ea38a1e87125043e728c'
        target = header_dir / 'PROOF_header.md'
        target.write_text(text)
        markdown.append(str(target))
    else:
        markdown.append(name)
    fenced = False
    for line in text.splitlines():
        if line.startswith('> '):
            line = line[2:]
        elif line == '>':
            line = ''
        if line.lstrip().startswith('```'):
            fenced = not fenced
            continue
        if fenced or line.startswith('    '):
            continue
        for value in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', line):
            target = value.split('#', 1)[0].strip('<>')
            if not target or re.match(r'^[a-zA-Z]+:', target):
                continue
            assert (p.parent / target).exists(), (name, target)
            local_links.append({'source': name, 'target': str(p.parent / target)})

vocab_path = header_dir / 'vocab.json'
lint = subprocess.run(['python3', 'scripts/vocab_lint.py', '--report-only', '--report-path', str(vocab_path), *markdown], capture_output=True)
assert lint.returncode == 0, lint.stderr.decode()
vocab = json.loads(vocab_path.read_bytes())
whitespace = subprocess.run(['git', 'diff', '--check', 'HEAD', '--', *sorted(paths)], capture_output=True)
assert whitespace.returncode == 0, whitespace.stdout.decode() + whitespace.stderr.decode()

result = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': __doc__,
    'all_ok': True,
    'base_revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'files': records,
    'receipt_pins': receipt_pins,
    'bound_artifact_records': len(artifact_records),
    'charged_proof_inputs_bound': len(charged['source_and_supporting_proof_inputs']),
    'rec_fix': {'exact_single_paragraph_replacement': True, 'unchanged_prefix_bytes': 5169,
                'affected_review_confirmed': True, 'source_read_ranges_bound': len(rec['source_read_ranges']),
                'whole_library_certified': False},
    'reviewer_programs_reproduced': 4,
    'reproduced_predicates': sum(run['total'] for run in replays['runs']),
    'archived_empty_json_preserved': empty_json,
    'local_links_checked': len(local_links),
    'vocabulary_report': vocab,
    'vocabulary_stdout': lint.stdout.decode(),
    'whitespace_exit_code': whitespace.returncode,
    'legacy_PROOF_body_unchanged': True,
    'bottom_curvature_independent_review': 'PENDING',
    'covariant_background_independent_review': 'PENDING',
    'LIB1_evidence_hold': 'OPEN: B1',
    'full_existence': 'OPEN',
    'physical_continuum_mass_gap': 'OPEN',
}
assert not OUT.exists(), str(OUT)
OUT.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'all_ok': True, 'files': len(records), 'bound_artifact_records': len(artifact_records),
                  'local_links_checked': len(local_links), 'vocabulary_report': vocab}))
