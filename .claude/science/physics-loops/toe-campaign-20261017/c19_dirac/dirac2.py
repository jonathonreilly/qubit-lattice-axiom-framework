import sys, itertools, numpy as np
sys.argv=['x','4']
import corner_psg as C
L=C.L; nV=len(C.VERTS)
u=np.load('u_L4.npy'); Xb=np.load('Xbasis.npy')
def dmod(x): return ((x+1)%L)-1
CI={c:i for i,c in enumerate(C.CORNERS)}
def H0(t1,t2):
    H=np.zeros((nV,nV))
    for key in C.EDGES:
        i,j=tuple(key); t=t1 if C.edges[key]=='onsite' else t2
        H[i,j]=H[j,i]=-t*(-1.0)**u[C.EID[key]]
    return H
def blochify(Hr):
    """12x12 Bloch blocks: dict shift -> matrix, from columns at site 0."""
    blocks={}
    cols=[C.VID[((0,0,0),c)] for c in C.CORNERS]
    for a,v in enumerate(C.VERTS):
        sh=tuple(dmod(x) for x in v[0])
        for bi,j in enumerate(cols):
            val=Hr[a,j]
            if abs(val)>1e-12:
                blocks.setdefault(sh,np.zeros((12,12),complex))[CI[v[1]],bi]+=val
    assert all(max(abs(x) for x in sh)<=1 for sh in blocks)
    return blocks
def Hk(blocks,k):
    H=np.zeros((12,12),complex)
    for sh,M in blocks.items(): H+=M*np.exp(1j*np.dot(k,sh))
    return H
rng=np.random.default_rng(5)
coef=rng.normal(size=len(Xb)); X=np.tensordot(coef,Xb,1); X/=np.abs(X).max()
kst=np.array([1,-1,1])*np.pi/2
def chern_sphere(f,k0,band,r=0.02,n=24):
    # Fukui-Hatsugai-Suzuki on a sphere around k0 for a single band
    th=np.linspace(0,np.pi,n+1); ph=np.linspace(0,2*np.pi,2*n,endpoint=False)
    U=np.empty((n+1,2*n),dtype=object)
    for i,t in enumerate(th):
        for j,p in enumerate(ph):
            k=k0+r*np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])
            w,v=np.linalg.eigh(f(k)); U[i,j]=v[:,band]
    tot=0
    for i in range(n):
        for j in range(2*n):
            a,b,c,d=U[i,j],U[i+1,j],U[i+1,(j+1)%(2*n)],U[i,(j+1)%(2*n)]
            tot+=np.angle(np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a))
    return tot/(2*np.pi)
for t1,t2,delta in ((-1.0,0.2,0.05),(-1.0,0.3,0.1)):
    Hr=H0(t1,t2)+delta*X
    assert np.allclose(Hr,Hr.conj().T)
    bl=blochify(Hr); f=lambda k: Hk(bl,k)
    for name,k0 in (('k*',kst),('-k*',-kst)):
        e=np.linalg.eigvalsh(f(k0))
        # dispersion of the lowest pair along random directions
        dirs=rng.normal(size=(4,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
        spl=[np.round((np.linalg.eigvalsh(f(k0+0.01*dd))[1]-np.linalg.eigvalsh(f(k0+0.01*dd))[0])/0.01,4) for dd in dirs]
        ch=chern_sphere(f,k0,0)
        print(f't1={t1} t2={t2} delta={delta} {name}: lowest {np.round(e[:4],5)}; splitting/|dk| along 4 dirs {spl}; Berry flux of lowest band through sphere {ch:+.3f}')
