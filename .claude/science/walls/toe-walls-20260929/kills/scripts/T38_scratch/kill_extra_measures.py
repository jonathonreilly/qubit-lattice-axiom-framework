"""Kill-check extras for T38: measures the attack omitted or mislabelled. Seed 20260930, N=4e6."""
import numpy as np
rng = np.random.default_rng(20260930)
N = 4_000_000
def r_of_lam(lam):
    s1 = lam.sum(1); s2 = (lam**2).sum(1)
    return 1.5*(s2/s1**2) - 0.5
def dirichlet(alpha, n=N):
    g = rng.gamma(alpha, size=(n,3)); return g/g.sum(1, keepdims=True)
def rep(name, r):
    print(f"{name:70s} mean {np.mean(r):8.4f}  median {np.median(r):8.4f}  P(0.45<r<0.55) {np.mean((r>.45)&(r<.55)):.3f}")
print("-- Dirichlet(alpha) on lambda fractions (attack family L; median NOT computed by attack)")
for al in (1/3, 0.5, 1.0):
    rep(f"Dir({al:.3f}) on lam fractions", r_of_lam(dirichlet(al)))
print("analytic mean Q for Dir(alpha) on K=3 = (alpha+1)/(3 alpha+1); Perks alpha=1/K gives Q=(K+1)/(2K)=2/3 at K=3")
print("-- Dirichlet(alpha) on MASS fractions m (lam = sqrt m)")
for al in (1/3, 0.5, 1.0, 2.0):
    rep(f"Dir({al:.3f}) on mass fractions", r_of_lam(np.sqrt(dirichlet(al))))
print("-- Uniform on r in [0,1] (== uniform in Q on [1/3,1] == uniform disc |b|<=a): mean/median exactly 1/2 by symmetry")
# qutrit-density-matrix spectra (full nonabelian ensembles) for context: HS and Bures spectra
def hs_spectra(n=1_000_000):
    G = rng.normal(size=(n,3,3)) + 1j*rng.normal(size=(n,3,3)); rho = G@np.conj(np.transpose(G,(0,2,1)))
    ev = np.linalg.eigvalsh(rho); return ev/ev.sum(1,keepdims=True)
def bures_spectra(n=1_000_000):
    # Bures: rho = (1+U) G G^dag (1+U^dag), U Haar
    G = rng.normal(size=(n,3,3)) + 1j*rng.normal(size=(n,3,3))
    Z = rng.normal(size=(n,3,3)) + 1j*rng.normal(size=(n,3,3))
    Q_, R_ = np.linalg.qr(Z); d = np.diagonal(R_, axis1=1, axis2=2); ph = d/np.abs(d); U = Q_*ph[:,None,:]
    A = (np.eye(3)+U)@G; rho = A@np.conj(np.transpose(A,(0,2,1)))
    ev = np.linalg.eigvalsh(rho); ev = np.clip(ev,0,None); return ev/ev.sum(1,keepdims=True)
rep("full qutrit HS-ensemble spectra (not C3-restricted)", r_of_lam(hs_spectra()))
rep("full qutrit Bures-ensemble spectra (not C3-restricted)", r_of_lam(bures_spectra()))
print("(Note: the C3-invariant slice is commuting, so Bures/Fisher restricted to it is the classical Dir(1/2): attack's D is the correct restriction.)")
