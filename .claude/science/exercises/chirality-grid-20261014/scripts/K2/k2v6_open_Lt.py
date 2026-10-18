"""Follow-up V6 (PREREG.md): open-time Lx = 2 kernels at Lt = 12, 16, 20 (ends receding)."""
import numpy as np, sys, time
from lat2d import Geom, rand_half, kernel, mineig
delta = 0.6; k = 8
for T in [6, 8, 10]:
    G = Geom(2, T, False, -1); rng = np.random.default_rng(9000 + T); t0 = time.time(); rows = []
    for rep in range(6):
        U = [rand_half(rng, G, 0.25, delta) for _ in range(k)]
        Ol = kernel(G, U, delta, 16, 'tri', 'O'); Oh = kernel(G, U, delta, 32, 'tri', 'O')
        Wh = kernel(G, U, delta, 32, 'tri', 'W'); Wl = kernel(G, U, delta, 16, 'tri', 'W')
        q = max(np.abs(Oh[0] - Ol[0]).max(), np.abs(Wh[0] - Wl[0]).max()); o = mineig(Oh[0]); w = mineig(Wh[0])
        fail = (o < -1e-6) and (abs(o) > 10 * q) and (w > -10 * q - 1e-10) and Oh[1] > 0.1 and q < 1e-5
        rows.append((o, w, q, Oh[1], fail))
        print(f"Lt={2*T} set {rep}: overlap min/max {o:+.3e} | Wilson {w:+.3e} | q {q:.1e} | min|H_W| {Oh[1]:.3f} | FAIL-line {fail}"); sys.stdout.flush()
    print(f"Lt={2*T} summary: FAIL-line sets {sum(r[4] for r in rows)}/6, most negative overlap {min(r[0] for r in rows):+.3e}, Wilson min {min(r[1] for r in rows):+.3e}, {time.time()-t0:.0f}s"); sys.stdout.flush()
print("done")
