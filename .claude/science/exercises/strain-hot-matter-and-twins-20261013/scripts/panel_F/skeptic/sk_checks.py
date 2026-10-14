"""Skeptic panel checks (read-only use of the archived R18-5 dirac.py / sublum.py).
(1) position-space hopping range of the root D1 symbol s(k), W(k): Fourier coefficients;
(2) free-vacuum <psibar psi> per Dirac field per site on the root edge, and doubler/corner masses;
(3) physical sizes at a = l_P: additive mass, critical-mass precision, Compton wavelengths in sites;
(4) GW evanescence length in Earth for F1's |m_g|; (5) a/l_P dependence of the Earth exceedance."""
import sys, numpy as np
sys.path.insert(0, '/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/C5/R18-5')
from dirac import D1
b, r = 0.909103708, 0.555604226
L = D1(b, r)
print('W(pi) = %.6f  (corner/doubler rest-mass increments n*W_pi, n=1..3: %s)' % (L.Wpi, [round(n*L.Wpi,4) for n in (1,2,3)]))
# (1) Fourier coefficients
K = 2**16
k = (np.arange(K) + 0.5) * 2*np.pi/K - np.pi
s = L.S(k); W = L.W(k)
ns = [1,2,3,4,6,8,12,16,24,32,48,64]
print('hopping amplitudes |s_n| (odd symbol, sin series) and |W_n| (even, cos series):')
for n in ns:
    sn = np.mean(s*np.sin(n*k))*2   # s(k) = sum s_n sin(nk)
    wn = np.mean(W*np.cos(n*k))*2
    print('  n=%3d  |s_n|=%.3e  |W_n|=%.3e' % (n, abs(sn), abs(wn)))
# nearest-neighbour Wilson for comparison: s=sin k has s_1=1, s_n=0 n>1
# (2) vacuum <psibar psi> = -2 <M/E> per Dirac field per site (4 comps, tr beta = 0), m = 0
N = 64
kk = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
S1, W1 = L.S(kk), L.W(kk)
X, Y, Z = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
M = W1[X] + W1[Y] + W1[Z]
E = np.sqrt(S1[X]**2 + S1[Y]**2 + S1[Z]**2 + M**2)
E = np.where(E == 0, 1e-300, E)
pbp = -2*np.mean(M/E)
print('free vacuum <psibar psi> per Dirac field per site (m=0, N=%d): %.4f  (lattice units)' % (N, pbp))
# (3) sizes
MP_GeV = 1.22089e19; lP = 1.616e-35
alpha = 1/137.036; e2 = 4*np.pi*alpha
dm_lat = 0.041858390  # per e^2, R19-34 root, h=0
print('additive mass on root edge: %.4f e^2 /a = %.3e /a (QED e^2=%.4f) = %.2e GeV at a=l_P; ratio to 1/a = %.2e' % (dm_lat, dm_lat*e2, e2, dm_lat*e2*MP_GeV, dm_lat*e2))
for nm, m in (('electron', 0.000511), ('up/down (MSbar 2 GeV ~ 3.5 MeV)', 0.0035), ('nucleon', 0.938), ('top', 172.7)):
    lam_C = 0.1973269804e-15/m  # reduced Compton wavelength in m (hbar c / m c^2, GeV fm)
    print('  %-30s m*a = %.2e ; reduced Compton wavelength = %.2e m = %.2e sites' % (nm, m/MP_GeV, lam_C, lam_C/lP))
print('  critical-mass precision for the electron at h=0: m_e a / (dm) = %.1e' % (0.000511/MP_GeV/(dm_lat*e2)))
# proton charge radius in sites
print('  proton radius 0.84 fm = %.2e sites' % (0.84e-15/lP))
# (4) evanescence length in Earth
hbarc_eVm = 1.973269804e-7
for mg in (3.63e-9, 2.34e-9, 2.9e-13):
    print('  |m_g| = %.2e eV: decay length hbar c/m_g = %.3g m' % (mg, hbarc_eVm/mg))
print('  100 Hz graviton energy: %.2e eV' % (4.135667696e-15*100))
# (5) a/l_P dependence. canonical mapping (f1_sizes.py): m_g^2 a^2 = 16 pi n a^3 w c/4 with a = l_P in both places, i.e. G = a^2.
# if G is the observed l_P^2 and a is free: m_g^2 = 16 pi G n w c/(4 a).  Exceedance in mu (m_g^2) scales as l_P/a.
exc = 1.62e8
print('  Earth exceedance 1.62e8 at a=l_P; with G fixed to observed, exceedance ~ 1.62e8*(l_P/a): <=1 needs 1/a <= %.1e GeV' % (MP_GeV/exc))
print('  under the literal canonical mapping (G = a^2), exceedance ~ 1.62e8*(a/l_P): it grows with a')
