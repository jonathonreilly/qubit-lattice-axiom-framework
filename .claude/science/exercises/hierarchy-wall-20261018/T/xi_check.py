"""T-SPIRAL-2 artefact check (planned in the 17:00Z follow-up): xi at the 3D truncated-matching 'fixed points'.
Fit ln C(r) on 4 <= r <= r_hi where C > 0.02; compare L = 64, 96, 128."""
import numpy as np, time
from sim import nbr_table, many_runs, xi2
pts = [(0.620, 8.65), (0.839, 8.49), (0.801, 7.70), (0.853, 8.95)]
t0 = time.time()
for t, mu in pts:
    K = float(np.arctanh(t)); line = []
    for L, S, ch in ((64, 32, 8), (96, 24, 4)):
        nb = nbr_table(L, 3); N = L ** 3; Cs = []
        for c0 in range(0, S, ch):
            st, _ = many_runs(nb, N, 6, K, mu, 4242 + 97 * c0 + L, ch)
            Cs.append(xi2(st.reshape((ch, L, L, L)), 3, rmax=L // 2))
        C = np.mean(Cs, axis=0); r = np.arange(len(C))
        ok = (r >= 4) & (C > 0.02) & (r <= L // 3)
        sl = np.polyfit(r[ok], np.log(C[ok]), 1)[0] if ok.sum() >= 3 else np.nan
        xi = -1 / sl if sl < 0 else np.inf
        line.append(f"L={L}: xi={xi:.1f} C(L/4)={C[L//4]:.3f} C(L/2)={C[L//2]:.3f}")
    print(f"(t={t}, mu={mu}): " + " | ".join(line) + f"   [{time.time()-t0:.0f}s]", flush=True)
