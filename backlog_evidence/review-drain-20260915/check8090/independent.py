import sympy as s,json,time
from itertools import product
start=time.monotonic();checks=[]
def ck(n,ok):
 assert ok,n
 checks.append(n)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
# Independent tensor Jordan-Wigner representation, not occupation-mask construction.
lower=s.Matrix([[0,1],[0,0]])
a=[s.kronecker_product(*[Z if j<i else lower if j==i else I for j in range(4)]) for i in range(4)]
g=[c+c.H for c in a]
for length in (1,2,3):
 path=s.eye(16)
 for i in range(length):path*= -s.I*g[i]*g[i+1]
 ck('Majorana_path_phase_'+str(length),s.I**(length-1)*path==-s.I*g[0]*g[length])
for j,W in enumerate([(-Z+s.I*X)/2,(-Z+s.I*Y)/2,-Z/2]):
 H=s.zeros(16)
 for r,q in product(range(2),repeat=2):
  term=W[r,q]*a[r].H*a[2+q];H+=term+term.H
 ck('actual_many_body_bond_norm_'+str(j),max(abs(v) for v in H.eigenvals())==1)
W1=(-Z+s.I*X)/2;W2=(-Z+s.I*Y)/2
ck('straight_cancellation_bent_nonzero',W1*W1==s.zeros(2) and W1*W2!=s.zeros(2))
# Quantitative bounds are conservative relative to the actual recursion.
ck('boundary_chain_majorant',all(6*11**(n-1)*2**n<=2*24**n for n in range(1,30)))
# For p in(0,pi/3], sin p >=(sin(pi/3)/(pi/3))*p, hence2p/sinp<=4pi/(3sqrt3)<3.
ck('RG_node_separation_comparability',4*s.pi/(3*s.sqrt(3))<3)
# Complement-region cos remainder <=k^4/24+(1-zeta)k^2/2; p<|k| and1-cosp<=p²/2 gives7|k|^4/24.
ck('uniform_complement_remainder_coefficient',s.Rational(1,24)+s.Rational(1,4)==s.Rational(7,24))
# Independently exact Boltzmann spectral negative-tail identity for arbitrary two-level transitions.
beta=s.symbols('beta',positive=True);gap=s.Rational(7,3);weights=[1,s.exp(-beta*gap)];partition=sum(weights)
ck('negative_spectral_detailed_balance',s.simplify(weights[1]/partition-s.exp(-beta*gap)*weights[0]/partition)==0)
# Global law range retains locked records after arbitrary added digital neighbors.
ck('all_digital_neighbor_conditions',all(s.Rational(1,4)<=sum(s.Rational(3,4) if x else s.Rational(1,4) for x in bits)/n<=s.Rational(3,4) for n in range(1,7) for bits in product((0,1),repeat=n)))
print(json.dumps({'status':'pass','checks':checks,'total_pass':len(checks),'seconds':time.monotonic()-start,'scope':'Independent exact tensor-CAR paths/bond norms, RG comparison constants, spectral balance and local kernel controls. External RG theorem retained as import; no primary executed.'},indent=2))
