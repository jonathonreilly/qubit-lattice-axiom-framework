#!/usr/bin/env python3
"""Retrospective ENS comparison; evaluation coordinates never enter fitting."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from itertools import product
import csv,hashlib,json
import numpy as np
from scipy.optimize import least_squares
from ens_andreev_resonator_model_2026_09_27 import predict,endpoint
from ens_direct_charge_check_2026_09_27 import solve

AUDIT_TIMEOUT_SEC=240
AUDIT_INPUT_PATHS=(
 'docs/ENS_CAVITY_CALIBRATED_HOLDOUT_OPEN_GATE_NOTE_2026-09-27.md',
 'scripts/ens_andreev_resonator_model_2026_09_27.py',
 'scripts/ens_direct_charge_check_2026_09_27.py',
 'scripts/data/ens_cavity_holdout_2026_09_27/Experiment.csv',
 'scripts/data/ens_cavity_holdout_2026_09_27/provenance.json',
 'scripts/data/ens_cavity_holdout_2026_09_27/PROTOCOL.md',
)
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'scripts/data/ens_cavity_holdout_2026_09_27/Experiment.csv'
SHA='0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b'
CAL_KEYS=('f01','f02','fres1','fres2','fres3')
CAL_INDEX=np.array([0,1,6,7,8])
ORDER=tuple([f'f0{j}' for j in range(1,7)]+[f'fres{j}' for j in range(1,8)])
DIV=np.array([1,2,3,4,5,6]+[1]*7)
BOUNDS=([.03,1,7,.001,0],[1,100,8.5,1,.99])
SCALES=np.array([.2,20,8,.1,.2])

def fit(target,start,cosine=False,stable_difference=False):
    n=4 if cosine else 5
    def residual(p):
        pp=np.r_[p,0.] if cosine else p
        return (predict(pp)[0][CAL_INDEX[:n]]-target)/np.array([1,2,1,1,1])[:n]
    options=dict(bounds=(BOUNDS[0][:n],BOUNDS[1][:n]),x_scale=SCALES[:n],ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=200)
    if stable_difference:options['diff_step']=1e-4
    result=least_squares(residual,start,**options)
    p=np.r_[result.x,0.] if cosine else result.x
    error=predict(p)[0][CAL_INDEX[:n]]-target
    record=dict(parameters=p.tolist(),success=bool(result.success),nfev=result.nfev,cost=float(result.cost),active_mask=result.active_mask.tolist(),calibration_residual_GHz=error.tolist())
    return p,record,result.jac

def construct(calibration):
    """Only declared calibration values are passed to the predictor construction."""
    target=np.array([calibration[k] for k in CAL_KEYS]);attempts=[]
    for tau in (.01,.2,.6):
        p,rec,jac=fit(target,[.18,20,7.75,.1,tau]);rec['start_tau']=tau
        rec['scaled_jacobian_singular_values']=np.linalg.svd(jac@np.diag(SCALES),compute_uv=False).tolist();attempts.append(rec)
    chosen=min(attempts,key=lambda r:r['cost']);p=np.array(chosen['parameters'])
    assert chosen['success'] and max(abs(np.array(chosen['calibration_residual_GHz'])))<1e-7
    assert 4*p[0]>p[3]**2/p[2], 'Quadratic stability condition'
    baseline,brec,_=fit(target[:4],[.18,20,7.75,.1],cosine=True)
    assert brec['success'] and max(abs(np.array(brec['calibration_residual_GHz'])))<1e-7
    result=dict(calibration_keys=CAL_KEYS,calibration_GHz=target.tolist(),attempts=attempts,selected=chosen,baseline_calibration=brec)
    for name,params in [('andreev',p),('cosine',baseline)]:
        f,detail=predict(params);fine,fdetail=predict(params,N=20,M=18,K=12,grid=8192)
        assert max(abs(fine-f))*1000<.001
        result[name]=dict(parameters=params.tolist(),prediction_GHz=f.tolist(),details=detail,cutoff_change_MHz=((fine-f)*1000/DIV).tolist())
    direct=[solve(20,12,ng,parameters=p)[0] for ng in (0.,.5)]
    dmean=np.mean([r['frequencies_GHz'] for r in direct],axis=0)
    assert max(abs(dmean-np.array(result['andreev']['prediction_GHz'])))*1000<.001
    assert max(r['eigen_residual_max_GHz'] for r in direct)<1e-7
    result['independent_direct']=direct
    # Central differences establish only local conditioning, not identifiability.
    steps=[1e-5,1e-3,1e-4,1e-5,1e-4]
    jac=np.column_stack([(predict(p+np.eye(5)[i]*h)[0][CAL_INDEX]-predict(p-np.eye(5)[i]*h)[0][CAL_INDEX])/(2*h) for i,h in enumerate(steps)])
    result['fifth_line_perturbations']=[]
    for khz in (-50,-10,-1,1,10,50):
        shift=np.array([0,0,0,0,khz*1e-6]);start=p+np.linalg.solve(jac,shift)
        pp,rec,_=fit(target+shift,start,stable_difference=True)
        assert rec['success'] and max(abs(np.array(rec['calibration_residual_GHz'])))<1e-7
        rec.update(fifth_line_shift_kHz=khz,prediction_GHz=predict(pp)[0].tolist());result['fifth_line_perturbations'].append(rec)
    result['rounding_corners']=[]
    for signs in product((-1,1),repeat=5):
        shift=np.array(signs)*[.0000005,.00005,.000005,.000005,.000005]
        pp,rec,_=fit(target+shift,p+np.linalg.solve(jac,shift),stable_difference=True)
        assert rec['success'] and max(abs(np.array(rec['calibration_residual_GHz'])))<1e-7
        rec.update(signs=signs,prediction_GHz=predict(pp)[0].tolist());result['rounding_corners'].append(rec)
    result['baseline_corners']=[]
    for signs in product((-1,1),repeat=4):
        shift=np.array(signs)*[.0000005,.00005,.000005,.000005]
        pp,rec,_=fit(target[:4]+shift,baseline[:4],cosine=True,stable_difference=True)
        assert rec['success'] and max(abs(np.array(rec['calibration_residual_GHz'])))<1e-7
        rec.update(signs=signs,prediction_GHz=predict(pp)[0].tolist());result['baseline_corners'].append(rec)
    result['paired_offsets']=[]
    for ng in (0.,.125,.25):
        a,da=endpoint(p,ng);b,db=endpoint(p,ng+.5)
        result['paired_offsets'].append(dict(ng=ng,prediction_GHz=((a+b)/2).tolist(),pair_split_drive_MHz=((a-b)*1000/DIV).tolist(),minimum_weight=min(da['min_weight'],db['min_weight'])))
    return result

def main():
    assert hashlib.sha256(DATA.read_bytes()).hexdigest()==SHA
    row=next(r for r in csv.DictReader(DATA.open()) if r['Experiment']=='ENS')
    calibration={key:float(row[key]) for key in CAL_KEYS}
    result=construct(calibration)
    # The first numerical access to evaluation coordinates occurs after all fits.
    observed=np.array([float(row[key]) for key in ORDER])
    for name in ('andreev','cosine'):
        result[name]['residual_drive_MHz']=((np.array(result[name]['prediction_GHz'])-observed)*1000/DIV).tolist()
    for section in ('fifth_line_perturbations','rounding_corners','baseline_corners','paired_offsets'):
        for rec in result[section]:rec['residual_drive_MHz']=((np.array(rec['prediction_GHz'])-observed)*1000/DIV).tolist()
    a=np.array(result['andreev']['residual_drive_MHz'])[2:6];b=np.array(result['cosine']['residual_drive_MHz'])[2:6]
    assert np.all(abs(a)<abs(b)), 'Declared nominal held-out improvement not reproduced'
    result.update(order=ORDER,observed_GHz=observed.tolist(),data_sha256=SHA,scope='Retrospective imported-model point comparison; finite rounding controls are not statistical or continuum bounds.')
    print(json.dumps(result,indent=2))
    print('TOTAL: PASS=3 FAIL=0 (calibration isolation, numerical controls, nominal comparison; not empirical confirmation)')
if __name__=='__main__':main()
