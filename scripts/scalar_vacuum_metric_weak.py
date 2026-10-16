"""Synthetic weak metric inverse with declared lower derivative readout."""
from pathlib import Path
import sys,json,hashlib,time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
import scalar_vacuum_metric_inverse as parent
NODES,WEIGHTS=leggauss(80)

def moments(metric_low,intervals):
    # Input callback returns [r,B,Bprime,ell,ellprime,ellsecond].
    # No Bsecond, ellthird, scalar, k or potential parameter is read here.
    base=metric_low(1.0);_,b0,_,e0,e10,_=base;q0=1-e10
    def shape(r):
        row=metric_low(r);_,b,bp,e,e1,e2=row;q=1/r-e1
        rr=(r+1)/2+(r-1)/2*NODES
        low=np.array([metric_low(t) for t in rr]);qq=1/rr-low[:,4]
        integ=(r-1)/2*np.sum(WEIGHTS/(low[:,1]*rr*rr*qq))
        return q0*np.sqrt(b0)/(q*np.sqrt(b)*r*r)*np.exp(e0-e+integ)
    records=[]
    for left,right in intervals:
        length=right-left;rs=(right+left)/2+length/2*NODES;t=(rs-left)/length
        w=30/length*t*t*(1-t)**2;wp=60/length**2*t*(1-t)*(1-2*t)
        rows=np.array([metric_low(r) for r in rs]);_,b,bp,ell,e1,e2=rows.T
        gt=(b-1)/rs**2+bp/rs;gr=(b-1)/rs**2+2*b*e1/rs
        ga=b*(e2+e1**2+e1/rs)+bp*(e1+1/rs)/2
        u=(ga-gt)/(b*(1/rs-e1));h=np.array([shape(r) for r in rs]);quad=WEIGHTS*length/2
        kk=np.sum(quad*(w*(2*e1/rs-bp/(b*rs)-u*u-(bp/(2*b)-e1)*u)+wp*u))
        tcore=-(gt+gr)*w/2+b*u*wp/2+w*(bp/4-b*e1/2-2*b/rs)*u
        records.append(dict(r=rs,h=h,u=u,quad=quad,w=w,K=kk,Tcore=tcore))
    order=sorted([0,1],key=lambda i:np.mean(records[i]['h']))
    p1,p2=[records[i] for i in order]
    assert np.max(p1['h'])<np.min(p2['h'])
    hmin=min(1.,shape(1.8))
    def aa(p,eta):return np.sum(p['quad']*p['w']*p['u']**2*p['h']/(p['h']-eta))
    if p1['K'] <= 0 or p2['K'] <= 0:
        raise ValueError('Nonpositive kinetic moment')
    ratio=p1['K']/p2['K']
    def residual(eta):return aa(p1,eta)/aa(p2,eta)-ratio
    low,high=1e-8,hmin-1e-8
    if not low < high or not residual(low) < 0 < residual(high):
        raise ValueError('No strictly bracketed positive amplitude root')
    eta=brentq(residual,low,high,xtol=1e-14,rtol=1e-14)
    lam=aa(p1,eta)/(2*p1['K']);k=(1-2/np.sqrt(1+3*lam))/3;a=lam/(1+3*lam);s=(1+k)/(k*(1-3*k))
    if not np.isfinite(lam) or lam <= 1:
        raise ValueError('Outside candidate kinetic parameter domain')
    coeff=[]
    for p in records:
        X=s*p['h']/eta;Y=X-s
        coeff.append([np.sum(p['quad']*p['w']*3*(s+Y*Y)),np.sum(p['quad']*p['w']*Y*Y*np.log(Y)**2/(4*a)),np.sum(p['quad']*X*p['Tcore'])])
    coeff=np.array(coeff);hv2,h2nu=np.linalg.solve(coeff[:2,:2],coeff[:2,2])
    if not np.all(np.isfinite([hv2,h2nu])) or hv2 <= 0 or h2nu <= 0:
        raise ValueError('Outside positive candidate potential domain')
    return dict(k=k,eta=eta,lam=lam,Hv2=hv2,nu=h2nu/hv2,
       calibration_intervals=intervals[:2],later_intervals=intervals[2:],
       kinetic_residuals=[p['K']-aa(p,eta)/(2*lam) for p in records],
       potential_residuals=(coeff[:,2]-coeff[:,:2]@np.array([hv2,h2nu])).tolist(),
       inverse_ratio_derivative=(residual(eta+1e-6)-residual(eta-1e-6))/2e-6,
       potential_condition=float(np.linalg.cond(coeff[:2,:2])),
       minimum_shape=hmin,maximum_shape=max(1.,shape(1.8)),
       profile_r=[1,1.2,1.4,1.6,1.8],profile_Y=[s*(shape(r)/eta-1) for r in [1,1.2,1.4,1.6,1.8]])

def controls():
    checks=[];results=[];start=time.time()
    intervals=[(1.02,1.12),(1.16,1.30),(1.40,1.55),(1.60,1.78)]
    for i,(k,hv,nu,z0,v0,b0,deform) in enumerate([(0.1,.03,1.2,1.4,.22,.9,0),(.22,.05,.7,1.2,-.12,.95,0),(.1,.03,1.2,1.4,.22,.9,.15)]):
        rhs,jets,pot,truth=parent.make_generator(k,hv,nu,deform)
        sol=solve_ivp(rhs,(1,1.8),[z0,v0,b0,0],method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True)
        assert sol.success
        def metric_low(r):
            state=sol.sol(r);jet=jets(r,state)
            return [r,state[2],jet[2],state[3],jet[4],jet[5]]
        try:
            result=moments(metric_low,intervals)
        except ValueError as error:
            checks.append(dict(name=f'case{i}_inverse_admitted',passed=False,error=str(error)))
            continue
        checks.append(dict(name=f'case{i}_inverse_admitted',passed=True))
        result['truth']=truth;result['deformation']=deform
        result['Y_max_error']=float(np.max(np.abs(np.array(result['profile_Y'])-sol.sol(result['profile_r'])[0]**2)))
        for n,cond in [('k',abs(result['k']-k)<1e-7),('Y',result['Y_max_error']<1e-6),('later_kinetic',max(abs(x) for x in result['kinetic_residuals'][2:])<1e-8)]:checks.append(dict(name=f'case{i}_{n}',passed=bool(cond)))
        if not deform:
            for n,cond in [('Hv2',abs(result['Hv2']-hv**2)<1e-8),('nu',abs(result['nu']-nu)<1e-6),('later_potential',max(abs(x) for x in result['potential_residuals'][2:])<1e-8)]:checks.append(dict(name=f'case{i}_{n}',passed=bool(cond)))
        else:checks.append(dict(name='changed_potential_later_rejection',passed=max(abs(x) for x in result['potential_residuals'][2:])>1e-8))
        results.append(result)
    output={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parent_generator_sha256':hashlib.sha256(Path(parent.__file__).read_bytes()).hexdigest(),'checks':checks,'results':results,'elapsed':time.time()-start,'new_observed_arrays':0,'empirical_tests':0,'status':'conditional synthetic lower-derivative moment inverse; no certified observation errors'}
    return output
