from pathlib import Path
import numpy as np,json
from neutral_kink_core import band,bits
rows=[]
for L in [6,8,12]:
 H1,H2,states,s0=band(L);sH=H1@s0;delta=[]
 for state in states:
  ds=[(state//8**j)%8 for j in range(L)]
  delta.append(-sum(2*(bits[ds[j]]^bits[ds[(j+2)%L]]).bit_count() for j in range(L)))
 delta=np.array(delta);support=abs(sH)>1e-12
 assert np.all(delta[support]==-16)
 assert np.all(delta[abs(s0)>1e-12]==-8)
 s1=delta*sH/64
 assert np.linalg.norm(s1+H1@s0/4)<1e-12
 rows.append(dict(L=L,source_norm=float(s0@s0),H1source_norm=float(sH@sH),deltaO_support_values=np.unique(delta[support]).tolist(),second_source_identity_residual=float(np.linalg.norm(s1+H1@s0/4))))
print(rows);open(Path(__file__).resolve().parent/'neutral_kink_source_dressing.json','w').write(json.dumps(rows,indent=2))
