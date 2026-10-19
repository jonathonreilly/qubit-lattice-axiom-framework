import json
from compass_sector_basis import basis
D=basis((3,3,3));out=[]
for y in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[1] in [y,y+1]);out.append(D['reduce_term'](m,m,-1))
import numpy as np
from pathlib import Path
from compass_sector_solve import apply
p=Path(__file__).resolve().parent
s=np.load(p/'stationary_3x3x3_plus.npz');vec=s['vectors'];rows=[]
for k in range(vec.shape[1]):
 vals=[]
 for f,z,c in out:
  v=vec[:,k];sv=apply(v,*np.array([(f,z,c)],dtype=np.int64).T.copy());mean=float(v@sv);vals.append(dict(mean=mean,variance=float(sv@sv-mean*mean)))
 rows.append(dict(energy=float(s['values'][k]),labels=vals))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
