import json,numpy as np,time
from scipy.sparse.linalg import eigsh
from neutral_cube_model import sector,op
rows=[]
for k in range(4):
 start=time.time();d=sector(3,tuple(a<k for a in range(3)));terms=sum(d['H'],[])
 for a in sum(d['physical_H'],[])+d['physical_S']:
  assert all(((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0 for b in d['all_generators'])
 assert all((x&z).bit_count()%2==0 for x,z,c in terms)
 H=op(terms,d['dim']);vals,vec=eigsh(H,k=2,which='SA',tol=2e-11,ncv=24,v0=np.random.default_rng(1831).normal(size=d['dim']))
 rows.append(dict(k=k,dim=d['dim'],energies=list(vals),residuals=[float(np.linalg.norm(H@vec[:,j]-vals[j]*vec[:,j])) for j in range(2)],seconds=time.time()-start));print(rows[-1],flush=True)
 open('/private/tmp/neutral_cube_sectors.json','w').write(json.dumps(rows,indent=2)+'\n')
