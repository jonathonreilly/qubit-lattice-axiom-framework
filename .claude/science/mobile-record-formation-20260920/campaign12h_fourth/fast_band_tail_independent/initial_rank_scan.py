from fiber_engine import *
from itertools import product
import json
assert len(WORDS)==168 and len(ONE)==96 and len(DARK)==24 and len(BRIGHT)==72
for q in WORDS:assert gauss(q,reference(q))
rows=[]
for k,powers in enumerate(product(range(4),repeat=5)):
 if k>255:break
 G,gamma,F=matrices(tuple(1j**p for p in powers))
 coupling=G[np.ix_(BRIGHT,DARK)]
 rank=int(np.linalg.matrix_rank(coupling,tol=1e-10))
 rows.append({'powers':powers,'rank_of_bright_G_dark':rank})
 if rank==24:break
print(json.dumps({'dimensions':[len(WORDS),len(ONE),len(DARK),len(BRIGHT)],'chords':CHORDS,'maximum_rank':max(r['rank_of_bright_G_dark'] for r in rows),'rows':rows},indent=2))
