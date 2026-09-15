"""Independent exact sensitive controls, no canonical code imports."""
from pathlib import Path
import sympy as s,itertools,json,time,signal
signal.alarm(30);start=time.monotonic();I=s.I;one=s.eye(2);z=s.diag(1,-1);low=s.Matrix([[0,1],[0,0]])
a=[s.kronecker_product(*([z]*j+[low]+[one]*(2-j))) for j in range(3)];vac=s.eye(8)[:,0]
# Non-Hermitian odd creator, with one- and three-particle parts; subtract actual linear part.
Y=(s.Rational(2,3)+I/5)*a[0].H+(s.Rational(3,7)-2*I/3)*a[0].H*a[1].H*a[2].H+a[2]
Z=Y-(s.Rational(2,3)+I/5)*a[0].H
for ids in itertools.permutations(range(3)):
 B=Z
 for parity,j in zip([1,0,1],ids):B=a[j]*B-(-1)**parity*B*a[j]
 direct=a[ids[2]]*a[ids[1]]*a[ids[0]]*Z*vac
 assert B*vac==direct
energies=[s.Rational(2,7),s.Rational(3,5),s.Rational(7,4)];checks=0
for mask in range(8):
 E=sum(energies[j] for j in range(3) if mask>>j&1)
 for eps in sorted(set(energies+[sum(energies),s.Rational(1,8),s.Rational(5,2)])):
  n=sum(mask>>j&1 for j in range(3));q=sum(int(bool(mask>>j&1) and bool(energies[j]<=eps)) for j in range(3))
  assert int(bool(0<E<=eps))<=q;assert int(bool(n>=3 and 0<E<=eps))<=q*(q-1)*(q-2)//6;checks+=2
# General integration-by-parts coefficient, not a finite fitted integral.
beta,power,eps=s.symbols('beta power eps',positive=True)
assert s.simplify(1+power/(beta-power)-beta/(beta-power))==0
alpha=s.Rational(7,8);exps=[s.Rational(7,2)*alpha,32-alpha,32-33*alpha];assert exps==[s.Rational(49,16),s.Rational(249,8),s.Rational(25,8)] and min(exps)>3
# Positive-frequency spectral multiplier: row zero at vacuum, column may create.
H=s.diag(*[sum(energies[j] for j in range(3) if mask>>(2-j)&1) for mask in range(8)])
X=s.zeros(8);T=s.zeros(8)
for i,j in itertools.product(range(8),repeat=2):
 gap=H[i,i]-H[j,j]
 if gap>0:X[i,j]=Z[i,j]/gap
 if gap!=0:T[i,j]=Z[i,j]/gap
assert X.H*vac==s.zeros(8,1) and X*vac!=s.zeros(8,1)
# Separate annihilation term makes the two-sided failure explicit.
assert T.H*vac!=s.zeros(8,1)
out=dict(status='PASS',triple_graded_cases=6,occupation_predicates=checks,stieltjes_coefficient='beta/(beta-s), with s<beta and no zero atom',spatial_exponents=list(map(str,exps)),positive_frequency_adjoint_vacuum=True,two_sided_counterexample=True,scope='Independent three-mode rational CAR and symbolic bound checks; analytical continuum proof read separately',seconds=time.monotonic()-start)
Path('/private/tmp/review-drain-20260915/check8064/control.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
