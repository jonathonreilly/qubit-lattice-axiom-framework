"""E3 (b2): does the perturbed-lattice mean go to zero at large displacement s?  High-statistics L = 8 (N = 512) runs at
s = 0.5, 0.8, 1.2, 1.6 and an iid (Poisson, fixed N) control in the SAME box to calibrate the torus-shape offset.
pd coupling, boson m2 = 1. Mean per channel (+- SE over realizations) and mean minus control."""
import numpy as np, time
import e23_core as c
rng = np.random.default_rng(808)
Lb, nr = 8, 400
g = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)
res = {}
for s in ['iid', 0.5, 0.8, 1.2, 1.6]:
    t0 = time.time(); acc = []
    for _ in range(nr):
        X = rng.uniform(0, Lb, g.shape) if s == 'iid' else np.mod(g + s * rng.standard_normal(g.shape), Lb)
        I, J, D = c.pairs_sparse(X, Lb, 'pd'); out, _ = c.derivs(len(X), I, J, D, 'pd', [c.boson_fns(1.0)])
        acc.append(out[0, :, 1])
    A = np.array(acc); res[s] = A
    print(f"s={s}: " + " | ".join(f"{ch}: {A[:, idx].mean():+.5f}+-{A[:, idx].mean(1).std(ddof=1)/np.sqrt(nr):.5f}" for ch, idx in c.CH.items())
          + f"  [{time.time()-t0:.0f}s]", flush=True)
print("mean minus iid control (same box):")
for s in [0.5, 0.8, 1.2, 1.6]:
    print(f"s={s}: " + " | ".join(
        f"{ch}: {res[s][:, idx].mean()-res['iid'][:, idx].mean():+.5f}+-{np.hypot(res[s][:, idx].mean(1).std(ddof=1), res['iid'][:, idx].mean(1).std(ddof=1))/np.sqrt(nr):.5f}"
        for ch, idx in c.CH.items()))
np.savez("E3_b2.npz", **{str(k): v for k, v in res.items()})
