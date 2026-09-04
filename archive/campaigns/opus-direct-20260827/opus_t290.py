"""
T288 - T281 rerun, memory-fixed and checkpointed.

T281 died at 0.0% CPU on its last row (L=72,p=0.70) and, because it saved only
after ALL rows, lost every raw Rtil it had computed. Two defects, both mine:
  1. build() accumulated ~2.2M-element PYTHON LISTS per axis (r,c,v) -- hundreds
     of MB of boxed floats at L=72. Replaced with flat numpy arrays.
  2. no incremental write. Each (L,p) row is now checkpointed to its own .npy
     the moment it completes, so a death costs one row, not the run.
"""
import numpy as np, time, os
from scipy.sparse import coo_matrix, diags
from scipy.sparse.csgraph import connected_components
from numpy.polynomial.legendre import leggauss
XS,WS=leggauss(24)
def integ(f,lo,hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    q=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(q),axis=1)

def build(L,eps,keep):
    """numpy-only assembly (T281 used python lists here and ran out of memory)"""
    kap=2*np.pi/L; t=np.arange(L,dtype=float)
    W  =lambda x:(1.0+eps*np.cos(kap*x))**0.5
    Rho=lambda x:(1.0+eps*np.cos(kap*x))**1.5
    w0=integ(W,t,t+1.0); wt=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    i,j,k=np.indices((L,L,L)); N=L**3
    flat=lambda a,b,c:((a%L)*L+(b%L))*L+(c%L)
    a=flat(i,j,k).ravel(); x0=i.ravel()
    R=[];C=[];V=[]; dg=np.zeros(N)
    for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
        b=flat(i+di,j+dj,k+dk).ravel(); ww=(w0 if ax==0 else wt)[x0]
        live=keep[a]&keep[b]
        aa=a[live]; bb=b[live]; ww=ww[live]
        R.append(aa); R.append(bb); C.append(bb); C.append(aa); V.append(-ww); V.append(-ww)
        np.add.at(dg,aa,ww); np.add.at(dg,bb,ww)
    R.append(np.arange(N)); C.append(np.arange(N)); V.append(dg)
    A=coo_matrix((np.concatenate(V),(np.concatenate(R),np.concatenate(C))),shape=(N,N)).tocsr()
    return A, m[x0]

def giant(L,p,seed):
    N=L**3
    if p>=1.0: return np.ones(N,bool)
    rng=np.random.default_rng(seed); keep=rng.random(N)<p
    A,_=build(L,0.0,keep); idx=np.where(keep)[0]
    nc,lab=connected_components(A[idx][:,idx],directed=False)
    g=np.zeros(N,bool); g[idx[lab==np.argmax(np.bincount(lab))]]=True; return g

def cheb_trace(B,svals,Z,lmax,chunk=8):
    """memory-lean: probes in chunks, in-place recursion, no acc array.
    T281/T288-v1 kept 4 arrays of (n x 32) float64 alive (380 MB at L=72) plus
    temporaries, on a machine with 66 MB free -- which is why they stalled at
    0% CPU with RSS collapsing: swapped out, not computing."""
    order=int(1.35*max(svals)*lmax/2)+70
    d=e=lmax/2; nz=Z.shape[1]
    kk=np.arange(order+1); th=np.pi*(kk+0.5)/(order+1); xk=np.cos(th)
    C=np.zeros((len(svals),order+1))
    for a,sv in enumerate(svals):
        fk=np.exp(-sv*(d*xk+e))
        C[a]=[(2.0/(order+1))*np.sum(fk*np.cos(q*th)) for q in range(order+1)]
        C[a,0]/=2
    out=np.zeros(len(svals))
    for c0 in range(0,nz,chunk):
        Zc=np.ascontiguousarray(Z[:,c0:c0+chunk])
        T0=Zc.copy(); T1=(B@Zc-e*Zc)/d
        out+=C[:,0]*np.sum(Zc*T0)+C[:,1]*np.sum(Zc*T1)
        for q in range(2,order+1):
            T2=B@T1; T2-=e*T1; T2*=2.0/d; T2-=T0
            out+=C[:,q]*np.sum(Zc*T2); T0,T1=T1,T2
        del Zc,T0,T1
    return out/nz

def K_pure(L,s):
    k=2*np.pi*np.arange(L)/L
    return np.array([np.sum(np.exp(-sv*2*(1-np.cos(k))))**3 for sv in s])

xs=np.array([0.10,0.16,0.24,0.34,0.46]); h=0.05
for L in (48,):
    kap=2*np.pi/L; s=xs/kap**2
    for p in (1.00,0.85,0.70):
        fn=f"t290_{L}_{int(p*100)}.npy"
        if os.path.exists(fn): print(f"  L={L} p={p:.2f} cached"); continue
        t0=time.time()
        g=giant(L,p,11); idx=np.where(g)[0]; n=len(idx)
        rng=np.random.default_rng(101); Z=rng.choice([-1.0,1.0],size=(n,32))
        Ks={};Vs={}
        for ei in (-2,-1,0,1,2):
            A,m=build(L,ei*h,g); ms=m[idx]
            Dm=diags(1.0/np.sqrt(ms)); B=(Dm@A[idx][:,idx]@Dm).tocsr()
            del A
            lmax=float(abs(B).sum(axis=1).max())*1.02
            Ks[ei]=cheb_trace(B,s,Z,lmax); Vs[ei]=ms.sum(); del B
        d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
        Rtil=(4*np.pi*s)**1.5*d2(Ks)/d2(Vs)
        D=(K_pure(L,s)/Ks[0])**(2.0/3.0)
        np.save(fn,np.vstack([Rtil,D,np.full(len(s),n/L**3),s]))   # CHECKPOINT
        print(f"  L={L:3d} p={p:.2f} q={n/L**3:.4f}  D="+" ".join(f"{v:6.4f}" for v in D)
              +f"  Rtil="+" ".join(f"{v:7.4f}" for v in Rtil)+f"  [{time.time()-t0:.0f}s]",flush=True)
