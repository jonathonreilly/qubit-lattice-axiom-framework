#!/usr/bin/env python3
"""New positive potential, fixed prior gas, actual full six-state evolution."""
from pathlib import Path
import argparse, datetime, hashlib, importlib.util, json, time, traceback
import numpy as np
import mpmath as mp
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
IC=HERE.parent/'direct_thermal_matter_bridge'
spec=importlib.util.spec_from_file_location('exponential_fixed_gas',IC/'check_thermal_matter_bridge_v3.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
CHECKS=[]

def check(name,ok,**detail):CHECKS.append(dict(name=name,passed=bool(ok),**detail))
def near(name,a,b,tol):
    error=float(np.max(np.abs(np.asarray(a)-np.asarray(b))/np.maximum(1,np.abs(b))))
    check(name,np.isfinite(error) and error<=tol,error=error,tolerance=tol)

def cfg(k,n):
    c=base.calibration(k);a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k))
    c.update(a=a,b=k,s=s,nu=base.INPUTS['nu'])
    c['xi']=np.sqrt(c['Rstar']*c['rho_di']);c['yi']=np.sqrt(c['Rstar']*base.gas(0,n)['rho_gas'])
    c['lambda_x']=2*np.sqrt(a)*(1+s*k)/(k*(1+s));c['lambda_y']=4*np.sqrt(a)*s/(1+s)
    return c

def action(phi,c):
    u,x,y=phi;a,b,s,nu=[c[z] for z in ['a','b','s','nu']];al=np.sqrt(a)
    E=np.exp(2*al*u);z=s*E;F=1+z;J=1+(1-3*a)*z;D=1+2*(1+b)*(x*x+y*y)/3
    K=np.array([J/F**2,(1+s)*4*b/(9*F*D),(1+s)*b/(3*F*D)])
    dk=np.zeros((3,3));dk[0,0]=K[0]*2*al*z*((1-3*a)/J-2/F)
    dk[0,1:]=K[1:]*(-2*al*z/F);dk[1,1:]=K[1:]*(-4*(1+b)*x/(3*D));dk[2,1:]=K[1:]*(-4*(1+b)*y/(3*D))
    ex=np.exp(-c['lambda_x']*u);ey=np.exp(-c['lambda_y']*u)
    Uv=1.5+1.5*s*np.expm1(2*al*u)**2/F**2
    Ux=b*x*x*ex/2;Uy=b*y*y*ey/3;Un=nu*(1+s)*u*u/(2*F**2)
    U=Uv+Ux+Uy+Un
    dUv=6*al*s*(1+s)*E*np.expm1(2*al*u)/F**3
    dUn=nu*(1+s)*u/F**2-4*al*z*Un/F
    dU=np.array([dUv-c['lambda_x']*Ux-c['lambda_y']*Uy+dUn,b*x*ex,2*b*y*ey/3])
    return K,dk,U,dU,al/F,(1+s)*E/F

def quantities(L,state,c,n):
    u,X,Y,pu,vx,vy=state;g=base.gas(float(L),n);sx=c['xi']*np.exp(-1.5*g['NJ']);sy=c['yi']*np.exp(-2*g['NJ'])
    phi=np.array([u,sx*X,sy*Y]);vel=np.array([pu,sx*vx,sy*vy]);K,dk,U,dU,ab,CB=action(phi,c)
    dust=c['rho_di']*np.exp(-3*g['NJ']);rho=dust+g['rho_gas'];P=g['P'];tau=dust+g['tau_gas'];R=c['Rstar']
    sig=CB*CB*R*rho;pres=CB*CB*R*P;trace=CB*CB*R*tau;T=K@(vel*vel)
    H2=2*(sig+U)/(3-T);h=-(sig+pres)/H2-T;njp=1+ab*pu
    if not np.all(np.isfinite(np.r_[K,H2,njp])) or min(K)<=0 or H2<=0 or njp<=0 or T>=3:raise ValueError(('physical chart',L,state.tolist()))
    connection=(vel*(vel@dk)-dk@(vel*vel)/2)/K;force=dU.copy();force[0]+=ab*trace
    acc=-(3+h)*vel-connection-force/(K*H2);HGR2=1+2*(1+c['k'])*R*rho/3;HJ2=H2*njp*njp/CB
    return dict(gas=g,sx=sx,sy=sy,phi=phi,p=vel,K=K,dk=dk,U=U,dU=dU,ab=ab,CB=CB,sigma=sig,pressure=pres,trace=trace,rho=rho,P=P,tau=tau,norm=T,H2=H2,h=h,njp=njp,acc=acc,HGR2=HGR2,HJ2=HJ2,Hratio=np.sqrt(HJ2/HGR2),GNratio=CB*(1+ab*ab/K[0])/(1+c['k']))

