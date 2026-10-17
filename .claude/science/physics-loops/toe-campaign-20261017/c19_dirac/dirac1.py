"""Search for O x I x translation invariant, complex-conjugation-odd one-fermion terms (range <= 1 site)."""
import sys, itertools, numpy as np
sys.argv=['x','4']
import corner_psg as C
import bloch as B
L=C.L; nV=len(C.VERTS)
F=dict(square=1,triangle=0,plaquette=1,tube=1)
ucell=B.solve(F)
def dmod(x): return ((x+1)%L)-1     # map to {-1,0,1,2}
u=np.zeros(C.nE,np.uint8)
for key,i in C.EID.items():
    a,b=tuple(key); (v,c),(w,c2)=C.VERTS[a],C.VERTS[b]
    sh=tuple(dmod(y-x) for x,y in zip(v,w))
    u[i]=ucell[B.ekey[(c,c2,sh)]]
# check fluxes of the L=4 gauge reproduce F
for k,cs in C.cycles.items():
    vals={int(sum(u[j] for j in c)%2) for c in cs}
    assert vals=={F[k]}, (k,vals)
INV=-np.eye(3,dtype=int)
def psg(f): return C.psg_sign(f,u)
group=[]
for R in C.ROTS:
    for Ig in (False,True):
        M=R@INV if Ig else R
        P,s=psg(lambda q,M=M: C.rot_vert(M,q))
        assert s is not None
        group.append((P,s))
trans=[]
for t in itertools.product(range(L),repeat=3):
    P,s=psg(lambda q,t=t: C.trans_vert(t,q)); trans.append((P,s))
assert all(len(set(s.tolist()))==1 for P,s in trans), "translations should act without gauge signs in this gauge"
def conj(Xm,P,s):
    sg=(-1.0)**s
    Y=np.zeros_like(Xm); Y[np.ix_(P,P)]=Xm*np.outer(sg,sg); return Y
SID={v:i for i,v in enumerate(C.SITES)}
def site_dist_ok(a,b):
    v,w=C.VERTS[a][0],C.VERTS[b][0]
    d=[abs(dmod(y-x)) for x,y in zip(v,w)]
    return max(d)<=1 and sum(d)<=1
rng=np.random.default_rng(0)
def symmetrize(Xm):
    Y=np.zeros_like(Xm)
    for P,s in trans: Y+=conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for P,s in group: Z+=conj(Y,P,s)
    return Z/(len(trans)*len(group))
# seeds restricted to site 0 corners and its 6 neighbours
loc0=[C.VID[((0,0,0),c)] for c in C.CORNERS]
nbr=[C.VID[(tuple(x%L for x in d),c)] for d in [(0,0,0)]+[tuple(e) for e in C.DIRS] for c in C.CORNERS]
basis=[]
for trial in range(14):
    A=np.zeros((nV,nV))
    for i in loc0:
        for j in nbr:
            if i!=j and site_dist_ok(i,j): A[i,j]=rng.normal()
    A=A-A.T
    X=symmetrize(1j*A)
    basis.append(X)
V=np.array([b.ravel() for b in basis])
sv=np.linalg.svd(V,compute_uv=False)
print('K-odd, I-even, O x T invariant terms (range <= 1 site): singular values', np.round(sv[:14]/sv[0],6))
np.save('Xbasis.npy', np.array(basis[:6]))
np.save('u_L4.npy', u)
