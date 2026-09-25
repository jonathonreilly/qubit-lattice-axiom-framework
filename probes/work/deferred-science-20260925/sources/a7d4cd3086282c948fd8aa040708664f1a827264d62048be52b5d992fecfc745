"""Mechanical final-source correspondence; never imports or runs a primary."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import copy
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
PUB = HERE/'publication_sources/publication'
EXT = HERE/'publication_sources/external'
RUNNER = 'scripts/optical_reference_energy_limits_for_original_record_counts_2026_09_24.py'
NOTE = 'docs/OPTICAL_REFERENCE_ENERGY_LIMITS_FOR_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RESULT = 'outputs/optical_observation_bridge_20260924/OPTICAL_OBSERVATION_RESULTS.json'
CACHE = 'logs/runner-cache/optical_reference_energy_limits_for_original_record_counts_2026_09_24.txt'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(p):
    return json.loads(p.read_text())


def dump(nodes):
    return ast.dump(ast.Module(body=nodes, type_ignores=[]), include_attributes=False)


def target(node, name):
    return isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)


def normalize_space(text):
    return re.sub(r'\s+', ' ', text).strip()


pins = load(HERE/'PUBLICATION_SOURCE_PINS.json')
for row in pins['sources']:
    assert sha(Path(row['origin'])) == row['sha256'] == sha(HERE/row['snapshot'])
    assert (HERE/row['snapshot']).stat().st_size == row['bytes']
for name in ['PRE_SEAL.json', 'POST_SEAL.json']:
    for row in load(HERE/name)['members']:
        assert sha(HERE/row['path']) == row['sha256']
        assert (HERE/row['path']).stat().st_size == row['bytes']

frozen = load(EXT/'OPTICAL_OBSERVATION_PUBLICATION_FROZEN_SOURCES.json')
root_report = load(EXT/'OPTICAL_OBSERVATION_PRIMARY_ROOT_VERIFICATION.json')
execution = load(EXT/'OPTICAL_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json')['result']
for rel, expected in (frozen['files_sha256'] | root_report['files_sha256']).items():
    assert sha(PUB/rel) == expected

tree = ast.parse((PUB/RUNNER).read_text())
functions = {n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
literal = {n.targets[0].id:ast.literal_eval(n.value) for n in tree.body
           if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)
           and n.targets[0].id in {'AUDIT_INPUT_PATHS','AUDIT_TIMEOUT_SEC','ROOT_CONTROL_SOURCES','RESULT_PATH'}}
paths = literal['AUDIT_INPUT_PATHS']
assert isinstance(paths,tuple) and len(paths)==len(set(paths))==5
assert paths[0] == NOTE and literal['RESULT_PATH'] == RESULT
assert literal['AUDIT_TIMEOUT_SEC'] == execution['timeout_sec'] == 120
digest=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
inputs=[]
for rel in paths:
    assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
    assert Path(rel).as_posix()==rel
    data=(PUB/rel).read_bytes();encoded=rel.encode()
    digest.update(len(encoded).to_bytes(8,'big'));digest.update(encoded)
    digest.update(len(data).to_bytes(8,'big'));digest.update(data)
    inputs.append({'path':rel,'sha256':sha(PUB/rel),'bytes':len(data)})

cache=(PUB/CACHE).read_text()
header, sections=cache.split('----- stdout -----\n',1)
cache_stdout, cache_stderr=sections.split('\n----- stderr -----\n',1)
fields=dict(line.split(': ',1) for line in header.splitlines()[1:])
assert fields['runner']==RUNNER==execution['runner']
assert fields['runner_sha256']==sha(PUB/RUNNER)
assert fields['input_fingerprint_sha256']==digest.hexdigest()
assert fields['exit_code']=='0' and fields['status']=='ok'
assert fields['timeout_sec']=='120'
assert fields['elapsed_sec']==f"{execution['elapsed_sec']:.2f}"
assert execution['status']=='ok' and execution['exit_code']==0 and execution['stderr']==''
assert execution['elapsed_sec']==0.23541903495788574==root_report['primary_seconds']
assert cache_stdout==execution['stdout']
assert cache_stderr==execution['stderr']+'\n'
assert execution['stdout']==(PUB/RESULT).read_text()+'TOTAL_PASS: 3\n'
combined=load(PUB/RESULT)
assert combined['all_assertions_passed'] is True
assert combined['source_sha256']==sha(PUB/RUNNER)

author_info=[
    ('volume','volume_checks','finite-volume-observation-personal','finite_volume_units.py','FINITE_VOLUME_UNITS.json','out'),
    ('band','band_checks','optical-band-response-personal','optical_band_controls.py','OPTICAL_BAND_RESULTS.json','result'),
    ('experiment','experiment_checks','optical-experiment-scope-personal','experiment_units.py','EXPERIMENT_UNITS.json','out'),
]
source_bindings=[]
ast_checks=[]
payload_checks=[]
leaf_counts={'float':0,'int':0,'bool':0,'str':0,'null':0}


def count_leaves(value):
    if isinstance(value,dict):
        for v in value.values():count_leaves(v)
    elif isinstance(value,list):
        for v in value:count_leaves(v)
    else:
        key='null' if value is None else type(value).__name__
        leaf_counts[key]+=1


for group, wrapper, folder, filename, resultfile, outputname in author_info:
    source=HERE/'post_sources'/folder/filename
    author_tree=ast.parse(source.read_text())
    source_bindings.append((folder+'/'+filename,sha(source)))
    start=next(i for i,n in enumerate(author_tree.body) if target(n,'start'))
    finish=next(i for i,n in enumerate(author_tree.body) if target(n,outputname))
    original_nodes=author_tree.body[start:finish+1]
    body=functions[wrapper].body
    assert isinstance(body[-1],ast.Return)
    assert isinstance(body[-1].value,ast.Name) and body[-1].value.id==outputname
    assert dump(body[:-1])==dump(original_nodes), wrapper
    ast_checks.append({'wrapper':wrapper,'complete_arithmetic_statement_count':len(original_nodes),'arithmetic_AST_exact':True,'only_final_serialization_replaced_with_return':True})
    author_data=load(HERE/'post_sources'/folder/resultfile)
    public_data=copy.deepcopy(combined[group])
    assert public_data['source_sha256']==sha(PUB/RUNNER)
    for data in [author_data,public_data]:
        del data['source_sha256'];del data['elapsed_seconds']
    renamed=0
    if group=='band':
        for volume in public_data['lattice_rows']:
            for band in volume['rows']:
                assert 'max_eta' not in band
                band['max_eta']=band.pop('projected_weight_fraction');renamed+=1
    assert public_data==author_data, group
    count_leaves(public_data)
    payload_checks.append({'group':group,'all_nonruntime_nonsource_payload_exact':True,'declared_key_renames':renamed})
assert literal['ROOT_CONTROL_SOURCES']==source_bindings

author_control=next(n for n in ast.parse((HERE/'post_sources/optical-band-response-personal/optical_band_controls.py').read_text()).body
                    if isinstance(n,ast.FunctionDef) and n.name=='control')
rename_count=0
for node in ast.walk(author_control):
    if isinstance(node,ast.Constant) and node.value=='max_eta':
        node.value='projected_weight_fraction';rename_count+=1
assert rename_count==1
assert ast.dump(author_control,include_attributes=False)==ast.dump(functions['control'],include_attributes=False)

note=(PUB/NOTE).read_text()
partA=note.split('## A. Finite-volume reference energy and conditional optical scale\n',1)[1].split('\n## B.',1)[0]
rootA=(HERE/'post_sources/finite-volume-observation-personal/FINITE_VOLUME_OPTICAL_SCALE_DIAGNOSTIC_ROOT.md').read_text()
rootA='Use exactly'+rootA.split('Use exactly',1)[1].split('\nCheck required before promotion:',1)[0]
rootA=rootA.replace('omega_min(L)=(2c/a) sin(pi/L), L>=4.','omega_min(L)=(2c/a) sin(pi/L), even L>=6 in this construction.')
assert normalize_space(partA)==normalize_space(rootA)

partB=note.split('## B. Spectral overlap and the original count contrast\n',1)[1].split('\n## C.',1)[0]
rootB=(HERE/'post_sources/optical-band-response-personal/OPTICAL_BAND_ORIGINAL_PROBE_RESPONSE_ROOT.md').read_text()
rootB='## 1. Sources and scope'+rootB.split('## 1. Sources and scope',1)[1]
rootB=re.sub(r'^## ', '### ', rootB, flags=re.M)
rootB=rootB.replace('Independent reconstruction is required before publication promotion.','The separate sealed independent PRE and released comparison provide the stated scoped reconstruction; the review packet records their exact sources and limits.')
assert normalize_space(partB)==normalize_space(rootB)

partC=note.split('## C. Comparison scope for a primary optical experiment\n',1)[1].split('\n## D.',1)[0]
rootC=(HERE/'post_sources/optical-experiment-scope-personal/OPTICAL_EXPERIMENT_COMPARISON_SCOPE_ROOT.md').read_text()
rootC='## Primary evidence and what its numbers mean'+rootC.split('## Primary evidence and what its numbers mean',1)[1]
rootC=re.sub(r'^## ', '### ', rootC, flags=re.M)
rootC=rootC.replace('Its signal/background parameter0.34 corrects','Its signal fraction rho=S/(S+B)=0.34 corrects')
rootC=rootC.replace('In the separately sealed original-local-probe candidate,','In Part B’s original-local-probe result,')
rootC=rootC.replace('Thus neither the measured efficiency nor','Thus neither the quoted detector-efficiency estimate nor')
assert normalize_space(partC)==normalize_space(rootC)

assert '**Type:** bounded_theorem' in note
assert '**Status:** conditional mathematical result; no retained audit verdict.' in note
assert 'claim_type: bounded_theorem' in note
assert 'max_eta' not in (PUB/RUNNER).read_text()
unavailable=[{'L':v['L'],'epsilon':b['epsilon'],'projected_weight_fraction':b['projected_weight_fraction']}
             for v in combined['band']['lattice_rows'] for b in v['rows'] if not b['normalized_band_packet_available']]
assert len(unavailable)==11 and all(row['projected_weight_fraction']==0 for row in unavailable)

report={
    'completed_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Final publication correspondence, not new scientific derivation or primary execution.',
    'verifier_sha256':sha(Path(__file__)),
    'PRE_and_POST_member_counts_unchanged':[len(load(HERE/'PRE_SEAL.json')['members']),len(load(HERE/'POST_SEAL.json')['members'])],
    'publication_source_origins_and_snapshots_verified':len(pins['sources']),
    'declared_input_paths':inputs,'computed_input_fingerprint_sha256':digest.hexdigest(),
    'runner_sha256':sha(PUB/RUNNER),'note_sha256':sha(PUB/NOTE),'result_sha256':sha(PUB/RESULT),'cache_sha256':sha(PUB/CACHE),
    'primary_receipt_seconds':execution['elapsed_sec'],'cache_rounded_seconds':fields['elapsed_sec'],
    'complete_stdout_result_and_cache_identity':True,'complete_empty_stderr_correspondence':True,
    'three_wrapper_AST_checks':ast_checks,'control_AST_exact_after_one_declared_key_rename':True,
    'complete_scientific_payload_comparisons':payload_checks,'compared_payload_leaf_counts':leaf_counts,
    'eleven_empty_band_field_repairs':unavailable,
    'note_part_A_exact_after_even_L_scope_and_removed_prepublication_check_paragraph':True,
    'note_part_B_exact_after_heading_and_evidence_status_changes':True,
    'note_part_C_exact_after_headings_crossreference_and_two_wording_repairs':True,
    'front_and_part_D_read_completely_for_scope_and_attribution':True,
    'primary_or_author_runner_executions_or_imports':0,
    'canonical_cache_rewrites_or_restamps':0,
    'new_physics_claim_or_audit_verdict':False,
    'limitations':['Inherited premises and archival timing identification remain conditional.',
                   'Static estimates do not supply full charged spectra, simultaneous large-volume dynamics or finite laboratory-time accuracy.',
                   'No empirical source/detector/count identification or exclusion; primary paper not newly refit or rerun.'],
}
output=json.dumps(report,indent=2,allow_nan=False)+'\n'
(HERE/'PUBLICATION_VERIFICATION_REPORT.json').write_text(output)
print(output,end='')
