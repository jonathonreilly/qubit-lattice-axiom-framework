"""R17-9: whole-zone v_max of the gauge symbols used (round-17 'gauge fields too' rule): R9-9's graviton d(q) (c1=1, c2=2.5),
R8-5's photon (c1=1, c2=2), and the VM-root photon. Separable omega^2 = sum d(k_i)^2 => |grad omega| <= max|d'| (Cauchy-Schwarz)."""
import numpy as np
from sublum import sstep
from photon import photonGw
a = np.linspace(0, np.pi, 400001)
for c1, c2, nm in ((1.0, 2.5, "R9-9 graviton d(q)"), (1.0, 2.0, "R8-5 photon")):
    rho = 1 - sstep((a - c1)/(c2 - c1)); d = rho*a + (1 - rho)*2*np.sin(a/2); dp = np.gradient(d, a)
    print('%s: d\' in [%.6f, %.6f]  => whole-zone v_max = %.6f' % (nm, dp.min(), dp.max(), np.abs(dp).max()))
z = np.load('verified_VM.npy'); L = photonGw(z[0], z[1]*(np.pi - z[0]))
print('VM-root photon %s: d\' in [%.6f, %.6f], v_max = %.6f' % (L.name, L.mindp, L.maxdp, L.maxdp))