def rhs(L,state,c,n):
    q=quantities(L,state,c,n);u,X,Y,pu,vx,vy=state;njp=q['njp']
    return np.array([pu,vx+1.5*njp*X,vy+2*njp*Y,q['acc'][0],q['acc'][1]/q['sx']+1.5*njp*vx,q['acc'][2]/q['sy']+2*njp*vy])/(q['gas']['cT']*njp)

def raw_mp(phi,c):
    u,x,y=phi;a,b,s,nu=[mp.mpf(str(c[z])) for z in ['a','b','s','nu']];al=mp.sqrt(a);E=mp.exp(2*al*u);F=1+s*E;D=1+mp.mpf(2)/3*(1+b)*(x*x+y*y)
    K=[(1-3*a*s*E)/F+mp.mpf(3)/4*(2*al*s*E/F)**2,(1+s)*4*b/(9*F*D),(1+s)*b/(3*F*D)]
    lx=2*al*(1+s*b)/(b*(1+s));ly=4*al*s/(1+s)
    U=mp.mpf('1.5')*(1+s)*(1+s*E*E)/F**2+b*x*x*mp.exp(-lx*u)/2+b*y*y*mp.exp(-ly*u)/3+nu*(1+s)*u*u/(2*F**2)
    return K,U,mp.sqrt((1+s)*E/F)

def oracle(L,state,c,n):
    q=quantities(L,state,c,n)
    with mp.workdps(80):
        f=lambda t:mp.mpf(str(t));phi=list(map(f,q['phi']));vel=list(map(f,q['p']));K,U,B=raw_mp(phi,c)
        dK=[[mp.diff(lambda t:raw_mp(phi[:i]+[t]+phi[i+1:],c)[0][j],phi[i]) for j in range(3)] for i in range(3)]
        dU=[mp.diff(lambda t:raw_mp(phi[:i]+[t]+phi[i+1:],c)[1],phi[i]) for i in range(3)]
        ab=mp.diff(lambda t:mp.log(raw_mp([t,*phi[1:]],c)[2]),phi[0]);CB=B*B;R=f(c['Rstar']);sig=CB*CB*R*f(q['rho']);pres=CB*CB*R*f(q['P']);tau=CB*CB*R*f(q['tau'])
        T=sum(z*v*v for z,v in zip(K,vel));H2=2*(sig+U)/(3-T);h=-(sig+pres)/H2-T;acc=[]
        for i in range(3):
            term=sum(dK[j][i]*vel[j]*vel[i] for j in range(3))-sum(dK[i][j]*vel[j]**2 for j in range(3))/2
            acc.append(-(3+h)*vel[i]-(term+(dU[i]+(ab*tau if i==0 else 0))/H2)/K[i])
        return dict(K=[float(z) for z in K],U=float(U),dU=[float(z) for z in dU],acc=[float(z) for z in acc],H2=float(H2),CB=float(CB))

def local_checks():
    rows=[]
    for k in [.01,1e-5,1e-6]:
        c=cfg(k,128)
        for i,L in enumerate([0.,3.5,c['Lf']]):
            for j,state in enumerate([[0,1,1,0,-1.5,-2],[.2,.8,1.1,.03,-1.2,-1.7],[-.3,1.2,.7,-.02,-.8,-1.1]]):
                st=np.array(state,dtype=float);q=quantities(L,st,c,128);o=oracle(L,st,c,128);tag=f'local.{k}.{i}.{j}';scale=np.array([1,q['sx'],q['sy']])
                near(tag+'.force',q['acc']/scale,np.array(o['acc'])/scale,3e-9)
                near(tag+'.potential',q['U'],o['U'],3e-12);near(tag+'.gradient',q['dU']/scale,np.array(o['dU'])/scale,3e-11)
                # Analytic differentiated constraint: fluid conservation plus full lowered field equations.
                normprime=(q['p']@q['dk'])@(q['p']**2)+2*(q['K']*q['p'])@q['acc']
                sigmap=-3*(q['sigma']+q['pressure'])+q['ab']*st[3]*q['trace']
                hp=.5*((sigmap+q['dU']@q['p'])/(q['sigma']+q['U'])+normprime/(3-q['norm']))
                near(tag+'.energy',hp,q['h'],3e-10)
                rows.append(dict(k=k,L=L,state=state,scaled_acceleration=(q['acc']/scale).tolist(),Hratio=q['Hratio']))
        # Exact ideal-orbit first jet, independently differentiated original potential.
        for j,(x,y) in enumerate([(0.,0.),(.7,.3),(1.2,-.9)]):
            K,dk,U,dU,ab,CB=action([0,x,y],c)
            old=base.CL.full_einstein_functions(np.array([0.,x,y]),c['a'],c['b'],c['s'],c['nu'])
            near(f'ideal_jet.{k}.{j}.U',U,old[2],2e-12);near(f'ideal_jet.{k}.{j}.gradient',dU,old[3],2e-12)
            check(f'positivity.{k}.{j}',U>=1.5 and min(K)>0)
    return rows

