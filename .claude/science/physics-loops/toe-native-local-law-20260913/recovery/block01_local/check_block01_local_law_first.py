"""Literal M2/nearest-neighbor relay checks, with generic probability parameters.
The symbolic p parameters carry the explicitly proved interval [1/5,4/5].
Rational endpoint fixtures separately execute the interval recognizers.
"""
from itertools import permutations,product
from pathlib import Path
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent
I=s.ImmutableMatrix(s.eye(2));Z=s.diag(1,-1);Y=s.Matrix([[0,-s.I],[s.I,0]])
pp,pm=s.symbols('p_plus p_minus',real=True)
E=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mat(a):return s.ImmutableMatrix(a.applyfunc(s.expand))
def same(a,b):return all(s.simplify(x)==0 for x in a-b)
def in_range(q,low,high,closed=True):
 if q in (pp,pm):return low<=s.Rational(1,5) and s.Rational(4,5)<=high
 if q.is_real is not True:return False
 return bool(q>=low) and bool(q<=high if closed else q<high)
def basis(a):
 lam=s.simplify((s.trace(a)-1)/2);P=mat(a-lam*I)
 if in_range(lam,20,21,False) and s.trace(P)==1 and same(P*P,P):return lam,P
 return None
def controller(a,tag):
 q=s.simplify(s.trace(a)/2-tag)
 return q if same(a,(tag+q)*I) and in_range(q,0,1) else None
def total(law):
 out=[]
 for a,p in law:
  p=s.simplify(p)
  if p==0:continue
  for j,(b,q) in enumerate(out):
   if same(a,b):out[j]=(b,s.simplify(q+p));break
  else:out.append((mat(a),p))
 return out
def F(neighbors):
 bs=[basis(a) for a in neighbors];bs=[b for b in bs if b is not None]
 if any(same(a,10*I) for a in neighbors) and len(bs)==1:
  _,P=bs[0]
  cps=[controller(a,100) for a in neighbors];cps=[p for p in cps if p is not None]
  cms=[controller(a,200) for a in neighbors];cms=[p for p in cms if p is not None]
  signs=[1 if same(a,P) else -1 for a in neighbors if same(a,P) or same(a,I-P)]
  p=(cps[0] if signs[0]==1 else cms[0]) if len(cps)==len(cms)==len(signs)==1 else s.Rational(1,2)
  return total([(P,p),(I-P,1-p)])
 if neighbors:return total([(a,s.Rational(1,len(neighbors))) for a in neighbors])
 return [(0*I,s.Integer(1))]
def neighbor_slots(R,x):
 return [R.get(add(x,mul(z,e))) for e in E for z in (-1,1)]
def neighbors(R,x):return [a for a in neighbor_slots(R,x) if a is not None]
def weight(law,a):return s.simplify(sum((p for b,p in law if same(a,b)),s.Integer(0)))
def positive(p):
 if not p.free_symbols:return bool(p>0)
 vals=[p.subs({pp:a,pm:b}) for a,b in product([s.Rational(1,5),s.Rational(4,5)],repeat=2)]
 # All symbolic weights used here are multiaffine over this rectangle.
 assert s.Poly(p,pp,pm).degree(pp)<=1 and s.Poly(p,pp,pm).degree(pm)<=1
 return all(v>0 for v in vals)
def fixture(P= s.diag(1,0),pplus=pp,pminus=pm,u=s.Rational(1,40)):
 P=mat(P);D=mat((20+u/(1+u))*I+P);T=10*I
 x1=(1,0,0);relay=(2,0,0);x2=(3,0,0);R={}
 def put(x,a):
  assert x not in R
  R[x]=mat(a)
 for x in (x1,x2):
  for k in (1,2):
   put(add(x,mul(-k,E[2])),D);put(add(x,mul(k,E[2])),T)
 put(add(x2,E[1]),(100+pplus)*I)
 put(add(add(x2,E[1]),E[2]),(100+pplus)*I)
 put(add(x2,mul(-1,E[1])),(200+pminus)*I)
 put(add(add(x2,mul(-1,E[1])),mul(-1,E[2])),(200+pminus)*I)
 return R,(x1,relay,x2),P
