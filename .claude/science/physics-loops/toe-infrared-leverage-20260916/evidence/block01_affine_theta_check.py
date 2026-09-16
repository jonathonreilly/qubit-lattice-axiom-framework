#!/usr/bin/env python3
"""Independent finite challenges of a proposed all-affine Gauss dressing.
Finite sums and cutoff comparisons are numerical evidence, not uniform proofs.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_FILES = []
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh


def cube(L):
    verts=list(itertools.product(range(L+1),repeat=3)); vi={v:i for i,v in enumerate(verts)}
    edges=[(x,i) for x in verts for i in range(3) if x[i]<L]; ei={e:i for i,e in enumerate(edges)}
    faces=[(x,i,j) for x in verts for i in range(3) for j in range(i+1,3) if x[i]<L and x[j]<L]
    cubes=[x for x in verts if all(t<L for t in x)]
    def step(x,i):
        y=list(x);y[i]+=1;return tuple(y)
    D=np.zeros((len(verts),len(edges)),dtype=int)
    for l,(x,i) in enumerate(edges):D[vi[x],l]=1;D[vi[step(x,i)],l]=-1
    C=np.zeros((len(faces),len(edges)),dtype=int);fi={f:i for i,f in enumerate(faces)}
    for p,(x,i,j) in enumerate(faces):
        for e,s in [((x,i),1),((step(x,i),j),1),((step(x,j),i),-1),((x,j),-1)]:C[p,ei[e]]=s
    B=np.zeros((len(cubes),len(faces)),dtype=int)
    for k,x in enumerate(cubes):
        for i,j,t in [(0,1,2),(1,0,2),(2,0,1)]:
            s=(-1)**i;B[k,fi[step(x,i),j,t]]=s;B[k,fi[x,j,t]]=-s
    return D,C,B


def matfun(M,p,zero=1e-10):
    w,v=eigh(M.astype(float)); q=np.zeros_like(w);q[w>zero]=w[w>zero]**p
    return (v*q)@v.T


def integer_cycles(D):
    # Every edge added by union-find either joins a tree or closes a cycle.
    nv,ne=D.shape; parent=list(range(nv)); tree=[];chords=[]
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for e in range(ne):
        x,y=np.flatnonzero(D[:,e]);a,b=root(x),root(y)
        if a==b:chords.append(e)
        else:parent[a]=b;tree.append(e)
    out=np.zeros((ne,len(chords)),dtype=int)
    for j,e in enumerate(chords):
        out[e,j]=1; coeff=np.linalg.lstsq(D[:,tree],-D[:,e],rcond=None)[0]
        assert np.max(np.abs(coeff-np.rint(coeff)))<1e-12
        out[tree,j]=np.rint(coeff).astype(int)
    assert np.max(np.abs(D@out))==0
    return out


def points(r,M):
    # Chunking prevents construction of the full rank-five product in memory.
    tail=np.array(list(itertools.product(range(-M,M+1),repeat=r-1)),dtype=float)
    for n in range(-M,M+1):yield np.column_stack((np.full(len(tail),n),tail))


def direct(B,K,a,g,M,t=None):
    z=0.;m=np.zeros(len(a));s=np.zeros((len(a),len(a)));over=0.
    for p in points(B.shape[1],M):
        n=p@B.T+a;w=np.exp(-g*g*np.einsum('ni,ij,nj->n',n,K,n))
        z+=w.sum();m+=w@n;s+=(n.T*w)@n
        if t is not None:over+=np.exp(-g*g/2*(np.einsum('ni,ij,nj->n',n,K,n)+np.einsum('ni,ij,nj->n',n+t,K,n+t))).sum()
    return z,m/z,s/z,over


def dual(B,A,a,g,M):
    dualbasis=B@np.linalg.inv(B.T@B);th=0j;d=np.zeros(len(a),complex);dd=np.zeros((len(a),len(a)),complex)
    for n in points(B.shape[1],M):
        eta=n@dualbasis.T;w=np.exp(-math.pi**2/g**2*np.einsum('ni,ij,nj->n',eta,A,eta)+2j*math.pi*(eta@a))
        th+=w.sum();d+=2j*math.pi*(w@eta);dd+=-4*math.pi**2*(eta.T*w)@eta
    assert abs(th.imag)<1e-12 and th.real>0
    grad=d/th;hess=dd/th-np.outer(grad,grad)
    assert max(np.max(abs(grad.imag)),np.max(abs(hess.imag)))<1e-10
    return float(th.real),grad.real,hess.real


def run():
    started=time.time();D,C,B=cube(1);cycles=integer_cycles(D)
    assert cycles.shape==(12,5) and np.max(abs(D@C.T))==0 and np.max(abs(B@C))==0
    A=matfun(C.T@C,.5);K=matfun(C.T@C,-.5);P=A@K;H2=C@C.T+B.T@B
    Db=cycles@np.linalg.inv(cycles.T@cycles);q=C@Db
    dual_metric_error=float(np.linalg.norm(Db.T@A@Db-q.T@matfun(H2,-.5)@q))
    assert dual_metric_error<1e-12
    c0=1/(2*math.sqrt(12));T=(A-c0*A@A)/2
    split_error=float(np.linalg.norm(T-C.T@(matfun(H2,-.5)-c0*np.eye(len(C)))@C/2))
    assert split_error<1e-12
    Q=D[:,0]+2*D[:,4]-D[:,8];E0=np.zeros(D.shape[1]);E0[[0,4,8]]=[1,2,-1]
    eQ=D.T@np.linalg.pinv(D@D.T)@Q;a=P@E0;t=P[:,3]
    assert np.linalg.norm(E0-eQ-a)<1e-12
    cases=[]
    for g,M in [(.9,7),(1.3,6),(1.8,5)]:
        z,mean,moment,ov=direct(cycles,K,a,g,M,t)
        z2,m2,s2,_=direct(cycles,K,a,g,M+2)
        th,grad,hess=dual(cycles,A,a,g,3)
        th4,_,_=dual(cycles,A,a,g,4)
        G=cycles.T@K@cycles
        pref=(math.pi/g**2)**(cycles.shape[1]/2)/math.sqrt(np.linalg.det(G))
        mp=-A@grad/(2*g*g);sp=A/(2*g*g)+A@hess@A/(4*g**4)+np.outer(mp,mp)
        thend,_,_=dual(cycles,A,a+t,g,4);thmid,_,_=dual(cycles,A,a+t/2,g,4)
        zend=direct(cycles,K,a+t,g,M)[0]
        overlap_direct=ov/math.sqrt(z*zend)
        overlap_pred=math.exp(-g*g*t@K@t/4)*thmid/math.sqrt(th4*thend)
        row={'g':g,'primal_cutoff':M,'cutoff_relative_change':abs(z2/z-1),'poisson_relative_error':abs(z/(pref*th4)-1),'mean_error':float(np.linalg.norm(mean-mp)),'second_moment_error':float(np.linalg.norm(moment-sp)),'overlap_error':abs(overlap_direct-overlap_pred),'theta':th4,'centered_only_overlap_error':abs(overlap_direct-math.exp(-g*g*t@K@t/4)),'dual_cutoff_change':abs(th-th4)}
        assert row['poisson_relative_error']<2e-8, row
        assert row['mean_error']<2e-7 and row['second_moment_error']<2e-6, row
        assert row['overlap_error']<1e-8, row
        cases.append(row)
    assert cases[-1]['centered_only_overlap_error']>1e-4
    bounds=[]
    for L in [1,2,3,4]:
        DL,CL,BL=cube(L);HL=DL.T@DL+CL.T@CL;KL=matfun(CL.T@CL,-.5);AL=matfun(CL.T@CL,.5)
        gl=matfun(DL@DL.T,-1);r=int(np.linalg.matrix_rank(CL))
        row={'L':L,'cells':[len(DL),len(CL.T),len(CL),len(BL)],'cycle_rank':r,'K_diagonal_max':float(np.diag(KL).max()),'trace_coulomb_per_vertex':float(np.trace(gl)/len(DL)),'K_below_H1_inverse_sqrt_min':float(np.linalg.eigvalsh(matfun(HL,-.5)-KL).min())}
        assert row['K_diagonal_max']<=14 and row['trace_coulomb_per_vertex']<=7/4
        assert row['K_below_H1_inverse_sqrt_min']>-1e-11
        bounds.append(row)
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dual_metric_error':dual_metric_error,'fractional_gaussian_split_error':split_error,'affine_cases':cases,'free_cube_bounds':bounds,'seconds':time.time()-started},indent=2))

if __name__=='__main__':run()
