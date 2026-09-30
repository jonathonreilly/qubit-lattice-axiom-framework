#!/usr/bin/env python3
"""Literal odd-torus removal normalization; exact scalar mean/Dirichlet control."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import time,resource,itertools,json,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
start=time.monotonic();cpu=time.process_time();p=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
L=9;V=L**3
coords=[(x,y,z) for z in range(L) for y in range(L) for x in range(L)]
def id_(v):return (v[0]%L)+L*(v[1]%L)+L*L*(v[2]%L)
def sh(i,v):return id_(tuple(a+b for a,b in zip(coords[i],v)))
def dif(a,b):return tuple((x-y)%L for x,y in zip(coords[a],coords[b]))
def canonical(S):return min(tuple(sorted(id_(dif(x,y)) for x in S)) for y in S)
def tr(S,t):return tuple(sorted(sh(x,coords[t]) for x in S))
def norm(z):return int(z.real)**2+int(z.imag)**2
unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
D=[tuple(2*a for a in e) for e in unit];planes=[]
for i in range(3):
 for j in range(i+1,3):
  plus=len(D);D.append(tuple(unit[i][k]+unit[j][k] for k in range(3)))
  minus=len(D);D.append(tuple(unit[i][k]-unit[j][k] for k in range(3)))
  planes.append((i,j,plus,minus))
edge_map={tuple(sorted((x,sh(x,d)))):(k,x) for x in range(V) for k,d in enumerate(D)}
assert len(edge_map)==9*V
soft=[[1,-1,0,0,0,0,0,0,0],[1,1,-2,0,0,0,0,0,0]]
for i,j,plus,minus in planes:
 v=[0]*9;v[plus]=-1;v[minus]=1;soft.append(v)
M=[]
for a in range(5):
 for b in range(a,5):
  M.append([[soft[a][i]*soft[b][j]+(soft[b][i]*soft[a][j] if a!=b else 0) for j in range(9)] for i in range(9)])
# Select actual orientation probes spanning all15 internal tensors.
echelon=[];chosen=[]
for d,e in itertools.product(range(9),repeat=2):
 row=[Q(m[d][e]) for m in M]
 for pivot,v in echelon:
  c=row[pivot];row=[x-c*y for x,y in zip(row,v)]
 nz=next((i for i,x in enumerate(row) if x),None)
 if nz is not None:
  c=row[nz];row=[x/c for x in row];echelon.append((nz,row));chosen.append((d,e))
 if len(chosen)==15:break
assert len(chosen)==15
far=id_((4,4,4));seeds=[]
for d,e in chosen:
 seeds.append(canonical((0,sh(0,D[e]),far,sh(far,D[d]))))
extra=[((0,0,0),(2,0,0),(4,0,0),(6,0,0)),((0,0,0),(2,0,0),(1,1,0),(1,-1,0)),((0,0,0),(2,0,0),(1,1,0),(4,4,4)),((0,0,0),(1,0,0),(0,1,0),(0,0,1)),((0,0,0),(3,0,0),(0,3,0),(0,0,3))]
seeds+= [canonical(tuple(id_(v) for v in S)) for S in extra]
seeds=list(dict.fromkeys(seeds)); amps={S:complex(i%5-2,(2*i)%7-3) for i,S in enumerate(seeds)}
amps={S:a for S,a in amps.items() if a}
state={}
for S,a in amps.items():
 orbit={tr(S,t) for t in range(V)};assert len(orbit)==V
 for T in orbit:assert T not in state;state[T]=a
# Physical bare operator application, then physical gradient and S row norms.
Dpsi={}
for S,a in state.items():
 for pair in itertools.combinations(S,2):
  if pair not in edge_map:continue
  d,x=edge_map[pair];eta=tuple(y for y in S if y not in pair)
  key=(d,x,eta);assert key not in Dpsi;Dpsi[key]=a

def grad_form(only_graph):
 selected={k:a for k,a in Dpsi.items() if not only_graph or k[2] in edge_map}
 val=6*sum(norm(a) for a in selected.values())
 for (d,x,eta),a in selected.items():
  for u in unit:val-=2*int((a.conjugate()*selected.get((d,sh(x,u),eta),0j)).real)
 return val
# Literal centered word inventory, independent of the relative-array evaluation.
words={}
for x in range(V):
 for i,u in enumerate(unit):
  edge=tuple(sorted((sh(x,u),sh(x,tuple(-v for v in u)))))
  words.setdefault(edge,[]).append(('a',x,0,0,1))
 for plane,(i,j,plus,minus) in enumerate(planes):
  for word,(s,t) in enumerate(itertools.product((-1,1),repeat=2)):
   edge=tuple(sorted((sh(x,tuple(s*v for v in unit[i])),sh(x,tuple(t*v for v in unit[j])))))
   words.setdefault(edge,[]).append(('p',x,plane,word,s*t))
ax={};pv={}
for (d,x,eta),a in Dpsi.items():
 edge=tuple(sorted((x,sh(x,D[d]))))
 for kind,center,plane,word,sign in words[edge]:
  if kind=='a':ax[(center,eta)]=ax.get((center,eta),0j)+a
  else:
   key=(center,plane,eta);pv.setdefault(key,[0j]*4);pv[key][word]+=sign*a

def s_form(only_graph):
 a=sum(norm(v) for (x,eta),v in ax.items() if not only_graph or eta in edge_map)
 b=Q(0)
 for (x,plane,eta),v in pv.items():
  if only_graph and eta not in edge_map:continue
  b+=sum(norm(z) for z in v)-Q(norm(sum(v)),4)
 return Q(2*a,3)+b
# Actual graph-residual removal fields f=sqrt2 F in the zero-momentum fiber.
f=[[[0j]*V for d in range(9)] for e in range(9)]
for e,de in enumerate(D):
 eta=(0,sh(0,de))
 for d,dd in enumerate(D):
  for r in range(V):
   S=set(eta)|{r,sh(r,dd)}
   if len(S)==4:f[e][d][r]=state.get(tuple(sorted(S)),0j)
assert all(f[e][d][0]==0 for d,e in itertools.product(range(9),repeat=2))
for e,d,r in itertools.product(range(9),range(9),range(V)):
 assert f[e][d][r]==f[d][e][id_(tuple(-x for x in coords[r]))]
grad_rel=sum(norm(f[e][d][sh(r,u)]-f[e][d][r]) for e,d,r in itertools.product(range(9),range(9),range(V)) for u in unit)
assert Q(grad_form(True),V)==grad_rel
assert grad_form(False)>=grad_form(True)
# Relative centered rows from endpoint coordinates at each center.
srel=Q(0)
for e in range(9):
 for r in range(V):
  axial=[f[e][i][sh(r,tuple(-v for v in unit[i]))] for i in range(3)]
  srel+=Q(2*norm(sum(axial)),3)
  for i,j,plus,minus in planes:
   v=[]
   for s,t in itertools.product((-1,1),repeat=2):
    x=sh(r,tuple(s*a for a in unit[i]));y=sh(r,tuple(t*a for a in unit[j]))
    d,anchor=edge_map[tuple(sorted((x,y)))];v.append(s*t*f[e][d][anchor])
   srel+=sum(norm(z) for z in v)-Q(norm(sum(v)),4)
assert s_form(True)/V==srel and s_form(False)>=s_form(True)
# Exact high-mean bound from the actual constant S projection.
high=Q(0)
for e in range(9):
 totals=[sum(f[e][d]) for d in range(9)]
 high+=Q(norm(sum(totals[:3])),3*V*V)
 for i,j,plus,minus in planes:high+=Q(norm(totals[plus]+totals[minus]),2*V*V)
assert srel>=2*V*high
# All15 frame overlaps: chi=2M on physical occupations, f=sqrt2 F.
def distance(x,y):return max(min((a-b)%L,(b-a)%L) for a,b in zip(coords[x],coords[y]))
def separated(e1,e2):return all(distance(x,y)>2 for x in e1 for y in e2)
physical=[0j]*15
for S,a in amps.items():
 selected=[]
 for pair in itertools.combinations(S,2):
  if pair not in edge_map:continue
  other=tuple(x for x in S if x not in pair)
  if other in edge_map and separated(pair,other):selected.append(pair)
 if selected:
  assert len(selected)==2
  d,x=edge_map[selected[0]];e,y=edge_map[selected[1]]
  for k,m in enumerate(M):physical[k]+=2*m[d][e]*a
relative=[0j]*15
for e,de in enumerate(D):
 eta=(0,sh(0,de))
 for d,dd in enumerate(D):
  for r in range(V):
   a=f[e][d][r]
   if not a or not separated(eta,(r,sh(r,dd))):continue
   for k,m in enumerate(M):relative[k]+=m[d][e]*a
assert physical==relative and any(physical)

# Exact scalar torus pseudoinverse and finite Dirichlet formula at L=3.
def inverse(A):
 n=len(A);a=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  pivot=next(j for j in range(i,n) if a[j][i]);a[i],a[pivot]=a[pivot],a[i]
  c=a[i][i];a[i]=[x/c for x in a[i]]
  for j in range(n):
   if j!=i and a[j][i]:
    c=a[j][i];a[j]=[x-c*y for x,y in zip(a[j],a[i])]
 return [row[n:] for row in a]
ls=3;vs=27;cc=[(x,y,z) for z in range(ls) for y in range(ls) for x in range(ls)]
def ii(v):return v[0]%ls+ls*(v[1]%ls)+ls*ls*(v[2]%ls)
Lap=[[Q(0) for j in range(vs)] for i in range(vs)]
for i,x in enumerate(cc):
 Lap[i][i]=6
 for u in unit:
  for s in (-1,1):Lap[i][ii(tuple(x[k]+s*u[k] for k in range(3))) ]-=1
aug=[[Lap[i][j]+Q(1,vs) for j in range(vs)] for i in range(vs)]
Inv=inverse(aug);G=[[Inv[i][j]-Q(1,vs) for j in range(vs)] for i in range(vs)]
Dir=inverse([row[1:] for row in Lap[1:]])
for i in range(1,vs):
 for j in range(1,vs):assert Dir[i-1][j-1]==G[i][j]-G[i][0]-G[0][j]+G[0][0]
wrong=G[1][1]-G[1][0]*G[0][1]/G[0][0]
assert wrong!=Dir[0][0]
out={'scope':'Exact finite identities supporting the analytic threshold limit; no full spectrum or T0 computation',
 'L':L,'orbit_profiles':len(amps),'physical_occupation_words':len(state),'relative_field_entries':81*V,'common_pins':81,'exchange_checks':81*V,
 'physical_graph_gradient_divV':str(Q(grad_form(True),V)),'relative_gradient':grad_rel,'physical_graph_S_divV':str(s_form(True)/V),'relative_S':str(srel),'high_mean_lower':str(2*V*high),'all15_complex_frame_overlaps_exact':True,
 'scalar_dirichlet_entries_checked':26**2,'scalar_dirichlet_11':str(Dir[0][0]),'incorrect_transient_style_11':str(wrong),
 'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert out['peak_rss_bytes']<150*1024*1024
(p/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
