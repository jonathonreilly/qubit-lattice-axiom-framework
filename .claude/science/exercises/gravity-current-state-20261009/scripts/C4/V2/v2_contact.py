"""V2 (b2'): contact-bound pair (separable, exact in infinite volume via a fine k-grid).
psi_Q(k) = C/(eps_Q(k) - E),  eps_Q(k) = w(k) + w(Q-k),  bound-state condition 1 = U * mean_k 1/(eps_Q(k) - E).
eta_mom(Q) = 1 - f_B(Q)/Q with f_B = <sin k + sin(Q-k)>; at Q -> 0 equals 1 - <cos kap_x>.
Contact tails psi ~ 1/kap^2 make <kap^2> UV-dominated in 3D: expect eta ~ c * p_B a (linear), not (p_B a)^2.
"""
import numpy as np, sys
from scipy.optimize import brentq
N = int(sys.argv[1]) if len(sys.argv) > 1 else 96
m = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
k1 = 2*np.pi*(np.arange(N) + 0.5)/N - np.pi      # midpoint grid (avoids k = 0 exactly)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
def wd(kx, ky, kz): return np.sqrt(m**2 + 4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2)
eps0 = wd(KX, KY, KZ)*2
thr = 2*m
Uc = 1/np.mean(1/(eps0 - thr))
print(f'N={N} m={m}: threshold coupling U_c = {Uc:.4f} (grid estimate)')
def state(U, q):
    eps = wd(KX, KY, KZ) + wd(q - KX, -KY, -KZ)
    g = lambda E: U*np.mean(1/(eps - E)) - 1
    E = brentq(g, eps.min() - 50*U, eps.min() - 1e-9, xtol=1e-14)
    p = 1/(eps - E)**2; p /= p.sum()
    fB = np.sum(p*(np.sin(KX) + np.sin(q - KX)))
    c = np.sum(p*np.cos(KX - q/2))
    kap2 = np.sum(p*4*np.sin(KX/2)**2)   # lattice <kap_x^2>
    f2 = lambda k: (4/3)*np.sin(k) - (1/6)*np.sin(2*k)   # improved symbol k - k^5/30
    fB2 = np.sum(p*(f2(KX) + f2(q - KX)))
    return E, fB, c, kap2, fB2
q = 0.02
print(' U/U_c   E_bind      p_B=sqrt(m E_b)  eta_mom(q)    1-<cos kap_x>  eta/p_B     eta/p_B^2   <kap_x^2>   eta_mom[f2]  eta[f2]/p_B')
for x in [1.005, 1.01, 1.02, 1.05, 1.1, 1.3, 2.0]:
    U = x*Uc
    E0, _, c0, k2, _ = state(U, 0.0)
    Eq, fB, cq, _, fB2 = state(U, q)
    Eb = thr - E0; pB = np.sqrt(m*Eb)
    eta = 1 - fB/q
    print(f'{x:6.2f} {Eb:10.4e} {pB:12.4e} {eta:+12.4e} {1-c0:+12.4e} {eta/pB:10.4f} {eta/pB**2:10.4f} {k2:10.4e} {1-fB2/q:+11.4e} {(1-fB2/q)/pB:9.4f}')
    sys.stdout.flush()
