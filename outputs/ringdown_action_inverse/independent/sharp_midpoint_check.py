"""Independent sharp Lipschitz quadrature cases, zero feature noise."""
AUDIT_TIMEOUT_SEC=120
import json
from scipy.integrate import quad
rows=[]
for a,b,L in [(-1.,1.,1.),(.2,1.7,2.3),(-.4,.1,.7)]:
    m=(a+b)/2;h=b-a
    for sign in [-1,1]:
        q=lambda x:sign*L*abs(x-m)
        exact=quad(q,a,b,points=[m],epsabs=1e-13,epsrel=1e-13)[0]
        estimate=h*q(m);error=abs(exact-estimate);bound=L*h*h/4
        rows.append({'a':a,'b':b,'L':L,'sign':sign,'true_integral':exact,'midpoint':estimate,'error':error,'bound':bound,'passed':abs(error-bound)<1e-13 and error>1e-4,'missing_term_detected':error>0})
print(json.dumps({'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows},indent=2))
assert all(r['passed'] for r in rows)
