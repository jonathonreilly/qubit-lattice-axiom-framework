#!/usr/bin/env python3
"""Author padded-fiber, Dirichlet-comparison and killed-clock controls."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import datetime,hashlib,itertools,json,math
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent

def matchings(q,edges,minimum=0):
 adj={a:[] for a in range(q)}
 for a,b in sorted(edges):adj[a].append(b)
 result=[]
 def visit(a,used,chosen):
  if len(chosen)+q-a<minimum:return
  if a==q:
   result.append(frozenset(chosen));return
  visit(a+1,used,chosen)
  for b in adj[a]:
   if b not in used:visit(a+1,used|{b},chosen+[(a,b)])
 visit(0,set(),[])
 return sorted(result,key=lambda M:(len(M),sorted(M)))

def connected(q,edges):
 adj={a:set() for a in range(2*q)}
 for a,b in edges:adj[a].add(b);adj[b].add(a)
 seen={0};stack=[0]
 while stack:
  for v in adj[stack.pop()]-seen:seen.add(v);stack.append(v)
 return len(seen)==2*q

def broder_graph(q,edges,states):
 index={M:i for i,M in enumerate(states)};adj={a:set() for a in range(2*q)}
 for a,b in edges:adj[a].add(b);adj[b].add(a)
 transitions=set()
 for i,M in enumerate(states):
  if len(M)==q:targets=[M-{e} for e in M]
  else:
   mate={x:y for a,b in M for x,y in [(a,b),(b,a)]}
   holes=set(range(2*q))-set(mate);assert len(holes)==2
   pair=tuple(sorted(holes));targets=[M|{pair}] if pair in edges else []
   for a in holes:
    for b in adj[a]:
     if b in mate:
      c=mate[b];targets.append((M-{tuple(sorted((b,c)))})|{tuple(sorted((a,b)))})
  assert len(set(targets))==len(targets)
  assert len(targets)<=len(edges)
  for target in targets:
   j=index[target];assert i!=j;transitions.add(tuple(sorted((i,j))))
 degrees=Counter(x for e in transitions for x in e)
 assert max(degrees.values())<=len(edges)
 return sorted(transitions)

def two_level_graph(edges,states):
 index={M:i for i,M in enumerate(states)};ranks={len(M) for M in states};top=max(ranks);out=set()
 for i,M in enumerate(states):
  used={x for e in M for x in e}
  if len(M)<top:
   for e in edges:
    if not set(e)&used:out.add(tuple(sorted((i,index[M|{e}]))))
  for e in M:
   rest=M-{e};occupied={x for f in rest for x in f}
   for f in edges-{e}:
    if not set(f)&occupied:
     other=index[rest|{f}]
     if i!=other:out.add(tuple(sorted((i,other))))
 return sorted(out)

def laplacian(n,edges):
 A=np.zeros((n,n),dtype=np.int64)
 for a,b in edges:A[a,a]+=1;A[b,b]+=1;A[a,b]-=1;A[b,a]-=1
 return A

def padded_case(K,edges,j,all_original):
 k=j+1;h=K-k;q=K+h;f0=math.factorial(h)**2
 aug={(a,q+b-K) for a,b in edges}
 aug|={(a,q+b) for a in range(K,q) for b in range(K)}
 aug|={(a,q+b) for a in range(K) for b in range(K,q)}
 assert len(aug)==len(edges)+2*h*K and connected(q,aug)
 original=[M for M in all_original if len(M) in (j,k)]
 index={M:i for i,M in enumerate(original)};nb=len(original)
 states=matchings(q,aug,q-1);nh=len(states)
 projections=[frozenset((a,K+b-q) for a,b in M if a<K and b<q+K) for M in states]
 bytype=Counter();fibers=Counter();Z=np.zeros((nh,nb),dtype=np.int64)
 original_vertices=set(range(K))|set(range(q,q+K))
 for i,(M,T) in enumerate(zip(states,projections)):
  holes=set(range(2*q))-{x for e in M for x in e}
  if len(M)==q:kind='perfect';expected=k
  else:
   count=len(holes&original_vertices)
   kind={2:'two_original',1:'mixed',0:'two_dummy'}[count];expected={2:j,1:k,0:k+1}[count]
  assert len(T)==expected
  bytype[kind]+=1;fibers[kind,T]+=1
  if len(T) in (j,k):Z[i,index[T]]=k+1
  else:
   for e in T:Z[i,index[T-{e}]]+=1
  assert int(Z[i].sum())==k+1
 counts=Counter(map(len,all_original));a=lambda r:counts[r]
 expected_fibers={'perfect':f0,'two_original':(h+1)**2*f0,'mixed':2*h*f0,'two_dummy':f0}
 for (kind,T),count in fibers.items():assert count==expected_fibers[kind]
 assert bytype['perfect']==a(k)*f0
 assert bytype['two_original']==a(j)*(h+1)**2*f0
 assert bytype['mixed']==a(k)*2*h*f0
 assert bytype['two_dummy']==a(k+1)*f0
 ratio=F(nh-bytype['perfect'],bytype['perfect'])
 R=F(a(K-1),a(K));upper=(h+1)*R+2*h+F(len(edges),k+1)
 assert ratio==(h+1)**2*F(a(j),a(k))+2*h+F(a(k+1),a(k)) and ratio<=upper
 b_edges=two_level_graph(edges,original);b_set=set(b_edges);aug_edges=broder_graph(q,aug,states)
 good_counts=Counter();boundary=Counter();energy=np.zeros((nb,nb),dtype=np.int64)
 for x,y in aug_edges:
  A,B=projections[x],projections[y];ga=len(A)<=k;gb=len(B)<=k
  if ga and gb:
   if A!=B:
    edge=tuple(sorted((index[A],index[B])));assert edge in b_set;good_counts[edge]+=1
  elif not ga and not gb:assert A==B
  else:
   U,T=(B,A) if ga else (A,B)
   assert len(U-T)==1 and T<U;boundary[U,T]+=1
  diff=Z[x]-Z[y];positions=np.flatnonzero(diff)
  for a in positions:
   for b in positions:energy[a,b]+=int(diff[a])*int(diff[b])
 fmin=(2*h+1)*f0;fmax=(h+1)**2*f0;mhat=len(aug)
 assert max(good_counts.values(),default=0)<=fmax*mhat
 assert max(boundary.values(),default=0)<=f0*mhat
 for T in original:assert sum(1 for U in projections if U==T)>=fmin
 LB=laplacian(nb,b_edges)
 energy_bound=mhat*f0*((k+1)**2*(h+1)**2+(k+1))*LB
 # Integer matrix assembly; eigenvalue PSD checks are explicitly numerical.
 slack=energy_bound-energy
 scale=max(1,float(np.linalg.norm(slack,ord=np.inf)))
 smallest=float(np.linalg.eigvalsh(slack.astype(float))[0])
 assert smallest>=-1e-12*scale
 assert np.all(energy.sum(axis=0)==0)
 summary=dict(K=K,j=j,h=h,m=len(edges),augmented_vertices=2*q,augmented_edges=mhat,
  original_two_level_states=nb,augmented_states=nh,augmented_transition_edges=len(aug_edges),
  fiber_counts=dict(bytype),exact_R_hat=str(ratio),proved_upper_R_hat=str(upper),
  maximum_good_projected_edge_multiplicity=max(good_counts.values(),default=0),
  maximum_bad_parent_multiplicity=max(boundary.values(),default=0),
  exact_good_minimum_fiber=fmin,energy_PSD_scaled_minimum=smallest/scale)
 if nh<=180:
  LH=laplacian(nh,aug_edges)
  gh=float(np.linalg.eigvalsh(LH.astype(float))[1]);gb=float(np.linalg.eigvalsh(LB.astype(float))[1])
  assert min(gh,gb)>0 and gb>=gh/(mhat*(h+2))-1e-12
  summary['numeric_gap_comparison']={'augmented':gh,'two_level':gb,'lower':gh/(mhat*(h+2))}
 return summary

def padded_controls():
 rows=[];graph_inventory=[]
 for K in (2,3):
  possible=[(a,K+b) for a in range(K) for b in range(K)]
  eligible=[]
  for mask in range(1<<len(possible)):
   edges={e for i,e in enumerate(possible) if mask>>i&1}
   if not connected(K,edges):continue
   allm=matchings(K,edges)
   if not any(len(M)==K for M in allm):continue
   eligible.append((mask,edges,allm))
  # All K2 cases; a fixed evenly spaced K3 subset including the complete graph.
  chosen=range(len(eligible)) if K==2 else sorted(set(np.linspace(0,len(eligible)-1,18,dtype=int)))
  for i in chosen:
   mask,edges,allm=eligible[i]
   for j in range(1,K):
    value=padded_case(K,edges,j,allm);value['graph_mask']=mask;rows.append(value)
  graph_inventory.append(dict(K=K,eligible_connected_graphs_with_perfect_matching=len(eligible),
                              selected_graphs=len(chosen)))
 K=4
 for kind in ['path','cycle','complete']:
  edges={(a,K+b) for a in range(K) for b in range(K) if kind=='complete' or b==a or b==a-1 or (kind=='cycle' and a==0 and b==K-1)}
  allm=matchings(K,edges)
  for j in range(1,K):
   value=padded_case(K,edges,j,allm);value['graph_kind']=kind;rows.append(value)
 return dict(inventory=graph_inventory,rows=rows)

def killed_controls():
 rows=[]
 for n,kind,gap in [(3,'path',1),(4,'cycle',2),(4,'complete',4)]:
  edges=[(i,j) for i in range(n) for j in range(i+1,n)
         if kind=='complete' or j==i+1 or (kind=='cycle' and i==0 and j==n-1)]
  L=s.Matrix(laplacian(n,edges).tolist())
  assert min(x for x in L.eigenvals() if x>0)==gap
  for hazards in [[1]*n,[1]+[0]*(n-1),list(range(n))]:
   m=max(hazards);p=s.Rational(sum(hazards),n)
   for beta in [s.Rational(1,100),s.Rational(1,3),s.Integer(1),s.Integer(7)]:
    A=L+beta*s.diag(*hazards);inverse=A.inv();mean=inverse*s.ones(n,1)
    factor=2/(beta*p)+(1+2*m/p)/gap
    matrix=factor*A-s.eye(n)
    # Exact rational LDL pivots certify the displayed operator inequality.
    _,D=matrix.LDLdecomposition(hermitian=False)
    assert all(D[i,i]>0 for i in range(n))
    bound=(1+.5*math.log(n))*float(factor)
    assert max(map(float,mean))<=bound
    rows.append(dict(n=n,kind=kind,hazards=hazards,beta=str(beta),known_gap=gap,
                     inverse_eigenvalue_bound=str(factor),exact_LDL_pivots=[str(D[i,i]) for i in range(n)],
                     exact_mean_by_start=[str(z) for z in mean],uniform_logarithmic_bound=bound))
 return rows

def cubic_constants():
 rows=[]
 for K in [256,500,864,2048,16384]:
  m=6*K;values=[]
  for j in sorted({1,2,K//2,K-2,K-1}):
   k=j+1;h=K-k;mhat=m+2*h*K
   upper=(h+1)*F(K*K,6)+2*h+F(m,k+1)
   C=1+(2*K-2)*(m+m*m)*(k-1)*(k+1+2*m)
   assert mhat<=4*K*K and h+2<=K and upper<=K**3 and C<=2**11*K**5
   denom=256*mhat*mhat*(h+2)*upper**4*C
   assert denom<=2**23*K**22
   values.append(dict(j=j,mhat=mhat,R_upper=str(upper),corridor_C=C,
                      ratio_to_coarse_gap_denominator=str(denom/F(2**23*K**22))))
  delta=F(3,32*K**3)
  assert 2*K*delta==F(3,16*K**2)
  assert 2*delta/(1-2*delta)<=F(3,13*K**3)
  assert F(1,6*K)+F(4,3)*K**3<=2*K**3
  assert 12*2**23<=2**27
  rows.append(dict(K=K,stages=values,selection_delta_bound=str(delta),
                   sequence_TV_bound=str(2*K*delta),relative_clock_mean_bound=str(F(3,13*K**3))))
 return rows

def main():
 out=HERE/'geometric_all_stage_polynomial_checks';out.mkdir(exist_ok=False)
 functions=[('padded_fibers_and_comparison',padded_controls),('arbitrary_birth_killing',killed_controls),('cubic_constants',cubic_constants)]
 groups=[]
 for name,fn in functions:
  value=fn();groups.append(dict(group=name,passed=True,detail=value))
  (out/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n');print(name,'PASS',flush=True)
 sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in (
  Path(__file__).name,'GEOMETRIC_ALL_STAGE_POLYNOMIAL_GAP_AND_FILLING.md',
  'GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md','GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md')}
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources_sha256=sources,groups=groups,
             scope='Author exact finite fibers/projections/operator inequalities plus labelled numerical matrix comparisons. Imported matching-chain and monomer theorems remain explicit dependencies; no empirical exponent or proof by enumeration.')
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
