import json,time,signal,math
from fractions import Fraction as Q
from collections import defaultdict
signal.alarm(30);start=time.monotonic()
# Independent nearest-neighbor walk dynamic programming, not closed return formula.
d={(0,0,0):1};returns=[]
for step in range(1,13):
 nxt=defaultdict(int)
 for x,c in d.items():
  for a in range(3):
   for sign in (-1,1):
    y=list(x);y[a]+=sign;nxt[tuple(y)]+=c
 d=nxt
 if step%2==0:
  n=step//2;actual=d[(0,0,0)];formula=math.comb(2*n,n)*sum(math.comb(n,j)**2*math.comb(2*j,j) for j in range(n+1))
  assert actual==formula;returns.append(actual)
# Clifford relations by tensor Pauli matrices, independent of occupation-bit builders.
import sympy as s
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
g=[s.kronecker_product(X,I),s.kronecker_product(Y,I),s.kronecker_product(Z,X),s.kronecker_product(Z,Y)]
H=s.diag(0,3,2,5);B=s.I*g[0]*(g[1]+g[2]);D=H+6*s.eye(4)+B;R=-D.inv()
a=(g[0]+s.I*g[1])/2;w=2;L=a*B-B*a;Rw=-(D+w*s.eye(4)).inv()
assert a*R==Rw*a+Rw*L*R
assert a*R!=R*a+R*L*R
# Exact real-spectral inverse derivative, both placements, noncommuting perturbations.
x=s.Symbol('x');W=s.I*g[0]*g[3];G=g[0];F=-(D+x*W).inv()*G*-(D+x*W).inv()
first=F.diff(x).subs(x,0)
assert first==R*W*R*G*R+R*G*R*W*R
assert first!=R*W*R*G*R
# Independent rational constants and domain estimate.
Btail=Q(4,3)*726*128**3;C=Q(90,8)*(2*8**3+24*8**4);e=Q(1,2**21)
err=(4*C+47520*Q(22,7))*e+Btail*Q(22,7)*e**3/24
assert Btail==2030043136 and C==1117440 and err<Q(7,2)
result={'status':'passed','scope':'independent walk DP and exact tensor-Pauli CAR inverse identities, plus rational operator constants; no primary execution','walk_return_counts':returns,'CAR_controls':['shifted pull-through','wrong unshifted control rejected','two-sided inverse derivative','omitted placement rejected'],'operator_relative_upper':str(err/7),'seconds':time.monotonic()-start}
print(json.dumps(result,indent=2))
