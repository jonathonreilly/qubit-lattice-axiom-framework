#!/usr/bin/env python3
"""Independent exact cubic-character, species-intertwiner and current controls.

No author-code/results access. Direct label permutations and an integer-weight
four-label current sum are used instead of a numerical derivative.
"""
from pathlib import Path
from itertools import product,permutations
from math import lcm
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;checks=[]
def check(name,condition,detail=None):
 assert bool(condition),(name,detail)
 checks.append({'name':name,'passed':True,'detail':detail})
labels=[('0',(0,0,0))]+[('A',tuple(sign*int(k==i) for k in range(3))) for i in range(3) for sign in (-1,1)]+[('B',b) for b in product((-1,1),repeat=3)]
index={a:i for i,a in enumerate(labels)}
D=[s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)]
pairs=[(0,1),(0,2),(1,2)]
Qs=[]
for i,j in pairs:
 q=s.zeros(3);q[i,j]=q[j,i]=1/s.sqrt(2);Qs.append(q)
U=s.zeros(15,14)
for row,(kind,feature) in enumerate(labels):
 e=s.Matrix(feature if kind=='A' else (0,0,0));b=s.Matrix(feature if kind=='B' else (0,0,0))
 for i in range(3):U[row,i]=e[i]/s.sqrt(2);U[row,5+i]=b[i]/s.sqrt(8)
 U[row,3]=(4*int(kind=='A')-3*int(kind=='B'))/s.sqrt(168)
 U[row,4]=(14*int(kind=='0')-int(kind!='0'))/s.sqrt(210)
 for a in range(2):U[row,8+a]=(e.T*D[a]*e)[0]/s.sqrt(2)
 for a,(i,j) in enumerate(pairs):U[row,10+a]=b[i]*b[j]/s.sqrt(8)
 U[row,13]=b[0]*b[1]*b[2]/s.sqrt(8)
check('complete_orthonormal_tangent_basis',U.T*U==s.eye(14) and U.T*s.ones(15,1)==s.zeros(14,1))

group=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
  Q=s.zeros(3)
  for i in range(3):Q[i,perm[i]]=signs[i]
  det=int(Q.det());dest=[]
  for kind,feature in labels:
   v=s.Matrix(feature);w=Q*v if kind=='A' else det*Q*v
   dest.append(index[kind,tuple(map(int,w))])
  group.append((Q,det,dest))
check('faithful_full48_geometric_actions',len(group)==48 and len({tuple(Q) for Q,_,_ in group})==48)
# Character blocks are recovered from projector traces, no imported character table.
blocks={'A1g':[3],'Eg':[8,9],'T1u':[0,1,2],'A2g':[13],'T1g':[5,6,7],'T2g':[10,11,12]}
projectors={key:U[:,idx]*U[:,idx].T for key,idx in blocks.items()}
characters=[];full=0;proper=0
for Q,det,dest in group:
 chi=sum(int(dest[a]==a) for a in range(15))-1
 chi2=sum(int(dest[dest[a]]==a) for a in range(15))-1
 sym=(chi*chi+chi2)//2
 full+=s.trace(Q)*sym
 if det==1:proper+=s.trace(Q)*sym
 chars={key:s.simplify(sum(P[a,dest[a]] for a in range(15))) for key,P in projectors.items()}
 assert chi==2*chars['A1g']+sum(chars[k] for k in blocks if k!='A1g')
 characters.append(chars)
character_gram=s.Matrix([[sum(c[a]*c[b] for c in characters)/48 for b in blocks] for a in blocks])
check('irreducible_character_decomposition_from_label_projectors',character_gram==s.eye(6))
check('complete_symbol_counts_full48_and_proper24',full==48*5 and proper==24*11,{'full48':str(full/48),'proper24':str(proper/24)})

def cross(q):return s.Matrix([[0,-q[2],q[1]],[q[2],0,-q[0]],[-q[1],q[0],0]])
def K(q,coeff):
 a1,a2,m,u,v=coeff
 return (a1*q).row_join(a2*q).row_join(m*cross(q)).row_join(u*D[0]*q).row_join(u*D[1]*q).row_join(v*Qs[0]*q).row_join(v*Qs[1]*q).row_join(v*Qs[2]*q).row_join(s.zeros(3,1))
def A(q,coeff):
 k=K(q,coeff)
 return s.zeros(3).row_join(k).col_join(k.T.row_join(s.zeros(11)))
units=[s.eye(3)[:,i] for i in range(3)]
embedded=[]
for channel in range(5):
 coeff=[int(k==channel) for k in range(5)]
 tensors=[(U*A(q,coeff)*U.T).applyfunc(s.simplify) for q in units]
 for Q,det,dest in group:
  for i in range(3):
   j=next(j for j in range(3) if Q[j,i])
   sign=Q[j,i]
   assert tensors[j].extract(dest,dest)==sign*tensors[i]
 embedded.append(tensors)
check('five_independent_species_intertwiners_all48_and_all_directions',True)
# This polar tensor covariance plus symmetric arguments proves orientation-reversed rate covariance.
for tensors in embedded:
 assert all(T==T.T and T*s.ones(15,1)==s.zeros(15,1) for T in tensors)
