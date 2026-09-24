#!/usr/bin/env python3
"""Source/cache comparison only; never imports or executes the primary runner."""
import ast
import copy
import datetime
import difflib
import hashlib
import json
import stat
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PUB=ROOT.parent/'no-first-birth-publication'
S=ROOT/'PUBLICATION_sources'
NOTE='NO_FIRST_BIRTH_CUBE_ENERGY_AND_APPARATUS_COHERENCE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER='no_first_birth_cube_energy_and_apparatus_coherence_2026_09_24.py'
CACHE=RUNNER.replace('.py','.txt')
RUNNER_REL='scripts/'+RUNNER


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def functions(p):
    return {n.name:n for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef)}


def dump(n):
    return ast.dump(n,include_attributes=False)


def differences(a,b,path=''):
    if isinstance(a,dict) and isinstance(b,dict):
        assert a.keys()==b.keys(),path
        return sum((differences(a[k],b[k],path+'/'+k) for k in a),[])
    if isinstance(a,list) and isinstance(b,list):
        assert len(a)==len(b),path
        return sum((differences(x,y,path+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))),[])
    return [] if a==b else [{'path':path,'before':a,'after':b}]


def main():
    preserved=[]
    for name,want in [('PRE_SEAL.json','7b3a5de5ad3c2d1d47ad259333aa7ab90297d0108ebe36868306a72f8f4b1234'),
                      ('POST_SEAL.json','5b0b5634b6096a95ef0956424f48b15e6ae83f70cc210d553dc9c67ed959b218')]:
        assert sha(ROOT/name)==want
        seal=json.loads((ROOT/name).read_text())
        for row in seal['members']:
            p=ROOT/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
            assert p.stat().st_mode & 0o222==0
        preserved.append({'seal':name,'sha256':want,'unchanged_members':len(seal['members'])})

    freeze=json.loads((ROOT/'PUBLICATION_SOURCE_FREEZE.json').read_text())
    for row in freeze['sources']:
        assert sha(Path(row['source']))==sha(ROOT/row['snapshot'])==row['sha256']
    frozen=json.loads((S/'SEVENTH_PUBLICATION_FROZEN_SOURCES.json').read_text())
    assert frozen['base_revision']=='e846ee9d4133f65d3778fa4dc36524a9ada6db6b'
    for rel,want in frozen['files_sha256'].items(): assert sha(PUB/rel)==want

    pub_fn=functions(S/RUNNER)
    old_fn=functions(ROOT/'POST_sources/noevent_controls.py')
    helper_fn=functions(ROOT/'POST_sources/REUSED_ORDINARY_ENERGY_RUNNER.py')
    exact_helpers=['complete_spin_one','riesz_action','canonical_preparation']
    for name in exact_helpers: assert dump(pub_fn[name])==dump(helper_fn[name]),name
    exact_controls=['geometry_and_words','two_level_controls']
    for name in exact_controls: assert dump(pub_fn[name])==dump(old_fn[name]),name
    adapted=copy.deepcopy(old_fn['actual_spin_one_controls'])
    removed=adapted.body[:6]
    assert [type(n).__name__ for n in removed]==['Assign','Assign','Assert','Assign','Assign','Expr']
    assert isinstance(adapted.body[6],ast.Assign) and adapted.body[6].targets[0].id=='m'
    adapted.body=adapted.body[6:]
    helper_hash='4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d'
    class LocalCalls(ast.NodeTransformer):
        def visit_Attribute(self,node):
            if isinstance(node.value,ast.Name) and node.value.id=='mod':
                assert node.attr in exact_helpers
                return ast.copy_location(ast.Name(id=node.attr,ctx=node.ctx),node)
            return self.generic_visit(node)
        def visit_Name(self,node):
            if node.id=='want': return ast.copy_location(ast.Constant(value=helper_hash),node)
            return node
    adapted=LocalCalls().visit(adapted)
    assert dump(adapted)==dump(pub_fn['actual_spin_one_controls'])
    old_source=(ROOT/'POST_sources/noevent_controls.py').read_text().splitlines()
    new_source=(S/RUNNER).read_text().splitlines()
    code_diff=''.join(difflib.unified_diff([x+'\n' for x in old_source],[x+'\n' for x in new_source],
                       fromfile='sealed author control',tofile='publication self-contained runner'))
    (ROOT/'PUBLICATION_CODE_DIFF.txt').write_text(code_diff)

    pre=(ROOT/'PRE.md').read_text();note=(S/NOTE).read_text()
    pre_core=pre[pre.index('## 1. Domain'):pre.index('## 9. Independent controls')]
    note_core=note[note.index('## 1. Domain'):note.index('## 9. Computation')]
    core_diff=''.join(difflib.unified_diff(pre_core.splitlines(keepends=True),note_core.splitlines(keepends=True),
                                        fromfile='sealed PRE sections 1-8',tofile='publication sections 1-8'))
    (ROOT/'PUBLICATION_PROOF_DIFF.txt').write_text(core_diff)

    module=ast.parse((S/RUNNER).read_text())
    declaration=next(n for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets))
    inputs=ast.literal_eval(declaration.value); assert len(inputs)==5 and len(set(inputs))==5
    fp=hashlib.sha256();fp.update(b'runner-cache-input-fingerprint-v1\0');input_rows=[]
    existing_pins=json.loads((ROOT/'SOURCE_PINS.json').read_text())
    old_by_name={Path(r['source_path']).name:r for r in existing_pins['scientific_sources']}
    for rel in inputs:
        part=Path(rel);assert not part.is_absolute() and '..' not in part.parts and part.as_posix()==rel
        lexical=PUB
        for component in part.parts:
            lexical/=component;assert not stat.S_ISLNK(lexical.lstat().st_mode)
        p=PUB/rel;data=p.read_bytes();rel_bytes=rel.encode()
        fp.update(len(rel_bytes).to_bytes(8,'big'));fp.update(rel_bytes)
        fp.update(len(data).to_bytes(8,'big'));fp.update(data)
        digest=hashlib.sha256(data).hexdigest()
        if part.name==NOTE:
            snapshot='PUBLICATION_sources/'+NOTE;assert sha(S/NOTE)==digest
        else:
            prior=old_by_name[part.name];assert prior['sha256']==digest;snapshot=prior['snapshot']
        input_rows.append({'relative_path':rel,'source':str(p),'snapshot':snapshot,'bytes':len(data),'sha256':digest})

    api=PUB/'scripts/runner_cache.py';api_copy=S/'RUNNER_CACHE_API.py';api_copy.write_bytes(api.read_bytes());api_copy.chmod(0o444)
    execution=json.loads((S/'SEVENTH_PUBLICATION_CACHE_EXECUTION.json').read_text())
    result=execution['result'];assert result['runner']==RUNNER_REL and result['status']=='ok' and result['exit_code']==0
    assert result['timeout_sec']==300 and result['stderr']==''
    cache_expected=(
        '===== runner cache v1 =====\n'+f'runner: {RUNNER_REL}\n'+f'runner_sha256: {sha(S/RUNNER)}\n'
        +f'input_fingerprint_sha256: {fp.hexdigest()}\n'+f"timeout_sec: {result['timeout_sec']}\n"
        +f"exit_code: {result['exit_code']}\n"+f"elapsed_sec: {result['elapsed_sec']:.2f}\n"
        +f"status: {result['status']}\n"+'----- stdout -----\n'+result['stdout'][-200000:]+'\n'
        +'----- stderr -----\n'+result['stderr'][-50000:]+'\n')
    assert cache_expected.encode()==(S/CACHE).read_bytes()
    assert len(result['stdout'])<200000
    stdout=result['stdout'];decoder=json.JSONDecoder();position=0;objects=[];intervals=[]
    for i in range(4):
        while position<len(stdout) and stdout[position].isspace():position+=1
        start=position;obj,position=decoder.raw_decode(stdout,position);objects.append(obj);intervals.append([start,position])
    assert stdout[position:]=='\nTOTAL: PASS=3 FAIL=0\n'
    published=json.loads((S/'NOEVENT_CONTROL_RESULTS.json').read_text())
    assert objects[-1]==published and objects[:3]==published['actual_spin_one']['rows']
    assert (stdout[intervals[-1][0]:intervals[-1][1]]+'\n').encode()==(S/'NOEVENT_CONTROL_RESULTS.json').read_bytes()
    assert published['source_sha256']==sha(S/RUNNER)
    previous=json.loads((ROOT/'POST_sources/NOEVENT_CONTROL_RESULTS.json').read_text())
    result_diff=differences(previous,published)
    assert {r['path'] for r in result_diff}=={'/elapsed_seconds','/source_sha256',*(f'/actual_spin_one/rows/{i}/elapsed_seconds' for i in range(3))}

    toy=published['toy']['rows'][-1];actual=published['actual_spin_one']['rows'][-1]
    assert round(toy['scaled_conditional_variance'],6)==.232958 and round(toy['predicted_conditional_coefficient'],4)==.2352
    assert round(toy['scaled_weighted_Fisher'],6)==.341712 and round(toy['predicted_Fisher_coefficient'],6)==.343343
    assert round(actual['high_norms_over_predicted_powers'][0],5)==4.84729 and round(actual['expected_first_high_coefficient'],5)==4.84974
    assert round(actual['low_vector_error'],5)==3.03414 and round(actual['low_scaled_second_moment'],4)==32.0717
    assert round(actual['expected_low_coefficient'],2)==23.52
    assert max(r['decomposition_residual'] for r in published['actual_spin_one']['rows'])<3e-15
    independent=json.loads((ROOT/'INDEPENDENT_CONTROL_RESULTS.json').read_text())
    finest=[r for r in independent['two_band_control']['rows'] if r['epsilon']==.005]
    assert all(round(r['eps2_conditional_variance'],7)==.0431741 for r in finest)
    assert all(round(r['eps2_conditional_variance_target'],4)==.0432 for r in finest)

    check={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'scope':'Read-only publication source/control/cache correspondence; no primary rerun or audit verdict',
           'preserved_packets':preserved,'publication_sources':freeze['sources'],
           'exact_copied_helper_ASTs':exact_helpers,'exact_author_control_ASTs':exact_controls,
           'actual_spin_one_AST_adaptation':{'removed_import_prologue':[ast.unparse(n) for n in removed],
                 'other_changes':'mod helper calls become local calls; preserved builder provenance name becomes literal pinned SHA; normalized AST matches exactly'},
           'declared_inputs':input_rows,'input_fingerprint_sha256':fp.hexdigest(),
           'cache_API_source':{'source':str(api),'snapshot':str(api_copy.relative_to(ROOT)),'sha256':sha(api_copy),'bytes':api_copy.stat().st_size},
           'cache_reconstructed_byte_count':len(cache_expected.encode()),'cache_sha256':sha(S/CACHE),
           'execution':{'status':result['status'],'exit_code':result['exit_code'],'elapsed_seconds':result['elapsed_sec'],'timeout_seconds':result['timeout_sec'],
                        'stdout_bytes':len(stdout.encode()),'stderr_field_bytes':len(result['stderr'].encode()),'stream_note':'API merges process stderr into stdout; complete stream contains four JSON objects and TOTAL only'},
           'stdout_JSON_object_intervals':intervals,'stdout_JSON_object_count':len(objects),
           'result_sha256':sha(S/'NOEVENT_CONTROL_RESULTS.json'),'all_scientific_result_values_identical_to_sealed_author_control':True,
           'complete_result_differences':result_diff,'numeric_prose_checks':'All published rounded diagnostics match complete result and independent PRE result',
           'primary_execution_repeated':False}
    (ROOT/'PUBLICATION_EVIDENCE_CHECK.json').write_text(json.dumps(check,indent=2)+'\n')
    print(json.dumps(check,indent=2))


if __name__=='__main__':main()
