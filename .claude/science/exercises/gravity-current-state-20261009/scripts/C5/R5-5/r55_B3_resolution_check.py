"""R5-5 (B3): contour-resolution check of the (B) zero counts (n = 60000 points per segment)."""
import numpy as np, sys
exec(open('r55_B_mean_law_stability.py').read().split("kap = np.logspace")[0].split('"""', 2)[2])
for name in ("4-shell {1,2,3,4}", "4-shell {1,2,4,7}", "smooth-f L=2 (all m<=96)", "smooth-f L=3 (all m<=96)"):
    g, c = kernels[name]
    w, hmin = winding(g, c, 0.0, delta=1e-4, n=60000)
    print(f"{name}: zeros in keyhole 1e-5<|z|<1e4 at n=60000: {w:+.3f} (min|h| {hmin:.2e})", flush=True)
