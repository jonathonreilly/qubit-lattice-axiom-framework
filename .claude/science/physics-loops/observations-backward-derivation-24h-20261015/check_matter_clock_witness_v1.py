"""Root's post-exposure check of the independent singular-chart witness."""
import hashlib
import json
from pathlib import Path
import sympy as s

p=Path(__file__).resolve().parent
t,T=s.symbols('t tau',positive=True)
H=s.Rational(12,17)/t
v=s.Rational(4,17)/t
A=t**s.Rational(2,17)
r=s.Rational(392,289)/t**2
V=s.Rational(32,289)/t**2
rho=r/A
tau=s.Rational(17,19)*t**s.Rational(19,17)
dp=lambda f:s.diff(f,t)/v
rows=[]
def ck(n,e):
 q=s.factor(s.cancel(e)); rows.append({'name':n,'pass':q==0,'residual':str(q)})
ck('Friedmann',3*H*H-v*v/2-V-r)
ck('Raychaudhuri',-2*s.diff(H,t)-v*v-r)
ck('original scalar',s.diff(v,t)+3*H*v+dp(V)+rho*dp(A))
ck('bare dust scaling',s.diff(rho*t**s.Rational(36,17),t))
ck('clock',s.diff(tau,t)-A)
ck('coupling',dp(A)/A-s.Rational(1,2))
ck('curvature',(dp(dp(V))+rho*dp(dp(A)))/A**2-s.Rational(2410,361)/tau**2)
ck('matter expansion',(H+s.diff(A,t)/A)/A-s.Rational(14,19)/tau)
ck('matter scalar speed',v/A-s.Rational(4,19)/tau)
ck('matter source',r/A**2-s.Rational(392,361)/tau**2)
h=s.Rational(14,19)/T;b=s.Rational(1,2);kap=s.Rational(2410,361)/T**2
X=s.symbols('X',real=True);xf=s.Rational(4,19)/T
r0=-2*s.diff(h,T)-2*b*h*X+(2*b*b-1)*X*X
B1=3*h-2*b*X-6*b*b*(h-b*X)
B0=(3*s.diff(h,T)+kap+6*h*b*X-4*b*b*X*X)*X-3*b*(h-b*X)*r0
C=-2*((6*b**4-2*b*b+1)*X+b*(1-6*b*b)*h)
N=s.diff(r0,T)+(3*h-2*b*X)*r0-2*b*B0
R=2*b*s.diff(xf,T)+r0.subs(X,xf)
ck('matter dust',s.diff(R,T)+(3*h-2*b*xf)*R)
ck('matter scalar',s.diff(xf,T,2)+B1.subs(X,xf)*s.diff(xf,T)+B0.subs(X,xf))
ck('C zero throughout physical history',C.subs(X,xf))
ck('N zero throughout physical history',N.subs(X,xf))
rows.append({'name':'positive R and nonzero x on T>0','pass':bool(R.is_positive and xf.is_positive),'evidence':str(R)})
sources=['check_matter_clock_witness_v1.py','MATTER_CLOCK_DERIVATION_v2.md','independent_matter_clock/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md']
result={'author':'/root','exposure':'post-exposure; witness found by independent checker, personally rechecked here',
        'checks':rows,'passed':sum(r['pass'] for r in rows),'failed':sum(not r['pass'] for r in rows),
        'source_sha256':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in sources},'empirical_validation':False}
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(int(result['failed']>0))
