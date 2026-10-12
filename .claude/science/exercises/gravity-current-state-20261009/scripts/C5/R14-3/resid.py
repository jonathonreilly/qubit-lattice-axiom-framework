"""Light-species residual of the m -> 0 tuned subluminal edge: mu_E(m) at fixed t*(m = 0.01)."""
import numpy as np, sys
sys.path.insert(0, '.')
from prof import *; from lap import *
exec(open('root.py').read().split('for law in [E1, E2]:')[0].split('T0 = time.time()')[1])
ts = 0.894027
law = Mix(ts)
for m in [0.001, 0.01, 0.03, 0.1, 0.3, 1.0]:
    mu, X = evaluate(law, m, n=1 << 17, nu=6000, umin=-24)
    print('t*=%.6f m=%.3f mu_E=%+.4e  mu_E/m^2=%+.4e  v_max(d=3)=%.6f' % (ts, m, mu, mu/m**2, law.vmax(m)), flush=True)
