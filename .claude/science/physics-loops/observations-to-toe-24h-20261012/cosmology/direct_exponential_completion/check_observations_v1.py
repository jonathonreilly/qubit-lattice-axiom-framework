#!/usr/bin/env python3
"""Unfitted new histories against exposed SN/BAO and conditional PPN summaries."""
from pathlib import Path
import hashlib,importlib.util,json
import numpy as np
import mpmath as mp
from scipy.integrate import cumulative_simpson
from scipy.interpolate import PchipInterpolator
from scipy.linalg import cho_factor,cho_solve
P=Path(__file__).resolve().parent
def load(name,file):
    sp=importlib.util.spec_from_file_location(name,file);o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o);return o
ex=load('exp_observations_action',P/'check_exponential_v1.py')
sn=load('exp_observations_sn',P.parent/'direct_history_distance_comparison/check_history_distances_v2.py')
bao=load('exp_observations_bao',P.parent/'direct_bao_distance_comparison/check_bao_v2.py')
ppn=load('exp_observations_ppn',P.parent/'direct_actual_background_weak_field/check_actual_background_v1.py')
checks=[]
def ck(name,good,**kw):checks.append(dict(name=name,passed=bool(good),**kw))
def near(name,a,b,tol):
    e=float(np.max(abs(np.asarray(a)-b)));ck(name,np.isfinite(e) and e<=tol,error=e,bound=tol)
