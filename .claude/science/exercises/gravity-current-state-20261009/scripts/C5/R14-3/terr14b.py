"""(a) at b = 1.4, refined: sharp first drop (w1), long flat terrace, late steep rise, short final flattening."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
b = 1.4
res = []
for w1 in [0.05, 0.1]:
    for a2 in [2.4, 2.55, 2.7, 2.85]:
        for w2 in [0.05, 0.1]:
            for w3 in [0.05, 0.1, 0.2]:
                a3 = np.pi - w3
                if a2 + w2 > a3 - 0.01: continue
                law = Law([1.0, 0.0, 1.0, 0.0], [b, a2, a3], [w1, w2, w3], 'T(w1=%.2f,a2=%.2f,w2=%.2f,w3=%.2f)' % (w1, a2, w2, w3))
                mu, X = evaluate(law, 0.1, n=1 << 15, nu=1500)
                res.append((mu, law.name))
                print('%-36s m=0.1 mu_E=%+.5e sigma(pi)=%.3f' % (law.name, mu, law.sig_pi), flush=True)
res.sort(); print('most negative:', res[:4]); print('runtime %.1fs' % (time.time()-T0))
