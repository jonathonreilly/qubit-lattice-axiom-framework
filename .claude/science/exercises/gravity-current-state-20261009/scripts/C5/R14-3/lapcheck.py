import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
for law in [G_law(1.4), S_law(1.4), Law([1.0, 0.0, 1.0, 0.0], [0.6, 1.5, 2.7], [0.2, 0.1, np.pi-2.7], 'terrace(0.6,1.5,2.7)')]:
    for m in [1.0, 0.3, 0.1]:
        mu, X = evaluate(law, m)
        mu2, X2 = evaluate(law, m, n=1 << 17, nu=6000, umin=-22)
        print('%s m=%.1f  Laplace: mu_E=%+.8e (n2: %+.8e) | ' % (law.name, m, mu, mu2) + ' '.join('%s %+.6e' % (v, x) for v, x in X.items()), flush=True)
        if m == 1.0 or law.name.startswith('terrace'):
            for N in ([160, 320] if not law.name.startswith('terrace') else [160, 320, 480]):
                a, b = mu_E(law, m, N)
                print('     grid N=%d: mu_E IBP form %+.8e  A-form %+.8e' % (N, b, a), flush=True)
            Xg = Xi(law, m, 160)
            print('     grid N=160 Xi (IBP): ' + ' '.join('%s %+.6e' % (v, x[1]) for v, x in Xg.items()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
