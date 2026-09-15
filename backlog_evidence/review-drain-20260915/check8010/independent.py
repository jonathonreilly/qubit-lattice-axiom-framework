import numpy as np, sympy as s, json, math
from scipy.integrate import quad
from pathlib import Path
out={};checks=[]
def ck(n,v):assert v,n;checks.append(n)
w=math.sqrt(5);t=(3-w)/2;a=2/w
# Direct real integral of full 1D kernel on polynomial eigenfunctions.
for degree in range(7):
 for x in [-1.2,0.3,1.1]:
  H=s.lambdify(s.Symbol('q'),s.hermite(degree,s.sqrt(s.sqrt(5))*s.Symbol('q')),'numpy')
  actual=quad(lambda y:math.exp(-1.5*(x*x+y*y)+2*x*y-w*y*y/2)*H(y)/math.sqrt(math.pi),-10,10,epsabs=1e-12)[0]
  expected=t**(degree+.5)*math.exp(-w*x*x/2)*H(x)
  ck(f'1D integral n{degree} x{x}',abs(actual-expected)<2e-10)
for n in [0,1]:
 P=lambda q:1 if n==0 else 4-w*q
 norm=quad(lambda q:q**3*math.exp(-w*q)*P(q)**2,0,np.inf)[0]
 ms=[quad(lambda q:q**(3+k)*math.exp(-w*q)*P(q)**2,0,np.inf)[0]/norm for k in [1,2]]
 ck(f'quadrature moments {n}',np.allclose(ms,[(4 if n==0 else 6)/w,4 if n==0 else 10],atol=1e-12))
 q=s.Symbol('q');F=s.exp(-s.Rational(2)/s.sqrt(5)*q)*(1 if n==0 else 4-4/s.sqrt(5)*q)
 lf=s.lambdify(q,q*s.diff(F,q,2)+4*s.diff(F,q),'numpy');f=s.lambdify(q,F,'numpy')
 norm2=quad(lambda q:q**3*f(q)**2,0,np.inf)[0]
 kinetic=quad(lambda q:q**3*lf(q)**2,0,np.inf)[0]/norm2
 ck(f'direct heat norm {n}',abs(kinetic-(4 if n==0 else 10))<1e-10)
 out[f'branch{n}']={'Q':ms,'heat':kinetic,'total':3-7*ms[0]/4+ms[1]/4+kinetic/4}
# Derive Fourier coefficients from actual six shifts, not authored expected polynomial.
u,v,h=s.symbols('u v h');steps=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
psi=1-sum(s.exp(s.I*h*(i*u+j*v)) for i,j in steps)/6
ck('sixshift quadratic',s.simplify(s.expand(psi.series(h,0,5).removeO()).coeff(h,2)-(u*u-u*v+v*v)/3)==0)
ck('sixshift quartic',s.simplify(s.expand(psi.series(h,0,5).removeO()).coeff(h,4)+(u*u-u*v+v*v)**2/36)==0)
# Reconstruct low PN cross terms with exact rational fractions.
ck('PN cubic cross terms',s.Rational(1,810)+s.Rational(1,1440)+s.Rational(1,144)==s.Rational(23,2592))
# Independent radial integration of conservative low envelope, and explicit tails.
alpha=23/72
cn=quad(lambda z:.5*math.exp(-alpha*z)*(z**5/20+23*z**6/2592+z**7/2592),0,np.inf)[0]
ck('ceiling low+actual tail',cn+.06+.001<21201)
ck('ratio ceiling',(1000/999)*(21201/14+4+(2618/14)*(1+4/2048))<1710)
out.update(checks=checks,low_integral=cn,scope='Independent finite numeric and symbolic cross-checks; analytic general proof separately reconstructed.')
Path('/private/tmp/review-drain-20260915/check8010/independent.json').write_text(json.dumps(out,indent=2))
print('TOTAL: PASS='+str(len(checks))+' FAIL=0')
