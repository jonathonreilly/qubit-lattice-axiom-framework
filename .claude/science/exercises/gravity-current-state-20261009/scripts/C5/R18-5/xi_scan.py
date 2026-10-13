"""R17-12 (c): per-vector graviton-cone shifts Xi (R17-9 pipeline: exact grid shifts + Richardson, beta exact) for
VU and VMone (rechecks of R17-9) and for the W1-forward-correct covariant family VW(n) (n = 0: offsets z +- 1/2;
n = 1: z +- 3/2), plus VMsym (covariant VM with R17-9's Eg).  q || z."""
import sys, time, numpy as np
from r1712_lib import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 48
laws = [photonNN(), photonG(0.6), photonG(1.4), photonG(2.2), photonGw(1.0, 0.8),
        photonGw(0.15, 0.25), photonGw(0.2, 0.5), photonGw(0.25133, 1.01946), photonGw(0.3, 0.5), photonGw(0.3, 1.0),
        photonGw(0.5, 0.5), photonGw(0.8, 0.25)]
vars_ = ['VU', 'VMone', 'VMsym', 'VW0', 'VW1']
t0 = time.time()
print('N=%d   columns: Xi_T2g  Xi_Eg  (Xi_Eg - Xi_T2g)' % N)
for law in laws:
    for var in vars_:
        a = xi(law, N, 'T2g', var)[0]; b = xi(law, N, 'Eg', var)[0]
        print('%-24s %-6s %+.5e %+.5e %+.5e' % (law.name, var, a, b, b - a), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
