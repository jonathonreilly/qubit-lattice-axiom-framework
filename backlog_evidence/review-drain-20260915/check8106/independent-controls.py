import sympy as s,itertools,time,json
from pathlib import Path
start=time.monotonic();checks=[]
def ck(n,v):
 assert v,n
 checks.append(n)
x,u=s.symbols('x u',real=True)
ck('sinc integral quadratic remainder coefficient',s.integrate(4*x*x*(1-u)*u*u,(u,0,1))==x*x/3)
lam=s.symbols('l',positive=True);z=s.symbols('z',nonnegative=True)
f=z**4*s.exp(-lam*z);ck('fourth moment envelope extremum',s.diff(f,z).subs(z,4/lam)==0 and s.simplify(f.subs(z,4/lam)-(4/(s.E*lam))**4)==0)
A=s.Matrix([[2,s.I],[0,1]]);B=s.Matrix([[1,0],[s.I,3]]);R=s.diag(s.I,-1)
wedge=lambda M:s.diag(1,M,s.det(M))
ck('ordered exterior trace with temporal insertion',s.trace(wedge(R)*wedge(B)*wedge(A))==s.det(s.eye(2)+R*B*A))
ck('same-order conjugation pairs, adjoint order differs',s.det(s.eye(2)+(R*B*A).conjugate())==s.conjugate(s.det(s.eye(2)+R*B*A)) and R*B*A!=(R*B*A).adjoint())
counts={}
for N in [3,5]:
 q=[sum(bits[:2])-sum(bits[4:6])+sum(bits[2:4])-sum(bits[6:]) for bits in itertools.product([0,1],repeat=8)];counts[N]=(sum(v%N==0 for v in q),sum(v%N==0 and v!=0 for v in q))
ck('all modular total-charge sectors',counts=={3:(86,16),5:(70,0)})
ck('ring positive-type violation leading coefficient',s.expand(s.series(s.cosh(x/s.sqrt(2))**2-s.cosh(x),x,0,6).removeO()).coeff(x,4)==s.Rational(1,24))
a,b,c,d=s.symbols('a b c d',real=True);h=s.Matrix([[c,a-s.I*b],[a+s.I*b,-c]]);Q=h.row_join(d*s.eye(2)).col_join((d*s.eye(2)).row_join(-h));ck('neutral pairing spectral gap square',s.simplify(Q*Q-(a*a+b*b+c*c+d*d)*s.eye(4))==s.zeros(4))
E=s.diag(-2,-1,0,1,2);V=s.zeros(5)
for i in range(4):V[i+1,i]=1
F=3*E;H=V+V.T;comm=lambda A,B:A*B-B*A
ck('charged hopping double-commutator sign',comm(F,comm(H,F))==-9*H)
W=V*V;Hmag=-(W+W.T)/2;ck('magnetic double-commutator sign',comm(F,comm(Hmag,F))==18*(W+W.T))
# Direct matrix exponential path majorant for a weighted three-site graph.
import numpy as np
from scipy.linalg import expm
M=np.array([[1.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
mu=.7;T=.6;dist=np.abs(np.arange(3)[:,None]-np.arange(3)[None,:]);C=max((M*np.exp(mu*dist)).sum(axis=1));K=expm(2*T*M)
ck('weighted row path exponential majorant',bool(np.all((K*np.exp(mu*dist)).sum(axis=1)<=np.exp(2*T*C)+1e-12)))
out={'independent_controls':checks,'pass_count':len(checks),'elapsed_seconds':time.monotonic()-start,'scope':'Independent algebra and path bound controls; no primary imported/executed. General proof independently read; no thermodynamic inference.'}
p=Path(__file__).with_name('independent-controls-result.json');assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
