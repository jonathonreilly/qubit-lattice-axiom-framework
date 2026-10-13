#!/usr/bin/env python3
"""Fixed-history BAO transfer with one low-redshift ruler calibration."""
from pathlib import Path
import argparse,hashlib,importlib.util,json
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.linalg import cho_factor,cho_solve

HERE=Path(__file__).resolve().parent
IC=HERE.parent/'direct_thermal_matter_bridge'
CHECKS=[]

def check(name,good,**detail):CHECKS.append(dict(name=name,passed=bool(good),**detail))
def near(name,got,want,tol,relative=False):
    delta=np.asarray(got)-np.asarray(want)
    err=float(np.max(abs(delta)/(abs(want) if relative else 1)))
    check(name,np.isfinite(err) and err<=tol,error=err,tolerance=tol,relative=relative)

def score(f,d,c,low,transfer):
    ll=c[np.ix_(low,low)];tl=c[np.ix_(transfer,low)];tt=c[np.ix_(transfer,transfer)]
    fl=cho_factor(ll,lower=True);fa=cho_factor(c,lower=True)
    qf=cho_solve(fl,f[low]);va=1/(f[low]@qf);ahat=va*(qf@d[low])
    gain=cho_solve(fl,tl.T).T;v=f[transfer]-gain@f[low]
    pred=gain@d[low]+v*ahat;schur=tt-gain@tl.T+va*np.outer(v,v)
    fs=cho_factor(schur,lower=True);rl=d[low]-ahat*f[low];rt=d[transfer]-pred
    cal=rl@cho_solve(fl,rl);tr=rt@cho_solve(fs,rt)
    allamp=(f@cho_solve(fa,d))/(f@cho_solve(fa,f));res=d-allamp*f;full=res@cho_solve(fa,res)
    return dict(amplitude_calibration_only=float(ahat),amplitude_calibration_standard_error=float(np.sqrt(va)),
                amplitude_full_profile_identity_only=float(allamp),calibration_chi2=float(cal),
                transfer_chi2=float(tr),full_profile_chi2=float(full),profile_decomposition_error=float(abs(cal+tr-full)),
                shape=f.tolist(),prediction_transfer=pred.tolist(),residual_transfer=rt.tolist(),
                residual_calibration=rl.tolist(),predictive_covariance=schur.tolist(),
                predictive_diagonal_standardized_residual=(rt/np.sqrt(np.diag(schur))).tolist())

def distances(inverse_e,z,kind,knots=None,method='adaptive'):
    points=[0.,*[v for v in ([] if knots is None else knots) if 0<v<z],z]
    if method=='adaptive':
        dm=sum(quad(inverse_e,lo,hi,epsabs=2e-12,epsrel=2e-12)[0] for lo,hi in zip(points,points[1:]))
    else:
        t,w=np.polynomial.legendre.leggauss(24)
        dm=sum((hi-lo)/2*sum(wj*inverse_e((hi+lo)/2+(hi-lo)*tj/2) for tj,wj in zip(t,w)) for lo,hi in zip(points,points[1:]))
    dh=inverse_e(z)
    if kind=='DM_over_rs':return dm
    if kind=='DH_over_rs':return dh
    if kind=='DV_over_rs':return np.cbrt(z*dm*dm*dh)
    raise ValueError(kind)

