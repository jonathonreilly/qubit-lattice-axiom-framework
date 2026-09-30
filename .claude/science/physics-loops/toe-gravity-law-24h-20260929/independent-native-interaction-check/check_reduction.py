"""Small exact reductions of the already independently assembled matrices."""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict
from fractions import Fraction as F
import json,time
t0=time.perf_counter()
out=Path(__file__).parent
d=json.loads((out/'quartic_matrices.json').read_text());mon=d['monomial_order']
idx={tuple(x):i for i,x in enumerate(mon)}
names=['mu_energy_gram_numerator_denominator_12','tau_energy_gram_numerator_denominator_12',
       'number_t4_gram_numerator_denominator_3']
G=[d[x] for x in names]
unit=[[int(i==j) for j in range(5)] for i in range(5)]
T=[[unit[0],unit[2],unit[3]],[unit[2],unit[1],unit[4]],
   [unit[3],unit[4],[-1,-1,0,0,0]]]
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
count=0
for p in permutations(range(3)):
 for sign in product([-1,1],repeat=3):
  if parity(p)*sign[0]*sign[1]*sign[2]!=1:continue
  L=[]
  for i,j in [(0,0),(1,1),(0,1),(0,2),(1,2)]:L.append([sign[i]*sign[j]*x for x in T[p[i]][p[j]]])
  U=[]
  for i,j in mon:
   row=[0]*15
   for k in range(5):
    for l in range(5):row[idx[tuple(sorted((k,l)))]]+=L[i][k]*L[j][l]
   U.append(row)
  for A in G:
   AU=[[sum(A[i][k]*U[k][j] for k in range(15)) for j in range(15)] for i in range(15)]
   transformed=[[sum(U[k][i]*AU[k][j] for k in range(15)) for j in range(15)] for i in range(15)]
   assert transformed==A
  count+=1

def polynomial(powers):return {tuple(powers):F(1)}
def add(*terms):
 z=defaultdict(F)
 for scale,P in terms:
  for e,x in P.items():z[e]+=scale*x
 return {e:x for e,x in z.items() if x}
def mul(P,Q):
 z=defaultdict(F)
 for e,x in P.items():
  for f,y in Q.items():z[tuple(a+b for a,b in zip(e,f))]+=x*y
 return dict(z)
a,b,p,q,r=[polynomial([int(i==j) for j in range(5)]) for i in range(5)]
D2=add((2,mul(a,a)),(2,mul(a,b)),(2,mul(b,b)))
U=add((1,mul(p,p)),(1,mul(q,q)),(1,mul(r,r)))
V4=add(*[(1,mul(mul(x,x),mul(x,x))) for x in [p,q,r]])
ab=add((1,a),(1,b))
W=add((1,mul(mul(ab,ab),mul(p,p))),(1,mul(mul(b,b),mul(q,q))),
      (1,mul(mul(a,a),mul(r,r))))
basis=[mul(D2,D2),mul(D2,U),W,mul(U,U),V4]
coeffs=[[F(52),F(512,3),F(202,3),F(772,3),F(-124,3)],
        [F(120),F(592),F(-4),F(704),F(-80)],
        [F(-5,3),F(-40,3),F(16),F(8,3),F(-28,3)]]
for A,den,coef in zip(G,[12,12,3],coeffs):
 P=defaultdict(F)
 for i,(a,b) in enumerate(mon):
  for j,(c,e) in enumerate(mon):
   powers=[0]*5
   for k in [a,b,c,e]:powers[k]+=1
   P[tuple(powers)]+=F(A[i][j],den)
 assert {e:x for e,x in P.items() if x}==add(*zip(coef,basis))
result={'full_complex_coefficient_covariance_rotations':count,
        'all_real_quartic_coefficients_match_compact_form':True,
        'real_invariant_order':['D2^2','D2 U','W','U^2','V4'],
        'real_invariant_coefficients':[[str(x) for x in row] for row in coeffs],
        'elapsed_seconds':time.perf_counter()-t0}
(out/'reduction_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
