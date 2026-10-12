#!/usr/bin/env python3
"""Reviewer-owned identity, port, IO and rejection checks. No empirical inputs.

Author code is executed only for synthetic IO/aggregation fixtures and targeted
in-memory mutants. The unchanged complete scientific battery is not rerun.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import ast, contextlib, copy, hashlib, io, json, subprocess, sys, time
from pathlib import Path
from datetime import datetime, timezone

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
BASE='516cb69d8487ff04f8a48e065d3dcbe71d7dd237'
HEAD='68a7fa78907c2737e9f850679ba5a1c8db0df819'
PACK='.claude/science/physics-loops/local-vector-response-milestone-20261012'
RUNNER='scripts/local_vector_homogeneous_response_2026_10_12.py'
NOTE='docs/LOCAL_VECTOR_HOMOGENEOUS_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md'
OLD_ROOT=Path('/Users/jonBridger/.codex/worktrees/observations-to-toe-24h-20261012/New Axioms Lets Go')
OLD_REL='.claude/science/physics-loops/observations-to-toe-24h-20261012/gravity/solar_kernel_inversion/direct_vector_response_completion'
OLD=OLD_ROOT/OLD_REL

def sha(data): return hashlib.sha256(data).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def save(rel, data):
    path=HERE/rel
    path.parent.mkdir(parents=True,exist_ok=True)
    if isinstance(data,str): data=data.encode()
    if path.exists():
        assert path.read_bytes()==data, f'immutable evidence collision: {rel}'
    else:
        with path.open('xb') as f: f.write(data)
    return {'path':rel,'sha256':sha(data),'bytes':len(data)}
def save_json(rel,obj): return save(rel,json.dumps(obj,indent=2,sort_keys=True)+'\n')
def load_author(source):
    namespace={'__file__':str(ROOT/RUNNER),'__name__':'review_fixture_only'}
    exec(compile(source,str(ROOT/RUNNER),'exec'),namespace)
    return namespace
def invoke_fixture(namespace, args=()):
    previous=sys.argv[:]; old_cwd=Path.cwd(); capture=io.StringIO()
    try:
        sys.argv=[RUNNER,*args]; os.chdir(HERE)
        with contextlib.redirect_stdout(capture): namespace['main']()
    finally:
        sys.argv=previous; os.chdir(old_cwd)
    return capture.getvalue()

def main():
    started=time.monotonic()
    assert git('rev-parse','HEAD').decode().strip()==HEAD
    assert git('merge-base',BASE,HEAD).decode().strip()==BASE
    paths=git('diff','--name-only','--no-renames',BASE,HEAD).decode().splitlines()
    assert len(paths)==11
    inventories=[]
    for rel in paths:
        original=git('show',f'{HEAD}:{rel}')
        assert (ROOT/rel).read_bytes()==original
        tree=git('ls-tree',HEAD,'--',rel).decode().strip().split(None,3)
        snap=save('snapshots/canonical/'+rel+'.snapshot',original)
        inventories.append({'path':rel,'sha256':sha(original),'bytes':len(original),
                            'mode':tree[0],'git_blob':tree[2],
                            'base_state':'absent','snapshot':snap['path']})
    save('original_delta.patch',git('diff','--binary','--full-index','--no-renames',BASE,HEAD))
    campaign=[]
    for rel in ['PROTOCOL.md','DIRECT_VECTOR_COMPLETION.md','direct_vector_check.py','evidence_v1/RESULTS.json',
                'independent_review/VECTOR_COMPLETION_REVIEW.md',
                'independent_review/check_vector_independent.py',
                'independent_review/check_vector_mutations.py',
                'independent_review/independent_vector_checks_v1.json',
                'independent_review/independent_mutations_v1.json',
                'independent_review/final_review_receipt_v1.json',
                'independent_review/snapshot_manifest_v1.json']:
        data=(OLD/rel).read_bytes()
        snap=save('snapshots/campaign/'+rel+'.snapshot',data)
        campaign.append({'original_path':OLD_REL+'/'+rel,'sha256':sha(data),'snapshot':snap['path']})
    context_rel='.claude/science/physics-loops/observations-to-toe-24h-20261012/gravity/solar_kernel_inversion/direct_constrained_dynamics/DIRECT_DYNAMICS.md'
    context_data=(OLD_ROOT/context_rel).read_bytes()
    context_snap=save('snapshots/campaign/prior_DIRECT_DYNAMICS.md.snapshot',context_data)
    campaign.append({'original_path':context_rel,'sha256':sha(context_data),'snapshot':context_snap['path']})
    save_json('source_manifest_v1.json',{'base':BASE,'head':HEAD,
        'tree':git('rev-parse',HEAD+'^{tree}').decode().strip(),
        'canonical':inventories,'campaign_context':campaign})

    source=(ROOT/RUNNER).read_text()
    old_source=(OLD/'direct_vector_check.py').read_text()
    def functions(source):
        return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source).body if isinstance(n,ast.FunctionDef)}
    current_ast,old_ast=functions(source),functions(old_source)
    bodies={name:{'identical':current_ast[name]==old_ast[name],
                  'ast_sha256':sha(current_ast[name].encode())}
            for name in ['symbolic','real_green_fourier','numeric']}
    assert all(x['identical'] for x in bodies.values())
    recorded=json.loads((ROOT/PACK/'evidence/SCIENTIFIC_RESULT_v1.json').read_text())
    prior=json.loads((OLD/'evidence_v1/RESULTS.json').read_text())
    assert recorded['symbolic']==prior['symbolic'] and recorded['numerical']==prior['numerical']
    assert recorded['checks_passed']==10 and recorded['checks_failed']==0
    assert len(recorded['check_families'])==10 and all(recorded['check_families'].values())
    for rel,digest in recorded['identities'].items(): assert sha((ROOT/rel).read_bytes())==digest
    rows=recorded['numerical']['real_to_Fourier_rows']
    assert len(rows)==64
    assert max(abs(r['real_integral']-r['spectral']) for r in rows)==recorded['numerical']['max_transform_error']
    assert all(abs(r['real_integral']-r['spectral'])==r['absolute_error'] for r in rows)
    fingerprint=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    note_bytes=(ROOT/NOTE).read_bytes(); path_bytes=NOTE.encode()
    fingerprint.update(len(path_bytes).to_bytes(8,'big')); fingerprint.update(path_bytes)
    fingerprint.update(len(note_bytes).to_bytes(8,'big')); fingerprint.update(note_bytes)
    cache=(ROOT/'logs/runner-cache/local_vector_homogeneous_response_2026_10_12.txt').read_text()
    cache_header=dict(line.split(': ',1) for line in cache.split('----- stdout -----')[0].splitlines() if ': ' in line)
    assert cache_header['runner_sha256']==sha(source.encode())
    assert cache_header['input_fingerprint_sha256']==fingerprint.hexdigest()
    assert cache_header['timeout_sec']=='60' and cache_header['status']=='ok' and cache_header['exit_code']=='0'
    raw=json.loads((ROOT/PACK/'evidence/RUN_RAW_v1.json').read_text())
    assert raw['status']=='ok' and raw['exit_code']==0 and raw['timeout_sec']==60
    stdout=cache.split('----- stdout -----\n',1)[1].split('----- stderr -----',1)[0]
    # write_cache appends one framing newline after each exact captured stream.
    assert stdout==raw['stdout']+'\n'
    assert cache.split('----- stderr -----\n',1)[1]==raw['stderr']+'\n'
    namespace=load_author(source)
    assert namespace['ROOT']==ROOT and namespace['AUDIT_TIMEOUT_SEC']==60
    assert namespace['AUDIT_INPUT_PATHS']==(NOTE,)

    # Only publishing/CLI are exercised with saved synthetic-science data here.
    # These invocations are NOT new scientific execution receipts.
    namespace['symbolic']=lambda:copy.deepcopy(recorded['symbolic'])
    namespace['numeric']=lambda:copy.deepcopy(recorded['numerical'])
    first=invoke_fixture(namespace); second=invoke_fixture(namespace)
    assert first==second==raw['stdout']
    sidecar=HERE/'synthetic_io_sidecar.json'
    parsed=invoke_fixture(namespace,['--json','--output-json',str(sidecar)])
    assert json.loads(parsed)==recorded and sidecar.read_text()==parsed
    before=sidecar.read_bytes()
    try: invoke_fixture(namespace,['--output-json',str(sidecar)])
    except FileExistsError: collision=True
    else: raise AssertionError('collision not rejected')
    assert sidecar.read_bytes()==before
    io_controls={'synthetic_fixtures_only':True,'repeat_default_identical':True,
        'unrelated_cwd_root_resolution':True,'json_roundtrip_matches_pinned_result':True,
        'same_invocation_sidecar_matches_stdout':True,'exclusive_collision_preserved':collision}

    family_mutants=[]
    cases=[('symbolic_false','symbolic','tensor_inverse',False),
           ('row_count','numerical','real_to_Fourier_rows',rows[:-1]),
           ('transform_threshold_equal','numerical','max_transform_error',2e-11),
           ('flux_count','numerical','flux_samples',119),
           ('flux_bound','numerical','max_flux_bound_ratio',1+3e-12),
           ('off_cone_count','numerical','off_cone_samples',[]),
           ('missing_middle_threshold_equal','numerical','missing_intervening_term_mutation',{'difference':.01})]
    for name,category,key,value in cases:
        data=copy.deepcopy(recorded); data[category][key]=value
        namespace['symbolic']=lambda data=data:copy.deepcopy(data['symbolic'])
        namespace['numeric']=lambda data=data:copy.deepcopy(data['numerical'])
        try: invoke_fixture(namespace,['--json'])
        except AssertionError as exc:
            family_mutants.append({'name':name,'rejected':True,'failed_families':str(exc)})
        else: raise AssertionError(f'aggregation mutant survived: {name}')
    data=copy.deepcopy(recorded); data['numerical']['off_cone_samples'][0]['outside_front']=False
    namespace['symbolic']=lambda:copy.deepcopy(data['symbolic'])
    namespace['numeric']=lambda:copy.deepcopy(data['numerical'])
    try: invoke_fixture(namespace,['--json'])
    except AssertionError as exc: family_mutants.append({'name':'off_cone_false','rejected':True,'failed_families':str(exc)})
    else: raise AssertionError('off-cone false mutant survived')

    # Corrupt one decisive expression in an isolated in-memory author module.
    formula_cases=[
       ('static_projectors_swapped','inv=(N*PT+D*PL)/k2','inv=(D*PT+N*PL)/k2','symbolic'),
       ('dynamic_sign','dynamic=PT/(k2/N-alpha*omega**2)+PL/(k2/D-alpha*omega**2)',
         'dynamic=PT/(k2/N+alpha*omega**2)+PL/(k2/D+alpha*omega**2)','symbolic'),
       ('point_kernel_sign','static=N/(4*s.pi*rad)+(D-N)*s.diff(rad,zz,2)/(8*s.pi)',
         'static=N/(4*s.pi*rad)+(N-D)*s.diff(rad,zz,2)/(8*s.pi)','symbolic'),
       ('time_integral_factor','+(3*ctheta**2-1)*(1/cT**2-1/cL**2)/2)',
         '+(3*ctheta**2-1)*(1/cT**2-1/cL**2))','symbolic'),
       ('bessel_sign','j2=(3/q**3-1/q)*s.sin(q)-3*s.cos(q)/q**2',
         'j2=(3/q**3-1/q)*s.sin(q)+3*s.cos(q)/q**2','symbolic'),
       ('middle_omitted','middle=0.0 if omit_middle else -2*t/alpha*p2*quad(',
         'middle=0.0 if True else -2*t/alpha*p2*quad(','numeric'),
       ('outer_speed_replaced_by_transverse','cL=math.sqrt((mu+beta)/alpha)',
         'cL=math.sqrt(mu/alpha)','numeric'),
    ]
    formula_mutants=[]
    for name,old,new,function in formula_cases:
        assert source.count(old)==1
        mutated=source.replace(old,new)
        module=load_author(mutated)
        try: module[function]()
        except AssertionError:
            formula_mutants.append({'name':name,'rejected':True,'source_sha256':sha(mutated.encode()),'executed_function':function})
        else: raise AssertionError(f'formula mutant survived: {name}')
    for item in inventories: assert sha((ROOT/item['path']).read_bytes())==item['sha256']
    assert git('rev-parse','HEAD').decode().strip()==HEAD
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'head':HEAD,
        'function_body_identity':bodies,'unchanged_scientific_payload':True,
        'cache_input_fingerprint':fingerprint.hexdigest(),'cache_raw_stdout_equal':True,
        'io_controls':io_controls,'aggregation_mutants':family_mutants,
        'formula_mutants':formula_mutants,'all_original_source_bytes_unchanged':True,
        'elapsed_seconds':time.monotonic()-started,
        'scope':'Focused source review. No formal audit, primary scientific replay, observations, fit or heavy field computation.'}
    save_json('canonical_port_checks_v1.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('aggregation_mutants','formula_mutants')},indent=2))
    print(f"Rejected {len(formula_mutants)} formula mutants and {len(family_mutants)} result-aggregation mutants")

if __name__=='__main__': main()
