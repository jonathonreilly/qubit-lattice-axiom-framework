# Independent implementation, written from the statements (LW1 sec.1 definitions), not from ZM1 proofs.
import numpy as np, itertools
from scipy.linalg import expm, logm
RES=[tuple(r) for r in itertools.product((0,1),repeat=3)]
IDX={r:i for i,r in enumerate(RES)}
def eta(j,x): return (-1)**(sum(x[:j])%2)
def Rfib(K,T):
    """Bloch fibre of R_T (T='e' or 'o') from the real-space definition; |K,r>=sum_b e^{iK.b}|2b+r>."""
    M=np.zeros((8,8),complex)
    for r in RES:
        for j in range(3):
            for sgn in (+1,-1):
                y=list(r); y[j]+=sgn
                lower = r if sgn==1 else tuple(y)
                own = 'e' if lower[j]%2==0 else 'o'
                if own!=T: continue
                b=[yi//2 for yi in y]; rp=tuple(yi%2 for yi in y)
                M[IDX[rp],IDX[r]] += eta(j,lower)*np.exp(-1j*np.dot(K,b))/np.sqrt(3)
    return M
def Vfib(K,eps,mu=0.0):
    ae=eps-mu/2; ao=eps+mu/2
    return expm(1j*ao*Rfib(K,'o'))@expm(-1j*ae*Rfib(K,'e'))
def hfib(K,eps): return 1j*logm(Vfib(K,eps))
def AZG():
    A=[];Z=[];G=[]
    for j in range(3):
        a=np.zeros((8,8),complex); z=np.zeros((8,8),complex)
        for r in RES:
            z[IDX[r],IDX[r]]=(-1)**r[j]
            if r[j]==0:
                rp=list(r); rp[j]=1; rp=tuple(rp)
                a[IDX[rp],IDX[r]]+=eta(j,r); a[IDX[r],IDX[rp]]+=eta(j,r)
        A.append(a);Z.append(z);G.append(1j*z@a)
    return A,Z,G
def GC(eps):
    A,Z,Gm=AZG(); s=np.sin(eps); c=np.cos(eps)
    R=sum(A)/np.sqrt(3); E=expm(-1j*eps*R)
    G=[g@E for g in Gm]
    C=[s/(2*np.sqrt(3))*(c*A[j]-1j*s/np.sqrt(3)*sum(A[j]@A[k] for k in range(3) if k!=j)) for j in range(3)]
    return G,C
def Ytr(th,eps):
    G,C=GC(eps); v=np.sin(eps)/np.sqrt(3)
    return 1j/(2*v)*sum(np.sin(th[j])*G[j]@C[j] for j in range(3))
nrm=lambda M: np.linalg.norm(M,2)
