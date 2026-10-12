from pathlib import Path
from datetime import datetime, timezone
import hashlib, itertools, json, math

S=Path(__file__).resolve().parent;E=S/'state_adapted_refinement_review'
R=S/'state_adapted_independent_root_verification';R.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
js=lambda p:json.loads(Path(p).read_bytes())
anchors={'PRE_EXECUTION_SEAL.json':'5df55a08aa0e8416de0f8f86162034a7dbf63edc59ba54fd1debae6e9c9a75d9','INDEPENDENT_CHECKS_SEAL.json':'a1fa9a76914840e2acc86f965a76c76e5c37ebfed27292c9bd9fe6df754ef426','INTEGRITY_EXECUTION_SEAL.json':'5c67601650f2ec1bebc0cd479aafcdbbf1d35956947b2f3e6e5eb475611e4e9d','INTEGRITY_RESULT_SEAL.json':'a6e1e00b8485aabfab00642095d1dc97d7da6d89a815cd23acd8af48baa6fbf9'}
for name,digest in anchors.items():
    assert sha(E/name)==digest
    for rel,h in js(E/name)['files'].items():assert sha(E/rel)==h
plan=js(E/'NEUTRAL_PLAN_SEAL.json');assert sha(E/'NEUTRAL_PLAN.md')==plan['plan_sha256']=='308f4e46581c07a2fedd4cb094c92403211aa61731bdd751f734b7d428b6a728'
pre=js(E/'PRE_EXECUTION_SEAL.json');independent=js(E/'INDEPENDENT_CHECKS_SEAL.json')
assert not pre['author_helper_protocol_result_exposure'] and not independent['author_helper_protocol_result_exposure']
assert plan['frozen_at_utc']<pre['frozen_at_utc']<independent['sealed_at_utc']
records=[]
for name in ['check_fock','check_strong_limit']:
    D=E/'attempt_01'/name;r=js(D/'OUTER_END.json');inner=js(D/'INNER_RECEIPT.json')
    assert r['source_hashes_before']==r['source_hashes_after']==pre['files']
    assert r['sources_unchanged'] and not r['timed_out'] and r['returncode']==0
    assert r['timeout_seconds']==120 and r['process_group'] and 0<=r['elapsed_seconds']<120
    assert pre['frozen_at_utc']<r['started_utc']<r['finished_utc']<independent['sealed_at_utc']
    assert all(inner[k]==r[k] for k in inner)
    assert js(D/'OUTER.stdout')==r and not (D/'OUTER.stderr').read_bytes()
    for stream in ['stdout','stderr']:assert sha(D/('INNER.'+stream))==r['inner_'+stream+'_sha256']
    assert not (D/'INNER.stderr').read_bytes()
    records.append({k:v for k,v in r.items() if k not in ['source_hashes_before','source_hashes_after']})
def raw_result(name):
    text=(E/'attempt_01'/name/'INNER.stdout').read_text();d,n=json.JSONDecoder().raw_decode(text);return d,text[n:].strip()
fock,total=raw_result('check_fock');assert total=='TOTAL: PASS=21 FAIL=0' and fock['passed']==21 and fock['failed']==0
params=[(0.7,1.3,0.8),(0.4,0.7,1.1),(1.0,0.9,0.0)]
basis=[list(x) for k in range(0,7,2) for x in itertools.combinations(range(6),k)]
assert len(fock['cases'])==3;moments=0;TOL=5e-10;DETECT=1e-5
for case,par in zip(fock['cases'],params):
    assert case['parameters']==dict(zip(['a','m','v'],par))
    strict=par[-1]>0;assert case['strict_target_domain']==strict
    maps=case['maps'];assert set(maps)=={'specified_adapted','bare_haar','reversed_fine_rotation','reversed_coarse_rotation'}
    for name,data in maps.items():
        assert data['isometry_error']<TOL
        rows=data['all_moment_rows'];assert [x['indices'] for x in rows]==basis
        for row in rows:
            c=complex(row['coarse']['real'],row['coarse']['imag']);f=complex(row['fine']['real'],row['fine']['imag'])
            assert abs(abs(c-f)-row['error'])<1e-15*max(1,row['error'])
            moments+=1
        assert max(x['error'] for x in rows)==data['max_moment_error']
    dyn=case['dynamics'];norm_difference=abs(dyn['direct_many_body_defect_norm']-dyn['one_body_rank_two_norm'])
    assert dyn['norm_difference']==norm_difference
    support=case['finite_support'];assert [x['site'] for x in support]==[2,3,4,5]
    support_max=max(x['commutator_norm'] for x in support)
    gates={'beta_ground_and_CAR':all(case[n][k]<TOL for n in ['coarse','fine'] for k in ['hermiticity_error','beta_reality_error','beta_orthogonality_error','beta_trace_vs_one_body_expm_error','beta_ground_alignment_error']),
           'adapted_isometry':maps['specified_adapted']['isometry_error']<TOL,
           'all_even_moments':maps['specified_adapted']['max_moment_error']<TOL,
           'mutation_behavior':all((v['max_moment_error']>DETECT if strict else v['max_moment_error']<TOL) for k,v in maps.items() if k!='specified_adapted'),
           'even_dynamic_behavior':dyn['direct_many_body_defect_norm']>DETECT if strict else dyn['direct_many_body_defect_norm']<TOL,
           'rank_two_norm_crosscheck':norm_difference<TOL,
           'finite_support_behavior':support_max>DETECT if strict else support_max<TOL}
    assert gates==case['gates'] and all(gates.values())
