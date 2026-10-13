"""R19-21 addendum (coordinator request; R19-20 item 3): the ONE-POINT enthalpy mismatch W = rho + p of the lattice Dirac sea in
non-lowest states, on R19-11's 0+ ROOT edge D1(b_f, r) (not naive Wilson), and its channels (vev shift, today's matter).
Per 4-component Dirac field, zero-point e(m) = -2<E>, E^2 = sum S^2 + (m + sum W)^2 (Wilson-type) or sum S^2 + (sum W)^2 + m^2 (twisted).
Isotropic dilation at fixed law data (H-cov dilation = same law at new spacing; R19-17's scaling): p = (e - m e')/3, so
  W(m) = (4e - m e')/3,  dW/dm|0 = e'(0) = -2<W_tot/E>_0,  dp/dm|0 = 0  (Wilson-type);   twisted: dW/d(m^2)|0 = (2/3) e_2, e_2 = -<1/E>_0.
Uses R18-5's D1 class (dirac.py + sublum.py, unmodified copies in ../arch/R18-5). Units: lattice, a = l_P, M_P = 1.22089e19 GeV.
rho_Lambda a^4 = 1.134e-123 (as rR19-14:7, RECALLED)."""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R18-5'))
from dirac import D1, kgrid
MP = 1.22089e19; rhoL = 1.134e-123; v = 246.22; mH = 125.25
def sea(law_S, law_W, N, m, kind):
    k = kgrid(N); s, w = law_S(k), law_W(k)
    X = s[:, None, None]**2 + s[None, :, None]**2 + s[None, None, :]**2
    Wt = w[:, None, None] + w[None, :, None] + w[None, None, :]
    if kind == 'W': E = np.sqrt(X + (m + Wt)**2); dEdm = (m + Wt)/E
    else: E = np.sqrt(X + Wt**2 + m*m); dEdm = m/E
    return -2*E.mean(), -2*dEdm.mean(), (1.0/E).mean()
# naive Wilson control (R19-20: d rho/dm = -1.767029 at N = 96)
for N in (96,):
    e0, de, invE = sea(np.sin, lambda k: 1 - np.cos(k), N, 0.0, 'W')
    print('naive Wilson r=1, N=%d: e0 %+.6f  de/dm %+.6f (R19-20: -1.767029)' % (N, e0, de))
law = D1(0.915438682, 0.568280847)       # R19-11 0+ root Dirac edge (b_f, r)
print('D1 root edge (b_f, r) = (0.915438682, 0.568280847): W_pi = %.5f' % law.Wpi)
for N in (64, 96, 128):
    e0, de, invE = sea(law.S, law.W, N, 0.0, 'W')
    print('  N=%3d: e0 = %+.7f   dW/dm = d rho/dm = e\'(0) = %+.7f   twisted e_2 = -<1/E> = %+.6f -> dW/dm^2 = %+.6f' % (N, e0, de, -invE, -2*invE/3), flush=True)
dWdm, dWdm2 = de, -2*invE/3
# finite-difference check of the scaling formula's ingredients at the root edge (N = 96)
h = 1e-4
ep, _, _ = sea(law.S, law.W, 96, h, 'W'); em, _, _ = sea(law.S, law.W, 96, -h, 'W'); e00, _, _ = sea(law.S, law.W, 96, 0.0, 'W')
print('  FD check (N=96): (e(h)-e(-h))/2h = %+.7f ; W(m) = (4e - m e\')/3 -> dp/dm|0 = -m e\'\'/3 = 0 exactly at m = 0' % ((ep - em)/(2*h)))
dirac = {'t': (172.69, 3), 'b': (4.18, 3), 'c': (1.27, 3), 's': (0.0934, 3), 'd': (0.00467, 3), 'u': (0.00216, 3),
         'tau': (1.77686, 1), 'mu': (0.10566, 1), 'e': (0.000511, 1)}
S1 = sum(n*m for m, n in dirac.values())/MP; S2 = sum(n*m*m for m, n in dirac.values())/MP**2
print('\nSymmetric phase (all Dirac masses -> 0): Delta W = W(0) - W(m_SM)')
for name, dW in (('Wilson-type D1 edge (linear)', -dWdm*S1), ('twisted-mass edge (quadratic)', -dWdm2*S2)):
    print('  %-30s Delta W = %+.3e per cell = %.2e rho_Lambda' % (name, dW, dW/rhoL))
gs = 106.75
for T in (1e16, 1e8, 1e3, 160.0):
    rr = (np.pi**2/30)*gs*(T/MP)**4
    print('  T = %-8.3g GeV: rho_rad = %.2e rho_Lambda;  |Delta W|/rho_rad = %.1e (Wilson-type D1), %.1e (twisted)' % (T, rr/rhoL, abs(dWdm*S1)/rr, abs(dWdm2*S2)/rr))
print('\nToday, matter channel (dv/v = -f_N rho/(v^2 m_H^2), f_N = 0.30 RECALLED):')
G4 = 5.61e23*(1.973e-14)**3
for name, rho in (('mean IGM baryons', 0.0224*1.878e-29), ('Earth', 5.5)):
    dx = -0.30*rho*G4/(v*v*mH*mH); rho_a4 = rho*G4/MP**4
    dWl = dWdm*S1*dx; dWq = dWdm2*S2*2*dx
    print('  %-17s dv/v %+.2e: Delta W = %+.2e (D1 linear), %+.2e (twisted) per cell; matter rho a^4 = %.2e -> ratios %.1e, %.1e'
          % (name, dx, dWl, dWq, rho_a4, abs(dWl)/rho_a4, abs(dWq)/rho_a4))
