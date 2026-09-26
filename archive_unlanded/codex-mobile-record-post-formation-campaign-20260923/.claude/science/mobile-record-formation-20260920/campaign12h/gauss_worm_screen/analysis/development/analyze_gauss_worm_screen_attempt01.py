#!/usr/bin/env python3
"""Prespecified block screen; intervals do not establish mixing or phase."""
from pathlib import Path
import hashlib,json,datetime
import numpy as np

HERE=Path(__file__).resolve().parent;RAW=HERE/'gauss_worm_screen';OUT=RAW/'analysis'
rng=np.random.default_rng(202609211027)
cases=[]
def boot_ratio(a,b):
    # The two mode means are resampled together, preserving their block covariance.
    x=np.column_stack((a,b));unique,counts=np.unique(x,axis=0,return_counts=True)
    n=len(x)
    if np.mean(b)<1e-15:return dict(estimate=None,interval=None,reason='zero spectrum to numerical precision')
    estimate=float(np.mean(a)/np.mean(b))
    if n<16:return dict(estimate=estimate,interval=None,reason='fewer than sixteen complete blocks')
    ratios=[]
    if len(unique)<=256:
        for _ in range(2000):
            weights=rng.multinomial(n,counts/n);s=weights@unique
            ratios.append(s[0]/s[1])
    else:
        for _ in range(2000):
            s=x[rng.integers(0,n,n)].sum(axis=0);ratios.append(s[0]/s[1])
    return dict(estimate=estimate,interval=np.quantile(ratios,[.025,.975]).tolist(),reason='paired 128-sample block bootstrap; dependence between blocks unbounded')

for f in sorted(OUT.glob('*_summary.json')):
    tag=f.name.removesuffix('_summary.json');summary=json.loads(f.read_text());meta=json.loads((RAW/(tag+'.json')).read_text())
    b=np.loadtxt(OUT/(tag+'_blocks.csv'),delimiter=',',skiprows=1,ndmin=2)[:,1:]
    assert len(b)==summary['blocks'] and meta['samples']==summary['samples']
    flags=[]
    if len(b)<16:flags.append('insufficient_prespecified_block_count')
    if summary['flux_changes']==0:flags.append('no_observed_winding_change')
    if summary['observable_changes']==0:flags.append('all_observed_states_identical_in_saved_observables')
    if summary['maximum_identical_observable_run']>128:flags.append('identical_run_exceeds_block_length')
    q=len(b)//2
    first=b[:q].mean(axis=0) if q else None;last=b[-q:].mean(axis=0) if q else None
    bcor=[]
    for i in range(8):
        x=b[:,i]
        bcor.append(float(np.corrcoef(x[:-1],x[1:])[0,1]) if len(x)>2 and np.std(x)>1e-13 else None)
    if any(x is not None and abs(x)>.2 for x in bcor):flags.append('material_lag1_block_dependence')
    cases.append(dict(tag=tag,metadata=meta,summary=summary,ratios=dict(axis=boot_ratio(b[:,1],b[:,2]),diagonal=boot_ratio(b[:,3],b[:,4])),flags=flags,block_lag1_correlation=bcor,first_half_block_mean=None if first is None else first.tolist(),last_half_block_mean=None if last is None else last.tolist()))

result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),analysis_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),raw_identities_sha256=hashlib.sha256((OUT/'RAW_IDENTITIES.json').read_bytes()).hexdigest(),block_size=128,bootstrap_replicates=2000,cases=cases,scope='Separate initializations; no pooling. Descriptive finite-size equilibrium-sampler screen. Block bootstrap coverage is not established when serial dependence or lack of equilibration persists. No phase, quantum-vacuum or formation-selected-state result.')
(OUT/'SCREEN_ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n')
for c in cases:
    print(c['tag'],'rho',c['summary']['mean'][0],'axis',c['ratios']['axis'],'diagonal',c['ratios']['diagonal'],'flags',c['flags'])
