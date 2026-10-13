"""R18-9: resolution check of photon quadratic coefficients and x = E0 - rho*T0 (rho = E1/T1) at chosen edges, several N."""
import sys, time, numpy as np, lib9 as L
edges = [(2.0, 0.75), (2.6, 1.0), (2.8, 0.5), (2.8, 1.0), (2.9, 1.0), (3.0, 1.0)]
Ns = [int(x) for x in sys.argv[1].split(',')]
for (b, fw) in edges:
    for N in Ns:
        t0 = time.time(); P = L.phot_quad(b, fw, N); T, E = P['T2g'], P['Eg']; rho = E[1]/T[1]
        print('gGw(%.2f,fw=%.2f) N=%3d T:(%+.5e %+.5e %+.2e) E:(%+.5e %+.5e %+.2e) muE %+.5e rho %.4f x %+.4e a_T0=-T0/T1 %+.4f [%.0fs]' % (b, fw, N, *T, *E, P['muE'], rho, E[0]-rho*T[0], -T[0]/T[1], time.time()-t0), flush=True)
