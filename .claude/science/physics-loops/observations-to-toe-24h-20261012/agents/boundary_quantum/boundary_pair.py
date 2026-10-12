"""Reproducible pair-law analysis. Read-only XLSX extraction; no workbook edits.

Run `python3 boundary_pair.py calibrate`, then (after preserving the returned
freeze) `python3 boundary_pair.py test`. Source metadata and caveats are recorded
in SOURCE_MAP_CORRECTION_PREFIT.json. All residual scores are conditional.
"""
import os
for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_v] = '1'
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math, sys, time, zipfile
import xml.etree.ElementTree as ET
import numpy as np
from scipy.optimize import least_squares, brentq, minimize_scalar

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RUNTIME / 'boundary_quantum'
SOURCE = OUT / 'song_Figure4_v1.xlsx'
NS = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def guard():
    deadline = json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert time.time() < deadline, 'Campaign deadline reached'
    for name in ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json', 'STOP_REQUESTED', 'USER_STOP_REQUESTED'):
        assert not (RUNTIME/name).exists(), name

def stamp():
    return datetime.now(timezone.utc).isoformat()

def write(path, obj):
    path.write_text(json.dumps(obj, indent=2, allow_nan=False)+'\n')

def extract(angles):
    """Only requested measured cells enter the returned data structure."""
    with zipfile.ZipFile(SOURCE) as z:
        root = ET.fromstring(z.read('xl/worksheets/sheet4.xml'))
    wanted = {f'{col}{a//20+2}' for a in angles for col in 'ABCEFG'}
    vals = {c.get('r'): float(c.find('x:v', NS).text)
            for c in root.findall('.//x:c', NS) if c.get('r') in wanted}
    result = []
    for j, (basis, cols) in enumerate((('H','EFG'), ('D','ABC'))):
        for angle in angles:
            row = angle//20+2
            result.append(dict(basis=basis, j=j, angle=angle,
                value=vals[f'{cols[1]}{row}'], error=vals[f'{cols[2]}{row}'],
                source_cells=f'{cols[0]}{row}:{cols[2]}{row}'))
    return result

def E(c, k):
    c = np.clip(np.asarray(c, dtype=float), -1, 1)
    e0 = -1+2*np.arccos(c)/np.pi
    # Stable weighted probabilities, including exact endpoints.
    wp = (1+e0)/2*np.exp(-k*c)
    wm = (1-e0)/2*np.exp(k*c)
    return (wp-wm)/(wp+wm)

