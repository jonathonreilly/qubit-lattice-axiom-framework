"""Publication Part C/unit/cache binding only; no primary code execution."""
from pathlib import Path
import ast, datetime, difflib, hashlib, json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUBLIC = BASE / 'probe-physical-limits-publication'
HISTORY = BASE / 'probe-physical-limits-publication-history-before-front-precision'
NOTE = 'docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER = 'scripts/prepared_original_record_probe_energy_and_observation_limits_2026_09_24.py'
RESULT = 'outputs/prepared_probe_physical_limits_20260924/PROBE_PHYSICAL_LIMITS_RESULTS.json'
CACHE = 'logs/runner-cache/prepared_original_record_probe_energy_and_observation_limits_2026_09_24.txt'
EXTERNAL = ['PROBE_PHYSICAL_LIMITS_PUBLICATION_FROZEN_SOURCES.json', 'PROBE_PHYSICAL_LIMITS_PUBLICATION_CACHE_EXECUTION.json', 'PROBE_PHYSICAL_LIMITS_PRIMARY_ROOT_VERIFICATION.json']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, obj):
    dst = HERE / name
    assert not dst.exists(), f'Preserve existing evidence: {dst}'
    dst.write_text(json.dumps(obj, indent=2) + '\n')

def fingerprint(paths, overrides=None):
    digest = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    overrides = overrides or {}
    for name in paths:
        body = overrides.get(name)
        if body is None:
            body = (PUBLIC / name).read_bytes()
        encoded = name.encode()
        digest.update(len(encoded).to_bytes(8, 'big'))
        digest.update(encoded)
        digest.update(len(body).to_bytes(8, 'big'))
        digest.update(body)
    return digest.hexdigest()

def expected_cache(receipt, input_fingerprint, runner_sha):
    result = receipt['result']
    return ('===== runner cache v1 =====\n'
            f'runner: {RUNNER}\n'
            f'runner_sha256: {runner_sha}\n'
            f'input_fingerprint_sha256: {input_fingerprint}\n'
            f'timeout_sec: {result["timeout_sec"]}\n'
            f'exit_code: {result["exit_code"]}\n'
            f'elapsed_sec: {result["elapsed_sec"]:.2f}\n'
            f'status: {result["status"]}\n'
            '----- stdout -----\n'
            f'{result["stdout"]}\n'
            '----- stderr -----\n'
            f'{result["stderr"]}\n').encode()

for seal_name, expected in [('PRE_SEAL.json','6e08c4d893c9f40eabdb0b296c37bf1b850d48b88a2ec5dd10e2f939e866dce3'), ('POST_SEAL.json','e7121548b9b0372773a21dd88db53684327ed6a8f88b4a8e99c08919b7cd09fd')]:
    assert sha(HERE / seal_name) == expected
    for member in json.loads((HERE / seal_name).read_text())['members']:
        assert sha(HERE / member['path']) == member['sha256']
        assert (HERE / member['path']).stat().st_size == member['bytes']

frozen = json.loads((BASE / EXTERNAL[0]).read_text())
assert sha(BASE / EXTERNAL[0]) == '9c2fa71f055ceecaa9bb3a3ef6929c9be3772f8bd7a10a2e83480c8641217c69'
for name, expected in frozen['files_sha256'].items():
    assert sha(PUBLIC / name) == expected
expected_final = {NOTE:'2dd49ffa004fa09726b2388decb7c4a36dd69f2cdaf5f3bbb8ffe3e829a47c6d', RUNNER:'9e67aa1bdc1d9fa2227a934d219495c672aa299f9210cfdd0caed07143061676', RESULT:'790a2a72d86f4ecf72395c400ee93ba981e854a1a19a7d25d1adc15d79692e7e', CACHE:'a13f49a4bc999f280335dd0351f44a483a80d632d1d94db734d5d0870b6e9cb6'}
for name, expected in expected_final.items():
    assert sha(PUBLIC / name) == expected

