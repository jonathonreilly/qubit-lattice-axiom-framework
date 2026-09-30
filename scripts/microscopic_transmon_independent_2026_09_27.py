"""Direct spatial/phase projection and full charge-photon check; supplied circuit."""
import numpy as np
from scipy.linalg import eigh

AUDIT_TIMEOUT_SEC = 600

def solve(p,q,N,K,grid,mode):
 ec,js,alpha,w,g,tau,psi=p;n=np.arange(-N,N+1);phi=2*np.pi*np.arange(grid)/grid
 rawpot=-np.cos(phi) if tau==0 else -np.sqrt(1-tau*np.sin(phi/2)**2)
 c1=np.mean(rawpot*np.cos(phi))
 x,weights=np.polynomial.legendre.leggauss(64 if grid==4096 else 128)
 def local(t): return -np.cos(t) if tau==0 else -np.sqrt(1-tau*np.sin(t/2)**2)
 # Independent real-space rectangular averages: phase ramp spans +/-pi B/Bnode.
 pot=np.zeros(grid)
 for J,Bnode,phase in [(js*(1+alpha)/2,.8,0),(js*(1-alpha)/2,.8*256/178,psi)]:
  pot+=J*(-1/(2*c1))*(local(phi[:,None]+phase+np.pi*.15/Bnode*x)@(weights/2) if mode=='spatial' else np.sinc(.15/Bnode)*local(phi+phase))
 pot-=pot.mean()
 F=np.exp(1j*phi[:,None]*n)/np.sqrt(grid)
 hd=(F.conj().T*pot)@F+np.diag(4*ec*(n-q)**2);de,du=eigh(hd)
 a=np.diag(np.sqrt(np.arange(1,K)),1)
 H=np.kron(hd,np.eye(K))+np.kron(np.eye(len(n)),np.diag(w*np.arange(K)))+g*np.kron(np.diag(n-q),a+a.T)
 E,U=eigh(H,subset_by_index=[0,30])
 bare=np.column_stack([np.kron(du[:,j],np.eye(K)[:,0]) for j in range(4)])
 ov=abs(bare.conj().T@U)**2;ix=np.argmax(ov,axis=1)
 if len(set(ix)) != 4:
  raise ValueError("nonunique independent dressed labels")
 return dict(q=q,gaps_GHz=(E[ix[1:]]-E[ix[0]]).tolist(),indices=ix.tolist(),weights=ov[np.arange(4),ix].tolist(),eigen_residual_GHz=float(np.linalg.norm(H@U[:,ix]-U[:,ix]*E[ix],axis=0).max()))
