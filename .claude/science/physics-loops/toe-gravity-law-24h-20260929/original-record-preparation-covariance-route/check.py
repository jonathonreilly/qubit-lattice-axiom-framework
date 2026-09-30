#!/usr/bin/env python3
"""Literal actual spin-coefficient and grade-zero original-jump controls."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import time,resource,json,hashlib,math
from pathlib import Path
from collections import defaultdict,deque
from itertools import product
ROOT=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
resource.setrlimit(resource.RLIMIT_CPU,(30,31))
start=time.monotonic();cpu=time.process_time()
def guard():
 assert not (RUNTIME/'STOP_REQUESTED.json').exists()
 assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
 assert time.monotonic()-start<90
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<120*1024**2
D=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def length(a):return sum(map(abs,a))
def parity(a):return sum(a)%2
def neigh(a):return [add(a,d) for d in D]
A2={add(d,e) for d in D for e in D if add(d,e)!=(0,0,0)}
AA=sorted({(0,0,0)}|A2|{(4,0,0),(3,1,0)})
BB=sorted({b for a in AA for b in neigh(a)})
EDGES=[(a,b) for a in AA for b in neigh(a)]
NG={s:[] for s in AA+BB}
for a,b in EDGES:NG[a].append(b);NG[b].append(a)
GATE={a:{c for b in NG[a] for c in NG[b] if c!=a} for a in AA}
def dq(s):return 0 if parity(s) else 1
def pack(q,e):return tuple(sorted((s,v) for s,v in q.items() if v!=dq(s))),tuple(sorted((e0,v) for e0,v in e.items() if v))
def qval(w,s):return dict(w[0]).get(s,dq(s))
def initial(S,h=None,circulation=0,a_minus=False):
 m=(len(S)-(h is not None))//2
 assert 2*m==len(S)-(h is not None)
 q={s:(-1 if j<m else 1) for j,s in enumerate(sorted(S))}
 if h is not None:q[h]=0
 if a_minus and m:
  b=next(s for s in S if q[s]==-1);q[b]=1;q[(2,0,0)]=-1
 defects={s:v-dq(s) for s,v in q.items()};assert sum(defects.values())==0
 origin=(0,0,0);parent={origin:None};queue=deque([origin])
 while queue:
  at=queue.popleft()
  for to in NG[at]:
   if to not in parent:parent[to]=at;queue.append(to)
 e=defaultdict(int)
 for target,value in defects.items():
  at=target
  while at!=origin:
   old=parent[at];a,b=(old,at) if not parity(old) else (at,old)
   e[(a,b)]+=(-value if old==a else value);at=old
 cycle=((4,0,0),(3,0,0),(3,1,0),(4,1,0),(4,0,0))
 for old,to in zip(cycle,cycle[1:]):
  a,b=(old,to) if not parity(old) else (to,old)
  assert (a,b) in EDGES;e[(a,b)]+=circulation if old==a else -circulation
 return pack(q,e)
def gauss(w):
 div=defaultdict(int)
 for (a,b),value in w[1]:div[a]+=value;div[b]-=value
 for s in set(div)|set(dict(w[0])):assert div[s]==qval(w,s)-dq(s)
def hop(w,a,b,dag=False):
 q,e=dict(w[0]),dict(w[1]);qa=q.get(a,1);qb=q.get(b,0);ee=e.get((a,b),0)
 if dag:
  if qa or not qb:return None
  rate=ee*(ee+qb);q[a]=qb;q[b]=0;e[(a,b)]=ee+qb
 else:
  if not qa or qb:return None
  rate=ee*(ee-qa);q[a]=0;q[b]=qa;e[(a,b)]=ee-qa
 out=pack(q,e)
 # Exact derivative compatibility of the adjoint normalized-spin amplitude.
 reverse_e=dict(out[1]).get((a,b),0)
 reverse_rate=reverse_e*(reverse_e-qb) if dag else reverse_e*(reverse_e+qa)
 assert reverse_rate==rate
 return out,rate

def twice(w,first,second):
 a,b,dag=first;r=hop(w,a,b,dag)
 if r is None:return None
 mid,rate1=r;a,b,dag=second;r=hop(mid,a,b,dag)
 if r is None:return None
 out,rate2=r
 return out,-rate1-rate2 # coefficient of 2*K1 for this unsigned product

def gate(w,a):return all(qval(w,c)!=0 for c in GATE[a])
def d_a(w,a):
 qa=qval(w,a)
 if not qa:return 0
 E=dict(w[1]);return sum(E.get((a,b),0)*(E.get((a,b),0)-qa) for b in NG[a] if not qval(w,b))
def d_gate(w):return sum(d_a(w,a) for a in AA if gate(w,a))
def full_K1(w):
 out=defaultdict(int)
 def put(r,sign):
  if r is not None:out[r[0]]+=sign*r[1]
 # Literal compensation derivative, including the spin diagonal correction.
 for a in AA:
  if gate(w,a):
   for b in NG[a]:
    for c in NG[a]:put(twice(w,(a,b,False),(a,c,True)),1)
 out[w]+=2*d_gate(w)
 # Literal GLOBAL +F F†-F†F derivative on this finite complete-star graph.
 for a,b in EDGES:
  for c,d in EDGES:
   put(twice(w,(a,b,True),(c,d,False)),1)
   put(twice(w,(a,b,False),(c,d,True)),-1)
 return {v:c for v,c in out.items() if c}

def local_K1(w,h):
 out=defaultdict(int);out[w]+=2*d_gate(w)
 def put(r,sign):
  if r is not None:out[r[0]]+=sign*r[1]
 for b in NG[h]:
  for c in NG[h]:put(twice(w,(h,b,True),(h,c,False)),1)
 for a in GATE[h]:
  for b in NG[a]:
   for c in NG[a]:put(twice(w,(a,b,False),(a,c,True)),-1)
  for b in set(NG[a])&set(NG[h]):
   put(twice(w,(h,b,True),(a,b,False)),1)
   put(twice(w,(a,b,False),(h,b,True)),-1)
 return {v:c for v,c in out.items() if c}

def F(w,dag=False,center=None):
 out=defaultdict(int)
 for a,b in EDGES:
  if center is not None and a!=center:continue
  r=hop(w,a,b,dag)
  if r is not None:out[r[0]]+=1
 return dict(out)
def j(w,a,b,signs):
 if qval(w,a) or qval(w,b):return {}
 out={}
 for s in signs:
  q,e=dict(w[0]),dict(w[1]);q[a]=s;q[b]=-s;e[(a,b)]=e.get((a,b),0)+s
  out[pack(q,e)]=1
 return out
def compose(v,fn):
 out=defaultdict(int)
 for w,c in v.items():
  for w2,c2 in fn(w).items():out[w2]+=c*c2
 return {w:c for w,c in out.items() if c}
def diff(x,y):
 out=defaultdict(int,x)
 for w,c in y.items():out[w]-=c
 return {w:c for w,c in out.items() if c}
fixtures=[('W0_vacuum_circulation',initial(set(),circulation=2),None),
 ('W0_8',initial(set(neigh((0,0,0)))|{(5,0,0),(4,1,0)},circulation=3,a_minus=True),None),
 ('W1_1_bright',initial({(5,0,0)},h=(0,0,0),circulation=2),(0,0,0)),
 ('W1_7_dark',initial(set(neigh((0,0,0)))|{(5,0,0)},h=(0,0,0),circulation=4,a_minus=True),(0,0,0)),
 ('W1_13_dark',initial(set(neigh((0,0,0)))|{tuple(3*x for x in d) for d in D if d!=(1,0,0)}|{(1,1,1),(5,0,0)},h=(0,0,0),circulation=1),(0,0,0))]
rows=[];noise_rows=0;noise_words=0;minus_hole_noise=False
for name,w,h in fixtures:
 guard();gauss(w);full=full_K1(w)
 if h is None:
  expect={w:2*sum(d_a(w,a) for a in AA)};expect={w:c for w,c in expect.items() if c}
  assert full==expect
 else:assert full==local_K1(w,h)
 for v in full:gauss(v)
 rows.append({'name':name,'full_K1_words':len(full),'sum_abs_twice_K1':sum(map(abs,full.values())),'D_gate':d_gate(w),'nonzero_E_links':len(w[1])})
 for a in ((0,0,0),(2,0,0),(4,0,0)):
  for b in NG[a]:
   for signs in ((1,),(-1,),(1,-1)):
    jfun=lambda z:j(z,a,b,signs)
    glob=diff(compose(F(w),jfun),compose(jfun(w),lambda z:F(z)))
    loc=diff(compose(F(w,center=a),jfun),compose(jfun(w),lambda z:F(z,center=a)))
    assert glob==loc
    grade_minus2=diff(compose(jfun(w),lambda z:F(z,dag=True)),compose(F(w,dag=True),jfun))
    assert not grade_minus2
    for v in glob:
     gauss(v)
     assert all(bool(qval(v,aa))==bool(qval(w,aa)) for aa in AA)
     assert sum(bool(qval(v,bb)) for bb in BB)==sum(bool(qval(w,bb)) for bb in BB)+2
    if h==a and glob:minus_hole_noise=True
    noise_rows+=1;noise_words+=len(glob)
assert minus_hole_noise
caps=0
for p in range(13):
 C=2**(3*p+1)*math.factorial(p)
 for n in range(129):assert (1+4*n)**p<=C*2**n;caps+=1
out={'graph':{'A':len(AA),'B':len(BB),'edges':len(EDGES),'scope':'Finite connected union of complete cubic A stars, all 19 central A centers plus two farther centers. Full central W1 cancellation and nonzero distant gated diagonal are literal; not a thermodynamic or large-spin simulation.'},'spin_coefficients':rows,'noise_comparisons':noise_rows,'noise_output_words':noise_words,'actual_hole_sector_negative_noise_tested':minus_hole_noise,'field_majorant_cases':caps,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
guard();(ROOT/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