old_note_path = HISTORY / Path(NOTE).name
old_text = old_note_path.read_text()
new_text = (PUBLIC / NOTE).read_text()
old_sentence = 'In the controlled small-background window, vacuum click probability remains'
new_sentence = "In Part C's regime b=o(tau g³), vacuum click probability remains"
assert sha(old_note_path) == '7b7814246e22731aac2538422d95035b60f6f1c23cf6035ade93c43dc137cce8'
assert old_text.count(old_sentence) == 1
assert new_text == old_text.replace(old_sentence, new_sentence)
delta = ''.join(difflib.unified_diff(old_text.splitlines(True), new_text.splitlines(True), fromfile='before-front-precision', tofile='final-publication'))
delta_path = HERE / 'PUBLICATION_FRONT_DELTA.diff'
assert not delta_path.exists()
delta_path.write_text(delta)

tree = ast.parse((PUBLIC / RUNNER).read_text())
declarations = {node.targets[0].id:ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in {'AUDIT_INPUT_PATHS','AUDIT_TIMEOUT_SEC','ROOT_CONTROL_SOURCES','RESULT_PATH'}}
paths = list(declarations['AUDIT_INPUT_PATHS'])
assert len(paths) == 7 and set(paths) == set(frozen['files_sha256']) - {RUNNER}
assert declarations['RESULT_PATH'] == RESULT and declarations['AUDIT_TIMEOUT_SEC'] == 120
original = ast.parse((HERE / 'post_sources' / 'unit_conversions.py').read_text())
start_index = next(i for i,n in enumerate(original.body) if isinstance(n,ast.Assign) and ast.unparse(n.targets[0]) == 'mp.mp.dps')
end_index = next(i for i in range(start_index,len(original.body)) if isinstance(original.body[i],ast.For))
unit = next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='unit_control')
assert isinstance(unit.body[-1],ast.Return) and ast.unparse(unit.body[-1].value) == 'rows'
dump = lambda body: ast.dump(ast.Module(body=body,type_ignores=[]), include_attributes=False)
assert dump(unit.body[:-1]) == dump(original.body[start_index:end_index+1])
arithmetic_ast_sha = hashlib.sha256(dump(unit.body[:-1]).encode()).hexdigest()

result_bytes = (PUBLIC / RESULT).read_bytes()
result = json.loads(result_bytes)
author_result = json.loads((HERE / 'post_sources' / 'UNIT_CONVERSIONS.json').read_text())
assert result['unit_rows'] == author_result['rows']
assert result['source_sha256'] == expected_final[RUNNER]
receipt = json.loads((BASE / EXTERNAL[1]).read_text())
execution = receipt['result']
assert execution['runner'] == RUNNER
assert execution['status'] == 'ok' and execution['exit_code'] == 0 and execution['stderr'] == ''
assert execution['elapsed_sec'] == 2.2022247314453125
assert execution['timeout_sec'] == declarations['AUDIT_TIMEOUT_SEC']
assert execution['stdout'].encode() == result_bytes + b'TOTAL_PASS: 3\n'
current_fp = fingerprint(paths)
assert (PUBLIC / CACHE).read_bytes() == expected_cache(receipt,current_fp,expected_final[RUNNER])
root_verification = json.loads((BASE / EXTERNAL[2]).read_text())
assert root_verification['files_sha256'] == expected_final
assert root_verification['primary_seconds'] == execution['elapsed_sec']
assert root_verification['exit_code'] == 0 and root_verification['stderr_bytes'] == 0

