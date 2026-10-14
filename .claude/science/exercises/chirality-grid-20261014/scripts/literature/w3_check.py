# Sanity check (not a proof): 3D winding W3 of Bloch unitaries U(k): T^3 -> U(2).
# Strictly local (Laurent-polynomial) walks should give W3 = 0 (Read 2017 K-theory corollary);
# a quasi-local (normalized) map can give W3 = +-1 (single unpaired Weyl node at one quasienergy).
import numpy as np
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex); I2=np.eye(2)
def expi(k,s): return np.cos(k)[...,None,None]*I2+1j*np.sin(k)[...,None,None]*s
def W3(Ufun,N=48):
    k=2*np.pi*np.arange(N)/N; h=2*np.pi/N
    KX,KY,KZ=np.meshgrid(k,k,k,indexing='ij')
    U=Ufun(KX,KY,KZ)
    Ud=np.conj(np.swapaxes(U,-1,-2))
    D=[ (np.roll(U,-1,axis=a)-np.roll(U,1,axis=a))/(2*h) for a in range(3)]
    A=[Ud@d for d in D]
    eps=[(0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,-1),(2,1,0,-1),(1,0,2,-1)]
    tot=sum(s*np.trace(A[i]@A[j]@A[l],axis1=-2,axis2=-1) for i,j,l,s in eps)
    return (tot.sum()*h**3/(24*np.pi**2)).real
rng=np.random.default_rng(1)
def rand_su2():
    q=rng.normal(size=4); q/=np.linalg.norm(q)
    return q[0]*I2+1j*(q[1]*sx+q[2]*sy+q[3]*sz)
coins=[rand_su2() for _ in range(9)]
def shift(axis_k):  # spin-up moves +1, spin-down moves -1 along one axis (strictly local)
    out=np.zeros(axis_k.shape+(2,2),complex); out[...,0,0]=np.exp(1j*axis_k); out[...,1,1]=np.exp(-1j*axis_k); return out
tests={
 'Laurent: exp(ikx sx)exp(iky sy)exp(ikz sz)': lambda x,y,z: expi(x,sx)@expi(y,sy)@expi(z,sz),
 'Laurent: random coin+conditional-shift walk (depth 9)': lambda x,y,z: __import__('functools').reduce(lambda A,B:A@B,[coins[i]@shift(x if i%3==0 else y if i%3==1 else z) for i in range(9)]),
}
def normalized_wilson(M):
    def f(x,y,z):
        m=M-np.cos(x)-np.cos(y)-np.cos(z); n=np.sqrt(m**2+np.sin(x)**2+np.sin(y)**2+np.sin(z)**2)
        return (m[...,None,None]*I2+1j*(np.sin(x)[...,None,None]*sx+np.sin(y)[...,None,None]*sy+np.sin(z)[...,None,None]*sz))/n[...,None,None]
    return f
tests['quasi-local: normalized Wilson map M=2']=normalized_wilson(2.0)
tests['quasi-local: normalized Wilson map M=4 (trivial)']=normalized_wilson(4.0)
import sys
NN=int(sys.argv[1]) if len(sys.argv)>1 else 48
for name,f in tests.items():
    print(f"{name:60s} W3 ~ {W3(f,NN):+.4f}")
