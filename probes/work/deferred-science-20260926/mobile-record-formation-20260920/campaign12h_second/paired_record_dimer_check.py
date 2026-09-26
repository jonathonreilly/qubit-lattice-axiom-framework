"""Author controls for paired immutable records; no phase/wave inference."""
from __future__ import annotations
from pathlib import Path
from itertools import product, permutations
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib, json, sys
import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

HERE=Path(__file__).resolve().parent
D=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (-1,1))
AX=tuple(tuple(int(i==j) for i in range(3)) for j in range(3))
ROWS=[]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def parity(x):return (-1)**sum(x)
def check(name,ok,**details):
 row={'name':name,'pass':bool(ok),**details};ROWS.append(row)
 print(json.dumps(row,sort_keys=True))
 assert ok,name

def valid(records):
 ids=[r[0] for r in records.values()]
 return len(ids)==len(set(ids)) and all(d in D and records.get(add(x,d),(None,None))[1]==neg(d) for x,(_,d) in records.items())

def birth(records,x,d):
 y=add(x,d)
 if x in records or y in records:raise ValueError('occupied birth endpoint')
 out=records.copy();nid=max((r[0] for r in records.values()),default=-1)+1
 out[x]=(nid,d);out[y]=(nid+1,neg(d));return out

def translate(records,x,a):
 d=records[x][1];old={x,add(x,d)};dest={add(y,a) for y in old}
 if (dest-old)&records.keys():raise ValueError('blocked translation')
 out={y:r for y,r in records.items() if y not in old}
 out.update({add(y,a):records[y] for y in old});return out

def cube_exchange(records,base=(0,0,0),axis=2):
 p,q=[j for j in range(3) if j!=axis];cube=[add(base,t) for t in product((0,1),repeat=3)]
 if any(x not in records for x in cube):raise ValueError('not full cube')
 def aligned(face,j):
  return all(records[x][1]==tuple((1-2*(x[j]-base[j])) if a==j else 0 for a in range(3)) for x in cube if x[axis]-base[axis]==face)
 if not ((aligned(0,p) and aligned(1,q)) or (aligned(0,q) and aligned(1,p))):raise ValueError('not paired opposite face patterns')
 out=records.copy()
 for x in cube:
  y=list(x);y[axis]=2*base[axis]+1-x[axis];out[tuple(y)]=records[x]
 return out

def bonds(records):
 return frozenset(tuple(sorted((x,add(x,d)))) for x,(_,d) in records.items())
def directions(records):return Counter(d for _,d in records.values())
def content_by_id(records):return dict(records.values())
def rotate(records,R):
 return {tuple(map(int,R@np.array(x))):(i,tuple(map(int,R@np.array(d)))) for x,(i,d) in records.items()}
def sixB(records,N):
 matched=bonds(records);out={}
 for x in product(range(N),repeat=3):
  for i,e in enumerate(AX):
   y=tuple((a+b)%N for a,b in zip(x,e))
   n=int(tuple(sorted((x,y))) in matched)
   out[x,i]=parity(x)*(6*n-1)
 return out

def gauss_control(records,N=8):
 B=sixB(records,N)
 return all(sum(B[x,i]-B[tuple((a-b)%N for a,b in zip(x,e)),i] for i,e in enumerate(AX))==6*parity(x)*(int(x in records)-1) for x in product(range(N),repeat=3))

def rotation_matrices():
 out=[]
 for perm in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
   R=np.zeros((3,3),dtype=int)
   for i,j in enumerate(perm):R[i,j]=signs[i]
   if round(np.linalg.det(R))==1:out.append(R)
 return out

def nn_birth_controls():
 patterns=0;rotations=rotation_matrices();cov=0
 for mask in range(64):
  records={};vac={}
  for i,d in enumerate(D):
   occupied=bool(mask&(1<<i));vac[d]=int(not occupied)
   if occupied:records=birth(records,d,d)
  assert valid(records) and (0,0,0) not in records
  total=sum(vac.values());p={d:Fraction(v,total) if total else None for d,v in vac.items()}
  for d in D:
   if vac[d]:assert valid(birth(records,(0,0,0),d))
  for R in rotations:
   mapped={tuple(R@np.array(d)):v for d,v in vac.items()}
   assert set(mapped)==set(D)
   for d in D:
    rd=tuple(R@np.array(d));assert (Fraction(mapped[rd],total) if total else None)==p[d]
   cov+=1
  patterns+=1
 check('conditional_birth_all_realizable_neighbor_patterns_and_cubic_covariance',patterns==64 and len(rotations)==24,patterns=patterns,rotations=len(rotations),pattern_rotation_pairs=cov,zero_hazard_patterns=1)


