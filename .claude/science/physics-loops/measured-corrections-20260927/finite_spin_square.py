"""Exploratory closed compensated square, joint epsilon/spin scaling.
No cavity, noninteger offset or empirical microscopic-scale identification.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from itertools import combinations
import numpy as np
from scipy.linalg import eigh,eigh_tridiagonal
import json

def construct(S,K=1.,delta=1.):
    C=S*(S+1);eps=np.sqrt(delta/(K*C))
    edges=((0,1),(0,3),(2,1),(2,3))
    states=[]
    for occ in combinations(range(4),2):
        q=tuple(int(i in occ) for i in range(4))
        for n in range(-S,S+1):
            E=(n,q[0]-1-n,-q[1]-n,q[2]-1+q[1]+n)
            if max(map(abs,E))<=S:states.append((q,E))
    index={v:i for i,v in enumerate(states)}
    w=np.array([2-q[0]-q[2] for q,E in states]);p=np.flatnonzero(w==0)
    h=np.diag(w+4*eps**2*(w==0)).astype(float)
    for i,(q,E) in enumerate(states):
        for edge,(a,b) in enumerate(edges):
            if q[a]==1 and q[b]==0 and E[edge]>-S:
                qq=list(q);qq[a]=0;qq[b]=1;ee=list(E);ee[edge]-=1
                j=index[tuple(qq),tuple(ee)]
                amplitude=np.sqrt(1-E[edge]*(E[edge]-1)/C)
                h[i,j]-=eps*amplitude;h[j,i]-=eps*amplitude
    return h*(delta/eps**4),p,states,eps

def spectrum(S,K=1.,delta=1.,count=7):
    h,p,states,eps=construct(S,K,delta)
    e,v=eigh(h,subset_by_index=(0,count-1),driver='evr')
    residual=np.max(np.linalg.norm(h@v-v*e,axis=0))
    n=np.arange(-max(100,S),max(100,S)+1,dtype=float)
    reference=eigh_tridiagonal(4*K*n*n-4*delta,np.full(len(n)-1,-2*delta),select='i',select_range=(0,count-1))[0]
    return dict(S=S,dimension=len(states),epsilon=eps,energies=e.tolist(),gaps=(e[1:]-e[0]).tolist(),reference_gaps=(reference[1:]-reference[0]).tolist(),gap_difference=((e[1:]-e[0])-(reference[1:]-reference[0])).tolist(),minimum_P_weight=float(np.min(np.sum(v[p,:]**2,axis=0))),eigen_residual=float(residual))
if __name__=='__main__':
    for ratio in (1.,31.607246):
        for S in (12,20,32,50,80,120):
            r=spectrum(S,delta=ratio);r['delta_over_K']=ratio
            print(json.dumps(r),flush=True)
