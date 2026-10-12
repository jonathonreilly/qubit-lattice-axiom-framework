"""R8-1, script 4 (d = 1): finite interacting boosts and the interacting leakage bound.

On states whose legs stay in the one-body box (here |q| < kappa and |P| <= 2), the lattice law in the
canonical chart (P, q) is exactly (Lemma L + chart identity, r81_d2_chart_algebra (a), d = 1 analogue)
  K_lat = (1/2){H_c(P), i d/dP},  H_c(P) = (1 - c(P)) sqrt(M0^2 + P^2) + c(P) sqrt(M^2 + P^2),
and the exact BT comparator is the same with c == 1.  We integrate d psi/d eta = -i K psi
(transport toward negative P) for both, on a spectral P-grid x Nystrom q-grid on supp g.
Theorem L (interacting leakage):  ||U_lat(eta) psi - U_BT(eta) psi|| <= 2 ||(1 - E) psi||,
  E = 1_I(P) 1_Sigma(M), for any interval I and spectral set Sigma whose BT orbits over [0, eta]
  (P -> mu sinh(asinh(P/mu) - s), mu in Sigma) stay in |P| < Pi1 (legs in the box automatically here).
Checks: (i) compactly supported bound-state packet: zero leakage until eta* = asinh(Pi1/M_b) - asinh(a/M_b);
(ii) bound + scattering mix: leakage vs the optimised bound over Sigma = spec(M) cap [0, mu_max].
"""
import numpy as np, sys
from r81_common import sstep, BTKernel, lam_for_mass

m, KAP, MU_B, PI1, PI2 = 0.5, 0.4, 0.85, 0.6, 1.2
lam = lam_for_mass(m, KAP, 1, MU_B)
Kk = BTKernel(m, KAP, lam, 1)
NQ = 241
q = np.linspace(-KAP, KAP, NQ); wq = np.full(NQ, q[1]-q[0])
sw = np.sqrt(wq)
M0 = Kk.M0(q)
Mm = np.diag(M0) + lam*np.outer(Kk.g1(q)*sw, Kk.g1(q)*sw)
mu, U = np.linalg.eigh(Mm)
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 640
Wn = 2.4
ONLY_I = len(sys.argv) > 2
Pg = np.linspace(-Wn, Wn, NP, endpoint=False); dP = Pg[1]-Pg[0]
kP = 2*np.pi*np.fft.fftfreq(NP, d=dP)
c = sstep((PI2 - np.abs(Pg))/(PI2 - PI1))
dc = np.gradient(c, dP)        # only used inside the transition shell; spectral below
dc = np.real(np.fft.ifft(1j*kP*np.fft.fft(c)))
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
pr('M spectrum min = %.10f (target %.2f); NP = %d on [-%.1f, %.1f), NQ = %d' % (mu.min(), MU_B, NP, Wn, Wn, NQ))

def Hc_apply(v, cc, dcc, deriv=False):
    """H_c(P) v and (d/dP H_c) v, v shape (NP, NQ) in the q-grid (Nystrom-weighted) basis."""
    P2 = Pg[:, None]**2
    vb = v @ U                                      # to M eigenbasis
    hM = np.sqrt(mu[None, :]**2 + P2); h0 = np.sqrt(M0[None, :]**2 + P2)
    HMv = (vb*hM) @ U.T; H0v = v*h0
    if not deriv:
        return (1 - cc)[:, None]*H0v + cc[:, None]*HMv
    dHM = (vb*(Pg[:, None]/hM)) @ U.T; dH0 = v*(Pg[:, None]/h0)
    return (-dcc)[:, None]*H0v + (1 - cc)[:, None]*dH0 + dcc[:, None]*HMv + cc[:, None]*dHM

def rhs(v, cc, dcc):            # -i K v = (1/2){H_c, d/dP} v = H_c dv/dP + (1/2)(dH_c/dP) v
    dv = np.fft.ifft(1j*kP[:, None]*np.fft.fft(v, axis=0), axis=0)
    return Hc_apply(dv, cc, dcc) + 0.5*Hc_apply(v, cc, dcc, deriv=True)

