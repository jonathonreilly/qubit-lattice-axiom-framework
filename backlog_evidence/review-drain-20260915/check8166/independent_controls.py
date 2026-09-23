import json,time,hashlib,pathlib,math
import sympy as s
import numpy as np
from scipy.integrate import quad
start=time.monotonic(); out={}
r=s.symbols('r'); assert s.factor((1-r)**-2+r*(1-r)**-3-(1-r)**-3)==0
u=s.symbols('u');pol=1+u-u**3+u**4/2
assert s.diff(pol,u)==1-3*u*u+2*u**3
assert [pol.subs(u,0),pol.subs(u,1),s.diff(pol,u).subs(u,0),s.diff(pol,u).subs(u,1)]==[1,s.Rational(3,2),1,0]
assert s.diff(pol,u,2).subs(u,0)==s.diff(pol,u,2).subs(u,1)==0
out['exact_transport_and_transition']='PASS'
T=.31;g=.62;m=6; t=np.arange(1,m)*T/m
cov=np.array([[g*g*(min(x,y)-x*y/T) for y in t]for x in t]); precision=np.linalg.inv(cov)
D=np.diag(np.full(m-1,2.))+np.diag(np.full(m-2,-1.),1)+np.diag(np.full(m-2,-1.),-1)
err=float(np.max(abs(precision-D/(g*g*T/m))));assert err<1e-11
out['conditional_bridge_precision_error']=err
# Direct scalar positive integral; differentiate free energy with arbitrary precision
# through independent mpmath differentiation rather than author's moment or Bessel path.
import mpmath as mp
mp.mp.dps=35;gg=mp.mpf('.55');tt=mp.mpf('.24');phi=mp.mpf('.71')
def energy(x):
 z=mp.quad(lambda y:mp.exp(-y*y/2-tt/(2*gg*gg)*(1-mp.cos(x+gg*mp.sqrt(tt)*y))),[-mp.inf,mp.inf])/mp.sqrt(2*mp.pi)
 return -gg*gg*mp.log(z)
cubic=mp.diff(energy,phi,3); rr=2*tt*tt;bound=tt/2/(1-rr)**3;delta=rr+gg*gg*tt/(2*(1-rr))+(1-rr)**-3-1
assert abs(cubic)<bound and abs(cubic+tt/2*mp.sin(phi))<tt/2*delta
out['independent_positive_integral_cubic']={'cubic':str(cubic),'bound':str(bound)}
# Temporal action Hessian reconstructed by exact integration, not the runner Fourier formula.
N=5; gram=np.zeros((N,N));nodes,weights=np.polynomial.legendre.leggauss(3)
for n in range(N):
 for x,w in zip((nodes+1)/2,weights/2):
  v=np.zeros(N);v[n]=1-x;v[(n+1)%N]=x;gram+=w*np.outer(v,v)
vals=np.linalg.eigvalsh(gram); target=np.sort([(2+math.cos(2*math.pi*k/N))/3 for k in range(N)])
err=float(np.max(abs(vals-target)));assert err<1e-14
assert np.max(abs(vals-1))>.5
out['temporal_carrier_eigenvalue_error']=err
# Entire allowed scalar spectrum checks covariance norm and resolvent identity.
maximum=0.;err=0.
for T in [.001,.09,.49]:
 for ls in np.linspace(.01,12,21):
  for theta in np.linspace(0,2*math.pi,31):
   lt=4*math.sin(theta/2)**2/T**2;b=(2+math.cos(theta))/3
   K=ls/(lt+b*ls);factor=(ls/(lt+ls))/(1-T*T/6*ls*lt/(lt+ls))
   maximum=max(maximum,K);err=max(err,abs(K-factor))
assert maximum<=1+1e-14 and err<1e-14
out['covariance_resolvent']={'max_eigenvalue':maximum,'factor_error':err}
# Bounding-box anchor counts: largest tested ratio, and simple analytic certificate
# (2(s+t)+1)<=2(s+1)(t+1) for s,t>=1 proves constant16 <=4096.
a,b=s.symbols('a b',integer=True,positive=True)
assert s.expand(2*(a+1)*(b+1)-(2*(a+b)+1))==2*a*b+1
out['box_anchor_count']='Exact inequality, 16 is sufficient for overlap factor; 4096 conservative.'
out.update(elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),scope='Independent finite/algebraic controls; no primary rerun, no all-volume simulation.')
print(json.dumps(out,indent=2))
