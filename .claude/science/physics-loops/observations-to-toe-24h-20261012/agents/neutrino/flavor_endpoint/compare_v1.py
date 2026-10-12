#!/usr/bin/env python3
"""Process only published standard-family summaries/grid; never extrapolate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import numpy as np

def crossings(x,y,level):
    inside=np.flatnonzero(y<=level)
    assert len(inside)>0 and inside[0]>0 and inside[-1]<len(x)-1
    assert np.all(np.diff(inside)==1)
    a,b=int(inside[0]),int(inside[-1])
    return [float(np.interp(level,[y[a],y[a-1]],[x[a],x[a-1]])),
            float(np.interp(level,[y[b],y[b+1]],[x[b],x[b+1]]))]

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--grid',type=Path,required=True)
    p.add_argument('--v1',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    data=np.loadtxt(args.grid,delimiter=',',skiprows=8)
    dm=np.unique(data[:,0]); th=np.unique(data[:,1])
    assert data.shape==(len(dm)*len(th),3)
    order=np.lexsort((data[:,1],data[:,0]))
    data=data[order]
    D,T=np.meshgrid(dm,th,indexing='ij')
    assert np.array_equal(D.ravel(),data[:,0])
    assert np.array_equal(T.ravel(),data[:,1])
    raw=data[:,2].reshape(D.shape)
    idx=np.unravel_index(np.argmin(raw),raw.shape)
    chi=raw-raw[idx]
    intervals={str(level):{'sin2_theta12':crossings(th,np.min(chi,axis=0),level),
                          'delta21_1e5_eV2':crossings(dm,np.min(chi,axis=1),level)}
               for level in (1.,3.841458820694124,9.)}
    local=[]
    for width in (3,5,8):
        sl=(slice(idx[0]-width,idx[0]+width+1),slice(idx[1]-width,idx[1]+width+1))
        a=(D[sl]-dm[idx[0]]).ravel()/.1
        b=(T[sl]-th[idx[1]]).ravel()/.01
        design=np.column_stack([np.ones_like(a),a,b,a*a,2*a*b,b*b])
        beta=np.linalg.lstsq(design,chi[sl].ravel(),rcond=None)[0]
        Q=np.array([[beta[3],beta[4]],[beta[4],beta[5]]])
        scale=np.diag([.1,.01])
        cov=scale@np.linalg.inv(Q)@scale
        center=np.array([dm[idx[0]],th[idx[1]]])-scale@np.linalg.solve(Q,beta[1:3])/2
        local.append({'half_width':width,'n_points':int(len(a)),
                      'fitted_center_dm21_1e5_sin2theta12':center.tolist(),
                      'covariance_order_dm21_1e5_sin2theta12':cov.tolist(),
                      'rho':float(cov[0,1]/np.sqrt(cov[0,0]*cov[1,1])),
                      'max_quadratic_fit_residual':float(np.max(np.abs(design@beta-chi[sl].ravel())))})
    v1=json.loads(args.v1.read_text())['selected']
    bands={key:[min(v1['-1.96'][key],v1['1.96'][key]),
                max(v1['-1.96'][key],v1['1.96'][key])]
           for key in ('s','sin2_theta13','sin2_theta12','sin2_theta23')}
    for pp in ('1','2'):
        for key in ('r21_over_31','r21_over_32'):
            vals=[v1[z]['fixed_mass_maps'][pp][key] for z in ('-1.96','1.96')]
            bands[f'p{pp}_{key}']=[min(vals),max(vals)]
    d21lo,d21hi=(7.50-.12)*1e-5,(7.50+.12)*1e-5
    d32lo,d32hi=(2.43-.03)*1e-3,(2.43+.04)*1e-3
    rectangle={'r21_over_31':[d21lo/(d32hi+d21lo),d21hi/(d32lo+d21hi)],
               'r21_over_32':[d21lo/d32hi,d21hi/d32lo],
               'note':'Endpoint rectangle of separate 1-sigma profile/HPD summaries, NOT joint CI'}
    out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'grid':{'file':str(args.grid),'sha256':hashlib.sha256(args.grid.read_bytes()).hexdigest(),
                 'shape':list(raw.shape),'sampled_best_fit':{'delta21_1e5_eV2':float(dm[idx[0]]),
                 'sin2_theta12':float(th[idx[1]]),'raw_delta_chi2':float(raw[idx])},
                 'domain':{'delta21_1e5_eV2':[float(dm[0]),float(dm[-1])],
                           'sin2_theta12':[float(th[0]),float(th[-1])]},
                 'profile_intervals':intervals,'local_quadratic_diagnostics':local},
         'V1_DayaBay_central_plusminus_1p96sigma_diagnostic_bands':bands,
         'target_gap_rectangle':rectangle,
         'JUNO_V1_evaluation':{'in_grid':bool(th[0]<=bands['sin2_theta12'][0] and bands['sin2_theta12'][1]<=th[-1]),
                              'delta_chi2_for_V1':None,'reason':'V1 outside grid; no extrapolation'},
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
