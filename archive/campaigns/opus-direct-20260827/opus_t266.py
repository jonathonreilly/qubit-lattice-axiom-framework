"""
T266 - is R186's 4/3 in my FORMULA or in my LATTICE OPERATOR?

R186 derived R(s) = 1 + (2/9)x for d=3 conformal and found the lattice
measurement 1.32x too large.  Two possibilities, and they are cleanly separable:

  (a) the analytic formula is wrong  -> the EXACT CONTINUUM operator will
      disagree with 1 + (2/9)x
  (b) the lattice operator is wrong  -> the continuum will AGREE with the
      formula, and the lattice is what deviates

Builds the exact continuum operator in d=3 by plane-wave diagonalisation (the
T202 construction, which was validated in d=4), needing no lattice and no D.
"""
import numpy as np
from collections import Counter

def cont_R(L, n_mode, eps, svals, J=40):
    tp = 2*np.pi/L; kap_i = n_mode
    # W = f^{1/2} (stiffness), rho = f^{3/2} (mass), f = 1 + eps cos(kappa x)
    Ng = 8192; x = np.arange(Ng)*L/Ng
    f = 1.0 + eps*np.cos(2*np.pi*n_mode*x/L)
    FW = np.fft.fft(f**0.5)/Ng
    FR = np.fft.fft(f**1.5)/Ng
    # transverse momenta: 2 directions, same weight -> bucket by j1^2 + j2^2
    j = np.arange(-J, J+1)
    c1 = Counter((j*j).tolist())
    c2 = Counter()
    for a,na in c1.items():
        for b,nb in c1.items(): c2[a+b] += na*nb
    sv = np.asarray(svals, float); out = np.zeros(len(sv))
    for r in range(n_mode):
        j0 = np.array([v for v in range(-J,J+1) if (v-r) % n_mode == 0], float)
        k0 = j0*tp; nb = len(k0)
        d = (np.arange(nb)[:,None]-np.arange(nb)[None,:])*n_mode
        Wd = np.real(FW[d % Ng]); Md = np.real(FR[d % Ng])
        A0 = (k0[:,None]*k0[None,:])*Wd
        ev_, U = np.linalg.eigh(Md); Mih = (U/np.sqrt(ev_)) @ U.T
        for q2i, mult in c2.items():
            A = A0 + (q2i*tp*tp)*Wd
            B = Mih @ A @ Mih; B = 0.5*(B+B.T)
            lam = np.maximum(np.linalg.eigvalsh(B), 0)
            out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

L, n = 40, 1
kappa = 2*np.pi*n/L
xs = np.array([0.05, 0.10, 0.20, 0.35, 0.50])
s = xs/kappa**2
h = 0.05
K = {}
for e in (-2,-1,0,1,2):
    K[e] = cont_R(L, n, e*h, s)
K2 = 0.5*(-K[2]+16*K[1]-30*K[0]+16*K[-1]-K[-2])/(12*h*h)
V2 = (3.0/8.0)*(L**3/2.0)          # (3/8) * integral of phi^2 over the box
R = (4*np.pi*s)**1.5 * K2 / V2
tgt = 1 + (2/9)*xs
print(f"EXACT CONTINUUM, d=3, L={L}, kappa={kappa:.4f}  (no lattice, no D)")
print(f"Vol_2 = (3/8) * L^3/2 = {V2:.2f}\n")
print("    x     R continuum    1 + (2/9)x     ratio")
for i in range(len(xs)):
    print(f"  {xs[i]:5.3f}   {R[i]:11.5f}   {tgt[i]:11.5f}   {R[i]/tgt[i]:7.4f}")
print(f"\n  mean ratio = {np.mean(R/tgt):.4f}")
print("  ratio ~ 1  => the FORMULA is right, the LATTICE OPERATOR is at fault")
print("  ratio ~ 4/3 => the FORMULA is wrong")
