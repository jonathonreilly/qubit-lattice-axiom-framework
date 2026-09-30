"""Independent incidence-matrix Gauss construction and Schur checks; no author imports."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import itertools,json
import numpy as np
from scipy.linalg import eigh,eigh_tridiagonal
from pathlib import Path
EDGES=((0,1),(0,3),(2,1),(2,3))
INC=np.array([[1,1,0,0],[-1,0,-1,0],[0,0,1,1],[0,-1,0,-1]])
BG=np.array([1,0,1,0])

def build(S):
    # Choose first three edges; incidence at vertices 0 and 1 fixes q0,q1.
    # Enumerate last two occupancies, solve vertex 2 for the fourth edge,
    # then independently enforce all four Gauss equations.
    states=[]
    for e0,e1,e2 in itertools.product(range(-S,S+1),repeat=3):
        q0=1+e0+e1;q1=-e0-e2
        if q0 not in (0,1) or q1 not in (0,1):continue
        for q2,q3 in itertools.product((0,1),repeat=2):
            q=np.array([q0,q1,q2,q3]);e3=q2-1-e2
            E=np.array([e0,e1,e2,e3])
            if q.sum()==2 and abs(e3)<=S and np.array_equal(INC@E,q-BG):
                states.append((tuple(q),tuple(E)))
    index={st:i for i,st in enumerate(states)};d=len(states);C=S*(S+1)
    F={a:np.zeros((d,d)) for a in (0,2)}
    for j,(qt,Et) in enumerate(states):
        for k,(a,b) in enumerate(EDGES):
            if qt[a] and not qt[b] and Et[k]>-S:
                q=list(qt);E=list(Et);q[a]=0;q[b]=1;E[k]-=1
                i=index[(tuple(q),tuple(E))]
                F[a][i,j]=np.sqrt((S+Et[k])*(S-Et[k]+1)/C)
    w=np.array([2-q[0]-q[2] for q,E in states]);P=np.flatnonzero(w==0)
    compensation=np.zeros((d,d))
    for a in (0,2):
        gram=F[a].T@F[a]
        dinf=np.array([q[a]*sum(1-q[b] for aa,b in EDGES if aa==a) for q,E in states])
        gate=np.array([q[2-a] for q,E in states])
        compensation+=(gram-np.diag(np.diag(gram))+np.diag(dinf))*gate[None,:]
    T=-F[0]-F[2]-F[0].T-F[2].T
    return states,w,P,T,compensation

checks=[]
for S in (3,5,8):
    states,w,P,T,comp=build(S);Q=np.flatnonzero(w==1);R=np.flatnonzero(w==2)
    A=T[np.ix_(Q,P)];B=T[np.ix_(R,Q)];n=np.array([states[i][1][0] for i in P]);C=S*(S+1)
    Z=B@A;M=A.T@A;N=Z.T@Z
    expected_M=np.diag(4-4*n*n/C)
    expected_N=np.diag(4*((1-n*(n-1)/C)**2+(1-n*(n+1)/C)**2))
    for i,ni in enumerate(n):
        for j,nj in enumerate(n):
            if nj==ni+1:expected_N[i,j]=expected_N[j,i]=4*(1-ni*(ni+1)/C)**2
    # Z formula at spin boundaries requires nonexistent outputs to be omitted;
    # on retained P endpoints amplitudes to them are already zero.
    checks.append(dict(S=S,dimension=len(states),gauss_verified=True,
        compensation_max_error=float(abs(comp-np.diag(4*(w==0))).max()),
        M_max_error=float(abs(M-expected_M).max()),N_max_error=float(abs(N-expected_N).max())))

spectra=[]
for S in (12,24,48):
    states,w,P,T,comp=build(S)
    for delta in (1.,31.607246):
        K=1.;x=delta/(K*S*(S+1));h=np.diag(w)+np.sqrt(x)*T+x*comp
        e,v=eigh(h,subset_by_index=(0,6),driver='evr');physical=e*delta/x**2
        residual=float(np.linalg.norm(h@v-v*e,axis=0).max()*delta/x**2)
        n=np.arange(-80,81,dtype=float)
        e0,v0=eigh_tridiagonal(4*K*n*n-4*delta,np.full(len(n)-1,-2*delta),select='i',select_range=(0,6))
        diagonal=8*delta-8*K*n*n;adjacent=4*delta+4*K*n[:-1]*(n[:-1]+1)
        shifts=np.sum(diagonal[:,None]*v0**2,axis=0)+2*np.sum(adjacent[:,None]*v0[:-1]*v0[1:],axis=0)
        remainder=(physical[1:]-physical[0])-(e0[1:]-e0[0])-x*(shifts[1:]-shifts[0])
        spectra.append(dict(S=S,delta=delta,x=x,maximum_gap_remainder=float(abs(remainder).max()),remainder_over_x2=float(abs(remainder).max()/x**2),eigen_residual=residual))
print(json.dumps(dict(exact_block_checks=checks,spectral_checks=spectra),indent=2))

AUDIT_TIMEOUT_SEC = 180