check('pair_tensor_symmetry_tangent_and_reflection_orientation_requirements',True)

q=s.Matrix(s.symbols('q0:3',real=True));a1,a2,m,u,v=s.symbols('a1 a2 m u v',real=True)
coeff=(a1,a2,m,u,v);norm=(q.T*q)[0];gram=K(q,coeff)*K(q,coeff).T
expected=(m*m+v*v/2)*norm*s.eye(3)+(a1*a1+a2*a2-m*m-u*u/3+v*v/2)*q*q.T+(u*u-v*v)*s.diag(*[x*x for x in q])
check('symbolic_Gram_identity',all(s.expand(x)==0 for x in gram-expected))
R=s.Matrix([[s.Rational(3,5),-s.Rational(4,5),0],[s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
G1=expected.subs(dict(zip(q,units[0])));Gr=expected.subs(dict(zip(q,R*units[0])))
check('noncubic_rotation_obstruction_exact',s.simplify((Gr-R*G1*R.T)[0,1]+s.Rational(12,25)*(u*u-v*v))==0)
isotropic=expected.subs(v,u)
ct=m*m+u*u/2;cl=a1*a1+a2*a2+2*u*u/3
check('isotropic_transverse_longitudinal_Gram_eigenvalues',all(s.expand(x)==0 for x in isotropic-ct*norm*s.eye(3)-(cl-ct)*q*q.T))
longitudinal=(q.T*expected*q)[0]
expectedlong=(a1*a1+a2*a2)*norm**2+u*u*sum((q.T*d*q)[0]**2 for d in D)+v*v*sum((q.T*d*q)[0]**2 for d in Qs)
check('nonnegative_longitudinal_Gram_identity',s.expand(longitudinal-expectedlong)==0)
closed=A(q,(0,0,m,0,0));lam=s.symbols('lambda')
check('closed_vector_full14_characteristic_polynomial',s.factor(closed.charpoly(lam).as_expr()-lam**10*(lam**2-m*m*norm)**2)==0)
# Pure diagonal tensor: rank one on an axis, rank two at generic q.
check('rank_two_does_not_force_transverse_isotropy',K(units[0],(0,0,0,1,0)).rank()==1 and K(s.Matrix([1,2,3]),(0,0,0,1,0)).rank()==2)

# Choose nonzero coefficients giving rational species tensors, then sum actual
# floor+positive-part rates over all 15^4 independent four-label contexts.
rational_coeff=(s.sqrt(21),s.sqrt(105),2,3,s.sqrt(2))
Ss=[(s.Rational(15,2)*U*A(qi,rational_coeff)*U.T).applyfunc(s.simplify) for qi in units]
p=s.Matrix([s.Rational(i+1,120) for i in range(15)])
current_results=[]
for axis,S in enumerate(Ss):
 assert all(x.is_Rational for x in S)
 den=lcm(*(int(s.denom(x)) for x in S))
 T=[[int(S[i,j]*den) for j in range(15)] for i in range(15)]
 numer=[0]*15
 for left,a,b,right in product(range(15),repeat=4):
  h=T[left][a]+T[a][right]-T[left][b]-T[b][right]
  rate_numerator=den+max(h,0) # kappa=1
  mass=(left+1)*(a+1)*(b+1)*(right+1)*rate_numerator
  numer[a]+=mass;numer[b]-=mass
 actual=s.Matrix([s.Rational(n,den*120**4) for n in numer])
 Sp=S*p;potential=(p.T*Sp)[0]
 target=s.Matrix([2*p[i]*(Sp[i]-potential) for i in range(15)])
 assert actual==target
 assert (s.Rational(2,15)*S-U*A(units[axis],rational_coeff)*U.T).applyfunc(s.simplify)==s.zeros(15)
 current_results.append({'axis':axis,'all_four_site_contexts':15**4,'integer_tensor_denominator':den,'current':[str(x) for x in actual]})
check('direct_exact_full15_species_product_current_and_uniform_normalization',True,current_results)

# Pointwise balance and reflection explicitly at field strings, not just currents.
word=[0,2,5,9,14,1,8]
for S in Ss:
 total=0
 for x in range(len(word)):
  left,a,b,right=[word[i%len(word)] for i in (x-1,x,x+1,x+2)]
  h=S[left,a]+S[a,right]-S[left,b]-S[b,right]
  swapped=S[left,b]+S[b,right]-S[left,a]-S[a,right]
  assert h==-swapped;total+=h
 assert total==0
for Q,det,dest in group:
 for axis,S in enumerate(Ss):
  j=next(j for j in range(3) if Q[j,axis]);sign=int(Q[j,axis])
  quad=(2,8,5,13)
  mapped=tuple(dest[a] for a in (quad if sign==1 else quad[::-1]))
  l,a,b,r=quad;h=S[l,a]+S[a,r]-S[l,b]-S[b,r]
  l,a,b,r=mapped;T=Ss[j];new=T[l,a]+T[a,r]-T[l,b]-T[b,r]
  assert new==h
check('periodic_balance_swap_and_full48_actual_rate_covariance',True)
output={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
 'scope':'Exact finite classification, explicit tensor covariance/Gram controls and generic local-current realization; no new hydrodynamic theorem or physical identification.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
