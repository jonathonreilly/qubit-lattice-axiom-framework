"""Kill-check: walker sea H(k)=sigma.sin(k) (2 comps/site) on an LxLxL torus, APBC, planar-slab region as in the attack's m2_torus.py.
eta = S_A / (2 * L^2 * |n|)."""
import numpy as np, sys, time
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
sig=[sx,sy,sz]
def build(L):
    N=L**3; H=np.zeros((2*N,2*N),complex)
    idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i=idx(x,y,z)
                for a,(dx,dy,dz) in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
                    wrap = (x==L-1 and a==0) or (y==L-1 and a==1) or (z==L-1 and a==2)
                    s=-1.0 if wrap else 1.0
                    j=idx(x+dx,y+dy,z+dz)
                    blk=(-0.5j)*sig[a]*s
                    H[2*j:2*j+2,2*i:2*i+2]+=blk
                    H[2*i:2*i+2,2*j:2*j+2]+=blk.conj().T
    return H
def S_of_corr(C):
    nu=np.linalg.eigvalsh(C); nu=np.clip(nu,1e-14,1-1e-14)
    return float(-np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu)))
def run(L,orients):
    H=build(L); E,V=np.linalg.eigh(H)
    print("  min|E|=",np.min(np.abs(E)), " #neg=",int(np.sum(E<0)),"of",2*L**3)
    occ=V[:,E<0]; P=occ@occ.conj().T
    X,Y,Z=np.meshgrid(np.arange(L),np.arange(L),np.arange(L),indexing='ij')
    out={}
    for (h,k,l) in orients:
        q=(h*X+k*Y+l*Z)%L
        sites=np.where((q<L//2).ravel())[0]
        sel=np.concatenate([[2*s,2*s+1] for s in sites])
        S=S_of_corr(P[np.ix_(sel,sel)])
        out[(h,k,l)]=S/(2*L*L*np.sqrt(h*h+k*k+l*l))
    return out
if __name__=="__main__":
    L=int(sys.argv[1]); t=time.time()
    orients=[(1,0,0),(1,1,0),(1,1,1)]
    if len(sys.argv)>2: orients=[tuple(int(c) for c in s) for s in sys.argv[2].split(',')]
    r=run(L,orients); print(f"walker torus L={L}",{k:round(float(v),5) for k,v in r.items()},f"({time.time()-t:.1f}s)")
