"""Kill check for T31: (1) free-field validation of build_D; (2) independent linear-response check
dP/dNs at Ns->0 = cov(P, ln det) on a QUENCHED ensemble (no dynamical-fermion HMC needed)."""
import numpy as np, sys, json
sys.path.insert(0,'.')
import hmc_unquench as H
L=H.L
# (1) free field: U = 1, antiperiodic time. det(D+m) should equal prod_k (m^2 + sum_mu sin^2 k_mu)^{...}
U=np.broadcast_to(np.eye(3,dtype=complex),(4,)+H.DIMS+(3,3)).copy()
D=H.build_D(U)
ev=np.linalg.eigvals(D)
print("anti-Hermitian check |D+D^dag|:",np.abs(D+D.conj().T).max())
print("eigenvalue real parts max:",np.abs(ev.real).max())
# analytic staggered free spectrum with eta phases: eigenvalues of D^2 = -sum_mu sin^2(k_mu) (k_t in (n+1/2)2pi/L, k_i 2pi n/L), times 3 colors, with 2 x degeneracy (taste pairs) -> just compare det
ks=[(2*np.pi*(n+0.5)/L) if mu==0 else 2*np.pi*n/L for mu in range(4) for n in range(L)]
def kk(mu): return [(2*np.pi*(n+0.5)/L) if mu==0 else 2*np.pi*n/L for n in range(L)]
import itertools
tot=0.0
for k in itertools.product(*[kk(mu) for mu in range(4)]):
    tot+=np.log(0.1**2+sum(np.sin(x)**2 for x in k))
# staggered: det over N sites (1 component) = prod over N momenta of (m^2+sum sin^2)^{1/2}; times 3 colors
analytic=3*0.5*tot
s,ld=H.ferm_logdet(U,0.1)
print("free lndet numeric",ld,"analytic",analytic)
# (2) covariance slope, quenched ensemble
rng=np.random.default_rng(777)
Uc=H.rand_su3((4,)+H.DIMS,rng)
S=H.action(Uc,6.0,0,0.1)
P=[];LD=[]
ntraj=int(sys.argv[1]); ntherm=60
for it in range(ntraj+ntherm):
    Pm=H.random_mom(rng)
    H0=H.kinetic(Pm)+S
    U1,P1=H.leapfrog(Uc,Pm,6.0,0,0.1,25,0.03)
    U1=H.reunit(U1)
    S1=H.action(U1,6.0,0,0.1)
    dH=H.kinetic(P1)+S1-H0
    if rng.random()<np.exp(-dH): Uc,S=U1,S1
    if it>=ntherm:
        P.append(H.plaq_avg(Uc)); s,ld=H.ferm_logdet(Uc,0.1); LD.append(ld)
P=np.array(P);LD=np.array(LD)
nb=10; n=len(P)//nb*nb
def slope(idx):
    return np.cov(P[idx],LD[idx])[0,1]
sl=slope(np.arange(len(P)))
# block jackknife
bl=np.arange(n).reshape(nb,-1)
js=[slope(np.concatenate([bl[j] for j in range(nb) if j!=i])) for i in range(nb)]
err=np.sqrt((nb-1)/nb*np.sum((np.array(js)-np.mean(js))**2))
print(f"quenched <P>={P.mean():.5f}  cov(P,lndet) slope dP/dNs|0 = {sl:.5f} +/- {err:.5f}  (HMC Ns=1 finite: 0.0212)")
json.dump(dict(P=P.mean(),slope=sl,err=err,ntraj=ntraj),open("cov_result.json","w"))
