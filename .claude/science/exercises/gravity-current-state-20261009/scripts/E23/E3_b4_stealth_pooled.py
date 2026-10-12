"""E3 (b4): pooled stealthy (chi = 0.30) noise scaling, E3_b (first run) + E3_b3 (extension), L = 6..12."""
import numpy as np
import e23_core as c
for k, fn in enumerate(['m2=1', 'm2=0.04']):
    for col, q in [(1, 'stiffness'), (0, 'stress')]:
        for ch, idx in c.CH.items():
            xs, ys, ws, txt = [], [], [], []
            for Lb in [6, 8, 10, 12]:
                parts = [np.load(f"E3_b3_stealth_L{Lb}.npy")]
                try: parts.append(np.load(f"E3_b_stealth_0.3_L{Lb}.npy"))
                except FileNotFoundError: pass
                A = np.concatenate(parts); st = A[:, k, idx, col]; nr = len(A); N = Lb**3
                sd = st.std(ddof=1); se = sd / np.sqrt(2 * (nr - 1))
                xs.append(np.log(N)); ys.append(np.log(sd)); ws.append((sd / se)**2)
                txt.append(f"L{Lb}(n={nr}): mean {st.mean():+.5f} sd*sqrtN {sd*np.sqrt(N):.4f}+-{se*np.sqrt(N):.4f}")
            Am = np.vstack([np.ones(4), xs]).T; W = np.diag(ws); cov = np.linalg.inv(Am.T @ W @ Am); b = cov @ Am.T @ W @ np.array(ys)
            print(f"{fn:8s} {q:9s} {ch:5s} | " + " | ".join(txt) + f" | q = {b[1]:+.3f} +- {np.sqrt(cov[1,1]):.3f}")
