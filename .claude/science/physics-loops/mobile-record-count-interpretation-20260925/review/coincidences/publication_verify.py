"""Read-only public-source, provenance, payload and cache correspondence.

Writes evidence only beside this verifier. Parses but never imports or runs
the public runner, author programs or repository cache implementation.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import ast
import difflib
import hashlib
import json
import shutil


HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PUBLIC=BASE/'count-interpretation-publication'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text())


def verify_seal(directory,name):
    seal=read(directory/name)
    for row in seal['members']:
        q=directory/row['path']
        assert sha(q)==row['sha256'] and q.stat().st_size==row['bytes']
    return len(seal['members'])


def verify_author(directory):
    seal=read(directory/'AUTHOR_SEAL.json')
    for name,row in seal['files'].items():
        q=directory/name
        assert sha(q)==row['sha256'] and q.stat().st_size==row['bytes']
    return seal


def literal_assignments(source):
    found={}
    for node in ast.parse(source).body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name):
                    try:found[target.id]=ast.literal_eval(node.value)
                    except (ValueError,TypeError):pass
    return found


def main():
    manifest_path=BASE/'COUNT_INTERPRETATION_PUBLICATION_FROZEN_SOURCES.json'
    frozen=read(manifest_path)
    for rel,expected in frozen['files_sha256'].items():assert sha(PUBLIC/rel)==expected
    assert sha(PUBLIC/frozen['note'])=='ce5fb4cb9e4196cfa4c1261c1e7d96e13671acc75a98fceacd07df75e57a4109'
    assert sha(PUBLIC/frozen['runner'])=='acb60f75ae0bc45c054c5867402ab6e9a2b98b322918b05bcfc64f43d1733523'
    assert sha(PUBLIC/frozen['result'])=='3ef652ef3ab22f246bab51d91c091ff4d46c703c9d76fdf3b868dc5d5750f8a8'
    assert sha(Path(frozen['primary_execution']['path']))==frozen['primary_execution']['sha256']
    old_counts={
        'PRE31':verify_seal(HERE,'PRE_SEAL.json'),
        'POST31':verify_seal(HERE,'POST_SEAL.json'),
        'PRE32':verify_seal(BASE/'number-offset-observation-independent','PRE_SEAL.json'),
        'POST32':verify_seal(BASE/'number-offset-observation-independent','POST_SEAL.json'),
        'POST32_chronology':verify_seal(BASE/'number-offset-observation-independent','POST_CHRONOLOGY_ADDENDUM_SEAL.json')}
    chronology=read(BASE/'number-offset-observation-independent/POST_CHRONOLOGY_ADDENDUM_SEAL.json')
    for row in chronology['sources']:
        q=Path(row['path']);assert sha(q)==row['sha256'] and q.stat().st_size==row['bytes']

    a31=BASE/'two-detector-coincidence-personal'
    a32=BASE/'number-offset-observation-personal'
    seals=[verify_author(a31),verify_author(a32)]
    for path,expected in [
        (a31/'AUTHOR_SEAL.json','effb2dc3b41f9e7c3cb8bc1b2b363fc86299feb3c38a752b4db4fec4a33c04cb'),
        (a32/'AUTHOR_SEAL.json','912d4bc7e1285d7001eabdcb1d0a2261c5c51b9be82f0e7555a791e476edd8b7'),
        (a31/'AUTHOR_SCOPE_ADDENDUM_SEAL.json','8b2a7452d211da8ec198891806971a528ebaca89201d1aca9d2919f3774f1a1c'),
        (BASE/'TWO_DETECTOR_TRANSLATION_QUALIFICATION.md','b09cbbe9bf4a83be75d18b087b24055fd617224ef15d432393ad8917ba26bc6e'),
        (BASE/'NUMBER_OFFSET_WEAK_FIELD_APPLICATION_SCOPE.md','d70c0b5fe16dc48fb5dee6a1695ecbad0e6c9f92b082c09825aa47148a0b22aa')]:
        assert sha(path)==expected
    root32=read(a32/'NUMBER_OFFSET_RESULTS.json')
    assert (a32/'CONTROL.stdout').read_bytes()==(a32/'NUMBER_OFFSET_RESULTS.json').read_bytes()
    assert (a32/'CONTROL.stderr').read_bytes()==b''
    r32=read(a32/'EXECUTION.json')
    assert r32['script_sha256']==sha(a32/'number_offset_controls.py')==root32['source_sha256']
    assert r32['stdout_sha256']==sha(a32/'CONTROL.stdout') and r32['exit_code']==0

    runner=PUBLIC/frozen['runner']
    literals=literal_assignments(runner.read_text())
    inputs=literals['AUDIT_INPUT_PATHS']
    assert len(inputs)==11 and len(set(inputs))==11
    assert tuple(inputs)==tuple([frozen['note']]+frozen['parent_paths']+frozen['runtime'])
    assert literals['AUDIT_TIMEOUT_SEC']==120
    assert literals['RESULT_PATH']==frozen['result'] and literals['RUNTIME']==frozen['runtime']
    fingerprint=hashlib.sha256();fingerprint.update(b'runner-cache-input-fingerprint-v1\0')
    input_rows=[]
    for rel in inputs:
        q=PUBLIC/rel
        assert q.is_file() and not q.is_symlink() and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        body=q.read_bytes();name=rel.encode()
        fingerprint.update(len(name).to_bytes(8,'big'));fingerprint.update(name)
        fingerprint.update(len(body).to_bytes(8,'big'));fingerprint.update(body)
        input_rows.append({'path':rel,'sha256':sha(q),'bytes':len(body)})
    identity=fingerprint.hexdigest()
    assert identity=='2dab98db60f0dd4213388f0267696b7d064681e8388f4442af25291d9fc3b145'

    exact_programs=[]
    for item in frozen['origins']:
        origin=Path(item['origin']);copy=PUBLIC/item['publication']
        assert sha(origin)==sha(copy)==item['sha256']
        source=origin.read_text();public_source=copy.read_text()
        assert ast.dump(ast.parse(source),include_attributes=False)==ast.dump(ast.parse(public_source),include_attributes=False)
        exact_programs.append({'origin':str(origin),'publication':item['publication'],'sha256':sha(copy),
                               'exact_bytes':True,'exact_AST':True,'function_definitions':sum(isinstance(n,ast.FunctionDef) for n in ast.walk(ast.parse(source)))})
    data=read(PUBLIC/frozen['result'])
    assert data['source_sha256']==sha(runner) and data['all_assertions_passed'] is True
    expected_names=['COINCIDENCE_RESULTS.json','NUMBER_OFFSET_RESULTS.json']
    assert list(data['payload'])==expected_names and len(data['stages'])==2
    old=[read(a31/expected_names[0]),root32]
    scalar_counts=Counter();differences=[];ignored=[]
    def compare(x,y,path):
        if path in [name+'/elapsed_seconds' for name in expected_names]:
            ignored.append({'path':path,'old':x,'fresh':y});return
        assert type(x) is type(y),(path,type(x).__name__,type(y).__name__)
        if isinstance(x,dict):
            assert list(x)==list(y),path
            for key in x:compare(x[key],y[key],path+'/'+key)
        elif isinstance(x,list):
            assert len(x)==len(y),path
            for index,(u,v) in enumerate(zip(x,y)):compare(u,v,path+'/'+str(index))
        else:
            scalar_counts[type(x).__name__]+=1
            if x!=y:differences.append({'path':path,'old':x,'fresh':y})
    stage_rows=[]
    for index,name in enumerate(expected_names):
        fresh=data['payload'][name];compare(old[index],fresh,name)
        stage=data['stages'][index]
        serialized=(json.dumps(fresh,indent=2,allow_nan=False)+'\n').encode()
        assert stage['stdout_sha256']==hashlib.sha256(serialized).hexdigest()
        assert stage['stdout_bytes']==len(serialized) and stage['stderr_bytes']==0 and stage['exit_code']==0
        assert stage['code_sha256']==exact_programs[index]['sha256']==fresh['source_sha256']
        assert stage['result']==name and stage['program']==Path(frozen['runtime'][index]).name
        stage_rows.append(dict(stage,full_serialized_child_stdout_verified=True))
        (HERE/f'PUBLICATION_CHILD_{index+1}_STDOUT.json').write_bytes(serialized)
    assert not differences,differences
    root_verification=read(BASE/'COUNT_INTERPRETATION_PRIMARY_ROOT_VERIFICATION.json')
    assert dict(scalar_counts)==root_verification['same_scientific_scalar_counts']
    assert [row['path'] for row in ignored]==root_verification['ignored_timing_only']

    execution_path=BASE/'COUNT_INTERPRETATION_PUBLICATION_CACHE_EXECUTION.json'
    execution=read(execution_path);result=execution['result']
    assert result['runner']==frozen['runner'] and result['exit_code']==0 and result['status']=='ok'
    assert result['stderr']=='' and result['timeout_sec']==120
    complete_stdout=(PUBLIC/frozen['result']).read_text()+'TOTAL_PASS: 2\n'
    assert result['stdout']==complete_stdout
    (HERE/'PUBLICATION_COMPLETE_PRIMARY_STDOUT.log').write_text(complete_stdout)
    cache=Path(execution['cache'])
    assert cache==PUBLIC/'logs/runner-cache/original_coincidences_and_number_energy_identifiability_2026_09_25.txt'
    stdout_tail=result['stdout'][-200_000:];stderr_tail=result['stderr'][-50_000:]
    expected_cache=(f'===== runner cache v1 =====\nrunner: {frozen["runner"]}\nrunner_sha256: {sha(runner)}\n'
                    f'input_fingerprint_sha256: {identity}\ntimeout_sec: 120\nexit_code: 0\n'
                    f'elapsed_sec: {result["elapsed_sec"]:.2f}\nstatus: ok\n----- stdout -----\n'
                    f'{stdout_tail}\n----- stderr -----\n{stderr_tail}\n')
    assert cache.read_text()==expected_cache
    assert stdout_tail==complete_stdout

    # Review views are exact JSON rows, not reexecuted numerical controls.
    offset=data['payload']['NUMBER_OFFSET_RESULTS.json']
    for start in range(0,108,36):
        (HERE/f'PUBLICATION_NUMBER_COUNT_ROWS_{start:03d}.jsonl').write_text(''.join(json.dumps({'index':i,**row},separators=(',',':'))+'\n' for i,row in enumerate(offset['count_rows']) if start<=i<start+36))
    for key in ['power_rows','same_sector_rows','history_rows']:
        (HERE/f'PUBLICATION_NUMBER_{key.upper()}.jsonl').write_text(''.join(json.dumps({'index':i,**row},separators=(',',':'))+'\n' for i,row in enumerate(offset[key])))
    assert len(offset['count_rows'])==108 and len(offset['power_rows'])==24 and len(offset['same_sector_rows'])==4 and len(offset['history_rows'])==36
    count_error=max(abs(complex(*row['reference'])-complex(*row['altered'])) for row in offset['count_rows'])
    power_error=max(abs((row['altered_power']-row['original_power'])-row['predicted_shift']) for row in offset['power_rows'])
    diagonal_error=max(row['diagonal_block_difference'] for row in offset['history_rows'])
    coherent_difference=max(row['full_conditional_unnormalized_state_difference'] for row in offset['history_rows'] if row['input']==2)
    assert count_error<2e-12 and power_error<1e-12 and diagonal_error<1e-12 and coherent_difference>.1

    # Preserve complete public-to-author argument differences for review.
    text=(PUBLIC/frozen['note']).read_text()
    a=text.split('## A. Two original-mark coincidences\n',1)[1].split('## B. What counts identify about number-sector energy\n',1)[0]
    b=text.split('## B. What counts identify about number-sector energy\n',1)[1].split('## C. Evidence, preserved corrections and scope\n',1)[0]
    for number,new,origin in [(31,a,a31/'TWO_ORIGINAL_DETECTOR_COINCIDENCES_ROOT.md'),(32,b,a32/'NUMBER_OFFSET_COUNT_IDENTIFIABILITY_ROOT.md')]:
        diff=''.join(difflib.unified_diff(origin.read_text().splitlines(keepends=True),new.splitlines(keepends=True),fromfile=f'sealed_root{number}',tofile=f'public_part_{number}'))
        (HERE/f'PUBLICATION_PART_{number}_DIFF.txt').write_text(diff)

    # New snapshots have explicit purpose. Earlier energy parents are hash-bound
    # declared inputs; their separate scientific arguments are not re-certified.
    origins=[]
    def add(origin,scope):
        if str(origin) not in {str(x[0]) for x in origins}:origins.append((origin,scope))
    for rel in frozen['files_sha256']:
        add(PUBLIC/rel,'Frozen public source/result/cache; parent notes bound as unchanged declared inputs, not a new transitive scientific audit.')
    add(PUBLIC/'scripts/runner_cache.py','Read cache fingerprint and serialization implementation only; no import or execution.')
    for name in ['COUNT_INTERPRETATION_PUBLICATION_FROZEN_SOURCES.json','COUNT_INTERPRETATION_PUBLICATION_CACHE_EXECUTION.json','COUNT_INTERPRETATION_PRIMARY_ROOT_VERIFICATION.json','TWO_DETECTOR_TRANSLATION_QUALIFICATION.md','NUMBER_OFFSET_WEAK_FIELD_APPLICATION_SCOPE.md']:
        add(BASE/name,'Explicitly authorized external source or execution/qualification record.')
    for directory,seal in [(a31,seals[0]),(a32,seals[1])]:
        for name in list(seal['files'])+['AUTHOR_SEAL.json']:add(directory/name,'Original released root history; program read as data only.')
    for name in ['AUTHOR_SCOPE_ADDENDUM_SEAL.json','SOURCE_METADATA_QUALIFICATION.md']:add(a31/name,'Existing unchanged root31 metadata qualification.')
    ind32=BASE/'number-offset-observation-independent'
    for name in ['PRE.md','PRE_SEAL.json','POST.md','POST_SEAL.json','POST_CHRONOLOGY_ADDENDUM.md','POST_CHRONOLOGY_ADDENDUM_SEAL.json','POST_CORRECTIONS.json','POST_BINDING_FAILURE_HISTORY.json','POST_BINDING_STDERR.txt','POST_BINDING_EXECUTION.json','POST_BINDING_STDOUT.json','POST_BINDING_ATTEMPT_02_EXECUTION.json','POST_BINDING_ATTEMPT_02_STDOUT.json','POST_BINDING_ATTEMPT_02_STDERR.txt','post_history/post_bind_and_check_attempt_01.py','post_bind_and_check.py']:
        add(ind32/name,'Previously sealed root32 independent history, now released for correspondence; no new claim of this reviewer blind reconstruction.')
    add(BASE/'photon-added-energy-independent/PUBLICATION_SCOPE_INCIDENT.json','The one specifically authorized earlier scope-incident record; no other source from that packet opened.')
    for name in ['PRE.md','PRE_SEAL.json','POST.md','POST_SEAL.json']:
        add(HERE/name,'Immutable own root31 PRE/POST anchor.')
    pins=[]
    for origin,scope in origins:
        if origin.parent==HERE:
            rel=None
        else:
            rel=Path('publication_sources')/origin.relative_to(BASE)
            target=HERE/rel;target.parent.mkdir(parents=True,exist_ok=True)
            assert not target.exists();shutil.copyfile(origin,target)
        pins.append({'origin':str(origin),'snapshot':str(rel) if rel else None,'sha256':sha(origin),'bytes':origin.stat().st_size,'scope':scope})
    manifest={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'Final released-source correspondence for public Parts A/B/C; no new blind PRE or dual full-independent-review claim.','sources':pins,'declared_inputs':input_rows,'author_or_primary_programs_imported_or_executed':0}
    (HERE/'PUBLICATION_SOURCE_PINS_INITIAL.json').write_text(json.dumps(manifest,indent=2)+'\n')
    report={'verified_utc':datetime.now(timezone.utc).isoformat(),'verifier_sha256':sha(Path(__file__)),
            'frozen_public_files_verified':len(frozen['files_sha256']),'new_source_and_anchor_origins':len(pins),
            'prior_seal_members_unchanged':old_counts,'exact_source_programs':exact_programs,
            'declared_inputs':len(inputs),'input_fingerprint_sha256':identity,
            'same_scientific_scalar_counts':dict(scalar_counts),'scientific_payload_differences':differences,
            'only_ignored_fields':ignored,'fresh_stages':stage_rows,
            'fresh_primary_elapsed_sec':result['elapsed_sec'],'fresh_primary_exit_code':0,'fresh_primary_stderr_bytes':0,
            'complete_primary_stdout_bytes':len(complete_stdout.encode()),'cache_contains_complete_stdout':True,
            'exact_cache_serialization_match':True,'primary_result_stdout_TOTAL_identity':True,
            'number_offset_stored_checks':{'count_rows':108,'power_rows':24,'same_sector_rows':4,'history_rows':36,
                                          'max_count_difference_recomputed':count_error,'max_power_difference_recomputed':power_error,
                                          'max_diagonal_block_difference_as_stored':diagonal_error,
                                          'max_coherent_state_difference_as_stored':coherent_difference},
            'author_or_primary_executions_by_checker':0,'new_matrix_Fourier_simulations':0,
            'limits':'Mechanical correspondence plus read mathematical review. Rerun payload identity is not independent scientific evidence, a full retained audit, a complete execution-history certificate, or an empirical test.'}
    output=json.dumps(report,indent=2)+'\n'
    (HERE/'PUBLICATION_VERIFICATION_REPORT.json').write_text(output)
    print(output,end='')


if __name__=='__main__':main()
