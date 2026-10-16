"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib,json

    from pathlib import Path

    import numpy as np

    import sympy as S

    from scipy.integrate import solve_ivp

    checks=[]

    def exact(name,e):
     z=S.factor(S.cancel(S.expand(e)));checks.append({'name':name,'pass':z==0,'residual':str(z)})

    def ck(name,ok,**e):checks.append({'name':name,'pass':bool(ok),**e})

    h,q,B,L,sd,sdp,At,Ct,Et,Ft,pp,p0,jp,j0=S.symbols('h q B L s sp At Ct Et Ft Pp P Jp J')

    physical=At*(pp-sd*p0)+Ct*p0+Et*(jp-sd*j0)+Ft*j0

    record=physical+4*sd*(pp-sd*p0)+(2*(sdp+sd**2)+8*h*sd)*p0

    target=(At+4*sd)*pp+(Ct-At*sd-2*sd**2+2*sdp+8*h*sd)*p0+Et*jp+(Ft-Et*sd)*j0

    exact('general trace gain transformation',record-target)

    exact('joint q from invariant trace derivative coefficient',B*(q/B)-q)

    at=3*(h-q)-2*L-2*sd

    exact('joint gain drift recovered', (3*(h-B*(q/B))-2*L-at)/2-sd)

    ck('wrong missing B factor changes joint reconstruction', S.simplify((q/B-q).subs({q:1,B:S.Rational(2,3)}))!=0)

    ck('wrong omitted trace gain derivative is detectable',S.diff(target,pp).subs(sd,1)-At==4)

    bc=S.sqrt(S.Rational(2,3))

    C0=S.Rational(1,2)

    n0=bc*C0

    p0c=(n0+2)/3

    r0=2*p0c-C0**2

    v0=3*p0c**2-2*p0c+C0**2/2

    f0=-2*v0/C0+bc*r0

    mu0=4*v0/C0**2+bc**2*r0

    exact('critical background Friedmann',3*p0c**2-(r0+C0**2/2+v0))

    exact('critical background Raychaudhuri',2*p0c-r0-C0**2)

    exact('critical background original scalar',-C0+3*p0c*C0+f0)

    exact('critical background dust evolution',-2-(bc*C0-3*p0c))

    exact('critical coupling exactly two thirds',bc**2-S.Rational(2,3))

    ck('critical background positive dust',r0>0,coefficient=str(r0))

    t,u,pi,P,U,d,k,b,n,p,C,Rc,muc,Fc,gamma=S.symbols('t u pi P U d k b n p C Rc muc Fc gamma',real=True)

    A=t**n

    H=p/t

    v=C/t

    r=Rc/t**2

    kE=k/t**(2*p)

    pd=(v*u-r*U)/2-H*P

    rates=[pi,-3*H*pi-(kE+muc/t**2)*u-b*r*d+4*v*pd-2*Fc*P/t**2,
           pd,-P-b*u-b*v*U,3*pd+kE*U]

    state=[u,pi,P,U,d]

    def der(e):return (S.diff(e,t)+sum(S.diff(e,x)*y for x,y in zip(state,rates)))/A

    def jets(e,count):
     out=[e]
     for _ in range(count):out.append(der(out[-1]))
     return out

    constants=[b,n,p,C,Rc,muc,Fc,gamma]

    values=[float(x) for x in [bc,n0,p0c,C0,r0,mu0,f0,S.Rational(2,7)]]

    gain=t**gamma

    obs=jets(gain*b*u,4)+jets(gain*P,3)+jets(k/(t**(2*p)*A**2),2)

    observed=S.lambdify([t]+state+[k]+constants,obs,'numpy',cse=True)

    rhs_mode=S.lambdify([t]+state+[k]+constants,rates,'numpy',cse=True)

    epsilon=1e-6

    kvalues=np.arange(1.,6.)

    desired=[(0.,1.,0.,0.),(1.,0.,0.,0.),(0.,0.,0.,1.),(0.,0.,1.,0.),(0.,0.,1.,0.)]

    bv,nv,pv,cv,rv,muv,fv,gv=values

    initial=[]

    for kv,(jj,jj1,pp0,pp1) in zip(kvalues,desired):
     uu=epsilon*jj/bv;ppii=epsilon*jj1/bv;PP=epsilon*pp0;Pdot=epsilon*pp1
     UU=(cv*uu-2*(Pdot+pv*PP))/rv
     dd=(-2*kv*PP-3*pv*(cv*uu-rv*UU)-cv*ppii+cv**2*PP-fv*uu)/rv
     initial.extend([uu,ppii,PP,UU,dd])

    def rhs(tt,yy):
     return np.concatenate([np.asarray(rhs_mode(tt,*row,kv,*values),float).ravel() for kv,row in zip(kvalues,yy.reshape(5,5))])

    sol=solve_ivp(rhs,(1.,1.2),np.asarray(initial),t_eval=np.linspace(1.,1.2,21),method='DOP853',rtol=2e-12,atol=2e-15,max_step=.005)

    ck('critical original-equation forward solve succeeds',sol.success,message=sol.message)

    maximum={z:0. for z in ['B','q','drift','kappa','trace_damping','trace_fit','scalar_fit','Hamiltonian']}

    sig5=1.

    sig4=1.

    rows=[]

    for tt,yy in zip(sol.t,sol.y.T):
     h0=(pv+nv)*tt**(-nv-1);h1=-(nv+1)*(pv+nv)*tt**(-2*nv-2)
     ds=[[],[],[]];ys=[[],[],[]];es=[[],[]];vs=[[],[]]
     for kv,st in zip(kvalues,yy.reshape(5,5)):
      j0,j1,j2,j3,j4,p0,p1,p2,p3,k0,k1,k2=np.asarray(observed(tt,*st,kv,*values),float)
      ds[0].append([-j1,-j0,p1,k0*p0,p0]);ds[1].append([-j2,-j1,p2,k1*p0+k0*p1,p1]);ds[2].append([-j3,-j2,p3,k2*p0+2*k1*p1+k0*p2,p2])
      ys[0].append(j2+k0*j0);ys[1].append(j3+k1*j0+k0*j1);ys[2].append(j4+k2*j0+2*k1*j1+k0*j2)
      h2=2*(nv+1)**2*(pv+nv)*tt**(-3*nv-3)
      K=4*h1+6*h0**2;Kp=4*h2+12*h0*h1
      es[0].append([p1,p0,j1,j0]);es[1].append([p2,p1,j2,j1])
      vs[0].append(2*p2+8*h0*p1+K*p0);vs[1].append(2*p3+8*h0*p2+(8*h1+K)*p1+Kp*p0)
      uu,ppi,PP,UU,dd=st
      ham=-2*(kv/tt**(2*pv))*PP-3*pv/tt*(cv*uu/tt-rv*UU/tt**2)-rv*dd/tt**2-cv*ppi/tt+(cv/tt)**2*PP-fv*uu/tt**2
      maximum['Hamiltonian']=max(maximum['Hamiltonian'],abs(ham)/epsilon)
     D,D1,D2=[np.asarray(z)/epsilon for z in ds];y,y1,y2=[np.asarray(z)/epsilon for z in ys]
     E,E1=[np.asarray(z)/epsilon for z in es];vv,vv1=[np.asarray(z)/epsilon for z in vs]
     theta=np.linalg.solve(D,y);theta1=np.linalg.solve(D,y1-D1@theta);theta2=np.linalg.solve(D,y2-D2@theta-2*D1@theta1)
     trace=np.linalg.lstsq(E,vv,rcond=None)[0];trace1=np.linalg.lstsq(E,vv1-E1@trace,rcond=None)[0]
     BB=theta[3]/2;Bp=theta1[3]/2;Bpp=theta2[3]/2;LL=Bp/(2*BB);Lp=Bpp/(2*BB)-Bp**2/(2*BB**2)
     qq=BB*trace[2];qp=Bp*trace[2]+BB*trace1[2]
     drift=(3*(h0-qq)-2*LL-theta[0])/2;driftp=(3*(h1-qp)-2*Lp-theta1[0])/2
     cphysical=theta[1]+theta[0]*drift+drift**2+driftp
     kap=cphysical-qp-3*h0*qq+2*qq**2-2*qq*LL-LL**2+Lp+3*h0*LL
     truth=[bv**2,nv*tt**(-nv-1),gv*tt**(-nv-1),muv*tt**(-2*nv-2)]
     for name,estimate,target0 in zip(['B','q','drift','kappa'],[BB,qq,drift,kap],truth):maximum[name]=max(maximum[name],abs(estimate-target0)/(1+abs(target0)))
     maximum['trace_damping']=max(maximum['trace_damping'],abs(trace[0]-6*qq-4*drift))
     maximum['trace_fit']=max(maximum['trace_fit'],float(np.max(abs(E@trace-vv))))
     maximum['scalar_fit']=max(maximum['scalar_fit'],float(np.max(abs(D@theta-y))))
     ss=np.linalg.svd(D,compute_uv=False);sig5=min(sig5,float(ss[-1]/ss[0]));ss=np.linalg.svd(E,compute_uv=False);sig4=min(sig4,float(ss[-1]/ss[0]))
     rows.append({'t_E':float(tt),'B':float(BB),'q':float(qq),'gain_drift':float(drift),'kappa':float(kap),'truth_after_inverse':truth,'record_scalar_coefficients':theta.tolist(),'record_trace_coefficients':trace.tolist()})

    for name,err in maximum.items():ck(name+' in critical-coupling gain witness',err<2e-8,max_error=float(err))

    ck('critical rank-five design persists',sig5>1e-4,min_relative_sigma=sig5)

    ck('critical rank-four trace design persists',sig4>1e-4,min_relative_sigma=sig4)

    return checks, {"rows": rows}
