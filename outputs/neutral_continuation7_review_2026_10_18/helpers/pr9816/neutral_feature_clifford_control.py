"""Explicit kinematic eight-site code, then challenge against native cube H."""
AUDIT_TIMEOUT_SEC=300
import numpy as np,json,hashlib
from itertools import product
I=np.eye(2);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);P=[X,Y,Z]
def kron(xs):
 a=np.array([[1]],complex)
 for x in xs:a=np.kron(a,x)
 return a
G=[]
for j in range(3):
 for a in (X,Y):G.append(kron([Z]*j+[a]+[I]*(2-j)))
for i in range(6):
 for j in range(6):assert np.linalg.norm(G[i]@G[j]+G[j]@G[i]-2*(i==j)*np.eye(8))<1e-12
blocks=[]
for bits in product((0,1),repeat=6):
 A=sum((-1)**bits[i]*G[i] for i in range(6))/np.sqrt(6)
 e,u=np.linalg.eigh(A);assert np.max(abs(e-np.array([-1]*4+[1]*4)))<1e-12
 # Deterministic projected-coordinate Gram-Schmidt fixes the physical code.
 projector=(np.eye(8)+A)/2; basis=[]
 for k in range(8):
  v=projector[:,k].copy()
  for _ in range(2):
   for q in basis:v-=q*np.vdot(q,v)
  norm=np.linalg.norm(v)
  if norm>1e-10:basis.append(v/norm)
  if len(basis)==4:break
 assert len(basis)==4
 blocks.append(np.column_stack(basis).conj().T/np.sqrt(32))
V=np.vstack(blocks);assert np.linalg.norm(V.conj().T@V-np.eye(8))<1e-12
# Six face ports, one physical qubit per cube site; two remaining sites complete the dilation.
ports=[0,7,4,3,2,5];anc=[1,6];order=ports+anc
W=np.zeros_like(V)
for reg in range(256):
 bits=[(reg>>(7-j))&1 for j in range(8)];physical=sum(bits[j]<<(7-order[j]) for j in range(8));W[physical]=V[reg]
rot=[I.astype(complex)]*8;had=(X+Z)/np.sqrt(2);phase=np.diag([1,1j])
axes=[0,0,1,1,2,2]
for site,ax in zip(ports,axes):rot[site]=had if ax==0 else phase@had if ax==1 else I
W=kron(rot)@W
errs=[]
for j,(site,ax) in enumerate(zip(ports,axes)):
 op=kron([P[ax] if i==site else I for i in range(8)])
 errs.append(float(np.linalg.norm(W.conj().T@op@W-G[j]/np.sqrt(6))))
assert max(errs)<1e-12
sites=list(product(range(2),repeat=3));ids={r:i for i,r in enumerate(sites)};Haxis=[np.zeros((256,256),complex) for _ in range(3)]
for r in sites:
 for a in range(3):
  t=list(r);t[a]+=1;t=tuple(t)
  if t in ids:Haxis[a]-=kron([P[a] if i in (ids[r],ids[t]) else I for i in range(8)])
rows=[]
for lam in (.1,.5,1.):
 H=lam*(Haxis[0]+Haxis[1])+Haxis[2];h=W.conj().T@H@W;leak=H@W-W@h;e=np.linalg.eigvalsh(H)
 rows.append(dict(lam=lam,leakage_norm=float(np.linalg.norm(leak,2)),code_energy_mean=float(np.trace(h).real/8),best_eight_state_energy_mean=float(np.mean(e[:8])),code_internal_width=float(np.ptp(np.linalg.eigvalsh(h))),lowest_eight_gap=float(e[8]-e[7])))
assert all(r['leakage_norm']>1 for r in rows)
print(json.dumps(dict(physical_sites=8,code_dimension=8,ports=ports,axes=axes,alpha=float(1/np.sqrt(6)),compression_errors=errs,isometry_error=float(np.linalg.norm(W.conj().T@W-np.eye(8))),native_challenge=rows,scope='One explicitly chosen kinematic code fails native invariance; not a no-go for all large-feature encodings')))