def evolve(v0, cc, dcc, etas, dt=2.0e-3*640/NP):
    v = v0.astype(complex); t = 0.0; res = {}
    for et in etas:
        while t < et - 1e-12:
            h = min(dt, et - t)
            k1 = rhs(v, cc, dcc); k2 = rhs(v + 0.5*h*k1, cc, dcc); k3 = rhs(v + 0.5*h*k2, cc, dcc); k4 = rhs(v + h*k3, cc, dcc)
            v = v + (h/6)*(k1 + 2*k2 + 2*k3 + k4); t += h
        res[et] = v.copy()
    return res

phib = U[:, np.argmin(mu)]                        # bound state (Nystrom-weighted vector)
etas = [0.1, 0.2, 0.3, 0.37, 0.45, 0.6, 0.8, 1.0]
# (i) compactly supported P-profile, radius a = 0.25, around P0 = 0 (C^inf bump)
a = 0.25
A = sstep(1 - (Pg/a)**2); A = A/np.linalg.norm(A)
v0 = A[:, None]*phib[None, :]
lat = evolve(v0, c, dc, etas); bt = evolve(v0, np.ones(NP), np.zeros(NP), etas)
eta_star = np.arcsinh(PI1/MU_B) - np.arcsinh(a/MU_B)
pr('(i) bound-state packet, P-support |P| < %.2f; exact range eta* = asinh(Pi1/M_b) - asinh(a/M_b) = %.4f' % (a, eta_star))
for et in etas:
    # BT analytic transport for mass M_b: half-density pull-back along P -> M_b sinh(asinh(P/M_b) + eta)
    th = np.arcsinh(Pg/MU_B); Pb = MU_B*np.sinh(th + et)
    Aan = sstep(1 - (Pb/a)**2)*np.sqrt(np.cosh(th + et)/np.cosh(th))/np.linalg.norm(sstep(1 - (Pg/a)**2))
    an_err = np.linalg.norm(bt[et] - Aan[:, None]*phib[None, :])
    leak = np.linalg.norm(lat[et] - bt[et])
    # bound: weight of P whose orbit over [0, eta] leaves |P| < Pi1  (Sigma = {M_b})
    Pmin = MU_B*np.sinh(np.arcsinh(-PI1/MU_B) + et)
    bad = np.linalg.norm(A[Pg <= Pmin])
    pr('    eta = %.2f : ||U_lat - U_BT|| psi = %.2e   bound 2||(1-E)psi|| = %.2e   (BT integrator vs analytic transport %.1e)'
       % (et, leak, 2*bad, an_err))
if ONLY_I:
    open(__file__.replace('.py', '_NP%d.out' % NP), 'w').write('\n'.join(out) + '\n'); sys.exit(0)
# (ii) mixed packet: Gaussian P-profile, bound + continuum internal state
A2 = np.exp(-(Pg + 0.1)**2/(4*0.07**2)); A2 = A2/np.linalg.norm(A2)
chi = phib + 0.9*(U[:, np.argsort(mu)[6]] + 0.6*U[:, np.argsort(mu)[30]])
chi = chi/np.linalg.norm(chi)
v0 = A2[:, None]*chi[None, :]
lat = evolve(v0, c, dc, etas); bt = evolve(v0, np.ones(NP), np.zeros(NP), etas)
pr('(ii) mixed packet (bound + two continuum levels mu = %.4f, %.4f), Gaussian in P, sigma = 0.07, P0 = -0.1'
   % (np.sort(mu)[6], np.sort(mu)[30]))
cb = chi @ U                                       # spectral amplitudes in M
for et in etas:
    leak = np.linalg.norm(lat[et] - bt[et])
    best = np.inf
    for mumax in np.unique(np.concatenate([np.sort(mu)[:40], [mu.max()]])):
        inS = mu <= mumax + 1e-14
        Pmin = np.max(mu[inS]*np.sinh(np.arcsinh(-PI1/mu[inS]) + et))   # fastest mu in Sigma sets the edge
        Ein = (Pg > Pmin)
        good = np.linalg.norm(A2[Ein])*np.linalg.norm(cb[inS])          # ||E psi|| (product state)
        badn = np.sqrt(max(1 - good**2, 0))
        best = min(best, 2*badn)
    pr('    eta = %.2f : ||U_lat - U_BT|| psi = %.2e   optimised bound 2||(1-E)psi|| = %.2e   %s'
       % (et, leak, best, 'OK' if leak <= best + 1e-12 else 'VIOLATED'))
with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
