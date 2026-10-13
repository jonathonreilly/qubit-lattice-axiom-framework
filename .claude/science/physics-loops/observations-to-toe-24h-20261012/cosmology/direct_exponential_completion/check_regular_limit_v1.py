#!/usr/bin/env python3
"""Personally authored regular full three-field limiting evolution."""
from pathlib import Path
import hashlib,importlib.util,json,time
import numpy as np
from scipy.integrate import solve_ivp
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('exp_limit_inputs',P/'check_exponential_v1.py');ex=importlib.util.module_from_spec(sp);sp.loader.exec_module(ex)
c=ex.base.calibration(0);c['nu']=ex.base.INPUTS['nu'];c['xi']=np.sqrt(c['Rstar']*c['rho_di']);c['yi']=np.sqrt(c['Rstar']*ex.base.gas(0,256)['rho_gas'])
checks=[]
def ck(n,v,**kw):checks.append(dict(name=n,passed=bool(v),**kw))
def quantities(L,z):
    u,X,Y,pu,vx,vy=z;gas=ex.base.gas(float(L),256);sx=c['xi']*np.exp(-1.5*gas['NJ']);sy=c['yi']*np.exp(-2*gas['NJ'])
    x,y=sx*X,sy*Y;p=np.array([pu,sx*vx,sy*vy]);t=np.exp(-u);D=1+2*(x*x+y*y)/3;nu=c['nu']
    g=t*np.array([.25,4/(9*D),1/(3*D)]);dg=np.zeros((3,3));dg[0,:]=-g;dg[1,1:]=-4*x*g[1:]/(3*D);dg[2,1:]=-4*y*g[1:]/(3*D)
    V=x*x/2+y*y/3+nu*u*u/2;W=1.5*(1-t)**2+t*t*V
    dW=np.array([3*t*(1-t)+t*t*(nu*u-2*V),t*t*x,2*t*t*y/3])
    dust=c['rho_di']*np.exp(-3*gas['NJ']);sig=c['Rstar']*(dust+gas['rho_gas']);pressure=c['Rstar']*gas['P'];trace=c['Rstar']*(dust+gas['tau_gas']);B=1+2*sig/3;h=-(sig+pressure)/B
    connection=(p*(p@dg)-dg@(p*p)/2)/g;force=dW.copy();force[0]+=t*trace/2
    acc=-(3+h)*p-connection-force/(g*B);T=g@(p*p);C=2*(W+sig*(1-2*t))/(3*B)+T/3+t*pu-1+t
    return dict(sx=sx,sy=sy,gas=gas,g=g,dg=dg,p=p,W=W,dW=dW,acc=acc,B=B,h=h,C=C,trace=trace,sig=sig,T=T)
def rhs(L,z):
    q=quantities(L,z);u,X,Y,pu,vx,vy=z
    return np.array([pu,vx+1.5*X,vy+2*Y,q['acc'][0],q['acc'][1]/q['sx']+1.5*vx,q['acc'][2]/q['sy']+2*vy])/q['gas']['cT']
def main():
    freeze=json.loads((P/'REGULAR_LIMIT_FREEZE_v1.json').read_text())
    for z in freeze['inputs']:ck('source.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    grid=np.linspace(0,c['Lf'],241);runs=[]
    for method,rtol,atol,step in [('DOP853',1e-10,1e-12,.0125),('Radau',2e-10,2e-12,.025)]:
        start=time.monotonic();sol=solve_ivp(rhs,(0,c['Lf']),[0,1,1,0,-1.5,-2],method=method,rtol=rtol,atol=atol,max_step=step,t_eval=grid)
        ck(method+'.complete',sol.success and len(sol.t)==241);rows=[]
        for L,z in zip(sol.t,sol.y.T):
            q=quantities(float(L),z);rows.append(dict(L=float(L),state=z.tolist(),NJ=q['gas']['NJ'],C_exp=float(q['C']),HGR2=float(q['B'])))
        runs.append(dict(method=method,nfev=sol.nfev,elapsed_seconds=time.monotonic()-start,success=bool(sol.success),message=sol.message,rows=rows))
    A=np.array([r['state'] for r in runs[0]['rows']]);B=np.array([r['state'] for r in runs[1]['rows']]);e=np.max(abs(A-B)/np.maximum(1,abs(B)));ck('method_refinement',e<3e-7,maximum_normalized_state_difference=float(e),bound=3e-7)
    histories=json.loads((P/'evidence_v1/RESULTS.json').read_text())['histories'];comparison=[]
    for h in histories:
        if not h['case']['refined']:continue
        k=h['case']['k'];z=np.array([r['state'] for r in h['rows']]);coeff=np.array([r['C_exp'] for r in runs[0]['rows']]);actual=(np.array([r['Hratio'] for r in h['rows']])**2-1)/k
        d=np.max(abs(z-A)/np.maximum(1,abs(A)),axis=0);res=actual-coeff
        ck(h['case']['id']+'.same_L',np.array_equal([r['L'] for r in h['rows']],grid))
        comparison.append(dict(case=h['case']['id'],k=k,maximum_normalized_state_difference=d.tolist(),maximum_coefficient_residual=float(np.max(abs(res))),coefficient_residual=res.tolist(),finite_scaled_physical_correction=actual.tolist()))
    for z in freeze['inputs']:ck('unchanged.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    out=dict(scope='Regular new-action limit and exposed finite-k convergence diagnostics. Conditional compact-solution theorem; no rigorous history error constant or empirical test.',configuration=c,runs=runs,comparison=comparison,checks=checks,counts=dict(passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks)))
    f=P/'REGULAR_LIMIT_RESULTS_v1.json';assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print([{k:v for k,v in x.items() if k not in ['coefficient_residual','finite_scaled_physical_correction']} for x in comparison]);return bool(out['counts']['failed'])
if __name__=='__main__':raise SystemExit(main())
