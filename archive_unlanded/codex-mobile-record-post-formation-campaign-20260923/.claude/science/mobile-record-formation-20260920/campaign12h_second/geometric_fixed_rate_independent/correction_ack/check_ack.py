#!/usr/bin/env python3
"""Narrow F1-F3 correction check using only sealed synthetic inputs, no production values."""
from pathlib import Path
from fractions import Fraction
import hashlib,importlib.util,json,math,shutil,subprocess,sys,datetime
import numpy as np
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;PRIOR=O.parent;R=PRIOR.parent
if (O/'TARGETED_RESULTS.json').exists():raise SystemExit('targeted evidence exists; preserve it')
ANALYZER=R/'analyze_geometric_fixed_rate_followup.py'
OLD=R/'geometric_fixed_rate_analysis_fix/before_analyze_geometric_fixed_rate_followup.py'
CORRECTION=R/'GEOMETRIC_FIXED_RATE_ANALYSIS_CORRECTION.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
assert sha(ANALYZER)=='9da84212404a18f7a1eaf6be7ddef3bfab657d6d8f5c201bba5778ac4720597a'
assert sha(OLD)=='531c59d50c910bca28f8ae0255bc3507831ac32dc3dbd2dd011cb433bd9d557d'
assert sha(CORRECTION)=='9caea17017738357a7a9a8ff6d32ef937265a08d249e7046f15b9595b7fc7857'
oldseal=json.loads((PRIOR/'FINAL_SEAL.json').read_text());authenticated=0
for group in ['sources','procedures_reused_unchanged','prior_independent_evidence_reused','prior_clock_report_and_seal_unchanged','artifacts']:
    for item in oldseal[group]:
        path=Path(item['path']);actual=OLD if path==ANALYZER else path
        assert sha(actual)==item['sha256'],(path,actual)
        authenticated+=1
assert sha(PRIOR/'FINAL_SEAL.json')=='b3754b93fa492301d4875760c3de7cc598664530a7cf119cda91b1958f39f7fb'
# Recover the exact earlier source by applying the inverse full diff to a local copy.
recovered=O/'inverse_recovered_analyzer.py';shutil.copyfile(ANALYZER,recovered)
p=subprocess.run(['patch','--batch','-R',str(recovered),str(O/'ANALYZER_SOURCE_DIFF.patch')],cwd=O,text=True,capture_output=True)
(O/'inverse_patch.stdout').write_text(p.stdout);(O/'inverse_patch.stderr').write_text(p.stderr)
assert p.returncode==0 and recovered.read_bytes()==OLD.read_bytes(),p.stderr
replays={}
for name in ['baseline','wrapper_exception','zero_winding','mixed_zero_winding']:
    source=PRIOR/f'synthetic_{name}_input';target=O/f'replay_{name}'
    command=[sys.executable,str(ANALYZER),str(source),str(target)]
    proc=subprocess.run(command,cwd=O,text=True,capture_output=True)
    (O/f'{name}.stdout').write_text(proc.stdout);(O/f'{name}.stderr').write_text(proc.stderr)
    dump(O/f'{name}.receipt.json',{'command':command,'returncode':proc.returncode,'source_kind':'previously sealed synthetic statistics fixture; not physical or production data'})
    assert proc.returncode==0 and not proc.stderr,(name,proc.stderr)
    result=json.loads((target/'RESULTS.json').read_text());assert len(result['cells'])==12 and result['runs_used']==2
    for j,cell in enumerate(result['cells']):
        assert cell['bootstrap_seed']==2109211530+j
        assert sum(cell['status_counts'].values())==cell['declared']
        assert cell['completed']+cell['event_cap_censored']+cell['not_started_deadline']+cell['other_excluded']==cell['declared']
        if j:
            assert cell['completed']==0 and all(x['estimate'] is None and x['CI95_pointwise'] is None for x in cell['observables'].values())
    replays[name]=result
old=json.loads((PRIOR/'synthetic_baseline_analysis/RESULTS.json').read_text())['cells'][0]['observables']
base=replays['baseline']['cells'][0]['observables']
for key,value in old.items():
    assert base[key]['estimate']==value['estimate']
    assert base[key]['CI95_pointwise']==value['CI95_pointwise']
