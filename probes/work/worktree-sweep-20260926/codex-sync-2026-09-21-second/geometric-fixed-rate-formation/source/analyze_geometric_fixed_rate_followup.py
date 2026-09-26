"""Declared whole-realization statistics; no phase or asymptotic fit inference."""
from pathlib import Path
import argparse,hashlib,json
from collections import Counter,defaultdict
import numpy as np

HERE=Path(__file__).resolve().parent
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()

COLUMNS=('S1','S2','S3','S4','W','axis_mode_square','axis_shell_square','winding_square','time_per_volume','slides_per_site','site_reuse_fraction')
METRICS=('S1','W','S2_over_S1','S3_over_S1','S4_over_S1','W_over_S1','axis_mode_fourth_ratio','axis_shell_fourth_ratio','winding_fourth_ratio','time_per_volume','slides_per_site','site_reuse_fraction')
METRIC_SPEC=((0,None,1),(4,None,1),(1,0,1),(2,0,1),(3,0,1),(4,0,1),(5,0,2),(6,0,2),(7,4,2),(8,None,1),(9,None,1),(10,None,1))
def metrics(m):
    ans=[]
    for num,den,power in METRIC_SPEC:
        if den is None:ans.append(m[...,num]);continue
        value=np.full(m.shape[:-1],np.nan)
        np.divide(m[...,num],m[...,den]**power,out=value,where=m[...,den]>0)
        ans.append(value)
    return np.stack(ans,axis=-1)

