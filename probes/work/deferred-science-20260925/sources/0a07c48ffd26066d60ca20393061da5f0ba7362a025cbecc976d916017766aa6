#!/usr/bin/env python3
"""Bounded source/evidence comparison; never imports or runs scientific code."""
from __future__ import annotations
import ast
from collections import Counter
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUB = BASE / 'prepared-observation-publication'
DEST = HERE / 'publication_sources'
NOTE = 'docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER = 'scripts/original_record_calibration_and_prepared_matter_probe_2026_09_24.py'
RESULT = 'outputs/prepared_original_record_probe_20260924/PREPARED_ORIGINAL_RECORD_PROBE_RESULTS.json'
CACHE = 'logs/runner-cache/original_record_calibration_and_prepared_matter_probe_2026_09_24.txt'
EXPECTED = {
    NOTE: '14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b',
    RUNNER: 'c760fac9894a0d0536e139a47723e282f7a96ef2f4aa69fdc5a4a7da31a77814',
    RESULT: 'f33be280f9a0f90aa2acb7da8bad01890da79a2e9df9eb4fe0645859e23a911a',
    CACHE: '041a5de0ab7d6c8cc0342446f192a4318b7b8da9b6180f10788105918febed03',
}
EXTERNAL = {
    'PREPARED_OBSERVATION_PUBLICATION_FROZEN_SOURCES.json': 'f299cae89c6852cb8e5e8b8b707f5e6743239ee4c95e6deba9de7af83d78f4c2',
    'PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json': '9e71e3314ff31d14191034dfd6ddb0d01423ce4e7dc85c995e6143bdd8295ea1',
    'PREPARED_OBSERVATION_PRIMARY_WRAPPER_FAILURE.md': '7b769eb4c97afdcc6be795d3b81937176b3b7ed2eafe4875feef00db6ecb6a21',
}

def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(path, data):
    with path.open('x') as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write('\n')


pins = []


def freeze(origin, relative, expected=None, scope='mechanical source binding'):
    data = origin.read_bytes()
    digest = sha(data)
    if expected is not None:
        assert digest == expected, (str(origin), digest, expected)
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        assert target.read_bytes() == data
    else:
        with target.open('xb') as handle:
            handle.write(data)
    assert target.read_bytes() == origin.read_bytes()
    pins.append(dict(origin=str(origin), frozen_path=str(target.relative_to(HERE)),
                     bytes=len(data), sha256=digest, reviewed_scope=scope))
    return data


def verify_seal(name, expected):
    p = HERE / name
    assert sha(p.read_bytes()) == expected
    seal = json.loads(p.read_text())
    for member in seal['members']:
        data = (HERE / member['path']).read_bytes()
        assert len(data) == member['bytes']
        assert sha(data) == member['sha256'], member['path']
    return dict(path=name, sha256=expected, members_verified=len(seal['members']))


preserved = [
    verify_seal('PRE_SEAL.json', '5c72901c7a027ba7f00685ce39abe206a2ae0b8a73098ab35e7f0b72324f177c'),
    verify_seal('POST_SEAL.json', 'dca495a9a8d810740b3048f38e6709584df74d4d707de593f19426defcae0af1'),
]

for rel, expected in EXPECTED.items():
    scope = ('Scientific review: sections B and C.2 only; full bytes pinned.' if rel == NOTE else
             'Scientific review: primitive_control, timing_probability, timing_control; full wrapper and declaration binding.' if rel == RUNNER else
             'Full bytes bound mechanically; prepared_primitive and separate_timing inspected scientifically.')
    freeze(PUB / rel, Path('publication') / rel, expected, scope)
for rel, expected in EXTERNAL.items():
    freeze(BASE / rel, Path('external') / rel, expected,
           'Execution/fingerprint provenance only; wrapper-failure file is author-reported.')
freeze(PUB / 'scripts/runner_cache.py', 'cache_implementation.py', scope=
       'Read declared_input_paths, declared_input_fingerprint and cache-output formatting; not an audit execution.')

