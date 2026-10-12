import numpy as np, sys
sys.path.insert(0, '.')
from prof import *; from lap import *
exec(open('root.py').read().split('for law in [E1, E2]:')[0].split('T0 = time.time()')[1])
law = Mix(0.894027)
for (n, nu, umin) in [(1 << 15, 3000, -18), (1 << 17, 6000, -24), (1 << 18, 12000, -24)]:
    out = []
    for m in [0.0003, 0.001, 0.003, 0.01]:
        out.append(evaluate(law, m, n=n, nu=nu, umin=umin)[0])
    print('n=2^%d nu=%d: ' % (int(np.log2(n)), nu) + '  '.join('m=%.4f %+.4e' % (m, x) for m, x in zip([0.0003, 0.001, 0.003, 0.01], out)), flush=True)
