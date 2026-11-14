# E2a / B10(4): P(K) formula at mu=0, derivative bound ~1/|K|, decay of P_xy (midpoint Bloch grid), half filling.
import numpy as np, itertools
E3=np.eye(3,dtype=int); res=list(itertools.product((0,1),repeat=3)); ridx={r:i for i,r in enumerate(res)}
def eta(i,x): return (-1)**(sum(x[:i])%2)
def fibres(K,o):   # K: (M,3) -> (M,8,8)
    R=np.zeros((len(K),8,8),complex)
    for r in res:
        for i in range(3):
            if r[i]%2==o:
                y=np.array(r)+E3[i]; cell=y//2; rr=tuple(y%2); ph=np.exp(-1j*K@cell)
                R[:,ridx[rr],ridx[r]]+=eta(i,r)*ph/np.sqrt(3); R[:,ridx[r],ridx[rr]]+=eta(i,r)*np.conj(ph)/np.sqrt(3)
    return R
def Vk(K,eps,mu):
    ae,ao=eps-mu/2,eps+mu/2; I=np.eye(8)
    return (np.cos(ao)*I+1j*np.sin(ao)*fibres(K,1))@(np.cos(ae)*I-1j*np.sin(ae)*fibres(K,0))
def Pk(K,eps,mu):
    V=Vk(K,eps,mu); A=(V-np.conj(np.swapaxes(V,1,2)))/(2j)        # Hermitian, eigenvalues +-sin w
    w,U=np.linalg.eigh(A); sel=(w>0)[:,None,:]
    return (U*sel)@np.conj(np.swapaxes(U,1,2)), V
rng=np.random.default_rng(2)
K=rng.uniform(-np.pi,np.pi,(500,3)); eps=0.9
P,V=Pk(K,eps,0.0); g=1-np.sin(eps)**2*(1-np.cos(K).sum(1)/3)
Pf=0.5*(np.eye(8)+(V-np.conj(np.swapaxes(V,1,2)))/(2j*np.sqrt(1-g**2))[:,None,None])
print("E2a: |P(K) formula - spectral projector on eigenvalues e^{+iw}| max:",abs(P-Pf).max(), " V(0)=I:",abs(Vk(np.zeros((1,3)),eps,0.0)[0]-np.eye(8)).max())
# sign convention: P fills quasi-energy in (-pi,0) with eigenvalue e^{-i w'}: eigenvalue angle in (0,pi) -> sin>0 branch. OK.
# derivative bound |K| * ||dP/dK_j|| bounded near 0
for r in (1e-1,1e-2,1e-3):
    d=rng.normal(size=(200,3)); d/=np.linalg.norm(d,axis=1)[:,None]; K0=r*d; h=r*1e-4
    worst=0
    for j in range(3):
        dP=(Pk(K0+h*E3[j],eps,0.0)[0]-Pk(K0-h*E3[j],eps,0.0)[0])/(2*h)
        worst=max(worst,np.linalg.norm(dP,ord=2,axis=(1,2)).max())
    print(f"   |K|={r:g}: max ||d_j P|| * |K| = {worst*r:.4f}")
def Pxy(eps,mu,N,seps):
    ax=(np.arange(N)+0.5)*2*np.pi/N-np.pi      # midpoint grid avoids K=0
    Kg=np.array(list(itertools.product(ax,repeat=3)))
    P=np.concatenate([Pk(Kg[i:i+20000],eps,mu)[0] for i in range(0,len(Kg),20000)])
    out={}
    for d in seps: out[d]=(P*np.exp(1j*Kg@np.array(d))[:,None,None]).mean(0)
    return out
seps=[(k,0,0) for k in range(0,9)]+[(k,k,k) for k in range(1,7)]+[(k,k,0) for k in range(1,7)]
for eps,mu,N in [(0.9,0.0,40),(0.9,0.6,40),(0.3,0.0,40)]:
    out=Pxy(eps,mu,N,seps)
    print(f"eps={eps} mu={mu} N={N}: diag of P_xx (cell sep 0): min {out[(0,0,0)].diagonal().real.min():.6f} max {out[(0,0,0)].diagonal().real.max():.6f}")
    line=[]
    for d in seps[1:]:
        dist=2*np.linalg.norm(d); m=abs(out[d]).max(); line.append(f"{d}:{m:.2e}[x(1+r)={m*(1+dist):.3f}]")
    print("   max|P_xy| by cell separation: "+"  ".join(line))
