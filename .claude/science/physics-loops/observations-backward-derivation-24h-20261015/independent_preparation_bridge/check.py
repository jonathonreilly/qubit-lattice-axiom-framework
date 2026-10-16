"""Independent state-transition, complex-prefix and moment checks."""
AUDIT_TIMEOUT_SEC=120
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
import json
rows=[]
def ck(n,c,d=None):rows.append({'name':n,'passed':bool(c),'detail':d})
x=s.symbols('x');ta=1+.08*x+.15*x*x;C=2+.2*x+.12*x*x;ga=.5+.03*x;M=2+.04*x*x;k=.2+.04*x*x;nu=.1+.02*x;d=.6;w0=.1+.25*x+.05*x*x;B=-C*w0;U=.3*x*x+C*w0*w0/2
expressions=[ta,C,ga,M,k,nu,B,U]
fn=s.lambdify(x,[s.diff(e,x,j) for e in expressions for j in range(3)],'numpy')
def p(xx):return np.asarray(fn(xx)).reshape(8,3)
def calc(xx,v,a,y):
    pp=p(xx);t,cc,g,mm,kk,nn,bb,uu=pp[:,0];tp,cp,gp,mp,kp,np_,bp,up=pp[:,1]
    w,h=y;acc=(-(tp*v+g)*h-cc*w-kk*a-kp*v*v-bb-nn*v)/t
    R=mm*a+.5*mp*v*v+kk*acc-.5*tp*h*h+up+bp*w+.5*cp*w*w+d*v+nn*h
    return np.array([h,acc]),R
x0=.12;T=np.linspace(0,3.4,171)
def drive(t,A):
    e=np.exp(-t);return x0+A*t*t*e,A*(2*t-t*t)*e,A*(2-4*t+t*t)*e
pp=p(x0);t0,C0,g0=pp[:3,0];la=-g0/(2*t0)+1j*np.sqrt(C0/t0-(g0/(2*t0))**2);weq=-pp[6,0]/C0
# Transition matrix and affine reference propagated together; no per-state fitting.
def transition(A):
    def fun(t,y):
        xx,v,a=drive(t,A);par=p(xx);ta=par[0,0];mat=np.array([[0.,1.],[-par[1,0]/ta,-(par[0,1]*v+par[2,0])/ta]])
        ref=calc(xx,v,a,y[:2])[0];Phi=y[2:].reshape(2,2)
        return np.r_[ref,(mat@Phi).ravel()]
    sol=solve_ivp(fun,[0,T[-1]],np.r_[[weq,0.],np.eye(2).ravel()],t_eval=T,rtol=1e-11,atol=1e-13,method='DOP853');assert sol.success
    return sol.y[:2].T,sol.y[2:].T.reshape(-1,2,2)
def record(A,c):
    y0=np.array([weq+2*c.real,2*(la*c).real])
    sol=solve_ivp(lambda tt,yy:calc(*drive(tt,A),yy)[0],[0,T[-1]],y0,t_eval=T,rtol=1e-11,atol=1e-13,method='DOP853');assert sol.success
    return np.array([calc(*drive(tt,A),yy)[1] for tt,yy in zip(T,sol.y.T)]),sol.y.T
# Prefix coordinates fitted using complex exponential basis, distinct from author real fit.
def prefix(c):
    ts=np.linspace(-2.6,0,91);eta=c*np.exp(la*ts);ys=np.column_stack([weq+2*eta.real,2*(la*eta).real])
    R=np.array([calc(x0,0,0,y)[1] for y in ys]);ex=[0,la,la.conjugate(),2*la.real,2*la,2*la.conjugate()]
    basis=np.exp(ts[:,None]*np.array(ex)[None,:]);cf=np.linalg.lstsq(basis,R,rcond=None)[0]
    return cf[1]
def design(z):return np.array([z.real*0+1,z.real,z.imag,z.real**2,z.real*z.imag,z.imag**2])
cs=np.array([.13+.22j,-.21+.11j,.31-.17j,-.18-.28j,.42+.19j,.06-.39j]);e0=np.array([1.,0,0,0,0,0])
ff=np.array([prefix(c) for c in cs]);Q=design(ff);weights=np.linalg.solve(Q,e0)
G=pp[6,1]+pp[1,1]*weq;n=G+pp[5,0]*la+pp[4,0]*la*la
ck('measured_prefix_coordinate',np.max(abs(ff-n*cs))<1e-12)
ck('signed_full_moments',np.linalg.norm(Q@weights-e0)<1e-12 and min(weights)<0)
for A in [.19,-.13]:
    ref,Phi=transition(A);refR=np.array([calc(*drive(tt,A),yy)[1] for tt,yy in zip(T,ref)]);records=[]
    for j,c in enumerate(cs):
        R,ys=record(A,c);records.append(R);initial=np.array([2*c.real,2*(la*c).real]);pred=ref+np.einsum('tij,j->ti',Phi,initial)
        ck('transition_'+str((A,j)),np.max(abs(pred-ys))<2e-10)
    records=np.array(records);ck('finite_drive_rest_'+str(A),np.max(abs(weights@records-refR))<2e-10)
    alpha=np.linalg.solve(Q.T,records)
    for c in [.24+.33j,-.39+.04j]:
        actual,_=record(A,c);pred=design(np.array([prefix(c)])).T@alpha
        ck('reserved_state_'+str((A,c)),np.max(abs(pred[0]-actual))<3e-10)
