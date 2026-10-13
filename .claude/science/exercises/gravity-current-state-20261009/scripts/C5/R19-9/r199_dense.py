"""R19-9 (a): dense W1 sweep of the glued exact photon stress: 10000 uniform pairs on T^3 x T^3 and 10000 pairs with
log-uniform leg sizes |k| in [1e-6, pi] (random directions), r from argv. Reports max abs / relative physical-block residual."""
import sys, time, numpy as np, lib199 as L
r = float(sys.argv[1]); rng = np.random.default_rng(int(1e6*r)); t0 = time.time()
def logleg():
    v = rng.normal(size=3); return L.wrap(v/np.linalg.norm(v)*10**rng.uniform(-6, np.log10(np.pi)))
for name, gen in (('uniform T3xT3', lambda: (rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3))),
                  ('log-uniform legs 1e-6..pi', lambda: (logleg(), logleg()))):
    mr = ma = 0.0; cnt = {}
    for _ in range(10000):
        k1, k2 = gen(); M, used, _ = L.glued(k1, k2, r, parts=True)
        for u in used: cnt[u] = cnt.get(u, 0) + 1
        res = L.w1_resid(M, k1, k2); mr = max(mr, max(x[1] for x in res)); ma = max(ma, max(x[0] for x in res))
    print(f'r={r} {name:28s}: max rel {mr:.2e}, max abs {ma:.2e}; piece usage {cnt} [{time.time()-t0:.0f}s]', flush=True)
