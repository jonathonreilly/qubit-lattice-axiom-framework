"""Test the specific unrestricted Haar Laplace assertion in arXiv:2606.19362.

Appendix A.3 permits C1 convex phi. Our phi is exactly s near zero,
C1 convex on [0,infty), and exactly s^2 for s>=2. The analytic cap argument
applies also to every smooth phi satisfying the paper's near-zero condition.
"""
import math,json,time
import numpy as np
from scipy.special import roots_legendre
start=time.monotonic();checks={};controls={};data=[]
def req(n,p):checks[n]=bool(p);assert p,n
def neg(n,p):controls[n]=bool(p);assert p,n
def phi(s):
    t=s-1
    return np.where(s<=1,s,np.where(s<2,s+3*t*t-t*t*t,s*s))
def integral(lam,lo=0,n=320):
    x,w=roots_legendre(n);ans=0.
    cuts=sorted(set([lo]+[v for v in [math.pi/3,math.pi/2,math.pi] if v>lo]))
    for a,b in zip(cuts,cuts[1:]):
        th=a+(b-a)*(x+1)/2
        ans+=(b-a)/math.pi*np.sum(w*np.sin(th)**2*np.exp(-lam*phi(2*(1-np.cos(th)))))
    return ans
for lam in [1,10,100,1000,10000]:
    z=integral(lam);z2=integral(lam,n=640)
    lower=math.exp(-1)/(6*math.pi)*lam**(-1.5)
    req('haar_cap_lower_'+str(lam),z>=lower)
    req('quadrature_refinement_'+str(lam),abs(z/z2-1)<1e-10)
    data.append({'lambda':lam,'integral':z,'analytic_cap_lower':lower,'minus_log_over_lambda':-math.log(z)/lam})
req('rate_tends_toward_zero_on_grid',all(b['minus_log_over_lambda']<a['minus_log_over_lambda'] for a,b in zip(data[1:],data[2:])))
neg('example_exponential_upper_c01_C10_rejected',integral(1000)>math.exp(-.1*1000+10))
for lam in [1,10,100]:
    # A genuine bad set delta>=1 has the valid exponential upper e^-lambda.
    zbad=integral(lam,lo=math.pi/3)
    req('fixed_bad_set_exponential_upper_'+str(lam),zbad<=math.exp(-lam)*(1+1e-12))
neg('removing_bad_indicator_changes_bound',integral(100)>math.exp(-100))
print(json.dumps({'checks':checks,'negative_controls':controls,'data':data,'elapsed_seconds':time.monotonic()-start,'scope':'Diagnostic for cited literature equation only; analytic cap lower bound supplies the all-lambda contradiction.'},indent=2))
