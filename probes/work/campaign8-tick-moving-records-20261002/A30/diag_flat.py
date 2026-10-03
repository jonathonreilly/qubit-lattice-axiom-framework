"""diagnostic: flat-face absorption split front/back; frame width and strength dependence."""
import signal, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import splu
signal.alarm(55)
t=1.0; N=128
X,Y=np.meshgrid(np.arange(N),np.arange(N),indexing='ij')
def solve(rec,Gam,k,frame):
    free=~rec; nfree=int(free.sum()); lab=-np.ones((N,N),dtype=np.int64); lab[free]=np.arange(nfree)
    E=-2*t*(np.cos(k)+1.0); phi=np.exp(1j*k*X)
    rows,cols=[],[]; nrec=np.zeros((N,N),dtype=np.int64); src=np.zeros((N,N),dtype=complex)
    for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]:
        Xn=(X+dx)%N; Yn=(Y+dy)%N
        m=free&free[Xn,Yn]; rows.append(lab[m]); cols.append(lab[Xn[m],Yn[m]])
        mr=free&rec[Xn,Yn]; nrec+=mr; src[mr]+=t*phi[Xn[mr],Yn[mr]]
    rows=np.concatenate(rows); cols=np.concatenate(cols)
    H=sp.csr_matrix((-t*np.ones(len(rows)),(rows,cols)),shape=(nfree,nfree))
    cap=free&(nrec>0); gam=np.where(cap,Gam,0.0); V=-0.5j*gam; src=src+V*phi
    A=sp.diags(E-V[free]+0.5j*frame[free])-H
    s=splu(A.tocsc()).solve(src[free]); psi=np.zeros((N,N),dtype=complex); psi[free]=phi[free]+s
    absb=gam*np.abs(psi)**2
    v=2*t*np.sin(k)
    return absb[79,:].sum()/v/N, absb[82,:].sum()/v/N
rec=np.zeros((N,N),dtype=bool); rec[80:82,:]=True
for W,Wmax in [(30,2.0),(36,1.5),(36,2.5)]:
    dx=np.minimum(X,N-1-X); fr=np.where(dx<W,Wmax*((W-dx)/W)**2,0.0)
    for k in [2*np.pi*m/N for m in (6,8,12,32,48,56)]:
        f,b=solve(rec,2.0,k,fr)
        V=-1j; R=-(t+V*np.exp(-1j*k))/(t+V*np.exp(1j*k))
        print(f"W={W} Wmax={Wmax} k={k:.4f}: front {f:.6f} back {b:.2e} exact {1-abs(R)**2:.6f}")