def integrate(k,refined,out):
    n=256 if refined else 128;c=cfg(k,n);start=time.monotonic();calls=0;last_L=0.;last_state=None
    def fun(L,z):
        nonlocal calls,last_L,last_state
        calls+=1;last_L=float(L);last_state=z.tolist()
        if calls%100==0 and time.monotonic()-start>120:raise TimeoutError('Frozen120secondcasecap')
        return rhs(L,z,c,n)
    label=f'exponential_k{k}'+('_refined' if refined else '');rows=[]
    try:
        sol=solve_ivp(fun,(0,c['Lf']),[0.,1.,1.,0.,-1.5,-2.],method='DOP853',rtol=1e-10 if refined else 1e-9,atol=1e-12 if refined else 1e-11,max_step=.0125 if refined else .025,t_eval=np.linspace(0,c['Lf'],241))
        success=sol.success and len(sol.t)==241;message=sol.message
        for i,(L,st) in enumerate(zip(sol.t,sol.y.T)):
            q=quantities(L,st,c,n);g=q['gas'];rows.append(dict(L=float(L),state=st.tolist(),T=g['T'],NJ=g['NJ'],Hratio=q['Hratio'],GNratio=q['GNratio'],H2=q['H2'],HJ2=q['HJ2'],HGR2=q['HGR2'],NJprime=q['njp'],K=q['K'].tolist(),kinetic_norm=q['norm']))
            check(label+'.positive.'+str(i),min(q['K'])>0 and q['norm']<3 and q['njp']>0)
            if i in [0,40,80,120,160,200,240]:
                o=oracle(float(L),st,c,n);near(label+'.action.'+str(i),q['acc']/[1,q['sx'],q['sy']],np.array(o['acc'])/[1,q['sx'],q['sy']],3e-9)
    except Exception as exc:success=False;message=repr(exc);(out/(label+'.traceback')).write_text(traceback.format_exc())
    check(label+'.complete',success,rows=len(rows),message=message)
    r=dict(case=dict(id=label,k=k,refined=refined,branch='new_exponential_split'),configuration=c,success=success,message=message,elapsed_seconds=time.monotonic()-start,nfev=calls,last_L=last_L,last_state=last_state,rows=rows)
    (out/(label+'.json')).write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(case=label,success=success,nfev=calls,elapsed=r['elapsed_seconds'],last_L=last_L)),flush=True)
    return r

def main(freeze,out):
    out.mkdir(exist_ok=False)
    inputs=json.loads(freeze.read_text())['inputs']
    for z in inputs:check('source.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    local=local_checks();histories=[]
    for k in [.01,1e-5,1e-6]:
        h=integrate(k,False,out);r=integrate(k,True,out);histories.extend([h,r])
        if h['success'] and r['success']:
            for i,(x,y) in enumerate(zip(h['rows'],r['rows'])):
                near(f'refinement.{k}.{i}',x['state'],y['state'],3e-6)
                near(f'physical_refinement.{k}.{i}',[x['Hratio'],x['GNratio']],[y['Hratio'],y['GNratio']],3e-6)
    for z in inputs:check('unchanged.'+z['path'],hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256'])
    result=dict(scope='New positive exponential potential. Exposed theory development, same gas and fixed initial data; no fit or empirical acceptance.',local=local,histories=histories,checks=CHECKS,counts=dict(passed=sum(z['passed'] for z in CHECKS),failed=sum(not z['passed'] for z in CHECKS),total=len(CHECKS)))
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result['counts']),flush=True)
    return bool(result['counts']['failed'])

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--freeze',type=Path,required=True);pa.add_argument('--out',type=Path,required=True);a=pa.parse_args();raise SystemExit(main(a.freeze,a.out))
