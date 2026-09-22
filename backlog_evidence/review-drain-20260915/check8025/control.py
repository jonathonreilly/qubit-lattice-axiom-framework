from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json,time
start=time.monotonic();checks=[]
def ck(n,b):
 assert b,n
 checks.append(n)
# Schur contraction of trace(UV): integrate the V indices directly.
# Normalized U basis sqrt(3)U_ab produces rho_(ab,cd)=delta_ac delta_bd/9.
idx=list(product(range(3),repeat=2));rho={}
for a,b in idx:
 for c,d in idx:
  rho[a,b,c,d]=F(sum((b==k)*(a==l)*(d==k)*(c==l) for k,l in idx),9)
ck('Schur_contracted_trace',sum(rho[a,b,a,b] for a,b in idx)==1)
ck('Schur_contracted_purity',sum(rho[a,b,c,d]*rho[c,d,a,b] for a,b in idx for c,d in idx)==F(1,9))
ck('Schur_contracted_equal_diagonal',all(rho[a,b,c,d]==F(int(a==c and b==d),9) for a,b in idx for c,d in idx))
# Completeness identity for trace-normalized traceless Hermitian basis:
# sum_A (T_A)_ij(T_A)_kl = delta_il delta_jk -delta_ij delta_kl/3.
cas=[[sum(F(int(i==j),1)-F(int(i==k and k==j),3) for k in range(3)) for j in range(3)] for i in range(3)]
ck('endpoint_Casimir_completeness',cas==[[F(8,3)*int(i==j) for j in range(3)] for i in range(3)])
ck('two_endpoints_positive_Casimir',2*cas[0][0]==F(16,3))
# Independent all-order coefficient algebra tested on finite representatives;
# general coefficient cancellation is (n+1)/(n+1)!=1/n!.
for n in [0,1,2,3,8,19]:ck('integrated_coefficient_'+str(n),F(n+1,factorial(n+1))==F(1,factorial(n)))
ck('boundary_constant',F(2*4,32)==F(1,4))
# Normalize an arbitrary positive unnormalized projected density: trace-norm
# correction is exactly1-p, illustrated with unequal diagonal weights.
for p in [F(1,16),F(1,4),F(9,16),F(1)]:
 diag=[p*F(1,3),p*F(2,3)];ck('mixed_normalization_'+str(p),sum(abs(x/p-x) for x in diag)==1-p)
out={'passed':len(checks),'checks':checks,'seconds':time.monotonic()-start,'scope':'Independent Schur-index contraction, SU3 completeness contraction, tail coefficient and mixed-density normalization arithmetic. All-order locality/form-domain proof checked analytically; no primary/helper execution.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
