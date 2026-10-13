"""R18-9: high-resolution photon quadratic coefficients for the b_gamma -> pi corner. argv: N, then edges b:fw,..."""
import sys, time, numpy as np, lib9 as L
N = int(sys.argv[1]); edges = [tuple(map(float, e.split(':'))) for e in sys.argv[2].split(',')]
out = []
for (b, fw) in edges:
    t0 = time.time(); P = L.phot_quad(b, fw, N); T, E = P['T2g'], P['Eg']; rho = E[1]/T[1]
    out.append([b, fw, *T, *E, P['muE']])
    print('gGw(%.3f,fw=%.2f) N=%3d T:(%+.5e %+.5e %+.2e) E:(%+.5e %+.5e %+.2e) muE %+.5e rho %.4f x %+.4e a_T0 %+.4f turn/h %.2f [%.0fs]' % (b, fw, N, *T, *E, P['muE'], rho, E[0]-rho*T[0], -T[0]/T[1], fw*(np.pi-b)/(2*np.pi/N), time.time()-t0), flush=True)
np.save('photres2_N%d_%s.npy' % (N, sys.argv[3] if len(sys.argv) > 3 else 'x'), np.array(out))
