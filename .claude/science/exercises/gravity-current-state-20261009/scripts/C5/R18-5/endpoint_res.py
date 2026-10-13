"""Resolution check of the VWa1 solve end point photon gammaGw(0.35275, 0.13944), a = 0.57782 (turn width ~ 1 grid step at N=48)."""
import numpy as np
from r1712_lib import *
law = photonGw(0.3527483489, 0.0500002450*(np.pi - 0.3527483489)); a = 0.5778223531
for N in (48, 64, 96):
    T = xi(law, N, 'T2g', 'VWa', lam=a)[0]; E = xi(law, N, 'Eg', 'VWa', lam=a)[0]
    print('N=%3d  12 x (Xi_T2g, Xi_Eg) = (%+.4e, %+.4e)' % (N, 12*T, 12*E), flush=True)
