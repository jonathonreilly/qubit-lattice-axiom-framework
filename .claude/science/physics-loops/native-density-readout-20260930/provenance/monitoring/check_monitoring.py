#!/usr/bin/env python3
# Independent literal original-Hamiltonian pin calculation; no author code imports.
from fractions import Fraction as F
import itertools,collections,json,time,resource,hashlib,pathlib
wall=time.monotonic();cpu=time.process_time();axes=((1,0,0),(0,1,0),(0,0,1));zero=(0,0,0)
def add(x,y,L):return tuple((a+b)%L for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def pair(x,y):return tuple(sorted((x,y)))
def combine(rows,cs):
 d=collections.defaultdict(int)
 for row,c in zip(rows,cs):
  for e,a in row.items():d[e]+=c*a
 return {e:a for e,a in d.items() if a}
def q(x,L):
 ds=[{pair(add(x,e,L),add(x,neg(e),L)):1} for e in axes]
 out=[(combine(ds,(1,-1,0)),F(1,2)),(combine(ds,(1,1,-2)),F(1,6))]
 for i,j in itertools.combinations(range(3),2):
  terms={}
  for s,t in itertools.product((-1,1),repeat=2):
   a=tuple(s*v for v in axes[i]);b=tuple(t*v for v in axes[j]);terms[pair(add(x,a,L),add(x,b,L))]=s*t
  out.append((terms,F(1,4)))
 return out
D=[];kinds=[]
for i in range(3):
 for s in (-1,1):D.append(tuple(2*s*v for v in axes[i]));kinds.append(('a',i,s))
for i,j in itertools.combinations(range(3),2):
 for s,t in itertools.product((-1,1),repeat=2):D.append(tuple(s*a+t*b for a,b in zip(axes[i],axes[j])));kinds.append(('p',i,j,s,t))
results={}
for L in (5,6):
 index={pair(zero,tuple(v%L for v in d)):i for i,d in enumerate(D)};assert len(index)==18
 M=[[F(2 if i==j else 0) for j in range(18)] for i in range(18)]
 T=[[F(0) for _ in range(18)] for _ in range(18)]
 def outer(target,row,coef):
  entries=[(index[e],v) for e,v in row.items() if e in index]
  for i,a in entries:
   for j,b in entries:target[i][j]+=coef*a*b
 sites=list(itertools.product(range(L),repeat=3));cache={x:q(x,L) for x in sites};nonempty_cross=0
 for x in sites:
  rows=cache[x]
  # Original attractions, plus2mu I from muN+V3-muDdiag. No S rows used.
  for a,(row,w) in enumerate(rows):outer(M,row,(-2 if a<2 else -1)*w)
  for e in axes:
   nextrows=cache[add(x,e,L)]
   for (a,w),(b,v) in zip(rows,nextrows):
    assert w==v
    if set(a)&set(index) and set(b)&set(index):nonempty_cross+=1
    outer(T,combine([b,a],(1,-1)),w)
 assert nonempty_cross==0
 # Entrywise comparison with PRE, including every offdiagonal and mixing zero.
 for i,ki in enumerate(kinds):
  for j,kj in enumerate(kinds):
   em=et=F(0)
   if i==j:em,et=(F(2,3),F(4)) if ki[0]=='a' else (F(3,2),F(3))
   elif ki[0]==kj[0]=='p' and ki[1:3]==kj[1:3] and sum(a!=b for a,b in zip(ki[3:],kj[3:]))==1:em,et=F(1,4),F(-3,2)
   assert M[i][j]==em and T[i][j]==et,(L,i,j,M[i][j],T[i][j],em,et)
 # Eigenvectors are independently enumerated sign characters on each plane.
 checks=0
 for plane in itertools.combinations(range(3),2):
  inds=[i for i,k in enumerate(kinds) if k[0]=='p' and k[1:3]==plane]
  for powers,eig in [((0,0),(F(2),F(0))),((1,0),(F(3,2),F(3))),((0,1),(F(3,2),F(3))),((1,1),(F(1),F(6)))]:
   vec=[F(0)]*18
   for i in inds:vec[i]=kinds[i][3]**powers[0]*kinds[i][4]**powers[1]
   for mat,val in zip((M,T),eig):assert [sum(mat[i][j]*vec[j] for j in range(18)) for i in range(18)]==[val*x for x in vec]
   checks+=1
 results[f'L{L}']={'matrix_entries_each':324,'pin_centers_with_cross_gradient':nonempty_cross,'plane_eigenvectors':checks,'mu_matrix':[[str(a) for a in row] for row in M],'tau_matrix':[[str(a) for a in row] for row in T]}
# Literal physical occupation action on four actual M2 factors.
pairs=list(itertools.combinations(range(4),2));counts=collections.Counter();paths=0
for p in pairs:
 for qpair in pairs:
  overlap=len(set(p)&set(qpair))
  for state in range(16):
   if any(not (state>>v)&1 for v in qpair):continue
   after=state
   for v in qpair:after &= ~(1<<v)
   if any((after>>v)&1 for v in p):continue
   for v in p:after |=1<<v
   actual=F(0)
   for v in range(4):
    ni=(state>>v)&1;no=(after>>v)&1
    actual+=ni*no-F(ni+no,2)
   assert actual==overlap-2
   paths+=1;counts[str(actual)]+=1
# Full integer occupation identity on an actual small embedded configuration menu.
menu=[zero]+D[:6]+D[6:9];Dset=set(D);cfgs=0
for mask in range(1<<len(menu)):
 occ={x for i,x in enumerate(menu) if (mask>>i)&1}
 deg={x:sum(tuple(y[k]-x[k] for k in range(3)) in Dset for y in occ) for x in occ}
 E=sum(deg.values())//2;triples=sum(m*(m-1)//2 for m in deg.values());Dval=sum((m-1)*(m-2)//2 for m in deg.values())
 assert Dval==len(occ)-2*E+triples
 for tau in (F(1,100),F(1,3),F(1),F(10)):
  c=min(F(1),F(1,3)+2*tau)
  assert 2*Dval+4*c*E-2*c*len(occ)==2*(1-c)*Dval+2*c*triples>=0
 cfgs+=1
results['physical_paths']={'nonzero_Bp_dagger_Bq_paths':paths,'coefficients':dict(counts),'all_pairs':36,'full_four_site_basis_masks':16}
results['actual_configuration_count_identity']={'embedded_sites':len(menu),'all_masks':cfgs,'parameter_cases_per_mask':4}
results['resources']={'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-wall,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
results['runner_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
print(json.dumps(results,sort_keys=True,indent=2))
