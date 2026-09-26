"""Supplied transmon plus full capacitive resonator model, GHz energy units."""
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal

def endpoint(p,ng,N=14,M=12,K=9,scale_G=1.0):
    ec,ej,omega,g=p
    charges=np.arange(-N,N+1,dtype=float)
    e,v=eigh_tridiagonal(4*ec*(charges-ng)**2,np.full(2*N,-ej/2),select='i',select_range=(0,M-1))
    e-=e[0]
    charge=v.T@(charges[:,None]*v)
    osc=np.diag(np.sqrt(np.arange(1,K)),1)
    h=np.diag((omega*np.arange(K)[:,None]+e[None,:]).ravel())+g*scale_G*np.kron(osc+osc.T,charge)
    energy,vec=eigh(h,driver='evr')
    # Bare product labels (k,m), matched to their dominant dressed eigenstate.
    targets=[(0,j) for j in range(7)]+[(1,0),(1,1)]
    ix=[int(np.argmax(abs(vec[k*M+j,:])**2)) for k,j in targets]
    if len(ix)!=len(set(ix)):raise ValueError('Nonunique spectral assignment')
    weights=[float(abs(vec[k*M+j,i])**2) for (k,j),i in zip(targets,ix)]
    labels={f'{k},{j}':int(i) for (k,j),i in zip(targets,ix)}
    ee={t:energy[i] for t,i in zip(targets,ix)}
    f=[ee[0,j]-ee[0,0] for j in range(1,7)]+[ee[1,0]-ee[0,0],ee[1,1]-ee[0,1]]
    return np.array(f),dict(labels=labels,weights=weights,min_weight=min(weights))

def predict(p,N=14,M=12,K=9):
    x,a=endpoint(p,0,N,M,K);y,b=endpoint(p,.5,N,M,K)
    return (x+y)/2,dict(ng0=x.tolist(),ng_half=y.tolist(),assignment_ng0=a,assignment_ng_half=b)
CAL_INDEX=[0,1,6,7]
