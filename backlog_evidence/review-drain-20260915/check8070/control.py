"""Independent rational and symbolic controls, no canonical imports."""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,time,signal
import sympy as s
signal.alarm(30);start=time.monotonic()
# Direct three-axis return allocation rather than the canonical Vandermonde reduction.
partial=F(0)
for n in range(33):
 count=sum(factorial(2*n)//(factorial(a)**2*factorial(b)**2*factorial(n-a-b)**2) for a in range(n+1) for b in range(n-a+1))
 partial+=F(count,6**(2*n))*F(comb(4*n,2*n),16**n)
old=json.loads(Path('check8070/original-8068/outputs/native_pair_vacuum_chart_2026_09_09.json').read_text());assert partial==F(old['partial'])
upper=partial*F(1000,2449)+F(1,192);assert upper==F(old['C0_h_upper'])<F(7,15)
c=F(1,150)/F(58,25);assert c==F(1,348) and (1-c)/(1+c)==F(347,349) and F(87,4)/(1+c)==F(7569,349)
# Fully symbolic Lyapunov identity in2D, with no positivity assumptions for equality.
p,q,t,k,z,r=s.symbols('p q t k z r',real=True);H=s.Matrix([[p,q],[q,t]]);J=s.Matrix([[0,1],[-1,0]]);K=k*J;Z=z*J;Zd=-K-H*Z-Z*H-Z*K*Z;M=r*r*s.eye(2)+Z*Z;A=H+Z*K;force=2*r*r*H-2*Z*H*Z-(1-r*r)*(K*Z+Z*K)
assert (Zd*Z+Z*Zd-force+A*M+M*A.T).applyfunc(s.expand)==s.zeros(2)
# The2mode even-sector Schr equation fixes creation sign and scalar cancellation.
mu,kappa,E,z=s.symbols('mu kappa E z',real=True);He=s.Matrix([[E,kappa],[kappa,E+2*mu]]);v=s.Matrix([1,z]);dv=-He*v;assert s.expand(dv[1]-z*dv[0]-(-kappa-2*mu*z+kappa*z*z))==0
margin=2*F(99,100)-99*(1-F(99,100)**2);assert margin==F(99,10000)
budget=F(6)*3**25*F(2,3)**129;assert budget<F(1,10**10) and F(6)*3**25*F(2,3)**65>F(1,10**10)
# Gaussian metric on a single real paired block; determinant amplitude exponent1/2 for real polar plane.
x=s.symbols('x',real=True);v=s.Matrix([1,x])/s.sqrt(1+x*x);assert s.simplify((v.diff(x).T*v.diff(x))[0]-1/(1+x*x)**2)==0
th=s.symbols('th',real=True);R=s.Matrix([[s.cos(th),-s.sin(th)],[s.sin(th),s.cos(th)]]);assert s.trigsimp(((s.eye(2)+R)/2).det()-(1+s.cos(th))/2)==0
# Positive atom spectral example tests uniform anchor without assuming an excitation gap.
for a2 in [F(1,100),F(1,3),F(9,10)]:
 for u in [F(0),F(1,10),F(1,2),F(1)]:
  m1=a2+(1-a2)*u;m2=a2+(1-a2)*u*u;assert m1*m1>=a2*m2
out=dict(status='PASS',partial=str(partial),weighted_bound=str(upper),disk_margin=str(margin),degree128_bound=str(budget),seconds=time.monotonic()-start,scope='Exact symbolic and rational identities; no physical propagation or canonical execution.')
Path('check8070/control.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['seconds'])
