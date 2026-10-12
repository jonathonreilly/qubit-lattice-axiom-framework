"""R6-3: per-frame translation variance distribution for diamonds (tail check), T given, eta_max=1.5."""
import numpy as np, sys, time
exec(open('r63_mc216.py').read().split('t0 = time.time()')[0])
rng = np.random.default_rng(int(sys.argv[2])); T = float(sys.argv[1]); nf = int(sys.argv[3]); nu = 24
t0 = time.time(); v = np.empty(nf)
for i in range(nf):
    e = sample_eta(1.5); n = rng.normal(size=3); n /= np.linalg.norm(n)
    v[i] = np.array([count(T, e, n, rng.random(4)) for _ in range(nu)]).var(ddof=1)
bs = [np.mean(rng.choice(v, nf)) for _ in range(500)]
print("diamond T=%g frames=%d x %d: mean Var_u/T^2 = %.4f +- %.4f ; median = %.4f ; q99 = %.4f ; max = %.3f ; top-1%% share = %.2f (%.0f s)" %
      (T, nf, nu, v.mean()/T**2, np.std(bs)/T**2, np.median(v)/T**2, np.quantile(v, .99)/T**2, v.max()/T**2, np.sort(v)[-nf//100:].sum()/v.sum(), time.time()-t0))
