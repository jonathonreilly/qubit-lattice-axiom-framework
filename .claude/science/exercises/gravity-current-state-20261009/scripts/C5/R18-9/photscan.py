"""R18-9: photon gammaGw(b, fw*(pi-b)) grid: Xi_T2g(a), Xi_Eg(a) quadratic coefficients under VWa and mu_E^gamma (per vector)."""
import sys, time, numpy as np, lib9 as L
N = int(sys.argv[1]); t0 = time.time(); out = []
for b in (0.3, 0.6, 1.0, 1.4, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8):
    for fw in (0.1, 0.3, 0.5, 0.75, 1.0):
        P = L.phot_quad(b, fw, N); out.append([b, fw, *P['T2g'], *P['Eg'], P['muE']])
        print('gGw(%.2f,fw=%.2f) N=%d T:(%+.4e %+.4e %+.2e) E:(%+.4e %+.4e %+.2e) muE %+.4e  rho=E1/T1 %.3f  E0-rho*T0 %+.4e' % (b, fw, N, *P['T2g'], *P['Eg'], P['muE'], P['Eg'][1]/P['T2g'][1], P['Eg'][0]-P['Eg'][1]/P['T2g'][1]*P['T2g'][0]), flush=True)
np.save('photscan_N%d.npy' % N, np.array(out)); print('elapsed %.0fs' % (time.time()-t0))
