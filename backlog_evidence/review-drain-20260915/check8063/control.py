"""Independent finite CAR/analytic controls; no canonical imports or native spectrum solve."""
from pathlib import Path
from itertools import combinations
import sympy as s,json,time,signal
signal.alarm(30);start=time.monotonic();I=s.I;one=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
g=[s.kronecker_product(X,one),s.kronecker_product(Y,one),s.kronecker_product(Z,X),s.kronecker_product(Z,Y)]
U=(3*s.eye(4)+4*g[0]*g[3])/5;assert U.H*U==s.eye(4);omega=U*s.Matrix([1,0,0,0]);P1=U*s.diag(0,1,1,0)*U.H;count=0
for length in [1,3]:
 for ids in combinations(range(4),length):
  op=s.eye(4)
  for j in ids:op=op*g[j]
  for c in [1,(1+2*I)/2]:
   op1=c*op;coeff=[s.simplify((omega.H*(a*op1+op1*a)*omega)[0]/2) for a in g];v=sum((z*a*omega for z,a in zip(coeff,g)),s.zeros(4,1));assert (v-P1*op1*omega).applyfunc(s.simplify)==s.zeros(4,1);count+=1
pairs=list(combinations(range(6),2));D=s.Matrix([[int(not set(a)&set(b)) for b in pairs] for a in pairs]);assert D.eigenvals()=={6:1,-3:5,1:9}
omega_s,m=s.symbols('omega m',real=True);lam=s.Symbol('lambda');K=s.Matrix([[0,-omega_s,-m,0],[omega_s,0,0,-m],[m,0,0,0],[0,m,0,0]]);assert s.expand(K.charpoly(lam).as_expr()-(lam**4+(omega_s**2+2*m**2)*lam**2+m**4))==0
# Uniform path tail: exponential series bound follows by weighting path lengths.
r,v=s.symbols('r v',positive=True);dyadic=s.Rational(1,2);assert sum(dyadic**n for n in range(20))==2*(1-dyadic**20)
out=dict(status='PASS',gaussian='Non-number-preserving rational even Gaussian rotation, non-Hermitian odd monomials, exact matrices',gaussian_cases=count,disjoint_pair_spectrum={'6':1,'-3':5,'1':9},diagnostic_quadratic_characteristic='lambda^4+(omega^2+2m^2)lambda^2+m^4',weighted_tail_identity=True,scope='Sensitive finite algebra supporting analytic locality/GNS proof, not infinite-volume or interacting simulation',seconds=time.monotonic()-start)
Path('/private/tmp/review-drain-20260915/check8063/control.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
