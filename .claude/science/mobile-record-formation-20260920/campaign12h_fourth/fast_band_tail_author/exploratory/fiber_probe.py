from itertools import combinations
from pathlib import Path
import json, numpy as np

A=(0,3,5,6);B=(1,2,4,7)
edges=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
words=[]
for occupied in combinations(range(8),6):
 for minus in occupied:
  words.append(tuple((-1 if i==minus else 1) if i in occupied else 0 for i in range(8)))
index={q:i for i,q in enumerate(words)}
W=np.array([sum(q[a]==0 for a in A) for q in words])
p=[np.flatnonzero(W==i) for i in (0,1,2)]
dark=np.array([j for j,i in enumerate(p[1]) if not any(words[i][a]==words[i][b]==0 for a,b in edges)])
bright=np.array([j for j in range(len(p[1])) if j not in dark])

def build(phases):
 F=np.zeros((len(words),len(words)),complex)
 for i,q in enumerate(words):
  for e,(a,b) in enumerate(edges):
   if q[a] and not q[b]:
    dest=list(q);dest[b]=q[a];dest[a]=0
    F[index[tuple(dest)],i]+=phases[e]**(-q[a])
 G=(F@F.conj().T-F.conj().T@F)[np.ix_(p[1],p[1])]
 return G

if __name__=='__main__':
 rng=np.random.default_rng(20260924);rows=[]
 for trial in range(8):
  exponents=None
  if trial==0:z=np.ones(12,complex)
  elif trial<5:
   exponents=rng.integers(0,4,size=12).tolist();z=np.array([1j**v for v in exponents])
  else:z=np.exp(2j*np.pi*rng.random(12))
  G=build(z);Q=G[np.ix_(bright,dark)];dd=G[np.ix_(dark,dark)];s=np.linalg.svd(Q,compute_uv=False)
  rows.append({'trial':trial,'fourth_root_exponents':exponents,'DD_max':float(np.max(abs(dd))),'BD_rank_at_1e_10':int(sum(s>1e-10)),'BD_singular_values':s.tolist()})
 result={'charge_dim':len(words),'W_dimensions':[len(x) for x in p],'dark_dimension':len(dark),'bright_dimension':len(bright),'rows':rows,'status':'exploratory ranks only'}
 (Path(__file__).parent/'FIBER_PROBE.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