manifest = json.loads((BASE / 'PREPARED_OBSERVATION_PUBLICATION_FROZEN_SOURCES.json').read_text())
source = (PUB / RUNNER).read_text()
tree = ast.parse(source)
assigns = {target.id: ast.literal_eval(node.value)
           for node in tree.body if isinstance(node, ast.Assign)
           for target in node.targets if isinstance(target, ast.Name)}
declared = assigns['AUDIT_INPUT_PATHS']
assert len(declared) == 6 and len(set(declared)) == 6
assert set(manifest['files_sha256']) == set(declared) | {RUNNER}
fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
declared_rows = []
for rel in declared:
    path = Path(rel)
    assert not path.is_absolute() and '..' not in path.parts and path.as_posix() == rel
    data = (PUB / rel).read_bytes()
    assert sha(data) == manifest['files_sha256'][rel]
    if rel != NOTE:
        freeze(PUB / rel, Path('declared') / rel, manifest['files_sha256'][rel],
               'Byte binding only here; prior checked parent premises reused only within PRE/POST scope.')
    name = rel.encode()
    fingerprint.update(len(name).to_bytes(8, 'big'))
    fingerprint.update(name)
    fingerprint.update(len(data).to_bytes(8, 'big'))
    fingerprint.update(data)
    declared_rows.append(dict(path=rel, bytes=len(data), sha256=sha(data)))
assert fingerprint.hexdigest() == '53913bb08db29e1c85b0665361ec01cf06bf78cc9d6b8651ccb61ac857c3d374'

author_source_path = HERE / 'post_sources/author/prepared_probe_controls.py'
author_source = author_source_path.read_text()
assert sha(author_source_path.read_bytes()) == '27da3c4fdff89c16e4c15c96e41296f2ae51964c6048b727c07c2b55cba9683c'
functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
author_functions = {node.name: node for node in ast.parse(author_source).body if isinstance(node, ast.FunctionDef)}
function_rows = []
for name in ('primitive_control', 'timing_probability', 'timing_control'):
    current = ast.get_source_segment(source, functions[name])
    author = ast.get_source_segment(author_source, author_functions[name])
    current_ast = ast.dump(functions[name], include_attributes=False)
    author_ast = ast.dump(author_functions[name], include_attributes=False)
    assert current == author and current_ast == author_ast
    assert sha(current.encode()) == manifest['root_functions'][name]
    function_rows.append(dict(name=name, source_bytes_sha256=sha(current.encode()),
                              ast_sha256=sha(current_ast.encode()),
                              exact_text_equal=True, ast_equal=True,
                              line=functions[name].lineno, end_line=functions[name].end_lineno))

receipt = json.loads((BASE / 'PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json').read_text())
execution = receipt['result']
assert receipt['wrapper_elapsed_recorded'] is False
assert receipt['path'] == str(PUB / CACHE)
assert execution['runner'] == RUNNER and execution['status'] == 'ok'
assert execution['exit_code'] == 0 and execution['stderr'] == ''
assert execution['elapsed_sec'] == 0.45025181770324707
assert execution['timeout_sec'] == assigns['AUDIT_TIMEOUT_SEC'] == 120
result_bytes = (PUB / RESULT).read_bytes()
assert execution['stdout'].encode() == result_bytes + b'TOTAL_PASS: 3\n'
result = json.loads(result_bytes)
assert result['source_sha256'] == EXPECTED[RUNNER] and result['all_assertions_passed'] is True
expected_cache = (
    '===== runner cache v1 =====\n'
    f'runner: {RUNNER}\n'
    f'runner_sha256: {EXPECTED[RUNNER]}\n'
    f'input_fingerprint_sha256: {fingerprint.hexdigest()}\n'
    f'timeout_sec: {execution["timeout_sec"]}\n'
    f'exit_code: {execution["exit_code"]}\n'
    f'elapsed_sec: {execution["elapsed_sec"]:.2f}\n'
    f'status: {execution["status"]}\n'
    '----- stdout -----\n' + execution['stdout'][-200000:] + '\n'
    '----- stderr -----\n' + execution['stderr'][-50000:] + '\n'
).encode()
assert len(execution['stdout']) < 200000
assert (PUB / CACHE).read_bytes() == expected_cache