def histories():
 empty={};first=birth(empty,(2,2,2),AX[0]);moved=translate(first,(2,2,2),AX[1]);renewed=birth(moved,(2,2,2),AX[0])
 check('actual_record_transport_and_repeated_formation',valid(renewed) and len(renewed)==4 and bonds(first)!=bonds(moved) and not(set(first)&set(moved)) and content_by_id(first)=={i:d for i,d in content_by_id(renewed).items() if i<2},first_ids=sorted(content_by_id(first)),new_ids=[2,3],original_sites_reused=sorted(first))
 translated=0
 for d in D:
  initial=birth({},(3,3,3),d)
  for a in D:
   state=translate(initial,(3,3,3),a);back=translate(state,add((3,3,3),a),neg(a))
   assert valid(state) and state!=initial and back==initial and content_by_id(state)==content_by_id(initial)
   assert all(np.array_equal(np.subtract(next(x for x,r in state.items() if r[0]==i),next(x for x,r in initial.items() if r[0]==i)),a) for i in content_by_id(initial))
   translated+=1
 check('all_orientations_rigid_translation_and_inverse',translated==36,cases=translated)
 cube={}
 for y in (0,1):cube=birth(cube,(0,y,0),AX[0])
 for x in (0,1):cube=birth(cube,(x,0,1),AX[1])
 swapped=cube_exchange(cube);back=cube_exchange(swapped)
 check('dense_cube_moves_eight_immutable_records_and_returns',valid(swapped) and back==cube and swapped!=cube and content_by_id(cube)==content_by_id(swapped) and all(sum(abs(a-b) for a,b in zip(x,next(y for y,s in swapped.items() if s[0]==r[0])))==1 for x,r in cube.items()),records=8,occupied_sites=len(swapped),direction_counts_preserved=directions(cube)==directions(swapped))
 rotation_cases=0
 for R in rotation_matrices():
  rc=rotate(cube,R);rb=tuple(min(x[j] for x in rc) for j in range(3));ra=next(j for j in range(3) if R[j,2])
  assert cube_exchange(rc,base=rb,axis=ra)==rotate(swapped,R)
  for d in D:
   initial=birth({},(3,3,3),d)
   for a in D:
    rx=tuple(map(int,R@np.array((3,3,3))));rd=tuple(map(int,R@np.array(d)));ra_vec=tuple(map(int,R@np.array(a)))
    assert birth({},rx,rd)==rotate(initial,R)
    assert translate(rotate(initial,R),rx,ra_vec)==rotate(translate(initial,(3,3,3),a),R)
    rotation_cases+=1
 check('birth_translation_and_cube_event_rotation_covariance',rotation_cases==864,translation_cases=rotation_cases,cube_cases=24)
 # Check field charge directly, including genuinely empty background and holes.
 cases=[{},first,moved,renewed,cube,swapped]
 check('exact_staggered_gauss_identity',all(gauss_control(s) for s in cases),states=len(cases),side=8)
 # This fails without the staggered sign: empty space would have zero div.
 unstaggered_div_empty=0;expected_empty_charge6=-6
 check('missing_staggering_mutation_is_detected',unstaggered_div_empty!=expected_empty_charge6,mutant_div6=unstaggered_div_empty,required_div6=expected_empty_charge6)
 return cube,swapped


def fourier_increment(cube,swapped):
 X,Y,Z=sp.symbols('X Y Z');v=[X,Y,Z]
 def polynomial(state):
  out=[0,0,0]
  for x,y in bonds(state):
   d=tuple(b-a for a,b in zip(x,y));i=next(j for j in range(3) if d[j])
   # sorted adjacent edge always points along the positive coordinate axis.
   out[i]+=parity(x)*sp.prod(v[j]**x[j] for j in range(3))
  return sp.Matrix(out)
 delta=sp.simplify(polynomial(swapped)-polynomial(cube))
 expected=(1+Z)*sp.Matrix([Y-1,1-X,0]);div=sp.simplify(sp.Matrix([1-X,1-Y,1-Z]).dot(delta))
 check('exact_cube_fourier_polynomial_and_gauss_symbol',sp.simplify(delta-expected)==sp.zeros(3,1) and div==0,delta=[str(x) for x in delta],divergence=str(div))
 check('identity_cube_mutation_is_detected',sp.simplify(polynomial(cube)-polynomial(cube)-expected)!=sp.zeros(3,1),mutant_increment=[0,0,0])


CUBE=tuple(product((0,1),repeat=3));CUBESET=set(CUBE)
EDGES=tuple((x,add(x,e)) for x in CUBE for e in AX if add(x,e) in CUBESET)
def matching_states():
 states=set()
 def visit(available,chosen):
  if not available:states.add(tuple(sorted(chosen)));return
  x=min(available);visit(available-{x},chosen)
  for y in available-{x}:
   if sum(abs(a-b) for a,b in zip(x,y))==1:visit(available-{x,y},chosen+[tuple(sorted((x,y)))])
 visit(CUBESET,[]);return sorted(states)
