import sys, itertools, numpy as np
sys.argv=['x','4']
import corner_psg as C
import bloch as B
L=C.L; nV=len(C.VERTS)
F=dict(square=1,triangle=0,plaquette=1,tube=1)
def dmod(x): return ((x+1)%L)-1
ucell=B.solve(F)
u=np.zeros(C.nE,np.uint8)
for key,i in C.EID.items():
    a,b=tuple(key); (v,c),(w,c2)=C.VERTS[a],C.VERTS[b]
    u[i]=ucell[B.ekey[(c,c2,tuple(dmod(y-x) for x,y in zip(v,w)))]]
INV=-np.eye(3,dtype=int)
def psg(f): return C.psg_sign(f,u)
rots=[psg(lambda q,M=R: C.rot_vert(M,q)) for R in C.ROTS]
invs=[psg(lambda q,M=R@INV: C.rot_vert(M,q)) for R in C.ROTS]
TV=list(itertools.product(range(L),repeat=3))
trans=[psg(lambda q,t=t: C.trans_vert(t,q)) for t in TV]
def conj(Xm,P,s):
    sg=(-1.0)**s; Y=np.zeros_like(Xm); Y[np.ix_(P,P)]=Xm*np.outer(sg,sg); return Y
loc0=[C.VID[((0,0,0),c)] for c in C.CORNERS]
CI={c:i for i,c in enumerate(C.CORNERS)}
def H0(t1,t2):
    H=np.zeros((nV,nV))
    for key in C.EDGES:
        i,j=tuple(key); t=t1 if C.edges[key]=='onsite' else t2
        H[i,j]=H[j,i]=-t*(-1.0)**u[C.EID[key]]
    return H
def blocks_from(Hr):
    bl={}
    for a,v in enumerate(C.VERTS):
        sh=tuple(dmod(x) for x in v[0])
        for bi,j in enumerate(loc0):
            if abs(Hr[a,j])>1e-12: bl.setdefault(sh,np.zeros((12,12),complex))[CI[v[1]],bi]+=Hr[a,j]
    return bl
def Hk(bl,k):
    H=np.zeros((12,12),complex)
    for sh,M in bl.items(): H+=M*np.exp(1j*np.dot(k,sh))
    return H
par=np.array([(-1)**sum(v) for v,c in C.VERTS],float)
kst=np.array([1,-1,1])*np.pi/2; Q=np.array([np.pi]*3)
Xb=np.load('Xbasis.npy')