exceptions=[x for x in replays['wrapper_exception']['excluded'] if x['status']=='wrapper_exception']
assert len(exceptions)==1 and exceptions[0]['traceback']=='synthetic; no production data'
assert exceptions[0]['receipt_present'] is False and exceptions[0]['receipt_files_authenticated'] is False
assert replays['wrapper_exception']['cells'][0]['other_excluded']==1
z=replays['zero_winding']['cells'][0]['observables'];m=replays['mixed_zero_winding']['cells'][0]['observables']
assert z['W']['estimate']==0 and z['W']['CI95_pointwise']==[0.,0.]
assert z['winding_fourth_ratio']['estimate'] is None and z['winding_fourth_ratio']['bootstrap_undefined_resamples']==10000
assert m['winding_fourth_ratio']['estimate'] is not None and m['winding_fourth_ratio']['CI95_pointwise'] is None
assert 0<m['winding_fourth_ratio']['bootstrap_undefined_resamples']<10000
# Independently reproduce the mixed-case degenerate-resample count.
idx=np.random.default_rng(2109211530).integers(0,2,size=(10000,2))
assert int(np.all(idx==0,axis=1).sum())==m['winding_fourth_ratio']['bootstrap_undefined_resamples']
# Independently calculate SEs as gradient * exact paired sample covariance * gradient / n.
spec=importlib.util.spec_from_file_location('corrected_analyzer',ANALYZER);a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
rows=json.loads((PRIOR/'synthetic_baseline_analysis/PER_HISTORY.json').read_text())
X=[[Fraction(str(row['observables'][key])) for key in a.COLUMNS] for row in rows]
n=len(X);means=[sum(x[j] for x in X)/n for j in range(len(a.COLUMNS))]
C=[[sum((x[j]-means[j])*(x[k]-means[k]) for x in X)/(n-1) for k in range(len(means))] for j in range(len(means))]
variances={}
for key,(num,den,power) in zip(a.METRICS,a.METRIC_SPEC):
    grad=[Fraction(0)]*len(means)
    if den is None:grad[num]=1
    else:
        grad[num]=1/means[den]**power
        grad[den]-=power*means[num]/means[den]**(power+1)
    variance=sum(grad[j]*C[j][k]*grad[k] for j in range(len(means)) for k in range(len(means)))/n
    assert variance>=0
    expected=math.sqrt(float(variance));got=base[key]['standard_error']
    assert math.isclose(got,expected,rel_tol=1e-13,abs_tol=1e-15),(key,got,expected)
    variances[key]=str(variance)
assert variances['S1']=='9/4' and variances['S2_over_S1']=='4/2401'
assert math.isclose(base['S2_over_S1']['standard_error'],2/49,rel_tol=0,abs_tol=1e-15)
# Direct affected-branch controls: no history, one history, and a zero S1 with nonzero W.
empty=a.summarize_cell([],1);assert all(v['estimate_status']=='no_completed_histories' for v in empty.values())
row=np.array([[float(x) for x in X[0]]])
one=a.summarize_cell(row,1);assert all(v['standard_error'] is None and v['standard_error_status']=='fewer_than_two_histories' for v in one.values())
zero=np.array([[float(v) for v in x] for x in X]);zero[:,[0,1,2,3,5,6]]=0
s=a.summarize_cell(zero,1);assert s['S1']['estimate']==0 and s['S1']['CI95_pointwise']==[0.,0.]
assert s['S2_over_S1']['estimate'] is None and s['W_over_S1']['estimate'] is None
assert s['winding_fourth_ratio']['estimate'] is not None
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prior_final_seal_rows_authenticated':authenticated,
        'prior_artifacts_preserved':len(oldseal['artifacts']),'inverse_full_diff_recovers_reviewed_source':True,
        'four_sealed_synthetic_replays_all_exit_zero':True,'successful_baseline_point_estimates_and_percentile_endpoints_byte_equal_as_JSON_values':True,
        'all_twelve_declared_cells_and_fixed_seed_indices_checked':True,'wrapper_exception_schema_preserved_and_excluded':True,
        'zero_winding_and_mixed_zero_resample_statuses_checked':True,'mixed_zero_resamples':m['winding_fourth_ratio']['bootstrap_undefined_resamples'],
        'exact_paired_covariance_delta_SE_squared':variances,'zero_one_and_zero_S1_history_branches_checked':True,
        'current_analyzer_sha256':sha(ANALYZER),'correction_note_sha256':sha(CORRECTION),'unchanged_protocol_sha256':sha(R/'GEOMETRIC_FIXED_RATE_FOLLOWUP_PROTOCOL.md'),
        'unchanged_plan_sha256':sha(R/'GEOMETRIC_FIXED_RATE_ANALYSIS_PLAN.md'),'production_values_read':False,'unresolved_findings':[]}
dump(O/'TARGETED_RESULTS.json',result);print(json.dumps(result,indent=2))
