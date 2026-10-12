"""R9-6, script 4 (d = 3): finite INTERACTING boosts with the p-wave triplet and the spin term; Theorem L in d = 3.

A boost along x leaves P_perp = (P_y, P_z) fixed and differentiates only in P_x, so at fixed P_perp the chart law
is a 1D transport in P_x on the l = 1 channel (m = -1, 0, 1) x radial grid on supp g:
  K_lat = (1/2){H_c, i d/dP_x} + (P x S)_x F_c,   (P x S)_x = P_y S_z - P_z S_y,
  H_c = (1 - c) sqrt(M0^2 + P^2) + c sqrt(M^2 + P^2),  F_c = (1 - c) f(M0) + c f(M),  f(x) = 1/(x + sqrt(x^2 + P^2)),
  c = c(|P|), |P|^2 = P_x^2 + |P_perp|^2   (the lattice law in the chart, R8-1 §3.2 lattice-native form, Lemma L);
the BT comparator is the same with c == 1.  Theorem L (d = 3):
  ||U_lat(eta) psi - U_BT(eta) psi|| <= 2 ||(1 - E) psi||,  E = 1_I(P) 1_Sigma(M),
  orbit condition: P_x -> m_perp sinh(asinh(P_x/m_perp) - s), m_perp = sqrt(mu^2 + |P_perp|^2), stays in |P| < Pi1,
  and every leg of (P(s), q), |q| in Q_Sigma (rotation invariant, so the Wigner rotation is irrelevant) stays in the
  exact region (cube or ball; here legs <= 1.6 < 2.6 automatically, so the plateau is the binding condition).
(i) compactly supported bound-triplet packet (m-superposition) with P_perp != 0; (ii) bound + continuum mix.
"""
import numpy as np, sys
from r81_common import sstep

m, KAP, MU_B, PI1, PI2 = 0.5, 0.8, 0.85, 0.6, 1.2
PPERP = np.array([0.20, -0.10])
Nr = 24
xr, wr = np.polynomial.legendre.leggauss(Nr); r = 0.5*KAP*(xr + 1); wr = 0.5*KAP*wr
M0r = 2*np.sqrt(m*m + r**2)
hvec = np.sqrt(wr*r**2)*r*(sstep(1.0 - r**2/KAP**2)/KAP)*np.sqrt(4*np.pi/3)
LAM = -1.0/np.sum(hvec**2/(M0r - MU_B))
mu, U = np.linalg.eigh(np.diag(M0r) + LAM*np.outer(hvec, hvec))
Sz = np.diag([1.0, 0.0, -1.0]).astype(complex)                 # basis m = +1, 0, -1
Sp = np.zeros((3, 3)); Sp[0, 1] = Sp[1, 2] = np.sqrt(2.0)
Sy = (Sp - Sp.T)/(2j)
SxP = PPERP[0]*Sz - PPERP[1]*Sy                                  # (P x S)_x at fixed P_perp
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 640
Wn = 2.4
Pg = np.linspace(-Wn, Wn, NP, endpoint=False); dP = Pg[1] - Pg[0]
kP = 2*np.pi*np.fft.fftfreq(NP, d=dP)
P2 = Pg**2 + PPERP @ PPERP
c = sstep((PI2 - np.sqrt(P2))/(PI2 - PI1))
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
pr('d = 3 boost along x at P_perp = (%.2f, %.2f); l = 1 channel, Nr = %d on supp g; M_min = %.10f; NP = %d on [-%.1f, %.1f)'
   % (PPERP[0], PPERP[1], Nr, mu.min(), NP, Wn, Wn))
# legs: max |k1| over |q| <= kappa and |P| <= 2.4 (worst case, q parallel to P)
qq = np.linspace(0, KAP, 81); Pn = np.linspace(0, 2.4, 241)
w_ = np.sqrt(m*m + qq[None, :]**2); M0_ = 2*w_; H0_ = np.sqrt(M0_**2 + Pn[:, None]**2)
leg = qq[None, :] + Pn[:, None]*(Pn[:, None]*qq[None, :]/(M0_*(H0_ + M0_)) + w_/M0_)
pr('legs: max |k_leg| for |q| <= kappa at |P| <= 1.2 (c > 0): %.3f; at |P| <= 2.4: %.3f  (cube/ball edge B = 2.6)'
   % (leg[Pn <= 1.2].max(), leg.max()))

def apply(v, cc, deriv=False):
    """v shape (NP, 3, Nr): returns H_c v (or dH_c/dP_x v) and F_c v."""
    vb = v @ U
    hM = np.sqrt(mu[None, None, :]**2 + P2[:, None, None]); h0 = np.sqrt(M0r[None, None, :]**2 + P2[:, None, None])
    if not deriv:
        HM = (vb*hM) @ U.T; H0 = v*h0
        return (1 - cc)[:, None, None]*H0 + cc[:, None, None]*HM
    dc = np.real(np.fft.ifft(1j*kP*np.fft.fft(cc)))
    Px = Pg[:, None, None]
    HM = (vb*hM) @ U.T; H0 = v*h0
    dHM = (vb*(Px/hM)) @ U.T; dH0 = v*(Px/h0)
    return (-dc)[:, None, None]*H0 + (1 - cc)[:, None, None]*dH0 + dc[:, None, None]*HM + cc[:, None, None]*dHM
