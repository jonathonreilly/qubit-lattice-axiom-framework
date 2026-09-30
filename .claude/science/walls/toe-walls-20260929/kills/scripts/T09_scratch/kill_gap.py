"""Kill check on 'with a Hamiltonian the qubit works' vs the wall target 'massless AND massive modes'.
For each covariant nearest-neighbour Hermitian H family (attack's own basis), minimise over the family
(unit-normalised random parameters) the max-over-k... we ask: is there any parameter point where the
lowest spectral GAP between the two/four bands is bounded away from zero on the whole torus AND the
band has a Dirac-like massive form?  Here: just report min over k of the interband gap for random draws."""
import numpy as np
from scipy.linalg import null_space
from common import *
def herm_basis(names):
    s,b0,bN=covariant_basis(names); n0=len(b0); nN=len(bN); nb=n0+nN
    rng=np.random.default_rng(3); ks=rng.uniform(-np.pi,np.pi,size=(12,3))
    Ms=[]
    for j in range(nb):
        M=np.zeros((len(ks),s,s),complex)
        if j<n0: M+=b0[j][None]
        else:
            d=bN[j-n0]
            for di,v in enumerate(DIRS): M+=np.exp(1j*(ks@v))[:,None,None]*d[di][None]
        Ms.append(M)
    cols=[]
    for j in range(nb):
        for ph in (1.0,1j):
            H=ph*Ms[j]; D=H-np.conj(np.transpose(H,(0,2,1)))
            cols.append(np.concatenate([D.real.ravel(),D.imag.ravel()]))
    N=null_space(np.array(cols).T)
    return s,n0,nN,N,b0,bN
def Hk(coefs,s,n0,b0,bN,k):
    c=np.array(coefs); # complex coefficients length nb
    H=np.zeros((s,s),complex)
    for j in range(n0): H+=c[j]*b0[j]
    for j in range(len(bN)):
        d=bN[j]
        for di,v in enumerate(DIRS): H+=c[n0+j]*np.exp(1j*(k@v))*d[di]
    return H
rng=np.random.default_rng(1)
KG=rng.uniform(-np.pi,np.pi,size=(4000,3))
for names in (['H1'],['E'],['H1','H1'],['G'],['H1','H2']):
    s,n0,nN,N,b0,bN=herm_basis(names); nb=n0+nN
    worst_gap=[]
    for trial in range(60):
        v=N@rng.normal(size=N.shape[1])
        c=v[0:2*nb:2]+1j*v[1:2*nb:2] if False else None
        # cols were ordered (x_j, y_j) pairs => coefficient c_j = x_j + i y_j
        xs=v[0::2]; ys=v[1::2]; c=xs+1j*ys
        gaps=[]
        for k in KG[:800]:
            e=np.linalg.eigvalsh(Hk(c,s,n0,b0,bN,k)); gaps.append(np.min(np.diff(e)))
        worst_gap.append(min(gaps))
    print(f"{'+'.join(names):6s} s={s} family dim {N.shape[1]}: over 60 random covariant H, min interband gap on 800 k-samples: max over draws = {max(worst_gap):.4f}, median = {np.median(worst_gap):.4f}")
