"""Task 1+2: standard 2-component Wilson-Dirac overlap, LxL torus, uniform U(1) flux n."""
import numpy as np
def idx(x,y,L): return x*L+y

def gauge(L,n):
    def U1(x,y): return np.exp(-1j*2*np.pi*n*y/(L*L))
    def U2(x,y): return np.exp(1j*2*np.pi*n*x/L) if y==L-1 else 1.0+0j
    return U1,U2

def plaq_check(L,n):
    U1,U2=gauge(L,n); tot=0.0; vals=[]
    for x in range(L):
        for y in range(L):
            P=U1(x,y)*U2((x+1)%L,y)*np.conj(U1(x,(y+1)%L))*np.conj(U2(x,y))
            vals.append(np.angle(P)); tot+=np.angle(P)
    return np.max(vals)-np.min(vals), tot/(2*np.pi)

def wilson_dirac_2d(L,n,r=1.0,a=1.0):
    s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
    s3=np.array([[1,0],[0,-1]],dtype=complex); g=[s1,s2]; I2=np.eye(2,dtype=complex)
    N=L*L; D=np.zeros((2*N,2*N),dtype=complex); U1,U2=gauge(L,n)
    for x in range(L):
        for y in range(L):
            i=idx(x,y,L); D[2*i:2*i+2,2*i:2*i+2]+=(2*r/a)*I2
            for mu,(dx,dy) in enumerate([(1,0),(0,1)]):
                j=idx((x+dx)%L,(y+dy)%L,L); U=U1(x,y) if mu==0 else U2(x,y)
                D[2*i:2*i+2,2*j:2*j+2]+=-(1/(2*a))*(r*I2-g[mu])*U
                D[2*j:2*j+2,2*i:2*i+2]+=-(1/(2*a))*(r*I2+g[mu])*np.conj(U)
    return D, np.kron(np.eye(N),s3)

def overlap(DW,mrho,a=1.0):
    A=DW-(mrho/a)*np.eye(DW.shape[0])
    U,S,Vh=np.linalg.svd(A); V=U@Vh
    return (1.0/a)*(np.eye(DW.shape[0])+V), S, V

def report(L,mrho,a=1.0,r=1.0,tag=""):
    print(f"=== Wilson-Dirac overlap {tag} L={L} m_rho={mrho} a={a} r={r} ===")
    sp,ft=plaq_check(L,1); print(f"  gauge check n=1: plaq-angle spread={sp:.2e}  total flux/2pi={ft:.6f}")
    print(f"{'n':>3} {'g5herm':>10} {'GWviol':>11} {'|aD|max':>8} {'minSV(A)':>10} {'index_tr':>11} {'nzero':>6} {'n+':>3} {'n-':>3}")
    for n in [0,1,2,3]:
        DW,G5=wilson_dirac_2d(L,n,r=r,a=a)
        gh=np.max(np.abs(G5@DW@G5-DW.conj().T))
        Dov,S,V=overlap(DW,mrho,a=a)
        gw=np.max(np.abs(G5@Dov+Dov@G5 - a*(Dov@G5@Dov)))
        ind=0.5*np.real(np.trace(G5@(2*np.eye(Dov.shape[0])-a*Dov)))
        # exact zero modes = V eigenvalue -1
        w,vecs=np.linalg.eig(V); k=np.where(np.abs(w+1)<1e-8)[0]
        npl=nmi=0
        if len(k):
            Q,_=np.linalg.qr(vecs[:,k]); M=Q.conj().T@G5@Q; ev=np.linalg.eigvalsh(M)
            npl=int(np.sum(ev>0.5)); nmi=int(np.sum(ev<-0.5))
        print(f"{n:>3} {gh:10.2e} {gw:11.3e} {np.max(np.abs(a*Dov)):8.3f} {S.min():10.3e} {ind:11.6f} {len(k):>6} {npl:>3} {nmi:>3}")

if __name__=="__main__":
    report(8,1.0,tag="")
    report(10,1.0,tag="")
