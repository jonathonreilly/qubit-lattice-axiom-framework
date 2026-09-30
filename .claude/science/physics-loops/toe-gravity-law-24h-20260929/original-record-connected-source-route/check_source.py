#!/usr/bin/env python3
"""Actual cubic oriented-star source, exact integers and original marks."""
import os,time,resource,json,hashlib
from pathlib import Path
from collections import defaultdict
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
t0=time.perf_counter();c0=time.process_time()
# Positive-coordinate orientations: A is tail on +ei and head on -ei.
eta=(1,-1,1,-1,1,-1)
omega=(1,(0,)*6,(0,)*6)
def gauss(w):
 a,bs,es=w
 return sum(s*e for s,e in zip(eta,es))+1-a==0 and all(-s*e-b==0 for s,e,b in zip(eta,es,bs))
def hop(w,b):
 a,bs,es=w
 if not a or bs[b]:return None
 outb=list(bs);oute=list(es);outb[b]=a;oute[b]-=eta[b]*a
 return (0,tuple(outb),tuple(oute))
def birth(w,b,c_edge):
 a,bs,es=w
 if a or bs[b]:return None
 ca=eta[b]*c_edge;outb=list(bs);oute=list(es)
 outb[b]=-ca;oute[b]+=c_edge
 return (ca,tuple(outb),tuple(oute))
def applyF(v):
 out=defaultdict(int)
 for w,c in v.items():
  for b in range(6):
   nw=hop(w,b)
   if nw is not None:out[nw]+=c
 return {w:c for w,c in out.items() if c}
def applyJ(v,b,signs):
 out=defaultdict(int)
 for w,c in v.items():
  for sign in signs:
   nw=birth(w,b,sign)
   if nw is not None:out[nw]+=c
 return {w:c for w,c in out.items() if c}
def add(*vs):
 out=defaultdict(int)
 for v in vs:
  for w,c in v.items():out[w]+=c
 return {w:c for w,c in out.items() if c}
def neg(v,m=-1):return {w:m*c for w,c in v.items()}
def norm(v):return sum(c*c for c in v.values())
rows=[]
for b in range(6):
 for signs in ((1,),(-1,),(1,-1)):
  v={omega:1}
  fjf=applyF(applyJ(applyF(v),b,signs))
  source=neg(fjf)
  # 2*J_(2,+1)=F²j-2FjF+jF², with literal original mark.
  double=add(applyF(applyF(applyJ(v,b,signs))),neg(fjf,-2),applyJ(applyF(applyF(v)),b,signs))
  assert double=={w:2*c for w,c in source.items()}
  expected=60 if len(signs)==2 else 40 if eta[b]*signs[0]==1 else 20
  assert norm(source)==expected
  assert all(gauss(w) and w[0]==0 and sum(q!=0 for q in w[1])==3 and sum(w[1])==1 and max(abs(e) for e in w[2])==1 for w in source)
  assert all(2*sum(q==0 for q in w[1])==6 for w in source)
  multiplicities={str(c):sum(v==c for v in source.values()) for c in set(source.values())}
  # Literal path count is not coherent norm: the distinction is detected.
  path_count=sum(abs(c) for c in source.values())
  if len(signs)==2:assert path_count==40 and norm(source)==60
  rows.append({'edge':b,'A_is_tail':eta[b]==1,'original_signs':signs,'output_words':len(source),'squared_norm':norm(source),'path_count':path_count,'amplitudes':multiplicities})
assert sum(r['squared_norm'] for r in rows if len(r['original_signs'])==2)==360
assert sum(r['squared_norm'] for r in rows if len(r['original_signs'])==1)==360
# Exact occupancy-count proof control for arbitrary NB<=3: G>=6 per hole.
assert min(2*(6-j) for j in range(4))==6
# All traversed spin steps have integer E=0 -> +/-1 or +/-1 ->0;
# here every edge is distinct, so normalized weights are exactly1 for all S>=1.
for S in (1,2,7,101):
 C=S*(S+1)
 assert all(C-e*(e+k)==C for e,k in ((0,1),(0,-1),(1,-1),(-1,1)))
# Exact total edge loss includes both original signs, even at spin boundaries.
from fractions import Fraction
loss_cases=0
for S in range(1,65):
 C=S*(S+1)
 for E in range(-S,S+1):
  up=Fraction(C-E*(E+1),C) if E<S else Fraction(0)
  dn=Fraction(C-E*(E-1),C) if E>-S else Fraction(0)
  assert up+dn==2-Fraction(2*E*E,C)
  assert up+dn>=Fraction(2,S+1)
  if abs(E)==S:assert up+dn==Fraction(2,S+1)
  loss_cases+=1
assert not (runtime/'STOP_REQUESTED.json').exists()
result={'scope':'exact original cubic-star J_(2,+1) source on bare Omega; no evolution approximation or field-box truncation','rows':rows,'per_A_squared_norm_resolved':360,'per_A_squared_norm_coherent':360,'incoherent_path_sum_wrong_total':240,'source_W':1,'source_NB':3,'source_G':6,'all_gauss':True,'nested_commutator_checks':18,'exact_spin_loss_cases':loss_cases,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.perf_counter()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('SOURCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
