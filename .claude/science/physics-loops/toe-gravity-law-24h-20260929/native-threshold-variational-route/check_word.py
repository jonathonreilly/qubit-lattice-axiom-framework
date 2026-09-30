#!/usr/bin/env python3
"""Actual N4 word action; no pair-boson replacement or imported action helper."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product,combinations
from pathlib import Path
import json,time,resource,signal
start=time.perf_counter();cpu=time.process_time();signal.alarm(30);resource.setrlimit(resource.RLIMIT_CPU,(20,21))
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not(runtime/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
ez=(0,0,0);axes=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def times(c,a):return tuple(c*x for x in a)
unit=[times(s,e) for e in axes for s in (-1,1)]
axial=[((times(-1,e),e),1) for e in axes]
channels=[[(axial[0][0],1),(axial[1][0],-1)],[(axial[0][0],1),(axial[1][0],1),(axial[2][0],-2)]]
for i,j in combinations(range(3),2):channels.append([((times(s,axes[i]),times(t,axes[j])),s*t) for s,t in product((-1,1),repeat=2)])
weights=[F(1,2),F(1,6),F(1,4),F(1,4),F(1,4)]
G={times(2,u) for u in unit}|{plus(times(s,axes[i]),times(t,axes[j])) for i,j in combinations(range(3),2) for s,t in product((-1,1),repeat=2)}
def canonical(S):return tuple(sorted(S))
def action(S):
 S=frozenset(S);out=defaultdict(lambda:[F(0),F(0)])
 tri=sum(sum(plus(x,d) in S for d in G)*(sum(plus(x,d) in S for d in G)-1)//2 for x in S)
 out[canonical(S)][0]+=len(S)+tri
 centers={plus(x,times(-1,u)) for x in S for u in unit}
 for c in centers:
  for a,ch in enumerate(channels):
   for pair,cs in ch:
    annih=frozenset(plus(c,u) for u in pair)
    if not annih<=S:continue
    remain=S-annih
    for target,mu,tau in [(c,F(-2 if a<2 else -1),F(6))]+[(plus(c,u),F(0),F(-1)) for u in unit]:
     for pp,ct in ch:
      create=frozenset(plus(target,u) for u in pp)
      if create&remain:continue
      key=canonical(remain|create);coeff=weights[a]*cs*ct
      out[key][0]+=coeff*mu;out[key][1]+=coeff*tau
 return {s:tuple(c) for s,c in out.items() if any(c)}
def incoming_Q_squared(S):
 a,b,c,d=S
 def edge(x,y):
  delta=tuple(v-u for u,v in zip(x,y))
  return 1 if delta in [times(s*2,axes[0]) for s in (-1,1)] else -1 if delta in [times(s*2,axes[1]) for s in (-1,1)] else 0
 return sum(edge(*e)*edge(*f) for e,f in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))])
T=canonical([ez,(3,-1,1),(3,1,1),(6,0,0)])
row=action(T);diag=row[T]
assert diag==(F(8,3),F(4)),diag
source=tuple(sum(coeff[j]*incoming_Q_squared(S) for S,coeff in row.items()) for j in range(2))
assert source==(F(0),F(1,3)),source
# Distinct implementation route: Hermitian row consistency on every resulting word.
for S,coeff in row.items():assert action(S).get(T,(F(0),F(0)))==coeff
# Exact optimized coefficient and separate genuine improvement at three supplied parameters.
rows=[]
for mu,tau in [(F(1),F(1)),(F(2),F(1)),(F(1,3),F(3,2))]:
 h=F(8,3)*mu+4*tau;c=-tau/(6*h);bare=52*mu+120*tau
 corrected=bare+c*tau/3+c*c*h
 improvement=tau*tau/(96*mu+144*tau)
 assert bare-corrected==improvement and improvement>0
 rows.append({'mu':str(mu),'tau':str(tau),'H_TT':str(h),'four_creation_generator_coefficient':str(c),'bare_u4':str(bare),'corrected_u4':str(corrected),'strict_improvement':str(improvement)})
# Linked bounds finite, with number/pair normalization conventions kept separate.
def rising(s,m):
 out=1
 for j in range(m):out*=s+3*j
 return out
assert rising(1,4)==280 and rising(25,3)==21700
out={'scope':'Exact local actual-M2 N4 word control; uniform many-particle remainder and threshold infimum are analytic obligations, not inferred from this job.','target':T,'nonzero_H_columns':len(row),'diagonal_mu_tau':[str(x) for x in diag],'H_Q_squared_source_mu_tau':[str(x) for x in source],'hermiticity_columns_checked':len(row),'parameter_controls':rows,'full_sparse_row':{str(s):[str(x) for x in c] for s,c in sorted(row.items())},'wall_seconds':time.perf_counter()-start,'cpu_seconds':time.process_time()-cpu,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'author_action_helper_reused':False}
Path(__file__).with_name('word_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='full_sparse_row'}))
