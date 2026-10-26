"""Imported short-junction shape with full capacitive cavity coupling, GHz."""
import numpy as np
from scipy.linalg import eigh

def potential_coefficients(tau,N,grid=4096):
    phi=2*np.pi*np.arange(grid)/grid
    s=np.sin(phi/2)**2
    v=4*s/(1+np.sqrt(1-tau*s))
    c=np.fft.rfft(v).real/grid
    return c[:2*N+1]/(-2*c[1])

def endpoint(p,ng,N=16,M=14,K=9,grid=4096):
    ec,ej,omega,g,tau=p
    n=np.arange(-N,N+1,dtype=float)
    coeff=potential_coefficients(tau,N,grid)
    h=ej*coeff[np.abs(np.subtract.outer(np.arange(2*N+1),np.arange(2*N+1)))]+np.diag(4*ec*(n-ng)**2)
    e,v=eigh(h,subset_by_index=[0,M-1]);e-=e[0]
    charge=v.T@(n[:,None]*v)
    a=np.diag(np.sqrt(np.arange(1,K)),1)
    coupled=np.diag((omega*np.arange(K)[:,None]+e).ravel())+g*np.kron(a+a.T,charge)
    energy,vec=eigh(coupled)
    targets=[(0,j) for j in range(7)]+[(1,j) for j in range(7)]
    ix=[int(np.argmax(abs(vec[k*M+j])**2)) for k,j in targets]
    if len(set(ix))!=len(ix):raise ValueError('Nonunique bare-state assignment')
    weight=[float(abs(vec[k*M+j,i])**2) for (k,j),i in zip(targets,ix)]
    ee={t:energy[i] for t,i in zip(targets,ix)}
    f=np.array([ee[0,j]-ee[0,0] for j in range(1,7)]+[ee[1,j]-ee[0,j] for j in range(7)])
    return f,dict(min_weight=min(weight),weights=weight,indices=ix)

def predict(p,**kwargs):
    f0,a=endpoint(p,0,**kwargs);fh,b=endpoint(p,.5,**kwargs)
    return (f0+fh)/2,dict(ng0=f0.tolist(),ng_half=fh.tolist(),assignment_ng0=a,assignment_ng_half=b)
