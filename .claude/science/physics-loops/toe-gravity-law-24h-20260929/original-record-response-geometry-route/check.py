#!/usr/bin/env python3
"""Exact sparse corroboration; no prior builder imported, no asymptotic inference."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[k]='1'
import time, resource, json, hashlib, math
from pathlib import Path
from collections import defaultdict
from itertools import product,combinations
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,31))
# macOS address-space rlimit is unsuitable for Python mapped libraries; supervise RSS separately.
t0=time.monotonic(); c0=time.process_time()
def guard():
 assert time.monotonic()-t0<90
 assert not (runtime/'STOP_REQUESTED.json').exists()
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<120*1024*1024
D=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,r):return tuple(r*x for x in a)
def norm(a):return sum(map(abs,a))
def parity(a):return sum(a)%2
def nb(a):return [add(a,d) for d in D]
A2=sorted({add(d,e) for d in D for e in D if add(d,e)!=(0,0,0)})
def ballodd(r):return {x for x in product(range(-r,r+1),repeat=3) if norm(x)<=r and parity(x)}
assert len(ballodd(5))==146
slabs=[]
for R in (4,6,8,12,16,24):
 guard(); f={}
 for x in range(-R+1,R):
  if x%2:continue
  for z in range(-R+1,R):
   w=(R*R-x*x)**2*(R*R-z*z)**2
   if w:f[(x,-z,z)]=(-1 if (x//2+z)%2 else 1)*w
 def K(v):
  out=defaultdict(int)
  for h,a in v.items():
   for b in nb(h):out[b]+=a
  return {h:a for h,a in out.items() if a}
 K1=K(f); K2=K(K1)
 n0=sum(a*a for a in f.values()); n2=sum(a*a for a in K2.values())
 ratio=Fraction(R**4*n2,n0)
 assert ratio<=8192**2
 S={ (x,m-z,z) for x in range(-R-3,R+4) for z in range(-R-3,R+4) for m in range(-3,4) if (x+m)%2 }
 corner=(R+3,-R-1,R+3);assert corner in S;S.remove(corner)
 assert len(S)==(7*R+24)*(2*R+7)-1 and len(S)%2
 # Literal locally cancelled Hamiltonian: every negative Fa†Fa has blocked first hop;
 # all diagonal returns and every positive shared-b path are then enumerated.
 literal=defaultdict(int); blocked=0
 for h,amplitude in f.items():
  assert all(add(h,b) in S for b in ballodd(3))
  for rel in A2:
   a=add(h,rel)
   for b in nb(a):assert b in S;blocked+=1
  for b in nb(h):
   assert b in S
   literal[h]+=amplitude
   for a in nb(b):
    if a!=h:literal[a]+=amplitude
 literal={h:a for h,a in literal.items() if a}
 assert literal==K2
 slabs.append({'R':R,'k':len(S),'input_holes':len(f),'K2_holes':len(K2),'R4_Hnorm2_over_norm2':str(ratio),'R2_Hnorm_over_norm':math.sqrt(float(ratio)),'negative_first_hops_blocked':blocked})
# Exact physical charge/field words.
def defaultq(s):return 0 if parity(s) else 1
def pack(q,e):return tuple(sorted((s,v) for s,v in q.items() if v!=defaultq(s))),tuple(sorted((l,v) for l,v in e.items() if v))
def charge(w,s):return dict(w[0]).get(s,defaultq(s))
def edge(a,b):return (a,b)
def initial(S,h=(0,0,0)):
 assert len(S)%2 and h not in S
 q={h:0}; q.update({s:(-1 if i<(len(S)-1)//2 else 1) for i,s in enumerate(sorted(S))})
 defects={s:v-defaultq(s) for s,v in q.items()}; assert sum(defects.values())==0
 e=defaultdict(int); origin=(0,0,0)
 for target,v in defects.items():
  at=origin
  for axis in range(3):
   while at[axis]!=target[axis]:
    dd=[0,0,0];dd[axis]=1 if target[axis]>at[axis] else -1
    to=add(at,dd);aa,bb=(at,to) if not parity(at) else (to,at)
    e[(aa,bb)]+=(-v if at==aa else v);at=to
 return pack(q,e)
def hop(w,a,b,dag=False):
 q,e=dict(w[0]),dict(w[1]);qa=q.get(a,1);qb=q.get(b,0)
 if dag:
  if qa or not qb:return None
  q[a]=qb;q[b]=0;e[(a,b)]=e.get((a,b),0)+qb
 else:
  if not qa or qb:return None
  q[a]=0;q[b]=qa;e[(a,b)]=e.get((a,b),0)-qa
 return pack(q,e)
def two(w,a,b,da,c,d,dc):
 out=hop(w,a,b,da)
 return None if out is None else hop(out,c,d,dc)
def hole(w):
 hh=[s for s,q in w[0] if not parity(s) and not q];assert len(hh)==1;return hh[0]
def Bmask(w):return {s for s,q in w[0] if parity(s) and q}
def gauss(w):
 div=defaultdict(int)
 for (a,b),v in w[1]:div[a]+=v;div[b]-=v
 q=dict(w[0]);sites=set(div)|set(q)
 assert all(div[s]==q.get(s,defaultq(s))-defaultq(s) for s in sites)
def H(w):
 h=hole(w);out=defaultdict(int)
 def put(v,c):
  if v is not None:out[v]+=c
 for b in nb(h):
  for bp in nb(h):put(two(w,h,b,True,h,bp,False),1)
 for r in A2:
  a=add(h,r)
  for b in nb(a):
   for bp in nb(a):put(two(w,a,b,False,a,bp,True),-1)
  for b in set(nb(a))&set(nb(h)):
   put(two(w,h,b,True,a,b,False),1)
   put(two(w,a,b,False,h,b,True),-1)
 return {v:c for v,c in out.items() if c}
def dark(w):return set(nb(hole(w)))<=Bmask(w)
def groups(h):return [set(nb(add(h,mul(d,2))))-{add(h,d)} for d in D]
def exposed(w):return dark(w) and any(not(Bmask(w)&s) for s in groups(hole(w)))
def Phi(w,T=None):
 h=hole(w);S=Bmask(w)
 if T is not None:S=S&T
 return sum(max(-5,min(5,h[0]-b[0])) for b in S)
assert len(set.union(*groups((0,0,0))))==30 and all(len(g)==5 for g in groups((0,0,0)))
# Enlarged good set is NOT DHD invariant.
S=set(nb((0,0,0)))|{mul(d,3) for d in D if d!=(1,0,0)}|{(1,1,1),(11,0,0)}
w=initial(S);gauss(w);assert exposed(w)
target=two(w,(1,1,0),(2,1,0),False,(1,1,0),(1,1,1),True)
assert target is not None and H(w)[target]==-1 and dark(target) and not exposed(target)
gauss(target)
# Exposed selected rows: original fields/charges, no source-count cap.
vrows=[]
for S in (set(nb((0,0,0)))|{(11,0,0)},S):
 w=initial(S);h=hole(w);direction=next(d for d,g in zip(D,groups(h)) if not S&g)
 b=add(h,direction);c=add(h,mul(direction,2));v=two(w,h,b,True,c,b,False)
 assert v is not None and 2*len(set(nb(c))-Bmask(v))==10
 rev={r:a for r,a in H(v).items() if dark(r)}
 assert rev=={w:1}
 for r in H(v):gauss(r)
 vrows.append({'k':len(S),'all_reverse_words':len(H(v)),'dark_reverse_words':len(rev)})
# Fixed +x all-dark selected row, including both same-hole reshuffles and moving holes.
S=ballodd(3)|{(11,0,0)};w=initial(S);gauss(w)
h=hole(w);b=add(h,(1,0,0));c=add(h,(2,0,0));v=two(w,h,b,True,c,b,False)
rows=H(v);assert rows[w]==1
others={r:a for r,a in rows.items() if dark(r) and r!=w}
T={add(h,b) for b in ballodd(5)}
classes=defaultdict(int)
for r,a in others.items():
 gauss(r);assert Bmask(r)-T==S-T and len(Bmask(r)&T)==len(S&T)
 dh=tuple(x-y for x,y in zip(hole(r),h));assert 1<=dh[0]<=4 and norm(dh)<=4
 assert Phi(r,T)-Phi(w,T)>=6
 classes['same_selected_hole' if hole(r)==c else 'moving_hole']+=1
# Literal small Dicke bijection: hop moves each fixed-sign assignment once.
dicke=[]
for occupied in range(2,9):
 for minus in range(occupied+1):
  words=list(combinations(range(occupied),minus))
  # Swap one occupied site with the vacancy, retaining the sign at that particle.
  mapped={tuple(sorted((occupied if j==0 else j) for j in ww)) for ww in words}
  assert len(mapped)==len(words)
  dicke.append(len(words))
result={'slabs':slabs,'enlarged_good_failure':{'k':len(Bmask(w)) if False else 13,'coefficient':-1,'input_good':True,'output_good':False},'exposed_inverse_rows':vrows,'directed_row':{'k':45,'all_words':len(rows),'other_dark_words':len(others),'classes':dict(classes),'tube_B_sites':len(T)},'dicke_cases':len(dicke),'dicke_assignments':sum(dicke),'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
guard();(ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
