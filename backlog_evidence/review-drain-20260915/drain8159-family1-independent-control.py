"""Bounded reviewer controls; no imports or execution of author sources."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math,cmath
R=Path('/private/tmp/review-drain-20260915')
def matmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def trans(a):return list(map(list,zip(*a)))
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def comm(a,b):return sub(matmul(a,b),matmul(b,a))
def diag(v):return [[x if i==j else 0 for j,x in enumerate(v)] for i in range(len(v))]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,s):return [[s*x for x in r] for r in a]
# Exhaust full ambient electric/occupation space, not reduced-coordinate source.
census=[]
for N in [3,5,7]:
 S=N//2; total=aliases=0
 for fields in product(range(-S,S+1),repeat=4):
  div=[fields[i]-fields[(i-1)%4] for i in range(4)]
  for bits in product([0,1],repeat=8):
   q=[bits[2*i]-bits[2*i+1] for i in range(4)]
   G=[a-b for a,b in zip(div,q)]
   if all(v%N==0 for v in G):
    total+=1; aliases+=any(G)
    for i in range(4):
     assert (N*N if G[i] else 0)<=3*(fields[i]**2+fields[(i-1)%4]**2+1)
 census.append([N,total,aliases])
assert census==[[3,258,106],[5,350,58],[7,490,58]]
# Ring CAR matrix from literal occupation sequences and wedge reordering.
occupations=list(__import__('itertools').combinations(range(4),2)); offsets=[]; As=[]; Cs=[]
forward=[[0]*6 for _ in range(6)]
for j,occ in enumerate(occupations):
 q=[int(x in occ)-int(x in (1,3)) for x in range(4)]
 e=[sum(q[:i+1]) for i in range(3)]+[0];offsets.append(e)
 A=F(sum(e),4);As.append(A);Cs.append(sum(F(v*v,2) for v in e)-2*A*A)
for j,occ in enumerate(occupations):
 for edge in range(4):
  destroy=(edge+1)%4
  if destroy not in occ or edge in occ:continue
  mid=list(occ);loc=mid.index(destroy);mid.pop(loc);sign=(-1)**loc
  pos=sum(x<edge for x in mid);sign*=(-1)**pos;mid.insert(pos,edge)
  row=occupations.index(tuple(mid));forward[row][j]+=sign*(-1 if edge==3 else 1)
  assert As[row]-As[j]+int(edge==3)==F(1,4)
assert comm(forward,trans(forward))==[[0]*6 for _ in range(6)]
# Occupation order combinations differs from bitmask order. Weights from two filled signed-ring plane waves.
ks=[3*math.pi/4,5*math.pi/4]; probs=[]
for i,j in occupations:
 amp=(cmath.exp(1j*(ks[0]*i+ks[1]*j))-cmath.exp(1j*(ks[1]*i+ks[0]*j)))/4
 probs.append(abs(amp)**2)
assert abs(sum(probs)-1)<1e-14
Cmean=sum(float(c)*p for c,p in zip(Cs,probs));assert abs(Cmean-5/16)<1e-14
# Wick gaussian fourth moment gives quartic coefficient  -(2j²+2j+1)/128.
c2=[F(5,16)-F(2*j*j+2*j+1,128) for j in range(4)]
assert c2==[F(39,128),F(35,128),F(27,128),F(15,128)]
# Exact shear and weighted optical matrix minimal polynomial.
K=[[4,1],[1,2]];J=[[1,0],[F(-1,4),1]]
assert matmul(matmul(J,K),trans(J))==[[4,0],[0,F(7,4)]]
optical=[]
for d,c,s in [([2,3,5],F(7,3),[1,2,3]),([F(1,2),F(4,3),F(7,5)],F(3,2),[2,-3,5])]:
 x,y,z=s;X=[[0,-z,y],[z,0,-x],[-y,x,0]];D=diag(d)
 A=scale(matmul(matmul(matmul(D,trans(X)),D),X),c)
 lam=c*sum(d[(i+1)%3]*d[(i+2)%3]*s[i]**2 for i in range(3))
 assert matmul(A,A)==scale(A,lam) and sum(A[i][i] for i in range(3))==2*lam
 optical.append(str(lam))
# Exact one-rotor commutators, retaining boundary failure for magnetic identity.
S=3;E=diag(list(range(-S,S+1)));U=[[int(i==j+1) for j in range(7)] for i in range(7)]
cos=scale(add(U,trans(U)),F(1,2));sin_numerator=sub(U,trans(U));H=scale(matmul(E,E),F(1,2))
# sin= numerator/(2i), so double commutator obtains -1/4.
lhs=scale(comm(sin_numerator,comm(H,sin_numerator)),F(-1,4));rhs=matmul(cos,cos);diff=sub(lhs,rhs)
assert all(diff[i][j]==0 for i in range(1,6) for j in range(1,6)) and any(diff[0])
# Electric double commutator includes same q² for +/- charges.
for T in [U,trans(U)]:
 assert comm(E,comm(add(T,trans(T)),E))==scale(add(T,trans(T)),-1)
# Full ground-space removal: variance1 is entirely elastic.
Hd=diag([0,0,2]);Fop=[[0,1,0],[1,0,0],[0,0,0]]
assert matmul(matmul(Fop,Hd),Fop)[0][0]==0 and matmul(Fop,Fop)[0][0]==1
# Product vs series normalization at alpha=2z; explicitly retain positive theta and minimum.
theta_error=0
for t in [.4,1,2]:
 vals=[]
 for a in [0,.7,math.pi]:
  series=1+2*sum(math.exp(-t*n*n)*math.cos(n*a) for n in range(1,40))
  prod=math.prod((1-math.exp(-2*t*n))*(1+2*math.exp(-(2*n-1)*t)*math.cos(a)+math.exp(-(4*n-2)*t)) for n in range(1,100))
  theta_error=max(theta_error,abs(series-prod)); vals.append(series)
 assert min(vals)>0 and vals[2]<vals[1]<vals[0]
assert theta_error<1e-13
out={'status':'PASS','primary_execution':False,'author_imports':False,'ambient_modular_census_N_dimension_aliases':census,'ring_charge_variance':Cmean,'ring_second_coefficients':[str(x) for x in c2],'tangent_schur':'7/4','weighted_optical_exact_double_eigenvalues':optical,'magnetic_boundary_difference':str(diff[0][0]),'opposite_charge_squared_addition':'verified','degenerate_elastic_variance':1,'degenerate_inelastic_variance':0,'theta_product_series_error':theta_error,'scope':'Finite independent algebra controls plus complete proof review; no phase, whole-pipeline or primary recapture.'}
(R/'drain8159-family1-independent-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
