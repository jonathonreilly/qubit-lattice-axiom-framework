"""R6-3: extra diamond MC at T=432 (eta_max=1.5), saving raw counts so runs can be pooled."""
import numpy as np, sys
exec(open('r63_mc216.py').read().split('t0 = time.time()')[0])
seed = int(sys.argv[1]); n = int(sys.argv[2]); rng = np.random.default_rng(seed)
T = 432.0; Ns = np.empty(n)
for i in range(n):
    e = sample_eta(1.5); v = rng.normal(size=3); v /= np.linalg.norm(v)
    Ns[i] = count(T, e, v, rng.random(4))
np.save('r63_mc432_seed%d.npy' % seed, Ns)
print("seed %d done" % seed)
