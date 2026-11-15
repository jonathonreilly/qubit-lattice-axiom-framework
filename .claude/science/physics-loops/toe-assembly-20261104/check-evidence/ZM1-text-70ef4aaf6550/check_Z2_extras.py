# Higher-correlation determinant bound; Corollary Z2.2 reality of the twisted map in the O frame; massive remark V(0).
import numpy as np, itertools
from scipy.linalg import expm
from check_common import *
rng=np.random.default_rng(5)
# determinant bound: entries of modulus <=1, |M-N|<=beta entrywise  =>  |det M-det N| <= n^{(n+2)/2} beta
w=0;wc=0
for _ in range(20000):
    n=rng.integers(1,6); beta=10**rng.uniform(-4,-0.5)
    N=np.exp(2j*np.pi*rng.uniform(size=(n,n)))*rng.uniform(.5,1,(n,n))
    M=N+beta*np.exp(2j*np.pi*rng.uniform(size=(n,n)))
    M=np.where(abs(M)>1,M/abs(M),M)
    b=np.max(abs(M-N)); d=abs(np.linalg.det(M)-np.linalg.det(N))
    w=max(w,d/(n**((n+2)/2)*b)); wc=max(wc,d/b)   # control: bound without the n-dependent factor
print(f"higher correlations: max |detM-detN|/(n^((n+2)/2) beta) = {w:.3f} (<=1); control with factor 1: {wc:.2f} (>1)")
# O frame: fibre of W_c X W_c^* at Pi+k is D X(k) D^*, D=diag(i^{sum r}); position-space reality <=> conj(Xhat(Pi+k)) = Xhat(Pi-k)
D=np.diag([1j**sum(r) for r in RES])
wr=0;wh=0;ctl=0
for eps in [0.2,0.9,1.4]:
    for _ in range(50):
        k=rng.uniform(-np.pi,np.pi,3); beta=0.5
        X=lambda q: D@expm(1j*beta*Ytr(q,eps))@D.conj().T
        wr=max(wr,nrm(np.conj(X(k))-X(-k)))
        VO=lambda q: D@Vfib(q,eps)@D.conj().T
        wh=max(wh,nrm(np.conj(VO(k))-VO(-k)))
        X0=lambda q: expm(1j*beta*Ytr(q,eps)); ctl=max(ctl,nrm(np.conj(X0(k))-X0(-k)))
print(f"Z2.2: reality residual of O-frame walk {wh:.1e}, of O-frame twist {wr:.1e}; control (twist without the site-phase gauge): {ctl:.3f}")
# kernel entry phase: (-1)^{sum c + sum u} from i^{sum(2c+r)} * conj(i^{sum(2u+r)})
ok=all(abs((1j**(2*c+r))*np.conj(1j**(2*u+r))-(-1)**(c+u))<1e-12 for c in range(-3,4) for u in range(-3,4) for r in (0,1))
print("Z2.2: residue phases cancel, entry phase (-1)^(c+u):",ok)
# massive remark
for mu,eps in [(0.3,0.8)]:
    A,Z,G=AZG(); R=sum(A)/np.sqrt(3)
    print("remark: ||V(0)-exp(i mu R)|| =",nrm(Vfib(np.zeros(3),eps,mu)-expm(1j*mu*R)))
