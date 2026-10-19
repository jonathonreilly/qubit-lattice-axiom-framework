from pathlib import Path
import numpy as np,json
from native_mpo import build,geometry,X,Z
Y=np.array([[0,-1j],[1j,0]])
rows=[]
for shape in [(2,2,2),(1,3,3),(3,2,1)]:
 sites,bonds=geometry(shape);N=len(sites);h=np.zeros((2**N,2**N),complex)
 for i,j,a in bonds:
  term=np.array([[1.]])
  for k in range(N):term=np.kron(term,[X,Y,Z][a] if k in [i,j] else np.eye(2))
  h-=term
 mpo=build(shape).to_dense();err=float(np.max(abs(h-mpo)));assert err==0
 rows.append(dict(shape=shape,physical_qubits=N,max_error=err))
print(rows);Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
