#!/usr/bin/env python3
"""Compare final analysis only after independent endpoint/aggregation seals."""
from pathlib import Path
import datetime,hashlib,json,math
HERE=Path(__file__).resolve().parent;RAW=HERE.parent
ANAL=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/geometric_fixed_rate_analysis')
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':h.hexdigest()}
def load(p):return json.loads(p.read_text())
pre=load(HERE/'AGGREGATION_PRECOMPARISON_SEAL.json')
for row in pre['sources']+pre['artifacts']:assert identity(row['path'])==row
own=load(HERE/'INDEPENDENT_AGGREGATION.json');auth=load(HERE/'PRODUCTION_AUTHENTICATION.json')
result=load(ANAL/'RESULTS.json')
assert result['source_manifest_sha256']==auth['manifest']['sha256'] and result['source_summary_sha256']==auth['summary']['sha256']
for key,name in [('analysis_sha256','analyze_geometric_fixed_rate_followup.py'),('analysis_plan_sha256','GEOMETRIC_FIXED_RATE_ANALYSIS_PLAN.md'),('analysis_correction_sha256','GEOMETRIC_FIXED_RATE_ANALYSIS_CORRECTION.md')]:
    assert result[key]==identity(RAW/name)['sha256']
assert result['runs_used']==2496 and result['excluded']==[] and result['status_counts']=={'full_verified':2496}
assert result['bootstrap_resamples']==10000 and len(result['cells'])==12
assert result['statistical_unit']=='one complete independent history'
assert result['gaussian_conditional_reference']=={'S2_over_S1':1,'S3_over_S1':1,'S4_over_S1':1,'W_over_S1':1,'axis_mode_fourth_ratio':1.5,'axis_shell_fourth_ratio':7/6,'winding_fourth_ratio':5/3}
comparisons=[];max_estimate=max_se=0.;intervals_authenticated=0
for declared,stored in zip(own['cells'],result['cells']):
    assert (declared['N'],declared['beta'])==(stored['N'],stored['beta'])
    n=declared['n'];assert stored['completed']==stored['declared']==n
    assert stored['status_counts']=={'full_verified':n} and not stored['conditional_on_full_verified_completion']
    assert stored['event_cap_censored']==stored['not_started_deadline']==stored['other_excluded']==0
    assert declared['bootstrap_seed']==stored['bootstrap_seed']
    assert set(declared['observables'])==set(stored['observables'])
    for metric,a in declared['observables'].items():
        b=stored['observables'][metric]
        assert a['estimate_status']==b['estimate_status'] and a['standard_error_status']==b['standard_error_status']
        differences={}
        for key in ['estimate','standard_error']:
            if a[key] is None:assert b[key] is None;differences[key]=None;continue
            assert math.isfinite(a[key]) and math.isfinite(b[key])
            delta=abs(a[key]-b[key]);assert delta<=1e-12+1e-12*max(abs(a[key]),abs(b[key])),(stored['N'],stored['beta'],metric,key,a[key],b[key])
            differences[key]=delta
            if key=='estimate':max_estimate=max(max_estimate,delta)
            else:max_se=max(max_se,delta)
        method='sample_standard_deviation_over_sqrt_n' if metric in ['S1','W','time_per_volume','slides_per_site','site_reuse_fraction'] else 'paired_delta_method_from_history_influence'
        assert b['standard_error_method']==method
        defined=b['bootstrap_defined_resamples'];undefined=b['bootstrap_undefined_resamples']
        assert defined+undefined==10000 and 0<=defined<=10000
        if undefined:
            assert b['CI95_pointwise'] is None and b['CI_status']=='zero_denominator_in_bootstrap'
        else:
            ci=b['CI95_pointwise'];assert b['CI_status']=='defined' and len(ci)==2 and all(map(math.isfinite,ci)) and ci[0]<=ci[1]
        intervals_authenticated+=1
        comparisons.append({'N':stored['N'],'beta':stored['beta'],'metric':metric,'point_estimate_difference':differences['estimate'],'standard_error_difference':differences['standard_error']})

# Authenticate presentation arithmetic while reusing, not recomputing, the
# previously checked bootstrap procedure and its saved interval endpoints.
lines=['# Declared fixed-rate formation follow-up','',result['scope'],'',
       f"Used {result['runs_used']} of2496 declared histories. Status counts: {result['status_counts']}.",'',
       'Intervals below are pointwise95% whole-history bootstrap intervals. They do not include finite-size or simulator bias.','',
       '| N | beta | runs | S1 | W | W/S1 | S4/S1 | meanT/V | slides/site |',
       '|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
def fmt(v):
    if v['estimate'] is None:return 'undefined ('+v['estimate_status']+')'
    se=f"; SE {v['standard_error']:.4g}" if v['standard_error'] is not None else '; SE undefined'
    ci=v['CI95_pointwise'];interval=f' [{ci[0]:.6g},{ci[1]:.6g}]' if ci is not None else ' [CI undefined]'
    return f"{v['estimate']:.6g}"+interval+se
for row in result['cells']:
    v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|{row['completed']}|"+'|'.join(fmt(v[k]) for k in ['S1','W','W_over_S1','S4_over_S1','time_per_volume','slides_per_site'])+'|')
lines+=['','## Fourth-moment diagnostics','','The listed Gaussian comparison values require the additional assumptions in the analysis plan.','',
        '| N | beta | individual-mode ratio (3/2) | axis-shell ratio (7/6) | winding ratio (5/3) |',
        '|---:|---:|---:|---:|---:|---:|']
for row in result['cells']:
    v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|"+'|'.join(fmt(v[k]) for k in ['axis_mode_fourth_ratio','axis_shell_fourth_ratio','winding_fourth_ratio'])+'|')
assert (ANAL/'TABLE.md').read_text()=='\n'.join(lines)+'\n'
assert len(comparisons)==144 and intervals_authenticated==144
out={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'analysis_sources':[identity(p) for p in sorted(ANAL.iterdir()) if p.is_file()],
     'all144_point_estimates_and144_standard_errors_checked':True,'comparisons':comparisons,
     'maximum_absolute_point_estimate_difference':max_estimate,'maximum_absolute_standard_error_difference':max_se,
     'all_cell_counts_seed_indices_and_statuses_match':True,'TABLE_rendering_matches_saved_results':True,
     'bootstrap_interval_entries_authenticated':intervals_authenticated,'bootstrap_resampling_rerun':False,
     'bootstrap_limit':'The unchanged previously checked whole-history resampling implementation is reused; production quantiles and statistical coverage are not independently recomputed.',
     'findings':[]}
(HERE/'ANALYSIS_COMPARISON.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print(json.dumps({k:out[k] for k in ['all144_point_estimates_and144_standard_errors_checked','maximum_absolute_point_estimate_difference','maximum_absolute_standard_error_difference','TABLE_rendering_matches_saved_results','bootstrap_resampling_rerun','findings']},indent=2))
