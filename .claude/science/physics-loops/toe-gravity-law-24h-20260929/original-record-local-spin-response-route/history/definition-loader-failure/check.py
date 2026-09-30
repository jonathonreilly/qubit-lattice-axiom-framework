"""Compact capacity completion and exact original Delta dressing controls."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import itertools,time,resource,json,hashlib,gc
resource.setrlimit(resource.RLIMIT_CPU,(20,20));t0=time.process_time();here=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not any((rt/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
 assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
guard()
steps=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1));zero=(0,0,0)
add=lambda a,b:tuple(x+y for x,y in zip(a,b));par=lambda a:sum(a)%2;rad=lambda a:sum(abs(x) for x in a)
near=lambda a:[add(a,x) for x in steps]
edge=lambda a,b:(a,b) if par(a)==0 else (b,a)
def divergence(E):
 z=defaultdict(int)
 for (a,b),v in E.items():z[a]+=v;z[b]-=v
 return z
def tree(V,root):
 order=[root];pa={root:None}
 for a in order:
  for b in near(a):
   if b in V and b not in pa:pa[b]=a;order.append(b)
 assert len(order)==len(V)
 return order,pa
def flow(order,pa,need):
 sums={a:int(need.get(a,0)) for a in order};E={}
 for a in reversed(order[1:]):
  b=pa[a];E[edge(a,b)]=sums[a]*(1 if par(a)==0 else -1);sums[b]+=sums[a]
 assert sums[order[0]]==0
 return {e:v for e,v in E.items() if v}
def route(E,a,pa,v):
 while pa[a] is not None:
  b=pa[a];e=edge(a,b);E[e]=E.get(e,0)+(v if par(a)==0 else -v);a=b
completion=[]
cases=[(2,[],False,0),(2,[1],False,3),(2,[-1],False,17),(3,[1,1,1],False,3),(3,[1,1,-1],True,7)]
for R,signs,minusA,flux in cases:
 D={a for a in itertools.product(range(-R,R+1),repeat=3) if rad(a)<=R};boundary={a for a in D if rad(a)==R};q={a:1-par(a) for a in D};q[zero]=0
 if minusA:q[(1,1,0)]=-1
 bs=sorted(a for a in D if par(a))
 for a,v in zip(bs,signs):q[a]=v
 Q=sum(q[a]-(1-par(a)) for a in D);K=len(signs)+abs(Q);assert K>=1
 assert sum(abs(q[a]-(1-par(a))) for a in D)<=2*K
 order,pa=tree(D,(R,0,0));E={}
 for a in D:route(E,a,pa,q[a]-(1-par(a)))
 route(E,(0,R,0),pa,flux);E={e:v for e,v in E.items() if v}
 E2=dict(E);loop=[zero,(1,0,0),(1,1,0),(0,1,0)]
 for a,b in zip(loop,loop[1:]+loop[:1]):
  e=edge(a,b);E2[e]=E2.get(e,0)+(2 if par(a)==0 else -2)
 E2={e:v for e,v in E2.items() if v}
 F=max(1+sum(map(abs,E.values())),1+sum(map(abs,E2.values())))
 D0=2*K+2*(F-1);B=R+K+3;cube=set(itertools.product(range(-B,B+1),repeat=3));ex=cube-D
 eo,ep=tree(ex,(B,B,0));N=(2*B+1)**3;M=F+D0+N*(D0+K);S=3*K+2*F
 extB=sorted(a for a in ex if a[0]==B and par(a));assert len(extB)>=K
 def complete(internal):
  vi=divergence(internal);d={a:q[a]-(1-par(a))-vi[a] for a in D};assert all(d[a]==0 for a in D-boundary);assert sum(d.values())==Q;assert sum(map(abs,d.values()))<=D0
  ef=dict(internal);qf={a:(q[a] if a in D else 1-par(a)) for a in cube}
  for a in extB[:abs(Q)]:qf[a]=-1 if Q>0 else 1
  for a in boundary:
   b=min(b for b in near(a) if b in ex);ef[edge(a,b)]=(1 if par(a)==0 else -1)*d[a]
  vc=divergence(ef);need={a:qf[a]-(1-par(a))-vc[a] for a in ex};assert sum(need.values())==0;assert sum(map(abs,need.values()))<=D0+K
  et=flow(eo,ep,need);assert max(map(abs,et.values()),default=0)<=Fraction(D0+K,2);ef.update(et);ef={e:v for e,v in ef.items() if v};vf=divergence(ef)
  assert all(vf[a]==qf[a]-(1-par(a)) for a in cube)
  assert sum(bool(qf[a]) for a in cube if par(a))==K and K%2==1
  assert max(map(abs,ef.values()),default=0)<=D0+K<=S
  qt=1+sum(map(abs,ef.values()));assert qt<=M
  for L in [max(28,4*K,2*B+4),max(28,4*K,2*B+4)+6]:
   assert L%2==0;ww={tuple(t%L for t in a) for a in cube};assert len(ww)==len(cube)
  outside=(tuple((a,qf[a]) for a in sorted(ex) if qf[a]!=(1-par(a))),tuple(sorted((e,v) for e,v in ef.items() if not all(a in D for a in e))))
  return d,outside,qt,max(map(abs,ef.values()),default=0)
 a=complete(E);b=complete(E2);assert a[:2]==b[:2]
 completion.append({'R':R,'K':K,'F':F,'S_sufficient':S,'shell_cube_radius':B,'tree_vertices':len(ex),'boundary_l1':sum(map(abs,a[0].values())),'bound_D0':D0,'max_completed_field':max(a[3],b[3]),'max_reference_Q':max(a[2],b[2]),'bound_reference_Q':M,'same_boundary_block_completion_preserves_offdiagonal':True})
 del cube,ex,eo,ep;gc.collect();guard()
# Exact geometric support sets; all site/link factors retained in each d_e.
d2={add(a,b) for a in steps for b in steps}-{zero}
def delta_cells(a,b):return {('v',x) for x in {a,b}|{add(a,v) for v in d2}}|{('e',edge(a,b))}
hsites={zero}|d2|{b for a in {zero}|d2 for b in near(a)};hcells={('v',a) for a in hsites}|{('e',edge(a,b)) for a in {zero}|d2 for b in near(a)}
jcells={('v',zero),('v',(1,0,0)),('e',(zero,(1,0,0)))}
terms=[delta_cells(a,b) for a in itertools.product(range(-5,6),repeat=3) if par(a)==0 and rad(a)<=5 for b in near(a)]
def halo(cells):return cells|set().union(*(t for t in terms if t&cells))
def cell_radius(cells):return max(rad(x) for tag,c in cells for x in ([c] if tag=='v' else c))
hh,jj=halo(hcells),halo(jcells);assert cell_radius(hh)<=7 and cell_radius(jj)<=5
geometry={'raw_H_access_radius':cell_radius(hcells),'dressed_H_access_radius':cell_radius(hh),'dressed_jump_access_radius':cell_radius(jj),'dressed_H_site_factors':sum(t=='v' for t,x in hh),'dressed_H_link_factors':sum(t=='e' for t,x in hh),'dressed_jump_site_factors':sum(t=='v' for t,x in jj),'dressed_jump_link_factors':sum(t=='e' for t,x in jj)}
# New exact Delta phase implementation over earlier checked elementary source words.
src=here.parent/'independent-fast-propagation-check/check.py';ns={'__file__':str(src)};exec(compile(src.read_text().split('\nfull=Preparation(8)')[0],str(src),'exec'),ns);resource.setrlimit(resource.RLIMIT_CPU,(20,20))
Preparation,relative_ops=ns['Preparation'],ns['relative_ops']
core=Preparation();core.move(zero,(0,0,1),'out');far=Preparation();far.move(zero,(0,0,1),'out');far.birth_pair((10,0,0))
def circulation(p,c,v):
 path=[c,add(c,(1,0,0)),add(c,(1,1,0)),add(c,(0,1,0))]
 for a,b in zip(path,path[1:]+path[:1]):
  e=edge(a,b);p.E[e]=p.E.get(e,0)+(v if par(a)==0 else -v)
for p in [core,far]:circulation(p,zero,2)
circulation(far,(14,0,0),6)
def delta(p,st,S):
 q=dict(p.q);q.update(dict(st[0]));E=dict(p.E);E.update({(a,b):v for a,b,v in st[1]});ans=Fraction()
 qc=lambda a:q.get(a,1-par(a))
 for (a,b),v in E.items():
  if not v or not qc(a) or qc(b) or not all(qc(add(a,z)) for z in d2):continue
  sig=-qc(a);w2=Fraction(S*(S+1)-v*(v+sig),S*(S+1)) if abs(v)<=S and abs(v+sig)<=S else Fraction(0)
  ans+=1-w2
 return ans
phase=[];empty=((),())
for S in [6,9]:
 data=[]
 for p in [core,far]:
  move,G,gauss,walk,holes=relative_ops(p)
  def fa(vec,a,kind):
   out=defaultdict(int)
   for st,c in vec.items():
    for b in near(a):
     z=move(st,a,b,kind)
     if z is not None:out[z[0]]+=c
   return {s:c for s,c in out.items() if c}
  out=defaultdict(int)
  def inc(v,sg=1):
   for st,c in v.items():out[st]+=sg*c
  inc(fa(fa({empty:1},zero,'in'),zero,'out'))
  for z in d2:
   inc(fa(fa({empty:1},z,'out'),z,'in'),-1);inc(fa(fa({empty:1},zero,'in'),z,'out'));inc(fa(fa({empty:1},z,'out'),zero,'in'),-1)
  out={s:c for s,c in out.items() if c};d0=delta(p,empty,S);hp={s:delta(p,s,S)-d0 for s in out};jp={}
  for b in near(zero):
   for sg in (-1,1):
    z=move(empty,zero,b,'birth',sg)
    if z is not None:jp[(b,sg,z[0])]=delta(p,z[0],S)-d0
  assert all(gauss(s) for s in out);assert all(gauss(z) for b,sg,z in jp);data.append((hp,jp,d0))
 assert data[0][:2]==data[1][:2];assert data[0][2]!=data[1][2];assert any(v for v in data[0][1].values())
 phase.append({'S':S,'H_original_word_phase_differences':len(data[0][0]),'original_resolved_birth_phase_differences':len(data[0][1]),'coherent_intra_edge_sign_phases_retained':True,'nonzero_birth_phase_count':sum(bool(v) for v in data[0][1].values()),'core_Delta':str(data[0][2]),'far_Delta':str(data[1][2]),'all_near_far_exact_phase_differences_equal':True})
result={'completion':completion,'geometry':geometry,'actual_Delta_phase':phase,'reused_elementary_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};print(json.dumps(result,indent=2));assert result['cpu_seconds']<20 and result['peak_rss_bytes']<120*1024**2;guard();(here/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
