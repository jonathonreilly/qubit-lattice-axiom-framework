"""Root targeted replay of sealed review fixtures, without production values."""
from pathlib import Path
import hashlib,importlib.util,json,subprocess,sys
from fractions import Fraction
import numpy as np

HERE=Path(__file__).resolve().parent;SRC=HERE.parent
REVIEW=SRC/'geometric_fixed_rate_independent'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('analysis',SRC/'analyze_geometric_fixed_rate_followup.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
results=[]
for kind in ['baseline','wrapper_exception','zero_winding','mixed_zero_winding']:
    source=REVIEW/f'synthetic_{kind}_input';output=HERE/f'after_02_{kind}'
    command=[sys.executable,SRC/'analyze_geometric_fixed_rate_followup.py',source,output]
    run=subprocess.run([str(v) for v in command],capture_output=True,text=True)
    (HERE/f'attempt02_{kind}.stdout').write_text(run.stdout);(HERE/f'attempt02_{kind}.stderr').write_text(run.stderr)
    assert run.returncode==0,(kind,run.stderr)
    r=json.loads((output/'RESULTS.json').read_text());assert len(r['cells'])==12 and r['runs_used']==2
    for i,c in enumerate(r['cells']):
        assert c['bootstrap_seed']==2109211530+i and sum(c['status_counts'].values())==c['declared']
        assert c['event_cap_censored']==0 and c['conditional_on_full_verified_completion']
        if i:assert c['completed']==0 and all(v['estimate'] is None for v in c['observables'].values())
    c=r['cells'][0];v=c['observables'];assert c['not_started_deadline']==(253 if kind=='wrapper_exception' else 254)
    assert v['S1']['estimate']==3.5 and abs(v['S1']['standard_error']-1.5)<1e-15
    assert abs(v['S2_over_S1']['standard_error']-float(Fraction(2,49)))<1e-15
    if kind=='baseline':
        before=json.loads((REVIEW/'synthetic_baseline_analysis/RESULTS.json').read_text())['cells'][0]['observables']
        for key in a.METRICS:
            assert v[key]['estimate']==before[key]['estimate']
            assert v[key]['CI95_pointwise']==before[key]['CI95_pointwise']
    if kind=='wrapper_exception':
        e=[x for x in r['excluded'] if x['status']=='wrapper_exception'];assert len(e)==1
        assert not e[0]['receipt_present'] and not e[0]['receipt_files_authenticated'] and c['other_excluded']==1
    if kind=='zero_winding':
        assert v['W']['estimate']==0 and v['W']['CI95_pointwise']==[0,0]
        assert v['winding_fourth_ratio']['estimate'] is None
        assert v['winding_fourth_ratio']['bootstrap_undefined_resamples']==10000
    if kind=='mixed_zero_winding':
        assert v['winding_fourth_ratio']['estimate'] is not None
        assert v['winding_fourth_ratio']['standard_error'] is not None
        assert v['winding_fourth_ratio']['CI95_pointwise'] is None
        assert 2000<v['winding_fourth_ratio']['bootstrap_undefined_resamples']<3000
    results.append({'fixture':kind,'command':[str(x) for x in command],'returncode':run.returncode,'result_sha256':sha(output/'RESULTS.json'),'pass':True})

# Direct degenerate controls do not rewrite any preserved input or prior seal.
zero=np.zeros((2,len(a.COLUMNS)));zero[:,4]=1;zero[:,7]=1
r=a.summarize_cell(zero,2109211542)
assert r['S1']['estimate']==0 and r['W']['estimate']==1
assert r['S2_over_S1']['estimate'] is None and r['axis_mode_fourth_ratio']['CI95_pointwise'] is None
assert r['winding_fourth_ratio']['estimate']==1
r=a.summarize_cell(np.ones((1,len(a.COLUMNS))),2109211543)
assert all(v['standard_error'] is None and v['standard_error_status']=='fewer_than_two_histories' for v in r.values())
r=a.summarize_cell([],2109211544);assert all(v['estimate'] is None for v in r.values())

result={'scope':'Author targeted repairs checked against sealed nonproduction fixtures; no production values read.',
        'analysis_sha256':sha(SRC/'analyze_geometric_fixed_rate_followup.py'),
        'correction_sha256':sha(SRC/'GEOMETRIC_FIXED_RATE_ANALYSIS_CORRECTION.md'),
        'original_review_seal_sha256':sha(REVIEW/'FINAL_SEAL.json'),'rows':results,
        'additional_controls':['zero first-shell denominator','one completed history','zero completed histories'],
        'successful_original_estimates_and_intervals_unchanged':True}
(HERE/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2))
