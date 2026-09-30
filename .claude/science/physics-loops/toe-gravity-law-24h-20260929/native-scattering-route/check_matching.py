"""Original hard-core N=4 words, not pair bosons.
Price: <=10 CPU s, <=120 wall s, <=100 MB, standard library, BLAS1.
"""
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict, Counter
from fractions import Fraction as F
import json, time, resource

t0,c0=time.monotonic(),time.process_time()
base=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (base/'STOP_REQUESTED').exists()
assert time.time()<json.loads((base/'DEADLINE.json').read_text())['deadline_epoch']
e=[(1,0,0),(0,1,0),(0,0,1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda s,a:tuple(s*x for x in a)
nn=[mul(s,v) for v in e for s in (-1,1)]
disp=set([mul(2,s) for s in nn])
disp.update(add(mul(s,e[i]),mul(t,e[j])) for i in range(3) for j in range(i+1,3) for s,t in product((-1,1),repeat=2))
assert len(disp)==18

def canonical(S):
 a=min(S)
 return tuple(sorted(sub(x,a) for x in S))

def matching_edges(S):
 a,b,c,d=S
 return [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]

def perfect(S):
 return any(sub(b,a) in disp and sub(d,c) in disp for (a,b),(c,d) in matching_edges(S))

def degrees(S):
 return [sum(sub(y,x) in disp for y in S if y!=x) for x in S]

def action12(S):
 """Return coefficients of mu and tau in 12 H|S>, literal sites."""
 out=defaultdict(lambda:[0,0]);S=tuple(S);deg=degrees(S)
 out[S][0]+=12*(len(S)+sum(d*(d-1)//2 for d in deg))
 for a,b in combinations(S,2):
  rem=set(S)-{a,b}
  centers=set(add(a,v) for v in nn)&set(add(b,v) for v in nn)
  for x in centers:
   da,db=sub(a,x),sub(b,x)
   ia=next(i for i in range(3) if da[i]);ib=next(i for i in range(3) if db[i])
   for shift in [(0,0,0)]+nn:
    y=add(x,shift);onsite=shift==(0,0,0)
    candidates=[]
    if ia==ib:
     assert da==mul(-1,db)
     for j in range(3):
      candidates.append((add(y,e[j]),sub(y,e[j]),12*(int(ia==j))-4,-2))
    else:
     sg=da[ia]*db[ib]
     for sa,sb in product((-1,1),repeat=2):
      candidates.append((add(y,mul(sa,e[ia])),add(y,mul(sb,e[ib])),3*sg*sa*sb,-1))
    for c,d,coef,attract in candidates:
     if c in rem or d in rem:continue
     target=tuple(sorted(rem|{c,d}));assert len(target)==len(S)
     out[target][0]+=coef*attract if onsite else 0
     out[target][1]+=coef*(6 if onsite else -1)
 return {k:tuple(v) for k,v in out.items() if any(v)}

# All abstract graphs, stronger than just those embedded in G.
edges=list(combinations(range(4),2));stats=Counter()
for mask in range(64):
 es={edges[i] for i in range(6) if mask>>i&1}
 pm=any(set(map(lambda z:tuple(sorted(z)),m))<=es for m in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))])
 deg=[sum(i in ed for ed in es) for i in range(4)]
 D=sum((d-1)*(d-2)//2 for d in deg)
 assert D>=0
 if not pm:assert D>=1
 stats[(pm,D)]+=1

# Count only connected translation shapes, no torus and no large N=4 box.
shapes={((0,0,0),)};sizes=[]
for n in range(2,5):
 nxt=set()
 for S in shapes:
  for x in S:
   for d in disp:
    y=add(x,d)
    if y not in S:nxt.add(canonical(S+(y,)))
 shapes=nxt;sizes.append(len(shapes))
assert all(perfect(S) or sum((d-1)*(d-2)//2 for d in degrees(S))>=1 for S in shapes)

S=tuple((j,0,0) for j in (0,2,4,6))
T=tuple(sorted([(0,0,0),(3,-1,1),(3,1,1),(6,0,0)]))
T0=tuple(sorted([(0,0,0),(3,-1,0),(3,1,0),(6,0,0)]))
assert perfect(S) and not perfect(T) and not perfect(T0)
row=action12(S);rev=action12(T)
assert row[T]==rev[S]==(0,4) # tau/3 at every positive tau
assert row[T0]==(8,-24) # (2mu-6tau)/3
qrow={z:c for z,c in row.items() if not perfect(z)}
norm2=sum((F(a+b,12))**2 for a,b in qrow.values())

# The K=0 orbit coefficient includes all translation returns, explicitly.
fiber=defaultdict(lambda:[0,0])
for z,(a,b) in row.items():
 f=fiber[canonical(z)];f[0]+=a;f[1]+=b
assert tuple(fiber[canonical(T)])==(0,4)

# Exact generalized uniform E1 E1 incoming amplitude C_E1^2 Omega.
# E1 coefficients (1,-1,0)/sqrt2 give this integer matching polynomial.
def ew(a,b):
 d=sub(b,a)
 for i in range(3):
  if d in (mul(2,e[i]),mul(-2,e[i])):return (1,-1,0)[i]
 return 0
def phi(z):
 return sum(ew(a,b)*ew(c,d) for (a,b),(c,d) in matching_edges(z))
incoming=[sum(F(c[i],12)*phi(z) for z,c in rev.items() if perfect(z)) for i in range(2)]
assert incoming==[F(0),F(1,3)]

# Actual literal Hermiticity controls, without importing an operator builder.
hermiticity=0
for target in list(row)[:20]:
 assert action12(target).get(S,(0,0))==row[target]
 hermiticity+=1

out={'abstract_graphs':64,'nonmatching_graph_count':sum(v for (pm,d),v in stats.items() if not pm),
 'nonmatching_diagonal_counts':{str(d):sum(v for (pm,dd),v in stats.items() if not pm and dd==d) for d in (1,2,4)},
 'connected_translation_shape_counts_N2_N3_N4':sizes,
 'connected_N4_with_perfect_matching':sum(perfect(z) for z in shapes),
 'witness_source':S,'witness_closed_target':T,
 'H_target_source_mu_tau':['0','1/3'],
 'zero_momentum_uniform_E1_pair_pair_target_mu_tau':[str(x) for x in incoming],
 'closed_output_words_from_one_source':len(qrow),
 'closed_output_norm_squared_at_mu_tau_1':str(norm2),
 'selfenergy_diagonal_bounds_mu_tau_1':[str(norm2/160),str(norm2)],
 'literal_hermiticity_columns_checked':hermiticity,
 'scope':'Actual N4 source action, abstract integer gap, finite connected shapes, one nonzero threshold-channel virtual-state source. No full scattering matrix computed.',
 'wall_seconds':time.monotonic()-t0,'cpu_seconds':time.process_time()-c0,
 'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('matching_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
