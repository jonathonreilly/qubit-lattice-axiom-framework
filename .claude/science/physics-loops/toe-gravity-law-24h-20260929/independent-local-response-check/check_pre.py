"""Independent exact Gauss completion/coherence control; no author imports."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import time,resource,json,hashlib,itertools
from pathlib import Path
from collections import deque,defaultdict
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_CPU,(10,10));t0=time.process_time();out=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not any((rt/k).exists() for k in ('STOP_REQUESTED','STOP_REQUESTED.json'))
 assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
guard()
results=[]
for L,insideB in [(12,{(1,0,0):1}),(12,{(1,0,0):-1}),(20,{(1,0,0):1,(0,1,0):1,(0,0,1):1})]:
 R=2;V=list(itertools.product(range(L),repeat=3));Vs=set(V);par=lambda x:sum(x)%2
 def nbr(x):
  return [tuple((x[j]+(sg if j==i else 0))%L for j in range(3)) for i in range(3) for sg in (-1,1)]
 def edge(x,y):return (x,y) if par(x)==0 else (y,x)
 def sgn(x):return 1 if par(x)==0 else -1
 D={x for x in V if max(min(a,L-a) for a in x)<=R};ext=Vs-D
 def divergence(E):
  v=defaultdict(int)
  for (a,b),f in E.items():v[a]+=f;v[b]-=f
  return v
 def treeflow(vertices,need):
  root=min(vertices);order=[root];parent={root:None}
  for x in order:
   for y in nbr(x):
    if y in vertices and y not in parent:parent[y]=x;order.append(y)
  assert len(order)==len(vertices)
  sums={x:int(need.get(x,0)) for x in vertices};E={}
  for x in reversed(order[1:]):
   y=parent[x];E[edge(x,y)]=sgn(x)*sums[x];sums[y]+=sums[x]
  assert sums[root]==0
  return {e:v for e,v in E.items() if v}
 q={x:(1 if par(x)==0 else 0) for x in V};q[(0,0,0)]=0;q.update(insideB)
 Q=sum(q[x]-(1 if par(x)==0 else 0) for x in D)
 exB=[x for x in sorted(ext) if par(x)==1];exA=[x for x in sorted(ext) if par(x)==0]
 for x in exB[:abs(Q)]:q[x]=-1 if Q>0 else 1
 # Additional charge-neutral exterior record changes, not retained by reference.
 for x in exB[abs(Q):abs(Q)+4]:q[x]=1
 for x in exA[:2]:q[x]=-1
 need={x:q[x]-(1 if par(x)==0 else 0) for x in V};assert sum(need.values())==0
 E=treeflow(Vs,need)
 # Add a divergence-free cycle crossing the regional boundary.
 cycle=[(R,0,0),(R+1,0,0),(R+1,1,0),(R,1,0)]
 for x,y in zip(cycle,cycle[1:]+cycle[:1]):
  e=edge(x,y);E[e]=E.get(e,0)+7*sgn(x)
 div=divergence(E);assert all(div[x]==need[x] for x in V)
 Ein={e:f for e,f in E.items() if all(x in D for x in e)}
 di=divergence(Ein);d={x:q[x]-(1 if par(x)==0 else 0)-di[x] for x in D};assert sum(d.values())==Q
 boundary={x for x in D if any(y in ext for y in nbr(x))};assert all(d[x]==0 for x in D-boundary)
 def complete(qin,internal):
  vi=divergence(internal);dd={x:qin[x]-(1 if par(x)==0 else 0)-vi[x] for x in D};total=sum(dd.values());fields=dict(internal)
  qr={x:(qin[x] if x in D else (1 if par(x)==0 else 0)) for x in V}
  # Deterministic exterior charge placement, depending only on d through total.
  for x in exB[:abs(total)]:qr[x]=-1 if total>0 else 1
  for x in boundary:
   y=min(y for y in nbr(x) if y in ext);fields[edge(x,y)]=sgn(x)*dd[x]
  vc=divergence(fields);remaining={x:qr[x]-(1 if par(x)==0 else 0)-vc[x] for x in ext}
  fields.update(treeflow(ext,remaining));vr=divergence(fields)
  assert all(vr[x]==qr[x]-(1 if par(x)==0 else 0) for x in V)
  assert all(qr[x]==qin[x] for x in D)
  assert all(fields.get(e,0)==internal.get(e,0) for e in internal)
  key=(tuple((x,qr[x]) for x in sorted(ext)),tuple(sorted((e,f) for e,f in fields.items() if not all(x in D for x in e) and f)))
  return qr,fields,dd,key
 qr,Er,dr,key=complete(q,Ein);assert dr==d
 k=sum(qr[x]!=0 for x in V if par(x)==1);kd=sum(q[x]!=0 for x in D if par(x)==1)+abs(Q);assert k==kd and k%2==1;assert L>=max(2*R+6,4*k)
 # A nonzero interior plaquette cycle changes the regional quantum word but not d.
 E2=dict(Ein);cc=[(0,0,0),(1,0,0),(1,1,0),(0,1,0)]
 for x,y in zip(cc,cc[1:]+cc[:1]):
  e=edge(x,y);E2[e]=E2.get(e,0)+3*sgn(x)
 q2,Ef2,d2,key2=complete(q,E2);assert d2==d and key2==key and E2!=Ein
 # Bell coherence between the two regional words and a retained ancilla survives.
 rho={(i,i,j,j):Fraction(1,2) for i in (0,1) for j in (0,1)}
 traced={(i,i,j,j):amp for (i,ai,j,aj),amp in rho.items() if [key,key2][i]==[key,key2][j]};assert traced==rho
 # A changed boundary internal edge gives distinct superselection and exterior data.
 E3=dict(Ein);e=edge((R,0,0),(R,1,0));E3[e]=E3.get(e,0)+1
 _,_,d3,key3=complete(q,E3);assert d3!=d and key3!=key and sum(d3.values())==Q
 results.append({'L':L,'regional_sites':len(D),'net_regional_charge':Q,'global_reference_B':k,'original_B':sum(q[x]!=0 for x in V if par(x)==1),'nonzero_boundary_divergences':sum(v!=0 for v in d.values()),'max_boundary_divergence':max(abs(v) for v in d.values()),'all_Gauss_equations_per_completion':len(V),'within_sector_offdiagonal_and_ancilla_preserved':True,'distinct_boundary_sector_exterior_orthogonality':True})
 guard()
result={'cases':results,'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'author_new_proof_code_results_read':False}
print(json.dumps(result,indent=2));assert result['cpu_seconds']<10 and result['peak_rss_bytes']<80*1024**2
(out/'PRE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
