"""O x I x T invariant conjugation-odd terms with |shift|_inf <= 1 (27-site cube), and A2 masses of the same range."""
from diraclib import *
rng=np.random.default_rng(0)
def sym(Xm, inversion=True):
    Y=np.zeros_like(Xm)
    for P,s in trans: Y+=conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for P,s in rots: Z+=conj(Y,P,s)
    if inversion: Z=(Z+conj(Z,*invs[0]))/2
    return Z
nbr=[C.VID[(tuple(x%L for x in d),c)] for d in itertools.product((-1,0,1),repeat=3) for c in C.CORNERS]
def seed():
    A=np.zeros((nV,nV))
    for i in loc0:
        for j in nbr:
            if i!=j: A[i,j]=rng.normal()
    return A-A.T
B=[sym(1j*seed()) for _ in range(60)]
M=np.array([b.ravel() for b in B]); U_,sv,Vt=np.linalg.svd(M,full_matrices=False)
r=int(np.sum(sv>1e-8*sv[0])); print('range |sh|_inf<=1: rank of invariant conjugation-odd terms', r)
basis=[(Vt[i]).reshape(nV,nV) for i in range(r)]
basis=[(b+b.conj().T)/2 for b in basis]
np.save('Xbasis2.npy',np.array(basis))
# also real (conjugation-even) invariant terms of the same range, for the kinetic part
Br=[sym(seed()+seed().T) for _ in range(60)]
Mr=np.array([b.ravel() for b in Br]); _,svr,Vtr=np.linalg.svd(Mr,full_matrices=False); rr=int(np.sum(svr>1e-8*svr[0]))
print('rank of invariant real (conjugation-even) terms', rr)
np.save('Rbasis2.npy',np.array([(Vtr[i].reshape(nV,nV)+Vtr[i].reshape(nV,nV).T)/2 for i in range(rr)]))
