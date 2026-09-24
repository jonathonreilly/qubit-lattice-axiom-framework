"""Final A/B public correspondence after the front precision edit; no rerun.

Section C and unit_control are outside the scientific review. Their bytes are
bound only as part of the shared public source/result/cache. No private unit
bridge root or independent packet is opened.
"""
from pathlib import Path
from hashlib import sha256
import ast
import copy
import difflib
import json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PUB=BASE/'probe-physical-limits-publication'
NOTE='docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER='scripts/prepared_original_record_probe_energy_and_observation_limits_2026_09_24.py'
RESULT='outputs/prepared_probe_physical_limits_20260924/PROBE_PHYSICAL_LIMITS_RESULTS.json'
CACHE='logs/runner-cache/prepared_original_record_probe_energy_and_observation_limits_2026_09_24.txt'
EXPECTED={NOTE:'2dd49ffa004fa09726b2388decb7c4a36dd69f2cdaf5f3bbb8ffe3e829a47c6d',
          RUNNER:'9e67aa1bdc1d9fa2227a934d219495c672aa299f9210cfdd0caed07143061676',
          RESULT:'790a2a72d86f4ecf72395c400ee93ba981e854a1a19a7d25d1adc15d79692e7e'}


def digest(data):return sha256(data).hexdigest()


def snapshot(origin,relative,expected=None):
    data=origin.read_bytes();identity=digest(data)
    if expected:assert identity==expected,(str(origin),identity,expected)
    target=HERE/'publication_final_sources'/relative
    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    return {'origin':str(origin),'copy':str(target.relative_to(HERE)),
            'sha256':identity,'bytes':len(data)}


def function(source,name):
    return copy.deepcopy(next(n for n in ast.parse(source).body
                              if isinstance(n,ast.FunctionDef)and n.name==name))


