"""R17-12 (a): W1 at O(q) = forward-value test. For random k (box and edge), compare the forward scattering stress
S_ll'(k,k) of each vertex with the W1-required -(w/2) e:(vv) delta_ll'. Also: the weaker rank-one test (any common
polarization matrix Lambda with S^e = e:(vv) Lambda for both TT components)."""
import numpy as np
from r1712_lib import *
rng = np.random.default_rng(7)
laws = [photonNN(), photonG(1.4), photonGw(0.25133, 1.01946), photonGw(0.3, 0.5)]
vars_ = ['VU', 'VMone', 'VMsym', 'VW0', 'VW1']
for law in laws:
    print('== %s (box |k_i| <= b: c = 1)' % law.name)
    for region in ('box', 'zedge', 'any'):
        ks = []
        for _ in range(400):
            if region == 'box':
                kv = rng.uniform(-0.2, 0.2, 3)
            elif region == 'zedge':      # transverse in box, k_z outside the photon box
                kv = np.array([rng.uniform(-0.2, 0.2), rng.uniform(-0.2, 0.2), rng.uniform(1.6, 3.0)*rng.choice([-1, 1])])
            else:
                kv = rng.uniform(-np.pi, np.pi, 3)
            ks.append(kv)
        for pol in ('T2g', 'Eg'):
            row = []
            for var in vars_:
                worst = 0.0; worst_rank1 = 0.0; scale = 0.0
                for kv in ks:
                    S, Sreq = forward_S(law, kv, pol, var)
                    worst = max(worst, np.abs(S - Sreq).max()); scale = max(scale, np.abs(Sreq).max())
                    # rank-one test needs both TT components: done below via ratio consistency
                row.append('%s %.2e' % (var, worst))
            print('  %-5s %-4s max|S - S_req| (scale %.2e): ' % (region, pol, scale) + ', '.join(row))
    # rank-one (weak) test: Lambda from T2g must reproduce Eg, for VU and VMone
    for var in ('VU', 'VMone', 'VW0'):
        dev = 0.0; n = 0
        for _ in range(400):
            kv = rng.uniform(-np.pi, np.pi, 3)
            sig = law.sig(kv); sp = law.dpr(kv); w = np.linalg.norm(sig); v = sig*sp/w
            S1, _ = forward_S(law, kv, 'T2g', var); S2, _ = forward_S(law, kv, 'Eg', var)
            a1 = v @ EPOL['T2g'] @ v; a2 = v @ EPOL['Eg'] @ v
            if abs(a1) < 1e-3 or abs(a2) < 1e-3: continue
            L1 = S1/a1; L2 = S2/a2
            dev = max(dev, np.abs(L1 - L2).max()/max(np.abs(L1).max(), 1e-12)); n += 1
        print('  rank-one test %-6s: max rel |Lambda_T2g - Lambda_Eg| over %d edge/zone points = %.3e' % (var, n, dev))
