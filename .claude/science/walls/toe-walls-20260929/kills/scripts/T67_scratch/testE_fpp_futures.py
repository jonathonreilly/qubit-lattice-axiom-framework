"""Kill-check T67: does the coupled (Richardson/FPP) clause have macroscopic futures?
Single seed (eps -> 0), open-ish torus large enough that wrap cannot matter (we measure futures of sources at distance r0 from the seed).
Same order definition as the attack: x<y iff a NN path with strictly increasing formation times.
"""
import numpy as np, time, sys
from numba import njit
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

def nbr_table(L):
    N=L**3; idx=np.arange(N).reshape(L,L,L); tab=np.empty((N,6),np.int64)
    for j,(ax,sh) in enumerate([(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1)]):
        tab[:,j]=np.roll(idx,sh,axis=ax).ravel()
    return tab

@njit(cache=True)
def sweep(order, rank, nbr, s, reach):
    N=order.shape[0]; reach[:]=False; reach[s]=True; cnt=1
    for r in range(rank[s]+1,N):
        y=order[r]
        for j in range(6):
            if reach[nbr[y,j]]:
                reach[y]=True; cnt+=1; break
    return cnt

def run(L, seed_rng, r0s, nsrc=12):
    N=L**3; nbr=nbr_table(L); rng=np.random.default_rng(seed_rng)
    W=rng.exponential(1.0,(N,3)); ii=np.arange(N)
    rows=[];cols=[];vals=[]
    for a in range(3):
        j=nbr[:,2*a]; rows+=[ii,j]; cols+=[j,ii]; vals+=[W[:,a],W[:,a]]
    G=csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(N,N))
    c0=L//2; seed=np.ravel_multi_index((c0,c0,c0),(L,L,L))
    T=dijkstra(G,directed=True,indices=seed)
    order=np.argsort(T); rank=np.empty(N,np.int64); rank[order]=np.arange(N)
    reach=np.zeros(N,np.bool_)
    coords=np.array(np.unravel_index(np.arange(N),(L,L,L)))  # 3 x N
    res={}
    for r0 in r0s:
        out=[]
        for _ in range(nsrc):
            # random direction, L-infinity-ish radius r0
            v=rng.normal(size=3); v/=np.linalg.norm(v)
            p=np.clip(np.round(c0+r0*v).astype(int),0,L-1)
            s=int(np.ravel_multi_index(tuple(p),(L,L,L)))
            c=sweep(order,rank,nbr,s,reach)
            ys=np.nonzero(reach)[0]
            d=coords[:,ys]-coords[:,[s]]
            ext=np.abs(d).max()
            # radial: how far beyond the source (in distance from seed) does the future reach
            rr=np.linalg.norm(coords[:,ys]-c0,axis=0)
            out.append((c, ext, rr.max()-np.linalg.norm(p-c0)))
        res[r0]=out
    return T,res

if __name__=="__main__":
    for L in [100, 140]:
        t0=time.time()
        T,res=run(L, 11, [8,16,24,36] if L==100 else [8,16,24,36,50])
        print(f"L={L} T range {T.max():.1f} ({time.time()-t0:.1f}s)")
        for r0,out in res.items():
            o=np.array(out)
            print(f"  source at distance r0={r0:3d}: future size median {np.median(o[:,0]):9.0f} mean {o[:,0].mean():9.0f} max {o[:,0].max():9.0f}; Linf extent median {np.median(o[:,1]):5.1f} max {o[:,1].max():4.0f}; radial reach beyond source median {np.median(o[:,2]):5.1f} max {o[:,2].max():5.1f}", flush=True)
