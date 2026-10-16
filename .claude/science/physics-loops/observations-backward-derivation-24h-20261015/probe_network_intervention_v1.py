"""Exact finite-network controls. All inputs synthetic and declared."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
P=Path(__file__).resolve().parent; checks=[]
def check(name,ok,**kw):
 assert bool(ok),name
 checks.append({'name':name,'passed':True,**kw})
t,z,a,b,c=s.symbols('t z a b c',positive=True,real=True)
# Independently substitute a polynomial observed history q=t^2 into a one-neighbor solution.
u=s.symbols('u',real=True);x0,v0=s.symbols('x0 v0',real=True)
xh=x0*s.cos(s.sqrt(c)*t)+v0/s.sqrt(c)*s.sin(s.sqrt(c)*t)
x=xh-s.integrate(b/s.sqrt(c)*s.sin(s.sqrt(c)*(t-u))*u**2,(u,0,t))
check('Duhamel hidden equation and both initial conditions',s.simplify(s.diff(x,t,2)+c*x+b*t**2)==0 and s.simplify(x.subs(t,0)-x0)==0 and s.simplify(s.diff(x,t).subs(t,0)-v0)==0)
A=s.Matrix([[z*z+a,b],[b,z*z+c]])
check('Schur response sign and denominator',s.simplify(A.inv()[0,0]-1/(z*z+a-b*b/(z*z+c)))==0)
K=s.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]])
O=s.Matrix([[1,0,0],[0,s.Rational(3,5),-s.Rational(4,5)],[0,s.Rational(4,5),s.Rational(3,5)]])
Kp=O*K*O.T;e=s.Matrix([1,0,0]);y=s.symbols('y',positive=True)
check('different spring adjacency with identical complete boundary response',O*O.T==s.eye(3) and all(Kp[i,j]<0 for i in range(3) for j in range(i)) and all(sum(Kp.row(i))>0 for i in range(3)) and all(K[:i,:i].det()>0 for i in range(1,4)) and s.simplify(((y*s.eye(3)+K).inv()-(y*s.eye(3)+Kp).inv())[0,0])==0,original=str(K),rotated=str(Kp))
th=s.symbols('theta',nonnegative=True);w=s.Matrix([0,1,-1]);src=s.Matrix([1,0,0]);obs=s.Matrix([0,1,0]);R=(y*s.eye(3)+K).inv();J=(w.T*R*w)[0];H=(obs.T*R*w)[0]*(w.T*R*src)[0]
Rth=(y*s.eye(3)+K+th*w*w.T).inv();delta=s.factor((obs.T*(R-Rth)*src)[0]);expected=th*H/(1+th*J)
check('full response under one interior spring intervention',s.simplify(delta-expected)==0,response=str(s.factor(delta)))
t1,t2,t3,hh,jj=s.symbols('t1 t2 t3 H J')
def residual(ts,ds):
 x1,x2,x3=ts;d1,d2,d3=ds
 return x2*(x3-x1)*d1*d3-x3*(x2-x1)*d1*d2+x1*(x2-x3)*d2*d3
expr=residual([t1,t2,t3],[t1*hh/(1+t1*jj),t2*hh/(1+t2*jj),t3*hh/(1+t3*jj)])
check('division-free three-intervention identity',s.factor(expr)==0 and residual([1,2,3],[0,0,0])==0)
# Visible rank-two example; use the same source and readout for positivity here.
A2=s.diag(2,5);v=s.Matrix([1,1]);vals=[]
for th0 in [1,2,3]:vals.append((v.T*(A2.inv()-(A2+th0*s.eye(2)).inv())*v)[0])
r2=s.factor(residual([1,2,3],vals))
check('rank-two alternative can violate the common rank-one test',r2!=0,residual=str(r2),differences=[str(x) for x in vals])
# Independent numerical stress of deterministic uncertainty bound, with complex
# H,J and deliberately correlated baseline error; not statistical coverage.
rng=np.random.default_rng(62841);max_fraction=0
for _ in range(2000):
 ts=np.array([.3,.8,1.7]);hv=rng.normal()+1j*rng.normal();jv=.2+.2j
 true=ts*hv/(1+ts*jv)
 common=.01*(rng.normal()+1j*rng.normal());individual=.005*(rng.normal(size=3)+1j*rng.normal(size=3));err=common+individual;d=true+err;eps=np.abs(err)
 B=lambda i,j:eps[i]*abs(d[j])+eps[j]*abs(d[i])+eps[i]*eps[j]
 bound=abs(ts[1]*(ts[2]-ts[0]))*B(0,2)+abs(ts[2]*(ts[1]-ts[0]))*B(0,1)+abs(ts[0]*(ts[1]-ts[2]))*B(1,2)
 value=abs(residual(ts,d));assert value<=bound+2e-14
 max_fraction=max(max_fraction,value/bound)
check('complex and correlated error certificate controls',True,cases=2000,max_residual_over_bound=max_fraction,scope='synthetic deterministic controls; not a data-fit or confidence calibration')
result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK09_v1.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Supplied finite linear network, source, readout, state and calibrated one-coupling perturbation; no action or physical graph derived.'}
text=json.dumps(result,indent=2)+'\n';(P/'NETWORK_INTERVENTION_CONTROLS_v1.json').write_text(text);print(text,end='')