def summarize_cell(rows,seed):
    n=len(rows)
    if not n:
        return {key:{'estimate':None,'estimate_status':'no_completed_histories',
                     'standard_error':None,'standard_error_status':'fewer_than_two_histories',
                     'CI95_pointwise':None,'CI_status':'no_completed_histories',
                     'bootstrap_defined_resamples':0,'bootstrap_undefined_resamples':0} for key in METRICS}
    a=np.asarray(rows);assert a.shape==(n,len(COLUMNS)) and np.all(np.isfinite(a))
    means=a.mean(axis=0);point=metrics(means);rng=np.random.default_rng(seed)
    boot=[]
    for start in range(0,10000,1000):
        idx=rng.integers(0,n,size=(1000,n));boot.append(metrics(a[idx].mean(axis=1)))
    boot=np.concatenate(boot);result={}
    for j,(key,(num,den,power)) in enumerate(zip(METRICS,METRIC_SPEC)):
        defined=bool(np.isfinite(point[j]));count=int(np.isfinite(boot[:,j]).sum())
        interval=np.quantile(boot[:,j],[.025,.975]).tolist() if count==10000 else None
        se=None
        if n>=2 and defined:
            if den is None:influence=a[:,num]-means[num]
            else:
                influence=(a[:,num]-means[num])/means[den]**power-power*means[num]*(a[:,den]-means[den])/means[den]**(power+1)
            se=float(np.std(influence,ddof=1)/np.sqrt(n))
        result[key]={'estimate':float(point[j]) if defined else None,
                     'estimate_status':'defined' if defined else 'zero_denominator',
                     'standard_error':se,
                     'standard_error_status':'defined' if se is not None else ('fewer_than_two_histories' if n<2 else 'zero_denominator'),
                     'standard_error_method':'sample_standard_deviation_over_sqrt_n' if den is None else 'paired_delta_method_from_history_influence',
                     'CI95_pointwise':interval,
                     'CI_status':'defined' if interval is not None else 'zero_denominator_in_bootstrap',
                     'bootstrap_defined_resamples':count,'bootstrap_undefined_resamples':10000-count}
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('source',type=Path);ap.add_argument('output',type=Path);args=ap.parse_args()
    src=args.source.resolve();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    summary=json.loads((src/'SUMMARY.json').read_text());manifest=json.loads((src/'MANIFEST.json').read_text())
    assert summary['manifest']==manifest and not manifest['pilot'] and len(manifest['cases'])==2496
    assert manifest['protocol_sha256']==sha(HERE/'GEOMETRIC_FIXED_RATE_FOLLOWUP_PROTOCOL.md')
    assert manifest['wrapper_sha256']==sha(HERE/'run_geometric_fixed_rate_followup.py')
    assert manifest['source_sha256']==sha(HERE/'geometric_partner_growth.cpp')
    cases={tuple(c) for c in manifest['cases']};assert len(cases)==2496
    assert len(summary['results'])==len(cases) and {tuple(r['case']) for r in summary['results']}==cases
    values=[];bindings=[];groups=defaultdict(list);excluded=[];cell_status=defaultdict(Counter)
    declared=Counter((N,beta) for N,beta,seed in manifest['cases'])
    for row in summary['results']:
        N,beta,seed=row['case'];name=f'N{N}_b{beta}_s{seed}';prefix=src/name
        assert row.get('name',name)==name
        cell_status[N,beta][row['status']]+=1
        rp=Path(str(prefix)+'.receipt.json')
        if row['status']=='wrapper_exception':
            # This is the wrapper's actual exception schema. A receipt is not
            # promised, and a partial receipt must not be treated as verified.
            excluded.append({**row,'name':name,'receipt_present':rp.exists(),
                             'receipt_sha256':sha(rp) if rp.exists() else None,
                             'receipt_files_authenticated':False})
            continue
        if row['status']=='not_started_deadline':
            assert not rp.exists();excluded.append(row);continue
        receipt=json.loads(rp.read_text());assert receipt['case']==row['case'] and receipt['status']==row['status']
        for filename,digest in receipt['files'].items():
            assert sha(src/filename)==digest,filename
        bindings.append({'name':name,'receipt_sha256':sha(rp),'files':len(receipt['files'])})
        if row['status']!='full_verified':excluded.append(row);continue
        d=json.loads(Path(str(prefix)+'.json').read_text());v=json.loads(Path(str(prefix)+'.verification.json').read_text())
        assert d['full'] and d['N']==N and d['beta']==beta and d['seed']==seed
        assert v['lossless_arrays_reopened_and_equal'] and v['integer_Gauss_max_abs']==0
        assert v['archive_sha256']==receipt['files'][v['archive']]
        assert v['shells']==row['shells'] and v['winding_power_per_component']==row['winding_power_per_component']
        axis=[m['transverse_per_polarization'] for m in v['modes'] if sum(a*a for a in m['ell'])==1]
        assert len(axis)==3 and min(axis)>=-1e-14
        shell=[v['shells'][str(k)] for k in [1,2,3,4]];W=v['winding_power_per_component']
        assert abs(np.mean(axis)-shell[0])<1e-14 and W==sum(w*w for w in d['winding'])/(3*N)
        obs=[*shell,W,float(np.mean(np.square(axis))),shell[0]**2,W**2,d['time']/N**3,d['slide_events']/N**3,v['site_reuse_fraction']]
        item={'case':row['case'],'name':name,'winding':d['winding'],'observables':dict(zip(COLUMNS,obs))}
        values.append(item);groups[N,beta].append(obs)
    results=[]
    for index,(N,beta) in enumerate(sorted(declared)):
        rows=groups[N,beta];n=len(rows);expected=declared[N,beta];assert n<=expected
        counts=cell_status[N,beta];assert sum(counts.values())==expected
        seed=2109211530+index
        result={'N':N,'beta':beta,'completed':n,'declared':expected,'status_counts':dict(counts),
                'conditional_on_full_verified_completion':n!=expected,
                'event_cap_censored':counts['event_cap_censored'],
                'not_started_deadline':counts['not_started_deadline'],
                'other_excluded':expected-n-counts['event_cap_censored']-counts['not_started_deadline'],
                'bootstrap_seed':seed,'observables':summarize_cell(rows,seed)}
        results.append(result)
    result={'scope':'Author descriptive statistics of the supplied fixed-rate geometry-only process. Selective independent source/observable review is separate; these production values are not independently replayed. No phase proof or Maxwell dynamics.',
            'source_manifest_sha256':sha(src/'MANIFEST.json'),'source_summary_sha256':sha(src/'SUMMARY.json'),
            'analysis_sha256':sha(Path(__file__)),'analysis_plan_sha256':sha(HERE/'GEOMETRIC_FIXED_RATE_ANALYSIS_PLAN.md'),
            'analysis_correction_sha256':sha(HERE/'GEOMETRIC_FIXED_RATE_ANALYSIS_CORRECTION.md'),
            'status_counts':dict(Counter(r['status'] for r in summary['results'])),'runs_used':len(values),'excluded':excluded,
            'bootstrap_resamples':10000,'statistical_unit':'one complete independent history','intervals':'95% pointwise percentile bootstrap; not simultaneous or a finite-size-bias estimate',
            'undefined_bootstrap_policy':'If any resample has zero denominator, the affected entire interval is undefined; no resample is dropped.',
            'standard_errors':'Across-history sample SE for linear means; paired delta-method influence SE for ratios; undefined for fewer than two histories or zero denominator.',
            'gaussian_conditional_reference':{'S2_over_S1':1,'S3_over_S1':1,'S4_over_S1':1,'W_over_S1':1,'axis_mode_fourth_ratio':1.5,'axis_shell_fourth_ratio':7/6,'winding_fourth_ratio':5/3},
            'cells':results}
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    (out/'PER_HISTORY.json').write_text(json.dumps(values,indent=2)+'\n')
    (out/'RECEIPT_VERIFICATION.json').write_text(json.dumps({'rows':bindings,'all_files_in_listed_receipts_hashed':True,
        'wrapper_exception_receipts_not_interpreted':sum(r['status']=='wrapper_exception' for r in excluded)},indent=2)+'\n')
    lines=['# Declared fixed-rate formation follow-up','',result['scope'],'',f"Used {len(values)} of2496 declared histories. Status counts: {result['status_counts']}.",'','Intervals below are pointwise95% whole-history bootstrap intervals. They do not include finite-size or simulator bias.','',
           '| N | beta | runs | S1 | W | W/S1 | S4/S1 | meanT/V | slides/site |','|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    def fmt(v):
        if v['estimate'] is None:return 'undefined ('+v['estimate_status']+')'
        se=f"; SE {v['standard_error']:.4g}" if v['standard_error'] is not None else '; SE undefined'
        ci=v['CI95_pointwise']
        interval=f' [{ci[0]:.6g},{ci[1]:.6g}]' if ci is not None else ' [CI undefined]'
        return f"{v['estimate']:.6g}"+interval+se
    for row in results:
        v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|{row['completed']}|"+'|'.join(fmt(v[k]) for k in ['S1','W','W_over_S1','S4_over_S1','time_per_volume','slides_per_site'])+'|')
    lines+=['','## Fourth-moment diagnostics','','The listed Gaussian comparison values require the additional assumptions in the analysis plan.','',
            '| N | beta | individual-mode ratio (3/2) | axis-shell ratio (7/6) | winding ratio (5/3) |','|---:|---:|---:|---:|---:|']
    for row in results:
        v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|"+'|'.join(fmt(v[k]) for k in ['axis_mode_fourth_ratio','axis_shell_fourth_ratio','winding_fourth_ratio'])+'|')
    (out/'TABLE.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'runs_used':len(values),'cells':len(results),'status_counts':result['status_counts'],'listed_receipt_files_authenticated':True,
                      'wrapper_exception_receipts_not_interpreted':sum(r['status']=='wrapper_exception' for r in excluded)},indent=2))

if __name__=='__main__':main()
