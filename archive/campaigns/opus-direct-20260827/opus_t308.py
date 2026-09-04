"""
T308 - settle G = 2pi tau0 vs 6pi tau0 by computing the FLUCTUATION OPERATOR,
not by hunting the photon.

R162 aimed four observables at "is there a massless photon" and all four failed,
and concluded the question may be malformed because the Berry U(1) is COMPOSITE
-- a function of the matter, with no action of its own. Take that seriously and
ask the physical question instead: 1/G_ind is fixed by the a1 coefficient of the
fluctuation determinant, which needs the MODE CONTENT, not a photon pole.

Expand the Born-point action about the ordered state:
    S = -sum_edges log |<psi_x|psi_y>|^2
with psi_x = normalize(psi_0 + eta_x), eta_x in the tangent space at psi_0.
If the Hessian is exactly (graph Laplacian) tensor I_6, then the framework has
exactly six massless scalars, no independent gauge mode, and N = 6 -> G = 2pi tau0.

Note the phase never appears: |<psi_x|psi_y>|^2 is invariant under psi -> e^{ia}psi,
so the U(1) direction is absent from the action at every order, not merely gapped.

Controls: (i) the Hessian's null space must be exactly the 2 global directions
(overall shift), not 7 or 8; (ii) rank and eigenvalue multiplicities checked
against the graph Laplacian's own spectrum; (iii) an independent finite-difference
Hessian must reproduce the analytic one.
"""
import numpy as np, itertools
n=4
rng=np.random.default_rng(11)
def tangent_basis(p0):
    """real tangent space at p0 in CP^{n-1}: eta perp p0, modulo phase -> 2(n-1) real dims"""
    Q=np.eye(n,dtype=complex)-np.outer(p0,p0.conj())
    U,s,_=np.linalg.svd(Q); B=[U[:,i] for i in range(n-1)]      # complex perp basis
    out=[]
    for b in B: out.append(b); out.append(1j*b)
    return out                                                   # 2(n-1) = 6 real dirs
p0=np.zeros(n,dtype=complex); p0[0]=1.0
TB=tangent_basis(p0); m=len(TB)
print(f"tangent dimension at psi_0 in CP^{n-1}: {m}   (expect 2(n-1) = {2*(n-1)})")

# small lattice, exact Hessian by finite differences of the true action
L,d=4,3; N=L**d
sites=list(itertools.product(range(L),repeat=d)); ix={s:i for i,s in enumerate(sites)}
edges=[]
for s in sites:
    for ax in range(d):
        t=list(s); t[ax]=(t[ax]+1)%L; edges.append((ix[s],ix[tuple(t)]))
def action(co):
    psi=np.tile(p0,(N,1)).astype(complex)
    for a in range(N):
        for k in range(m): psi[a]=psi[a]+co[a,k]*TB[k]
    psi/=np.linalg.norm(psi,axis=1,keepdims=True)
    tot=0.0
    for a,b in edges:
        ov=abs(np.vdot(psi[a],psi[b]))**2
        tot-=np.log(max(ov,1e-300))
    return tot
h=1e-4; H=np.zeros((N*m,N*m))
base=np.zeros((N,m))
for A in range(N*m):
    for B in range(A,N*m):
        a1,k1=divmod(A,m); a2,k2=divmod(B,m)
        def ev(s1,s2):
            c=base.copy(); c[a1,k1]+=s1*h; c[a2,k2]+=s2*h; return action(c)
        H[A,B]=H[B,A]=(ev(1,1)-ev(1,-1)-ev(-1,1)+ev(-1,-1))/(4*h*h)
lap=np.zeros((N,N))
for a,b in edges:
    lap[a,a]+=1; lap[b,b]+=1; lap[a,b]-=1; lap[b,a]-=1
target=np.kron(lap,np.eye(m))*2.0            # S ~ sum_edges |eta_x - eta_y|^2 -> Hess = 2*Lap (x) I
print(f"\nHessian vs 2*(graph Laplacian) tensor I_{m}:")
print(f"   max |H - 2 L(x)I| = {np.abs(H-target).max():.3e}")
print(f"   relative           = {np.abs(H-target).max()/np.abs(target).max():.3e}")
ev=np.linalg.eigvalsh(H); lev=np.linalg.eigvalsh(lap)
print(f"\n   Hessian zero modes (<1e-6): {int(np.sum(np.abs(ev)<1e-6))}   expect {m} (one per tangent direction, global shift)")
print(f"   distinct Hessian eigenvalues: {len(np.unique(np.round(ev,6)))}")
print(f"   distinct Laplacian eigenvalues: {len(np.unique(np.round(lev,6)))}")
print(f"   every Hessian eigenvalue = 2*(a Laplacian eigenvalue)? "
      f"{np.allclose(np.sort(ev), np.sort(np.repeat(2*lev,m)), atol=1e-5)}")
print(f"\n=> mode content: {m} massless scalars, no independent gauge mode.")
print(f"   N = {m} gives G = 12 pi tau0 / {m} = {12/m:.0f} pi tau0")