assert moments==384
limit,total=raw_result('check_strong_limit');assert total=='TOTAL: PASS=3 FAIL=0'
low,high=limit['low_rule'],limit['high_rule'];assert len(low)==len(high)==9
for series in [low,high]:
    assert [r['n'] for r in series]==list(range(1,10))
    assert all(r['a']==2.**(-r['n']) for r in series)
keys=['squared_error_correct','squared_error_missing_continuum_unrotation']
difference=max(abs(a[k]-b[k]) for a,b in zip(low,high) for k in keys)
assert difference==limit['maximum_quadrature_difference']
assert limit['omitted_squared_error_tail_upper_bound']==16/(math.pi*limit['parameters']['qmax'])
gates={'quadrature_agreement':difference<1e-7,'correct_final_below_first':high[-1][keys[0]]<high[0][keys[0]],'missing_unrotation_detected':high[-1][keys[1]]-high[-1][keys[0]]>1e-3}
assert gates==limit['gates'] and all(gates.values())
integrity=js(E/'INTEGRITY_EXECUTION_SEAL.json');results=E/'integrity_01/results'
outcomes={}
for name,expected in [('valid',0),('tampered_checker',1),('exit_only_survivor',0)]:
    D=results/name;r=js(D/'OUTER_END.json')
    assert r['source_hashes_before']==r['source_hashes_after']==integrity['files']
    assert r['sources_unchanged'] and not r['timed_out'] and r['timeout_seconds']==20
    assert r['process_group'] and r['returncode']==expected and 0<=r['elapsed_seconds']<20
    assert r['expected_execution_seal_sha256']==anchors['INTEGRITY_EXECUTION_SEAL.json']
    assert js(D/'OUTER.stdout')==r and not (D/'OUTER.stderr').read_bytes()
    for stream in ['stdout','stderr']:assert sha(D/('INNER.'+stream))==r[stream+'_sha256']
    if name=='tampered_checker':
        assert r['launch_markers']==[] and not r['attempt_exists'] and r['complete'] is None
        assert (D/'INNER.stderr').read_text()=='Pre-execution source mismatch: check_fock.py\n'
    else:
        assert r['launch_markers']==['check_fock.launched','check_strong_limit.launched'] and r['attempt_exists']
        assert [x['returncode'] for x in r['complete']['records']]==([7,0] if name=='exit_only_survivor' else [0,0])
    outcomes[name]={'driver_exit':r['returncode'],'elapsed_seconds':r['elapsed_seconds'],'complete':r['complete']}
(R/'verified_scientific_receipts.json').write_text(json.dumps(records,indent=2)+'\n')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'sealed_independent_evidence_checked','seals':anchors,'complex_moments_mechanically_verified':moments,'scientific_gates_recomputed':24,'quadrature_values':36,'independent_source_and_derivation_full_root_read':True,'manual_data_scope':'All case metadata/gates/extreme moments and all36 quadrature values; earlier oversized384moment print truncated and not counted as complete manual read. Every384complex residual checked from full stored originals by this program.','integrity_outcomes':outcomes,'science_rerun':False,'author_source_exposure_after_independent_seal':True,'scope_limits':['finite periodic CAR diagnostics','finite quadrature uncertified','same model family and exposed theorem/parents','driver exit0 alone is insufficient'],'pending':['final reviewer report and final manifest integration']}
(R/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