old_result_path = HISTORY / Path(RESULT).name
old_result = json.loads(old_result_path.read_text())
assert sha(old_result_path) == '9e43d561fb8a01e806b8e64e11028da0de4af33e085c29ac5304402a164ee78d'
nonruntime = lambda r: {k:v for k,v in r.items() if k != 'elapsed_seconds'}
assert nonruntime(result) == nonruntime(old_result)
old_receipt = json.loads((HISTORY / EXTERNAL[1]).read_text())
assert old_receipt['result']['stdout'].encode() == old_result_path.read_bytes() + b'TOTAL_PASS: 3\n'
old_fp = fingerprint(paths, {NOTE:old_note_path.read_bytes()})
assert old_fp != current_fp
assert (HISTORY / Path(CACHE).name).read_bytes() == expected_cache(old_receipt,old_fp,expected_final[RUNNER])

pins = []
sources = [(PUBLIC/n, 'publication_sources/tree/'+n, 'Frozen publication bytes; A/B portions bound mechanically only.') for n in frozen['files_sha256']]
sources += [(PUBLIC/n,'publication_sources/tree/'+n,'Complete execution output/cache, mechanical correspondence only for A/B rows.') for n in [RESULT,CACHE]]
sources += [(BASE/n,'publication_sources/receipts/'+n,'External source/execution receipt; root A/B claims are declarations outside independent science scope.') for n in EXTERNAL]
sources += [(PUBLIC/'scripts/runner_cache.py','publication_sources/infrastructure/runner_cache.py','Only input fingerprint and cache serialization logic used; no import or execution.')]
sources += [(p,'publication_sources/prior_run/'+p.name,'Preserved pre-precision publication history; mechanical delta/cache check.') for p in sorted(HISTORY.iterdir()) if p.is_file()]
for origin, name, scope in sources:
    dst = HERE / name
    dst.parent.mkdir(parents=True,exist_ok=True)
    assert not dst.exists()
    body = origin.read_bytes()
    dst.write_bytes(body)
    pins.append({'origin':str(origin),'snapshot':name,'sha256':sha(dst),'bytes':len(body),'scope':scope})
for pin in pins:
    assert sha(Path(pin['origin'])) == pin['sha256']

write('PUBLICATION_SOURCE_PINS.json', {'phase':'narrow released-source final binding', 'science_scope':'Complete Part C, its relevant introduction and D scope; unit-control arithmetic. No A/B science or root23/24 packet read.', 'sources':pins, 'PRE_seal_sha256':sha(HERE/'PRE_SEAL.json'), 'POST_seal_sha256':sha(HERE/'POST_SEAL.json')})
write('PUBLICATION_VERIFICATION_REPORT.json', {'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'frozen_sources_verified':len(frozen['files_sha256']), 'declared_inputs':paths, 'declared_input_count':len(paths), 'current_input_fingerprint_sha256':current_fp, 'prior_input_fingerprint_sha256':old_fp, 'final_source_hashes':expected_final, 'sole_note_delta':{'before':old_sentence,'after':new_sentence}, 'unit_core_AST_exact':True, 'unit_core_statement_count':len(unit.body)-1,'unit_core_AST_sha256':arithmetic_ast_sha,'unit_rows_exact_to_sealed_author':len(result['unit_rows']),'complete_result_stdout_exact':True,'cache_complete_bytes_match_receipt_and_sources':True,'nonruntime_payload_equal_to_prior_run':True,'primary_elapsed_seconds':execution['elapsed_sec'],'primary_exit_code':execution['exit_code'],'primary_stderr_bytes':0,'primary_reruns_by_checker':0,'author_programs_imported_or_executed':0,'root_AB_AST_and_source_equivalence_independently_checked':False,'root_AB_science_checked':False,'snapshots':len(pins),'PRE_and_POST_members_preserved':True})
print(json.dumps({'frozen_sources':len(frozen['files_sha256']),'declared_inputs':len(paths),'unit_AST_exact':True,'unit_rows_exact':len(result['unit_rows']),'full_stdout_cache_exact':True,'prior_nonruntime_payload_exact':True,'new_input_fingerprint':current_fp,'snapshots':len(pins),'primary_reruns':0},indent=2))
