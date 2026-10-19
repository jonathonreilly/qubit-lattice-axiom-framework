"""Check parity-coordinate mapping directly against four physical Pauli qubits."""
from pathlib import Path
import json,itertools
import numpy as np
from native_rung import h,Ds,xs,mpo
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
def op(a,i):
 out=np.array([[1.]])
 for j in range(4):out=np.kron(out,a if i==j else I)
 return out
U=np.zeros((16,8))
for a,b,c in itertools.product(range(2),repeat=3):U[8*a+4*b+2*c+(a^b^c),4*a+2*b+c]=1
H=-op(X,0)@op(X,2)-op(X,1)@op(X,3)-op(Y,0)@op(Y,1)-op(Y,2)@op(Y,3)
errors=[np.max(abs(U.T@H@U-h))]
errors.extend(np.max(abs(U.T@op(Z,i)@U-Ds[i])) for i in range(4))
errors.append(np.max(abs(U.T@op(X,0)@op(X,1)@U-xs[0]@xs[1])))
target=np.kron(h,np.eye(8))+np.kron(np.eye(8),h)-sum(np.kron(d,d) for d in Ds)
errors.append(np.max(abs(mpo(2).to_dense()-target)))
assert max(errors)<1e-13
result=dict(max_error=float(max(errors)),physical_qubits_per_rung=4,sector_dimension=8,checks=len(errors),scope='Exact native parity-coordinate representation, not additional qubits')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
