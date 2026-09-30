#!/usr/bin/env python3
"""Independent sparse geometry/algebra controls; no author imports."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
import time,resource,json,hashlib,signal
started=time.monotonic(); cpu0=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(30,31));signal.alarm(60)
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert not (runtime/'STOP_REQUESTED.json').exists()
root=Path(__file__).resolve().parent
zero=(0,0,0);axes=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(s,a):return tuple(s*x for x in a)
pairs=[(neg(e),e) for e in axes]
for i,j in combinations(range(3),2):
 for s,t in product((-1,1),repeat=2):pairs.append((scale(s,axes[i]),scale(t,axes[j])))
Delta=sorted({sub(v,u) for u,v in pairs}|{sub(u,v) for u,v in pairs});assert len(Delta)==18
assert [sum(abs(d[j]) for d in Delta) for j in range(3)]==[12]*3
counts=defaultdict(F);pin_columns=0;representations=0;path_controls=0
for d in Delta:
 reps=[]
 for typ,(u,v) in enumerate(pairs):
  for first,second in [(u,v),(v,u)]:
   if sub(second,first)==d:reps.append((typ,neg(first)))
 assert len(reps)==(1 if max(map(abs,d))==2 else 2)
 representations+=len(reps)
 for e in Delta:
  if e==d:continue
  steps=[]
  for j in range(3):
   steps += [scale(1 if e[j]>0 else -1,axes[j])]*abs(e[j])
  paths=sorted(set([(steps[0],steps[1]),(steps[1],steps[0])]))
  for typ,c in reps:
   for s,t in paths:
    assert add(s,t)==e
    for step in (s,t):counts[(typ,next(j for j,x in enumerate(step) if x))]+=F(1,len(reps)*len(paths))
    u,v=pairs[typ];p0=(add(c,u),add(c,v));p2=(add(add(c,e),u),add(add(c,e),v))
    positions=sorted(set(p0+p2+(e,)));idx={x:i for i,x in enumerate(positions)}
    assert set(p0)=={zero,d};assert e in p2
    for word in range(1<<len(positions)):
     def apply(pair):
      bits=(1<<idx[pair[0]])|(1<<idx[pair[1]])
      return word^bits if word&bits==bits else None
     a,b=apply(p0),apply(p2)
     projected_a=a is not None and bool(a&(1<<idx[e]))
     projected_b=b is not None and bool(b&(1<<idx[e]))
     triple=all(word&(1<<idx[x]) for x in [zero,d,e])
     assert projected_a==triple and not projected_b
     pin_columns+=1
    path_controls+=1
assert max(counts.values())==24
for typ,(u,v) in enumerate(pairs):
 d=sub(v,u)
 for j in range(3):assert counts[(typ,j)]==F(2 if typ<3 else 1)*(12-abs(d[j]))
# Exact vacuum Gram Laurent polynomials for rescaled five channels.
channels=[[(pairs[0],1),(pairs[1],-1)],[(pairs[0],1),(pairs[1],1),(pairs[2],-2)]]
for i,j in combinations(range(3),2):
 channels.append([((scale(s,axes[i]),scale(t,axes[j])),s*t) for s,t in product((-1,1),repeat=2)])
poly_count=0
for ia,A in enumerate(channels):
 for ib,B in enumerate(channels):
  poly=defaultdict(int)
  for (u,v),ca in A:
   for (w,z),cb in B:
    for shift in {sub(u,w),sub(u,z)}:
     if {add(shift,w),add(shift,z)}=={u,v}:poly[shift]+=ca*cb
  poly={k:v for k,v in poly.items() if v}
  want={}
  if ia==ib:
   want={zero:2 if ia==0 else 6 if ia==1 else 4}
   if ia>=2:
    i,j=list(combinations(range(3),2))[ia-2]
    want.update({add(scale(s,axes[i]),scale(t,axes[j])):1 for s,t in product((-1,1),repeat=2)})
  assert poly==want;poly_count+=1
# Literal hard-core commutators on 4 physical qubits, all 36 pair choices.
primitive=list(combinations(range(4),2));ccr_columns=0
for A in primitive:
 for B in primitive:
  for word in range(16):
   def act(w,p,create=False):
    if w is None:return None
    mask=sum(1<<j for j in p)
    if (w&mask)==(0 if create else mask):return w^mask
    return None
   got=defaultdict(int)
   out=act(act(word,B,True),A)
   if out is not None:got[out]+=1
   out=act(act(word,A),B,True)
   if out is not None:got[out]-=1
   got={w:c for w,c in got.items() if c}
   if A==B:
    coeff=1-sum(bool(word&(1<<j)) for j in A);want={word:coeff} if coeff else {}
   elif len(set(A)&set(B))==1:
    shared=next(iter(set(A)&set(B)));old=next(iter(set(A)-set(B)));new=next(iter(set(B)-set(A)))
    out=act(act(word,(old,)),(new,),True)
    want={} if out is None else {out:1-2*bool(word&(1<<shared))}
   else:want={}
   assert got==want;ccr_columns+=1
# Graph inequality stronger than the lattice specialization, all labelled n<=6.
graphs=0
for n in range(1,7):
 edges=list(combinations(range(n),2))
 for mask in range(1<<len(edges)):
  nbr=[set() for _ in range(n)]
  for k,(i,j) in enumerate(edges):
   if mask>>k&1:nbr[i].add(j);nbr[j].add(i)
  degrees=list(map(len,nbr));D=sum((m-1)*(m-2)//2 for m in degrees);T=sum(m*(m-1)//2 for m in degrees)
  O=sum(not(len(nbr[i])==1 and len(nbr[next(iter(nbr[i]))])==1) for i in range(n))
  assert O<=D+3*T and (n-O)%2==0
  graphs+=1
assert F(256,3)<324
out={'pin_path_controls':path_controls,'pin_basis_columns':pin_columns,'bare_representations':representations,'exact_gradient_multiplicities':{str(k):str(v) for k,v in counts.items()},'max_multiplicity':str(max(counts.values())),'vacuum_Gram_polynomials':poly_count,'literal_CCR_columns':ccr_columns,'arbitrary_graphs':graphs,'five_channel_norm_error_coefficient':'256/3 (independent conservative bound)','author_code_imported':False,'wall_seconds':time.monotonic()-started,'cpu_seconds':time.process_time()-cpu0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'pre_sha256':hashlib.sha256((root/'PRE.md').read_bytes()).hexdigest()}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='exact_gradient_multiplicities'}))
