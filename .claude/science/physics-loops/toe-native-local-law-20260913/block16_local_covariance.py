"""Challenge fixed local free covariance and Abel normalization independently."""
from pathlib import Path
import numpy as np,json
from scipy.integrate import quad

sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);one=np.eye(2)
sig=[np.kron(one,s) for s in [sx,sy,sz]];tx=np.kron(sx,one);tz=np.kron(sz,one)
on=2.6*sig[2]+.2*tx@(.8*sig[0]+.6*sig[2])
Cs=np.array([-.8*sig[0]-.6*sig[2],-sig[2],-sig[2]])
Ss=np.array([tz@(.6*sig[0]-.8*sig[2]),sig[1],np.zeros((4,4))])
ds=np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])


def covariances(L,phi):
    k=np.indices((L,L,L)).reshape(3,-1).T*2*np.pi/L+np.array(phi)/L
    H=on+np.einsum('ni,ijk->njk',np.cos(k),Cs)+np.einsum('ni,ijk->njk',np.sin(k),Ss)
    e,v=np.linalg.eigh(H)
    occupied=v[:,:,:2];P=occupied@occupied.conj().transpose(0,2,1)
    dressed=np.einsum('nd,nij->dij',np.exp(1j*k@ds.T),P)/(L**3)
    canonical=np.exp(-1j*ds@np.array(phi)/L)[:,None,None]*dressed
    return dressed,canonical


rows=[]
for L in [8,16,32]:
    base,_=covariances(L,[0,0,0])
    for phi in [[0,np.pi,0],[np.pi,np.pi,np.pi]]:
        dressed,canonical=covariances(L,phi)
        rows.append(dict(L=L,phi=phi,dressed_max_difference=float(np.max(abs(dressed-base))),
                         canonical_max_difference=float(np.max(abs(canonical-base)))))
abel=[]
for radius in [.7,1.,2.3]:
    for epsilon in [.2,.05]:
        endpoint=50/epsilon
        tail=np.exp(-epsilon*endpoint)*(endpoint**2/epsilon+2*endpoint/epsilon**2+2/epsilon**3)
        assert tail<1e-12
        value,error=quad(lambda q:q*q*np.exp(-epsilon*q),0,endpoint,weight='sin',wvar=radius,epsabs=1e-9,limit=300)
        exact=(2/(epsilon-1j*radius)**3).imag
        assert abs(value-exact)<1e-7
        abel.append(dict(radius=radius,epsilon=epsilon,quadrature=value,closed_form=exact,reported_error=error,absolute_tail_bound=tail,finite_endpoint=endpoint))
out=dict(covariance_samples=rows,independent_Abel_quadrature=abel,
         limitation='Finite free-state checks; no interacting phase, uniform rate or full reciprocal tail certification.')
p=Path(__file__).resolve().parent;(p/'BLOCK16_LOCAL_COVARIANCE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
