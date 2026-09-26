#!/usr/bin/env python3
"""Separate-chain follow-up analysis with two declared block lengths."""
from pathlib import Path
import datetime,hashlib,json
import numpy as np

HERE=Path(__file__).resolve().parent;RAW=HERE/'gauss_worm_z1_followup';OUT=RAW/'analysis'
rng=np.random.default_rng(202609211031)
cases=[]
for f in sorted(OUT.glob('*_summary.json')):
    tag=f.name.removesuffix('_summary.json');summary=json.loads(f.read_text());meta=json.loads((RAW/(tag+'.json')).read_text())
    b128=np.loadtxt(OUT/(tag+'_blocks.csv'),delimiter=',',skiprows=1,ndmin=2)[:,1:]
    assert len(b128)==summary['blocks'] and meta['samples']==summary['samples']
    profiles=[]
    for size in (128,1024):
        count=size//128;n=len(b128)//count
        b=b128[:n*count].reshape(n,count,8).mean(axis=1)
        mean=b.mean(axis=0);half=n//2
        lag=[]
        for k in range(8):
            x=b[:,k];lag.append(float(np.corrcoef(x[:-1],x[1:])[0,1]) if n>2 and min(np.std(x[:-1]),np.std(x[1:]))>1e-13 else None)
        boot=[]
        for _ in range(2000):
            m=b[rng.integers(0,n,n)].mean(axis=0)
            boot.append([m[0],m[1],m[2],m[3],m[4],m[1]/m[2],m[3]/m[4]])
        estimates=list(mean[:5])+[mean[1]/mean[2],mean[3]/mean[4]]
        interval=np.quantile(boot,[.025,.975],axis=0).T
        values={key:dict(estimate=float(estimates[i]),interval=None if n<16 else interval[i].tolist()) for i,key in enumerate(['rho','S_x1','S_x2','S_xy1','S_xy2','ratio_axis','ratio_diagonal'])}
        flags=[]
        if n<16:flags.append('fewer_than_16_complete_blocks')
        if any(x is not None and abs(x)>.2 for x in lag):flags.append('material_lag1_block_dependence')
        if summary['maximum_identical_observable_run']>size:flags.append('identical_run_exceeds_block_size')
        profiles.append(dict(block_size=size,blocks=n,discarded_samples=meta['samples']-n*size,values=values,lag1_block_correlation=lag,flags=flags,first_half_mean=b[:half].mean(axis=0).tolist(),last_half_mean=b[-half:].mean(axis=0).tolist()))
    cases.append(dict(tag=tag,metadata=meta,summary=summary,profiles=profiles))
result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),raw_identities_sha256=hashlib.sha256((OUT/'RAW_IDENTITIES.json').read_bytes()).hexdigest(),cases=cases,bootstrap_replicates=2000,scope='Adaptive finite-size equilibrium-sampler follow-up. Separate initializations, no pooling. Paired block bootstrap is descriptive; equilibrium and interval coverage are not proved. No continuum phase, exponent, quantum vacuum or physical formation-state claim.')
(OUT/'FOLLOWUP_ANALYSIS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
for c in cases:
    p=c['profiles'][1]
    print(c['tag'],'rho=',p['values']['rho'],'axis=',p['values']['ratio_axis'],'diagonal=',p['values']['ratio_diagonal'],'blocks=',p['blocks'],'fluxchanges=',c['summary']['flux_changes'],'flags=',p['flags'])
