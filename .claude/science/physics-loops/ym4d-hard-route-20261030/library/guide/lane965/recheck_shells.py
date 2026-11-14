#!/usr/bin/env python3
"""Row 965 Step 6: recheck of two G1 instances by eigenvalue log-determinants (eigvalsh),
because numpy's slogdet printed floating-point warnings in squeeze_guide.log. GUIDE only."""
import math, sys, warnings
import numpy as np
sys.path.insert(0, sys.argv[1])
import squeeze_guide as g
warnings.simplefilter("error")  # any floating-point warning now raises
for (b, r, ma) in ((12, 2, 4.0), (16, 4, 4.0)):
    a = b // r; m = ma / a
    eps = g.modes(b, m)
    Cd = g.kernel(b, 1/(2*np.sinh(eps))); CAd = g.kernel(b, np.exp(-a*eps)/(2*np.sinh(eps)))
    out = []
    for (side, off) in g.schedule(b)[1:]:
        sites = g.box_sites(b, side, off)
        Cq = g.sub_matrix(Cd, b, sites); CAq = g.sub_matrix(CAd, b, sites)
        l1 = np.sum(np.log(np.linalg.eigvalsh(Cq))); l2 = np.sum(np.log(np.linalg.eigvalsh(Cq - CAq)))
        out.append(math.exp(l1 - l2) - 1)
    print(b, r, ma, "S_j (j>=1) by eigvalsh:", ["%.6e" % v for v in out])
