import numpy as np, itertools, sys, time
from scipy.optimize import least_squares
from common import *
def setup(rng_r, group, j):
    N=[tuple(n) for n in itertools.product(range(-rng_r,rng_r+1),repeat=3)]
    idx={n:i for i,n in enumerate(N)}
    Ds=[lift(R,j) for R in group]; d=Ds[0].shape[0]
    # projector on equivariant families: X[n] -> avg D X[R^-1 n] D^dag
    rnd=np.random.default_rng(0)
    nb=0; cols=[]
    dimtot=len(N)*d*d
    # build basis via projecting unit vectors orbit-wise
    def proj(X):
        Y=np.zeros_like(X)
        for R,D in zip(group,Ds):
            Ri=R.T
            for n in N:
                Y[idx[n]]+=D@X[idx[tuple(Ri@np.array(n))]]@D.conj().T
        return Y/len(group)
    B=[]
    for k in range(dimtot):
        X=np.zeros((len(N),d,d),complex); X.flat[k]=1
        Y=proj(X).ravel()
        if np.linalg.norm(Y)>1e-9: B.append(Y)
    B=np.array(B).T
    # complex column space
    u,s,vh=np.linalg.svd(B,full_matrices=False); r=(s>1e-8).sum(); B=u[:,:r]
    return N,idx,d,B
def resid_fun(N,idx,d,B):
    L=len(N); r=B.shape[1]
    Nn=np.array(N)
    def A_of(x):
        c=x[:r]+1j*x[r:]; return (B@c).reshape(L,d,d)
    def res(x):
        A=A_of(x)
        # U U^dag coefficients: sum_n A_{n+m} A_n^dag ; compute via FFT on grid
        M=2*max(abs(Nn).max(),1)*2+1
        G=np.zeros((M,M,M,d,d),complex)
        for i,n in enumerate(N): G[n[0]%M,n[1]%M,n[2]%M]=A[i]
        F=np.fft.fftn(G,axes=(0,1,2))
        P=np.einsum('xyzab,xyzcb->xyzac',F,F.conj())-np.eye(d)
        P2=np.einsum('xyzba,xyzbc->xyzac',F.conj(),F)-np.eye(d)
        out=np.concatenate([P.ravel(),P2.ravel()])/np.sqrt(M**3)
        return np.concatenate([out.real,out.imag])
    return A_of,res
if __name__=="__main__":
    rr=int(sys.argv[1]); grp=sys.argv[2]; j=float(sys.argv[3]); ntry=int(sys.argv[4])
    G=rotations()
    if grp=='T': G=[R for R in G if any(all(abs(R[i,(i+s)%3])==1 for i in range(3)) for s in [0,1,2])]
    print('group size',len(G))
    t=time.time(); N,idx,d,B=setup(rr,G,j); print('basis dim (complex)',B.shape[1],time.time()-t)
    A_of,res=resid_fun(N,idx,d,B)
    rng=np.random.default_rng(int(sys.argv[5]) if len(sys.argv)>5 else 1)
    i0=idx[(0,0,0)]
    best=[]
    for t_ in range(ntry):
        x0=rng.normal(size=2*B.shape[1])*rng.uniform(0.1,1)
        sol=least_squares(res,x0,xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=20000)
        A=A_of(sol.x); mov=np.sqrt(sum(np.linalg.norm(A[i])**2 for i in range(len(N)) if i!=i0))
        print(t_, 'res %.2e'%np.linalg.norm(sol.fun),'moving weight %.3e'%mov, flush=True)
        if np.linalg.norm(sol.fun)<1e-10 and mov>1e-6:
            np.save('sol_%s_%d_%g_%d.npy'%(grp,rr,j,t_),sol.x)
