"""(a) at b = 1.4: monotone terrace laws (0 <= sigma' <= 1, subluminal for every m) -- search for mu_E < 0.
sigma': 1 -> 0 on [b, b+w1]; 0 -> c on [a2, a2+w2]; c -> 0 on [a3, pi]."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
b = 1.4
best = []
for w1 in [0.15, 0.3]:
    for a2 in [1.8, 2.0, 2.2, 2.4]:
        for w2 in [0.1, 0.2, 0.3]:
            for a3 in [2.6, 2.8, 2.95]:
                if a2 + w2 > a3 - 0.02 or b + w1 > a2: continue
                law = Law([1.0, 0.0, 1.0, 0.0], [b, a2, a3], [w1, w2, np.pi-a3], 'T(w1=%.2f,a2=%.1f,w2=%.1f,a3=%.2f)' % (w1, a2, w2, a3))
                mu, X = evaluate(law, 0.1, n=1 << 15, nu=1500)
                best.append((mu, law.name))
                print('%-34s m=0.1 mu_E=%+.5e  sigma(pi)=%.3f' % (law.name, mu, law.sig_pi), flush=True)
best.sort()
print('most negative:', best[:5])
print('runtime %.1fs' % (time.time()-T0))
