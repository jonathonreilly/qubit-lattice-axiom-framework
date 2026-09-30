"""Kill-check T67: the attack's nucleation clause (rate eps spontaneous + rate 1 per recorded neighbour)
at larger L: do futures grow as eps -> 0? (The attack found Linf extent 16..40 at L=80 and read that as bounded;
40 = L/2 is the torus wrap limit.)"""
import numpy as np, time
from testE_fpp_futures import nbr_table, sweep
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
def run(L, eps, nsrc, seed):
    N=L**3; nbr=nbr_table(L); rng=np.random.default_rng(seed)
    W=rng.exponential(1.0,(N,3)); X=rng.exponential(1.0/eps,N); ii=np.arange(N)
    rows=[];cols=[];vals=[]
    for a in range(3):
        j=nbr[:,2*a]; rows+=[ii,j]; cols+=[j,ii]; vals+=[W[:,a],W[:,a]]
    src=N; rows.append(np.full(N,src)); cols.append(ii); vals.append(X)
    G=csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(N+1,N+1))
    T=dijkstra(G,directed=True,indices=src)[:N]
    order=np.argsort(T); rank=np.empty(N,np.int64); rank[order]=np.arange(N)
    reach=np.zeros(N,np.bool_)
    coords=np.array(np.unravel_index(np.arange(N),(L,L,L)))
    ex=[];sz=[]
    for s in rng.choice(N,nsrc,replace=False):
        c=sweep(order,rank,nbr,int(s),reach); ys=np.nonzero(reach)[0]
        d=coords[:,ys]-coords[:,[s]]; d=(d+L//2)%L-L//2
        ex.append(np.abs(d).max()); sz.append(c)
    return np.array(ex),np.array(sz),T
L=160
for eps in [1e-3,1e-4,1e-5,1e-6]:
    t0=time.time(); ex,sz,T=run(L,eps,40,3)
    print(f"L={L} eps={eps:g}: Linf extent median {np.median(ex):5.1f} p90 {np.percentile(ex,90):5.1f} max {ex.max():4.0f} (wrap limit {L//2}); future size median {np.median(sz):9.0f} max {sz.max():9.0f}; eps^(-1/4)={eps**-0.25:5.1f}; T max {T.max():.1f} ({time.time()-t0:.0f}s)",flush=True)
