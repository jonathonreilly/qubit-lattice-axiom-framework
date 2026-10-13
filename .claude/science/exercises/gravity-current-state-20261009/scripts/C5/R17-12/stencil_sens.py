"""R17-12 (c): sensitivity of the vector Xi rows to the residual placement datum (W1-invisible, covariant):
P(s) = (1-a) cos(s/2) + a cos(3s/2), lam = 1/4 + 2a (O(q^2) coefficient -lam/2).  a = 0: VW0; a = 1: VW1."""
import numpy as np, time
from r1712_lib import *
t0 = time.time()
for law in (photonGw(0.25133, 1.01946), photonGw(0.3, 1.0), photonG(1.4)):
    for a in (-0.3, -0.2, -0.1, 0.0, 0.1, 0.2):
        T = xi(law, 48, 'T2g', 'VWa', lam=a)[0]; E = xi(law, 48, 'Eg', 'VWa', lam=a)[0]
        print('%-24s a=%+.2f lam=%+.3f  Xi_T2g %+.4e  Xi_Eg %+.4e  diff %+.4e' % (law.name, a, 0.25 + 2*a, T, E, E - T), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
