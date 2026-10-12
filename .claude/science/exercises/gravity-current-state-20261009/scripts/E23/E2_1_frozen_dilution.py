"""E2 (a) frozen dilution: Z^3 sites present independently with probability p; field on present sites only.
Couplings: 'pd' (R3's proper-distance kernel, R = 1.8, label-blind pair choice) and 'nn' (unit Z^3 bonds among present
sites, w = 1/d_g^2). Functionals: boson m2 = 1, boson m2 = 0.04, smeared spinless fermion sea (H = L_g, mu = median of
pilot spectrum at that p, T = lambda_max/30).  Exact first/second t-derivatives per realization, per TT direction.
Mean (per present site) per channel; noise = per-direction sd * sqrt(N_present) (S(0) estimator, K1 convention).
Pre-stated reading for noise (K1's): WHITE (S(0) > 0) if sd*sqrt(N) shows no downward trend > 3 SE from smallest to
largest box and the fitted exponent of sd vs N is -0.5 within 2 SE; SUPPRESSED if exponent < -0.65.
usage: python3 E2_1_frozen_dilution.py mode  -> writes E2_1_<mode>.out and .npz
"""
import numpy as np, sys, time, os
import e23_core as c

mode = sys.argv[1]
rng = np.random.default_rng({'pd': 11, 'nn': 12}[mode])
PS = [1.0, 0.9, 0.7, 0.5, 0.3116, 0.3, 0.2, 0.1]
PLAN = {8: 100, 10: 60, 12: 30}
FN_NAMES = ['boson_m2=1', 'boson_m2=0.04', 'fermion_sea']


def lattice(Lb):
    return np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)


def fermion_params(p):
    X = lattice(8); X = X[rng.random(len(X)) < p] if p < 1 else X
    I, J, D = c.pairs(X, 8, mode)
    w = c.kernel(mode, np.einsum('pk,pk->p', D, D))[0]
    lam = np.linalg.eigvalsh(c.lap_dense(len(X), I, J, w))
    return float(np.median(lam)), float(lam.max() / 30)


raw = {}
lines = []
for p in PS:
    mu, T = fermion_params(p)
    fns = [c.boson_fns(1.0), c.boson_fns(0.04), c.fermion_fns(mu, T)]
    for Lb, nr in PLAN.items():
        if p == 1.0:
            nr = 1
        g = lattice(Lb); t0 = time.time(); acc = []; Ns = []
        for _ in range(nr):
            X = g if p == 1.0 else g[rng.random(len(g)) < p]
            I, J, D = c.pairs(X, Lb, mode)
            out, _ = c.derivs(len(X), I, J, D, mode, fns)
            acc.append(out); Ns.append(len(X))
        A = np.array(acc); Ns = np.array(Ns)        # nr x 3 x 5 x 2
        raw[f"p{p}_L{Lb}"] = A; raw[f"p{p}_L{Lb}_N"] = Ns
        for k, fn in enumerate(FN_NAMES):
            msg = [f"{mode} p={p:<6} L={Lb:2d} n={nr:3d} <N>={Ns.mean():7.1f} {fn:14s}"]
            for ch, idx in c.CH.items():
                st = A[:, k, idx, 1]; ss = A[:, k, idx, 0]
                mean = st.mean(); se = st.mean(axis=1).std(ddof=1) / np.sqrt(nr) if nr > 1 else 0.0
                sd = st.std(ddof=1) if nr > 1 else 0.0; sdN = sd * np.sqrt(Ns.mean())
                sdNse = sdN / np.sqrt(2 * max(nr - 1, 1))
                tsd = ss.std(ddof=1) * np.sqrt(Ns.mean()) if nr > 1 else 0.0
                msg.append(f"{ch}: mean {mean:+.5f}+-{se:.5f} sd*sqrtN {sdN:.4f}+-{sdNse:.4f} stress_sd*sqrtN {tsd:.4f}")
            lines.append(" | ".join(msg)); print(lines[-1], flush=True)
        print(f"   [{time.time()-t0:.0f}s]  fermion mu={mu:.3f} T={T:.3f}", flush=True)

# white-noise fits (sd vs N) per p, functional, channel
print("\nFITS sd ~ N^q (white: q = -0.5)")
for p in PS[1:]:
    for k, fn in enumerate(FN_NAMES):
        for ch, idx in c.CH.items():
            xs, ys, ws = [], [], []
            for Lb, nr in PLAN.items():
                A = raw[f"p{p}_L{Lb}"]; Ns = raw[f"p{p}_L{Lb}_N"]
                sd = A[:, k, idx, 1].std(ddof=1); se = sd / np.sqrt(2 * (nr - 1))
                xs.append(np.log(Ns.mean())); ys.append(np.log(sd)); ws.append((sd / se)**2)
            Am = np.vstack([np.ones(len(xs)), xs]).T; W = np.diag(ws)
            cov = np.linalg.inv(Am.T @ W @ Am); beta = cov @ Am.T @ W @ np.array(ys)
            print(f"{mode} p={p:<6} {fn:14s} {ch}: q = {beta[1]:+.3f} +- {np.sqrt(cov[1,1]):.3f}", flush=True)
np.savez(f"E2_1_{mode}.npz", **raw)
