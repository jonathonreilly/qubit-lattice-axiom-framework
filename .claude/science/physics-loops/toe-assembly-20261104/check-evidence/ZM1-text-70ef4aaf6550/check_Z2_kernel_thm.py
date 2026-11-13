# Lemma Z2.3 (kernel), covariance claim (5), Lemma Z2.4, Theorem Z2 (3),(4).
# Different implementation from the text: real-space psi; block fibre built directly from the hopping rule with
# twisted block boundary conditions (no use of the iota_m / alpha_m decomposition).
import numpy as np, itertools
from scipy.linalg import expm, logm
from check_common import *
rng=np.random.default_rng(7)
M=96  # coarse cells in the periodised 1D lattice used to tabulate psi
def kernel(L):
    N=L*M; a=np.zeros(N)
    box=np.zeros(N); box[:L]=1
    Gs=np.zeros(N)
    if L%2: 
        for n in range(-(L-1)//2,(L-1)//2+1): Gs[n%N]+=1
    else:
        for n in range(-(L//2-1),L//2): Gs[n%N]+=1
        Gs[(L//2)%N]+=.5; Gs[(-L//2)%N]+=.5
    ah=np.fft.fft(box)*np.fft.fft(Gs)          # hat a on xi=2 pi k/N
    g=np.array([np.sum(np.abs(ah[(k%M)+M*np.arange(L)])**2)/L for k in range(N)])  # g(L xi)
    psih=ah/np.sqrt(g); psi=np.fft.ifft(psih)
    return ah,g,psih,psi
def ahat(L,xi):
    B=sum(np.exp(-1j*n*xi) for n in range(L))
    if L%2: G=sum(np.exp(-1j*n*xi) for n in range(-(L-1)//2,(L-1)//2+1))
    else: G=sum(np.exp(-1j*n*xi) for n in range(-(L//2-1),L//2))+np.cos(L*xi/2)
    return B*G
def alphas(L,th):
    a=np.array([ahat(L,(th+2*np.pi*m)/L) for m in range(L)]); return a/np.sqrt(np.sum(abs(a)**2))
PSI={}
for L in [2,3,4,5,8]:
    ah,g,psih,psi=kernel(L); N=L*M
    im=np.max(abs(psi.imag)); psi=psi.real; PSI[L]=psi
    gram=max(abs(np.dot(psi,np.roll(psi,L*b))-(b==0)) for b in range(0,8))
    sym=max(abs(psi[n%N]-psi[(L-1-n)%N]) for n in range(-N//2,N//2))
    ths=np.linspace(-np.pi,np.pi,2001); ths=ths[abs(ths)>1e-6]
    leak=max((1-abs(alphas(L,t)[0])**2)/t**4 for t in ths)
    gmin=min(sum(abs(ahat(L,(t+2*np.pi*m)/L))**2 for m in range(L))/L for t in np.linspace(-np.pi,np.pi,2001))
    tail=max(abs(psi[n%N])*np.exp(0.5*abs(n)/L) for n in range(-N//2,N//2))
    print(f"Z2.3 L={L}: imag {im:.1e} gram-residual {gram:.1e} symmetry {sym:.1e} max leak/theta^4 {leak:.4f} (<=1.75) min g/L^3 {gmin/L**3:.4f} (>=0.078) sup|psi(n)|e^(0.5|n|/L) {tail:.3f}")
    # control: plain box kernel (hat a = B only) leaks like theta^2, so leak/theta^4 is unbounded near 0
    t=1e-2; bb=np.array([sum(np.exp(-1j*n*(t+2*np.pi*m)/L) for n in range(L)) for m in range(L)]); bb=bb/np.linalg.norm(bb)
    print(f"   control box kernel leak/theta^4 at theta=0.01: {(1-abs(bb[0])**2)/t**4:.1f}")
def psi1(L,n):
    N=L*M
    return PSI[L][n%N] if abs(n)<N//2 else 0.0
# covariance claim (5): J_L rho_c(Q) = F_Q J_L, tested on site coefficients (the common sign s_Q(r) dropped on both sides)
def rots():
    out=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            Q=np.zeros((3,3),int)
            for j in range(3): Q[p[j],j]=sg[j]
            if round(np.linalg.det(Q))==1: out.append(Q)
    return out
c0=np.array([.5]*3)
def cov_resid(L,Q,u,r,centre_shift=0):
    one=np.ones(3); p=(L-0.5)*one+centre_shift; W=2*L+2
    gq=lambda x: Q@(x-c0)+c0
    psi3=lambda c: np.prod([psi1(L,int(ci)) for ci in c])
    res=0
    # left: J_L |Qu, g_Q(r)>  ; right: site map x-> Q(x-p)+p applied to J_L|u,r>
    left={};right={}
    Qu=Q@u; gr=np.rint(gq(np.array(r))).astype(int)
    for c in itertools.product(range(-W,W+1),repeat=3):
        c=np.array(c)
        x=2*(c+L*Qu)+gr; left[tuple(x)]=psi3(c)
        y=2*(c+L*u)+np.array(r); z=np.rint(Q@(y-p)+p).astype(int); right[tuple(z)]=psi3(c)
    keys=set(left)&set(right)   # compare on the common window only (window-edge truncation otherwise)
    assert len(keys)>0.5*len(left)
    return max(abs(left[k]-right[k]) for k in keys)
for L in [2,3]:
    w=0
    for Q in rots()[::3]:
        w=max(w,cov_resid(L,Q,np.array([1,-1,0]),(1,0,1)))
    Qz=np.array([[0,-1,0],[1,0,0],[0,0,1]])
    print(f"Z2.3 covariance (5) L={L}: max residual {w:.1e}; control (rotation about centre shifted by (2,0,0)): {cov_resid(L,Qz,np.array([1,-1,0]),(1,0,1),np.array([2,0,0])):.3f}")
# Lemma Z2.4
wr=0;wc=0
for _ in range(4000):
    n=rng.integers(2,7); g=rng.uniform(.2,2)
    ev=rng.uniform(g,3*g,n)*rng.choice([-1,1],n); U=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
    B=U@np.diag(ev)@U.conj().T; H=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H=H+H.conj().T
    d=rng.uniform(0.01,0.99)*g; A=B+H*d/nrm(H)
    def neg(X):
        e,v=np.linalg.eigh(X); v=v[:,e<0]; return v@v.conj().T
    diff=nrm(neg(A)-neg(B)); wr=max(wr,diff/(2*d/(2*g-d))); wc=max(wc,diff/(d/(4*g)))
print(f"Z2.4: max lhs/bound over 4000 random cases {wr:.3f} (<=1); control bound delta/(4g): max ratio {wc:.2f} (>1 shows the control fails)")
# Theorem Z2 with block fibre from the hopping rule
def Rblock(th,T,L):
    cells=list(itertools.product(range(L),repeat=3)); ci={c:i for i,c in enumerate(cells)}
    n=8*L**3; Mx=np.zeros((n,n),complex)
    for c in cells:
        for r in RES:
            x=[2*c[i]+r[i] for i in range(3)]
            for j in range(3):
                for sgn in (1,-1):
                    y=list(x); y[j]+=sgn
                    lower=x if sgn==1 else y
                    own='e' if lower[j]%2==0 else 'o'
                    if own!=T: continue
                    cc=[yi//2 for yi in y]; rp=tuple(yi%2 for yi in y)
                    up=[ci_//L for ci_ in cc]; cp=tuple(ci_%L for ci_ in cc)
                    Mx[ci[cp]*8+IDX[rp],ci[c]*8+IDX[r]]+=eta(j,lower)*np.exp(-1j*np.dot(th,up))/np.sqrt(3)
    return Mx,cells
def Jblock(th,L,cells):
    n=8*L**3; J=np.zeros((n,8),complex)
    def f(ci_,t): return sum(psi1(L,ci_+L*v)*np.exp(-1j*t*v) for v in range(-30,31))
    for i,c in enumerate(cells):
        amp=np.prod([f(c[k],th[k]) for k in range(3)])
        for r in RES: J[i*8+IDX[r],IDX[r]]=amp
    return J
def negproj(V):
    h=1j*logm(V); h=(h+h.conj().T)/2; e,v=np.linalg.eigh(h); v=v[:,e<-1e-12]; return v@v.conj().T
w3=0;w4=0;wiso=0;wm0=0;ctl=0
for L in [2,3]:
    beta=1-1/L
    for eps in [0.1,0.8,1.4]:
        v=np.sin(eps)/np.sqrt(3)
        for trial in range(6):
            th=rng.normal(size=3); th*= (rng.uniform(0.05,1.0) if trial<3 else rng.uniform(0.05,np.sqrt(v)/2))/np.linalg.norm(th); k=np.linalg.norm(th)
            Re,cells=Rblock(th,'e',L); Ro,_=Rblock(th,'o',L)
            Vb=expm(1j*eps*Ro)@expm(-1j*eps*Re); Vc=Vfib(th,eps)
            W=expm(1j*beta*Ytr(th,eps)); Jt=Jblock(th,L,cells)@W.conj().T
            wiso=max(wiso,nrm(Jt.conj().T@Jt-np.eye(8)))
            A=W@(L*hfib(th/L,eps))@W.conj().T; wm0=max(wm0,nrm(A-hfib(th,eps))/k**3)
            A0=L*hfib(th/L,eps); ctl=max(ctl,nrm(A0-hfib(th,eps))/k**3)
            VbL=np.linalg.matrix_power(Vb,L)
            for t in [1,2,5,int(1/k)+1]:
                D=np.linalg.matrix_power(VbL,t)@Jt-Jt@np.linalg.matrix_power(Vc,t)
                w3=max(w3,nrm(D)/(2.66*k**2+1.5*t*k**3))
                if k<=np.sqrt(v)/2:
                    Pb=negproj(Vb); Pc=negproj(Vc)
                    S=Jt.conj().T@Pb@np.linalg.matrix_power(VbL,t)@Jt-Pc@np.linalg.matrix_power(Vc,t)
                    w4=max(w4,nrm(S)/((3.5/v+2.66)*k**2+1.5*t*k**3))
print(f"Z2(1) isometry residual of J~(theta) built in real space: {wiso:.1e}")
print(f"Z2(3) m=0 step: max ||W L h(th/L) W* - h(th)||/|th|^3 = {wm0:.4f} (<=1.5); control without twist: {ctl:.2f}")
print(f"Z2(3) full: max lhs/bound = {w3:.4f} (<=1)   Z2(4) full: max lhs/bound = {w4:.5f} (<=1)")
# control for Z2(3): without the twist the m=0 defect is second order: ratio to |th|^3 grows like 1/|th|
eps=0.8; L=2
for k in [0.2,0.05,0.0125]:
    th=np.array([1,0.5,-0.7]); th=th*k/np.linalg.norm(th)
    print(f"   control no-twist ||L h(th/L)-h(th)||/|th|^3 at |th|={k}: {nrm(L*hfib(th/L,eps)-hfib(th,eps))/k**3:.2f};  with twist: {nrm(expm(1j*.5*Ytr(th,eps))@(L*hfib(th/L,eps))@expm(-1j*.5*Ytr(th,eps))-hfib(th,eps))/k**3:.4f}")
