"""F5 (a)/(b)(i): the mass derivative of the one-loop P = 0 self-energy on F1's SF law (B1, Psym, E_g), via F1's UNMODIFIED
library (dm_sf with propagator mass mprop = m).  Gives
  - the implicit-function slope dm_pole/dm0 = 1 + e^2 z(m), z = [Sigma(m) - Sigma(0)]/m (uniqueness of m_c(h) near the free point);
  - the strain Hessian of z (the multiplicative channel's coefficient z'' = d^2_t z, SF units), extrapolated m -> 0.
Euclidean, off-shell P = 0 (R19-34 found the on-shell/off-shell difference O(m)); an ESTIMATE of the on-shell z''.
argv: n hmax mph d"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f1_lib as L
t00 = time.time()
n, hm, mph, d = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
br = [L.ROOT[0], np.pi - L.ROOT[0]] + [L.CPH + i*(np.pi - L.CPH)/mph for i in range(mph)]
g = L.Grid(br, n, hm)
F = L.Ferm(*L.ROOT, mflow=0.01); G = L.Phot(L.CPH)
print('grid n=%d hmax=%.2f mph=%d (%d nodes), d=%.4f; R18-9 root B1 Psym; per e^2, SF units' % (n, hm, mph, len(g.x), d), flush=True)
res = {}
for m in (0.0, 0.0025, 0.005, 0.01, 0.02):
    f0 = L.dm_sf(F, G, g, 0.0, mprop=m); f1 = L.dm_sf(F, G, g, d, mprop=m, nrk=2); f2 = L.dm_sf(F, G, g, 2*d, mprop=m, nrk=2)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2; hr = (4*h1 - h2)/3
    res[m] = (f0, hr)
    print('  m=%.4f  Sigma(P=0) %+.10f  Hess_t %+.7e' % (m, f0, hr), flush=True)
S0, H0 = res[0.0]
for m in (0.0025, 0.005, 0.01, 0.02):
    print('  m=%.4f  z(m) = [Sigma(m)-Sigma(0)]/m = %+.6f   z\'\' = [Hess(m)-Hess(0)]/m = %+.6e' % (m, (res[m][0] - S0)/m, (res[m][1] - H0)/m))
print('time %.0f s' % (time.time() - t00))
