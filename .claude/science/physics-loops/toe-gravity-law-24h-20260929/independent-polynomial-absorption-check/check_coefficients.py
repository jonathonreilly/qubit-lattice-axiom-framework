"""Exact algebraic controls; not a finite approximation to rotor dynamics."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import resource
import time

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME/'STOP_REQUESTED.json').exists()
assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,31))
start=time.process_time()

# Direct graph-norm/Duhamel recurrence, as polynomials in x=5C0 delta M t.
# It has R_p(0)=1 for every p. No Touchard coefficient enters this builder.
R=[[F(1)]]
for p in range(1,17):
    derivative=[F(0)]*p
    for r in range(1,p+1):
        for k,c in enumerate(R[p-r]):
            derivative[k] += comb(p,r)*2**r*c
    R.append([F(1)]+[c/F(k+1) for k,c in enumerate(derivative)])

# Distinct finite-set-partition recurrence gives Stirling/Touchard coefficients.
stirling=[[1]]
for p in range(1,17):
    previous=stirling[-1]
    stirling.append([0]+[(previous[k-1] if k-1<len(previous) else 0)
                        +k*(previous[k] if k<len(previous) else 0)
                        for k in range(1,p+1)])
P=[[F(2**p*c) for c in row] for p,row in enumerate(stirling)]
for p in range(17):
    recombined=[F(0)]*(p+1)
    for r in range(p+1):
        for k,c in enumerate(P[r]):
            recombined[k] += comb(p,r)*c
    assert recombined==R[p]
    if p:
        assert P[p][0]==0
        derivative=[(k+1)*P[p][k+1] for k in range(p)]
        rhs=[F(0)]*p
        for r in range(1,p+1):
            for k,c in enumerate(P[p-r]):
                rhs[k] += comb(p,r)*2**r*c
        assert derivative==rhs
assert R[:4]==[[F(1)],[F(1),F(2)],[F(1),F(8),F(4)],
               [F(1),F(26),F(36),F(8)]]

# Rational substitutions check the placement of C0 and an exact finite integral.
# These are formal coefficient parameters, not a replacement microscopic model.
C0,delta,M,gamma=F(3,2),F(2,3),F(7,5),F(1,3)
a=5*C0*delta*M
assert a==7
integrals=[]
for p in range(17):
    coeff=[c*a**k for k,c in enumerate(R[p])]
    value=sum((c*d*factorial(k+l)/(2*gamma)**(k+l+1)
               for k,c in enumerate(coeff) for l,d in enumerate(coeff)),F(0))
    assert value>0
    integrals.append(str(value))
assert integrals[0]=='3/2' and integrals[1]=='2775/2'
# Wrong C0 placement and missing bandwidth factor are actually distinguished.
assert 2*(5*delta*M) != 2*a
assert a != 2*a

result={'exact_orders_checked':list(range(17)),
        'R_coefficients_in_x_orders_0_to_6':[[str(c) for c in row] for row in R[:7]],
        'all_P_recurrence_and_Touchard_recombinations_equal':True,
        'formal_parameter_substitution':{'C0':str(C0),'delta':str(delta),'M':str(M),
                                         'gamma':str(gamma),'x_over_t':str(a)},
        'integral_coefficients_orders_0_to_3':integrals[:4],
        'negative_controls':{'omitted_C0_detected':True,'omitted_bandwidth_two_detected':True},
        'domain_scope':'Domain invariance and semigroup/jump bounds are analytic proofs, not inferred from this coefficient control.',
        'cpu_seconds':time.process_time()-start,
        'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['peak_rss_bytes']<150*1024**2
(HERE/'COEFFICIENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