def Fc(v, cc):
    vb = v @ U
    fM = 1.0/(mu[None, None, :] + np.sqrt(mu[None, None, :]**2 + P2[:, None, None]))
    f0 = 1.0/(M0r[None, None, :] + np.sqrt(M0r[None, None, :]**2 + P2[:, None, None]))
    return (1 - cc)[:, None, None]*v*f0 + cc[:, None, None]*((vb*fM) @ U.T)
def rhs(v, cc):          # -i K v = H_c dv/dP + (1/2)(dH_c/dP) v - i (P x S)_x F_c v
    dv = np.fft.ifft(1j*kP[:, None, None]*np.fft.fft(v, axis=0), axis=0)
    return apply(dv, cc) + 0.5*apply(v, cc, deriv=True) - 1j*np.einsum('ab,pbr->par', SxP, Fc(v, cc))
def evolve(v0, cc, etas, dt=2.0e-3*640/NP):
    v = v0.astype(complex); t = 0.0; res = {}
    for et in etas:
        while t < et - 1e-12:
            h = min(dt, et - t)
            k1 = rhs(v, cc); k2 = rhs(v + 0.5*h*k1, cc); k3 = rhs(v + 0.5*h*k2, cc); k4 = rhs(v + h*k3, cc)
            v = v + (h/6)*(k1 + 2*k2 + 2*k3 + k4); t += h
        res[et] = v.copy()
    return res
one = np.ones(NP)
phib = U[:, np.argmin(mu)]
spin = np.array([0.6, 0.5j, -0.62]); spin = spin/np.linalg.norm(spin)
etas = [0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.8, 1.0]
a = 0.25
mperp = np.sqrt(MU_B**2 + PPERP @ PPERP); Pi1x = np.sqrt(PI1**2 - PPERP @ PPERP)
A = sstep(1 - (Pg/a)**2); A = A/np.linalg.norm(A)
v0 = A[:, None, None]*spin[None, :, None]*phib[None, None, :]
lat = evolve(v0, c, etas); bt = evolve(v0, one, etas)
eta_star = np.arcsinh(Pi1x/mperp) - np.arcsinh(a/mperp)
pr('(i) bound-triplet packet, spin (0.6, 0.5i, -0.62), P_x-support |P_x| < %.2f; eta* = asinh(sqrt(Pi1^2 - P_perp^2)/m_perp) - asinh(a/m_perp) = %.4f'
   % (a, eta_star))
for et in etas:
    leak = np.linalg.norm(lat[et] - bt[et])
    Pmin = mperp*np.sinh(np.arcsinh(-Pi1x/mperp) + et)
    bad = np.linalg.norm(A[Pg <= Pmin])
    sp = np.einsum('pmr,r->pm', bt[et], phib); spn = np.linalg.norm(sp)
    pr('    eta = %.2f : ||U_lat - U_BT|| psi = %.2e   bound 2||(1-E)psi|| = %.2e   %s   (BT norm %.12f; spin weights |m=+1,0,-1|^2 = %s)'
       % (et, leak, 2*bad, 'OK' if leak <= 2*bad + 1e-6 else 'VIOLATED', np.linalg.norm(bt[et]),
          np.array2string((np.abs(sp)**2).sum(0)/spn**2, precision=4)))
A2 = np.exp(-(Pg + 0.1)**2/(4*0.07**2)); A2 = A2/np.linalg.norm(A2)
chi = phib + 0.9*(U[:, np.argsort(mu)[4]] + 0.6*U[:, np.argsort(mu)[12]]); chi = chi/np.linalg.norm(chi)
v0 = A2[:, None, None]*spin[None, :, None]*chi[None, None, :]
lat = evolve(v0, c, etas); bt = evolve(v0, one, etas)
pr('(ii) mixed packet (bound + continuum mu = %.4f, %.4f), Gaussian in P_x, sigma = 0.07, P_x0 = -0.1' % (np.sort(mu)[4], np.sort(mu)[12]))
cb = chi @ U
for et in etas:
    leak = np.linalg.norm(lat[et] - bt[et]); best = np.inf
    for mumax in np.unique(np.concatenate([np.sort(mu), [mu.max()]])):
        inS = mu <= mumax + 1e-14
        mp = np.sqrt(mu[inS]**2 + PPERP @ PPERP)
        Pmin = np.max(mp*np.sinh(np.arcsinh(-Pi1x/mp) + et))
        good = np.linalg.norm(A2[Pg > Pmin])*np.linalg.norm(cb[inS])
        best = min(best, 2*np.sqrt(max(1 - good**2, 0)))
    pr('    eta = %.2f : ||U_lat - U_BT|| psi = %.2e   optimised bound 2||(1-E)psi|| = %.2e   %s'
       % (et, leak, best, 'OK' if leak <= best + 1e-6 else 'VIOLATED'))
with open(__file__.replace('.py', '_NP%d.out' % NP), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
