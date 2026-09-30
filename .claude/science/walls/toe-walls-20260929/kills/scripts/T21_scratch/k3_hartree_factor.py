"""K3: normalisation of the attacker's Hartree gap equation (Test D).  Uses the framework's walker
H = sum_j sigma_j S_j (2 coin states per site), antiperiodic BC (no zero modes), staggered term Delta*eps,
half filling (N filled of 2N).  Compares the staggered density  m = (1/N) sum_x eps_x n_x  (n_x = total density)
with Delta*<1/sqrt(s^2+Delta^2)>_BZ (grid shifted by pi/L, the same momentum set)."""
import numpy as np
L=10; N=L**3
def idx(x,y,z): return ((x%L)*L+(y%L))*L+(z%L)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
H=np.zeros((2*N,2*N),complex)
for x in range(L):
  for y in range(L):
    for z in range(L):
      i=idx(x,y,z); X=(x,y,z)
      for j in range(3):
        d=[0,0,0]; d[j]=1
        f=idx(x+d[0],y+d[1],z+d[2]); b=idx(x-d[0],y-d[1],z-d[2])
        sf=-1.0 if X[j]==L-1 else 1.0; sb=-1.0 if X[j]==0 else 1.0
        H[2*i:2*i+2,2*f:2*f+2]+= sf*sig[j]/(2j)
        H[2*i:2*i+2,2*b:2*b+2]-= sb*sig[j]/(2j)
eps=np.array([(-1)**((i//(L*L))+(i//L)%L+i%L) for i in range(N)],float)
print("hermitian:",np.abs(H-H.conj().T).max())
# momentum set for antiperiodic BC:  k=(2pi/L)(n+1/2)
k=(np.arange(L)+0.5)*2*np.pi/L
kx,ky,kz=np.meshgrid(k,k,k,indexing='ij'); s2=(np.sin(kx)**2+np.sin(ky)**2+np.sin(kz)**2).ravel()
for D in (0.3,0.8):
    Hm=H+D*np.kron(np.diag(eps),np.eye(2))
    E,V=np.linalg.eigh(Hm)
    filled=V[:,:N]
    dens=(np.abs(filled)**2).reshape(N,2,N).sum(axis=(1,2))   # n_x
    m=(eps*dens).sum()/N
    pred=D*np.mean(1/np.sqrt(s2+D*D))
    print(f"Delta={D}: spectrum min|E|={np.abs(E).min():.4f} sqrt(min s2+D2)={np.sqrt(s2.min()+D*D):.4f} | staggered density m={m:.5f}  vs  Delta*<1/E>={pred:.5f}  ratio={abs(m)/pred:.4f}")