def main(freeze,out):
    for x in json.loads(freeze.read_text())['inputs']:
        check('source.'+x['path'],hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
    primary=json.loads((HERE/'PRIMARY_DATA_v1.json').read_text())
    for x in primary['files']:
        check('primary.'+Path(x['campaign_copy']).name,hashlib.sha256(Path(x['campaign_copy']).read_bytes()).hexdigest()==x['sha256'])
    arr=np.loadtxt(HERE/'data/desi_gaussian_bao_ALL_GCcomb_mean.txt',dtype=str)
    z=arr[:,0].astype(float);d=arr[:,1].astype(float);kind=arr[:,2].tolist()
    c=np.loadtxt(HERE/'data/desi_gaussian_bao_ALL_GCcomb_cov.txt')
    check('data.census',len(z)==13 and c.shape==(13,13))
    check('data.allowed_rows',np.all((z>0)&(z<=4.5)) and set(kind)=={'DV_over_rs','DM_over_rs','DH_over_rs'})
    check('data.covariance_exact_symmetric',np.array_equal(c,c.T))
    check('data.covariance_positive',np.min(np.linalg.eigvalsh(c))>0)
    check('data.offdiagonals_retained',np.count_nonzero(c-np.diag(np.diag(c)))==12)
    low=np.flatnonzero(z==np.min(z));transfer=np.flatnonzero(z>np.min(z))
    check('partition.frozen_rule',low.tolist()==[0] and transfer.tolist()==list(range(1,13)))
    check('partition.lowest_kind',z[0]==.295 and kind[0]=='DV_over_rs')
    for zi in [.1,.5,1.,2.33]:
        for typ in ['DM_over_rs','DH_over_rs','DV_over_rs']:
            got=distances(lambda zz:1.,zi,typ);near(f'geometry.constant_H.{zi}.{typ}',got,1. if typ=='DH_over_rs' else zi,1e-13)
            dm=2*(1-1/np.sqrt(1+zi));dh=(1+zi)**(-1.5);want={'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':np.cbrt(zi*dm*dm*dh)}[typ]
            near(f'geometry.EdS.{zi}.{typ}',distances(lambda zz:(1+zz)**(-1.5),zi,typ),want,1e-13)
    # Nonzero correlations and two calibration rows exercise the general formula.
    synthetic_c=np.array([[2.,.3,.2,.1],[.3,1.5,.1,.2],[.2,.1,1.8,.4],[.1,.2,.4,1.7]])
    synth=score(np.array([.3,.5,.8,1.2]),np.array([1.1,1.8,2.7,4.5]),synthetic_c,np.array([0,1]),np.array([2,3]))
    check('calibration.synthetic_decomposition',synth['profile_decomposition_error']<1e-12)
    near('calibration.synthetic_normal_equation',np.array([.3,.5])@np.linalg.solve(synthetic_c[:2,:2],synth['residual_calibration']),0.,1e-12)
    spec=importlib.util.spec_from_file_location('bao_fixed_fluid',IC/'check_thermal_matter_bridge_v3.py');model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
    histories=json.loads((IC/'evidence_v3/histories/RESULTS.json').read_text())['histories']
    output=[];ids=['supplied_LCDM_0.3','split_k0.01','equal_k0.01','split_k1e-05','equal_k1e-05','split_k1e-06','equal_k1e-06']
    for ident in ids:
        cfg=None
        if ident=='supplied_LCDM_0.3':
            inverse_e=lambda redshift:1/np.sqrt(.3*(1+redshift)**3+.7)
            alternative=inverse_e;knots=[]
        else:
            history=next(x for x in histories if x['case']['id']==ident);cfg=history['configuration'];rows=history['rows']
            check(ident+'.complete',history['success'] and len(rows)==241)
            nj=np.array([r['NJ'] for r in rows]);logr=np.log([r['Hratio'] for r in rows]);hnow=rows[-1]['HJ2']
            check(ident+'.monotone_clock',np.all(np.diff(nj)>0))
            check(ident+'.no_extrapolation',cfg['Ntotal']-np.log1p(max(z))>nj[0] and abs(nj[-1]-cfg['Ntotal'])<2e-9)
            for j,r in enumerate(rows):
                u,pu=r['state'][0],r['state'][3];A=np.exp(np.sqrt(cfg['a'])*u);F=1+cfg['s']*A*A
                CB=(1+cfg['s'])*A*A/F;rate=1+np.sqrt(cfg['a'])*pu/F
                physical=r['H2']*rate*rate/CB
                near(ident+f'.physical_interpolation.{j}',np.exp(logr[j]),np.sqrt(physical/r['HGR2']),3e-12,True)
            near(ident+'.physical_normalization',hnow,physical,3e-12,True)
            hermite=PchipInterpolator(nj,logr,extrapolate=False)
            def ie(redshift,linear=False):
                L=cfg['Lf']-np.log1p(redshift);N=cfg['Ntotal']-np.log1p(redshift);g=model.gas(float(L),256)
                rho=cfg['rho_di']*np.exp(-3*g['NJ'])+g['rho_gas'];hg=1+2*(1+cfg['k'])*cfg['Rstar']*rho/3
                lr=np.interp(N,nj,logr) if linear else float(hermite(N))
                return np.sqrt(hnow/hg)*np.exp(-lr)
            inverse_e=lambda zz:ie(zz);alternative=lambda zz:ie(zz,True)
            knots=sorted(np.expm1(cfg['Ntotal']-nj[(nj<cfg['Ntotal'])&(nj>cfg['Ntotal']-np.log1p(max(z)))]).tolist())
            for j,zi in enumerate([0.,*sorted(set(z))]):
                g=model.gas(float(cfg['Lf']-np.log1p(zi)),256)
                near(ident+f'.entropy.{j}',g['NJ'],cfg['Ntotal']-np.log1p(zi),2e-9)
        near(ident+'.E_zero',inverse_e(0),1.,3e-10)
        shape=np.array([distances(inverse_e,zi,typ,knots) for zi,typ in zip(z,kind)])
        independent=np.array([distances(inverse_e,zi,typ,knots,'fixed') for zi,typ in zip(z,kind)])
        linear=np.array([distances(alternative,zi,typ,knots) for zi,typ in zip(z,kind)])
        near(ident+'.quadrature',shape,independent,2e-7,True)
        near(ident+'.interpolation',shape,linear,2e-3,True)
        check(ident+'.positive_shape',np.isfinite(shape).all() and min(shape)>0)
        fitted=score(shape,d,c,low,transfer)
        check(ident+'.positive_amplitude',fitted['amplitude_calibration_only']>0)
        check(ident+'.profile_identity',fitted['profile_decomposition_error']<1e-9)
        near(ident+'.calibration_normal_equation',shape[low]@np.linalg.solve(c[np.ix_(low,low)],fitted['residual_calibration']),0.,1e-10)
        # The actual calibration has one row; bind its amplitude directly.
        near(ident+'.one_row_ruler',fitted['amplitude_calibration_only'],d[0]/shape[0],2e-12)
        output.append(dict(case=ident,history_configuration=cfg,quadrature_maximum_relative_difference=float(np.max(abs(shape-independent)/shape)),linear_maximum_relative_difference=float(np.max(abs(shape-linear)/shape)),**fitted))
    result=dict(scope='Fixed previously developed histories; new campaign BAO summary input; one lowest-z ruler fit, twelve transfer rows; no sound-horizon prediction, raw-catalog fit or empirical acceptance.',primary=primary,data=dict(redshift=z.tolist(),quantity=kind,value=d.tolist(),covariance=c.tolist(),calibration_indices=low.tolist(),transfer_indices=transfer.tolist()),synthetic_control=synth,models=output,checks=CHECKS,counts=dict(passed=sum(x['passed'] for x in CHECKS),failed=sum(not x['passed'] for x in CHECKS),total=len(CHECKS)))
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(counts=result['counts'],models=[{k:v for k,v in x.items() if k in ['case','amplitude_calibration_only','amplitude_calibration_standard_error','transfer_chi2','linear_maximum_relative_difference']} for x in output]),indent=2));return bool(result['counts']['failed'])
if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--freeze',type=Path,required=True);pa.add_argument('--out',type=Path,required=True);ar=pa.parse_args()
    if ar.out.exists():raise FileExistsError(ar.out)
    raise SystemExit(main(ar.freeze,ar.out))