# Tangent propagated using independent complex-step Jacobians of full moving equations.
c=.23-.18j;yinit=np.array([weq+2*c.real,2*(la*c).real])
def tangent(c):
    init=np.array([weq+2*c.real,2*(la*c).real,0.,0.]);h=1e-25
    def fun(tt,yy):
        base=yy[:2];eta=yy[2:];xx,v,a=drive(tt,0);dx,dv,da=np.array(drive(tt,1))-np.array(drive(tt,0))
        direct=calc(xx+1j*h*dx,v+1j*h*dv,a+1j*h*da,base)[0].imag/h
        J=np.column_stack([calc(xx,v,a,base+1j*h*np.eye(2)[j])[0].imag/h for j in range(2)])
        return np.r_[calc(xx,v,a,base)[0],J@eta+direct]
    sol=solve_ivp(fun,[0,T[-1]],init,t_eval=T,rtol=1e-11,atol=1e-13,method='DOP853');assert sol.success
    out=[]
    for tt,y in zip(T,sol.y.T):
        dx,dv,da=np.array(drive(tt,1))-np.array(drive(tt,0));out.append(calc(x0+1j*h*dx,1j*h*dv,1j*h*da,y[:2]+1j*h*y[2:])[1].imag/h)
    return np.array(out)
nonrest=tangent(c);rest=tangent(0j);eps=1e-4
fd=(record(eps,c)[0]-record(-eps,c)[0])/(2*eps)
ck('independent_complexstep_tangent',np.max(abs(fd-nonrest))<1e-7,float(np.max(abs(fd-nonrest))))
ck('baseline_not_rest',np.max(abs(nonrest-rest))>1e-3)
errs=[]
for eps in [.04,.02,.01]:
    out=[]
    for sign,preps in [(1,cs),(-1,.8*np.exp(.41j)*cs)]:
        fq=np.array([prefix(z) for z in preps]);u=np.linalg.solve(design(fq),e0);rs=np.array([record(sign*eps,z)[0] for z in preps]);out.append(u@rs)
    errs.append(float(np.max(abs((out[0]-out[1])/(2*eps)-rest))))
ck('unmatched_centered_order',all(3.5<a/b<4.5 for a,b in zip(errs[:-1],errs[1:])),errs)
# Necessary moment geometry: arbitrary rotations/scales and radius obstruction.
for z in [1,.4+.7j,-2j]:
    qs=design(z*np.array([1.,2.,4.]));u=np.array([8/3,-2.,1/3]);ck('rank_deficient_feasible_'+str(z),np.linalg.norm(qs@u-e0)<1e-12)
circle=np.exp(1j*np.linspace(0,2*np.pi,11,endpoint=False))*1.7;qc=design(circle);dual=np.array([-1.7**2,0,0,1,0,1]);ck('fixed_radius_dual',np.max(abs(dual@qc))<1e-12 and abs(dual@e0)>1)
# Deterministic correlated feature and readout errors, with arbitrary quadratic outputs.
rng=np.random.default_rng(81)
for i in range(100):
    delta=rng.uniform(-1e-6,1e-6,(2,6));fh=ff+delta[0]+1j*delta[1];Qh=design(fh);uh=np.linalg.solve(Qh,e0);e=1e-6;rad=np.array([np.zeros(6),np.full(6,e),np.full(6,e),2*abs(fh.real)*e+e*e,(abs(fh.real)+abs(fh.imag))*e+e*e,2*abs(fh.imag)*e+e*e]);eta=np.linalg.norm(rad);AA=np.linalg.norm(np.linalg.inv(Qh),2);eu=AA*eta*np.linalg.norm(uh)/(1-AA*eta)
    alpha=rng.normal(size=6);R=Q.T@alpha;er=1e-5;Rh=R+er*np.sign(uh);bound=er*sum(abs(uh))+eu*(np.linalg.norm(Rh)+np.sqrt(6)*er)
    ck('error_certificate_'+str(i),AA*eta<1 and np.linalg.norm(Q-Qh,2)<=eta and np.linalg.norm(weights-uh)<=eu and abs(uh@Rh-alpha[0])<=bound)
result={'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows,'empirical_validation':False};print(json.dumps(result,indent=2));assert not result['summary']['failed']
