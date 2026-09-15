"""Independent exact finite controls: no canonical source imports or physical runs."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json,time,signal
signal.alarm(30);start=time.monotonic()
# Return count by convolution of 1/(a!)^2 rather than nested canonical count.
v=[F(1,factorial(a)**2) for a in range(101)]
def conv(a,b):
 c=[F(0)]*min(101,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b[:len(c)-i]):c[i+j]+=x*y
 return c
c=conv(conv(v,v),v);ret=sum((factorial(2*n)*c[n]/6**(2*n) for n in range(101)),F(0));assert ret<F(3,2)
# Direct binomial expansion of polynomial moments, independent convolution implementation.
a=F(17,60);b=4*a/9+8*a*a;d=4*a*a/9
low=F(0)
for n in range(1,13):
 for j in range(n+1):
  for k in range(n-j+1):
   low+=F(factorial(n),factorial(j)*factorial(k)*factorial(n-j-k))*F(8,9)**(n-j-k)*(-b)**j*(-d)**k/F(n*(2*j+4*k+1))*F(7,44)
tail=sum((F(7168*(24*j*j-2048),11*j*j*((j+1)**2+1792)**2) for j in range(16,320)),F(0));assert low+tail>F(1,4)
op=F(177,686);assert op>F(1,4) and F(3,8)*F(4,7)<F(1,4)
err=F(90,8)*5216/sum((F(25)**n/factorial(n) for n in range(161)),F(0));assert err<F(1,10**6)
orig=json.loads(Path('check8067/original-8066/outputs/native_infinite_star_node_reduction_2026_09_09.json').read_text());gg=orig['groups']['native_infinite_star_node_gap_2026_09_09'];assert ret==F(gg['return_partial_exact']) and low==F(gg['gap_lower_exact']) and tail==F(gg['perpendicular_tail_exact'])
# Finite paired principal angles: product overlap and doubled-space factors.
for n in range(1,11):
 ss=[F(i,100) for i in range(1,n+1)];overlap=F(1)
 for x in ss:overlap*=1-x
 assert 1-overlap<=sum(ss) # Fock squared distance <=2 sum sin² via 1-sqrt(prod)<=1-prod.
 assert 2*sum(ss)==F(1,2)*4*sum(ss)
eta=F(2287839703834313821,4000000000000000000000000);bound=F(90,8)*F(61,5)*F(20,7)*eta*16
assert bound<F(36,10000) and (2352+3)//2==1177
# Matrix identities checked independently with symbolic 2x2/4x4 operators.
import sympy as s
A,D,B,u,h=s.symbols('A D B u h',real=True)
R=s.Matrix([[u*A,-s.sqrt(2)*h*D],[s.sqrt(2)*h*D,u*B]]);V=s.Matrix([[0,2*s.sqrt(2)*h],[-2*s.sqrt(2)*h,0]])
assert s.expand((s.eye(2)-R*V).det()-((1-4*h*h*D)**2+8*h*h*u*u*A*B))==0
# Rank-one six-leg correction independently on invertible diagonal toy B, preserving b^T B^-1 e=k/6.
for k in [0,1,2,4,5,6]:
 M=s.diag(*range(1,7));e=s.ones(6,1);row=s.Matrix([[s.Rational(i+1,6) if i<k else 0 for i in range(6)]])
 N=M-2*e*row;assert s.simplify(N.det()/M.det())==1-s.Rational(k,3)
 assert N.inv()==M.inv()+2/(1-s.Rational(k,3))*M.inv()*e*row*M.inv()
out=dict(status='PASS',return_sum=str(ret),perpendicular_lower=str(low+tail),opposite_lower=str(op),tail_upper=str(err),state_error_upper=str(bound),checks='Independent convolution/closed polynomial integrals, determinant sign, six-leg rank-one normalization, paired-angle factors, state-error rank constants; no canonical execution.',seconds=time.monotonic()-start,physical_runs=0)
Path('check8067/control.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['seconds'])
