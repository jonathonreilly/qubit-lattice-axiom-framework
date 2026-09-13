from pathlib import Path
import json,numpy as np
P=Path(__file__).resolve().parent
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
def chern_slice(M,N):
 k=np.arange(N)*2*np.pi/N-np.pi;X,Y=np.meshgrid(k,k,indexing='ij');d=np.stack([np.sin(X),np.sin(Y),M-np.cos(X)-np.cos(Y)],axis=-1)
 h=np.einsum('...a,aij->...ij',d,S);energies,U=np.linalg.eigh(h);u=U[...,0]
 def link(axis):
  overlap=np.sum(u.conj()*np.roll(u,-1,axis=axis),axis=-1);return overlap/abs(overlap),float(abs(overlap).min())
 Ux,mx=link(0);Uy,my=link(1);flux=np.angle(Ux*np.roll(Uy,-1,axis=0)/(np.roll(Ux,-1,axis=1)*Uy))
 # Direct differentiated projector/Kubo curvature, independent of eigenvector
 # phases and of the four-corner topological formula.
 dx=np.stack([np.cos(X),np.zeros_like(X),np.sin(X)],axis=-1);dy=np.stack([np.zeros_like(X),np.cos(Y),np.sin(Y)],axis=-1)
 berry=-np.sum(d*np.cross(dx,dy),axis=-1)/(2*np.linalg.norm(d,axis=-1)**3)
 direct=float(np.mean(berry)*2*np.pi)
 return dict(M=M,N=N,link_C=float(np.sum(flux)/(2*np.pi)),Kubo_C=direct,min_overlap=min(mx,my),gap=float(np.min(abs(energies))))
if __name__=='__main__':
 rows=[chern_slice(M,N) for M in [.7,1.4,1.8,2.2,2.8,3.7] for N in [24,48,96]]
 (P/'BLOCK10_HALL_EXPLORATION.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
