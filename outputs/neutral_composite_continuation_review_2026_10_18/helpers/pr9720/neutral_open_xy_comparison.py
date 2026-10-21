"""Derived weak-rung expansion versus native selected-plane-sector gaps."""
from pathlib import Path
import numpy as np,json
P=Path(__file__).resolve().parent
I=np.eye(2);X=np.array([[0.,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1])
def pair(a,i,j,L):
 out=np.array([[1.+0j]])
 for k in range(L):out=np.kron(out,a if k in (i,j) else I)
 return out
rows=[]
for L in [4,6,8]:
 N=1<<L;ids=[b for b in range(N) if b.bit_count()%2==(L//2)%2 and b<(b^(N-1))];W=np.zeros((N,len(ids)))
 for i,b in enumerate(ids):W[b,i]=W[b^(N-1),i]=1/np.sqrt(2)
 eye=np.eye(N,dtype=complex);H=np.zeros_like(eye);V4=np.zeros_like(eye);O=np.zeros_like(eye)
 XY=lambda i,j:pair(X,i,j,L)+pair(Y,i,j,L)
 for j in range(L-1):
  H-=.5*XY(j,j+1);V4+=-eye/32+XY(j,j+1)/16-5*pair(Z,j,j+1,L)/32
 for j in range(L-2):
  V4+=-eye/8-(XY(j,j+1)+XY(j+1,j+2))/16-3*XY(j,j+2)/16
  O+=.375*(XY(j,j+1)+XY(j+1,j+2)+XY(j,j+2))/np.sqrt(L-2)
 H=W.T@H@W;V4=W.T@V4@W;O=W.T@O@W
 for lam in [1.,.7,.5,.35,.2,.1]:
  e,u=np.linalg.eigh(H+lam**2*V4);g=u[:,0];src=O@g-g*(g.conj()@O@g);weights=abs(u.conj().T@src)**2
  e2=np.linalg.eigvalsh(H)
  rows.append(dict(L=L,lambda_z=lam,leading_gaps_over_t=(e2[:4]-e2[0]).tolist(),fourth_gaps_over_t=(e[:4]-e[0]).tolist(),O2_mode_weights=weights[:4].tolist(),scope='Exact finite diagonalization of derived fourth-order truncation in matching globalX/Y+ low band; omitted terms not bounded atlambda1'))
(P/'neutral_open_xy_comparison.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n');print(rows)
