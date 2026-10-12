"""E2 (3): pooled white-noise fits, boxes L = 8..24 (E2_1 + E2_1b), bosons m2 = 1, 0.04, p = 0.1, 0.3116, 0.5.
sd of the per-site stiffness per direction vs <N_present>: sd ~ N^q, white q = -0.5 (K1 reading: white if within 2 SE)."""
import numpy as np, glob
import e23_core as c
for mode in ['pd', 'nn']:
    z = np.load(f"E2_1_{mode}.npz")
    for p in [0.1, 0.3116, 0.5]:
        data = []
        for Lb in [8, 10, 12]:
            data.append((z[f"p{p}_L{Lb}_N"].mean(), z[f"p{p}_L{Lb}"][:, :2]))   # first two functionals = bosons
        for f in sorted(glob.glob(f"E2_1b_{mode}_p{p}_L*.npy")):
            A = np.load(f); Lb = int(f.split('_L')[1].split('.')[0]); data.append((p * Lb**3, A))
        for k, fn in enumerate(['m2=1', 'm2=0.04']):
            for ch, idx in c.CH.items():
                xs, ys, ws, sdN = [], [], [], []
                for N, A in data:
                    st = A[:, k, idx, 1]; nr = len(st); sd = st.std(ddof=1); se = sd / np.sqrt(2 * (nr - 1))
                    xs.append(np.log(N)); ys.append(np.log(sd)); ws.append((sd / se)**2); sdN.append(sd * np.sqrt(N))
                Am = np.vstack([np.ones(len(xs)), xs]).T; W = np.diag(ws)
                cov = np.linalg.inv(Am.T @ W @ Am); beta = cov @ Am.T @ W @ np.array(ys)
                print(f"{mode} p={p:<6} {fn:8s} {ch:5s}: N {np.exp(min(xs)):.0f}..{np.exp(max(xs)):.0f}  sd*sqrtN = "
                      + " ".join(f"{v:.4f}" for v in sdN) + f"  q = {beta[1]:+.3f} +- {np.sqrt(cov[1,1]):.3f}")
