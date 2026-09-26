from pathlib import Path
import sympy as s
import hashlib,json

a=s.symbols('a',real=True)
residual=s.log((s.cosh(a)+2)/3)
assert s.simplify(s.diff(residual,a,2).subs(a,0))==s.Rational(1,3)
assert s.simplify(residual.subs(a,s.log(2))-s.log(s.Rational(13,12)))==0
w=s.symbols('w',positive=True)
drift=sum((w*s.eye(3)[:,i]/6-w*s.eye(3)[:,i]/6 for i in range(3)),s.zeros(3,1))
assert drift==s.zeros(3,1)
# One-dimensional periodic restriction: nonuniform residence weights, zero
# conditional lifted displacement. The 3D six-direction formula is above.
rates=[s.Rational(1),s.Rational(2),s.Rational(3),s.Rational(4),s.Rational(5)]
L=s.zeros(5)
for i,r in enumerate(rates):
    for sign in [-1,1]:L[i,(i+sign)%5]+=r/2
    L[i,i]-=r
pi=s.Matrix([[1/r for r in rates]]);pi/=sum(pi)
assert pi*L==s.zeros(1,5)
assert all(r/2-r/2==0 for r in rates)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'arithmetic_mean_nonlinear_residual_at_log2':str(residual.subs(a,s.log(2)).simplify()),
     'residual_second_derivative_at_zero':'1/3',
     'symmetric_departure_clock_conditional_lifted_drift':'zero',
     'inverse_rate_stationary_law_exact':True,
     'scope':'Author checks of narrow reading observations; no complete PR review or audit verdict.'}
(Path(__file__).parent/'LATEST_CLOCK_SCOPE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
