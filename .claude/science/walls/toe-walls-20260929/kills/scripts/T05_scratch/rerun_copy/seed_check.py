"""Seed robustness of arms (a), (b): repeat with 5 other seeds, M=30000 (F) / 10000 (S)."""
import sys, numpy as np
sys.argv = ["x", "30000"]
import calib_test as C
evens = np.where(C.parity == 0)[0]
out = []
for seed in [1, 2, 3, 4, 5]:
    C.rng = np.random.default_rng(seed)
    vals, P, Ph, X = C.world_formation(30000, "random")
    ra = C.calib(P.reshape(-1, 6), X.reshape(-1))
    qs = C.static_probs(vals, evens)
    rc = C.calib(qs.reshape(-1, 6), vals[:, evens].reshape(-1))
    print(f"seed {seed}: (a) chi2/df={ra['chi2_df']:.3f} max|z|={ra['zmax']:.2f} | (c) chi2/df={rc['chi2_df']:.2f}", flush=True)
    out.append((ra['chi2_df'], ra['zmax']))
print("mean (a) chi2/df over 5 seeds + original 1.372:", np.mean([o[0] for o in out] + [1.372]))
