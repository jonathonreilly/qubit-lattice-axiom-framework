"""Check exact energy-current identity on finite-support integer profiles."""
from collections import defaultdict
from itertools import product as cartesian
from pathlib import Path
import json,random
from compass_local_transport import word,shift,derivative
P=Path(__file__).resolve().parent
rows=[]
for seed in [11,42,105]:
 rng=random.Random(seed);f={x:rng.randrange(-3,4) for x in cartesian(range(-1,2),repeat=3)}
 source=defaultdict(int)
 for x,fx in f.items():
  for a in range(3):
   for s in [-1,1]:source[word([(x,a),(shift(x,a,s),a)])]+=fx
 source={k:v for k,v in source.items() if v};actual=derivative(source);pred=defaultdict(int)
 centers={shift(x,a,s) for x in f for a in range(3) for s in [-1,1]}
 for p in centers:
  for a in range(3):
   for b in range(a+1,3):
    c=3-a-b;eps=1 if (b-a)%3==1 else -1
    for s in [-1,1]:
     for t in [-1,1]:
      x=shift(p,a,s);y=shift(p,b,t);coef=-2*eps*(f.get(y,0)-f.get(x,0))
      pred[word([(x,a),(p,c),(y,b)])]+=coef
 pred={k:v for k,v in pred.items() if v}
 assert pred==actual
 # Profiles here represent 2E_f at K=1; current squared norm divided4.
 assert sum(v*v for v in actual.values())==sum(v*v for v in pred.values())
 rows.append(dict(seed=seed,profile_sites=len(f),bond_words=len(source),current_words=len(actual),twice_energy_current_norm_squared=sum(v*v for v in actual.values())))
print(rows)
(P/'energy_current_identity.json').write_text(json.dumps(dict(scope='Exact local current identity, integer compact-support profile controls',rows=rows),indent=2)+'\n')