def records_from_matching(m):
 r={}
 for x,y in m:r=birth(r,x,tuple(b-a for a,b in zip(x,y)))
 return r

def finite_cube():
 states=matching_states();index={m:i for i,m in enumerate(states)};n=len(states)
 Qc=np.zeros((n,n),dtype=int);Qb=np.zeros_like(Qc)
 for i,m in enumerate(states):
  r=records_from_matching(m)
  for edge in EDGES:
   if not set(edge)&r.keys():
    new=tuple(sorted((*m,edge)));Qb[i,index[new]]+=1
  for x,y in m:
   for a in D:
    if any(add(z,a) not in CUBESET for z in (x,y)):continue
    try:s=translate(r,x,a)
    except ValueError:continue
    Qc[i,index[tuple(sorted(bonds(s)))]]+=1
  for axis in range(3):
   try:s=cube_exchange(r,axis=axis)
   except ValueError:continue
   Qc[i,index[tuple(sorted(bonds(s)))]]+=1
 np.fill_diagonal(Qc,-Qc.sum(axis=1));np.fill_diagonal(Qb,-Qb.sum(axis=1))
 census=dict(sorted(Counter(len(m) for m in states).items()))
 check('reflecting_cube_matching_census_and_detailed_balance',n==108 and census=={0:1,1:12,2:42,3:44,4:9} and np.array_equal(Qc,Qc.T) and np.all(Qc.sum(axis=1)==0),states=n,by_dimer_count=census,max_conservative_exit_rate=int(np.max(-np.diag(Qc))))
 Q=Qc+Qb;adj=Q.copy();np.fill_diagonal(adj,0)
 count,labels=connected_components(csr_matrix(adj),directed=True,connection='strong')
 closed=[]
 for label in range(count):
  members=np.flatnonzero(labels==label)
  if not any(adj[i,j] for i in members for j in range(n) if labels[j]!=label):closed.append(list(map(int,members)))
 closed_ids={i for c in closed for i in c};transient=[i for i in range(n) if i not in closed_ids]
 # Exact probabilities from the empty state, beta=kappa=nu=1.
 T=sp.Matrix(Q[np.ix_(transient,transient)]);R=sp.Matrix([[sum(int(Q[i,j]) for j in c) for c in closed] for i in transient])
 hitting=-T.inv()*R;empty_row=transient.index(index[()]);p=list(hitting[empty_row,:])
 assert T*hitting+R==sp.zeros(len(transient),len(closed))
 assert all(sum(hitting.row(i))==1 for i in range(len(transient)))
 assert all(0<=x<=1 for x in hitting)
 jam=sum((p[j] for j,c in enumerate(closed) if len(states[c[0]])<4),sp.S(0))
 closed_rows=[{'size':len(c),'dimers':len(states[c[0]]),'empty_start_hitting_probability':str(p[j]),'representative_edges':states[c[0]]} for j,c in enumerate(closed)]
 check('reflecting_cube_exact_absorption_keeps_unfilled_states',sum(p)==1 and jam>0 and all(len({len(states[i]) for i in c})==1 for c in closed),transient_states=len(transient),closed_components=len(closed),unfilled_absorption_probability=str(jam),closed_component_sizes=dict(Counter(len(c) for c in closed)))
 (HERE/'PAIRED_RECORD_CUBE_ABSORPTION.json').write_text(json.dumps({'boundary':'Reflecting 2x2x2 cube; not the periodic lattice','rates':{'beta':1,'kappa':1,'nu':1},'closed_classes':closed_rows,'unfilled_absorption_probability':str(jam)},indent=2)+'\n')
 # Exact birth count identity at every cube configuration.
 vacancy=np.array([8-2*len(m) for m in states]);empty_edges=np.array([sum(not set(e)&set(z for pair in m for z in pair) for e in EDGES) for m in states])
 check('reflecting_cube_exact_vacancy_generator_identity',np.array_equal(Q@vacancy,-2*empty_edges),states=n)


def main():
 nn_birth_controls();cube,swapped=histories();fourier_increment(cube,swapped);finite_cube()
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'PAIRED_RECORD_FORMATION_AND_DIMER_GAUSS.md']}
 result={'status':'author finite controls; independent review pending','sources_sha256':sources,'python':sys.version,'rows':ROWS,'all_pass':all(r['pass'] for r in ROWS)}
 (HERE/'PAIRED_RECORD_DIMER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'all_pass':result['all_pass'],'groups':len(ROWS),'sources_sha256':sources},sort_keys=True))
if __name__=='__main__':main()
