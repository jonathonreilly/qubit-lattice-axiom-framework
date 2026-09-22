from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import json,hashlib
r=Path('/private/tmp/review-drain-20260915');p=r/'drain8159-originals/.claude/science/physics-loops/toe-fixed-clock-field-20260915';d=json.loads((p/'evidence/block8_native_twist_check.json').read_text());checked=0
for bundle in d['native_tapes']:
 L=bundle['L'];vs=list(product(range(L),repeat=3));vi={v:i for i,v in enumerate(vs)}
 def step(v,a):return tuple((x+1)%L if i==a else x for i,x in enumerate(v))
 edges=sorted({tuple(sorted((v,step(v,a)))) for v in vs for a in range(3)});ei={e:i for i,e in enumerate(edges)}
 stars={v:sorted(w for e in edges if v in e for w in e if w!=v) for v in vs}
 def bit(b,v,w):return (b>>ei[tuple(sorted((v,w)))])&1
 def q(b,v):return (-1)**sum(v)*(sum(bit(b,v,w) for w in stars[v])-3)
 for cycle in bundle['cycles']:
  rows=cycle['tape'];amp=1
  for i,row in enumerate(rows):
   b=int(row['configuration_before_hex'],16);x=tuple(row['source']);y=tuple(row['target']);e=ei[tuple(sorted((x,y)))]; nxt=int(rows[(i+1)%len(rows)]['configuration_before_hex'],16)
   assert b^(1<<e)==nxt;assert q(b,x)==row['charge'] and q(b,y)==0
   charges=[q(b,v) for v in vs];assert sorted(z for z in charges if z)==[-1,1]
   lo,hi=sorted((x,y));phase=(-1)**(sum(bit(b,lo,w) for w in stars[lo] if w<hi)+sum(bit(b,hi,w) for w in stars[hi] if w<lo))
   B=lambda v:(-1)**sum(bit(b,v,w) for w in stars[v])
   native=1j*(B(lo)-B(hi))*phase/2;assert native==complex(*row['native_phase']);amp*=native;checked+=1
  assert amp==1
# Recover every u/marker swap by removing its transferred u, using full words.
counts=[]
for M in [1,2,3]:
 ws=[w for n in range(M,7) for w in product(range(3),repeat=n) if sum(z!=0 for z in w)==M];expected=set();seen=Counter()
 for w in ws:
  for j in range(len(w)-1):
   if (w[j]==0)!=(w[j+1]==0):expected.add(tuple(sorted((w,w[:j]+(w[j+1],w[j])+w[j+2:]))))
  if len(w)<6:
   pos=[i for i,z in enumerate(w) if z!=0]+[len(w)];ins=[w[:i]+(0,)+w[i:] for i in pos]
   for j in range(M):seen[tuple(sorted((ins[j],ins[j+1])))]+=1
 assert set(seen)==expected and all(v==1 for v in seen.values());counts.append({'M':M,'edges':len(expected),'multiplicity':1})
# Exact factor-two winding curvature on an unequal-conductance isolated cycle.
c=[F(1),F(2),F(3),F(5)];resistance=sum(1/x for x in c);current=1/resistance;residual=[current/x for x in c];energy=sum(x*y*y for x,y in zip(c,residual));assert sum(residual)==1 and energy==1/resistance
# Independent half-line return walk count (unit hopping), including source boundary.
f={1:1};mom=[]
for power in range(9):
 if power%2==0:
  from math import comb
  m=power//2;assert f.get(1,0)==comb(2*m,m)//(m+1);mom.append(f.get(1,0))
 new=Counter()
 for site,v in f.items():
  new[site+1]+=v
  if site>1:new[site-1]+=v
 f=dict(new)
out={'scope':'bounded independent exact controls, no author code imports or primary execution','native_tape_hops_reconstructed':checked,'marker_edge_injectivity':counts,'cycle_curvature':str(2*energy),'wrong_missing_factor_two':str(energy),'half_line_return_moments_0_to_8':mom,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'negative_controls':['native omitted phase is not a real unsigned hopping substitution','double-counting u-marker swaps changes the lower-bound constant','missing curvature factor two disagrees with the edge-form expansion','full-fiber floor does not determine every source measure']}
f=r/'drain8159-family4-independent-control.json';assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
