"""E1: is the growth seen in E1_4 only element-wise jitter, or does the COARSE-GRAINED
propagated field grow too?  4D retarded evolution of phi=1 initial data (tau_b<3) on
diamonds; Gaussian windows (sd lam=1, truncated 2.5) centred on the axis at t=tc.
Reports, over realizations, sd of the window average of d_open = W1-1 and d_closed = phi-1,
and the element rms of each inside the window."""
import numpy as np, time, sys
from math import sqrt
from bd_core import sprinkle4d, bd4d_weights, csr_apply, evolve
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
lam = 1.0
for eps, T, nreal in [(0.2, 9.5, 24), (0.1, 9.0, 16), (0.05, 8.0, 8)]:
    tcs = [4.5, 5.5, 6.5] + ([7.0] if T >= 9.5 else [])
    rec = {tc: ([], [], [], []) for tc in tcs}
    t0 = time.time()
    for r in range(nreal):
        P = sprinkle4d(1/eps, T, rng)
        tb = np.sqrt(np.maximum(P[:, 0]**2 - (P[:, 1:]**2).sum(1), 0))
        allx = np.arange(len(P))
        ip, ix, w = bd4d_weights(P, allx, eps)
        phi = evolve(ip, ix, w, allx, np.ones(len(P)), tb < 3.0)
        dO = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
        dC = phi - 1.0
        rr = np.sqrt((P[:, 1:]**2).sum(1))
        for tc in tcs:
            dt = P[:, 0] - tc
            sel = (np.abs(dt) < 2.5*lam) & (rr < 2.5*lam) & (tb >= 3.0)
            wt = np.exp(-(dt[sel]**2 + rr[sel]**2)/(2*lam*lam))
            rec[tc][0].append((wt*dO[sel]).sum()/wt.sum())
            rec[tc][1].append((wt*dC[sel]).sum()/wt.sum())
            rec[tc][2].append(sqrt((dO[sel]**2).mean())); rec[tc][3].append(sqrt((dC[sel]**2).mean()))
    print(f"\n== eps={eps} T={T} N~{len(P)} nreal={nreal}  [{time.time()-t0:.0f}s]", flush=True)
    for tc in tcs:
        a = [np.array(x) for x in rec[tc]]
        print(f"   tc={tc}: window-avg sd: open={a[0].std(ddof=1):.4f} closed={a[1].std(ddof=1):.4f}"
              f" (ratio {a[1].std(ddof=1)/a[0].std(ddof=1):.2f}) | element rms: open={a[2].mean():.3f}"
              f" closed={a[3].mean():.3f}", flush=True)
