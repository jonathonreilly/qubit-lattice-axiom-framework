#!/usr/bin/env python3
"""Literal position control of the projected N4 trial frame, NOT T0."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import time,json,resource,hashlib,itertools,math
from pathlib import Path
start=time.monotonic(); cpu=time.process_time(); p=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
import numpy as np
L=19; V=L**3; R=4
unit=np.eye(3,dtype=int)
D=[tuple(2*e) for e in unit]
planes=[]
for i in range(3):
    for j in range(i+1,3):
        plus=len(D);D.append(tuple(unit[i]+unit[j]));minus=len(D);D.append(tuple(unit[i]-unit[j]));planes.append((i,j,plus,minus))
U=np.zeros((9,5));U[0,:2]=(1/np.sqrt(2),1/np.sqrt(6));U[1,:2]=(-1/np.sqrt(2),1/np.sqrt(6));U[2,1]=-2/np.sqrt(6)
for k,(i,j,plus,minus) in enumerate(planes):U[plus,2+k]=-1/np.sqrt(2);U[minus,2+k]=1/np.sqrt(2)
assert np.max(abs(U.T@U-np.eye(5)))<5e-16
basis=[]
for i in range(5):
    A=np.zeros((5,5));A[i,i]=1;basis.append(A)
for i in range(5):
    for j in range(i+1,5):
        A=np.zeros((5,5));A[i,j]=A[j,i]=1/np.sqrt(2);basis.append(A)
M=np.einsum('sa,kab,db->sdk',U,np.array(basis),U)
G0=np.einsum('sdk,sdl->kl',M,M)
assert np.max(abs(G0-np.eye(15)))<2e-15
coords=np.indices((L,L,L)).reshape(3,-1).T

def torus_distance(a,b):
    dif=(a-b+L//2)%L-L//2
    return np.max(abs(dif),axis=-1)

def matrices(F):
    sm=np.zeros((15,15));wm=sm.copy();jm=sm.copy()
    def outer_add(target,field,scale=1):
        v=field.reshape(V,15);target+=scale*(v.T@v)
    ax=[np.roll(F[i],1,axis=i) for i in range(3)]
    outer_add(sm,sum(ax),2/3)
    Q=[(ax[0]-ax[1])/np.sqrt(2),(ax[0]+ax[1]-2*ax[2])/np.sqrt(6)]
    for i,j,plus,minus in planes:
        vv=[]
        for s,t in itertools.product((-1,1),repeat=2):
            if s<0:
                ix=plus if t>0 else minus
                vv.append(-t*np.roll(F[ix],1,axis=i))
            else:
                ix=minus if t>0 else plus
                vv.append(t*np.roll(F[ix],-t,axis=j))
        for a,b in itertools.combinations(vv,2):outer_add(sm,a-b,.25)
        Q.append(sum(vv)/2)
    for q in Q:
        for j in range(3):outer_add(wm,np.roll(q,-1,axis=j)-q)
    for f in F:
        for j in range(3):outer_add(jm,np.roll(f,-1,axis=j)-f)
    return sm,wm,jm+sm

H=np.zeros((15,15));J=H.copy();G=H.copy();row_control=0
qs=[]
for s,ds in enumerate(D):
    q=[]
    for d in D:
        endpoint=(coords+np.array(d))%L
        distance=np.minimum.reduce((torus_distance(coords,0),torus_distance(coords,np.array(ds)),torus_distance(endpoint,0),torus_distance(endpoint,np.array(ds))))
        q.append((distance>R).reshape((L,L,L)))
    q=np.array(q);qs.append(q)
    F=q[...,None]*M[s,:,None,None,None,:]
    sm,wm,jm=matrices(F)
    H+=(2/V)*(sm+wm);J+=(2/V)*jm
    counts=q.reshape(9,V).sum(axis=1)
    G+=np.einsum('d,dk,dl->kl',counts,M[s],M[s])/V
    # Constant soft fields annihilate every complete physical S/W row.
    F0=np.broadcast_to(M[s,:,None,None,None,:],F.shape)
    sm0,wm0,jm0=matrices(F0)
    row_control=max(row_control,float(np.max(abs(sm0))+np.max(abs(wm0))))
assert row_control<2e-24
G=(G+G.T)/2;H=(H+H.T)/2
ge=np.linalg.eigvalsh(G);he=np.linalg.eigvalsh(H)
delta=(2*R+9)**3/V
sR=(2*R+9)**3-(2*R-7)**3
bound=60*2*sR*2/V
assert ge.min()>=1-delta-2e-13 and ge.max()<=1+2e-13
assert he.min()>-2e-12 and he.max()<=bound
# The exact single residual/removed axial guard face from the counterfamily.
q=qs[0][0]
faces=sum(int(np.count_nonzero(np.roll(q,-1,axis=j)!=q)) for j in range(3))
assert faces==24*R**2+56*R+22
# Frobenius normalization via literal ordered creation on sampled occupations.
rng=np.random.default_rng(902103)
A=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5));A=(A+A.T)/2;A/=np.linalg.norm(A)
max_creation_error=0.0; samples=0
for s,ds in enumerate(D):
    for d_idx,d in enumerate(D):
        allowed=np.flatnonzero(qs[s][d_idx].reshape(-1))
        if not len(allowed):continue
        x=coords[allowed[len(allowed)//2]]
        e1=frozenset((tuple(np.zeros(3,dtype=int)),tuple(np.array(ds)%L)))
        e2=frozenset((tuple(x),tuple((x+np.array(d))%L)))
        S=e1|e2; assert len(S)==4
        # Two explicit creator orders and all internal tensor entries.
        literal=0j
        for aa,bb in itertools.product(range(5),repeat=2):
            literal+=A[aa,bb]*(U[s,aa]*U[d_idx,bb]+U[d_idx,aa]*U[s,bb])/(np.sqrt(2)*V)
        predicted=np.sqrt(2)*(U@A@U.T)[s,d_idx]/V
        max_creation_error=max(max_creation_error,abs(literal-predicted));samples+=1
assert max_creation_error<2e-19
out={'scope':'N4 projected trial frame only; NOT threshold T0, NOT an all-N spectrum or a finite check of the large-radius isolation premise',
'L':L,'V':V,'R':R,'mu':1,'tau':1,'internal_dimension':15,
'Gram_eigenvalues':ge.tolist(),'trial_quadratic_eigenvalues':he.tolist(),'Gram_union_bound_delta':delta,'trial_bound_B1':bound,'constant_soft_row_max':row_control,'literal_complex_creation_samples':samples,'literal_complex_creation_max_error':max_creation_error,'axial_guard_boundary_edges':faces,
'Gram_matrix':G.tolist(),'H_trial_matrix':H.tolist(),'J_trial_matrix':J.tolist(),
'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert out['peak_rss_bytes']<150*1024*1024
(p/'periodic_frame.json').write_text(json.dumps(out,indent=2)+'\n')
small={k:v for k,v in out.items() if not k.endswith('_matrix')}
print(json.dumps(small,indent=2))
