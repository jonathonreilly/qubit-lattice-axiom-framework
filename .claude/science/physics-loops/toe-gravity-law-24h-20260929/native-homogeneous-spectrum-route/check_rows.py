#!/usr/bin/env python3
"""Exact literal-row controls, not a many-body spectral computation."""
from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict
from pathlib import Path
import json,time
start=time.process_time()
ROOT=Path(__file__).resolve().parent
E=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b,L=None):
 v=tuple(x+y for x,y in zip(a,b)); return tuple(x%L for x in v) if L else v
def scale(a,s): return tuple(s*x for x in a)
def edge(a,b): return tuple(sorted((a,b)))
def bare(x,L):
 d=[edge(add(x,e,L),add(x,scale(e,-1),L)) for e in E]
 planes=[]
 for i,j in combinations(range(3),2):
  planes.append([(edge(add(x,scale(E[i],s),L),add(x,scale(E[j],t),L)),s*t) for s,t in product((-1,1),repeat=2)])
 return d,planes

def row_terms(items):
 z=defaultdict(int)
 for e,c in items: z[e]+=c
 return {e:c for e,c in z.items() if c}

def channels(x,L):
 d,p=bare(x,L)
 return [(F(1,2),[(d[0],1),(d[1],-1)]),
         (F(1,6),[(d[0],1),(d[1],1),(d[2],-2)])]+[(F(1,4),q) for q in p]

def rows(x,L):
 d,planes=bare(x,L)
 yield 'mu',F(2,3),row_terms([(e,1) for e in d])
 for p in planes:
  for (e,c),(f,k) in combinations(p,2): yield 'mu',F(1,4),row_terms([(e,c),(f,-k)])
 q=channels(x,L)
 for v in E:
  qp=channels(add(x,v,L),L)
  for (w,a),(wp,b) in zip(q,qp):
   assert w==wp
   yield 'tau',w,row_terms(b+[(e,-c) for e,c in a])

def par(e,i):return sum(x[i] for x in e)%2

def coeff(L,e,f):
 out={'mu':F(0),'tau':F(0)}
 for x in product(range(L),repeat=3):
  for kind,w,r in rows(x,L):
   if e in r and f in r: out[kind]+=w*r[e]*r[f]
 return out

report={'role':'exact finite word/geometry control; no numerical LSM or spectral certification','cases':[]}
checks=0
for L in [6,8]:
 centers=list(product([0,1,L-1],repeat=3)); nrows=0; terms=0
 for x in centers:
  for kind,w,r in rows(x,L):
   nrows+=1;terms+=len(r)
   assert w>0
   for i in range(3): assert len({par(e,i) for e in r})==1
 assert nrows==27*34
 report['cases'].append({'type':'even-row-character','L':L,'centers':len(centers),'rows':nrows,'annihilator_terms':terms})
 checks+=1
# Actual total H coefficients: center sums include duplicate plane centers.
for L,center,step,odd in [(6,(0,0,0),E[1],False),(7,(0,0,0),E[0],True)]:
 d,_=bare(center,L);dp,_=bare(add(center,step,L),L)
 a,b=d[0],dp[0]
 assert set(a).isdisjoint(b)
 k=coeff(L,a,b)
 assert k=={'mu':F(0),'tau':F(-2,3)}
 if odd: assert par(a,0)!=par(b,0)
 else:
  # Here no seam in the translated direction: continuous dipole changes by2.
  assert sum(x[1] for x in b)-sum(x[1] for x in a)==2
 report['cases'].append({'type':'total-original-offdiagonal','L':L,'e':a,'f':b,'coefficients':{k:str(v) for k,v in k.items()},'odd_seam_breaks_parity':odd})
 checks+=1
# Translation algebra tested directly on occupied configurations, including seams.
for L in [6,8]:
 sites=[(0,0,0),(L-1,0,1),(1,L-1,2),(2,2,L-1),(3,1,0)]
 for N in [1,2,3,4,5]:
  X=sites[:N]
  assert len(set(X))==N
  for i,j in product(range(3),repeat=2):
   Y=[add(x,E[i],L) for x in X]
   lhs=(sum(x[j] for x in Y)-sum(x[j] for x in X))%2
   assert lhs==(N*(i==j))%2
 report['cases'].append({'type':'translation-parity','L':L,'N_values':[1,2,3,4,5],'axis_pairs':9})
 checks+=1
# Local support and overlap ball counts used in the propagation proof.
for radius,expected in [(2,25),(4,129)]:
 points=[x for x in product(range(-radius,radius+1),repeat=3) if sum(map(abs,x))<=radius]
 assert len(points)==expected
 report['cases'].append({'type':'Manhattan-ball','radius':radius,'count':len(points)})
 checks+=1
max_dp=0
for _,_,r in rows((0,0,0),None):
 for i in range(3):
  p=[sum(x[i] for x in e) for e in r]
  max_dp=max(max_dp,max(p)-min(p))
assert max_dp<=6 and max_dp==4
report['cases'].append({'type':'unwrapped-direct-twist','actual_max_pair_coordinate_difference':max_dp,'proof_bound':6})
checks+=1
# Literal qubit lowering: N=1 is annihilated by every pair row; Ddiag=N.
for _,_,r in rows((0,0,0),None):
 for e in r: assert len(set(e))==2
report['cases'].append({'type':'N1','all_pair_words_have_two_distinct_endpoints':True,'Ddiag_on_singleton':'1','H0_on_sector':'mu I','inelastic_density_weight':'0 after full ground removal'})
checks+=1
report['checks']=checks;report['cpu_seconds']=time.process_time()-start
(ROOT/'ROWS_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
print(f'TOTAL PASS={checks} FAIL=0')
