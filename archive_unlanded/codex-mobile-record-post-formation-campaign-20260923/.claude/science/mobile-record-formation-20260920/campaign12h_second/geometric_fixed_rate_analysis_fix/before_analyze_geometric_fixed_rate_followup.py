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
def metrics(m):
    return np.stack((m[...,0],m[...,4],m[...,1]/m[...,0],m[...,2]/m[...,0],m[...,3]/m[...,0],m[...,4]/m[...,0],m[...,5]/m[...,0]**2,m[...,6]/m[...,0]**2,m[...,7]/m[...,4]**2,m[...,8],m[...,9],m[...,10]),axis=-1)

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
    values=[];bindings=[];groups=defaultdict(list);excluded=[]
    for row in summary['results']:
        N,beta,seed=row['case'];name=row['name'];prefix=src/name
        rp=Path(str(prefix)+'.receipt.json')
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
    for index,((N,beta),rows) in enumerate(sorted(groups.items())):
        a=np.asarray(rows);n=len(a);assert a.shape==(n,len(COLUMNS))
        expected=64 if N==128 else 256;assert n<=expected
        means=a.mean(axis=0);point=metrics(means);seed=2109211530+index;rng=np.random.default_rng(seed)
        boot=[]
        for start in range(0,10000,1000):
            idx=rng.integers(0,n,size=(1000,n));boot.append(metrics(a[idx].mean(axis=1)))
        boot=np.concatenate(boot);lo,hi=np.quantile(boot,[.025,.975],axis=0)
        assert np.all(np.isfinite(point)) and np.all(np.isfinite(boot))
        result={'N':N,'beta':beta,'completed':n,'declared':expected,'conditional_on_cap_completion':n!=expected,'bootstrap_seed':seed,
                'observables':{key:{'estimate':float(p),'CI95_pointwise':[float(l),float(h)]} for key,p,l,h in zip(METRICS,point,lo,hi)}}
        results.append(result)
    result={'scope':'Author descriptive statistics of the supplied fixed-rate geometry-only process; no independent production-code review, phase proof or Maxwell dynamics.',
            'source_manifest_sha256':sha(src/'MANIFEST.json'),'source_summary_sha256':sha(src/'SUMMARY.json'),
            'analysis_sha256':sha(Path(__file__)),'analysis_plan_sha256':sha(HERE/'GEOMETRIC_FIXED_RATE_ANALYSIS_PLAN.md'),
            'status_counts':dict(Counter(r['status'] for r in summary['results'])),'runs_used':len(values),'excluded':excluded,
            'bootstrap_resamples':10000,'statistical_unit':'one complete independent history','intervals':'95% pointwise percentile bootstrap; not simultaneous or a finite-size-bias estimate',
            'gaussian_conditional_reference':{'S2_over_S1':1,'S3_over_S1':1,'S4_over_S1':1,'W_over_S1':1,'axis_mode_fourth_ratio':1.5,'axis_shell_fourth_ratio':7/6,'winding_fourth_ratio':5/3},
            'cells':results}
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'PER_HISTORY.json').write_text(json.dumps(values,indent=2)+'\n')
    (out/'RECEIPT_VERIFICATION.json').write_text(json.dumps({'rows':bindings,'all_declared_receipt_files_hashed':True},indent=2)+'\n')
    lines=['# Declared fixed-rate formation follow-up','',result['scope'],'',f"Used {len(values)} of2496 declared histories. Status counts: {result['status_counts']}.",'','Intervals below are pointwise95% whole-history bootstrap intervals. They do not include finite-size or simulator bias.','',
           '| N | beta | runs | S1 | W | W/S1 | S4/S1 | meanT/V | slides/site |','|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    def fmt(v):return f"{v['estimate']:.6g} [{v['CI95_pointwise'][0]:.6g},{v['CI95_pointwise'][1]:.6g}]"
    for row in results:
        v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|{row['completed']}|"+'|'.join(fmt(v[k]) for k in ['S1','W','W_over_S1','S4_over_S1','time_per_volume','slides_per_site'])+'|')
    lines+=['','## Fourth-moment diagnostics','','The listed Gaussian comparison values require the additional assumptions in the analysis plan.','',
            '| N | beta | individual-mode ratio (3/2) | axis-shell ratio (7/6) | winding ratio (5/3) |','|---:|---:|---:|---:|---:|']
    for row in results:
        v=row['observables'];lines.append(f"|{row['N']}|{row['beta']}|"+'|'.join(fmt(v[k]) for k in ['axis_mode_fourth_ratio','axis_shell_fourth_ratio','winding_fourth_ratio'])+'|')
    (out/'TABLE.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'runs_used':len(values),'cells':len(results),'status_counts':result['status_counts'],'all_receipt_files_authenticated':True},indent=2))

if __name__=='__main__':main()
