"""Independent six added maps: exact species covariance, constraints, determinant."""
from pathlib import Path
from itertools import product,permutations
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
D=[s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)]
pairs=[(0,1),(0,2),(1,2)];Q=[]
for i,j in pairs:
 M=s.zeros(3);M[i,j]=M[j,i]=1/s.sqrt(2);Q.append(M)
labels=[('0',(0,0,0))]+[('A',tuple(sign*int(k==i) for k in range(3))) for i in range(3) for sign in (-1,1)]+[('B',b) for b in product((-1,1),repeat=3)]
index={a:i for i,a in enumerate(labels)};U=s.zeros(15,14)
for row,(kind,feature) in enumerate(labels):
 e=s.Matrix(feature if kind=='A' else (0,0,0));b=s.Matrix(feature if kind=='B' else (0,0,0))
 for i in range(3):U[row,i]=e[i]/s.sqrt(2);U[row,5+i]=b[i]/s.sqrt(8)
 U[row,3]=(4*int(kind=='A')-3*int(kind=='B'))/s.sqrt(168)
 U[row,4]=(14*int(kind=='0')-int(kind!='0'))/s.sqrt(210)
 for a in range(2):U[row,8+a]=(e.T*D[a]*e)[0]/s.sqrt(2)
 for a,(i,j) in enumerate(pairs):U[row,10+a]=b[i]*b[j]/s.sqrt(8)
 U[row,13]=b[0]*b[1]*b[2]/s.sqrt(8)
assert U.T*U==s.eye(14)
def cross(q):return s.Matrix([[0,-q[2],q[1]],[q[2],0,-q[0]],[-q[1],q[0],0]])
def symbol(q,c):
 a1,a2,m,u,v,b1,b2,bu,bv,d,g=c;M=s.zeros(14);C=cross(q)
 M[0:3,3]=a1*q;M[0:3,4]=a2*q;M[0:3,5:8]=m*C
 M[5:8,3]=b1*q;M[5:8,4]=b2*q
 for j in range(2):
  M[0:3,8+j]=u*D[j]*q;M[5:8,8+j]=bu*D[j]*q
 for j in range(3):
  M[0:3,10+j]=v*Q[j]*q;M[5:8,10+j]=bv*Q[j]*q
  for k in range(2):M[10+j,8+k]=d*s.trace(Q[j]*(C*D[k]-D[k]*C))
 M[10:13,13]=g*s.Matrix([q[2],q[1],q[0]])
 return M+M.T
units=[s.eye(3)[:,i] for i in range(3)]
channels=[[symbol(q,[int(k==a) for k in range(11)]) for q in units] for a in range(11)]
# Complete actual proper label action, not a substituted continuum-tensor action.
group=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
  R=s.zeros(3)
  for i in range(3):R[i,perm[i]]=signs[i]
  if R.det()!=1:continue
  dest=[index[kind,tuple(map(int,R*s.Matrix(feature)))] for kind,feature in labels]
  group.append((R,dest))
assert len(group)==24
for a in range(5,11):
 tensors=[(U*M*U.T).applyfunc(s.simplify) for M in channels[a]]
 for R,dest in group:
  for i in range(3):
   j=next(k for k in range(3) if R[k,i]);sign=R[j,i]
   assert tensors[j].extract(dest,dest)==sign*tensors[i]
flat=s.Matrix.hstack(*[s.Matrix([x for M in ch for x in M]) for ch in channels]);assert flat.rank()==11
q=s.Matrix(s.symbols('q1:4',real=True));c=s.symbols('a1 a2 m u v b1 b2 bu bv d g',real=True)
A=symbol(q,c);T=s.diag(*([-1]*3+[1]*11))
assert T*symbol(q,c[:5]+(0,)*6)*T==-symbol(q,c[:5]+(0,)*6)
assert T*symbol(q,(0,)*5+c[5:])*T==symbol(q,(0,)*5+c[5:])
# Constraint coefficient systems, collecting all q-polynomial coefficients.
vector=[0,1,2,5,6,7];other=[i for i in range(14) if i not in vector]
def equations(M):
 out=[]
 for x in M:
  out.extend(s.Poly(s.expand(x),*q).coeffs())
 return out
closed=equations(A.extract(vector,other))
G=s.zeros(2,14);G[0,0:3]=q.T;G[1,5:8]=q.T
raw=equations(G*A)
R=s.zeros(6,14);R[0:3,5:8]=cross(q);R[3:6,0:3]=-cross(q)
curl=equations((R*A).extract(range(6),other))
expected8={c[i]:0 for i in [0,1,3,4,5,6,7,8]}
expected4={c[i]:0 for i in [3,4,7,8]}
assert s.solve(closed,c,dict=True)==[expected8]
assert s.solve(raw,c,dict=True)==[expected8]
assert s.solve(curl,c,dict=True)==[expected4]
# Longitudinal vector data are also invisible to derivative readout at all allowed coefficients.
long=s.zeros(14,2);long[0:3,0]=q;long[5:8,1]=q
assert (R*A*long).subs(expected4)==s.zeros(6,2)
C=A.extract([10,11,12],[8,9,13]);det=s.factor(C.det())
assert det==-6*s.sqrt(3)*c[9]**2*c[10]*q[0]*q[1]*q[2]
example=A.subs(expected8).subs({c[2]:1,c[9]:1,c[10]:1,q[0]:1,q[1]:2,q[2]:3})
assert example.rank()==10
# Generic species realization has derivative (2/15)S on the tangent, so S=15/2 UAU^T.
for a in range(5,11):
 for M in channels[a]:
  S=s.Rational(15,2)*U*M*U.T
  assert S==S.T and S*s.ones(15,1)==s.zeros(15,1)
  assert (U.T*(s.Rational(2,15)*S)*U-M).applyfunc(s.simplify)==s.zeros(14)
output={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'all exact assertions passed',
 'proper_group_elements':24,'six_extra_actual_species_covariance':True,'all_eleven_independent':True,
 'vector_closure_conditions':[str(x) for x in expected8], 'raw_gauss_conditions_same':True,
 'curl_closure_conditions':[str(x) for x in expected4],'longitudinal_kernel_checked':True,
 'nonvector_determinant':str(det),'generic_closed_vector_example_rank':10,
 'extra_reversal_even_old_reversal_odd':True,'six_extra_uniform_current_normalizations':True,
 'scope':'Exact finite symbol/realization checks; no new continuum theorem, no interpretation of extra moments.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
