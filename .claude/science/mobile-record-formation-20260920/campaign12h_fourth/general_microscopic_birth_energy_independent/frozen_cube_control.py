#!/usr/bin/env python3
"""Full weighted charge-matrix control for n/S -> alpha, not a finite-S cube.

The corresponding infinite translated-field operator has these Fourier fibers.
The normalizable-input leading coefficients were separately derived by paths.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,sys,traceback
sys.dont_write_bytecode=True
import numpy as np
import matrix_control as m

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value:raise AssertionError(name)

def run(attempt):
    out=HERE/f'FROZEN_CUBE_RESULTS_{attempt}.json'
    if out.exists():raise FileExistsError(out)
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'matrix_source_sha256':hashlib.sha256((HERE/'matrix_control.py').read_bytes()).hexdigest(),'status':'running','checks':checks,'scope':'Complete weighted charge Fourier fibers; physical fixed-field and moving-field coefficients separately reconstructed by independent paths.'}
    try:
        rows=[];balances=[]
        edges=m.geometry(8)[1];face={(0,1),(0,2),(1,3),(2,3)}
        for u in (1.,.75,.25):
            weights=[u if e in face else 1. for e in edges]
            pre=m.matrices(8,4,edge_weights=weights);post=m.matrices(8,6,edge_weights=weights)
            x=np.eye(len(pre['basis']))[:,pre['P'][0]]
            instruments={kind:[m.jump(pre,post,e,sign) for e in range(12) for sign in ((-1,1) if kind=='resolved' else (None,))] for kind in ('resolved','coherent')}
            for eps in (.02,.01,.005):
                hin,_,_,uin=m.canonical(pre,eps);hout,_,_,uout=m.canonical(post,eps)
                d=uin[:,0];hd=hin@d;h2d=hin@hd;ein=np.vdot(d,hd).real
                for sign in (-1,1,None):
                    J=m.jump(pre,post,0,sign);B,R,w,ell,mu,*_=m.coefficients(pre,post,J,x)
                    check(f'weighted u={u} sign={sign} exact leading mean identity',abs(mu+ell-({1:2,-1:2/(1+u),None:(2+u)/(1+u)}[sign]))<1e-11)
                    y=J@d;norm=np.vdot(y,y).real;phi=y/np.sqrt(norm);hphi=hout@phi
                    mean=np.vdot(phi,hphi).real;second=np.vdot(hphi,hphi).real
                    row={'u':u,'epsilon':eps,'sign':sign,'expected_mean_scaled':mu+ell,'mean_scaled':mean/eps**2,'expected_fast_variance_scaled':ell,'variance_scaled':(second-mean*mean)/eps**2,'expected_intensity_over_kappa':w,'intensity_over_kappa':norm/eps**2}
                    if eps==.005:
                        check(f'weighted u={u} sign={sign} finite canonical mean',abs(row['mean_scaled']-row['expected_mean_scaled'])<.003)
                        check(f'weighted u={u} sign={sign} finite canonical variance',abs(row['variance_scaled']-ell)<.003)
                    rows.append(row)
                for kind,Js in instruments.items():
                    de=d2=rate=0.
                    for J in Js:
                        y=J@d;hy=hout@y
                        rate+=np.vdot(y,y).real
                        de+=np.vdot(y,hy).real-np.vdot(y,J@hd).real
                        d2+=np.vdot(hy,hy).real-np.vdot(y,J@h2d).real
                    row={'u':u,'epsilon':eps,'instrument':kind,'rate_over_kappa':rate/eps**2,'expected_rate':8*(u*u+2*u+3),'epsilon2_energy_derivative_over_kappa_delta':de/eps**4,'expected_energy_derivative':4+36*u*u+32*u**3,'epsilon6_variance_derivative_over_kappa_delta2':(d2-2*ein*de)/eps**4,'expected_variance_derivative':36*(1+u*u)}
                    if eps==.005:
                        check(f'weighted u={u} {kind} full GKLS energy derivative',abs(row['epsilon2_energy_derivative_over_kappa_delta']-row['expected_energy_derivative'])<.3)
                        check(f'weighted u={u} {kind} full GKLS variance derivative',abs(row['epsilon6_variance_derivative_over_kappa_delta2']-row['expected_variance_derivative'])<.1)
                    balances.append(row)
        result['conditional_rows']=rows;result['full_GKLS_balances']=balances
        result['matrix_checks']=m.checks
        check('all complete matrix checks passed',all(row['passed'] for row in m.checks))
        result['status']='completed'
    except Exception as exc:
        result['status']='failed';result['exception']=repr(exc);result['traceback']=traceback.format_exc();raise
    finally:
        result['summary']={'passed':sum(row['passed'] for row in checks),'failed':sum(not row['passed'] for row in checks),'supporting_matrix_checks':len(m.checks)}
        out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':str(out),'status':result['status'],**result['summary']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--attempt',required=True);run(parser.parse_args().attempt)
