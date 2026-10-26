import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, pickle, time
from engine import *

sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.diag([1,-1]).astype(complex)
SIGMA=[sx,sy]

def idx(N):
    return lambda rx,ry: (rx%N)*N+(ry%N)

def build(N,m1,m2,R=4):
    """fiber operators on torus Z_N^2 x C^4 at K=2 pi (m1,m2)/N. returns H2 (compressed), J (full), J0 (free scalar two-step), O etc."""
    K=2*np.pi*np.array([m1,m2])/N
    n=N*N
    # translation shifts on r: (S_e phi)(r)=phi(r-e)
    def shift(ex,ey):
        rows=[];cols=[]
        for rx in range(N):
            for ry in range(N):
                rows.append(((rx+ex)%N)*N+((ry+ey)%N)); cols.append(rx*N+ry)
        return sp.csr_matrix((np.ones(n),(rows,cols)),shape=(n,n))   # |r+e><r|
    E=[(1,0),(0,1)]
    I2=np.eye(2)
    H=sp.csr_matrix((4*n,4*n),dtype=complex)
    # record 1: |x1+e><x1|: coefficient (i/2) sigma_a ; |x1-e>: -(i/2) sigma_a ; r -> r+-e, coin on c1
    # record 2: x2 -> x2+-e: r -> r -+ e, and phase e^{iK x2}: amplitude picks e^{-+iK.e}?  psi=e^{iK x2}phi(r); (h2 psi)(y)=sum_x H_{yx}psi(x)
    for a,(ex,ey) in enumerate(E):
        Sp=shift(ex,ey); Sm=shift(-ex,-ey)
        sa=SIGMA[a]
        # record1
        H=H+sp.kron(Sp,np.kron(sa,I2))*(0.5j)+sp.kron(Sm,np.kron(sa,I2))*(-0.5j)
        # record2: moving x2 -> x2+e: new r = r - e ; new fiber function phase: psi'(y)=e^{iK y2}phi'(y1-y2): amplitude from x2=y2-e: e^{iK(y2-e)}phi(r+... )
        # state |x1,x2> -> |x1,x2+e> (coefficient (i/2) sigma_a on c2).  Take psi=e^{iK x2}phi(r). Contribution to phi'(r') : phi(r'+e)? work in operator form:
        #   (h2 psi)(y1,y2) = (i/2) s psi(y1,y2-e) - (i/2) s psi(y1,y2+e) = e^{iK y2}[ (i/2) s e^{-iK.e} phi(r+e) - (i/2) s e^{+iK.e} phi(r-e) ]
        ke=K[a]
        H=H+sp.kron(Sm,np.kron(I2,sa))*(0.5j*np.exp(-1j*ke))+sp.kron(Sp,np.kron(I2,sa))*(-0.5j*np.exp(1j*ke))
    # careful: record1 operator: (h1 psi)(y)=(i/2)s psi(y1-e,y2) - (i/2) s psi(y1+e,y2): phi'(r)=(i/2)s phi(r-e) - (i/2)s phi(r+e) -> uses |r+e><r| for phi(r-e) : Sp ok
    P=sp.diags(np.where(np.repeat(np.arange(n),4)==0,0.0,1.0)).tocsr()   # remove r=0 (all coin states)
    H2=P@H@P
    return K,H,H2,P

if __name__=="__main__":
    N=8
    K,H,H2,P=build(N,1,1)
    print("hermitian:",abs(H-H.getH()).max())


def jtable(excl, comp, rmax):
    W=Walk(2,2,[(0,1)] if excl else [])
    tab={}
    for rx in range(-rmax,rmax+1):
        for ry in range(-rmax,rmax+1):
            for c1 in range(2):
                for c2 in range(2):
                    st=(((rx,ry),c1),((0,0),c2))
                    if excl and not W.allowed(st): continue
                    tab[(rx,ry,c1,c2)]=W.J8({st:(1,0)},comp)
    return tab

def build_J(N,K,comp,R=4):
    n=N*N
    tex=jtable(True,comp,R)
    W=Walk(2,2,[])
    far=(11,11)
    templ={}
    for c1 in range(2):
        for c2 in range(2):
            st=((far,c1),((0,0),c2))
            templ[(c1,c2)]=W.J8({st:(1,0)},comp)
    rows=[];cols=[];vals=[]
    for rx in range(N):
        for ry in range(N):
            rr=(rx if rx<=N//2 else rx-N, ry if ry<=N//2 else ry-N)
            for c1 in range(2):
                for c2 in range(2):
                    col=(rx*N+ry)*4+c1*2+c2
                    if max(abs(rr[0]),abs(rr[1]))<=R:
                        if (rr[0],rr[1],c1,c2) not in tex: continue   # excluded (r=0) column: zero
                        ent=tex[(rr[0],rr[1],c1,c2)].items()
                    else:
                        ent=[]
                        for t,a in templ[(c1,c2)].items():
                            (z1,d1),(z2,d2)=t
                            z1n=(rr[0]+z1[0]-far[0], rr[1]+z1[1]-far[1])
                            ent.append((((z1n,d1),(z2,d2)),a))
                    for t,a in ent:
                        (z1,d1),(z2,d2)=t
                        rp=((z1[0]-z2[0])%N,(z1[1]-z2[1])%N)
                        ph=np.exp(-1j*(K[0]*z2[0]+K[1]*z2[1]))
                        rows.append((rp[0]*N+rp[1])*4+d1*2+d2); cols.append(col)
                        vals.append(complex(a[0],a[1])*ph*0.125j)     # J = (i/8) J8
    J=sp.csr_matrix((vals,(rows,cols)),shape=(4*n,4*n))
    return J
