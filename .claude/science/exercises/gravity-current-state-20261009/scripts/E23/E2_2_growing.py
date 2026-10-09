"""E2 (b) growing dilution and E3 (c) growing Poisson set: sites appear over time and never disappear.
Nested realizations: each site/point carries an arrival time; stage k uses every site that has arrived by then.
The vacuum is taken to be the instantaneous (adiabatic) ground state of the field on the PRESENT set (supplied reading:
growth slow compared with 1/m).  Quantities per stage: mean stiffness, sd*sqrt(N), and the correlation across
realizations between the stiffness of the same direction at different stages (how much of the random part persists).
  substrate 'dil' : Z^3, iid uniform activation times u_x; present at stage p iff u_x <= p   (Theorem A, docs/RECORD_
                    ACTIVATION_CRITICALITY..._2026-10-08.md: at fixed time the law is Bernoulli(p) site percolation)
  substrate 'poi' : iid uniform positions in the box, arrival order random; stage = density rho (first rho*Lb^3 points);
                    coupling range R = 1.8 FIXED in proper units (density grows -> more neighbours)
usage: python3 E2_2_growing.py dil pd|nn  |  python3 E2_2_growing.py poi pd
"""
import numpy as np, sys, time
import e23_core as c

sub, mode = sys.argv[1], sys.argv[2]
rng = np.random.default_rng({("dil", "pd"): 21, ("dil", "nn"): 22, ("poi", "pd"): 23}[(sub, mode)])
fns = [c.boson_fns(1.0)]
if sub == 'dil':
    STAGES = [0.3, 0.5, 0.7, 0.9, 1.0]; PLAN = {10: 40}
else:
    STAGES = [0.25, 0.5, 1.0, 2.0]; PLAN = {8: 40, 10: 20}

for Lb, nr in PLAN.items():
    t0 = time.time()
    res = np.zeros((nr, len(STAGES), 5)); Ns = np.zeros((nr, len(STAGES)))
    stress = np.zeros((nr, len(STAGES), 5))
    if sub == 'dil':
        g = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)
    for r in range(nr):
        if sub == 'dil':
            u = rng.random(len(g))
        else:
            P = rng.uniform(0, Lb, (int(max(STAGES) * Lb**3), 3))
        for k, s in enumerate(STAGES):
            X = g[u <= s] if sub == 'dil' else P[:int(round(s * Lb**3))]
            I, J, D = c.pairs(X, Lb, mode)
            out, _ = c.derivs(len(X), I, J, D, mode, fns)
            res[r, k] = out[0, :, 1]; stress[r, k] = out[0, :, 0]; Ns[r, k] = len(X)
    print(f"== {sub} {mode} L={Lb} n={nr} [{time.time()-t0:.0f}s]")
    for k, s in enumerate(STAGES):
        msg = [f"stage {s:<5} <N>={Ns[:, k].mean():7.1f}"]
        for ch, idx in c.CH.items():
            st = res[:, k, idx]; sd = st.std(ddof=1)
            msg.append(f"{ch}: mean {st.mean():+.5f}+-{st.mean(axis=1).std(ddof=1)/np.sqrt(nr):.5f} "
                       f"sd*sqrtN {sd*np.sqrt(Ns[:, k].mean()):.4f} stress_sd*sqrtN {stress[:, k, idx].std(ddof=1)*np.sqrt(Ns[:, k].mean()):.4f}")
        print(" | ".join(msg))
    # persistence of the random part: correlation (over realizations, pooled over directions) between stages
    dev = res - res.mean(axis=0, keepdims=True)
    C = np.zeros((len(STAGES), len(STAGES)))
    for a in range(len(STAGES)):
        for b in range(len(STAGES)):
            x, y = dev[:, a, :].ravel(), dev[:, b, :].ravel()
            C[a, b] = np.dot(x, y) / np.sqrt(np.dot(x, x) * np.dot(y, y)) if np.dot(x, x) > 0 and np.dot(y, y) > 0 else np.nan
    print("stage-stage correlation of per-realization stiffness (pooled directions):")
    for a, s in enumerate(STAGES):
        print(f"  {s:<5} " + " ".join(f"{C[a, b]:+.2f}" for b in range(len(STAGES))))
    # extensive totals: does the old random part survive? total E'' (not per site) covariance stage a vs b
    tot = res * Ns[:, :, None]
    devt = tot - tot.mean(axis=0, keepdims=True)
    print("stage-stage correlation of TOTAL stiffness E'' (extensive):")
    for a, s in enumerate(STAGES):
        row = []
        for b in range(len(STAGES)):
            x, y = devt[:, a, :].ravel(), devt[:, b, :].ravel()
            row.append(np.dot(x, y) / np.sqrt(np.dot(x, x) * np.dot(y, y)) if np.dot(x, x) > 0 and np.dot(y, y) > 0 else np.nan)
        print(f"  {s:<5} " + " ".join(f"{v:+.2f}" for v in row))
    np.savez(f"E2_2_{sub}_{mode}_L{Lb}.npz", res=res, stress=stress, Ns=Ns, stages=STAGES)