author = json.loads((HERE / 'post_sources/author/PREPARED_PROBE_RESULTS.json').read_text())
assert result['prepared_primitive'] == author['primitive']
assert result['separate_timing'] == author['separate_timing']
primitive = result['prepared_primitive']
assert len(primitive['rows']) == 4 and len(primitive['common_flow_paths']) == 3
assert set(primitive['effects']) == {'-1', '1'}
for row in primitive['rows']:
    assert row['initial_records'] == 112 and row['output_records'] == 114
    assert row['retained_paths'] == row['outward_to_birth_site_rejected'] == 1
    assert row['physical_flux_cases_checked'] == 5
timing = result['separate_timing']
assert len(timing['rows']) == 10
small, large = timing['rows'][-2:]
assert small['g'] == large['g'] == .025
assert small['window_exponent'] == 3.5 and large['window_exponent'] == 2.
assert round(small['vacuum_over_b_g2'], 7) == .5165821
assert round(small['excess_over_b_g2'], 7) == .9996747
assert round(large['vacuum_over_b_g2'], 2) == 872.39
assert format(timing['maximum_scaled_quadrature_refinement'], '.3g') == '5.22e-08'
# The note's 5.23e-8 is a conservative three-significant-figure upper bound.
assert timing['maximum_scaled_quadrature_refinement'] < 5.23e-8
arithmetic = []
for row in timing['rows']:
    # Preserve the author's left-associated denominator; g**2 can differ by one ulp.
    scale = row['window'] * row['g'] * row['g']
    for label, value in [('vacuum_over_b_g2', row['vacuum_probability']/scale),
                         ('one_over_b_g2', row['one_probability']/scale),
                         ('excess_over_b_g2', (row['one_probability']-row['vacuum_probability'])/scale)]:
        assert row[label] == value
    arithmetic.append(dict(g=row['g'], window_exponent=row['window_exponent'], exact_stored_arithmetic=True))
historical = json.loads((HERE / 'post_sources/author/EXECUTION.json').read_text())
assert historical['elapsed_seconds'] == 1.5052074589766562
assert historical['stderr_bytes'] == historical['exit_code'] == 0

note = (PUB / NOTE).read_text()
section_b = note.split('## B. A supplied physical preparation for one original mark\n', 1)[1].split('\n## C.', 1)[0]
section_c2 = note.split('### C.2 Preparation choices carry the single-mark response\n', 1)[1].split('\n## D.', 1)[0]
excerpt = ('## B. A supplied physical preparation for one original mark\n' + section_b +
           '\n### C.2 Preparation choices carry the single-mark response\n' + section_c2)
with (HERE / 'PUBLICATION_SCOPED_EXCERPT.md').open('x') as h:
    h.write(excerpt)
assert '4M lambda_j eta' in section_b
assert 'j_S P=0' in section_b
assert 'literal annotations' in section_b
assert 'not a computed Gram matrix' in section_b
assert 'not graph-norm guarantees' in section_c2
root_note = (HERE / 'post_sources/author/PREPARED_MATTER_INTERFERENCE_PROBE_ROOT.md').read_text()
root_body = '## 1. A physical two-branch preparation\n' + root_note.split('## 1. A physical two-branch preparation\n', 1)[1]
normalized_b = section_b.replace('### ', '## ')
diff = ''.join(difflib.unified_diff(root_body.splitlines(True), normalized_b.splitlines(True),
                                 fromfile='sealed root prepared proof (body)', tofile='publication section B'))
with (HERE / 'PUBLICATION_B_SOURCE_DIFF.txt').open('x') as h:
    h.write(diff)

# Symbolic check of the explicit C.2 translation, not a new primitive simulation.
ac, dc, de, ae = ('a','c'), ('d','c'), ('d','e'), ('a','e')
new_c = Counter({ae:1, ac:-1, de:-1})
old_c = Counter({dc:-1})
loop = Counter({ac:1, dc:-1, de:1, ae:-1})
def add(*parts):
    out = Counter()
    for part in parts:
        for key, value in part.items(): out[key] += value
    return {key:value for key,value in out.items() if value}
def div(flow):
    out = Counter()
    for (start,end),value in flow.items(): out[start] += value; out[end] -= value
    return {key:value for key,value in out.items() if value}
