#!/usr/bin/env python3
"""Independent checks of the component-polymer proof, before author checker access."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter,defaultdict,deque
from fractions import Fraction
from math import factorial
import hashlib,json,sys
import sympy as s
HERE=Path(__file__).resolve().parent
N=7
unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
origin=(0,0,0)
pos=lambda x:tuple(a%N for a in x)
add=lambda a,b,m=1:pos(tuple(a[i]+m*b[i] for i in range(3)))
checks=[]
def check(name,condition,detail=None):
 assert condition,(name,detail)
 checks.append(dict(name=name,detail=detail))
 print("VERIFIED",name,json.dumps(detail,sort_keys=True),flush=True)
# Every unoriented charge edge has one midpoint/axis identifier on this odd torus.
edges=[(r,i) for r in product(range(N),repeat=3) for i in range(3)]
endpoints={e:(add(e[0],unit[e[1]],-1),add(e[0],unit[e[1]])) for e in edges}
endpoint_index=defaultdict(set)
for e,ends in endpoints.items():
 for x in ends:endpoint_index[x].add(e)
line_adj={e:set.union(*(endpoint_index[x] for x in ends))-{e} for e,ends in endpoints.items()}
check("simple_step_two_graph_and_line_degree",
 len({frozenset(v) for v in endpoints.values()})==len(edges)
 and {len(v) for v in endpoint_index.values()}=={6}
 and {len(v) for v in line_adj.values()}=={10},
 dict(charge_vertices=N**3,charge_edges=len(edges),line_degree=10))
anchor=(origin,0)
same_species={(0,e) for x in endpoints[anchor] for e in endpoint_index[x]}
midpoint={(species,(origin,i)) for species in range(2) for i in range(3)}
check("typed_incompatibility_anchor_overcount",
 len(same_species)==11 and len(midpoint)==6 and len(same_species|midpoint)==16,
 dict(endpoint_anchors=11,midpoint_anchors=6,union=16,claimed_safe_bound=17))
animals={frozenset([anchor])};counts={};four=None
def canonical_walk(animal):
 visited={anchor};walk=[anchor]
 def dfs(e):
  for f in sorted(line_adj[e]&set(animal)):
   if f not in visited:
    visited.add(f);walk.append(f);dfs(f);walk.append(e)
 dfs(anchor)
 return tuple(walk)
for n in range(1,5):
 walks={canonical_walk(a) for a in animals}
 assert len(walks)==len(animals)
 assert all(len(w)==2*n-1 and set(w)==set(a) for a,w in ((a,canonical_walk(a)) for a in animals))
 assert len(animals)<=10**(2*n-2)
 counts[n]=len(animals)
 if n==4:four=animals;break
 enlarged=set()
 for a in animals:
  boundary=set.union(*(line_adj[e] for e in a))-set(a)
  for e in boundary:enlarged.add(frozenset(set(a)|{e}))
 animals=enlarged
check("canonical_depth_first_injection_for_rooted_edge_animals",True,dict(counts=counts,walk_length="2(n-1)"))
balanced_four=0
for animal in four:
 ordered=sorted(animal)
 if len({e[0] for e in ordered})!=4:continue
 for signs in product((-1,1),repeat=4):
  charge=Counter()
  for e,sign in zip(ordered,signs):
   a,b=endpoints[e];charge[a]+=sign;charge[b]-=sign
  if all(v==0 for v in charge.values()):balanced_four+=1
check("balanced_signed_four_edge_anchor_count",balanced_four==8,dict(count=balanced_four))
# The scalar criterion uses an exponential activity enlargement AND a=n.
q=s.Rational(1,2)
S=s.factor(q**4/(100*(1-q)))
check("enlarged_activity_and_zero_activity_ghost_constants",
 S==s.Rational(1,800) and 17*S<1 and 6*S<1,
 dict(S=str(S),ordinary_root_budget=str(17*S),spatial_ghost_budget=str(6*S),
      z_star="1/(400 e^2)",q="200 e^2 z"))
# Balanced branch with two distinct simple-cycle decompositions.
u=(0,0,0);v=(2,0,0)
paths=[
 [u,v],
 [u,(0,2,0),(2,2,0),v],
 [u,(0,-2,0),(2,-2,0),v],
 [u,(0,0,2),(2,0,2),v]]
def path_records(path,species=0):
 records=[]
 for a,b in zip(path,path[1:]):
  r=pos(tuple((a[i]+b[i])//2 for i in range(3)))
  feature=tuple((b[i]-a[i])//2 for i in range(3))
  assert sum(abs(x) for x in feature)==1
  records.append((r,species,feature))
 return records
record_paths=[path_records(path if i<2 else list(reversed(path))) for i,path in enumerate(paths)]
branch=sum(record_paths,[])
def charge_and_components(records):
 charge=Counter();vertices=[]
 for r,kind,f in records:
  a=add(r,f,-1);b=add(r,f)
  charge[(kind,a)]+=1;charge[(kind,b)]-=1;vertices.append({(kind,a),(kind,b)})
 adjacency=[{j for j in range(len(records)) if j!=i and vertices[i]&vertices[j]} for i in range(len(records))]
 unseen=set(range(len(records)));parts=[]
 while unseen:
  start=min(unseen);todo=[start];part=set()
  while todo:
   i=todo.pop()
   if i in part:continue
   part.add(i);todo.extend(adjacency[i]-part)
  unseen-=part;parts.append(part)
 return charge,parts,adjacency
charge,parts,adjacency=charge_and_components(branch)
decomposition_one=[record_paths[0]+record_paths[2],record_paths[1]+record_paths[3]]
decomposition_two=[record_paths[0]+record_paths[3],record_paths[1]+record_paths[2]]
for decomposition in (decomposition_one,decomposition_two):
 assert Counter(sum(decomposition,[]))==Counter(branch)
 assert all(all(x==0 for x in charge_and_components(cycle)[0].values()) for cycle in decomposition)
check("branched_component_is_unique_when_cycle_decomposition_is_not",
 len(branch)==10 and len({r[0] for r in branch})==10 and len(parts)==1
 and all(x==0 for x in charge.values())
 and {frozenset(x) for x in decomposition_one}!={frozenset(x) for x in decomposition_two},
 dict(records=10,component_count=1,simple_cycle_decompositions=2))
def loop(center,i,j,kind=0):
 c=center
 return [(add(c,unit[j],-1),kind,unit[i]),(add(c,unit[i]),kind,unit[j]),
         (add(c,unit[j]),kind,tuple(-a for a in unit[i])),
         (add(c,unit[i],-1),kind,tuple(-a for a in unit[j]))]
first=loop(origin,0,1)
second=loop((0,-1,1),1,2)
a,pa,_=charge_and_components(first);b,pb,_=charge_and_components(second)
both=first+second
c,pc,_=charge_and_components(both)
check("midpoint_capacity_is_independent_of_charge_component_separation",
 all(x==0 for x in a.values()) and all(x==0 for x in b.values())
 and len(pc)==2 and len({r[0] for r in both})==7,
 dict(individually_balanced=True,charge_components=2,records=8,physical_slots=7))
first=loop((1,1,0),0,1,kind=0)
second=loop((3,3,0),0,1,kind=1)
c,pc,_=charge_and_components(first+second)
Avertices={q[1] for q in charge_and_components(first)[0]}
Bvertices={q[1] for q in charge_and_components(second)[0]}
check("different_species_may_share_charge_vertex_without_conflict",
 len({r[0] for r in first+second})==8 and len(pc)==2 and bool(Avertices&Bvertices)
 and all(x==0 for x in c.values()))
# Exact Mayer coefficients with repeated copies of a self-incompatible polymer.
phi={}
for n in range(1,6):
 if n==1:phi[n]=Fraction(1)
 else:
  potential=list(combinations(range(n),2));total=0
  for bits in range(1<<len(potential)):
   adjacency=[set() for _ in range(n)];present=0
   for a,(i,j) in enumerate(potential):
    if bits>>a&1:adjacency[i].add(j);adjacency[j].add(i);present+=1
   reached={0};todo=[0]
   while todo:
    i=todo.pop()
    for j in adjacency[i]-reached:reached.add(j);todo.append(j)
   if len(reached)==n:total+=(-1)**present
  phi[n]=Fraction(total,factorial(n))
 assert phi[n]==Fraction((-1)**(n-1),n)
w,hx,hy=s.symbols("w hx hy")
actual=s.diff(s.log(1+w*s.exp(hx+hy)),hx,hy).subs({hx:0,hy:0})
jet=sum(s.Rational(c.numerator,c.denominator)*n*n*w**n for n,c in phi.items())
check("root_multiplicity_and_two_source_derivative_factorials",
 s.simplify(actual-w/(1+w)**2)==0
 and s.series(actual-jet,w,0,6).removeO()==0
 and all(abs(phi[n])*n==1 for n in phi),
 dict(phi={str(n):str(v) for n,v in phi.items()},root_insertion="R_x=n",two_insertions="n^2"))
# Record-adjacency distance for the branched example, and the general scalar envelope.
branch_adjacency=charge_and_components(branch)[2]
for start in range(len(branch)):
 distance={start:0};todo=deque([start])
 while todo:
  i=todo.popleft()
  for j in branch_adjacency[i]:
   if j not in distance:distance[j]=distance[i]+1;todo.append(j)
 for end,hops in distance.items():
  r=sum(min((a-b)%N,(b-a)%N) for a,b in zip(branch[start][0],branch[end][0]))
  assert r<=2*hops<=2*(len(branch)-1)
M=s.symbols("M",positive=True)
check("distance_and_cluster_mass_exponential_envelope",
 s.simplify(s.diff(M*s.exp(-M/2),M)/s.exp(-M/2)-(1-M/2))==0
 and s.simplify((M*s.exp(-M/2)).subs(M,2)-2/s.E)==0,
 dict(graph_step_bound=2,covariance_envelope="(2/e) exp(-r/4)"))
a,b,c,k1,k2,k3=s.symbols("a b c k1 k2 k3")
k=s.Matrix([k1,k2,k3]);K2=k.dot(k)
tensor=s.Matrix(3,3,lambda i,j:(a*K2+b*k[i]**2) if i==j else c*k[i]*k[j])
coefficients=s.Poly((tensor*k)[0],k1,k2,k3).coeffs()
solution=s.solve(coefficients,(b,c),dict=True)
check("cubic_analytic_Gauss_quadratic_tensor",solution==[{b:-a,c:-a}],
 dict(solution={str(x):str(y) for x,y in solution[0].items()}))
result=dict(scope="Independent provisional proof controls before author polymer checker/results access.",
 checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 versions=dict(python=sys.version,sympy=s.__version__),failed_executions=["ATTEMPT_01_RECEIPT.json"])
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print("INDEPENDENT_GROUPS",len(checks),flush=True)
