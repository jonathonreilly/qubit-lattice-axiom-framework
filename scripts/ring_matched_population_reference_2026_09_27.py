"""Build the finite ring component and matched finite-age spectral reference.

No saved component or result is read. Full diagonalization and selected sparse
exponentials are floating diagnostics, not exact-real interval certificates.
"""
import numpy as np
import time
from scipy.sparse import coo_matrix,diags
from scipy.linalg import eigh
from scipy.sparse.linalg import expm_multiply
import ring_matched_population_kernel_2026_09_27 as kernel
AUDIT_TIMEOUT_SEC = 120


def build():
    ice=kernel.Ice(2);canon=ice.sector_state(0);bits=np.arange(ice.nl)
    code0=int(np.sum(((canon+1)//2)*(1<<bits)))
    masks=[sum(1<<int(l) for l in links) for links in ice.plaq]
    order=[code0];indices={code0:0};rows=[];cols=[];states=[];flips=[];q=0;t=time.time()
    while q<len(order):
        assert len(order)<=50000,'component ceiling exceeded; no truncation accepted'
        code=order[q];sig=((code>>bits)&1)*2-1;states.append(sig)
        fl=np.flatnonzero(np.abs((sig[ice.plaq]*ice.sign).sum(axis=1))==4);flips.append(len(fl))
        for j in fl:
            nxt=code^masks[j]
            if nxt not in indices:indices[nxt]=len(order);order.append(nxt)
            rows.append(indices[nxt]);cols.append(q)
        q+=1
    H=coo_matrix((-np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(q,q)).tocsr()
    assert (H-H.T).nnz==0
    S=np.array(states,dtype=np.int8);hv,_=kernel.triple(ice,np.pi);F=S@hv
    assert np.max(np.abs(F-np.rint(F)))<1e-12;F=np.rint(F).astype(np.int64)
    assert all(sum(int(S[k,l])*sign for l,sign in ice.inc[v])==0 for k in range(q) for v in range(ice.nv))
    comp=[indices.get(code^((1<<ice.nl)-1),-1) for code in order];assert min(comp)>=0
    assert np.array_equal(F[np.array(comp)],-F)
    assert q==864 and H.nnz==6912 and F[0]==16
    return ice,canon,hv,H,S,F,np.array(flips)


def reference(H,F,nf):
    H=H.astype(float);n=H.shape[0]
    ages=np.arange(1,2001)*.015
    means=np.empty((2,3));rows=[];checks=[]
    for j,h in enumerate([0.,.15,.30]):
        matrix=H-h*diags(F,dtype=float);dense=matrix.toarray()
        vals,vec=eigh(dense,driver='evr')
        residual=float(np.linalg.norm(dense@vec-vec*vals,ord='fro'))
        orth=float(np.linalg.norm(vec.T@vec-np.eye(n),ord='fro'))
        assert residual<1e-9 and orth<1e-9
        delta=vals-vals[0];decay=np.exp(-ages[:,None]*delta[None,:]);coeff=vec[0,:]
        for i,hguide in enumerate([.15,h]):
            logpsi=.2*nf+.5*hguide*F;psi=np.exp(logpsi-logpsi.max())
            amplitude=(psi@vec)*coeff;den=decay@amplitude;assert den.min()>0
            energy=vals[0]+(decay@(amplitude*delta))/den
            means[i,j]=np.mean(energy[500:2000])
            for t in (7.515,30.):
                e0=np.zeros(n);e0[0]=1
                y=expm_multiply(-(matrix-vals[0]*diags(np.ones(n)))*t,e0)
                alternate=float(psi@(matrix@y)/(psi@y));index=int(round(t/.015))-1
                diff=abs(alternate-energy[index]);assert diff<1e-10
                checks.append({'field':h,'guide':i,'age':t,'difference':diff})
        rows.append({'field':h,'ground_energy':float(vals[0]),'gap':float(vals[1]-vals[0]),'residual':residual,'orthogonality':orth})
    target=(15*means[:,0]-16*means[:,1]+means[:,2])/(9*8*.15**2)
    return {'energy_means':means.tolist(),'curvature_targets':target.tolist(),'spectral_diagnostics':rows,'alternate_checks':checks,'scope':'Matched finite-age finite-probe floating reference; no population-limit theorem or physical susceptibility.'}
