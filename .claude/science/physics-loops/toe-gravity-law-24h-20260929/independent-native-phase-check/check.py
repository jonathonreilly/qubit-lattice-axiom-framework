#!/usr/bin/env python3
"""Independent exact one-site matrix multiplication and Pauli partial traces."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']: os.environ[k]='1'
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import time,json,resource,datetime
start=time.monotonic();cpu=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(30,31))
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
assert not (rt/'STOP_REQUESTED.json').exists()
I=(1,0,0,1);b=(0,1,0,0);bd=(0,0,1,0);n=(0,0,0,1)
e=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def tr(m,p):
 if p=='I':return (F(m[0]+m[3],2),F(0))
 if p=='X':return (F(m[1]+m[2],2),F(0))
 if p=='Y':return (F(0),F(m[1]-m[2],2))
 return (F(m[0]-m[3],2),F(0))
def cmul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
G=[tuple(2*s*x for x in v) for v in e for s in [-1,1]]
G += [add(tuple(s*x for x in e[i]),tuple(t*x for x in e[j])) for i,j in combinations(range(3),2) for s,t in product([-1,1],repeat=2)]
offs=[(0,0,0)]+e+list(map(neg,e))+G
axis=[(v,neg(v)) for v in e]
channels=[(F(1,2),[(axis[0],1),(axis[1],-1)],'E'),(F(1,6),[(axis[0],1),(axis[1],1),(axis[2],-2)],'E')]
for i,j in combinations(range(3),2):channels.append((F(1,4),[((tuple(s*x for x in e[i]),tuple(t*x for x in e[j])),s*t) for s,t in product([-1,1],repeat=2)],'T'))
left=[(-1,0,0),(-2,0,0)];right=[(2,0,0),(3,0,0)];targets=[(a,b) for a in left for b in right]
centers=sorted({add(t,neg(o)) for pair in targets for t in pair for o in offs})
ans={};terms=0
# Matrices at each site are actually multiplied in operator order, independently
# of the author's endpoint-case projector expansion.
def term(coef,param,word):
 global terms
 terms+=1;mats={}
 for site,m in word:mats[site]=mul(mats.get(site,I),m)
 for idx,(a,bsite) in enumerate(targets):
  if a not in mats or bsite not in mats:continue
  outside=(F(1),F(0))
  for site,m in mats.items():
   if site not in (a,bsite):outside=cmul(outside,tr(m,'I'))
  if outside==(0,0):continue
  for pa,pb in product('XYZ',repeat=2):
   value=cmul(cmul(outside,tr(mats[a],pa)),tr(mats[bsite],pb));value=tuple(coef*x for x in value)
   key=(idx,param,pa,pb);old=ans.get(key,(F(0),F(0)));ans[key]=tuple(x+y for x,y in zip(old,value))
for x in centers:
 term(F(1),'mu',[(x,n)]);term(F(-1),'nu',[(x,n)])
 for d,f in combinations(G,2):term(F(1),'mu',[(x,n),(add(x,d),n),(add(x,f),n)])
 for weight,words,kind in channels:
  for (a,ca),(bb,cb) in product(words,repeat=2):
   def pw(x1,x2):return[(add(x1,a[0]),bd),(add(x1,a[1]),bd),(add(x2,bb[0]),b),(add(x2,bb[1]),b)]
   term((-2 if kind=='E' else -1)*weight*ca*cb,'mu',pw(x,x))
   for ek in e:
    y=add(x,ek)
    for x1,x2,sg in [(x,x,1),(y,y,1),(x,y,-1),(y,x,-1)]:term(sg*weight*ca*cb,'tau',pw(x1,x2))
nonzero={str(k):[str(x) for x in v] for k,v in ans.items() if v!=(0,0)}
expected={(1,'mu','Z','Z'):(F(1,8),F(0)),(2,'mu','Z','Z'):(F(1,8),F(0))}
assert {k:v for k,v in ans.items() if v!=(0,0)}==expected,nonzero
# q=-Z/2, so two off-diagonal terms give derivative -(2/4)*(mu/8).
derivative=-sum(v[0]/4 for v in expected.values());assert derivative==F(-1,16)
A=24**4*25*28*31*34//24;B=24**4*1*4*7*10//24;D=24**3*4*7*10*3//6
assert (A,B,D)==(10199347200,3870720,1935360)
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'centers':len(centers),'literal_terms':terms,'nonzero_cross_Pauli_coefficients':nonzero,'negative_derivative_per_mu':str(derivative),'ABC_integer_constants':[A,B,D],'checks':'all36 Pauli entries for each of mu,tau,nu exact; actual ordered 2x2 site-matrix contraction; infinite lattice geometry','cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
