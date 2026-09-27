"""Independent raw-potential Fourier series and direct charge-photon check.
Adapted from independently checked exploratory source; no file reads.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix,diags,kron,eye
from scipy.sparse.linalg import eigsh
from scipy.optimize import linear_sum_assignment
labels=[(j,0) for j in range(7)]+[(j,1) for j in range(7)]

def potential(N,parameters):
    ec,ej,omega,g,tau=parameters
    coeff=np.zeros(2*N+1)
    if tau==0:coeff[1]=-.5*ej
    else:
        # sqrt(1-tau/2)*sqrt(1+rho*cos(phi)); Fourier coefficients
        # follow by binomial expansion and exact integer cos-power coefficients.
        # For frozen tau≈.155, rho≈.084; truncation at140 is negligible.
        rho=tau/(2-tau);binomial=1.;raw=np.zeros(2*N+1)
        for order in range(1,141):
            binomial*= (.5-(order-1))/order
            prefactor=-np.sqrt(1-tau/2)*binomial*rho**order/(2.**order)
            for k in range(1,min(order,2*N)+1):
                if (order-k)%2==0:raw[k]+=prefactor*math.comb(order,(order-k)//2)
        coeff[1:]=raw[1:]*(-ej/(2*raw[1]))
    return coeff

def solve(N,K,ng,parameters=None,fraction=1,previous=None):
    ec,ej,omega,g,tau=parameters;n=np.arange(-N,N+1,dtype=float)
    coeff=potential(N,parameters)
    hc=coeff[np.abs(np.subtract.outer(np.arange(len(n)),np.arange(len(n))))]+np.diag(4*ec*(n-ng)**2)
    _,barevec=eigh(hc)
    a=diags(np.sqrt(np.arange(1,K)),1,shape=(K,K),format='csr')
    h=kron(csr_matrix(hc),eye(K))+kron(eye(len(n)),diags(omega*np.arange(K)))+g*fraction*kron(diags(n),a+a.T)
    energy,v=eigsh(h,k=50,which='SA',tol=1e-12,v0=np.random.default_rng(270926).normal(size=h.shape[0]))
    order=np.argsort(energy);energy=energy[order];v=v[:,order]
    bare=np.column_stack([np.kron(barevec[:,j],np.eye(K)[:,k]) for j,k in labels])
    overlaps=abs(bare.T@v)**2;indices=overlaps.argmax(axis=1)
    _,assigned=linear_sum_assignment(-overlaps)
    assert len(set(indices))==14 and np.array_equal(indices,assigned)
    weights=overlaps[np.arange(14),indices];assert min(weights)>.5
    continuation=None
    if previous is not None:
        _,tracked=linear_sum_assignment(-abs(previous.T@v)**2)
        continuation=bool(np.array_equal(tracked,indices));assert continuation
    levels=energy[indices];freq=np.r_[levels[1:7]-levels[0],levels[7:14]-levels[:7]]
    selected=v[:,indices]
    result=dict(N=N,K=K,ng=ng,coupling_fraction=fraction,frequencies_GHz=freq.tolist(),indices=indices.tolist(),weights=weights.tolist(),runner_up_weights=np.sort(overlaps,axis=1)[:,-2].tolist(),continuation_agrees=continuation,eigen_residual_max_GHz=float(np.linalg.norm(h@selected-selected*levels,axis=0).max()))
    return result,selected
