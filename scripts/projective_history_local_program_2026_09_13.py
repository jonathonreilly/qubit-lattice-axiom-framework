"""Exact finite programmed Record histories on literal physical Z3.

The fixed local kernel is evaluated on actual complete neighbor multisets.
The transition selector reconstructs its current prefix from Records alone.
Supplied quantum probability banks are compared with separate pure-ensemble
amplitude cylinders, not interpreted as a physical probability derivation.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product, permutations
from pathlib import Path
import hashlib,json,time
import sympy as sp

AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/PROJECTIVE_HISTORY_FIXED_FIRST_TARGET_LOCAL_PROGRAM_BOUNDED_THEOREM_NOTE_2026-09-13.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md',
 '.claude/science/physics-loops/projective-history-local-program-20260913/SOURCE_MANIFEST.json',
 '.claude/science/physics-loops/projective-history-local-program-20260913/NO_GO_DISCIPLINE_CHECKLIST.md',
 '.claude/science/physics-loops/projective-history-local-program-20260913/mutations/RESULTS.json',
)
I=sp.ImmutableMatrix(sp.eye(2));ZERO=sp.ImmutableMatrix(sp.zeros(2))
X=sp.ImmutableMatrix([[0,1],[1,0]])
Y=sp.ImmutableMatrix([[0,-sp.I],[sp.I,0]])
Z=sp.ImmutableMatrix([[1,0],[0,-1]])
T=10*I
AXES=((1,0,0),(0,1,0),(0,0,1))
OFFSETS=tuple(tuple(s*v for v in e) for e,s in product(AXES,(1,-1)))
FRAME=(-10,-10,-10)


def scalar(v):return sp.simplify(sp.radsimp(v))
def clean(m):return sp.ImmutableMatrix(m.applyfunc(sp.expand))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def times(n,x):return tuple(n*a for a in x)
def center(j):return (20*2**j,0,0)
def bank_index(h):return 1+sum(b*2**(len(h)-k-1) for k,b in enumerate(h))
def bank(j,l):return add(center(j),(-3*l,3,0))
def proj(a,bit):return clean((I+(-1)**bit*a)/2)
def encode(p,P):return clean((2+p)*I+P)


@lru_cache(None)
def decode(value):
 p=scalar((sp.trace(value)-5)/2)
 if p.is_real is not True or not (p>=0 and p<=1):return None
 P=clean(value-(2+p)*I)
 return (p,P) if all(scalar(v)==0 for v in P*P-P) and sp.trace(P)==1 else None


def neighbors(site,records):return [add(site,d) for d in OFFSETS if add(site,d) in records]


def measure(site,records):
 contents=[records[q] for q in neighbors(site,records)]
 programs=[decode(value) for value in contents if decode(value) is not None]
 if T in contents and len(programs)==1:
  p,P=programs[0]
  return {value:weight for value,weight in ((P,p),(clean(I-P),1-p)) if weight!=0}
 if not contents:return {ZERO:sp.Integer(1)}
 result={}
 for value in contents:result[value]=result.get(value,0)+sp.Rational(1,len(contents))
 return result


def program_path(j,l):
 c=center(j)
 return [add(c,(-3*l,y,0)) for y in (2,1,0)]+[add(c,(x,0,0)) for x in range(-3*l+1,0)]


def preparation(programs,N):
 records={}
 for j in range(1,N+1):
  for l in range(1,2**(j-1)+1):
   p,P=programs[j,l];value=encode(p,P)
   records[bank(j,l)]=value;records[add(bank(j,l),(0,0,1))]=value
  records[add(center(j),(1,0,0))]=T;records[add(center(j),(2,0,0))]=T
 for tag,places in (
  (20,(FRAME,add(FRAME,(-1,0,0)))),
  (21,(add(FRAME,(1,0,0)),add(FRAME,(2,0,0)))),
  (22,(add(FRAME,(0,2,0)),add(FRAME,(1,2,0)))),
  (23,(add(FRAME,(0,0,3)),add(FRAME,(1,0,3))))):
  for site in places:records[site]=tag*I
 return records


def rotations():
 out=[]
 for p in permutations(range(3)):
  parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
  for signs in product((1,-1),repeat=3):
   if parity*signs[0]*signs[1]*signs[2]==1:
    out.append(tuple(tuple(signs[j]*x for x in AXES[p[j]]) for j in range(3)))
 return out


def rotate(r,x):return tuple(sum(r[j][i]*x[j] for j in range(3)) for i in range(3))


def canonicalize(records):
 tagged={tag:[site for site,value in records.items() if value==tag*I] for tag in (20,21,22,23)}
 roots=[site for site in tagged[20] if any(sum(abs(x) for x in sub(site,t))==1 for t in tagged[21])]
 assert len(roots)==1,'unique_frame_root'
 root=roots[0]
 e1=sub(next(t for t in tagged[21] if sum(abs(x) for x in sub(t,root))==1),root)
 t2=min(tagged[22],key=lambda t:sum(abs(x) for x in sub(t,root)))
 t3=min(tagged[23],key=lambda t:sum(abs(x) for x in sub(t,root)))
 d2,d3=sub(t2,root),sub(t3,root)
 assert all(x%2==0 for x in d2) and all(x%3==0 for x in d3),'integral_frame_axes'
 e2,e3=tuple(x//2 for x in d2),tuple(x//3 for x in d3)
 axes=(e1,e2,e3)
 assert sp.Matrix.hstack(*(sp.Matrix(e) for e in axes)).det()==1,'proper_frame'
 def canonical(site):return add(FRAME,tuple(sum(a*b for a,b in zip(sub(site,root),e)) for e in axes))
 def world(site):return add(root,rotate(axes,sub(site,FRAME)))
 return {canonical(site):value for site,value in records.items()},world


def current_prefix(canonical):
 N=sum(value==T for value in canonical.values())//2
 h=[]
 for j in range(1,N+1):
  if center(j) not in canonical:break
  p,P=decode(canonical[bank(j,bank_index(h))])
  value=canonical[center(j)]
  assert value in (P,clean(I-P)),'data_matches_its_prepared_program'
  h.append(0 if value==P else 1)
 return N,tuple(h)


def next_transition(records):
 canonical,world=canonicalize(records)
 N,h=current_prefix(canonical)
 if len(h)==N:return None
 j=len(h)+1;l=bank_index(h)
 for site in program_path(j,l)+[center(j)]:
  if site not in canonical:
   target=world(site)
   return target,measure(target,records)
 raise AssertionError('missing_next_event')


def tree_weights(programs,N):
 result={():sp.Integer(1)}
 for j in range(1,N+1):
  for h in product((0,1),repeat=j-1):
   p,_=programs[j,bank_index(h)]
   for bit in (0,1):result[h+(bit,)]=scalar(result[h]*(p if bit==0 else 1-p))
 return {h:w for h,w in result.items() if len(h)==N}


def run():
 start=time.monotonic();checks=[];stats={'program_appends':0,'data_appends':0,'affected_support_conditions':0,'zero_branches':0,'decoded_prefixes':0}
 def checked(name,condition,**data):
  assert bool(condition),name
  checks.append({'name':name,**data})
 def equal(name,a,b):
  if isinstance(a,sp.MatrixBase):condition=all(scalar(v)==0 for v in a-b)
  else:condition=scalar(a-b)==0
  checked(name,condition)
 def supported(site,records):return records[site] in measure(site,records)
 def append(records,site,value):
  assert site not in records,'single_Record_per_site'
  records[site]=value
  affected=[site]+neighbors(site,records)
  for q in affected:
   assert supported(q,records),'continued_local_support'
   stats['affected_support_conditions']+=1
 def simulate(name,programs,N,expected=None):
  ready=preparation(programs,N)
  checked(name+'_prepared_count',len(ready)==2*(2**N-1)+2*N+8)
  checked(name+'_all_initial_support',all(supported(site,ready) for site in ready))
  checked(name+'_initial_frame',canonicalize(ready)[0]==ready)
  result={};final_example=None
  for bits in product((0,1),repeat=N):
   records=dict(ready);mass=sp.Integer(1)
   for j in range(1,N+1):
    h=bits[:j-1];l=bank_index(h);value=ready[bank(j,l)]
    for site in program_path(j,l):
     target,mu=next_transition(records)
     assert target==site and mu=={value:1},'actual_single_predecessor_copy_measure'
     append(records,target,value);stats['program_appends']+=1
    target,mu=next_transition(records)
    assert target==center(j),'fixed_first_data_target'
    assert set(neighbors(target,records))=={add(target,(-1,0,0)),add(target,(1,0,0))},'complete_data_neighbors'
    p,P=decode(value);outcome=P if bits[j-1]==0 else clean(I-P)
    probability=mu.get(outcome,sp.Integer(0))
    assert scalar(probability-(p if bits[j-1]==0 else 1-p))==0,'local_program_probability'
    mass=scalar(mass*probability)
    if mass==0:
     stats['zero_branches']+=1
     break
    append(records,target,outcome);stats['data_appends']+=1
    _,recovered=current_prefix(canonicalize(records)[0])
    assert recovered==bits[:j],'Record_only_prefix_reconstruction'
    stats['decoded_prefixes']+=1
   result[bits]=mass
   if mass:
    assert next_transition(records) is None,'finite_horizon_absorption'
    assert all(supported(site,records) for site in records),'all_final_Record_support'
    actual_new=len(records)-len(ready)
    exact_new=sum(3*bank_index(bits[:j-1])+3 for j in range(1,N+1))
    assert actual_new==exact_new<=3*(2**N-1)+3*N,'exact_new_Record_count'
    final_example=records
   if expected is not None:assert scalar(mass-expected(bits))==0,'independent_cylinder_weight'
  equal(name+'_normalization',sum(result.values()),1)
  checked(name+'_tree_vs_physical_cylinders',result==tree_weights(programs,N))
  return ready,final_example,result

 checked('empty_law',measure((0,0,0),{})=={ZERO:1})
 repeated={(1,0,0):Z,(0,1,0):Z,(0,0,1):X}
 checked('empirical_multiplicity',measure((0,0,0),repeated)=={Z:sp.Rational(2,3),X:sp.Rational(1,3)})
 for p in (0,sp.Rational(1,5),sp.Rational(1,2),1):
  P=proj(Y,0);value=encode(p,P)
  checked('program_decode_'+str(p),decode(value)==(p,P))
  mu=measure((0,0,0),{(-1,0,0):value,(1,0,0):T})
  checked('program_local_law_'+str(p),mu=={q:w for q,w in ((P,p),(clean(I-P),1-p)) if w!=0})
 checked('radical_program_idempotence_normalized',decode(encode(sp.Rational(1,2),proj((Z-X)/sp.sqrt(2),0))) is not None)
 checked('malformed_program_is_not_accepted',decode(3*I) is None and decode(T) is None and decode(X) is None)
 double_program={(-1,0,0):encode(sp.Rational(1,3),proj(Z,0)),(0,1,0):encode(sp.Rational(1,3),proj(Z,0)),(1,0,0):T}
 checked('program_occurrences_not_deduplicated',measure((0,0,0),double_program)=={encode(sp.Rational(1,3),proj(Z,0)):sp.Rational(2,3),T:sp.Rational(1,3)})
 g=sp.Matrix([[1,sp.I],[0,2]])
 original={(-1,0,0):encode(sp.Rational(2,7),proj(Y,0)),(1,0,0):T}
 transformed={site:clean(g*value*g.inv()) for site,value in original.items()}
 checked('nonunitary_similarity_covariance',measure((0,0,0),transformed)=={clean(g*value*g.inv()):weight for value,weight in measure((0,0,0),original).items()})
 checked('complex_conjugation_covariance',measure((0,0,0),{site:clean(value.conjugate()) for site,value in original.items()})=={clean(value.conjugate()):weight for value,weight in measure((0,0,0),original).items()})
 exact=encode(sp.Rational(1,2),proj(Z,0))
 off_code=clean(exact+sp.diag(sp.Rational(1,100),-sp.Rational(1,100)))
 original_mu=measure((0,0,0),{(-1,0,0):exact,(1,0,0):T})
 perturbed_mu=measure((0,0,0),{(-1,0,0):off_code,(1,0,0):T})
 checked('explicit_off_code_matrix_comparison',decode(off_code) is None and
         set(original_mu).isdisjoint(perturbed_mu) and perturbed_mu=={off_code:sp.Rational(1,2),T:sp.Rational(1,2)})

 # A generic adaptive five-event tree, including deterministic branches.
 N=5
 generic={(j,l):(sp.Rational((3*l+j)%7,6),proj((Z,X,Y)[(j+l)%3],0)) for j in range(1,N+1) for l in range(1,2**(j-1)+1)}
 ready,last,weights=simulate('adaptive_five_event',generic,N)
 smaller=preparation({key:value for key,value in generic.items() if key[0]<N},N-1)
 checked('nested_preparation',set(smaller.items())<=set(ready.items()))
 small_weights=tree_weights(generic,N-1)
 checked('prefix_cylinder_consistency',all(scalar(weights[h+(0,)]+weights[h+(1,)]-w)==0 for h,w in small_weights.items()))
 maxerror=sp.Rational(0)
 rounded={}
 for key,(p,P) in generic.items():
  q=sp.Rational(round(4*p),4);rounded[key]=(q,P);maxerror=max(maxerror,abs(p-q))
 approx=tree_weights(rounded,N)
 tv=scalar(sum(abs(w-approx[h]) for h,w in weights.items())/2)
 checked('finite_probability_precision_data_bound',tv<=1-(1-maxerror)**N<=N*maxerror,
         exact_total_variation=str(tv),uniform_probability_error=str(maxerror))

 # Rigid-frame recovery and the same actual next event under all24 cubic rotations.
 offset=(7,-4,9)
 for idx,r in enumerate(rotations()):
  moved={add(rotate(r,site),offset):value for site,value in ready.items()}
  canonical,_=canonicalize(moved)
  target,mu=next_transition(moved)
  base_target,base_mu=next_transition(ready)
  checked('rotation_frame_and_transition_'+str(idx),canonical==ready and target==add(rotate(r,base_target),offset) and mu==base_mu)

 # Two independently drawn setting Records precede the two quantum data events.
 singlet=sp.Matrix([0,1,-1,0])/sp.sqrt(2)
 plus=sp.Matrix([1,1])/sp.sqrt(2);iplus=sp.Matrix([1,sp.I])/sp.sqrt(2)
 product_state=sp.kronecker_product(plus,iplus)
 scenarios=[('singlet',[(sp.Integer(1),singlet)]),
            ('mixed',[(sp.Rational(3,4),singlet)]+[(sp.Rational(1,16),sp.eye(4)[:,k]) for k in range(4)]),
            ('product',[(sp.Integer(1),product_state)])]
 observables=((Z,X),((Z+X)/sp.sqrt(2),(Z-X)/sp.sqrt(2)))
 for name,ensemble in scenarios:
  rho=clean(sum((w*v*v.H for w,v in ensemble),sp.zeros(4)))
  tables=[]
  for reverse in (False,True):
   order=(1,0) if reverse else (0,1)
   programs={}
   for j in range(1,5):
    for h in product((0,1),repeat=j-1):
     if j<=2:p,P=sp.Rational(1,2),proj(Z,0)
     else:
      wing=order[j-3];setting=h[wing]
      P=proj(observables[wing][setting],0)
      op=sp.kronecker_product(P,I) if wing==0 else sp.kronecker_product(I,P)
      sigma=rho
      if j==4:
       first=order[0];Pfirst=proj(observables[first][h[first]],h[2])
       first_op=sp.kronecker_product(Pfirst,I) if first==0 else sp.kronecker_product(I,Pfirst)
       sigma=clean(first_op*rho*first_op)
      denominator=scalar(sp.trace(sigma))
      p=scalar(sp.trace(op*sigma*op)/denominator) if denominator else sp.Rational(1,2)
     programs[j,bank_index(h)]=(p,clean(P))
   def independent(bits):
    a,b=bits[:2];outcomes={order[0]:bits[2],order[1]:bits[3]}
    pa,pb=proj(observables[0][a],outcomes[0]),proj(observables[1][b],outcomes[1])
    joint=sp.kronecker_product(pa,pb)
    return scalar(sum(w*((joint*v).H*(joint*v))[0] for w,v in ensemble)/4)
   _,_,physical=simulate(name+('_reverse' if reverse else '_forward'),programs,4,independent)
   table={}
   for bits,mass in physical.items():
    a,b=bits[:2];outcomes={order[0]:bits[2],order[1]:bits[3]}
    table[a,b,outcomes[0],outcomes[1]]=4*mass
   tables.append(table)
  checked(name+'_opposite_wing_order_same_logical_law',tables[0]==tables[1])
  table=tables[0]
  for a,b in product((0,1),repeat=2):
   equal(name+f'_conditional_setting_normalization_{a}_{b}',sum(table[a,b,s,t] for s,t in product((0,1),repeat=2)),1)
  checked(name+'_both_no_signaling_marginals',all(scalar(sum(table[a,0,s,t]-table[a,1,s,t] for t in (0,1)))==0 for a,s in product((0,1),repeat=2)) and
          all(scalar(sum(table[0,b,s,t]-table[1,b,s,t] for s in (0,1)))==0 for b,t in product((0,1),repeat=2)))
  corr={(a,b):scalar(sum((-1)**(s+t)*table[a,b,s,t] for s,t in product((0,1),repeat=2))) for a,b in product((0,1),repeat=2)}
  chsh=scalar(corr[0,0]+corr[0,1]+corr[1,0]-corr[1,1])
  if name=='singlet':equal('supplied_singlet_CHSH',chsh,-2*sp.sqrt(2))
  if name=='mixed':equal('supplied_mixed_CHSH',chsh,-3*sp.sqrt(2)/2)
  if name=='product':
   checked('product_state_factorization',all(scalar(table[a,b,s,t]-sum(table[a,b,s,u] for u in (0,1))*sum(table[a,b,v,t] for v in (0,1)))==0
           for a,b,s,t in product((0,1),repeat=4)))
 # A second trace fixture revisits both wings. The Y event is complex and
 # noncommutes with the earlier A-Z event; the last B-Z is a deterministic
 # repeat. Its zeros would be lost if the earlier state update were omitted.
 history_ensemble=[(sp.Rational(3,4),singlet)]+[(sp.Rational(1,16),sp.eye(4)[:,k]) for k in range(4)]
 history_rho=clean(sum((w*v*v.H for w,v in history_ensemble),sp.zeros(4)))
 events=((0,Z),(1,Z),(0,Y),(1,Z))
 def event_op(j,bit):
  wing,obs=events[j];P=proj(obs,bit)
  return sp.kronecker_product(P,I) if wing==0 else sp.kronecker_product(I,P)
 programs={}
 for j in range(1,5):
  for h in product((0,1),repeat=j-1):
   sigma=history_rho
   for k,bit in enumerate(h):
    op=event_op(k,bit);sigma=clean(op*sigma*op)
   op=event_op(j-1,0);denominator=scalar(sp.trace(sigma))
   p=scalar(sp.trace(op*sigma*op)/denominator) if denominator else sp.Rational(1,2)
   programs[j,bank_index(h)]=(p,proj(events[j-1][1],0))
 def history_amplitudes(bits):
  value=0
  for w,v in history_ensemble:
   vector=v
   for j,bit in enumerate(bits):vector=event_op(j,bit)*vector
   value+=w*(vector.H*vector)[0]
  return scalar(value)
 _,_,history_weights=simulate('noncommuting_repeated_quantum_history',programs,4,history_amplitudes)
 checked('repeated_B_Record_zero_children',all(weight==0 for h,weight in history_weights.items() if h[1]!=h[3]))
 checked('noncommuting_complex_program_actually_present',any(P==proj(Y,0) for p,P in programs.values()))
 checked('zero_branches_exercised',stats['zero_branches']>0,**stats)
 return {'status':'pass','total_pass':len(checks),'total_fail':0,'checks':checks,'stats':stats,'seconds':time.monotonic()-start,
         'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
 import signal
 signal.alarm(AUDIT_TIMEOUT_SEC)
 result=run()
 print(json.dumps(result,indent=2))
 print('per_element: Exact matrix program decoding, malformed inputs and probability measures are checked.')
 print('per_site: Actual complete nearest-neighbor content laws and permanent Record support are checked.')
 print('per_mode: Two quantum wings with complex noncommuting programs and repeated-projector zeros are checked.')
 print('per_block: Full finite data cylinders match independent amplitude sums and Record-only transition reconstruction.')
 print('lattice_wide: checked and not executed — the all-finite-horizon result follows from the written geometry and induction; no infinite finite-resource apparatus or physical selector is claimed.')
 print(f"TOTAL: PASS={result['total_pass']} FAIL=0")
 signal.alarm(0)