def main():
    for name,identity in [('PRE_SEAL.json','c6686cc03d195af4487e3df90cd64e152869c608d5170cd70c5dd81f544b9fdc'),
                          ('POST_SEAL.json','60736b57d4e82d4803bae3f1b260fd00f330c277010eda990089034f81762217')]:
        data=(HERE/name).read_bytes();assert digest(data)==identity
        seal=json.loads(data)
        for member in seal['members']:
            content=(HERE/member['path']).read_bytes()
            assert digest(content)==member['sha256']and len(content)==member['bytes']
    source=(PUB/RUNNER).read_text();tree=ast.parse(source)
    declaration=next(n.value for n in tree.body if isinstance(n,ast.Assign)
                     and any(isinstance(t,ast.Name)and t.id=='AUDIT_INPUT_PATHS'for t in n.targets))
    inputs=ast.literal_eval(declaration)
    assert len(inputs)==len(set(inputs))==7
    frozen_path=BASE/'PROBE_PHYSICAL_LIMITS_PUBLICATION_FROZEN_SOURCES.json'
    execution_path=BASE/'PROBE_PHYSICAL_LIMITS_PUBLICATION_CACHE_EXECUTION.json'
    frozen=json.loads(frozen_path.read_text());execution=json.loads(execution_path.read_text())
    records=[];fingerprint=sha256();fingerprint.update(b'runner-cache-input-fingerprint-v1\0')
    for relative in inputs:
        assert not Path(relative).is_absolute()and '..'not in Path(relative).parts
        data=(PUB/relative).read_bytes()
        assert digest(data)==frozen['files_sha256'][relative]
        name_bytes=relative.encode('utf-8')
        fingerprint.update(len(name_bytes).to_bytes(8,'big'));fingerprint.update(name_bytes)
        fingerprint.update(len(data).to_bytes(8,'big'));fingerprint.update(data)
        records.append(snapshot(PUB/relative,'repo/'+relative,frozen['files_sha256'][relative]))
    assert frozen['files_sha256'][RUNNER]==EXPECTED[RUNNER]
    for relative in [RUNNER,RESULT,CACHE,'scripts/runner_cache.py',
                     'outputs/prepared_probe_physical_limits_20260924/FLAT_ACTION_SIDE_6.json',
                     'outputs/prepared_probe_physical_limits_20260924/FLAT_ACTION_SIDE_16.json']:
        records.append(snapshot(PUB/relative,'repo/'+relative,EXPECTED.get(relative)))
    assert digest((PUB/NOTE).read_bytes())==EXPECTED[NOTE]
    records.append(snapshot(frozen_path,'external/'+frozen_path.name))
    records.append(snapshot(execution_path,'external/'+execution_path.name))
    cache=(PUB/CACHE).read_text()
    header,body=cache.split('----- stdout -----\n',1)
    stdout,stderr=body.split('\n----- stderr -----\n',1)
    fields=dict(line.split(': ',1)for line in header.splitlines()if': 'in line)
    assert fields['runner']==RUNNER and fields['runner_sha256']==EXPECTED[RUNNER]
    assert fields['input_fingerprint_sha256']==fingerprint.hexdigest()
    assert fields['status']=='ok'and fields['exit_code']=='0'and stderr=='\n'
    actual=execution['result']
    assert actual['runner']==RUNNER and actual['exit_code']==0 and actual['status']=='ok'
    assert actual['stderr']==''and actual['stdout']==stdout
    assert actual['elapsed_sec']==2.2022247314453125
    assert fields['elapsed_sec']==f"{actual['elapsed_sec']:.2f}"
    result_text=(PUB/RESULT).read_text()
    assert stdout==result_text+'TOTAL_PASS: 3\n'
    result=json.loads(result_text)
    assert result['source_sha256']==EXPECTED[RUNNER]and result['all_assertions_passed']is True
    droot=HERE/'post_sources/prepared-probe-dynamics-personal'
    oroot=HERE/'post_sources/prepared-probe-output-energy-personal'
    dyn=json.loads((droot/'FLAT_MATTER_RESULTS.json').read_text())
    out=json.loads((oroot/'OUTPUT_ENERGY_RESULTS.json').read_text())
    assert result['input_rows']==dyn['rows']
    assert result['output_rows']==out['rows']
    certs=[]
    for row in result['input_rows']:
        name=f"FLAT_ACTION_SIDE_{row['side']}.json"
        public_data=(PUB/Path(RESULT).parent/name).read_bytes()
        assert public_data==(droot/name).read_bytes()
        assert digest(public_data)==row['action_certificate_sha256']
        certs.append({'side':row['side'],'sha256':digest(public_data),'bytes':len(public_data),
                      'exactly_equal_POST_checked_certificate':True})
    original_input=function((droot/'flat_matter_controls.py').read_text(),'control')
    public_input=function(source,'input_control');public_input.name='control'
    path_adaptations=[]
    for label,node in [('root',original_input),('public',public_input)]:
        matches=[n for n in node.body if isinstance(n,ast.Assign)
                 and any(isinstance(t,ast.Name)and t.id=='path'for t in n.targets)]
        assert len(matches)==1
        path_adaptations.append({'source':label,'statement':ast.unparse(matches[0])})
        matches[0].value=ast.Constant('certificate destination only')
    assert ast.dump(original_input,include_attributes=False)==ast.dump(public_input,include_attributes=False)
    original_output=function((oroot/'output_energy_controls.py').read_text(),'control')
    public_output=function(source,'output_control');public_output.name='control'
    assert ast.dump(original_output,include_attributes=False)==ast.dump(public_output,include_attributes=False)
    text=(PUB/NOTE).read_text()
    a=text[text.index('### 1.',text.index('## A.')):text.index('## B.')].strip()+'\n'
    b=text[text.index('### 1.',text.index('## B.')):text.index('## C.')].strip()+'\n'
    a=a.replace('### ','## ');b=b.replace('### ','## ')
    original_a=(droot/'PREPARED_PROBE_ENERGY_AND_FINITE_SCALE_WINDOW_ROOT.md').read_text()
    original_a=original_a[original_a.index('## 1.'):].strip()+'\n'
    original_b=(oroot/'SELECTED_PROBE_OUTPUT_ENERGY_ROOT.md').read_text()
    original_b=original_b[original_b.index('## 1.'):].strip()+'\n'
    for label,old,new in [('A',original_a,a),('B',original_b,b)]:
        diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
                    fromfile='frozen_root_'+label,tofile='public_'+label))
        (HERE/f'FINAL_PUBLICATION_{label}_CORRESPONDENCE.diff').write_text(diff)
    assert 'microscopic spin limit at each fixed time mesh, followed by mesh refinement.'in a
    assert 'The weighted output norm itself has relative O(g²) corrections' in b
    assert 'cutoff-induced normalization errors are exponentially' in b
    assert 'the earlier superposed-input Hermiticity and dark-mark assertions are omitted' in b
    old_note=(HERE/'publication_sources/repo'/NOTE).read_text()
    assert old_note.replace('In the controlled small-background window,',
                            "In Part C's regime b=o(tau g³),")==text
    old_result=json.loads((HERE/'publication_sources/repo'/RESULT).read_text())
    new_payload=dict(result);old_payload=dict(old_result)
    new_payload.pop('elapsed_seconds');old_payload.pop('elapsed_seconds')
    assert new_payload==old_payload
    assert digest((PUB/CACHE).read_bytes())=='a13f49a4bc999f280335dd0351f44a483a80d632d1d94db734d5d0870b6e9cb6'
    assert digest(frozen_path.read_bytes())=='9c2fa71f055ceecaa9bb3a3ef6929c9be3772f8bd7a10a2e83480c8641217c69'
    verification_path=BASE/'PROBE_PHYSICAL_LIMITS_PRIMARY_ROOT_VERIFICATION.json'
    verification=json.loads(verification_path.read_text())
    for relative,identity in verification['files_sha256'].items():
        assert digest((PUB/relative).read_bytes())==identity
    assert verification['primary_seconds']==actual['elapsed_sec']
    assert verification['exit_code']==0 and verification['stderr_bytes']==0
    records.append(snapshot(verification_path,'external/'+verification_path.name))
    pins={'scope':'Byte identities for narrow public A/B/context comparison. Section C, unit_control and unit_rows are outside the scientific review; their bytes participate only in the shared source/cache binding. Extra declared public parents were hashed for the fingerprint without reopening their scientific claims.',
          'records':records,'input_fingerprint_sha256':fingerprint.hexdigest(),
          'checker_sha256':digest(Path(__file__).read_bytes())}
    (HERE/'FINAL_PUBLICATION_SOURCE_PINS.json').write_text(json.dumps(pins,indent=2)+'\n')
    report={'scope':__doc__,'PRE_and_POST_members_verified_unchanged':[42,25],
            'note_sha256':EXPECTED[NOTE],'runner_sha256':EXPECTED[RUNNER],
            'result_sha256':EXPECTED[RESULT],'cache_sha256':digest((PUB/CACHE).read_bytes()),
            'declared_inputs':list(inputs),'input_fingerprint_sha256':fingerprint.hexdigest(),
            'snapshot_count':len(records),'canonical_primary_elapsed_seconds':actual['elapsed_sec'],
            'canonical_internal_elapsed_seconds':result['elapsed_seconds'],
            'source_fingerprint_result_stdout_cache_execution_all_match':True,
            'public_input_rows_exactly_match_root_rows':True,
            'public_output_rows_exactly_match_root_rows':True,
            'input_AST_equal_except_name_and_disclosed_path':True,
            'output_AST_equal_except_name':True,'input_path_adaptation':path_adaptations,
            'certificates':certs,'two_public_wording_corrections_present':True,
            'assertion_reuse_qualification_present':True,
            'review_exclusions':['Section C scientific argument','unit_control scientific arithmetic','unit_rows scientific interpretation','private observation-unit-bridge root/checker packets'],
            'final_note_diff_is_only_the_disclosed_front_phrase':True,'all_public_result_fields_identical_except_elapsed_seconds':True,'no_primary_or_author_execution':True,'checker_sha256':digest(Path(__file__).read_bytes())}
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