def decode(R):
 cp=[x for x,a in R.items() if controller(a,100) is not None]
 cm=[x for x,a in R.items() if controller(a,200) is not None]
 pairs=[(dist(a,b),a,b) for a in cp for b in cm]
 least=min(pairs)[0];matches=[(a,b) for d,a,b in pairs if d==least]
 assert len(matches)==1 and least==2
 a,b=matches[0];x2=tuple((v+w)//2 for v,w in zip(a,b))
 ey=tuple((v-w)//2 for v,w in zip(a,b))
 other=next(x for x in cp if x!=a);ez=tuple(v-w for v,w in zip(other,a));ex=cross(ey,ez)
 assert sum(v*v for v in ey)==sum(v*v for v in ez)==sum(v*v for v in ex)==1
 x1=add(x2,mul(-2,ex));relay=add(x2,mul(-1,ex))
 lam,P=basis(R[add(x2,mul(-1,ez))])
 v=lam-20;u=s.simplify(v/(1-v))
 stage=sum(x in R for x in (x1,relay,x2))
 assert all(x in R for x in (x1,relay,x2)[:stage])
 return (x1,relay,x2),P,u,stage
def rotations():
 out=[]
 for perm in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
   M=s.zeros(3)
   for j in range(3):M[perm[j],j]=signs[j]
   if M.det()==1:out.append(M)
 return out
def run():
 start=time.monotonic();checks=[];support_visits=0;prefixes=[]
 def check(name,ok):
  assert bool(ok),name
  checks.append(name)
 def eq(name,a,b):check(name,s.simplify(a-b)==0)
 def law_equal(a,b):
  return all(weight(a,x)==weight(b,x) for x,_ in a+b)
 def supported(R):
  nonlocal support_visits
  for x,a in R.items():
   law=F(neighbors(R,x))
   assert s.simplify(sum(p for _,p in law)-1)==0,('law_norm',x)
   assert positive(weight(law,a)),('Record_support',x,str(a))
   support_visits+=1
 R,sites,P=fixture();x1,relay,x2=sites
 check('twelve_prepared_Records',len(R)==12)
 coarse={0:(0,0,0),1:(1,0,0),2:(2,0,0),3:(0,1,0),4:(1,1,0),5:(2,1,0)}
 edges=[(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(4,5)]
 native={tuple(a+b for a,b in zip(coarse[v],coarse[w])) for v,w in edges}
 check('metadata_avoids_native_and_relay',not(set(R)&native) and relay not in R)
 check('twenty_total_sites',len(set(R)|native|{relay})==20)
 check('native_midpoints_independent',all(dist(a,b)!=1 for a,b in product(native,native)))
 check('relay_is_physical_NN',dist(x1,relay)==dist(relay,x2)==1)
 check('first_complete_neighbor_count',len(neighbors(R,x1))==2)
 check('second_initial_complete_neighbor_count',len(neighbors(R,x2))==4)
 check('relay_initially_has_no_Record_neighbors',neighbors(R,relay)==[])
 check('initial_law_frame_decoder',decode(R)[0]==sites and decode(R)[2]==s.Rational(1,40))
 supported(R);prefixes.append((R,s.Integer(1)))
 final=[];first=[]
 for z in (1,-1):
  A=P if z==1 else I-P
  p1=weight(F(neighbors(R,x1)),A);eq('first_fair_'+str(z),p1,s.Rational(1,2))
  R1=dict(R);R1[x1]=mat(A);first.append(R1);supported(R1);prefixes.append((R1,p1))
  check('first_stage_decoded_'+str(z),decode(R1)[3]==1)
  check('relay_single_actual_neighbor_'+str(z),len(neighbors(R1,relay))==1)
  eq('relay_copies_actual_projector_'+str(z),weight(F(neighbors(R1,relay)),A),1)
  R2=dict(R1);R2[relay]=mat(A);supported(R2);prefixes.append((R2,p1))
  check('second_full_five_neighbor_condition_'+str(z),len(neighbors(R2,x2))==5)
  check('relay_stage_decoded_'+str(z),decode(R2)[3]==2)
  for w in (1,-1):
   out=P if w==1 else I-P;p=pp if z==1 else pm
   p2=weight(F(neighbors(R2,x2)),out)
   eq('native_symbolic_second_law_'+str((z,w)),p2,p if w==1 else 1-p)
   R3=dict(R2);R3[x2]=mat(out);supported(R3)
   check('fifteen_final_Records_'+str((z,w)),len(R3)==15)
   check('completed_stage_decoded_'+str((z,w)),decode(R3)[3]==3)
   check('relay_retained_after_second_'+str((z,w)),positive(weight(F(neighbors(R3,relay)),A)))
   final.append((R3,p1*p2));prefixes.append((R3,p1*p2))
 eq('complete_native_history_normalization',sum(p for _,p in final),1)
 n1=neighbor_slots(first[0],x2);n2=neighbor_slots(first[1],x2)
 check('unrelayed_conditions_identical',all((a is None and b is None) or(a is not None and b is not None and same(a,b)) for a,b in zip(n1,n2)))
 eq('unrelayed_kernel_cannot_select_first_sign',weight(F(neighbors(first[0],x2)),P),s.Rational(1,2))
 # The matrix kernel is checked with non-Hermitian idempotents as an algebraic
 # covariance extension, not as an additional physical quantum-data claim.
 for k,G in enumerate([s.Matrix([[1,1],[0,1]]),s.Matrix([[1,s.I],[s.I,1]])/s.sqrt(2)]):
  for Rj,_ in prefixes:
   transformed={x:mat(G*a*G.inv()) for x,a in Rj.items()}
   for x in sites:
    original=[(mat(G*a*G.inv()),p) for a,p in F(neighbors(Rj,x))]
    assert law_equal(F(neighbors(transformed,x)),original),(k,x)
  check('actual_matrix_similarity_kernel_'+str(k),True)
 shift=s.Matrix([7,-11,5])
 for k,M in enumerate(rotations()):
  transform=lambda x:tuple(int(t) for t in M*s.Matrix(x)+shift)
  for Rj,_ in prefixes:
   Rt={transform(x):a for x,a in Rj.items()}
   ds,DP,du,stage=decode(Rt)
   assert ds==tuple(transform(x) for x in sites)
   assert same(DP,P) and du==s.Rational(1,40)
   for x in sites:assert law_equal(F(neighbors(Rt,transform(x))),F(neighbors(Rj,x)))
   supported(Rt)
  check('complete_rotated_prefixes_'+str(k),True)
 # Exact controller endpoints and malformed multiplicities test normalization.
 for a,b in product([s.Integer(0),s.Rational(1,5),s.Rational(1,2),s.Rational(4,5),s.Integer(1)],repeat=2):
  Q,ss,PP=fixture(pplus=a,pminus=b,u=0)
  for z in (1,-1):
   V=dict(Q);V[ss[0]]=PP if z==1 else I-PP;V[ss[1]]=V[ss[0]]
   eq('rational_controller_'+str((a,b,z)),weight(F(neighbors(V,ss[2])),PP),a if z==1 else b)
   supported(V)
   for out,prob in F(neighbors(V,ss[2])):
    W=dict(V);W[ss[2]]=out;supported(W)
 check('empty_rule',same(F([])[0][0],0*I) and F([])[0][1]==1)
 D=R[add(x1,mul(-1,E[2]))]
 eq('duplicate_basis_uses_empirical_fallback',weight(F([10*I,D,D]),D),s.Rational(2,3))
 eq('duplicate_data_uses_declared_fair_fallback',weight(F([10*I,D,(100+pp)*I,(200+pm)*I,P,P]),P),s.Rational(1,2))
 # A unique-neighbor-only copy rule would erase the relay's support after the
 # second data appears. Keep this failed alternative explicit.
 mixed=next(Rj for Rj,_ in final if not same(Rj[x1],Rj[x2]))
 nn=neighbors(mixed,relay)
 check('opposite_data_neighbors_both_present',len(nn)==2 and not same(nn[0],nn[1]))
 check('unique_neighbor_only_copy_would_fail',weight([(0*I,s.Integer(1))],mixed[relay])==0)
 return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,'seconds':time.monotonic()-start,'complete_prefix_states':len(prefixes),'Record_support_visits':support_visits,'symbolic_parameter_domain':'p_plus,p_minus in [1/5,4/5], supplied by the native effect proof; recognizer interval membership on these symbols is a declared test premise','native_nonzero_dwell_probabilities':'represented symbolically here; separately enclosed in BLOCK01_NATIVE_CHECKS.json','runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(HERE/'BLOCK01_LOCAL_LAW_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
