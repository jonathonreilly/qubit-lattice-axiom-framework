"""R19-24 recheck of the archived runners (R16-10 Theorem-L split, R16-2/R10-1 photon moment, R18-5 photon)
through R19-12's unmodified r1912_lib.py, at the refined gravity-root edges. Targets: R19-12 r1912_a.out
(F_1/2 N=64 -5.24436, N=128 -5.24444; F_0 N=128 -1.16743; G_1/2(m=0.0025, N=128) +0.114293; G_0 -0.059166)."""
import time, numpy as np
from r1912_lib import *
t0 = time.time(); R = ROOT; d, pr = photon_Gw(R['bg'], np.pi - R['bg']); cb = R['bg']
for N in (64, 128):
    Fd, Td = F_dirac(R['bf'], R['r'], d, cb, N); Fs, Ts = F_scalar(R['bs'], d, cb, N)
    print('N=%3d F_1/2(0+)=%+.5f [tad %+.5f]  F_0(0+)=%+.5f [sea %+.5f] (%.0fs)' % (N, Fd, Td, Fs, Ts, time.time()-t0), flush=True)
g12 = G_dirac(R['bf'], R['r'], 0.0025, 128); g0 = G_scalar(R['bs'], 0.0025, 128)
print('N=128 m=0.0025 G12=%+.6f G0=%+.6f (%.0fs)' % (g12, g0, time.time()-t0), flush=True)
u = u_phys
F = F_dirac(R['bf'], R['r'], d, cb, 128)[0]; Sig = 8*0.11484
print('u=%.4e  kappa_e=%+.4e kappa_u=%+.4e kappa_d=%+.4e kappa_gamma=%+.4e (uSigma with Sigma=8*0.11484)' % (u, -u*F, -u*F*4/9, -u*F/9, -u*Sig))
print('bare in-box speed under a D1 counterterm on the spatial symbol: 1+kappa_e = %.5f (whole-zone v_max of the bare e-class law)' % (1 - u*F))
