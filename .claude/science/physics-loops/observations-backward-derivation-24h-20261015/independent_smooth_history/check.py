"""Independent manufactured-history and deterministic perturbation checks."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s
import numpy as np
import json
from itertools import product
checks=[]
def ck(name, ok):
    checks.append({'name':name,'passed':bool(ok)})
t=s.symbols('t', real=True)
G=s.Integer(3); O=s.Integer(2); K=s.Integer(2)
B=t*t; H=6*t-7+5*s.exp(-t)-3*s.exp(-2*t)
A=t-s.Rational(1,2); Y=A*H; phi=t*t*(1-t)**2
D=lambda f,n=1:s.diff(f,t,n)
ck('arbitrary_two_mode_preparation',s.simplify(D(H,2)+G*D(H)+O*H-K*(D(B,2)+G*D(B)))==0)
L0=A*A*D(phi,2)+6*A*D(A)*D(phi)+(6*D(A)**2+3*A*D(A,2))*phi
L1=-A*A*D(phi)-3*A*D(A)*phi
L2=A*A*phi
integrand=Y*L0+G*Y*L1+O*Y*L2-K*A*B*L0-K*G*A*B*L1
ck('crossing_zero_exact_weak_integral',s.simplify(s.integrate(s.expand(integrand),(t,0,1)))==0)
ck('crossing_not_blind',s.simplify(L0)!=0 and A.subs(t,s.Rational(1,2))==0)
ck('regular_exact_weak_integral',s.simplify(s.integrate(s.expand(H*(D(phi,2)-G*D(phi)+O*phi)-K*B*(D(phi,2)-G*D(phi))),(t,0,1)))==0)
# Derivative forcing gives a distinct linear L, violating common-action constraint.
eta=s.Rational(1,7); Hextra=eta*(t-s.Rational(3,2))
ck('derivative_forcing_alternative',s.simplify(D(Hextra,2)+G*D(Hextra)+O*Hextra-eta*D(B))==0)
ck('derivative_forcing_constraint_violation',eta!=0)
# Offset recovery independently sampled for stable, critical and undamped modes.
for name,r1,r2 in [('over',-.2,-1.1),('critical',-.7,-.7),('under',-.1+1.2j,-.1-1.2j),('undamped',1.2j,-1.2j)]:
    h=.31; z1=np.exp(r1*h); z2=np.exp(r2*h); ss=z1+z2; pp=z1*z2
    f=np.array([2.1+(1+.4*n*h)*z1**n if name=='critical' else 2.1+.7*z1**n-.3*z2**n for n in range(3)])
    ck('offset_'+name,abs((f[2]-ss*f[1]+pp*f[0])/(1-ss+pp)-2.1)<1e-12)
rng=np.random.default_rng(721)
for i in range(100):
    ss,pp=rng.uniform(-.8,.8,2); f=rng.uniform(-2,2,3); d=1-ss+pp
    ef=.01; es=.015; ep=.012; ed=es+ep
    if abs(d)<=ed:continue
    en=(1+abs(ss)+abs(pp))*ef+2*ed+ef*ed
    budget=en/(abs(d)-ed)+(1+abs(ss)+abs(pp))*2*ed/(abs(d)*(abs(d)-ed))
    old=(f[2]-ss*f[1]+pp*f[0])/d
    errs=[]
    for signs in product([-1,1],repeat=5):
        ff=f+ef*np.array(signs[:3]); st=ss+es*signs[3]; pt=pp+ep*signs[4]
        errs.append(abs((ff[2]-st*ff[1]+pt*ff[0])/(1-st+pt)-old))
    ck('offset_error_corners_'+str(i),max(errs)<=budget+1e-12)
for sign in [-1,1]:
    aa=sign*.8; yy=-1.7; ea=.03; ey=.035
    bound=ey/(abs(aa)-ea)+abs(yy)*ea/(abs(aa)*(abs(aa)-ea))
    ck('quotient_signed_'+str(sign),all(abs((yy+dy)/(aa+da)-yy/aa)<=bound+1e-14 for da,dy in product([-ea,ea],[-ey,ey])))
result={'checks':checks,'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'empirical_validation':False}
print(json.dumps(result,indent=2))
assert not result['failed']
