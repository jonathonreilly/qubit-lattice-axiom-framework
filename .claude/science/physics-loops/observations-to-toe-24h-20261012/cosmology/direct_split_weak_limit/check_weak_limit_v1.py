#!/usr/bin/env python3
"""Conditional coefficient limit; regular transverse dynamics, not finite-k repair."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, time
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
IC=HERE.parent/'direct_thermal_matter_bridge'
spec=importlib.util.spec_from_file_location('fixed_gas_for_limit',IC/'check_thermal_matter_bridge_v3.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
CHECKS=[]

def check(name,good,**detail):CHECKS.append(dict(name=name,passed=bool(good),**detail))
def near(name,got,want,tol):
    err=float(np.max(np.abs(np.asarray(got)-np.asarray(want))/np.maximum(1.,np.abs(want))))
    check(name,np.isfinite(err) and err<=tol,normalized_error=err,tolerance=tol)

def symbolic():
    k=sp.symbols('k',positive=True);u,x,y,nu=sp.symbols('u x y nu',real=True)
    a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));al=sp.sqrt(a);D=1+sp.Rational(2,3)*(1+k)*(x*x+y*y)
    F=1+s*sp.exp(2*al*u);J=1+(1-3*a)*s*sp.exp(2*al*u)
    K=[J/F**2,(1+s)*4*k/(9*F*D),(1+s)*k/(3*F*D)]
    fc=k*(1+s)/2+al*(s*k-1)*u+2*a*(1+s)*u*u/k
    U=(1+s)*(sp.Rational(3,2)+fc*x*x+k*(1+s)*y*y/3+nu*u*u/2+sp.Rational(3,2)*s*sp.exp(4*al*u))/F**2
    D0=1+sp.Rational(2,3)*(x*x+y*y);data=[]
    candidates=[('U_zero_exact',sp.cancel(U.subs(u,0)-sp.Rational(3,2)-k*(x*x/2+y*y/3)),sp.Integer(0),False),
                ('K_u',sp.cancel(K[0].subs(u,0)/k),sp.Rational(1,4),True),
                ('K_x',sp.cancel(K[1].subs(u,0)/k),4/(9*D0),True),
                ('K_y',sp.cancel(K[2].subs(u,0)/k),1/(3*D0),True),
                ('U_u',sp.simplify(sp.diff(U,u).subs(u,0)/k),-x*x-sp.Rational(2,3)*y*y,True),
                ('U_uu',sp.simplify(k*sp.diff(U,u,2).subs(u,0)),x*x,True),
                ('alpha_B',sp.simplify((al/F).subs(u,0)/k),sp.Rational(1,2),True)]
    for name,expr,want,do_limit in candidates:
        got=sp.limit(expr,k,0,dir='+') if do_limit else expr
        residue=sp.factor(sp.cancel(got-want));check('symbolic.'+name,residue==0,residue=str(residue))
        data.append(dict(name=name,original=str(expr),limit=str(got),expected=str(want)))
    return data

def raw_coefficients(k,v,x,y,nu):
    a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));al=mp.sqrt(a);u=k*k*v
    def original(t):
        A=mp.exp(al*t);F=1+s*A*A;D=1+mp.mpf(2)/3*(1+k)*(x*x+y*y)
        ku=(1-3*a*s*A*A)/F+mp.mpf(3)/4*(2*al*s*A*A/F)**2
        K=[ku,(1+s)*4*k/(9*F*D),(1+s)*k/(3*F*D)]
        V0=mp.mpf('1.5')+(k/2-al*t+2*a*t*t/k)*x*x+k*y*y/3+nu*t*t/2
        V1=(k/2+al*k*t+2*a*t*t/k)*x*x+k*y*y/3
        U=(1+s)*(V0+s*V1+mp.mpf('1.5')*s*A**4)/F**2
        return K,U,al/F,(1+s)*A*A/F
    K,U,ab,cb=original(u)
    return [* [z/k for z in K],(U-mp.mpf('1.5'))/k,ab/k,cb,
            mp.diff(lambda t:original(t)[1],u)/k,
            k*mp.diff(lambda t:original(t)[1],u,2)]

def coefficient_controls():
    rows=[]
    with mp.workdps(80):
        for i,values in enumerate([('.2','.7','-.4','1'),('-2','1.3','.9','2'),('3','-.8','1.2','.4')]):
            v,x,y,nu=map(mp.mpf,values);D=1+mp.mpf(2)/3*(x*x+y*y)
            want=[mp.mpf(1)/4,4/(9*D),1/(3*D),x*x/2+y*y/3,mp.mpf(1)/2,mp.mpf(1),v*x*x-x*x-2*y*y/3,x*x]
            errors=[]
            for power in [4,6,8,10]:
                k=mp.mpf(10)**(-power);got=raw_coefficients(k,v,x,y,nu)
                err=max(abs(g-w)/max(1,abs(w)) for g,w in zip(got,want));errors.append(err)
                check(f'coefficient.{i}.{power}',err<=100*k,error=mp.nstr(err,25),bound=mp.nstr(100*k,25))
                rows.append(dict(point=values,k=mp.nstr(k,12),actual=[mp.nstr(t,35) for t in got],limit=[mp.nstr(t,35) for t in want],normalized_error=mp.nstr(err,25)))
            check(f'coefficient.{i}.decreasing',all(b<a for a,b in zip(errors,errors[1:])))
    return rows

def background(L,cfg):
    g=model.gas(float(L),256)
    dust=cfg['rho_di']*np.exp(-3*g['NJ']);rho=dust+g['rho_gas'];pres=g['P'];tau=dust+g['tau_gas']
    H2=1+2*cfg['R0']*rho/3;h=-cfg['R0']*(rho+pres)/H2
    sx=cfg['xi0']*np.exp(-1.5*g['NJ']);sy=cfg['yi0']*np.exp(-2*g['NJ'])
    return dict(gas=g,dust=dust,rho=rho,P=pres,tau=tau,H2=H2,h=h,sx=sx,sy=sy)

def acceleration(pos,vel,H2,h):
    x,y=pos;px,py=vel;D=1+2*(x*x+y*y)/3
    # Explicit connection ratios derived from the two diagonal metric entries.
    cx=(-2*x*px*px-4*y*px*py+1.5*x*py*py)/(3*D)
    cy=(-4*x*px*py-2*y*py*py+(8/3)*y*px*px)/(3*D)
    return np.array([-(3+h)*px-cx-9*D*x/(4*H2),-(3+h)*py-cy-2*D*y/H2])

def derivative(L,state,cfg):
    X,Y,vx,vy=state;q=background(L,cfg)
    x=q['sx']*X;y=q['sy']*Y;px=q['sx']*vx;py=q['sy']*vy
    ac=acceleration([x,y],[px,py],q['H2'],q['h'])
    return np.array([vx+1.5*X,vy+2*Y,ac[0]/q['sx']+1.5*vx,ac[1]/q['sy']+2*vy])/q['gas']['cT']

def local_controls(cfg):
    for i,L in enumerate([0.,3.,12.,20.,cfg['Lf']]):
        q=background(L,cfg)
        for j,st in enumerate([[1,1,-1.5,-2],[.7,1.3,-.6,-1.5],[1.2,-.4,.3,.9]]):
            X,Y,vx,vy=st;x=q['sx']*X;y=q['sy']*Y;px=q['sx']*vx;py=q['sy']*vy
            actual=acceleration([x,y],[px,py],q['H2'],q['h'])
            with mp.workdps(60):
                p=list(map(lambda t:mp.mpf(float(t)),[x,y]));v=list(map(lambda t:mp.mpf(float(t)),[px,py]));H2=mp.mpf(float(q['H2']));h=mp.mpf(float(q['h']))
                def raw(z):
                    xx,yy=z;D=1+mp.mpf(2)/3*(xx*xx+yy*yy)
                    return [4/(9*D),1/(3*D)],xx*xx/2+yy*yy/3
                K,U=raw(p);wanted=[]
                for z in range(2):
                    dK=[[mp.diff(lambda t:raw(p[:r]+[t]+p[r+1:])[0][c],p[r]) for c in range(2)] for r in range(2)]
                    du=mp.diff(lambda t:raw(p[:z]+[t]+p[z+1:])[1],p[z])
                    # Differentiate lowered momenta before raising the index.
                    mom=sum(dK[r][z]*v[r]*v[z] for r in range(2))-sum(dK[z][r]*v[r]*v[r] for r in range(2))/2
                    wanted.append(float(-(3+h)*v[z]-(mom+du/H2)/K[z]))
            near(f'local.{i}.{j}',actual/np.array([q['sx'],q['sy']]),np.array(wanted)/np.array([q['sx'],q['sy']]),5e-13)


def integrate(cfg,refined=False):
    grid=np.linspace(0,cfg['Lf'],241);start=time.monotonic()
    sol=solve_ivp(lambda L,st:derivative(L,st,cfg),(0,cfg['Lf']),[1.,1.,-1.5,-2.],method='DOP853',
                  rtol=2e-11 if refined else 2e-10,atol=2e-13 if refined else 2e-12,max_step=.02 if refined else .04,t_eval=grid)
    label='refined' if refined else 'baseline';check(label+'.complete',sol.success and sol.y.shape==(4,241),message=sol.message)
    rows=[]
    for L,st in zip(sol.t,sol.y.T):
        q=background(L,cfg);x,y=q['sx']*st[0],q['sy']*st[1];px,py=q['sx']*st[2],q['sy']*st[3]
        D=1+2*(x*x+y*y)/3;Tbar=(4*px*px/9+py*py/3)/D
        balance=(x*x+2*y*y/3-cfg['R0']*q['tau']/2-q['H2']*Tbar/2)/(x*x) if x else None
        rows.append(dict(L=float(L),NJ=q['gas']['NJ'],state=st.tolist(),H2=q['H2'],x=x,y=y,px=px,py=py,
                         leading_omega_squared_times_k_squared=4*x*x/q['H2'],zero_inertia_balance_v=balance))
    return dict(refined=refined,success=bool(sol.success),nfev=sol.nfev,elapsed_seconds=time.monotonic()-start,rows=rows)

def main(freeze,out):
    for x in json.loads(freeze.read_text())['inputs']:
        check('source.'+x['path'],hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
    sy=symbolic();co=coefficient_controls();cfg=model.calibration(1e-5)
    cfg['R0']=cfg['Rstar']*(1+cfg['k']);cfg['xi0']=np.sqrt(cfg['R0']*cfg['rho_di']);cfg['yi0']=np.sqrt(cfg['R0']*model.gas(0.,256)['rho_gas'])
    local_controls(cfg);base=integrate(cfg);refined=integrate(cfg,True)
    if len(base['rows'])==len(refined['rows'])==241:
        for i,(a,b) in enumerate(zip(base['rows'],refined['rows'])):near('refinement.'+str(i),a['state'],b['state'],3e-6)
    comparisons=[];old=json.loads((IC/'evidence_v3/histories/RESULTS.json').read_text())['histories']
    for caseid in ['split_k1e-05','split_k1e-06']:
        item=next(x for x in old if x['case']['id']==caseid);k=item['configuration']['k'];a=np.asarray([r['state'] for r in item['rows']]);b=np.asarray([r['state'] for r in refined['rows']])
        check(caseid+'.same_temperature_sites',np.array_equal([r['L'] for r in item['rows']],[r['L'] for r in refined['rows']]))
        # Physical field comparison: parent scaling uses R0/(1+k).
        supplied=a[:,[1,2,4,5]]/np.sqrt(1+k);diff=supplied-b
        comparisons.append(dict(case=caseid,scope='Descriptive difference, no asserted finite-k convergence or history repair.',
                                maximum_scaled_state_difference_by_component=np.max(abs(diff),axis=0).tolist(),
                                final_scaled_state_difference=diff[-1].tolist(),
                                maximum_absolute_u=float(np.max(abs(a[:,0]))),maximum_absolute_pu=float(np.max(abs(a[:,3]))),
                                leading_frequency_initial=np.sqrt(refined['rows'][0]['leading_omega_squared_times_k_squared'])/k,
                                leading_frequency_final=np.sqrt(refined['rows'][-1]['leading_omega_squared_times_k_squared'])/k))
    result=dict(scope='Conditional pointwise weak-coupling limit and separate regular limiting ODE; no finite-k convergence theorem, no replacement for failed histories.',configuration=cfg,symbolic=sy,coefficient_controls=co,histories=[base,refined],descriptive_finite_k_comparison=comparisons,checks=CHECKS,counts=dict(passed=sum(x['passed'] for x in CHECKS),failed=sum(not x['passed'] for x in CHECKS),total=len(CHECKS)))
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(counts=result['counts'],comparisons=comparisons,nfev=[base['nfev'],refined['nfev']]),indent=2))
    return bool(result['counts']['failed'])
if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--freeze',type=Path,required=True);pa.add_argument('--out',type=Path,required=True);ar=pa.parse_args()
    if ar.out.exists():raise FileExistsError(ar.out)
    raise SystemExit(main(ar.freeze,ar.out))
