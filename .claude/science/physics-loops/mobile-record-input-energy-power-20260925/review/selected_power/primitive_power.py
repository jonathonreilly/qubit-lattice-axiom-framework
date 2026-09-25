#!/usr/bin/env python3
"""Fresh exact local-word calculation of selected adjoint-dissipator H4 power.

No imported builder. Integers are used throughout; initial vectors omit a
common 1/sqrt(2), restored analytically in the Laurent coefficients below.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import product
import hashlib,json,sys,time
from pathlib import Path

HERE=Path(__file__).resolve().parent
SIDE=int(sys.argv[1]) if len(sys.argv)>1 else 0
TAG=sys.argv[2] if len(sys.argv)>2 else ('infinite' if not SIDE else 'L'+str(SIDE))

def coord(v):return tuple(x%SIDE for x in v) if SIDE else tuple(v)
def is_a(v):return sum(v)%2==0
def nbr(v):
 for axis in range(3):
  for sign in (-1,1):
   w=list(v);w[axis]+=sign;yield coord(w)
def edge(a,b):
 assert is_a(a) and not is_a(b)
 return a,b
def charge(m,v):return dict(m).get(v,1 if is_a(v) else 0)
def setq(m,changes):
 out=dict(m)
 for v,q in changes.items():
  if q==(1 if is_a(v) else 0):out.pop(v,None)
  else:out[v]=q
 return tuple(sorted(out.items()))
def fk(d):return tuple(sorted((e,n) for e,n in d.items() if n))
def fadd(*parts):
 d=Counter()
 for part in parts:
  for e,n in part:d[e]+=n
 return fk(d)
def neg(flow):return tuple((e,-n) for e,n in flow)
def shift(flow,e,n):return fadd(flow,((e,n),))
def wave(rows):
 out=defaultdict(Counter)
 for m,f,n in rows:out[m][f]+=n
 return {m:Counter({f:n for f,n in terms.items() if n}) for m,terms in out.items() if any(terms.values())}
def rows(w):
 for m,terms in w.items():
  for f,n in terms.items():yield m,f,n
def outward(w,a):
 out=[]
 for m,f,n in rows(w):
  q=charge(m,a)
  if not q:continue
  for b in nbr(a):
   if charge(m,b):continue
   out.append((setq(m,{a:0,b:q}),shift(f,edge(a,b),-q),n))
 return wave(out)
def inward(w,a):
 out=[]
 for m,f,n in rows(w):
  if charge(m,a):continue
  for b in nbr(a):
   q=charge(m,b)
   if not q:continue
   out.append((setq(m,{a:q,b:0}),shift(f,edge(a,b),q),n))
 return wave(out)
def birth(w,a,b,sigma):
 out=[]
 for m,f,n in rows(w):
  if charge(m,a) or charge(m,b):continue
  out.append((setq(m,{a:sigma,b:-sigma}),shift(f,edge(a,b),sigma),n))
 return wave(out)
def unbirth(w,a,b,sigma):
 out=[]
 for m,f,n in rows(w):
  if charge(m,a)!=sigma or charge(m,b)!=-sigma:continue
  out.append((setq(m,{a:0,b:0}),shift(f,edge(a,b),-sigma),n))
 return wave(out)
def selected(w,sigma):return birth(outward(w,A),A,B,sigma)
def selected_adj(w,sigma):return inward(unbirth(w,A,B,sigma),A)
def pairhop(w,pair):return outward(outward(w,pair[0]),pair[1])
def inner(left,right):
 out=Counter()
 for m,ls in left.items():
  for lf,ln in ls.items():
   for rf,rn in right.get(m,{}).items():out[fadd(rf,neg(lf))]+=ln*rn
 return Counter({f:n for f,n in out.items() if n})
def sum_poly(target,p,scale=1):
 for f,n in p.items():target[f]+=scale*n
def adj(p):return Counter({neg(f):n for f,n in p.items()})
def divergence(f):
 d=Counter()
 for (a,b),n in f:d[a]+=n;d[b]-=n
 return {x:n for x,n in d.items() if n}
def winding(f):
 out=[0,0,0]
 for (a,b),n in f:
  differences=[b[i]-a[i] for i in range(3)]
  if SIDE:
   differences=[d-SIDE if d>SIDE//2 else d+SIDE if d<-SIDE//2 else d for d in differences]
  assert sum(abs(d) for d in differences)==1
  for i,d in enumerate(differences):out[i]+=n*d
 return tuple(out)
def serialize(p):
 return [dict(flow=[dict(a=a,b=b,shift=n) for (a,b),n in f],coefficient=c) for f,c in sorted(p.items()) if c]
def quadratic4(p):
 out=Counter()
 for f,c in p.items():
  if winding(f)!=(0,0,0):continue
  for x,n in f:
   for y,m in f:out[x,y]-=c*n*m
 return Counter({ij:n for ij,n in out.items() if n})
def diag_flat(m,pair):
 u,v=pair
 nu={b for b in nbr(u) if not charge(m,b)}
 nv={b for b in nbr(v) if not charge(m,b)}
 r=len(nu&nv)
 return len(nu)*len(nv)-r+(r*(r-1) if charge(m,u)==charge(m,v) else 0)

A,D,H,C,E,B,V1,V2,V3=map(coord,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)])
base=setq((),{D:-1,H:-1,V1:1,V2:1,V3:1})
mc=setq(base,{C:1});me=setq(base,{E:1})
psi=wave([(mc,((edge(D,C),-1),),1),(me,((edge(D,E),-1),),-1)])
loop=fk({edge(A,C):1,edge(D,C):-1,edge(D,E):1,edge(A,E):-1})
near={A}|{u for b in nbr(A) for u in nbr(b)}
pairset=set()
for u in near:
 for b in nbr(u):
  for v in nbr(b):
   if u!=v:pairset.add(tuple(sorted((u,v))))
pairs=sorted(pairset)
start=time.perf_counter()
answers=[]
for sigma in (-1,1):
 born=selected(psi,sigma)
 assert len(born)==1 and len(list(rows(born)))==2
 outmatter=next(iter(born))
 back=selected_adj(born,sigma)
 assert len(back)==5
 assert inner(born,born)==Counter({():2,loop:-1,neg(loop):-1})
 gain2=Counter();minus_loss2=Counter();pair_rows=[]
 for pair in pairs:
  sb=pairhop(born,pair)
  sback=pairhop(back,pair)
  sp=pairhop(psi,pair)
  gram=inner(sb,sb)
  overlap=inner(sback,sp)
  assert sum(gram.values())==sum(overlap.values())==0
  sum_poly(gain2,gram,-2)
  sum_poly(minus_loss2,overlap)
  sum_poly(minus_loss2,adj(overlap))
  this=Counter();sum_poly(this,gram,-2);sum_poly(this,overlap);sum_poly(this,adj(overlap))
  this=Counter({f:n for f,n in this.items() if n})
  pair_rows.append(dict(pair=pair,source_paths=sum(len(v) for v in sp.values()),
                        born_paths=sum(len(v) for v in sb.values()),
                        backward_paths=sum(len(v) for v in sback.values()),
                        power2_terms=len(this),power2_coefficient_sum=sum(this.values()),
                        gain_flat_diagonal=-2*diag_flat(outmatter,pair)))
 total=Counter();sum_poly(total,gain2);sum_poly(total,minus_loss2)
 total=Counter({f:n for f,n in total.items() if n})
 gain2=Counter({f:n for f,n in gain2.items() if n})
 minus_loss2=Counter({f:n for f,n in minus_loss2.items() if n})
 assert total==adj(total)
 assert all(not divergence(f) for f in total)
 assert sum(c for f,c in total.items() if winding(f)==(0,0,0))==0
 Q4=quadratic4(total)
 ell=dict(loop);pivot=edge(A,C)
 r4={}
 all_edges={e for ij in Q4 for e in ij}|set(ell)
 r_p=Fraction(Q4.get((pivot,pivot),0),ell[pivot])
 for e in all_edges:
  r4[e]=(2*Q4.get((pivot,e),0)-r_p*ell.get(e,0))/ell[pivot]
 r4={e:n for e,n in r4.items() if n}
 factored=all(Fraction(Q4.get((x,y),0))==(ell.get(x,0)*r4.get(y,0)+r4.get(x,0)*ell.get(y,0))/2
              for x,y in product(all_edges,repeat=2))
 assert factored
 assert not divergence(tuple(r4.items())) and winding(tuple(r4.items()))==(0,0,0)
 # Full flat diagonal correction relative to the empty-B all-plus baseline.
 special_A={u for b in nbr(A) for u in nbr(b)}|{D,H}|({A} if sigma==-1 else set())
 correction_pairs=set()
 for u in special_A:
  for b in nbr(u):
   for v in nbr(b):
    if u!=v:correction_pairs.add(tuple(sorted((u,v))))
 correction=-2*sum(diag_flat(outmatter,p)-diag_flat((),p) for p in correction_pairs)
 h0local=sum(row['gain_flat_diagonal'] for row in pair_rows)
 result=dict(sigma=sigma,local_pairs=len(pairs),changed_pairs=sum(r['power2_terms']>0 for r in pair_rows),
   twice_power_laurent=serialize(total),twice_gain_local_laurent=serialize(gain2),
   twice_minus_anticommutator_local_laurent=serialize(minus_loss2),
   power2_terms=len(total),nonzero_winding_terms=sum(winding(f)!=(0,0,0) for f in total),
   quadratic_form='Q_2(x)=(ell.x)(r.x), r=r4/4',
   r4=[dict(a=a,b=b,numerator=n.numerator,denominator=n.denominator) for (a,b),n in sorted(r4.items())],
   flat_output_H4='-321*L^3+correction for local geometry without periodic identifications',
   flat_output_correction=correction,local_output_H4_flat=h0local,
   pair_inventory=pair_rows,
   max_flow_l1=max(sum(abs(n) for e,n in f) for f in total),
   quadratic4_entries=len(Q4))
 answers.append(result)
 print(json.dumps({k:v for k,v in result.items() if k not in ['twice_power_laurent','twice_gain_local_laurent','twice_minus_anticommutator_local_laurent','pair_inventory']},indent=2),flush=True)
payload=dict(scope='Exact original primitive local commutator; no author builder; common integer dressing cancels for the rotor magnetic operator only.',
    side=SIDE,infinite_local_lift=not SIDE,near_A_count=len(near),local_pairs=len(pairs),answers=answers,
    elapsed_seconds=time.perf_counter()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with (HERE/(TAG+'_RESULTS.json')).open('x') as f:json.dump(payload,f,indent=2);f.write('\n')
print('COMPLETE',TAG,'elapsed',payload['elapsed_seconds'])
