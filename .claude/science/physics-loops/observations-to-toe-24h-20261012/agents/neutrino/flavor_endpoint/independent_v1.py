#!/usr/bin/env python3
"""Small independent V1 calculation. No experimental holdout fit or root output."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import brentq

CALIBRATION = {'sin2_2theta13': 0.0851, 'sigma': 0.0024, 's_domain': [0.01,10.]}

def independent_map(s):
    J = np.array([[s,-np.sqrt(s),0.],[-np.sqrt(s),s+2,-np.sqrt(2*(s+1))],
                  [0.,-np.sqrt(2*(s+1)),s+4]])
    x, U = np.linalg.eigh(J)
    U *= np.sign(U[0,:])
    va = np.array([np.ones(3),(s-x)/np.sqrt(s),
                  (x*x-2*(s+1)*x+s*(s+1))/np.sqrt(2*s*(s+1))])
    va /= np.sqrt(np.sum(va*va,axis=0))
    w = U[0]**2
    a13 = 4*w[2]*(1-w[2])
    t13 = w[2]
    t12 = w[1]/(1-w[2])
    t23 = U[1,2]**2/(1-w[2])
    cosdelta = (U[1,0]**2-t12*(1-t23)-(1-t12)*t23*t13)/(2*np.sqrt(t12*(1-t12)*t23*(1-t23)*t13))
    poly = [1.,-3*(s+2),3*(s+1)*(s+2),-s*(s+1)*(s+2)]
    gaps = {}
    for p in (1,2):
        xp = x**p
        r31 = (xp[1]-xp[0])/(xp[2]-xp[0])
        gaps[str(p)] = {'r21_over_31':float(r31), 'r21_over_32':float(r31/(1-r31))}
    return {'s': float(s), 'x':x.tolist(), 'U_e_mu_tau':U.tolist(),
            'electron_weights':w.tolist(),'sin2_2theta13':float(a13),
            'sin2_theta13':float(t13),'sin2_theta12':float(t12),'sin2_theta23':float(t23),
            'cos_delta_standard':float(cosdelta), 'Jarlskog':0., 'fixed_mass_maps':gaps,
            'checks':{'max_analytic_vector_error':float(np.max(np.abs(va-U))),
                      'max_eigen_residual':float(np.max(np.abs(J@va-va*x))),
                      'max_poly_root_residual':float(np.max(np.abs(np.polyval(poly,x)))),
                      'orthogonality_residual':float(np.max(np.abs(va.T@va-np.eye(3)))),
                      'trace_error':float(abs(sum(x)-3*(s+2)))}}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args=parser.parse_args()
    grid=np.geomspace(*CALIBRATION['s_domain'],1001)
    maps=[independent_map(s) for s in grid]
    amplitudes=np.array([m['sin2_2theta13'] for m in maps])
    assert np.all(np.diff(amplitudes)>0)
    selected={}
    for z in (0.,-1.,1.,-1.96,1.96):
        target=CALIBRATION['sin2_2theta13']+z*CALIBRATION['sigma']
        s=brentq(lambda s:independent_map(s)['sin2_2theta13']-target,
                 *CALIBRATION['s_domain'],xtol=5e-14)
        selected[str(z)]=independent_map(s)
    check_keys=maps[0]['checks'].keys()
    checks={k:max(m['checks'][k] for m in maps) for k in check_keys}
    assert checks['max_analytic_vector_error']<2e-12
    assert checks['max_eigen_residual']<2e-11
    assert checks['orthogonality_residual']<2e-12
    result={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status':'conditional V1; no holdout fit; no root numerical output read',
            'calibration':CALIBRATION,'selected':selected,
            'grid_monotonicity':{'n':len(grid),'min_increment':float(min(np.diff(amplitudes))),
                                 'endpoint_amplitudes':[float(amplitudes[0]),float(amplitudes[-1])]},
            'checks_across_domain':checks,
            'software':{'numpy':np.__version__,'scipy':scipy.__version__},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'central':selected['0.0'],'checks':checks},indent=2))

if __name__=='__main__':
    main()
