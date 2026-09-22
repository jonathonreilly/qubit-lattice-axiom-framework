from fractions import Fraction as F
import json
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915')
def add(a,b): return [a[i]+b[i] for i in range(3)]
def mul(a,b): return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(3)]
def scale(a,c): return [c*x for x in a]
def power(a,p):
    assert a[0]==1
    return [F(1),p*a[1],p*a[2]+p*(p-1)*a[1]**2/2]
E=[[F(1),F(c),F(0)] for c in (0,1,-1,0)]
E2=[mul(e,e) for e in E]
tr=[sum(e[i] for e in E2) for i in range(3)]
def integrand(x,j):
    A=[add([x,0,0],scale(e,1-x)) for e in E2]
    det=[F(1),F(0),F(0)]
    for a in A: det=mul(det,a)
    return scale(mul(mul(mul(power(det,F(-1,2)),add(scale(E2[j],2),scale(tr,-1))),E[j]),power(A[j],F(-1))),-x)
M=[]
for j in range(4):
    rows=[integrand(F(i,3),j) for i in range(4)]
    M.append([sum(F(w,8)*r[k] for w,r in zip((1,3,3,1),rows)) for k in range(3)])
assert M[0]==[1,0,1] and M[1]==[1,F(-5,3),-1] and M[2]==[1,F(5,3),-1]
velocity=add(M[1],scale(mul(M[0],E[1]),-1))
assert velocity==[0,F(-8,3),-2]
# Star generator with four Weyl weights 1/2 and photon weight 2.
A=[[F(0) for _ in range(5)] for _ in range(5)]
for i in range(4): A[i][i]=2; A[i][4]=-2; A[4][i]=F(-1,2)
A[4][4]=2
for v,lam in [([1]*5,0),([1,-1,0,0,0],2),([0,1,-1,0,0],2),([0,0,1,-1,0],2),([1,1,1,1,-1],4)]:
    assert [sum(a*x for a,x in zip(row,v)) for row in A]==[lam*x for x in v]
weights=[F(1,2)]*4+[F(2)]
assert all(weights[i]*A[i][j]==weights[j]*A[j][i] for i in range(5) for j in range(5))
# N=2 resonant relative source and integrated common drift.
assert (F(2)-3)/(2*2)==F(-1,4)
assert -F(5,2*(2+2))*F(2,4)==F(-5,16)
# Reject substituting boundary group-velocity excess into generic interior formula.
assert F(5,2)/3-F(7,12)==F(1,4)
out={'status':'PASS','author_imports':False,'primary_execution':False,'exact_quadratic_coframe_M':[[str(v) for v in r] for r in M],'temporal_subtracted_velocity':[str(v) for v in velocity],'weighted_star_eigenvalues':[0,2,2,2,4],'N2_relative_log_source':'-1/4','N2_common_drift':'-5/16','boundary_naive_generic_coefficient_rejected_difference_in_units_1_over_pi':'1/4','limits':'Independent finite algebra controls only; not phase existence, a full pipeline, or new primary evidence.'}
(R/'drain8159-family6-independent-control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
