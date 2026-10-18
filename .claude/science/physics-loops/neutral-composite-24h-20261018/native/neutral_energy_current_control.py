"""Finite native spin-algebra and spectral continuity controls; no fitted data."""
import numpy as np,json
from itertools import product
L=(2,2,2);sites=list(product(*(range(n) for n in L)));index={r:i for i,r in enumerate(sites)};N=len(sites);dim=1<<N
I=np.eye(2);pauli=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
def op(items):
 a=np.array([[1.+0j]])
 for i in range(N):a=np.kron(a,pauli[items[i]] if i in items else I)
 return a
bonds=[]
for r in sites:
 for ax,j in enumerate((.37,.37,1.)):
  t=list(r);t[ax]+=1;t=tuple(t)
  if t not in index:continue
  bonds.append((-.0+j,np.array(r,float)/2+np.array(t,float)/2,index[r],index[t],ax))
hs=[-j*op({i:ax,k:ax}) for j,r,i,k,ax in bonds];H=sum(hs);evals,U=np.linalg.eigh(H);g=U[:,0]
rows=[]
for q in (np.zeros(3),np.array([.31,.47,.83]),np.array([.7,-.2,.11])):
 E=sum(np.exp(-1j*q@r)*h for (_,r,_,_,_),h in zip(bonds,hs))/np.sqrt(N)
 current=[np.zeros_like(H) for a in range(3)]
 for a,(ja,ra,ia,ka,aa) in enumerate(bonds):
  for b,(jb,rb,ib,kb,ab) in enumerate(bonds):
   shared={ia,ka}&{ib,kb}
   if len(shared)!=1 or aa==ab:continue
   comm=hs[a]@hs[b]-hs[b]@hs[a]
   center=next(iter(shared));othera=ka if ia==center else ia;otherb=kb if ib==center else ib
   ac=3-aa-ab;epsilon=1 if (aa,ab,ac) in ((0,1,2),(1,2,0),(2,0,1)) else -1
   expected=2j*ja*jb*epsilon*op({center:ac,othera:aa,otherb:ab})
   assert np.linalg.norm(comm-expected)<1e-12
   d=rb-ra;factor=1j*np.sinc((q@d)/(2*np.pi))*np.exp(-1j*q@(ra+rb)/2)/(2*np.sqrt(N))
   for ax in range(3):current[ax]+=factor*d[ax]*comm
 residual=np.linalg.norm(H@E-E@H+sum(q[a]*current[a] for a in range(3)))
 assert residual<1e-11
 amplitudes=U.conj().T@E@g
 jamp=U.conj().T@sum(q[a]*current[a] for a in range(3))@g
 spectral=np.max(np.abs((evals-evals[0])*amplitudes+jamp));assert spectral<1e-11
 rows.append(dict(q=q.tolist(),operator_residual=float(residual),spectral_residual=float(spectral)))
q=np.array([.31,.47,.83]);Fop=sum(np.cos(q@r)*h for (_,r,_,_,_),h in zip(bonds,hs))/np.sqrt(N)
a=U.conj().T@Fop@g;gap=evals-evals[0];mask=gap>1e-9;chi=2*sum(abs(a[mask])**2/gap[mask]);eps=1e-3
curvature=-(np.linalg.eigvalsh(H+eps*Fop)[0]+np.linalg.eigvalsh(H-eps*Fop)[0]-2*evals[0])/eps**2
assert abs(chi-curvature)<1e-6
print(json.dumps(dict(sites=N,bonds=len(bonds),continuity=rows,hermitian_source_susceptibility=float(chi),finite_field_ground_curvature=float(curvature))))
