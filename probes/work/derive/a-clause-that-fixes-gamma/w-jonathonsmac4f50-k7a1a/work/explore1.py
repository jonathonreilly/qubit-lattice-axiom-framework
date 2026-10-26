import numpy as np, itertools
N=6
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
sites=list(itertools.product(range(N),repeat=3)); idx={s:i for i,s in enumerate(sites)}
V=len(sites)
# H = sum_j sigma_j D_j, D_j=(i/2)(T-T^dag),(T psi)(x)=psi(x-e) -> symbol sum sigma_j sin k_j ? check sign
H=np.zeros((2*V,2*V),complex)
for s in sites:
    for j in range(3):
        e=[0,0,0];e[j]=1
        sm=tuple((s[a]-e[a])%N for a in range(3)); sp=tuple((s[a]+e[a])%N for a in range(3))
        # (T psi)(x)=psi(x-e): row x col x-e coefficient (i/2); T^dag: row x col x+e coefficient -(i/2)
        H[2*idx[s]:2*idx[s]+2,2*idx[sm]:2*idx[sm]+2]+=0.5j*sig[j]
        H[2*idx[s]:2*idx[s]+2,2*idx[sp]:2*idx[sp]+2]+=-0.5j*sig[j]
print(np.abs(H-H.conj().T).max())
def Eminus(u):
    phi=np.exp(np.repeat(u,2)/2)
    Hw=phi[:,None]*H*phi[None,:]
    ev=np.linalg.eigvalsh(Hw)
    return ev[ev<0].sum()
E0=Eminus(np.zeros(V)); print("E0/V",E0/V)
# formula
def A(q,M=64):
    ks=np.arange(M)*2*np.pi/M
    K=np.stack(np.meshgrid(ks,ks,ks,indexing='ij'),-1).reshape(-1,3)
    d1=np.sin(K); d2=np.sin(K+q)
    r1=np.linalg.norm(d1,axis=1); r2=np.linalg.norm(d2,axis=1)
    n1=d1/r1[:,None]; n2=d2/r2[:,None]
    a=(d1+d2)/2
    t1=0.25*(-(n1*d2).sum(1)-r1)
    num=0.5*((a*a).sum(1)*(1+(n1*n2).sum(1))-2*(a*n1).sum(1)*(a*n2).sum(1))
    t2=-num/(r1+r2)
    return (t1+t2).mean()
# test against FD for u=a cos(q x), q commensurate with N=6
for qn in [(0,0,0),(1,0,0),(1,1,0),(3,3,3),(2,1,0)]:
    q=2*np.pi*np.array(qn)/N
    a=1e-2
    u=np.array([a*np.cos(q@np.array(s)) for s in sites])
    d2E=(Eminus(u)+Eminus(-u)-2*E0)/2   # second order part (even part) /...
    # E2 total = V * <u^2>-weighted sum_q |u_q|^2 A(q); u = a cos -> |u_q|^2 = a^2/4 for +-q (two terms) -> sum = a^2/2 if q!=-q
    uq2=np.mean(u**2)
    # if q=-q mod 2pi (components 0 or pi) then u_q = a (single), sum|u_q|^2 = a^2 /... mean(u^2)
    pred=V*uq2*A(q)   # A depends on q even so sum_q|u_q|^2 A(q)=mean(u^2)*A(q)
    print(qn, d2E, pred)
