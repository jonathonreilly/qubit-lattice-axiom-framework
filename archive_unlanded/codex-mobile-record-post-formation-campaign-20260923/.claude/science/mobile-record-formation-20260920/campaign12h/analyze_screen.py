#!/usr/bin/env python3
"""Trajectory bootstrap of exploratory finite-cube comparisons."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
rng=np.random.default_rng(719205)
report=[]
for path in sorted(HERE.glob('cubic_L8_p*_e*.json')):
    data=json.loads(path.read_text());raw=np.load(path.with_suffix('.npz'))['raw']
    n=len(raw);indices=rng.integers(n,size=(4000,n));rows=[]
    for step in (5,10,15,20):
        values=raw[:,step,:];means=values[indices].mean(axis=1);mu=values.mean(axis=0)
        transforms={'density':lambda x:x[...,0],
            'per_record_response_gain':lambda x:(data['rho0']+x[...,5])/x[...,0],
            'S0_per_record':lambda x:x[...,1]/x[...,0],
            'Smin_per_record':lambda x:x[...,2]/x[...,0],
            'bond_alignment_given_pair':lambda x:x[...,3]/x[...,4],
            'radius_two_multiple_probability':lambda x:x[...,8],
            'mean_absolute_component_residual':lambda x:x[...,9]}
        row={'tau':data['rows'][step]['tau']}
        for key,fn in transforms.items():
            est=fn(mu);lo,hi=np.quantile(fn(means),[.025,.975])
            row[key]={'estimate':float(est),'bootstrap_95_percentile':[float(lo),float(hi)]}
        # Finite interval rate, averaged over independent trajectories.
        dt=(data['rows'][step]['tau']-data['rows'][step-1]['tau'])/(6*data['epsilon'])
        rates=(raw[:,step,10]-raw[:,step-1,10])/dt
        row['successful_hops_per_site_per_time']={'estimate':float(rates.mean()),'standard_error':float(rates.std(ddof=1)/np.sqrt(n))}
        rows.append(row)
    report.append({'case':path.stem,'replicates':n,'vertices':data['vertices'],'rows':rows})
    row=rows[1]
    print(path.stem,'tau=2',json.dumps({k:row[k] for k in ('density','per_record_response_gain','S0_per_record','Smin_per_record','successful_hops_per_site_per_time')}))
(HERE/'SCREEN_ANALYSIS.json').write_text(json.dumps({'analysis':'exploratory finite-volume estimates; pointwise trajectory-bootstrap intervals, no phase inference','bootstrap_resamples':4000,'bootstrap_seed':719205,'cases':report},indent=2)+'\n')