assert div(new_c) == {'d':-1,'c':1}
assert add(old_c, {key:-value for key,value in loop.items()}) == dict(new_c)
assert add(new_c,{ae:-1}) == add({de:-1},{ac:-1})
dressing = dict(new_c_divergence=div(new_c), equal_surviving_output=True,
                equals_prior_POST_eta_c_minus_loop=True,
                meaning='Both branch outputs agree; balanced minus state is annihilated for every reference field.')

# Count-bracket identity has an analytic proof for all M; finite arithmetic only checks transcription.
bracket_cases = 0
for cap in range(55):
    for lower in range(cap+1):
        for upper in range(lower,cap+1):
            assert upper*upper-lower*lower <= 2*cap*(upper-lower)
            bracket_cases += 1

reused = []
for rel in ['PRE.md','PRE_SEAL.json','POST.md','POST_SEAL.json','POST_SOURCE_PINS.json',
            'POST_CONTROL_RESULTS.json','POST_PATH_CERTIFICATES.json','post_control.py',
            'post_sources/author/AUTHOR_SEAL.json','post_sources/author/PREPARED_MATTER_INTERFERENCE_PROBE_ROOT.md',
            'post_sources/author/prepared_probe_controls.py','post_sources/author/PREPARED_PROBE_RESULTS.json',
            'post_sources/author/EXECUTION.json']:
    data=(HERE/rel).read_bytes()
    reused.append(dict(path=rel,bytes=len(data),sha256=sha(data)))
dump(HERE/'PUBLICATION_SOURCE_PINS.json',dict(
    created_utc=datetime.now(timezone.utc).isoformat(),
    scope='Scientific: B and C.2 only; source/evidence byte and declared-input cache bindings.',
    sources=pins,reused_immutable_sources=reused,preserved=preserved,
    no_author_code_executed=True,no_primary_rerun=True,no_other_active_packets_read=True))

summary = dict(
    scope='B and C.2 only; prepared author controls and full mechanical source/runtime binding.',
    preserved=preserved, frozen_origins=len(pins), declared_inputs=declared_rows,
    input_fingerprint_sha256=fingerprint.hexdigest(), helper_comparison=function_rows,
    receipt_sha256=EXTERNAL['PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json'],
    primary_elapsed_sec=execution['elapsed_sec'],cache_elapsed_display='0.45',
    wrapper_elapsed_recorded=False,result_internal_elapsed_seconds=result['elapsed_seconds'],
    historical_author_elapsed_seconds=historical['elapsed_seconds'],
    historical_author_internal_elapsed_seconds=author['elapsed_seconds'],
    full_execution_stdout_equals_result_plus_certificate=True,
    cache_bytes_exactly_reconstructed=True,cache_stdout_not_truncated=True,
    primary_exit_code=execution['exit_code'],primary_stderr_bytes=len(execution['stderr'].encode()),
    prepared_scientific_payload_exactly_equal_to_sealed_author=True,
    prepared_primitive=primitive,separate_timing=timing,
    arithmetic_rows=arithmetic,C2_symbolic_translation=dressing,
    count_bracket_transcription=dict(cases=bracket_cases,maximum_cap=54,
        analytic_identity='upper^2-lower^2=(upper-lower)(upper+lower)<=2M(upper-lower)'),
    wrapper_failure=dict(kind='author-reported PosixPath receipt serialization failure before fresh run',
        traceback_independently_read=False,failure_file_sha256=EXTERNAL['PREPARED_OBSERVATION_PRIMARY_WRAPPER_FAILURE.md']),
    evidence_limits=['No author/primary scientific program executed or imported.',
                    'Timing propagation and quadrature were not independently reproduced.',
                    'Calibration payload is mechanically byte-bound only; sections A, C.1 and D outside scientific review.',
                    'The 5.23e-8 prose value bounds the stored 5.224698474128429e-8; no interval enclosure.',
                    'No audit verdict or entire-publication approval.'])
dump(HERE/'PUBLICATION_EVIDENCE_VERIFICATION.json',summary)
print(json.dumps(summary,indent=2,allow_nan=False))
