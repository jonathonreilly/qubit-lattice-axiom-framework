import numpy as np, time
from engine import *
for dims in [(4,4,4,4),(6,6,6,6)]:
    lat=Lat(dims); rng=np.random.default_rng(1)
    U=random_su3(rng,(4,lat.V)); f=Fermion(lat,0.1); f.prep(U)
    psi=rng.normal(size=(lat.V,3))+1j*rng.normal(size=(lat.V,3))
    n=200
    t=time.time()
    for _ in range(n): f.D(psi)
    print(dims,'matmul D',(time.time()-t)/n)
    def D2(psi):
        pf=psi[lat.fwd]; pb=psi[lat.bwd]
        t1=np.einsum('mvij,mvj->mvi',f.U,pf,optimize=False)
        t2=np.einsum('mvij,mvj->mvi',f.Ub,pb,optimize=False)
        return 0.5*np.sum(lat.ef*t1-lat.eb*t2,axis=0)
    t=time.time()
    for _ in range(n): D2(psi)
    print(dims,'einsum D',(time.time()-t)/n, np.abs(D2(psi)-f.D(psi)).max())
    # split-component trick: store U as 9 arrays
    Ur=[[f.U[:,:,i,j] for j in range(3)] for i in range(3)]
    Ubr=[[f.Ub[:,:,i,j] for j in range(3)] for i in range(3)]
    def D3(psi):
        pf=psi[lat.fwd]; pb=psi[lat.bwd]   # (4,V,3)
        out=np.empty((lat.V,3),complex)
        for i in range(3):
            t1=Ur[i][0]*pf[...,0]+Ur[i][1]*pf[...,1]+Ur[i][2]*pf[...,2]
            t2=Ubr[i][0]*pb[...,0]+Ubr[i][1]*pb[...,1]+Ubr[i][2]*pb[...,2]
            out[:,i]=0.5*np.sum(lat.ef[...,0]*t1-lat.eb[...,0]*t2,axis=0)
        return out
    t=time.time()
    for _ in range(n): D3(psi)
    print(dims,'comp D',(time.time()-t)/n, np.abs(D3(psi)-f.D(psi)).max())
