"""Post-freeze comparison and independent expansion of printed invariants.

Reads frozen author DATA only; no author code is imported or executed.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
import json,time,hashlib
t0=time.perf_counter()
out=Path(__file__).parent; root=out.parent
own=json.loads((out/'quartic_matrices.json').read_text())
author=json.loads((root/'native-interaction-route/quartic.json').read_text())
mon=own['monomial_order'];idx={tuple(x):i for i,x in enumerate(mon)}
assert [[author['coordinates'].index(x) for x in row] for row in author['monomial_order']]==mon
keys=[('energy_mu_matrix_numerator','mu_energy_gram_numerator_denominator_12',12),
      ('energy_tau_matrix_numerator','tau_energy_gram_numerator_denominator_12',12),
      ('number_quartic_matrix_numerator','number_t4_gram_numerator_denominator_3',3)]
for a,b,den in keys:assert author[a]==own[b]
assert author['energy_denominator']==12 and author['number_quartic_denominator']==3

def clean(P):return {e:x for e,x in P.items() if x}
def add(*terms):
 P=defaultdict(F)
 for a,Q in terms:
  for e,x in Q.items():P[e]+=a*x
 return clean(P)
def mul(P,Q):
 R=defaultdict(F)
 for e,x in P.items():
  for f,y in Q.items():R[tuple(a+b for a,b in zip(e,f))]+=x*y
 return clean(R)
def conjugate(P):return {e[5:]+e[:5]:x for e,x in P.items()}
def real(P):return add((F(1,2),P),(F(1,2),conjugate(P)))
def square(P):return mul(P,P)
def abs2(P):return mul(P,conjugate(P))
var=[{tuple(int(j==i) for j in range(10)):F(1)} for i in range(5)]
u=[var[0],var[1],add((-1,var[0]),(-1,var[1]))]
v=[var[4],var[3],var[2]]
U=add(*[(1,abs2(x)) for x in u]); p=add(*[(1,abs2(x)) for x in v])
qE=add(*[(1,square(x)) for x in u]);qT=add(*[(1,square(x)) for x in v])
r=add(*[(1,square(abs2(x))) for x in v])
J=add(*[(1,mul(abs2(x),abs2(y))) for x,y in zip(u,v)])
L4=add(*[(1,mul(square(x),conjugate(square(y)))) for x,y in zip(u,v)])
M4={}
for i in range(3):
 j,k=[a for a in range(3) if a!=i]
 M4=add((1,M4),(1,mul(mul(conjugate(u[i]),conjugate(v[i])),mul(v[j],v[k]))))
cross=real(mul(qE,conjugate(qT)))
printed=[
 add((52,square(U)),(F(700,3),square(p)),(24,abs2(qT)),(F(-124,3),r),
     (F(490,3),mul(U,p)),(66,J),(F(22,3),cross),(F(4,3),real(L4)),(-48,real(M4))),
 add((120,square(U)),(632,square(p)),(72,abs2(qT)),(-80,r),(620,mul(U,p)),
     (-60,J),(-28,cross),(56,real(L4)),(-96,real(M4))),
 add((F(-26,9),square(U)),(F(11,9),abs2(qE)),(F(-16,3),square(p)),
     (8,abs2(qT)),(F(-28,3),r),(-16,mul(U,p)),(F(32,3),J),
     (F(8,3),cross),(F(16,3),real(L4))) ]
def matrix(P):
 A=[[F(0)]*15 for _ in range(15)]
 for powers,x in P.items():
  h=[i for i in range(5) for _ in range(powers[i])]
  c=[i for i in range(5) for _ in range(powers[i+5])]
  assert len(h)==len(c)==2
  A[idx[tuple(c)]][idx[tuple(h)]]+=x
 return A
for P,(_,key,den) in zip(printed,keys):
 assert matrix(P)==[[F(x,den) for x in row] for row in own[key]]

# Reconstruct the quartic positivity certificate from OUR matrices and the
# independently expanded norm polynomial, not the author's LDL output.
norm2=square(add((1,U),(2,p)))
certificates=[]
for P,bound in zip(printed[:2],[40,100]):
 A=matrix(add((1,P),(-bound,norm2)));n=len(A)
 L=[[F(int(i==j)) for j in range(n)] for i in range(n)];D=[]
 for i in range(n):
  pivot=A[i][i]-sum(L[i][k]**2*D[k] for k in range(i))
  assert pivot>0;D.append(pivot)
  for j in range(i+1,n):
   L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/pivot
 assert [[sum(L[i][k]*D[k]*L[j][k] for k in range(n)) for j in range(n)]
         for i in range(n)]==A
 certificates.append({'subtracted_pair_norm_squared_multiple':bound,
                      'positive_LDL_pivots':[str(x) for x in D],
                      'exact_reconstruction':True})
result={'author_report_sha256':hashlib.sha256((root/'native-interaction-route/REPORT.md').read_bytes()).hexdigest(),
        'matched_matrix_entries':675,'matched_complex_invariant_entries':675,
        'monomial_order_translation_verified':True,'positivity_certificates':certificates,
        'author_code_imported_or_executed':False,'elapsed_seconds':time.perf_counter()-t0}
(out/'comparison_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
