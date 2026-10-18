"""Finite-field certificate for no globally flat bilinear transition at q=Q.
Input JSON decimal literals are exact rational numbers, not inferred axioms.
"""
from pathlib import Path
from fractions import Fraction
import json,math,hashlib,numpy as np
P=Path(__file__).resolve().parent;R=P.parents[4];path=R/'data/collective_corner_response/candidate.json'
d=json.loads(path.read_text(),parse_float=Fraction);sh=d['shifts'];br=d['blocks']['real'];bi=d['blocks']['imag']
points=[[(3,4,5),(5,12,13),(8,15,17)],[(7,24,25),(20,21,29),(12,35,37)]]
for t,shift in enumerate(sh):
 opposite=sh.index([-x for x in shift])
 for i in range(12):
  for j in range(12):
   assert br[t][i][j]==br[opposite][j][i]
   assert bi[t][i][j]==-bi[opposite][j][i]
assert all(a*a+b*b==c*c for point in points for a,b,c in point)

def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def rem(a,b,p):
 a=a.copy()
 while len(a)>=len(b) and any(a):
  c=a[-1]*pow(int(b[-1]),-1,p)%p;j=len(a)-len(b)
  for i,x in enumerate(b):a[j+i]=(a[j+i]-c*x)%p
  trim(a)
 return a
def gcd(a,b,p):
 while any(b):a,b=b,rem(a,b,p)
 return [(x*pow(int(a[-1]),-1,p))%p for x in a]
def cert(prime,point,staggered=True,zero_h=False):
 p=prime;ii=next(x for x in range(p) if x*x%p==p-1)
 def mod(x):
  x=Fraction(x);return x.numerator%p*pow(x.denominator%p,-1,p)%p
 B=np.array([[[ (mod(br[t][i][j])+ii*mod(bi[t][i][j]))%p for j in range(12)] for i in range(12)] for t in range(7)],dtype=np.int64)
 phases=[(a+ii*b)*pow(c,-1,p)%p for a,b,c in point]
 h=np.zeros((12,12),dtype=np.int64);hq=h.copy()
 for shift,block in zip(sh,B):
  z=math.prod(pow(int(v),int(s),p) for v,s in zip(phases,shift))%p
  h=(h+z*block)%p;hq=(hq+(-1 if staggered and sum(shift)%2 else 1)*z*block)%p
 hq=hq.astype(np.int64)
 if zero_h:h[:]=0;hq[:]=0
 def traces(a):
  power=np.eye(12,dtype=np.int64);out=[12]
  for n in range(1,145):power=power@a%p;out.append(int(np.trace(power)%p))
  return out
 t=traces(h);u=traces(hq)
 tl=[144]+[sum(math.comb(n,j)*(-1)**(n-j)*u[j]*t[n-j] for j in range(n+1))%p for n in range(1,145)]
 # det(xI-L)=x^144+c1*x^143+... ; Newton identities.
 coeff=[1]
 for n in range(1,145):coeff.append(-sum(coeff[n-j]*tl[j] for j in range(1,n+1))*pow(n,-1,p)%p)
 # Independent direct 144-dimensional matrix traces for low orders.
 L=(np.kron(np.eye(12,dtype=np.int64),hq)-np.kron(h.T,np.eye(12,dtype=np.int64)))%p
 power=np.eye(144,dtype=np.int64)
 for n in range(1,5):power=power@L%p;assert int(np.trace(power)%p)==tl[n]
 return list(reversed(coeff))
rows=[]
for p in [1009,1013]:
 polys=[cert(p,point) for point in points];g=gcd(*polys,p);row=dict(prime=p,degree=144,gcd_degree=len(g)-1,gcd=g,polynomials_ascending=polys);rows.append(row);print('prime',p,'gcd degree',len(g)-1,flush=True)
 assert g==[1],g
controls=[]
for label,kw in [('conserved_q0',dict(staggered=False)),('zero_hamiltonian',dict(zero_h=True))]:
 polys=[cert(1009,point,**kw) for point in points];g=gcd(*polys,1009);degree=len(g)-1
 assert degree>=12 if label=='conserved_q0' else degree==144
 controls.append(dict(control=label,gcd_degree=degree));print(label,degree,flush=True)
(P/'exact_no_flat_transition.json').write_text(json.dumps(dict(input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),scope='Exact decimal-rational candidate; q=Q only; two rational unit-circle momenta; finite-field coprimality certificate. No statement for arbitrary other q or interacting Hamiltonians.',phase_triples=points,controls=controls,rows=rows),indent=2)+'\n')