def main():
    freeze=json.loads((P/'OBSERVATION_FREEZE_v1.json').read_text())
    for z in freeze['inputs']:ck('source.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    _,chosen,z,zh,mag,c,low,high,_=sn.inputs();checks.extend(sn.CHECKS)
    cl=c[np.ix_(low,low)];ct=c[np.ix_(high,low)];ch=c[np.ix_(high,high)];fl=cho_factor(cl,lower=True)
    ones=np.ones(len(low));q=cho_solve(fl,ones);var=1/(ones@q);gain=cho_solve(fl,ct.T).T;v=np.ones(len(high))-gain@ones
    sc=ch-gain@ct.T+var*np.outer(v,v);sc=(sc+sc.T)/2;fs=cho_factor(sc,lower=True)
    def snscore(shape):
        dl=mag[low]-shape[low];M=var*(q@dl);pred=shape[high]+gain@dl+v*M;res=mag[high]-pred
        return dict(intercept_calibration_only=float(M),intercept_standard_error=float(np.sqrt(var)),transfer_chi2=float(res@cho_solve(fs,res)),shape=shape.tolist(),prediction_transfer=pred.tolist())
    # Read the already frozen public components directly; preserve published ordering.
    arr=np.loadtxt(bao.HERE/'data/desi_gaussian_bao_ALL_GCcomb_mean.txt',dtype=str)
    bz=arr[:,0].astype(float);data=arr[:,1].astype(float);kind=arr[:,2].tolist();cov=np.loadtxt(bao.HERE/'data/desi_gaussian_bao_ALL_GCcomb_cov.txt')
    oldbao=json.loads((bao.HERE/'evidence_v2/RESULTS.json').read_text())
    ck('bao.exact_row_identity',bz.tolist()==oldbao['data']['redshift'] and kind==oldbao['data']['quantity'] and data.tolist()==oldbao['data']['value'])
    ck('bao.exact_covariance',cov.tolist()==oldbao['data']['covariance']);bl=np.array([0]);bh=np.arange(1,13)
    obs=json.loads((P.parent/'direct_weak_field_inverse/OBSERVATION_INPUTS_v1.json').read_text())
    histories=json.loads((P/'evidence_v1/RESULTS.json').read_text())['histories'];outputs=[];mp.mp.dps=80
    for h in histories:
        ident=h['case']['id'];cfg=h['configuration'];rows=h['rows'];ck(ident+'.complete',h['success'] and len(rows)==241)
        nj=np.array([r['NJ'] for r in rows]);lr=np.log([r['Hratio'] for r in rows]);curve=PchipInterpolator(nj,lr,extrapolate=False);hn=rows[-1]['HJ2']
        for j,r in enumerate(rows):
            u,pu=r['state'][0],r['state'][3];al=np.sqrt(cfg['a']);E=np.exp(2*al*u);F=1+cfg['s']*E;CB=(1+cfg['s'])*E/F;rate=1+al*pu/F
            raw=r['H2']*rate*rate/CB;near(ident+f'.clock.{j}',np.exp(lr[j])/np.sqrt(raw/r['HGR2']),1.,3e-12)
        ck(ident+'.clock_domain',np.all(np.diff(nj)>0) and cfg['Ntotal']-np.log1p(max(bz))>nj[0])
        def inverse(redshift):
            L=cfg['Lf']-np.log1p(redshift);N=cfg['Ntotal']-np.log1p(redshift);g=ex.base.gas(float(L),256)
            rho=cfg['rho_di']*np.exp(-3*g['NJ'])+g['rho_gas'];hg=1+2*(1+cfg['k'])*cfg['Rstar']*rho/3
            return float(np.sqrt(hn/hg)*np.exp(-curve(N)))
        near(ident+'.normalization',inverse(0),1.,3e-10)
        shapes=[]
        for n in [1025,2049]:
            grid=np.linspace(0,1.5,n);integ=cumulative_simpson([inverse(zz) for zz in grid],x=grid,initial=0)
            shapes.append(5*np.log10((1+zh)*PchipInterpolator(grid,integ)(z)))
        near(ident+'.sn_grid',shapes[0],shapes[1],2e-5)
        knots=sorted(np.expm1(cfg['Ntotal']-nj[(nj<cfg['Ntotal'])&(nj>cfg['Ntotal']-np.log1p(max(bz)))]).tolist())
        shape=np.array([bao.distances(inverse,zz,typ,knots) for zz,typ in zip(bz,kind)])
        other=np.array([bao.distances(inverse,zz,typ,knots,'fixed') for zz,typ in zip(bz,kind)])
        near(ident+'.bao_quadrature',shape/other,1.,2e-7);bscore=bao.score(shape,data,cov,bl,bh)
        ck(ident+'.bao_positive_ruler',bscore['amplitude_calibration_only']>0)
        ck(ident+'.bao_profile_identity',bscore['profile_decomposition_error']<1e-9)
        cv=lambda x:mp.mpf(str(x));u=cv(rows[-1]['state'][0]);form=ppn.supplied_formula(u,cv(cfg['a']),cv(cfg['s']),cv(cfg['k']))
        oracle=ppn.original_metric_oracle(u,cv(cfg['a']),cv(cfg['s']),cv(cfg['k']))
        for key in form:ck(ident+'.ppn_raw.'+key,abs(form[key]-oracle[key])<mp.mpf('1e-55')*max(1,abs(form[key])))
        bands=[]
        for label,key in [('Cassini','delta_gamma'),('LLR','eta')]:
            center=cv(obs[label]['mean']);err=cv(obs[label]['reported_uncertainty'])
            bands.append(dict(source=label,prediction=mp.nstr(form[key],30),one_reported_error_inside=bool(abs(form[key]-center)<=err),two_reported_error_inside=bool(abs(form[key]-center)<=2*err)))
        outputs.append(dict(case=ident,configuration=cfg,sn=snscore(shapes[1]),bao=bscore,ppn={k:mp.nstr(v,35) for k,v in form.items()},separate_working_rectangles=bands))
    for z in freeze['inputs']:ck('unchanged.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    result=dict(scope='New exponential potential; all observations already exposed. Fixed candidate and initial state. Nuisance calibration only. No joint likelihood, scalar-range proof, empirical acceptance or TOE.',selected_rows=chosen.tolist(),calibration_indices=low.tolist(),transfer_indices=high.tolist(),models=outputs,checks=checks,counts=dict(passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks)))
    f=P/'OBSERVATION_RESULTS_v1.json';assert not f.exists();f.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(counts=result['counts'],models=[dict(case=x['case'],SN=x['sn']['transfer_chi2'],BAO=x['bao']['transfer_chi2'],bands=x['separate_working_rectangles']) for x in outputs]),indent=2))
if __name__=='__main__':main()
