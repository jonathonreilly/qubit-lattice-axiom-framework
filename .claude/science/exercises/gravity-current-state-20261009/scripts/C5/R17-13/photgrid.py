"""R17-13 photgrid: VM photon rows per vector (Xi_T2g, Xi_Eg, mu_E) on gammaGw(b, fw*(pi-b)) at N=48 (archived R17-9 smsolve_lib.phot), saved to photgrid.npy."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1])
import smsolve_lib as L
L.vert = 'VM'; t0 = time.time(); out = []
for b in (0.15, 0.2, 0.25, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6, 2.0, 2.4, 2.8):
    for fw in (0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0):
        v = L.phot(b, fw, 48)[0]; out.append([b, fw, *v[:3]])
        print('gammaGw(%.2f, fw=%.2f) VM N=48: T2g %+.4e Eg %+.4e muE %+.4e' % (b, fw, *v[:3]), flush=True)
np.save('photgrid.npy', np.array(out)); print('elapsed %.0fs' % (time.time()-t0))