def direct_geometry(theta, k):
    """Independent azimuth-wedge integration of original response functions."""
    cuts = sorted(set([0., 2*np.pi, np.pi/2, 3*np.pi/2,
                        (theta+np.pi/2)%(2*np.pi), (theta+3*np.pi/2)%(2*np.pi)]))
    probs = np.zeros((2,2)); Z = 0.
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        phi = (lo+hi)/2
        a = 1 if np.cos(phi)>0 else -1
        b = -1 if np.cos(phi-theta)>0 else 1
        w = (hi-lo)/(2*np.pi)*np.exp(-k*np.cos(theta)*a*b)
        probs[(a+1)//2,(b+1)//2] += w
        Z += w
    probs /= Z
    return Z, float(np.sum(probs*np.array([[1,-1],[-1,1]]))), probs

def algebra_checks():
    worst = dict(correlation=0., normalization=0., marginal=0., oddness=0.)
    for theta in np.linspace(0, np.pi, 127):
        c = np.cos(theta); e0 = -1+2*theta/np.pi
        for k in (0., .1, .5, 1., 5., 20.):
            z, eg, p = direct_geometry(theta, k)
            worst['correlation'] = max(worst['correlation'], abs(eg-float(E(c,k))))
            zf = np.cosh(k*c)-e0*np.sinh(k*c)
            worst['normalization'] = max(worst['normalization'], abs(z-zf)/zf)
            worst['marginal'] = max(worst['marginal'], *abs(p.sum(axis=0)-.5), *abs(p.sum(axis=1)-.5))
            worst['oddness'] = max(worst['oddness'], abs(float(E(c,k)+E(-c,k))))
    assert max(worst.values()) < 2e-13
    return worst

def predict(params, angles, j, model='boundary'):
    # Each scan: log(mean count), visibility, physical analyzer-angle offset deg.
    p = np.asarray(params)
    m = np.exp(p[3*j]); v = p[3*j+1]; phi = p[3*j+2]
    delta = 2*np.asarray(angles)-45*j-phi
    c = np.cos(np.deg2rad(2*delta))
    corr = c if model == 'quantum' else -E(c, 0 if model == 'triangular' else p[6])
    return m*(1+v*corr)

def vector_predict(p, rows, model):
    return np.array([float(predict(p,r['angle'],r['j'],model)) for r in rows])

def limits(model):
    low = [np.log(1), 0., -10.]*2
    high = [np.log(1e6), 1., 10.]*2
    if model == 'boundary': low += [0.]; high += [40.]
    return np.array(low), np.array(high)

def fit_model(rows, model, fixed_k=None, initial=None):
    y = np.array([r['value'] for r in rows]); sig=np.array([r['error'] for r in rows])
    lo,hi = limits(model)
    x0 = np.array([np.log(13000), .96, 0., np.log(13000), .96, 0.]+([.5] if model=='boundary' else []))
    if initial is not None: x0=np.array(initial)
    if fixed_k is not None:
        lo=lo[:6];hi=hi[:6];x0=x0[:6]
    def full(p): return np.r_[p, fixed_k] if fixed_k is not None else p
    def fun(p): return (vector_predict(full(p),rows,model)-y)/sig
    starts = [x0]
    if initial is None:
        for ph in (-5., 5.):
            st=x0.copy();st[[2,5]]=ph;starts.append(st)
        if model=='boundary' and fixed_k is None:
            for k in (0.,1.,3.,10.,30.):
                st=x0.copy();st[-1]=k;starts.append(st)
    best=None
    for st in starts:
        fit=least_squares(fun,np.clip(st,lo+1e-10,hi-1e-10),bounds=(lo,hi),
            xtol=1e-12, ftol=1e-12, gtol=1e-10, max_nfev=1500)
        if best is None or sum(fit.fun**2)<sum(best.fun**2): best=fit
    return best, full(best.x)

def numerical_jac(p, rows, model):
    p=np.array(p,dtype=float); result=np.zeros((len(rows),len(p)))
    for j in range(len(p)):
        h=1e-5 if j%3 != 1 else 1e-6
        pp=p.copy();pm=p.copy();pp[j]+=h;pm[j]-=h
        result[:,j]=(vector_predict(pp,rows,model)-vector_predict(pm,rows,model))/(2*h)
    return result

def decode(p,model):
    a={basis:dict(mean_count=float(np.exp(p[3*j])),visibility=float(p[3*j+1]),
                  analyzer_offset_degrees=float(p[3*j+2])) for j,basis in enumerate(('H','D'))}
    a['k']=float(p[6]) if model=='boundary' else (0. if model=='triangular' else None)
    return a

def calibrate():
    guard()
    protocol=json.loads((HERE/'SOURCE_MAP_CORRECTION_PREFIT.json').read_text())
    rows=extract(protocol['calibration_degrees'])
    test_template=[dict(j=j,basis=basis,angle=a) for j,basis in enumerate(('H','D')) for a in protocol['test_degrees']]
    results={'created_at':stamp(),'protocol_sha256':hashlib.sha256((HERE/'SOURCE_MAP_CORRECTION_PREFIT.json').read_bytes()).hexdigest(),
             'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'algebra_checks':algebra_checks(),'calibration_data':rows,'prediction_settings':test_template,'models':{}}
    for model in ('boundary','quantum','triangular'):
        guard(); fit,p=fit_model(rows,model)
        J=numerical_jac(p,rows,model)/np.array([r['error'] for r in rows])[:,None]
        cov=np.linalg.inv(J.T@J)
        jt=numerical_jac(p,test_template,model); pcov=jt@cov@jt.T
        results['models'][model]={'parameters':p.tolist(),'decoded':decode(p,model),'calibration_weighted_square':float(sum(fit.fun**2)),
            'calibration_residuals':fit.fun.tolist(),'n_data':len(rows),'n_parameters':len(p),
            'fit_success':bool(fit.success),'active_bounds':fit.active_mask.tolist(),
            'normal_matrix_condition':float(np.linalg.cond(J.T@J)),
            'local_parameter_covariance':cov.tolist(),'predicted_test_mean':vector_predict(p,test_template,model).tolist(),
            'local_prediction_covariance':pcov.tolist(),'local_test_prediction_sd':np.sqrt(np.diag(pcov)).tolist()}
    # Cal-only profile at fixed k, useful even when diagonal Gaussian model is inadequate.
    bp=results['models']['boundary']['parameters']; kbest=bp[-1]; bestscore=results['models']['boundary']['calibration_weighted_square']
    grid=np.unique(np.r_[np.linspace(0,1.5,61),[2.,3.,5.,10.,20.,40.,kbest]])
    profile=[]
    for k in grid:
        guard();ff,p=fit_model(rows,'boundary',fixed_k=float(k),initial=bp)
        profile.append(dict(k=float(k),weighted_square=float(sum(ff.fun**2)),parameters=p.tolist()))
    results['profile']=profile
    def dp(k):
        ff,_=fit_model(rows,'boundary',fixed_k=float(k),initial=bp)
        return sum(ff.fun**2)-bestscore-3.841458820694124
    intervals=[]
    for aa,bb in zip(profile[:-1],profile[1:]):
        if (aa['weighted_square']-bestscore-3.841458820694124)*(bb['weighted_square']-bestscore-3.841458820694124)<0:
            intervals.append(float(brentq(dp,aa['k'],bb['k'],xtol=1e-11)))
    results['conditional_profile_delta_3p841459_crossings']=intervals
    results['uncertainty_warning']='Local covariance/profile uses independent Gaussian published errors, without reduced-score rescaling. If calibration does not fit, these quantify curvature inside a misspecified observation map, not validated confidence coverage. Boundary-active fits make local normal approximation unreliable.'
    write(HERE/'CALIBRATION_AND_PREDICTIONS_FREEZE.json',results)
    print(json.dumps({m:{k:v for k,v in d.items() if k in ('decoded','calibration_weighted_square','active_bounds','normal_matrix_condition')} for m,d in results['models'].items()},indent=2))

def test():
    guard()
    f=HERE/'CALIBRATION_AND_PREDICTIONS_FREEZE.json'
    res=json.loads(f.read_text()); protocol=json.loads((HERE/'SOURCE_MAP_CORRECTION_PREFIT.json').read_text())
    rows=extract(protocol['test_degrees'])
    out={'test_numerical_read_at':stamp(),'calibration_freeze_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
         'scope':'Frozen parameters used; no test retuning. Public model-development holdout; partial prior numeric and full graphical exposure documented.',
         'data':rows,'models':{}}
    yy=np.array([r['value'] for r in rows]); ss=np.array([r['error'] for r in rows])
    new=np.array([r['angle'] in protocol['genuine_new_absolute_dot_product_test_degrees'] for r in rows])
    for model,md in res['models'].items():
        mu=np.array(md['predicted_test_mean']); cov=np.array(md['local_prediction_covariance'])+np.diag(ss**2)
        rr=yy-mu; standardized=rr/np.sqrt(np.diag(cov))
        out['models'][model]={'test_weighted_square_fixed_parameters':float(sum((rr/ss)**2)),
            'test_weighted_square_with_local_correlated_prediction_uncertainty':float(rr@np.linalg.solve(cov,rr)),
            'new_angle_weighted_square_fixed_parameters':float(sum((rr[new]/ss[new])**2)),
            'n_test':len(rows),'n_new_angle':int(sum(new)),
            'observed_minus_predicted':rr.tolist(),'marginal_standardized_residual_including_cal_uncertainty':standardized.tolist(),
            'no_p_value':'Not a validated statistical exclusion. Source angle mapping, selection/detection response, calibration model adequacy, and published-error covariance remain conditional.'}
    write(HERE/'HELDOUT_RESULTS.json',out)
    print(json.dumps({m:{k:v for k,v in d.items() if 'square' in k or k.startswith('n_')} for m,d in out['models'].items()},indent=2))

if __name__=='__main__':
    {'calibrate':calibrate,'test':test}[sys.argv[1]]()
