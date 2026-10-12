"""E2 (a) noise extension: larger boxes at p = 0.1, 0.3116 (site-percolation threshold), 0.5 for both couplings,
bosons m2 = 1 and 0.04. Same estimator as E2_1 (per-direction sd * sqrt(N_present)); KD-tree pairs (checked
identical to dense pairs to 5e-16).  usage: python3 E2_1b_noise_extension.py mode"""
import numpy as np, sys, time
import e23_core as c
mode = sys.argv[1]
rng = np.random.default_rng({'pd': 31, 'nn': 32}[mode])
PLAN = {0.1: {14: 60, 18: 40, 24: 20}, 0.3116: {14: 40, 16: 30, 18: 20}, 0.5: {14: 30, 16: 20}}
fns = [c.boson_fns(1.0), c.boson_fns(0.04)]
for p, plan in PLAN.items():
    for Lb, nr in plan.items():
        g = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)
        t0 = time.time(); acc = []; Ns = []
        for _ in range(nr):
            X = g[rng.random(len(g)) < p]
            I, J, D = c.pairs_sparse(X, Lb, mode)
            out, _ = c.derivs(len(X), I, J, D, mode, fns); acc.append(out); Ns.append(len(X))
        A = np.array(acc); Ns = np.array(Ns)
        np.save(f"E2_1b_{mode}_p{p}_L{Lb}.npy", A)
        for k, fn in enumerate(['boson_m2=1', 'boson_m2=0.04']):
            msg = [f"{mode} p={p:<6} L={Lb:2d} n={nr:3d} <N>={Ns.mean():7.1f} {fn:14s}"]
            for ch, idx in c.CH.items():
                st = A[:, k, idx, 1]; sd = st.std(ddof=1); sdN = sd * np.sqrt(Ns.mean())
                msg.append(f"{ch}: mean {st.mean():+.5f}+-{st.mean(axis=1).std(ddof=1)/np.sqrt(nr):.5f} sd*sqrtN {sdN:.4f}+-{sdN/np.sqrt(2*(nr-1)):.4f}")
            print(" | ".join(msg), flush=True)
        print(f"   [{time.time()-t0:.0f}s]", flush=True)
