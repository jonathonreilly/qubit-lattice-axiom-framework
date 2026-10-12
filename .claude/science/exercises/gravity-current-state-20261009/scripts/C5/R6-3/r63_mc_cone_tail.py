"""R6-3 (c): heavy-tail check for truncated past cones at small T: many frames, report mean, median and
upper quantiles of the per-frame translation variance Var_u N (estimated with 24 torus shifts per frame).
Ensemble Var = E_g Var_u (E_u N = rho V in every frame), so the ensemble value is the mean over frames."""
import numpy as np, time, sys
exec(open('r63_mc_cone.py').read().split('t0 = time.time()')[0])
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 77)
T = float(sys.argv[1]); nf = int(sys.argv[3]) if len(sys.argv) > 3 else 4000; nu = 24
t0 = time.time(); v = np.empty(nf)
for i in range(nf):
    e = sample_eta(1.5); n = rng.normal(size=3); n /= np.linalg.norm(n)
    Ns = np.array([count(T, e, n, rng.random(4)) for _ in range(nu)])
    v[i] = Ns.var(ddof=1)
bs = [np.mean(rng.choice(v, nf)) for _ in range(500)]
print("T=%g frames=%d x %d shifts: mean Var_u/T^3 = %.4f +- %.4f ; median = %.4f ; q90 = %.4f ; q99 = %.4f ; max = %.3f ; top-1%% share of mean = %.2f  (%.0f s)" %
      (T, nf, nu, v.mean()/T**3, np.std(bs)/T**3, np.median(v)/T**3, np.quantile(v, .9)/T**3, np.quantile(v, .99)/T**3, v.max()/T**3,
       np.sort(v)[-nf//100:].sum()/v.sum(), time.time()-t0), flush=True)
