"""Independent focused finite lemma controls; no canonical imports or physical solve."""
import sympy as s,json,time
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
start=time.monotonic();u,k=s.symbols('u k',positive=True);E=(k-s.sqrt(k*k+4*u*u))/2
H=s.Matrix([[0,-u],[-u,k]]);psi=s.Matrix([1,-E/u]);assert (H*psi-E*psi).applyfunc(s.simplify)==s.zeros(2,1)
Q=s.diag(0,1);R=s.eye(2)-Q;assert (Q*(H-E*s.eye(2))*Q*psi+u*Q*s.Matrix([[0,-1],[-1,0]])*R*psi).applyfunc(s.simplify)==s.zeros(2,1)
assert H*Q!=Q*H
# Independent fixed seam face incidence, represented by unordered endpoint pairs.
rows=[]
for L in [4,6]:
 step=lambda v,a,d:tuple((v[i]+(d if i==a else 0))%L for i in range(3))
 v=(L-1,L-1,0);a=step(v,0,1);b=step(v,1,1);c=step(a,1,1);face={frozenset((v,a)),frozenset((v,b)),frozenset((a,c)),frozenset((b,c))};counts={'perpendicular':0,'opposite':0}
 for x in product(range(L),repeat=3):
  edges=[(axis,frozenset((x,step(x,axis,d)))) for axis in range(3) for d in [-1,1]]
  for e,f in combinations(edges,2):
   if (e[1] in face) != (f[1] in face):counts['opposite' if e[0]==f[0] else 'perpendicular']+=1
 assert counts=={'perpendicular':24,'opposite':8};rows.append(dict(L=L,counts=counts))
# Exact shortest removal-depth control, independent of ceiling implementation.
for m0 in [0,1,7,8,19]:
 depth=[0]*(m0+1)
 for m in range(m0+1,100):depth.append(1+min(depth[max(0,m-d)] for d in range(1,min(8,m)+1)));assert depth[m]==(m-m0+7)//8
for theta in [F(1,4),F(1,2),F(3,4)]:
 b=(1-theta)/2;A=75/(1-theta)**2;assert (1-b-theta)*A==75/(4*b)
 for m in range(1,17):assert (F(3,4)*m-F(m,4))==F(m,2)
out=dict(status='PASS',scope='Independent symbolic noncommuting projected eigen-equation; seam incidence; exact removal depth and optimized Young identity. No perturbed native ground-state solve.',symbolic_eigenvector_and_projected_equation=True,noncommuting=True,seam_faces=rows,depth_max=99,young_theta=['1/4','1/2','3/4'],seconds=time.monotonic()-start)
Path('/private/tmp/review-drain-20260915/check8060/control.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
